// CHALKBOARD: the scene drawn in chalk on a green slate. Chalk-textured wobbly lines (grain breaks, pressure),
// hatching in the shadows, pastel "side-of-the-chalk" rubbed fills (chart bars, plant, robot lights, white shell),
// solid chalk eyes, erased-chalk smudges and eraser swirls on the board, wooden frame with a chalk tray.
import * as THREE from 'three';
import { Pass, EDGES } from '../common.js';
import { gInfoScene, makeGTarget } from '../ginfo.js';
import { PAL } from '../set.js';

const FRAG = /* glsl */ `
uniform sampler2D tI; uniform vec2 uRes; uniform float uT; varying vec2 vUv;
vec2 wob(vec2 uv, float seed, float amp) {
  float b = floor(uT * 6.0) * 2.1 + seed;
  return (vec2(vnoise(uv * vec2(6.0, 8.0) + b), vnoise(uv * vec2(8.0, 5.0) + b + 9.7)) - 0.5) * amp * uTexel;
}
// chalk grain: fine tooth + streaks along a direction
float grain(vec2 p, float dens) {
  float n = vnoise(p * 0.9) * 0.55 + vnoise(p * 2.3 + 7.0) * 0.3 + h12(floor(p)) * 0.35;
  return smoothstep(1.0 - dens - 0.18, 1.0 - dens + 0.18, n);
}
vec3 pastel(float id) {
  if (abs(id - ${PAL.bar1 + 1}.0) < 0.5) return vec3(0.62, 0.90, 0.72);
  if (abs(id - ${PAL.bar2 + 1}.0) < 0.5) return vec3(1.0, 0.90, 0.55);
  if (abs(id - ${PAL.bar3 + 1}.0) < 0.5) return vec3(1.0, 0.68, 0.70);
  if (abs(id - ${PAL.bar4 + 1}.0) < 0.5) return vec3(0.62, 0.84, 1.0);
  if (abs(id - ${PAL.leaf + 1}.0) < 0.5) return vec3(0.60, 0.88, 0.58);
  if (abs(id - ${PAL.pot + 1}.0) < 0.5) return vec3(1.0, 0.72, 0.55);
  if (abs(id - ${PAL.deskTop + 1}.0) < 0.5) return vec3(0.95, 0.80, 0.60);
  return vec3(0.0);
}
void main() {
  vec2 px = vUv * uRes;
  // ---- board
  vec3 board = vec3(0.19, 0.33, 0.26);
  float sm = fbm(px * 0.004 + 3.0);
  board += vec3(0.05, 0.07, 0.06) * smoothstep(0.35, 0.85, sm);                      // erased-chalk haze
  float sw = abs(sin(length(px - vec2(uRes.x * 0.78, uRes.y * 0.82)) * 0.045 + fbm(px * 0.01) * 3.0));
  board += vec3(0.025, 0.035, 0.03) * smoothstep(0.85, 1.0, sw) * smoothstep(0.4, 0.7, fbm(px * 0.006 + 11.0));   // eraser swirls
  board *= 0.96 + 0.06 * vnoise(px * 0.35);
  // ---- chalk drawing
  vec2 w1 = wob(vUv, 0.0, 4.0), w2 = wob(vUv, 23.0, 6.0);
  vec3 K = vec3(0.016, 0.32, 1.0);
  float e1 = max(max(edgeG(vUv + w1, 1.8, K), edgeG(vUv + w1 + vec2(1.1, 0.7) * uTexel, 1.8, K)), edgeG(vUv + w1 - vec2(0.6, 1.0) * uTexel, 1.8, K));
  float e2 = edgeG(vUv + w2 + vec2(-1.0, 1.2) * uTexel, 1.2, K);
  vec4 g = texture2D(tG, vUv + w1); vec4 inf = texture2D(tI, vUv + w1);
  float robot = step(29.5, g.w), has = step(0.5, g.w);
  float pr = 0.6 + 0.4 * vnoise(px * vec2(0.03, 0.035) + 5.0);
  float line = max(e1 * pr, e2 * 0.45) * grain(px, 0.78);
  vec3 chalkW = vec3(0.93, 0.95, 0.92);
  vec3 col = board;
  // rubbed pastel fills
  vec3 pc = pastel(g.w);
  // side-of-the-chalk rub: streaky (stretched noise along the stroke direction), never fully opaque
  vec2 rp = mat2(0.8, -0.6, 0.6, 0.8) * px;
  float rub = 0.45 + 0.35 * vnoise(rp * vec2(0.05, 0.9)) + 0.2 * vnoise(px * 0.6);
  float fillA = (pc.r + pc.g + pc.b > 0.1 ? 0.62 : 0.0) * smoothstep(0.3, 0.75, rub);
  col = mix(col, pc, fillA);
  // robot: faint white rub on the shell, pastel-blue lights, solid chalk eyes, chalk lettering
  float shell = robot * step(g.w, 30.5);
  col = mix(col, chalkW, 0.3 * shell * smoothstep(0.35, 0.8, rub));
  col = mix(col, vec3(0.55, 0.85, 1.0), smoothstep(0.3, 0.7, inf.b) * robot * grain(px + 9.0, 0.85));
  col = mix(col, vec3(0.88, 0.97, 1.0), smoothstep(0.3, 0.7, inf.g) * robot * grain(px + 1.0, 0.92));
  col = mix(col, chalkW, smoothstep(0.35, 0.7, inf.a) * robot * grain(px + 4.0, 0.85));
  // hatching in shadow (diagonal strokes, broken)
  float shade = (1.0 - inf.r) * has;
  vec2 hp = px + w1 / uTexel;
  float hl = abs(fract((hp.x + hp.y) / 7.0) - 0.5) * 2.0;
  float hatch = (1.0 - smoothstep(0.18, 0.42, hl)) * step(0.52, shade) * step(0.4, vnoise(hp * vec2(0.08, 0.02)));
  float hatch2 = (1.0 - smoothstep(0.18, 0.42, abs(fract((hp.x - hp.y) / 7.0) - 0.5) * 2.0)) * step(0.7, shade);
  col = mix(col, chalkW, max(hatch, hatch2) * 0.38 * grain(px * 1.3, 0.7) * (1.0 - step(32.5, g.w)));
  col = mix(col, chalkW, clamp(line, 0.0, 1.0) * 0.95);
  // dust halo around strokes
  col += vec3(0.03) * smoothstep(0.0, 1.0, max(e1, e2)) * (1.0 - grain(px, 0.78));
  // ---- wooden frame + chalk tray
  float fw = 22.0;
  vec2 dd = min(px, uRes - px); float m = min(dd.x, dd.y);
  float tray = step(px.y, 46.0);
  if (m < fw || tray > 0.5) {
    float along = (dd.x < dd.y) ? px.y : px.x;
    float across = min(dd.x, dd.y);
    vec3 wood = vec3(0.52, 0.32, 0.17);
    float gr = vnoise(vec2(along * 0.02, across * 0.6)) * 0.6 + vnoise(vec2(along * 0.08, across * 1.7)) * 0.4;
    wood *= 0.8 + 0.35 * gr;
    float bev = tray > 0.5 ? smoothstep(46.0, 30.0, px.y) * 0.25 + 0.0 : (across / fw);
    wood *= 0.75 + 0.35 * bev;
    if (tray > 0.5) {
      wood *= 0.85 + 0.2 * smoothstep(20.0, 40.0, px.y);
      // chalk sticks + eraser in the tray
      float y = px.y - 30.0;
      float stick1 = step(abs(y), 4.5) * step(abs(px.x - uRes.x * 0.62), 26.0);
      float stick2 = step(abs(y - 0.5), 4.0) * step(abs(px.x - uRes.x * 0.71), 15.0);
      float stick3 = step(abs(y), 4.0) * step(abs(px.x - uRes.x * 0.29), 19.0);
      float er = step(abs(y - 4.0), 10.0) * step(abs(px.x - uRes.x * 0.42), 46.0);
      wood = mix(wood, vec3(0.92, 0.91, 0.86) * (0.9 + 0.1 * vnoise(px)), stick1);
      wood = mix(wood, vec3(1.0, 0.86, 0.55), stick2);
      wood = mix(wood, vec3(0.98, 0.72, 0.76), stick3);
      wood = mix(wood, mix(vec3(0.28, 0.24, 0.2), vec3(0.85, 0.83, 0.78), step(y, 0.0)) * (0.9 + 0.1 * vnoise(px * 0.5)), er);
    }
    col = wood;
  }
  // inner shadow of the frame on the board
  col *= 1.0 - 0.35 * (1.0 - smoothstep(fw, fw + 14.0, m)) * step(fw, m) * (1.0 - tray);
  gl_FragColor = vec4(col, 1.0);
}`;

export default function createChalk(ctx) {
  const { W, H } = ctx;
  const gs = gInfoScene(ctx, { keyDir: [-0.55, 0.65, 0.5], smooth: true, hideCity: true });
  const rtG = makeGTarget(W, H);
  const pass = new Pass(EDGES + FRAG, { tG: { value: rtG.textures[1] }, tI: { value: rtG.textures[0] }, uTexel: { value: new THREE.Vector2(1 / W, 1 / H) },
    uRes: { value: new THREE.Vector2(W, H) }, uT: { value: 0 } });
  return {
    render(target) { gs.render(rtG); pass.u.uT.value = ctx.t; pass.render(ctx.renderer, target); },
  };
}
