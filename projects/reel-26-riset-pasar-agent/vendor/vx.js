/* reel-26 · 35 agent AI riset pasar — voxel night worlds, one absolute camera path through 6 floating islands.
   Deterministic: render(t) is a pure function of t ("hf-seek").
   Transitions (all different): portal zoom-through (H->G), island-hop flight (G->K), iris (K->V), whip tilt to the sky
   (V->R), dive-into-object match cut (R->B), zoom-out reveal + shockwave ring (B->CTA). */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { MAT, rnd, setSeed, boxes, emi, ctex, rr, cl, EZ, U, keys, person, glow, label, setLabel, FONT } from "./vxlib.js";

const cv = document.getElementById("vx");
const W = cv.width, H = cv.height;
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H, false);
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.22;
{ const c = document.createElement("canvas"); c.width = 4; c.height = 512; const g = c.getContext("2d"); const gr = g.createLinearGradient(0, 0, 0, 512);
  gr.addColorStop(0, "#040a1f"); gr.addColorStop(0.55, "#0a1840"); gr.addColorStop(1, "#13285a"); g.fillStyle = gr; g.fillRect(0, 0, 4, 512);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; scene.background = t; }
scene.fog = new THREE.Fog(0x0c1a44, 26, 74);
scene.add(new THREE.HemisphereLight(0x9fbaff, 0x0a1230, 0.78));
const moon = new THREE.DirectionalLight(0xc6dbff, 2.1); moon.castShadow = true; moon.shadow.mapSize.set(2048, 2048); moon.shadow.bias = -0.0004; moon.shadow.normalBias = 0.025;
Object.assign(moon.shadow.camera, { left: -11, right: 11, top: 11, bottom: -11, near: 1, far: 48 }); scene.add(moon, moon.target);
const warm = new THREE.DirectionalLight(0xffc48a, 0.7); scene.add(warm, warm.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 150);

/* ------------------------------------------------------------------ stars */
const stars = new THREE.Group(); scene.add(stars);
{ setSeed(91); const N = 700, p = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { const u = rnd() * 2 - 1, a = rnd() * Math.PI * 2, r = 95, s = Math.sqrt(1 - u * u); p[i * 3] = r * s * Math.cos(a); p[i * 3 + 1] = Math.abs(r * u) * 0.9 + 4; p[i * 3 + 2] = r * s * Math.sin(a); }
  const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(p, 3));
  stars.add(new THREE.Points(g, new THREE.PointsMaterial({ color: 0xcfe2ff, size: 2.2, sizeAttenuation: false, fog: false, transparent: true, opacity: 0.85 }))); }

/* ------------------------------------------------------------------ shared */
const RIM = emi("#36e0ff", 1.3);
const MATB = new THREE.MeshStandardMaterial({ color: 0x111827, roughness: 0.6 });
function island(nx, nz, a = "#1d3266", b = "#172a58") {
  const g = new THREE.Group(), L = [];
  for (let i = -nx; i <= nx; i++) for (let j = -nz; j <= nz; j++) L.push([i, -0.05, j, 1, 0.1, 1, (i + j) & 1 ? a : b]);
  const top = boxes(L, MAT, false); top.castShadow = false; top.receiveShadow = true; g.add(top);
  const Wd = 2 * nx + 1, D = 2 * nz + 1;
  g.add(boxes([[0, -0.55, 0, Wd, 0.9, D, "#0f2147"], [0, -1.15, 0, Wd - 0.8, 0.3, D - 0.8, "#0b1a3a"], [0, -1.5, 0, Wd - 2.2, 0.4, D - 2.2, "#08142e"],
    [0, -1.95, 0, Math.max(1, Wd * 0.35), 0.5, Math.max(1, D * 0.35), "#060f24"]], MAT, false));
  for (const [x, z, w, d] of [[0, D / 2, Wd + 0.06, 0.05], [0, -D / 2, Wd + 0.06, 0.05], [Wd / 2, 0, 0.05, D + 0.06], [-Wd / 2, 0, 0.05, D + 0.06]]) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, 0.05, d), RIM); m.position.set(x, -0.1, z); g.add(m); }
  return g;
}
const WP = { H: [0, 0, 0], G: [60, 0, 0], K: [120, 0, 0], V: [180, 0, 0], R: [240, 0, 0], B: [300, 0, 0] };
const VIS = { H: [-1, 10.0], G: [9.9, 20.22], K: [20.1, 31.0], V: [30.86, 40.56], R: [40.44, 50.3], B: [50.18, 99] };
const worlds = {}; const mk = (k) => { const g = new THREE.Group(); g.position.set(...WP[k]); worlds[k] = g; scene.add(g); return g; };
function clouds(k, n, sd) { setSeed(sd); for (let i = 0; i < n; i++) { const x = (rnd() - 0.5) * 34, y = -6 + rnd() * 9, z = -18 + rnd() * 22;
  if (Math.hypot(x, z) < 9 && y > -4) continue; const L = [], q = 3 + Math.floor(rnd() * 3), sz = 0.8 + rnd() * 1.1;
  for (let j = 0; j < q; j++) L.push([(j - q / 2) * sz * 0.8, (rnd() - 0.3) * sz * 0.5, (rnd() - 0.5) * sz, sz * (1 + rnd()), sz * (0.55 + rnd() * 0.5), sz * (1 + rnd() * 0.8), j & 1 ? "#22386c" : "#1b2f60"]);
  const m = boxes(L, MAT, false); m.castShadow = m.receiveShadow = false; m.position.set(x, y, z); worlds[k].add(m); } }

/* ------------------------------------------------------------------ textures */
const TX = {};
function fitFont(g, lines, px, maxW) { do { g.font = `700 ${px}px ${FONT}`; if (lines.every((l) => g.measureText(l).width <= maxW)) return; px -= 2; } while (px > 10); }
function card(title, rows, accent = "#01ccf7") { // dark panel with a title and rows (no cut text)
  return ctex(512, 384, (g) => {
    g.fillStyle = "#0a1644"; rr(g, 0, 0, 512, 384, 30); g.fill(); g.lineWidth = 6; g.strokeStyle = accent; rr(g, 3, 3, 506, 378, 28); g.stroke();
    g.fillStyle = accent; g.font = `700 30px ${FONT}`; g.textBaseline = "middle"; fitFont(g, [title], 30, 430); g.fillText(title, 40, 52);
    rows.forEach((r, i) => { const y = 120 + i * 72;
      g.fillStyle = "rgba(255,255,255,.07)"; rr(g, 34, y - 30, 444, 60, 16); g.fill();
      g.fillStyle = "#ffffff"; fitFont(g, [r[0]], 30, 270); g.fillText(r[0], 54, y);
      g.fillStyle = r[2] || accent; g.textAlign = "right"; fitFont(g, [r[1]], 30, 150); g.fillText(r[1], 458, y); g.textAlign = "left"; });
  });
}
function board(big, sub, accent = "#ff6b8a") { // big number board (your stall / competitor stall)
  return ctex(384, 288, (g) => {
    g.fillStyle = "#0a1644"; rr(g, 0, 0, 384, 288, 26); g.fill(); g.lineWidth = 6; g.strokeStyle = accent; rr(g, 3, 3, 378, 282, 24); g.stroke();
    g.fillStyle = "#9fb6e8"; g.font = `700 26px ${FONT}`; g.textAlign = "center"; g.textBaseline = "middle"; fitFont(g, [sub], 26, 320); g.textAlign = "center"; g.fillText(sub, 192, 62);
    g.fillStyle = accent; g.font = `700 150px ${FONT}`; fitFont(g, [big], 150, 320); g.textAlign = "center"; g.fillText(big, 192, 180);
  });
}
function phrase(txt) { // a buyer phrase slab
  return ctex(512, 128, (g) => {
    g.fillStyle = "#0a1644"; rr(g, 0, 0, 512, 128, 26); g.fill(); g.lineWidth = 5; g.strokeStyle = "#01ccf7"; rr(g, 3, 3, 506, 122, 24); g.stroke();
    g.fillStyle = "#ffffff"; g.font = `700 44px ${FONT}`; g.textBaseline = "middle"; g.textAlign = "center"; fitFont(g, [txt], 44, 440); g.textAlign = "center"; g.fillText(txt, 256, 66);
  });
}
function page() { // the Monday one-pager
  return ctex(512, 672, (g) => {
    g.fillStyle = "#f3f7ff"; rr(g, 0, 0, 512, 672, 24); g.fill();
    g.fillStyle = "#0a1644"; g.font = `700 36px ${FONT}`; g.textBaseline = "middle"; fitFont(g, ["RINGKASAN SENIN"], 36, 420); g.fillText("RINGKASAN SENIN", 40, 56);
    g.fillStyle = "#01ccf7"; rr(g, 40, 84, 110, 8, 4); g.fill();
    [["Yang berubah minggu ini", "#294b77"], ["Yang pelanggan tanyain", "#294b77"], ["Satu penawaran buat minggu ini", "#294b77"]].forEach(([s], i) => {
      const y = 150 + i * 170; g.fillStyle = "rgba(10,22,68,.06)"; rr(g, 36, y - 36, 440, 140, 18); g.fill();
      g.fillStyle = "#01ccf7"; g.beginPath(); g.arc(68, y, 14, 0, 7); g.fill();
      g.fillStyle = "#0a1644"; g.font = `700 30px ${FONT}`; fitFont(g, [s], 30, 350); g.fillText(s, 96, y);
      for (let k = 0; k < 2; k++) { g.fillStyle = "rgba(41,75,119,.3)"; rr(g, 96, y + 32 + k * 26, k ? 230 : 330, 10, 5); g.fill(); } });
  });
}
function makeTextures() {
  TX.you = board("0", "PESANAN MINGGU INI", "#ff6b8a");
  TX.rival = board("24", "LAPAK SEBELAH", "#3ddc97");
  TX.k1 = card("LAPAK A · SIMULASI", [["Penawaran", "4 paket"], ["Harga", "Rp150rb"], ["Review", "4,2 ★"]]);
  TX.k2 = card("LAPAK B · SIMULASI", [["Penawaran", "6 paket"], ["Harga", "Rp210rb"], ["Review", "3,9 ★"]]);
  TX.k3 = card("LAPAK C · SIMULASI", [["Penawaran", "3 paket"], ["Harga", "Rp175rb"], ["Review", "4,5 ★"]]);
  TX.page = page();
  TX.ph = ["“ada slot besok?”", "“harganya berapa?”", "“bisa booking lewat WA?”", "“ready kapan?”"].map(phrase);
}

/* ------------------------------------------------------------------ H: market street — your stall is empty, the next one has a queue */
const Hh = {};
function stall(g, x, awn, tex, flip) {
  const s = new THREE.Group(); s.position.set(x, 0, -0.6); s.rotation.y = flip ? -0.34 : 0.34; g.add(s);
  s.add(boxes([[0, 0.5, 0, 2.5, 1.0, 1.3, "#17306a"], [0, 1.03, 0.52, 2.5, 0.12, 0.3, "#24407f"],
    [-1.2, 1.6, -0.5, 0.12, 2.2, 0.12, "#8a9bb8"], [1.2, 1.6, -0.5, 0.12, 2.2, 0.12, "#8a9bb8"],
    [0, 2.62, 0.06, 2.7, 0.14, 1.5, awn], [0, 2.46, 0.78, 2.7, 0.24, 0.06, awn]]));
  const b = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 1.125), new THREE.MeshBasicMaterial({ map: tex, toneMapped: false }));
  b.position.set(0, 1.78, -0.42); s.add(b);
  const gl = glow(awn, 2.6, 1.8); gl.position.set(0, 2.0, 0.3); gl.material.opacity = 0.18; s.add(gl);
  return { s, b, gl };
}
function buildH() {
  const g = mk("H"); g.add(island(6, 5)); clouds("H", 9, 3);
  g.add(boxes([[0, 0.005, 1.6, 12, 0.01, 2.4, "#13265a"]], MAT, false)); // street
  Hh.you = stall(g, -2.9, "#ff6b8a", TX.you, false);
  Hh.riv = stall(g, 3.0, "#3ddc97", TX.rival, true);
  // queue at the competitor
  setSeed(5); Hh.q = [];
  const SK = ["#e8b48c", "#d79b74", "#f0c49f", "#c98a63", "#eab896"], TOPS = ["#2f6bff", "#ff8a3d", "#7c5cff", "#2ecc71", "#ff5c8a"];
  for (let i = 0; i < 5; i++) { const p = person({ pants: "#1b2238", top: TOPS[i], top2: "#ffffff", skin: SK[i], hair: i & 1 ? "#2b2118" : "#1a1410", fringe: [[-0.2, 0.12], [0.1, 0.1]], glasses: i === 2, bun: i === 1, strings: false });
    p.root.position.set(2.25 - i * 0.78, 0, 1.45 + (i & 1 ? 0.18 : -0.1)); p.root.rotation.y = -1.3 + (rnd() - 0.5) * 0.3; p.root.scale.setScalar(0.92); p.setMouth("smile"); g.add(p.root); Hh.q.push(p); }
  // one lone person walks past your stall and leaves
  Hh.pass = person({ pants: "#243156", top: "#9fb6e8", top2: "#ffffff", skin: "#e8b48c", hair: "#1a1410", fringe: [[-0.18, 0.1]], glasses: false, bun: false, strings: false });
  Hh.pass.root.scale.setScalar(0.92); Hh.pass.setMouth("n"); g.add(Hh.pass.root);
  // question mark over your stall / cyan knowledge beam over theirs
  Hh.qm = label("?", null, null, 0.85); Hh.qm.position.set(-2.9, 3.5, -0.3); g.add(Hh.qm); setLabel(Hh.qm, 0);
  Hh.beam = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.9, 3.4, 18, 1, true), new THREE.MeshBasicMaterial({ color: 0x36e0ff, transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false, toneMapped: false }));
  Hh.beam.position.set(3.0, 4.2, -0.6); g.add(Hh.beam);
  Hh.portal = glow("#36e0ff", 3.2, 2.6); Hh.portal.position.set(-2.9, 1.78, -0.1); Hh.portal.material.opacity = 0; g.add(Hh.portal);
}
function animH(t) {
  Hh.you.gl.material.opacity = 0.14 + 0.05 * Math.sin(t * 2.2);
  Hh.riv.gl.material.opacity = 0.16 + 0.07 * Math.sin(t * 2.6 + 1);
  // the lone passer-by crosses and never stops
  { const u = cl((t - 0.5) / 5.2, 0, 1); Hh.pass.root.visible = u > 0 && u < 1;
    Hh.pass.root.position.set(-6.4 + u * 11, 0, 2.3); Hh.pass.root.rotation.y = 1.57;
    Hh.pass.armL.rotation.x = Math.sin(t * 7) * 0.6; Hh.pass.armR.rotation.x = -Math.sin(t * 7) * 0.6;
    Hh.pass.root.position.y = Math.abs(Math.sin(t * 7)) * 0.05; }
  // the queue builds on line 2
  Hh.q.forEach((p, i) => { const a = 4.3 + i * 0.36, u = U(t, a, a + 0.42, "back"); p.root.visible = t > a;
    p.root.scale.setScalar(Math.max(0.001, 0.92 * u)); p.root.position.y = (1 - u) * 0.7;
    p.armL.rotation.x = Math.sin(t * 3 + i) * 0.18; p.head.rotation.y = Math.sin(t * 1.4 + i) * 0.25; });
  // line 3: "?" over your stall, knowledge beam over theirs
  setLabel(Hh.qm, U(t, 6.9, 7.3, "back")); Hh.qm.position.y = 3.5 + 0.08 * Math.sin(t * 2.4);
  Hh.beam.material.opacity = 0.3 * U(t, 7.9, 8.5) * (1 - U(t, 9.5, 9.9));
  Hh.beam.rotation.y = t * 0.8;
  Hh.portal.material.opacity = 0.9 * U(t, 9.5, 9.9, "in"); // portal bloom before the zoom-through
}

/* ------------------------------------------------------------------ G: 35 agents -> three question towers */
const Gg = {};
const Q3 = [["PELANGGAN MAU APA", "#01ccf7"], ["KOMPETITOR LEWATIN APA", "#ffc531"], ["DUITNYA DI MANA", "#3ddc97"]];
function buildG() {
  const g = mk("G"); g.add(island(6, 5)); clouds("G", 8, 11);
  Gg.ag = []; setSeed(23);
  for (let i = 0; i < 35; i++) { const col = i % 7, row = (i / 7) | 0;
    const grp = new THREE.Group(); const c = Q3[i % 3][1];
    grp.add(boxes([[0, 0.3, 0, 0.42, 0.6, 0.34, "#e2e8f2"], [0, 0.72, 0, 0.5, 0.36, 0.4, "#f3f6fb"], [0, 0.95, 0, 0.08, 0.12, 0.08, c]], MAT, false));
    const vis = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.16, 0.02), emi(c, 0.15)); vis.position.set(0, 0.74, 0.205); grp.add(vis);
    grp.position.set((col - 3) * 0.86, 0, (row - 2) * 0.86 - 0.3);
    g.add(grp); Gg.ag.push({ g: grp, v: vis, c, i, col, row, home: grp.position.clone() }); }
  Gg.tow = Q3.map(([txt, c], i) => { const grp = new THREE.Group(); grp.position.set((i - 1) * 3.5, 0, 0); g.add(grp);
    const base = boxes([[0, 0.12, 0, 2.2, 0.24, 2.2, "#17306a"]], MAT, false); grp.add(base);
    const ring = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.06, 2.3), emi(c, 1.2)); ring.position.y = 0.26; grp.add(ring);
    const lb = label(txt, null, null, 0.42); lb.position.set(0, 2.5, 0); grp.add(lb); setLabel(lb, 0);
    const gl = glow(c, 3.0, 2.0); gl.position.set(0, 1.2, 0); gl.material.opacity = 0; grp.add(gl);
    return { grp, ring, lb, gl, c }; });
}
function animG(t) {
  const form = U(t, 15.2, 17.6, "io"); // 35 agents walk into their three towers
  Gg.ag.forEach((a) => { const on = U(t, 10.4 + a.row * 0.16 + a.col * 0.03, 10.9 + a.row * 0.16 + a.col * 0.03, "back");
    a.g.visible = t > 10.4 + a.row * 0.16 + a.col * 0.03;
    const k = a.i % 3, slot = a.i / 3 | 0, ang = (slot / 12) * Math.PI * 2;
    const tx = (k - 1) * 3.5 + Math.cos(ang) * 0.8, tz = Math.sin(ang) * 0.8;
    a.g.position.x = a.home.x + (tx - a.home.x) * form;
    a.g.position.z = a.home.z + (tz - a.home.z) * form;
    a.g.position.y = Math.max(0, (1 - on) * 0.8) + Math.sin(form * Math.PI) * 0.12 * Math.abs(Math.sin(t * 6 + a.i));
    a.g.rotation.y = form * ((a.i % 2 ? 1 : -1) * 0.5) + Math.sin(t * 1.2 + a.i) * 0.08;
    a.g.scale.setScalar(Math.max(0.001, on));
    a.v.material.emissiveIntensity = 0.15 + 1.9 * U(t, 10.5 + a.i * 0.055, 10.75 + a.i * 0.055) * (0.75 + 0.25 * Math.sin(t * 5 + a.i)); });
  Gg.tow.forEach((T, i) => { const on = U(t, 15.6 + i * 0.95, 16.2 + i * 0.95, "back");
    T.ring.material.emissiveIntensity = 0.2 + 1.4 * on; setLabel(T.lb, U(t, 15.9 + i * 0.95, 16.4 + i * 0.95, "back"));
    T.lb.position.y = 2.5 + 0.06 * Math.sin(t * 2 + i); T.gl.material.opacity = 0.22 * on; });
}

/* ------------------------------------------------------------------ K: three competitor stalls scanned -> two gaps */
const Kk = {};
function buildK() {
  const g = mk("K"); g.add(island(7, 4)); clouds("K", 8, 31);
  Kk.cards = [TX.k1, TX.k2, TX.k3].map((tx, i) => { const grp = new THREE.Group(); grp.position.set((i - 1) * 3.4, 0, 0); g.add(grp);
    grp.add(boxes([[0, 0.5, 0, 2.0, 1.0, 1.1, "#17306a"], [-0.95, 1.5, -0.4, 0.1, 2.0, 0.1, "#8a9bb8"], [0.95, 1.5, -0.4, 0.1, 2.0, 0.1, "#8a9bb8"],
      [0, 2.5, 0.06, 2.2, 0.12, 1.3, ["#2f6bff", "#ff8a3d", "#7c5cff"][i]]]));
    const p = new THREE.Mesh(new THREE.PlaneGeometry(1.7, 1.275), new THREE.MeshBasicMaterial({ map: tx, toneMapped: false, transparent: true, opacity: 0 }));
    p.position.set(0, 1.72, -0.32); grp.add(p);
    const gl = glow("#36e0ff", 2.6, 2.2); gl.position.set(0, 1.7, 0.1); gl.material.opacity = 0; grp.add(gl);
    return { grp, p, gl }; });
  // scan beam
  Kk.beam = new THREE.Mesh(new THREE.BoxGeometry(0.1, 5.0, 3.2), new THREE.MeshBasicMaterial({ color: 0x36e0ff, transparent: true, opacity: 0, depthWrite: false, toneMapped: false }));
  Kk.beam.position.set(0, 2.4, 0); g.add(Kk.beam);
  // the two gaps rise out of the ground between the stalls
  Kk.gap = [["LAYANAN YANG NGGAK ADA", -1.7], ["KELUHAN YANG NGGAK DIBERESIN", 1.7]].map(([txt, x], i) => {
    const grp = new THREE.Group(); grp.position.set(x, 0, 2.3); g.add(grp);
    const pil = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1.5, 0.5), emi("#01ccf7", 1.1)); pil.position.y = 0.75; grp.add(pil);
    const lb = label(txt, null, null, 0.4); lb.position.set(0, 2.1, 0); grp.add(lb); setLabel(lb, 0);
    const gl = glow("#01ccf7", 2.4, 2.4); gl.position.y = 1.0; gl.material.opacity = 0; grp.add(gl);
    return { grp, pil, lb, gl }; });
}
function animK(t) {
  Kk.cards.forEach((c, i) => { const a = 21.4 + i * 1.5, u = U(t, a, a + 0.5, "out");
    c.p.material.opacity = u * (1 - 0.55 * U(t, 26.3, 26.9)); c.p.position.y = 1.72 + (1 - u) * 0.25;
    c.gl.material.opacity = 0.3 * (U(t, a - 0.25, a) - U(t, a + 0.9, a + 1.3));
    c.grp.position.y = 0.04 * Math.sin(t * 1.6 + i); });
  { const sw = cl((t - 21.1) / 4.6, 0, 1); Kk.beam.visible = t > 21.05 && t < 26.3;
    Kk.beam.position.x = -3.4 + sw * 6.8; Kk.beam.material.opacity = 0.22 * U(t, 21.05, 21.3) * (1 - U(t, 25.9, 26.3)); }
  Kk.gap.forEach((G2, i) => { const a = 26.9 + i * 1.9, u = U(t, a, a + 0.55, "back");
    G2.grp.visible = t > a - 0.02; G2.pil.scale.y = Math.max(0.001, u); G2.pil.position.y = 0.75 * u;
    setLabel(G2.lb, U(t, a + 0.25, a + 0.7, "back")); G2.lb.position.y = 2.1 + 0.06 * Math.sin(t * 2.2 + i);
    G2.gl.material.opacity = 0.26 * u; });
}

/* ------------------------------------------------------------------ V: wall of reviews -> buyer phrases lift out */
const Vv = {};
function buildV() {
  const g = mk("V"); g.add(island(6, 4)); clouds("V", 7, 47);
  const N = 96; Vv.N = N;
  Vv.tiles = new THREE.InstancedMesh(new THREE.BoxGeometry(0.46, 0.34, 0.07),
    new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x2fd6ff, emissiveIntensity: 0.1, roughness: 0.5 }), N);
  Vv.tiles.frustumCulled = false; g.add(Vv.tiles);
  Vv.pos = []; for (let i = 0; i < N; i++) { const col = i % 12, row = (i / 12) | 0; Vv.pos.push([(col - 5.5) * 0.56, 0.5 + row * 0.44, -1.2]); }
  Vv.frame = boxes([[0, 2.1, -1.45, 7.2, 4.0, 0.14, "#132a5e"]], MAT, false); g.add(Vv.frame);
  Vv.ph = TX.ph.map((tx, i) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 0.55), new THREE.MeshBasicMaterial({ map: tx, toneMapped: false, transparent: true, opacity: 0 }));
    m.position.set(i % 2 ? 1.9 : -1.9, 1.0 + i * 0.75, 1.1); g.add(m); return m; });
}
const _o = new THREE.Object3D();
function animV(t) {
  const lit = cl((t - 31.3) / 3.2, 0, 1) * Vv.N;
  for (let i = 0; i < Vv.N; i++) { const p = Vv.pos[i], on = i < lit ? 1 : 0;
    const u = U(t, 31.0 + i * 0.012, 31.3 + i * 0.012, "back");
    _o.position.set(p[0], p[1], p[2] + (1 - u) * -0.5); _o.rotation.set(0, 0, 0); _o.scale.setScalar(Math.max(0.001, u));
    _o.updateMatrix(); Vv.tiles.setMatrixAt(i, _o.matrix); }
  Vv.tiles.instanceMatrix.needsUpdate = true;
  Vv.tiles.material.emissiveIntensity = 0.1 + 0.5 * cl((t - 31.2) / 3, 0, 1);
  Vv.ph.forEach((m, i) => { const a = 36.3 + i * 0.75, u = U(t, a, a + 0.55, "out"); m.visible = t > a - 0.02;
    m.material.opacity = u * (1 - U(t, 40.2, 40.5)); m.position.z = 1.1 * u + 0.2; m.position.y = 1.0 + i * 0.75 + (1 - u) * -0.4 + 0.03 * Math.sin(t * 2 + i);
    m.scale.setScalar(0.6 + 0.4 * u); });
}

/* ------------------------------------------------------------------ R: local demand radar */
const Rr = {};
const BARS = [["facial malam hari", 64, "#01ccf7"], ["paket pengantin", 38, "#ffc531"], ["kulit berminyak", 21, "#7c5cff"], ["promo gajian", 12, "#3ddc97"]];
function buildR() {
  const g = mk("R"); g.add(island(6, 5)); clouds("R", 7, 59);
  const dish = new THREE.Group(); dish.position.set(-2.2, 0, 0.4); g.add(dish);
  dish.add(boxes([[0, 0.4, 0, 0.3, 0.8, 0.3, "#8a9bb8"], [0, 0.06, 0, 1.0, 0.12, 1.0, "#5b6b8c"]]));
  Rr.dish = new THREE.Group(); Rr.dish.position.y = 1.0; dish.add(Rr.dish);
  Rr.dish.add(boxes([[0, 0, 0, 1.6, 0.14, 1.6, "#e2e8f2"], [0, 0.3, -0.7, 1.6, 0.6, 0.14, "#c3cfe2"]]));
  const sweep = new THREE.Mesh(new THREE.CircleGeometry(2.6, 32, 0, 1.0), new THREE.MeshBasicMaterial({ color: 0x36e0ff, transparent: true, opacity: 0.22, side: THREE.DoubleSide, depthWrite: false, toneMapped: false }));
  sweep.rotation.x = -Math.PI / 2; sweep.position.set(-2.2, 0.03, 0.4); g.add(sweep); Rr.sweep = sweep;
  for (let r = 1; r <= 3; r++) { const ring = new THREE.Mesh(new THREE.TorusGeometry(r * 0.85, 0.02, 6, 40), emi("#36e0ff", 0.8)); ring.rotation.x = -Math.PI / 2; ring.position.set(-2.2, 0.03, 0.4); g.add(ring); }
  Rr.blip = []; setSeed(17);
  for (let i = 0; i < 7; i++) { const a = rnd() * 6.28, r = 0.7 + rnd() * 1.8;
    const m = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.16, 0.16), emi("#ffc531", 2.0)); m.position.set(-2.2 + Math.cos(a) * r, 0.12, 0.4 + Math.sin(a) * r); g.add(m); Rr.blip.push({ m, a }); }
  // rising bars
  Rr.bars = BARS.map(([txt, pct, c], i) => { const grp = new THREE.Group(); grp.position.set(2.1, 0, 1.9 - i * 1.25); g.add(grp);
    const bar = new THREE.Mesh(new THREE.BoxGeometry(0.44, 1, 0.44), emi(c, 1.0)); bar.position.y = 0.5; grp.add(bar);
    const lb = label(txt + "  +" + pct + "%", null, null, 0.36); lb.position.set(1.0, 0.5, 0); grp.add(lb); setLabel(lb, 0);
    return { grp, bar, lb, pct, c }; });
  Rr.gl = glow("#01ccf7", 3.0, 3.0); Rr.gl.position.set(2.1, 1.6, 1.9); Rr.gl.material.opacity = 0; g.add(Rr.gl);
  Rr.core = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.3, 0.3), emi("#01ccf7", 2.4)); Rr.core.position.set(2.1, 1.7, 1.9); Rr.core.visible = false; g.add(Rr.core);
}
function animR(t) {
  Rr.dish.rotation.y = t * 0.9; Rr.sweep.rotation.z = -t * 0.9;
  Rr.blip.forEach((b, i) => { const ph = ((t * 0.9 + b.a) % 6.28) / 6.28; const k = Math.exp(-ph * 4);
    b.m.material.emissiveIntensity = 0.2 + 3 * k; b.m.scale.setScalar(0.7 + 0.8 * k); });
  Rr.bars.forEach((B, i) => { const a = 41.4 + i * 0.5, u = U(t, a, a + 0.7, "out");
    const h = Math.max(0.001, (0.45 + B.pct * 0.032) * u); B.bar.scale.y = h / 1; B.bar.position.y = h / 2;
    B.grp.visible = t > a - 0.02; setLabel(B.lb, U(t, a + 0.2, a + 0.6, "back")); B.lb.position.y = h + 0.3;
    const win = i === 0 ? U(t, 45.0, 45.5) : 0;
    B.bar.material.emissiveIntensity = 1.0 + 2.2 * win * (0.7 + 0.3 * Math.sin(t * 6)); });
  Rr.gl.material.opacity = 0.3 * U(t, 45.0, 45.6);
  Rr.gl.position.y = 0.45 + 64 * 0.032 + 0.2;
  const dv = U(t, 49.6, 50.18, "in"); Rr.core.visible = t > 49.5; Rr.core.position.set(2.1, 0.45 + 64 * 0.032 + 0.2, 1.9); Rr.core.scale.setScalar(0.3 + 9 * dv);
  Rr.core.material.emissiveIntensity = 2.4 + 8 * dv;
}

/* ------------------------------------------------------------------ B: research brain -> Monday one-pager */
const Bb = {};
function buildB() {
  const g = mk("B"); g.add(island(6, 5)); clouds("B", 7, 71);
  Bb.core = new THREE.Group(); Bb.core.position.set(0, 2.0, 0); g.add(Bb.core);
  setSeed(37); const L = [];
  for (let i = 0; i < 46; i++) { const a = rnd() * 6.28, b = Math.acos(2 * rnd() - 1), r = 0.55 + rnd() * 0.25, s = 0.16 + rnd() * 0.12;
    L.push([Math.sin(b) * Math.cos(a) * r, Math.cos(b) * r, Math.sin(b) * Math.sin(a) * r, s, s, s, i % 3 ? "#1b3a7a" : "#2b5bbf"]); }
  Bb.core.add(boxes(L, MAT, false));
  Bb.lit = new THREE.Mesh(new THREE.IcosahedronGeometry(0.42, 0), emi("#01ccf7", 2.2)); Bb.core.add(Bb.lit);
  Bb.gl = glow("#01ccf7", 4.2, 4.2); Bb.gl.position.copy(Bb.core.position); g.add(Bb.gl); Bb.gl.material.opacity = 0.2;
  // three streams of cubes flowing in
  Bb.str = [0, 1, 2].map((i) => { const c = Q3[i][1]; const ang = -0.9 + i * 0.9;
    const im = new THREE.InstancedMesh(new THREE.BoxGeometry(0.17, 0.17, 0.17), emi(c, 1.6), 9); im.frustumCulled = false; g.add(im);
    return { im, ang, c }; });
  // the printed page
  Bb.page = new THREE.Mesh(new THREE.PlaneGeometry(2.0, 2.625), new THREE.MeshBasicMaterial({ map: TX.page, toneMapped: false, transparent: true, opacity: 0 }));
  Bb.page.position.set(0, 2.1, 2.3); g.add(Bb.page);
  Bb.pgl = glow("#ffffff", 3.0, 3.6); Bb.pgl.position.set(0, 2.1, 2.1); Bb.pgl.material.opacity = 0; g.add(Bb.pgl);
}
function animB(t) {
  Bb.core.rotation.y = t * 0.35; Bb.core.position.y = 2.0 + 0.07 * Math.sin(t * 1.3);
  Bb.lit.rotation.set(t * 0.8, t * 0.6, 0);
  const pulse = 0.7 + 0.3 * Math.sin(t * 3.4); Bb.lit.material.emissiveIntensity = 1.6 + 1.6 * pulse;
  Bb.gl.position.copy(Bb.core.position); Bb.gl.material.opacity = 0.18 + 0.1 * pulse;
  Bb.str.forEach((S, si) => { for (let i = 0; i < 9; i++) {
      const ph = ((t * 0.55 + i / 9 + si * 0.1) % 1); const d = 6.5 * (1 - ph);
      const x = Math.cos(S.ang) * d, z = Math.sin(S.ang) * d + 1.0;
      _o.position.set(x, 0.8 + (2.0 - 0.8) * (1 - ph) * 0.4 + ph * 1.2, z);
      _o.rotation.set(ph * 5, ph * 4, 0); _o.scale.setScalar(ph > 0.92 ? 0.001 : 0.5 + 0.5 * ph);
      _o.updateMatrix(); S.im.setMatrixAt(i, _o.matrix); }
    S.im.instanceMatrix.needsUpdate = true;
    S.im.visible = t > 50.4 && t < 56.4; });
  const pu = U(t, 53.0, 53.9, "out"); Bb.page.visible = t > 52.9;
  Bb.page.material.opacity = pu; Bb.page.position.y = 2.1 + (1 - pu) * -1.1 + 0.03 * Math.sin(t * 1.7);
  Bb.page.scale.setScalar(0.7 + 0.3 * pu); Bb.pgl.material.opacity = 0.3 * pu * (1 - U(t, 58.4, 59.2));
  Bb.pgl.position.y = Bb.page.position.y;
}

/* ------------------------------------------------------------------ camera path (absolute), with cuts */
const C = []; const at = (w) => (v) => [v[0] + WP[w][0], v[1] + WP[w][1], v[2] + WP[w][2], v[3] + WP[w][0], v[4] + WP[w][1], v[5] + WP[w][2], v[6]];
const k = (w, t, v, e) => C.push([t, at(w)(v), e]);
const cut = (w, t, v) => C.push([t, at(w)(v), "lin"]);
// H — market street: wide on your empty stall, pan to the queue, back, then push into the board (portal)
k("H", 0, [-1.4, 3.1, 9.4, -1.6, 1.7, 0.2, 44]); k("H", 3.9, [-2.0, 2.7, 7.6, -2.3, 1.7, -0.2, 42], "sine");
k("H", 5.2, [1.8, 2.6, 7.2, 2.4, 1.5, 0.8, 42], "io"); k("H", 6.6, [1.6, 2.6, 7.0, 2.4, 1.5, 0.8, 42], "sine");
k("H", 8.0, [0.0, 3.4, 9.0, -0.2, 2.0, -0.2, 46], "io"); k("H", 9.5, [-1.9, 2.6, 5.0, -2.6, 1.8, -0.4, 42], "io");
k("H", 9.99, [-2.75, 2.0, 0.55, -2.9, 1.78, -0.42, 38], "in");
// G — portal zoom-through lands close on an agent visor, pulls out over the grid
cut("G", 10.0, [0.1, 1.0, 1.3, 0, 0.78, 0, 38]); k("G", 11.6, [0, 5.6, 11.6, 0, 1.2, -0.2, 40], "io");
k("G", 14.0, [0, 5.0, 10.4, 0, 1.0, -0.2, 40], "sine"); k("G", 17.6, [0, 5.4, 13.2, 0, 1.6, 0, 44], "io");
k("G", 20.0, [0, 5.2, 12.6, 0, 1.6, 0, 44], "sine");
// island hop: one flight key, the camera physically crosses to K
C.push([20.62, [120, 5.6, 13.6, 120, 1.8, 0, 44], "io"]);
// K — scan the three stalls, then down to the two gaps
k("K", 21.4, [0, 4.6, 11.4, 0, 1.8, 0, 42], "sine"); k("K", 23.0, [-3.3, 3.0, 6.2, -3.4, 1.7, 0, 40], "io");
k("K", 24.6, [0.1, 3.2, 6.6, 0, 1.7, 0, 40], "io"); k("K", 26.2, [3.3, 3.1, 6.4, 3.4, 1.7, 0, 40], "io");
k("K", 27.4, [-1.7, 3.0, 7.4, -1.7, 1.5, 1.6, 42], "io"); k("K", 29.4, [1.7, 3.0, 7.6, 1.7, 1.5, 1.8, 42], "io");
k("K", 30.9, [0, 3.6, 9.6, 0, 1.6, 1.4, 44], "sine");
// V — after the iris: the review wall, then the phrases
cut("V", 31.0, [0, 3.2, 8.6, 0, 1.9, -1.2, 42]); k("V", 34.4, [0, 3.0, 7.4, 0, 1.8, -1.2, 40], "sine");
k("V", 36.6, [0, 2.9, 6.6, 0, 1.8, 0.4, 42], "io"); k("V", 39.6, [0, 3.1, 7.2, 0, 2.0, 0.6, 42], "sine");
k("V", 40.52, [0, 3.2, 7.2, 0, 26, -6, 42], "expo"); // whip tilt up to the sky
// R — starts on the sky, tilts down onto the radar
cut("R", 40.56, [-0.6, 4.0, 11.0, -0.4, 26, -6, 42]); k("R", 41.3, [-0.6, 3.9, 10.6, -0.6, 1.5, 0.4, 42], "io");
k("R", 43.6, [-2.2, 2.6, 6.2, -2.2, 1.2, 0.4, 40], "io"); k("R", 45.4, [1.6, 3.0, 7.2, 2.1, 1.7, 0.6, 42], "io");
k("R", 48.6, [1.9, 3.0, 6.8, 2.1, 1.8, 0.8, 42], "sine"); k("R", 50.16, [2.08, 2.6, 2.5, 2.1, 2.5, 1.9, 40], "in");
// B — dive-into-object match cut on the core, pull out over the brain, then the page, then the CTA pull-back
cut("B", 50.2, [0, 2.1, 1.1, 0, 2.0, 0, 38]); k("B", 51.6, [0, 3.4, 8.2, 0, 2.0, 0, 42], "io");
k("B", 53.6, [0, 3.2, 7.6, 0, 2.1, 1.4, 42], "io"); k("B", 56.4, [0.1, 3.1, 6.8, 0, 2.1, 1.8, 42], "sine");
k("B", 58.9, [0, 3.6, 9.4, 0, 2.0, 0.6, 44], "io"); k("B", 61.5, [0, 4.4, 13.0, 0, 2.2, 0, 46], "io");
k("B", 68.6, [0, 4.6, 13.6, 0, 2.2, 0, 46], "sine");
C.sort((a, b) => a[0] - b[0]);
window.VX = { C, WP };
scene.add(cam);

/* ------------------------------------------------------------------ render */
let ready = false; const LIFTAT = (t) => 230 * U(t, 6.6, 7.4);
const ANIM = { H: animH, G: animG, K: animK, V: animV, R: animR, B: animB };
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  for (const kk in worlds) { const [a, b] = VIS[kk]; worlds[kk].visible = t >= a && t < b; if (worlds[kk].visible) ANIM[kk](t); }
  const v = keys(t, C), hx = Math.sin(t * 0.9) * 0.025, hy = Math.sin(t * 1.3 + 1) * 0.02;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.up.set(0, 1, 0); cam.lookAt(v[3], v[4], v[5]);
  const roll = 0.32 * Math.sin(Math.PI * cl((t - 40.3) / 0.5, 0, 1)); if (roll) cam.rotateZ(roll);
  stars.position.copy(cam.position);
  const tx = v[3], tz = v[5]; moon.position.set(tx - 6, 12, tz + 8); moon.target.position.set(tx, 0, tz - 1); warm.position.set(tx + 6, 4, tz + 7); warm.target.position.set(tx, 1, tz);
  renderer.render(scene, cam);
}
window.VX.render = render;
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  makeTextures(); buildH(); buildG(); buildK(); buildV(); buildR(); buildB(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = PR;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
