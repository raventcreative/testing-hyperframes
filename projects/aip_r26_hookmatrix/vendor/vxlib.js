/* AIpreneur voxel kit (shared helpers from projects/aip_voxel_uji/vendor/vx.js): box merging with vertex colours, emissive
   materials, canvas textures, easing + keyframe interpolation, blinks, the voxel person and the AI robot builders, glow sprites. */
import * as THREE from "three";
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";
const FONT = "Poppins, sans-serif";
/* ---------------------------------------------------------------- helpers */
const MAT = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.78, metalness: 0 });
const ENVMAT = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.6, metalness: 0, emissive: 0x7d8aa3, emissiveIntensity: 0.55 });
export let seed = 7; export const setSeed = (v) => (seed = v); const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
function boxes(list, mat = MAT, shade = true) { // [cx, cy, cz, w, h, d, hex]
  const geos = list.map(([x, y, z, w, h, d, c]) => {
    const g = new THREE.BoxGeometry(w, h, d); g.translate(x, y, z);
    const col = new THREE.Color(c), n = g.attributes.position.count, a = new Float32Array(n * 3);
    const j = shade ? 1 + (rnd() - 0.5) * 0.05 : 1;
    for (let i = 0; i < n; i++) { a[i * 3] = col.r * j; a[i * 3 + 1] = col.g * j; a[i * 3 + 2] = col.b * j; }
    g.setAttribute("color", new THREE.BufferAttribute(a, 3)); return g;
  });
  const m = new THREE.Mesh(mergeGeometries(geos), mat); m.castShadow = true; m.receiveShadow = true; return m;
}
const emi = (hex, k = 1.6) => new THREE.MeshStandardMaterial({ color: 0x0b1640, emissive: new THREE.Color(hex), emissiveIntensity: k, roughness: 0.4 });
function ctexRaw(w, h, draw) { const c = document.createElement("canvas"); c.width = w; c.height = h; draw(c.getContext("2d"), w, h); return new THREE.CanvasTexture(c); }
function safeText(g, w, h) { // no cut text: shrink the font until the text's ends land inside the canvas (any transform)
  const orig = g.fillText.bind(g), pad = 8;
  g.fillText = (t, x, y, mw) => {
    const f0 = g.font, m0 = /(\d+(?:\.\d+)?)px/.exec(f0); if (!m0) return orig(t, x, y, mw);
    let px = parseFloat(m0[1]);
    const fits = () => { const m = g.measureText(t).width, al = g.textAlign, T = g.getTransform();
      const l = al === "center" ? x - m / 2 : al === "right" || al === "end" ? x - m : x, r = l + m;
      return [[l, y - px * 0.8], [r, y - px * 0.8], [l, y + px * 0.25], [r, y + px * 0.25]].every(([u, v]) => {
        const X = T.a * u + T.c * v + T.e, Y = T.b * u + T.d * v + T.f; return X >= pad && X <= w - pad && Y >= 0 && Y <= h; }); };
    while (!fits() && px > 10) { px -= 2; g.font = f0.replace(/(\d+(?:\.\d+)?)px/, px + "px"); }
    orig(t, x, y, mw); g.font = f0;
  };
}
function ctex(w, h, draw) {
  const c = document.createElement("canvas"); c.width = w; c.height = h; const g0 = c.getContext("2d"); safeText(g0, w, h); draw(g0, w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t;
}
function rr(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
const cl = (x, a, b) => Math.min(b, Math.max(a, x));
const EZ = {
  lin: (x) => x, io: (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2), out: (x) => 1 - Math.pow(1 - x, 3),
  in: (x) => x * x * x, sine: (x) => -(Math.cos(Math.PI * x) - 1) / 2,
  back: (x) => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); },
  expo: (x) => (x <= 0 ? 0 : x >= 1 ? 1 : x < 0.5 ? Math.pow(2, 20 * x - 10) / 2 : (2 - Math.pow(2, -20 * x + 10)) / 2),
};
const U = (t, a, b, e = "io") => EZ[e](cl((t - a) / (b - a), 0, 1));
function keys(t, K) { // [[time, [vals], ease]] — ease of the segment that ENDS at that key
  if (t <= K[0][0]) return K[0][1].slice();
  for (let i = 1; i < K.length; i++) if (t <= K[i][0]) {
    const [t0, a] = K[i - 1], [t1, b, e] = K[i], k = EZ[e || "io"]((t - t0) / (t1 - t0)); return a.map((v, j) => v + (b[j] - v) * k);
  }
  return K[K.length - 1][1].slice();
}
const blinkAt = (t, off = 0) => { let b = 1; for (let s = 1.1 + off; s < 120; s += 2.9 + ((s * 7) % 1.3)) { const d = t - s; if (d >= 0 && d < 0.16) b = Math.min(b, 0.12 + 0.88 * Math.abs(d - 0.08) / 0.08); } return b; };

function person(o) {
  const root = new THREE.Group();
  root.add(boxes([[-0.13, 0.3, 0, 0.22, 0.5, 0.26, o.pants], [0.13, 0.3, 0, 0.22, 0.5, 0.26, o.pants],
    [-0.13, 0.05, 0.03, 0.24, 0.1, 0.32, "#ffffff"], [0.13, 0.05, 0.03, 0.24, 0.1, 0.32, "#ffffff"]]));
  const torso = new THREE.Group(); torso.position.y = 0.55; root.add(torso);
  const tb = [[0, 0.31, 0, 0.62, 0.62, 0.36, o.top], [0, 0.13, 0.181, 0.42, 0.17, 0.01, o.top2]];
  if (o.strings) tb.push([-0.09, 0.47, 0.182, 0.03, 0.17, 0.01, "#ffffff"], [0.09, 0.47, 0.182, 0.03, 0.17, 0.01, "#ffffff"]);
  torso.add(boxes(tb));
  const arm = (s) => { const g = new THREE.Group(); g.position.set(s * 0.41, 0.57, 0);
    g.add(boxes([[0, -0.24, 0, 0.18, 0.5, 0.2, o.top], [0, -0.55, 0, 0.17, 0.14, 0.18, o.skin]])); torso.add(g); return g; };
  const armL = arm(-1), armR = arm(1);
  const head = new THREE.Group(); head.position.y = 0.62; torso.add(head);
  const hb = [[0, 0.43, 0, 0.86, 0.86, 0.86, o.skin], [-0.46, 0.42, 0, 0.07, 0.16, 0.14, o.skin], [0.46, 0.42, 0, 0.07, 0.16, 0.14, o.skin],
    [0, 0.93, 0, 0.94, 0.16, 0.94, o.hair], [0, 0.58, -0.45, 0.94, 0.74, 0.08, o.hair],
    [-0.465, 0.7, -0.06, 0.08, 0.4, 0.82, o.hair], [0.465, 0.7, -0.06, 0.08, 0.4, 0.82, o.hair],
    [-0.27, 0.27, 0.432, 0.12, 0.05, 0.01, "#ff9fae"], [0.27, 0.27, 0.432, 0.12, 0.05, 0.01, "#ff9fae"],
    [-0.17, o.glasses ? 0.63 : 0.6, 0.433, 0.15, 0.035, 0.01, o.hair], [0.17, o.glasses ? 0.63 : 0.6, 0.433, 0.15, 0.035, 0.01, o.hair]];
  o.fringe.forEach(([x, h]) => hb.push([x, 0.86 - h / 2, 0.445, 0.19, h, 0.07, o.hair]));
  if (o.bun) hb.push([0, 1.1, -0.18, 0.38, 0.26, 0.38, o.hair], [0, 0.25, -0.46, 0.9, 0.5, 0.1, o.hair]);
  if (o.glasses) for (const x of [-0.17, 0.17]) hb.push([x, 0.57, 0.437, 0.28, 0.03, 0.01, "#1b2238"], [x, 0.31, 0.437, 0.28, 0.03, 0.01, "#1b2238"],
    [x - 0.125, 0.44, 0.437, 0.03, 0.27, 0.01, "#1b2238"], [x + 0.125, 0.44, 0.437, 0.03, 0.27, 0.01, "#1b2238"]);
  if (o.glasses) hb.push([0, 0.49, 0.437, 0.1, 0.03, 0.01, "#1b2238"]);
  head.add(boxes(hb));
  const eye = (x) => { const m = boxes([[0, 0, 0, 0.1, 0.15, 0.02, "#1a1f36"], [0.025, 0.035, 0.012, 0.035, 0.045, 0.005, "#ffffff"]], MAT, false);
    m.position.set(x, 0.44, 0.432); head.add(m); return m; };
  const eyes = [eye(-0.17), eye(0.17)];
  const mk = (l) => { const m = boxes(l, MAT, false); m.visible = false; head.add(m); return m; };
  const R = "#8a3030";
  const mouth = { n: mk([[0, 0.22, 0.432, 0.15, 0.035, 0.01, R]]), o: mk([[0, 0.2, 0.432, 0.11, 0.11, 0.01, R], [0, 0.17, 0.433, 0.07, 0.04, 0.005, "#ff8f8f"]]),
    sad: mk([[0, 0.235, 0.432, 0.1, 0.035, 0.01, R], [-0.07, 0.207, 0.432, 0.045, 0.035, 0.01, R], [0.07, 0.207, 0.432, 0.045, 0.035, 0.01, R]]),
    smile: mk([[0, 0.205, 0.432, 0.11, 0.035, 0.01, R], [-0.075, 0.235, 0.432, 0.045, 0.035, 0.01, R], [0.075, 0.235, 0.432, 0.045, 0.035, 0.01, R]]) };
  return { root, torso, head, armL, armR, eyes, mouth, setMouth(k) { for (const n in mouth) mouth[n].visible = n === k; } };
}
function robot(role, cardTex) {
  const root = new THREE.Group(), inner = new THREE.Group(); root.add(inner);
  inner.add(boxes([[0, 0.88, 0, 0.66, 0.6, 0.5, "#f3f6fb"], [0, 0.5, 0, 0.48, 0.18, 0.38, "#c3cfe2"], [0, 0.9, 0.252, 0.36, 0.22, 0.012, role],
    [0, 0.9, 0.259, 0.2, 0.04, 0.005, "#ffffff"], [-0.335, 1.12, 0, 0.08, 0.12, 0.3, "#c3cfe2"], [0.335, 1.12, 0, 0.08, 0.12, 0.3, "#c3cfe2"]]));
  const eyeMat = emi("#22d3ff", 0);
  const thr = new THREE.Mesh(new THREE.BoxGeometry(0.28, 0.04, 0.22), emi("#36e0ff", 2.2)); thr.position.y = 0.39; inner.add(thr);
  const arm = (s) => { const g = new THREE.Group(); g.position.set(s * 0.42, 1.08, 0);
    g.add(boxes([[0, -0.2, 0, 0.14, 0.4, 0.16, "#e2e8f2"], [0, -0.45, 0, 0.17, 0.13, 0.19, "#c3cfe2"]])); inner.add(g); return g; };
  const armL = arm(-1), armR = arm(1);
  const head = new THREE.Group(); head.position.y = 1.2; inner.add(head);
  head.add(boxes([[0, 0.32, 0, 0.82, 0.62, 0.64, "#f3f6fb"], [0, 0.33, 0.321, 0.68, 0.38, 0.012, "#0b1640"],
    [-0.44, 0.32, 0, 0.06, 0.22, 0.24, "#c3cfe2"], [0.44, 0.32, 0, 0.06, 0.22, 0.24, "#c3cfe2"], [0, 0.72, 0, 0.04, 0.18, 0.04, "#c3cfe2"],
    [0, 0.86, 0, 0.13, 0.13, 0.13, role]]));
  const eg = mergeGeometries([[-0.15, 0.36], [0.15, 0.36]].map(([x, y]) => new THREE.BoxGeometry(0.1, 0.14, 0.02).translate(x, y, 0.33)).concat([new THREE.BoxGeometry(0.16, 0.03, 0.02).translate(0, 0.23, 0.33)]));
  const eyes = new THREE.Mesh(eg, eyeMat); head.add(eyes);
  const eg2 = glow("#3fdcff", 1.05, 0.55); eg2.position.set(0, 0.34, 0.42); eg2.material.opacity = 0; head.add(eg2);
  const card = new THREE.Group();
  card.add(boxes([[0, 0, -0.02, 0.48, 0.48, 0.03, "#ffffff"]]));
  const face = new THREE.Mesh(new THREE.PlaneGeometry(0.46, 0.46), new THREE.MeshBasicMaterial({ map: cardTex, toneMapped: false })); face.position.z = 0.0; card.add(face);
  card.visible = false; inner.add(card);
  // landing dust
  const dust = []; for (let i = 0; i < 7; i++) { const d = boxes([[0, 0, 0, 0.09, 0.09, 0.09, "#dfe7f3"]], MAT, false); d.castShadow = false; d.visible = false; root.add(d); dust.push(d); }
  return { root, inner, head, armL, armR, eyes, eyeMat, card, dust, eg2 };
}
const GLOW = (() => ctexRaw(128, 128, (g) => { const r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, "rgba(255,255,255,1)"); r.addColorStop(0.35, "rgba(255,255,255,.45)"); r.addColorStop(1, "rgba(255,255,255,0)"); g.fillStyle = r; g.fillRect(0, 0, 128, 128); }))();
const glow = (hex, sx, sy) => { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: GLOW, color: new THREE.Color(hex), transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false })); s.scale.set(sx, sy, 1); return s; };

function label(text, bg, fg = "#ffffff", h = 0.32) { // pill sprite, always readable (drawn on top)
  const c = document.createElement("canvas"), g2 = c.getContext("2d"); g2.font = `700 64px ${FONT}`;
  const tw = Math.ceil(g2.measureText(text).width) + 72; c.width = tw; c.height = 104;
  const g = c.getContext("2d"); g.font = `700 64px ${FONT}`; g.fillStyle = "#0a1644"; rr(g, 4, 4, tw - 8, 96, 48); g.fill();   // brand UI: navy pill, cyan rim, white text
  g.lineWidth = 6; g.strokeStyle = "#01ccf7"; rr(g, 4, 4, tw - 8, 96, 48); g.stroke(); g.fillStyle = "#ffffff"; g.textBaseline = "middle"; g.fillText(text, 36, 55);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, transparent: true, depthTest: false, toneMapped: false }));
  sp.renderOrder = 20; sp.userData.aspect = tw / 104; sp.userData.h = h; sp.scale.set(h * tw / 104, h, 1); return sp;
}
const setLabel = (sp, k) => { const h = sp.userData.h * Math.max(0.0001, k); sp.scale.set(h * sp.userData.aspect, h, 1); sp.visible = k > 0.01; };
export { MAT, ENVMAT, rnd, boxes, emi, ctexRaw, ctex, rr, cl, EZ, U, keys, blinkAt, person, robot, GLOW, glow, label, setLabel, FONT };
