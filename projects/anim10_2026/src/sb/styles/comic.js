// COMIC: 3-tone cel shading with flat print colours, halftone (Ben-Day) dots in the shadow tones, glossy ink highlights,
// bold black ink outlines (thick outer silhouettes, thinner inner lines), Ben-Day dot wall, inside a panel with a thick
// border and a white page gutter. The upper part of the panel stays calm for a speech bubble added later in HTML.
import * as THREE from 'three';
import { styleMat, makeRT, Pass, EDGES, ROBOT_ID, sc } from '../common.js';
import { PAL, NPAL } from '../set.js';

const P = (o) => { const a = new Array(NPAL).fill(0x888888); for (const [k, v] of Object.entries(o)) a[PAL[k]] = v; return a.map(sc); };
const BASE = P({ floor: 0xffd23f, wall: 0x8fd6f5, trim: 0xffffff, deskTop: 0xe8433a, deskBody: 0xf4f1e8, monitor: 0x2b2b3a, screen: 0x1f8bd6,
  bar1: 0x2ec27e, bar2: 0xffd23f, bar3: 0xe8433a, bar4: 0x2a7de1, board: 0xffffff, boardFrame: 0x3a62c9, leaf: 0x37b34a, pot: 0xe8433a,
  winFrame: 0xffffff, sky: 0xbfeaff, city: 0x6cb5e0, clock: 0xffffff, clockHand: 0x111111, keyboard: 0xf4f1e8, mug: 0xffffff, axis: 0x111111, soil: 0x5a3b22 });

const SHADE = /* glsl */ `
uniform vec3 uL; uniform float uDot;
// halftone: rotated dot grid in screen space, dot radius grows with darkness k (0..1)
float halftone(float k, float ang, float cell) {
  vec2 p = gl_FragCoord.xy; float c = cos(ang), s = sin(ang);
  vec2 q = mat2(c, -s, s, c) * p / cell; vec2 f = fract(q) - 0.5;
  float r = sqrt(clamp(k, 0.0, 1.0)) * 0.62;
  float d = length(f); float w = 0.7 / cell;
  return 1.0 - smoothstep(r - w, r + w, d);
}
// 3 tones: 1 = light, 0.5 = mid, 0 = shadow
float tone3(vec3 n) { float d = dot(normalize(n), uL); float w = fwidth(d) + 1e-4; return 0.5 * smoothstep(-0.12 - w, -0.12 + w, d) + 0.5 * smoothstep(0.45 - w, 0.45 + w, d); }
`;

export default function createComic(ctx) {
  const { W, H } = ctx;
  const uL = { value: new THREE.Vector3(-0.55, 0.7, 0.48).normalize() };
  const robotMat = styleMat({ robot: true, blob: true, shared: ctx.rig.shared, defines: { MRT: '' }, uniforms: { uL }, extra: SHADE + ROBOT_ID, frag: /* glsl */ `
    void main() {
      RobotSurf s = robotSurf();
      float t = tone3(vN);
      vec3 V = normalize(cameraPosition - vW);
      float spec = pow(max(dot(reflect(-uL, normalize(vN)), V), 0.0), 24.0);
      // white shell: paper white / light blue-grey dots / blue-grey shadow
      vec3 wL = vec3(1.0, 0.99, 0.95), wM = vec3(0.70, 0.80, 0.93), wS = vec3(0.50, 0.60, 0.80);
      vec3 white = t > 0.75 ? wL : (t > 0.25 ? mix(wL, wM, halftone(0.55, 0.785, 6.0)) : mix(wM, wS, halftone(0.5, 0.785, 6.0)));
      // dark parts: ink black with a blue rim highlight
      vec3 dark = t > 0.75 ? vec3(0.17, 0.19, 0.28) : vec3(0.07, 0.07, 0.10);
      vec3 blue = vec3(0.15, 0.80, 1.0);
      vec3 c = white * s.white + dark * s.dark + blue * s.blue;
      // visor: ink black with a crisp white gloss streak
      float gx = vFace.x * 0.42 + vFace.y * 0.9;
      float gl = smoothstep(1.02, 1.06, gx) * (1.0 - smoothstep(1.32, 1.36, gx)) * step(-0.2, vFace.x * -1.0 + 0.4);
      vec3 vis = mix(vec3(0.06, 0.06, 0.09), vec3(0.95), gl * s.visor * smoothstep(0.5, 0.9, vFace.z));
      c = mix(c, vis, s.visor);
      float ew = fwidth(s.eyeSD) + 1e-4;
      float eye = (1.0 - smoothstep(-ew, ew, s.eyeSD)) * smoothstep(0.2, 0.6, vFace.z);
      c = mix(c, vec3(0.80, 0.97, 1.0), eye);
      c = mix(c, vec3(0.08, 0.08, 0.12), smoothstep(0.35, 0.6, s.logo));
      // glossy highlight shapes on the white shell (cut hard, comic style)
      c = mix(c, vec3(1.0), step(0.55, spec) * s.white);
      gl_FragColor = vec4(c, 1.0);
      writeG(robotId(s));
    }` });
  const setMat = styleMat({ robot: false, defines: { MRT: '' }, uniforms: { uL, uPal: { value: BASE } }, extra: SHADE + `uniform vec3 uPal[${NPAL}];\n`, frag: /* glsl */ `
    void main() {
      int p = vPal; vec3 b = uPal[p];
      float t = tone3(vN);
      vec3 shd = b * vec3(0.62, 0.66, 0.85);
      vec3 c = t > 0.75 ? b : (t > 0.25 ? mix(b, shd, halftone(0.45, 0.785, 6.0)) : shd);
      if (p == ${PAL.wall}) {
        // Ben-Day dots on the wall, denser towards the top
        float k = 0.25 + 0.25 * smoothstep(0.6, 2.4, vW.y);
        c = mix(c, vec3(0.38, 0.69, 0.92), halftone(k, 0.26, 9.0));
      } else if (p == ${PAL.floor}) {
        // floor planks: ink lines across, dots in the back
        float pl = abs(fract(vW.x / 0.32) - 0.5);
        c = mix(c, vec3(0.80, 0.55, 0.12), smoothstep(0.47, 0.49, pl));
        c = mix(c, vec3(0.92, 0.62, 0.15), halftone(0.18, 0.785, 7.0) * smoothstep(-0.2, -1.2, vW.z));
      } else if (p == ${PAL.sky}) {
        c = mix(vec3(0.75, 0.92, 1.0), vec3(0.55, 0.82, 0.98), halftone(0.35, 0.3, 7.0));
      } else if (p == ${PAL.screen}) {
        c = mix(vec3(0.14, 0.55, 0.85), vec3(0.08, 0.4, 0.7), halftone(0.4, 0.785, 5.0));
      }
      gl_FragColor = vec4(c, 1.0);
      writeG(float(p) + 1.0);
    }` });
  const scene = new THREE.Scene();
  const robot = ctx.robotMesh(robotMat); scene.add(robot);
  scene.add(new THREE.Mesh(ctx.setGeo.sharp, setMat));
  const rt = makeRT(W, H, { count: 2, type: THREE.HalfFloatType });
  const ink = new Pass(EDGES + /* glsl */ `
    uniform sampler2D tC; uniform vec2 uRes; varying vec2 vUv;
    void main() {
      vec3 K = vec3(0.025, 0.38, 1.0);
      float e = 0.0;
      e = max(e, edgeG(vUv, 1.6, K));
      e = max(e, edgeG(vUv + vec2(0.8, 0.8) * uTexel, 1.6, K));
      e = max(e, edgeG(vUv - vec2(0.8, 0.8) * uTexel, 1.6, K));
      // thick outer silhouettes: depth-only edges, wider radius
      vec3 KS = vec3(0.06, 9.0, 0.0);
      float es = max(edgeG(vUv, 3.2, KS), edgeG(vUv + vec2(1.5, -1.0) * uTexel, 3.2, KS));
      e = max(e, es);
      vec3 col = texture2D(tC, vUv).rgb;
      col = mix(col, vec3(0.05, 0.05, 0.07), clamp(e, 0.0, 1.0));
      // panel: white page gutter + thick ink border (slightly rough, like a brush-inked frame)
      vec2 p = vUv * uRes;
      float gut = 16.0, bw = 7.0;
      vec2 dd = min(p, uRes - p);
      float m = min(dd.x, dd.y) + (vnoise(p * 0.08) - 0.5) * 0.9;
      vec3 paper = vec3(0.985, 0.975, 0.95);
      col = m < gut ? paper : (m < gut + bw ? vec3(0.05, 0.05, 0.07) : col);
      // paper tooth
      col *= 0.985 + 0.03 * h12(floor(p * 0.5));
      gl_FragColor = vec4(col, 1.0);
    }`, { tG: { value: rt.textures[1] }, tC: { value: rt.textures[0] }, uTexel: { value: new THREE.Vector2(1 / W, 1 / H) }, uRes: { value: new THREE.Vector2(W, H) } });
  return {
    render(target) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      r.setRenderTarget(rt); r.setClearColor(new THREE.Color(0.5, 0.5, 0.0), 0.0); r.clear(); r.render(scene, ctx.camera); r.setClearColor(0x000000, 1);
      ink.render(r, target);
    },
  };
}
