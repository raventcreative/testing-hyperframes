/* R29 · Dadu bisnis — the 3D dice + tray world (own assets, built in code). Transparent WebGL canvas over the client's light
   background; dice = idea + approach, tray = market. Deterministic: render(t) is a pure function of global time ("hf-seek").
   Props are reset every frame; each scene block shows and poses only what it uses. Camera = shot groups with a slow 4 % push
   (1.0 -> 1.04) per group and one eased move between groups. The guide dot (#gdot, the six-pip) is positioned from here. */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";

const R = window.R29, Wd = R.W, S = R.S, E = R.E;
const cv = document.getElementById("world");
const CW = cv.width, CH = cv.height, CTOP = 200;   // canvas sits at page y 200..1000
const renderer = new THREE.WebGLRenderer({ canvas: cv, antialias: true, alpha: true, preserveDrawingBuffer: true, premultipliedAlpha: true });
renderer.setPixelRatio(1); renderer.setSize(CW, CH, false); renderer.setClearColor(0x000000, 0);
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.NeutralToneMapping; renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.45;
scene.add(new THREE.HemisphereLight(0xffffff, 0xb9c8e6, 1.25));
const key = new THREE.DirectionalLight(0xffffff, 2.0); key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; key.shadow.normalBias = 0.02; key.shadow.radius = 4;
Object.assign(key.shadow.camera, { left: -9, right: 9, top: 9, bottom: -9, near: 1, far: 40 }); key.position.set(-5, 11, 7); scene.add(key, key.target);
const fill = new THREE.DirectionalLight(0xdfe9ff, 0.55); fill.position.set(6, 4, -5); scene.add(fill);
const cam = new THREE.PerspectiveCamera(34, CW / CH, 0.1, 120); cam.aspect = CW / CH;
const ground = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), new THREE.ShadowMaterial({ color: 0x0a0d2c, opacity: 0.16 }));
ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);

/* ---------------------------------------------------------------- math */
const one = (x) => Math.max(0, Math.min(1, x)), L = (a, b, u) => a + (b - a) * u;
const EZ = { lin: (x) => x, io: (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2), out: (x) => 1 - Math.pow(1 - x, 3),
  in: (x) => x * x * x, sine: (x) => -(Math.cos(Math.PI * x) - 1) / 2, out2: (x) => 1 - (1 - x) * (1 - x),
  back: (x) => { const c1 = 1.25, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); } };
const U = (t, a, b, e = "io") => EZ[e](one((t - a) / (b - a)));
const spring = (t, a, d = 0.45) => { if (t <= a) return 0; const k = (t - a) / d; return k >= 3 ? 1 : 1 - Math.exp(-5 * k) * Math.cos(7.5 * k) * (1 - 0) ; };   // small overshoot
const bump = (t, a, d) => (t > a && t < a + d ? Math.sin(Math.PI * (t - a) / d) : 0);
const hsh = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
const V3 = (x, y, z) => new THREE.Vector3(x, y, z), Y = V3(0, 1, 0);
const FONT = "Poppins, sans-serif";

/* ---------------------------------------------------------------- textures */
function ctex(w, h, draw) { const c = document.createElement("canvas"); c.width = w; c.height = h; draw(c.getContext("2d"), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; }
function rr(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
function fitFont(g, txt, px, maxW, wt = 700) { do { g.font = `${wt} ${px}px ${FONT}`; if (g.measureText(txt).width <= maxW) return px; px -= 2; } while (px > 10); return px; }
const PIPS = { 1: [[0, 0]], 2: [[-1, -1], [1, 1]], 3: [[-1, -1], [0, 0], [1, 1]], 4: [[-1, -1], [1, -1], [-1, 1], [1, 1]], 5: [[-1, -1], [1, -1], [0, 0], [-1, 1], [1, 1]],
  6: [[-1, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [1, 1]] };
function faceTex(v, body, pip, mark) {
  return ctex(256, 256, (g, w, h) => {
    g.fillStyle = body; g.fillRect(0, 0, w, h);
    const gr = g.createRadialGradient(128, 128, 30, 128, 128, 190); gr.addColorStop(0, "rgba(255,255,255,0.10)"); gr.addColorStop(1, "rgba(0,0,0,0.06)"); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    if (v === "?") { g.fillStyle = pip; g.textAlign = "center"; g.textBaseline = "middle"; g.font = `700 170px ${FONT}`; g.fillText("?", 128, 140); return; }
    for (const [x, y] of PIPS[v] || []) { const cx = 128 + x * 58, cy = 128 + y * 58;
      g.fillStyle = pip; g.beginPath(); g.arc(cx, cy, 24, 0, Math.PI * 2); g.fill();
      g.fillStyle = "rgba(255,255,255,0.18)"; g.beginPath(); g.arc(cx - 6, cy - 7, 8, 0, Math.PI * 2); g.fill(); }
    if (mark) { g.strokeStyle = mark; g.lineWidth = 10; rr(g, 12, 12, 232, 232, 30); g.stroke(); }
  });
}
const NORMALS = [V3(1, 0, 0), V3(-1, 0, 0), V3(0, 1, 0), V3(0, -1, 0), V3(0, 0, 1), V3(0, 0, -1)];
const VALS = [3, 4, 1, 6, 2, 5];           // face value per BoxGeometry group (+x,-x,+y,-y,+z,-z); opposite faces sum to 7
const VALS_NOSIX = [3, 4, 1, 5, 2, 5];     // the "wrong idea" die: no six at all
function matSet(body, pip, vals = VALS, rough = 0.32) {
  return vals.map((v) => new THREE.MeshStandardMaterial({ map: faceTex(v, body, pip), roughness: rough, metalness: 0 }));
}
const SETS = {};
const GEO_DIE = new RoundedBoxGeometry(1, 1, 1, 4, 0.13);

/* ---------------------------------------------------------------- props */
const P = {};       // name -> Object3D
const ALL = [];
function reg(name, o) { o.visible = false; P[name] = o; ALL.push(o); scene.add(o); return o; }
function die(name, set, vals = VALS) { const m = new THREE.Mesh(GEO_DIE, SETS[set]); m.castShadow = true; m.receiveShadow = true; m.userData.vals = vals;
  const g = new THREE.Group(); g.add(m); g.userData.mesh = m; g.userData.vals = vals; return reg(name, g); }
function setDieMat(g, set, vals) { g.userData.mesh.material = SETS[set]; g.userData.vals = vals || VALS; }
const rbox = (w, h, d, col, r = 0.08, rough = 0.6) => { const m = new THREE.Mesh(new RoundedBoxGeometry(w, h, d, 3, Math.min(r, w / 2 - 0.001, h / 2 - 0.001, d / 2 - 0.001)),
  new THREE.MeshStandardMaterial({ color: col, roughness: rough })); m.castShadow = true; m.receiveShadow = true; return m; };
function tray(name, w, d, o = {}) {
  const g = new THREE.Group(), h = o.h || 0.5, th = o.th || 0.3, rim = o.rim || "#ffffff", felt = o.felt || "#294b77";
  const floor = rbox(w + th, 0.14, d + th, felt, 0.05, 0.95); floor.position.y = 0.07; g.add(floor); g.userData.floor = floor;
  const rims = new THREE.Group(); g.add(rims);
  for (const [x, z, ww, dd] of [[0, d / 2 + th / 2, w + 2 * th, th], [0, -d / 2 - th / 2, w + 2 * th, th], [w / 2 + th / 2, 0, th, d], [-w / 2 - th / 2, 0, th, d]]) {
    const r = rbox(ww, h, dd, rim, 0.1, 0.45); r.position.set(x, h / 2, z); rims.add(r); }
  if (o.label) { const pl = new THREE.Mesh(new THREE.PlaneGeometry(Math.min(w + 2 * th, o.labelW || w), h * 0.86), new THREE.MeshBasicMaterial({ map: o.label, transparent: true, toneMapped: false }));
    pl.position.set(0, h / 2, d / 2 + th + 0.004); g.add(pl); g.userData.plate = pl; }
  g.userData.w = w; g.userData.d = d; return reg(name, g);
}
function labelTex(txt, sub, o = {}) {   // a white pill with navy text (fits, never cut)
  const W0 = o.w || 640, H0 = sub ? 200 : 140;
  return ctex(W0, H0, (g, w, h) => {
    g.fillStyle = o.bg || "#ffffff"; rr(g, 6, 6, w - 12, h - 12, 34); g.fill();
    g.strokeStyle = o.stroke || "#294b77"; g.lineWidth = 6; rr(g, 6, 6, w - 12, h - 12, 34); g.stroke();
    g.fillStyle = o.fg || "#0a0d2c"; g.textAlign = "center"; g.textBaseline = "middle";
    fitFont(g, txt, sub ? 64 : 68, w - 70); g.fillText(txt, w / 2, sub ? 76 : h / 2 + 3);
    if (sub) { g.fillStyle = o.fg2 || "#294b77"; fitFont(g, sub, 42, w - 80, 400); g.fillText(sub, w / 2, 148); }
  });
}
function sprite(name, tex, wUnits) { const m = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true, toneMapped: false, depthTest: false }));
  const ar = tex.image.height / tex.image.width; m.scale.set(wUnits, wUnits * ar, 1); m.userData.w = wUnits; m.userData.ar = ar; m.renderOrder = 10; return reg(name, m); }
const sprSize = (m, k) => m.scale.set(m.userData.w * k, m.userData.w * m.userData.ar * k, 1);
function plateTex(txt, o = {}) { return ctex(o.w || 900, 150, (g, w, h) => { g.fillStyle = o.bg || "#ffffff"; g.fillRect(0, 0, w, h);
  g.fillStyle = o.fg || "#0a0d2c"; g.textAlign = "center"; g.textBaseline = "middle"; fitFont(g, txt, 74, w - 60); g.fillText(txt, w / 2, h / 2 + 4); }); }

/* ---------------------------------------------------------------- pose helpers */
const _q = new THREE.Quaternion(), _q2 = new THREE.Quaternion(), _ax = new THREE.Vector3();
function upQuat(vals, v, yaw, out) {
  const i = vals.indexOf(v); out.setFromUnitVectors(NORMALS[i], Y); _q2.setFromAxisAngle(Y, yaw || 0); return out.premultiply(_q2);
}
/** throw: o = {t0 release, ti first impact, t1 rest, p0 [x,y,z], pi [x,z], p1 [x,z], v face, yaw, spin, ax [x,y,z], h arc, s scale, hb hop} */
function throwDie(g, t, o) {
  const s = o.s || 1, rest = 0.5 * s + (o.fy || 0), vals = g.userData.vals;
  if (t < o.t0 && !o.pre) { g.visible = false; return false; }
  g.visible = true; g.scale.setScalar(s);
  let x, y, z;
  const pi = o.pi || o.p1;
  if (t < o.ti) { const u = one((t - o.t0) / (o.ti - o.t0)); x = L(o.p0[0], pi[0], u); z = L(o.p0[2], pi[1], u); y = L(o.p0[1], rest, u * u) + 4 * (o.h || 0) * u * (1 - u); }
  else { const k = one((t - o.ti) / (o.t1 - o.ti)); x = L(pi[0], o.p1[0], EZ.out(k)); z = L(pi[1], o.p1[1], EZ.out(k));
    y = rest + (o.hb == null ? 0.45 : o.hb) * s * Math.abs(Math.sin(Math.PI * 2 * k)) * (1 - k) * (1 - k); }
  const gp = one((t - o.t0) / (o.t1 - o.t0)), ang = (o.spin == null ? 9 : o.spin) * (1 - EZ.out2(gp));
  upQuat(vals, o.v, o.yaw || 0, _q); _ax.set(...(o.ax || [0.7, 0.2, 0.6])).normalize(); _q2.setFromAxisAngle(_ax, ang); g.quaternion.copy(_q).multiply(_q2);
  const a2 = Math.abs(ang) % (Math.PI / 2); y += 0.5 * s * (Math.abs(Math.cos(a2)) + Math.abs(Math.sin(a2)) - 1);
  g.position.set(x, y, z);
  return t >= o.t1;
}
function restDie(g, x, z, v, yaw = 0, s = 1, fy = 0) { g.visible = true; g.scale.setScalar(s); upQuat(g.userData.vals, v, yaw, g.quaternion); g.position.set(x, 0.5 * s + fy, z); }
function show(name, x, y, z, s = 1) { const o = P[name]; o.visible = true; o.position.set(x, y, z); if (o.isSprite) sprSize(o, s); else o.scale.setScalar(s); return o; }

/* ---------------------------------------------------------------- build */
const TX = {};
const N_INST = 100;
let INST = null;
function build() {
  SETS.white = matSet("#ffffff", "#0a0d2c"); SETS.navy = matSet("#0a0d2c", "#ffffff"); SETS.blue = matSet("#294b77", "#ffffff");
  SETS.sky = matSet("#e3edfa", "#0a0d2c"); SETS.nosix = matSet("#ffffff", "#0a0d2c", VALS_NOSIX); SETS.q = [0, 1, 2, 3, 4, 5].map(() => new THREE.MeshStandardMaterial({ map: faceTex("?", "#e3edfa", "#294b77"), roughness: 0.4 }));
  SETS.win = VALS.map((v) => new THREE.MeshStandardMaterial({ map: faceTex(v, "#ffffff", v === 6 ? "#294b77" : "#0a0d2c", v === 6 ? "#294b77" : null), roughness: 0.32 }));
  for (let i = 0; i < 12; i++) die("d" + i, "white");
  die("big", "white"); die("tiny", "white"); die("nosix", "nosix", VALS_NOSIX);
  for (let i = 0; i < 4; i++) die("q" + i, "q");
  // trays
  tray("T", 6.4, 4.0, { felt: "#294b77", rim: "#ffffff" });
  tray("Ts", 2.3, 1.5, { felt: "#294b77", rim: "#ffffff", h: 0.42, th: 0.24 });
  tray("Tf", 3.6, 2.4, { felt: "#294b77", rim: "#ffffff" });
  tray("Th", 2.8, 2.0, { felt: "#0a0d2c", rim: "#e3edfa" });
  tray("Tb", 2.4, 1.7, { felt: "#13307e", rim: "#ffffff", h: 0.4, th: 0.24 });
  tray("Tc", 3.0, 2.0, { felt: "#e3edfa", rim: "#294b77", h: 0.42, th: 0.26 });
  // instanced dice (100 throws)
  INST = new THREE.InstancedMesh(GEO_DIE, SETS.white, N_INST); INST.castShadow = true; INST.receiveShadow = true; INST.visible = false; scene.add(INST);
  // labels (sprites)
  TX.lb = {
    dadu: labelTex("DADU = IDE + CARA", null, { w: 700 }), nampan: labelTex("NAMPAN = PASAR", null, { w: 640 }),
    ruko: labelTex("RUKO 3 LANTAI", null, { w: 600 }), grup: labelTex("GRUP KELUARGA", "1× sebulan", { w: 560 }),
    produk: labelTex("PRODUK BARU", null, { w: 560 }), pasar: labelTex("PASAR BARU", null, { w: 520 }), harga: labelTex("HARGA BARU", null, { w: 520 }), cara: labelTex("CARA JUALAN BARU", null, { w: 700 }),
    six: labelTex("HARUS 6", null, { w: 380 }), miss: labelTex("BUKAN 6", null, { w: 380, fg: "#ffffff", bg: "#294b77", stroke: "#294b77" }),
    ide: labelTex("IDE TEPAT", null, { w: 420 }), tepat: labelTex("PASAR BESAR & TUMBUH", null, { w: 780 }),
    target: labelTex("TARGET", null, { w: 400, fg: "#ffffff", bg: "#294b77", stroke: "#294b77" }), shiny: labelTex("KINCLONG!", null, { w: 460 }),
    a: labelTex("CARA A", "ganti dadu + nampan", { w: 600 }), b: labelTex("CARA B", "dadu & nampan dikunci", { w: 640 }),
  };
  for (const [k, tx] of Object.entries(TX.lb)) sprite("L_" + k, tx, k === "tepat" ? 3.2 : 2.4);
  // padlocks
  for (const n of ["lockA", "lockB"]) { const g = new THREE.Group(); const body = rbox(0.62, 0.5, 0.26, "#294b77", 0.08, 0.35); body.position.y = 0.25; g.add(body);
    const sh = new THREE.Mesh(new THREE.TorusGeometry(0.2, 0.055, 10, 24, Math.PI), new THREE.MeshStandardMaterial({ color: "#c9d4e6", metalness: 0.8, roughness: 0.25 }));
    sh.position.y = 0.5; g.add(sh); g.userData.sh = sh; const kh = new THREE.Mesh(new THREE.CircleGeometry(0.06, 16), new THREE.MeshBasicMaterial({ color: "#ffffff" })); kh.position.set(0, 0.27, 0.131); g.add(kh);
    g.traverse((o) => { if (o.isMesh) o.castShadow = true; }); reg(n, g); }
  // magnifier
  { const g = new THREE.Group(); const ring = new THREE.Mesh(new THREE.TorusGeometry(0.75, 0.1, 12, 40), new THREE.MeshStandardMaterial({ color: "#0a0d2c", roughness: 0.35 }));
    const glass = new THREE.Mesh(new THREE.CircleGeometry(0.72, 40), new THREE.MeshStandardMaterial({ color: "#e3edfa", transparent: true, opacity: 0.35, roughness: 0.05, metalness: 0.1 }));
    const handle = rbox(0.2, 1.1, 0.2, "#294b77", 0.08, 0.4); handle.position.set(0.75, -0.95, 0); handle.rotation.z = 0.7;
    g.add(ring, glass, handle); ring.castShadow = true; handle.castShadow = true; reg("mag", g); }
  // gem (shiny object)
  { const g = new THREE.Group(); const geo = new THREE.OctahedronGeometry(0.7, 0); geo.scale(1, 1.35, 1);
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: "#d9ecff", metalness: 0.65, roughness: 0.12, flatShading: true, emissive: "#6aa5ff", emissiveIntensity: 0.22 }));
    m.castShadow = true; g.add(m); g.userData.m = m;
    const st = ctex(128, 128, (c) => { const gr = c.createRadialGradient(64, 64, 0, 64, 64, 60); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(0.25, "rgba(200,225,255,0.8)"); gr.addColorStop(1, "rgba(200,225,255,0)");
      c.fillStyle = gr; c.beginPath(); c.moveTo(64, 0); c.lineTo(72, 56); c.lineTo(128, 64); c.lineTo(72, 72); c.lineTo(64, 128); c.lineTo(56, 72); c.lineTo(0, 64); c.lineTo(56, 56); c.closePath(); c.fill(); });
    g.userData.sp = []; for (let i = 0; i < 4; i++) { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: st, transparent: true, depthWrite: false, toneMapped: false })); s.scale.set(0.5, 0.5, 1); g.add(s); g.userData.sp.push(s); }
    reg("gem", g); }
  // target (flag + rings)
  { const g = new THREE.Group(); const cols = ["#294b77", "#ffffff", "#294b77", "#ffffff"]; cols.forEach((c, i) => { const r = 0.9 - i * 0.22;
      const m = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 0.06, 40), new THREE.MeshStandardMaterial({ color: c, roughness: 0.5 })); m.position.y = 0.03 + i * 0.012; m.receiveShadow = true; g.add(m); });
    const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 2.2, 12), new THREE.MeshStandardMaterial({ color: "#0a0d2c" })); pole.position.set(0, 1.1, 0); pole.castShadow = true; g.add(pole);
    const fl = new THREE.Mesh(new THREE.PlaneGeometry(1.0, 0.62), new THREE.MeshStandardMaterial({ color: "#294b77", side: THREE.DoubleSide })); fl.position.set(0.52, 1.85, 0); fl.castShadow = true; g.add(fl); g.userData.fl = fl;
    reg("target", g); }
  // dots (paths, trails) — one instanced sphere mesh
  P.dots = new THREE.InstancedMesh(new THREE.SphereGeometry(0.09, 12, 8), new THREE.MeshStandardMaterial({ color: "#294b77", roughness: 0.4 }), 64); P.dots.visible = false; scene.add(P.dots);
  // growth arrow
  { const g = new THREE.Group(); const mat = new THREE.MeshStandardMaterial({ color: "#294b77", roughness: 0.4 });
    const sh = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 1.6, 16), mat); sh.position.y = 0.8; const hd = new THREE.Mesh(new THREE.ConeGeometry(0.42, 0.7, 24), mat); hd.position.y = 1.95;
    sh.castShadow = hd.castShadow = true; g.add(sh, hd); reg("arrow", g); }
  // the pit under the floorless tray
  { const tx = ctex(256, 256, (c) => { const gr = c.createRadialGradient(128, 128, 10, 128, 128, 128); gr.addColorStop(0, "rgba(10,13,44,0.85)"); gr.addColorStop(0.7, "rgba(10,13,44,0.55)"); gr.addColorStop(1, "rgba(10,13,44,0)"); c.fillStyle = gr; c.fillRect(0, 0, 256, 256); });
    const m = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ map: tx, transparent: true, depthWrite: false, toneMapped: false })); m.rotation.x = -Math.PI / 2; m.renderOrder = 1; reg("pit", m); }
  // glow ring under a winning die
  { const tx = ctex(256, 256, (c) => { const gr = c.createRadialGradient(128, 128, 40, 128, 128, 126); gr.addColorStop(0, "rgba(41,75,119,0)"); gr.addColorStop(0.62, "rgba(41,75,119,0.55)"); gr.addColorStop(0.72, "rgba(41,75,119,0.85)"); gr.addColorStop(1, "rgba(41,75,119,0)"); c.fillStyle = gr; c.fillRect(0, 0, 256, 256); });
    for (const n of ["ring0", "ring1", "ring2", "ring3", "ring4"]) { const m = new THREE.Mesh(new THREE.PlaneGeometry(1.9, 1.9), new THREE.MeshBasicMaterial({ map: tx, transparent: true, depthWrite: false, toneMapped: false })); m.rotation.x = -Math.PI / 2; m.renderOrder = 2; reg(n, m); } }
}

/* ---------------------------------------------------------------- camera shots */
// [px,py,pz, lx,ly,lz, fov]
const SH = {   // [px,py,pz, lx,ly,lz, fov, a] — a = image shift down (px) so the tray sits low in the hero zone and cards fit above
  hook: [0, 8.6, 9.4, 0, 0.1, 0.3, 34, 150], main: [0, 9.6, 10.2, 0, 0.1, 0.3, 34, 150], high: [0, 13.2, 7.4, 0, 0, 0.2, 34, 140],
  spread: [0, 10.4, 11.0, 0, 0, -0.5, 36, 120], low: [0, 6.0, 11.4, 0, 0.8, 0, 34, 120], wide: [0, 10.8, 12.4, 0, 0.2, 0, 34, 140],
  lowmain: [0, 9.6, 10.2, 0, 0.1, 0.3, 34, 215], path: [0, 9.6, 10.8, 0, 0.2, 0.1, 34, 150], net: [0, 10.2, 7.6, 0, 0, 0.6, 34, 140], gem: [0, 5.0, 9.6, 0, 1.2, 0, 34, 120],
};
// shot per scene (groups = consecutive scenes with the same shot keep pushing); tr = blend into this group (s)
const SHOTS = { 1: "hook", 2: "main", 3: "high", 4: "high", 5: "high", 6: "spread", 7: "main", 8: "main", 9: "main", 10: "net", 11: "main", 12: "main", 13: "main", 14: "main", 15: "main",
  16: "main", 17: "main", 18: "main", 19: "main", 20: "main", 21: "main", 22: "main", 23: "low", 24: "low", 25: "wide", 26: "main", 27: "main", 28: "main", 29: "main", 30: "main",
  31: "main", 32: "wide", 33: "main", 34: "gem", 35: "path", 36: "path", 37: "spread", 38: "spread", 39: "lowmain", 40: "lowmain", 41: "main", 42: "wide", 43: "lowmain", 44: "lowmain", 45: "lowmain" };
const NSC = window.VO_SCENES.length;
const GROUPS = []; { let k = 1; while (k <= NSC) { let j = k; while (j + 1 <= NSC && SHOTS[j + 1] === SHOTS[k]) j++; GROUPS.push({ a: S(k), b: E(j), shot: SH[SHOTS[k]], k, j }); k = j + 1; } }
function shotAt(G, t) { const u = one((t - G.a) / (G.b - G.a)), push = 1 - 0.04 * EZ.sine(u), s = G.shot;
  return [s[3] + (s[0] - s[3]) * push, s[4] + (s[1] - s[4]) * push, s[5] + (s[2] - s[5]) * push, s[3], s[4], s[5], s[6], s[7] || 0]; }
function camAt(t) {
  let gi = GROUPS.findIndex((G) => t >= G.a && t < G.b); if (gi < 0) gi = t < 0 ? 0 : GROUPS.length - 1;
  const G = GROUPS[gi]; let v = shotAt(G, t);
  const TR = 0.55;
  if (gi > 0 && t < G.a + TR) { const pv = shotAt(GROUPS[gi - 1], G.a), k = EZ.io(one((t - G.a + 0.0) / TR)); v = pv.map((x, i) => L(x, v[i], k)); }
  return v;
}

/* ---------------------------------------------------------------- guide dot (#gdot) + screen anchors */
const gdot = document.getElementById("gdot");
const _pv = new THREE.Vector3();
function toPage(x, y, z) { _pv.set(x, y, z).project(cam); return [(_pv.x + 1) / 2 * CW, CTOP + (1 - _pv.y) / 2 * CH]; }
function anchor(id, x, y, z, dx = 0, dy = 0) { const el = document.getElementById(id); if (!el) return; const [px, py] = toPage(x, y, z); el.style.left = (px + dx).toFixed(1) + "px"; el.style.top = (py + dy).toFixed(1) + "px"; }

/* ---------------------------------------------------------------- scenes */
// tray with felt + rim; most scenes use T at the origin
function trayT(t, s = 1, x = 0, z = 0) { const g = P.T; g.visible = true; g.position.set(x, 0, z); g.scale.set(s, 1, s); return g; }
const _m4 = new THREE.Matrix4(), _p = new THREE.Vector3(), _sc = new THREE.Vector3();
const ringAt = (n, x, z, s, a) => { const r = P[n]; r.visible = a > 0.01; r.position.set(x, 0.155, z); r.scale.setScalar(s); r.material.opacity = a; };
// common throw timing for a single die landing at word w (impact ~0.25 s before the word, rest 0.35 s after)
const TH = (w, o) => Object.assign({ t0: w - 0.65, ti: w - 0.12, t1: w + 0.38 }, o);
const DIE_GRID10 = Array.from({ length: 10 }, (_, i) => [-2.3 + (i % 5) * 1.15, i < 5 ? -0.75 : 0.75]);
const V10 = [3, 6, 2, 5, 1, 4, 4, 6, 2, 5];
let SCN = [];
function defineScenes() {
  const w = Wd;
  // ---------------------------------------------------------------- s01 hook: one die, lands 6, pips glow
  const s1 = { a: -1, b: S(2) + 0.6 };
  const T1 = { t0: -0.25, ti: 0.95, t1: 1.5, p0: [-3.1, 2.3, 1.0], pi: [-1.9, 0.3], p1: [-1.4, 0.2], v: 6, yaw: 0.35, spin: 13, ax: [0.6, 0.3, 0.75], pre: true, h: 0.8 };
  SCN.push([s1.a, s1.b, (t) => { trayT(t);
    if (t < S(2) + 0.2) { throwDie(P.d0, t, T1); setDieMat(P.d0, t > w("6") - 0.1 ? "win" : "white"); }
    ringAt("ring0", -1.4, 0.2, 1 + 0.25 * bump(t, w("16,7%.") - 0.1, 0.6), U(t, w("6") - 0.15, w("6") + 0.25) * (t < S(2) ? 1 : 0));
    // guide dot: the centre-left pip of the six lifts off towards the stat card
    const k = U(t, w("16,7%.") - 0.25, w("16,7%.") + 0.35, "io");
    if (t > w("6") && t < S(2) + 0.1) { const [px, py] = toPage(-1.4 - 0.23, 1.0, 0.2); const tx = 624, ty = 618; gdot.style.opacity = "1";
      gdot.style.transform = `translate(${L(px, tx, k).toFixed(1)}px, ${(L(py, ty, k) - 120 * Math.sin(Math.PI * k)).toFixed(1)}px) scale(${L(0.7, 1, k).toFixed(3)})`; }
  }]);
  // ---------------------------------------------------------------- s02 ten throws into a 5x2 grid
  SCN.push([S(2) - 0.1, S(3) + 0.5, (t) => { trayT(t);
    const base = w("Lempar", S(2) - 0.1) + 0.05, step = 0.2;
    for (let i = 0; i < 10; i++) { const g = P["d" + i]; const tl = base + 0.35 + i * step;
      if (i === 0) { const k = U(t, S(2) - 0.05, S(2) + 0.45); restDie(g, L(-1.4, DIE_GRID10[0][0], k), L(0.2, DIE_GRID10[0][1], k), 6, L(0.35, 0.1, k)); g.position.y += 0.6 * Math.sin(Math.PI * k); V10[0] = 6; continue; }
      setDieMat(g, "white");
      throwDie(g, t, { t0: tl - 0.5, ti: tl, t1: tl + 0.4, p0: [DIE_GRID10[i][0] - 2.4, 3.2, DIE_GRID10[i][1] - 2.2], pi: [DIE_GRID10[i][0] - 0.25, DIE_GRID10[i][1] - 0.2], p1: DIE_GRID10[i], v: V10[i], yaw: 0.1 + 0.2 * hsh(i), spin: 10 + 3 * hsh(i + 4), ax: [hsh(i), 0.3, hsh(i + 9)] }); }
    setDieMat(P.d0, t > w("83,8%.") - 0.2 ? "win" : "white"); setDieMat(P.d7, t > w("83,8%.") - 0.2 ? "win" : "white");
    const a = U(t, w("83,8%.") - 0.2, w("83,8%.") + 0.2) * (1 - U(t, S(3) + 0.1, S(3) + 0.4));
    ringAt("ring0", DIE_GRID10[0][0], DIE_GRID10[0][1], 0.9, a); ringAt("ring1", DIE_GRID10[7][0], DIE_GRID10[7][1], 0.9, a);
    if (t > S(3)) { const k = U(t, S(3), S(3) + 0.35, "in"); for (let i = 0; i < 10; i++) { const g = P["d" + i]; g.scale.multiplyScalar(Math.max(0.001, 1 - k)); g.position.y -= 0.4 * k; } }
  }]);
  // ---------------------------------------------------------------- s03-s05 a hundred dice rain in (instanced), then the tray tilts away under the type
  SCN.push([S(3) - 0.1, S(6) + 0.1, (t) => { trayT(t); INST.visible = true;
    const t0 = w("Lempar", S(3) - 0.1) - 0.05;
    for (let i = 0; i < N_INST; i++) {
      const cx = -2.7 + (i % 10) * 0.6, cz = -1.62 + Math.floor(i / 10) * 0.36, tl = t0 + 0.3 + (i % 10) * 0.045 + Math.floor(i / 10) * 0.11 + 0.08 * hsh(i);
      const s = 0.42, o = { t0: tl - 0.45, ti: tl, t1: tl + 0.35, p0: [cx + (hsh(i + 1) - 0.5) * 2, 2.6 + 1.2 * hsh(i + 2), cz - 1.2], pi: [cx, cz], p1: [cx, cz], v: hsh(i + 7) < 0.17 ? 6 : 1 + Math.floor(hsh(i + 3) * 5), yaw: hsh(i + 5) * 0.4, spin: 8, s, hb: 0.3 };
      const dummy = { userData: { vals: VALS }, visible: true, scale: _sc, position: _p, quaternion: new THREE.Quaternion() };
      dummy.scale = { setScalar: () => {} }; dummy.position = { set: (x, y, z) => _p.set(x, y, z) };
      const on = throwDie(dummy, t, o);
      if (t < o.t0) _p.set(0, -50, 0);
      if (t > S(6) - 0.5) _p.y -= 6 * U(t, S(6) - 0.5, S(6) + 0.1, "in");
      _m4.compose(_p, dummy.quaternion, _sc.set(s, s, s)); INST.setMatrixAt(i, _m4); }
    INST.instanceMatrix.needsUpdate = true;
    if (t > S(6) - 0.5) { P.T.position.y = -3 * U(t, S(6) - 0.5, S(6) + 0.1, "in"); }
  }]);
  // ---------------------------------------------------------------- s06 the table: dice = idea + approach, trays = markets
  const s6 = S(6), s6e = S(7);
  const SPD = [["d0", "white", -3.6, 2.4, 5], ["d1", "navy", -2.3, 2.6, 3], ["d2", "blue", -1.0, 2.5, 6], ["d3", "sky", 0.3, 2.65, 2], ["nosix", "nosix", 1.6, 2.5, 4], ["d4", "white", 2.9, 2.6, 1]];
  const SPT = [["Tc", -3.9, -1.4, 0.66], ["T", -1.05, -1.5, 0.42], ["Th", 1.8, -1.5, 0.74], ["Tb", 4.25, -1.3, 0.78]];
  SCN.push([s6 - 0.1, s6e + 0.35, (t) => {
    const lift = U(t, s6 - 0.1, s6 + 0.5, "out");
    SPT.forEach(([n, x, z, sc], i) => { const g = P[n]; g.visible = true; const sp = spring(t, s6 + 0.1 + i * 0.12, 0.5); g.position.set(x, -2 * (1 - sp), z); g.scale.set(sc, 1, sc);
      if (t > w("Nampannya") - 0.1) g.position.y += 0.35 * bump(t, w("Nampannya") - 0.05 + i * 0.12, 0.42); });
    SPD.forEach(([n, set, x, z, v], i) => { const g = P[n]; setDieMat(g, set, set === "nosix" ? VALS_NOSIX : VALS); const sp = spring(t, s6 + 0.25 + i * 0.08, 0.5);
      restDie(g, x, z, v, 0.3 * (i - 2.5) * 0.3, 0.9); g.position.y += 2.5 * (1 - sp) + 0.7 * bump(t, w("Dadunya") - 0.05 + i * 0.1, 0.4); });
    // labels ride above the rows
    const ld = U(t, w("Dadunya"), w("Dadunya") + 0.35, "back"); if (ld > 0.01) { show("L_dadu", -0.35, 1.7 + 0.1 * Math.sin(t * 2), 2.55, ld * 2.0); }
    const ln = U(t, w("Nampannya"), w("Nampannya") + 0.35, "back"); if (ln > 0.01) { show("L_nampan", 0.3, 1.5 + 0.1 * Math.sin(t * 2 + 1), -1.2, ln * 1.9); }
    if (t > s6e - 0.3) { const k = U(t, s6e - 0.3, s6e + 0.3, "in"); for (const [n] of SPD) P[n].position.y -= 0; for (const [n] of SPT) if (n !== "T") P[n].position.x *= 1 + 1.6 * k;
      for (const [n] of SPD) P[n].position.z += 4 * k; P.T.position.x = L(P.T.position.x, 0, U(t, s6e - 0.3, s6e + 0.3)); P.T.position.z = L(P.T.position.z, 0, U(t, s6e - 0.3, s6e + 0.3));
      P.T.scale.set(L(0.42, 1, U(t, s6e - 0.3, s6e + 0.3)), 1, L(0.46, 1, U(t, s6e - 0.3, s6e + 0.3))); P.L_dadu.visible = P.L_nampan.visible = false; }
  }]);
  // ---------------------------------------------------------------- s07 kegedean / kekecilan: giant die + tiny die
  SCN.push([S(7) + 0.3, S(10), (t) => { trayT(t);
    const gk = U(t, w("kegedean,") - 0.2, w("kegedean,") + 0.45, "back"), tk = U(t, w("kekecilan.") - 0.2, w("kekecilan.") + 0.4, "back");
    if (t < S(8)) {
      restDie(P.big, -1.5, -0.2, 5, 0.3, Math.max(0.01, L(1, 2.4, gk)) * (gk > 0 ? 1 : 0.0001), 0.12); P.big.visible = gk > 0;
      restDie(P.tiny, 1.8, 0.2, 2, -0.3, Math.max(0.0001, L(1, 0.32, tk)), 0.12); P.tiny.visible = tk > 0;
    }
    // s08: the giant die (ruko 3 lantai) crashes onto the rim, the tray jumps, the die tips over the back
    if (t >= S(8)) { const ti = w("ruko") - 0.05;
      const fall = U(t, w("langsung") - 0.1, ti, "in");
      if (t < ti) { P.big.visible = true; P.big.scale.setScalar(2.4); upQuat(VALS, 5, 0.3 + 2 * fall, P.big.quaternion); P.big.position.set(L(-1.5, -1.6, fall), L(1.32, 6, 1 - fall) * 1, L(-0.2, -1.2, fall)); if (t < w("langsung") - 0.1) P.big.position.y = 1.32 + 0.15 * Math.sin(t * 3); }
      else { const k = U(t, ti, ti + 0.9, "out"); P.big.visible = true; P.big.scale.setScalar(2.4); upQuat(VALS, 5, 0.3, P.big.quaternion);
        _q2.setFromAxisAngle(V3(1, 0, 0), -1.1 * k); P.big.quaternion.premultiply(_q2); P.big.position.set(-1.6, 1.9 - 0.5 * k, -1.2 - 1.3 * k); }
      const jolt = bump(t, ti, 0.35); P.T.position.y = 0.25 * jolt; P.T.rotation.x = -0.12 * jolt;
      const lr = U(t, ti + 0.15, ti + 0.5, "back"); if (lr > 0.01 && t < S(9)) show("L_ruko", -1.6, 1.5, 1.2, lr * 0.95);
      if (t >= S(9)) { // s09 the tiny die: offered once a month — barely rolls
        const ex = U(t, S(9) - 0.05, S(9) + 0.4, "in"); P.big.scale.multiplyScalar(Math.max(0.001, 1 - ex)); if (ex >= 1) P.big.visible = false;
        setDieMat(P.tiny, "white"); throwDie(P.tiny, t, { t0: w("cuma", S(9)) - 0.3, ti: w("nawarin") + 0.1, t1: w("keluarga,") - 0.2, p0: [2.6, 1.4, 0.9], pi: [2.2, 0.8], p1: [1.9, 0.75], v: 2, yaw: -0.3, spin: 3, s: 0.32, hb: 0.2 });
        const lg = U(t, w("grup") - 0.1, w("grup") + 0.3, "back"); if (lg > 0.01) show("L_grup", 1.9, 1.2, 0.75, lg * 0.95);
      }
    }
  }]);
  // ---------------------------------------------------------------- s10 the wrong idea: the die unfolds into its net (no six)
  const FACE_NET = [[0, 0], [1, 0], [-1, 0], [0, -1], [0, 1], [0, 2]];   // net cell per BoxGeometry group order? (computed below)
  P.net = []; { const geo = new THREE.PlaneGeometry(0.98, 0.98); geo.rotateX(-Math.PI / 2);
    for (let i = 0; i < 6; i++) { const m = new THREE.Mesh(geo, SETS.nosix[i]); m.castShadow = true; m.receiveShadow = true; m.visible = false; scene.add(m); P.net.push(m); ALL.push(m); }
    const xm = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ map: ctex(256, 256, (g) => { g.fillStyle = "rgba(255,255,255,0.0)"; g.fillRect(0, 0, 256, 256); g.setLineDash([22, 16]); g.strokeStyle = "#294b77"; g.lineWidth = 12; rr(g, 14, 14, 228, 228, 26); g.stroke();
      g.setLineDash([]); g.fillStyle = "#294b77"; g.textAlign = "center"; g.textBaseline = "middle"; g.font = `700 150px ${FONT}`; g.fillText("6?", 128, 140); }), transparent: true, toneMapped: false }));
    xm.visible = false; scene.add(xm); P.ghost6 = xm; ALL.push(xm); }
  // cube face transforms (local) for group order +x,-x,+y,-y,+z,-z ; net = cross laid flat (z rows), values 1..5,5 visible, slot for the missing 6
  const CUBE = [[0.5, 0.5, 0, 0, 0, -Math.PI / 2], [-0.5, 0.5, 0, 0, 0, Math.PI / 2], [0, 1, 0, 0, 0, 0], [0, 0, 0, Math.PI, 0, 0], [0, 0.5, 0.5, Math.PI / 2, 0, 0], [0, 0.5, -0.5, -Math.PI / 2, 0, 0]];
  const NET = [[1.05, 0.02, 0], [-1.05, 0.02, 0], [0, 0.02, 0], [0, 0.02, 2.1], [0, 0.02, 1.05], [0, 0.02, -1.05]];
  const _e = new THREE.Euler(), _qa = new THREE.Quaternion(), _qb = new THREE.Quaternion();
  SCN.push([S(10) - 0.05, S(11) + 0.05, (t) => { trayT(t, 1);
    const drop = U(t, S(10) - 0.05, S(10) + 0.5, "out"), unf = U(t, w("Dadunya", S(10)) - 0.15, w("Dadunya", S(10)) + 0.75, "io"), sp = (1 - unf) * (t - S(10)) * 1.6;
    for (let i = 0; i < 6; i++) { const m = P.net[i]; m.visible = true; const c = CUBE[i], n = NET[i];
      _e.set(c[3], c[4], c[5]); _qa.setFromEuler(_e); _qb.setFromAxisAngle(Y, sp); _qa.premultiply(_qb); const cp = V3(c[0], c[1], c[2]).applyAxisAngle(Y, sp);
      _q.identity(); m.quaternion.copy(_qa).slerp(_q, unf);
      m.position.set(L(cp.x, n[0], unf), L(cp.y + 2.4 * (1 - drop) + 0.12, n[1] + 0.14, unf), L(cp.z, n[2] - 0.5, unf)); m.scale.setScalar(1); }
    const g6 = U(t, w("angka", S(10)) - 0.1, w("angka", S(10)) + 0.3, "back"); P.ghost6.visible = g6 > 0.01; P.ghost6.position.set(1.05, 0.18, 1.6); P.ghost6.scale.setScalar(Math.max(0.01, g6));
    if (t > S(11) - 0.3) { const k = U(t, S(11) - 0.3, S(11) + 0.05); for (const m of P.net) { m.scale.setScalar(Math.max(0.001, 1 - k)); } P.ghost6.visible = false; }
  }]);
  // ---------------------------------------------------------------- s11 a thousand throws, never a six
  SCN.push([S(11) - 0.05, S(12) + 0.1, (t) => { trayT(t); const t0 = S(11);
    const k = Math.floor((t - t0) / 0.42), lt = t0 + k * 0.42; const v = 1 + Math.floor(hsh(k + 31) * 5);
    throwDie(P.nosix, t, { t0: lt, ti: lt + 0.22, t1: lt + 0.42, p0: [-2.8, 2.6, -1.4], pi: [-0.4 + hsh(k) * 0.6, 0.2], p1: [0.2 + hsh(k + 3) * 0.8, 0.3 - hsh(k + 5) * 0.6], v, yaw: hsh(k + 8), spin: 10, hb: 0.3 });
    if (t > S(12) - 0.25) P.nosix.scale.multiplyScalar(Math.max(0.001, 1 - U(t, S(12) - 0.25, S(12) + 0.1, "in")));
  }]);
  // ---------------------------------------------------------------- s12-s15 unknowns: ? cubes drop on each "baru", flip into dice, five dice thrown together
  const QX = [-2.3, -0.75, 0.75, 2.3], QW = [];
  SCN.push([S(12) - 0.05, S(16) + 0.1, (t) => { trayT(t);
    QW.length = 0; QW.push(w("Produk"), w("pasar", S(13)), w("harga"), w("cara", S(13)));
    const LB = ["L_produk", "L_pasar", "L_harga", "L_cara"];
    for (let i = 0; i < 4; i++) { const g = P["q" + i];
      if (t < S(13)) { // s12: the unknowns hover in a ring above the tray, spinning slowly
        const a = U(t, S(12) + 0.2 + i * 0.15, S(12) + 0.7 + i * 0.15, "back"); g.visible = a > 0.01; g.scale.setScalar(Math.max(0.01, a * 0.85)); const ang = t * 0.6 + i * Math.PI / 2;
        g.position.set(Math.cos(ang) * 2.2, 2.2 + 0.25 * Math.sin(t * 2 + i), Math.sin(ang) * 1.1); g.rotation.set(t * 0.9 + i, t * 1.2 + i, 0.3); continue; }
      // s13: each drops into its slot on its word
      const tw = QW[i], k = U(t, tw - 0.35, tw + 0.05, "in");
      const ang = (S(13)) * 0.6 + i * Math.PI / 2, hx = Math.cos(ang) * 2.2, hz = Math.sin(ang) * 1.1;
      g.visible = true; g.scale.setScalar(L(0.85, 1, k));
      if (t < S(14) + 0.4) { setDieMat(g, "q"); g.position.set(L(hx, QX[i], k), L(2.2, 0.5, k) + 0.3 * bump(t, tw + 0.05, 0.3) * (k >= 1 ? 1 : 0), L(hz, 0.4, k));
        if (k < 1) g.rotation.set(t * 0.9 + i, t * 1.2 + i, 0.3 * (1 - k)); else g.rotation.set(0, 0, 0);
        if (t > w("semuanya") - 0.05 && t < S(14)) { g.position.x += 0.06 * Math.sin((t - w("semuanya")) * 60 + i); g.rotation.z = 0.08 * Math.sin((t - w("semuanya")) * 47 + i); }
        
      }
      // s14: flips into a die that must land on 6 (flip on "dadu tambahan")
      if (t >= S(14) - 0.1 && t < S(15)) { const tf = w("tambahan") - 0.5 + i * 0.12, f = U(t, tf, tf + 0.45, "io");
        setDieMat(g, f > 0.5 ? "white" : "q"); g.quaternion.setFromAxisAngle(V3(0, 0, 1), 3 * Math.PI * f);
        g.position.set(QX[i] * L(1, 0.82, f), 0.5 + 0.9 * Math.sin(Math.PI * f), L(0.4, 0.55, f)); }
    }
    // the main die joins as the fifth (centre)
    if (t >= S(14) && t < S(15)) { const a = U(t, w("satu", S(14)) - 0.2, w("satu", S(14)) + 0.3, "back"); setDieMat(P.d0, "white"); restDie(P.d0, 0, -1.0, 6, 0, Math.max(0.01, a));
      const h6 = U(t, w("harus") - 0.1, w("harus") + 0.3, "back"); if (h6 > 0.01) show("L_six", 0, 2.2, -0.6, h6 * 1.1); }
    // s15: all five thrown together: 6 6 3 6 6 -> fail
    if (t >= S(15)) { const tl = w("sekaligus?") + 0.1, FV = [6, 6, 3, 6, 6], FX = [-2.4, -1.2, 0, 1.2, 2.4];
      const ds = [P.q0, P.q1, P.d0, P.q2, P.q3];
      ds.forEach((g, i) => { setDieMat(g, t > tl + 0.5 && FV[i] === 6 ? "win" : "white"); throwDie(g, t, { t0: tl - 0.75, ti: tl - 0.05 + i * 0.05, t1: tl + 0.5 + i * 0.05, p0: [FX[i] - 1.5, 3.5, -2.6], pi: [FX[i] - 0.2, -0.2], p1: [FX[i], 0.2], v: FV[i], yaw: 0.15 * (i - 2), spin: 11 + i, ax: [hsh(i + 2), 0.4, hsh(i + 6)] }); });
      const lm = U(t, tl + 0.55, tl + 0.85, "back"); if (lm > 0.01) show("L_miss", 0, 1.55, 0.2, lm * 0.8);
      if (t > S(16) - 0.35) { const k = U(t, S(16) - 0.35, S(16) + 0.1, "in"); ds.forEach((g) => g.scale.multiplyScalar(Math.max(0.001, 1 - k))); P.L_miss.visible = false; }
    }
  }]);
  // ---------------------------------------------------------------- s16-s18 tray too small: the tray shrinks, the die bounces out
  SCN.push([S(16) - 0.05, S(19) + 0.05, (t) => {
    const k = U(t, w("nampannya") - 0.1, w("kekecilan.", S(16)) + 0.3, "io");
    trayT(t, L(1, 0.5, k)); P.T.visible = k < 0.999; P.T.position.x = 0;
    const sm = P.Ts; sm.visible = k > 0.98; sm.position.set(L(0, -1.6, U(t, w("kekecilan.", S(16)) + 0.3, S(17) + 0.4)), 0, 0.2); sm.scale.set(1, 1, 1); if (k > 0.98) P.T.visible = false;
    if (t > S(18)) { const tl = w("dadunya", S(18)); setDieMat(P.d0, "white");
      // arrives, hits the near rim, bounces high and leaves to the right
      const t0 = tl - 0.55, ti = tl - 0.05, t2 = tl + 0.9;
      if (t >= t0) { P.d0.visible = true; let x, y, z; if (t < ti) { const u = one((t - t0) / (ti - t0)); x = L(-4.6, -2.0, u); z = L(-1.6, 0.85, u); y = L(3.2, 0.95, u * u) + 1.2 * u * (1 - u); }
        else { const u = one((t - ti) / (t2 - ti)); x = L(-2.0, 5.2, u); z = L(0.85, 2.4, u); y = 0.95 + 2.4 * Math.sin(Math.PI * Math.min(1, u * 1.1)) - 2.5 * u * u; }
        P.d0.position.set(x, y, z); upQuat(VALS, 3, 0, _q); _q2.setFromAxisAngle(V3(0.6, 0.2, 0.7).normalize(), (t - t0) * 11); P.d0.quaternion.copy(_q).multiply(_q2); P.d0.scale.setScalar(0.8); }
    }
  }]);
  // ---------------------------------------------------------------- s19-s22 tray without a floor: the felt falls away, the die drops through
  SCN.push([S(19) - 0.05, S(23) + 0.05, (t) => { const g = trayT(t, 0.8); const fl = g.userData.floor;
    const k = U(t, w("tanpa") - 0.05, w("lantai.", S(19)) + 0.35, "in"); fl.position.y = 0.07 - 3.5 * k; fl.visible = k < 0.98; fl.material.transparent = true; fl.material.opacity = 1 - k;
    g.rotation.y = 0.25 * Math.sin((t - S(19)) * 0.5);
    if (k > 0.05 && t < S(23) - 0.2) { const pt = P.pit; pt.visible = true; pt.position.set(0, 0.01, 0); pt.rotation.z = g.rotation.y; pt.scale.set(6.4 * 0.8 * k, 4.0 * 0.8 * k, 1); pt.material.opacity = k; }
    if (t > S(22) - 0.6) { const tl = w("lolos"); setDieMat(P.d0, "white"); P.d0.visible = t > tl - 0.6;
      const u = one((t - (tl - 0.6)) / 0.6), u2 = one((t - tl) / 0.7); P.d0.scale.setScalar(0.8);
      P.d0.position.set(L(-2.5, 0, u), t < tl ? L(3.0, 0.6, u * u) : 0.6 - 6 * u2 * u2, L(-1.2, 0.2, u)); upQuat(VALS, 4, 0, _q); _q2.setFromAxisAngle(V3(0.5, 0.3, 0.8).normalize(), (t - tl) * 8); P.d0.quaternion.copy(_q).multiply(_q2); }
    if (t > S(23) - 0.2) { fl.position.y = 0.07; fl.visible = true; fl.material.opacity = U(t, S(23) - 0.2, S(23) + 0.2); }
  }]);
  // ---------------------------------------------------------------- s23-s24 limited throws: three dice = three tries, spent on modal / waktu / tenaga
  const LIVES = [-1.2, 0, 1.2];
  SCN.push([S(23) - 0.05, S(25) + 0.1, (t) => { trayT(t, 1, 0, -0.6);
    const use = [w("Modal,"), w("waktu,"), w("tenaga")];
    LIVES.forEach((x, i) => { const g = P["d" + (i + 1)]; setDieMat(g, "white"); const a = U(t, w("lemparanmu") - 0.1 + i * 0.12, w("lemparanmu") + 0.35 + i * 0.12, "back");
      if (t < use[i] - 0.1) { restDie(g, x, 1.75, [1, 3, 5][i], 0.2, Math.max(0.01, a * 0.8)); g.position.y += 0.06 * Math.sin(t * 3 + i); }
      else { throwDie(g, t, { t0: use[i] - 0.1, ti: use[i] + 0.3, t1: use[i] + 0.7, p0: [x, 0.4, 1.75], pi: [x * 0.6 - 0.3, -0.3], p1: [x * 0.8, -0.9 + 0.3 * i], v: [2, 4, 5][i], yaw: 0.3 * i, spin: 9, h: 1.4, s: 0.8 });
        if (t > use[i] + 0.7) { const fd = U(t, use[i] + 0.8, use[i] + 1.2); g.scale.setScalar(0.8 * (1 - 0.0 * fd)); } } });
    if (t > S(25) - 0.3) { const k = U(t, S(25) - 0.3, S(25) + 0.1, "in"); for (let i = 1; i <= 3; i++) P["d" + i].scale.multiplyScalar(Math.max(0.001, 1 - k)); }
  }]);
  // ---------------------------------------------------------------- s25-s27 cara A: every miss, swap the die AND the tray (chaos)
  const CHT = ["T", "Th", "Tb", "Tc", "Tf"], CHD = ["white", "navy", "blue", "sky", "white"];
  SCN.push([S(25) - 0.05, S(28) + 0.1, (t) => {
    const la = U(t, w("Ada") - 0.1, w("Ada") + 0.3, "back") * (1 - U(t, S(26) - 0.2, S(26))), lb = U(t, w("dua") - 0.1, w("dua") + 0.3, "back") * (1 - U(t, S(26) - 0.2, S(26)));
    if (t < S(26)) { trayT(t, 0.8); 
      restDie(P.d5, -2.0, 0.2, 2, 0.2, 0.8); P.d5.visible = la > 0.01; setDieMat(P.d5, "navy"); restDie(P.d6, 2.0, 0.2, 5, -0.2, 0.8); P.d6.visible = lb > 0.01; setDieMat(P.d6, "white"); return; }
    const per = 0.62, k = Math.floor((t - S(26)) / per), lt = S(26) + k * per;
    for (let j = 0; j < 2; j++) { const kk = k * 2 + j, tn = CHT[(kk * 3 + j) % CHT.length]; const tg = P[tn]; if (tg.visible) continue; tg.visible = true;
      const ss = tn === "T" ? 0.55 : tn === "Tf" ? 0.8 : 1.15; const pop = spring(t, lt + 0.05 * j, 0.3); const x0 = j ? 2.2 : -2.2;
      tg.position.set(x0 + ((kk * 7) % 3 - 1) * 0.5, 0, ((kk * 5) % 3 - 1) * 0.6); tg.scale.set(ss * (0.6 + 0.4 * pop), 1, ss * (0.6 + 0.4 * pop)); if (tn === "Tf") tg.userData.floor.visible = false;
      const g = P[j ? "d9" : "d8"]; setDieMat(g, CHD[(kk + j) % CHD.length]); const tj = lt + 0.3 * j, v = 1 + Math.floor(hsh(kk + 77) * 5);
      throwDie(g, t, { t0: tj - 0.02, ti: tj + 0.26, t1: tj + 0.55, p0: [x0 - 2.2, 1.6, 0.6], pi: [tg.position.x + (hsh(kk + 3) - 0.5) * 1.6, tg.position.z + 0.2], p1: [tg.position.x + (hsh(kk + 4) - 0.5) * 2.4, tg.position.z + (hsh(kk + 9) - 0.5) * 1.6], v, yaw: hsh(kk + 1), spin: 9, s: 0.7 }); }
  }]);
  // ---------------------------------------------------------------- s28-s30 cara B: lock the die and the tray, change only the throw (ghost arcs converge)
  const ARC = [[-2.4, 0.5, 0.9, 2.6, 0.9, 1.5], [-2.4, 0.5, 0.9, 1.3, 0.5, 1.3], [-2.4, 0.5, 0.9, 0.2, 0.15, 1.1]];   // p0 + landing x,z + apex
  SCN.push([S(28) - 0.05, S(31) + 0.05, (t) => { trayT(t); setDieMat(P.d0, "white");
    const lk = [U(t, w("kunci") - 0.2, w("kunci") + 0.25, "in"), U(t, w("kunci") - 0.05, w("kunci") + 0.4, "in")];
    const thr = [w("Dadu", S(29)) + 0.1, w("ubah") - 0.1, w("Tiap", S(30)) + 0.1];
    let landed = 0;
    // three throws, each closer to the centre; the third lands six
    let done = false;
    for (let j = 2; j >= 0; j--) { if (t >= thr[j] - 0.55) { const a = ARC[j]; throwDie(P.d0, t, { t0: thr[j] - 0.55, ti: thr[j], t1: thr[j] + 0.45, p0: [a[0], a[1], a[2]], pi: [a[3] - 0.3, a[4] - 0.1], p1: [a[3], a[4]], v: [3, 2, 6][j], yaw: 0.2, spin: 10, h: a[5] });
        landed = j; done = true; break; } }
    if (!done) restDie(P.d0, -2.4, 0.9, 1, 0.3, 1, 0.0);
    if (t >= thr[2] + 0.4) setDieMat(P.d0, "win");
    // padlocks: one on the die, one on the tray rim
    const dp = P.d0.position; if (lk[0] > 0) { const g = P.lockA; g.visible = true; g.position.set(t < thr[0] - 0.55 ? -2.4 : dp.x, (t < thr[0] - 0.55 ? 1.0 : dp.y + 0.55) + 2.5 * (1 - lk[0]), t < thr[0] - 0.55 ? 0.9 : dp.z); g.scale.setScalar(0.85);
      g.userData.sh.position.y = 0.5 + 0.1 * (1 - U(t, w("kunci") + 0.2, w("kunci") + 0.35)); }
    if (lk[1] > 0) { const g = P.lockB; g.visible = true; g.position.set(2.6, 0.5 + 2.5 * (1 - lk[1]), 2.25); g.scale.setScalar(0.9); g.userData.sh.position.y = 0.5 + 0.1 * (1 - U(t, w("kunci") + 0.35, w("kunci") + 0.5)); }
    // ghost arcs (dot trails) of the earlier throws
    let n = 0; P.dots.visible = true;
    for (let j = 0; j < 3; j++) { const a = ARC[j]; const vis = t > thr[j] + 0.05; for (let q = 0; q < 14; q++) { const u = q / 13, x = L(a[0], a[3] - 0.3, u), z = L(a[2], a[4] - 0.1, u), y = L(a[1], 0.5, u * u) + 4 * a[5] * u * (1 - u);
        const sc = vis ? (j === 2 ? 1.0 : 0.7) * U(t, thr[j] + 0.05 + u * 0.3, thr[j] + 0.2 + u * 0.3) * (1 - 0.6 * U(t, S(31) - 0.3, S(31))) : 0;
        _m4.compose(_p.set(x, y, z), _q.identity(), _sc.set(sc, sc, sc)); P.dots.setMatrixAt(n++, _m4); } }
    for (; n < 64; n++) { _m4.compose(_p.set(0, -50, 0), _q.identity(), _sc.set(0, 0, 0)); P.dots.setMatrixAt(n, _m4); } P.dots.instanceMatrix.needsUpdate = true;
    ringAt("ring0", ARC[2][3], ARC[2][4], 0.9, U(t, thr[2] + 0.45, thr[2] + 0.75));
  }]);
  // ---------------------------------------------------------------- s31 pick the right idea (die on a ring), s32 the market grows
  SCN.push([S(31) - 0.05, S(33) + 0.05, (t) => {
    const gr = U(t, w("besar") - 0.2, w("tumbuh.") + 0.2, "io"); trayT(t, L(1, 1.22, gr));
    setDieMat(P.d0, "win"); restDie(P.d0, L(0.2, 0, U(t, S(31), S(31) + 0.5)), L(0.15, 0, U(t, S(31), S(31) + 0.5)), 6, 0.2 + 0.4 * U(t, S(31), S(32)), 1, 0.25 * bump(t, w("ide", S(31)) - 0.05, 0.4));
    ringAt("ring0", P.d0.position.x, P.d0.position.z, 1.1 + 0.15 * Math.sin(t * 4), U(t, w("ide", S(31)) - 0.1, w("ide", S(31)) + 0.3) * (1 - U(t, S(32), S(32) + 0.3)));
    const li = U(t, w("tepat,") - 0.1, w("tepat,") + 0.3, "back") * (1 - U(t, S(32) - 0.2, S(32))); if (li > 0.01) show("L_ide", -2.6, 1.3, 0.3, li * 0.8);
    if (t > S(32)) { const a = U(t, w("pasar,", S(32)) - 0.1, w("pasar,", S(32)) + 0.4, "back"); const ag = P.arrow; ag.visible = a > 0.01; ag.position.set(-4.4, 0, -0.6); ag.scale.set(Math.max(0.01, a), Math.max(0.01, a) * L(0.6, 1.25, gr), Math.max(0.01, a));
      const lt = U(t, w("idealnya") - 0.1, w("idealnya") + 0.3, "back");  }
    if (t > S(33) - 0.25) { P.arrow.visible = false; P.L_tepat.visible = false; }
  }]);
  // ---------------------------------------------------------------- s33 misses once -> the idea gets yanked away and swapped
  SCN.push([S(33) - 0.05, S(34) + 0.1, (t) => { trayT(t);
    const tl = w("Ganti", S(33)) - 0.2; setDieMat(P.d0, "white");
    if (t < S(33) + 0.3) restDie(P.d0, 0, 0, 6, 0.4, 1, 3.0 * U(t, S(33) - 0.05, S(33) + 0.3, "in"));
    else { throwDie(P.d0, t, { t0: S(33) + 0.3, ti: tl, t1: tl + 0.4, p0: [-3.2, 2.8, -1.4], pi: [-0.5, -0.2], p1: [-0.1, 0.1], v: 3, yaw: 0.2, spin: 10 });
      const yk = U(t, w("meleset") - 0.05, w("meleset") + 0.4, "in"); P.d0.position.y += 2.2 * yk; P.d0.position.x += 4.5 * yk; P.d0.scale.multiplyScalar(Math.max(0.001, 1 - yk));
      if (t > w("meleset") + 0.2) { setDieMat(P.d9, "navy"); throwDie(P.d9, t, { t0: w("meleset") + 0.2, ti: w("sekali.", S(33)) + 0.05, t1: w("sekali.", S(33)) + 0.45, p0: [3.6, 3.2, -1.2], pi: [0.6, 0.1], p1: [0.3, 0.2], v: 2, yaw: -0.3, spin: 10 }); }
      if (t > S(34) - 0.2) { const k = U(t, S(34) - 0.2, S(34) + 0.1, "in"); P.d9.scale.multiplyScalar(Math.max(0.001, 1 - k)); P.T.position.y -= 3 * k; } }
  }]);
  // ---------------------------------------------------------------- s34-s36 shiny object syndrome: target path, the gem pulls the die off course, back to zero
  const PATH = (u) => [L(-3.6, 3.4, u), 0.5, -0.6 + 0.9 * Math.sin(Math.PI * u) * 0.0];
  SCN.push([S(34) - 0.05, S(37) + 0.05, (t) => {
    const gem = P.gem; const ga = U(t, w("shiny") - 0.25, w("shiny") + 0.3, "back");
    if (t < S(35)) { gem.visible = ga > 0.01; gem.position.set(0, 1.5 + 0.12 * Math.sin(t * 2.4), 0); gem.scale.setScalar(Math.max(0.01, ga * 1.5)); gem.userData.m.rotation.y = t * 1.6;
      gem.userData.sp.forEach((s, i) => { const a = t * 1.3 + i * 1.57; s.position.set(Math.cos(a) * 1.0, 0.6 * Math.sin(t * 3 + i * 2), Math.sin(a) * 0.5); const k = 0.5 + 0.5 * Math.sin(t * 9 + i * 1.7); s.scale.set(0.25 + 0.35 * k, 0.25 + 0.35 * k, 1); }); return; }
    // the path to the target
    const tg = P.target; tg.visible = true; tg.position.set(3.6, 0, -0.6); tg.scale.setScalar(spring(t, S(35) - 0.1, 0.5)); tg.userData.fl.rotation.y = 0.15 * Math.sin(t * 3);
    const lt = U(t, w("target,") - 0.1, w("target,") + 0.3, "back"); 
    const prog = t < w("kinclong,") ? 0.62 * U(t, S(35) + 0.1, w("kinclong,"), "sine") : 0.62;
    const veer = U(t, w("banting") - 0.05, w("sana.") + 0.1, "io");
    const back = U(t, w("Semuanya") - 0.05, w("nol") + 0.2, "io");
    const pp = PATH(prog * (1 - back));
    const gx = 0.6, gz = 1.9;
    let x = L(pp[0], gx - 0.8, veer), z = L(pp[2], gz - 0.1, veer);
    if (back > 0) { x = L(L(PATH(0.62)[0], gx - 0.8, 1), -3.6, back); z = L(gz - 0.1, -0.6, back); }
    setDieMat(P.d0, "white"); restDie(P.d0, x, z, 5, 0, 0.9); upQuat(VALS, 5, 0, _q); _q2.setFromAxisAngle(V3(0, 0, -1), (x + 3.6) / 0.45); P.d0.quaternion.copy(_q).premultiply(_q2);
    { const a2 = Math.abs((x + 3.6) / 0.45) % (Math.PI / 2); P.d0.position.y = 0.45 * (Math.abs(Math.cos(a2)) + Math.abs(Math.sin(a2))); }
    // dotted route: done part fades, the rest waits
    let n = 0; P.dots.visible = true;
    for (let q = 0; q < 22; q++) { const u = q / 21, p = PATH(u); const sc = (1 - 0.5 * U(t, w("banting"), w("banting") + 0.4)) * spring(t, S(35) + q * 0.02, 0.4) * (u < prog * (1 - back) ? 0.55 : 1);
      _m4.compose(_p.set(p[0], 0.06, p[2] + 0.75), _q.identity(), _sc.set(sc, 0.4 * sc, sc)); P.dots.setMatrixAt(n++, _m4); }
    for (; n < 64; n++) { _m4.compose(_p.set(0, -50, 0), _q.identity(), _sc.set(0, 0, 0)); P.dots.setMatrixAt(n, _m4); } P.dots.instanceMatrix.needsUpdate = true;
    // the gem pops up beside the route
    const ge = U(t, w("kinclong,") - 0.25, w("kinclong,") + 0.2, "back") * (1 - U(t, w("Semuanya"), w("Semuanya") + 0.3));
    gem.visible = ge > 0.01; gem.position.set(gx, 1.2 + 0.1 * Math.sin(t * 2.4), gz); gem.scale.setScalar(Math.max(0.01, ge * 0.9)); gem.userData.m.rotation.y = t * 1.6;
    gem.userData.sp.forEach((s, i) => { const a = t * 1.3 + i * 1.57; s.position.set(Math.cos(a) * 1.0, 0.5 * Math.sin(t * 3 + i * 2), Math.sin(a) * 0.5); const k = 0.5 + 0.5 * Math.sin(t * 9 + i * 1.7); s.scale.set(0.25 + 0.35 * k, 0.25 + 0.35 * k, 1); });
    const lk = U(t, w("kinclong,") - 0.05, w("kinclong,") + 0.3, "back") * (1 - U(t, w("Semuanya") - 0.1, w("Semuanya") + 0.2)); if (lk > 0.01) show("L_shiny", gx, 2.6, gz, lk * 0.95);
  }]);
  // ---------------------------------------------------------------- s37-s38 the opposite: inspect markets (trays) with the magnifier, pick one; then the idea
  const TR3 = [["Tb", -3.1, -0.6, 0.95], ["Tf", 0.0, -0.9, 0.75], ["T", 3.1, -0.6, 0.5]], DI3 = [["d1", "navy", -2.0, 2.4, 2], ["nosix", "nosix", 0, 2.5, 4], ["d2", "white", 2.0, 2.4, 6]];
  SCN.push([S(37) - 0.05, S(39) + 0.1, (t) => {
    const intro = spring(t, S(37) + 0.1, 0.5);
    TR3.forEach(([n, x, z, sc], i) => { const g = P[n]; g.visible = true; g.position.set(x, -1.5 * (1 - spring(t, S(37) + 0.05 + i * 0.1, 0.5)), z); g.scale.set(sc, 1, sc);
      if (n === "Tf") { g.userData.floor.visible = false; } });
    DI3.forEach(([n, set, x, z, v], i) => { const g = P[n]; setDieMat(g, set, set === "nosix" ? VALS_NOSIX : VALS); restDie(g, x, z, v, 0.2, 0.75); g.position.y += 2 * (1 - spring(t, S(37) + 0.3 + i * 0.1, 0.5)); });
    // magnifier: hover over trays (milih pasar ... diteliti), settle on the big tray; then over the dice, settle on the white die
    const m = P.mag; const mv = t > w("pasar", S(38)) - 0.4;
    if (mv) { m.visible = true; const tA = w("pasar", S(38)) - 0.4, tB = w("dulu."), tC = w("Milih", S(38)), tD = w("hati-hati.", S(38));
      let x, z, y = 1.7; if (t < tB) { const u = one((t - tA) / (tB - tA)); x = L(-3.1, 3.1, EZ.io(u)); z = -0.6; }
      else if (t < tC) { x = 3.1; z = -0.6; } else { const u = U(t, tC, tD); x = L(3.1, 2.0, u); z = L(-0.6, 2.4, u); y = L(1.7, 1.5, u); }
      m.position.set(x, y + 0.08 * Math.sin(t * 3), z); m.rotation.set(-1.1, 0, 0.2); m.scale.setScalar(1.0); }
    const pick = U(t, w("dulu.") - 0.1, w("dulu.") + 0.35, "io");
    ringAt("ring0", 3.1, -0.6, 2.0, pick); if (pick > 0) { P.Tb.position.y -= 1.2 * pick; P.Tf.position.y -= 1.2 * pick; }
    const pickD = U(t, w("hati-hati.", S(38)) - 0.1, w("hati-hati.", S(38)) + 0.3, "io"); ringAt("ring1", 2.0, 2.4, 1.0, pickD);
    if (pickD > 0) { P.d1.position.y -= 1.5 * pickD; P.nosix.position.y -= 1.5 * pickD; }
    if (t > S(39) - 0.35) { const k = U(t, S(39) - 0.35, S(39) + 0.1, "in"); m.scale.multiplyScalar(Math.max(0.001, 1 - k)); P.d2.scale.multiplyScalar(Math.max(0.001, 1 - k)); P.T.position.y -= 3 * k; }
  }]);
  // ---------------------------------------------------------------- s39-s40 refine product / offer / price / channel (the process fill is UI), then the six
  SCN.push([S(39) - 0.05, S(41) + 0.4, (t) => { trayT(t);
    const tw = [w("produknya,"), w("penawarannya,"), w("harganya,"), w("jualannya.")];
    const tl = w("6.", S(40)) - 0.05;
    if (t < S(40) - 0.1) { setDieMat(P.d0, "white"); restDie(P.d0, -2.6, 1.0, 1, 0.3, 0.9); P.d0.position.y = 0.45 + 0.25 * Math.max(...tw.map((x) => bump(t, x, 0.35)));
      P.d0.rotation.y += 0.25 * tw.filter((x) => t > x).length; }
    else { setDieMat(P.d0, t > tl + 0.3 ? "win" : "white"); throwDie(P.d0, t, { t0: S(40) - 0.1, ti: tl, t1: tl + 0.45, p0: [-2.6, 0.9, 1.0], pi: [-0.3, 0.05], p1: [0, 0], v: 6, yaw: 0.3, spin: 12, h: 1.8 }); }
    ringAt("ring0", 0, 0, 1.0 + 1.6 * U(t, tl + 0.4, tl + 1.0, "out"), U(t, tl + 0.35, tl + 0.5) * (1 - U(t, tl + 0.8, tl + 1.1)));
    // the guide dot: the six's centre-left pip -> floods the frame into the AI beat (UI handles the flood circle)
    if (t > tl + 0.45 && t < S(41) + 0.4) { const [px, py] = toPage(-0.23, 1.0, 0); gdot.style.opacity = "1"; const k = U(t, tl + 0.55, tl + 0.95, "in");
      gdot.style.transform = `translate(${px.toFixed(1)}px, ${py.toFixed(1)}px) scale(${(0.7 + 140 * k * k).toFixed(3)})`; }
    if (t > S(41) - 0.05) { const k = U(t, S(41) - 0.05, S(41) + 0.3); P.T.position.y -= 4 * k; P.d0.position.y -= 4 * k; }
  }]);
  // ---------------------------------------------------------------- s42 not about the number of throws: a storm of dice blows across, then clears
  SCN.push([S(42) - 0.05, S(43) + 0.1, (t) => { trayT(t, 1);
    INST.visible = true;
    for (let i = 0; i < N_INST; i++) { const tl = S(42) + 0.05 + hsh(i + 11) * 1.6, u = (t - tl) / 1.2;
      const vis = u > 0 && u < 1; const x = L(-7, 7, u), y = 0.3 + 0.8 * Math.sin(Math.PI * one(u)) * (0.5 + hsh(i + 2)), z = -2.0 + 4.2 * hsh(i + 5);
      _q.setFromEuler(_e.set(t * 7 + i, t * 5 + i * 2, i)); const s = vis ? 0.42 : 0; _m4.compose(_p.set(x, y, z), _q, _sc.set(s, s, s)); INST.setMatrixAt(i, _m4); }
    INST.instanceMatrix.needsUpdate = true;
  }]);
  // ---------------------------------------------------------------- s43-s45 the rule: one die, one tray, the throw lands six; stays for the CTA
  SCN.push([S(43) - 0.05, R.D + 1, (t) => { const ti = U(t, S(43) - 0.05, S(43) + 0.4, "out"); trayT(t); P.T.position.y = 0;
    const d1 = U(t, w("dadu", S(43)) - 0.15, w("dadu", S(43)) + 0.25, "back");
    const tl = w("ganti", S(43)) + 0.15;
    setDieMat(P.d0, t > tl + 0.4 ? "win" : "white");
    if (t < tl - 0.55) { restDie(P.d0, -2.4, 1.2, 2, 0.3, Math.max(0.01, d1), 1.2 + 0.1 * Math.sin(t * 2)); P.d0.rotation.y += t * 0.8; }
    else throwDie(P.d0, t, { t0: tl - 0.55, ti: tl, t1: tl + 0.45, p0: [-2.4, 1.7, 1.2], pi: [-0.25, 0.05], p1: [0, 0.05], v: 6, yaw: 0.3, spin: 12, h: 1.2 });
    const tn = U(t, w("nampan", S(43)) - 0.15, w("nampan", S(43)) + 0.3, "out"); P.T.position.y = 0.35 * bump(t, w("nampan", S(43)) - 0.1, 0.4);
    ringAt("ring0", 0, 0.05, 1.05 + 0.1 * Math.sin(t * 3), U(t, tl + 0.4, tl + 0.7));
    // CTA end: the world steps back a little (the page dims it)
  }]);
}

/* ---------------------------------------------------------------- render */
let ready = false;
function render(t) {
  if (!ready) return;
  for (const o of ALL) o.visible = false;
  INST.visible = false; P.dots.visible = false;
  P.T.position.set(0, 0, 0); P.T.rotation.set(0, 0, 0); P.T.scale.set(1, 1, 1); P.T.userData.floor.position.y = 0.07; P.T.userData.floor.visible = true; P.T.userData.floor.material.opacity = 1;
  for (const n of ["Tf"]) P[n].userData.floor.visible = n !== "Tf";
  gdot.style.opacity = "0";
  for (const [a, b, f] of SCN) if (t >= a && t < b) f(t);
  const v = camAt(t), hx = 0.03 * Math.sin(t * 0.7), hy = 0.02 * Math.sin(t * 0.9 + 1);
  const A = v[7], FH = CH + 2 * A; cam.fov = (2 * Math.atan(Math.tan((v[6] * Math.PI) / 360) * FH / CH) * 180) / Math.PI;
  cam.setViewOffset(CW, FH, 0, 0, CW, CH); cam.position.set(v[0] + hx, v[1] + hy, v[2]); cam.updateProjectionMatrix(); cam.lookAt(v[3], v[4], v[5]); cam.updateMatrixWorld();
  key.target.position.set(v[3], 0, v[5]); key.position.set(v[3] - 5, 11, v[5] + 7);
  renderer.render(scene, cam);
}
window.DW = { render, toPage, cam, P, scene };
const PR = Promise.all([document.fonts.load(`700 60px Poppins`), document.fonts.load(`400 60px Poppins`)]).then(() => {
  build(); P.Tf.userData.floor.visible = false; defineScenes(); ready = true; render(window.__T0dev || 0);
});
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady.world = PR;
window.addEventListener("hf-seek", (e) => { const t = e.detail.time; if (ready) render(t); else if (e.detail.waitUntil) e.detail.waitUntil(PR.then(() => render(t))); });
