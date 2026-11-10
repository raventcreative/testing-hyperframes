// FLAT VECTOR: solid fills, 2 tones per surface (lit / shade, hard terminator), crisp anti-aliased edges, no textures.
// Evening office palette (indigo wall, coral desk, teal / mustard accents), flat moon + stars in the window,
// window-light patch and a round rug on the floor, flat ellipse cast shadow under the hovering robot.
import * as THREE from 'three';
import { styleMat, makeRT, Pass, sc } from '../common.js';
import { PAL, NPAL, LAYOUT } from '../set.js';

const P = (o) => { const a = new Array(NPAL).fill(0x888888); for (const [k, v] of Object.entries(o)) a[PAL[k]] = v; return a.map(sc); };
const LIT = P({ floor: 0x2a3566, wall: 0x34437a, trim: 0x2a3566, deskTop: 0xf08a5d, deskBody: 0xd0694a, monitor: 0x1c2140, screen: 0x2c3e7a,
  bar1: 0x4fd1c5, bar2: 0xffc857, bar3: 0xf26d6d, bar4: 0x7fe3ff, board: 0xf3efe6, boardFrame: 0x5b6aa3, leaf: 0x3fbf8a, pot: 0xf2c14e,
  winFrame: 0xe9e4f2, sky: 0x1a2350, city: 0x10163a, clock: 0xf08a5d, clockHand: 0x1c2140, keyboard: 0xdfe3f0, mug: 0xffc857, axis: 0x2b2f4a, soil: 0x3a2a2a });
const SHD = P({ floor: 0x222c58, wall: 0x2b386b, trim: 0x222c58, deskTop: 0xc96a4a, deskBody: 0xa8503d, monitor: 0x141831, screen: 0x223267,
  bar1: 0x35a89f, bar2: 0xd9a23e, bar3: 0xc65058, bar4: 0x5fb9dc, board: 0xc9c5d6, boardFrame: 0x45528a, leaf: 0x2b9470, pot: 0xc99a35,
  winFrame: 0xb9b3d1, sky: 0x1a2350, city: 0x10163a, clock: 0xc96a4a, clockHand: 0x141831, keyboard: 0xaeb3cc, mug: 0xd9a23e, axis: 0x2b2f4a, soil: 0x2a1e1e });

const COMMON = /* glsl */ `
uniform vec3 uL;
float toon(vec3 n, float th) { float d = dot(normalize(n), uL); float w = fwidth(d) * 1.2 + 1e-4; return smoothstep(th - w, th + w, d); }
`;

export default function createFlat(ctx) {
  const { W, H } = ctx;
  const uL = { value: new THREE.Vector3(-0.75, 0.55, 0.42).normalize() };
  const uShadow = { value: new THREE.Vector4(0, 0, 0.35, 0.18) };
  const robotMat = styleMat({ robot: true, blob: true, shared: ctx.rig.shared, uniforms: { uL }, extra: COMMON, frag: /* glsl */ `
    void main() {
      RobotSurf s = robotSurf();
      float lit = toon(vN, 0.05);
      vec3 white = mix(vec3(0.70, 0.74, 0.88), vec3(0.97, 0.96, 0.94), lit);
      vec3 dark = mix(vec3(0.075, 0.08, 0.16), vec3(0.16, 0.18, 0.31), lit);
      vec3 blue = vec3(0.30, 0.78, 1.0);
      vec3 c = white * s.white + dark * s.dark + blue * s.blue;
      // visor: deep navy with one flat highlight band (classic vector gloss)
      vec3 vis = vec3(0.075, 0.08, 0.16);
      float gl = smoothstep(0.35, 0.37, vFace.y * 0.55 + vFace.x * -0.25) * (1.0 - smoothstep(0.62, 0.64, vFace.y * 0.55 + vFace.x * -0.25));
      vis = mix(vis, vec3(0.15, 0.17, 0.30), gl * 0.8);
      c = mix(c, vis, s.visor);
      float ew = fwidth(s.eyeSD) * 1.0 + 1e-4;
      float eye = (1.0 - smoothstep(-ew, ew, s.eyeSD)) * smoothstep(0.2, 0.6, vFace.z);
      c = mix(c, vec3(0.86, 0.97, 1.0), eye);
      float lw = 0.5;
      c = mix(c, vec3(0.11, 0.12, 0.24), smoothstep(0.35, 0.6, s.logo));
      gl_FragColor = vec4(c, 1.0);
    }` });
  const setMat = styleMat({ robot: false, uniforms: { uL, uPal: { value: LIT }, uShd: { value: SHD }, uShadow }, extra: COMMON + /* glsl */ `
    uniform vec3 uPal[${NPAL}]; uniform vec3 uShd[${NPAL}]; uniform vec4 uShadow;`, frag: /* glsl */ `
    float aaStep(float e, float x) { float w = fwidth(x) + 1e-5; return smoothstep(e - w, e + w, x); }
    void main() {
      int p = vPal;
      float lit = toon(vN, 0.12);
      vec3 c = mix(uShd[p], uPal[p], lit);
      if (p == ${PAL.floor}) {
        // round rug under the robot + window light patch + flat ellipse shadow
        vec2 q = (vW.xz - vec2(0.0, 0.08)) / vec2(0.78, 0.5);
        float rug = 1.0 - aaStep(1.0, length(q));
        float rug2 = 1.0 - aaStep(0.78, length(q));
        c = mix(c, vec3(0.86, 0.42, 0.40), rug); c = mix(c, vec3(0.93, 0.52, 0.47), rug2);
        // light through the window: trace back to the wall plane along the light direction
        vec3 ld = normalize(vec3(-0.5, 0.62, -0.6));
        float tt = (${LAYOUT.wallZ.toFixed(3)} - vW.z) / ld.z; vec3 hp = vW + ld * tt;
        float inW = aaStep(${LAYOUT.win.x0.toFixed(3)}, hp.x) * (1.0 - aaStep(${LAYOUT.win.x1.toFixed(3)}, hp.x)) * aaStep(${LAYOUT.win.y0.toFixed(3)}, hp.y) * (1.0 - aaStep(${LAYOUT.win.y1.toFixed(3)}, hp.y));
        c = mix(c, c + vec3(0.035, 0.035, 0.05), inW);
        vec2 sq = (vW.xz - uShadow.xy) / vec2(uShadow.z, uShadow.w);
        c = mix(c, c * vec3(0.62, 0.62, 0.78), 1.0 - aaStep(1.0, length(sq)));
      } else if (p == ${PAL.sky}) {
        // flat night sky: two bands, a moon and a few stars
        float b = aaStep(1.18, vW.y); c = mix(vec3(0.20, 0.24, 0.50), vec3(0.14, 0.17, 0.40), b);
        vec2 mp = vW.xy - vec2(${(LAYOUT.win.x0 + 0.33).toFixed(3)} - 0.15, 1.58);
        c = mix(c, vec3(1.0, 0.93, 0.74), 1.0 - aaStep(0.09, length(mp)));
        c = mix(c, vec3(0.14, 0.17, 0.40), (1.0 - aaStep(0.085, length(mp - vec2(0.045, 0.03)))) * (1.0 - aaStep(0.09, length(mp))) * 0.0);
        vec2 g = floor(vW.xy * 9.0); float st = step(0.93, h12(g));
        vec2 f = fract(vW.xy * 9.0) - 0.5 - (h22(g) - 0.5) * 0.6;
        c = mix(c, vec3(0.95, 0.95, 1.0), st * (1.0 - aaStep(0.06, length(f))) * b);
      } else if (p == ${PAL.city}) {
        // lit windows on the skyline
        vec2 g = floor(vec2(vW.x * 40.0, vW.y * 30.0)); vec2 f = fract(vec2(vW.x * 40.0, vW.y * 30.0));
        float win = step(0.55, h12(g)) * step(0.3, f.x) * step(f.x, 0.7) * step(0.3, f.y) * step(f.y, 0.75);
        c = mix(c, vec3(1.0, 0.82, 0.45), win * 0.85);
      } else if (p == ${PAL.screen}) {
        c = vec3(0.16, 0.22, 0.45);
      }
      gl_FragColor = vec4(c, 1.0);
    }` });
  const scene = new THREE.Scene();
  scene.background = sc(0x34437a);
  const robot = ctx.robotMesh(robotMat); scene.add(robot);
  scene.add(new THREE.Mesh(ctx.setGeo.sharp, setMat));
  const rt = makeRT(W, H, { samples: 4, type: THREE.UnsignedByteType });
  const out = new Pass(/* glsl */ `uniform sampler2D tSrc; varying vec2 vUv; void main() { gl_FragColor = vec4(texture2D(tSrc, vUv).rgb, 1.0); }`, { tSrc: { value: rt.texture } });
  return {
    render(target) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      const rr = ctx.rig.rigRoot; uShadow.value.set(rr.position.x, rr.position.z + 0.02, 0.34 * rr.scale.x, 0.17 * rr.scale.x);
      r.setRenderTarget(rt); r.clear(); r.render(scene, ctx.camera);
      out.render(r, target);
    },
  };
}
