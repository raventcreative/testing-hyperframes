/* R32 · Foto produk -> video promo (contoh alur) — voxel night worlds (own assets), one absolute camera path.
   Deterministic: render(t) is a pure function of t ("hf-seek"). Times come from the VO alignment (window.VO_WORDS).
   Through-line object: the PRODUCT PHOTO CARD (born at the shutter, rides into the AI cube, becomes the chat attachment, the
   face of the HOOK block, the FOTO input of the render machine, and finally the DM attachment on the CTA).
   Transitions (all different): zoom-out reveal (H->map), island-hop flight (X->H), dive into the photo card (H->N, match cut),
   elevator doors = chat screen splits (N chat -> N tower), vertical whip tilt (N->S), 180° orbit (S->R), dolly zoom (R),
   iris (R->C, page), button shockwave (C->CTA, page). */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { SVGLoader } from "three/addons/loaders/SVGLoader.js";
import { MAT, rnd, setSeed, boxes, emi, rr, cl, EZ, U, keys, blinkAt, person, glow, label, setLabel, FONT, safeText } from "./vxlib.js";

const cv = document.getElementById("vx");
const W = cv.width, H = cv.height;
// brand rule (batch 8 addendum): the backdrop is the client navy plate (<img id="plate"> under this canvas) -> transparent WebGL
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, alpha: true, premultipliedAlpha: true, preserveDrawingBuffer: true });
renderer.setClearColor(0x000000, 0);
renderer.setPixelRatio(1); renderer.setSize(W, H, false);
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.22;
scene.background = null;   // no sky gradient: the brand plate shows through
scene.fog = new THREE.Fog(0x13284f, 40, 140);   // subtle, tinted to the plate mid colour
const hemi = new THREE.HemisphereLight(0x9fbaff, 0x0a1230, 0.75); scene.add(hemi);
const moon = new THREE.DirectionalLight(0xc6dbff, 2.1); moon.castShadow = true; moon.shadow.mapSize.set(2048, 2048); moon.shadow.bias = -0.0004; moon.shadow.normalBias = 0.025;
Object.assign(moon.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10, near: 1, far: 45 }); scene.add(moon, moon.target);
const warm = new THREE.DirectionalLight(0xffc48a, 0.7); scene.add(warm, warm.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 160);

/* ---------------------------------------------------------------- VO word times */
const VW = window.VO_WORDS;
const wt = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after); if (!w) throw new Error("vx: word not found " + txt); return w[1]; };
const T = {
  produk: wt("produk,"), ai: wt("AI"), bikinin: wt("bikinin"), video: wt("video"), suara: wt("suara"), marketer: wt("marketer."),
  ini: wt("Ini"), cocok: wt("cocok"), umkm: wt("UMKM,"), online: wt("online"), sampai: wt("sampai"),
  satu: wt("Satu."), terang: wt("terang:"), depan: wt("depan,"), samping: wt("samping,"), detail: wt("detail"), kemasan: wt("kemasan."),
  dua: wt("Dua."), kirim: wt("Kirim"), asisten: wt("asisten"), nulis: wt("nulis"), naskah: wt("naskah"), susunan: wt("susunan"), adegan: wt("adegan,"),
  detik: wt("detik"), detik2: wt("detik."), sertakan: wt("Sertakan"), harga: wt("harga,"), ukuran: wt("ukuran,"), siapa: wt("siapa"),
  hook: wt("Hook"), manfaat: wt("manfaat"), satu1: wt("satu", 20), persatu: wt("satu,", 20), ajakan: wt("ajakan"), keranjang: wt("keranjang"),
  tiga: wt("Tiga."), naskah2: wt("Naskah"), dibacakan: wt("dibacakan"), suara2: wt("suara", 30), gaya: wt("gaya"), marketer2: wt("marketer", 30), jualan: wt("jualan."),
  empat: wt("Empat."), adegan2: wt("Adegan,"), foto2: wt("foto,", 30), suara3: wt("suara", 36), dirender: wt("dirender"), video2: wt("video", 36), siap: wt("siap"),
  video3: wt("Video"), kamu: wt("kamu"), juga: wt("juga", 40), dibikin: wt("dibikin"), pakai: wt("pakai"), alur: wt("alur"), mirip: wt("mirip."),
  tapi: wt("Tapi"), alat: wt("alat"), bukan: wt("bukan"), jaminan: wt("jaminan"), cek: wt("Cek"), klaim: wt("klaim"), sebelum: wt("sebelum"), posting: wt("posting."),
  komen: wt("Komen"), promo: wt("promo,"), kirim2: wt("kirim", 50), dm: wt("DM."),
};
window.VX_T = T;
const envAt = (t) => { const E = window.VO_ENV; const i = Math.floor(t * 100); return i >= 0 && i < E.length ? E[i] / 99 : 0; };

const stars = new THREE.Group();   // no star sprites (brand plate only)

/* ---------------------------------------------------------------- shared */
const RIM = emi("#36e0ff", 1.3);
function island(nx, nz, a = "#1d3266", b = "#172a58") {
  const g = new THREE.Group(), L = [];
  for (let i = -nx; i <= nx; i++) for (let j = -nz; j <= nz; j++) L.push([i, -0.05, j, 1, 0.1, 1, (i + j) & 1 ? a : b]);
  const top = boxes(L, MAT, false); top.castShadow = false; g.add(top);
  const Wd = 2 * nx + 1, D = 2 * nz + 1;
  g.add(boxes([[0, -0.55, 0, Wd, 0.9, D, "#0f2147"], [0, -1.15, 0, Wd - 0.8, 0.3, D - 0.8, "#0b1a3a"], [0, -1.5, 0, Math.max(0.6, Wd - 2.2), 0.4, Math.max(0.6, D - 2.2), "#08142e"],
    [0, -1.95, 0, Math.max(0.6, Wd * 0.35), 0.5, Math.max(0.6, D * 0.35), "#060f24"]], MAT, false));
  for (const [x, z, w, d] of [[0, D / 2, Wd + 0.06, 0.05], [0, -D / 2, Wd + 0.06, 0.05], [Wd / 2, 0, 0.05, D + 0.06], [-Wd / 2, 0, 0.05, D + 0.06]]) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, 0.05, d), RIM); m.position.set(x, -0.1, z); g.add(m); }
  return g;
}
// world placement: position + yaw (R faces -z so the 180° orbit from S lands in front of it)
const WP = { H: [0, 0, 0, 0], N: [-3, 0, -17, 0], S: [3, 0, -34, 0], R: [-1, 0, -50, Math.PI], X: [30, 0, -16, 0], C: [80, 0, 0, 0] };
const VIS = { H: [-1, 16.3], N: [16.25, 30.74], S: [30.6, 36.3], R: [35.05, 44.32], X: [6.6, 11.2], C: [44.3, 99] };
const MAP = [5.4, 7.6]; // all chain islands visible together (reveal)
const worlds = {}; const mk = (k) => { const g = new THREE.Group(); g.position.set(WP[k][0], WP[k][1], WP[k][2]); g.rotation.y = WP[k][3]; worlds[k] = g; scene.add(g); return g; };
function clouds() { }   // no voxel clouds (brand plate only)
function cloudsUnused(k, n, sd) { setSeed(sd); for (let i = 0; i < n; i++) { const x = (rnd() - 0.5) * 34, y = -6 + rnd() * 9, z = -18 + rnd() * 22;
  if (Math.hypot(x, z) < 9 && y > -4) continue; const L = [], q = 3 + Math.floor(rnd() * 3), sz = 0.8 + rnd() * 1.1;
  for (let j = 0; j < q; j++) L.push([(j - q / 2) * sz * 0.8, (rnd() - 0.3) * sz * 0.5, (rnd() - 0.5) * sz, sz * (1 + rnd()), sz * (0.55 + rnd() * 0.5), sz * (1 + rnd() * 0.8), j & 1 ? "#22386c" : "#1b2f60"]);
  const m = boxes(L, MAT, false); m.castShadow = m.receiveShadow = false; m.position.set(x, y, z); worlds[k].add(m); } }
const _o = new THREE.Object3D();
// closed-form step-response spring (small overshoot), pure function of t
const spring = (t, t0, dur = 0.5) => { const x = (t - t0) / dur; if (x <= 0) return 0; if (x >= 3) return 1; return 1 - Math.exp(-5.2 * x) * Math.cos(7.0 * x); };

/* ---------------------------------------------------------------- 3D brand logos (Simple Icons CC0 paths -> extruded meshes) */
function logo3d(name, color, size, depth = 3.2) {
  const Lg = window.LOGOS[name]; const data = new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="${Lg.path}"/></svg>`);
  const shapes = data.paths.flatMap((p) => SVGLoader.createShapes(p));
  const g = new THREE.ExtrudeGeometry(shapes, { depth, bevelEnabled: true, bevelThickness: 0.5, bevelSize: 0.32, bevelSegments: 2, curveSegments: 10 });
  g.translate(-12, -12, -depth / 2); g.rotateX(Math.PI); g.scale(size / 24, size / 24, size / 24);
  const c = new THREE.Color(color); const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.28, roughness: 0.35, metalness: 0.1 }));
  m.castShadow = true; const w = new THREE.Group(); w.add(m); return w;
}
const LOGO = {};

/* ---------------------------------------------------------------- 2D drawing (product art, cards, live screens) */
function fitFont(g, lines, px, maxW, wgt = 700) { do { g.font = `${wgt} ${px}px ${FONT}`; if (lines.every((l) => g.measureText(l).width <= maxW)) return px; px -= 2; } while (px > 10); return px; }
function canvasTex(w, h, draw) { const c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d"); safeText(g, w, h); if (draw) draw(g, w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return { c, g, t, w, h }; }
function dyn(w, h, view) { const d = canvasTex(w, h); d.view = view; d.last = -1;
  d.update = (t) => { if (Math.abs(t - d.last) < 1e-4) return; d.last = t; d.g.setTransform(1, 0, 0, 1, 0, 0); d.g.clearRect(0, 0, w, h); d.g.textAlign = "left"; d.g.textBaseline = "alphabetic"; d.view(d.g, w, h, t); d.t.needsUpdate = true; if (d.t2) d.t2.needsUpdate = true; };
  return d; }
const NAVY = "#0a1644", NAVY2 = "#13285a", CY = "#01ccf7", INK = "#0a0d2c";
// product art (props keep their own colours): kopi susu bottle, sambal jar, honey tube — all labelled CONTOH
function artBottle(g, cx, cy, s, side = 0) {
  const w = 120 * s * (1 - 0.35 * side), hh = 230 * s;
  g.fillStyle = "#3b2a20"; rr(g, cx - 26 * s, cy - hh / 2 - 62 * s, 52 * s, 30 * s, 6 * s); g.fill();
  g.fillStyle = "#d9b48a"; rr(g, cx - 22 * s, cy - hh / 2 - 36 * s, 44 * s, 40 * s, 8 * s); g.fill();
  g.fillStyle = "#c79a6b"; rr(g, cx - w / 2, cy - hh / 2, w, hh, 22 * s); g.fill();
  g.fillStyle = "rgba(255,255,255,.18)"; rr(g, cx - w / 2 + 10 * s, cy - hh / 2 + 12 * s, 14 * s, hh - 24 * s, 7 * s); g.fill();
  const lw = w * 0.86; g.fillStyle = "#fffaf0"; rr(g, cx - lw / 2, cy - 50 * s, lw, 110 * s, 10 * s); g.fill();
  g.fillStyle = INK; g.textAlign = "center";
  if (side < 0.5) { fitFont(g, ["CONTOH"], Math.round(30 * s), lw * 0.86); g.fillText("CONTOH", cx, cy - 8 * s);
    g.fillStyle = "#7a5a3a"; fitFont(g, ["Kopi Susu 1 L"], Math.round(20 * s), lw * 0.86, 400); g.fillText("Kopi Susu 1 L", cx, cy + 30 * s); }
  else { g.fillStyle = "#c9b48f"; for (let i = 0; i < 4; i++) { rr(g, cx - lw * 0.38, cy - 30 * s + i * 20 * s, lw * (0.76 - (i % 2) * 0.2), 8 * s, 4 * s); g.fill(); } }
  g.textAlign = "left";
}
function artJar(g, cx, cy, s) {
  g.fillStyle = "#2b3348"; rr(g, cx - 66 * s, cy - 82 * s, 132 * s, 30 * s, 8 * s); g.fill();
  g.fillStyle = "#b8322a"; rr(g, cx - 60 * s, cy - 54 * s, 120 * s, 130 * s, 18 * s); g.fill();
  g.fillStyle = "#fffaf0"; rr(g, cx - 50 * s, cy - 24 * s, 100 * s, 64 * s, 8 * s); g.fill();
  g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["CONTOH"], Math.round(22 * s), 88 * s); g.fillText("CONTOH", cx, cy + 4 * s);
  g.fillStyle = "#8a3030"; fitFont(g, ["Sambal"], Math.round(18 * s), 88 * s, 400); g.fillText("Sambal", cx, cy + 28 * s); g.textAlign = "left";
}
function artTube(g, cx, cy, s) {
  g.fillStyle = "#ffffff"; rr(g, cx - 22 * s, cy - 120 * s, 44 * s, 34 * s, 6 * s); g.fill();
  g.fillStyle = "#f0a92a"; rr(g, cx - 46 * s, cy - 88 * s, 92 * s, 190 * s, 18 * s); g.fill();
  g.fillStyle = "#fffaf0"; rr(g, cx - 38 * s, cy - 30 * s, 76 * s, 70 * s, 8 * s); g.fill();
  g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["CONTOH"], Math.round(20 * s), 68 * s); g.fillText("CONTOH", cx, cy);
  g.fillStyle = "#9a6a1a"; fitFont(g, ["Madu"], Math.round(18 * s), 68 * s, 400); g.fillText("Madu", cx, cy + 24 * s); g.textAlign = "left";
}
// polaroid: k = 0 depan, 1 samping, 2 detail
const PCAP = ["DEPAN", "SAMPING", "DETAIL"];
function drawPolaroid(g, w, h, k) {
  g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h);
  const px = w * 0.07, pw = w - 2 * px, ph = h * 0.72;
  const gr = g.createLinearGradient(0, px, 0, px + ph); gr.addColorStop(0, "#f3f7fd"); gr.addColorStop(1, "#dbe6f5"); g.fillStyle = gr; g.fillRect(px, px, pw, ph);
  g.save(); g.beginPath(); g.rect(px, px, pw, ph); g.clip();
  if (k === 0) artBottle(g, w / 2, px + ph * 0.56, ph / 330);
  if (k === 1) artBottle(g, w / 2, px + ph * 0.56, ph / 330, 1);
  if (k === 2) { artBottle(g, w / 2, px + ph * 0.36, ph / 120); }
  g.restore();
  g.fillStyle = INK; g.textAlign = "center"; fitFont(g, [PCAP[k]], Math.round(h * 0.1), pw); g.fillText(PCAP[k], w / 2, px + ph + h * 0.15); g.textAlign = "left";
}
// promo "video" (what the AI builds): navy, white text, cyan accent; voice bars from the real VO envelope
function promoView(g, w, h, lt, t) {
  const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, "#0b1a4a"); gr.addColorStop(1, "#05102e"); g.fillStyle = gr; g.fillRect(0, 0, w, h);
  g.fillStyle = "rgba(1,204,247,.16)"; g.beginPath(); g.arc(w / 2, h * 0.5, w * 0.42, 0, Math.PI * 2); g.fill();
  const sc = lt < 0 ? 0 : Math.floor(lt / 1.6) % 3, u = lt < 0 ? 0 : (lt % 1.6) / 1.6, pop = spring(u * 1.6, 0, 0.45);
  g.textAlign = "center"; g.fillStyle = "#ffffff";
  if (sc === 0) { fitFont(g, ["Ngantuk", "jam 2 siang?"], 46, w * 0.84); g.fillText("Ngantuk", w / 2, 92); g.fillText("jam 2 siang?", w / 2, 144);
    artBottle(g, w / 2, h * 0.56 + 60 * (1 - pop), 0.95); }
  if (sc === 1) { fitFont(g, ["Kopi susu 1 liter"], 40, w * 0.86); g.fillText("Kopi susu 1 liter", w / 2, 96); g.fillStyle = CY; fitFont(g, ["Rp55.000"], 52, w * 0.8); g.fillText("Rp55.000", w / 2, 156);
    g.save(); g.translate(w / 2, h * 0.58); g.rotate(-0.12 * (1 - pop)); g.scale(0.8 + 0.25 * pop, 0.8 + 0.25 * pop); artBottle(g, 0, 0, 0.9); g.restore(); }
  if (sc === 2) { fitFont(g, ["Cek keranjang", "kuning"], 44, w * 0.84); g.fillText("Cek keranjang", w / 2, 96); g.fillText("kuning", w / 2, 148);
    const cx = w / 2, cy = h * 0.55, s = 1.1 * (0.6 + 0.4 * pop); g.strokeStyle = CY; g.lineWidth = 12 * s; g.lineJoin = "round"; g.lineCap = "round";
    g.beginPath(); g.moveTo(cx - 90 * s, cy - 70 * s); g.lineTo(cx - 60 * s, cy - 70 * s); g.lineTo(cx - 40 * s, cy + 30 * s); g.lineTo(cx + 70 * s, cy + 30 * s); g.lineTo(cx + 85 * s, cy - 40 * s); g.lineTo(cx - 52 * s, cy - 40 * s); g.stroke();
    g.fillStyle = CY; for (const x of [-30, 55]) { g.beginPath(); g.arc(cx + x * s, cy + 58 * s, 13 * s, 0, Math.PI * 2); g.fill(); } }
  // voice bars
  const n = 21, bw = w * 0.62 / n; for (let i = 0; i < n; i++) { const e = envAt(t - (n - i) * 0.035); const bh = 8 + 70 * e * (0.6 + 0.4 * Math.abs(Math.sin(i * 1.7)));
    g.fillStyle = i % 2 ? CY : "#7fe8ff"; rr(g, w * 0.19 + i * bw, h - 70 - bh / 2, bw * 0.6, bh, bw * 0.3); g.fill(); }
  g.fillStyle = "rgba(255,255,255,.9)"; rr(g, w - 118, 14, 104, 32, 16); g.fill(); g.fillStyle = INK; g.font = `700 18px ${FONT}`; g.fillText("CONTOH", w - 66, 37);
  g.textAlign = "left";
}

/* ---------------------------------------------------------------- textures */
const TX = {};
function makeTextures() {
  TX.pol = [0, 1, 2].map((k) => canvasTex(300, 370, (g, w, h) => drawPolaroid(g, w, h, k)).t);
  TX.bottleLabel = canvasTex(256, 220, (g, w, h) => { g.fillStyle = "#fffaf0"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["CONTOH"], 60, w * 0.86); g.fillText("CONTOH", w / 2, 96);
    g.fillStyle = "#7a5a3a"; fitFont(g, ["Kopi Susu"], 40, w * 0.86, 400); g.fillText("Kopi Susu", w / 2, 150); g.font = `700 34px ${FONT}`; g.fillText("1 L", w / 2, 196); }).t;
  TX.jarLabel = canvasTex(256, 140, (g, w, h) => { g.fillStyle = "#fffaf0"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["CONTOH"], 54, w * 0.86); g.fillText("CONTOH", w / 2, 66);
    g.fillStyle = "#8a3030"; fitFont(g, ["Sambal"], 40, w * 0.86, 400); g.fillText("Sambal", w / 2, 116); }).t;
  TX.tubeLabel = canvasTex(160, 180, (g, w, h) => { g.fillStyle = "#fffaf0"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["CONTOH"], 40, w * 0.86); g.fillText("CONTOH", w / 2, 78);
    g.fillStyle = "#9a6a1a"; fitFont(g, ["Madu"], 36, w * 0.86, 400); g.fillText("Madu", w / 2, 128); }).t;
  TX.ai = canvasTex(256, 256, (g, w, h) => { g.fillStyle = "#0a1644"; g.fillRect(0, 0, w, h); g.strokeStyle = CY; g.lineWidth = 14; g.strokeRect(10, 10, w - 20, h - 20);
    g.fillStyle = "#ffffff"; g.textAlign = "center"; g.font = `700 120px ${FONT}`; g.fillText("AI", w / 2, 170); }).t;
  TX.blocks = [["HOOK", "Ngantuk jam 2 siang?"], ["MANFAAT 1", "Melek tanpa ribet"], ["MANFAAT 2", "1 liter buat seminggu"], ["MANFAAT 3", "Gula aren asli"], ["AJAKAN BELI", "Cek keranjang kuning"]].map(([a, b], i) =>
    canvasTex(640, 112, (g, w, h) => { g.fillStyle = "#f4f8ff"; g.fillRect(0, 0, w, h); g.fillStyle = CY; g.fillRect(0, 0, 14, h);
      let x0 = 34; if (i === 0) { g.drawImage(TX.pol[0].image, 30, 8, 78, 96); x0 = 126; }
      g.fillStyle = INK; g.font = `700 40px ${FONT}`; fitFont(g, [a], 40, w - x0 - 20); g.fillText(a, x0, 50); g.fillStyle = "#294b77"; fitFont(g, [b], 30, w - x0 - 20, 400); g.fillText(b, x0, 92); }).t);
  TX.script = canvasTex(360, 260, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.font = `700 34px ${FONT}`; g.fillText("NASKAH", 24, 48); });
  TX.storyboard = canvasTex(300, 370, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["ADEGAN"], 40, w * 0.8); g.fillText("ADEGAN", w / 2, 52);
    for (let i = 0; i < 4; i++) { const y = 76 + i * 70; g.fillStyle = "#dbe6f5"; rr(g, 22, y, 110, 58, 8); g.fill(); g.fillStyle = CY; g.font = `700 22px ${FONT}`; g.textAlign = "left"; g.fillText(["0:00", "0:03", "0:15", "0:25"][i], 148, y + 26);
      g.fillStyle = "#9fb3d1"; rr(g, 148, y + 38, 120 - (i % 2) * 30, 10, 5); g.fill(); } }).t;
  TX.wave = canvasTex(300, 370, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = INK; g.textAlign = "center"; fitFont(g, ["SUARA"], 40, w * 0.8); g.fillText("SUARA", w / 2, 52);
    for (let i = 0; i < 17; i++) { const bh = 30 + 180 * Math.abs(Math.sin(i * 1.3) * Math.cos(i * 0.4)); g.fillStyle = i % 2 ? CY : "#294b77"; rr(g, 30 + i * 14.5, 210 - bh / 2, 9, bh, 4); g.fill(); } }).t;
  TX.onair = canvasTex(512, 110, (g, w, h) => { g.fillStyle = "#0a1644"; g.fillRect(0, 0, w, h); g.fillStyle = CY; g.textAlign = "center"; g.font = `700 64px ${FONT}`; g.fillText("SUARA AI", w / 2, 78); }).t;
  TX.board = canvasTex(256, 256, (g, w, h) => { g.fillStyle = "#e9eef7"; g.fillRect(0, 0, w, h); });
}

/* ---------------------------------------------------------------- products (voxel) */
function productBottle() { const g = new THREE.Group();
  g.add(boxes([[0, 0.42, 0, 0.42, 0.84, 0.42, "#c79a6b"], [0, 0.9, 0, 0.3, 0.12, 0.3, "#c79a6b"], [0, 1.0, 0, 0.17, 0.1, 0.17, "#d9b48a"], [0, 1.1, 0, 0.21, 0.12, 0.21, "#3b2a20"]]));
  const lb = new THREE.Mesh(new THREE.PlaneGeometry(0.38, 0.33), new THREE.MeshStandardMaterial({ map: TX.bottleLabel, roughness: 0.7 })); lb.position.set(0, 0.42, 0.212); g.add(lb);
  const sd = new THREE.Mesh(new THREE.PlaneGeometry(0.36, 0.3), new THREE.MeshStandardMaterial({ color: 0xfffaf0, roughness: 0.7 })); sd.position.set(0.212, 0.42, 0); sd.rotation.y = Math.PI / 2; g.add(sd);
  return g; }
function productJar() { const g = new THREE.Group();
  g.add(boxes([[0, 0.24, 0, 0.5, 0.48, 0.5, "#b8322a"], [0, 0.53, 0, 0.54, 0.1, 0.54, "#2b3348"]]));
  const lb = new THREE.Mesh(new THREE.PlaneGeometry(0.44, 0.24), new THREE.MeshStandardMaterial({ map: TX.jarLabel, roughness: 0.7 })); lb.position.set(0, 0.25, 0.252); g.add(lb); return g; }
function productTube() { const g = new THREE.Group();
  g.add(boxes([[0, 0.34, 0, 0.32, 0.68, 0.24, "#f0a92a"], [0, 0.75, 0, 0.16, 0.14, 0.16, "#ffffff"]]));
  const lb = new THREE.Mesh(new THREE.PlaneGeometry(0.26, 0.29), new THREE.MeshStandardMaterial({ map: TX.tubeLabel, roughness: 0.7 })); lb.position.set(0, 0.34, 0.122); g.add(lb); return g; }
const polMesh = (k, s = 1) => new THREE.Mesh(new THREE.PlaneGeometry(0.4 * s, 0.493 * s), new THREE.MeshBasicMaterial({ map: TX.pol[k], toneMapped: false, side: THREE.DoubleSide }));

/* ---------------------------------------------------------------- H: product photo studio (hook + step 1) */
const Hh = {};
const TBL = 0.9; // table top
function buildH() {
  const g = mk("H"); g.add(island(5, 4)); clouds("H", 9, 3);
  g.add(boxes([[0, TBL - 0.05, 0.3, 3.0, 0.1, 1.5, "#f3f6fb"], [-1.35, (TBL - 0.1) / 2, -0.3, 0.1, TBL - 0.1, 0.1, "#c3cfe2"], [1.35, (TBL - 0.1) / 2, -0.3, 0.1, TBL - 0.1, 0.1, "#c3cfe2"],
    [-1.35, (TBL - 0.1) / 2, 0.9, 0.1, TBL - 0.1, 0.1, "#c3cfe2"], [1.35, (TBL - 0.1) / 2, 0.9, 0.1, TBL - 0.1, 0.1, "#c3cfe2"]]));
  Hh.bottle = productBottle(); Hh.bottle.position.set(0, TBL, 0.35); g.add(Hh.bottle);
  Hh.jar = productJar(); Hh.jar.position.set(-0.85, TBL, 0.45); Hh.jar.rotation.y = 0.25; g.add(Hh.jar);
  Hh.tube = productTube(); Hh.tube.position.set(0.82, TBL, 0.45); Hh.tube.rotation.y = -0.25; g.add(Hh.tube);
  // softboxes
  Hh.panels = []; Hh.panelMat = emi("#fff1d8", 2.2);
  for (const [x, z, ry] of [[-2.4, 1.5, 0.75], [2.4, 1.5, -0.75]]) { const s = new THREE.Group(); s.position.set(x, 0, z); s.rotation.y = ry; g.add(s);
    s.add(boxes([[0, 0.9, 0, 0.07, 1.8, 0.07, "#8a9bb8"], [0, 0.03, 0, 0.6, 0.06, 0.6, "#5b6b8c"], [0, 2.0, -0.12, 0.9, 0.7, 0.2, "#1b2238"]]));
    const p = new THREE.Mesh(new THREE.BoxGeometry(0.82, 0.62, 0.02), Hh.panelMat); p.position.set(0, 2.0, 0.0); s.add(p); }
  Hh.pl = new THREE.PointLight(0xfff0dd, 7, 9); Hh.pl.position.set(0, 2.6, 2.2); g.add(Hh.pl);
  // phone on a tripod, aimed at the bottle
  Hh.rig = new THREE.Group(); Hh.rig.position.set(1.55, 0, 2.15); Hh.rig.rotation.y = Math.atan2(-1.55, -1.8); g.add(Hh.rig);
  Hh.rig.add(boxes([[0, 0.6, 0, 0.05, 1.2, 0.05, "#8a9bb8"], [-0.18, 0.3, 0.1, 0.04, 0.6, 0.04, "#8a9bb8"], [0.18, 0.3, 0.1, 0.04, 0.6, 0.04, "#8a9bb8"], [0, 0.3, -0.2, 0.04, 0.6, 0.04, "#8a9bb8"],
    [0, 1.3, 0, 0.38, 0.68, 0.06, "#111827"], [0.09, 1.55, -0.035, 0.08, 0.08, 0.02, "#2a3350"]]));
  Hh.flash = glow("#ffffff", 1.4, 1.4); Hh.flash.position.set(0.09, 1.55, -0.12); Hh.rig.add(Hh.flash);
  // polaroid rail + three photo cards (the through-line object)
  g.add(boxes([[0, 2.33, 0.95, 2.6, 0.02, 0.02, "#c3cfe2"], [-1.32, 1.6, 0.95, 0.04, 1.5, 0.04, "#8a9bb8"], [1.32, 1.6, 0.95, 0.04, 1.5, 0.04, "#8a9bb8"]]));
  Hh.pol = [0, 1, 2].map((k) => { const m = polMesh(k); m.visible = false; g.add(m); return m; });
  Hh.hookPol = polMesh(0); g.add(Hh.hookPol);
  // hook: AI cube -> vertical promo screen (shared element), speaker with rings
  Hh.cube = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.5, 0.5), new THREE.MeshStandardMaterial({ map: TX.ai, emissive: 0x01ccf7, emissiveIntensity: 0.35, emissiveMap: TX.ai, roughness: 0.4 })); g.add(Hh.cube);
  Hh.cg = glow("#38dcff", 1.6, 1.6); g.add(Hh.cg);
  Hh.promo = dyn(360, 640, (gg, w, h, t) => promoView(gg, w, h, t - T.bikinin - 0.3, t));
  Hh.bill = new THREE.Group(); Hh.bill.position.set(0, 3.5, 0.3); g.add(Hh.bill);
  Hh.bill.add(boxes([[0, 0, -0.04, 1.62, 2.78, 0.06, "#0b1640"]]));
  const sc = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 2.667), new THREE.MeshBasicMaterial({ map: Hh.promo.t, toneMapped: false })); Hh.bill.add(sc);
  for (const [x, y, w, h] of [[0, 1.39, 1.64, 0.04], [0, -1.39, 1.64, 0.04], [0.81, 0, 0.04, 2.82], [-0.81, 0, 0.04, 2.82]]) { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.05), RIM); m.position.set(x, y, 0); Hh.bill.add(m); }
  // two speakers flank the promo screen ("suara marketer")
  Hh.spk = new THREE.Group(); Hh.spk.position.set(0, 3.5, 0.3); g.add(Hh.spk); Hh.cone = []; Hh.rings = [];
  for (const sx of [-1, 1]) { const sp = new THREE.Group(); sp.position.set(sx * 1.22, -0.55, 0); sp.rotation.y = -sx * 0.25; Hh.spk.add(sp);
    sp.add(boxes([[0, 0, 0, 0.5, 0.9, 0.42, "#1b2238"], [0, 0.2, 0.215, 0.3, 0.3, 0.02, "#2a3350"], [0, -0.2, 0.215, 0.36, 0.36, 0.02, "#2a3350"]]));
    const c1 = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.16, 0.04), emi("#36e0ff", 1.6)), c2 = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.04), emi("#36e0ff", 1.6));
    c1.position.set(0, 0.2, 0.23); c2.position.set(0, -0.2, 0.23); sp.add(c1, c2); Hh.cone.push(c1, c2);
    for (let i = 0; i < 2; i++) { const r = new THREE.Mesh(new THREE.TorusGeometry(0.22, 0.02, 6, 40), new THREE.MeshBasicMaterial({ color: 0x5fe6ff, transparent: true, toneMapped: false })); r.position.set(0, -0.2, 0.3); sp.add(r); Hh.rings.push(r); } }
  Hh.lb = label("1 · FOTO", "#01ccf7", "#fff", 1.6); Hh.lb.position.set(0, 4.6, 0); g.add(Hh.lb);
}
// polaroid flight: from the phone to rail slot k
const POL_T = () => [T.depan, T.samping, T.detail];
const RAIL = [[0, 2.08, 0.97], [0.78, 2.08, 0.97], [-0.78, 2.08, 0.97]];
const PHONE = new THREE.Vector3(1.38, 1.3, 1.95);
function animH(t) {
  // lights: on in the hook, dimmed when we come back for step 1, on again on "terang"
  const lit = t < T.satu - 0.3 ? 1 : U(t, T.terang - 0.05, T.terang + 0.25, "out"); const dimmed = 0.25 + 0.75 * lit;
  Hh.panelMat.emissiveIntensity = 0.15 + 2.3 * lit; Hh.pl.intensity = 1.5 + 7 * lit; hemi.intensity = 0.75 * (t > 10 && t < 16.4 ? dimmed : 1);
  // phone flash pulses
  const flashes = [T.produk, ...POL_T()]; let f = 0; for (const x of flashes) f = Math.max(f, Math.exp(-Math.max(0, t - x) * 9) * (t >= x ? 1 : 0)); Hh.flash.material.opacity = f; Hh.flash.visible = f > 0.01;
  // bottle turns to show its side on "samping", back to the front for the detail
  Hh.bottle.rotation.y = -Math.PI / 2 * U(t, T.samping - 0.25, T.samping + 0.05, "io") * (1 - U(t, T.detail - 0.3, T.detail, "io"));
  // step 1 polaroids: eject from the phone and land on the rail (spring)
  POL_T().forEach((t0, k) => { const m = Hh.pol[k]; m.visible = t > t0 && t < 16.4; if (!m.visible) return;
    const u = U(t, t0, t0 + 0.55, "out"), sp = spring(t, t0 + 0.3, 0.45), [x, y, z] = RAIL[k];
    m.position.set(PHONE.x + (x - PHONE.x) * u, PHONE.y + (y - PHONE.y) * u + 0.45 * Math.sin(Math.PI * u), PHONE.z + (z - PHONE.z) * u);
    m.rotation.set(0, (1 - u) * 4, 0.12 * (1 - sp) * (k - 1) + (k === 0 ? 0 : (k === 1 ? -0.05 : 0.05))); m.scale.setScalar(0.4 + 0.6 * u);
    if (k === 0 && t > T.dua - 0.4) {   // shared element: the front photo flies into the lens (match cut to the chat attachment)
      const w = EZ.in(cl((t - T.dua + 0.4) / 0.38, 0, 1)), cp = new THREE.Vector3(0.1, 1.33, 2.3), tg = new THREE.Vector3(0, 1.255, 0.56);
      const P = cp.clone().add(tg.clone().sub(cp).normalize().multiplyScalar(0.27)); m.position.lerp(P, w); m.rotation.set(0, 0, m.rotation.z * (1 - w)); m.lookAt(cp); m.rotateY(Math.PI * 0);
      if (w < 1) { const q = m.quaternion.clone(); m.rotation.set(0, (1 - u) * 4, 0); m.quaternion.slerp(q, w); } } });
  // hook polaroid: eject, flip to camera, ride into the AI cube
  { const t0 = T.produk + 0.02, u = U(t, t0, t0 + 0.6, "out"), v = U(t, T.ai - 0.05, T.ai + 0.35, "in"); const m = Hh.hookPol;
    m.visible = t > t0 && t < T.ai + 0.35;
    const p0 = PHONE, p1 = new THREE.Vector3(0.6, 1.9, 1.7), p2 = new THREE.Vector3(0, 2.85, 0.3);
    m.position.copy(p0).lerp(p1, u).lerp(p2, v); m.rotation.set(0, (1 - u) * 5 + v * 3, 0); m.scale.setScalar((0.5 + 0.7 * u) * (1 - 0.85 * v)); }
  // AI cube appears on "AI", spins, then unfolds into the promo screen (shared element)
  { const on = spring(t, T.ai, 0.4), mo = U(t, T.bikinin - 0.05, T.video + 0.05, "io"); Hh.cube.visible = t > T.ai && mo < 0.98 && t < 6;
    Hh.cube.position.set(0, 2.85 + 0.65 * mo, 0.3); Hh.cube.rotation.set(0.4 * (1 - mo), t * 2.4 * (1 - mo), 0); Hh.cube.scale.set(Math.max(0.001, on) * (1 + 2.0 * mo), Math.max(0.001, on) * (1 + 4.4 * mo), Math.max(0.001, on) * (1 - 0.85 * mo));
    Hh.cg.visible = Hh.cube.visible; Hh.cg.position.copy(Hh.cube.position); Hh.cg.material.opacity = 0.7 * on * (1 - mo);
    const b = U(t, T.video - 0.15, T.video + 0.2, "out"); Hh.bill.visible = t > T.video - 0.15 && t < 10.5; Hh.bill.scale.set(0.3 + 0.7 * b, 0.25 + 0.75 * b, 1);
    if (Hh.bill.visible) Hh.promo.update(t); }
  // speaker rings on "suara marketer"
  Hh.spk.visible = t < 10.5 && t > T.video - 0.1; const ring0 = T.suara - 0.05;
  { const sp = spring(t, T.video - 0.1, 0.45); Hh.spk.scale.setScalar(Math.max(0.001, sp)); }
  Hh.rings.forEach((r, i) => { const u = ((t - ring0) * 1.4 + (i % 2) / 2) % 1; r.visible = t > ring0 && t < 6.5 && u >= 0; r.scale.setScalar(1 + 1.8 * u); r.material.opacity = 0.9 * (1 - u); });
  const pump = t > ring0 ? 1 + 0.18 * envAt(t) : 1; Hh.cone.forEach((c) => c.scale.set(pump, pump, 1));
  Hh.rig.visible = true;
}

/* ---------------------------------------------------------------- X: who it's for (three islets) */
const Xx = {};
function buildX() {
  const g = mk("X"); clouds("X", 8, 31);
  Xx.isl = [[-3.4, 0, 0], [0, 0.5, -0.6], [3.4, 0, 0]].map(([x, y, z]) => { const s = new THREE.Group(); s.position.set(x, y, z); g.add(s); s.add(island(1, 1)); return s; });
  // UMKM: warung stall with an awning
  const w = Xx.isl[0]; w.add(boxes([[0, 0.4, 0.2, 1.8, 0.8, 0.7, "#e9cfa8"], [0, 0.83, 0.2, 1.9, 0.06, 0.8, "#c79a6b"], [-0.85, 1.2, -0.25, 0.08, 1.5, 0.08, "#8a6a4a"], [0.85, 1.2, -0.25, 0.08, 1.5, 0.08, "#8a6a4a"]]));
  for (let i = 0; i < 6; i++) w.add(boxes([[-0.8 + i * 0.32, 1.95, 0.05, 0.32, 0.08, 1.1, i % 2 ? "#ffffff" : "#01ccf7"]]));
  w.add(boxes([[-0.5, 0.98, 0.25, 0.22, 0.24, 0.22, "#b8322a"], [-0.5, 1.12, 0.25, 0.24, 0.05, 0.24, "#2b3348"], [0.1, 1.02, 0.25, 0.2, 0.34, 0.2, "#c79a6b"], [0.55, 0.98, 0.25, 0.16, 0.26, 0.12, "#f0a92a"]]));
  // online shop: parcel stack
  const o = Xx.isl[1]; Xx.box = [[0, 0.3, 0, 0.9, 0.6, 0.7], [0.15, 0.85, 0.05, 0.7, 0.5, 0.6], [-0.1, 1.3, 0, 0.55, 0.4, 0.5]].map(([x, y, z, a, b, c]) => {
    const m = boxes([[0, 0, 0, a, b, c, "#c9955e"], [0, 0, c / 2 + 0.006, 0.08, b, 0.01, "#e8d2b0"], [0, b / 2 + 0.006, 0, 0.08, 0.01, c, "#e8d2b0"]]); m.position.set(x, y, z); o.add(m); return m; });
  // affiliator: a creator with a phone and a little yellow cart
  const a = Xx.isl[2]; Xx.p = person({ skin: "#f1c39d", hair: "#2a1e18", top: "#2f6bff", top2: "#2559d6", pants: "#26314d", fringe: [[-0.36, 0.18], [-0.18, 0.14], [0, 0.2], [0.18, 0.12], [0.36, 0.18]] });
  Xx.p.root.scale.setScalar(0.7); Xx.p.root.position.set(-0.3, 0, 0.1); a.add(Xx.p.root); Xx.p.setMouth("smile");
  Xx.p.armR.add(boxes([[0, -0.62, 0.16, 0.2, 0.34, 0.03, "#111827"]])); Xx.p.armR.rotation.x = -1.2;
  Xx.cart = cartMesh(0.55); Xx.cart.position.set(0.55, 0.0, 0.25); a.add(Xx.cart);
  Xx.lb = ["UMKM", "ONLINE SHOP", "AFFILIATOR"].map((s, i) => { const l = label(s, "#01ccf7", "#fff", 0.62); l.position.set(Xx.isl[i].position.x, Xx.isl[i].position.y + 2.65, 0.3); g.add(l); return l; });
}
function cartMesh(s) { const c = new THREE.Group(); const Y = "#ffc531";
  c.add(boxes([[0, 0.55, 0, 1.0, 0.08, 0.7, Y], [0, 0.85, 0.35, 1.0, 0.6, 0.06, Y], [0, 0.85, -0.35, 1.0, 0.6, 0.06, Y], [0.5, 0.85, 0, 0.06, 0.6, 0.7, Y], [-0.5, 0.85, 0, 0.06, 0.6, 0.7, Y],
    [-0.75, 1.15, 0, 0.5, 0.06, 0.06, "#2b3348"], [-0.52, 1.0, 0, 0.06, 0.3, 0.06, Y], [-0.3, 0.12, 0.32, 0.18, 0.18, 0.08, "#2b3348"], [0.35, 0.12, 0.32, 0.18, 0.18, 0.08, "#2b3348"],
    [-0.3, 0.12, -0.32, 0.18, 0.18, 0.08, "#2b3348"], [0.35, 0.12, -0.32, 0.18, 0.18, 0.08, "#2b3348"], [0, 0.32, 0.3, 0.06, 0.4, 0.06, Y], [0, 0.32, -0.3, 0.06, 0.4, 0.06, Y]]));
  c.scale.setScalar(s); return c; }
function animX(t) {
  const AT = [T.cocok + 0.2, T.online - 0.15, T.sampai - 0.1], LH = [2.65, 2.1, 2.65], fade = 1 - U(t, 10.2, 10.4);
  Xx.isl.forEach((s, i) => { const u = spring(t, AT[i], 0.5); s.visible = t > AT[i] - 0.05; s.position.y = [0, 0.5, 0][i] - 3 * (1 - Math.min(1, U(t, AT[i] - 0.05, AT[i] + 0.35, "out"))) + 0.04 * Math.sin(t * 2 + i);
    s.scale.setScalar(Math.max(0.001, 0.6 + 0.4 * u)); setLabel(Xx.lb[i], EZ.back(cl((t - AT[i] - 0.1) / 0.3, 0, 1)) * fade); Xx.lb[i].position.y = s.position.y + LH[i]; });
  Xx.box.forEach((m, i) => (m.rotation.y = 0.1 * Math.sin(t * 1.5 + i)));
  Xx.p.eyes.forEach((e) => (e.scale.y = blinkAt(t, 0.7))); Xx.p.head.rotation.y = 0.2 * Math.sin(t * 1.3);
  Xx.cart.rotation.y = 0.3 * Math.sin(t * 1.1) - 0.4;
}

/* ---------------------------------------------------------------- N: the chat window (html-demo View(t)) + the script tower */
const Nn = {};
const CW = 1280, CH = 760;   // chat canvas; plane 4.0 x 2.375
const PROMPT = "Buatkan naskah video promo 30 detik + adegan per detik.";
const TYPE0 = () => T.dua + 0.12, TYPE1 = () => T.kirim + 0.45, SEND = () => T.asisten + 0.02;
const ROWS = [["0–3 dtk", "Hook: Ngantuk jam 2?"], ["3–15 dtk", "Manfaat 1·2·3 + foto"], ["15–25 dtk", "Harga + ukuran"], ["25–30 dtk", "Ajakan: keranjang kuning"]];
const ROW_T = () => [T.susunan - 0.05, T.adegan, T.detik - 0.05, T.detik2 - 0.15];
const CHIPS = [["Rp55.000", () => T.harga], ["1 liter", () => T.ukuran], ["Pekerja kantoran", () => T.siapa]];
const BX = 230, BY = 96, TH = [96, 118];
function chatView(g, w, h, t) {
  g.fillStyle = "#081236"; g.fillRect(0, 0, w, h);
  // title bar
  g.fillStyle = "#0e1d52"; g.fillRect(0, 0, w, 80); g.fillStyle = "#294b77"; for (let i = 0; i < 3; i++) { g.beginPath(); g.arc(36 + i * 30, 40, 10, 0, Math.PI * 2); g.fill(); }
  g.fillStyle = "#ffffff"; g.font = `700 40px ${FONT}`; g.fillText("Claude", 206, 55); g.fillStyle = "#8fa6d6"; g.font = `400 30px ${FONT}`; g.fillText("· chat baru", 352, 55);
  g.strokeStyle = CY; g.lineWidth = 3; rr(g, w - 280, 16, 254, 48, 24); g.stroke(); g.fillStyle = CY; g.font = `700 27px ${FONT}`; g.textAlign = "center"; g.fillText("CONTOH ALUR", w - 153, 50); g.textAlign = "left";
  // user bubble: 3 photo thumbs + typed prompt + chips
  const bx = BX, by = BY, bw = w - bx - 26;
  const typed = Math.max(0, Math.min(PROMPT.length, Math.floor((t - TYPE0()) / (TYPE1() - TYPE0()) * PROMPT.length)));
  const sent = t >= SEND();
  const nChips = CHIPS.filter(([, f]) => t >= f() - 0.05).length;
  const bh = 162 + (nChips ? 70 : 0);
  g.fillStyle = sent ? "rgba(1,204,247,.16)" : "rgba(1,204,247,.07)"; rr(g, bx, by, bw, bh, 24); g.fill(); g.strokeStyle = "rgba(1,204,247,.55)"; g.lineWidth = 2; rr(g, bx, by, bw, bh, 24); g.stroke();
  for (let k = 0; k < 3; k++) { const s = Math.min(1.05, spring(t, T.dua - 0.25 + k * 0.08, 0.35)); if (s <= 0) continue; g.save(); g.translate(bx + 22 + k * 106 + TH[0] / 2, by + 22 + TH[1] / 2); g.scale(s, s); g.drawImage(TX.pol[k].image, -TH[0] / 2, -TH[1] / 2, TH[0], TH[1]); g.restore(); }
  g.fillStyle = "#ffffff"; g.font = `400 40px ${FONT}`;
  const tx0 = bx + 350, maxW = bw - 350 - 140;
  const txt = PROMPT.slice(0, typed), words = txt.split(" "); let line = "", ly = by + 62, lines = [];
  for (const wd of words) { const tst = line ? line + " " + wd : wd; if (g.measureText(tst).width > maxW) { lines.push(line); line = wd; } else line = tst; } lines.push(line);
  lines.slice(0, 2).forEach((l, i) => g.fillText(l, tx0, ly + i * 52));
  if (!sent && t > TYPE0() - 0.3) { const li = Math.min(1, lines.length - 1); const cxp = tx0 + g.measureText(lines[li]).width + 4; if (Math.floor(t * 4) % 2 === 0) { g.fillStyle = CY; g.fillRect(cxp, ly + li * 52 - 34, 4, 44); } }
  // chips (include price, size, target)
  let cx = bx + 22; CHIPS.forEach(([s, f]) => { g.font = `700 34px ${FONT}`; const cw = g.measureText("+ " + s).width + 44; const p = spring(t, f() - 0.05, 0.4);
    if (p > 0) { g.save(); g.translate(cx + cw / 2, by + 194); g.scale(Math.min(1.06, p), Math.min(1.06, p)); g.fillStyle = CY; rr(g, -cw / 2, -27, cw, 54, 27); g.fill(); g.fillStyle = INK; g.fillText("+ " + s, -cw / 2 + 22, 12); g.restore(); }
    cx += cw + 16; });
  // send button + cursor
  const sx = bx + bw - 132, sy = by + 162 - 70; const press = t > SEND() && t < SEND() + 0.18 ? 0.88 : 1;
  g.save(); g.translate(sx + 56, sy + 26); g.scale(press, press); g.fillStyle = sent ? "#294b77" : CY; rr(g, -56, -26, 112, 52, 26); g.fill(); g.fillStyle = sent ? "#9fb3d1" : INK; g.font = `700 28px ${FONT}`; g.textAlign = "center"; g.fillText("Kirim", 0, 10); g.textAlign = "left"; g.restore();
  { const a0 = TYPE1() - 0.55, a1 = SEND() - 0.12; const u = EZ.io(cl((t - a0) / (a1 - a0), 0, 1)); const out = U(t, SEND() + 0.35, SEND() + 0.9, "io");
    if (t > a0 - 0.1 && t < SEND() + 0.95) { const x = 760 + (sx + 66 - 760) * u + 300 * out, y = h - 40 + (sy + 34 - (h - 40)) * u + 200 * out; drawCursor(g, x, y, t > SEND() - 0.02 && t < SEND() + 0.16); } }
  // assistant reply
  if (sent) { const ry = by + bh + 18; const think = t < T.nulis - 0.05;
    g.fillStyle = "#12205a"; rr(g, 26, ry, w - 52, h - ry - 14, 22); g.fill();
    if (LOGO_IMG) g.drawImage(LOGO_IMG, 46, ry + 16, 46, 46);
    if (think) { for (let i = 0; i < 3; i++) { const a = 0.35 + 0.65 * Math.max(0, Math.sin(t * 9 - i * 0.9)); g.fillStyle = `rgba(1,204,247,${a.toFixed(2)})`; g.beginPath(); g.arc(126 + i * 28, ry + 39, 9, 0, Math.PI * 2); g.fill(); } }
    else { g.fillStyle = "#ffffff"; g.font = `700 36px ${FONT}`; g.fillText("Siap! Naskah + adegan (30 dtk):", 110, ry + 52);
      const RT = ROW_T(), hiI = t >= T.detik - 0.05 && t < T.detik2 + 0.5 ? Math.min(3, Math.floor((t - T.detik + 0.05) / 0.22)) : -1;
      const rows = ROWS;
      rows.forEach(([tc, s], i) => { const p = U(t, RT[i], RT[i] + 0.25, "out"); if (p <= 0) return; const y = ry + 76 + i * 60; g.globalAlpha = p;
        const hi = i === hiI; g.fillStyle = hi ? CY : "rgba(1,204,247,.18)"; rr(g, 54 - 20 * (1 - p), y, 200, 50, 25); g.fill();
        g.fillStyle = hi ? INK : CY; g.font = `700 29px ${FONT}`; g.textAlign = "center"; g.fillText(tc, 154 - 20 * (1 - p), y + 35); g.textAlign = "left";
        g.fillStyle = "#ffffff"; fitFont(g, [s], 38, w - 330, 400); g.fillText(s, 278, y + 37); g.globalAlpha = 1; }); } }
}
let LOGO_IMG = null;
function drawCursor(g, x, y, down) { g.save(); g.translate(x, y); const s = down ? 0.86 : 1; g.scale(s, s); g.fillStyle = "#ffffff"; g.strokeStyle = INK; g.lineWidth = 3;
  g.beginPath(); g.moveTo(0, 0); g.lineTo(0, 42); g.lineTo(11, 32); g.lineTo(19, 50); g.lineTo(27, 46); g.lineTo(19, 29); g.lineTo(33, 29); g.closePath(); g.fill(); g.stroke();
  if (down) { g.strokeStyle = CY; g.lineWidth = 4; g.beginPath(); g.arc(0, 0, 26, 0, Math.PI * 2); g.stroke(); } g.restore(); }
const BLK_T = () => [T.hook - 0.1, T.manfaat, T.satu1, T.persatu, T.ajakan];
function buildN() {
  const g = mk("N"); g.add(island(5, 4)); clouds("N", 4, 5);
  Nn.chat = dyn(CW, CH, chatView);
  Nn.chat.t2 = new THREE.CanvasTexture(Nn.chat.c); Nn.chat.t2.colorSpace = THREE.SRGBColorSpace; Nn.chat.t2.anisotropy = 8;
  Nn.chat.t.repeat.set(0.5, 1); Nn.chat.t2.repeat.set(0.5, 1); Nn.chat.t2.offset.set(0.5, 0);
  // two halves (elevator doors) with bezel
  Nn.half = [Nn.chat.t, Nn.chat.t2].map((tx, i) => { const s = new THREE.Group(); g.add(s);
    s.add(boxes([[(i ? 1 : -1) * 1.05, 0, -0.07, 2.1 + 0.06, 2.55, 0.12, "#0b1640"]]));
    const m = new THREE.Mesh(new THREE.PlaneGeometry(2.0, 2.375), new THREE.MeshBasicMaterial({ map: tx, toneMapped: false })); m.position.x = (i ? 1 : -1) * 1.0; s.add(m);
    const e = new THREE.Mesh(new THREE.BoxGeometry(2.16, 0.04, 0.05), RIM); e.position.set((i ? 1 : -1) * 1.05, 1.29, 0); s.add(e);
    const e2 = e.clone(); e2.position.y = -1.29; s.add(e2); const e3 = new THREE.Mesh(new THREE.BoxGeometry(0.04, 2.62, 0.05), RIM); e3.position.set((i ? 1 : -1) * 2.12, 0, 0); s.add(e3);
    s.position.y = 1.78; return s; });
  g.add(boxes([[0, 0.3, -0.25, 0.16, 0.6, 0.16, "#5b6b8c"], [0, 0.03, -0.25, 1.4, 0.06, 0.7, "#5b6b8c"]]));
  LOGO.n = logo3d("claude", window.LOGOS.claude.hex, 0.3); LOGO.n.position.set(-1.74, 2.73, 0.2); g.add(LOGO.n);
  // sharp copy of the photo card exactly over its chat thumbnail (the match-cut target)
  Nn.thumb = new THREE.Mesh(new THREE.PlaneGeometry(TH[0] / CW * 4, TH[1] / CH * 2.375), new THREE.MeshBasicMaterial({ map: TX.pol[0], toneMapped: false }));
  Nn.thumb.position.set(THP[0], THP[1], 0.004); g.add(Nn.thumb);
  // script tower (words as architecture) behind the screen
  g.add(boxes([[0, 0.27, -2.3, 2.9, 0.54, 1.4, "#1f3c62"], [0, 0.555, -2.3, 2.94, 0.03, 1.44, "#01ccf7"]]));
  Nn.blk = TX.blocks.map((tx, i) => { const m = new THREE.Mesh(new THREE.BoxGeometry(2.5, 0.4, 1.0), [MATW, MATW, MATW, MATW, new THREE.MeshStandardMaterial({ map: tx, roughness: 0.6 }), MATW]);
    m.castShadow = m.receiveShadow = true; m.userData.y = 0.78 + i * 0.43; m.visible = false; g.add(m); return m; });
  Nn.cart = cartMesh(0.62); g.add(Nn.cart);
  Nn.clb = label("KERANJANG KUNING", "#01ccf7", "#fff", 0.3); g.add(Nn.clb);
  Nn.dust = []; for (let i = 0; i < 10; i++) { const d = boxes([[0, 0, 0, 0.08, 0.08, 0.08, "#dfe7f3"]], MAT, false); d.castShadow = false; d.visible = false; g.add(d); Nn.dust.push(d); }
  Nn.lb = label("2 · NASKAH", "#01ccf7", "#fff", 1.6); Nn.lb.position.set(0, 4.6, 0); g.add(Nn.lb);
}
const MATW = new THREE.MeshStandardMaterial({ color: 0xf4f7fc, roughness: 0.6 });
const THP = [(BX + 24 + TH[0] / 2) / CW * 4 - 2, 1.78 + 1.1875 - (BY + 22 + TH[1] / 2) / CH * 2.375];
const DOORS = () => [T.hook - 0.42, T.hook - 0.05];
function animN(t) {
  const [d0, d1] = DOORS(); const op = U(t, d0, d1, "in");
  Nn.half.forEach((s, i) => { s.position.x = (i ? 1 : -1) * 3.4 * op; s.visible = op < 0.99; });
  if ((t > 15.9 && t < d1 + 0.05) || (t > 5.3 && t < 7.8)) Nn.chat.update(t);
  Nn.thumb.visible = t < T.dua + 0.55;
  LOGO.n.visible = op < 0.5 && t > 16; LOGO.n.rotation.y = t > SEND() && t < T.detik2 ? (t - SEND()) * 5 : 0.4 * Math.sin(t * 1.4); LOGO.n.position.x = -1.74 - 3.4 * op;
  // blocks drop and stack (small-overshoot landing + dust)
  const BT = BLK_T();
  Nn.blk.forEach((m, i) => { const t0 = BT[i]; m.visible = t > t0 - 0.3; if (!m.visible) return; const u = U(t, t0 - 0.3, t0, "in"), s = t - t0;
    m.scale.setScalar(Math.max(0.001, 0.3 + 0.7 * Math.min(1.04, spring(t, t0 - 0.3, 0.35)))); m.position.set(0, m.userData.y + (i === 4 ? 0 : 0.45) * (1 - u) + (s > 0 ? Math.exp(-s * 9) * Math.abs(Math.sin(s * 16)) * 0.08 : 0), -2.3); m.rotation.y = (1 - u) * 0.6; });
  Nn.dust.forEach((d, i) => { const k = i % 5, t0 = BT[k], s = t - t0; d.visible = s > 0 && s < 0.45; if (!d.visible) return; const a = (i / 10) * Math.PI * 2;
    d.position.set(Math.cos(a) * (1.3 + s * 1.2), Nn.blk[k].userData.y - 0.2 + s * 0.6 - s * s * 2, -2.3 + Math.sin(a) * (0.6 + s)); d.scale.setScalar(1 - s / 0.45); });
  // the yellow cart rolls in beside the top block on "keranjang"
  { const c0 = T.keranjang - 0.35, u = U(t, c0, c0 + 0.5, "out"); Nn.cart.visible = t > c0; Nn.cart.position.set(1.75 + 3.2 * (1 - u), 0.0 + 0.04 * Math.abs(Math.sin((t - c0) * 14)) * (1 - u), -1.2); Nn.cart.rotation.y = -0.45;
    Nn.clb.visible = false; }
}

/* ---------------------------------------------------------------- S: AI voice booth (waveform from the real VO) */
const Ss = {};
function buildS() {
  const g = mk("S"); g.add(island(5, 4)); clouds("S", 9, 7);
  g.add(boxes([[0, 0.2, -1.1, 3.3, 0.4, 0.6, "#1f3c62"], [0, 0.415, -1.1, 3.34, 0.03, 0.64, "#01ccf7"]]));
  Ss.bars = []; for (let i = 0; i < 19; i++) { const m = new THREE.Mesh(new THREE.BoxGeometry(0.12, 1, 0.12), emi(i % 2 ? "#36e0ff" : "#7fe8ff", 1.4)); m.position.set(-1.44 + i * 0.16, 0.43, -1.1); g.add(m); Ss.bars.push(m); }
  // microphone
  Ss.mic = new THREE.Group(); Ss.mic.position.set(-1.5, 0, 0.75); g.add(Ss.mic);
  Ss.mic.add(boxes([[0, 0.03, 0, 0.5, 0.06, 0.5, "#5b6b8c"], [0, 0.75, 0, 0.05, 1.5, 0.05, "#8a9bb8"], [0, 1.62, 0, 0.24, 0.4, 0.24, "#3a4560"], [0, 1.62, 0.125, 0.18, 0.3, 0.01, "#7f8aa8"]]));
  const pf = new THREE.Mesh(new THREE.TorusGeometry(0.2, 0.02, 6, 30), RIM); pf.position.set(0, 1.62, 0.32); Ss.mic.add(pf);
  // script page that gets read line by line
  Ss.page = dyn(360, 260, (gg, w, h, t) => { gg.fillStyle = "#ffffff"; gg.fillRect(0, 0, w, h); gg.fillStyle = INK; gg.font = `700 34px ${FONT}`; gg.fillText("NASKAH", 24, 48);
    const p = cl((t - T.naskah2) / (T.jualan + 0.6 - T.naskah2), 0, 1) * 5; for (let i = 0; i < 5; i++) { const k = cl(p - i, 0, 1); gg.fillStyle = "#c9d6ea"; rr(gg, 24, 76 + i * 34, 300 - (i % 2) * 60, 14, 7); gg.fill();
      if (k > 0) { gg.fillStyle = CY; rr(gg, 24, 76 + i * 34, (300 - (i % 2) * 60) * k, 14, 7); gg.fill(); } } });
  Ss.pg = new THREE.Mesh(new THREE.PlaneGeometry(0.78, 0.563), new THREE.MeshBasicMaterial({ map: Ss.page.t, toneMapped: false, side: THREE.DoubleSide })); g.add(Ss.pg);
  // marketer (voxel character with a headset, holding the CONTOH bottle)
  Ss.p = person({ skin: "#e8b48f", hair: "#2a1e18", top: "#01a9d1", top2: "#0190b3", pants: "#26314d", fringe: [[-0.36, 0.16], [-0.18, 0.12], [0, 0.18], [0.18, 0.12], [0.36, 0.16]] });
  Ss.p.root.position.set(1.22, 0, 0.6); Ss.p.root.rotation.y = -0.35; Ss.p.root.scale.setScalar(0.9); g.add(Ss.p.root);
  Ss.p.head.add(boxes([[0, 0.98, 0, 0.98, 0.07, 0.12, "#1b2238"], [-0.5, 0.45, 0, 0.1, 0.24, 0.24, "#1b2238"], [0.5, 0.45, 0, 0.1, 0.24, 0.24, "#1b2238"], [-0.45, 0.24, 0.24, 0.04, 0.04, 0.3, "#1b2238"], [-0.38, 0.22, 0.4, 0.08, 0.08, 0.08, "#01ccf7"]]));
  const mb = productBottle(); mb.scale.setScalar(0.5); mb.position.set(0, -0.75, 0.12); Ss.p.armR.add(mb);
  Ss.rings = [0, 1, 2].map(() => { const r = new THREE.Mesh(new THREE.TorusGeometry(0.35, 0.03, 6, 40), new THREE.MeshBasicMaterial({ color: 0x5fe6ff, transparent: true, toneMapped: false })); g.add(r); return r; });
  LOGO.el = logo3d("elevenlabs", "#ffffff", 0.36); LOGO.el.position.set(-1.5, 2.2, 0.75); g.add(LOGO.el);
  Ss.lb = label("3 · SUARA", "#01ccf7", "#fff", 1.6); Ss.lb.position.set(0, 4.6, 0); g.add(Ss.lb);
}
const MATN = new THREE.MeshStandardMaterial({ color: 0x0b1640, roughness: 0.5 });
function animS(t) {
  const on = t > T.naskah2 - 0.2;
  Ss.bars.forEach((m, i) => { const e = on ? envAt(t - (18 - i) * 0.045) : 0.05 + 0.04 * Math.sin(t * 2 + i); const h = 0.08 + 1.55 * e * (0.55 + 0.45 * Math.abs(Math.sin(i * 1.9))); m.scale.y = h; m.position.y = 0.43 + h / 2; });
  if (t > 30 && t < 36.5) Ss.page.update(t);
  const pu = U(t, T.naskah2 - 0.3, T.naskah2 + 0.2, "out"); Ss.pg.visible = t > T.naskah2 - 0.3; Ss.pg.position.set(-0.6, 1.62 + 1.0 * (1 - pu) + 0.03 * Math.sin(t * 2), 1.15); Ss.pg.rotation.set(-0.15, 0.25 + (1 - pu) * 2, 0);
  { const u = spring(t, T.suara2 - 0.05, 0.45); LOGO.el.visible = t > T.suara2 - 0.05; LOGO.el.scale.setScalar(Math.max(0.001, u)); LOGO.el.rotation.y = 0.5 * Math.sin(t * 1.6); LOGO.el.position.y = 2.2 + 0.05 * Math.sin(t * 2.2); }
  // marketer rises from a trapdoor on "gaya marketer", pitches the bottle
  const r = U(t, T.gaya - 0.15, T.gaya + 0.3, "out"), p = Ss.p; p.root.position.y = -2.2 * (1 - r); p.root.visible = t > T.gaya - 0.15;
  p.eyes.forEach((e) => (e.scale.y = blinkAt(t, 0.5))); p.setMouth(envAt(t) > 0.35 ? "o" : "smile");
  p.armR.rotation.set(-1.4 - 0.25 * Math.max(0, Math.sin(t * 5)), 0, -0.2); p.armL.rotation.set(-0.5 + 0.35 * Math.sin(t * 6), 0, 0.5); p.head.rotation.set(0, 0.25 * Math.sin(t * 2.2), 0.05 * Math.sin(t * 3));
  Ss.rings.forEach((m, i) => { const u = ((t - T.jualan + 0.1) * 1.5 + i / 3) % 1; m.visible = t > T.jualan - 0.1 && u >= 0 && t < 36.3; m.position.set(1.0, 1.4, 1.0); m.rotation.y = -0.35; m.scale.setScalar(1 + 2.6 * u); m.material.opacity = 0.85 * (1 - u); });
}

/* ---------------------------------------------------------------- R: render machine (process fill) -> vertical video -> "this reel" */
const Rr = {};
function machineView(g, w, h, t) {
  g.fillStyle = "#081236"; g.fillRect(0, 0, w, h);
  const p = cl((t - T.dirender) / 0.75, 0, 1), done = p >= 1;
  g.fillStyle = "#ffffff"; g.textAlign = "center"; g.font = `700 52px ${FONT}`;
  if (!done) { const n = IN_T().filter((x) => t >= x + 0.4).length; g.fillText(t < T.dirender ? "BAHAN " + n + "/3" : "RENDER…", w / 2, 88); g.fillStyle = "#1b2f60"; rr(g, 60, 128, w - 120, 46, 23); g.fill(); g.fillStyle = CY; rr(g, 60, 128, Math.max(46, (w - 120) * p), 46, 23); g.fill();
    g.fillStyle = "#9fdcff"; g.font = `700 34px ${FONT}`; g.fillText(Math.round(p * 100) + "%", w / 2, 230); }
  else { g.strokeStyle = CY; g.lineWidth = 22; g.lineCap = "round"; g.lineJoin = "round"; g.beginPath(); g.moveTo(w / 2 - 70, 140); g.lineTo(w / 2 - 15, 192); g.lineTo(w / 2 + 80, 82); g.stroke(); }
  g.textAlign = "left";
}
function metaView(g, w, h, t) {   // the reel you are watching, drawn small (navy, logo, the two hosts, a caption box) + how it was made
  const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, "#0b1a4a"); gr.addColorStop(1, "#05102e"); g.fillStyle = gr; g.fillRect(0, 0, w, h);
  g.fillStyle = "#ffffff"; g.font = `700 22px ${FONT}`; g.fillText("AI PRENEUR", 22, 40);
  g.fillStyle = "#c3cfe2"; g.beginPath(); g.arc(112, h - 120, 70, 0, Math.PI * 2); g.fill(); g.fillStyle = "#2a1e18"; rr(g, 52, h - 205, 120, 50, 22); g.fill();
  g.fillStyle = "#f1c39d"; g.beginPath(); g.arc(112, h - 140, 46, 0, Math.PI * 2); g.fill(); g.fillStyle = "#1b2238"; rr(g, 50, h - 70, 124, 70, 16); g.fill();
  g.fillStyle = "#eef3fb"; rr(g, 230, h - 150, 92, 84, 26); g.fill(); g.fillStyle = "#0b1640"; rr(g, 242, h - 138, 68, 44, 14); g.fill(); g.fillStyle = CY; g.fillRect(256, h - 122, 10, 12); g.fillRect(286, h - 122, 10, 12);
  g.fillStyle = "rgba(10,13,44,.85)"; rr(g, 34, h - 300, w - 68, 54, 14); g.fill(); g.fillStyle = "#ffffff"; g.textAlign = "center"; g.font = `700 26px ${FONT}`; fitFont(g, ["Video yang lagi kamu tonton"], 26, w - 100); g.fillText("Video yang lagi kamu tonton", w / 2, h - 264); g.textAlign = "left";
  const R = [["Naskah + adegan", "Claude", T.juga], ["Suara", "AI voice", T.dibikin + 0.2], ["Render", "HyperFrames", T.pakai + 0.1]];
  R.forEach(([a, b, t0], i) => { const p = spring(t, t0, 0.4); if (p <= 0) return; const y = 76 + i * 92; g.save(); g.translate(w / 2, y + 38); g.scale(0.7 + 0.3 * Math.min(1, p), 0.7 + 0.3 * Math.min(1, p)); g.translate(-w / 2, -(y + 38));
    g.fillStyle = "rgba(1,204,247,.16)"; rr(g, 22, y, w - 44, 78, 18); g.fill(); g.strokeStyle = CY; g.lineWidth = 2; rr(g, 22, y, w - 44, 78, 18); g.stroke();
    g.fillStyle = CY; g.beginPath(); g.arc(56, y + 39, 17, 0, Math.PI * 2); g.fill(); g.strokeStyle = INK; g.lineWidth = 5; g.beginPath(); g.moveTo(47, y + 39); g.lineTo(54, y + 46); g.lineTo(66, y + 32); g.stroke();
    g.fillStyle = "#9fdcff"; g.font = `400 25px ${FONT}`; g.fillText(a, 86, y + 32); g.fillStyle = "#ffffff"; fitFont(g, [b], 36, w - 120); g.fillText(b, 86, y + 68); g.restore(); });
}
const IN_T = () => [T.adegan2, T.foto2, T.suara3];
const MX = -0.75, PH = [1.45, 1.32, 0.3];   // machine x, phone resting spot (beside the machine)
function buildR() {
  const g = mk("R"); g.add(island(5, 4)); clouds("R", 9, 13);
  Rr.mach = new THREE.Group(); Rr.mach.position.x = MX; g.add(Rr.mach);
  Rr.mach.add(boxes([[0, 0.8, 0, 2.1, 1.6, 1.3, "#f3f6fb"], [0, 1.72, 0, 1.1, 0.24, 0.8, "#2b3348"], [0, 1.88, 0, 1.3, 0.08, 1.0, "#3a4560"], [0, 0.1, 0, 2.2, 0.2, 1.4, "#c3cfe2"],
    [-1.06, 0.8, 0.4, 0.04, 1.2, 0.04, "#01ccf7"], [1.06, 0.8, 0.4, 0.04, 1.2, 0.04, "#01ccf7"], [1.07, 1.05, 0.1, 0.06, 0.5, 0.9, "#2b3348"]]));
  Rr.scr = dyn(520, 280, machineView);
  const s = new THREE.Mesh(new THREE.PlaneGeometry(1.6, 0.86), new THREE.MeshBasicMaterial({ map: Rr.scr.t, toneMapped: false })); s.position.set(0, 0.95, 0.655); Rr.mach.add(s);
  Rr.lamp = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.16, 0.16), emi("#36e0ff", 0.4)); Rr.lamp.position.set(0.85, 1.72, 0.3); Rr.mach.add(Rr.lamp);
  Rr.cards = [TX.storyboard, TX.pol[0], TX.wave].map((tx) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(0.5, 0.617), new THREE.MeshBasicMaterial({ map: tx, toneMapped: false, side: THREE.DoubleSide })); g.add(m); return m; });
  // the output: a vertical phone that slides out of the side slot
  Rr.phone = new THREE.Group(); g.add(Rr.phone);
  Rr.phone.add(boxes([[0, 0, -0.03, 0.9, 1.6, 0.07, "#111827"]]));
  Rr.pv = dyn(360, 640, (gg, w, h, t) => (t < T.video3 + 0.45 ? promoView(gg, w, h, t - T.video2, t) : metaView(gg, w, h, t)));
  const ps = new THREE.Mesh(new THREE.PlaneGeometry(0.82, 1.458), new THREE.MeshBasicMaterial({ map: Rr.pv.t, toneMapped: false })); ps.position.z = 0.01; Rr.phone.add(ps);
  Rr.pg = glow("#38dcff", 2.4, 3.2); Rr.pg.position.z = -0.1; Rr.phone.add(Rr.pg);
  // upload badge on the phone screen ("siap diunggah"): a round navy badge with a cyan arrow
  Rr.up = new THREE.Group(); Rr.up.position.set(0, -0.12, 0.05); Rr.phone.add(Rr.up);
  const disc = new THREE.Mesh(new THREE.CircleGeometry(0.3, 40), new THREE.MeshBasicMaterial({ color: 0x0a1644, toneMapped: false })); Rr.up.add(disc);
  const rim = new THREE.Mesh(new THREE.TorusGeometry(0.3, 0.025, 6, 40), new THREE.MeshBasicMaterial({ color: 0x01ccf7, toneMapped: false })); Rr.up.add(rim);
  const arrowMat = new THREE.MeshBasicMaterial({ color: 0x01ccf7, toneMapped: false });
  const shp = new THREE.Shape(); shp.moveTo(0, 0.2); shp.lineTo(0.15, 0.04); shp.lineTo(0.055, 0.04); shp.lineTo(0.055, -0.17); shp.lineTo(-0.055, -0.17); shp.lineTo(-0.055, 0.04); shp.lineTo(-0.15, 0.04); shp.closePath();
  const ar = new THREE.Mesh(new THREE.ShapeGeometry(shp), arrowMat); ar.position.z = 0.005; Rr.up.add(ar);
  Rr.ulb = label("SIAP DIUNGGAH", "#01ccf7", "#fff", 0.24); g.add(Rr.ulb);
  Rr.clb = []; Rr.lb = label("4 · RENDER", "#01ccf7", "#fff", 1.6); Rr.lb.position.set(0, 4.6, 0); g.add(Rr.lb);
}
function animR(t) {
  const IT = IN_T(), hop = new THREE.Vector3(MX, 2.0, 0);
  // the three inputs fly in from the left, one per word, and drop into the hopper (process fill)
  Rr.cards.forEach((m, i) => { const t0 = IT[i]; const u = U(t, t0 - 0.25, t0 + 0.42, "io"); m.visible = t > t0 - 0.25 && t < t0 + 0.42;
    const sx = -1.85, sy = 2.05, pop = Math.min(1.05, spring(t, t0 - 0.25, 0.3));
    m.position.set(sx + (hop.x - sx) * u, sy + (hop.y - sy) * u + 0.35 * Math.sin(Math.PI * u), 0.4 * (1 - u));
    m.rotation.set(-Math.PI / 2 * EZ.in(u), 0.4 * (1 - u), -0.2 * (1 - u)); m.scale.setScalar(Math.max(0.001, pop) * (1 - 0.5 * EZ.in(u))); });
  const shake = t > T.dirender && t < T.dirender + 0.8 ? 0.025 * Math.sin(t * 70) : 0; Rr.mach.position.x = MX + shake; Rr.mach.rotation.z = shake * 0.6;
  Rr.lamp.material.emissiveIntensity = t > T.dirender && t < T.dirender + 0.8 ? (Math.floor(t * 10) % 2 ? 3 : 0.6) : t > T.dirender ? 2.4 : 0.4;
  if ((t > 35 && t < 44.4) || (t > 5.3 && t < 7.8)) { Rr.scr.update(t); Rr.pv.update(t); }
  // the phone slides out of the side slot on "video vertikal" and stands up beside the machine
  const pu = U(t, T.video2 - 0.25, T.video2 + 0.35, "out"), ps = spring(t, T.video2 - 0.25, 0.5); Rr.phone.visible = t > T.video2 - 0.25;
  Rr.phone.position.set(MX + 1.0 + (PH[0] - MX - 1.0) * pu, 1.05 + (PH[1] - 1.05) * pu + 0.03 * Math.sin(t * 2), PH[2]);
  Rr.phone.rotation.set(0, (1 - pu) * 1.4 + 0.06 * Math.sin(t * 1.2) * (t < T.video3 ? 1 : 0.2), (1 - pu) * -1.2); Rr.phone.scale.setScalar(Math.max(0.001, 0.3 + 0.7 * Math.min(1.04, ps)));
  Rr.pg.material.opacity = 0.55 * pu;
  const uu = Math.min(1.06, spring(t, T.siap - 0.05, 0.4)); Rr.up.visible = t > T.siap - 0.05 && t < T.video3 + 0.3; Rr.up.position.y = -0.12 + 0.03 * Math.sin(t * 6); Rr.up.scale.setScalar(Math.max(0.001, uu * (1 - U(t, T.video3, T.video3 + 0.3))));
  Rr.ulb.visible = false;
  LOGO.r.forEach((o, i) => { const t0 = [T.juga, T.dibikin + 0.2][i], u = spring(t, t0, 0.45); o.visible = t > t0; o.scale.setScalar(Math.max(0.001, u)); o.rotation.y = 0.5 * Math.sin(t * 1.5 + i); o.position.y = 1.95 - i * 0.55 + 0.03 * Math.sin(t * 2 + i); });
}

/* ---------------------------------------------------------------- C: check before posting (+ CTA backdrop) */
const Cc = {};
const CROWS = [["AI = alat bantu produksi", () => T.alat, "ok"], ["Jaminan laku", () => T.jaminan, "x"], ["Klaim produk sesuai fakta?", () => T.klaim, "box"], ["Harga & ukuran benar?", () => T.sebelum, "box"], ["Foto = produk asli?", () => T.posting, "box"]];
function boardView(g, w, h, t) {
  g.fillStyle = "#f4f8ff"; g.fillRect(0, 0, w, h); g.fillStyle = NAVY; g.fillRect(0, 0, w, 92);
  g.fillStyle = "#ffffff"; g.font = `700 50px ${FONT}`; g.fillText("CEK SEBELUM POSTING", 40, 66);
  CROWS.forEach(([s, f, kind], i) => { const t0 = f(), y = 128 + i * 82; const appear = i < 2 ? U(t, t0 - 0.35, t0 - 0.05, "out") : 1; if (appear <= 0) return; g.globalAlpha = appear;
    g.fillStyle = INK; fitFont(g, [s], 46, w - 240); g.fillText(s, 116, y + 52);
    const done = U(t, t0, t0 + 0.2, "out");
    g.strokeStyle = "#294b77"; g.lineWidth = 5; rr(g, 40, y + 12, 50, 50, 10); g.stroke();
    if (kind === "x") { if (done > 0) { g.strokeStyle = CY; g.lineWidth = 8; g.beginPath(); g.moveTo(50, y + 22); g.lineTo(50 + 30 * done, y + 22 + 30 * done); g.moveTo(80, y + 22); g.lineTo(80 - 30 * done, y + 22 + 30 * done); g.stroke();
        g.fillStyle = CY; g.fillRect(114, y + 34, (g.measureText(s).width + 12) * done, 7); } }
    else if (done > 0) { g.fillStyle = CY; rr(g, 40, y + 12, 50, 50, 10); g.fill(); g.strokeStyle = INK; g.lineWidth = 7; g.beginPath(); g.moveTo(52, y + 38); g.lineTo(52 + 10 * Math.min(1, done * 2), y + 38 + 10 * Math.min(1, done * 2));
      if (done > 0.5) g.lineTo(62 + 18 * (done - 0.5) * 2, y + 48 - 22 * (done - 0.5) * 2); g.stroke(); }
    g.globalAlpha = 1; });
}
const BW = 3.0, BH = 1.867, BCY = 1.85;
function buildC() {
  const g = mk("C"); g.add(island(5, 4)); clouds("C", 9, 17);
  Cc.bd = dyn(900, 560, boardView);
  Cc.brd = new THREE.Group(); g.add(Cc.brd);
  Cc.brd.add(boxes([[0, BCY, -0.06, BW + 0.14, BH + 0.12, 0.1, "#c3cfe2"], [0, BCY + BH / 2 + 0.1, 0.0, 0.8, 0.18, 0.16, "#8a9bb8"], [-1.25, (BCY - BH / 2) / 2, -0.1, 0.1, BCY - BH / 2, 0.1, "#8a9bb8"], [1.25, (BCY - BH / 2) / 2, -0.1, 0.1, BCY - BH / 2, 0.1, "#8a9bb8"]]));
  const b = new THREE.Mesh(new THREE.PlaneGeometry(BW, BH), new THREE.MeshBasicMaterial({ map: Cc.bd.t, toneMapped: false })); b.position.set(0, BCY, 0.0); Cc.brd.add(b);
  Cc.mag = new THREE.Group(); g.add(Cc.mag);
  const ring = new THREE.Mesh(new THREE.TorusGeometry(0.15, 0.035, 8, 32), new THREE.MeshStandardMaterial({ color: 0x2b3348, roughness: 0.4 })); Cc.mag.add(ring);
  const lens = new THREE.Mesh(new THREE.CircleGeometry(0.14, 32), new THREE.MeshBasicMaterial({ color: 0x9fe6ff, transparent: true, opacity: 0.3, toneMapped: false })); Cc.mag.add(lens);
  const hd = boxes([[0, -0.2, 0, 0.07, 0.24, 0.07, "#c79a6b"]]); hd.rotation.z = 0.78; Cc.mag.add(hd);
  // after the check: the cart + parcels wait on the island (no text) behind the CTA cards
  Cc.cart = cartMesh(0.7); Cc.cart.position.set(-1.0, 0, 0.6); Cc.cart.rotation.y = 0.5; g.add(Cc.cart);
  Cc.box = boxes([[1.1, 0.3, 0.5, 0.8, 0.6, 0.6, "#c9955e"], [1.2, 0.8, 0.5, 0.6, 0.4, 0.5, "#c9955e"], [1.1, 0.3, 0.806, 0.07, 0.6, 0.01, "#e8d2b0"]]); g.add(Cc.box);
}
function animC(t) {
  if (t > 44 && t < 56) Cc.bd.update(t);
  // the board sinks away before the CTA cards come in (no text left behind the comment box / DM)
  const sink = U(t, T.komen - 0.45, T.komen + 0.05, "in"); Cc.brd.position.y = -3.2 * sink; Cc.brd.visible = sink < 0.999;
  const rise = spring(t, T.komen - 0.05, 0.5); Cc.cart.visible = Cc.box.visible = t > T.komen - 0.1; Cc.cart.scale.setScalar(0.7 * Math.max(0.001, rise)); Cc.box.scale.setScalar(Math.max(0.001, rise));
  Cc.cart.rotation.y = 0.5 + 0.15 * Math.sin(t * 1.3);
  // magnifier hops to the row being checked and rests at its right end
  const rows = CROWS.map(([, f]) => f()); let ri = 0; for (let i = 0; i < rows.length; i++) if (t >= rows[i] - 0.3) ri = i;
  const rowY = (i) => BCY + BH / 2 - (128 + i * 82 + 37) / 560 * BH;
  const prev = Math.max(0, ri - 1), u = U(t, rows[ri] - 0.3, rows[ri], "io");
  const y = ri === 0 ? rowY(0) : rowY(prev) + (rowY(ri) - rowY(prev)) * u;
  Cc.mag.visible = t > T.tapi && t < T.komen - 0.3; Cc.mag.position.set(1.33 + 0.02 * Math.sin(t * 5), y + 0.05 * Math.sin(Math.PI * u), 0.3); Cc.mag.rotation.z = 0.1 * Math.sin(t * 2);
}

/* ---------------------------------------------------------------- the reveal map: chain of 4 islands + glowing path */
const Mp = {};
function buildMap() {
  const P = ["H", "N", "S", "R"].map((k) => new THREE.Vector3(WP[k][0], 0, WP[k][2]));
  Mp.seg = []; for (let i = 0; i < 3; i++) { const a = P[i], b = P[i + 1], len = a.distanceTo(b); const m = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.12, len), emi("#36e0ff", 1.8));
    m.position.copy(a).lerp(b, 0.5); m.position.y = -0.4; m.lookAt(b.x, -0.4, b.z); scene.add(m); Mp.seg.push({ m, a, b }); }
  Mp.dot = glow("#7fe8ff", 2.6, 2.6); scene.add(Mp.dot);
  Mp.P = P;
}
function animMap(t) {
  const vis = t >= MAP[0] && t < MAP[1] + 0.05; const t0 = T.ini - 0.1;
  Mp.seg.forEach((s, i) => { const u = U(t, t0 + i * 0.28, t0 + 0.28 + i * 0.28, "io"); s.m.visible = vis && u > 0.001; s.m.scale.z = Math.max(0.001, u); s.m.position.copy(s.a).lerp(s.b, u / 2); s.m.position.y = -0.4; });
  const k = cl((t - t0) / 0.84, 0, 1) * 3, i = Math.min(2, Math.floor(k)); Mp.dot.visible = vis && t > t0; Mp.dot.position.copy(Mp.P[i]).lerp(Mp.P[i + 1], k - i); Mp.dot.position.y = 0.6;
  [Hh.lb, Nn.lb, Ss.lb, Rr.lb].forEach((l, j) => { l.userData.h = [1.9, 2.3, 2.9, 3.5][j]; setLabel(l, vis ? EZ.back(cl((t - (t0 + j * 0.28 - 0.1)) / 0.3, 0, 1)) * (1 - U(t, MAP[1] - 0.3, MAP[1])) : 0); });
}

/* ---------------------------------------------------------------- camera path (absolute), with cuts */
const C = [];
const at = (w) => (v) => { const [px, py, pz, ry] = WP[w], c = Math.cos(ry), s = Math.sin(ry);
  const tr = (x, y, z) => [px + x * c + z * s, py + y, pz - x * s + z * c]; return [...tr(v[0], v[1], v[2]), ...tr(v[3], v[4], v[5]), v[6]]; };
const k = (w, t, v, e) => C.push([t, at(w)(v), e]);
const cut = (w, t, v) => C.push([t, at(w)(v), "lin"]);
const AB = (t, v, e) => C.push([t, v, e]);
function buildCamera() {
  const P0 = T.produk, AI = T.ai;
  // H — hook, full frame (no hosts yet)
  k("H", 0, [1.3, 1.72, 4.75, 0.35, 1.42, 0.5, 40]); k("H", P0 + 0.3, [1.15, 1.7, 4.4, 0.33, 1.45, 0.5, 40], "sine");
  k("H", AI + 0.3, [0.6, 2.45, 6.4, 0.05, 2.5, 0.4, 40], "io"); k("H", T.video + 0.15, [0.3, 3.05, 8.1, 0, 3.05, 0.3, 40], "io"); k("H", 5.45, [0.15, 3.05, 7.6, 0, 3.05, 0.3, 40], "sine");
  // zoom-out reveal to the map of the whole flow
  AB(6.45, [0, 36, 30, 0, 1, -28, 46], "io"); AB(T.cocok - 0.1, [0, 35.2, 29, 0, 1, -28, 46], "sine");
  // pan to "who it's for"
  k("X", T.cocok + 0.6, [0, 8.6, 25.5, 0, 1.35, -0.3, 40], "io"); k("X", 10.3, [0.5, 8.2, 24.2, 0, 1.35, -0.3, 40], "sine");
  // island-hop flight back to the studio (step 1)
  k("H", 10.98, [0.7, 2.15, 6.9, 0, 1.48, 0.3, 40], "io"); k("H", T.depan - 0.3, [0.4, 2.05, 6.4, 0, 1.48, 0.3, 40], "sine");
  k("H", T.samping - 0.1, [1.2, 2.0, 6.1, 0, 1.48, 0.3, 40], "io"); k("H", T.detail - 0.08, [0.9, 2.0, 6.2, 0, 1.48, 0.3, 40], "sine");
  k("H", T.detail + 0.4, [0.15, 1.34, 2.46, 0, 1.255, 0.56, 40], "io"); k("H", T.kemasan + 0.4, [0.12, 1.33, 2.36, 0, 1.255, 0.56, 40], "sine");
  k("H", T.dua - 0.02, [0.1, 1.33, 2.3, 0, 1.255, 0.56, 40], "sine");
  // N — match cut out of the same photo (now the chat attachment), pull back to the window; screen-studio pushes
  cut("N", T.dua, [THP[0], THP[1], 0.165, THP[0], THP[1], 0, 40]); k("N", T.dua + 0.62, [0, 1.95, 10.9, 0, 1.78, 0, 40], "io");
  k("N", SEND() + 0.25, [0.05, 1.92, 10.7, 0.05, 1.76, 0, 40], "sine"); k("N", T.nulis + 0.2, [0.05, 1.82, 10.4, 0.05, 1.68, 0, 40], "io"); k("N", T.detik2 + 0.3, [0.05, 1.8, 10.2, 0.05, 1.68, 0, 40], "sine");
  k("N", DOORS()[0], [0.0, 1.85, 10.4, 0.0, 1.72, 0, 40], "sine");
  // elevator doors: push through the gap to the tower
  k("N", DOORS()[1] + 0.3, [0.15, 2.22, 8.8, 0.05, 1.5, -2.3, 40], "io"); k("N", T.ajakan + 0.4, [0.25, 2.22, 9.1, 0.12, 1.48, -2.3, 40], "sine");
  k("N", T.keranjang + 0.2, [0.4, 2.22, 9.7, 0.25, 1.45, -2.1, 40], "io"); k("N", T.tiga - 0.35, [0.4, 2.27, 9.6, 0.25, 1.45, -2.1, 40], "sine");
  // vertical whip tilt to the sky -> S
  k("N", T.tiga - 0.04, [0.4, 2.3, 9.6, 0.25, 30, -10, 40], "expo");
  cut("S", T.tiga - 0.03, [0.2, 2.6, 10.6, 0.2, 30, -8, 40]); k("S", T.tiga + 0.6, [0.2, 2.45, 10.9, 0, 1.4, 0, 40], "io");
  k("S", T.gaya - 0.2, [0.0, 2.4, 10.5, 0.0, 1.38, 0, 40], "sine"); k("S", T.jualan + 0.1, [0.15, 2.4, 10.7, 0.05, 1.38, 0, 40], "io");
  // 180° orbit around the midpoint S..R
  { const S0 = WP.S, R0 = WP.R, M = [(S0[0] + R0[0]) / 2, 0, (S0[2] + R0[2]) / 2], o0 = T.jualan + 0.25, o1 = T.empat - 0.02;
    const r0 = Math.hypot(S0[0] + 0.3 - M[0], S0[2] + 10.6 - M[2]), a0 = Math.atan2(S0[0] + 0.3 - M[0], S0[2] + 10.6 - M[2]);
    for (let i = 0; i <= 16; i++) { const u = i / 16, a = a0 + Math.PI * EZ.io(u); const tgt = [S0[0] + (R0[0] - S0[0]) * EZ.io(u), 1.4 + 0.3 * u, S0[2] + (R0[2] - S0[2]) * EZ.io(u)];
      AB(o0 + (o1 - o0) * u, [M[0] + Math.sin(a) * r0, 2.3 + 3.5 * Math.sin(Math.PI * u), M[2] + Math.cos(a) * r0, ...tgt, 40], "lin"); } }
  // R — process fill, phone rises
  k("R", T.adegan2 - 0.1, [-0.2, 2.1, 10.9, -0.2, 1.25, 0, 40], "io"); k("R", T.dirender, [-0.1, 2.05, 10.5, -0.15, 1.25, 0, 40], "sine");
  k("R", T.video2 + 0.3, [0.25, 2.05, 10.6, 0.25, 1.3, 0, 40], "io"); k("R", T.video3 - 0.05, [0.3, 2.0, 10.3, 0.3, 1.3, 0, 40], "sine");
  window.VX.DOLLY = [T.video3, T.kamu + 0.5];   // dolly zoom handled in render()
  k("R", T.kamu + 0.5, [1.2, 1.5, 6.5, 1.2, 1.46, 0.3, 40], "lin"); k("R", T.mirip + 0.3, [1.2, 1.5, 6.25, 1.2, 1.46, 0.3, 40], "sine"); k("R", T.tapi - 0.03, [1.2, 1.5, 6.23, 1.2, 1.46, 0.3, 40], "sine");
  // C — after the iris
  cut("C", T.tapi - 0.02, [0.3, 2.35, 11.2, 0.05, 1.78, 0, 40]); k("C", T.cek - 0.1, [0.1, 2.3, 10.8, 0.0, 1.78, 0, 40], "sine"); k("C", T.posting + 0.3, [0.0, 2.25, 10.5, 0.0, 1.78, 0, 40], "sine");
  k("C", T.komen + 0.6, [0.0, 3.2, 9.6, 0.0, 1.2, 0, 40], "io"); k("C", 58, [0.0, 3.1, 9.2, 0.0, 1.2, 0, 40], "sine");
  C.sort((a, b) => a[0] - b[0]);
}
window.VX = { C, WP, T };
scene.add(cam);

/* ---------------------------------------------------------------- render */
let ready = false; const LIFTAT = (t) => 230 * U(t, 6.95, 7.6);
const ANIM = { H: animH, N: animN, S: animS, R: animR, X: animX, C: animC };
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  hemi.intensity = 0.75;
  const inMap = t >= MAP[0] && t < MAP[1];
  for (const kk in worlds) { const [a, b] = VIS[kk]; let v = t >= a && t < b; if (["N", "S", "R"].includes(kk) && inMap) v = true; if (kk === "H" && t > 6.6 && t < 10.3) v = inMap; worlds[kk].visible = v; if (v) ANIM[kk](t); }
  animMap(t);
  let v = keys(t, C); if (window.VX.camOverride) v = window.VX.camOverride.slice();
  const DL = window.VX.DOLLY;
  if (t > DL[0] && t < DL[1]) {   // dolly zoom on the phone: subject size constant, background stretches, then settles
    const u = EZ.io((t - DL[0]) / (DL[1] - DL[0])), A = at("R")([0.3, 2.0, 10.3, 0.3, 1.3, 0, 40]), B = at("R")([1.2, 1.5, 6.5, 1.2, 1.46, 0.3, 40]);
    v = A.map((x, i) => x + (B[i] - x) * u); const d0 = 10.3, d1 = 6.2, d = d0 + (d1 - d0) * u, t20 = Math.tan((20 * Math.PI) / 180);
    const S0 = 1 / (d0 * t20), S1 = 1 / (d1 * t20), Sz = S0 + (S1 - S0) * Math.pow(u, 2.6); v[6] = (2 * Math.atan(1 / (d * Sz)) * 180) / Math.PI;
  }
  const hx = Math.sin(t * 0.9) * 0.025, hy = Math.sin(t * 1.3 + 1) * 0.02;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.up.set(0, 1, 0); cam.lookAt(v[3], v[4], v[5]);
  // fog opens up for the wide map shot
  const far = inMap || (t > 5.3 && t < 11.2) ? 200 : 140; scene.fog.near = far > 150 ? 90 : 40; scene.fog.far = far;
  if (!LOGO.ig) { LOGO.ig = logo3d("instagram", window.LOGOS.instagram.hex, 1); cam.add(LOGO.ig); }
  { const on = U(t, T.komen - 0.05, T.komen + 0.35, "back"), d = 3.0; LOGO.ig.visible = t > T.komen - 0.05; cam.updateMatrixWorld();
    const v2 = new THREE.Vector3((540 / W) * 2 - 1, 1 - (420 / H) * 2, 0.5).unproject(cam).sub(cam.position).normalize().multiplyScalar(d).add(cam.position); cam.worldToLocal(v2);
    LOGO.ig.position.copy(v2); LOGO.ig.position.y += 0.03 * Math.sin(t * 3); LOGO.ig.rotation.set(0, Math.sin(t * 1.4) * 0.5 + (1 - on) * 5, 0); LOGO.ig.scale.setScalar(Math.max(0.001, on) * 0.2 * (1 + 0.12 * Math.max(0, Math.sin((t - T.kirim2) * 12)) * (t > T.kirim2 && t < T.kirim2 + 0.25 ? 1 : 0))); }
  stars.position.copy(cam.position);
  const tx = v[3], tz = v[5]; moon.position.set(tx - 6, 12, tz + 8); moon.target.position.set(tx, 0, tz - 1); warm.position.set(tx + 6, 4, tz + 7); warm.target.position.set(tx, 1, tz);
  renderer.render(scene, cam);
}
window.VX.render = render;
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(async () => {
  // claude mark as an image for the chat avatar (Simple Icons path, CC0)
  LOGO_IMG = await new Promise((res) => { const im = new Image(); im.onload = () => res(im); im.onerror = () => res(null);
    im.src = "data:image/svg+xml;utf8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="${window.LOGOS.claude.hex}" d="${window.LOGOS.claude.path}"/></svg>`); });
  makeTextures(); buildH(); buildX(); buildN(); buildS(); buildR(); buildC(); buildMap();
  LOGO.r = [logo3d("claude", window.LOGOS.claude.hex, 0.3), logo3d("elevenlabs", "#ffffff", 0.28)]; LOGO.r.forEach((o, i) => { o.position.set(PH[0] - 0.74, 1.95, 0.45); worlds.R.add(o); });
  buildCamera(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = PR;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
