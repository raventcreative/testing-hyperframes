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
#endif
`;

// robot surface classes from the textures: white shell / dark parts / blue lights / visor / eyes / wordmark
export const ROBOT_CLASS = /* glsl */ `
struct RobotSurf { float white; float dark; float grey; float blue; float visor; float eye; float eyeSD; float logo; vec3 alb; };
RobotSurf robotSurf() {
  RobotSurf s;
  s.alb = texture2D(uMap, vUv).rgb;
  float fw = max(fwidth(vCls.x), 1e-3) * 0.8;
  float wv = smoothstep(0.5 - fw, 0.5 + fw, vCls.x);
  float fb = max(fwidth(vCls.y), 1e-3) * 0.8;
  s.blue = smoothstep(0.42 - fb, 0.42 + fb, vCls.y) * (1.0 - smoothstep(0.3, 0.8, vFace.z));
  s.visor = smoothstep(0.08, 0.3, vFace.z);
  s.eyeSD = vFace.z > 0.01 ? faceSD(vFace.xy) : 1e3;
  s.eye = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
  s.white = wv * (1.0 - s.blue) * (1.0 - s.visor);
  s.dark = (1.0 - s.white) * (1.0 - s.blue);
  s.grey = smoothstep(0.45, 0.55, vCls.z) * s.dark * (1.0 - s.visor);
  s.logo = logoMask(vRest, vRestN) * s.white;
  return s;
}
`;

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
