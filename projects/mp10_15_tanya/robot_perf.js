// MasterPajak AI robot host — Video 15 'Tanya Cepat ke Robot' (FAQ: the robot is the star). Beat times come from window.TM.
// Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle layers (hover,
// breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived secondary
// motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
// Acting: pops up big at the bottom centre and waves, counts the three numbered questions with head tilts -> glides right
// for Q1 (reads, thinks with a head tilt, nods "Perlu." and presents the answer card) -> hops left with the chat scroll for
// Q2 (leans back at the falling book, shakes its head "Nggak harus.", flicks the book away) -> ducks under the bands ->
// brand: half-body bottom-left with the chest hologram, points at the tidy report -> glides right for Q3 ("ta-da" with a
// chest glow: the asisten AI is the robot itself, then points at the AI card and the tim ahli card) -> end card.
// Mouth channel `mo` stays 0 during speech: lip-sync drives the mouth once the VO exists. Face stays camera-readable on VO lines.
(function () {
  const KEYS = {};
  const RAW = { op: 1, holoA: 1, holoRev: 1, holoGl: 1, hx: 1, hy: 1, hw: 1 };
  const key = (ch, t, v, e) => { (KEYS[ch] = KEYS[ch] || []).push([t, v, e || "io"]); };
  const EASE = { io: (p) => p * p * p * (p * (p * 6 - 15) + 10), o: (p) => 1 - Math.pow(1 - p, 3), i: (p) => p * p * p, lin: (p) => p, hold: (p) => (p < 1 ? 0 : 1) };
  const DEF = { x: 790, y: 2250, h: 560, op: 1, yaw: 0, pitch: 0, roll: 0, hYaw: 0, hPitch: 0, hRoll: 0,
    lR: 6, lF: 0, lB: 6, lY: 0, rR: 6, rF: 0, rB: 6, rY: 0, lookX: 0, lookY: 0, happy: 0, xe: 0, smile: 1, mo: 0, squint: 0, rim: 1, sh: 0.32,
    chest: 0, holoA: 0, holoRev: 0, holoGl: 0, hx: 720, hy: 1520, hw: 420 };
  function raw(ch, t) {
    const ks = KEYS[ch]; if (!ks) return DEF[ch];
    if (t <= ks[0][0]) return ks[0][1];
    for (let i = 0; i < ks.length - 1; i++) { const a = ks[i], b = ks[i + 1]; if (t < b[0]) { const p = (t - a[0]) / (b[0] - a[0]); return a[1] + (b[1] - a[1]) * EASE[b[2]](p); } }
    return ks[ks.length - 1][1];
  }
  const DT = 1 / 90, KER = {};
  function kernel(f, z) {
    const id = f + "_" + z; if (KER[id]) return KER[id];
    const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - z * z), n = Math.min(160, Math.ceil(5 / (z * w) / DT)); const k = []; let s = 0;
    for (let i = 0; i < n; i++) { const tau = i * DT, h = Math.exp(-z * w * tau) * Math.sin(wd * tau); k.push(h); s += h; }
    for (let i = 0; i < n; i++) k[i] /= s; return (KER[id] = k);
  }
  // hard cuts (robot off-frame when it jumps): springs never look back across them
  const CUTS = [window.TM.sol - 0.05, window.TM.end - 0.01];
  const lastCut = (t) => { let c = -1e9; for (const q of CUTS) if (q <= t) c = q; return c; };
  function filt(ch, t, f, z) { const c = lastCut(t), k = kernel(f, z); let y = 0; for (let i = 0; i < k.length; i++) y += k[i] * raw(ch, Math.max(c, t - i * DT)); return y; }
  const GRP = { pos: [1.5, 0.74], body: [1.7, 0.6], head: [2.3, 0.52], arm: [2.0, 0.56], look: [5.5, 0.92], face: [4.0, 0.95] };
  const G = { x: "pos", y: "pos", h: "pos", yaw: "body", pitch: "body", roll: "body", hYaw: "head", hPitch: "head", hRoll: "head",
    lR: "arm", lF: "arm", lB: "arm", lY: "arm", rR: "arm", rF: "arm", rB: "arm", rY: "arm", lookX: "look", lookY: "look",
    happy: "face", xe: "face", smile: "face", mo: "face", squint: "face", rim: "face", sh: "face", chest: "face" };
  const F = (ch, t) => (RAW[ch] ? raw(ch, t) : filt(ch, t, GRP[G[ch]][0], GRP[G[ch]][1]));
  const hover = (t, h) => Math.sin((2 * Math.PI * t) / 1.9) * 0.012 * h;
  const BLINKS = []; for (let t = 1.3; t < window.TM.total; t += 2.3 + 0.6 * Math.sin(t * 7.1)) BLINKS.push(t);
  function blink(t) { let b = 0; for (const t0 of BLINKS) { const u = (t - t0) / 0.15; if (u > 0 && u < 1) b = Math.max(b, Math.sin(Math.PI * u)); } return b; }
  const LS = window.LIPSYNC || { fps: 60, open: [], wide: [] };
  const lip = (arr, t) => { const f = t * LS.fps, i = Math.floor(f), u = f - i; const a = arr[i] || 0, b = arr[i + 1] || 0; return a + (b - a) * u; };

  // ---------------- choreography (all times from window.TM, so a VO re-time moves everything) ----------------
  const TM = window.TM;
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const NAVY = { sh: 0.5, rim: 2.0 }, LIGHT = { sh: 0.32, rim: 1.0 };
  const REST = (t) => { armL(t, 15, 0, 10, 0); armR(t, 15, 0, 10, 0); };
  const wave = (arm, t0, n) => { arm(t0, 15, 0, 10, 0); arm(t0 + 0.25, 145, 0, 30, 90, "o"); for (let j = 0; j < n; j++) arm(t0 + 0.47 + j * 0.22, 145, 0, j % 2 ? 30 : 62, 90); arm(t0 + 0.6 + n * 0.22, 15, 0, 10, 0); };
  // aR = arm on the screen-left side, aL = screen-right side; yaw > 0 turns the robot to face screen-right
  // Q-scene host size: head + shoulders, antenna top ~1185, face ~1300-1730 (all question / answer text sits above 1150)
  const QY = 1720, QH = 1000;

  // S0 · hook: big host bottom centre, the antenna peeks at frame 0, pops up, waves hello
  pose(0, Object.assign({ x: 540, y: 2180, h: 1050, yaw: 0, pitch: 0, roll: 0, hYaw: 0, hPitch: -10, hRoll: 0, lookX: 0, lookY: 0.6, smile: 1, happy: 0, xe: 0, mo: 0, squint: 0, chest: 0 }, LIGHT)); REST(0);
  pose(0.05, { y: 2180 }, "hold"); pose(0.72, { y: 1690 }, "o");
  pose(0.55, { hPitch: -2, lookY: 0 }); pose(0.85, { happy: 1 }); pose(1.9, { happy: 0 });
  wave(armL, 0.65, 4);
  // counts the three numbered questions (badges pop at hook + 1.95 / 2.22 / 2.49)
  const B0 = TM.hook + 1.95;
  pose(B0 + 0.1, { hYaw: -16, hPitch: -12, hRoll: 7, lookX: -0.85, lookY: 0.8 });
  pose(B0 + 0.37, { hYaw: 14, hPitch: -6, hRoll: -7, lookX: 0.8, lookY: 0.5 });
  pose(B0 + 0.64, { hYaw: -14, hPitch: -4, hRoll: 6, lookX: -0.8, lookY: 0.3 });
  pose(B0 + 0.95, { hYaw: 0, hPitch: -3, hRoll: 0, lookX: 0, lookY: 0 });
  // dive: glides to the right as the camera flies into the field
  pose(TM.q1 - 0.6, { x: 540, y: 1690, h: 1050 }); pose(TM.q1 + 0.3, { x: 770, y: QY, h: QH });
  pose(TM.q1 - 0.35, { yaw: 16 }); pose(TM.q1 + 0.5, { yaw: -14 });
  // S1 · Q1: reads the question, thinks, types, nods "Perlu." and presents the answer card
  pose(TM.q1 + 0.45, { hYaw: -8, hPitch: -20, hRoll: 0, lookX: -0.35, lookY: 1 });
  pose(TM.q1 + 1.35, { hRoll: 9, squint: 0.3, lookX: -0.55, lookY: 0.9 }); pose(TM.a1 - 0.2, { hRoll: 0, squint: 0 });
  pose(TM.a1 + 0.05, { hYaw: -6, hPitch: -6, lookX: -0.1, lookY: 0.2 }); pose(TM.a1 + 0.25, { hPitch: 9 }); pose(TM.a1 + 0.48, { hPitch: -7, happy: 1 }); pose(TM.a1 + 0.7, { hPitch: -2 });
  armR(TM.a1, 15, 0, 10, 0); armR(TM.a1 + 0.35, 118, 34, 28, 0, "o"); armR(TM.a1 + 1.5, 118, 34, 28, 0); armR(TM.a1 + 1.8, 15, 0, 10, 0);
  pose(TM.a1 + 1.0, { hYaw: -15, hPitch: -13, lookX: -0.75, lookY: 0.75, happy: 0 });                        // "biar kamu tahu untungnya"
  pose(TM.a1 + 2.0, { hYaw: -3, hPitch: -2, lookX: 0, lookY: 0 }); pose(TM.a1 + 2.3, { happy: 1 }); pose(TM.a1 + 3.0, { happy: 0 });   // "beneran berapa" to the viewer
  armL(TM.a1 + 1.9, 15, 0, 10, 0); armL(TM.a1 + 2.2, 60, 50, 70, 0, "o"); armL(TM.a1 + 2.9, 60, 50, 70, 0); armL(TM.a1 + 3.2, 15, 0, 10, 0);
  // T · the chat scrolls: the host hops to the left
  pose(TM.q2 - 0.5, { x: 770, y: QY }); pose(TM.q2 - 0.12, { y: QY - 34 }); pose(TM.q2 + 0.32, { x: 310, y: QY });
  pose(TM.q2 - 0.25, { yaw: -24 }); pose(TM.q2 + 0.45, { yaw: 14 });
  // S2 · Q2: reads, leans back at the falling book, sceptical tilt, head shake "Nggak harus.", flicks the book away
  pose(TM.q2 + 0.45, { hYaw: 10, hPitch: -20, lookX: 0.45, lookY: 1 });
  pose(TM.q2 + 1.5, { pitch: -7, hPitch: -24, hYaw: 16, lookX: 0.6, lookY: 0.95 });
  pose(TM.q2 + 1.95, { pitch: 0, hRoll: -10, hPitch: -14, lookX: 0.6, lookY: 0.6, squint: 0.25 });
  pose(TM.a2 - 0.05, { hRoll: 0, hYaw: 0, hPitch: -4, lookX: 0, lookY: 0.1, squint: 0 });
  [[0.15, 26], [0.33, -26], [0.51, 22], [0.69, -14], [0.87, 4]].forEach(([d, v]) => key("hYaw", TM.a2 + d, v));
  pose(TM.a2 + 0.6, { happy: 1 }); pose(TM.sol - 0.6, { happy: 0 });
  armL(TM.a2 - 0.15, 15, 0, 10, 0); armL(TM.a2 + 0.05, 40, 40, 60, 0, "o"); armL(TM.a2 + 0.3, 125, 30, 20, 0); armL(TM.a2 + 0.85, 125, 30, 20, 0); armL(TM.a2 + 1.1, 15, 0, 10, 0);
  pose(TM.a2 + 1.0, { hYaw: 6, hPitch: -6, lookX: 0.3, lookY: 0.4 });
  // T · ducks under the bands
  pose(TM.sol - 0.5, { x: 310, y: QY }); pose(TM.sol - 0.08, { y: 2700 }, "i");
  // S3 · brand: half-body bottom-left, chest hologram to the right (on screen ~4.3 s)
  pose(TM.sol - 0.05, Object.assign({ x: 200, y: 2700, h: 900, yaw: 30, pitch: 0, hYaw: 6, hPitch: 0, hRoll: 0, lookX: 0.2, lookY: 0, happy: 0, xe: 0, smile: 1, squint: 0 }, NAVY), "hold");
  armL(TM.sol - 0.05, 15, 0, 10, 0, "hold"); armR(TM.sol - 0.05, 20, -50, 14, 0, "hold");
  pose(TM.sol + 0.55, { y: 1660 }, "o");
  key("hx", 0, 720, "hold"); key("hy", 0, 1480, "hold"); key("hw", 0, 420, "hold");
  pose(TM.sol + 0.35, { chest: 0 }); pose(TM.sol + 0.6, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", TM.sol + 0.5, 0, "hold"); key("holoA", TM.sol + 0.72, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", TM.sol + 0.56, 0, "hold"); key("holoRev", TM.sol + 1.76, 1.1, "o");
  key("holoGl", 0, 0, "hold");
  for (const g0 of [TM.sol + 2.6, TM.sol + 4.4]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(TM.sol + 0.3, 15, 0, 10, 0); armL(TM.sol + 0.7, 80, 38, 36, 0, "o"); armL(TM.sol + 1.5, 80, 38, 36, 0); armL(TM.sol + 1.8, 18, 0, 12, 0);   // presents the logo
  pose(TM.sol + 1.0, { hYaw: 24, hPitch: 4, lookX: 1, lookY: -0.3, happy: 1 });
  pose(TM.sol + 1.9, { hYaw: 10, hPitch: -16, lookX: 0.5, lookY: 1, happy: 0 });                       // looks up at the messy notes
  armL(TM.lap - 0.1, 18, 0, 12, 0); armL(TM.lap + 0.3, 150, 28, 10, 0, "o"); armL(TM.lap + 1.4, 150, 28, 10, 0); armL(TM.lap + 1.7, 18, 0, 12, 0);   // points at the report
  pose(TM.lap + 0.3, { hYaw: 14, hPitch: -20, lookX: 0.6, lookY: 1, happy: 1 });
  pose(TM.lap + 1.6, { hYaw: 4, hPitch: -4, lookX: 0, lookY: 0 }); pose(TM.lap + 2.4, { happy: 0 });       // "gampang dibaca" to the viewer
  key("holoA", TM.q3 - 0.55, 1, "hold"); key("holoA", TM.q3 - 0.35, 0, "i"); pose(TM.q3 - 0.55, { chest: 1 }); pose(TM.q3 - 0.35, { chest: 0 });
  // T · whip pan: the host glides to the bottom-right
  pose(TM.q3 - 0.5, { x: 200, y: 1660, h: 900 }); pose(TM.q3 + 0.35, { x: 820, y: QY, h: 980 });
  pose(TM.q3 - 0.25, { yaw: 34 }); pose(TM.q3 + 0.5, { yaw: -18 });
  // S4 · Q3: reads, playful tilt at "bingung", "ta-da" with the chest glow (that's me), points at the two helper cards
  pose(TM.q3 + 0.5, { hYaw: -6, hPitch: -22, lookX: -0.2, lookY: 1 });
  pose(TM.q3 + 1.15, { hRoll: -10, squint: 0.2 }); pose(TM.a3 - 0.2, { hRoll: 0, squint: 0 });
  armL(TM.a3, 15, 0, 10, 0); armR(TM.a3, 15, 0, 10, 0);
  armL(TM.a3 + 0.3, 95, 25, 35, 0, "o"); armR(TM.a3 + 0.3, 95, 25, 35, 0, "o"); armL(TM.a3 + 1.0, 95, 25, 35, 0); armL(TM.a3 + 1.3, 15, 0, 10, 0);
  pose(TM.a3 + 0.1, { chest: 0 }); pose(TM.a3 + 0.4, { chest: 1 }); pose(TM.a3 + 1.4, { chest: 1 }); pose(TM.a3 + 1.7, { chest: 0 });
  pose(TM.a3 + 0.3, { hYaw: -2, hPitch: -2, lookX: 0, lookY: 0, happy: 1 });
  armR(TM.a3 + 1.0, 95, 25, 35, 0); armR(TM.a3 + 1.3, 128, 26, 14, 0);                                  // asisten AI card
  pose(TM.a3 + 1.2, { hYaw: -18, hPitch: -14, lookX: -0.8, lookY: 0.7, happy: 0 });
  armR(TM.tim + 0.35, 108, 30, 12, 0); armR(TM.tim + 1.6, 108, 30, 12, 0); armR(TM.tim + 1.9, 15, 0, 10, 0);   // tim ahli card
  pose(TM.tim + 0.35, { hYaw: -16, hPitch: -8, lookX: -0.8, lookY: 0.4 });
  pose(TM.tim + 1.05, { hPitch: 5 }); pose(TM.tim + 1.3, { hYaw: -4, hPitch: -3, lookX: 0, lookY: 0, happy: 1 }); pose(TM.tim + 2.0, { happy: 0 });
  // T · ducks out under the beam
  pose(TM.end - 0.5, { x: 820, y: QY, h: 980 }); pose(TM.end - 0.06, { x: 820, y: 2700, h: 980 }, "i");
  // S5 · end card: half-body bottom-right, logo hologram left, waves, points at the CTA
  pose(TM.end - 0.01, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, pitch: 0, yaw: -30, hYaw: 0, hPitch: 0, hRoll: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0, squint: 0 }, NAVY), "hold");
  armL(TM.end - 0.01, 18, 0, 14, 0, "hold"); armR(TM.end - 0.01, 20, -50, 14, 0, "hold");
  pose(TM.end + 0.5, { y: 1660 }, "o");
  key("hx", TM.end - 0.01, 360, "hold"); key("hy", TM.end - 0.01, 1500, "hold"); key("hw", TM.end - 0.01, 420, "hold");
  pose(TM.end + 0.4, { chest: 0 }); pose(TM.end + 0.65, { chest: 1 });
  key("holoA", TM.end + 0.52, 0, "hold"); key("holoA", TM.end + 0.75, 1, "o");
  key("holoRev", TM.end + 0.56, 0, "hold"); key("holoRev", TM.end + 1.76, 1.1, "o");
  for (const g0 of [TM.end + 4.4, TM.end + 7.0]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(TM.end + 0.6, 18, 0, 14, 0); armL(TM.end + 0.85, 145, 0, 30, 90, "o"); armL(TM.end + 1.07, 145, 0, 62, 90); armL(TM.end + 1.29, 145, 0, 30, 90); armL(TM.end + 1.51, 145, 0, 58, 90); armL(TM.end + 1.9, 18, 0, 14, 0);
  pose(TM.end + 1.2, { happy: 1 }); pose(TM.end + 2.0, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(TM.end + 3.2, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  armL(TM.cta - 0.2, 18, 0, 14, 0); armL(TM.cta + 0.15, 165, 25, 8, 0, "o"); armL(TM.cta + 1.8, 165, 25, 8, 0); armL(TM.cta + 2.1, 18, 0, 14, 0);
  pose(TM.cta + 0.2, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.cta + 1.9, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.bio + 0.6, 18, 0, 14, 0); armL(TM.bio + 0.85, 145, 0, 30, 90, "o"); armL(TM.bio + 1.07, 145, 0, 62, 90); armL(TM.bio + 1.29, 145, 0, 30, 90); armL(TM.bio + 1.8, 18, 0, 14, 0);

  for (const ch in KEYS) KEYS[ch].sort((a, b) => a[0] - b[0]);
  // hold-then-move: a key is when a pose is REACHED; the move takes at most MAXD[group] s and the previous pose holds until then
  const MAXD = { pos: 0.75, body: 0.55, head: 0.45, arm: 0.5, look: 0.3, face: 0.3 };
  for (const ch in KEYS) {
    if (RAW[ch]) continue; const md = MAXD[G[ch]] || 0.5, ks = KEYS[ch], out = [ks[0]];
    for (let i = 1; i < ks.length; i++) { const a = out[out.length - 1], b = ks[i];
      if (b[0] - a[0] > md + 1e-6 && b[2] !== "hold" && a[1] !== b[1]) out.push([b[0] - md, a[1], "hold"]); out.push(b); }
    KEYS[ch] = out;
  }

  // ---------------- per-frame state ----------------
  function state(t) {
    const v = {}; for (const ch in DEF) v[ch] = F(ch, t);
    const h = v.h, y = v.y + hover(t, h), cut = lastCut(t);
    const dd = 1 / 60, yA = F("y", Math.max(cut, t - dd)), yB = F("y", t + dd), ay = (yB - 2 * v.y + yA) / (dd * dd);
    const squash = Math.max(-0.07, Math.min(0.07, (-ay / h) * 0.0022)) + Math.sin((2 * Math.PI * t) / 1.9 + 1.2) * 0.006;
    const sig = (ch, tt) => (ch === "z" ? (F("x", tt) / F("h", tt)) * 55 + F("roll", tt) + F("hRoll", tt) : -(F("y", tt) / F("h", tt)) * 55 + F("pitch", tt) + F("hPitch", tt));
    const kA = kernel(2.4, 0.2); let az = 0, ax = 0, wsum = 0;
    for (let i = 0; i < kA.length; i += 3) { const tt = Math.max(cut, t - i * DT); az += kA[i] * sig("z", tt); ax += kA[i] * sig("x", tt); wsum += kA[i]; }
    az = az / wsum - sig("z", t); ax = ax / wsum - sig("x", t);
    const clamp = (a, m) => Math.max(-m, Math.min(m, a));
    const talk = lip(LS.open, t), wide = lip(LS.wide, t);
    // speech beats: a slow average of the envelope nods the head a little into stressed syllables
    let tAvg = 0; for (let i = 0; i < 12; i++) tAvg += lip(LS.open, Math.max(0, t - i / 60)); tAvg /= 12;
    const idleL = Math.sin(t * 2.1) * 3, idleR = Math.sin(t * 2.1 + 1.7) * 3;
    return {
      t, x: v.x, y, h, opacity: Math.max(0, Math.min(1, v.op)), yaw: v.yaw, pitch: v.pitch, roll: v.roll + Math.sin((2 * Math.PI * t) / 2.7) * 1.2, squash,
      headYaw: v.hYaw + Math.sin(t * 1.3) * 1.5 * tAvg, headPitch: v.hPitch + (talk - tAvg) * 3.0 + tAvg * 1.2, headRoll: v.hRoll + Math.sin(t * 1.9) * 1.2 * tAvg,
      antZ: clamp(az * 0.9, 28), antX: clamp(ax * 0.9, 22),
      aL: { raise: v.lR + idleL, fwd: v.lF, bend: v.lB + idleL, bendYaw: v.lY }, aR: { raise: v.rR + idleR, fwd: v.rF, bend: v.rB + idleR, bendYaw: v.rY },
      face: { blink: Math.max(blink(t), v.squint), lookX: v.lookX, lookY: v.lookY, happy: Math.max(0, Math.min(1, v.happy)), x: Math.max(0, Math.min(1, v.xe)),
              smile: v.smile, o: Math.max(0, Math.min(1, v.mo)), talk, wide },
      rim: v.rim, shadow: v.sh, chest: Math.max(0, Math.min(1, v.chest)),
      holo: { a: Math.max(0, Math.min(1, v.holoA)), rev: v.holoRev, glitch: v.holoGl, x: v.hx, y: v.hy, w: v.hw },
    };
  }
  window.ROBOT_STATE = state;
  const cv = document.getElementById("robot");
  let robot = null, lastT = 0;
  const ready = window.RobotMP.create(cv, { url: "assets/robot/robot_mp.glb", width: 1080, height: 1920 }).then((r) => { robot = r; robot.render(state(lastT)); lastDrawn = lastT; return 1; });
  window.__robotReady = ready;
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady["robot"] = ready;
  let lastDrawn = -1;   // render once per frame (the timeline onUpdate and hf-seek both call this)
  window.ROBOT_APPLY = (t) => { lastT = t; if (robot && Math.abs(t - lastDrawn) > 1e-7) { robot.render(state(t)); lastDrawn = t; } };
  window.addEventListener("hf-seek", (e) => { const t = e.detail.time; if (robot) window.ROBOT_APPLY(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => window.ROBOT_APPLY(t))); });
})();
