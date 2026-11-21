/* R31 "VOLUME" — voxel worlds (white theme). Our own props only (no stick figure, no basket, nothing from the reference).
   render(t) is a pure function of video time t (HyperFrames dispatches "hf-seek"). Through-line object: ONE cyan cube
   ("satu percobaan") — fired at the target island, becomes a video tile, a follow-up bubble, an ad coin, a day tile, a draft
   card, then climbs the spiral staircase of 30 days and finally hits the bullseye it missed in the hook.
   A  range: cube cannon + floating target island (3 misses -> give up flag -> 100 tries, hits stick to the target)
   B  content wall 10x10 (5 videos -> 100 videos, a few tiles rise)
   C  follow-up hub: shop + 6 houses, chat bubbles in waves, replies light up
   D  ad billboards: 1 billboard + whole budget -> 10 variations, data bars pick the winner
   E  30-day grid (olahraga) -> bars rise per day (catat -> perbaiki)
   F  AI desk: monitor drawn live as a scripted chat window View(t) (html-demo technique) + output card stacks
   G  two big buttons (POSTING / KIRIM) at the foot of a 30-step spiral staircase to the target summit (CTA) */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { MAT, rnd, setSeed, boxes, emi, ctex, rr, cl, EZ, U, keys, glow, label, setLabel, FONT } from "./vxlib.js";

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
{ const c = document.createElement("canvas"); c.width = 4; c.height = 512; const g = c.getContext("2d");
  const gr = g.createLinearGradient(0, 0, 0, 512); gr.addColorStop(0, "#9fc4f3"); gr.addColorStop(0.5, "#d3e4fa"); gr.addColorStop(1, "#f3f8ff");
  g.fillStyle = gr; g.fillRect(0, 0, 4, 512); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; scene.background = t; }
scene.fog = new THREE.Fog(0xdde9f9, 24, 60);
scene.add(new THREE.HemisphereLight(0xffffff, 0xa9bddc, 0.95));
const sun = new THREE.DirectionalLight(0xfff1df, 2.9); sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048); sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.025;
Object.assign(sun.shadow.camera, { left: -12, right: 12, top: 12, bottom: -12, near: 1, far: 60 });
scene.add(sun); scene.add(sun.target);
const fill = new THREE.DirectionalLight(0xcfe0ff, 0.55); scene.add(fill); scene.add(fill.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 160);

const CY = "#01ccf7", NV = "#294b77", NV2 = "#0a0d2c";
const spring = (t, t0, w = 13, z = 7) => (t <= t0 ? 0 : 1 - Math.exp(-z * (t - t0)) * Math.cos(w * (t - t0)));   // small overshoot
const S = (x) => Math.max(0.0001, x);
const V3 = (x, y, z) => new THREE.Vector3(x, y, z);
const hash = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };

function island(nx, nz, top = ["#f5f8fd", "#d8e4f4"]) {
  const g = new THREE.Group(), L = [];
  for (let i = -nx; i <= nx; i++) for (let j = -nz; j <= nz; j++) L.push([i, -0.05, j, 1, 0.1, 1, (i + j) & 1 ? top[0] : top[1]]);
  const t = boxes(L, MAT, false); t.castShadow = false; g.add(t);
  const Wd = 2 * nx + 1, D = 2 * nz + 1;
  g.add(boxes([[0, -0.55, 0, Wd, 0.9, D, NV], [0, -0.12, 0, Wd + 0.04, 0.05, D + 0.04, CY], [0, -1.15, 0, Wd - 0.8, 0.3, D - 0.8, "#1f3c62"],
    [0, -1.5, 0, Math.max(1, Wd - 2.2), 0.4, Math.max(1, D - 2.2), "#16304f"], [0, -1.95, 0, Wd * 0.35, 0.5, D * 0.35, "#10243d"]], MAT, false));
  return g;
}
function bullseye(R = 1.5, s = 0.15) { // voxel target disc in the xy plane (faces +z)
  const L = [], n = Math.ceil(R / s);
  for (let i = -n; i <= n; i++) for (let j = -n; j <= n; j++) { const r = Math.hypot(i * s, j * s); if (r > R) continue;
    const k = Math.floor((r / R) * 5); L.push([i * s, j * s, 0, s, s, 0.16, [CY, "#ffffff", NV, "#ffffff", NV][k]]); }
  L.push([0, 0, -0.14, R * 2, R * 2, 0.1, "#dfe7f2"]);
  return boxes(L, MAT, false);
}
const CUBE_GEO = new THREE.BoxGeometry(0.26, 0.26, 0.26);
const CUBE_MAT = new THREE.MeshStandardMaterial({ color: 0x01ccf7, emissive: 0x01a8d6, emissiveIntensity: 0.45, roughness: 0.35 });
const cube = (k = 1) => { const m = new THREE.Mesh(CUBE_GEO, CUBE_MAT); m.scale.setScalar(k); m.castShadow = true; return m; };

/* ---------------------------------------------------------------- worlds */
const WP = { A: [0, 0, 0], B: [44, 0, 0], C: [88, 0, 0], D: [132, 0, 0], E: [176, 0, 0], F: [220, 0, 0], G: [264, 0, 0] };
const worlds = {}, A = {}, B = {}, C = {}, D = {}, E = {}, F = {}, G = {};
const grp = (k) => { const g = new THREE.Group(); g.position.set(...WP[k]); worlds[k] = g; scene.add(g); return g; };
const CLOUDS = [];
function buildClouds() {
  setSeed(77);
  for (const k in WP) { const [ox] = WP[k]; let n = 0;
    for (let tries = 0; tries < 40 && n < 6; tries++) {
      const x = (rnd() - 0.5) * 40, y = -6 + rnd() * 16, z = -30 + rnd() * 26;
      if (Math.hypot(x, z) < 13 && y > -5) continue;
      const L = [], m = 3 + Math.floor(rnd() * 4), sz = 0.8 + rnd() * 1.2;
      for (let i = 0; i < m; i++) L.push([(i - m / 2) * sz * 0.8, (rnd() - 0.3) * sz * 0.5, (rnd() - 0.5) * sz, sz * (1 + rnd()), sz * (0.6 + rnd() * 0.6), sz * (1 + rnd() * 0.8), i & 1 ? "#ffffff" : "#eef4ff"]);
      const c = boxes(L, MAT, false); c.castShadow = false; c.receiveShadow = false; c.position.set(ox + x, y, z); scene.add(c); CLOUDS.push({ m: c, w: k, x: ox + x, ph: rnd() * 6 }); n++;
    } }
}

/* A — range */
const HOOK = [[0.556, V3(-2.6, 2.1, -10.2)], [1.111, V3(0.9, 5.2, -10.6)], [1.667, V3(0.4, 0.3, -7.4)]];   // 3 misses (on the beat)
const RAPID = []; { setSeed(5); const n = 97, a = 7.62, b = 12.5, HITS = new Set([14, 27, 38, 47, 56, 64, 71, 79, 86, 96]);
  for (let i = 0; i < n; i++) { const t0 = a + (b - a) * (i / (n - 1)), hit = HITS.has(i);
    let p; if (hit) { const r = i === 96 ? 0 : 0.25 + rnd() * 1.0, ang = rnd() * 6.28; p = V3(Math.cos(ang) * r, 2.55 + Math.sin(ang) * r, -10.12); }
    else { const ang = rnd() * 6.28, r = 1.8 + rnd() * 2.2; p = V3(Math.cos(ang) * r, 2.55 + Math.sin(ang) * r * 0.8, -10.4 - rnd()); }
    RAPID.push({ t0, end: p, hit, rot: [rnd() * 6, rnd() * 6] }); } }
const FLY = 0.72, MUZ = V3(0, 1.55, 2.35);
const ALLSHOTS = HOOK.map(([t0, end]) => ({ t0, end, hit: false, rot: [1, 2] })).concat(RAPID);
const triesAt = (t) => ALLSHOTS.filter((s) => t >= s.t0).length;
const hitsAt = (t) => ALLSHOTS.filter((s) => s.hit && t >= s.t0 + FLY).length;
function buildA() {
  const g = grp("A"); g.add(island(4, 4));
  const ti = island(2, 2); ti.position.set(0, 0.2, -10.6); g.add(ti);
  // cannon (voxel), barrel pivot at (0,1.15,3.2), points to -z
  g.add(boxes([[0, 0.3, 3.3, 1.4, 0.6, 1.6, "#dfe7f2"], [0, 0.62, 3.3, 1.5, 0.06, 1.7, CY], [-0.78, 0.35, 3.0, 0.16, 0.7, 0.7, NV2], [0.78, 0.35, 3.0, 0.16, 0.7, 0.7, NV2],
    [-0.78, 0.35, 3.75, 0.16, 0.5, 0.5, NV2], [0.78, 0.35, 3.75, 0.16, 0.5, 0.5, NV2], [0, 0.85, 3.3, 0.7, 0.5, 0.7, NV]]));
  A.barrel = new THREE.Group(); A.barrel.position.set(0, 1.15, 3.2); g.add(A.barrel);
  A.barrel.add(boxes([[0, 0, -0.55, 0.56, 0.56, 1.5, NV], [0, 0, -1.33, 0.68, 0.68, 0.14, CY], [0, 0.31, -0.4, 0.3, 0.06, 0.9, "#3567b5"], [0, 0, 0.3, 0.7, 0.7, 0.4, "#1f3c62"]]));
  A.flag = new THREE.Group(); A.flag.position.set(0.55, 1.1, 3.0); g.add(A.flag);   // white "give up" flag pops out of the cannon
  A.flag.add(boxes([[0, 0.8, 0, 0.08, 1.6, 0.08, NV], [0.5, 1.3, 0, 0.9, 0.6, 0.04, "#ffffff"], [0.5, 1.3, 0.025, 0.9, 0.08, 0.005, "#d3ddeb"]]));
  // ammo crate + pile (how much volume is loaded)
  g.add(boxes([[2.0, 0.25, 3.4, 1.6, 0.5, 1.6, "#e9cfa8"], [2.0, 0.52, 3.4, 1.66, 0.05, 1.66, "#d8b98e"]]));
  const PL = []; for (let y = 0; y < 8; y++) for (let i = 0; i < 5; i++) for (let j = 0; j < 5; j++) PL.push([(i - 2) * 0.28, 0.14 + y * 0.28, (j - 2) * 0.28, 0.26, 0.26, 0.26, (i + j + y) & 1 ? CY : "#36b8e6"]);
  A.pile = boxes(PL, MAT, false); A.pile.position.set(2.0, 0.55, 3.4); g.add(A.pile);
  // bullseye on a stand on the target island
  g.add(boxes([[-0.9, 0.9, -10.5, 0.14, 1.6, 0.14, "#c3cfe2"], [0.9, 0.9, -10.5, 0.14, 1.6, 0.14, "#c3cfe2"]]));
  A.target = bullseye(1.55); A.target.position.set(0, 2.55, -10.3); g.add(A.target);
  A.tglow = glow("#5fe2ff", 3.4, 3.4); A.tglow.position.set(0, 2.55, -10.0); A.tglow.material.opacity = 0; g.add(A.tglow);
  A.shots = ALLSHOTS.map((s) => { const m = cube(); m.visible = false; g.add(m); return m; });
  A.conf = []; setSeed(41); for (let i = 0; i < 40; i++) { const c = boxes([[0, 0, 0, 0.12, 0.12, 0.05, [CY, "#ffffff", NV, "#7fe3ff"][i % 4]]], MAT, false); c.castShadow = false; c.visible = false; g.add(c);
    A.conf.push({ c, v: V3((rnd() - 0.5) * 6, 2 + rnd() * 4, 1 + rnd() * 3), r: rnd() * 9 }); }
}
function shotPos(s, t) { // flight from the muzzle; misses keep falling after the target plane
  const u = (t - s.t0) / FLY; if (u < 0) return null;
  const end = s.end, h = 1.6 + 0.6 * Math.abs(end.x) * 0.2;
  if (u <= 1) { const p = MUZ.clone().lerp(end, u); p.y += 4 * h * u * (1 - u); return p; }
  if (s.hit) return end.clone();
  const tau = (u - 1) * FLY, v = end.clone().sub(MUZ).divideScalar(FLY); v.y -= 4 * h / FLY;
  const p = end.clone().addScaledVector(v, tau); p.y -= 4.9 * tau * tau; return tau < 1.6 ? p : null;
}
function animA(t) {
  const droop = U(t, 2.7, 3.1, "out") * (1 - U(t, 5.6, 6.0, "back"));
  A.barrel.rotation.x = 0.36 - 0.5 * droop + (t > 7.5 && t < 12.6 ? 0.02 * Math.sin(t * 60) : 0);
  for (const s of ALLSHOTS) { const k = (t - s.t0); if (k > 0 && k < 0.12) A.barrel.position.z = 3.2 + 0.12 * (1 - k / 0.12); }
  if (!ALLSHOTS.some((s) => t - s.t0 > 0 && t - s.t0 < 0.12)) A.barrel.position.z = 3.2;
  const fl = spring(t, 2.72) * (1 - U(t, 5.4, 5.7)); A.flag.visible = fl > 0.01; A.flag.scale.set(1, S(fl), 1);
  A.flag.rotation.z = 0.08 * Math.sin(t * 5);
  // the pile: grows on "jumlah percobaan", then empties shot by shot
  const load = spring(t, 6.0, 10, 6), used = triesAt(t) / 100;
  A.pile.scale.set(1, S(0.12 + 0.88 * load * (1 - 0.9 * U(t, 7.6, 12.6, "lin"))), 1); void used;
  ALLSHOTS.forEach((s, i) => { const m = A.shots[i], p = shotPos(s, t); m.visible = !!p; if (!p) return; m.position.copy(p);
    const u = Math.min(1, (t - s.t0) / FLY); m.rotation.set(s.rot[0] * u * 3, s.rot[1] * u * 3, 0);
    const sq = s.hit && t > s.t0 + FLY ? 1 + 0.35 * Math.exp(-(t - s.t0 - FLY) * 10) * Math.cos((t - s.t0 - FLY) * 30) : 1;
    m.scale.set(sq, 2 - sq, s.hit && t > s.t0 + FLY ? 0.6 : 1); if (s.hit && t > s.t0 + FLY) m.position.z = -10.12; });
  const big = U(t, 13.2, 13.35) * (1 - U(t, 14.0, 14.6));
  A.tglow.material.opacity = 0.45 * big + 0.25 * U(t, 12.9, 13.2) * (1 - U(t, 13.6, 14));
  A.target.scale.setScalar(1 + 0.08 * Math.exp(-Math.max(0, t - 13.22) * 6) * (t > 13.22 ? Math.cos((t - 13.22) * 25) : 0));
  A.conf.forEach((q, i) => { const tau = t - 13.24 - (i % 5) * 0.02; q.c.visible = tau > 0 && tau < 1.5; if (!q.c.visible) return;
    q.c.position.set(q.v.x * tau * 0.6, 2.6 + q.v.y * tau - 4.9 * tau * tau, -10 + q.v.z * tau * 0.7); q.c.rotation.set(q.r + tau * 9, tau * 7, 0); q.c.scale.setScalar(Math.min(1, (1.5 - tau) * 2)); });
}

/* B — content wall (10 x 10) */
let TX = {};
function makeTextures() {
  const pal = [["#294b77", "#3567b5"], ["#1f9fd6", "#7fd8f5"], ["#0a0d2c", "#294b77"], ["#5b8fd6", "#a9c6ee"], ["#3567b5", "#01ccf7"], ["#1f3c62", "#5b8fd6"], ["#7aa7e0", "#d3e4fa"], ["#294b77", "#01ccf7"]];
  TX.thumb = pal.map(([a, b], k) => ctex(160, 100, (g, w, h) => { const gr = g.createLinearGradient(0, 0, w, h); gr.addColorStop(0, a); gr.addColorStop(1, b); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    g.fillStyle = "rgba(255,255,255,.92)"; g.beginPath(); g.moveTo(66, 30); g.lineTo(66, 70); g.lineTo(100, 50); g.closePath(); g.fill();
    g.fillStyle = "rgba(255,255,255,.55)"; rr(g, 10, 82, 60 + (k * 13) % 50, 8, 4); g.fill(); }));
  TX.ad = Array.from({ length: 10 }, (_, i) => ctex(320, 200, (g, w, h) => { const dark = i % 3 === 0;
    g.fillStyle = dark ? NV2 : "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = [CY, NV, "#3567b5", "#7fe3ff"][i % 4]; g.fillRect(0, 0, 18, h);
    g.font = `700 64px ${FONT}`; g.fillStyle = dark ? "#ffffff" : NV2; g.fillText("V" + (i + 1), 40, 82);
    g.fillStyle = dark ? "rgba(255,255,255,.5)" : "#c9d6e8"; rr(g, 40, 104, 200 - (i * 17) % 90, 16, 8); g.fill(); rr(g, 40, 132, 150 - (i * 29) % 70, 16, 8); g.fill();
    g.fillStyle = CY; rr(g, 40, 160, 90, 24, 12); g.fill(); }));
  TX.ad1 = ctex(640, 400, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = NV2; g.fillRect(0, 0, w, 86);
    g.font = `700 50px ${FONT}`; g.fillStyle = "#ffffff"; g.fillText("1 MATERI IKLAN", 34, 62);
    g.fillStyle = "#c9d6e8"; rr(g, 34, 130, 520, 34, 17); g.fill(); rr(g, 34, 190, 400, 34, 17); g.fill(); g.fillStyle = CY; rr(g, 34, 280, 220, 70, 35); g.fill(); });
  TX.day = Array.from({ length: 30 }, (_, i) => [0, 1, 2].map((on) => ctex(128, 128, (g, w) => { g.fillStyle = on ? CY : "#ffffff"; g.fillRect(0, 0, w, w);
    g.lineWidth = 6; g.strokeStyle = on ? "#7fe3ff" : "#c9d6e8"; g.strokeRect(3, 3, w - 6, w - 6);
    if (on < 2) { g.font = `700 54px ${FONT}`; g.textAlign = "center"; g.fillStyle = on ? NV2 : NV; g.fillText(String(i + 1), 64, 84); } })));
  TX.btn = ["POSTING", "KIRIM"].map((s) => ctex(512, 256, (g, w, h) => { g.fillStyle = CY; g.fillRect(0, 0, w, h); g.font = `700 104px ${FONT}`; g.textAlign = "center"; g.fillStyle = NV2; g.fillText(s, w / 2, 166); }));
  TX.btnBlank = ctex(64, 32, (g, w, h) => { g.fillStyle = CY; g.fillRect(0, 0, w, h); });
  TX.check = ctex(128, 128, (g) => { g.fillStyle = "#ffffff"; g.beginPath(); g.arc(64, 64, 58, 0, 7); g.fill(); g.fillStyle = CY; g.beginPath(); g.arc(64, 64, 48, 0, 7); g.fill();
    g.strokeStyle = "#ffffff"; g.lineWidth = 14; g.lineCap = "round"; g.lineJoin = "round"; g.beginPath(); g.moveTo(38, 66); g.lineTo(56, 84); g.lineTo(90, 46); g.stroke(); });
  TX.note = ctex(256, 320, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = NV; g.fillRect(0, 0, w, 52); g.fillStyle = CY; g.fillRect(20, 20, 40, 14); });
}
function buildB() {
  const g = grp("B"); g.add(island(7, 3));
  g.add(boxes([[0, 3.25, -0.4, 9.6, 6.6, 0.3, "#f3f6fb"], [0, 3.25, -0.24, 9.2, 6.2, 0.02, "#dfe7f2"], [0, 0.2, -0.4, 10, 0.4, 0.9, NV], [0, 6.6, -0.4, 9.7, 0.12, 0.42, CY],
    [-4.6, 0.6, 0.2, 0.3, 1.2, 0.3, "#c3cfe2"], [4.6, 0.6, 0.2, 0.3, 1.2, 0.3, "#c3cfe2"]]));
  B.tiles = [];
  for (let r = 0; r < 10; r++) for (let c = 0; c < 10; c++) {
    const i = r * 10 + c, k = Math.floor(hash(i) * 8), grpT = new THREE.Group();
    const back = boxes([[0, 0, -0.04, 0.82, 0.52, 0.08, "#c3cfe2"]], MAT, false); back.castShadow = false; grpT.add(back);
    const face = new THREE.Mesh(new THREE.PlaneGeometry(0.8, 0.5), new THREE.MeshStandardMaterial({ map: TX.thumb[k], roughness: 0.6 })); face.position.z = 0.002; grpT.add(face);
    grpT.position.set(-4.05 + c * 0.9, 6.05 - r * 0.6, -0.18); grpT.visible = false; g.add(grpT); B.tiles.push(grpT);
  }
  B.rise = [33, 66, 87].map((i) => { const s = glow("#5fe2ff", 1.6, 1.1); s.material.opacity = 0; g.add(s); return { i, s }; });
}
const TORD = (() => { const o = [...Array(100).keys()].sort((p, q) => { const d = (i) => Math.hypot((i % 10) - 4.5, (Math.floor(i / 10) - 4.5) * 1.4) + hash(i) * 0.3; return d(p) - d(q); });
  const r = []; o.forEach((i, k) => (r[i] = k)); return r; })();
const TILE_T = (i) => { const k = TORD[i]; return k < 5 ? 15.5 + k * 0.07 : 16.7 + ((k - 5) / 94) * 1.05; };
function animB(t) {
  B.tiles.forEach((m, i) => { const t0 = TILE_T(i), u = spring(t, t0, 16, 9); m.visible = t > t0; if (!m.visible) return;
    m.scale.setScalar(S(Math.min(1.12, u))); m.position.z = -0.18 + 0.5 * (1 - Math.min(1, u)); });
  B.rise.forEach(({ i, s }, k) => { const t0 = 17.6 + k * 0.2, u = spring(t, t0, 10, 6), m = B.tiles[i];
    const z = -0.18 + (0.9 + 0.5 * (k === 1)) * u; m.position.z = Math.max(m.position.z, z); m.scale.setScalar(1 + (0.25 + 0.25 * (k === 1)) * Math.min(1.1, u));
    s.position.set(m.position.x, m.position.y, z - 0.1); s.material.opacity = 0.7 * Math.min(1, u); });
}

/* C — follow-up hub */
const HOUSES = [-2.6, -1.55, -0.5, 0.5, 1.55, 2.6].map((a, i) => ({ a, p: V3(Math.sin(a * 0.48) * 4.4, 0, -Math.cos(a * 0.48) * 3.0 - 0.4) }));
const WAVES = [20.2, 22.32, 22.88, 23.44];          // follow-up waves (1x, then 2x..4x)
const REPLY = [[1, 3], [4, 3], [2, 2], [5, 3]];     // [house, wave] that gets a reply (illustrative)
function buildC() {
  const g = grp("C"); g.add(island(6, 4));
  // shop (centre front)
  g.add(boxes([[0, 0.7, 2.2, 2.0, 1.4, 1.5, "#ffffff"], [0, 1.5, 2.2, 2.3, 0.2, 1.8, NV], [0, 0.5, 2.96, 0.7, 1.0, 0.04, "#1f3c62"], [-0.7, 0.85, 2.96, 0.4, 0.4, 0.04, "#bfe9ff"], [0.7, 0.85, 2.96, 0.4, 0.4, 0.04, "#bfe9ff"],
    [0, 1.72, 2.2, 1.2, 0.24, 0.3, "#f3f6fb"]]));
  C.sign = new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.16, 0.04), emi(CY, 2)); C.sign.position.set(0, 1.72, 2.37); g.add(C.sign);
  C.shutter = boxes([[0, 0, 0, 0.74, 1.0, 0.03, "#8a9bb8"]], MAT, false); C.shutter.position.set(0, 0.5, 2.99); g.add(C.shutter);
  C.houses = HOUSES.map(({ p }, i) => { const h = new THREE.Group(); h.position.copy(p); h.lookAt(0, 0, 2.2); g.add(h);
    const col = ["#3567b5", "#5b8fd6", NV, "#7aa7e0", "#1f9fd6", "#3567b5"][i];
    h.add(boxes([[0, 0.45, 0, 1.0, 0.9, 0.9, "#f3f6fb"], [0, 1.0, 0, 1.15, 0.2, 1.05, col], [0, 1.2, 0, 0.8, 0.2, 0.8, col], [0, 1.36, 0, 0.4, 0.14, 0.5, col], [0, 0.3, 0.46, 0.28, 0.6, 0.03, "#8a6a4a"]]));
    const win = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.24, 0.03), new THREE.MeshStandardMaterial({ color: 0xdfe7f2, emissive: 0x01ccf7, emissiveIntensity: 0, roughness: 0.4 }));
    win.position.set(0.3, 0.6, 0.46); h.add(win);
    const ck = new THREE.Sprite(new THREE.SpriteMaterial({ map: TX.check, transparent: true, depthTest: false, toneMapped: false })); ck.renderOrder = 12; ck.visible = false; g.add(ck);
    return { h, win, ck }; });
  const bub = boxes([[0, 0, 0, 0.56, 0.36, 0.14, "#ffffff"], [-0.14, -0.22, 0, 0.12, 0.1, 0.12, "#ffffff"], [-0.14, 0, 0.075, 0.08, 0.08, 0.02, CY], [0, 0, 0.075, 0.08, 0.08, 0.02, CY], [0.14, 0, 0.075, 0.08, 0.08, 0.02, CY]], MAT, false);
  C.bubs = []; WAVES.forEach((w, k) => HOUSES.forEach((h, i) => { const m = bub.clone(); m.visible = false; g.add(m); C.bubs.push({ m, t0: w + i * 0.045, i }); }));
}
function animC(t) {
  const off = U(t, 21.45, 21.75) * (1 - U(t, 22.05, 22.3));
  C.sign.material.emissiveIntensity = 2 * (1 - off); C.shutter.scale.y = S(off); C.shutter.position.y = 1.0 - 0.5 * off;
  const FROM = V3(0, 2.0, 2.2);
  C.bubs.forEach(({ m, t0, i }) => { const u = (t - t0) / 0.6; m.visible = u > 0 && u < 1.25; if (!m.visible) return;
    const to = HOUSES[i].p.clone(); to.y = 1.9; const k = EZ.io(Math.min(1, u)); const p = FROM.clone().lerp(to, k); p.y += 1.3 * Math.sin(Math.PI * Math.min(1, u));
    m.position.copy(p); m.lookAt(cam.position); m.scale.setScalar(1.8 * S(u < 1 ? Math.min(1, u * 5) : 1 - (u - 1) * 4)); });
  C.houses.forEach((h, i) => { const r = REPLY.find(([hi]) => hi === i); const t0 = r ? WAVES[r[1]] + i * 0.045 + 0.62 : 1e9, u = spring(t, t0, 14, 8);
    h.win.material.emissiveIntensity = 1.6 * Math.min(1, u); h.ck.visible = u > 0.01;
    const p = HOUSES[i].p; h.ck.position.set(p.x, 2.05 + 0.06 * Math.sin(t * 4 + i), p.z); h.ck.scale.setScalar(S(0.62 * Math.min(1.1, u)));
    const land = WAVES.some((w) => { const d = t - (w + i * 0.045 + 0.6); return d > 0 && d < 0.25; });
    h.h.scale.set(1, land ? 1 - 0.06 * Math.sin(Math.PI * 4 * ((t * 10) % 0.25)) : 1, 1); });
}
const followAt = (t) => WAVES.filter((w) => t >= w).length;
const repliesAt = (t) => REPLY.filter(([i, w]) => t >= WAVES[w] + i * 0.045 + 0.62).length;

/* D — ad billboards */
const BARS = [0.5, 0.8, 0.6, 1.1, 0.55, 0.9, 2.0, 0.75, 0.45, 0.7], WIN = 6;
const BB = Array.from({ length: 10 }, (_, i) => { const row = i < 5 ? 0 : 1, c = i % 5; return V3(-3.6 + c * 1.8, row ? 0.95 : 0, row ? -1.6 : 0.6); });
function buildD() {
  const g = grp("D"); g.add(island(6, 4));
  D.big = new THREE.Group(); g.add(D.big);
  D.big.add(boxes([[0, 1.0, -0.06, 0.2, 2.0, 0.2, "#c3cfe2"], [0, 2.45, -0.12, 4.2, 2.7, 0.16, NV]]));
  const bf = new THREE.Mesh(new THREE.PlaneGeometry(4.0, 2.5), new THREE.MeshStandardMaterial({ map: TX.ad1, roughness: 0.7 })); bf.position.set(0, 2.45, -0.03); D.big.add(bf);
  g.add(boxes([[0, 0.45, -1.6, 9.4, 0.9, 1.4, "#f3f6fb"], [0, 0.92, -1.6, 9.44, 0.05, 1.44, CY], [0, 0.45, -0.89, 9.4, 0.9, 0.02, "#dfe7f2"]]));
  D.boards = BB.map((p, i) => { const b = new THREE.Group(); b.position.copy(p); g.add(b);
    b.add(boxes([[0, 0.45, -0.05, 0.1, 0.9, 0.1, "#c3cfe2"], [0, 1.25, -0.09, 1.56, 1.0, 0.1, NV]]));
    const f = new THREE.Mesh(new THREE.PlaneGeometry(1.48, 0.92), new THREE.MeshStandardMaterial({ map: TX.ad[i], roughness: 0.7 })); f.position.set(0, 1.25, -0.035); b.add(f);
    const bar = new THREE.Mesh(new THREE.BoxGeometry(0.34, 1, 0.34), new THREE.MeshStandardMaterial({ color: i === WIN ? 0x01ccf7 : 0x7aa7e0, emissive: i === WIN ? 0x01a8d6 : 0x000000, emissiveIntensity: 0.5, roughness: 0.4 }));
    bar.position.set(0.98, 0, 0); bar.castShadow = true; b.add(bar);
    b.visible = false; return { b, bar }; });
  const coin = boxes([[0, 0, 0, 0.34, 0.08, 0.34, "#ffc531"], [0, 0.041, 0, 0.2, 0.005, 0.2, "#ffdb6e"]], MAT, false);
  D.coins = []; setSeed(9); for (let i = 0; i < 40; i++) { const m = coin.clone(); g.add(m); D.coins.push({ m, k: i % 10, h: Math.floor(i / 10), j: [rnd() - 0.5, rnd() - 0.5] }); }
  D.crown = boxes([[0, 0, 0, 0.6, 0.14, 0.6, "#ffc531"], [-0.22, 0.16, 0, 0.12, 0.2, 0.12, "#ffc531"], [0, 0.2, 0, 0.12, 0.26, 0.12, "#ffc531"], [0.22, 0.16, 0, 0.12, 0.2, 0.12, "#ffc531"], [0, 0.07, 0.31, 0.1, 0.07, 0.02, CY]], MAT, false);
  g.add(D.crown); D.wglow = glow("#5fe2ff", 3.0, 3.0); D.wglow.material.opacity = 0; g.add(D.wglow);
}
function animD(t) {
  const split = U(t, 27.98, 28.5, "io"), sp = spring(t, 28.0, 12, 7);
  D.big.visible = split < 0.98; D.big.scale.setScalar(S(1 - split)); D.big.position.y = -0.4 * split;
  D.boards.forEach(({ b, bar }, i) => { const u = spring(t, 28.05 + i * 0.05, 13, 7); b.visible = u > 0.005; b.scale.setScalar(S(Math.min(1.1, u)));
    const hb = BARS[i] * U(t, 29.55 + i * 0.03, 30.0 + i * 0.03, "out"); bar.scale.y = S(hb); bar.position.y = hb / 2; bar.visible = hb > 0.01;
    const win = i === WIN ? spring(t, 30.14, 10, 6) : 0; b.position.y = BB[i].y + 0.45 * Math.min(1.1, win); b.position.z = BB[i].z + 0.6 * Math.min(1, win);
    const dim = i === WIN ? 0 : U(t, 30.14, 30.5); if (dim > 0) b.scale.multiplyScalar(1 - 0.12 * dim); });
  D.coins.forEach(({ m, k, h, j }) => { const pile = V3(j[0] * 0.5 + (k - 4.5) * 0.12, 0.04 + (h * 10 + k) * 0.05 * 0.55, 1.5 + j[1] * 0.4);
    const dst = BB[k].clone().add(V3(-0.5, 0.04 + h * 0.085, 0.35)); const u = U(t, 28.1 + k * 0.04, 28.7 + k * 0.04, "io");
    const p = pile.lerp(dst, u); p.y += 0.3 * Math.sin(Math.PI * u); m.position.copy(p); m.rotation.y = u * 3 + k; m.visible = t > 25.0; void sp; });
  const w = spring(t, 30.18, 10, 6), bw = D.boards[WIN].b;
  D.crown.visible = w > 0.01; D.crown.position.set(bw.position.x, bw.position.y + 2.05 + 0.6 * (1 - Math.min(1, w)), bw.position.z); D.crown.scale.setScalar(S(Math.min(1.1, w))); D.crown.rotation.y = t * 1.5;
  D.wglow.position.set(bw.position.x, bw.position.y + 1.25, bw.position.z - 0.3); D.wglow.material.opacity = 0.7 * Math.min(1, w);
}

/* E — 30-day grid + bars (catat -> perbaiki) */
const DAY = (i) => 31.78 + i * 0.052;
function buildE() {
  const g = grp("E"); g.add(island(5, 4));
  g.add(boxes([[0, 0.12, 0, 6.9, 0.24, 5.9, NV], [0, 0.25, 0, 7.0, 0.03, 6.0, CY]]));
  E.tiles = []; for (let i = 0; i < 30; i++) { const r = Math.floor(i / 6), c = i % 6;
    const m = new THREE.Group(); m.position.set(-2.75 + c * 1.1, 0.3, -2.2 + r * 1.1); g.add(m);
    m.add(boxes([[0, 0.06, 0, 0.98, 0.12, 0.98, "#f3f6fb"]], MAT, false));
    const top = new THREE.Mesh(new THREE.PlaneGeometry(0.9, 0.9), new THREE.MeshStandardMaterial({ map: TX.day[i][0], roughness: 0.6, emissive: 0xffffff, emissiveMap: TX.day[i][0], emissiveIntensity: 0.15 }));
    top.rotation.x = -Math.PI / 2; top.position.y = 0.125; m.add(top);
    const bar = new THREE.Mesh(new THREE.BoxGeometry(0.44, 1, 0.44), new THREE.MeshStandardMaterial({ color: 0x01ccf7, emissive: 0x01a8d6, emissiveIntensity: 0.35, roughness: 0.4 }));
    bar.castShadow = true; bar.visible = false; m.add(bar); E.tiles.push({ m, top, bar }); }
  // dumbbell + bottle (olahraga), notebook (catatan)
  E.bell = boxes([[0, 0, 0, 1.0, 0.12, 0.12, "#8a9bb8"], [-0.5, 0, 0, 0.16, 0.5, 0.5, NV2], [0.5, 0, 0, 0.16, 0.5, 0.5, NV2], [-0.36, 0, 0, 0.1, 0.38, 0.38, NV], [0.36, 0, 0, 0.1, 0.38, 0.38, NV]]);
  E.bell.position.set(2.4, 0.3, -3.55); g.add(E.bell);
  g.add(boxes([[3.6, 0.45, -3.5, 0.36, 0.9, 0.36, "#bfe9ff"], [3.6, 0.95, -3.5, 0.2, 0.12, 0.2, NV]]));
  E.note = new THREE.Group(); E.note.position.set(-3.6, 0.0, -3.75); E.note.rotation.y = 0.3; g.add(E.note);
  E.note.add(boxes([[0, 0.2, -0.12, 0.3, 0.4, 0.2, "#c3cfe2"], [0, 1.05, -0.04, 1.36, 1.66, 0.06, NV]]));
  const np = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 1.5), new THREE.MeshStandardMaterial({ map: TX.note, roughness: 0.8 })); np.position.set(0, 1.05, 0.0); E.note.add(np);
  E.lines = []; for (let k = 0; k < 6; k++) { const l = boxes([[0, 0, 0, 1, 0.07, 0.02, k % 2 ? NV : "#3567b5"]], MAT, false); l.castShadow = false; l.position.set(-0.45, 1.25 - k * 0.17, 0.02); E.note.add(l); E.lines.push(l); }
  E.wave = glow("#5fe2ff", 2.4, 2.4); E.wave.material.opacity = 0; g.add(E.wave);
}
const BARH = (i) => 0.35 + i * 0.075 + 0.12 * Math.sin(i * 2.3);
function animE(t) {
  E.tiles.forEach(({ m, top, bar }, i) => { const u = spring(t, DAY(i), 16, 8); const on = t >= DAY(i);
    const bt0 = 35.62 + i * 0.03; top.material.map = TX.day[i][t >= bt0 - 0.02 ? 2 : on ? 1 : 0]; top.material.emissiveMap = top.material.map; top.material.emissiveIntensity = on ? 0.55 : 0.15;
    m.position.y = 0.3 + 0.14 * Math.min(1.2, u) * (1 - U(t, DAY(i) + 0.25, DAY(i) + 0.55)) ;
    const pulse = Math.exp(-Math.pow((t - (33.4 + i * 0.03)) / 0.08, 2)); m.position.y += 0.12 * pulse;
    const bt = 35.62 + i * 0.03, hb = BARH(i) * U(t, bt, bt + 0.45, "out") + 0.25 * U(t, 36.86 + i * 0.02, 37.2 + i * 0.02, "out") * (i / 29);
    bar.visible = hb > 0.01; bar.scale.y = S(hb); bar.position.y = 0.12 + hb / 2; });
  E.bell.position.y = 0.3 + 0.35 * Math.max(0, Math.sin((t - 31.8) * 7)) * U(t, 31.8, 32.0) * (1 - U(t, 34.6, 34.9)); E.bell.rotation.z = 0.1 * Math.sin(t * 7);
  { const u = spring(t, 34.95, 12, 7); E.note.scale.setScalar(S(Math.min(1.08, u))); E.note.visible = u > 0.01; }
  E.lines.forEach((l, k) => { const u = U(t, 35.3 + k * 0.17, 35.55 + k * 0.17, "out"); l.scale.x = S(u * (0.6 + 0.4 * hash(k))); l.position.x = -0.45 + 0.5 * l.scale.x * 0.9; l.visible = u > 0.01; });
}
const daysAt = (t) => Math.max(0, Math.min(30, Math.floor((t - 31.78) / 0.052) + 1));

/* F — AI desk with a live chat window on the monitor (View(t)) */
const PROMPT = "Bikin 10 draf naskah, 10 variasi iklan, 10 pesan follow-up";
const SCR = { w: 1024, h: 600 };
function buildF() {
  const g = grp("F"); g.add(island(5, 4));
  g.add(boxes([[0, 0.45, 0.6, 7.2, 0.1, 2.2, "#e9cfa8"], [-3.3, 0.2, 0.6, 0.2, 0.4, 2.0, "#d8b98e"], [3.3, 0.2, 0.6, 0.2, 0.4, 2.0, "#d8b98e"],
    [0, 1.0, -0.7, 0.5, 1.0, 0.3, "#c3cfe2"], [0, 0.55, -0.7, 1.6, 0.1, 0.9, "#c3cfe2"], [0, 3.15, -0.82, 6.1, 3.7, 0.22, NV2]]));
  const c = document.createElement("canvas"); c.width = SCR.w; c.height = SCR.h; F.g2 = c.getContext("2d");
  F.tex = new THREE.CanvasTexture(c); F.tex.colorSpace = THREE.SRGBColorSpace; F.tex.anisotropy = 8;
  const scr = new THREE.Mesh(new THREE.PlaneGeometry(5.9, 3.46), new THREE.MeshBasicMaterial({ map: F.tex, toneMapped: false })); scr.position.set(0, 3.15, -0.7); g.add(scr);
  const card = boxes([[0, 0, 0, 0.9, 0.05, 0.62, "#ffffff"], [-0.1, 0.027, -0.12, 0.6, 0.005, 0.06, NV], [-0.15, 0.027, 0.0, 0.5, 0.005, 0.05, "#a9c6ee"], [-0.2, 0.027, 0.1, 0.4, 0.005, 0.05, "#a9c6ee"]], MAT, false);
  F.stacks = [-2.3, 0, 2.3].map((x, s) => Array.from({ length: 10 }, (_, k) => { const m = card.clone(); m.visible = false; g.add(m); return { m, x, s, k }; }));
  F.lbl = ["DRAF NASKAH", "VARIASI IKLAN", "PESAN FOLLOW-UP"].map((s) => { const l = label(s, NV2, "#fff", 0.34); g.add(l); return l; });
}
const STACK_T = [40.45, 41.28, 42.25];
function drawScreen(t) {
  const g = F.g2, w = SCR.w, h = SCR.h; g.save();
  g.fillStyle = "#f4f8ff"; g.fillRect(0, 0, w, h); g.fillStyle = NV2; g.fillRect(0, 0, w, 64);
  [[30, "#c9d6e8"], [58, "#c9d6e8"], [86, "#c9d6e8"]].forEach(([x, c]) => { g.fillStyle = c; g.beginPath(); g.arc(x, 32, 9, 0, 7); g.fill(); });
  g.font = `700 28px ${FONT}`; g.fillStyle = "#ffffff"; g.fillText("Asisten AI · volume konten", 120, 42);
  // input box + typing
  const n = Math.max(0, Math.min(PROMPT.length, Math.floor((t - 38.15) * 42)));
  g.fillStyle = "#ffffff"; rr(g, 28, 84, w - 220, 76, 18); g.fill(); g.lineWidth = 3; g.strokeStyle = t > 38.1 && t < 39.9 ? CY : "#c9d6e8"; rr(g, 28, 84, w - 220, 76, 18); g.stroke();
  g.font = `400 25px ${FONT}`; g.fillStyle = NV2; const txt = PROMPT.slice(0, n);
  let shown = txt; while (g.measureText(shown).width > w - 270 && shown.length) shown = shown.slice(1);
  g.fillText(n ? shown : "", 48, 131); if (!n) { g.fillStyle = "#8a97b3"; g.fillText("Tulis perintah…", 48, 131); }
  if (t > 38.1 && t < 39.9 && Math.floor(t * 3) % 2 === 0) { g.fillStyle = CY; g.fillRect(52 + g.measureText(n ? shown : "").width, 104, 4, 38); }
  const press = U(t, 39.72, 39.8) * (1 - U(t, 39.86, 39.95));
  g.fillStyle = press > 0.5 ? "#0aa7d6" : CY; rr(g, w - 176, 84, 150, 76, 18); g.fill(); g.font = `700 28px ${FONT}`; g.fillStyle = NV2; g.fillText("Kirim", w - 140, 131);
  // results
  if (t > 39.9) {
    if (t < 40.4) { g.font = `400 26px ${FONT}`; g.fillStyle = NV; g.fillText("AI sedang menulis" + ".".repeat(1 + (Math.floor(t * 8) % 3)), 40, 220); }
    const rows = [["Draf naskah", STACK_T[0]], ["Variasi iklan", STACK_T[1]], ["Pesan follow-up", STACK_T[2]]];
    rows.forEach(([nm, t0], i) => { if (t < t0) return; const y = 190 + i * 118, k = Math.min(10, Math.floor((t - t0) / 0.07) + 1);
      g.fillStyle = "#ffffff"; rr(g, 28, y, w - 56, 98, 18); g.fill(); g.fillStyle = CY; rr(g, 28, y, 12, 98, 6); g.fill();
      g.font = `700 32px ${FONT}`; g.fillStyle = NV2; g.fillText(nm, 64, y + 44); g.font = `400 24px ${FONT}`; g.fillStyle = NV; g.fillText("draf siap dicek, kamu yang putuskan", 64, y + 80);
      g.font = `700 40px ${FONT}`; g.textAlign = "right"; g.fillStyle = NV; g.fillText(k + "/10", w - 56, y + 62); g.textAlign = "left";
      for (let j = 0; j < 10; j++) { g.fillStyle = j < k ? CY : "#dfe7f2"; rr(g, w - 430 + j * 22, y + 70, 16, 12, 4); g.fill(); } });
  }
  // scripted cursor (arrives early, presses, glides on a soft curve)
  const cx = keys(t, [[38.0, [700, 470]], [39.2, [700, 470]], [39.7, [w - 100, 124], "io"], [40.3, [w - 100, 124]], [41.0, [760, 420], "io"]]);
  if (t > 38.0) { g.save(); g.translate(cx[0], cx[1]); const sc = 1 - 0.15 * press; g.scale(sc, sc); g.fillStyle = NV2; g.strokeStyle = "#ffffff"; g.lineWidth = 3;
    g.beginPath(); g.moveTo(0, 0); g.lineTo(0, 40); g.lineTo(11, 30); g.lineTo(19, 47); g.lineTo(26, 44); g.lineTo(18, 27); g.lineTo(32, 27); g.closePath(); g.fill(); g.stroke(); g.restore(); }
  g.restore(); F.tex.needsUpdate = true;
}
function animF(t) {
  drawScreen(t);
  F.stacks.forEach((st, s) => st.forEach(({ m, x, k }) => { const t0 = STACK_T[s] + k * 0.07, u = U(t, t0, t0 + 0.28, "out"); m.visible = u > 0;
    m.position.set(x, 0.53 + k * 0.06 + 1.6 * (1 - u), 1.15 + 1.0 * (1 - u)); m.rotation.set(0.6 * (1 - u), (hash(k + s * 10) - 0.5) * 0.2, 0); }));
  F.lbl.forEach((l, s) => { const u = spring(t, STACK_T[s], 14, 8); setLabel(l, Math.min(1.08, u)); l.position.set([-2.3, 0, 2.3][s], 1.55, 1.25); });
}
const draftsAt = (t) => STACK_T.reduce((a, t0) => a + Math.max(0, Math.min(10, Math.floor((t - t0) / 0.07) + 1)), 0);

/* G — buttons + 30-step spiral staircase to the target summit */
const STEP = (i) => { const a = 1.2 - i * 0.25; return { a, p: V3(Math.cos(a) * 2.6, 0.32 + i * 0.3, -3.2 + Math.sin(a) * 2.6) }; };
const HOP0 = 47.62, HOP = 0.118;
function buildG() {
  const g = grp("G"); g.add(island(5, 6));
  g.add(boxes([[0, 4.8, -3.2, 0.8, 9.6, 0.8, "#dfe7f2"], [0, 9.7, -3.2, 3.4, 0.3, 3.4, NV], [0, 9.86, -3.2, 3.44, 0.05, 3.44, CY]]));
  G.steps = []; for (let i = 0; i < 30; i++) { const { a, p } = STEP(i); const s = new THREE.Group(); s.position.copy(p); s.rotation.y = -a; g.add(s);
    s.add(boxes([[0, -0.02, 0, 1.6, 0.2, 0.7, NV], [0, 0.08, 0, 1.5, 0.02, 0.62, "#f3f6fb"], [0.81, -0.02, 0, 0.04, 0.2, 0.72, CY], [-0.95, 0, 0, 0.3, 0.12, 0.3, "#c3cfe2"]]));
    const lit = new THREE.Mesh(new THREE.BoxGeometry(1.62, 0.03, 0.72), new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x01ccf7, emissiveIntensity: 0, roughness: 0.4 })); lit.position.y = 0.095; s.add(lit);
    G.steps.push({ s, lit }); }
  G.dayLbl = [[0, "HARI 1"], [14, "HARI 15"], [29, "HARI 30"]].map(([i, s]) => { const l = label(s, NV2, "#fff", 0.3); g.add(l); const a = STEP(i).a; l.position.set(Math.cos(a) * 2.3, STEP(i).p.y + 1.05, -3.2 + Math.sin(a) * 2.3); return { l, i }; });
  G.target = bullseye(1.1, 0.12); G.target.position.set(0, 11.2, -3.6); g.add(G.target);
  g.add(boxes([[-0.75, 10.4, -3.75, 0.12, 1.1, 0.12, "#c3cfe2"], [0.75, 10.4, -3.75, 0.12, 1.1, 0.12, "#c3cfe2"]]));
  G.tglow = glow("#5fe2ff", 3.0, 3.0); G.tglow.position.set(0, 11.2, -3.3); G.tglow.material.opacity = 0; g.add(G.tglow);
  // buttons
  g.add(boxes([[0, 0.3, 3.0, 5.6, 0.6, 2.0, NV], [0, 0.62, 3.0, 5.7, 0.05, 2.1, CY]]));
  G.btn = [-1.35, 1.35].map((x, k) => { const b = new THREE.Group(); b.position.set(x, 0.65, 3.0); g.add(b);
    b.add(boxes([[0, 0.25, 0, 2.3, 0.5, 1.5, "#ffffff"]]));
    const top = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 1.1), new THREE.MeshStandardMaterial({ map: TX.btn[k], emissive: 0xffffff, emissiveMap: TX.btn[k], emissiveIntensity: 0.25, roughness: 0.5 }));
    top.rotation.x = -Math.PI / 2; top.position.y = 0.505; b.add(top);
    const ring = new THREE.Mesh(new THREE.RingGeometry(0.9, 1.05, 48), new THREE.MeshBasicMaterial({ color: 0x01ccf7, transparent: true, opacity: 0, depthWrite: false, side: THREE.DoubleSide, toneMapped: false }));
    ring.rotation.x = -Math.PI / 2; ring.position.y = 0.01; b.add(ring); return { b, top, ring }; });
  G.cube = cube(1.5); g.add(G.cube);
  G.conf = []; setSeed(43); for (let i = 0; i < 44; i++) { const c = boxes([[0, 0, 0, 0.12, 0.12, 0.05, [CY, "#ffffff", NV, "#7fe3ff"][i % 4]]], MAT, false); c.castShadow = false; c.visible = false; g.add(c);
    G.conf.push({ c, v: V3((rnd() - 0.5) * 5, 2 + rnd() * 3.5, 1 + rnd() * 2.5), r: rnd() * 9 }); }
}
const PRESS = [44.63, 45.51];
function cubeG(t) { // the through-line cube: sits on POSTING, pops off, hops up the 30 steps, then jumps into the bullseye
  if (t < 47.4) { const b = G.btn[0].b.position; return V3(b.x, b.y + 1.55 + 0.08 * Math.sin(t * 4), b.z - 0.2); }
  const k = (t - HOP0) / HOP;
  if (k < 0) { const u = U(t, 47.4, HOP0, "out"), b = G.btn[0].b.position, p0 = V3(b.x, b.y + 1.55, b.z - 0.2), p1 = STEP(0).p.clone().add(V3(0, 0.3, 0)); const p = p0.lerp(p1, u); p.y += 1.2 * Math.sin(Math.PI * u); return p; }
  if (k < 29) { const i = Math.floor(k), f = k - i, a = STEP(i).p.clone().add(V3(0, 0.3, 0)), b = STEP(i + 1).p.clone().add(V3(0, 0.3, 0)); const p = a.lerp(b, f); p.y += 0.35 * Math.sin(Math.PI * f); return p; }
  const top = STEP(29).p.clone().add(V3(0, 0.3, 0));
  if (t < 52.1) return top;
  const u = U(t, 52.1, 52.55, "in"), aim = V3(0, 11.2, -3.45); const p = top.lerp(aim, u); p.y += 1.3 * Math.sin(Math.PI * u); return p;
}
function animG(t) {
  G.btn.forEach(({ b, top, ring }, k) => { const d = t - PRESS[k], pr = d > -0.08 && d < 0.3 ? Math.sin(Math.PI * Math.min(1, (d + 0.08) / 0.38)) : 0;
    b.scale.y = 1 - 0.3 * pr; top.material.emissiveIntensity = 0.25 + 0.9 * pr;
    const m = t > 47.8 ? TX.btnBlank : TX.btn[k]; if (top.material.map !== m) { top.material.map = m; top.material.emissiveMap = m; top.material.needsUpdate = true; }
    const rr2 = d > 0 && d < 0.7 ? d / 0.7 : 0; ring.material.opacity = rr2 > 0 ? 0.9 * (1 - rr2) : 0; ring.scale.setScalar(1 + 4 * EZ.out(rr2)); });
  const k = (t - HOP0) / HOP;
  G.steps.forEach(({ lit }, i) => { lit.material.emissiveIntensity = 1.4 * U(t, HOP0 + i * HOP, HOP0 + i * HOP + 0.1) + (t > 50.7 ? 0.25 * Math.sin(t * 6 - i * 0.4) : 0); });
  G.dayLbl.forEach(({ l }) => setLabel(l, 0));   // day count lives in the chip (labels on the moving spiral risked the frame edge)
  const p = cubeG(t); G.cube.position.copy(p); G.cube.rotation.set(t > 47.4 ? k * 1.57 : 0, 0.4 + (t > 47.4 ? k * 0.3 : 0), 0);
  const hit = t > 52.55; if (hit) { G.cube.position.set(0, 11.2, -3.45); G.cube.scale.set(1.5, 1.5, 0.9); } else G.cube.scale.setScalar(1.5);
  const gl = U(t, 50.7, 51.3) * 0.35 + spring(t, 52.55, 9, 5) * 0.6 * (1 - U(t, 53.8, 54.6));
  G.tglow.material.opacity = Math.min(0.9, gl); G.target.scale.setScalar(1 + 0.1 * (t > 52.55 ? Math.exp(-(t - 52.55) * 6) * Math.cos((t - 52.55) * 25) : 0));
  G.conf.forEach((q, i) => { const tau = t - 52.57 - (i % 5) * 0.02; q.c.visible = tau > 0 && tau < 1.6; if (!q.c.visible) return;
    q.c.position.set(q.v.x * tau * 0.7, 11.2 + q.v.y * tau - 4.9 * tau * tau, -3.3 + q.v.z * tau * 0.6); q.c.rotation.set(q.r + tau * 9, tau * 7, 0); q.c.scale.setScalar(Math.min(1, (1.6 - tau) * 2)); });
}
const stepsAt = (t) => Math.max(0, Math.min(30, Math.floor((t - HOP0) / HOP) + 1));

/* ---------------------------------------------------------------- shots (video time; VO starts at 0.3 s) */
const SHOT = [
  { w: "A", a: -1, b: 13.33, cam: [
    [0, [2.4, 4.0, 11.5, 0, 2.2, -6.5, 44]], [3.2, [2.2, 3.9, 10.8, 0, 2.2, -6.5, 44], "sine"],
    [4.25, [21, 27, 36, 0, 1.2, -4.6, 40], "io"], [7.2, [19, 25, 33, 0, 1.2, -4.6, 40], "sine"],
    [7.36, [3.2, 7.4, 12.5, 0, 1.6, -6.5, 44], "expo"], [11.4, [2.6, 6.8, 10.8, 0, 1.8, -7, 44], "sine"],
    [12.9, [1.0, 3.8, -2.6, 0, 2.55, -10.2, 44], "io"], [13.33, [0.95, 3.75, -3.2, 0, 2.55, -10.2, 44], "sine"]] },
  { abs: true, ws: ["A", "B"], a: 13.33, b: 13.89, cam: [[13.33, [0.95, 3.75, -3.2, 0, 2.55, -10.2, 44]], [13.6, [22, 8, 22, 38, 3, -1, 48], "in"], [13.89, [44, 3.7, 19.0, 44, 3.4, -0.4, 44], "out"]] },
  { w: "B", a: 13.89, b: 18.75, cam: [[13.89, [0, 3.7, 19.0, 0, 3.4, -0.4, 44]], [16.4, [0, 3.6, 24.0, 0, 3.35, -0.4, 44], "io"], [18.3, [0, 3.55, 29.5, 0, 3.3, -0.4, 44], "io"],
    [18.6, [0, 3.55, 29.6, 0, 3.4, -0.4, 44], "sine"], [18.75, [0, 3.7, 29.4, 0, 16, -0.4, 44], "in"]] },
  { w: "C", a: 18.75, b: 25.0, cam: [[18.75, [0, 11.5, 21.5, 0, -10, -1, 44]], [19.15, [0, 11.0, 21.0, 0, 1.0, -0.6, 44], "out"], [21.9, [0.8, 10.6, 20.0, 0, 1.0, -0.6, 44], "sine"],
    [24.7, [-0.6, 10.2, 19.0, 0, 1.0, -0.6, 44], "sine"], [25.0, [-14, 9.0, 11.0, 0, 1.0, -0.6, 44], "in"]] },
  { w: "D", a: 25.0, b: 30.56, orbit: [25.0, 25.95, Math.PI * 0.9, 0], cam: [[25.0, [0, 4.3, 16.6, 0, 1.9, 0, 44]], [27.9, [0, 4.2, 15.6, 0, 1.9, 0, 44], "sine"], [28.5, [0, 6.6, 22.0, 0, 1.3, -0.4, 44], "io"],
    [29.9, [0.2, 6.4, 21.0, 0, 1.3, -0.4, 44], "sine"], [30.3, [BB[WIN].x * 0.5, 4.3, 8.8, BB[WIN].x, 2.5, -1.0, 40], "io"], [30.56, [BB[WIN].x, 2.65, 0.5, BB[WIN].x, 2.6, -1.2, 24], "in"]] },
  { w: "E", a: 30.56, b: 37.78, cam: [[30.56, [-2.75, 1.6, -1.6, -2.75, 0.3, -2.2, 30]], [31.5, [0, 16.8, 12.8, 0, 0, 0.35, 44], "out"], [34.6, [0.4, 16.4, 12.4, 0, 0, 0.35, 44], "sine"],
    [36.4, [5.0, 9.4, 15.6, -0.6, 0.9, -0.4, 44], "io"], [37.78, [4.6, 9.0, 14.8, -0.6, 0.9, -0.4, 44], "sine"]] },
  { w: "F", a: 37.78, b: 44.3, cam: [[37.78, [0, 3.0, 15.2, 0, 3.0, -0.7, 44]], [40.1, [0, 3.0, 14.6, 0, 3.0, -0.7, 44], "sine"], [40.9, [0, 9.0, 19.5, 0, 2.75, -0.2, 44], "io"],
    [44.0, [0.4, 8.8, 18.8, 0, 2.75, -0.2, 44], "sine"], [44.3, [0, 3.1, 6.5, 0, 3.0, -0.7, 60], "in"]] },
  { w: "G", a: 44.3, b: 99, camf: camG },
];
function camG(t) {
  const K1 = [[44.3, [0, 22.4, 43.4, 0, 1.0, 2.6, 14]], [44.85, [0, 7.5, 15.0, 0, 1.0, 2.6, 44], "out"], [47.2, [0.6, 7.2, 14.4, 0, 1.0, 2.6, 44], "sine"]];
  const K3 = [[51.4, [6.2, 12.4, 6.4, 0, 10.5, -3.4, 44]], [57.2, [4.2, 12.6, 8.0, 0, 10.5, -3.4, 44], "sine"]];
  if (t < 47.25) return keys(t, K1);
  // crane that follows the through-line cube up the spiral (camera stays on the cube's side, so it is never behind the column)
  const k = cl((t - HOP0) / HOP, -1, 29), a = 1.2 - Math.max(0, k) * 0.25 + 0.22, yc = 0.6 + Math.max(0, k) * 0.3;
  const fol = [Math.cos(a) * 10.5, yc + 3.0, -3.2 + Math.sin(a) * 10.5, Math.cos(a - 0.2) * 1.6, yc + 0.7, -3.2 + Math.sin(a - 0.2) * 1.6, 44];
  const v1 = keys(47.25, K1), u1 = U(t, 47.25, 47.9, "io"); let v = v1.map((x, j) => x + (fol[j] - x) * u1);
  if (t > 51.2) { const v3 = keys(t, K3), u3 = U(t, 51.2, 52.0, "io"); v = v.map((x, j) => x + (v3[j] - x) * u3); }
  return v;
}
const BLUR = [[7.22, 7.4], [13.33, 13.95], [18.6, 19.05], [24.8, 25.6], [30.3, 30.62], [44.2, 44.7]];
window.VX = { SHOT, triesAt, hitsAt, followAt, repliesAt, daysAt, draftsAt, stepsAt, PRESS };

let ready = false; const LIFTAT = (t) => 230 * U(t, 3.33, 4.25);
const ANIM = { A: animA, B: animB, C: animC, D: animD, E: animE, F: animF, G: animG };
function setup(t) {
  const sh = SHOT.find((s) => t >= s.a && t < s.b) || SHOT[SHOT.length - 1], ws = sh.ws || [sh.w];
  for (const k in worlds) worlds[k].visible = ws.includes(k);
  CLOUDS.forEach((c) => { c.m.visible = ws.includes(c.w); c.m.position.x = c.x + Math.sin(t * 0.25 + c.ph) * 0.8 + t * 0.05; });
  const o = sh.abs ? [0, 0, 0] : WP[sh.w];
  let v = sh.camf ? sh.camf(t) : keys(t, sh.cam);
  if (sh.orbit) { const [a, b, a0, a1] = sh.orbit, ang = a0 + (a1 - a0) * EZ.expo(cl((t - a) / (b - a), 0, 1)) * (t < b ? 1 : 1);
    if (t < b + 0.001) { const dx = v[0] - v[3], dz = v[2] - v[5], r = Math.hypot(dx, dz), base = Math.atan2(dx, dz); v[0] = v[3] + Math.sin(base + ang) * r; v[2] = v[5] + Math.cos(base + ang) * r; } }
  const hx = Math.sin(t * 0.9) * 0.025, hy = Math.sin(t * 1.3 + 1) * 0.02;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(o[0] + v[0] + hx, o[1] + v[1] + hy, o[2] + v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  const tx = o[0] + v[3], ty = o[1] + v[4], tz = o[2] + v[5]; cam.lookAt(tx, ty, tz);
  const d = Math.hypot(v[0] - v[3], v[1] - v[4], v[2] - v[5]); scene.fog.near = d + 8; scene.fog.far = d + 55;
  const sx = sh.abs ? tx : o[0], sz = sh.abs ? tz : o[2];
  sun.position.set(sx + 6, 14 + o[1], sz + 9); sun.target.position.set(sx, o[1], sz - 1.5); fill.position.set(sx - 6, 5, sz + 7); fill.target.position.set(sx, 1, sz - 1);
  cam.updateMatrixWorld();
  for (const k of ws) ANIM[k](t);   // after the camera (bubbles face it)
}
/* motion blur from 3 subframes (t - 1/90, t, t + 1/90) on fast camera moves, averaged in a full-screen pass */
const RT = [0, 1, 2].map(() => new THREE.WebGLRenderTarget(W, H, { samples: 4, type: THREE.HalfFloatType }));
const qScene = new THREE.Scene(), qCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
const qMat = new THREE.ShaderMaterial({ uniforms: { a: { value: null }, b: { value: null }, c: { value: null } }, depthTest: false, depthWrite: false,
  vertexShader: "varying vec2 v; void main(){ v = uv; gl_Position = vec4(position.xy, 0., 1.); }",
  fragmentShader: "uniform sampler2D a, b, c; varying vec2 v; void main(){ gl_FragColor = (texture2D(a, v) + texture2D(b, v) + texture2D(c, v)) / 3.;\n#include <tonemapping_fragment>\n#include <colorspace_fragment>\n}" });
qScene.add(new THREE.Mesh(new THREE.PlaneGeometry(2, 2), qMat));
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  const blur = BLUR.some(([a, b]) => t >= a && t <= b);
  if (!blur) { setup(t); renderer.setRenderTarget(null); renderer.render(scene, cam); return; }
  [-1 / 90, 0, 1 / 90].forEach((dt, k) => { setup(t + dt); renderer.setRenderTarget(RT[k]); renderer.render(scene, cam); });
  setup(t); qMat.uniforms.a.value = RT[0].texture; qMat.uniforms.b.value = RT[1].texture; qMat.uniforms.c.value = RT[2].texture;
  renderer.setRenderTarget(null); renderer.render(qScene, qCam);
}
window.VX.render = render;
const P = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  makeTextures(); buildA(); buildB(); buildC(); buildD(); buildE(); buildF(); buildG(); buildClouds(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = P;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
