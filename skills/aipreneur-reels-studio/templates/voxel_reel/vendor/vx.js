/* R26 · Hook × Isi × CTA — voxel night worlds (own assets), one absolute camera path through 9 floating islands.
   Deterministic: render(t) is a pure function of t ("hf-seek"). Transitions (all different): portal zoom-through (H->S), elevator
   layers (S->T), whip tilt to the sky (T->M), jackpot cube burst (M->P, + page flash), iris (P->L, page), 180° orbit (L->R),
   turntable spin-blur (R->D, + page blur), button shockwave (D->A, page ring). */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { SVGLoader } from "three/addons/loaders/SVGLoader.js";
import { MAT, rnd, setSeed, boxes, emi, ctex, rr, cl, EZ, U, keys, blinkAt, person, robot, glow, label, setLabel, FONT } from "./vxlib.js";

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
scene.fog = new THREE.Fog(0x0c1a44, 26, 70);
const hemi = new THREE.HemisphereLight(0x9fbaff, 0x0a1230, 0.75); scene.add(hemi);
const moon = new THREE.DirectionalLight(0xc6dbff, 2.1); moon.castShadow = true; moon.shadow.mapSize.set(2048, 2048); moon.shadow.bias = -0.0004; moon.shadow.normalBias = 0.025;
Object.assign(moon.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10, near: 1, far: 45 }); scene.add(moon, moon.target);
const warm = new THREE.DirectionalLight(0xffc48a, 0.7); scene.add(warm, warm.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 140);

/* ---------------------------------------------------------------- stars + clouds */
const stars = new THREE.Group(); scene.add(stars);
{ setSeed(91); const N = 700, p = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { const u = rnd() * 2 - 1, a = rnd() * Math.PI * 2, r = 95, s = Math.sqrt(1 - u * u); p[i * 3] = r * s * Math.cos(a); p[i * 3 + 1] = Math.abs(r * u) * 0.9 + 4; p[i * 3 + 2] = r * s * Math.sin(a); }
  const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(p, 3));
  stars.add(new THREE.Points(g, new THREE.PointsMaterial({ color: 0xcfe2ff, size: 2.2, sizeAttenuation: false, fog: false, transparent: true, opacity: 0.85 }))); }

/* ---------------------------------------------------------------- shared */
const RIM = emi("#36e0ff", 1.3);
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
const WP = { H: [0, 0, 0], S: [60, 0, 0], T: [60, 0, -30], M: [120, 0, 0], P: [180, 0, 0], L: [240, 0, 0], R: [240, 0, 34], D: [300, 0, 0], A: [360, 0, 0] };
const VIS = { H: [-1, 3.47], S: [3.43, 10.0], T: [9.3, 14.62], M: [14.45, 21.4], P: [21.15, 27.95], L: [27.6, 34.4], R: [33.3, 39.6], D: [39.4, 46.42], A: [46.2, 99] };
const worlds = {}; const mk = (k) => { const g = new THREE.Group(); g.position.set(...WP[k]); worlds[k] = g; scene.add(g); return g; };
function clouds(k, n, sd) { setSeed(sd); for (let i = 0; i < n; i++) { const x = (rnd() - 0.5) * 34, y = -6 + rnd() * 9, z = -18 + rnd() * 22;
  if (Math.hypot(x, z) < 8 && y > -4) continue; const L = [], q = 3 + Math.floor(rnd() * 3), sz = 0.8 + rnd() * 1.1;
  for (let j = 0; j < q; j++) L.push([(j - q / 2) * sz * 0.8, (rnd() - 0.3) * sz * 0.5, (rnd() - 0.5) * sz, sz * (1 + rnd()), sz * (0.55 + rnd() * 0.5), sz * (1 + rnd() * 0.8), j & 1 ? "#22386c" : "#1b2f60"]);
  const m = boxes(L, MAT, false); m.castShadow = m.receiveShadow = false; m.position.set(x, y, z); worlds[k].add(m); } }

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
/* ---------------------------------------------------------------- textures */
const TX = {};
function fitFont(g, lines, px, maxW) { // shrink until every line fits the card (no cut text)
  do { g.font = `700 ${px}px ${FONT}`; if (lines.every((l) => g.measureText(l).width <= maxW)) return; px -= 2; } while (px > 10);
}
function adBand(g, w, h, k) { // the ad mock in three bands: 0 hook, 1 isi, 2 cta
  if (k === 0) { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = "#ff5c8a"; g.fillRect(0, 0, w, 14);
    g.fillStyle = "#0a0d2c"; g.textAlign = "center"; fitFont(g, ["Masih bikin", "iklan satu-satu?"], Math.round(h * 0.2), w * 0.84); g.fillText("Masih bikin", w / 2, h * 0.46); g.fillText("iklan satu-satu?", w / 2, h * 0.74); }
  if (k === 1) { g.fillStyle = "#eef3fb"; g.fillRect(0, 0, w, h); g.fillStyle = "#b9cdeb"; rr(g, w * 0.1, h * 0.08, w * 0.8, h * 0.56, 18); g.fill();
    g.fillStyle = "#ffffff"; g.beginPath(); g.moveTo(w * 0.45, h * 0.24); g.lineTo(w * 0.58, h * 0.36); g.lineTo(w * 0.45, h * 0.48); g.fill();
    g.fillStyle = "#c9d6ea"; for (let i = 0; i < 2; i++) { rr(g, w * 0.1, h * (0.72 + i * 0.12), w * (0.8 - i * 0.25), h * 0.06, 8); g.fill(); } }
  if (k === 2) { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = "#01ccf7"; rr(g, w * 0.14, h * 0.26, w * 0.72, h * 0.42, h * 0.21); g.fill();
    g.fillStyle = "#0a0d2c"; g.textAlign = "center"; fitFont(g, ["Pesan sekarang"], Math.round(h * 0.17), w * 0.66); g.fillText("Pesan sekarang", w / 2, h * 0.53); }
}
function makeTextures() {
  TX.band = [0, 1, 2].map((k) => ctex(600, 450, (g, w, h) => adBand(g, w, h, k)));
  TX.ad = ctex(600, 1350, (g, w) => { [0, 1, 2].forEach((k) => { g.save(); g.translate(0, k * 450); adBand(g, w, 450, k); g.restore(); });
    g.strokeStyle = "#dbe5f4"; g.lineWidth = 10; g.strokeRect(5, 5, w - 10, 1340); });
  TX.clap = ctex(512, 360, (g, w, h) => { g.fillStyle = "#111827"; g.fillRect(0, 0, w, h); g.strokeStyle = "#ffffff"; g.lineWidth = 4;
    for (const y of [120, 220]) { g.beginPath(); g.moveTo(16, y); g.lineTo(w - 16, y); g.stroke(); } g.beginPath(); g.moveTo(w / 2, 120); g.lineTo(w / 2, 220); g.stroke();
    g.fillStyle = "#ffffff"; g.font = `700 54px ${FONT}`; g.fillText("AI PRENEUR", 30, 84); g.font = `700 34px ${FONT}`; g.fillText("SCENE 1", 30, 182); g.fillText("TAKE 1", w / 2 + 24, 182);
    g.fillStyle = "#7fe3ff"; g.fillText("1x SYUTING", 30, 290); });
  TX.stripe = ctex(512, 80, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = "#111827"; for (let x = -80; x < w; x += 80) { g.beginPath(); g.moveTo(x, h); g.lineTo(x + 40, 0); g.lineTo(x + 80, 0); g.lineTo(x + 40, h); g.fill(); } });
  const sym = (txt, col, sub) => ctex(256, 256, (g, w) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, 256, 256); g.fillStyle = col; g.fillRect(0, 0, 256, 18); g.fillRect(0, 238, 256, 18);
    g.fillStyle = "#0a0d2c"; g.textAlign = "center"; g.font = `700 ${txt.length > 6 ? 40 : 66}px ${FONT}`; g.fillText(txt, 128, 140); if (sub) { g.fillStyle = col; g.font = `700 30px ${FONT}`; g.fillText(sub, 128, 196); } });
  TX.reel = [["H1", "H7", "H12", "H23", "H31", "H38", "H44", "H50"].map((s) => sym(s, "#ff5c8a", "HOOK")),
    ["DEMO", "TESTI", "EDUKASI", "CERITA", "DEMO", "TESTI", "EDUKASI", "CERITA"].map((s) => sym(s, "#22d3ff", "ISI")),
    ["CTA 1", "CTA 2", "CTA 3", "CTA 1", "CTA 2", "CTA 3", "CTA 1", "CTA 2"].map((s) => sym(s, "#ffc531", "CTA"))];
  TX.marquee = ctex(1024, 200, (g, w, h) => { g.fillStyle = "#0a0d2c"; g.fillRect(0, 0, w, h); g.fillStyle = "#ffc531"; g.font = `700 92px ${FONT}`; g.textAlign = "center"; g.fillText("HOOK × ISI × CTA", w / 2, 132); });
  TX.play = ctex(256, 180, (g, w, h) => { g.fillStyle = "#101a3a"; g.fillRect(0, 0, w, h); g.fillStyle = "#ff4d5e"; rr(g, 78, 40, 100, 100, 26); g.fill(); g.fillStyle = "#fff"; g.beginPath(); g.moveTo(114, 66); g.lineTo(150, 90); g.lineTo(114, 114); g.fill(); });
  TX.board = ctex(512, 340, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = "#294b77"; [[60, 170], [150, 120], [240, 200], [330, 90]].forEach(([x, hh]) => g.fillRect(x, 300 - hh, 60, hh));
    g.strokeStyle = "#ff5c8a"; g.lineWidth = 8; g.beginPath(); g.moveTo(70, 220); g.lineTo(180, 170); g.lineTo(270, 120); g.lineTo(380, 60); g.stroke(); });
  TX.screen = ctex(320, 200, (g, w, h) => { g.fillStyle = "#e9f2ff"; g.fillRect(0, 0, w, h); g.fillStyle = "#0a0d2c"; g.fillRect(0, 0, w, 34); g.fillStyle = "#01ccf7"; rr(g, 24, 60, 170, 46, 12); g.fill();
    g.fillStyle = "#c9d6ea"; rr(g, 24, 124, 260, 16, 8); g.fill(); rr(g, 24, 152, 200, 16, 8); g.fill(); g.fillStyle = "#0a0d2c"; g.beginPath(); g.moveTo(170, 84); g.lineTo(170, 116); g.lineTo(180, 106); g.lineTo(192, 124); g.lineTo(198, 120); g.lineTo(186, 102); g.lineTo(198, 100); g.fill(); });
  TX.dom = ["1  Lakukan apa", "2  Kenapa penting", "3  Kapan", "4  Segampang apa", "5  Dapat apa"].map((s) => ctex(256, 640, (g, w, h) => {
    g.fillStyle = "#f4f7fc"; g.fillRect(0, 0, w, h); g.fillStyle = "#ffc531"; g.fillRect(0, 0, w, 20); g.save(); g.translate(w / 2, h / 2); g.rotate(-Math.PI / 2);
    g.fillStyle = "#0a0d2c"; g.textAlign = "center"; g.font = `700 ${s.length > 12 ? 50 : 60}px ${FONT}`; g.fillText(s, 0, 20); g.restore(); }));
  TX.card = ctex(256, 340, (g, w, h) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, w, h); g.fillStyle = "#ff5c8a"; g.fillRect(0, 0, w, 16); g.fillStyle = "#0a0d2c";
    g.font = `700 40px ${FONT}`; g.fillText("HOOK", 24, 72); g.fillStyle = "#c9d6ea"; for (let i = 0; i < 4; i++) { rr(g, 24, 104 + i * 44, 200 - (i % 2) * 50, 18, 9); g.fill(); } });
  TX.brief = ctex(256, 340, (g, w, h) => { g.fillStyle = "#fff8e6"; g.fillRect(0, 0, w, h); g.fillStyle = "#0a0d2c"; g.font = `700 44px ${FONT}`; g.fillText("BRIEF", 24, 70);
    g.fillStyle = "#e3c98f"; for (let i = 0; i < 5; i++) { rr(g, 24, 100 + i * 42, 200 - (i % 3) * 40, 16, 8); g.fill(); } });
  TX.robo = ctex(256, 256, (g) => { g.fillStyle = "#ffffff"; g.fillRect(0, 0, 256, 256); });
}

/* ---------------------------------------------------------------- H: film set + clapper shatter + portal card */
const Hh = {};
function buildH() {
  const g = mk("H"); g.add(island(5, 4)); clouds("H", 9, 3);
  // camera rig
  const rig = new THREE.Group(); rig.position.set(-1.05, 0, -1.5); rig.rotation.y = 0.45; g.add(rig);
  rig.add(boxes([[0, 0.55, 0, 0.08, 1.1, 0.08, "#8a9bb8"], [0, 0.03, 0, 0.7, 0.06, 0.7, "#5b6b8c"], [0, 1.45, 0, 0.5, 0.42, 0.8, "#1b2238"], [0, 1.45, 0.52, 0.32, 0.32, 0.26, "#3a4560"],
    [0, 1.45, 0.66, 0.36, 0.36, 0.04, "#0b1020"], [0, 1.82, -0.14, 0.06, 0.36, 0.36, "#2a3350"], [0, 1.82, 0.22, 0.06, 0.3, 0.3, "#2a3350"]]));
  Hh.rec = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.08, 0.08), emi("#ff3344", 3)); Hh.rec.position.set(0.18, 1.7, 0.3); rig.add(Hh.rec);
  Hh.recG = glow("#ff3344", 0.6, 0.6); Hh.recG.position.copy(Hh.rec.position); rig.add(Hh.recG);
  // light stands with softboxes
  for (const [x, z, ry] of [[2.2, -1.2, -0.6], [-2.8, 1.2, 0.9]]) { const s = new THREE.Group(); s.position.set(x, 0, z); s.rotation.y = ry; g.add(s);
    s.add(boxes([[0, 0.9, 0, 0.07, 1.8, 0.07, "#8a9bb8"], [0, 0.03, 0, 0.6, 0.06, 0.6, "#5b6b8c"], [0, 2.0, -0.12, 0.9, 0.7, 0.2, "#1b2238"]]));
    const p = new THREE.Mesh(new THREE.BoxGeometry(0.82, 0.62, 0.02), emi("#fff1d8", 2.2)); p.position.set(0, 2.0, 0.0); s.add(p); }
  const pl = new THREE.PointLight(0xffd9a8, 6, 8); pl.position.set(0.8, 2.4, 1.6); g.add(pl);
  // director chair + floor mark
  g.add(boxes([[2.6, 0.45, 1.6, 0.6, 0.06, 0.5, "#c0392b"], [2.6, 0.75, 1.36, 0.6, 0.5, 0.05, "#c0392b"], [2.33, 0.22, 1.6, 0.05, 0.45, 0.5, "#e9cfa8"], [2.87, 0.22, 1.6, 0.05, 0.45, 0.5, "#e9cfa8"],
    [0, 0.005, 0.2, 0.7, 0.01, 0.08, "#ffc531"], [0, 0.005, 0.2, 0.08, 0.01, 0.7, "#ffc531"]]));
  // clapperboard on a stand
  Hh.clap = new THREE.Group(); Hh.clap.position.set(0, 1.25, 0.9); g.add(Hh.clap);
  g.add(boxes([[0, 0.55, 0.9, 0.06, 1.1, 0.06, "#8a9bb8"], [0, 0.03, 0.9, 0.5, 0.06, 0.5, "#5b6b8c"]]));
  const body = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.62, 0.05), [MATB, MATB, MATB, MATB, new THREE.MeshStandardMaterial({ map: TX.clap, roughness: 0.6 }), MATB]); body.castShadow = true; Hh.clap.add(body);
  Hh.stick = new THREE.Group(); Hh.stick.position.set(-0.45, 0.34, 0); Hh.clap.add(Hh.stick);
  const st = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.13, 0.05), [MATB, MATB, MATB, MATB, new THREE.MeshStandardMaterial({ map: TX.stripe }), MATB]); st.position.set(0.45, 0.065, 0); Hh.stick.add(st);
  // the swarm of ad cards (instanced)
  const N = 360; Hh.N = N;
  Hh.cards = new THREE.InstancedMesh(new THREE.BoxGeometry(0.13, 0.17, 0.012), new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x2fd6ff, emissiveIntensity: 0.55, roughness: 0.5 }), N);
  Hh.cards.frustumCulled = false; g.add(Hh.cards); setSeed(13);
  Hh.cv = []; for (let i = 0; i < N; i++) { const a = rnd() * Math.PI * 2, el = 0.15 + rnd() * 1.1, sp = 2.2 + rnd() * 6.5;
    Hh.cv.push({ v: new THREE.Vector3(Math.cos(a) * Math.cos(el) * sp, Math.sin(el) * sp + 1.2, Math.sin(a) * Math.cos(el) * sp), r: [rnd() * 6, rnd() * 6, rnd() * 6], d: rnd() * 0.12 }); }
  LOGO.h = [["instagram", window.LOGOS.instagram.hex, -0.85, 1.1, 0.4], ["tiktok", "#ffffff", 0.9, 1.45, 0.2], ["meta", window.LOGOS.meta.hex, -0.1, 2.3, -0.2]].map(([n, c, x, y, z]) => { const o = logo3d(n, c, 0.5); o.userData.p = new THREE.Vector3(x, y, z); o.visible = false; g.add(o); return o; });
  // portal hero card
  Hh.hero = new THREE.Mesh(new THREE.PlaneGeometry(0.6, 1.35), new THREE.MeshBasicMaterial({ map: TX.ad, toneMapped: false })); g.add(Hh.hero);
  Hh.hg = glow("#38dcff", 1.6, 2.4); g.add(Hh.hg);
}
const MATB = new THREE.MeshStandardMaterial({ color: 0x111827, roughness: 0.6 });
const _o = new THREE.Object3D();
function animH(t) {
  const blink = Math.floor(t * 2) % 2; Hh.rec.material.emissiveIntensity = blink ? 3.5 : 0.6; Hh.recG.material.opacity = blink ? 0.9 : 0.15;
  Hh.stick.rotation.z = 0.55 * (1 - U(t, 1.45, 1.62, "in")) + (t > 1.62 ? 0.04 * Math.exp(-(t - 1.62) * 12) * Math.sin((t - 1.62) * 60) : 0);
  const shat = t >= 2.05; Hh.clap.visible = !shat; Hh.clap.position.y = 1.25 + (t > 1.62 && t < 2.05 ? 0.02 * Math.sin(t * 90) : 0);
  Hh.cards.visible = shat;
  if (shat) { const tau = t - 2.05;
    Hh.cv.forEach((c, i) => { const k = 2.2, f = (1 - Math.exp(-k * Math.max(0, tau - c.d))) / k;
      _o.position.set(c.v.x * f, 1.25 + c.v.y * f + 0.25 * tau, 0.9 + c.v.z * f); _o.rotation.set(c.r[0] + tau * 3, c.r[1] + tau * 2, c.r[2]);
      _o.scale.setScalar(tau < c.d ? 0.001 : Math.min(1, (tau - c.d) * 6)); _o.updateMatrix(); Hh.cards.setMatrixAt(i, _o.matrix); });
    Hh.cards.instanceMatrix.needsUpdate = true; }
  LOGO.h.forEach((o, i) => { const u = U(t, 2.06 + i * 0.07, 2.5 + i * 0.07, "back"); o.visible = t > 2.06 + i * 0.07; o.position.set(o.userData.p.x * u, 1.25 + (o.userData.p.y - 1.25 + 1.0) * u, 0.9 + (o.userData.p.z - 0.9 + 0.8) * u); o.rotation.set(0.2 * Math.sin(t * 2 + i), (1 - u) * 6 + Math.sin(t * 1.6 + i) * 0.6, 0); o.scale.setScalar(Math.max(0.001, u)); });
  const hu = U(t, 2.25, 2.9, "out"); Hh.hero.visible = Hh.hg.visible = t > 2.2;
  Hh.hero.position.set(0.6 * (1 - hu), 1.4 + 1.2 * hu, 0.9 + 1.3 * hu); Hh.hero.rotation.set(0, (1 - hu) * 2.5, (1 - hu) * 0.8); Hh.hero.scale.setScalar(0.25 + 0.75 * hu);
  Hh.hg.position.copy(Hh.hero.position); Hh.hg.position.z -= 0.05; Hh.hg.material.opacity = 0.5 * hu;
}

/* ---------------------------------------------------------------- S: the ad block sliced into HOOK / ISI / CTA */
const S = {};
const ROLE = ["#ff5c8a", "#22d3ff", "#ffc531"];
function buildS() {
  const g = mk("S"); g.add(island(4, 4)); clouds("S", 8, 5);
  g.add(boxes([[0, 0.15, 0, 2.2, 0.3, 1.6, "#24407a"], [0, 0.31, 0, 2.24, 0.03, 1.64, "#3b5ea8"]]));
  S.lay = [0, 1, 2].map((k) => { const l = new THREE.Group(); g.add(l);
    const m = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.2, 1.0), new THREE.MeshStandardMaterial({ color: 0xe8eef8, roughness: 0.6 })); m.castShadow = m.receiveShadow = true; l.add(m);
    const f = new THREE.Mesh(new THREE.PlaneGeometry(1.6, 1.2), new THREE.MeshBasicMaterial({ transparent: true, map: TX.band[2 - k] === undefined ? TX.band[0] : TX.band[k === 0 ? 2 : k === 2 ? 0 : 1], toneMapped: false })); f.position.z = 0.501; l.add(f);
    const side = new THREE.MeshStandardMaterial({ color: 0x0b1640, emissive: new THREE.Color(ROLE[2 - k]), emissiveIntensity: 0 });
    for (const x of [-0.805, 0.805]) { const s = new THREE.Mesh(new THREE.BoxGeometry(0.01, 1.2, 1.0), side); s.position.x = x; l.add(s); }
    const lb = label(["CTA", "ISI", "HOOK"][k], ROLE[2 - k], "#0a0d2c", 0.36); lb.position.set(1.45, 0, 0.6); l.add(lb);
    return { l, side, lb, f }; });   // k = 0 bottom (CTA) .. 2 top (HOOK)
  S.em = [-1, 1].map((sx) => { const e = boxes([[0, 0, 0, 0.22, 0.22, 0.22, "#3a4560"]]); e.position.set(sx * 1.45, 0, 0.8); g.add(e); return e; });
  S.beam = new THREE.Mesh(new THREE.BoxGeometry(2.9, 0.03, 0.04), emi("#ff3b6b", 4)); g.add(S.beam);
  S.bg = glow("#ff3b6b", 3.2, 0.5); g.add(S.bg);
  S.sp = []; for (let i = 0; i < 24; i++) { const m = new THREE.Mesh(new THREE.BoxGeometry(0.045, 0.045, 0.045), emi("#ffd166", 3)); m.visible = false; g.add(m); S.sp.push({ m, a: (i / 24) * Math.PI * 2, s: 0.6 + (i % 5) * 0.25 }); }
}
function animS(t) {
  const cutAt = [6.3, 6.55], hy = [1.5, 2.7];
  const sep = U(t, 6.95, 7.45, "back"), slide = U(t, 9.42, 9.86, "in");
  S.lay.forEach((o, k) => { const y0 = 0.9 + 1.2 * k;
    o.l.position.set((k === 1 ? 1 : -1) * 3.8 * slide, y0 + 0.28 * k * sep, 0); o.l.rotation.z = (k - 1) * 0.04 * sep * (1 - slide);
    const on = [U(t, 8.9, 9.1), U(t, 8.1, 8.3), U(t, 7.55, 7.75)][k];
    o.side.emissiveIntensity = 2.4 * on; const fade = 1 - U(t, 8.95, 9.2); setLabel(o.lb, EZ.back(cl(on, 0, 1)) * fade); o.f.material.opacity = fade; });
  // two laser passes front -> back at the two seams
  let bv = false; [0, 1].forEach((c) => { const u = (t - cutAt[c]) / 0.32; if (u > 0 && u < 1) { bv = true;
    S.beam.position.set(0, hy[c], 0.75 - 1.5 * u); S.bg.position.copy(S.beam.position); S.em.forEach((e) => { e.position.y = hy[c]; e.position.z = S.beam.position.z; }); } });
  S.beam.visible = S.bg.visible = bv; S.em.forEach((e) => (e.visible = t > 5.9 && t < 7.2));
  S.sp.forEach((s, i) => { const c = i % 2, u = (t - cutAt[c] - 0.05) / 0.5; s.m.visible = u > 0 && u < 1; if (!s.m.visible) return;
    s.m.position.set(-0.8 + Math.cos(s.a) * 0.6 * u * s.s - 0.05, hy[c] + Math.sin(s.a) * 0.5 * u * s.s - 0.9 * u * u, 0.5 + 0.3 * u); s.m.scale.setScalar(1 - u); });
}

/* ---------------------------------------------------------------- T: towers fill (50 / 3–5 / 1–3) */
const T = {};
function buildT() {
  const g = mk("T"); g.add(island(5, 3)); clouds("T", 8, 7);
  const frame = (x, w, h) => { for (const [dx, dz] of [[-1, -1], [1, -1], [-1, 1], [1, 1]]) { const p = new THREE.Mesh(new THREE.BoxGeometry(0.05, h, 0.05), RIM); p.position.set(x + dx * w / 2, h / 2, dz * 0.4); g.add(p); }
    const back = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.03), new THREE.MeshStandardMaterial({ color: 0x0d1b40, transparent: true, opacity: 0.7 })); back.position.set(x, h / 2, -0.42); g.add(back); };
  frame(-2.4, 1.7, 3.5); frame(0.3, 1.3, 2.3); frame(2.6, 1.0, 1.8);
  T.hook = []; for (let k = 0; k < 50; k++) { const c = k % 5, r = Math.floor(k / 5); const m = boxes([[0, 0, 0, 0.3, 0.3, 0.3, ["#ff5c8a", "#ff7aa0", "#e8457a"][(c + r) % 3]]]);
    m.userData.p = new THREE.Vector3(-2.4 + (c - 2) * 0.32, 0.17 + r * 0.32, 0); m.visible = false; g.add(m); T.hook.push(m); }
  T.isi = []; for (let k = 0; k < 5; k++) { const m = boxes([[0, 0, 0, 1.15, 0.4, 0.62, k < 3 ? "#22d3ff" : "#1b7fa3"]]); m.userData.p = new THREE.Vector3(0.3, 0.22 + k * 0.43, 0); m.visible = false; g.add(m); T.isi.push(m); }
  T.cta = []; for (let k = 0; k < 3; k++) { const m = boxes([[0, 0, 0, 0.86, 0.5, 0.62, k < 1 ? "#ffc531" : "#b88d1f"]]); m.userData.p = new THREE.Vector3(2.6, 0.27 + k * 0.53, 0); m.visible = false; g.add(m); T.cta.push(m); }
  T.lb = [["50 HOOK", ROLE[0], -2.4, 3.95], ["3–5 ISI", ROLE[1], 0.3, 2.75], ["1–3 CTA", ROLE[2], 2.6, 2.25]].map(([s, c, x, y]) => { const l = label(s, c, "#0a0d2c", 0.4); l.position.set(x, y, 0.3); g.add(l); return l; });
}
const T_HOOK = (k) => 10.15 + k * 0.03, T_ISI = (k) => 11.5 + k * 0.13, T_CTA = (k) => 12.7 + k * 0.32;
function drop(m, t, t0) { const u = U(t, t0 - 0.3, t0, "in"), s = t - t0; m.visible = t > t0 - 0.3; if (!m.visible) return;
  m.position.copy(m.userData.p); m.position.y += 5 * (1 - u) + (s > 0 ? Math.exp(-s * 10) * Math.abs(Math.sin(s * 18)) * 0.12 : 0); }
function animT(t) {
  T.hook.forEach((m, k) => drop(m, t, T_HOOK(k))); T.isi.forEach((m, k) => drop(m, t, T_ISI(k))); T.cta.forEach((m, k) => drop(m, t, T_CTA(k)));
  T.lb.forEach((l) => (l.visible = false));
}

/* ---------------------------------------------------------------- M: slot machine + conveyor + jackpot burst */
const M = {};
const REEL = [ // spins: [start, stop, landing face]
  [[14.95, 15.95, 3], [17.55, 18.3, 6], [18.85, 19.6, 1], [19.95, 20.4, 7]],
  [[14.95, 16.15, 2], [17.6, 18.45, 1], [18.9, 19.75, 3], [20.0, 20.45, 0]],
  [[14.95, 16.35, 0], [17.65, 18.6, 1], [18.95, 19.9, 2], [20.05, 20.5, 0]]];
function buildM() {
  const g = mk("M"); g.add(island(5, 4)); clouds("M", 9, 9);
  g.add(boxes([[0, 1.7, 0, 3.0, 3.4, 1.4, "#1f3c62"], [0, 0.05, 0, 3.3, 0.1, 1.7, "#ffc531"], [0, 3.45, 0, 3.2, 0.12, 1.6, "#ffc531"], [0, 1.95, 0.71, 2.7, 1.25, 0.02, "#0a1430"],
    [0, 0.85, 0.75, 1.6, 0.4, 0.2, "#0a1430"], [0, 0.66, 0.9, 1.7, 0.06, 0.5, "#ffc531"], [1.62, 1.6, 0, 0.24, 0.9, 0.5, "#294b77"]]));
  const mq = new THREE.Mesh(new THREE.PlaneGeometry(2.8, 0.55), new THREE.MeshBasicMaterial({ map: TX.marquee, toneMapped: false })); mq.position.set(0, 3.0, 0.711); g.add(mq);
  M.bA = emi("#ffe08a", 2.5); M.bB = emi("#ffe08a", 0.3);
  for (let i = 0; i < 16; i++) { const b = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.09, 0.05), i % 2 ? M.bA : M.bB); const u = i / 15; b.position.set(-1.45 + 2.9 * u, 3.32, 0.73); g.add(b);
    const b2 = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.09, 0.05), i % 2 ? M.bB : M.bA); b2.position.set(-1.45 + 2.9 * u, 2.68, 0.73); g.add(b2); }
  M.reels = [-0.86, 0, 0.86].map((x, r) => { const d = new THREE.Group(); d.position.set(x, 1.95, 0.25); g.add(d);
    TX.reel[r].forEach((tx, f) => { const q = new THREE.Mesh(new THREE.PlaneGeometry(0.74, 0.44), new THREE.MeshBasicMaterial({ map: tx, toneMapped: false }));
      const a = (f / 8) * Math.PI * 2; q.position.set(0, Math.sin(a) * 0.53, Math.cos(a) * 0.53); q.rotation.x = -a; d.add(q); }); return d; });
  M.lever = new THREE.Group(); M.lever.position.set(1.78, 1.9, 0); g.add(M.lever);
  M.lever.add(boxes([[0, 0.55, 0, 0.08, 1.1, 0.08, "#c3cfe2"]])); const ball = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.26, 0.26), emi("#ff4d5e", 1.4)); ball.position.y = 1.15; M.lever.add(ball);
  g.add(boxes([[3.6, 0.5, 1.05, 4.6, 0.1, 0.7, "#2b3348"], [3.6, 0.25, 1.4, 4.6, 0.5, 0.05, "#3a4560"], [3.6, 0.25, 0.7, 4.6, 0.5, 0.05, "#3a4560"]]));
  M.cards = []; for (let i = 0; i < 24; i++) { const c = new THREE.Mesh(new THREE.PlaneGeometry(0.34, 0.46), new THREE.MeshBasicMaterial({ map: TX.ad, toneMapped: false, side: THREE.DoubleSide })); c.visible = false; g.add(c); M.cards.push(c); }
  M.coins = new THREE.InstancedMesh(new THREE.BoxGeometry(0.16, 0.16, 0.05), new THREE.MeshStandardMaterial({ color: 0xffc531, emissive: 0xffa400, emissiveIntensity: 0.8, metalness: 0.3, roughness: 0.4 }), 220);
  M.coins.frustumCulled = false; g.add(M.coins); setSeed(29); M.cv = []; for (let i = 0; i < 220; i++) M.cv.push({ v: new THREE.Vector3((rnd() - 0.5) * 7, 1 + rnd() * 5, 3 + rnd() * 9), r: rnd() * 9, d: rnd() * 0.25 });
  LOGO.m = [["meta", window.LOGOS.meta.hex, 1.15, 0.5], ["tiktok", "#ffffff", 1.15, 1.02]].map(([n, c, x, y]) => { const o = logo3d(n, c, 0.42); o.position.set(x, y, 0.95); o.userData.y = y; g.add(o); return o; });
  M.glow = glow("#ffc531", 6, 6); M.glow.position.set(0, 2.2, 1.2); g.add(M.glow);
}
function reelAngle(r, t) { let a = 0; for (const [t0, t1, face] of REEL[r]) { const base = a; if (t < t0) break;
  const target = Math.ceil(base / (Math.PI * 2)) * Math.PI * 2 + 5 * Math.PI * 2 + (face / 8) * Math.PI * 2;
  a = t >= t1 ? target : base + (target - base) * EZ.out((t - t0) / (t1 - t0)); } return a; }
function animM(t) {
  M.reels.forEach((d, r) => (d.rotation.x = reelAngle(r, t)));
  LOGO.m.forEach((o, i) => { o.rotation.y = 0.5 * Math.sin(t * 1.6 + i * 1.5); o.position.y = o.userData.y + 0.08 * Math.sin(t * 2.2 + i) + (t > 20.45 ? 0.5 * EZ.out(cl((t - 20.45) / 0.4, 0, 1)) : 0); });
  M.lever.rotation.x = 1.15 * U(t, 14.78, 14.95, "in") * (1 - U(t, 15.05, 15.5, "back"));
  const jack = U(t, 20.45, 20.6); const ph = Math.floor(t * 7) % 2;
  M.bA.emissiveIntensity = jack > 0 ? 4 : ph ? 2.6 : 0.3; M.bB.emissiveIntensity = jack > 0 ? 4 : ph ? 0.3 : 2.6;
  M.glow.material.opacity = 0.9 * jack * (0.7 + 0.3 * Math.sin(t * 30));
  M.cards.forEach((c, i) => { const e = 16.45 + i * 0.16, s = t - e; c.visible = s > 0 && s < 1.6; if (!c.visible) return;
    const pop = U(t, e, e + 0.22, "back"); const q = Math.max(0, s - 0.15), side = i % 2 ? 1 : -1; c.position.set(side * (0.9 + q * 1.6), 0.95 + q * 1.1 - 0.5 * q * q, 1.1 + q * 0.9);
    c.rotation.set(-0.2, side * q * 1.2, side * q * 0.5); c.scale.setScalar(Math.max(0.001, pop) * 1.3 * (1 - U(t, e + 1.15, e + 1.55))); });
  const tau = t - 20.55; M.coins.visible = tau > 0;
  if (tau > 0) { M.cv.forEach((c, i) => { const s = Math.max(0, tau - c.d * 0.4); _o.position.set(c.v.x * s * 1.2, 2.0 + c.v.y * s - 2.5 * s * s, 0.9 + c.v.z * s * 1.3);
      _o.rotation.set(c.r + s * 9, s * 7, 0); _o.scale.setScalar(s > 0 ? 1 + s * 2 : 0.001); _o.updateMatrix(); M.coins.setMatrixAt(i, _o.matrix); }); M.coins.instanceMatrix.needsUpdate = true; }
}

/* ---------------------------------------------------------------- P: three proven sources feed the hook tower */
const P = {};
const SRC = [[-5, 0.9, -3], [0, 1.7, -6.5], [5, 0.9, -3]], SRC_T = [23.0, 24.45, 25.8];
function buildP() {
  const g = mk("P"); g.add(island(2, 2)); clouds("P", 10, 11);
  for (let k = 0; k < 24; k++) { const c = k % 3, r = Math.floor(k / 3); g.add(boxes([[(c - 1) * 0.36, 0.2 + r * 0.36, 0, 0.32, 0.32, 0.32, ["#ff5c8a", "#ff7aa0", "#e8457a"][(c + r) % 3]]])); }
  const tg = glow("#ff5c8a", 3, 5); tg.position.set(0, 1.6, 0); g.add(tg);
  P.isl = SRC.map(([x, y, z], i) => { const s = new THREE.Group(); s.position.set(x, y, z); g.add(s); s.add(island(1, 1)); return s; });
  // trophy
  P.isl[0].add(boxes([[0, 0.1, 0, 0.6, 0.2, 0.6, "#8a6a2a"], [0, 0.35, 0, 0.14, 0.3, 0.14, "#ffc531"], [0, 0.75, 0, 0.6, 0.5, 0.6, "#ffc531"], [0, 1.0, 0, 0.66, 0.06, 0.66, "#ffd75e"],
    [-0.38, 0.8, 0, 0.12, 0.3, 0.1, "#ffc531"], [0.38, 0.8, 0, 0.12, 0.3, 0.1, "#ffc531"]]));
  // content screen with play
  P.isl[1].add(boxes([[0, 0.5, 0, 0.08, 1.0, 0.08, "#5b6b8c"], [0, 1.25, -0.05, 1.3, 0.92, 0.08, "#1b2238"]]));
  const scr = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 0.84), new THREE.MeshBasicMaterial({ map: TX.play, toneMapped: false })); scr.position.set(0, 1.25, 0.0); P.isl[1].add(scr);
  // flame ("laris")
  P.flame = [0, 1, 2, 3, 4, 5].map((i) => { const m = boxes([[0, 0, 0, 0.3 - i * 0.03, 0.3, 0.3 - i * 0.03, ["#ff4d1f", "#ff7a1f", "#ffb02e", "#ffd75e", "#ff7a1f", "#ffb02e"][i]]], emi(["#ff4d1f", "#ff7a1f", "#ffb02e", "#ffd75e", "#ff7a1f", "#ffb02e"][i], 1.2));
    m.position.set((i % 2 ? 0.12 : -0.1) * (i > 2 ? 0.5 : 1), 0.2 + i * 0.2, (i % 3 - 1) * 0.08); P.isl[2].add(m); return m; });
  P.fg = glow("#ff8a3d", 2.2, 2.6); P.fg.position.set(0, 0.8, 0); P.isl[2].add(P.fg);
  // glowing pipes source -> tower, with travelling hook cubes
  P.pipe = SRC.map(([x, y, z]) => { const a = new THREE.Vector3(x, y + 0.3, z), b = new THREE.Vector3(0, 1.4, 0), len = a.distanceTo(b);
    const p = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.08, len), emi("#36e0ff", 1.8)); p.position.copy(a).lerp(b, 0.5); p.lookAt(b); g.add(p);
    const cubes = [0, 1, 2, 3, 4].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.2), emi("#ff5c8a", 1.6)); m.visible = false; g.add(m); return m; });
    return { p, a, b, cubes }; });
  P.lb = [["IKLAN LAMA YANG MENANG", "#ffc531"], ["KONTEN GRATIS", "#ff4d5e"], ["IKLAN ORANG YANG LARIS", "#ff8a3d"]].map(([s, c], i) => {
    const l = label(s, c, "#0a0d2c", 0.32); l.position.set(SRC[i][0], SRC[i][1] + 2.2, SRC[i][2]); g.add(l); return l; });
}
function animP(t) {
  P.pipe.forEach((q, i) => { const on = U(t, SRC_T[i], SRC_T[i] + 0.3); q.p.scale.z = Math.max(0.001, on); q.p.visible = on > 0.001;
    q.cubes.forEach((m, j) => { const u = ((t - SRC_T[i] - 0.2) * 0.9 + j / 5) % 1; m.visible = t > SRC_T[i] + 0.2 && u >= 0; if (!m.visible) return; m.position.copy(q.a).lerp(q.b, u); m.rotation.set(t * 3, t * 2, 0); });
    P.lb[i].visible = false; });
  P.flame.forEach((m, i) => m.scale.set(1 + 0.12 * Math.sin(t * 13 + i), 1 + 0.2 * Math.sin(t * 17 + i * 2), 1)); P.fg.material.opacity = 0.6 + 0.2 * Math.sin(t * 11);
}

/* ---------------------------------------------------------------- L: three awareness levels */
const L = {};
const LV_T = [29.05, 31.0, 32.75];
function buildL() {
  const g = mk("L"); g.add(island(5, 3)); clouds("L", 9, 15);
  g.add(boxes([[-2.6, 0.2, 0, 1.9, 0.4, 2.0, "#24407a"], [0, 0.6, 0, 1.9, 1.2, 2.0, "#2b4c8f"], [2.6, 1.0, 0, 1.9, 2.0, 2.0, "#3359a6"],
    [-2.6, 0.55, 0.2, 1.3, 0.3, 0.7, "#e9eef7"], [-3.15, 0.75, 0.2, 0.25, 0.25, 0.6, "#ffffff"]]));
  for (const [x, y] of [[-2.6, 0.41], [0, 1.21], [2.6, 2.01]]) { const e = new THREE.Mesh(new THREE.BoxGeometry(1.92, 0.03, 0.03), RIM); e.position.set(x, y, 1.0); g.add(e); }
  const base = { skin: "#f1c39d", hair: "#3b2a20", pants: "#26314d", fringe: [[-0.36, 0.18], [-0.18, 0.14], [0, 0.2], [0.18, 0.12], [0.36, 0.18]] };
  L.p = [Object.assign({}, base, { top: "#7c5cff", top2: "#6847ef" }), Object.assign({}, base, { top: "#2ecc71", top2: "#27b062", glasses: true }), Object.assign({}, base, { top: "#ff8a3d", top2: "#f2772a", bun: true, hair: "#4a2c1e" })].map((o) => person(o));
  L.p[0].root.position.set(-1.9, 0.72, 0.2); L.p[0].root.rotation.set(0, 0, Math.PI / 2); L.p[0].root.scale.setScalar(0.7);
  L.p[1].root.position.set(0, 1.2, 0.1); L.p[2].root.position.set(2.6, 2.0, 0.1);
  L.p.forEach((p) => g.add(p.root));
  const mag = boxes([[0, -0.68, 0.12, 0.05, 0.25, 0.05, "#5b4636"], [0, -0.42, 0.12, 0.26, 0.26, 0.04, "#d8f3ff"]]); L.p[1].armR.add(mag);
  L.prod = boxes([[0, 0, 0, 0.32, 0.42, 0.22, "#01ccf7"], [0, 0.05, 0.115, 0.22, 0.08, 0.01, "#ffffff"]]); L.p[2].torso.add(L.prod); L.prod.position.set(0, 0.32, 0.35);
  L.zz = label("Zzz", "#7c5cff", "#ffffff", 0.3); L.zz.position.set(-2.3, 1.55, 0.3); g.add(L.zz);
  L.lb = [["BELUM SADAR", "#7c5cff", -2.6, 0.95], ["CARI SOLUSI", "#2ecc71", 0, 3.05], ["KENAL PRODUK", "#ff8a3d", 2.6, 3.85]].map(([s, c, x, y]) => { const l = label(s, c, "#ffffff", 0.32); l.position.set(x, y, 1.1); g.add(l); return l; });
  L.hooks = LV_T.map(() => { const m = new THREE.Mesh(new THREE.PlaneGeometry(0.34, 0.45), new THREE.MeshBasicMaterial({ map: TX.card, toneMapped: false, side: THREE.DoubleSide })); m.visible = false; g.add(m); return m; });
  L.hg = LV_T.map(() => { const s = glow("#ff5c8a", 0.9, 0.9); s.visible = false; g.add(s); return s; });
}
function animL(t) {
  L.p.forEach((p, i) => { p.eyes.forEach((e) => (e.scale.y = i === 0 && t < LV_T[0] + 0.35 ? 0.12 : blinkAt(t, i)));
    const hit = U(t, LV_T[i] + 0.3, LV_T[i] + 0.5, "back"); p.setMouth(i === 0 ? (t < LV_T[0] + 0.35 ? "n" : "o") : hit > 0.5 ? (i === 2 ? "smile" : "o") : "n");
    p.head.rotation.set(0, 0.25 * Math.sin(t * 1.3 + i) , 0); });
  L.p[1].armR.rotation.set(-1.2 + 0.1 * Math.sin(t * 2), 0.3 * Math.sin(t * 1.6), -0.2);
  L.p[2].armL.rotation.set(-1.0, 0, 0.35); L.p[2].armR.rotation.set(-1.0, 0, -0.35);
  L.p[0].root.position.y = 0.72 + 0.25 * U(t, LV_T[0] + 0.35, LV_T[0] + 0.6, "back");
  setLabel(L.zz, (1 - U(t, LV_T[0] + 0.3, LV_T[0] + 0.45)) * (0.85 + 0.15 * Math.sin(t * 4))); L.zz.position.y = 1.55 + 0.08 * Math.sin(t * 3);
  const tgt = [[-2.6, 1.3, 0.6], [0, 2.4, 0.6], [2.6, 3.2, 0.6]];
  L.hooks.forEach((m, i) => { const u = U(t, LV_T[i] - 0.15, LV_T[i] + 0.35, "out"); m.visible = L.hg[i].visible = t > LV_T[i] - 0.15 && t < LV_T[i] + 0.9;
    m.position.set(-5 + (tgt[i][0] + 5) * u, 6 - (6 - tgt[i][1]) * u, 2.5 - (2.5 - tgt[i][2]) * u); m.rotation.set(0, (1 - u) * 6, 0); m.scale.setScalar(1 - 0.7 * U(t, LV_T[i] + 0.45, LV_T[i] + 0.9));
    L.hg[i].position.copy(m.position); });
  L.lb.forEach((l) => (l.visible = false));
}

/* ---------------------------------------------------------------- R: turntable with five formats */
const R = {};
const FMT_T = [35.7, 36.05, 36.8, 37.5, 38.3];
function buildR() {
  const g = mk("R"); g.add(island(5, 5)); clouds("R", 9, 17);
  R.tt = new THREE.Group(); R.tt.position.y = 0.0; g.add(R.tt);
  const disc = new THREE.Mesh(new THREE.CylinderGeometry(3.6, 3.6, 0.35, 48), new THREE.MeshStandardMaterial({ color: 0x24407a, roughness: 0.6 })); disc.position.y = 0.18; disc.receiveShadow = true; R.tt.add(disc);
  const ring = new THREE.Mesh(new THREE.TorusGeometry(3.6, 0.04, 6, 64), RIM); ring.rotation.x = Math.PI / 2; ring.position.y = 0.36; R.tt.add(ring);
  R.sets = []; const names = [["DEMO", "#22d3ff"], ["TESTIMONI", "#ffc531"], ["EDUKASI", "#2ecc71"], ["CERITA", "#ff8a3d"], ["TANPA WAJAH", "#ff5c8a"]];
  names.forEach(([n, c], i) => { const s = new THREE.Group(); const a = (i / 5) * Math.PI * 2; s.position.set(Math.sin(a) * 2.35, 0.36, Math.cos(a) * 2.35); s.rotation.y = a; R.tt.add(s);
    if (i === 0) { s.add(boxes([[0, 0.45, 0, 1.2, 0.08, 0.7, "#e9cfa8"], [0, 0.22, 0, 1.0, 0.44, 0.08, "#d8b98e"], [0, 0.51, 0.05, 0.7, 0.04, 0.45, "#aab6c8"]]));
      const lid = new THREE.Mesh(new THREE.PlaneGeometry(0.66, 0.42), new THREE.MeshBasicMaterial({ map: TX.screen, toneMapped: false })); lid.position.set(0, 0.76, -0.16); lid.rotation.x = -0.25; s.add(lid); }
    if (i === 1) { const p = person({ skin: "#e8b48f", hair: "#2a1e18", top: "#ffc531", top2: "#e8b22a", pants: "#26314d", fringe: [[-0.36, 0.16], [0, 0.2], [0.36, 0.16]] }); p.root.scale.setScalar(0.62); p.setMouth("smile"); s.add(p.root); s.userData.p = p;
      const st = label("★★★★★", "#ffc531", "#0a0d2c", 0.24); st.position.set(0, 1.9, 0.2); s.add(st); s.userData.st = st; }
    if (i === 2) { s.add(boxes([[-0.45, 0.6, -0.1, 0.05, 1.2, 0.05, "#8a6a4a"], [0.45, 0.6, -0.1, 0.05, 1.2, 0.05, "#8a6a4a"]]));
      const b = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 0.8), new THREE.MeshBasicMaterial({ map: TX.board, toneMapped: false })); b.position.set(0, 1.05, -0.05); s.add(b); }
    if (i === 3) { s.add(boxes([[-0.3, 0.12, 0, 0.6, 0.06, 0.8, "#fff6e0"], [0.3, 0.12, 0, 0.6, 0.06, 0.8, "#fff6e0"], [0, 0.07, 0, 1.25, 0.06, 0.85, "#c0392b"]]));
      const gl = glow("#ffb02e", 1.4, 1.0); gl.position.set(0, 0.5, 0); s.add(gl); s.add(boxes([[-0.3, 0.16, 0.1, 0.4, 0.01, 0.04, "#c9b48f"], [0.3, 0.16, 0.1, 0.4, 0.01, 0.04, "#c9b48f"], [-0.3, 0.16, -0.1, 0.35, 0.01, 0.04, "#c9b48f"]])); }
    if (i === 4) { const p = person({ skin: "#e8b48f", hair: "#2a1e18", top: "#ff5c8a", top2: "#e8457a", pants: "#26314d", fringe: [[0, 0.1]] }); p.root.scale.setScalar(0.62); s.add(p.root);
      p.head.add(boxes([[0, 0.48, 0, 0.98, 1.0, 0.98, "#c49a6c"], [-0.17, 0.5, 0.495, 0.12, 0.07, 0.01, "#3b2a20"], [0.17, 0.5, 0.495, 0.12, 0.07, 0.01, "#3b2a20"]]));
      p.eyes.forEach((e) => (e.visible = false)); p.setMouth("none"); p.armR.rotation.x = -1.1; p.armR.add(boxes([[0, -0.6, 0.18, 0.2, 0.34, 0.03, "#0a0d2c"]])); }
    const lb = label(n, c, "#0a0d2c", 0.34); lb.position.set(0, 2.0, 0.3); s.add(lb); s.userData.lb = lb; R.sets.push(s); });
}
function ttAngle(t) { // hold each set at the front, snap (0.22 s) to the next one on its word, spin-blur exit
  const st = (i) => -i * Math.PI * 2 / 5; const K = [[34.0, [0.5]], [FMT_T[0], [st(0)], "out"]];
  for (let i = 1; i < 5; i++) { const h = Math.max(K[K.length - 1][0] + 0.02, FMT_T[i] - 0.22); K.push([h, [st(i - 1)]], [FMT_T[i], [st(i)], "out"]); }
  return keys(t, K)[0] - 9 * Math.PI * EZ.in(cl((t - 38.85) / 0.6, 0, 1)); }
function animR(t) {
  R.tt.rotation.y = ttAngle(t);
  R.sets.forEach((s, i) => { s.userData.lb.visible = false; if (s.userData.st) s.userData.st.visible = false; if (s.userData.p) s.userData.p.eyes.forEach((e) => (e.scale.y = blinkAt(t, 0.4))); });
}

/* ---------------------------------------------------------------- D: five dominoes -> CTA button */
const D = {};
const DOM_T = [40.95, 41.95, 43.05, 43.45, 45.3], PRESS = 45.62;
function buildD() {
  const g = mk("D"); g.add(island(5, 2)); clouds("D", 9, 19);
  D.dom = TX.dom.map((tx, i) => { const piv = new THREE.Group(); piv.position.set(-3.1 + i * 0.95 + 0.15, 0, 0); g.add(piv);
    const m = new THREE.Mesh(new THREE.BoxGeometry(0.3, 2.2, 1.05), [MATW, MATW, MATW, MATW, new THREE.MeshStandardMaterial({ map: tx, roughness: 0.6 }), MATW]); m.position.set(-0.15, 1.1, 0); m.castShadow = true; piv.add(m);
    return piv; });
  g.add(boxes([[2.3, 0.15, 0, 1.6, 0.3, 1.6, "#1f3c62"], [2.3, 0.32, 0, 1.64, 0.04, 1.64, "#01ccf7"]]));
  D.btn = new THREE.Mesh(new THREE.CylinderGeometry(0.62, 0.66, 0.36, 32), new THREE.MeshStandardMaterial({ color: 0xff4d5e, emissive: 0xff2a44, emissiveIntensity: 0.6, roughness: 0.4 })); D.btn.position.set(2.3, 0.52, 0); g.add(D.btn);
  D.bl = label("CTA", "#ff4d5e", "#ffffff", 0.42); D.bl.position.set(2.3, 1.45, 0.3); g.add(D.bl);
  D.bg = glow("#ff4d5e", 3.5, 3.5); D.bg.position.set(2.3, 0.8, 0.2); g.add(D.bg);
}
const MATW = new THREE.MeshStandardMaterial({ color: 0xf4f7fc, roughness: 0.6 });
function animD(t) {
  const fin = U(t, PRESS - 0.25, PRESS, "in");
  D.dom.forEach((p, i) => { let a = 0; if (t > DOM_T[i]) a = -0.5 * U(t, DOM_T[i], DOM_T[i] + 0.28, "in"); if (i < 4 && t > DOM_T[i + 1]) a = -0.5 - 0.35 * U(t, DOM_T[i + 1], DOM_T[i + 1] + 0.2);
    p.rotation.z = a + (-1.5 - a) * fin * (i === 4 ? 1 : U(t, PRESS - 0.1, PRESS + 0.25)); });
  const pr = U(t, PRESS, PRESS + 0.08) * (1 - U(t, PRESS + 0.2, PRESS + 0.5));
  D.btn.scale.set(1, 1 - 0.5 * pr, 1); D.btn.material.emissiveIntensity = 0.6 + 3 * U(t, PRESS, PRESS + 0.1); D.bg.material.opacity = 0.3 + 0.7 * U(t, PRESS, PRESS + 0.1);
}

/* ---------------------------------------------------------------- A: the hard part (50 blank hooks) -> AI printer + three trays */
const A = {};
const PICK = 53.2;
function buildA() {
  const g = mk("A"); g.add(island(5, 3)); clouds("A", 9, 23);
  g.add(boxes([[-2.6, 0.9, 0.2, 1.6, 0.1, 0.9, "#e9cfa8"], [-3.3, 0.45, 0.2, 0.1, 0.9, 0.8, "#d8b98e"], [-1.9, 0.45, 0.2, 0.1, 0.9, 0.8, "#d8b98e"]]));
  A.w = person({ skin: "#f1c39d", hair: "#3b2a20", top: "#3567b5", top2: "#2c5598", pants: "#26314d", glasses: true, strings: true, fringe: [[-0.36, 0.2], [-0.18, 0.14], [0, 0.22], [0.18, 0.12], [0.36, 0.2]] });
  A.w.root.position.set(-2.6, 0, -0.45); g.add(A.w.root);
  A.stack = []; for (let i = 0; i < 50; i++) { const m = boxes([[0, 0, 0, 0.7, 0.028, 0.5, i % 2 ? "#ffffff" : "#eef3fb"]]); m.position.set(-1.25 + Math.sin(i * 1.7) * 0.04, 0.02 + i * 0.03, 0.3); m.visible = false; g.add(m); A.stack.push(m); }
  A.sweat = [0, 1, 2].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.09, 0.06), emi("#7fe3ff", 1.2)); m.visible = false; g.add(m); return m; });
  // printer + robot
  g.add(boxes([[0.9, 0.45, -0.2, 1.5, 0.9, 1.0, "#f3f6fb"], [0.9, 0.93, -0.2, 1.3, 0.06, 0.8, "#c3cfe2"], [0.9, 0.55, 0.31, 1.0, 0.08, 0.02, "#0a0d2c"], [0.4, 0.75, 0.31, 0.12, 0.12, 0.02, "#2ecc71"]]));
  A.pl = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.14, 0.02), emi("#2ecc71", 2)); A.pl.position.set(0.4, 0.75, 0.32); g.add(A.pl);
  A.bot = robot("#01ccf7", TX.robo); A.bot.root.position.set(2.2, 0.1, -0.5); A.bot.root.scale.setScalar(1.25); A.bot.root.rotation.y = -0.5; A.bot.card.visible = false; g.add(A.bot.root);
  A.brief = new THREE.Mesh(new THREE.PlaneGeometry(0.4, 0.53), new THREE.MeshBasicMaterial({ map: TX.brief, toneMapped: false, side: THREE.DoubleSide })); g.add(A.brief);
  A.tray = [-0.6, 0.9, 2.4].map((x, i) => { g.add(boxes([[x, 0.08, 1.6, 1.0, 0.16, 0.8, "#1f3c62"], [x, 0.17, 1.6, 1.04, 0.02, 0.84, ROLE[[0, 1, 2][i]]]])); return x; });
  A.tl = [["BELUM SADAR", "#7c5cff"], ["CARI SOLUSI", "#2ecc71"], ["KENAL PRODUK", "#ff8a3d"]].map(([s, c], i) => { const l = label(s, c, "#ffffff", 0.26); l.position.set(A.tray[i], 0.75, 2.1); g.add(l); return l; });
  A.cards = []; for (let i = 0; i < 30; i++) { const m = new THREE.Mesh(new THREE.PlaneGeometry(0.3, 0.4), new THREE.MeshBasicMaterial({ map: TX.card, toneMapped: false, side: THREE.DoubleSide })); m.visible = false; g.add(m); A.cards.push(m); }
  A.pick = new THREE.Mesh(new THREE.PlaneGeometry(0.42, 0.56), new THREE.MeshBasicMaterial({ map: TX.card, toneMapped: false, side: THREE.DoubleSide })); g.add(A.pick);
  A.pg = glow("#ffc531", 1.8, 2.2); g.add(A.pg);
  LOGO.a = logo3d("claude", window.LOGOS.claude.hex, 0.55); LOGO.a.position.set(0.9, 1.55, -0.2); g.add(LOGO.a);
}
function animA(t) {
  const w = A.w; w.eyes.forEach((e) => (e.scale.y = blinkAt(t, 0.3))); w.setMouth("sad");
  w.armR.rotation.set(-1.0 + 0.12 * Math.sin(t * 16), 0, -0.1); w.armL.rotation.set(-0.9, 0, 0.1); w.head.rotation.set(0.25, 0, 0.08 * Math.sin(t * 2));
  A.stack.forEach((m, i) => (m.visible = t > 46.35 + i * 0.04));
  A.sweat.forEach((m, i) => { const u = ((t - 46.4) * 1.1 + i / 3) % 1; m.visible = t > 46.4 && t < 49.5; m.position.set(-2.95 + i * 0.05, 2.15 - u * 0.6, -0.1); m.scale.setScalar(1 - u); });
  // robot arrives on "AI bantu", the brief goes in, cards stream into the trays
  const r = A.bot, arr = U(t, 49.2, 49.65, "back"); r.root.position.y = 0.1 + 4 * (1 - arr); r.root.visible = t > 48.9;
  r.eyeMat.emissiveIntensity = 2.2 * U(t, 49.6, 49.8); r.eg2.material.opacity = 0.35 * U(t, 49.6, 49.8); r.eyes.scale.y = blinkAt(t, 0.9);
  r.armL.rotation.set(-1.3 * U(t, 50.0, 50.3) * (1 - U(t, 50.7, 51.0)), 0, 0.2); r.armR.rotation.set(-0.3 * Math.sin(t * 3), 0, -0.1);
  const bi = U(t, 50.1, 50.6, "io"); A.brief.visible = t > 49.9 && t < 50.65; A.brief.position.set(2.0 - 1.1 * bi, 1.6 - 0.62 * bi, -0.15); A.brief.rotation.set(-Math.PI / 2 * bi, 0.4 * (1 - bi), 0);
  A.pl.material.emissiveIntensity = t > 50.6 && t < 52.8 ? (Math.floor(t * 8) % 2 ? 3 : 0.5) : 1.2;
  A.cards.forEach((m, i) => { const e = 50.85 + i * 0.06, u = U(t, e, e + 0.55, "out"); m.visible = t > e; if (!m.visible) return; const k = i % 3, x = A.tray[k];
    m.position.set(0.9 + (x - 0.9) * u, 0.6 + 1.0 * Math.sin(Math.PI * u) + (0.22 + Math.floor(i / 3) * 0.012 - 0.6) * u, 0.4 + 1.2 * u); m.rotation.set(-Math.PI / 2 * u, (1 - u) * 3, 0); });
  A.tl.forEach((l) => (l.visible = false));
  { const u = U(t, 49.75, 50.1, "back"); LOGO.a.visible = t > 49.75; LOGO.a.scale.setScalar(Math.max(0.001, u)); LOGO.a.rotation.y = t * 1.8; LOGO.a.position.y = 1.55 + 0.06 * Math.sin(t * 2.4); }
  const pk = U(t, PICK, PICK + 0.45, "back"); A.pick.visible = A.pg.visible = t > PICK;
  A.pick.position.set(0.9, 0.35 + 1.5 * pk, 1.6 + 0.3 * pk); A.pick.rotation.set(0, Math.sin(t * 2) * 0.3, 0); A.pg.position.copy(A.pick.position); A.pg.position.z -= 0.05; A.pg.material.opacity = 0.8 * pk;
}

/* ---------------------------------------------------------------- camera path (absolute), with cuts */
const C = []; const at = (w) => (v) => [v[0] + WP[w][0], v[1] + WP[w][1], v[2] + WP[w][2], v[3] + WP[w][0], v[4] + WP[w][1], v[5] + WP[w][2], v[6]];
const k = (w, t, v, e) => C.push([t, at(w)(v), e]);
const cut = (w, t, v) => C.push([t, at(w)(v), "lin"]);
// H — hook, full frame
k("H", 0, [0.7, 1.9, 5.6, -0.1, 1.35, 0.2, 42]); k("H", 1.55, [0.5, 1.75, 4.8, -0.05, 1.35, 0.4, 42], "sine");
k("H", 2.5, [1.6, 3.2, 7.4, 0, 2.2, 0, 50], "out"); k("H", 2.85, [0.3, 2.6, 5.4, 0, 2.6, 2.2, 42], "io"); k("H", 3.43, [0, 2.6, 2.62, 0, 2.6, 2.2, 40], "in");
// S — match cut on the ad face, zoom-out reveal, slicing, elevator exit
cut("S", 3.44, [0, 2.1, 1.05, 0, 2.1, 0, 40]); k("S", 4.35, [0, 5.2, 17, 0, 2.0, 0, 32], "io"); k("S", 5.6, [4.6, 4.2, 17.6, 0.3, 2.4, 0, 40], "io");
k("S", 7.3, [3.4, 4.0, 17.4, 0.3, 2.4, 0, 40], "sine"); k("S", 8.95, [3.0, 3.9, 17.0, 0.3, 2.4, 0, 40], "sine"); k("S", 9.3, [0, 2.6, 8.4, 0, 2.4, 0, 44], "io"); k("S", 9.5, [0, 2.5, 7.0, 0, 2.35, 0, 44], "sine");
C.push([9.98, [60, 4.4, -30 + 18.6, 60, 2.5, -30, 42], "in"]);
// T
k("T", 13.95, [0, 4.2, 17.8, 0, 2.5, 0, 42], "sine"); k("T", 14.48, [0, 4.4, 17.8, 0, 30, -12, 42], "expo");
// M — starts looking at the sky, tilts down
cut("M", 14.49, [0.3, 4.0, 13.6, 0.2, 30, -12, 42]); k("M", 15.1, [0.3, 3.9, 13.6, 0, 2.35, 0, 40], "io"); k("M", 16.3, [0, 3.2, 10.8, 0, 2.4, 0, 40], "sine");
k("M", 17.7, [0.2, 3.7, 14.2, 0.1, 2.3, 0, 42], "io"); k("M", 20.3, [0.1, 3.7, 13.8, 0.1, 2.3, 0, 42], "sine"); k("M", 21.1, [0, 2.6, 7.0, 0, 2.2, 0, 42], "in");
// P — after the jackpot burst
cut("P", 21.12, [0, 3.0, 4.5, 0, 1.5, -1, 40]); k("P", 22.5, [0, 6.8, 13.5, 0, 1.4, -2.8, 44], "io"); k("P", 23.4, [-3.4, 3.0, 5.0, -4.9, 1.45, -3, 40], "io");
k("P", 24.25, [-3.3, 3.0, 4.7, -4.9, 1.45, -3, 40], "sine"); k("P", 24.85, [0.1, 3.9, 1.4, 0, 3.2, -6.5, 40], "io"); k("P", 25.6, [0.1, 3.9, 1.2, 0, 3.2, -6.5, 40], "sine");
k("P", 26.2, [3.4, 3.0, 5.0, 4.9, 1.45, -3, 40], "io"); k("P", 27.3, [0, 6.6, 13, 0, 1.4, -2.8, 44], "io"); k("P", 27.61, [0, 6.4, 12.4, 0, 1.4, -2.8, 44], "sine");
// L — after the iris; 180° orbit at the end towards R
cut("L", 27.62, [0, 4.8, 18.2, 0, 2.0, 0, 42]); k("L", 28.9, [-2.7, 2.8, 8.6, -2.7, 1.5, 0, 40], "io"); k("L", 30.8, [0, 3.3, 7.8, 0, 2.35, 0, 40], "io");
k("L", 32.6, [2.6, 4.1, 8.4, 2.6, 3.15, 0, 40], "io"); k("L", 33.3, [0, 4.8, 18.2, 0, 2.0, 0, 42], "io");
for (let i = 1; i <= 16; i++) { const u = i / 16, a = Math.PI * EZ.io(u), r = 18.2; k("L", 33.3 + 0.95 * u, [Math.sin(a) * r * 0.9, 4.8 + 2.2 * Math.sin(a), Math.cos(a) * r, 0, 2.0 - 0.4 * u, 8 * u, 42], "lin"); }
k("R", 34.6, [0, 5.2, 17.0, 0, 0.8, 2.0, 40], "out"); k("R", 38.8, [0.2, 5.0, 16.4, 0, 0.8, 2.0, 40], "sine"); k("R", 39.44, [0.0, 4.4, 13.4, 0, 0.8, 2.0, 40], "in");
// D — after the spin-blur cut; track the dominoes
cut("D", 39.45, [-0.6, 4.2, 17.4, -0.35, 1.25, 0, 40]); k("D", 45.2, [-0.4, 4.0, 16.4, -0.35, 1.2, 0, 40], "sine"); k("D", 45.75, [0.6, 3.4, 13.2, 0.4, 1.1, 0, 40], "io"); k("D", 46.34, [0.7, 3.3, 12.6, 0.5, 1.1, 0, 40], "sine");
// A
cut("A", 46.35, [-2.0, 3.0, 7.8, -1.95, 1.55, 0, 40]); k("A", 48.8, [-1.9, 2.9, 7.4, -1.9, 1.55, 0, 40], "sine"); k("A", 49.7, [0.7, 3.3, 11.0, 0.7, 1.3, 0, 42], "io");
k("A", 51.0, [0.7, 3.5, 12.2, 0.7, 1.0, 0, 42], "io"); k("A", 53.0, [0.7, 3.4, 11.8, 0.7, 1.1, 0.4, 42], "sine"); k("A", 53.8, [0.7, 3.2, 10.8, 0.7, 1.3, 0.6, 42], "io"); k("A", 58.5, [0.7, 3.4, 11.6, 0.7, 1.2, 0.4, 42], "sine");
C.sort((a, b) => a[0] - b[0]);
window.VX = { C, WP };
scene.add(cam);

/* ---------------------------------------------------------------- render */
let ready = false; const LIFTAT = (t) => 230 * U(t, 3.45, 4.2);
const ANIM = { H: animH, S: animS, T: animT, M: animM, P: animP, L: animL, R: animR, D: animD, A: animA };
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  for (const kk in worlds) { const [a, b] = VIS[kk]; worlds[kk].visible = t >= a && t < b; if (worlds[kk].visible) ANIM[kk](t); }
  const v = keys(t, C), hx = Math.sin(t * 0.9) * 0.025, hy = Math.sin(t * 1.3 + 1) * 0.02;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.up.set(0, 1, 0); cam.lookAt(v[3], v[4], v[5]);
  const roll = 0.35 * Math.sin(Math.PI * cl((t - 38.85) / 0.6, 0, 1)) + 0.05 * Math.sin(Math.PI * cl((t - 45.6) / 0.6, 0, 1)); if (roll) cam.rotateZ(roll);
  if (!LOGO.ig) { LOGO.ig = logo3d("instagram", window.LOGOS.instagram.hex, 1); cam.add(LOGO.ig); }
  { const on = U(t, 53.95, 54.35, "back"), d = 3.0; LOGO.ig.visible = t > 53.95; cam.updateMatrixWorld();
    const v2 = new THREE.Vector3((540 / W) * 2 - 1, 1 - (420 / H) * 2, 0.5).unproject(cam).sub(cam.position).normalize().multiplyScalar(d).add(cam.position); cam.worldToLocal(v2);
    LOGO.ig.position.copy(v2); LOGO.ig.position.y += 0.03 * Math.sin(t * 3); LOGO.ig.rotation.set(0, Math.sin(t * 1.4) * 0.5 + (1 - on) * 5, 0); LOGO.ig.scale.setScalar(Math.max(0.001, on) * 0.2 * (1 + 0.12 * Math.max(0, Math.sin((t - 54.75) * 12)) * (t > 54.75 && t < 55.0 ? 1 : 0))); }
  stars.position.copy(cam.position);
  const tx = v[3], tz = v[5]; moon.position.set(tx - 6, 12, tz + 8); moon.target.position.set(tx, 0, tz - 1); warm.position.set(tx + 6, 4, tz + 7); warm.target.position.set(tx, 1, tz);
  renderer.render(scene, cam);
}
window.VX.render = render;
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  makeTextures(); buildH(); buildS(); buildT(); buildM(); buildP(); buildL(); buildR(); buildD(); buildA(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = PR;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
