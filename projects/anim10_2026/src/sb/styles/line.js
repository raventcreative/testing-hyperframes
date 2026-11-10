// MINIMAL LINE: black background, thin white contour lines only (silhouettes + main creases + region boundaries),
// no fills. Robot lines bright, set lines dimmer; eyes as small solid glows; a single cyan accent on the robot's
// light strip; perspective dot grid on the floor. Edges supersampled (4 sub-pixel taps) for clean thin lines.
import * as THREE from 'three';
import { Pass, EDGES } from '../common.js';
import { gInfoScene, makeGTarget } from '../ginfo.js';

const FRAG = /* glsl */ `
uniform sampler2D tI; uniform vec2 uRes; varying vec2 vUv;
void main() {
  vec3 K = vec3(0.02, 0.3, 1.0);
  float e = 0.0;
  e += edgeG(vUv + vec2(-0.45, -0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(0.45, -0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(-0.45, 0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(0.45, 0.45) * uTexel, 1.0, K);
  e = min(1.0, e * 0.4);
  vec4 g = texture2D(tG, vUv); vec4 inf = texture2D(tI, vUv);
  float robot = step(29.5, g.w);
  float setDim = 0.42 - 0.18 * smoothstep(0.18, 0.12, g.z);   // far set lines fade a little
  vec3 lc = mix(vec3(setDim), vec3(0.97), robot);
  float bl = smoothstep(0.2, 0.8, texture2D(tI, vUv + vec2(0.0, 1.5) * uTexel).b) * robot;
  lc = mix(lc, vec3(0.4, 0.86, 1.0), bl);
  vec3 col = lc * e;
  col += vec3(0.97) * smoothstep(0.35, 0.75, inf.g) * robot;
  col += vec3(0.9) * smoothstep(0.4, 0.75, inf.a) * robot * 0.85;
  float floorM = step(0.5, g.w) * step(g.w, 1.5);
  col += vec3(0.5) * inf.b * floorM * smoothstep(0.08, 0.2, g.z);
  gl_FragColor = vec4(col, 1.0);
}`;

export default function createLine(ctx) {
  const { W, H } = ctx;
  const gs = gInfoScene(ctx, { smooth: true, hideCity: true, simpleIds: true });
  const rtG = makeGTarget(W, H);
  const pass = new Pass(EDGES + FRAG, { tG: { value: rtG.textures[1] }, tI: { value: rtG.textures[0] }, uTexel: { value: new THREE.Vector2(1 / W, 1 / H) }, uRes: { value: new THREE.Vector2(W, H) } });
  return {
    render(target) { gs.render(rtG); pass.render(ctx.renderer, target); },
  };
}
