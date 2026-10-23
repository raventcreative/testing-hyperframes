// Mascot runtime: loads the rigged GLB copy, drives 19 bones + surface-following facial
// controls (blink, lower lid, gaze, brows, mouth visemes) from a pure state object.
// Bundled to vendor/mascot3d.js (IIFE, exposes window.Mascot3D). No clock, no randomness.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import * as Acting from './acting.js';

const lin = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };

const FACE_GLSL_PARS = /* glsl */ `
varying float vFM;
varying vec3 vRest;
uniform vec4 uEA; uniform vec4 uEB;      // eye centre xy, radius xy (A = screen-left, B = screen-right)
uniform vec4 uJA; uniform vec4 uJB;      // dUV/dxy per eye (du/dx du/dy dv/dx dv/dy)
uniform vec4 uBA; uniform vec4 uBB;      // brow centre xy, half-size xy
uniform vec4 uJBA; uniform vec4 uJBB;
uniform vec2 uBlink; uniform vec2 uLower; uniform vec2 uGaze; uniform vec2 uBrow; uniform vec2 uBrowTilt;
uniform float uMouthMix; uniform vec4 uMouth; uniform vec3 uMC; uniform vec3 uSkin; uniform vec3 uSkinEye;
float gCover = 0.0;
uniform float uDebug;
uniform mat3 uHeadNM; uniform vec3 uHeadC;
vec2 jmul(vec4 J, vec2 d){ return vec2(J.x*d.x + J.y*d.y, J.z*d.x + J.w*d.y); }
vec3 eyeLayer(vec3 col, vec2 p, vec4 E, vec4 J, float blink, float lower, vec2 gaze, vec2 baseUv){
  vec2 d = (p - E.xy) / E.zw;
  float e = dot(d, d);
  // gaze: re-sample iris/white inside the inner opening
  if (e < 0.72 && (abs(gaze.x) + abs(gaze.y)) > 1e-5) {
    vec2 ds = (p - gaze - E.xy) / E.zw;
    vec3 s = texture2D(map, baseUv - jmul(J, gaze)).rgb;
    if (dot(ds, ds) > 0.72) s = vec3(0.86, 0.87, 0.90);
    col = mix(col, s, smoothstep(0.72, 0.55, e));
  }
  // lids (upper from top, lower from bottom) inside the enlarged cover ellipse
  vec2 dc = (p - E.xy) / (E.zw * vec2(1.16, 1.22));
  float ec = dot(dc, dc);
  if (ec < 1.0 && (blink > 0.001 || lower > 0.001)) {
    float arc = sqrt(max(0.0, 1.0 - dc.x * dc.x));
    float yu = (1.0 - 2.0 * blink) * arc;
    float yl = -(1.0 - 2.0 * lower) * arc;
    float covered = max(smoothstep(yu - 0.03, yu + 0.03, dc.y), smoothstep(yl + 0.03, yl - 0.03, dc.y));
    float edge = smoothstep(1.0, 0.78, ec);
    col = mix(col, uSkinEye * mix(0.94, 1.0, smoothstep(0.0, 0.3, abs(dc.y - yu))), covered * edge);
    gCover = max(gCover, covered * edge);
    // lash line on the upper lid edge
    float lw2 = mix(0.07, 0.13, smoothstep(0.6, 1.0, blink));
    float lash = smoothstep(lw2, lw2 * 0.35, abs(dc.y - yu)) * step(0.02, blink) * smoothstep(0.98, 0.7, abs(dc.x));
    col = mix(col, vec3(0.045, 0.028, 0.024), lash * edge);
  }
  return col;
}
vec3 browLayer(vec3 col, vec2 p, vec4 Bc, vec4 J, float raise, float tilt, vec2 baseUv){
  float sh = raise + tilt * (p.x - Bc.x) / Bc.z;
  if (abs(sh) < 1e-5) return col;
  vec2 d = p - Bc.xy;
  float wx = smoothstep(Bc.z, Bc.z * 0.75, abs(d.x));
  float wy = smoothstep(Bc.w + abs(sh) * 0.5 + 0.004, Bc.w + abs(sh) * 0.5, abs(d.y - sh * 0.5));
  float w = wx * wy;
  if (w <= 0.0) return col;
  vec3 s = texture2D(map, baseUv - jmul(J, vec2(0.0, sh))).rgb;
  return mix(col, s, w);
}
vec3 mouthLayer(vec3 col, vec2 p){
  if (uMouthMix <= 0.001) return col;
  vec2 q = p - uMC.xy;
  // 1) cover the baked mouth with skin
  vec2 dc = (p - vec2(uMC.x, uMC.z)) / vec2(0.047, 0.034);
  float cov = smoothstep(1.0, 0.72, dot(dc, dc));
  col = mix(col, uSkin, cov * uMouthMix);
  gCover = max(gCover, cov * uMouthMix * 0.85);
  // 2) procedural mouth: uMouth = (halfWidth, open, cornerCurve, tongue)
  float hw = uMouth.x, op = uMouth.y, cv = uMouth.z;
  float x = q.x / hw;
  if (abs(x) < 1.0) {
    float yu = cv * x * x;
    float yl = yu - op * sqrt(max(0.0, 1.0 - x * x));
    float lw = mix(0.0028, 0.0013, x * x);
    vec3 inside = vec3(0.32, 0.055, 0.06);
    if (q.y < yu && q.y > yl) {
      float tg = smoothstep(yl + (yu - yl) * 0.55, yl + (yu - yl) * 0.35, q.y) * uMouth.w;
      inside = mix(inside, vec3(0.86, 0.33, 0.31), tg);
      col = mix(col, inside, uMouthMix);
    }
    float ln = smoothstep(lw, lw * 0.4, abs(q.y - yu));
    if (op > 0.002) ln = max(ln, smoothstep(lw * 0.9, lw * 0.3, abs(q.y - yl)) * 0.85);
    col = mix(col, vec3(0.20, 0.035, 0.035), ln * uMouthMix);
  }
  return col;
}
`;

export class Mascot {
  static async create(canvas, opts) {
    const m = new Mascot();
    await m.init(canvas, opts);
    return m;
  }
  async init(canvas, { url, face, width = 1080, height = 1920 }) {
    this.W = width; this.H = height;
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true, premultipliedAlpha: true }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.NoToneMapping;
    r.setClearColor(0x000000, 0);
    const scene = (this.scene = new THREE.Scene());
    const pm = new THREE.PMREMGenerator(r);
    scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
    scene.environmentIntensity = 0.45;
    scene.add(new THREE.HemisphereLight(0xf4f8ff, 0x9fb0cc, 1.15));
    const key = new THREE.DirectionalLight(0xfff6ee, 1.9); key.position.set(-1.2, 2.2, 2.0); scene.add(key);   // upper-left key
    const rim = new THREE.DirectionalLight(0xcfe0ff, 1.1); rim.position.set(1.4, 1.2, -1.6); scene.add(rim);    // cool rim
    const fill = new THREE.DirectionalLight(0xffffff, 0.35); fill.position.set(1.5, 0.6, 2.0); scene.add(fill);
    this.cam = new THREE.OrthographicCamera(-1, 1, 1, -1, -10, 10);

    const gltf = await new GLTFLoader().loadAsync(url);
    this.root = gltf.scene;
    scene.add(this.root);
    this.rigRoot = this.root.getObjectByName('rig_root');
    this.bones = {};
    this.root.traverse((o) => { if (o.isBone) this.bones[o.name] = o; if (o.isSkinnedMesh) this.mesh = o; });
    this.rest = {};
    for (const [n, b] of Object.entries(this.bones)) this.rest[n] = b.position.clone();
    this.mesh.frustumCulled = false;

    // facial controls through a surface-following shader patch
    const F = face, mat = this.mesh.material;
    const U = (this.u = {
      uEA: { value: new THREE.Vector4(F.eyeA.c[0], F.eyeA.c[1], F.eyeA.r[0], F.eyeA.r[1]) },
      uEB: { value: new THREE.Vector4(F.eyeB.c[0], F.eyeB.c[1], F.eyeB.r[0], F.eyeB.r[1]) },
      uJA: { value: new THREE.Vector4(...F.eyeA.J) }, uJB: { value: new THREE.Vector4(...F.eyeB.J) },
      uBA: { value: new THREE.Vector4(F.browA.c[0], F.browA.c[1], 0.042, 0.012) },
      uBB: { value: new THREE.Vector4(F.browB.c[0], F.browB.c[1], 0.042, 0.012) },
      uJBA: { value: new THREE.Vector4(...F.browA.J) }, uJBB: { value: new THREE.Vector4(...F.browB.J) },
      uBlink: { value: new THREE.Vector2() }, uLower: { value: new THREE.Vector2() },
      uGaze: { value: new THREE.Vector2() }, uBrow: { value: new THREE.Vector2() }, uBrowTilt: { value: new THREE.Vector2() },
      uMouthMix: { value: 0 }, uDebug: { value: 0 }, uHeadNM: { value: new THREE.Matrix3() }, uHeadC: { value: new THREE.Vector3(0, 0.6, -0.04) }, uMouth: { value: new THREE.Vector4(0.026, 0, 0.004, 0.6) },
      uMC: { value: new THREE.Vector3(F.mouth.c[0], F.mouth.c[1] + 0.0135, F.mouth.c[1]) },
      uSkin: { value: new THREE.Vector3(lin(F.skin[0]), lin(F.skin[1]), lin(F.skin[2])) },
      uSkinEye: { value: new THREE.Vector3(lin(F.skinEye[0]), lin(F.skinEye[1]), lin(F.skinEye[2])) },
    });
    mat.onBeforeCompile = (sh) => {
      Object.assign(sh.uniforms, U);
      sh.vertexShader = sh.vertexShader
        .replace('#include <common>', '#include <common>\nattribute float _facemask;\nvarying float vFM;\nvarying vec3 vRest;')
        .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFM = _facemask;\nvRest = position;');
      sh.fragmentShader = sh.fragmentShader
        .replace('#include <map_pars_fragment>', '#include <map_pars_fragment>\n' + FACE_GLSL_PARS)
        .replace('#include <map_fragment>', `
#ifdef USE_MAP
  vec4 sampledDiffuseColor = texture2D( map, vMapUv );
  if (vFM > 0.5) {
    vec2 fp = vRest.xy;
    vec3 c = sampledDiffuseColor.rgb;
    c = browLayer(c, fp, uBA, uJBA, uBrow.x, uBrowTilt.x, vMapUv);
    c = browLayer(c, fp, uBB, uJBB, uBrow.y, uBrowTilt.y, vMapUv);
    c = eyeLayer(c, fp, uEA, uJA, uBlink.x, uLower.x, uGaze, vMapUv);
    c = eyeLayer(c, fp, uEB, uJB, uBlink.y, uLower.y, uGaze, vMapUv);
    c = mouthLayer(c, fp);
    sampledDiffuseColor.rgb = c;
  }
  if (uDebug > 0.5 && vFM > 0.5) sampledDiffuseColor.rgb = mix(sampledDiffuseColor.rgb, vec3(1.0, 0.0, 0.0), 0.55);
  diffuseColor *= sampledDiffuseColor;
#endif`)
        .replace('#include <roughnessmap_fragment>', '#include <roughnessmap_fragment>\nroughnessFactor = mix(roughnessFactor, 0.85, gCover);')
        .replace('#include <normal_fragment_maps>', '#include <normal_fragment_maps>\nnormal = normalize(mix(normal, normalize(uHeadNM * normalize(vRest - uHeadC)), gCover));');
    };
    mat.customProgramCacheKey = () => 'mascot-face-v5';
    mat.needsUpdate = true;
    if (mat.roughness !== undefined) { mat.roughness = Math.max(mat.roughness, 0.55); mat.metalness = 0; }

    // soft contact shadow (follows the root on the floor)
    const sc = document.createElement('canvas'); sc.width = sc.height = 128;
    const g = sc.getContext('2d'); const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
    grd.addColorStop(0, 'rgba(18,21,50,0.42)'); grd.addColorStop(0.5, 'rgba(18,21,50,0.16)'); grd.addColorStop(1, 'rgba(18,21,50,0)');
    g.fillStyle = grd; g.fillRect(0, 0, 128, 128);
    const st = new THREE.CanvasTexture(sc); st.colorSpace = THREE.SRGBColorSpace;
    this.shadow = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.36), new THREE.MeshBasicMaterial({ map: st, transparent: true, depthWrite: false }));
    this.shadow.rotation.x = -Math.PI / 2; this.shadow.position.y = 0.002; this.shadow.renderOrder = -1;
    scene.add(this.shadow);
    // compile once so the first seek is not slower than the rest
    r.compile(scene, this.cam);
  }
  // framing: feet at (fx, fy) px, figure height h px, camera yaw/pitch in degrees
  setView({ fx, fy, h, yaw = 0, pitch = 6 }) {
    const k = h / 0.98, c = this.cam;
    c.left = -fx / k; c.right = (this.W - fx) / k; c.top = fy / k; c.bottom = -(this.H - fy) / k;
    const a = (yaw * Math.PI) / 180, p = (pitch * Math.PI) / 180;
    c.position.set(Math.sin(a) * Math.cos(p) * 4, Math.sin(p) * 4, Math.cos(a) * Math.cos(p) * 4);
    c.up.set(0, 1, 0); c.lookAt(0, 0, 0); c.updateProjectionMatrix();
  }
  setState(s) {
    const R = s.root || {};
    const rr = this.rigRoot;
    rr.position.set(R.x || 0, R.y || 0, R.z || 0);
    rr.rotation.set(R.rx || 0, R.ry || 0, R.rz || 0, 'YXZ');
    const sc = R.s == null ? 1 : R.s; rr.scale.set(sc * (R.sx || 1), sc * (R.sy || 1), sc * (R.sx || 1));
    for (const [n, b] of Object.entries(this.bones)) {
      const v = (s.bones && s.bones[n]) || [0, 0, 0];
      b.rotation.set(v[0], v[1], v[2], 'XYZ');
      b.position.copy(this.rest[n]);
    }
    this.shadow.position.x = R.x || 0; this.shadow.position.z = (R.z || 0) + 0.03;
    const lift = Math.max(0, R.y || 0);
    this.shadow.scale.setScalar(Math.max(0.55, 1 - lift * 2.2) * sc);
    this.shadow.material.opacity = Math.max(0.35, 1 - lift * 3);
    const f = s.face || {};
    const u = this.u;
    u.uBlink.value.set(...(f.blink || [0, 0])); u.uLower.value.set(...(f.lower || [0, 0]));
    u.uGaze.value.set(...(f.gaze || [0, 0])); u.uBrow.value.set(...(f.brow || [0, 0]));
    u.uBrowTilt.value.set(...(f.browTilt || [0, 0]));
    u.uMouthMix.value = f.mouthMix || 0; u.uDebug.value = s.debug ? 1 : 0;
    const mo = f.mouth || [0.026, 0, 0.004, 0.6]; u.uMouth.value.set(mo[0], mo[1], mo[2], mo[3]);
    this.visible = s.visible !== false;
  }
  render() {
    // smooth head-sphere normal (view space) used under the eyelids / closed mouth
    this.root.updateMatrixWorld(true); this.cam.updateMatrixWorld(true);
    const hb = this.bones.head; const m4 = new THREE.Matrix4().multiplyMatrices(this.cam.matrixWorldInverse, hb.matrixWorld);
    this.u.uHeadNM.value.setFromMatrix4(m4);
    this.renderer.clear();
    if (this.visible) this.renderer.render(this.scene, this.cam);
  }
}
window.Mascot3D = { Mascot, ...Acting };
