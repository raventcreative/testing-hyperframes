/* R35 · 7 aplikasi AI open-source dari GitHub — navy voxel islands (own assets), one absolute camera path.
   Deterministic: render(t) is a pure function of t ("hf-seek").
   Through-line object: ONE cyan "data dot" (#01ccf7 sphere). It drops from the GitHub mark into the laptop, hops over the four
   business needs, dives into the laptop screen (portal), bounces off the cloud and stays on the laptop (Jan), is the pixel that
   gets enlarged and the GPU's power LED (Upscayl), the REC light on the mic and the subtitle playhead (Buzz), the playhead of the
   separated vocal track (UVR), the centre of the speaker cone we dive into (Chatterbox), the REC light locked in the glass box
   (Meetily), the signal that runs through the node cables (ComfyUI) and finally the DM dot on the CTA.
   Transitions (all different): zoom-out reveal (hook) · portal dive into the laptop screen + flash (L->J) · whip pan (J->U) ·
   iris on the dot (U->Z) · whip tilt down (Z->V) · turntable spin blur (V->C) · dive into the speaker cone (C->M) ·
   island-hop flight (M->Y) · dolly zoom + shockwave ring (Y->CTA). */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { SVGLoader } from "three/addons/loaders/SVGLoader.js";
import { MAT, rnd, setSeed, boxes, emi, ctex, rr, cl, EZ, U, keys, glow, label, setLabel, FONT, person } from "./vxlib.js";

const cv = document.getElementById("vx");
const W = cv.width, H = cv.height;
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, alpha: true, premultipliedAlpha: true, preserveDrawingBuffer: true });
renderer.setClearColor(0x000000, 0);   // client rule: the only background is the brand navy plate (img under the canvas)
renderer.setPixelRatio(1); renderer.setSize(W, H, false);
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.22;
scene.background = null;
scene.fog = new THREE.Fog(0x13284f, 45, 110);
scene.add(new THREE.HemisphereLight(0x9fbaff, 0x0a1230, 0.8));
const moon = new THREE.DirectionalLight(0xc6dbff, 2.1); moon.castShadow = true; moon.shadow.mapSize.set(2048, 2048); moon.shadow.bias = -0.0004; moon.shadow.normalBias = 0.025;
Object.assign(moon.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10, near: 1, far: 45 }); scene.add(moon, moon.target);
const warm = new THREE.DirectionalLight(0xbfe9ff, 0.6); scene.add(warm, warm.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 160);

/* ---------------------------------------------------------------- shared */
const RIM = emi("#36e0ff", 1.3);
const CY = "#01ccf7";
function island(nx, nz, a = "#1d3266", b = "#172a58") {
  const g = new THREE.Group(), L = [];
  for (let i = -nx; i <= nx; i++) for (let j = -nz; j <= nz; j++) L.push([i, -0.05, j, 1, 0.1, 1, (i + j) & 1 ? a : b]);
  const top = boxes(L, MAT, false); top.castShadow = false; g.add(top);
  const Wd = 2 * nx + 1, D = 2 * nz + 1;
  g.add(boxes([[0, -0.55, 0, Wd, 0.9, D, "#0f2147"], [0, -1.15, 0, Wd - 0.8, 0.3, D - 0.8, "#0b1a3a"], [0, -1.5, 0, Wd - 2.2, 0.4, D - 2.2, "#08142e"],
    [0, -1.95, 0, Math.max(1, Wd * 0.35), 0.5, Math.max(1, D * 0.35), "#060f24"]], MAT, false));
  for (const [x, z, w, d] of [[0, D / 2, Wd + 0.06, 0.05], [0, -D / 2, Wd + 0.06, 0.05], [Wd / 2, 0, 0.05, D + 0.06], [-Wd / 2, 0, 0.05, D + 0.06]]) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, 0.05, d), RIM); m.position.set(x, -0.1, z); g.add(m); }
  return g;
}
const WP = { L: [0, 0, 0], J: [60, 0, 0], U: [120, 0, 0], Z: [180, 0, 0], V: [240, 0, 0], C: [300, 0, 0], M: [360, 0, 0], Y: [372, 3, -16] };
const VIS = { L: [[-1, 13.06], [80.15, 99]], J: [[13.04, 21.73]], U: [[21.72, 32.36]], Z: [[32.35, 41.16]], V: [[41.15, 50.46]], C: [[50.45, 60.91]], M: [[60.9, 69.35]], Y: [[68.7, 80.16]] };
const worlds = {}; const mk = (k) => { const g = new THREE.Group(); g.position.set(...WP[k]); worlds[k] = g; scene.add(g); return g; };
/* 3D brand logo: Simple Icons CC0 path -> SVGLoader -> ExtrudeGeometry with a small bevel (only GitHub is in Simple Icons) */
function logo3d(name, color, size, depth = 3.2) {
  const Lg = window.LOGOS[name]; const data = new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="${Lg.path}"/></svg>`);
  const shapes = data.paths.flatMap((p) => SVGLoader.createShapes(p));
  const g = new THREE.ExtrudeGeometry(shapes, { depth, bevelEnabled: true, bevelThickness: 0.5, bevelSize: 0.32, bevelSegments: 2, curveSegments: 10 });
  g.translate(-12, -12, -depth / 2); g.rotateX(Math.PI); g.scale(size / 24, size / 24, size / 24);
  const c = new THREE.Color(color); const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.3, roughness: 0.35, metalness: 0.1 }));
  m.castShadow = true; const w = new THREE.Group(); w.add(m); w.visible = false; return w;
}
const popIn = (o, t, a, b, s0 = 1) => { const u = U(t, a, a + 0.35, "back") * (1 - U(t, b, b + 0.22, "in")); o.visible = t > a && t < b + 0.22 && u > 0.001; o.scale.setScalar(Math.max(0.001, u * s0)); return u; };
const popLabel = (l, t, a, b) => setLabel(l, EZ.back(cl((t - a) / 0.35, 0, 1)) * (1 - U(t, b, b + 0.2)));
function live(w, h, draw) { const tex = ctex(w, h, () => {}); const c = tex.image, g = c.getContext("2d"); let last = null;
  return { tex, redraw(t) { const k = Math.round(t * 30); if (k === last) return; last = k; g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, w, h); draw(g, w, h, t); tex.needsUpdate = true; } }; }
const plane = (w, h, map, o = {}) => new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial(Object.assign({ map, toneMapped: false, transparent: true }, o)));
const bez = (a, b, c, u) => a * (1 - u) * (1 - u) + 2 * b * u * (1 - u) + c * u * u;
const typed = (s, t, a, cps = 40) => s.slice(0, Math.max(0, Math.min(s.length, Math.floor((t - a) * cps))));
const hop = (t, a, b, h) => Math.sin(Math.PI * cl((t - a) / (b - a), 0, 1)) * h;
function monitor(g, x, y, z, ry, sw, sh, map) { // voxel monitor: bezel + stand + screen plane
  const m = new THREE.Group(); m.position.set(x, y, z); m.rotation.y = ry; g.add(m);
  m.add(boxes([[0, 0, -0.08, sw + 0.22, sh + 0.22, 0.14, "#1b2a55"], [0, -sh / 2 - 0.4, -0.2, 0.18, 0.8, 0.14, "#24345f"], [0, -y + 0.05, -0.2, 1.0, 0.1, 0.6, "#24345f"]]));
  const s = plane(sw, sh, map, { transparent: false }); m.add(s);
  const rim = new THREE.Mesh(new THREE.BoxGeometry(sw + 0.26, 0.04, 0.02), RIM); rim.position.set(0, -sh / 2 - 0.12, 0); m.add(rim);
  return m;
}
function laptop(g, map, sw = 3.9) { // voxel laptop: base + hinged screen (rotation.x on .lid)
  const sh = sw * 0.62, o = new THREE.Group(); g.add(o);
  o.add(boxes([[0, 0.1, 0, sw + 0.3, 0.2, sh * 0.9, "#c3cfe2"], [0, 0.205, -0.05, sw - 0.2, 0.012, sh * 0.5, "#8fa0bf"], [0, 0.205, sh * 0.3, sw * 0.28, 0.012, sh * 0.16, "#aebcd6"]]));
  const lid = new THREE.Group(); lid.position.set(0, 0.2, -sh * 0.45); o.add(lid);
  lid.add(boxes([[0, sh / 2 + 0.12, -0.05, sw + 0.3, sh + 0.24, 0.1, "#c3cfe2"]]));
  const s = plane(sw, sh, map, { transparent: false }); s.position.set(0, sh / 2 + 0.12, 0.002); lid.add(s);
  o.userData = { lid, screen: s, sw, sh }; return o;
}
function gpuCard() { // voxel graphics card with two spinning fans
  const g = new THREE.Group();
  g.add(boxes([[0, 0.32, 0, 1.9, 0.64, 0.22, "#1b2238"], [0, 0.0, 0, 1.6, 0.08, 0.06, "#2a3350"], [-0.2, -0.05, 0, 1.1, 0.06, 0.04, "#d8b98e"], [1.0, 0.32, 0, 0.08, 0.7, 0.26, "#8a9bb8"]]));
  g.userData.fans = [-0.45, 0.45].map((x) => { const f = new THREE.Group(); f.position.set(x, 0.32, 0.12); g.add(f);
    f.add(boxes([[0, 0, 0, 0.5, 0.06, 0.02, "#3a4560"], [0, 0, 0, 0.06, 0.5, 0.02, "#3a4560"], [0, 0, 0.01, 0.14, 0.14, 0.02, "#5b6b8c"]], MAT, false));
    const r = new THREE.Mesh(new THREE.TorusGeometry(0.27, 0.025, 6, 24), emi(CY, 0.8)); f.add(r); return f; });
  return g;
}
function wifi(col = "#c3cfe2") { const L = []; [0.32, 0.56, 0.8].forEach((r) => { for (let a = 50; a <= 130; a += 13) { const q = (a * Math.PI) / 180; L.push([Math.cos(q) * r, Math.sin(q) * r, 0, 0.1, 0.1, 0.1, col]); } });
  L.push([0, 0.06, 0, 0.14, 0.14, 0.14, col]); const g = new THREE.Group(); g.add(boxes(L, MAT, false)); return g; }
function cloud(col = "#c3cfe2") { const g = new THREE.Group(); g.add(boxes([[0, 0, 0, 1.4, 0.5, 0.6, col], [-0.3, 0.3, 0, 0.6, 0.5, 0.55, col], [0.25, 0.38, 0, 0.7, 0.6, 0.55, col]], MAT, false)); return g; }
function waveBars(n, w, col) { const g = new THREE.Group(); const bars = [];
  for (let i = 0; i < n; i++) { const m = boxes([[0, 0.5, 0, (w / n) * 0.62, 1, 0.12, col]], MAT, false); m.position.x = -w / 2 + (i + 0.5) * (w / n); g.add(m); bars.push(m); }
  g.userData.bars = bars; return g; }
const setBars = (g, t, amp, seed = 0, on = 1) => g.userData.bars.forEach((m, i) => { const v = 0.12 + on * amp * (0.5 + 0.5 * Math.sin(t * 9 + i * 1.7 + seed) * Math.sin(t * 5.3 + i * 0.9 + seed * 2)); m.scale.y = Math.max(0.05, v); });

/* ---------------------------------------------------------------- the 7 tools: own voxel icons (none is in Simple Icons) */
const TOOLS = ["Jan", "Upscayl", "Buzz", "Ultimate Vocal Remover", "Chatterbox", "Meetily", "ComfyUI"];
const REPOS = ["janhq/jan", "upscayl/upscayl", "chidiwilliams/buzz", "Anjok07/ultimatevocalremovergui", "resemble-ai/chatterbox", "Zackriya-Solutions/meetily", "Comfy-Org/ComfyUI"];
function icon(i) {
  const a = new THREE.Group(); const W_ = "#ffffff", N = "#0c1a48";
  if (i === 0) a.add(boxes([[0, 0.05, 0, 0.62, 0.42, 0.14, W_], [-0.18, -0.2, 0, 0.14, 0.12, 0.14, W_], [-0.15, 0.05, 0.075, 0.08, 0.08, 0.01, CY], [0, 0.05, 0.075, 0.08, 0.08, 0.01, CY], [0.15, 0.05, 0.075, 0.08, 0.08, 0.01, CY]]));
  if (i === 1) a.add(boxes([[0, 0, 0, 0.62, 0.48, 0.08, W_], [0, 0, 0.045, 0.5, 0.36, 0.01, "#2a4f8f"], [-0.1, -0.08, 0.05, 0.2, 0.14, 0.01, "#7fe8ff"], [0.14, 0.1, 0.06, 0.1, 0.1, 0.01, CY], [0.24, 0.32, 0.03, 0.08, 0.2, 0.08, CY], [0.24, 0.42, 0.03, 0.2, 0.06, 0.08, CY]]));
  if (i === 2) a.add(boxes([[0, 0.12, 0, 0.22, 0.34, 0.22, "#c3cfe2"], [0, 0.12, 0.112, 0.16, 0.26, 0.01, "#5b6b8c"], [0, -0.14, 0, 0.06, 0.18, 0.06, "#8a9bb8"], [0, -0.24, 0, 0.3, 0.05, 0.16, "#8a9bb8"], [0.0, 0.33, 0.0, 0.08, 0.08, 0.08, CY]]));
  if (i === 3) { const L = []; for (let k = 0; k < 6; k++) { const h1 = 0.1 + 0.18 * Math.abs(Math.sin(k * 1.3 + 0.4)), h2 = 0.1 + 0.18 * Math.abs(Math.sin(k * 0.9 + 1.4));
    L.push([-0.3 + k * 0.12, 0.17, 0, 0.07, h1, 0.08, CY], [-0.3 + k * 0.12, -0.17, 0, 0.07, h2, 0.08, W_]); } a.add(boxes(L)); }
  if (i === 4) a.add(boxes([[0, 0, 0, 0.46, 0.6, 0.3, "#1b2238"], [0, 0.1, 0.155, 0.3, 0.3, 0.01, "#3a4560"], [0, 0.1, 0.16, 0.1, 0.1, 0.01, CY], [0, -0.18, 0.155, 0.14, 0.14, 0.01, "#3a4560"]]));
  if (i === 5) a.add(boxes([[0, -0.05, 0, 0.66, 0.08, 0.36, "#d8b98e"], [-0.22, 0.14, -0.2, 0.14, 0.24, 0.1, W_], [0.22, 0.14, -0.2, 0.14, 0.24, 0.1, W_], [0, 0.14, -0.2, 0.14, 0.24, 0.1, CY], [-0.22, 0.31, -0.2, 0.12, 0.12, 0.1, "#f1c39d"], [0.22, 0.31, -0.2, 0.12, 0.12, 0.1, "#f1c39d"], [0, 0.31, -0.2, 0.12, 0.12, 0.1, "#f1c39d"]]));
  if (i === 6) a.add(boxes([[-0.24, 0.16, 0, 0.26, 0.2, 0.1, W_], [0.24, -0.16, 0, 0.26, 0.2, 0.1, W_], [0.24, 0.2, 0, 0.26, 0.2, 0.1, CY], [-0.06, 0.16, 0, 0.12, 0.04, 0.04, CY], [0.06, 0.0, 0, 0.04, 0.32, 0.04, CY], [0.06, -0.16, 0, 0.1, 0.04, 0.04, CY]]));
  if (i === 7) a.add(boxes([[0, 0, 0, 0.66, 0.44, 0.08, W_], [-0.2, -0.04, 0.05, 0.16, 0.2, 0.01, CY], [0.0, 0.08, 0.05, 0.12, 0.08, 0.01, "#2a4f8f"], [0.18, -0.02, 0.05, 0.14, 0.24, 0.01, "#2a4f8f"]])); // generic "konten" (play card)
  return a;
}

/* ---------------------------------------------------------------- data dot (through-line) */
const DOT = new THREE.Mesh(new THREE.IcosahedronGeometry(0.15, 2), emi(CY, 2.2)); DOT.castShadow = true; scene.add(DOT);
const DOTG = glow("#3fdcff", 1.2, 1.2); scene.add(DOTG);
function dotAt(w, x, y, z, s = 1) { DOT.visible = DOTG.visible = s > 0.01; DOT.position.set(x + WP[w][0], y + WP[w][1], z + WP[w][2]); DOT.scale.setScalar(Math.max(0.001, s));
  DOTG.position.copy(DOT.position); DOTG.scale.set(1.2 * s, 1.2 * s, 1); }

/* ---------------------------------------------------------------- scripted windows (html-demo: View(t) redrawn from t alone) */
function header(c, w, txt, sub) { c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 76); [0, 1, 2].forEach((i) => { c.fillStyle = i ? "rgba(255,255,255,.35)" : CY; c.beginPath(); c.arc(38 + i * 34, 38, 10, 0, 7); c.fill(); });
  c.fillStyle = "#cfe6ff"; c.font = `700 34px ${FONT}`; c.textAlign = "left"; c.fillText(txt, 150, 50);
  if (sub) { c.font = `700 26px ${FONT}`; const tw = c.measureText(sub).width + 36; c.fillStyle = CY; rr(c, w - tw - 24, 18, tw, 42, 21); c.fill(); c.fillStyle = "#0a0d2c"; c.fillText(sub, w - tw - 6, 48); } }
function bubble(c, x, y, w, h, me) { c.fillStyle = me ? CY : "#1d3266"; rr(c, x, y, w, h, 26); c.fill(); }
function chatView(c, w, h, t, t0) { // Jan-like local chat (illustration, labelled SIMULASI)
  c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); header(c, w, "chat lokal · offline", "SIMULASI");
  const q = "Bikin 3 ide caption buat produk baru", a = ["1. Pagi lebih segar, mulai dari sini", "2. Kecil di tas, besar manfaatnya", "3. Coba seminggu, rasakan bedanya"];
  const s = typed(q, t, t0, 46); c.font = `700 34px ${FONT}`; const qw = Math.min(w - 120, c.measureText(q).width + 56);
  if (s.length) { bubble(c, w - qw - 40, 110, qw, 74, true); c.fillStyle = "#0a0d2c"; c.fillText(s, w - qw - 12, 158); }
  const t1 = t0 + q.length / 46 + 0.35;
  if (t > t1) { bubble(c, 40, 214, w - 200, 318, false); c.fillStyle = "#ffffff"; c.font = `700 33px ${FONT}`;
    let left = Math.floor((t - t1) * 34); a.forEach((ln, i) => { if (left <= 0) return; c.fillText(ln.slice(0, left), 76, 284 + i * 86); left -= ln.length; });
    if (left <= 0 && Math.floor(t * 3) % 2 === 0) { c.fillStyle = CY; c.fillRect(76, 470, 18, 36); } }
  c.fillStyle = "#13245a"; rr(c, 40, h - 92, w - 80, 66, 33); c.fill(); c.fillStyle = "#7f95c8"; c.font = `400 30px ${FONT}`; c.fillText("Tulis pesan…", 76, h - 48);
}

/* ---------------------------------------------------------------- L: hub — the laptop (hook + 4 needs + CTA) */
const Lh = {};
const NEEDS = [["CHAT", 0, 9.9], ["FOTO PRODUK", 1, 10.42], ["KONTEN", 7, 11.34], ["MEETING", 5, 12.3]];
const NX = [-2.55, -0.85, 0.85, 2.55], NZ = 2.3;
function hubView(c, w, h, t) {
  c.fillStyle = "#081233"; c.fillRect(0, 0, w, h);
  if (t > 12.45 && t < 80) { chatView(c, w, h, t, 12.5); return; }
  if (t >= 82.8) { c.strokeStyle = "rgba(1,204,247,.16)"; c.lineWidth = 3; for (let x = 0; x <= w; x += 64) { c.beginPath(); c.moveTo(x, 0); c.lineTo(x, h); c.stroke(); } return; }
  if (t >= 80) { // CTA: the 7 repos tick in
    header(c, w, "github.com · 7 repo", null); c.textAlign = "left";
    REPOS.forEach((r, i) => { const u = cl((t - 80.4 - i * 0.14) / 0.25, 0, 1); if (u <= 0) return; c.globalAlpha = u; const y = 132 + i * 70;
      c.fillStyle = CY; rr(c, 36, y - 38, 52, 52, 12); c.fill(); c.fillStyle = "#0a0d2c"; c.font = `700 40px ${FONT}`; c.fillText("✓", 46, y + 2);
      c.fillStyle = "#ffffff"; c.font = `700 44px ${FONT}`; c.fillText(r, 108, y + 4); c.globalAlpha = 1; });
    return; }
  header(c, w, "github.com", "OPEN-SOURCE");
  c.fillStyle = "#ffffff"; c.font = `700 52px ${FONT}`; c.textAlign = "left"; c.fillText(typed("7 aplikasi AI · gratis", t, 0.25, 30), 44, 150);
  TOOLS.forEach((n, i) => { const a = 0.9 + i * 0.16, u = EZ.back(cl((t - a) / 0.3, 0, 1)); if (u <= 0) return;
    const col = i % 4, row = Math.floor(i / 4), x = 44 + col * 238 + (row ? 119 : 0), y = 196 + row * 196, ww = 218, hh = 176;
    c.save(); c.translate(x + ww / 2, y + hh / 2); c.scale(u, u); c.translate(-ww / 2, -hh / 2);
    c.fillStyle = "#14275a"; rr(c, 0, 0, ww, hh, 22); c.fill(); c.strokeStyle = CY; c.lineWidth = 4; rr(c, 2, 2, ww - 4, hh - 4, 22); c.stroke();
    c.fillStyle = CY; c.font = `700 64px ${FONT}`; c.textAlign = "center"; c.fillText(String(i + 1), ww / 2, 78);
    c.fillStyle = "#ffffff"; c.font = `700 ${n.length > 12 ? 24 : 30}px ${FONT}`; c.fillText(n.length > 12 ? "Ultimate Vocal" : n, ww / 2, 126); if (n.length > 12) c.fillText("Remover", ww / 2, 156);
    c.restore(); });
  c.textAlign = "left";
  if (t > 6.0) { const u = cl((t - 6.0) / 0.25, 0, 1); c.globalAlpha = u; c.fillStyle = CY; rr(c, 700, 108, 280, 60, 30); c.fill(); c.fillStyle = "#0a0d2c"; c.font = `700 32px ${FONT}`; c.fillText("Rp0 / bulan", 728, 150); c.globalAlpha = 1; }
}
function buildL() {
  const g = mk("L"); g.add(island(5, 4));
  Lh.scr = live(1024, 640, hubView);
  Lh.lap = laptop(g, Lh.scr.tex, 3.9); Lh.lap.position.set(0, 0, -0.6);
  Lh.gh = logo3d("github", "#ffffff", 1.2); g.add(Lh.gh);
  // subscription cards that fall off the island ("nggak perlu langganan bulanan")
  const sub = ctex(420, 260, (c, w, h) => { c.fillStyle = "#e9eef7"; rr(c, 4, 4, w - 8, h - 8, 26); c.fill(); c.fillStyle = "#0c1a48"; c.font = `700 52px ${FONT}`; c.textAlign = "center"; c.fillText("LANGGANAN", w / 2, 110);
    c.fillStyle = "#294b77"; c.font = `700 60px ${FONT}`; c.fillText("/ bulan", w / 2, 196); });
  Lh.subs = [0, 1, 2].map((i) => { const m = plane(1.3, 0.8, sub, { side: THREE.DoubleSide }); m.visible = false; g.add(m); return m; });
  // 4 business needs: icon + pill on a plinth
  Lh.needs = NEEDS.map(([txt, ic], i) => { const o = new THREE.Group(); o.position.set(NX[i], 0, NZ); g.add(o);
    o.add(boxes([[0, 0.15, 0, 1.2, 0.3, 0.9, "#14275a"], [0, 0.31, 0, 1.24, 0.04, 0.94, "#1d3a7a"]]));
    const ico = icon(ic); ico.position.y = 0.85; ico.scale.setScalar(1.25); o.add(ico); const l = label(txt, "", "#fff", 0.32); l.position.set(0, i % 2 ? 1.95 : 1.45, 0.1); o.add(l);
    o.userData = { ico, l }; o.visible = false; return o; });
  Lh.orb = [0, 1, 2, 3, 4, 5, 6].map((i) => { const o = icon(i === 0 ? 0 : i === 1 ? 1 : i === 2 ? 2 : i === 3 ? 3 : i === 4 ? 4 : i === 5 ? 5 : 6); o.visible = false; g.add(o); return o; });
  Lh.ghC = logo3d("github", "#ffffff", 1.3); g.add(Lh.ghC);
}
const LAPS = [0, 0.3, -0.6]; // laptop world position (screen centre ~ y 1.6)
function animL(t) {
  Lh.scr.redraw(t);
  const cta = t > 80;
  Lh.lap.userData.lid.rotation.x = -0.12;
  popIn(Lh.gh, t, 1.62, 5.0, 1); Lh.gh.position.set(0, 3.55 + 0.06 * Math.sin(t * 2.4), -0.6); Lh.gh.rotation.y = (1 - U(t, 1.62, 2.2, "out")) * 5 + Math.sin(t * 1.5) * 0.4;
  if (cta) Lh.gh.visible = false;
  // subscription cards: appear on "Nggak perlu", get knocked off by the dot on "bulanan" and fall
  Lh.subs.forEach((m, i) => { const a = 6.0 + i * 0.1, k = Math.max(0, t - 6.95 - i * 0.07); m.visible = !cta && t > a && t < 8.3;
    const u = U(t, a, a + 0.3, "back"); m.scale.setScalar(Math.max(0.001, u));
    m.position.set(3.55 + i * 0.2 + 1.2 * k, 2.75 - i * 0.66 - 4.9 * k * k, -0.3 + i * 0.12 + 1.5 * k); m.rotation.set(-0.1 + k * 3 * (i + 1), -0.35 + k * 2, k * 2); });
  // needs pop on their words
  Lh.needs.forEach((o, i) => { const a = NEEDS[i][2] - 0.08, u = cta ? 0 : U(t, a, a + 0.35, "back") * (1 - U(t, 12.55, 12.8, "in")); o.visible = u > 0.01; o.scale.setScalar(Math.max(0.001, u));
    o.userData.ico.rotation.y = Math.sin(t * 1.6 + i) * 0.5; o.userData.ico.position.y = 0.85 + 0.05 * Math.sin(t * 2.6 + i); });
  // CTA: seven tool icons orbit the GitHub mark above the laptop
  Lh.ghC.visible = cta && t > 80.3; Lh.ghC.position.set(0, 3.75, -0.6); Lh.ghC.scale.setScalar(Math.max(0.001, U(t, 80.3, 80.7, "back"))); Lh.ghC.rotation.y = t * 1.2;
  Lh.orb.forEach((o, i) => { o.visible = cta && t > 80.4; const u = U(t, 80.4 + i * 0.12, 80.8 + i * 0.12, "back"), a = t * 0.8 + (i * Math.PI * 2) / 7;
    o.position.set(Math.cos(a) * 2.3, 3.6 + 0.15 * Math.sin(a * 2), -0.6 + Math.sin(a) * 1.0); o.scale.setScalar(Math.max(0.001, u * 1.0)); o.rotation.y = -a + Math.PI / 2; });
  // data dot: drops out of the GitHub mark into the laptop, knocks the cards, hops the four needs, dives into the screen
  if (!cta && t < 13.06) {
    if (t < 3.3) DOT.visible = DOTG.visible = false;
    else if (t < 4.8) { const u = U(t, 3.3, 4.8, "io"); dotAt("L", bez(0, 0.9, 1.4, u), bez(3.1, 3.6, 1.9, u), bez(-0.4, 0.4, 0.2, u), U(t, 3.3, 3.5)); }
    else if (t < 6.85) { const k = t - 4.8; dotAt("L", 1.4 + 0.25 * Math.sin(k * 1.5), 1.9 + 0.12 * Math.abs(Math.sin(k * 4)), 0.2); }
    else if (t < 7.15) { const u = U(t, 6.85, 7.15, "in"); dotAt("L", 1.4 + 2.1 * u, 1.9 + 0.5 * u, 0.2 - 0.4 * u); }
    else if (t < 9.75) { const u = U(t, 7.15, 9.75, "io"); dotAt("L", bez(3.5, 0, NX[0], u), bez(2.4, 3.2, 1.85, u), bez(-0.2, 1.6, NZ, u)); }
    else if (t < 12.55) { let x = NX[0], y = 1.85; for (let i = 1; i < 4; i++) { const a = NEEDS[i][2] - 0.25, b = NEEDS[i][2] + 0.05; if (t > a) { const u = U(t, a, b, "io"); x = NX[i - 1] + (NX[i] - NX[i - 1]) * u; y = 1.85 + hop(t, a, b, 0.7); } }
      dotAt("L", x, y + 0.04 * Math.sin(t * 6), NZ); }
    else { const u = U(t, 12.55, 13.0, "in"); dotAt("L", bez(NX[3], 1.6, 0, u), bez(1.85, 2.6, 1.6, u), bez(NZ, 1.2, -0.1, u), 1 - 0.6 * u); }
  }
  if (cta) { DOT.visible = DOTG.visible = false; }
}

/* ---------------------------------------------------------------- J: Jan — local chat, download the model, offline, data stays */
const J = {};
const JMON = [-0.4, 1.95, -1.2];
function buildJ() {
  const g = mk("J"); g.add(island(5, 4));
  J.scr = live(1024, 640, (c, w, h, t) => chatView(c, w, h, t, 12.5));
  J.mon = monitor(g, JMON[0], JMON[1], JMON[2], 0.1, 3.4, 2.12, J.scr.tex);
  J.model = new THREE.Group(); g.add(J.model);
  J.model.add(boxes([[0, 0, 0, 0.8, 0.8, 0.8, "#3f7fd6"]]));
  { const lt = ctex(256, 256, (c, w, h) => { c.fillStyle = "#1b2a55"; c.fillRect(0, 0, w, h); c.fillStyle = "#ffffff"; c.font = `700 62px ${FONT}`; c.textAlign = "center"; c.fillText("MODEL", w / 2, 116); c.fillStyle = CY; c.font = `700 50px ${FONT}`; c.fillText("AI", w / 2, 186); });
    const p = plane(0.7, 0.7, lt, { transparent: false }); p.position.z = 0.405; J.model.add(p); }
  J.arrow = boxes([[0, 0.2, 0, 0.16, 0.5, 0.16, CY], [0, -0.1, 0, 0.5, 0.12, 0.16, CY], [0, -0.2, 0, 0.3, 0.12, 0.16, CY], [0, -0.28, 0, 0.12, 0.08, 0.16, CY]]); g.add(J.arrow);
  J.wifi = wifi(); J.wifi.position.set(1.55, 2.25, -0.2); g.add(J.wifi);
  J.slash = new THREE.Mesh(new THREE.BoxGeometry(1.25, 0.12, 0.12), emi(CY, 1.6)); J.slash.position.set(1.55, 2.6, -0.1); J.slash.rotation.z = -0.75; g.add(J.slash);
  J.cloud = cloud("#8a9bb8"); J.cloud.position.set(2.7, 3.55, -1.3); g.add(J.cloud);
  J.dome = new THREE.Group(); J.dome.position.set(JMON[0], 0, JMON[2] + 0.3); g.add(J.dome);
  J.dome.add(new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(2.55, 1)), new THREE.LineBasicMaterial({ color: 0x01ccf7, transparent: true, opacity: 0.55 })));
  J.dome.add(new THREE.Mesh(new THREE.IcosahedronGeometry(2.53, 1), new THREE.MeshBasicMaterial({ color: 0x01ccf7, transparent: true, opacity: 0.08, depthWrite: false })));
  J.lab = label("tetap di laptop", "", "#fff", 0.32); J.lab.position.set(JMON[0], 3.45, JMON[2] + 1.0); g.add(J.lab);
}
function animJ(t) {
  J.scr.redraw(t);
  // model block downloads into the monitor on "model AI-nya kamu unduh"
  const mu = U(t, 16.3, 16.7, "back"), md = U(t, 17.35, 17.95, "in"); J.model.visible = t > 16.3 && t < 17.95;
  J.model.scale.setScalar(Math.max(0.001, mu * (1 - 0.7 * md))); J.model.position.set(JMON[0] + 2.55 - 2.55 * md, 2.6 - 0.6 * md, JMON[2] + 0.5); J.model.rotation.y = Math.sin(t * 2) * 0.3 * (1 - md);
  J.arrow.visible = t > 16.9 && t < 17.95; J.arrow.position.set(JMON[0] + 2.55 - 2.55 * md, 1.85 - 0.3 * md + 0.08 * Math.sin(t * 10), JMON[2] + 0.5); J.arrow.scale.setScalar(Math.max(0.001, U(t, 16.9, 17.1, "back") * (1 - md)));
  // offline: the wi-fi icon is struck through on "tanpa koneksi"
  const wu = U(t, 18.0, 18.35, "back"); J.wifi.visible = t > 18.0 && t < 21.0; J.wifi.scale.setScalar(Math.max(0.001, wu * (1 - U(t, 19.6, 19.9))));
  const su = U(t, 18.85, 19.1, "out"); J.slash.visible = t > 18.85 && t < 19.9; J.slash.scale.set(Math.max(0.001, su * (1 - U(t, 19.6, 19.9))), 1, 1);
  // data stays: dome closes over the monitor, the dot bounces off it towards the cloud and comes back
  const du = U(t, 19.75, 20.25, "back"); J.dome.visible = t > 19.75; J.dome.scale.set(Math.max(0.001, du), Math.max(0.001, du), Math.max(0.001, du)); J.dome.rotation.y = t * 0.15;
  J.cloud.visible = t > 19.75; J.cloud.scale.setScalar(Math.max(0.001, U(t, 19.75, 20.1, "back"))); J.cloud.position.y = 3.55 + 0.05 * Math.sin(t * 2);
  popLabel(J.lab, t, 20.6, 21.5);
  if (t < 21.73) {
    const sx = JMON[0], sy = JMON[1], sz = JMON[2] + 0.2;
    if (t < 13.6) { const u = U(t, 13.05, 13.6, "out"); dotAt("J", sx, sy, sz + 0.5 * u, 0.4 + 0.6 * u); }
    else if (t < 20.3) dotAt("J", sx + 1.95 + 0.04 * Math.sin(t * 3), sy - 1.25 + 0.06 * Math.abs(Math.sin(t * 3.4)), sz + 0.25);
    else if (t < 21.2) { const k = t - 20.3, out = Math.min(k, 0.4) / 0.4, back = Math.max(0, k - 0.4) / 0.5; const r = 2.3 * Math.sin(Math.PI * Math.min(1, k / 0.8));
      dotAt("J", sx + 1.95 + (0.0 + 0.55 * r * 0.4) , sy - 1.25 + r, sz + 0.25); }
    else { const u = U(t, 21.2, 21.73, "in"); dotAt("J", sx + 1.95 + 4 * u, sy - 1.25 + 0.3 * u, sz + 0.25); }
  }
}

/* ---------------------------------------------------------------- U: Upscayl — small photo -> big & sharp, 3 OSes, Vulkan GPU */
const Up = {};
function productArt(c, w, h, k) { // illustrative product (CONTOH, no brand) at full detail
  const g2 = c.createLinearGradient(0, 0, 0, h); g2.addColorStop(0, "#dbe7f7"); g2.addColorStop(1, "#9fb6d8"); c.fillStyle = g2; c.fillRect(0, 0, w, h);
  c.fillStyle = "rgba(10,13,44,.18)"; c.beginPath(); c.ellipse(w / 2, h * 0.86, w * 0.3, h * 0.04, 0, 0, 7); c.fill();
  const bg = c.createLinearGradient(w * 0.3, 0, w * 0.7, 0); bg.addColorStop(0, "#ffffff"); bg.addColorStop(0.5, "#eef3fb"); bg.addColorStop(1, "#c9d6ea"); c.fillStyle = bg; rr(c, w * 0.32, h * 0.28, w * 0.36, h * 0.58, w * 0.08); c.fill();
  c.fillStyle = "#294b77"; rr(c, w * 0.39, h * 0.16, w * 0.22, h * 0.14, w * 0.03); c.fill(); c.fillStyle = CY; c.fillRect(w * 0.32, h * 0.5, w * 0.36, h * 0.12);
  c.fillStyle = "#0a0d2c"; c.font = `700 ${Math.round(w * 0.07)}px ${FONT}`; c.textAlign = "center"; c.fillText("CONTOH", w / 2, h * 0.585);
  c.fillStyle = "rgba(255,255,255,.7)"; c.fillRect(w * 0.37, h * 0.32, w * 0.04, h * 0.42);
}
function buildU() {
  const g = mk("U"); g.add(island(5, 4));
  const big = document.createElement("canvas"); big.width = 400; big.height = 500; productArt(big.getContext("2d"), 400, 500);
  const small = document.createElement("canvas"); small.width = 20; small.height = 25; small.getContext("2d").drawImage(big, 0, 0, 20, 25);
  Up.lo = ctex(400, 500, (c) => { c.imageSmoothingEnabled = false; c.drawImage(small, 0, 0, 400, 500); });
  Up.hi = ctex(400, 500, (c) => { c.drawImage(big, 0, 0); });
  Up.lo.magFilter = THREE.NearestFilter;
  Up.sm = new THREE.Group(); Up.sm.position.set(-2.6, 1.0, 0.4); g.add(Up.sm);
  Up.sm.add(boxes([[0, 0, -0.05, 0.86, 1.06, 0.08, "#ffffff"]])); Up.smP = plane(0.76, 0.95, Up.lo, { transparent: false }); Up.smP.position.z = 0.0; Up.sm.add(Up.smP);
  g.add(boxes([[-2.6, 0.25, 0.2, 0.08, 0.5, 0.08, "#8a9bb8"], [-2.6, 0.03, 0.3, 0.6, 0.06, 0.5, "#5b6b8c"]]));
  Up.bg = new THREE.Group(); Up.bg.position.set(0.4, 1.95, -0.9); g.add(Up.bg);
  Up.bg.add(boxes([[0, 0, -0.08, 2.5, 3.08, 0.12, "#ffffff"]]));
  Up.bgLo = plane(2.3, 2.88, Up.lo, { transparent: false }); Up.bg.add(Up.bgLo);
  Up.bgHi = new THREE.Mesh(new THREE.PlaneGeometry(2.3, 2.88), new THREE.MeshBasicMaterial({ map: Up.hi, toneMapped: false })); Up.bgHi.position.z = 0.004; Up.bg.add(Up.bgHi);
  Up.beam = new THREE.Mesh(new THREE.BoxGeometry(2.5, 0.06, 0.06), emi(CY, 2.4)); Up.beam.position.z = 0.06; Up.bg.add(Up.beam);
  // three OS plinths (text only: no Windows mark in Simple Icons)
  Up.os = ["Windows", "Mac", "Linux"].map((n, i) => { const o = new THREE.Group(); o.position.set(-2.2 + i * 2.2, 0, 2.6); g.add(o);
    o.add(boxes([[0, 0.12, 0, 1.6, 0.24, 0.9, "#14275a"], [0, 0.25, 0, 1.64, 0.03, 0.94, "#1d3a7a"]]));
    const l = label(n, "", "#fff", 0.42); l.position.set(0, 0.66, 0.1); o.add(l); o.userData.l = l; o.visible = false; return o; });
  Up.gpu = gpuCard(); Up.gpu.position.set(2.85, 0.35, 0.6); Up.gpu.rotation.y = -0.5; g.add(Up.gpu);
  Up.gl = label("GPU + Vulkan", "", "#fff", 0.32); Up.gl.position.set(2.85, 1.55, 0.8); g.add(Up.gl);
}
function animU(t) {
  // small blurry photo on the easel; on "diperbesar" a big frame grows out of it (shared element), on "dipertajam" a beam sharpens it
  const gone = 1 - U(t, 27.5, 27.85, "in");
  Up.sm.visible = t > 22.0 && gone > 0.001; Up.sm.scale.setScalar(Math.max(0.001, U(t, 22.0, 22.35, "back") * gone)); Up.sm.rotation.y = 0.25 + Math.sin(t * 1.4) * 0.06;
  const gu = U(t, 24.9, 25.55, "io"); Up.bg.visible = t > 24.9 && gone > 0.001;
  Up.bg.position.set(-2.6 + 3.0 * gu, 1.0 + 0.8 * gu, 0.4 - 1.3 * gu); Up.bg.scale.setScalar(Math.max(0.001, (0.36 + 0.49 * gu) * gone));
  const sh = cl((t - 25.8) / 0.8, 0, 1); Up.beam.visible = t > 25.75 && t < 26.7; Up.beam.position.y = 1.44 - 2.88 * sh;
  Up.bgHi.visible = t > 25.8; { const y0 = 1.44 - 2.88 * sh; Up.bgHi.scale.y = Math.max(0.001, sh); Up.bgHi.position.y = (1.44 + y0) / 2; Up.bgHi.material.map.repeat.set(1, Math.max(0.001, sh)); Up.bgHi.material.map.offset.set(0, 1 - Math.max(0.001, sh)); }
  // OSes pop on their words, the GPU rises on "kartu grafis"
  [27.85, 28.57, 29.05].forEach((a, i) => { const o = Up.os[i], u = U(t, a, a + 0.35, "back") * (1 - U(t, 30.1, 30.35, "in")); o.visible = t > a && u > 0.001; o.scale.setScalar(Math.max(0.001, u)); });
  const gp = U(t, 30.3, 30.75, "back"); Up.gpu.visible = t > 30.3; Up.gpu.scale.setScalar(Math.max(0.001, gp)); Up.gpu.position.y = 0.35 + 0.08 * Math.sin(t * 2);
  Up.gpu.userData.fans.forEach((f, i) => (f.rotation.z = t * (8 + i)));
  popLabel(Up.gl, t, 31.45, 32.3);
  // data dot = the pixel: flies in from the whip, sits on the small photo, rides the big frame, sharpening beam, then the GPU LED
  if (t < 32.36) {
    if (t < 22.4) { const u = U(t, 21.73, 22.4, "out"); dotAt("U", -6 + 3.4 * u, 1.4 + 0.2 * Math.sin(u * 3), 0.6); }
    else if (t < 24.9) dotAt("U", -2.6 + 0.3, 1.0 + 0.62 + 0.05 * Math.abs(Math.sin(t * 3)), 0.5);
    else if (t < 25.8) { const u = U(t, 24.9, 25.55, "io"); dotAt("U", -2.3 + 3.75 * u, 1.62 + 1.4 * u, 0.5 - 1.2 * u); }
    else if (t < 26.7) dotAt("U", 1.45, 3.02 - 2.45 * sh, -0.7);
    else if (t < 30.8) { const k = t - 26.7; dotAt("U", 1.7 + 0.04 * Math.sin(k * 3), 0.55 + 0.06 * Math.abs(Math.sin(k * 3.2)), -0.6); }
    else { const u = U(t, 30.8, 31.4, "io"); const tx = 2.85 + 0.75 * Math.cos(-0.5), tz = 0.6 - 0.75 * Math.sin(-0.5) + 0.15; dotAt("U", bez(1.7, 2.3, tx - 0.15, u), bez(0.55, 1.6, 1.0, u) + (t > 31.4 ? 0.08 * Math.sin(t * 2) : 0), bez(-0.6, 0.6, tz, u), 1 - 0.3 * u); }
  }
}

/* ---------------------------------------------------------------- Z: Buzz — podcast -> text -> subtitle files, offline, Whisper */
const Z = {};
const TRANS = ["Halo, selamat datang di podcast", "kita. Hari ini kita bahas", "cara jualan online…"];
function buildZ() {
  const g = mk("Z"); g.add(island(5, 4));
  Z.mic = new THREE.Group(); Z.mic.position.set(-2.7, 0, -0.2); g.add(Z.mic);
  Z.mic.add(boxes([[0, 0.03, 0, 0.8, 0.06, 0.8, "#5b6b8c"], [0, 0.8, 0, 0.08, 1.6, 0.08, "#8a9bb8"], [0, 1.95, 0.05, 0.56, 0.9, 0.56, "#c3cfe2"], [0, 2.44, 0.05, 0.44, 0.1, 0.44, "#c3cfe2"], [0, 1.47, 0.05, 0.44, 0.1, 0.44, "#c3cfe2"], [0, 1.55, 0.0, 0.36, 0.12, 0.36, "#8a9bb8"]].concat([0, 1, 2, 3, 4, 5].map((i) => [0, 1.62 + i * 0.13, 0.335, 0.5, 0.05, 0.02, "#3a4560"])).concat([[0, 1.95, 0.335, 0.6, 0.12, 0.04, CY]])));
  Z.wave = waveBars(14, 2.6, CY); Z.wave.position.set(-0.55, 1.35, -0.2); g.add(Z.wave);
  Z.doc = live(800, 580, (c, w, h, t) => { c.fillStyle = "#ffffff"; c.fillRect(0, 0, w, h); c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 80); c.fillStyle = "#ffffff"; c.font = `700 42px ${FONT}`; c.fillText("transkrip.txt", 30, 55);
    let left = Math.floor((t - 35.45) * 36); c.fillStyle = "#0a0d2c"; c.font = `700 44px ${FONT}`;
    TRANS.forEach((ln, i) => { if (left <= 0) return; c.fillText(ln.slice(0, left), 30, 140 + i * 56); left -= ln.length; });
    if (t > 36.6) { c.fillStyle = "#e8f6fd"; rr(c, 20, 368, w - 40, 196, 22); c.fill(); c.strokeStyle = CY; c.lineWidth = 5; rr(c, 20, 368, w - 40, 196, 22); c.stroke();
      c.fillStyle = "#294b77"; c.font = `700 34px ui-monospace, Menlo, monospace`; c.fillText("subtitle.srt  1", 44, 420); c.fillText("00:00:01,0 --> 00:00:03,2", 44, 470);
      c.fillStyle = "#0a0d2c"; c.font = `700 40px ${FONT}`; c.fillText("Halo, selamat datang…", 44, 532); } });
  Z.board = new THREE.Group(); Z.board.position.set(1.75, 1.6, -0.7); Z.board.rotation.y = -0.22; g.add(Z.board);
  Z.board.add(boxes([[0, 0, -0.06, 2.7, 2.0, 0.1, "#1b2a55"], [0, -1.2, -0.1, 0.12, 0.5, 0.12, "#24345f"]])); Z.board.add(plane(2.6, 1.885, Z.doc.tex, { transparent: false }));
  const fileTex = (ext) => ctex(256, 300, (c, w, h) => { c.fillStyle = "#ffffff"; rr(c, 4, 4, w - 8, h - 8, 26); c.fill(); c.fillStyle = CY; rr(c, 4, h - 110, w - 8, 106, 26); c.fill(); c.fillRect(4, h - 110, w - 8, 40);
    c.fillStyle = "#0c1a48"; c.font = `700 80px ${FONT}`; c.textAlign = "center"; c.fillText(ext, w / 2, h - 32); c.fillStyle = "#b9c6dc"; for (let i = 0; i < 3; i++) c.fillRect(40, 50 + i * 40, w - 80, 16); });
  Z.files = ["TXT", "SRT", "VTT"].map((e, i) => { const m = plane(0.62, 0.73, fileTex(e), { side: THREE.DoubleSide }); m.position.set(-1.1 + i * 0.85, 0.55, 1.9); m.visible = false; g.add(m); return m; });
  // internet cable that gets unplugged
  Z.globe = new THREE.Group(); Z.globe.position.set(3.4, 0.7, 2.4); g.add(Z.globe);
  Z.globe.add(new THREE.Mesh(new THREE.IcosahedronGeometry(0.42, 1), new THREE.MeshStandardMaterial({ color: 0x8a9bb8, flatShading: true, roughness: 0.6 })));
  Z.cA = boxes([[0, 0, 0, 1.0, 0.07, 0.07, "#8a9bb8"]]); Z.cB = boxes([[0, 0, 0, 1.0, 0.07, 0.07, "#8a9bb8"]]); g.add(Z.cA, Z.cB);
  Z.plug = boxes([[0, 0, 0, 0.18, 0.16, 0.16, "#c3cfe2"]]); g.add(Z.plug);
  Z.wl = label("Whisper · OpenAI", "", "#fff", 0.36); Z.wl.position.set(-2.7, 3.05, 0.1); g.add(Z.wl);
  Z.ol = label("OFFLINE", "", "#fff", 0.42); Z.ol.position.set(2.6, 1.45, 2.4); g.add(Z.ol);
}
function animZ(t) {
  Z.doc.redraw(t);
  setBars(Z.wave, t, 1.3, 1, U(t, 33.6, 34.0) * (1 - 0.6 * U(t, 41.0, 41.2)));
  { const wv = U(t, 33.5, 33.8, "back") * (1 - U(t, 35.15, 35.4, "in")) + U(t, 39.3, 39.6, "back"); Z.wave.visible = wv > 0.01; Z.wave.scale.setScalar(Math.max(0.001, Math.min(1, wv))); }
  Z.files.forEach((m, i) => { const a = 36.7 + i * 0.12, u = U(t, a, a + 0.35, "back") * (1 - U(t, 39.15, 39.4, "in")); m.visible = t > a && u > 0.001; m.scale.setScalar(Math.max(0.001, u)); m.rotation.y = Math.sin(t * 1.5 + i) * 0.25; m.position.y = 0.55 + 0.05 * Math.sin(t * 2.4 + i); });
  // cable: plugged until "tanpa koneksi internet", then pulled apart
  const pu = U(t, 37.6, 38.1, "back"); const ax = 1.85, bx = 2.95;
  Z.cA.position.set(ax + 0.0 - 0.35 * pu, 0.55, 2.4); Z.cB.position.set(bx + 0.35 * pu, 0.55, 2.4); Z.cA.scale.x = 0.9; Z.cB.scale.x = 0.9; Z.plug.position.set(2.4 - 0.25 * pu, 0.55, 2.4);
  Z.board.position.y = 1.6 - 4.0 * U(t, 37.05, 37.4, "in"); Z.board.visible = t < 37.4;
  Z.globe.rotation.y = t * 0.6; Z.globe.children[0].material.emissive = new THREE.Color(0x000000);
  popLabel(Z.ol, t, 38.15, 41.0); popLabel(Z.wl, t, 39.4, 41.0);
  // dot: REC light on the mic while recording, then the playhead along the subtitle card, then falls (tilt down)
  if (t < 41.16) {
    if (t < 35.3) { const u = U(t, 32.36, 32.9, "out"); dotAt("Z", -2.7, 2.6 + 1.2 * (1 - u), 0.35, 0.3 + 0.7 * u); }
    else if (t < 35.8) { const u = U(t, 35.3, 35.8, "io"); dotAt("Z", bez(-2.7, -0.4, 0.5, u), bez(2.6, 3.4, 2.75, u), bez(0.35, 0.3, -0.45, u)); }
    else if (t < 37.0) { const k = cl((t - 35.8) / 1.1, 0, 1); dotAt("Z", 0.5 + 2.3 * k, 2.75 - 0.5 * U(t, 36.6, 36.9), -0.45 - 0.5 * k, 0.8); }
    else if (t < 37.5) { const u = U(t, 37.0, 37.5, "io"); dotAt("Z", bez(2.5, 2.6, 2.4, u), bez(1.3, 2.2, 0.8, u), bez(-0.75, 1.0, 2.4, u)); }
    else if (t < 39.2) { const pu = U(t, 37.6, 38.1, "back"); dotAt("Z", 2.4 - 0.25 * pu, 0.8 + 0.5 * hop(t, 37.6, 38.2, 1), 2.4); }
    else if (t < 39.7) { const u = U(t, 39.2, 39.7, "io"); dotAt("Z", bez(2.15, 0, -2.7, u), bez(0.8, 3.2, 2.6, u), bez(2.4, 1.5, 0.35, u)); }
    else if (t < 40.6) dotAt("Z", -2.7, 2.6 + 0.05 * Math.abs(Math.sin(t * 3)), 0.35);
    else { const u = U(t, 40.6, 41.16, "in"); dotAt("Z", -2.7, 2.6 - 3.0 * u, 0.35); }
  }
}

/* ---------------------------------------------------------------- V: Ultimate Vocal Remover — one song in, two files out */
const V = {};
function buildV() {
  const g = mk("V"); g.add(island(5, 4));
  V.tt = new THREE.Group(); V.tt.position.set(-3.0, 0, 0.4); g.add(V.tt);
  V.tt.add(boxes([[0, 0.25, 0, 1.6, 0.5, 1.5, "#24345f"], [0.6, 0.55, -0.45, 0.08, 0.1, 0.5, "#8a9bb8"]]));
  V.disc = new THREE.Group(); V.disc.position.y = 0.53; V.tt.add(V.disc);
  V.disc.add(new THREE.Mesh(new THREE.CylinderGeometry(0.66, 0.66, 0.04, 40), new THREE.MeshStandardMaterial({ color: 0x111522, roughness: 0.35 })));
  const lbl = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 0.05, 24), emi(CY, 0.6)); V.disc.add(lbl);
  for (let i = 0; i < 3; i++) { const r = new THREE.Mesh(new THREE.TorusGeometry(0.32 + i * 0.1, 0.006, 4, 40), new THREE.MeshBasicMaterial({ color: 0x3a4560 })); r.rotation.x = Math.PI / 2; r.position.y = 0.022; V.disc.add(r); }
  V.song = new THREE.Group(); g.add(V.song); V.song.add(boxes([[0, 0, 0, 0.9, 0.5, 0.12, "#ffffff"]]));
  { const st = ctex(360, 200, (c, w, h) => { c.fillStyle = "#ffffff"; c.fillRect(0, 0, w, h); c.fillStyle = "#0c1a48"; c.font = `700 56px ${FONT}`; c.textAlign = "center"; c.fillText("lagu.mp3", w / 2, 80);
    for (let i = 0; i < 14; i++) { const hh = 20 + 60 * Math.abs(Math.sin(i * 1.3)); c.fillStyle = i % 2 ? CY : "#294b77"; c.fillRect(30 + i * 22, 150 - hh / 2, 14, hh); } });
    const p = plane(0.86, 0.48, st, { transparent: false }); p.position.z = 0.065; V.song.add(p); }
  // the separator machine
  V.mac = new THREE.Group(); V.mac.position.set(-0.4, 0, -0.6); g.add(V.mac);
  V.mac.add(boxes([[0, 0.9, 0, 1.9, 1.8, 1.5, "#14275a"], [0, 1.95, 0, 1.3, 0.3, 1.1, "#1d3a7a"], [0, 2.2, 0, 0.9, 0.2, 0.8, "#24407a"], [0.96, 0.6, 0.2, 0.1, 0.3, 0.5, "#0b1640"], [0.96, 1.25, 0.2, 0.1, 0.3, 0.5, "#0b1640"]]));
  { const ft = ctex(400, 300, (c, w, h) => { c.fillStyle = "#0c1a48"; c.fillRect(0, 0, w, h); c.strokeStyle = CY; c.lineWidth = 10; c.strokeRect(5, 5, w - 10, h - 10); c.fillStyle = "#ffffff"; c.font = `700 120px ${FONT}`; c.textAlign = "center"; c.fillText("UVR", w / 2, 150);
    c.fillStyle = "#9fdcff"; c.font = `700 40px ${FONT}`; c.fillText("pisah vokal + musik", w / 2, 230); });
    const f = plane(1.6, 1.2, ft, { transparent: false }); f.position.set(0, 0.95, 0.755); V.mac.add(f); }
  V.lights = [0, 1, 2].map((i) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.14, 0.04), emi(CY, 0.3)); m.position.set(-0.4 + i * 0.4, 1.68, 0.76); V.mac.add(m); return m; });
  // two output tracks on two belts
  V.belts = [0, 1].map((i) => { const z = 0.6 + i * 1.7; g.add(boxes([[2.45, 0.14, z, 3.5, 0.12, 0.7, "#24407a"], [2.45, 0.205, z, 3.5, 0.01, 0.06, i ? "#7f95c8" : CY]])); return z; });
  const trk = (name, col) => ctex(420, 220, (c, w, h) => { c.fillStyle = "#0c1a48"; rr(c, 4, 4, w - 8, h - 8, 26); c.fill(); c.strokeStyle = col; c.lineWidth = 8; rr(c, 4, 4, w - 8, h - 8, 26); c.stroke();
    c.fillStyle = "#ffffff"; c.font = `700 58px ${FONT}`; c.textAlign = "center"; c.fillText(name, w / 2, 76);
    for (let i = 0; i < 16; i++) { const hh = 14 + 70 * Math.abs(Math.sin(i * (name === "VOKAL" ? 0.7 : 1.9) + 0.3)); c.fillStyle = col; c.fillRect(40 + i * 22, 160 - hh / 2, 13, hh); } });
  V.trk = [["VOKAL", CY], ["MUSIK", "#7f95c8"]].map(([n, c]) => { const o = new THREE.Group(); o.add(boxes([[0, 0, -0.04, 1.32, 0.72, 0.08, "#0b1640"]])); const p = plane(1.26, 0.66, trk(n, c), { transparent: false }); o.add(p); o.visible = false; g.add(o); return o; });
  // mixer console
  V.mix = new THREE.Group(); V.mix.position.set(-2.7, 0, 2.6); g.add(V.mix);
  V.mix.add(boxes([[0, 0.25, 0, 1.6, 0.5, 1.0, "#1b2238"], [-0.35, 0.51, 0, 0.06, 0.02, 0.7, "#3a4560"], [0.35, 0.51, 0, 0.06, 0.02, 0.7, "#3a4560"]]));
  V.fad = [-0.35, 0.35].map((x, i) => { const m = boxes([[0, 0, 0, 0.26, 0.1, 0.14, i ? "#ffffff" : CY]]); m.position.set(x, 0.56, 0); V.mix.add(m); return m; });
}
function animV(t) {
  V.disc.rotation.y = -t * 3.5;
  // song card: rises off the disc on "satu lagu", into the funnel
  const su = U(t, 43.4, 43.7, "back"), sf = U(t, 43.95, 44.55, "in"); V.song.visible = t > 43.4 && t < 44.55;
  V.song.position.set(bez(-3.0, -1.8, -0.4, sf), bez(1.3, 3.4, 2.3, sf), bez(0.4, 0.3, -0.6, sf)); V.song.scale.setScalar(Math.max(0.001, su * (1 - 0.6 * sf))); V.song.rotation.set(0, 0.3 * (1 - sf), sf * 1.5);
  V.lights.forEach((m, i) => (m.material.emissiveIntensity = 0.3 + 2.4 * U(t, 44.5 + i * 0.12, 44.7 + i * 0.12) * (0.6 + 0.4 * Math.sin(t * 12 + i))));
  V.mac.position.y = t > 44.5 && t < 45.4 ? 0.03 * Math.sin(t * 60) : 0;
  // two files out: VOKAL on "vokal", MUSIK on "musiknya", pulled apart on "terpisah"
  [[45.6, 0], [46.2, 1]].forEach(([a, i]) => { const o = V.trk[i], u = U(t, a, a + 0.55, "out"), sep = U(t, 46.7, 47.1, "back");
    o.visible = t > a; o.position.set(0.7 + 2.1 * u + (i ? 0.25 : -0.25) * 0, 0.6 + (i ? -0.0 : 0.0) + 0.04 * Math.sin(t * 3 + i), V.belts[i] + (i ? 0.25 : -0.25) * sep); o.scale.setScalar(Math.max(0.001, U(t, a, a + 0.3, "back"))); o.rotation.y = -0.2; });
  V.fad.forEach((m, i) => (m.position.z = 0.25 * Math.sin((t - 47.6) * 2.2 + i * 1.6) * U(t, 47.6, 47.9)));
  V.mix.visible = t > 47.55; V.mix.scale.setScalar(Math.max(0.001, U(t, 47.55, 47.9, "back")));
  // dot: lands on the disc label (from the tilt), rides into the machine, comes out as the VOKAL playhead
  if (t < 50.46) {
    if (t < 41.8) { const u = U(t, 41.16, 41.8, "out"); dotAt("V", -3.0, 0.75 + 3.0 * (1 - u), 0.4); }
    else if (t < 43.95) dotAt("V", -3.0 + 0.3 * Math.cos(-t * 3.5), 0.75, 0.4 - 0.3 * Math.sin(-t * 3.5));
    else if (t < 44.55) { const u = U(t, 43.95, 44.55, "in"); dotAt("V", bez(-3.0, -1.8, -0.4, u), bez(1.6, 3.6, 2.4, u), bez(0.4, 0.3, -0.6, u)); }
    else if (t < 45.6) DOT.visible = DOTG.visible = false;
    else { const o = V.trk[0]; const k = cl((t - 46.0) / 3.2, 0, 1); dotAt("V", o.position.x - 0.55 + 1.1 * k, o.position.y + 0.42, o.position.z + 0.05, 0.7 * U(t, 45.9, 46.1)); }
  }
}

/* ---------------------------------------------------------------- C: Chatterbox — script -> voice; honest notes (no ID, archived) */
const Cb = {};
const LANGS = ["AR", "DA", "DE", "EL", "EN", "ES", "FI", "FR", "HE", "HI", "IT", "JA", "KO", "MS", "NL", "NO", "PL", "PT", "RU", "SV", "SW", "TR", "ZH"];
function buildC() {
  const g = mk("C"); g.add(island(5, 4));
  Cb.paper = live(512, 400, (c, w, h, t) => { c.fillStyle = "#ffffff"; c.fillRect(0, 0, w, h); c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 74); c.fillStyle = "#ffffff"; c.font = `700 40px ${FONT}`; c.fillText("naskah.txt", 26, 52);
    c.fillStyle = "#0a0d2c"; c.font = `700 48px ${FONT}`; const s = typed("Halo! Ini contoh voice over buat konten.", t, 51.95, 30);
    const words = s.split(" "); let line = "", y = 140; for (const wd of words) { if (c.measureText(line + wd).width > w - 60) { c.fillText(line, 26, y); y += 58; line = ""; } line += wd + " "; } c.fillText(line, 26, y); });
  Cb.kb = new THREE.Group(); Cb.kb.position.set(-2.6, 0, 1.2); g.add(Cb.kb);
  Cb.kb.add(boxes([[0, 0.12, 0, 1.7, 0.24, 0.8, "#c3cfe2"], [0, 0.25, 0.05, 1.5, 0.02, 0.6, "#8fa0bf"]]));
  Cb.sheet = plane(1.25, 0.98, Cb.paper.tex, { transparent: false, side: THREE.DoubleSide }); Cb.sheet.position.set(-2.6, 0.95, 0.75); Cb.sheet.rotation.x = -0.15; g.add(Cb.sheet);
  Cb.spk = new THREE.Group(); Cb.spk.position.set(2.05, 0, -0.2); g.add(Cb.spk);
  Cb.spk.add(boxes([[0, 1.1, 0, 1.5, 2.2, 1.1, "#1b2238"]]));
  Cb.cone = new THREE.Group(); Cb.cone.position.set(0, 1.35, 0.56); Cb.spk.add(Cb.cone);
  { const cn = new THREE.Mesh(new THREE.CylinderGeometry(0.58, 0.2, 0.3, 32, 1, true), new THREE.MeshStandardMaterial({ color: 0x3a4560, roughness: 0.7, side: THREE.DoubleSide })); cn.rotation.x = Math.PI / 2; cn.position.z = -0.1; Cb.cone.add(cn);
    const rim = new THREE.Mesh(new THREE.TorusGeometry(0.6, 0.05, 8, 32), new THREE.MeshStandardMaterial({ color: 0x5b6b8c })); rim.position.z = 0.04; Cb.cone.add(rim); }
  { const tw = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.1, 20), new THREE.MeshStandardMaterial({ color: 0x3a4560 })); tw.rotation.x = Math.PI / 2; tw.position.set(0, 0.45, 0.58); Cb.spk.add(tw); }
  Cb.rings = [0, 1, 2].map(() => { const r = new THREE.Mesh(new THREE.TorusGeometry(0.7, 0.04, 6, 40), new THREE.MeshBasicMaterial({ color: 0x01ccf7, transparent: true, opacity: 0, depthWrite: false })); r.position.set(2.05, 1.35, 0.5); g.add(r); return r; });
  // honest-notes board: the README's language list (23 codes) — ID is not in it; then the "ARSIP" stamp (retired, Aug 2026)
  Cb.lb = live(1024, 720, (c, w, h, t) => { c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); header(c, w, "README · daftar bahasa", null);
    LANGS.forEach((L, i) => { const u = cl((t - 55.7 - i * 0.04) / 0.2, 0, 1); if (u <= 0) return; const col = i % 6, row = Math.floor(i / 6), x = 36 + col * 162, y = 100 + row * 104;
      c.globalAlpha = u; c.fillStyle = "#14275a"; rr(c, x, y, 146, 86, 18); c.fill(); c.fillStyle = "#ffffff"; c.font = `700 50px ${FONT}`; c.textAlign = "center"; c.fillText(L, x + 73, y + 60); c.globalAlpha = 1; });
    c.textAlign = "left";
    if (t > 56.6) { const x = 36 + 5 * 162, y = 100 + 3 * 104, k = cl((t - 56.6) / 0.25, 0, 1); c.globalAlpha = k; c.setLineDash([12, 10]); c.strokeStyle = CY; c.lineWidth = 5; rr(c, x, y, 146, 86, 18); c.stroke(); c.setLineDash([]);
      c.fillStyle = CY; c.font = `700 46px ${FONT}`; c.textAlign = "center"; c.fillText("ID ?", x + 73, y + 60); c.textAlign = "left";
      c.fillStyle = "#9fdcff"; c.font = `700 50px ${FONT}`; c.fillText("Bahasa Indonesia: belum ada", 36, 584); c.globalAlpha = 1; }
    if (t > 59.4) { const k = EZ.back(cl((t - 59.4) / 0.3, 0, 1)); c.save(); c.translate(690, 300); c.rotate(-0.16); c.scale(2.2 - 1.2 * k, 2.2 - 1.2 * k); c.globalAlpha = cl(k, 0, 1);
      c.strokeStyle = "#ffffff"; c.lineWidth = 10; rr(c, -250, -66, 500, 132, 22); c.stroke(); c.fillStyle = "rgba(8,18,51,.92)"; rr(c, -244, -60, 488, 120, 18); c.fill(); c.fillStyle = "#ffffff"; c.font = `700 74px ${FONT}`; c.textAlign = "center"; c.fillText("DIARSIPKAN", 0, 26); c.restore();
      c.globalAlpha = 1; c.fillStyle = "#ffffff"; c.font = `700 40px ${FONT}`; c.textAlign = "left"; c.fillText("README: retired, tidak di-update (Agt 2026)", 36, 670); } });
  Cb.board = new THREE.Group(); Cb.board.position.set(-1.0, 2.2, -2.2); g.add(Cb.board);
  Cb.board.add(boxes([[0, 0, -0.08, 3.9, 2.78, 0.14, "#1b2a55"], [-1.5, -1.8, -0.1, 0.14, 1.0, 0.14, "#24345f"], [1.5, -1.8, -0.1, 0.14, 1.0, 0.14, "#24345f"]]));
  Cb.board.add(plane(3.76, 2.64, Cb.lb.tex, { transparent: false }));
}
function animC(t) {
  Cb.paper.redraw(t); Cb.lb.redraw(t);
  const talk = U(t, 52.8, 53.0) * (1 - U(t, 54.4, 54.7));
  Cb.cone.position.z = 0.56 + 0.05 * talk * Math.max(0, Math.sin(t * 40));
  Cb.rings.forEach((r, i) => { const ph = ((t - 52.86) * 1.4 + i / 3) % 1; const on = t > 52.86 && t < 54.8 ? 1 : 0; r.scale.setScalar(0.8 + ph * 1.6); r.material.opacity = on * 0.8 * (1 - ph); r.visible = on > 0; });
  { const u = U(t, 51.6, 51.95, "back"), f = U(t, 52.75, 53.25, "in"); Cb.sheet.visible = t > 51.6 && t < 53.25; Cb.sheet.scale.setScalar(Math.max(0.001, u * (1 - 0.9 * f)));
    Cb.sheet.position.set(bez(-2.6, 0, 2.05, f), bez(0.95, 2.4, 1.35, f), bez(0.75, 1.2, 0.5, f)); Cb.sheet.rotation.set(-0.15 * (1 - f), 0, f * 2); }
  const bu = U(t, 54.5, 55.1, "out"), bx = 1 - U(t, 60.15, 60.3, "in"); Cb.board.visible = t > 54.5 && t < 60.3; Cb.board.position.y = 2.2 - 4.4 * (1 - bu); Cb.board.scale.setScalar(Math.max(0.001, bx));
  // dot: lands on the keyboard, flies to the speaker cone centre (the dive target)
  if (t < 60.91) {
    if (t < 51.2) { const u = U(t, 50.46, 51.2, "out"); dotAt("C", -2.6 + 4 * (1 - u), 0.42 + 2.5 * (1 - u) * (1 - u), 1.2); }
    else if (t < 52.6) dotAt("C", -2.6 + 0.5 * Math.sin((t - 51.2) * 6) * U(t, 52.0, 52.2), 0.42 + 0.08 * Math.abs(Math.sin(t * 9)), 1.25);
    else if (t < 53.0) { const u = U(t, 52.6, 53.0, "io"); dotAt("C", bez(-2.6, -0.5, 2.05, u), bez(0.42, 2.6, 1.35, u), bez(1.25, 1.2, 0.72, u)); }
    else dotAt("C", 2.05, 1.35, 0.72 + 0.05 * talk * Math.max(0, Math.sin(t * 40)));
  }
}

/* ---------------------------------------------------------------- M: Meetily — record, transcript, summary; stays on the laptop */
const Mt = {};
function meetView(c, w, h, t) {
  c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); header(c, w, "meeting · lokal", "SIMULASI");
  const rec = t > 63.3; c.fillStyle = rec ? CY : "#3a4e86"; c.beginPath(); c.arc(70, 130, 22, 0, 7); c.fill();
  c.fillStyle = "#ffffff"; c.font = `700 40px ${FONT}`; c.textAlign = "left"; const s = Math.max(0, Math.floor((t - 63.3) * 1)); c.fillText(rec ? `REC 00:${String(12 + s).padStart(2, "0")}` : "Siap merekam", 108, 144);
  const LN = ["A: Target minggu ini apa?", "B: Konten 5 video.", "C: Aku pegang editing."];
  if (t > 63.95) { let left = Math.floor((t - 63.95) * 40); c.font = `700 34px ${FONT}`; c.fillStyle = "#cfe6ff"; LN.forEach((ln, i) => { if (left <= 0) return; c.fillText(ln.slice(0, left), 44, 220 + i * 52); left -= ln.length; }); }
  if (t > 64.75) { const k = EZ.back(cl((t - 64.75) / 0.35, 0, 1)); c.save(); c.translate(w / 2, 470); c.scale(k, k); c.translate(-w / 2, -470);
    c.fillStyle = CY; rr(c, 40, 380, w - 80, 220, 24); c.fill(); c.fillStyle = "#0a0d2c"; c.font = `700 40px ${FONT}`; c.fillText("Ringkasan otomatis", 70, 432);
    c.font = `700 32px ${FONT}`; ["• 5 video minggu ini", "• Editing: C"].forEach((s2, i) => c.fillText(s2, 70, 486 + i * 48)); c.restore(); }
}
function buildM() {
  const g = mk("M"); g.add(island(5, 4));
  g.add(boxes([[0.2, 0.62, 0.4, 3.6, 0.1, 1.5, "#d8b98e"], [-1.4, 0.3, -0.2, 0.12, 0.6, 0.12, "#b48a5e"], [1.8, 0.3, -0.2, 0.12, 0.6, 0.12, "#b48a5e"], [-1.4, 0.3, 1.0, 0.12, 0.6, 0.12, "#b48a5e"], [1.8, 0.3, 1.0, 0.12, 0.6, 0.12, "#b48a5e"]]));
  const base = { skin: "#f1c39d", hair: "#3b2a20", pants: "#26314d", fringe: [[-0.36, 0.18], [-0.18, 0.14], [0, 0.2], [0.18, 0.12], [0.36, 0.18]] };
  Mt.ppl = [["#3567b5", "#2c5598", -1.35, -0.75, 0.15], ["#e9eef7", "#c3cfe2", -0.35, -0.75, 0], ["#294b77", "#1d3a7a", 0.65, -0.75, -0.15]].map(([top, top2, x, z, ry], i) => {
    const p = person(Object.assign({}, base, { top, top2, glasses: i === 1, bun: i === 2, hair: i === 2 ? "#2a1e18" : "#3b2a20" })); p.root.scale.setScalar(0.62); p.root.position.set(x, 0, z); p.root.rotation.y = ry; p.setMouth("smile"); g.add(p.root); return p; });
  Mt.scr = live(1024, 640, meetView);
  Mt.lap = laptop(g, Mt.scr.tex, 1.6); Mt.lap.position.set(1.0, 0.67, 0.85); Mt.lap.rotation.y = -0.3; Mt.lap.userData.lid.rotation.x = -0.2;
  Mt.bub = [0, 1, 2].map((i) => { const sp = label("…", "", "#fff", 0.28); sp.position.set([-1.35, -0.35, 0.65][i], 1.95, -0.75); g.add(sp); return sp; });
  // glass box + padlock: audio and transcript stay on the laptop
  Mt.box = new THREE.Group(); Mt.box.position.set(1.05, 1.25, 0.6); Mt.box.rotation.y = -0.3; g.add(Mt.box);
  Mt.box.add(new THREE.Mesh(new THREE.BoxGeometry(2.1, 1.3, 1.5), new THREE.MeshBasicMaterial({ color: 0x01ccf7, transparent: true, opacity: 0.1, depthWrite: false })));
  Mt.box.add(new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(2.1, 1.3, 1.5)), new THREE.LineBasicMaterial({ color: 0x01ccf7 })));
  Mt.lock = new THREE.Group(); Mt.lock.position.set(1.05, 2.25, 0.6); g.add(Mt.lock);
  Mt.lock.add(boxes([[0, 0, 0, 0.5, 0.4, 0.2, "#ffffff"], [-0.17, 0.3, 0, 0.07, 0.22, 0.08, "#c3cfe2"], [0.17, 0.3, 0, 0.07, 0.22, 0.08, "#c3cfe2"], [0, 0.42, 0, 0.41, 0.07, 0.08, "#c3cfe2"], [0, -0.02, 0.105, 0.08, 0.16, 0.01, "#0c1a48"]]));
  Mt.lab = label("tetap di laptop kamu", "", "#fff", 0.3); Mt.lab.position.set(-0.75, 2.15, 0.6); g.add(Mt.lab);
}
function animM(t) {
  Mt.scr.redraw(t);
  Mt.ppl.forEach((p, i) => { p.head.rotation.x = 0.08 * Math.sin(t * 3 + i * 2) * U(t, 62.3, 62.6); p.head.rotation.y = 0.15 * Math.sin(t * 0.9 + i); p.armR.rotation.x = -0.2 * Math.max(0, Math.sin(t * 2.2 + i * 1.7)); });
  Mt.bub.forEach((b, i) => { const a = 62.5 + i * 0.25; setLabel(b, EZ.back(cl((t - a) / 0.3, 0, 1)) * (1 - U(t, 63.6, 63.8)) * (0.85 + 0.15 * Math.sin(t * 6 + i))); });
  const bu = U(t, 65.95, 66.45, "back"); Mt.box.visible = t > 65.95; Mt.box.scale.setScalar(Math.max(0.001, bu));
  Mt.lock.visible = t > 66.8; Mt.lock.scale.setScalar(Math.max(0.001, U(t, 66.8, 67.15, "back"))); Mt.lock.position.y = 2.25 + 0.4 * (1 - U(t, 66.8, 67.15, "out"));
  popLabel(Mt.lab, t, 67.3, 68.6);
  // dot: comes out of the dive as the laptop's REC light, bounces inside the glass box
  if (t < 69.35) {
    const lx = 0.5, ly = 2.25, lz = 0.2;
    if (t < 65.95) { const u = U(t, 60.91, 61.6, "out"); dotAt("M", lx, ly + 1.5 * (1 - u), lz + 0.6 * (1 - u), 0.5 - 0.1 * u); }
    else if (t < 68.6) { const k = t - 65.95; dotAt("M", 1.05 + 0.75 * Math.sin(k * 2.3), 1.25 + 0.45 * Math.abs(Math.sin(k * 3.1)), 0.6 + 0.45 * Math.sin(k * 1.7)); }
    else { const u = U(t, 68.6, 69.3, "io"); const P = [WP.Y[0] - WP.M[0] - 2.4, WP.Y[1] + 0.9, WP.Y[2] + 0.2]; dotAt("M", bez(1.05, 6, P[0], u), bez(1.4, 6, P[1], u), bez(0.6, -8, P[2], u)); }
  }
}

/* ---------------------------------------------------------------- Y: ComfyUI — nodes snapped together, output image/video/audio, GPU+RAM */
const Y = {};
const NODES = [["Prompt", [-2.3, 0.95, 0.3]], ["Model", [-0.5, 2.25, -0.5]], ["Sampler", [1.0, 0.95, 0.4]]];
const YWIN = [2.6, 2.3, -1.3];
function buildY() {
  const g = mk("Y"); g.add(island(5, 4));
  const nodeTex = (n) => ctex(400, 260, (c, w, h) => { c.fillStyle = "#14275a"; rr(c, 4, 4, w - 8, h - 8, 22); c.fill(); c.fillStyle = CY; rr(c, 4, 4, w - 8, 66, 22); c.fill(); c.fillRect(4, 40, w - 8, 30);
    c.fillStyle = "#0a0d2c"; c.font = `700 46px ${FONT}`; c.fillText(n, 26, 54); c.fillStyle = "rgba(255,255,255,.22)"; for (let i = 0; i < 3; i++) rr(c, 26, 96 + i * 50, w - 120 - i * 40, 30, 10), c.fill();
    c.fillStyle = "#ffffff"; c.beginPath(); c.arc(w - 26, 150, 14, 0, 7); c.fill(); c.beginPath(); c.arc(26, 150, 14, 0, 7); c.fill(); });
  Y.nodes = NODES.map(([n, p]) => { const o = new THREE.Group(); o.position.set(...p); g.add(o); o.add(boxes([[0, 0, -0.08, 1.9, 1.25, 0.14, "#1b2a55"]])); const f = plane(1.8, 1.17, nodeTex(n), { transparent: false }); o.add(f); o.visible = false; o.userData.p = p; return o; });
  // output window: image -> video -> audio
  Y.out = live(640, 520, (c, w, h, t) => { c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.fillStyle = CY; rr(c, 0, 0, w, 70, 20); c.fill(); c.fillRect(0, 40, w, 30);
    c.fillStyle = "#0a0d2c"; c.font = `700 44px ${FONT}`; c.fillText(t < 71.2 ? "Gambar" : t < 72.1 ? "Video" : "Audio", 26, 52);
    if (t < 71.2) { const gr = c.createLinearGradient(0, 70, 0, h); gr.addColorStop(0, "#2a4f8f"); gr.addColorStop(1, "#0e1d4d"); c.fillStyle = gr; c.fillRect(20, 90, w - 40, h - 110);
      c.fillStyle = "#ffffff"; c.beginPath(); c.arc(470, 190, 50, 0, 7); c.fill(); c.fillStyle = "#3f7fd6"; c.beginPath(); c.moveTo(20, h - 20); c.lineTo(220, 240); c.lineTo(380, h - 20); c.fill(); c.fillStyle = CY; c.beginPath(); c.moveTo(250, h - 20); c.lineTo(430, 300); c.lineTo(w - 20, h - 20); c.fill(); }
    else if (t < 72.1) { c.fillStyle = "#14275a"; c.fillRect(20, 90, w - 40, h - 110); c.fillStyle = "#ffffff"; c.beginPath(); c.moveTo(270, 200); c.lineTo(270, 400); c.lineTo(420, 300); c.fill();
      c.fillStyle = "rgba(255,255,255,.3)"; c.fillRect(40, h - 50, w - 80, 12); c.fillStyle = CY; c.fillRect(40, h - 50, (w - 80) * cl((t - 71.2) / 0.9, 0, 1), 12); }
    else { c.fillStyle = "#14275a"; c.fillRect(20, 90, w - 40, h - 110); for (let i = 0; i < 20; i++) { const hh = 30 + 250 * Math.abs(Math.sin(i * 1.1 + t * 6) * Math.sin(i * 0.4 + 1)); c.fillStyle = i % 2 ? CY : "#ffffff"; c.fillRect(46 + i * 28, 300 - hh / 2, 16, hh); } } });
  Y.win = new THREE.Group(); Y.win.position.set(...YWIN); Y.win.rotation.y = -0.25; g.add(Y.win);
  Y.win.add(boxes([[0, 0, -0.06, 1.98, 1.62, 0.1, "#1b2a55"], [0, -1.35, -0.1, 0.12, 1.0, 0.12, "#24345f"]])); Y.win.add(plane(1.9, 1.54, Y.out.tex, { transparent: false }));
  // cables (tubes drawn progressively)
  const mat = emi(CY, 1.4); const pts = [[NODES[0][1], NODES[1][1]], [NODES[1][1], NODES[2][1]], [NODES[2][1], [YWIN[0] - 0.92 + 0.9, YWIN[1] - 0.2, YWIN[2] + 0.3]]];
  Y.cab = pts.map(([a, b]) => { const A = new THREE.Vector3(a[0] + 0.9, a[1], a[2] + 0.02), B = new THREE.Vector3(b[0] - 0.9, b[1], b[2] + 0.02);
    const cur = new THREE.CubicBezierCurve3(A, new THREE.Vector3(A.x + 0.7, A.y, A.z + 0.3), new THREE.Vector3(B.x - 0.7, B.y, B.z + 0.3), B);
    const geo = new THREE.TubeGeometry(cur, 40, 0.045, 8, false); const m = new THREE.Mesh(geo, mat); m.visible = false; g.add(m); m.userData.cur = cur; return m; });
  Y.gpu = gpuCard(); Y.gpu.position.set(-2.3, 0.3, 2.5); Y.gpu.rotation.y = 0.35; g.add(Y.gpu);
  Y.ram = [0, 1].map((i) => { const m = boxes([[0, 0.3, 0, 1.3, 0.5, 0.06, "#2a3350"], [-0.4, 0.32, 0.04, 0.22, 0.26, 0.02, "#0b1020"], [0, 0.32, 0.04, 0.22, 0.26, 0.02, "#0b1020"], [0.4, 0.32, 0.04, 0.22, 0.26, 0.02, "#0b1020"], [0, 0.07, 0, 1.2, 0.05, 0.07, "#d8b98e"]]);
    m.position.set(0.6 + i * 0.35, 0.05, 2.6 + i * 0.25); m.rotation.y = -0.25; g.add(m); return m; });
  Y.gl = label("GPU", "", "#fff", 0.4); Y.gl.position.set(-2.3, 1.45, 2.6); g.add(Y.gl);
  Y.rl = label("RAM", "", "#fff", 0.4); Y.rl.position.set(0.8, 1.35, 2.8); g.add(Y.rl);
}
function animY(t) {
  Y.out.redraw(t);
  // nodes snap in on "rakit dari blok-blok node", cables draw on "disambung"; the output window is there from "Gambar"
  const NA = [73.1, 73.6, 74.2];
  const gone = 1 - U(t, 75.5, 75.85, "in");
  Y.nodes.forEach((o, i) => { const a = NA[i], u = U(t, a, a + 0.4, "back") * gone, d = U(t, a, a + 0.4, "out"); o.visible = t > a && u > 0.001; o.scale.setScalar(Math.max(0.001, u)); o.position.y = o.userData.p[1] + 1.2 * (1 - d) + 0.04 * Math.sin(t * 2 + i); });
  Y.win.visible = t > 70.3 && gone > 0.001; Y.win.scale.setScalar(Math.max(0.001, U(t, 70.3, 70.7, "back") * gone));
  const CA = [74.3, 74.75, 75.1]; Y.cab.forEach((m, i) => { const u = U(t, CA[i], CA[i] + 0.4, "io"); m.visible = u > 0.01 && gone > 0.01; m.scale.setScalar(Math.max(0.001, gone)); m.geometry.setDrawRange(0, Math.floor(u * 40) * 8 * 6); });
  Y.gpu.visible = t > 76.3; Y.gpu.scale.setScalar(Math.max(0.001, U(t, 76.3, 76.7, "back"))); Y.gpu.userData.fans.forEach((f, i) => (f.rotation.z = t * (9 + i)));
  Y.ram.forEach((m, i) => { const a = 77.0 + i * 0.15; m.visible = t > a; m.scale.setScalar(Math.max(0.001, U(t, a, a + 0.35, "back"))); });
  popLabel(Y.gl, t, 76.55, 80.2); popLabel(Y.rl, t, 77.3, 80.2);
  // dot: lands from the flight on the Prompt node's port, runs along the three cables, then sits on the GPU
  if (t > 68.7 && t < 80.16) {
    const P0 = [NODES[0][1][0] + 0.9, NODES[0][1][1], NODES[0][1][2] + 0.1];
    if (t < 69.3) { /* handled by M during the flight */ }
    else if (t < 72.9) dotAt("Y", YWIN[0] - 1.0 + 0.03 * Math.sin(t * 3), YWIN[1] + 0.95 + 0.05 * Math.abs(Math.sin(t * 3.2)), YWIN[2] + 0.2);
    else if (t < 74.3) { const u = U(t, 72.9, 73.5, "io"); dotAt("Y", bez(YWIN[0] - 1.0, -0.5, P0[0], u), bez(YWIN[1] + 0.95, 3.4, P0[1], u) + (t > 73.5 ? 0.04 * Math.sin(t * 4) : 0), bez(-0.4, 0.4, P0[2], u)); }
    else if (t < 75.5) { const k = cl((t - 74.3) / 1.2, 0, 1) * 3, i = Math.min(2, Math.floor(k)), p = Y.cab[i].userData.cur.getPoint(Math.min(1, k - i)); dotAt("Y", p.x, p.y + 0.06, p.z + 0.05); }
    else if (t < 76.3) { const p = Y.cab[2].userData.cur.getPoint(1); dotAt("Y", p.x, p.y + 0.06 * Math.sin(t * 4), p.z + 0.05); }
    else { const p = Y.cab[2].userData.cur.getPoint(1), u = U(t, 76.3, 76.9, "io"); dotAt("Y", bez(p.x, 0, -2.3, u), bez(p.y, 2.6, 0.95, u) + 0.05 * Math.sin(t * 3), bez(p.z, 2.0, 2.75, u), 1 - 0.3 * u); }
  }
}

/* ---------------------------------------------------------------- camera path (absolute), with cuts.
   FR(): camera from a target + how wide (metres) should span how many pixels. After the mascot rises the target sits at
   screen y≈730 (LIFT view offset), so the 3D action band is y≈500–980. */
const C = []; const at = (w) => (v) => [v[0] + WP[w][0], v[1] + WP[w][1], v[2] + WP[w][2], v[3] + WP[w][0], v[4] + WP[w][1], v[5] + WP[w][2], v[6]];
const TH = Math.tan((40 * Math.PI) / 360) * W / H;
const FR = (T, wm, px, el = 0.2, yaw = 0) => { const d = (wm * 1080) / (px * 2 * TH); return [T[0] + d * Math.sin(yaw) * Math.cos(el), T[1] + d * Math.sin(el), T[2] + d * Math.cos(yaw) * Math.cos(el), T[0], T[1], T[2], 40]; };
const k = (w, t, v, e) => C.push([t, at(w)(v), e]);
const cut = (w, t, v) => C.push([t, at(w)(v), "lin"]);
const SCR = [0, 1.72, -0.75]; // hub laptop screen centre
// L — world first: the laptop screen fills the width (GitHub mark above), zoom-out reveal, the four needs, portal into the screen
k("L", 0, FR(SCR, 4.2, 1000, 0.1)); k("L", 4.9, FR([0, 2.1, -0.7], 4.6, 1000, 0.12), "sine");
k("L", 6.3, FR([0.6, 1.4, 0.6], 8.6, 1060, 0.3), "io"); k("L", 7.9, FR([0.6, 1.4, 0.6], 8.4, 1060, 0.3), "sine");
k("L", 8.9, FR([0, 1.25, 1.6], 8.4, 1080, 0.26), "io"); k("L", 12.3, FR([0, 1.25, 1.6], 8.1, 1080, 0.25), "sine");
k("L", 12.75, FR(SCR, 4.4, 1000, 0.08), "io"); k("L", 13.04, FR(SCR, 0.7, 1000, 0.03), "in");
// J — out of the screen (same chat UI on the monitor), model download, offline, dome + cloud, whip pan right
cut("J", 13.05, FR([JMON[0], JMON[1], JMON[2]], 2.4, 1000, 0.06, 0.1)); k("J", 13.7, FR([JMON[0], 2.0, JMON[2]], 4.0, 1000, 0.1, 0.1), "out");
k("J", 16.2, FR([JMON[0] + 0.9, 2.1, JMON[2]], 5.4, 1040, 0.1, 0.1), "io"); k("J", 17.0, FR([JMON[0] + 1.0, 2.2, JMON[2]], 5.4, 1000, 0.12, 0.05), "io");
k("J", 19.6, FR([JMON[0] + 1.0, 2.2, JMON[2]], 5.4, 1030, 0.12, 0.05), "sine"); k("J", 20.4, FR([0.4, 2.4, -0.6], 7.0, 1000, 0.18), "io"); k("J", 21.35, FR([0.4, 2.4, -0.6], 6.8, 1000, 0.18), "sine");
C.push([21.72, (() => { const v = at("J")(FR([0.4, 2.4, -0.6], 6.8, 1000, 0.18)); v[3] += 14; return v; })(), "expo"]);
// U — whip lands on the small photo; frame grows; three OSes; GPU; iris on the dot
C.push([21.73, (() => { const v = at("U")(FR([-2.4, 1.2, 0.4], 3.2, 1000, 0.12)); v[3] -= 14; return v; })(), "lin"]);
k("U", 22.2, FR([-2.4, 1.2, 0.4], 3.2, 1000, 0.12), "out"); k("U", 24.85, FR([-2.4, 1.2, 0.4], 3.0, 1000, 0.12), "sine");
k("U", 25.6, FR([0.3, 1.8, -0.8], 5.6, 1000, 0.1), "io"); k("U", 27.3, FR([0.3, 1.8, -0.8], 5.4, 1000, 0.1), "sine");
k("U", 28.0, FR([0.0, 0.7, 2.0], 7.2, 1060, 0.35), "io"); k("U", 30.1, FR([0.2, 0.7, 2.0], 7.0, 1060, 0.35), "sine");
k("U", 30.9, FR([2.9, 0.9, 0.9], 4.0, 1000, 0.25, -0.2), "io"); k("U", 31.6, FR([3.2, 1.0, 1.05], 3.6, 1000, 0.25, -0.2), "io"); k("U", 32.36, FR([3.36, 1.0, 1.11], 3.2, 1000, 0.25, -0.2), "sine");
// Z — iris opens on the mic; waveform -> transcript board; files; unplugged cable; whip tilt down
cut("Z", 32.37, FR([-2.4, 2.0, -0.1], 3.4, 1000, 0.1, 0.1)); k("Z", 34.0, FR([-2.2, 1.9, -0.1], 3.8, 1000, 0.1, 0.1), "sine");
k("Z", 35.3, FR([1.55, 1.6, -0.7], 4.4, 1080, 0.08, -0.15), "io"); k("Z", 36.5, FR([1.55, 1.6, -0.7], 4.3, 1080, 0.08, -0.15), "sine");
k("Z", 37.05, FR([1.55, 1.6, -0.7], 4.3, 1080, 0.08, -0.15), "sine"); k("Z", 37.55, FR([1.1, 0.6, 2.0], 5.2, 1040, 0.55), "io"); k("Z", 39.1, FR([1.1, 0.6, 2.0], 5.0, 1040, 0.55), "sine");
k("Z", 39.7, FR([-1.5, 1.9, 0.0], 5.0, 1060, 0.18, 0.15), "io"); k("Z", 40.8, FR([-1.5, 1.9, 0.0], 4.8, 1060, 0.18, 0.15), "sine");
C.push([41.15, (() => { const v = at("Z")(FR([-1.5, 1.9, 0.0], 4.8, 1060, 0.18, 0.15)); v[4] -= 9; return v; })(), "expo"]);
// V — tilt in from above onto the turntable, song into the machine, two tracks, mixer, spin-blur out
C.push([41.16, (() => { const v = at("V")(FR([-1.7, 1.0, 0.0], 5.4, 1000, 0.3)); v[4] += 9; return v; })(), "lin"]);
k("V", 41.6, FR([-1.7, 1.0, 0.0], 5.4, 1000, 0.3), "out"); k("V", 43.4, FR([-1.7, 1.1, 0.0], 5.6, 1000, 0.3), "sine");
k("V", 44.4, FR([-0.9, 1.4, -0.3], 6.0, 1000, 0.2), "io"); k("V", 45.5, FR([3.0, 0.75, 1.4], 3.9, 1000, 0.45, -0.1), "io");
k("V", 47.1, FR([3.0, 0.75, 1.4], 3.7, 1000, 0.45, -0.1), "sine"); k("V", 47.9, FR([0.0, 0.8, 1.6], 7.0, 1040, 0.3), "io"); k("V", 49.7, FR([0.0, 0.8, 1.6], 6.8, 1040, 0.3), "sine");
for (let i = 1; i <= 6; i++) { const u = i / 6, yaw = u * Math.PI * 1.1; k("V", 49.7 + 0.76 * u, FR([0.0, 0.8, 1.0], 6.8, 1040, 0.3, yaw), "lin"); }
// C — keyboard + script, speaker, honest-notes board, dive into the speaker cone
cut("C", 50.46, FR([-2.6, 0.7, 1.1], 3.0, 1000, 0.35)); k("C", 52.4, FR([-2.2, 0.8, 1.0], 3.4, 1000, 0.32), "sine");
k("C", 53.1, FR([0.0, 1.2, 0.4], 6.4, 1060, 0.18), "io"); k("C", 54.5, FR([0.0, 1.2, 0.4], 6.2, 1060, 0.18), "sine");
k("C", 55.4, FR([-1.0, 2.2, -2.2], 3.9, 700, 0.05), "io"); k("C", 60.3, FR([-1.0, 2.2, -2.2], 3.9, 720, 0.05), "sine");
k("C", 60.62, FR([2.05, 1.35, 0.6], 2.2, 1000, 0.03), "io"); k("C", 60.9, FR([2.05, 1.35, 0.7], 0.25, 1000, 0.0), "in");
// M — out of the REC light; meeting table; glass box; island hop flight to Y
cut("M", 60.91, FR([0.5, 2.25, 0.2], 0.6, 1000, 0.05, -0.3)); k("M", 61.8, FR([0.0, 1.25, 0.2], 5.0, 1040, 0.14), "out");
k("M", 63.2, FR([0.0, 1.25, 0.2], 4.8, 1040, 0.14), "sine"); k("M", 63.9, FR([1.13, 1.45, 0.42], 2.3, 1000, 0.12, -0.3), "io"); k("M", 65.6, FR([1.13, 1.45, 0.42], 2.2, 1000, 0.12, -0.3), "sine");
k("M", 66.4, FR([0.3, 1.5, 0.4], 5.0, 1040, 0.25), "io"); k("M", 68.55, FR([0.3, 1.5, 0.4], 4.8, 1040, 0.25), "sine");
k("M", 69.3, (() => { const v = FR([0.3, 1.5, 0.4], 4.8, 1040, 0.25); const T = [WP.Y[0] - WP.M[0], WP.Y[1] - WP.M[1], WP.Y[2] - WP.M[2]];
  return [v[0] + T[0] * 0.55, v[1] + 9, v[2] + T[2] * 0.55, T[0] * 0.6, T[1] + 2, T[2] * 0.6, 40]; })(), "in");
k("Y", 70.0, FR(YWIN, 3.6, 1000, 0.08, -0.25), "out");
// Y
k("Y", 72.85, FR(YWIN, 3.4, 1000, 0.08, -0.25), "sine"); k("Y", 73.35, FR([0.5, 1.6, -0.3], 7.8, 1060, 0.15), "io"); k("Y", 75.4, FR([0.5, 1.6, -0.3], 7.6, 1060, 0.15), "sine");
k("Y", 76.3, FR([-0.8, 0.7, 2.6], 5.0, 1040, 0.45), "io"); k("Y", 79.5, FR([-0.8, 0.7, 2.6], 4.8, 1040, 0.45), "sine");
// dolly zoom: the camera pulls back while the fov narrows (subject size kept), then the shockwave cut to the CTA
{ const T = [-0.8, 0.7, 2.6]; for (let i = 1; i <= 4; i++) { const u = i / 4, fov = 40 - 26 * u, d0 = (4.8 * 1080) / (1040 * 2 * TH), th = Math.tan((fov * Math.PI) / 360) * W / H, d = (4.8 * 1080) / (1040 * 2 * th);
  const el = 0.45; C.push([79.5 + 0.64 * u, at("Y")([T[0], T[1] + d * Math.sin(el), T[2] + d * Math.cos(el), T[0], T[1], T[2], fov]), "sine"]); void d0; } }
cut("L", 80.15, FR([0, 2.45, -0.5], 5.4, 1000, 0.14)); k("L", 87.5, FR([0, 2.5, -0.5], 5.8, 1000, 0.16), "sine");
C.sort((a, b) => a[0] - b[0]);
window.VX = { C, WP };
scene.add(cam);

/* ---------------------------------------------------------------- render */
let ready = false; const LIFTAT = (t) => 230 * U(t, 5.9, 6.6);
const ANIM = { L: animL, J: animJ, U: animU, Z: animZ, V: animV, C: animC, M: animM, Y: animY };
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  DOT.visible = DOTG.visible = false;
  for (const kk in worlds) { worlds[kk].visible = VIS[kk].some(([a, b]) => t >= a && t < b); if (worlds[kk].visible) ANIM[kk](t); }
  const v = keys(t, C), hx = Math.sin(t * 0.9) * 0.02, hy = Math.sin(t * 1.3 + 1) * 0.015;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.up.set(0, 1, 0); cam.lookAt(v[3], v[4], v[5]);
  const tx = v[3], ty = Math.abs(v[4] - cam.position.y) > 8 ? cam.position.y - 3 : v[4], tz = v[5]; moon.position.set(tx - 6, ty + 12, tz + 8); moon.target.position.set(tx, ty - 1, tz - 1); warm.position.set(tx + 6, ty + 4, tz + 7); warm.target.position.set(tx, ty, tz);
  renderer.render(scene, cam);
}
window.VX.render = render;
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  buildL(); buildJ(); buildU(); buildZ(); buildV(); buildC(); buildM(); buildY(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = PR;
window.addEventListener("hf-seek", (e) => render(window.WARP(e.detail.time)));   // scenes are keyed to the take-2 timeline (tools/warp.py)
