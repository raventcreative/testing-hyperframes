/* R34 · 4 repo open-source: Claude jadi studio animasi — voxel night worlds (own assets), one absolute camera path.
   Deterministic: render(t) is a pure function of t ("hf-seek").
   Through-line object: ONE cyan cube (#01ccf7). It is the text cursor on the code monitor, jumps out of the screen and knocks the
   clips off the editing timeline, hops into crate 1 (portal), rides the smooth GSAP lane and falls off its end into the Blender
   island where it lands as the "default cube" and grows into the table, then the edit cursor's target in the shot strip.
   Transitions (all different): cursor knock + zoom-out reveal (H), portal dive into crate 1 (H->F), whip tilt to the sky (F->G),
   fall flight following the cube (G->B), dive into the camera lens (B->S), shot card flies into the lens + flash (S->CTA). */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { SVGLoader } from "three/addons/loaders/SVGLoader.js";
import { MAT, rnd, setSeed, boxes, emi, ctex, rr, cl, EZ, U, keys, glow, label, setLabel, FONT } from "./vxlib.js";

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
scene.fog = new THREE.Fog(0x0c1a44, 30, 80);
scene.add(new THREE.HemisphereLight(0x9fbaff, 0x0a1230, 0.8));
const moon = new THREE.DirectionalLight(0xc6dbff, 2.1); moon.castShadow = true; moon.shadow.mapSize.set(2048, 2048); moon.shadow.bias = -0.0004; moon.shadow.normalBias = 0.025;
Object.assign(moon.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10, near: 1, far: 45 }); scene.add(moon, moon.target);
const warm = new THREE.DirectionalLight(0xbfe9ff, 0.6); scene.add(warm, warm.target);
const cam = new THREE.PerspectiveCamera(40, W / H, 0.05, 160);

/* ---------------------------------------------------------------- stars */
const stars = new THREE.Group(); scene.add(stars);
{ setSeed(91); const N = 700, p = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { const u = rnd() * 2 - 1, a = rnd() * Math.PI * 2, r = 110, s = Math.sqrt(1 - u * u); p[i * 3] = r * s * Math.cos(a); p[i * 3 + 1] = r * u * 0.9 + 4; p[i * 3 + 2] = r * s * Math.sin(a); }
  const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(p, 3));
  stars.add(new THREE.Points(g, new THREE.PointsMaterial({ color: 0xcfe2ff, size: 2.2, sizeAttenuation: false, fog: false, transparent: true, opacity: 0.85 }))); }

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
const WP = { H: [0, 0, 0], F: [60, 0, 0], G: [120, 0, 0], B: [126, -24, 6], S: [200, 0, 0] };
const VIS = { H: [[-1, 9.17], [38.27, 99]], F: [[9.1, 19.2]], G: [[19.1, 26.45]], B: [[25.85, 30.93]], S: [[30.9, 38.3]] };
const worlds = {}; const mk = (k) => { const g = new THREE.Group(); g.position.set(...WP[k]); worlds[k] = g; scene.add(g); return g; };
function clouds(k, n, sd) { setSeed(sd); for (let i = 0; i < n; i++) { const x = (rnd() - 0.5) * 34, y = -6 + rnd() * 9, z = -18 + rnd() * 22;
  if (Math.hypot(x, z) < 8 && y > -4) continue; const L = [], q = 3 + Math.floor(rnd() * 3), sz = 0.8 + rnd() * 1.1;
  for (let j = 0; j < q; j++) L.push([(j - q / 2) * sz * 0.8, (rnd() - 0.3) * sz * 0.5, (rnd() - 0.5) * sz, sz * (1 + rnd()), sz * (0.55 + rnd() * 0.5), sz * (1 + rnd() * 0.8), j & 1 ? "#22386c" : "#1b2f60"]);
  const m = boxes(L, MAT, false); m.castShadow = m.receiveShadow = false; m.position.set(x, y, z); worlds[k].add(m); } }
/* 3D brand logos: Simple Icons CC0 paths -> SVGLoader -> ExtrudeGeometry with a small bevel */
function logo3d(name, color, size, depth = 3.2) {
  const Lg = window.LOGOS[name]; const data = new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="${Lg.path}"/></svg>`);
  const shapes = data.paths.flatMap((p) => SVGLoader.createShapes(p));
  const g = new THREE.ExtrudeGeometry(shapes, { depth, bevelEnabled: true, bevelThickness: 0.5, bevelSize: 0.32, bevelSegments: 2, curveSegments: 10 });
  g.translate(-12, -12, -depth / 2); g.rotateX(Math.PI); g.scale(size / 24, size / 24, size / 24);
  const c = new THREE.Color(color); const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.3, roughness: 0.35, metalness: 0.1 }));
  m.castShadow = true; const w = new THREE.Group(); w.add(m); w.visible = false; return w;
}
const popLogo = (o, t, a, b, base, spin = 1.6) => { const u = U(t, a, a + 0.4, "back") * (1 - U(t, b, b + 0.25, "in")); o.visible = t > a && t < b + 0.25;
  o.scale.setScalar(Math.max(0.001, u)); o.rotation.y = (1 - U(t, a, a + 0.5, "out")) * 5 + Math.sin(t * spin) * 0.45; o.position.y = base + 0.06 * Math.sin(t * 2.4); };
const popLabel = (l, t, a, b) => setLabel(l, EZ.back(cl((t - a) / 0.35, 0, 1)) * (1 - U(t, b, b + 0.2)));
/* live canvas textures (html-demo idea: the app window is View(t), redrawn from t alone) */
function live(w, h, draw) { const tex = ctex(w, h, () => {}); const c = tex.image, g = c.getContext("2d"); let last = null;
  return { tex, redraw(t) { const k = Math.round(t * 30); if (k === last) return; last = k; g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, w, h); draw(g, w, h, t); tex.needsUpdate = true; } }; }
const plane = (w, h, map, o = {}) => new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial(Object.assign({ map, toneMapped: false, transparent: true }, o)));
const MON = "#0a1644";
function monitor(g, x, y, z, ry, sw, sh, map) { // voxel monitor: bezel + stand + screen plane
  const m = new THREE.Group(); m.position.set(x, y, z); m.rotation.y = ry; g.add(m);
  m.add(boxes([[0, 0, -0.08, sw + 0.22, sh + 0.22, 0.14, "#1b2a55"], [0, -sh / 2 - 0.4, -0.2, 0.18, 0.8, 0.14, "#24345f"], [0, -y + 0.05, -0.2, 1.0, 0.1, 0.6, "#24345f"]]));
  const s = plane(sw, sh, map, { transparent: false }); s.position.z = 0.0; m.add(s);
  const rim = new THREE.Mesh(new THREE.BoxGeometry(sw + 0.26, 0.04, 0.02), RIM); rim.position.set(0, -sh / 2 - 0.12, 0); m.add(rim);
  return m;
}
const typed = (s, t, a, cps = 45) => s.slice(0, Math.max(0, Math.min(s.length, Math.floor((t - a) * cps))));
function codeView(g, w, h, lines, n, opts = {}) { // dark editor window, brand colours, n = chars visible
  g.fillStyle = "#081233"; g.fillRect(0, 0, w, h); g.fillStyle = "#0e1d4d"; g.fillRect(0, 0, w, 64);
  [0, 1, 2].forEach((i) => { g.fillStyle = i ? "rgba(255,255,255,.35)" : CY; g.beginPath(); g.arc(36 + i * 34, 32, 10, 0, 7); g.fill(); });
  g.fillStyle = "#cfe6ff"; g.font = `700 30px ${FONT}`; g.textAlign = "left"; g.fillText(opts.file || "index.html", 150, 43);
  g.font = `700 ${opts.px || 40}px ui-monospace, Menlo, monospace`; let left = n, cx = 0, cy = 0; const lh = opts.lh || 60, x0 = 90, y0 = 130;
  lines.forEach((ln, i) => { if (left <= 0 && i > 0) return; const s = ln.slice(0, Math.max(0, left)); left -= ln.length + 1;
    g.fillStyle = "rgba(160,190,240,.45)"; g.textAlign = "right"; g.font = `700 26px ${FONT}`; g.fillText(String(i + 1), 60, y0 + i * lh); g.textAlign = "left";
    g.font = `700 ${opts.px || 40}px ui-monospace, Menlo, monospace`;
    let x = x0; for (const part of s.split(/(<\/?[a-z0-9]+|>|"[^"]*"?|\{|\})/i)) { if (!part) continue;
      g.fillStyle = /^<|^>$/.test(part) ? CY : /^"/.test(part) ? "#9fe8ff" : /^[{}]$/.test(part) ? "#7fe8ff" : "#ffffff"; g.fillText(part, x, y0 + i * lh); x += g.measureText(part).width; }
    cx = x; cy = y0 + i * lh; });
  return [cx, cy];
}

/* ---------------------------------------------------------------- H: code studio hub (hook + 4 crates + CTA) */
const Hh = {};
const CODE_H = ['<div class="reel">', '  <h1>Dibikin pakai kode</h1>', '  <div id="maskot"></div>', '</div>', "<script>", '  gsap.to("#maskot", { y: -40 })', "</script>"];
const REPOS = [["1", ["HyperFrames"]], ["2", ["GSAP skills"]], ["3", ["Blender MCP"]], ["4", ["Video", "Shotcraft"]]];
const CRX = [-2.625, -0.875, 0.875, 2.625], CRZ = 2.1;
function buildH() {
  const g = mk("H"); g.add(island(5, 4)); clouds("H", 9, 3);
  Hh.code = live(1024, 640, (c, w, h, t) => {
    if (t > 5.0) { c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.strokeStyle = "rgba(1,204,247,.16)"; c.lineWidth = 3; for (let x = 0; x <= w; x += 64) { c.beginPath(); c.moveTo(x, 0); c.lineTo(x, h); c.stroke(); }
      for (let y = 0; y <= h; y += 64) { c.beginPath(); c.moveTo(0, y); c.lineTo(w, y); c.stroke(); } return; }
    const n = Math.floor(Math.max(0, t - 0.15) * 52); c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.globalAlpha = Math.max(0.001, 1 - cl((t - 3.7) / 0.2, 0, 1)); const [x, y] = codeView(c, w, h, CODE_H, n, { px: 42, lh: 66 }); c.globalAlpha = 1;
    if (t < 4.12 && (Math.floor(t * 3) % 2 === 0 || t < 3.3 || t > 3.7)) { c.fillStyle = CY; c.fillRect(x + 4, y - 36, 22, 44); } });
  Hh.mon = monitor(g, 0, 2.0, -1.2, 0, 3.3, 2.06, Hh.code.tex);
  // the "editing app" timeline board (NLE) that gets knocked over
  Hh.nle = new THREE.Group(); Hh.nle.position.set(2.9, 0, -0.2); Hh.nle.rotation.y = -0.5; g.add(Hh.nle);
  Hh.nle.add(boxes([[0, 0.55, 0, 0.12, 1.1, 0.12, "#24345f"], [0, 1.45, 0, 2.3, 1.2, 0.1, "#0e1a3e"], [0, 1.45, 0.055, 2.18, 1.08, 0.01, "#16265a"],
    [-0.98, 1.45, 0.07, 0.04, 1.0, 0.01, "#ffffff"]]));
  setSeed(5); Hh.clips = [];
  const CC = ["#7c5cff", "#2ecc71", "#ff8a3d", "#22d3ff", "#ff5c8a"];
  for (let r = 0; r < 3; r++) { let x = -0.95; while (x < 0.95) { const w = Math.min(0.95 - x, 0.25 + rnd() * 0.45); if (w < 0.12) break;
    const m = boxes([[0, 0, 0, w - 0.04, 0.24, 0.06, CC[(r * 2 + Hh.clips.length) % 5]]]); m.userData = { p: new THREE.Vector3(x + w / 2, 1.82 - r * 0.34, 0.1), v: new THREE.Vector3((rnd() - 0.3) * 2.2, 1 + rnd() * 2.2, 1.2 + rnd() * 1.6), s: rnd() * 6 };
    Hh.nle.add(m); Hh.clips.push(m); x += w; } }
  // 4 repo crates
  Hh.crates = REPOS.map(([n, name], i) => { const c = new THREE.Group(); c.position.set(CRX[i], 0, CRZ); g.add(c);
    c.add(boxes([[0, 0.55, 0, 1.5, 1.1, 1.0, "#14275a"], [0, 1.12, 0, 1.56, 0.06, 1.06, "#1d3a7a"]]));
    const tx = ctex(600, 432, (q, w, h) => { q.fillStyle = "#0c1a48"; q.fillRect(0, 0, w, h); q.strokeStyle = CY; q.lineWidth = 12; q.strokeRect(6, 6, w - 12, h - 12);
      q.fillStyle = CY; q.textAlign = "center"; q.font = `700 150px ${FONT}`; q.fillText(n, w / 2, name.length > 1 ? 160 : 190);
      q.fillStyle = "#ffffff"; q.font = `700 86px ${FONT}`; name.forEach((l, k) => q.fillText(l, w / 2, (name.length > 1 ? 268 : 320) + k * 92)); });
    const f = plane(1.44, 1.04, tx, { transparent: false }); f.position.set(0, 0.55, 0.505); c.add(f);
    const topL = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.03, 0.9), emi(CY, 0)); topL.position.y = 1.16; c.add(topL);
    const gl = glow("#3fdcff", 1.8, 1.0); gl.position.set(0, 1.35, 0); gl.material.opacity = 0; c.add(gl);
    return { c, f, topL, gl }; });
  // little icons that pop out of the crates on "studio animasi"
  const ic = [];
  { const a = new THREE.Group(); a.add(boxes([[0, 0, 0, 0.62, 0.42, 0.05, "#ffffff"], [0, 0, 0.03, 0.5, 0.3, 0.01, "#0c1a48"], [-0.22, 0, 0.04, 0.05, 0.42, 0.01, CY], [0.22, 0, 0.04, 0.05, 0.42, 0.01, CY]])); ic.push(a); }
  { const a = new THREE.Group(); const L = []; for (let i = 0; i <= 8; i++) { const u = i / 8, y = 1 - Math.pow(1 - u, 3); L.push([-0.32 + 0.64 * u, -0.22 + 0.44 * y, 0, 0.09, 0.09, 0.09, i === 8 ? CY : "#ffffff"]); } a.add(boxes(L)); ic.push(a); }
  { const a = new THREE.Group(); a.add(boxes([[0, 0, 0, 0.4, 0.4, 0.4, "#c3cfe2"]])); const e = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(0.42, 0.42, 0.42)), new THREE.LineBasicMaterial({ color: 0xe87d0d })); a.add(e); ic.push(a); }
  { const a = new THREE.Group(); a.add(boxes([[0, 0, 0, 0.46, 0.32, 0.3, "#1b2238"], [0, 0, 0.22, 0.2, 0.2, 0.16, "#3a4560"], [0, 0.22, -0.05, 0.16, 0.12, 0.16, "#2a3350"]]));
    const l = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.12, 0.02), emi(CY, 2)); l.position.z = 0.31; a.add(l); ic.push(a); }
  Hh.icons = ic.map((a, i) => { a.position.set(CRX[i], 1.6, CRZ); a.visible = false; g.add(a); return a; });
  // logos (Simple Icons CC0, extruded)
  Hh.gh = logo3d("github", "#ffffff", 1.1); Hh.gh.position.set(0, 2.45, 1.0); g.add(Hh.gh);
  Hh.cl = logo3d("claude", window.LOGOS.claude.hex, 1.15); Hh.cl.position.set(0, 2.45, 1.0); g.add(Hh.cl);
  Hh.orb = [["claude", window.LOGOS.claude.hex], ["gsap", window.LOGOS.gsap.hex], ["blender", window.LOGOS.blender.hex], ["html5", window.LOGOS.html5.hex]].map(([n, c]) => { const o = logo3d(n, c, 0.62); g.add(o); return o; });
  Hh.ghC = logo3d("github", "#ffffff", 0.9); g.add(Hh.ghC);
}
const CUBE = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.34, 0.34), emi(CY, 1.5)); CUBE.castShadow = true; scene.add(CUBE);
const CUBEG = glow("#3fdcff", 1.3, 1.3); scene.add(CUBEG);
const _v = new THREE.Vector3();
function cubeAt(w, x, y, z, s = 1, rx = 0, ry = 0) { CUBE.visible = CUBEG.visible = true; CUBE.position.set(x + WP[w][0], y + WP[w][1], z + WP[w][2]); CUBE.scale.setScalar(s); CUBE.rotation.set(rx, ry, 0);
  CUBEG.position.copy(CUBE.position); CUBEG.scale.set(1.3 * s, 1.3 * s, 1); }
const bez = (a, b, c, u) => a * (1 - u) * (1 - u) + 2 * b * u * (1 - u) + c * u * u;
function animH(t) {
  Hh.code.redraw(t);
  const cta = t > 30;
  // NLE clips: knocked off by the cursor cube at 4.45; the board tips over and sinks
  const hit = 4.45;
  Hh.clips.forEach((m) => { const d = m.userData, k = Math.max(0, t - hit - d.s * 0.01);
    m.visible = !cta && k < 1.6; m.position.set(d.p.x + d.v.x * k * 0.5, d.p.y + d.v.y * k * 0.6 - 4.9 * k * k * 0.6, d.p.z + d.v.z * k * 0.5); m.rotation.set(k * d.s, k * 2, k * d.s * 0.5); });
  Hh.nle.rotation.x = -1.5 * U(t, hit + 0.3, hit + 1.0, "in"); Hh.nle.position.y = -1.5 * U(t, hit + 0.9, hit + 1.4, "in"); Hh.nle.visible = !cta && t < hit + 1.4;
  // crates rise on "Empat repo"; at the CTA they sink so the comment card has room
  Hh.crates.forEach((o, i) => { const a = 5.55 + i * 0.12, u = cta ? 0 : U(t, a, a + 0.5, "back"); o.c.position.y = -1.4 * (1 - u); o.c.visible = t > a - 0.05 && u > 0.01;
    const lit = cta ? 0 : U(t, 7.66 + i * 0.14, 7.9 + i * 0.14) * (1 - U(t, 8.6, 8.9)) + (i === 0 ? U(t, 8.6, 8.9) : 0);
    o.topL.material.emissiveIntensity = 2.2 * lit; o.gl.material.opacity = 0.55 * lit; });
  Hh.icons.forEach((a, i) => { const s = 7.66 + i * 0.14, u = cta ? 0 : U(t, s, s + 0.35, "back") * (1 - U(t, 8.4, 8.6)); a.visible = u > 0.01;
    a.scale.setScalar(Math.max(0.001, u)); a.position.y = 1.25 + 0.5 * u + 0.04 * Math.sin(t * 3 + i); a.rotation.y = Math.sin(t * 1.5 + i) * 0.5; });
  popLogo(Hh.gh, t, 5.82, 6.85, 2.45); popLogo(Hh.cl, t, 7.02, 8.45, 2.45);
  if (!cta) Hh.gh.visible = Hh.gh.visible && t < 7.1;
  // CTA: the four logos orbit the GitHub mark
  Hh.orb.forEach((o, i) => { o.visible = cta && t > 38.3; const u = U(t, 38.5 + i * 0.1, 38.95 + i * 0.1, "back"), a = t * 0.9 + i * Math.PI / 2;
    o.position.set(Math.cos(a) * 2.4, 3.3 + 0.15 * Math.sin(a * 2), 1.0 + Math.sin(a) * 1.0); o.scale.setScalar(Math.max(0.001, u)); o.rotation.y = -a + Math.PI / 2; });
  Hh.ghC.visible = cta && t > 38.3; Hh.ghC.position.set(0, 3.3, 1.0); Hh.ghC.scale.setScalar(Math.max(0.001, U(t, 38.4, 38.8, "back"))); Hh.ghC.rotation.y = t * 1.2;
  // through-line cube: the code cursor jumps out of the screen, knocks the clips, lands on crate 2, hops into crate 1
  if (t < 9.17 && !cta) {
    const top = 1.32;
    if (t < 4.12) { CUBE.visible = CUBEG.visible = false; }
    else if (t < hit) { const u = U(t, 4.12, hit, "in"); cubeAt("H", bez(0.9, 1.9, 2.75, u), bez(1.45, 2.6, 1.75, u), bez(-1.0, 0.4, 0.0, u), 0.3 + 0.7 * U(t, 4.12, 4.25), u * 4, u * 3); }
    else if (t < 5.75) { const u = U(t, hit, 5.75, "out"); cubeAt("H", bez(2.75, 1.0, CRX[1], u), bez(1.75, 3.2, top, u), bez(0.0, 1.6, CRZ, u), 1, 4 + u * 3, 3); }
    else if (t < 8.45) { const k = t - 5.75, sq = Math.exp(-k * 6) * Math.sin(k * 30) * 0.15; cubeAt("H", CRX[1], top + 0.06 * Math.abs(Math.sin(k * 3.2)) * (k > 0.6 ? 1 : 0), CRZ, 1 + sq, 0, t * 0.6); }
    else { const u = U(t, 8.45, 8.85, "io"); cubeAt("H", bez(CRX[1], -1.75, CRX[0], u), bez(top, 2.4, 0.6, u), bez(CRZ, CRZ + 0.4, CRZ + 0.62, u), 1 - 0.3 * u, 0, t * 0.6 + u * 3);
      if (t > 8.85) CUBE.scale.setScalar(Math.max(0.001, 0.7 * (1 - U(t, 8.85, 9.05)))); }
  }
}

/* ---------------------------------------------------------------- F: HyperFrames — README facts, HTML -> render -> video */
const F = {};
const CODE_F = ['<section class="scene">', '  <h1>Studio AI</h1>', '  <div class="maskot"></div>', "</section>"];
const MONF = [-0.6, 1.95, -1.0], PHF = [2.4, 1.55, -0.3];
function buildF() {
  const g = mk("F"); g.add(island(5, 4)); clouds("F", 9, 11);
  F.scr = live(1024, 640, (c, w, h, t) => {
    if (t < 12.85) { // README card: verified facts only (stars on 21 Nov 2026, licence, tagline)
      c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.globalAlpha = cl((t - 9.85) / 0.25, 0, 1); c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 76); c.fillStyle = "#cfe6ff"; c.font = `700 40px ${FONT}`; c.fillText("github.com/heygen-com/hyperframes", 36, 52);
      c.fillStyle = "#ffffff"; c.font = `700 104px ${FONT}`; c.fillText("HyperFrames", 56, 220); c.fillStyle = "#9fdcff"; c.font = `400 54px ${FONT}`; c.fillText("Write HTML. Render video.", 60, 300);
      const n = 87.5 * EZ.out(cl((t - 10.5) / 1.9, 0, 1)); c.fillStyle = CY; rr(c, 56, 370, 470, 130, 30); c.fill();
      c.fillStyle = "#0a0d2c"; c.font = `700 76px ${FONT}`; c.fillText("★ " + n.toFixed(1).replace(".", ",") + " rb", 88, 462);
      c.strokeStyle = CY; c.lineWidth = 7; rr(c, 560, 370, 400, 130, 30); c.stroke(); c.fillStyle = "#ffffff"; c.font = `700 58px ${FONT}`; c.fillText("Apache-2.0", 596, 456);
      c.fillStyle = "#9fdcff"; c.font = `400 40px ${FONT}`; c.fillText("bintang GitHub · 21 Nov 2026", 60, 580); c.globalAlpha = 1; return; }
    const n = Math.floor(Math.max(0, t - 12.95) * 48); const [x, y] = codeView(c, w, h, CODE_F, n, { px: 46, lh: 72 });
    if (t < 14.45) { if (Math.floor(t * 3) % 2 === 0) { c.fillStyle = CY; c.fillRect(x + 4, y - 38, 24, 46); } return; }
    const p = EZ.io(cl((t - 14.55) / 0.7, 0, 1));
    if (p >= 1) { c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.fillStyle = CY; c.beginPath(); c.arc(w / 2, 320, 170, 0, 7); c.fill(); c.strokeStyle = "#0a0d2c"; c.lineWidth = 26; c.lineCap = "round";
      c.lineWidth = 34; c.beginPath(); c.moveTo(w / 2 - 78, 320); c.lineTo(w / 2 - 18, 382); c.lineTo(w / 2 + 88, 255); c.stroke(); return; }
    c.fillStyle = "#0e1d4d"; rr(c, 50, 420, w - 100, 170, 26); c.fill();
    c.fillStyle = "#ffffff"; c.font = `700 66px ${FONT}`; c.fillText(p < 1 ? "Rendering… " + Math.round(p * 100) + "%" : "✓ video.mp4", 90, 500);
    c.fillStyle = "rgba(255,255,255,.18)"; rr(c, 90, 528, w - 180, 32, 16); c.fill(); c.fillStyle = CY; rr(c, 90, 528, Math.max(32, (w - 180) * p), 32, 16); c.fill(); });
  F.mon = monitor(g, MONF[0], MONF[1], MONF[2], 0.12, 3.1, 1.94, F.scr.tex);
  // phone: plays the rendered video = a still of this very reel
  F.ph = live(540, 960, (c, w, h, t) => { c.fillStyle = "#07102e"; c.fillRect(0, 0, w, h); c.textAlign = "center";
    if (t < 15.55) { c.strokeStyle = "rgba(1,204,247,.7)"; c.lineWidth = 12; c.beginPath(); c.arc(w / 2, h / 2 - 40, 80, t * 5, t * 5 + 4.2); c.stroke(); c.fillStyle = "#9fdcff"; c.font = `700 60px ${FONT}`; c.fillText("video.mp4", w / 2, h / 2 + 140); return; }
    const gr = c.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, "#0a1a4a"); gr.addColorStop(1, "#13285a"); c.fillStyle = gr; c.fillRect(0, 0, w, h);
    c.fillStyle = "#ffffff"; c.font = `700 46px ${FONT}`; c.textAlign = "left"; c.fillText("AI PRENEUR", 36, 84);
    c.fillStyle = "#1d3266"; c.fillRect(60, 300, 420, 60); c.fillStyle = CY; c.fillRect(60, 356, 420, 6);
    for (let i = 0; i < 4; i++) { c.fillStyle = "#14275a"; c.fillRect(74 + i * 102, 220, 86, 80); c.fillStyle = CY; c.font = `700 56px ${FONT}`; c.textAlign = "center"; c.fillText(String(i + 1), 117 + i * 102, 282); }
    c.fillStyle = "#f1c39d"; c.beginPath(); c.arc(170, 770, 120, 0, 7); c.fill(); c.fillStyle = "#2a2a33"; c.beginPath(); c.arc(170, 700, 112, Math.PI, 0); c.fill(); c.fillStyle = "#1b2a55"; c.fillRect(50, 880, 240, 80);
    c.fillStyle = "#e9eef7"; rr(c, 360, 700, 130, 160, 34); c.fill(); c.fillStyle = "#0b1640"; rr(c, 376, 726, 98, 60, 14); c.fill();
    c.fillStyle = "rgba(10,13,44,.88)"; rr(c, 40, 440, w - 80, 120, 24); c.fill(); c.fillStyle = "#ffffff"; c.font = `700 66px ${FONT}`; c.textAlign = "center";
    c.fillText(t < 16.55 ? "pakai kode" : "reel ini ✓", w / 2, 523);
    const p = cl((t - 15.6) / 3.4, 0, 1); c.fillStyle = "rgba(255,255,255,.25)"; c.fillRect(30, h - 44, w - 60, 12); c.fillStyle = CY; c.fillRect(30, h - 44, (w - 60) * p, 12); c.textAlign = "left"; });
  F.phone = new THREE.Group(); F.phone.position.set(...PHF); F.phone.rotation.y = -0.4; g.add(F.phone);
  F.phone.add(boxes([[0, 0, -0.06, 1.12, 1.92, 0.12, "#e9eef7"], [0, -1.1, -0.1, 0.3, 0.3, 0.1, "#24345f"], [0, -PHF[1] + 0.05, -0.1, 0.8, 0.1, 0.5, "#24345f"]]));
  const ps = plane(1.0, 1.78, F.ph.tex, { transparent: false }); ps.position.z = 0.005; F.phone.add(ps);
  const ft = ctex(256, 160, (c, w, h) => { c.fillStyle = "#ffffff"; c.fillRect(0, 0, w, h); c.fillStyle = "#0c1a48"; c.fillRect(22, 14, w - 44, h - 28); c.fillStyle = CY; c.fillRect(36, 30, 80, 14); c.fillRect(36, 54, 130, 10);
    for (let i = 0; i < 6; i++) { c.fillStyle = "#0c1a48"; c.fillRect(4, 10 + i * 25, 12, 14); c.fillRect(w - 16, 10 + i * 25, 12, 14); } });
  F.frames = []; for (let i = 0; i < 8; i++) { const m = plane(0.5, 0.31, ft, { side: THREE.DoubleSide }); m.visible = false; g.add(m); F.frames.push(m); }
  F.cl = logo3d("claude", window.LOGOS.claude.hex, 0.5); F.cl.position.set(0.15, 0, -0.75); g.add(F.cl);
  F.html = logo3d("html5", window.LOGOS.html5.hex, 0.5); F.html.position.set(0.68, 0, -0.75); g.add(F.html);
}
function animF(t) {
  F.scr.redraw(t); F.ph.redraw(t);
  popLogo(F.cl, t, 12.95, 14.1, 1.38, 2); popLogo(F.html, t, 13.42, 14.1, 1.38, 2);
  F.frames.forEach((m, i) => { const s = 14.85 + i * 0.12, u = U(t, s, s + 0.55, "io"); m.visible = t > s && t < s + 0.56;
    m.position.set(bez(MONF[0] + 0.6, 1.0, PHF[0], u), bez(1.9, 3.0, PHF[1] + 0.2, u), bez(-0.8, 0.4, PHF[2] + 0.1, u)); m.rotation.set(0, -0.4 * u + 0.3, Math.sin(u * 6) * 0.2); m.scale.setScalar(1 - 0.5 * u); });
  // through-line cube = the render key: comes out of the crate portal, hops onto the monitor stand, then to the phone
  if (t > 9.17 && t < 19.2) {
    const cx = MONF[0] + 1.2, cy = 3.25, cz = MONF[2] + 0.15;
    if (t < 14.45) cubeAt("F", cx, cy + 0.05 * Math.abs(Math.sin(t * 3.2)), cz, 1, 0, t * 0.6);
    else if (t < 16.0) { const u = U(t, 14.45, 15.9, "io"); cubeAt("F", bez(cx, 1.6, PHF[0] - 0.9, u), bez(cy, 3.4, 0.17, u), bez(cz, 0.6, PHF[2] + 0.5, u), 1, 0, u * 4); }
    else cubeAt("F", PHF[0] - 0.9, 0.17 + 0.05 * Math.abs(Math.sin(t * 3.4)), PHF[2] + 0.5, 1, 0, t * 0.6);
  }
}

/* ---------------------------------------------------------------- G: GSAP skills — logo, easing board, two lanes */
const G = {};
const ez3 = (x) => 1 - Math.pow(1 - cl(x, 0, 1), 3);
const RACE = 24.45, RACE1 = 25.6, X0 = -1.4, X1 = 2.6;
function buildG() {
  const g = mk("G"); g.add(island(5, 4)); clouds("G", 9, 17);
  G.bd = live(1024, 672, (c, w, h, t) => { c.fillStyle = "#081233"; c.fillRect(0, 0, w, h); c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 84); c.globalAlpha = 1 - cl((t - 24.1) / 0.15, 0, 1); if (c.globalAlpha <= 0) { c.globalAlpha = 1; return; }
    c.fillStyle = "#cfe6ff"; c.font = `700 50px ${FONT}`; c.fillText("ease: \"power3.out\"", 36, 60);
    const X0b = 90, Y0 = 560, SW = 470, SH = 380; c.strokeStyle = "rgba(160,190,240,.5)"; c.lineWidth = 5; c.beginPath(); c.moveTo(X0b, Y0 - SH - 10); c.lineTo(X0b, Y0); c.lineTo(X0b + SW + 10, Y0); c.stroke();
    c.setLineDash([12, 14]); c.beginPath(); c.moveTo(X0b, Y0); c.lineTo(X0b + SW, Y0 - SH); c.stroke(); c.setLineDash([]);
    const p = cl((t - 23.1) / 0.9, 0, 1); c.strokeStyle = CY; c.lineWidth = 12; c.lineCap = "round"; c.beginPath();
    for (let i = 0; i <= 60 * p; i++) { const u = i / 60, X = X0b + SW * u, Y = Y0 - SH * ez3(u); i ? c.lineTo(X, Y) : c.moveTo(X, Y); } c.stroke();
    if (p > 0) { const X = X0b + SW * p, Y = Y0 - SH * ez3(p); c.fillStyle = "#ffffff"; c.beginPath(); c.arc(X, Y, 18, 0, 7); c.fill(); }
    c.fillStyle = "#9fdcff"; c.font = `700 52px ${FONT}`; c.fillText("easing", X0b + 20, Y0 + 70);
    c.fillStyle = "#ffffff"; c.font = `700 52px ${FONT}`; c.fillText("timeline", 640, 160);
    [["judul", 0], ["maskot", 0.16], ["CTA", 0.32]].forEach(([s, d], i) => { const u = ez3((t - 23.95 - d) / 0.45), y = 200 + i * 120; c.fillStyle = "rgba(255,255,255,.12)"; rr(c, 640, y, 340, 86, 20); c.fill();
      if (u > 0) { c.fillStyle = i === 2 ? CY : "#3f7fd6"; rr(c, 640 + 40 * i, y, Math.max(40, (300 - 40 * i) * u), 86, 20); c.fill(); c.fillStyle = i === 2 ? "#0a0d2c" : "#ffffff"; c.font = `700 46px ${FONT}`; c.fillText(s, 660 + 40 * i, y + 58); } }); c.globalAlpha = 1;
  });
  G.board = new THREE.Group(); G.board.position.set(0, 2.05, -1.5); g.add(G.board);
  G.board.add(boxes([[0, 0, -0.08, 3.64, 2.42, 0.14, "#1b2a55"], [-1.4, -1.55, -0.1, 0.14, 1.0, 0.14, "#24345f"], [1.4, -1.55, -0.1, 0.14, 1.0, 0.14, "#24345f"]]));
  G.board.add(plane(3.5, 2.3, G.bd.tex, { transparent: false }));
  G.lane = [0.9, 2.6].map((z, i) => { g.add(boxes([[0.6, 0.06, z, 5.4, 0.12, 0.5, "#24407a"], [0.6, 0.125, z, 5.4, 0.01, 0.06, i ? CY : "#7f95c8"]]));
    const tx = ctex(600, 140, (c, w, h) => { c.fillStyle = i ? CY : "#3a4e86"; rr(c, 4, 4, w - 8, h - 8, 34); c.fill(); c.fillStyle = i ? "#0a0d2c" : "#ffffff"; c.font = `700 74px ${FONT}`; c.textAlign = "center"; c.fillText(i ? "DENGAN SKILL" : "TANPA SKILL", w / 2, 96); });
    const p = plane(1.7, 0.4, tx); p.position.set(-1.25, 0.62, z - 0.05); g.add(p); return { z, p }; });
  G.grey = boxes([[0, 0, 0, 0.34, 0.34, 0.34, "#b9c6dc"]]); g.add(G.grey);
  G.logo = logo3d("gsap", window.LOGOS.gsap.hex, 1.6); G.logo.position.set(0, 0, 0.2); g.add(G.logo);
  G.lab = label("greensock/gsap-skills", "", "#fff", 0.34); G.lab.position.set(0, 0.62, 0.6); g.add(G.lab);
}
function animG(t) {
  G.bd.redraw(t);
  popLogo(G.logo, t, 19.74, 22.0, 1.75, 1.8);
  popLabel(G.lab, t, 20.35, 22.0);
  const br = U(t, 22.2, 22.65, "out") * (1 - U(t, 24.3, 24.65, "in")); G.board.position.y = 2.05 - 3.6 * (1 - br); G.board.visible = t > 22.25 && t < 24.6;
  G.lane.forEach((l) => (l.p.visible = t > 24.0));
  // lane A: stepped ("patah-patah"); lane B: the through-line cube on power3.out = the board's curve function
  const c = cl((t - RACE) / (RACE1 - RACE), 0, 1); G.grey.visible = t > 24.0;
  G.grey.position.set(X0 + (X1 - X0) * Math.floor(c * 6) / 6, 0.3, 0.9);
  if (t > 19.1 && t < 26.5) {
    if (t < 24.0) { CUBE.visible = CUBEG.visible = false; }
    else if (t < RACE1) cubeAt("G", X0 + (X1 - X0) * ez3(c), 0.3, 2.6, U(t, 24.0, 24.3, "back") + 0.001, 0, 0);
    else { const u = t - RACE1; cubeAt("G", X1 + 3.2 * u, 0.3 + 1.2 * u - 9 * Math.max(0, u - 0.12) ** 2, 2.6 + 1.0 * u, 1, -u * 4, u * 3); }
  }
}

/* ---------------------------------------------------------------- B: Blender MCP — default cube, prompt, Claude builds the scene */
const B = {};
const PROMPT = "Buat scene 3D: meja, lampu, tanaman, kamera";
const BCAM = [1.55, 0, 1.3], BCRY = Math.atan2(-1.55, -1.3);
function buildB() {
  const g = mk("B"); g.add(island(4, 3, "#2f3650", "#293046")); clouds("B", 7, 29);
  B.pr = live(1024, 300, (c, w, h, t) => { c.fillStyle = "#ffffff"; rr(c, 6, 6, w - 12, h - 12, 40); c.fill(); c.strokeStyle = CY; c.lineWidth = 10; rr(c, 6, 6, w - 12, h - 12, 40); c.stroke();
    c.fillStyle = "#294b77"; c.font = `700 40px ${FONT}`; c.fillText("Contoh prompt · kamu → Claude", 50, 76);
    const s = typed(PROMPT, t, 28.05, 42); c.fillStyle = "#0a0d2c"; c.font = `700 56px ${FONT}`;
    const lines = []; let line = ""; for (const wd of s.split(" ")) { const tt = line ? line + " " + wd : wd; if (c.measureText(tt).width > w - 110) { lines.push(line); line = wd; } else line = tt; } lines.push(line);
    lines.slice(0, 2).forEach((l, i) => c.fillText(l, 50, 162 + i * 76));
    if (s.length < PROMPT.length && Math.floor(t * 3) % 2 === 0) { const li = Math.min(1, lines.length - 1), lw = c.measureText(lines[li]).width; c.fillStyle = CY; c.fillRect(58 + lw, 162 + li * 76 - 44, 6, 54); } });
  B.card = plane(3.3, 0.97, B.pr.tex); B.card.position.set(0, 2.0, -1.7); g.add(B.card);
  B.logo = logo3d("blender", window.LOGOS.blender.hex, 1.05); B.logo.position.set(0, 0, -0.3); g.add(B.logo);
  B.lab = label("ahujasid/mcp-for-blender", "", "#fff", 0.3); B.lab.position.set(0, 1.05, -0.2); g.add(B.lab);
  B.cl = logo3d("claude", window.LOGOS.claude.hex, 0.5); B.cl.position.set(1.5, 0, -1.45); g.add(B.cl);
  B.sel = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(0.36, 0.36, 0.36)), new THREE.LineBasicMaterial({ color: 0xe87d0d })); g.add(B.sel);
  const part = (L, p) => { const m = boxes(L); m.position.set(...p); m.visible = false; g.add(m); return m; };
  B.top = boxes([[0, 0, 0, 1.0, 1.0, 1.0, "#d8b98e"]]); g.add(B.top);
  B.legs = [[-0.7, -0.4], [0.7, -0.4], [-0.7, 0.4], [0.7, 0.4]].map(([x, z]) => part([[0, 0.34, 0, 0.1, 0.68, 0.1, "#b48a5e"]], [x, 0, z]));
  B.lamp = [part([[0, 0.05, 0, 0.4, 0.1, 0.4, "#c3cfe2"]], [-2.0, 0, -0.6]), part([[0, 0.7, 0, 0.08, 1.2, 0.08, "#c3cfe2"]], [-2.0, 0, -0.6]), part([[0, 1.4, 0, 0.5, 0.3, 0.5, "#ffffff"]], [-2.0, 0, -0.6])];
  B.bulb = new THREE.PointLight(0xfff1d8, 0, 5); B.bulb.position.set(-2.0, 1.2, -0.6); g.add(B.bulb);
  B.plant = [part([[0, 0.2, 0, 0.44, 0.4, 0.44, "#8a5a3c"]], [-1.0, 0, -1.2]), part([[0, 0.6, 0, 0.3, 0.4, 0.3, "#2ecc71"], [0.18, 0.75, 0, 0.2, 0.3, 0.2, "#27ae60"], [-0.16, 0.8, 0.05, 0.2, 0.3, 0.2, "#27ae60"]], [-1.0, 0, -1.2]),
    part([[0, 1.0, 0, 0.22, 0.3, 0.22, "#2ecc71"]], [-1.0, 0, -1.2])];
  // voxel camera on a tripod, looking at the table; its back screen is the viewfinder we dive into
  B.cam = new THREE.Group(); B.cam.position.set(...BCAM); B.cam.rotation.y = BCRY; g.add(B.cam);
  B.cam.add(boxes([[0, 0.5, 0, 0.06, 1.0, 0.06, "#8a9bb8"], [-0.25, 0.25, 0, 0.05, 0.6, 0.05, "#8a9bb8"], [0.25, 0.25, 0, 0.05, 0.6, 0.05, "#8a9bb8"],
    [0, 1.25, 0, 0.7, 0.5, 0.5, "#1b2238"], [0, 1.25, 0.34, 0.36, 0.36, 0.2, "#3a4560"], [0, 1.25, 0.45, 0.4, 0.4, 0.03, "#0b1020"]]));
  B.vf = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.34, 0.02), emi(CY, 1.2)); B.vf.position.set(0, 1.25, -0.26); B.cam.add(B.vf);
  B.cam.visible = false;
}
function animB(t) {
  B.pr.redraw(t);
  popLogo(B.logo, t, 26.86, 27.9, 1.95, 1.6); popLabel(B.lab, t, 27.25, 27.9);
  const cu = U(t, 27.95, 28.3, "back") * (1 - U(t, 30.3, 30.5, "in")); B.card.visible = t > 27.95 && cu > 0.01; B.card.scale.setScalar(Math.max(0.001, cu));
  popLogo(B.cl, t, 29.26, 30.3, 2.45, 2);
  const land = 26.3, grow = U(t, 29.5, 29.95, "back");
  if (t > 25.75 && t < 30.95) {
    if (t < land) { const u = U(t, 25.85, land, "in"); cubeAt("B", -2.6 + 2.6 * u, 24.45 - 24.28 * u, -3.15 + 3.15 * u, 1, u * 5, u * 3); }
    else if (t < 29.5) { const k = t - land, sq = Math.exp(-k * 7) * Math.sin(k * 26) * 0.22; cubeAt("B", 0, 0.17, 0, 1); CUBE.scale.set(1 + sq, 1 - sq, 1 + sq); }
  }
  B.sel.visible = t > land && t < 29.5; B.sel.position.set(0, 0.17, 0);
  B.top.visible = t >= 29.5; B.top.position.set(0, 0.17 + (0.74 - 0.17) * grow, 0); B.top.scale.set(0.34 + (1.8 - 0.34) * grow, 0.34 + (0.1 - 0.34) * grow, 0.34 + (1.1 - 0.34) * grow);
  const pop = (m, a) => { const u = U(t, a, a + 0.25, "back"); m.visible = t > a; m.scale.setScalar(Math.max(0.001, u)); };
  B.legs.forEach((m, i) => pop(m, 29.62 + i * 0.05));
  B.lamp.forEach((m, i) => pop(m, 29.75 + i * 0.09)); B.bulb.intensity = 6 * U(t, 30.0, 30.15);
  B.plant.forEach((m, i) => pop(m, 29.85 + i * 0.09));
  { const u = U(t, 30.0, 30.3, "back"); B.cam.visible = t > 30.0; B.cam.scale.setScalar(Math.max(0.001, u)); }
  B.vf.material.emissiveIntensity = 1.2 + 3 * U(t, 30.6, 30.9);
}

/* ---------------------------------------------------------------- S: Video Shotcraft — turntable promo, dolly cam, editable shots */
const Sx = {};
const SHOTS = [["SHOT 1", "PUSH-IN"], ["SHOT 2", "ORBIT"], ["SHOT 3", "DOLLY"], ["SHOT 4", "HERO"]];
const shotTex = (a, b, sel) => ctex(384, 256, (c, w, h) => { c.fillStyle = sel ? CY : "#0c1a48"; rr(c, 4, 4, w - 8, h - 8, 26); c.fill(); c.strokeStyle = sel ? "#ffffff" : CY; c.lineWidth = 8; rr(c, 4, 4, w - 8, h - 8, 26); c.stroke();
  c.fillStyle = sel ? "#0a0d2c" : "#9fdcff"; c.font = `700 54px ${FONT}`; c.textAlign = "center"; c.fillText(a, w / 2, 100); c.fillStyle = sel ? "#0a0d2c" : "#ffffff"; c.font = `700 68px ${FONT}`; c.fillText(b, w / 2, 192); });
const CARDP = (i) => [-1.68 + i * 1.12, 1.25, 1.5];
function buildS() {
  const g = mk("S"); g.add(island(5, 4)); clouds("S", 9, 37);
  const shot = ctex(1024, 640, (c, w, h) => { c.fillStyle = "#f4f7fc"; c.fillRect(0, 0, w, h); c.fillStyle = "#0e1d4d"; c.fillRect(0, 0, w, 80); c.fillStyle = "#ffffff"; c.font = `700 44px ${FONT}`; c.fillText("tokokamu.id", 36, 56);
    c.fillStyle = "#0a0d2c"; c.font = `700 84px ${FONT}`; c.fillText("Serum Pagi", 60, 230); c.fillStyle = "#294b77"; c.font = `400 50px ${FONT}`; c.fillText("halaman produkmu", 64, 300);
    c.fillStyle = CY; rr(c, 60, 350, 300, 100, 50); c.fill(); c.fillStyle = "#0a0d2c"; c.font = `700 50px ${FONT}`; c.fillText("Beli", 160, 418);
    c.fillStyle = "#dbe5f4"; rr(c, 620, 120, 340, 460, 30); c.fill(); c.fillStyle = "#ffffff"; rr(c, 720, 190, 140, 330, 40); c.fill(); c.fillStyle = CY; rr(c, 750, 160, 80, 50, 12); c.fill();
    c.fillStyle = CY; rr(c, 760, 14, 230, 54, 27); c.fill(); c.fillStyle = "#0a0d2c"; c.font = `700 36px ${FONT}`; c.textAlign = "center"; c.fillText("CONTOH", 875, 54); c.textAlign = "left"; });
  Sx.bd = new THREE.Group(); g.add(Sx.bd); Sx.bd.add(boxes([[0, 0, -0.08, 3.16, 2.02, 0.12, "#1b2a55"]])); Sx.bd.add(plane(3.0, 1.88, shot, { transparent: false }));
  Sx.tt = new THREE.Group(); g.add(Sx.tt);
  g.add(boxes([[0, 0.1, 0, 1.6, 0.2, 1.6, "#24345f"]]));
  Sx.tt.add(boxes([[0, 0.23, 0, 1.4, 0.06, 1.4, "#c3cfe2"]]));
  Sx.tt.add(boxes([[0, 0.8, 0, 0.5, 1.0, 0.5, "#ffffff"], [0, 1.4, 0, 0.26, 0.2, 0.26, "#e9eef7"], [0, 1.6, 0, 0.3, 0.2, 0.3, CY]]));
  const lb = ctex(256, 256, (c, w, h) => { c.fillStyle = "#0a1644"; c.fillRect(0, 0, w, h); c.fillStyle = CY; c.fillRect(0, 0, w, 16); c.fillStyle = "#ffffff"; c.font = `700 50px ${FONT}`; c.textAlign = "center"; c.fillText("CONTOH", w / 2, 140); });
  const lp = plane(0.42, 0.42, lb, { transparent: false }); lp.position.set(0, 0.8, 0.252); Sx.tt.add(lp);
  const sb = new THREE.Group(); sb.position.set(-3.0, 0, -1.4); sb.rotation.y = 0.7; g.add(sb);
  sb.add(boxes([[0, 0.9, 0, 0.07, 1.8, 0.07, "#8a9bb8"], [0, 0.03, 0, 0.6, 0.06, 0.6, "#5b6b8c"], [0, 2.0, -0.12, 0.9, 0.7, 0.2, "#1b2238"]]));
  const pp = new THREE.Mesh(new THREE.BoxGeometry(0.82, 0.62, 0.02), emi("#e8f8ff", 2.2)); pp.position.set(0, 2.0, 0.0); sb.add(pp);
  Sx.key = new THREE.PointLight(0xdff6ff, 0, 7); Sx.key.position.set(-1.2, 2.2, 1.2); g.add(Sx.key);
  g.add(boxes([[2.25, 0.04, 0.5, 0.1, 0.08, 2.2, "#8a9bb8"], [2.55, 0.04, 0.5, 0.1, 0.08, 2.2, "#8a9bb8"]]));
  Sx.cam = new THREE.Group(); g.add(Sx.cam);
  Sx.cam.add(boxes([[0, 0.12, 0, 0.6, 0.16, 0.5, "#3a4560"], [0, 0.6, 0, 0.08, 0.8, 0.08, "#8a9bb8"], [0, 1.1, 0, 0.5, 0.36, 0.6, "#1b2238"], [0, 1.1, 0.38, 0.28, 0.28, 0.18, "#3a4560"]]));
  Sx.cards = SHOTS.map(([a, b]) => { const m = plane(0.98, 0.65, shotTex(a, b, false), { side: THREE.DoubleSide }); g.add(m); m.visible = false; return m; });
  Sx.edited = shotTex("SHOT 3", "ORBIT ✓", true);
  Sx.cur = new THREE.Sprite(new THREE.SpriteMaterial({ map: ctex(128, 128, (c) => { c.fillStyle = "#ffffff"; c.strokeStyle = "#0a0d2c"; c.lineWidth = 6; c.beginPath(); c.moveTo(30, 14); c.lineTo(30, 104); c.lineTo(52, 84); c.lineTo(68, 118); c.lineTo(84, 110); c.lineTo(68, 78); c.lineTo(98, 78); c.closePath(); c.stroke(); c.fill(); }), depthTest: false, toneMapped: false }));
  Sx.cur.renderOrder = 30; Sx.cur.scale.set(0.3, 0.3, 1); g.add(Sx.cur);
  Sx.lab = label("Vincentwei1021/video-shotcraft", "", "#fff", 0.3); Sx.lab.position.set(0, 2.35, 0.2); g.add(Sx.lab);
  Sx.cl = logo3d("claude", window.LOGOS.claude.hex, 0.7); Sx.cl.position.set(-1.85, 0, 0.2); g.add(Sx.cl);
  Sx.l1 = label("Claude Code", "", "#fff", 0.3); Sx.l1.position.set(-1.85, 1.1, 0.5); g.add(Sx.l1);
  Sx.l2 = label("Codex", "", "#fff", 0.3); Sx.l2.position.set(1.85, 1.6, 0.5); g.add(Sx.l2);
}
function animS(t) {
  popLabel(Sx.lab, t, 31.7, 32.6);
  popLogo(Sx.cl, t, 32.78, 34.15, 1.85, 2); popLabel(Sx.l1, t, 32.85, 34.15); popLabel(Sx.l2, t, 33.5, 34.15);
  Sx.tt.rotation.y = t * 0.9; Sx.key.intensity = 5 * U(t, 34.3, 34.6);
  const dl = U(t, 34.25, 36.1, "io"); Sx.cam.position.set(2.4, 0, 1.5 - 1.6 * dl); Sx.cam.rotation.y = -Math.PI / 2 - 0.5 + 0.5 * dl;
  const bu = U(t, 35.3, 35.85, "back"); Sx.bd.position.set(0, 1.75 + 3.5 * (1 - bu), -2.2); Sx.bd.visible = t > 35.25;
  Sx.cards.forEach((m, i) => { const a = 36.45 + i * 0.1, u = U(t, a, a + 0.35, "back"); m.visible = t > a; const p = CARDP(i);
    let y = p[1] + (i === 2 ? 0.22 * U(t, 37.1, 37.3, "back") : 0), z = p[2], s = Math.max(0.001, u);
    if (i === 2 && t > 37.75) { const v = U(t, 37.75, 38.25, "in"); y += 0.6 * v; z += 4.5 * v; s *= 1 + 0.4 * v; }
    m.position.set(p[0], y, z); m.scale.setScalar(s); m.rotation.x = -0.12; if (i === 2) m.material.map = t > 37.25 ? Sx.edited : m.userData.m0 || (m.userData.m0 = m.material.map); });
  const c3 = CARDP(2), cu = U(t, 36.55, 37.0, "io"); Sx.cur.visible = t > 36.5 && t < 37.75;
  const press = t > 37.08 && t < 37.22 ? 0.85 : 1; Sx.cur.scale.set(0.3 * press, 0.3 * press, 1);
  Sx.cur.position.set(bez(2.4, 1.6, c3[0] + 0.42, cu), bez(0.6, 0.9, c3[1] - 0.3 + (t > 37.1 ? 0.22 * U(t, 37.1, 37.3, "back") : 0), cu), c3[2] + 0.12);
  // through-line cube: the tally light on the dolly camera, then the marker on the edited shot
  if (t > 30.92 && t < 38.3) { const tallyY = 1.42;
    if (t < 36.4) cubeAt("S", Sx.cam.position.x, tallyY, Sx.cam.position.z, 0.55, 0, t);
    else { const u = U(t, 36.4, 36.9, "io"), p = CARDP(2); cubeAt("S", bez(Sx.cam.position.x, 1.2, p[0], u), bez(tallyY, 2.4, p[1] + 0.48 + (t > 37.1 ? 0.22 * U(t, 37.1, 37.3, "back") : 0), u), bez(Sx.cam.position.z, 1.4, p[2], u), 0.55, 0, t);
      if (t > 37.75) CUBE.visible = CUBEG.visible = false; } }
}

/* ---------------------------------------------------------------- camera path (absolute), with cuts.
   FR(): camera from a target + how wide (metres) should span how many pixels (screen-studio framing). After the mascot
   rises the target sits at screen y≈730 (LIFT view offset), so the 3D action band is y≈500–980. */
const C = []; const at = (w) => (v) => [v[0] + WP[w][0], v[1] + WP[w][1], v[2] + WP[w][2], v[3] + WP[w][0], v[4] + WP[w][1], v[5] + WP[w][2], v[6]];
const TH = Math.tan((40 * Math.PI) / 360) * W / H;
const FR = (T, wm, px, el = 0.2, yaw = 0) => { const d = (wm * 1080) / (px * 2 * TH); return [T[0] + d * Math.sin(yaw) * Math.cos(el), T[1] + d * Math.sin(el), T[2] + d * Math.cos(yaw) * Math.cos(el), T[0], T[1], T[2], 40]; };
const k = (w, t, v, e) => C.push([t, at(w)(v), e]);
const cut = (w, t, v) => C.push([t, at(w)(v), "lin"]);
// H — world first: the code monitor fills the width, pan to the editing board, zoom-out reveal of the hub
k("H", 0, FR([0, 2.0, -1.2], 3.3, 960, 0.04)); k("H", 3.8, FR([0, 2.0, -1.2], 3.3, 1010, 0.05), "sine");
k("H", 4.35, FR([2.7, 1.5, -0.2], 3.0, 900, 0.12, -0.45), "io"); k("H", 4.75, FR([2.6, 1.45, -0.1], 3.6, 900, 0.14, -0.42), "sine");
k("H", 5.8, FR([0, 0.82, CRZ], 7.2, 1040, 0.26), "io"); k("H", 8.4, FR([0, 0.82, CRZ], 7.2, 1070, 0.25), "sine");
k("H", 8.8, FR([CRX[0], 0.6, CRZ + 0.5], 1.6, 900, 0.08), "io"); k("H", 9.16, FR([CRX[0], 0.55, CRZ + 0.5], 0.4, 900, 0.05), "in");
// F — out of the portal on the cube, README facts, code, frames fly to the phone, push to the phone, whip tilt up
cut("F", 9.17, FR([MONF[0] + 1.2, 3.25, MONF[2] + 0.15], 0.55, 900, 0.15)); k("F", 10.1, FR([MONF[0], 2.0, MONF[2]], 3.3, 830, 0.12, 0.12), "io");
k("F", 12.8, FR([MONF[0], 2.0, MONF[2]], 3.3, 860, 0.12, 0.12), "sine"); k("F", 14.45, FR([MONF[0], 2.0, MONF[2]], 3.3, 900, 0.12, 0.12), "sine");
k("F", 15.3, FR([0.8, 1.75, -0.6], 6.6, 1000, 0.16), "io"); k("F", 16.35, FR([PHF[0], 1.6, PHF[2]], 4.3, 1080, 0.1, -0.4), "io"); k("F", 18.75, FR([PHF[0], 1.6, PHF[2]], 4.15, 1080, 0.1, -0.4), "sine");
C.push([19.16, (() => { const v = at("F")(FR([PHF[0], 1.6, PHF[2]], 4.15, 1080, 0.1, -0.4)); v[4] += 30; return v; })(), "expo"]);
// G — tilt down from the sky onto the logo, the board rises, then the lanes; follow the falling cube down to B
C.push([19.17, (() => { const v = at("G")(FR([0, 1.5, 0.2], 4.4, 1000, 0.15)); v[4] += 30; return v; })(), "lin"]);
k("G", 19.6, FR([0, 1.5, 0.2], 4.4, 1000, 0.15), "out"); k("G", 22.3, FR([0, 1.5, 0.2], 4.4, 1060, 0.15), "sine");
k("G", 22.75, FR([0, 2.05, -1.5], 5.8, 1080, 0.1), "io"); k("G", 23.95, FR([0, 2.05, -1.5], 5.6, 1080, 0.1), "sine");
k("G", 24.5, FR([0.6, 0.55, 1.8], 6.6, 1000, 0.5), "io"); k("G", 25.55, FR([0.8, 0.55, 1.8], 6.4, 1000, 0.5), "sine");
C.push([25.8, at("G")(FR([4.2, 0.0, 2.9], 6.0, 1000, 0.8)), "io"]);
C.push([26.3, at("B")(FR([0, 0.9, 0], 5.0, 1000, 0.45)), "out"]);
// B
k("B", 27.9, FR([0, 0.95, -0.1], 5.0, 1000, 0.3), "io"); k("B", 28.3, FR([0, 1.15, -0.5], 4.7, 1080, 0.25), "io"); k("B", 30.35, FR([0, 1.15, -0.5], 4.6, 1080, 0.25), "sine");
k("B", 30.68, (() => { const bx = BCAM[0] - 0.9 * Math.sin(BCRY), bz = BCAM[2] - 0.9 * Math.cos(BCRY); return [bx, 1.3, bz, BCAM[0], 1.25, BCAM[2], 40]; })(), "io");
k("B", 30.92, (() => { const bx = BCAM[0] - 0.2 * Math.sin(BCRY), bz = BCAM[2] - 0.2 * Math.cos(BCRY); return [bx, 1.25, bz, BCAM[0] + Math.sin(BCRY), 1.25, BCAM[2] + Math.cos(BCRY), 40]; })(), "in");
// S — out of the viewfinder: bottle close-up, pull back, logos, dolly, backdrop, shot strip, card flies into the lens
cut("S", 30.93, FR([0, 1.0, 0], 1.6, 1000, 0.08)); k("S", 31.9, FR([0, 1.35, 0], 6.2, 1000, 0.2), "io");
k("S", 34.2, FR([0, 1.35, 0], 6.0, 1000, 0.2), "sine"); k("S", 35.25, FR([0.6, 1.1, 0.3], 4.6, 1000, 0.15, 0.25), "io"); k("S", 36.3, FR([0, 1.5, -0.6], 6.2, 1000, 0.18), "io");
k("S", 36.75, FR([0, 1.3, 1.5], 4.7, 1000, 0.12), "io"); k("S", 37.7, FR([0, 1.3, 1.5], 4.5, 1000, 0.12), "sine"); k("S", 38.26, FR([0.56, 1.5, 3.0], 1.2, 1000, 0.1), "in");
// CTA back on the hub: crates sink, logos orbit the GitHub mark
cut("H", 38.27, FR([0, 1.95, 1.0], 6.0, 1000, 0.2)); k("H", 42.5, FR([0, 1.95, 1.0], 6.6, 1000, 0.22), "sine");
C.sort((a, b) => a[0] - b[0]);
window.VX = { C, WP };
scene.add(cam);

/* ---------------------------------------------------------------- render */
let ready = false; const LIFTAT = (t) => 230 * U(t, 5.3, 6.0);
const ANIM = { H: animH, F: animF, G: animG, B: animB, S: animS };
function render(t) {
  window.VX.lastT = t; if (!ready) return;
  CUBE.visible = CUBEG.visible = false;
  for (const kk in worlds) { worlds[kk].visible = VIS[kk].some(([a, b]) => t >= a && t < b); if (worlds[kk].visible) ANIM[kk](t); }
  const v = keys(t, C), hx = Math.sin(t * 0.9) * 0.02, hy = Math.sin(t * 1.3 + 1) * 0.015;
  const LIFT = LIFTAT(t), Hf = H + 2 * LIFT, fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * Hf / H) * 180) / Math.PI;
  cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.fov = fov; cam.setViewOffset(W, Hf, 0, 2 * LIFT, W, H); cam.updateProjectionMatrix();
  cam.up.set(0, 1, 0); cam.lookAt(v[3], v[4], v[5]);
  stars.position.copy(cam.position);
  const tx = v[3], ty = Math.abs(v[4] - cam.position.y) > 8 ? cam.position.y - 3 : v[4], tz = v[5]; moon.position.set(tx - 6, ty + 12, tz + 8); moon.target.position.set(tx, ty - 1, tz - 1); warm.position.set(tx + 6, ty + 4, tz + 7); warm.target.position.set(tx, ty, tz);
  renderer.render(scene, cam);
}
window.VX.render = render;
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  buildH(); buildF(); buildG(); buildB(); buildS(); ready = true; render(window.VX.t0 || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.vx = PR;
window.addEventListener("hf-seek", (e) => render(e.detail.time));
