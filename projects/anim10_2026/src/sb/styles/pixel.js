// PIXEL ART: the scene rendered at 1/8 resolution (~103x123) with a fixed 24-colour palette: 3-step colour ramps per
// material, ordered (Bayer 4x4) dithering only on the ramp transitions, 1-px dark outline on silhouettes, selective
// darker lines between objects, pixel floor planks / wallpaper / starry window. Upscaled nearest-neighbour x8.
// HUD (hearts, AI PRENEUR in a 3x5 bitmap font, XP bar, hotbar) drawn into a low-res overlay.
import * as THREE from 'three';
import { styleMat, makeRT, Pass, ROBOT_ID, sc } from '../common.js';
import { PAL } from '../set.js';

const SCALE = 8;
// palette (24): outline, darks, robot whites, blues, woods, purples, greens, accents
const C = {
  ink: 0x0c0a18, d1: 0x15172b, d2: 0x262a45, d3: 0x3b4064, w1: 0x8590b8, w2: 0xc3cbe8, w3: 0xf5f7ff,
  b1: 0x1a6b9c, b2: 0x22c7f0, b3: 0x8ff8ff, o1: 0x6b3d24, o2: 0x9b5d33, o3: 0xc7844a, p1: 0x2a1f54, p2: 0x3a2c70, p3: 0x4f3e94,
  g1: 0x1d5c2e, g2: 0x2e8f3e, g3: 0x5ad25a, r1: 0xa52a2a, r2: 0xe8433a, y2: 0xffd23f, y3: 0xfff1a8, sky: 0x1d1a3d,
};
const v3 = (h) => { const c = sc(h); return `vec3(${c.r.toFixed(4)}, ${c.g.toFixed(4)}, ${c.b.toFixed(4)})`; };
const RAMP = (a, b, c) => `ramp3(t, ${v3(C[a])}, ${v3(C[b])}, ${v3(C[c])})`;

const SHADE = /* glsl */ `
uniform vec3 uL;
float bayer4(vec2 p) { ivec2 i = ivec2(mod(p, 4.0)); int k = i.x + i.y * 4;
  float m[16] = float[16](0.0, 8.0, 2.0, 10.0, 12.0, 4.0, 14.0, 6.0, 3.0, 11.0, 1.0, 9.0, 15.0, 7.0, 13.0, 5.0); return (m[k] + 0.5) / 16.0; }
// light level -> ramp position 0..2 with ordered dither near the steps
float rampT(vec3 n, float bias, float dith) {
  float d = dot(normalize(n), uL) * 0.5 + 0.5 + bias;
  float t = clamp(d * 3.0 - 0.6, 0.0, 2.0);
  return floor(t + (bayer4(gl_FragCoord.xy) - 0.5) * dith + 0.5);
}
vec3 ramp3(float t, vec3 a, vec3 b, vec3 c) { return t < 0.5 ? a : (t < 1.5 ? b : c); }
`;

// 3x5 bitmap font (rows top->bottom, 3 bits each)
const FONT = { A: [2, 5, 7, 5, 5], I: [7, 2, 2, 2, 7], P: [6, 5, 6, 4, 4], R: [6, 5, 6, 5, 5], E: [7, 4, 6, 4, 7], N: [5, 7, 7, 7, 5], U: [5, 5, 5, 5, 7],
  L: [4, 4, 4, 4, 7], V: [5, 5, 5, 5, 2], X: [5, 5, 2, 5, 5], 0: [7, 5, 5, 5, 7], 1: [2, 6, 2, 2, 7], 2: [6, 1, 2, 4, 7], 3: [6, 1, 2, 1, 6], 4: [5, 5, 7, 1, 1],
  5: [7, 4, 6, 1, 6], 6: [3, 4, 7, 5, 7], 7: [7, 1, 2, 2, 2], 8: [7, 5, 7, 5, 7], 9: [7, 5, 7, 1, 6], ' ': [0, 0, 0, 0, 0], ':': [0, 2, 0, 2, 0] };

function hudTexture(w, h) {
  const d = new Uint8Array(w * h * 4);
  const put = (x, y, hex, a = 255) => { if (x < 0 || y < 0 || x >= w || y >= h) return; const i = 4 * ((h - 1 - y) * w + x); d[i] = (hex >> 16) & 255; d[i + 1] = (hex >> 8) & 255; d[i + 2] = hex & 255; d[i + 3] = a; };
  const rect = (x, y, rw, rh, hex) => { for (let j = 0; j < rh; j++) for (let i = 0; i < rw; i++) put(x + i, y + j, hex); };
  const text = (s, x, y, hex) => { for (const ch of s) { const g = FONT[ch] || FONT[' ']; g.forEach((row, j) => { for (let i = 0; i < 3; i++) if (row & (4 >> i)) put(x + i, y + j, hex); }); x += 4; } };
  // top bar
  rect(0, 0, w, 9, C.ink); rect(0, 9, w, 1, C.d2);
  const heart = [[0, 1, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]];
  for (let k = 0; k < 3; k++) heart.forEach((row, j) => row.forEach((v, i) => { if (v) put(2 + k * 8 + i, 2 + j, k < 2 ? (j === 1 && i === 1 ? C.y3 : C.r2) : C.d3); }));
  text('AI PRENEUR', w - 17 - 40, 2, C.w3);                               // right side: the round title covers the top-left
  rect(w - 15, 2, 13, 5, C.d2); rect(w - 14, 3, 8, 3, C.g3); rect(w - 14, 3, 8, 1, 0xa8f0a0);
  // (no bottom hotbar: the reel captions sit on the stage floor)
  const t = new THREE.DataTexture(d, w, h, THREE.RGBAFormat); t.magFilter = t.minFilter = THREE.NearestFilter; t.needsUpdate = true;
  return t;
}

export default function createPixel(ctx) {
  const { W, H } = ctx;
  const Wl = Math.ceil(W / SCALE), Hl = Math.ceil(H / SCALE);
  const uL = { value: new THREE.Vector3(-0.6, 0.7, 0.45).normalize() };
  const robotMat = styleMat({ robot: true, blob: true, shared: ctx.rig.shared, defines: { MRT: '' }, uniforms: { uL }, extra: SHADE + ROBOT_ID, frag: /* glsl */ `
    void main() {
      RobotSurf s = robotSurf();
      float t = rampT(vN, 0.05, 0.4);
      vec3 c = ${RAMP('w1', 'w2', 'w3')};
      if (s.white < 0.5) c = ${RAMP('d1', 'd2', 'd3')};
      if (vCls.y > 0.22 && s.visor < 0.5 && s.white < 0.5) c = t > 1.5 ? ${v3(C.b3)} : ${v3(C.b2)};
      if (s.visor > 0.5) {
        c = ${v3(C.d1)};
        float gx = vFace.x * 0.42 + vFace.y * 0.9;
        if (gx > 1.0 && gx < 1.3 && vFace.x < 0.6) c = ${v3(C.d3)};
      }
      // pixel eyes: the face shapes dilated so they survive at sprite resolution
      if (vFace.z > 0.3 && s.eyeSD < 0.16) c = ${v3(C.b3)};
      if (vFace.z > 0.3 && s.eyeSD < 0.02) c = ${v3(C.w3)};
      gl_FragColor = vec4(c, 1.0);
      writeG(robotId(s));
    }` });
  const setMat = styleMat({ robot: false, defines: { MRT: '' }, uniforms: { uL }, extra: SHADE, frag: /* glsl */ `
    void main() {
      int p = vPal; float t = rampT(vN, 0.0, 0.0);
      vec3 c = ${RAMP('d1', 'd2', 'd3')};
      if (p == ${PAL.floor}) {
        c = ${v3(C.o2)};
        float pl = fract(vW.x / 0.22 + floor(vW.z / 0.6) * 0.5);
        if (pl < 0.12) c = ${v3(C.o1)};
        if (fract(vW.z / 0.6) < 0.05) c = ${v3(C.o1)};
        if (pl > 0.5 && pl < 0.6 && fract(vW.z / 0.6) > 0.5) c = ${v3(C.o3)};
        if (length((vW.xz - vec2(0.0, 0.05)) / vec2(0.36, 0.2)) < 1.0) c = ${v3(C.o1)};
      }
      else if (p == ${PAL.wall}) { float st = fract(vW.x / 0.18); c = st < 0.5 ? ${v3(C.p2)} : ${v3(C.p3)}; if (st > 0.92) c = ${v3(C.p1)}; if (vW.y < 0.12) c = ${v3(C.p1)}; }
      else if (p == ${PAL.trim}) c = ${v3(C.p1)};
      else if (p == ${PAL.deskTop} || p == ${PAL.deskBody}) c = ${RAMP('o1', 'o2', 'o3')};
      else if (p == ${PAL.screen}) { c = ${v3(C.b1)}; }
      else if (p == ${PAL.bar1} || p == ${PAL.leaf}) c = t > 0.5 ? ${v3(C.g3)} : ${v3(C.g2)};
      else if (p == ${PAL.bar2} || p == ${PAL.mug}) c = ${v3(C.y2)};
      else if (p == ${PAL.bar3} || p == ${PAL.pot}) c = t > 0.5 ? ${v3(C.r2)} : ${v3(C.r1)};
      else if (p == ${PAL.bar4}) c = ${v3(C.b2)};
      else if (p == ${PAL.board} || p == ${PAL.clock} || p == ${PAL.keyboard}) c = ${RAMP('w1', 'w2', 'w3')};
      else if (p == ${PAL.winFrame}) c = ${RAMP('w1', 'w2', 'w3')};
      else if (p == ${PAL.sky}) { c = ${v3(C.sky)}; if (h12(floor(gl_FragCoord.xy)) > 0.97) c = ${v3(C.w2)}; if (length(vW.xy - vec2(-0.62, 1.55)) < 0.075) c = ${v3(C.y3)}; }
      else if (p == ${PAL.city}) { c = ${v3(C.p1)}; vec2 f = floor(gl_FragCoord.xy); if (mod(f.x, 2.0) < 1.0 && mod(f.y, 3.0) < 1.0 && h12(floor(f / vec2(2.0, 3.0))) > 0.45) c = ${v3(C.y2)}; }
      else if (p == ${PAL.axis} || p == ${PAL.clockHand}) c = ${v3(C.ink)};
      else if (p == ${PAL.soil}) c = ${v3(C.o1)};
      gl_FragColor = vec4(c, 1.0);
      writeG(float(p) + 1.0);
    }` });
  const scene = new THREE.Scene();
  const robot = ctx.robotMesh(robotMat); scene.add(robot);
  scene.add(new THREE.Mesh(ctx.setGeo.sharp, setMat));
  const rt = makeRT(Wl, Hl, { count: 2, type: THREE.HalfFloatType, nearest: true });
  const hud = hudTexture(Wl, Hl);
  const off = new THREE.Vector2(Math.floor((Wl * SCALE - W) / 2), Math.floor((Hl * SCALE - H) / 2));
  const up = new Pass(/* glsl */ `
    uniform sampler2D tC; uniform sampler2D tG; uniform sampler2D tH; uniform vec2 uOff; uniform vec2 uLow;
    varying vec2 vUv;
    vec4 G(ivec2 p) { return texelFetch(tG, clamp(p, ivec2(0), ivec2(uLow) - 1), 0); }
    void main() {
      ivec2 p = ivec2(floor((gl_FragCoord.xy + uOff) / ${SCALE}.0));
      vec3 c = texelFetch(tC, p, 0).rgb;
      vec4 g = G(p);
      // 1-px outline: this pixel is nearer than a neighbour by a clear margin, or borders the empty background
      float o = 0.0, sel = 0.0;
      ivec2 nb[4] = ivec2[4](ivec2(1, 0), ivec2(-1, 0), ivec2(0, 1), ivec2(0, -1));
      for (int k = 0; k < 4; k++) {
        vec4 q = G(p + nb[k]);
        if (g.w > 0.5 && (q.w < 0.5 || g.z > q.z * 1.12)) o = 1.0;
        else if (g.w > 29.5 && q.w > 0.5 && q.w < 29.5) o = 1.0;
        else if (g.w > 0.5 && abs(g.w - q.w) > 0.5 && g.w > q.w && g.w < 33.5 && q.w > 0.5) sel = 1.0;
      }
      if (sel > 0.5 && g.w > 1.5) c *= 0.62;
      if (o > 0.5) c = ${v3(C.ink)};
      vec4 h = texelFetch(tH, p, 0);
      c = mix(c, h.rgb, h.a);
      gl_FragColor = vec4(c, 1.0);
    }`, { tC: { value: rt.textures[0] }, tG: { value: rt.textures[1] }, tH: { value: hud }, uOff: { value: off }, uLow: { value: new THREE.Vector2(Wl, Hl) } });
  return {
    render(target) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      r.setRenderTarget(rt); r.setClearColor(new THREE.Color(0.5, 0.5, 0.0), 0.0); r.clear(); r.render(scene, ctx.camera); r.setClearColor(0x000000, 1);
      up.render(r, target);
    },
  };
}
