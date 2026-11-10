// StyleBot shared helpers: deterministic hash noise (GLSL + JS), the robot's procedural screen face, the shared vertex
// shader used by every custom style material (skinning aware), and a tiny full-screen pass helper.
import * as THREE from 'three';

// ------------------------------------------------------------------ JS side (deterministic, seeded)
export const hash1 = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
export const hash2 = (a, b) => hash1(a * 157.31 + b * 113.97 + 0.5);
export const clamp01 = (x) => Math.max(0, Math.min(1, x));
export const srgbToLin = (c) => (c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
// hex 0xRRGGBB -> THREE.Color holding *display* (sRGB) values (no conversion): used by custom shaders that output sRGB
export const sc = (hex) => { const c = new THREE.Color(); c.r = ((hex >> 16) & 255) / 255; c.g = ((hex >> 8) & 255) / 255; c.b = (hex & 255) / 255; return c; };
// hex -> linear THREE.Color (for lit / linear pipelines)
export const lc = (hex) => { const c = sc(hex); c.r = srgbToLin(c.r); c.g = srgbToLin(c.g); c.b = srgbToLin(c.b); return c; };
export const palArray = (list, conv = sc) => list.map((h) => (typeof h === 'number' ? conv(h) : h));

// ------------------------------------------------------------------ GLSL chunks
export const NOISE = /* glsl */ `
float h12(vec2 p) { vec3 p3 = fract(vec3(p.xyx) * 0.1031); p3 += dot(p3, p3.yzx + 33.33); return fract((p3.x + p3.y) * p3.z); }
vec2 h22(vec2 p) { vec3 p3 = fract(vec3(p.xyx) * vec3(0.1031, 0.1030, 0.0973)); p3 += dot(p3, p3.yzx + 33.33); return fract((p3.xx + p3.yz) * p3.zy); }
float h13(vec3 p3) { p3 = fract(p3 * 0.1031); p3 += dot(p3, p3.zyx + 31.32); return fract((p3.x + p3.y) * p3.z); }
float vnoise(vec2 p) { vec2 i = floor(p), f = fract(p); vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(h12(i), h12(i + vec2(1, 0)), u.x), mix(h12(i + vec2(0, 1)), h12(i + vec2(1, 1)), u.x), u.y); }
float fbm(vec2 p) { float a = 0.0, w = 0.5; for (int i = 0; i < 4; i++) { a += w * vnoise(p); p = p * 2.03 + vec2(17.1, 9.2); w *= 0.5; } return a; }
vec3 toSRGB(vec3 c) { c = max(c, 0.0); return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }
vec3 toLin(vec3 c) { return mix(c / 12.92, pow((c + 0.055) / 1.055, vec3(2.4)), step(0.04045, c)); }
float luma(vec3 c) { return dot(c, vec3(0.2126, 0.7152, 0.0722)); }
`;

// robot screen face (same shapes as robot_base.js): eyes at s = +-1, talk bars at t = -1
export const FACE = /* glsl */ `
uniform float uBlink; uniform vec2 uGaze; uniform float uHappy; uniform float uTalk; uniform vec4 uBars; uniform float uBar5;
uniform float uEyeGlow; uniform float uSquint; uniform float uRing;
float sdEll(vec2 p, vec2 r) { float k0 = length(p / r); float k1 = length(p / (r * r)); return k0 * (k0 - 1.0) / max(k1, 1e-5); }
float sdRound(vec2 p, vec2 b, float rr) { vec2 q = abs(p) - b + rr; return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - rr; }
// signed distance to the face shapes (negative inside), in visor units
float faceSD(vec2 p) {
  float dm = 1e5;
  for (int i = 0; i < 2; i++) {
    float sx = i == 0 ? -1.0 : 1.0;
    vec2 c = vec2(sx, 0.02) + uGaze;
    float open = max(0.07, 1.0 - uBlink);
    vec2 r = vec2(0.39 * (1.0 + 0.08 * uBlink), 0.58 * open * (1.0 - 0.25 * uSquint));
    float d = sdEll(p - c, r);
    float dh = max(d, -sdEll(p - c - vec2(0.0, -0.34), vec2(0.46, 0.62)));
    d = mix(d, dh, uHappy);
    dm = min(dm, d);
  }
  float bars[5]; bars[0] = uBars.x; bars[1] = uBars.y; bars[2] = uBars.z; bars[3] = uBars.w; bars[4] = uBar5;
  if (uTalk > 0.01) for (int k = 0; k < 5; k++) {
    float h = 0.035 + 0.20 * bars[k];
    float d = sdRound(p - vec2(-0.36 + 0.18 * float(k), -1.0), vec2(0.045, h), 0.045);
    dm = min(dm, d + (1.0 - uTalk) * 0.3);
  }
  return dm;
}
float screenFace(vec2 p) { return 1.0 - smoothstep(-0.03, 0.03, faceSD(p)); }
`;

// AI PRENEUR wordmark: cylindrical projection around the collar (same mapping as robot-collab/tools/bake_logo.py)
export const LOGO = /* glsl */ `
uniform sampler2D uLogo;
float logoMask(vec3 rp, vec3 rn) {
  const float AX = 0.023, AZ = 0.005, RREF = 0.215, W = 0.27, YC = 0.385, H = 0.0241;
  float th = atan(rp.x - AX, rp.z - AZ);
  float lu = (th * RREF + W * 0.5) / W, lv = (YC + H * 0.5 - rp.y) / H;
  vec2 rd = normalize(vec2(rp.x - AX, rp.z - AZ));
  float facing = dot(normalize(rn.xz), rd);
  if (lu < 0.0 || lu > 1.0 || lv < 0.0 || lv > 1.0 || rp.z < 0.0 || facing < 0.35) return 0.0;
  return texture2D(uLogo, vec2(lu, lv)).a;
}
`;

// ------------------------------------------------------------------ shared vertex shader for custom style materials
// varyings: vN (world normal), vNV (view normal), vW (world pos), vRest (bind-pose object pos), vRestN, vUv, vDepth (view z)
// ROBOT: vFace (visor coords); SET: vPal (palette index)
export const VERT = /* glsl */ `
#include <common>
#include <skinning_pars_vertex>
#ifdef ROBOT
attribute vec3 _face;
attribute vec3 aSmoothN;
attribute vec3 aBlobN;
attribute vec3 aCls;
varying vec3 vFace;
varying vec3 vCls;
#else
attribute float aPal;
flat varying int vPal;
#endif
#ifdef SNAP
uniform vec2 uSnap;
#endif
#ifdef AFFINE
varying vec3 vAff;
#endif
varying vec3 vN; varying vec3 vNV; varying vec3 vW; varying vec3 vRest; varying vec3 vRestN; varying vec2 vUv; varying float vDepth;
#ifdef VLIGHT
uniform vec3 uKeyDir; uniform vec3 uKeyCol; uniform vec3 uAmbUp; uniform vec3 uAmbDn;
varying vec3 vGouraud;
#endif
void main() {
  vUv = uv;
  #include <beginnormal_vertex>
  #if defined(ROBOT) && defined(BLOBN)
  objectNormal = aBlobN;
  #elif defined(ROBOT) && defined(SMOOTHN)
  objectNormal = aSmoothN;
  #endif
  #include <skinbase_vertex>
  #include <skinnormal_vertex>
  #include <defaultnormal_vertex>
  #include <begin_vertex>
  #include <skinning_vertex>
  #include <project_vertex>
  vNV = normalize(transformedNormal);
  vN = normalize((vec4(transformedNormal, 0.0) * viewMatrix).xyz);
  vW = (modelMatrix * vec4(transformed, 1.0)).xyz;
  vRest = position; vRestN = normal;
  #if defined(ROBOT) && defined(SMOOTHN)
  vRestN = aSmoothN;
  #endif
  vDepth = -mvPosition.z;
  #ifdef ROBOT
  vFace = _face; vCls = aCls;
  #else
  vPal = int(aPal + 0.5);
  #endif
  #ifdef SNAP
  vec4 cp = gl_Position; cp.xy = floor(cp.xy / cp.w * uSnap + 0.5) / uSnap * cp.w; gl_Position = cp;
  #endif
  #ifdef AFFINE
  vec3 an = abs(vN); vec2 puv = an.y > 0.5 ? vW.xz : (an.z > 0.5 ? vW.xy : vW.zy);
  vAff = vec3(puv * gl_Position.w, gl_Position.w);
  #endif
  #ifdef VLIGHT
  float nl = max(dot(vN, normalize(uKeyDir)), 0.0);
  vGouraud = uKeyCol * nl + mix(uAmbDn, uAmbUp, vN.y * 0.5 + 0.5);
  #endif
}
`;

// fragment preamble for custom style materials (MRT outputs declared when MRT is defined)
export const FRAG_HEAD = /* glsl */ `
#ifdef ROBOT
varying vec3 vFace; varying vec3 vCls;
uniform sampler2D uMap; uniform sampler2D uEmi;
#else
flat varying int vPal;
#endif
varying vec3 vN; varying vec3 vNV; varying vec3 vW; varying vec3 vRest; varying vec3 vRestN; varying vec2 vUv; varying float vDepth;
#ifdef MRT
layout(location = 1) out highp vec4 gOut1;
// G-buffer: view normal xy, inverse view depth (planes are linear in screen space -> clean Laplacian edges), surface id
void writeG(float id) { vec3 n = normalize(vNV); n = gl_FrontFacing ? n : -n; gOut1 = vec4(n.xy * 0.5 + 0.5, 1.0 / max(vDepth, 1e-3), id); }
#endif
`;

// robot surface classes from the textures: white shell / dark parts / blue lights / visor / eyes / wordmark
export const ROBOT_CLASS = /* glsl */ `
struct RobotSurf { float white; float dark; float grey; float blue; float visor; float rim; float eye; float eyeSD; float logo; vec3 alb; };
RobotSurf robotSurf() {
  RobotSurf s;
  s.alb = texture2D(uMap, vUv).rgb;
  float fw = max(fwidth(vCls.x), 1e-3) * 0.8;
  float wv = smoothstep(0.5 - fw, 0.5 + fw, vCls.x);
  float fb = max(fwidth(vCls.y), 1e-3) * 0.8;
  s.blue = smoothstep(0.42 - fb, 0.42 + fb, vCls.y) * (1.0 - smoothstep(0.3, 0.8, vFace.z));
  // visor = geometric ellipse in rest space (front of the helmet) -> one clean visor outline in every style
  float ell = pow((vRest.x - 0.078) / 0.27, 2.0) + pow((vRest.y - 0.647) / 0.18, 2.0);
  float front = step(0.1, vRest.z) * step(0.0, vRestN.z);
  float fe = fwidth(ell) + 1e-4;
  s.visor = max(smoothstep(0.08, 0.3, vFace.z), (1.0 - smoothstep(1.2 - fe, 1.2 + fe, ell)) * front);
  s.eyeSD = vFace.z > 0.01 ? faceSD(vFace.xy) : 1e3;
  s.eye = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
  // the dark bezel just outside the glass reads as white shell (the scan texture is ragged there)
  float bez = (1.0 - smoothstep(1.55, 1.65, ell)) * front * (1.0 - s.visor);
  wv = max(wv, bez * (1.0 - s.blue));
  s.white = wv * (1.0 - s.blue) * (1.0 - s.visor);
  s.rim = 0.0;
  s.dark = (1.0 - s.white) * (1.0 - s.blue);
  s.grey = smoothstep(0.45, 0.55, vCls.z) * s.dark * (1.0 - s.visor);
  s.logo = logoMask(vRest, vRestN) * s.white;
  return s;
}
`;

// robot surface ids for the G-buffer (set ids = palette index + 1)
export const ROBOT_ID = /* glsl */ `
float robotId(RobotSurf s) {
  if (s.eye > 0.5) return 34.0;
  if (s.visor > 0.5) return 33.0;
  if (s.blue > 0.5) return 32.0;
  if (s.white > 0.5) return 30.0;
  return 31.0;
}
`;

// edge detection on the G-buffer (tG = gOut1). Returns edge strength 0..1. r = sample radius in px.
// k.x: relative inverse-depth Laplacian threshold (silhouettes, creases; near side only), k.y: normal threshold,
// k.z: id-change weight (material / region boundaries; drawn on the higher-id side only)
export const EDGES = /* glsl */ `
uniform sampler2D tG; uniform vec2 uTexel;
vec3 decN(vec2 e) { vec2 f = e * 2.0 - 1.0; return vec3(f, sqrt(max(0.0, 1.0 - dot(f, f)))); }
float edgeTerm(vec4 c, vec3 n, vec4 a, vec4 b, vec3 k, inout float ie) {
  float lap = (2.0 * c.z - a.z - b.z) / max(c.z, 1e-4);
  float de = smoothstep(k.x, k.x * 2.5, lap);
  float ne = 0.0;
  if (a.w > 0.5) ne = max(ne, 1.0 - dot(n, decN(a.xy)));
  if (b.w > 0.5) ne = max(ne, 1.0 - dot(n, decN(b.xy)));
  ne = smoothstep(k.y, k.y * 1.7, ne) * step(abs(a.z - b.z) / max(c.z, 1e-4), 0.25);
  ie = max(ie, max(step(0.5, c.w - a.w) * step(0.5, a.w), step(0.5, c.w - b.w) * step(0.5, b.w)) * step(c.w, 33.5));
  return max(de, ne);
}
float edgeG(vec2 uv, float r, vec3 k) {
  vec4 c = texture2D(tG, uv);
  if (c.w < 0.5) return 0.0;
  vec3 n = decN(c.xy);
  vec2 o = uTexel * r;
  float ie = 0.0, e = 0.0;
  e = max(e, edgeTerm(c, n, texture2D(tG, uv + vec2(o.x, 0.0)), texture2D(tG, uv - vec2(o.x, 0.0)), k, ie));
  e = max(e, edgeTerm(c, n, texture2D(tG, uv + vec2(0.0, o.y)), texture2D(tG, uv - vec2(0.0, o.y)), k, ie));
  e = max(e, 0.85 * edgeTerm(c, n, texture2D(tG, uv + o), texture2D(tG, uv - o), k, ie));
  e = max(e, 0.85 * edgeTerm(c, n, texture2D(tG, uv + vec2(o.x, -o.y)), texture2D(tG, uv + vec2(-o.x, o.y)), k, ie));
  return max(e, ie * k.z);
}
// background silhouette: background pixel next to geometry (for outer outlines that grow outward)
float silOut(vec2 uv, float r) {
  vec4 c = texture2D(tG, uv); if (c.w > 0.5) return 0.0;
  vec2 o = uTexel * r; float m = 0.0;
  m = max(m, texture2D(tG, uv + vec2(o.x, 0.0)).w); m = max(m, texture2D(tG, uv - vec2(o.x, 0.0)).w);
  m = max(m, texture2D(tG, uv + vec2(0.0, o.y)).w); m = max(m, texture2D(tG, uv - vec2(0.0, o.y)).w);
  return step(0.5, m);
}
`;

// separable gaussian blur pass (9 taps), dir in texels
export const BLUR9 = /* glsl */ `
uniform sampler2D tSrc; uniform vec2 uDir; varying vec2 vUv;
void main() {
  vec4 s = texture2D(tSrc, vUv) * 0.2270270270;
  s += (texture2D(tSrc, vUv + uDir * 1.3846153846) + texture2D(tSrc, vUv - uDir * 1.3846153846)) * 0.3162162162;
  s += (texture2D(tSrc, vUv + uDir * 3.2307692308) + texture2D(tSrc, vUv - uDir * 3.2307692308)) * 0.0702702703;
  gl_FragColor = s;
}`;
export class Blur {
  // blurs src (any size) into a w x h ping-pong pair; result in this.out.texture
  constructor(w, h, type) {
    this.a = makeRT(w, h, { depth: false, type }); this.b = makeRT(w, h, { depth: false, type });
    this.p = new Pass(BLUR9, { tSrc: { value: null }, uDir: { value: new THREE.Vector2() } });
    this.w = w; this.h = h; this.out = this.b;
  }
  run(renderer, src, radius = 1, iters = 1) {
    let s = src;
    for (let i = 0; i < iters; i++) {
      this.p.u.tSrc.value = s; this.p.u.uDir.value.set(radius / this.w, 0); this.p.render(renderer, this.a);
      this.p.u.tSrc.value = this.a.texture; this.p.u.uDir.value.set(0, radius / this.h); this.p.render(renderer, this.b);
      s = this.b.texture;
    }
    return this.b.texture;
  }
}

// ------------------------------------------------------------------ full-screen pass
const FSQ_GEO = new THREE.BufferGeometry();
FSQ_GEO.setAttribute('position', new THREE.Float32BufferAttribute([-1, 3, 0, -1, -1, 0, 3, -1, 0], 3));
FSQ_GEO.setAttribute('uv', new THREE.Float32BufferAttribute([0, 2, 0, 0, 2, 0], 2));
const FSQ_CAM = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
export const FSQ_VERT = /* glsl */ `varying vec2 vUv; void main() { vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }`;
export class Pass {
  constructor(frag, uniforms = {}, opts = {}) {
    this.material = new THREE.ShaderMaterial({ vertexShader: FSQ_VERT, fragmentShader: NOISE + frag, uniforms, depthTest: false, depthWrite: false, ...opts });
    this.mesh = new THREE.Mesh(FSQ_GEO, this.material); this.mesh.frustumCulled = false;
    this.u = this.material.uniforms;
  }
  render(renderer, target) { renderer.setRenderTarget(target || null); renderer.render(this.mesh, FSQ_CAM); }
}

export function makeRT(w, h, opts = {}) {
  const rt = new THREE.WebGLRenderTarget(w, h, {
    type: opts.type ?? THREE.HalfFloatType, format: THREE.RGBAFormat, depthBuffer: opts.depth !== false,
    samples: opts.samples || 0, count: opts.count || 1, minFilter: opts.nearest ? THREE.NearestFilter : THREE.LinearFilter,
    magFilter: opts.nearest ? THREE.NearestFilter : THREE.LinearFilter, generateMipmaps: false,
  });
  if (opts.depthTexture) { rt.depthTexture = new THREE.DepthTexture(w, h); rt.depthTexture.type = THREE.UnsignedIntType; }
  for (const t of rt.textures) { t.minFilter = rt.texture.minFilter; t.magFilter = rt.texture.magFilter; t.generateMipmaps = false; }
  return rt;
}

// custom style material: shared vertex shader + style fragment (fragment gets NOISE, FACE, LOGO, ROBOT_CLASS when robot)
export function styleMat({ robot, frag, uniforms = {}, defines = {}, shared, side = THREE.FrontSide, extra = '', rawNormals = false, blob = false }) {
  const d = { ...defines }; if (robot) { d.ROBOT = ''; if (!rawNormals) d.SMOOTHN = ''; if (blob) d.BLOBN = ''; }
  const u = { ...uniforms };
  if (robot && shared) Object.assign(u, shared.faceU, { uMap: shared.map, uEmi: shared.emi, uLogo: shared.logo });
  const fs = NOISE + (robot ? FACE + LOGO : '') + FRAG_HEAD + (robot ? ROBOT_CLASS : '') + extra + frag;
  return new THREE.ShaderMaterial({ vertexShader: VERT, fragmentShader: fs, uniforms: u, defines: d, side });
}
