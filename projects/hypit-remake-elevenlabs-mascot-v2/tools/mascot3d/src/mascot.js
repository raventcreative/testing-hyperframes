// Mascot runtime: loads the rigged GLB copy, drives 19 bones + surface-following facial
// controls (blink, lower lid, gaze, brows, mouth visemes) from a pure state object.
// Bundled to vendor/mascot3d.js (IIFE, exposes window.Mascot3D). No clock, no randomness.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import * as Acting from './acting.js';
import * as Perform from './perform.js';
import * as Direct from './direct.js';

const lin = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };

const FACE_GLSL_PARS = /* glsl */ `
varying float vFM;
varying vec3 vRest;
varying vec3 vLidN;
uniform vec4 uEA; uniform vec4 uEB;      // eye centre xy, radius xy (A = screen-left, B = screen-right)
uniform vec4 uJA; uniform vec4 uJB;      // dUV/dxy per eye (du/dx du/dy dv/dx dv/dy)
uniform vec4 uBA; uniform vec4 uBB;      // brow centre xy, half-size xy
uniform vec4 uJBA; uniform vec4 uJBB;
uniform vec2 uBlink; uniform vec2 uLower; uniform vec2 uGaze; uniform vec2 uBrow; uniform vec2 uBrowTilt;
uniform float uMouthMix; uniform vec4 uMouth; uniform vec3 uMC; uniform vec3 uSkin; uniform vec3 uSkinEye;
vec2 gRimUV = vec2(0.0); float gRimOK = 0.0;
float gCover = 0.0; float gLid = 0.0; float gLidShade = 1.0; float gLash = 0.0;
uniform float uDebug;
uniform mat3 uHeadNM; uniform vec3 uHeadC; uniform float uCoverN; uniform vec3 uLidLit; uniform float uFaceSmooth;
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
  // lids (v6, suit mascot): an upper lid of sampled cheek skin sweeps down over the painted eye (incl. its upper
  // lashes) and a lower lid rises to meet it; the meeting line is a soft downward arc drawn as a thick lash line.
  if (blink > 0.001) {
    // v18: rounded-square lid (superellipse, p=3) sized to the painted eye incl. the outer lash flick
    float outer = (p.x - E.x) * sign(E.x) > 0.0 ? 1.0 : 0.0;
    float sx = E.z * mix(1.5, 1.8, outer);
    float nx = (p.x - E.x) / sx;
    float dy = p.y - (E.y + 0.004);
    float sy = dy > 0.0 ? E.w * 1.9 : E.w * 1.6;
    float ny = dy / sy;
    float ee = pow(abs(nx), 3.0) + pow(abs(ny), 3.0);
    if (ee < 1.6) {
      float b = smoothstep(0.0, 1.0, blink);
      float aa = fwidth(ny) * 1.2 + 1e-4;
      float yu = 2.0, covered;
      if (ee < 1.0) {
        float arc = pow(max(0.0, 1.0 - pow(abs(nx), 3.0)), 1.0 / 3.0);
        yu = mix(1.02, -0.2, b) * arc;                                       // upper lid edge
        float yl = mix(-1.02, -0.2, smoothstep(0.55, 1.0, b)) * arc;         // lower lid edge
        covered = max(smoothstep(yu - aa, yu + aa, ny), smoothstep(yl + aa, yl - aa, ny));
      } else {
        // just outside the lid: plain skin, faded to the lid colour so the lid never shows an outline
        // (dark texels are kept only above the lid, where the brow is)
        covered = smoothstep(0.1, 0.5, b) * mix(1.0, smoothstep(0.2, 0.45, dot(col, vec3(0.3, 0.55, 0.15))), smoothstep(0.6, 0.95, ny));
      }
      float edge = smoothstep(1.6, 1.0, ee);
      // lid skin: at the rim it takes the nearest skin texel just outside the lid along the ray from the eye centre
      // (lash / brow / eye-white texels are skipped), easing to the ring colour toward the centre
      vec2 dir = vec2(nx, ny) / max(pow(ee, 1.0 / 3.0), 1e-3);
      vec3 rimC = uSkinEye; bool found = false;
      for (int k = 0; k < 4; k++) {
        vec2 t = dir * max(1.03 + 0.09 * float(k), pow(ee, 1.0 / 3.0) + 0.02);
        vec2 q = vec2(E.x + t.x * sx, E.y + 0.004 + t.y * (t.y > 0.0 ? E.w * 1.9 : E.w * 1.6));
        vec3 sc = texture2D(map, baseUv + jmul(J, q - p)).rgb;
        bool skin = dot(sc, vec3(0.3, 0.55, 0.15)) > 0.5 && sc.r - sc.b > 0.04;
        if (!found && skin) { rimC = sc; found = true; gRimUV = baseUv + jmul(J, q - p); gRimOK = 1.0; }
      }
      rimC = mix(uSkinEye, rimC, 1.0 - smoothstep(0.15, 0.4, length(rimC - uSkinEye)));
      vec3 lid = mix(uSkinEye, rimC, smoothstep(0.3, 0.95, ee));
      if (ee < 1.0) {
        lid *= mix(0.975, 1.0, smoothstep(-1.0, 0.6, ny));                     // faint top-light gradient
        lid *= mix(0.93, 1.0, smoothstep(0.0, 0.3, abs(ny - yu)));              // soft crease under the lid edge
      }
      col = mix(col, lid, covered * edge);
      float ein = covered * step(ee, 1.0);
      gCover = max(gCover, ein);
      gLid = max(gLid, ein);
      // lash line on the moving lid edge (grows as the lid closes), tapered at the corners, lifted at the outer tip
      float lw = ee < 1.0 ? mix(0.0, 0.11, smoothstep(0.25, 0.9, b)) : 0.0;
      float tip = smoothstep(0.55, 1.0, abs(nx)) * 0.06 * b;
      float lash = smoothstep(lw + aa, lw * 0.35, abs(ny - (yu + tip))) * smoothstep(1.0, 0.72, abs(nx));
      col = mix(col, vec3(0.06, 0.04, 0.035), lash * step(0.001, lw));
      gLash = max(gLash, lash * step(0.001, lw));
    }
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
  // v4: the baked mouth was painted out of the texture and the cavity filled (facepatch.mjs),
  // so the procedural mouth is drawn straight onto clean skin. uMouth = (halfWidth, open, smile, tongue)
  if (uMouthMix <= 0.001) return col;
  vec2 q = p - uMC.xy;
  float hw = uMouth.x, op = uMouth.y, cv = uMouth.z;
  float x = q.x / hw;
  if (abs(x) > 1.25) return col;
  float aa = fwidth(q.y) * 1.25 + 1e-5;
  float xc = clamp(x, -1.0, 1.0);
  float s = sqrt(max(0.0, 1.0 - xc * xc));
  float yu = cv * xc * xc + op * 0.10 * s;           // upper lip edge (smile curve, lifts a little when open)
  float yl = cv * xc * xc - op * pow(s, 0.85);        // lower lip edge
  vec3 c = col;
  if (op > 0.0015) {
    float inside = smoothstep(-aa, aa, yu - q.y) * smoothstep(-aa, aa, q.y - yl) * smoothstep(1.0 + aa / hw, 1.0 - aa / hw, abs(x));
    float d = clamp((yu - q.y) / max(1e-4, yu - yl), 0.0, 1.0);
    vec3 cav = mix(vec3(0.30, 0.045, 0.05), vec3(0.40, 0.075, 0.075), smoothstep(0.2, 1.0, d));
    float teeth = smoothstep(0.30 + aa / op, 0.30 - aa / op, d) * smoothstep(0.009, 0.016, op) * smoothstep(0.92, 0.55, abs(x));
    cav = mix(cav, vec3(0.97, 0.955, 0.94), teeth * 0.92);
    float tg = smoothstep(0.55, 0.8, d) * uMouth.w * smoothstep(0.95, 0.4, abs(x));
    cav = mix(cav, vec3(0.88, 0.38, 0.36), tg);
    c = mix(c, cav, inside);
    // soft lip rim around the opening
    float rim = smoothstep(aa * 2.2, 0.0, abs(q.y - yu)) + smoothstep(aa * 2.2, 0.0, abs(q.y - yl)) * 0.7;
    c = mix(c, vec3(0.36, 0.09, 0.09), clamp(rim, 0.0, 1.0) * 0.6 * smoothstep(1.02, 0.85, abs(x)));
  } else {
    // closed: a soft smile line with tapered corners
    float lw = mix(0.0019, 0.0008, xc * xc);
    float ln = smoothstep(lw + aa, lw * 0.25, abs(q.y - yu)) * smoothstep(1.05, 0.88, abs(x));
    c = mix(c, vec3(0.42, 0.13, 0.12), ln);
  }
  // faint lower-lip blush that keeps the mouth from looking drawn-on
  vec2 lb = vec2(q.x / (hw * 0.75), (q.y - (yl - 0.004)) / 0.004);
  c = mix(c, c * vec3(1.0, 0.93, 0.92), smoothstep(1.0, 0.3, dot(lb, lb)) * 0.35);
  return mix(col, c, uMouthMix);
}
`;


// v18: smooth shading normals for the face skin (welded Laplacian) and, under each eyelid, the normal of a quadratic
// surface fitted to the skin ring around the eye, so a closed lid is lit exactly like the skin around it (the eye
// geometry itself is a bumpy relief). Stored as attribute _lidN (rest object space).
const LID_S = [1.5, 1.8, 1.9, 1.6];   // lid superellipse scale (eye radii): inner x, outer x, above, below
function lidEE(E, x, y) {   // superellipse "radius" (p=3) in lid units, same shape as the shader lid
  const out = (x - E.c[0]) * Math.sign(E.c[0]) > 0;
  const nx = (x - E.c[0]) / (E.r[0] * (out ? LID_S[1] : LID_S[0])), dy = y - (E.c[1] + 0.004);
  const ny = dy / (dy > 0 ? E.r[1] * LID_S[2] : E.r[1] * LID_S[3]);
  return Math.cbrt(Math.abs(nx) ** 3 + Math.abs(ny) ** 3);
}
function solve6(A, b) {   // gaussian elimination, 6x6
  const n = 6, M = A.map((r, i) => [...r, b[i]]);
  for (let c = 0; c < n; c++) {
    let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r;
    [M[c], M[p]] = [M[p], M[c]]; if (Math.abs(M[c][c]) < 1e-14) return null;
    for (let r = 0; r < n; r++) if (r !== c) { const f = M[r][c] / M[c][c]; for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k]; }
  }
  return M.map((r, i) => r[n] / r[i]);
}
function buildLidNormals(geo, F) {
  const ga = geo.attributes, n = ga.position.count;
  const P = new Float32Array(n * 3), N = new Float32Array(n * 3), FMa = new Float32Array(n);
  for (let i = 0; i < n; i++) {
    P[3 * i] = ga.position.getX(i); P[3 * i + 1] = ga.position.getY(i); P[3 * i + 2] = ga.position.getZ(i);
    N[3 * i] = ga.normal.getX(i); N[3 * i + 1] = ga.normal.getY(i); N[3 * i + 2] = ga.normal.getZ(i);
    FMa[i] = ga._facemask.getX(i);
  }
  // the outer lash flick sits on vertices outside the baked face mask: flag every front-facing vertex inside the
  // lid region as face so the lid (and the face shading) reaches them
  let flipped = 0;
  for (let i = 0; i < n; i++) {
    if (FMa[i] >= 0.5 || P[3 * i + 2] < 0.1 || N[3 * i + 2] < 0.15) continue;
    if (Math.min(lidEE(F.eyeA, P[3 * i], P[3 * i + 1]), lidEE(F.eyeB, P[3 * i], P[3 * i + 1])) < 1.2) { FMa[i] = 1; ga._facemask.setX(i, 1); flipped++; }
  }
  if (flipped) ga._facemask.needsUpdate = true;
  const out = new Float32Array(N);
  const canon = new Int32Array(n), seen = new Map();
  for (let i = 0; i < n; i++) {
    const k = Math.round(P[3 * i] * 1e5) + ',' + Math.round(P[3 * i + 1] * 1e5) + ',' + Math.round(P[3 * i + 2] * 1e5);
    let c = seen.get(k); if (c === undefined) { c = i; seen.set(k, i); } canon[i] = c;
  }
  const face = new Uint8Array(n); for (let i = 0; i < n; i++) if (FMa[i] > 0.5) face[canon[i]] = 1;
  const nb = new Map(), border = new Uint8Array(n), idx = geo.index ? geo.index.array : Uint32Array.from({ length: n }, (_, i) => i);
  const link = (u, v) => { let s = nb.get(u); if (!s) nb.set(u, (s = new Set())); s.add(v); };
  for (let t = 0; t < idx.length; t += 3) for (let a = 0; a < 3; a++) {
    const u = canon[idx[t + a]], v = canon[idx[t + (a + 1) % 3]];
    if (face[u] && face[v]) { link(u, v); link(v, u); } else if (face[u] || face[v]) { border[face[u] ? u : v] = 1; }
  }
  let cur = new Map();
  for (let i = 0; i < n; i++) { const c = canon[i]; if (!face[c]) continue; let a = cur.get(c); if (!a) cur.set(c, (a = [0, 0, 0])); a[0] += N[3 * i]; a[1] += N[3 * i + 1]; a[2] += N[3 * i + 2]; }
  const nrm = (a) => { const l = Math.hypot(a[0], a[1], a[2]) || 1; a[0] /= l; a[1] /= l; a[2] /= l; return a; };
  for (const a of cur.values()) nrm(a);
  for (let it = 0; it < 10; it++) {
    const nx = new Map();
    for (const [c, a] of cur) {
      if (border[c]) { nx.set(c, a); continue; }
      const s = [a[0], a[1], a[2]]; const ns = nb.get(c); let k = 0, q = [0, 0, 0];
      if (ns) for (const v of ns) { const b = cur.get(v); if (b) { q[0] += b[0]; q[1] += b[1]; q[2] += b[2]; k++; } }
      if (k) { s[0] = 0.4 * s[0] + 0.6 * q[0] / k; s[1] = 0.4 * s[1] + 0.6 * q[1] / k; s[2] = 0.4 * s[2] + 0.6 * q[2] / k; }
      nx.set(c, nrm(s));
    }
    cur = nx;
  }
  for (const E of [F.eyeA, F.eyeB]) {
    let ring = [];
    for (const [c, a] of cur) { const e = lidEE(E, P[3 * c], P[3 * c + 1]); if (e > 1.15 && e < 1.75 && a[2] > 0.25) ring.push(c); }
    let coef = null;
    for (let pass = 0; pass < 4; pass++) {
      const A = Array.from({ length: 6 }, () => new Array(6).fill(0)), b = new Array(6).fill(0);
      for (const c of ring) {
        const x = P[3 * c] - E.c[0], y = P[3 * c + 1] - E.c[1], z = P[3 * c + 2];
        const f = [1, x, y, x * x, x * y, y * y];
        for (let r = 0; r < 6; r++) { b[r] += f[r] * z; for (let k = 0; k < 6; k++) A[r][k] += f[r] * f[k]; }
      }
      coef = solve6(A, b); if (!coef) break;
      const res = (c) => { const x = P[3 * c] - E.c[0], y = P[3 * c + 1] - E.c[1]; return Math.abs(P[3 * c + 2] - (coef[0] + coef[1] * x + coef[2] * y + coef[3] * x * x + coef[4] * x * y + coef[5] * y * y)); };
      ring = ring.filter((c) => res(c) < [0.01, 0.005, 0.003, 0.002][pass]);
    }
    if (!coef) continue;
    for (const [c, a] of cur) {
      const e = lidEE(E, P[3 * c], P[3 * c + 1]); if (e > 1.25) continue;
      const x = P[3 * c] - E.c[0], y = P[3 * c + 1] - E.c[1];
      const fn = nrm([-(coef[1] + 2 * coef[3] * x + coef[4] * y), -(coef[2] + coef[4] * x + 2 * coef[5] * y), 1]);
      const t = Math.min(1, Math.max(0, (1.25 - e) / 0.3)), w = t * t * (3 - 2 * t);
      cur.set(c, nrm([a[0] + (fn[0] - a[0]) * w, a[1] + (fn[1] - a[1]) * w, a[2] + (fn[2] - a[2]) * w]));
    }
  }
  for (let i = 0; i < n; i++) { const a = cur.get(canon[i]); if (a) { out[3 * i] = a[0]; out[3 * i + 1] = a[1]; out[3 * i + 2] = a[2]; } }
  geo.setAttribute('_lidN', new THREE.BufferAttribute(out, 3));
}

export class Mascot {
  static async create(canvas, opts) {
    const m = new Mascot();
    await m.init(canvas, opts);
    return m;
  }
  async init(canvas, { url, face, width = 1080, height = 1920, envIntensity = 0.45, decals = [] }) {
    this.W = width; this.H = height;
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true, premultipliedAlpha: true }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.NoToneMapping;
    r.setClearColor(0x000000, 0);
    const scene = (this.scene = new THREE.Scene());
    const pm = new THREE.PMREMGenerator(r);
    scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
    scene.environmentIntensity = envIntensity;
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
    // opt-in (window.MASCOT_TEX_CLEAN): the Tripo atlas packs unrelated charts edge to edge with no gutters, so mipmapped
    // minification blends hair/skin texels into jacket edges ("frayed fibre" fringe). Sampling the base level only removes it.
    if (typeof window !== 'undefined' && window.MASCOT_TEX_CLEAN) {
      const m = this.mesh.material;
      for (const k of ['map', 'normalMap', 'roughnessMap', 'metalnessMap']) { const tx = m[k]; if (!tx) continue; tx.generateMipmaps = false; tx.minFilter = THREE.LinearFilter; tx.anisotropy = 1; tx.needsUpdate = true; }
    }
    // optional surface decals (e.g. a crisp logo on the jacket): a curved grid that follows the rest-pose surface
    // (z sampled offline), parented to a bone so it moves with the body. Texture is high-res, independent of the atlas.
    this.root.updateMatrixWorld(true);
    for (const d of decals) {
      const tex = await new THREE.TextureLoader().loadAsync(d.url);
      tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
      const [x0, x1, y0, y1] = d.box, Z = d.zgrid, ny = Z.length, nx = Z[0].length;
      const pos = [], uv = [], ix = [];
      for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) {
        const u = i / (nx - 1), v = j / (ny - 1);
        pos.push(x0 + (x1 - x0) * u, y1 - (y1 - y0) * v, Z[j][i] + (d.offset || 0.0012)); uv.push(u, 1 - v);
      }
      for (let j = 0; j < ny - 1; j++) for (let i = 0; i < nx - 1; i++) { const a = j * nx + i; ix.push(a, a + nx, a + 1, a + 1, a + nx, a + nx + 1); }
      const g = new THREE.BufferGeometry();
      g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
      g.setIndex(ix); g.computeVertexNormals();
      const mat = new THREE.MeshStandardMaterial({ map: tex, transparent: true, roughness: d.roughness ?? 0.55, metalness: 0, depthWrite: false,
        polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -2 });
      const mesh = new THREE.Mesh(g, mat); mesh.frustumCulled = false; mesh.renderOrder = 2;
      const bone = this.bones[d.bone || 'chest'];
      bone.add(mesh);
      // geometry is authored in rest object space: express it in the bone's frame
      const inv = new THREE.Matrix4().copy(bone.matrixWorld).invert().multiply(this.mesh.matrixWorld);
      mesh.applyMatrix4(inv);
    }

    // facial controls through a surface-following shader patch
    const F = face, mat = this.mesh.material;
    buildLidNormals(this.mesh.geometry, F);
    const U = (this.u = {
      uEA: { value: new THREE.Vector4(F.eyeA.c[0], F.eyeA.c[1], F.eyeA.r[0], F.eyeA.r[1]) },
      uEB: { value: new THREE.Vector4(F.eyeB.c[0], F.eyeB.c[1], F.eyeB.r[0], F.eyeB.r[1]) },
      uJA: { value: new THREE.Vector4(...F.eyeA.J) }, uJB: { value: new THREE.Vector4(...F.eyeB.J) },
      uBA: { value: new THREE.Vector4(F.browA.c[0], F.browA.c[1], 0.042, 0.012) },
      uBB: { value: new THREE.Vector4(F.browB.c[0], F.browB.c[1], 0.042, 0.012) },
      uJBA: { value: new THREE.Vector4(...F.browA.J) }, uJBB: { value: new THREE.Vector4(...F.browB.J) },
      uBlink: { value: new THREE.Vector2() }, uLower: { value: new THREE.Vector2() },
      uGaze: { value: new THREE.Vector2() }, uBrow: { value: new THREE.Vector2() }, uBrowTilt: { value: new THREE.Vector2() },
      uMouthMix: { value: 0 }, uDebug: { value: 0 }, uHeadNM: { value: new THREE.Matrix3() }, uHeadC: { value: new THREE.Vector3(...(F.headC || [0, 0.6, -0.04])) }, uCoverN: { value: F.coverNormal ?? 1 }, uLidLit: { value: new THREE.Vector3(...(F.lidLit || [0.98, 0.95, 0.93])) }, uMouth: { value: new THREE.Vector4(0.026, 0, 0.004, 0.6) },
      uMC: { value: new THREE.Vector3(F.mouth.c[0], F.mouth.c[1] + (F.mouthDy ?? 0.0135), F.mouth.c[1]) }, uFaceSmooth: { value: F.faceSmooth ?? 0 },
      uSkin: { value: new THREE.Vector3(lin(F.skin[0]), lin(F.skin[1]), lin(F.skin[2])) },
      uSkinEye: { value: new THREE.Vector3(lin(F.skinEye[0]), lin(F.skinEye[1]), lin(F.skinEye[2])) },
    });
    mat.onBeforeCompile = (sh) => {
      Object.assign(sh.uniforms, U);
      sh.vertexShader = sh.vertexShader
        .replace('#include <common>', '#include <common>\nattribute float _facemask;\nvarying float vFM;\nvarying vec3 vRest;\nuniform vec4 uEA; uniform vec4 uEB; uniform vec2 uBlink;\nattribute vec3 _lidN;\nvarying vec3 vLidN;')
        .replace('#include <defaultnormal_vertex>', '#include <defaultnormal_vertex>\n#ifdef USE_SKINNING\nvLidN = normalMatrix * (skinMatrix * vec4(_lidN, 0.0)).xyz;\n#else\nvLidN = normalMatrix * _lidN;\n#endif')
        .replace('#include <begin_vertex>', `#include <begin_vertex>
vFM = _facemask;
vRest = position;
// v5: blinks disabled (the GLB has no eyelid geometry; every overlay/squash variant produced visible artifacts)
`);
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
  if (uDebug > 0.5 && uDebug < 1.5 && vFM > 0.5) sampledDiffuseColor.rgb = mix(sampledDiffuseColor.rgb, vec3(1.0, 0.0, 0.0), 0.55);
  diffuseColor *= sampledDiffuseColor;
#endif`)
        .replace('#include <roughnessmap_fragment>', '#include <roughnessmap_fragment>\nroughnessFactor = mix(roughnessFactor, max(roughnessFactor, 0.5), step(0.5, vFM) * uFaceSmooth);\n#ifdef USE_ROUGHNESSMAP\nif (gRimOK > 0.5) { vec4 rimMR = texture2D(roughnessMap, gRimUV); roughnessFactor = mix(roughnessFactor, max(rimMR.g * roughness, 0.5), gCover); }\n#endif')
        .replace('#include <metalnessmap_fragment>', '#include <metalnessmap_fragment>\n#ifdef USE_METALNESSMAP\nif (gRimOK > 0.5) { metalnessFactor = mix(metalnessFactor, texture2D(metalnessMap, gRimUV).b * metalness, gCover); }\n#endif')
        .replace('#include <dithering_fragment>', '#include <dithering_fragment>\n// v18: lids are lit like skin (smooth fitted normal, see buildLidNormals); only the lash line is laid on top\n// highlight shoulder: roll bright values off softly (hue kept) so pale skin never clips to flat white\n{ float mx = max(gl_FragColor.r, max(gl_FragColor.g, gl_FragColor.b));\n  if (mx > 0.78) gl_FragColor.rgb *= (0.78 + 0.2 * (1.0 - exp(-(mx - 0.78) / 0.2))) / mx; }\ngl_FragColor.rgb = mix(gl_FragColor.rgb, vec3(0.16, 0.11, 0.1), gLash);\nif (uDebug > 1.5) gl_FragColor = vec4(vMapUv, 0.0, 1.0);')
        .replace('#include <normal_fragment_maps>', '#include <normal_fragment_maps>\nfloat sNl = length(vLidN);\nif (vFM > 0.5 && sNl > 1e-5) {\n  vec3 sN = (vLidN / sNl) * faceDirection;\n  normal = normalize(mix(normal, sN, uFaceSmooth));\n  normal = normalize(mix(normal, sN, gCover));\n}');
    };
    mat.customProgramCacheKey = () => 'mascot-face-v18g';
    mat.needsUpdate = true;
    if (mat.roughness !== undefined) { mat.roughness = Math.max(mat.roughness, 0.55); mat.metalness = 0; }

    // soft contact shadow (follows the root on the floor)
    const sc = document.createElement('canvas'); sc.width = sc.height = 128;
    const g = sc.getContext('2d'); const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
    grd.addColorStop(0, 'rgba(10,13,44,0.42)'); grd.addColorStop(0.5, 'rgba(10,13,44,0.16)'); grd.addColorStop(1, 'rgba(10,13,44,0)');
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
    u.uMouthMix.value = f.mouthMix || 0; u.uDebug.value = s.debug === 'uv' ? 2 : s.debug ? 1 : 0;
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
window.Mascot3D = { Mascot, ...Acting, ...Perform, ...Direct };
