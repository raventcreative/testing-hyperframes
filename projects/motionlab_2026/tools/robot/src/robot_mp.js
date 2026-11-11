// MasterPajak AI trial robot — real-time runtime (three.js), deterministic: every frame is a pure function of the state passed in.
// The Tripo mesh arrives with its fused arms already cut away (cut_arms.py). This runtime adds:
//   * a 3-bone skin (body / head / antenna) computed on load from the bind pose (smooth neck + antenna-base blends)
//   * procedural "rubber-hose" arms: tube along a quadratic bezier shoulder -> elbow -> wrist, rebuilt every frame with
//     parallel-transport frames (no twisting, no seams), ball shoulder cap + white ball hand — same radius and colours as the
//     original pill arms, so the rest pose is identical but any pose (wave / point / push) bends smoothly, never tears
//   * a procedural face on the visor screen (shader SDFs in bind-pose space): oval eyes with blink / look, happy "^ ^" arcs,
//     "x x" eyes, smile / flat / "o" mouth, soft emissive glow — crisp at any size
//   * soft ground shadow, studio lighting (room env + key + cool rim)
// API: const r = await RobotMP.create(canvas, { url, width, height }); r.render(state)
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { RoomEnvironment } from "three/examples/jsm/environments/RoomEnvironment.js";

const D2R = Math.PI / 180;
const NECK = new THREE.Vector3(0, 0.445, 0.0), ANT = new THREE.Vector3(0, 0.848, 0.034);
const ARM = { r: 0.047, shoulder: new THREE.Vector3(0.267, 0.358, 0.033), len: 0.206, hand: 0.046 };
const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

const FACE_GLSL = /* glsl */ `
uniform float uBlink, uLookX, uLookY, uHappy, uX, uSmile, uMouthO, uGlow, uScan;
varying vec3 vRest; varying vec3 vRestN;
float sdRoundBox(vec2 p, vec2 b, float r) { vec2 q = abs(p) - b + r; return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r; }
float sdEllipse(vec2 p, vec2 r) { float k0 = length(p / r); float k1 = length(p / (r * r)); return k0 * (k0 - 1.0) / max(k1, 1e-5); }
float sdSeg(vec2 p, vec2 a, vec2 b) { vec2 pa = p - a, ba = b - a; float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0); return length(pa - ba * h); }
// arc of a circle centred c, radius r, spanning angles around direction "up" (+1) or "down" (-1), half-angle ha
float sdArc(vec2 p, vec2 c, float r, float ha, float dirY) {
  vec2 q = p - c; q.y *= dirY; float ang = atan(q.x, q.y);
  if (abs(ang) <= ha) return abs(length(q) - r);
  vec2 e = vec2(sin(ha) * sign(q.x), cos(ha)) * r; return length(vec2(abs(q.x), q.y) - vec2(abs(e.x), e.y));
}
float faceScreen() {   // 1 on the visor screen (front of the head, bind pose)
  float d = sdRoundBox(vRest.xy - vec2(0.0, 0.6425), vec2(0.201, 0.117), 0.082);
  float aa = fwidth(d) * 1.2;
  return smoothstep(aa, -aa, d) * smoothstep(0.10, 0.13, vRest.z) * smoothstep(0.15, 0.4, vRestN.z);
}
vec3 faceGlow(out float ink) {   // emissive features; ink = coverage of the yellow strokes
  vec2 p = vRest.xy; vec2 look = vec2(uLookX, uLookY) * vec2(0.026, 0.018);
  float d = 1e3;
  for (int i = 0; i < 2; i++) {
    float s = i == 0 ? 1.0 : -1.0; vec2 c = vec2(0.083 * s, 0.646) + look;
    // oval eye (blink squashes it to a line), happy arc, cross
    float open = max(0.06, 1.0 - uBlink);
    float eo = sdEllipse(p - c, vec2(0.029, 0.043 * open));
    float eh = sdArc(p, c + vec2(0.0, -0.012), 0.030, 1.05, 1.0) - 0.0085;
    float ex = min(sdSeg(p - c, vec2(-0.026, -0.026), vec2(0.026, 0.026)), sdSeg(p - c, vec2(-0.026, 0.026), vec2(0.026, -0.026))) - 0.0085;
    float e = mix(mix(eo, eh, uHappy), ex, uX);
    d = min(d, e);
  }
  // mouth: smile arc (uSmile 1) -> flat (0); "o" mouth blends in with uMouthO
  vec2 mc = vec2(0.0, 0.592) + look * 0.5;
  float sm = clamp(uSmile, 0.0, 1.0);
  float ms = sdArc(p, mc + vec2(0.0, 0.03 * sm + 0.002), 0.03 + 0.012 * (1.0 - sm), mix(0.25, 0.85, sm), -1.0) - 0.0068;
  float mf = sdSeg(p, mc + vec2(-0.024, 0.004), mc + vec2(0.024, 0.004)) - 0.0068;
  float mo = abs(sdEllipse(p - mc - vec2(0.0, 0.004), vec2(0.016, 0.019))) - 0.0062;
  float m = mix(mix(mf, ms, step(0.05, uSmile)), mo, uMouthO);
  d = min(d, m);
  float aa = fwidth(d) * 1.1;
  ink = smoothstep(aa, -aa, d);
  float halo = exp(-max(d, 0.0) / 0.012) * 0.35 * uGlow;
  return vec3(1.0, 0.82, 0.07) * (ink * 1.25 + halo);
}
`;

function makeFaceMaterial(base, U) {
  base.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.vertexShader = sh.vertexShader
      .replace("#include <common>", "#include <common>\nvarying vec3 vRest; varying vec3 vRestN;")
      .replace("#include <begin_vertex>", "#include <begin_vertex>\nvRest = position; vRestN = normal;");
    sh.fragmentShader = sh.fragmentShader
      .replace("#include <common>", "#include <common>\n" + FACE_GLSL)
      .replace("#include <map_fragment>", `#include <map_fragment>
        float fScr = faceScreen(); float fInk = 0.0; vec3 fEm = vec3(0.0);
        if (fScr > 0.001) { fEm = faceGlow(fInk);
          vec3 scr = vec3(0.016, 0.022, 0.052) + vec3(0.0, 0.004, 0.012) * (0.5 + 0.5 * sin(vRest.y * 900.0)) * uScan;
          diffuseColor.rgb = mix(diffuseColor.rgb, mix(scr, vec3(1.0, 0.82, 0.07) * 0.35, fInk), fScr); }`)
      .replace("#include <roughnessmap_fragment>", "#include <roughnessmap_fragment>\nroughnessFactor = mix(roughnessFactor, 0.16, fScr);")
      .replace("#include <emissivemap_fragment>", "#include <emissivemap_fragment>\ntotalEmissiveRadiance += fEm * fScr;");
  };
  base.customProgramCacheKey = () => "mp-face";
  return base;
}

// ---- rubber-hose arm: tube along a quadratic bezier, rebuilt in place every frame ----
class HoseArm {
  constructor(mat, handMat, side) {
    this.side = side; this.group = new THREE.Group();
    this.N = 30; this.M = 20;
    const g = new THREE.BufferGeometry(), nv = (this.N + 1) * (this.M + 1);
    g.setAttribute("position", new THREE.BufferAttribute(new Float32Array(nv * 3), 3));
    g.setAttribute("normal", new THREE.BufferAttribute(new Float32Array(nv * 3), 3));
    const idx = [];
    for (let i = 0; i < this.N; i++) for (let j = 0; j < this.M; j++) {
      const a = i * (this.M + 1) + j, b = a + this.M + 1; idx.push(a, b, a + 1, b, b + 1, a + 1);
    }
    g.setIndex(idx); this.geo = g;
    this.tube = new THREE.Mesh(g, mat); this.tube.frustumCulled = false;
    const sg = new THREE.SphereGeometry(ARM.r, 32, 20);
    this.capS = new THREE.Mesh(sg, mat); this.capW = new THREE.Mesh(sg, mat);
    this.hand = new THREE.Mesh(new THREE.SphereGeometry(ARM.hand, 40, 28), handMat);
    this.group.add(this.tube, this.capS, this.capW, this.hand);
    this._v = [new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3()];
  }
  // pose: raise (abduction, deg), fwd (flexion, deg), bend (elbow, deg), bendYaw (plane of the bend, deg: 0 fwd, 90 outward)
  pose(p) {
    const s = this.side, S = ARM.shoulder.clone(); S.x *= s;
    const q = new THREE.Quaternion().setFromEuler(new THREE.Euler(-(p.fwd || 0) * D2R, 0, s * (p.raise || 0) * D2R, "ZYX"));
    const d1 = new THREE.Vector3(0, -1, 0).applyQuaternion(q), fw = new THREE.Vector3(0, 0, 1).applyQuaternion(q);
    // bend plane: forward vector rotated about the upper-arm axis by bendYaw (mirrored per side)
    const bdir = fw.clone().applyAxisAngle(d1, s * (p.bendYaw || 0) * D2R);
    const axis = new THREE.Vector3().crossVectors(d1, bdir).normalize();
    const d2 = d1.clone().applyAxisAngle(axis, -(p.bend || 0) * D2R);
    const L = ARM.len * 0.5, E = S.clone().addScaledVector(d1, L), H = E.clone().addScaledVector(d2, L);
    const C = E.clone().multiplyScalar(2).sub(S.clone().add(H).multiplyScalar(0.5));   // control point: curve passes through E
    const curve = new THREE.QuadraticBezierCurve3(S, C, H);
    const pos = this.geo.attributes.position.array, nor = this.geo.attributes.normal.array;
    let T = curve.getTangent(0).normalize(), Nn = new THREE.Vector3(1, 0, 0);
    if (Math.abs(T.dot(Nn)) > 0.9) Nn.set(0, 0, 1);
    Nn.sub(T.clone().multiplyScalar(T.dot(Nn))).normalize();
    for (let i = 0; i <= this.N; i++) {
      const t = i / this.N, P = curve.getPoint(t), Ti = curve.getTangent(t).normalize();
      // parallel transport of the normal
      const ax = new THREE.Vector3().crossVectors(T, Ti), sn = ax.length();
      if (sn > 1e-6) Nn.applyAxisAngle(ax.normalize(), Math.asin(Math.min(1, sn)));
      T = Ti; const B = new THREE.Vector3().crossVectors(T, Nn).normalize();
      for (let j = 0; j <= this.M; j++) {
        const a = (j / this.M) * Math.PI * 2, cx = Math.cos(a), cy = Math.sin(a);
        const nx = Nn.x * cx + B.x * cy, ny = Nn.y * cx + B.y * cy, nz = Nn.z * cx + B.z * cy, k = (i * (this.M + 1) + j) * 3;
        pos[k] = P.x + nx * ARM.r; pos[k + 1] = P.y + ny * ARM.r; pos[k + 2] = P.z + nz * ARM.r;
        nor[k] = nx; nor[k + 1] = ny; nor[k + 2] = nz;
      }
    }
    this.geo.attributes.position.needsUpdate = true; this.geo.attributes.normal.needsUpdate = true;
    this.geo.computeBoundingSphere();
    this.capS.position.copy(S); this.capW.position.copy(H);
    const dEnd = curve.getTangent(1).normalize();
    this.hand.position.copy(H).addScaledVector(dEnd, ARM.hand * 0.86).addScaledVector(fw, 0.012);
    const hs = p.hand || 1; this.hand.scale.setScalar(hs);
  }
}

function shadowTexture() {
  const c = document.createElement("canvas"); c.width = c.height = 256; const g = c.getContext("2d");
  const r = g.createRadialGradient(128, 128, 0, 128, 128, 128);
  r.addColorStop(0, "rgba(0,0,0,0.55)"); r.addColorStop(0.45, "rgba(0,0,0,0.28)"); r.addColorStop(1, "rgba(0,0,0,0)");
  g.fillStyle = r; g.fillRect(0, 0, 256, 256); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}

export async function create(canvas, opts = {}) {
  const W = opts.width || 1080, H = opts.height || 1920;
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, preserveDrawingBuffer: true, powerPreference: "high-performance" });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false); renderer.setClearColor(0x000000, 0);
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = opts.exposure || 1.0; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene();
  const pm = new THREE.PMREMGenerator(renderer); scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = opts.envIntensity || 0.75;
  const key = new THREE.DirectionalLight(0xfff4e6, 1.55); key.position.set(-1.2, 2.2, 2.4); scene.add(key);
  const rim = new THREE.DirectionalLight(0xbcd2ff, 1.35); rim.position.set(1.8, 1.2, -1.6); scene.add(rim);
  const fill = new THREE.HemisphereLight(0xeef2ff, 0x2a3466, 0.35); scene.add(fill);
  // camera: fixed; px -> world scale so the robot can be placed in screen pixels
  const FOV = 22, DIST = 6, cam = new THREE.PerspectiveCamera(FOV, W / H, 0.1, 50); cam.position.set(0, 0, DIST); cam.lookAt(0, 0, 0);
  const worldH = 2 * DIST * Math.tan((FOV / 2) * D2R), k = worldH / H;

  const gltf = await new GLTFLoader().loadAsync(opts.url);
  let src = null; gltf.scene.traverse((o) => { if (o.isMesh && !src) src = o; });
  const geo = src.geometry; const P = geo.attributes.position;
  // 3-bone skin
  const si = new Uint16Array(P.count * 4), sw = new Float32Array(P.count * 4);
  for (let v = 0; v < P.count; v++) {
    const x = P.getX(v), y = P.getY(v), z = P.getZ(v);
    const wh = smooth(0.43, 0.468, y), wa = smooth(0.842, 0.862, y) * (Math.hypot(x, z - 0.034) < 0.06 ? 1 : 0);
    si[v * 4] = 0; si[v * 4 + 1] = 1; si[v * 4 + 2] = 2; sw[v * 4] = 1 - wh; sw[v * 4 + 1] = wh * (1 - wa); sw[v * 4 + 2] = wh * wa;
  }
  geo.setAttribute("skinIndex", new THREE.BufferAttribute(si, 4)); geo.setAttribute("skinWeight", new THREE.BufferAttribute(sw, 4));
  const bRoot = new THREE.Bone(), bHead = new THREE.Bone(), bAnt = new THREE.Bone();
  bHead.position.copy(NECK); bAnt.position.copy(ANT).sub(NECK); bRoot.add(bHead); bHead.add(bAnt);
  const U = { uBlink: { value: 0 }, uLookX: { value: 0 }, uLookY: { value: 0 }, uHappy: { value: 0 }, uX: { value: 0 }, uSmile: { value: 1 }, uMouthO: { value: 0 }, uGlow: { value: 1 }, uScan: { value: 1 } };
  const mat = makeFaceMaterial(src.material.clone(), U); mat.envMapIntensity = 1.0;
  const body = new THREE.SkinnedMesh(geo, mat); body.frustumCulled = false;
  body.add(bRoot); body.bind(new THREE.Skeleton([bRoot, bHead, bAnt]));
  const armMat = new THREE.MeshStandardMaterial({ color: new THREE.Color().setStyle(opts.armColor || "#2d3c6b"), roughness: 0.66, metalness: 0.0 });
  const handMat = new THREE.MeshStandardMaterial({ color: new THREE.Color().setStyle(opts.handColor || "#d6d7e0"), roughness: 0.7, metalness: 0.0 });
  const armL = new HoseArm(armMat, handMat, 1), armR = new HoseArm(armMat, handMat, -1);
  const rig = new THREE.Group(); rig.add(body, armL.group, armR.group);
  const pivot = new THREE.Group(); pivot.add(rig); rig.position.y = -0.45;   // rotate the body about its centre
  const root = new THREE.Group(); root.add(pivot); scene.add(root);
  const shadow = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ map: shadowTexture(), transparent: true, depthWrite: false, toneMapped: false }));
  shadow.rotation.x = -Math.PI / 2; scene.add(shadow);

  function render(s) {
    const vis = s.visible !== false && (s.opacity == null || s.opacity > 0.001);
    root.visible = vis; shadow.visible = vis && (s.shadow == null || s.shadow > 0.001);
    if (vis) {
      const sc = (s.h * k) / 0.977;   // s.h = on-screen height in px (antenna tip to body bottom)
      root.position.set((s.x - W / 2) * k, (H / 2 - s.y) * k, s.z || 0); root.scale.setScalar(sc);
      pivot.rotation.set((s.pitch || 0) * D2R, (s.yaw || 0) * D2R, -(s.roll || 0) * D2R, "YXZ");
      pivot.scale.set(1 + (s.squash || 0) * -0.5, 1 + (s.squash || 0), 1 + (s.squash || 0) * -0.5);
      bHead.rotation.set((s.headPitch || 0) * D2R, (s.headYaw || 0) * D2R, -(s.headRoll || 0) * D2R, "YXZ");
      bAnt.rotation.set((s.antX || 0) * D2R, 0, -(s.antZ || 0) * D2R);
      armL.pose(s.aL || {}); armR.pose(s.aR || {});
      const f = s.face || {};
      U.uBlink.value = f.blink || 0; U.uLookX.value = f.lookX || 0; U.uLookY.value = f.lookY || 0; U.uHappy.value = f.happy || 0;
      U.uX.value = f.x || 0; U.uSmile.value = f.smile == null ? 1 : f.smile; U.uMouthO.value = f.o || 0; U.uGlow.value = f.glow == null ? 1 : f.glow;
      // ground shadow under the body bottom (s.ground = screen y of the floor; default 60 px below the body)
      const bottomY = s.y + s.h * 0.5, gy = s.ground == null ? bottomY + s.h * 0.06 : s.ground;
      shadow.position.set((s.x - W / 2) * k, (H / 2 - gy) * k, -0.2);
      const lift = Math.max(0, gy - bottomY) / s.h;
      shadow.scale.set(s.h * k * 0.62 * (1 - lift * 0.5), s.h * k * 0.62 * 0.28 * (1 - lift * 0.5), 1);
      shadow.rotation.x = 0; shadow.material.opacity = (s.shadow == null ? 0.45 : s.shadow) * Math.max(0.2, 1 - lift * 1.4);
      renderer.domElement.style.opacity = s.opacity == null ? "1" : String(s.opacity);
      rim.intensity = 1.35 * (s.rim == null ? 1 : s.rim); key.intensity = 1.55 * (s.key == null ? 1 : s.key);
    }
    renderer.render(scene, cam);
  }
  return { render, renderer, scene, camera: cam, k };
}
if (typeof window !== "undefined") window.RobotMP = { create };
