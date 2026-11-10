// Signature transition: the scene "re-renders" from style A into style B behind a travelling scan line.
// Passed side = B, the rest = A. On the boundary: a hot white core + cyan (#01CCF7) glow, a fringe of render buckets
// (tiles of B popping in just ahead of the line, outlined in cyan), a short trail of scan rasters and chroma split
// behind it, and a few sparks riding the line. Deterministic (hash noise only; u and the angle fully define the frame).
import * as THREE from 'three';
import { Pass } from './common.js';

const FRAG = /* glsl */ `
uniform sampler2D tA; uniform sampler2D tB; uniform vec2 uRes; uniform float uU; uniform vec2 uDir;
varying vec2 vUv;
vec3 sampleB(vec2 uv) { return texture2D(tB, uv).rgb; }
void main() {
  vec2 px = vUv * uRes; vec2 c = uRes * 0.5;
  float smax = 0.5 * (abs(uRes.x * uDir.x) + abs(uRes.y * uDir.y));
  float margin = 90.0;
  float pos = mix(-smax - margin, smax + margin, uU);
  float s = dot(px - c, uDir);
  float d = s - pos;                                   // < 0: already passed (style B)
  vec2 tng = vec2(-uDir.y, uDir.x);
  float along = dot(px - c, tng);
  // render-bucket fringe just ahead of the line
  float tile = 14.0;
  vec2 tid = floor(px / tile); vec2 tf = fract(px / tile);
  float th = h12(tid + 7.0);
  vec2 tc = (tid + 0.5) * tile; float tdist = dot(tc - c, uDir) - pos;
  float fringe = 64.0;
  float tileOn = step(tdist, fringe * th * th) * step(0.0, tdist) * step(0.35, h12(tid * 1.7 + 3.0));
  float isB = max(step(d, 0.0), tileOn);
  // subtle heat shimmer along the line
  float sh = exp(-abs(d) / 26.0);
  vec2 off = uDir / uRes * (sin(along * 0.09 + uU * 31.0) * 2.5 * sh);
  vec3 a = texture2D(tA, vUv + off * 0.6).rgb;
  vec3 b;
  float trail = exp(max(d, -400.0) / 46.0) * step(d, 0.0);             // 1 at the line, fading into B
  vec2 ca = uDir / uRes * 3.0 * trail;
  b = vec3(texture2D(tB, vUv - ca + off).r, texture2D(tB, vUv + off).g, texture2D(tB, vUv + ca + off).b);
  // scan rasters behind the line (lines parallel to the boundary)
  float ras = 0.5 + 0.5 * cos(6.2831853 * d / 4.0);
  b *= 1.0 - 0.16 * trail * ras;
  b += vec3(0.004, 0.8, 0.97) * 0.10 * trail;
  vec3 col = mix(a, b, isB);
  // bucket outlines + tint in the fringe
  float edge = 1.0 - smoothstep(0.0, 0.09, min(min(tf.x, tf.y), min(1.0 - tf.x, 1.0 - tf.y)));
  float inFr = step(0.0, tdist) * step(tdist, fringe);
  col += vec3(0.004, 0.8, 0.97) * (edge * 0.55 * tileOn + 0.10 * tileOn) * (1.0 - tdist / fringe);
  // ahead of the line: faint cyan pre-scan haze on A
  col += vec3(0.004, 0.8, 0.97) * 0.07 * exp(-max(d, 0.0) / 70.0) * step(0.0, d);
  // the line: white-hot core + cyan glow (#01CCF7) + wide haze
  float ad = abs(d);
  float core = exp(-ad / 1.1);
  float glow = exp(-ad / 9.0);
  float haze = exp(-ad / 60.0);
  float flick = 0.85 + 0.15 * vnoise(vec2(along * 0.035, uU * 12.0));
  vec3 cy = vec3(0.004, 0.80, 0.969);
  col = col * (1.0 - 0.35 * glow) + cy * (glow * 0.95 + haze * 0.22) * flick + vec3(0.85, 1.0, 1.0) * core * 1.1;
  // sparks riding the line
  float cell = 34.0; float k = floor(along / cell); float hk = h12(vec2(k, 3.1));
  float sa = (k + 0.5 + (hk - 0.5) * 0.6) * cell; float sd = (h12(vec2(k, 9.7)) - 0.5) * 18.0 - 4.0;
  float spark = exp(-length(vec2(along - sa, d - sd)) / 1.6) * step(0.72, hk);
  col += vec3(0.7, 1.0, 1.0) * spark * 1.4;
  gl_FragColor = vec4(min(col, vec3(1.0)), 1.0);
}`;

export function createSweep(ctx) {
  const pass = new Pass(FRAG, {
    tA: { value: null }, tB: { value: null }, uRes: { value: new THREE.Vector2(ctx.W, ctx.H) }, uU: { value: 0 }, uDir: { value: new THREE.Vector2(1, 0) },
  });
  return {
    render(tA, tB, u, angleDeg, target) {
      const a = THREE.MathUtils.degToRad(angleDeg);
      pass.u.tA.value = tA; pass.u.tB.value = tB; pass.u.uU.value = u; pass.u.uDir.value.set(Math.cos(a), Math.sin(a));
      pass.render(ctx.renderer, target);
    },
  };
}
