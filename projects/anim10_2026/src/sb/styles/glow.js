// GLOW SKETCH: a dark room drawn in glowing hand-sketched lines. Edges from the G-buffer (silhouettes, creases,
// region boundaries), drawn twice with different low-frequency wobble (sketchy double strokes, line boil at 8 fps),
// pressure variation along the strokes; warm gold for the set and the robot, cyan for its lights and eyes; bloom;
// a spotlight cone from above with a light pool and dust motes; hatch strokes in the pool shadow.
import * as THREE from 'three';
import { Pass, makeRT, Blur, EDGES } from '../common.js';
import { gInfoScene, makeGTarget } from '../ginfo.js';

const LINES = /* glsl */ `
uniform sampler2D tI; uniform float uT; varying vec2 vUv;
vec2 wob(vec2 uv, float seed, float amp) {
  float b = floor(uT * 8.0) * 1.37 + seed;
  return (vec2(vnoise(uv * vec2(7.0, 9.0) + b), vnoise(uv * vec2(9.0, 6.5) + b + 17.3)) - 0.5) * amp * uTexel;
}
void main() {
  vec2 w1 = wob(vUv, 0.0, 3.2), w2 = wob(vUv, 41.0, 5.0);
  vec3 K = vec3(0.012, 0.28, 1.0);
  float e1 = edgeG(vUv + w1, 1.2, K);
  float e2 = edgeG(vUv + w2 + vec2(0.7, -0.5) * uTexel, 1.0, K);
  vec4 g = texture2D(tG, vUv + w1); vec4 inf = texture2D(tI, vUv + w1);
  float robot = step(29.5, g.w);
  // pressure: strokes fade in and out along their length
  float pr = 0.55 + 0.45 * smoothstep(0.25, 0.7, vnoise(vUv * vec2(55.0, 61.0) + floor(uT * 8.0)));
  float e = max(e1 * pr, e2 * 0.5 * (1.0 - pr * 0.5));
  vec3 gold = vec3(1.0, 0.72, 0.34), cy = vec3(0.30, 0.86, 1.0);
  vec3 lc = mix(gold * 0.55, gold * 1.05, robot);
  lc = mix(lc, cy * 1.1, smoothstep(0.3, 0.7, inf.b) * robot);
  vec3 col = lc * e;
  // eyes + lights: filled glow; wordmark in thin gold
  col += cy * smoothstep(0.3, 0.7, inf.g) * robot * 1.25;
  col += cy * 0.35 * smoothstep(0.3, 0.7, inf.b) * robot;
  col += gold * 0.9 * smoothstep(0.35, 0.7, inf.a) * robot;
  // monitor screen faint glow
  col += vec3(0.35, 0.6, 0.9) * 0.10 * inf.g * (1.0 - robot);
  // hatch strokes on the floor around the light pool (shadow side)
  float floorM = step(0.5, g.w) * step(g.w, 1.5);
  vec2 hp = gl_FragCoord.xy + w1 / uTexel;
  float hatch = 1.0 - smoothstep(0.0, 0.22, abs(fract((hp.x * 0.55 - hp.y) / 8.0) - 0.5) * 2.0);
  float hz = smoothstep(0.02, 0.2, inf.a) * (1.0 - smoothstep(0.35, 0.6, inf.a)) * floorM;
  float brk = step(0.35, vnoise(vec2((hp.x * 0.55 - hp.y) / 8.0, hp.x * 0.04)));
  col += gold * 0.2 * hatch * hz * brk;
  gl_FragColor = vec4(col, 1.0);
}`;

const DOWN = /* glsl */ `uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv;
void main() { vec4 s = texture2D(tSrc, vUv + uTexel * vec2(-1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, 1.0)); gl_FragColor = s * 0.25; }`;

const COMP = /* glsl */ `
uniform sampler2D tL; uniform sampler2D tB1; uniform sampler2D tB2; uniform vec2 uRes; uniform float uT;
uniform vec2 uLamp; uniform vec2 uPoolC; uniform vec2 uPoolR; uniform float uLampW;
varying vec2 vUv;
void main() {
  vec2 p = vUv * uRes;
  vec3 lines = texture2D(tL, vUv).rgb;
  vec3 b1 = texture2D(tB1, vUv).rgb, b2 = texture2D(tB2, vUv).rgb;
  vec3 gold = vec3(1.0, 0.70, 0.33);
  // room: near black, warm
  vec3 col = vec3(0.026, 0.020, 0.016);
  // spotlight cone: from the lamp (above the frame) to the pool ellipse
  float t = (p.y - uLamp.y) / (uPoolC.y - uLamp.y);
  float hw = mix(uLampW, uPoolR.x * 0.98, clamp(t, 0.0, 1.0));
  float cx = mix(uLamp.x, uPoolC.x, t);
  float inC = (1.0 - smoothstep(hw * 0.78, hw, abs(p.x - cx))) * step(0.0, t) * (1.0 - smoothstep(0.92, 1.02, t));
  float coreC = 1.0 - smoothstep(0.0, hw * 0.75, abs(p.x - cx));
  col += gold * inC * (0.07 + 0.07 * coreC) * (0.55 + 0.45 * t);
  // cone edge strokes (sketched)
  float edgeL = exp(-abs(abs(p.x - cx) - hw) / 1.1) * step(0.0, t) * step(t, 0.97);
  col += gold * edgeL * 0.35 * (0.6 + 0.4 * vnoise(vec2(p.y * 0.05, 3.0)));
  // dust motes in the beam
  vec2 g = floor(p / 23.0); vec2 f = fract(p / 23.0) - 0.5 - (h22(g) - 0.5) * 0.7;
  col += gold * 0.5 * step(0.86, h12(g + 3.0)) * exp(-dot(f, f) * 900.0) * inC;
  // light pool on the floor
  vec2 q = (p - uPoolC) / uPoolR; float pool = 1.0 - smoothstep(0.55, 1.0, length(q));
  col += gold * pool * 0.10;
  col += lines + b1 * 0.85 + b2 * 0.45;
  // vignette + film-like grain (deterministic per frame)
  vec2 v = vUv - 0.5; col *= 1.0 - 0.55 * dot(v, v) * 2.0;
  col += (h12(p + floor(uT * 24.0) * 13.7) - 0.5) * 0.012;
  col = col / (1.0 + max(col - 0.85, 0.0));
  gl_FragColor = vec4(col, 1.0);
}`;

export default function createGlow(ctx) {
  const { W, H } = ctx;
  const gs = gInfoScene(ctx, { keyDir: [0.0, 1.0, 0.2], smooth: false, poolR: 0.95, hideCity: true });
  const rtG = makeGTarget(W, H);
  const texel = new THREE.Vector2(1 / W, 1 / H);
  const lines = new Pass(EDGES + LINES, { tG: { value: rtG.textures[1] }, tI: { value: rtG.textures[0] }, uTexel: { value: texel }, uT: { value: 0 } });
  const rtL = makeRT(W, H, { depth: false, type: THREE.HalfFloatType });
  const qw = Math.ceil(W / 4), qh = Math.ceil(H / 4);
  const rtQ = makeRT(qw, qh, { depth: false, type: THREE.HalfFloatType });
  const down = new Pass(DOWN, { tSrc: { value: rtL.texture }, uTexel: { value: texel } });
  const blurA = new Blur(qw, qh, THREE.HalfFloatType), blurB = new Blur(Math.ceil(qw / 2), Math.ceil(qh / 2), THREE.HalfFloatType);
  const comp = new Pass(COMP, { tL: { value: rtL.texture }, tB1: { value: null }, tB2: { value: null }, uRes: { value: new THREE.Vector2(W, H) }, uT: { value: 0 },
    uLamp: { value: new THREE.Vector2() }, uPoolC: { value: new THREE.Vector2() }, uPoolR: { value: new THREE.Vector2() }, uLampW: { value: 30 } });
  const v = new THREE.Vector3();
  const proj = (x, y, z) => { v.set(x, y, z).project(ctx.camera); return new THREE.Vector2((v.x * 0.5 + 0.5) * W, (v.y * 0.5 + 0.5) * H); };
  return {
    render(target) {
      const r = ctx.renderer, rr = ctx.rig.rigRoot;
      gs.render(rtG);
      lines.u.uT.value = ctx.t; lines.render(r, rtL);
      down.render(r, rtQ);
      comp.u.tB1.value = blurA.run(r, rtQ.texture, 1.0, 2);
      comp.u.tB2.value = blurB.run(r, blurA.out.texture, 2.0, 2);
      // spotlight geometry (screen space) from the robot's position
      const px = rr.position.x, pz = rr.position.z;
      const c = proj(px, 0, pz), a = proj(px - 0.62, 0, pz), b = proj(px + 0.62, 0, pz), f = proj(px, 0, pz + 0.62), k = proj(px, 0, pz - 0.62);
      comp.u.uPoolC.value.copy(c); comp.u.uPoolR.value.set(Math.abs(b.x - a.x) / 2, Math.abs(k.y - f.y) / 2);
      comp.u.uLamp.value.copy(proj(px, 2.4, pz)); comp.u.uLampW.value = 26;
      comp.u.uT.value = ctx.t; comp.render(r, target);
    },
  };
}
