/* AIpreneur 3D presenter robot (client GLB, decimated) for HyperFrames.
   - skinned at load: body (root) + two arm bones with smooth weights (arm = its own mesh island in the side box,
     inside a capsule shoulder->hand), so arms can wave / point / beat in real 3D
   - visor face is procedural (shader): the baked eyes/mouth are painted over, then glowing eyes and mouth are drawn on
     the visor surface: blink, expressions (happy, x, wide, excited, flat) and a mouth that opens with the VO loudness
   - deterministic: render(t) reads only window.R3D.state (tweened by the GSAP timeline) and t (blinks, idle, VO_ENV)
   Page needs: <canvas id="robo3d">, importmap for "three" + "three/addons/", vendor/robot3d_state.js loaded first. */
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const R3D = window.R3D;
const base = R3D.base || "vendor/robot3d/";
const cv = document.getElementById("robo3d");
const W = cv.width, H = cv.height;
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, alpha: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H, false); renderer.setClearColor(0x000000, 0);
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.85;
const key = new THREE.DirectionalLight(0xfff3e6, 1.15); key.position.set(1.2, 2.2, 3); scene.add(key);
const rim = new THREE.DirectionalLight(0xbfd8ff, 0.9); rim.position.set(-2.5, 1.5, -1.5); scene.add(rim);
// framing: PX px per model unit, head top 40 px below the canvas top (close-ups zoom in 3D, never by CSS scaling)
const PX = R3D.pxPerUnit || 628, visH = H / PX, fov = 22, dist = visH / (2 * Math.tan((fov * Math.PI) / 360));
const camY = 0.978 - (H / 2 - 40) / PX;
const cam = new THREE.PerspectiveCamera(fov, W / H, 0.05, 20); cam.position.set(0, camY, dist); cam.lookAt(0, camY, 0);

const SL = new THREE.Vector3(-0.178, 0.315, 0.04), HL = new THREE.Vector3(-0.32, 0.345, 0.2);
const SR = new THREE.Vector3(0.178, 0.315, 0.04), HR = new THREE.Vector3(0.32, 0.24, 0.19);
const U = {
  uBlink: { value: 0 }, uW: { value: new THREE.Vector4() }, uFlat: { value: 0 }, uMouth: { value: 0 }, uLook: { value: new THREE.Vector2() },
  uVisor: { value: new THREE.Color(0.012, 0.014, 0.024) }, uLogo: { value: null },
  uLogoBox: { value: new THREE.Vector4(-0.155, 0.2305, 0.30, 0.0272) }, // x0, y0, w, h in model units (front of the belly, under the light bar)
};
let root, armL, armR, group, ready = false;

const sstep = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
function skin(geo) {
  const P = geo.attributes.position, n = P.count, ia = geo.index.array;
  // weld by position so UV seams do not split islands
  const map = new Map(), rep = new Int32Array(n);
  for (let i = 0; i < n; i++) { const k = Math.round(P.getX(i) * 2e4) + "," + Math.round(P.getY(i) * 2e4) + "," + Math.round(P.getZ(i) * 2e4);
    let r = map.get(k); if (r === undefined) { r = i; map.set(k, i); } rep[i] = r; }
  // islands inside each side box: the arm is the big island below the helmet rim
  const island = (box) => { const inB = (i) => { const x = P.getX(i), y = P.getY(i); return x > box[0] && x < box[1] && y > box[2] && y < box[3]; };
    const par = new Int32Array(n); for (let i = 0; i < n; i++) par[i] = i;
    const f = (a) => { while (par[a] !== a) { par[a] = par[par[a]]; a = par[a]; } return a; };
    const u = (a, b) => { a = f(a); b = f(b); if (a !== b) par[a] = b; };
    for (let i = 0; i < n; i++) if (inB(i)) u(i, rep[i]);
    for (let t = 0; t < ia.length; t += 3) { const a = ia[t], b = ia[t + 1], c = ia[t + 2]; if (inB(a) && inB(b) && inB(c)) { u(a, b); u(a, c); } }
    const stat = new Map(); for (let i = 0; i < n; i++) if (inB(i)) { const r = f(i); const s = stat.get(r) || { c: 0, y: 0 }; s.c++; s.y += P.getY(i); stat.set(r, s); }
    let best = -1, bc = 0; stat.forEach((s, r) => { if (s.y / s.c < 0.38 && s.c > bc) { bc = s.c; best = r; } });
    const m = new Uint8Array(n); for (let i = 0; i < n; i++) if (inB(i) && f(i) === best) m[i] = 1; return m; };
  const mL = island([-0.6, -0.15, 0.14, 0.47]), mR = island([0.15, 0.6, 0.08, 0.47]);
  const torso = (p) => Math.pow(Math.pow(Math.abs(p.x / 0.212), 3) + Math.pow(Math.abs((p.y - 0.21) / 0.18), 3) + Math.pow(Math.abs((p.z - 0.05) / 0.175), 3), 1 / 3);
  // hand centre = mean of the island's outermost points; arm = island AND outside the torso AND near the shoulder->hand axis
  const handC = (m, sgn) => { const c = new THREE.Vector3(); let k = 0; for (let i = 0; i < n; i++) if (m[i] && P.getX(i) * sgn > 0.27) { c.x += P.getX(i); c.y += P.getY(i); c.z += P.getZ(i); k++; } return c.multiplyScalar(1 / Math.max(1, k)); };
  HL.copy(handC(mL, -1)); HR.copy(handC(mR, 1)); R3D.hands = [HL.toArray(), HR.toArray()];
  const axisD = (p, S, Hd) => { const d = Hd.clone().sub(S), t = Math.min(1.25, Math.max(0, p.clone().sub(S).dot(d) / d.lengthSq())); return p.distanceTo(S.clone().add(d.multiplyScalar(t))); };
  const capW = (p, S, Hd, inI) => (inI ? sstep(0.97, 1.07, torso(p)) * sstep(0.135, 0.105, axisD(p, S, Hd)) : 0);
  const si = new Uint16Array(n * 4), sw = new Float32Array(n * 4), p = new THREE.Vector3();
  for (let i = 0; i < n; i++) { p.set(P.getX(i), P.getY(i), P.getZ(i));
    const wl = capW(p, SL, HL, mL[i]), wr = capW(p, SR, HR, mR[i]);
    si[i * 4] = 0; si[i * 4 + 1] = 1; si[i * 4 + 2] = 2; sw[i * 4] = Math.max(0, 1 - wl - wr); sw[i * 4 + 1] = wl; sw[i * 4 + 2] = wr; }
  // drop "bridge" triangles where a hand is fused to the belly (big weight jump far from the shoulder) -> no stretched sheets
  const keep = []; let dropped = 0; const c = new THREE.Vector3();
  for (let t = 0; t < ia.length; t += 3) { const v = [ia[t], ia[t + 1], ia[t + 2]]; let bad = false;
    for (const [k, S] of [[1, SL], [2, SR]]) { const w = v.map((i) => sw[i * 4 + k]); if (Math.max(...w) - Math.min(...w) > 0.45) {
      c.set(0, 0, 0); v.forEach((i) => c.add(p.set(P.getX(i), P.getY(i), P.getZ(i)))); c.multiplyScalar(1 / 3); if (c.distanceTo(S) > 0.075) bad = true; } }
    if (bad) dropped++; else keep.push(v[0], v[1], v[2]); }
  geo.setIndex(keep); R3D.dropped = dropped;
  { const N = new Float32Array(n * 3), A = keep, a = new THREE.Vector3(), b = new THREE.Vector3(), q = new THREE.Vector3(), r = new THREE.Vector3();
    for (let t = 0; t < A.length; t += 3) { const i0 = rep[A[t]], i1 = rep[A[t + 1]], i2 = rep[A[t + 2]];
      a.set(P.getX(i0), P.getY(i0), P.getZ(i0)); b.set(P.getX(i1), P.getY(i1), P.getZ(i1)); q.set(P.getX(i2), P.getY(i2), P.getZ(i2));
      r.subVectors(b, a).cross(q.clone().sub(a)); for (const i of [i0, i1, i2]) { N[i * 3] += r.x; N[i * 3 + 1] += r.y; N[i * 3 + 2] += r.z; } }
    const norm = (B) => { for (let i = 0; i < n; i++) if (rep[i] === i) { const l = Math.hypot(B[i * 3], B[i * 3 + 1], B[i * 3 + 2]) || 1; B[i * 3] /= l; B[i * 3 + 1] /= l; B[i * 3 + 2] /= l; } };
    norm(N);
    const visor = (i) => { const x = P.getX(i), y = P.getY(i), z = P.getZ(i); return z > 0.1 && Math.abs(x) < 0.3 && y > 0.43 && y < 0.9; };
    for (let it = 0; it < 14; it++) { const M = new Float32Array(N);
      for (let t = 0; t < A.length; t += 3) { const v = [rep[A[t]], rep[A[t + 1]], rep[A[t + 2]]];
        if (it >= 4 && !visor(v[0])) continue;
        for (const i of v) for (const j of v) if (i !== j) { M[i * 3] += N[j * 3]; M[i * 3 + 1] += N[j * 3 + 1]; M[i * 3 + 2] += N[j * 3 + 2]; } }
      norm(M); N.set(M); }
    const NA = geo.attributes.normal; for (let i = 0; i < n; i++) { const k = rep[i]; NA.setXYZ(i, N[k * 3], N[k * 3 + 1], N[k * 3 + 2]); } NA.needsUpdate = true; }
  geo.setAttribute("skinIndex", new THREE.Uint16BufferAttribute(si, 4)); geo.setAttribute("skinWeight", new THREE.Float32BufferAttribute(sw, 4));
  if (R3D.debugWeights) { const c = new Float32Array(n * 3); for (let i = 0; i < n; i++) { c[i * 3] = 1 - sw[i * 4 + 2] * 0.8; c[i * 3 + 1] = 1 - sw[i * 4 + 1] * 0.8 - sw[i * 4 + 2] * 0.1; c[i * 3 + 2] = 1 - sw[i * 4 + 1] * 0.8 - sw[i * 4 + 2] * 0.8; }
    geo.setAttribute("color", new THREE.Float32BufferAttribute(c, 3)); }
}

function faceShader(mat) {
  mat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.vertexShader = sh.vertexShader.replace("#include <common>", "#include <common>\nvarying vec3 vBP;")
      .replace("#include <begin_vertex>", "#include <begin_vertex>\nvBP = position; vArm = skinWeight.y + skinWeight.z; vVN = normalMatrix * normalize(vec3(position.x / 0.40, (position.y - 0.66) / 0.29, 1.0));")
      .replace("varying vec3 vBP;", "varying vec3 vBP; varying float vArm; varying vec3 vVN;");
    sh.fragmentShader = sh.fragmentShader.replace("#include <common>", `#include <common>
varying vec3 vBP; varying float vArm; varying vec3 vVN; uniform sampler2D uLogo; uniform vec4 uLogoBox; uniform float uBlink; uniform vec4 uW; uniform float uFlat; uniform float uMouth; uniform vec2 uLook; uniform vec3 uVisor;
float visorMaskBig(vec2 p){ vec2 q = abs((p - vec2(0.0, 0.662)) / vec2(0.29, 0.226)); float s = pow(pow(q.x,4.0)+pow(q.y,4.0), 0.25); return 1.0 - smoothstep(0.9, 1.0, s); }
float visorMask(vec2 p){ vec2 q = abs((p - vec2(0.0, 0.66)) / vec2(0.262, 0.198)); float s = pow(pow(q.x,4.0)+pow(q.y,4.0), 0.25); return 1.0 - smoothstep(0.86, 0.99, s); }
float seg(vec2 p, vec2 a, vec2 b){ vec2 pa = p - a, ba = b - a; float h = clamp(dot(pa,ba)/dot(ba,ba), 0.0, 1.0); return length(pa - ba*h); }
float ell(vec2 p, vec2 r){ return (length(p / r) - 1.0) * min(r.x, r.y); }
float rbox(vec2 p, vec2 b, float r){ vec2 q = abs(p) - b + r; return length(max(q,0.0)) + min(max(q.x,q.y),0.0) - r; }
float eyeD(vec2 p, float side){
  float wn = clamp(1.0 - uW.x - uW.y - uW.z - uW.w - uFlat, 0.0, 1.0);
  vec2 r = vec2(0.05, 0.062) * mix(1.0, 1.2, uW.z);
  float dn = ell(p, vec2(r.x, max(0.004, r.y * (1.0 - 0.94 * uBlink))));
  float dh = length(p - vec2(0.0, -0.022)) - 0.046; dh = (p.y > -0.022) ? abs(dh) - 0.011 : length(vec2(abs(p.x) - 0.046, p.y + 0.022)) - 0.011;
  float dx = min(seg(p, vec2(-0.036, 0.04), vec2(0.036, -0.04)), seg(p, vec2(-0.036, -0.04), vec2(0.036, 0.04))) - 0.011;
  float dg = min(seg(p, vec2(-0.034 * side, 0.036), vec2(0.03 * side, 0.0)), seg(p, vec2(0.03 * side, 0.0), vec2(-0.034 * side, -0.036))) - 0.011;
  float df = seg(p, vec2(-0.045, 0.0), vec2(0.045, 0.0)) - 0.01;
  // soft union weighted by expression weights: each shape fades and grows in with its weight
  float d = 1.0;
  d = min(d, mix(0.05, dn, smoothstep(0.0, 1.0, max(wn, uW.z))));
  d = min(d, mix(0.05, dh / mix(0.6, 1.0, uW.x), smoothstep(0.0, 1.0, uW.x)));
  d = min(d, mix(0.05, dx / mix(0.6, 1.0, uW.y), smoothstep(0.0, 1.0, uW.y)));
  d = min(d, mix(0.05, dg / mix(0.6, 1.0, uW.w), smoothstep(0.0, 1.0, uW.w)));
  d = min(d, mix(0.05, df / mix(0.6, 1.0, uFlat), smoothstep(0.0, 1.0, uFlat)));
  return d; }
`).replace("#include <map_fragment>", `#include <map_fragment>
float lum0 = dot(diffuseColor.rgb, vec3(0.299, 0.587, 0.114));
float vm = max((vBP.z > 0.1) ? visorMask(vBP.xy) : 0.0, ((vBP.z > 0.05) ? visorMaskBig(vBP.xy) : 0.0) * (1.0 - smoothstep(0.32, 0.55, lum0)));
diffuseColor.rgb = mix(diffuseColor.rgb, uVisor, vm);
vec2 luv = (vBP.xy - uLogoBox.xy) / uLogoBox.zw;
if (vBP.z > 0.05 && vArm < 0.5 && luv.x > 0.0 && luv.x < 1.0 && luv.y > 0.0 && luv.y < 1.0) { vec4 lc = texture2D(uLogo, luv); diffuseColor.rgb = mix(diffuseColor.rgb, lc.rgb, lc.a * 0.96); }`)
      .replace("#include <roughnessmap_fragment>", "#include <roughnessmap_fragment>\nroughnessFactor = mix(roughnessFactor, 0.22, vm);")
      .replace("#include <normal_fragment_maps>", "#include <normal_fragment_maps>\nnormal = normalize(mix(normal, normalize(vVN), vm));")
      .replace("#include <lights_fragment_maps>", "#include <lights_fragment_maps>\n#if defined( RE_IndirectSpecular )\nradiance *= mix(1.0, 0.28, vm);\n#endif")
      .replace("#include <metalnessmap_fragment>", "#include <metalnessmap_fragment>\nmetalnessFactor = mix(metalnessFactor, 0.0, vm);")
      .replace("#include <emissivemap_fragment>", `#include <emissivemap_fragment>
if (vm > 0.0) { vec2 p = vBP.xy + uLook;
  float dL = eyeD(p - vec2(-0.131, 0.6725), 1.0), dR = eyeD(p - vec2(0.129, 0.6725), -1.0), de = min(dL, dR);
  float aa = max(fwidth(de), 0.0008); float eye = 1.0 - smoothstep(-aa, aa, de); float eg = exp(-max(de, 0.0) / 0.011);
  float mo = clamp(uMouth, 0.0, 1.0); vec2 mb = vec2(0.041 * (1.0 - 0.15 * mo) * (1.0 + 0.15 * uW.x), 0.0145 + 0.03 * mo);
  float dm = rbox(p - vec2(0.0, 0.612 - 0.012 * mo), mb, mb.y * 0.95); float am = max(fwidth(dm), 0.0008);
  float mth = 1.0 - smoothstep(-am, am, dm); float mg = exp(-max(dm, 0.0) / 0.009);
  vec3 eyeC = vec3(1.0, 1.0, 1.0) * 2.4 * eye + vec3(0.35, 0.75, 1.0) * 0.55 * eg * (1.0 - eye);
  vec3 mC = vec3(0.35, 0.9, 1.0) * 2.0 * mth + vec3(0.2, 0.7, 1.0) * 0.45 * mg * (1.0 - mth);
  totalEmissiveRadiance += (eyeC + mC) * vm; diffuseColor.rgb *= (1.0 - max(eye, mth)); }`);
  };
  mat.customProgramCacheKey = () => "r3dface";
}

const logoTex = new THREE.TextureLoader().load(base + "chest_logo.png"); logoTex.colorSpace = THREE.SRGBColorSpace; logoTex.anisotropy = 4; U.uLogo.value = logoTex;
const ld = new GLTFLoader(); const dr = new DRACOLoader(); dr.setDecoderPath(base + "three/addons/libs/draco/"); ld.setDRACOLoader(dr);
R3D.buildReady = new Promise((res, rej) => {
  ld.load(base + "robot.glb", (g) => {
    let mesh; g.scene.traverse((o) => { if (o.isMesh) mesh = o; });
    const geo = mesh.geometry; skin(geo);
    const mat = mesh.material; if (R3D.debugWeights) { mat.vertexColors = true; } if (mat.normalScale) mat.normalScale.set(0.35, 0.35); faceShader(mat);
    root = new THREE.Bone(); armL = new THREE.Bone(); armR = new THREE.Bone();
    armL.position.copy(SL); armR.position.copy(SR); root.add(armL); root.add(armR);
    const sm = new THREE.SkinnedMesh(geo, mat); sm.add(root); sm.bind(new THREE.Skeleton([root, armL, armR]));
    sm.frustumCulled = false;
    group = new THREE.Group(); group.add(sm); scene.add(group);
    ready = true; render(R3D.t0 || 0); res();
  }, undefined, (e) => rej(e));
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.robot3d = R3D.buildReady;

const D2R = Math.PI / 180;
function blinkAt(t) { // deterministic blinks every 2.6-4.1 s, sometimes double
  let b = 0; for (let s = 1.6, k = 0; s < 400; s += [3.2, 2.6, 4.1, 3.4][k++ % 4]) { if (s > t + 0.3) break;
    for (const o of k % 3 === 0 ? [0, 0.3] : [0]) { const d = t - (s + o); if (d >= 0 && d < 0.22) { const u = d < 0.09 ? d / 0.09 : 1 - (d - 0.09) / 0.13; b = Math.max(b, 0.5 - 0.5 * Math.cos(Math.PI * u)); } } }
  return b; }
function render(t) {
  R3D.lastT = t; if (!ready) return;
  const S = R3D.state, env = window.VO_ENV || [];
  const fe = (k) => env[Math.min(env.length - 1, Math.max(0, k))] || 0, ft = t * 30 + 1.2, f0 = Math.floor(ft), fr = ft - f0;
  const lin = (k) => fe(k) * (1 - fr) + fe(k + 1) * fr; // sub-frame interpolation
  const e = 0.12 * lin(f0 + 1) + 0.38 * lin(f0) + 0.3 * lin(f0 - 1) + 0.2 * lin(f0 - 2);
  const talk = R3D.talkUntil == null || t < R3D.talkUntil ? 1 : 0;
  const mo = Math.min(1, Math.max(0, (e - 0.04) * 1.35)); U.uMouth.value = talk * (mo * mo * (3 - 2 * mo));
  const expr = S.happy + S.x + S.wide + S.excited + S.flat;
  U.uBlink.value = expr > 0.3 ? 0 : blinkAt(t);
  U.uW.value.set(S.happy, S.x, S.wide, S.excited); U.uFlat.value = S.flat; U.uLook.value.set(-S.lookX, -S.lookY);
  // idle life (functions of t only) + tweened state
  const idle = Math.sin(t * 2 * Math.PI / 2.8), idle2 = Math.sin(t * 2 * Math.PI / 3.7 + 1.3);
  group.rotation.set(S.pitch * D2R, (S.yaw + (S.yawT || 0) + 3 * idle2) * D2R, (S.lean + 1.2 * idle) * D2R);
  const z = S.zoom || 1, A = 0.978 - ((R3D.anchorY || 1990) - (R3D.headTopY || 1402)) / PX; // zoom about the robot's base anchor
  group.position.set(0, A * (1 - z) - (S.zy || 0) / PX + S.bob + 0.005 * Math.sin(t * 2 * Math.PI / 1.6) + 0.003 * e, 0);
  group.scale.set(z / Math.sqrt(S.sq), z * S.sq, z / Math.sqrt(S.sq));
  armL.rotation.set((S.aLx + 3 * idle) * D2R, S.aLy * D2R, (S.aLz + 4 * idle2) * D2R);
  armR.rotation.set((S.aRx - 3 * idle) * D2R, S.aRy * D2R, (S.aRz - 4 * idle) * D2R);
  renderer.render(scene, cam);
}
R3D.render = render;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
