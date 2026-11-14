/* AIpreneur voxel test — three worlds built from boxes (our own characters + props, nothing from the reference), rendered
   deterministically from the timeline time: render(t) is a pure function of t (HyperFrames dispatches "hf-seek").
   World A: job seeker at a desk, CV envelopes fly out, empty mailbox, a "?" assembles from flying cubes, then bursts.
   World B: board table, 7 hovering AI robots drop in one by one, a CV slides in, score cards rise; camera dives into the CV.
   World C: ATS scanner: CV rides a conveyor through a laser gate, keyword tags pop, trapdoor drops it into the reject bin
            before the HR person at the end of the belt can read it. */
import * as THREE from "three";
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const cv = document.getElementById("vx");
const W = cv.width, H = cv.height;
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H, false);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.98;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.12;
{ // sky: soft vertical gradient (white theme)
  const c = document.createElement("canvas"); c.width = 4; c.height = 512; const g = c.getContext("2d");
  const gr = g.createLinearGradient(0, 0, 0, 512);
  gr.addColorStop(0, "#9fc4f3"); gr.addColorStop(0.5, "#d3e4fa"); gr.addColorStop(1, "#f3f8ff");
  g.fillStyle = gr; g.fillRect(0, 0, 4, 512);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; scene.background = t;
}
scene.fog = new THREE.Fog(0xdde9f9, 24, 60);
const hemi = new THREE.HemisphereLight(0xffffff, 0xa9bddc, 0.95); scene.add(hemi);
const sun = new THREE.DirectionalLight(0xfff1df, 2.9); sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048); sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.025;
Object.assign(sun.shadow.camera, { left: -9, right: 9, top: 9, bottom: -9, near: 1, far: 40 });
scene.add(sun); scene.add(sun.target);
const fill = new THREE.DirectionalLight(0xcfe0ff, 0.55); scene.add(fill); scene.add(fill.target);

const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 90);

/* ---------------------------------------------------------------- helpers */
const MAT = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.78, metalness: 0 });
const ENVMAT = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.6, metalness: 0, emissive: 0x7d8aa3, emissiveIntensity: 0.55 });
let seed = 7; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
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
function ctex(w, h, draw) {
  const c = document.createElement("canvas"); c.width = w; c.height = h; draw(c.getContext("2d"), w, h);
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
const blinkAt = (t, off = 0) => { let b = 1; for (let s = 1.1 + off; s < 30; s += 2.9 + ((s * 7) % 1.3)) { const d = t - s; if (d >= 0 && d < 0.16) b = Math.min(b, 0.12 + 0.88 * Math.abs(d - 0.08) / 0.08); } return b; };

/* ---------------------------------------------------------------- textures */
const FONT = "Poppins, sans-serif";
let TX = {};
function makeTextures() {
  TX.cv = ctex(620, 860, (g, w, h) => {
    g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h);
    g.fillStyle = "#0a0d2c"; g.fillRect(0, 0, w, 168);
    g.fillStyle = "#01ccf7"; g.fillRect(0, 168, w, 10);
    g.font = `700 76px ${FONT}`; g.fillStyle = "#ffffff"; g.fillText("CV", 40, 112);
    g.fillStyle = "#7fe3ff"; g.fillText("KAMU", 160, 112);
    g.fillStyle = "#d7e8ff"; rr(g, 452, 26, 128, 128, 18); g.fill();
    g.fillStyle = "#7fa6d9"; g.beginPath(); g.arc(516, 74, 26, 0, Math.PI * 2); g.fill(); rr(g, 474, 106, 84, 48, 22); g.fill();
    const sec = (y, label, bars) => {
      g.font = `700 30px ${FONT}`; g.fillStyle = "#0a0d2c"; g.fillText(label, 40, y);
      g.fillStyle = "#01ccf7"; g.fillRect(40, y + 12, 56, 6);
      bars.forEach((bw, i) => { g.fillStyle = "#cbd7e8"; rr(g, 40, y + 38 + i * 36, bw, 16, 8); g.fill(); });
    };
    sec(236, "PENGALAMAN", [530, 470, 380]); sec(408, "PENDIDIKAN", [500, 340]);
    g.font = `700 30px ${FONT}`; g.fillStyle = "#0a0d2c"; g.fillText("SKILL", 40, 548); g.fillStyle = "#01ccf7"; g.fillRect(40, 560, 56, 6);
    let x = 40; for (const s of ["Excel", "Analisis data", "Komunikasi"]) {
      g.font = `700 24px ${FONT}`; const tw = g.measureText(s).width + 36;
      g.fillStyle = "#e3f2ff"; rr(g, x, 584, tw, 46, 23); g.fill(); g.fillStyle = "#294b77"; g.fillText(s, x + 18, 615); x += tw + 12;
    }
    [[680, 520], [716, 450], [752, 300]].forEach(([y, bw]) => { g.fillStyle = "#dfe7f2"; rr(g, 40, y, bw, 14, 7); g.fill(); });
    g.strokeStyle = "#d3ddeb"; g.lineWidth = 6; g.strokeRect(3, 3, w - 6, h - 6);
  });
  const sym = (kind, col) => ctex(256, 256, (g, w) => {
    g.fillStyle = "#ffffff"; rr(g, 8, 8, 240, 240, 36); g.fill(); g.lineWidth = 10; g.strokeStyle = col; rr(g, 13, 13, 230, 230, 32); g.stroke();
    g.fillStyle = col; g.strokeStyle = col; g.lineCap = "round";
    if (kind === "x") { g.lineWidth = 36; g.beginPath(); g.moveTo(78, 78); g.lineTo(178, 178); g.moveTo(178, 78); g.lineTo(78, 178); g.stroke(); }
    else { g.font = `700 190px ${FONT}`; g.textAlign = "center"; g.fillText(kind, 128, 196); }
  });
  TX.cards = [sym("x", "#ff4d5e"), sym("!", "#ff8a3d"), sym("?", "#7c5cff"), sym("x", "#ff4d5e"), sym("!", "#ff8a3d"), sym("x", "#ff4d5e"), sym("?", "#7c5cff")];
  const tag = (txt, ok) => ctex(520, 132, (g, w, h) => {
    const col = ok ? "#12b76a" : "#ff4d5e";
    g.fillStyle = "rgba(10,13,44,0.18)"; rr(g, 10, 16, w - 16, h - 22, 52); g.fill();
    g.fillStyle = "#ffffff"; rr(g, 4, 6, w - 16, h - 22, 52); g.fill(); g.lineWidth = 7; g.strokeStyle = col; rr(g, 8, 10, w - 24, h - 30, 48); g.stroke();
    g.fillStyle = col; g.beginPath(); g.arc(62, 58, 34, 0, Math.PI * 2); g.fill();
    g.strokeStyle = "#ffffff"; g.lineWidth = 9; g.lineCap = "round"; g.lineJoin = "round"; g.beginPath();
    if (ok) { g.moveTo(46, 58); g.lineTo(58, 71); g.lineTo(79, 46); } else { g.moveTo(49, 45); g.lineTo(75, 71); g.moveTo(75, 45); g.lineTo(49, 71); }
    g.stroke(); g.font = `700 50px ${FONT}`; g.fillStyle = "#0a0d2c"; g.fillText(txt, 112, 76);
  });
  TX.tags = [tag("Excel", true), tag("Analisis data", true), tag("SQL", false)];
  TX.screen = ctex(512, 320, (g, w, h) => {
    g.fillStyle = "#f4f8ff"; g.fillRect(0, 0, w, h); g.fillStyle = "#0a0d2c"; g.fillRect(0, 0, w, 54);
    g.font = `700 26px ${FONT}`; g.fillStyle = "#ffffff"; g.fillText("Kirim Lamaran", 22, 36); g.fillStyle = "#01ccf7"; g.fillRect(w - 128, 14, 106, 26);
    g.font = `700 16px ${FONT}`; g.fillStyle = "#0a0d2c"; g.fillText("KIRIM SEMUA", w - 122, 33);
    for (let i = 0; i < 5; i++) { const y = 74 + i * 48; g.fillStyle = "#ffffff"; rr(g, 18, y, w - 36, 38, 9); g.fill();
      g.fillStyle = "#cbd7e8"; rr(g, 66, y + 13, 200 - i * 18, 12, 6); g.fill(); g.fillStyle = "#294b77"; rr(g, 28, y + 7, 26, 24, 6); g.fill();
      g.fillStyle = "#12b76a"; g.beginPath(); g.arc(w - 46, y + 19, 11, 0, Math.PI * 2); g.fill(); }
  });
  TX.bin = ctex(256, 256, (g) => { g.fillStyle = "#ffffff"; g.font = `700 64px ${FONT}`; g.textAlign = "center"; g.fillText("TOLAK", 128, 150); });
}

/* ---------------------------------------------------------------- builders */
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
  const card = new THREE.Group();
  card.add(boxes([[0, 0, -0.02, 0.48, 0.48, 0.03, "#ffffff"]]));
  const face = new THREE.Mesh(new THREE.PlaneGeometry(0.46, 0.46), new THREE.MeshBasicMaterial({ map: cardTex, toneMapped: false })); face.position.z = 0.0; card.add(face);
  card.visible = false; inner.add(card);
  // landing dust
  const dust = []; for (let i = 0; i < 7; i++) { const d = boxes([[0, 0, 0, 0.09, 0.09, 0.09, "#dfe7f3"]], MAT, false); d.castShadow = false; d.visible = false; root.add(d); dust.push(d); }
  return { root, inner, head, armL, armR, eyes, eyeMat, card, dust };
}
function diorama() { // finite floating slab (6.5 x 6.5 half size) with a navy base and a little town around the edge
  const g = new THREE.Group(); const L = [];
  for (let i = -6; i < 7; i++) for (let j = -6; j < 7; j++) L.push([i, -0.05, j, 1, 0.1, 1, (i + j) & 1 ? "#f5f8fd" : "#d8e4f4"]);
  const top = boxes(L, MAT, false); top.castShadow = false; g.add(top);
  g.add(boxes([[0, -0.55, 0, 13.0, 0.9, 13.0, "#294b77"], [0, -0.12, 0, 13.04, 0.05, 13.04, "#01ccf7"], [0, -1.1, 0, 12.4, 0.25, 12.4, "#1f3c62"]], MAT, false));
  seed = 19; const T = [];
  const bld = (x, z, w, d, h, c) => { T.push([x, h / 2, z, w, h, d, c], [x, h + 0.06, z, w + 0.06, 0.12, d + 0.06, "#ffffff"]);
    for (let y = 0.45; y < h - 0.3; y += 0.42) for (let k = -w / 2 + 0.28; k < w / 2 - 0.15; k += 0.34) {
      T.push([x + k, y, z + d / 2 + 0.01, 0.18, 0.22, 0.02, rnd() > 0.3 ? "#bfe9ff" : "#e9f3ff"]); T.push([x + k, y, z - d / 2 - 0.01, 0.18, 0.22, 0.02, "#e9f3ff"]); } };
  const pal = ["#3567b5", "#294b77", "#7aa7e0", "#ff8a3d", "#5b8fd6", "#1f3c62", "#a9c6ee", "#ffc531"];
  [[-5.0, 1.3], [-3.3, 1.2], [3.3, 1.2], [5.0, 1.3]].forEach(([x, w], i) => bld(x, 5.2, w, 1.0, 1.6 + rnd() * 1.8, pal[i]));          // in front of the desk (gap in the middle)
  [[-5.0, 1.2], [-3.4, 1.3], [-1.7, 1.1], [0, 1.4], [1.7, 1.2], [3.4, 1.3], [5.0, 1.1]].forEach(([x, w], i) => bld(x, -5.2, w, 1.0, 1.8 + rnd() * 2.6, pal[(i + 3) % 8]));
  [[-5.4, -3], [-5.4, 2.4], [5.4, -3], [5.4, 2.4]].forEach(([x, z], i) => bld(x, z, 1.0, 1.4, 1.2 + rnd() * 1.4, pal[(i + 5) % 8]));
  for (const [x, z] of [[-4.1, 3.4], [4.2, 3.6], [-2.6, -3.9], [2.7, -3.8], [-4.4, -1.0], [4.5, 0.6]]) T.push([x, 0.3, z, 0.12, 0.6, 0.12, "#8a6a4a"], [x, 0.85, z, 0.6, 0.6, 0.6, "#4cc56a"], [x, 1.25, z, 0.36, 0.3, 0.36, "#58d277"]);
  g.add(boxes(T));
  return g;
}
function floor(n, a, b) {
  const L = []; for (let i = -n; i < n; i++) for (let j = -n; j < n; j++) L.push([i + 0.5, -0.05, j + 0.5, 1, 0.1, 1, (i + j) & 1 ? a : b]);
  const m = boxes(L, MAT, false); m.castShadow = false; return m;
}
function skyline(z0, flip) {
  const L = []; seed = 31;
  for (let row = 0; row < 2; row++) for (let x = -22; x < 22;) {
    const w = 1.6 + rnd() * 2.2, h = 2 + rnd() * (row ? 7 : 4.5), z = z0 - row * 5 - rnd() * 1.5, c = row ? "#94b3e0" : "#adc6ec";
    L.push([x + w / 2, h / 2, z, w, h, 1.6, c]);
    for (let wy = 0.8; wy < h - 0.6; wy += 0.75) for (let wx = x + 0.45; wx < x + w - 0.4; wx += 0.55) if (rnd() > 0.35) L.push([wx, wy, z + 0.81, 0.26, 0.36, 0.02, row ? "#d3e2f7" : "#eaf2fd"]);
    x += w + 0.25 + rnd() * 0.6;
  }
  const m = boxes(L, MAT, false); m.castShadow = false; m.receiveShadow = false; if (flip) m.rotation.y = Math.PI; return m;
}
const WX = { A: 0, B: 40, C: 80 };
const worlds = {}, A = {}, B = {}, C = {};

function buildA() {
  const g = new THREE.Group(); worlds.A = g; scene.add(g);
  g.add(diorama());
  // desk + props
  g.add(boxes([[0, 0.9, 0, 2.3, 0.1, 1.05, "#e9cfa8"], [0, 0.84, 0.5, 2.3, 0.04, 0.06, "#d8b98e"], [-1.05, 0.42, 0.42, 0.1, 0.84, 0.1, "#d8b98e"], [1.05, 0.42, 0.42, 0.1, 0.84, 0.1, "#d8b98e"],
    [-1.05, 0.42, -0.42, 0.1, 0.84, 0.1, "#d8b98e"], [1.05, 0.42, -0.42, 0.1, 0.84, 0.1, "#d8b98e"],
    [0, 0.975, 0.02, 0.74, 0.04, 0.5, "#aab6c8"], [0, 0.997, -0.05, 0.6, 0.006, 0.28, "#8794a8"],                       // laptop base + keys
    [-0.78, 1.06, 0.15, 0.2, 0.22, 0.2, "#ffffff"], [-0.78, 1.18, 0.15, 0.21, 0.03, 0.21, "#01ccf7"], [-0.665, 1.08, 0.15, 0.04, 0.1, 0.06, "#ffffff"], // mug
    [0.82, 1.03, 0.1, 0.24, 0.16, 0.24, "#294b77"], [0.82, 1.2, 0.1, 0.1, 0.22, 0.1, "#3fae5a"], [0.74, 1.3, 0.1, 0.12, 0.1, 0.12, "#4cc56a"], [0.9, 1.34, 0.12, 0.12, 0.12, 0.12, "#3fae5a"], [0.8, 1.42, 0.06, 0.1, 0.1, 0.1, "#58d277"]]));
  const lid = new THREE.Group(); lid.position.set(0, 0.995, 0.27); lid.rotation.x = -0.32; g.add(lid);
  lid.add(boxes([[0, 0.24, 0, 0.74, 0.48, 0.035, "#c4cedc"], [0, 0.26, 0.019, 0.1, 0.1, 0.004, "#01ccf7"]]));
  const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.68, 0.42), new THREE.MeshBasicMaterial({ map: TX.screen, toneMapped: false })); scr.position.set(0, 0.24, -0.019); scr.rotation.y = Math.PI; lid.add(scr);
  A.kid = person({ skin: "#f1c39d", hair: "#4a3326", top: "#3567b5", top2: "#2c5598", pants: "#26314d", glasses: true, strings: true,
    fringe: [[-0.36, 0.22], [-0.18, 0.15], [0, 0.24], [0.18, 0.13], [0.36, 0.2]] });
  A.kid.root.position.set(0, 0, -0.78); g.add(A.kid.root);
  // mailbox
  const mb = new THREE.Group(); mb.position.set(2.25, 0, 0.25); mb.rotation.y = -0.35; g.add(mb); A.mb = mb;
  mb.add(boxes([[0, 0.45, 0, 0.12, 0.9, 0.12, "#8798b6"], [0, 0.03, 0, 0.36, 0.06, 0.36, "#8798b6"], [0, 1.11, 0, 0.5, 0.44, 0.72, "#294b77"], [0, 1.34, 0, 0.42, 0.06, 0.64, "#1f3c62"],
    [0, 1.11, 0.358, 0.4, 0.34, 0.01, "#0b1230"]]));
  const door = new THREE.Group(); door.position.set(0, 0.89, 0.37); mb.add(door); A.door = door;
  door.add(boxes([[0, 0.22, 0.015, 0.5, 0.44, 0.03, "#2f5b8f"], [0, 0.34, 0.04, 0.12, 0.04, 0.03, "#dfe7f3"]]));
  const flag = new THREE.Group(); flag.position.set(0.27, 1.05, -0.1); mb.add(flag); A.flag = flag;
  flag.add(boxes([[0, 0.2, 0, 0.03, 0.4, 0.04, "#d7dfeb"], [0, 0.36, -0.1, 0.03, 0.12, 0.18, "#ff4d5e"]]));
  A.mdust = []; for (let i = 0; i < 9; i++) { const d = boxes([[0, 0, 0, 0.07, 0.07, 0.07, "#c9d3e3"]], MAT, false); d.visible = false; mb.add(d); A.mdust.push(d); }
  // envelopes
  A.env = []; const eg = boxes([[0, 0, 0, 0.36, 0.02, 0.25, "#ffffff"], [-0.08, 0.012, 0.03, 0.2, 0.006, 0.03, "#294b77"], [0.08, 0.012, 0.03, 0.2, 0.006, 0.03, "#294b77"], [0, 0.016, 0.0, 0.07, 0.008, 0.07, "#01ccf7"]], MAT, false);
  seed = 5; for (let k = 0; k < 18; k++) { const m = eg.clone(); m.material = ENVMAT; m.visible = false; g.add(m); const side = k & 1 ? 1 : -1; A.env.push({ m, x: side * (3.0 + rnd() * 2.4), y: 0.8 + rnd() * 1.8, z: 4.7, r: rnd() * 6 }); }
  // question mark from cubes
  const Q = [".####.", "##..##", "....##", "...##.", "..##..", "..##..", "......", "..##.."];
  A.q = []; seed = 11;
  Q.forEach((row, r) => [...row].forEach((ch, c) => { if (ch !== "#") return;
    const m = boxes([[0, 0, 0, 0.165, 0.165, 0.165, (r + c) & 1 ? "#294b77" : "#1f9fd6"]], MAT, false); g.add(m); m.visible = false;
    const slot = new THREE.Vector3((c - 2.5) * 0.17, 3.68 - r * 0.17, -0.78);
    const a = rnd() * Math.PI * 2, rad = 1.6 + rnd() * 1.6;
    A.q.push({ m, slot, from: new THREE.Vector3(Math.cos(a) * rad, 2.6 + (rnd() - 0.3) * 2.4, -0.78 + Math.sin(a) * rad), rot: [rnd() * 6, rnd() * 6, rnd() * 6], dir: new THREE.Vector3(rnd() - 0.5, rnd() - 0.4, 0.6 + rnd()).normalize() });
  }));
}
function buildB() {
  const g = new THREE.Group(); g.position.x = WX.B; worlds.B = g; scene.add(g);
  g.add(floor(14, "#f5f8fd", "#d8e4f4")); g.add(skyline(-19));
  // three-tier jury stand: white steps, navy risers, cyan edge lights; lectern with the CV in front
  const L = [[0, 0.35, -1.7, 4.2, 0.7, 1.2, "#f3f6fb"], [0, 0.7, -1.7, 4.22, 0.05, 1.22, "#294b77"], [0, 0.35, -1.105, 4.2, 0.6, 0.01, "#dfe7f2"],
    [0, 0.7, -2.95, 3.0, 1.4, 1.3, "#f3f6fb"], [0, 1.4, -2.95, 3.02, 0.05, 1.32, "#294b77"], [0, 1.05, -2.295, 3.0, 0.6, 0.01, "#dfe7f2"],
    [0, 0.06, 1.55, 1.0, 0.12, 0.8, "#1f3c62"], [0, 0.5, 1.55, 0.8, 0.85, 0.6, "#294b77"], [0, 0.95, 1.6, 1.0, 0.06, 0.78, "#f7f9fd"], [0, 0.6, 1.86, 0.5, 0.06, 0.01, "#01ccf7"]];
  g.add(boxes(L));
  for (const [y, z, w] of [[0.72, -1.1, 4.2], [1.42, -2.29, 3.0]]) { const e = new THREE.Mesh(new THREE.BoxGeometry(w, 0.025, 0.025), emi("#36e0ff", 2.2)); e.position.set(0, y, z); g.add(e); }
  const pos = [[-0.62, 0.1, -0.35], [0.62, 0.1, -0.35], [-1.25, 0.8, -1.6], [0, 0.8, -1.6], [1.25, 0.8, -1.6], [-0.62, 1.5, -2.85], [0.62, 1.5, -2.85]];
  const roles = ["#01ccf7", "#ff8a3d", "#ffc531", "#ff5c8a", "#2ecc71", "#7c5cff", "#ff4d5e"];
  B.order = [3, 0, 6, 2, 1, 5, 4];                     // landing order (scattered over the stand)
  B.bots = pos.map(([x, y, z], i) => { const r = robot(roles[i], TX.cards[i]); r.root.position.set(x, y, z); r.y0 = y;
    r.yaw = Math.atan2(0 - x, 6 - z) * 0.8; r.root.rotation.y = r.yaw; g.add(r.root); return r; });
  const cvm = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.86), new THREE.MeshStandardMaterial({ map: TX.cv, roughness: 0.9 }));
  cvm.rotation.x = -Math.PI / 2; cvm.receiveShadow = true; B.cv = new THREE.Group(); B.cv.add(cvm); g.add(B.cv);
}
function buildC() {
  const g = new THREE.Group(); g.position.x = WX.C; worlds.C = g; scene.add(g);
  g.add(floor(14, "#f5f8fd", "#d8e4f4")); g.add(skyline(-18));
  const L = [[-1.5, 0.78, 0, 7.0, 0.1, 1.15, "#a9b8cf"], [-1.5, 0.83, 0, 7.0, 0.02, 1.0, "#2b3348"], [-1.5, 0.78, 0.6, 7.0, 0.14, 0.06, "#8a9bb8"], [-1.5, 0.78, -0.6, 7.0, 0.14, 0.06, "#8a9bb8"]];
  for (const x of [-4.6, -2.8, -1.0, 0.8]) L.push([x, 0.37, 0.45, 0.1, 0.74, 0.1, "#8a9bb8"], [x, 0.37, -0.45, 0.1, 0.74, 0.1, "#8a9bb8"]);
  L.push([0, 1.12, 0.72, 0.22, 2.24, 0.22, "#f3f6fb"], [0, 1.12, -0.72, 0.22, 2.24, 0.22, "#f3f6fb"], [0, 2.3, 0, 0.3, 0.28, 1.72, "#f3f6fb"], [0, 2.3, 0, 0.32, 0.08, 1.5, "#294b77"],
    [0, 0.06, 0.72, 0.4, 0.12, 0.4, "#c3cfe2"], [0, 0.06, -0.72, 0.4, 0.12, 0.4, "#c3cfe2"]);
  // reject bin under the trapdoor
  L.push([1.85, 0.05, 0, 0.9, 0.1, 0.9, "#d63a4c"], [1.85, 0.32, 0.44, 0.9, 0.54, 0.04, "#ff4d5e"], [1.85, 0.32, -0.44, 0.9, 0.54, 0.04, "#ff4d5e"], [1.42, 0.32, 0, 0.04, 0.54, 0.86, "#ff4d5e"], [2.28, 0.32, 0, 0.04, 0.54, 0.86, "#ff4d5e"]);
  // HR desk
  L.push([3.45, 0.86, 0, 1.0, 0.1, 1.3, "#e9cfa8"], [3.45, 0.42, 0.55, 0.9, 0.8, 0.06, "#d8b98e"], [3.45, 0.42, -0.55, 0.9, 0.8, 0.06, "#d8b98e"],
    [3.25, 0.92, -0.3, 0.32, 0.02, 0.4, "#ffffff"], [3.28, 0.93, -0.32, 0.22, 0.006, 0.05, "#cbd7e8"]);
  g.add(boxes(L));
  const ls = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.05, 1.24), emi("#36e0ff", 2.6)); ls.position.set(0.17, 2.3, 0); g.add(ls);
  const lm = new THREE.MeshBasicMaterial({ color: 0x38dcff, transparent: true, opacity: 0.22, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending });
  C.laser = new THREE.Mesh(new THREE.PlaneGeometry(1.24, 1.38), lm); C.laser.rotation.y = Math.PI / 2; C.laser.position.set(0, 1.53, 0); g.add(C.laser);
  C.line = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.01, 1.0), emi("#36e0ff", 3)); C.line.position.set(0, 0.85, 0); g.add(C.line);
  const binLbl = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.62), new THREE.MeshBasicMaterial({ map: TX.bin, transparent: true, toneMapped: false })); binLbl.position.set(1.85, 0.33, 0.465); g.add(binLbl);
  C.binGlow = new THREE.PointLight(0xff3344, 0, 3); C.binGlow.position.set(1.85, 0.9, 0.6); g.add(C.binGlow);
  // belt slats (scroll), trapdoor
  C.slats = []; for (let i = 0; i < 16; i++) { const s = boxes([[0, 0, 0, 0.05, 0.012, 0.98, "#46506a"]], MAT, false); s.castShadow = false; g.add(s); C.slats.push(s); }
  C.trap = new THREE.Group(); C.trap.position.set(1.42, 0.835, 0); g.add(C.trap);
  C.trap.add(boxes([[0.43, 0.0, 0, 0.86, 0.02, 0.98, "#3a4560"]]));
  g.add(boxes([[1.85, 0.78, 0.6, 0.9, 0.14, 0.06, "#8a9bb8"], [1.85, 0.78, -0.6, 0.9, 0.14, 0.06, "#8a9bb8"]]));
  const cvm = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.86), new THREE.MeshStandardMaterial({ map: TX.cv, roughness: 0.9, side: THREE.DoubleSide }));
  cvm.rotation.x = -Math.PI / 2; cvm.receiveShadow = true; cvm.castShadow = true; C.cv = new THREE.Group(); C.cv.add(cvm); g.add(C.cv);
  C.tags = TX.tags.map((t) => { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, transparent: true, toneMapped: false, depthTest: false })); s.renderOrder = 10; s.visible = false; g.add(s); return s; });
  C.hr = person({ skin: "#e8b48f", hair: "#3b2318", top: "#ff7aa0", top2: "#f2648d", pants: "#2d3550", bun: true,
    fringe: [[-0.36, 0.16], [-0.18, 0.2], [0.0, 0.12], [0.18, 0.2], [0.36, 0.16]] });
  C.hr.root.position.set(3.95, 0, 0.1); C.hr.root.rotation.y = -Math.PI / 2 + 0.55; g.add(C.hr.root);
  C.mug = boxes([[0, 0, 0, 0.17, 0.2, 0.17, "#ffffff"], [0, 0.1, 0, 0.18, 0.03, 0.18, "#01ccf7"]]); g.add(C.mug);
}

/* ---------------------------------------------------------------- shots (video time; VO starts at 0.3 s) */
const SHOT = [
  { w: "A", a: -1, b: 6.98, cam: [[0, [2.5, 3.2, -2.7, -0.25, 1.25, 0.6, 44]], [0.55, [2.4, 3.15, -2.55, -0.25, 1.25, 0.6, 44], "sine"], [2.3, [2.7, 4.6, -3.3, 0.2, 1.9, 3.2, 50], "io"],
    [2.82, [3.75, 1.75, 3.7, 2.05, 1.1, 0.15, 40], "expo"], [3.8, [3.55, 1.7, 3.45, 2.05, 1.12, 0.15, 40], "sine"], [4.3, [0.3, 2.9, 7.1, 0, 2.5, -0.78, 42], "expo"],
    [5.9, [0.22, 2.9, 6.6, 0, 2.52, -0.78, 42], "sine"], [6.85, [0, 27, 50, 0, 0.4, 0, 30], "io"], [6.98, [0, 27.4, 50.8, 0, 0.4, 0, 30], "sine"]] },
  { w: "B", a: 6.98, b: 11.27, cam: [[6.98, [1.2, 3.4, 5.4, 0, 2.1, -1.4, 46]], [8.9, [0, 3.5, 9.6, 0, 1.75, -1.2, 42], "io"], [10.55, [0, 3.2, 8.6, 0, 1.7, -1.2, 42], "sine"],
    [11.27, [0, 1.62, 1.8, 0, 0.98, 1.65, 30], "expo"]] },
  { w: "C", a: 11.27, b: 99, cam: [[11.27, [-3.2, 1.9, 0.06, -3.2, 0.84, 0.0, 34]], [12.8, [-1.9, 4.6, 10.4, -1.6, 1.2, 0, 40], "io"], [14.4, [-0.6, 4.5, 10.4, -0.4, 1.25, 0, 40], "sine"],
    [15.25, [0.3, 4.5, 10.4, 0.4, 1.25, 0, 40], "sine"], [16.15, [2.9, 4.3, 10.6, 3.05, 1.25, 0, 40], "io"], [18.5, [3.1, 4.1, 10.0, 3.15, 1.25, 0, 40], "sine"]] },
];
const ROB_LAND = (i) => 7.42 + i * 0.2;
const CV_X = (t) => t < 12.9 ? -3.2 : t < 15.85 ? -3.2 + 5.0 * EZ.sine((t - 12.9) / 2.95) : 1.8;
window.VX = { SHOT, ROB_LAND }; // read by the page (counter chip, sfx)

/* ---------------------------------------------------------------- per-frame */
function animA(t) {
  const k = A.kid; k.root.visible = true;
  const blink = blinkAt(t); k.eyes.forEach((e) => (e.scale.y = blink));
  // typing (0..2.4) -> look up at envelopes -> look at mailbox -> slump + scratch head
  const typ = 1 - U(t, 2.2, 2.6);
  k.armL.rotation.set(-0.95 * typ + Math.sin(t * 22) * 0.06 * typ, 0, 0.12 * typ); k.armR.rotation.set(-0.95 * typ + Math.sin(t * 22 + 1.7) * 0.06 * typ, 0, -0.12 * typ);
  const lookUp = U(t, 0.9, 1.4) * (1 - U(t, 2.3, 2.7));
  const toMb = U(t, 2.45, 2.85, "out") * (1 - U(t, 3.75, 4.15));
  k.head.rotation.set(0.2 * (1 - U(t, 0.6, 1.0)) * typ - 0.3 * lookUp + 0.06 * toMb, 0.75 * toMb + 0.12 * lookUp, 0.16 * U(t, 4.1, 4.5) * (1 - U(t, 5.9, 6.2)));
  const slump = U(t, 3.15, 3.7) * (1 - U(t, 5.9, 6.2)); k.torso.rotation.x = 0.1 * slump;
  const scr = U(t, 4.25, 4.6, "out") * (1 - U(t, 5.75, 6.05));
  if (scr > 0) { k.armR.rotation.set(-2.75 * scr + 0.12 * Math.sin(t * 17) * scr, 0, 0.55 * scr); }
  k.setMouth(t < 0.9 ? "n" : t < 2.6 ? "o" : t < 3.1 ? "n" : "sad");
  // envelopes: one launch every 0.1 s from the laptop
  A.env.forEach((e, i) => { const t0 = 0.62 + i * 0.095, u = (t - t0) / 1.15; e.m.visible = u > 0 && u < 1;
    if (!e.m.visible) return; const s = EZ.out(u);
    e.m.position.set(0 + (e.x - 0) * s, 1.25 + (e.y - 1.25) * s + 2.2 * Math.sin(Math.PI * Math.min(1, u)), 0.1 + (e.z - 0.1) * s);
    e.m.rotation.set(0.4 + e.r * u, e.r * 0.6 * u, Math.sin(u * 9 + e.r) * 0.5); e.m.scale.setScalar(2.3 - 1.1 * u * u); });
  // mailbox: flag down, door drops open, dust puff
  A.door.rotation.x = 1.5 * U(t, 2.92, 3.22, "back"); A.flag.rotation.x = -0.05 * Math.sin(t * 3);
  A.mdust.forEach((d, i) => { const u = (t - 3.08 - i * 0.02) / 0.75; d.visible = u > 0 && u < 1; if (!d.visible) return;
    const a = (i / 9) * Math.PI * 2; d.position.set(Math.cos(a) * 0.45 * EZ.out(u), 1.12 + Math.sin(a) * 0.25 * EZ.out(u) + 0.15 * u, 0.42 + 0.5 * EZ.out(u)); d.scale.setScalar(1 - u); });
  // "?" assembles (4.15..4.9), bobs, bursts toward camera (5.9..6.4)
  const bob = Math.sin(t * 3.2) * 0.05;
  A.q.forEach((q, i) => { const t0 = 4.12 + i * 0.03, u = U(t, t0, t0 + 0.55, "back"); q.m.visible = t > t0 - 0.01;
    if (!q.m.visible) return; const p = q.from.clone().lerp(q.slot, u); p.y += bob * u;
    const ex = U(t, 5.95, 6.5, "out"); if (ex > 0) p.addScaledVector(q.dir, ex * 5.5);
    q.m.position.copy(p); q.m.rotation.set(q.rot[0] * (1 - u) + ex * q.rot[0], q.rot[1] * (1 - u) + ex * q.rot[1], q.rot[2] * (1 - u));
    q.m.scale.setScalar(Math.max(0.001, U(t, t0, t0 + 0.2) * (1 - U(t, 6.2, 6.6)))); });
}
function animB(t) {
  B.bots.forEach((r, i) => {
    const n = B.order.indexOf(i), tl = ROB_LAND(n), f = U(t, tl - 0.34, tl, "in"); r.root.visible = t > tl - 0.36;
    const since = t - tl, sq = since > 0 ? Math.exp(-since * 7) * Math.cos(since * 22) * 0.22 : 0;
    r.root.position.y = r.y0 + (1 - f) * 5.5 + (since > 0 ? Math.sin(t * 2.4 + i) * 0.035 : 0);
    r.inner.scale.set(1 + sq * 0.6, 1 - sq, 1 + sq * 0.6);
    const on = U(t, tl + 0.08, tl + 0.22), raise = U(t, 9.83 + n * 0.06, 10.13 + n * 0.06, "back");
    r.eyeMat.emissiveIntensity = 2.2 * on + 1.6 * raise * (0.5 + 0.5 * Math.sin(t * 18));
    r.eyes.scale.y = since > 0.3 ? blinkAt(t, i * 0.37) : 1;
    r.head.rotation.set(0.22 * U(t, 8.85 + i * 0.03, 9.2 + i * 0.03) * (1 - raise * 0.8), Math.sin(t * 1.3 + i) * 0.08, 0);
    r.armR.rotation.set(-2.85 * raise, 0, 0.18 * raise); r.armL.rotation.set(0.15 * Math.sin(t * 2 + i), 0, -0.1);
    r.card.visible = raise > 0.01; r.card.position.set(0.47, 1.0 + 1.22 * raise, 0.12 + 0.1 * raise); r.card.scale.setScalar(Math.max(0.001, raise));
    r.card.rotation.set(0, 0, Math.sin(t * 5 + i) * 0.06 * raise);
    r.dust.forEach((d, j) => { const u = (t - tl) / 0.6; d.visible = u > 0 && u < 1; if (!d.visible) return;
      const a = (j / 7) * Math.PI * 2 + i; d.position.set(Math.cos(a) * 0.7 * EZ.out(u), 0.12 + 0.18 * EZ.out(u), Math.sin(a) * 0.7 * EZ.out(u)); d.scale.setScalar(1.2 * (1 - u)); });
  });
  const s = U(t, 8.3, 8.9, "out"); B.cv.visible = t > 8.25;
  B.cv.position.set(0.15 * (1 - s), 0.985 + 0.35 * Math.sin(Math.PI * s) * (1 - s), 1.6 + 2.2 * (1 - s)); B.cv.rotation.y = 0.5 * (1 - s);
}
function animC(t) {
  const x = CV_X(t), fall = U(t, 15.92, 16.38, "in");
  C.cv.position.set(x + 0.25 * fall, 0.845 - 0.62 * fall, 0); C.cv.rotation.set(fall * 1.1, 0, fall * 0.6);
  C.trap.rotation.z = -1.3 * U(t, 15.86, 16.06, "out") * (1 - U(t, 16.8, 17.1));
  const moving = t > 12.9 && t < 15.85 ? 1 : 0, off = (CV_X(t) + 3.2) * 1.0;
  C.slats.forEach((s, i) => { let sx = ((i * 0.38 + off) % 6.08) - 4.9; s.position.set(sx, 0.842, 0); s.visible = sx < 1.38; });
  const pass = U(t, 14.45, 14.75) * (1 - U(t, 15.05, 15.35));
  C.laser.material.opacity = 0.16 + 0.04 * Math.sin(t * 20) + 0.28 * pass; C.line.position.x = 0;
  C.tags.forEach((s, i) => { const t0 = 14.55 + i * 0.25, u = U(t, t0, t0 + 0.4, "back"), o = 1 - U(t, 16.6, 16.9); s.visible = t > t0 && o > 0;
    s.position.set(1.05, 1.42 + i * 0.33 + 0.03 * Math.sin(t * 3 + i), 0.45); s.scale.set(1.0 * u * o, 0.254 * u * o, 1); });
  C.binGlow.intensity = 6 * U(t, 16.32, 16.42) * (1 - U(t, 16.7, 17.3)) + 3 * U(t, 16.42, 16.5) * (1 - U(t, 17.3, 17.8));
  const h = C.hr; h.eyes.forEach((e) => (e.scale.y = blinkAt(t, 0.6)));
  const look = U(t, 16.25, 16.55, "out");
  h.head.rotation.set(0.25 * look, -0.35 * look, 0.08 * Math.sin(t * 1.4));
  h.armR.rotation.set(-1.25 * (1 - look * 0.5) - 0.05 * Math.sin(t * 2), 0.2, 0.15);
  h.armL.rotation.set(-0.15, 0, 0);
  h.setMouth(t < 16.3 ? "smile" : "o");
  // the mug follows HR's right hand (world-space)
  h.armR.updateWorldMatrix(true, false); const hp = new THREE.Vector3(0, -0.62, 0.05).applyMatrix4(h.armR.matrixWorld);
  worlds.C.worldToLocal(hp); C.mug.position.copy(hp); C.mug.rotation.y = 0.3;
}
let ready = false; const LIFTAT = (t) => 230 * U(t, 6.0, 6.8);   // the camera target lands at y = 960 - LIFT on screen
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  const sh = SHOT.find((s) => t >= s.a && t < s.b) || SHOT[SHOT.length - 1];
  for (const k in worlds) worlds[k].visible = k === sh.w;
  const ox = WX[sh.w];
  if (sh.w === "A") animA(t); else if (sh.w === "B") animB(t); else animC(t);
  const v = keys(t, sh.cam), hx = Math.sin(t * 0.9) * 0.025, hy = Math.sin(t * 1.3 + 1) * 0.02;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(ox + v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.lookAt(ox + v[3], v[4], v[5]);
  sun.position.set(ox + 5, 10, 7); sun.target.position.set(ox, 0, -1.5); fill.position.set(ox - 6, 4, 6); fill.target.position.set(ox, 1, -1);
  renderer.render(scene, cam);
}
window.VX.render = render;
const P = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  makeTextures(); buildA(); buildB(); buildC(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = P;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
