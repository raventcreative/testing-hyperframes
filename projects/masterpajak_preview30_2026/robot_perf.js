// MasterPajak AI trial robot — 38.5 s performance locked to the client's VO (word stamps: production/vo_words.json).
// Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle layers (hover,
// breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived secondary
// motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
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
  // hard cuts (robot hidden / off-frame when it jumps): springs never look back across them
  const CUTS = [22.7, 30.29];
  const lastCut = (t) => { let c = -1e9; for (const q of CUTS) if (q <= t) c = q; return c; };
  function filt(ch, t, f, z) { const c = lastCut(t), k = kernel(f, z); let y = 0; for (let i = 0; i < k.length; i++) y += k[i] * raw(ch, Math.max(c, t - i * DT)); return y; }
  const GRP = { pos: [1.5, 0.74], body: [1.7, 0.6], head: [2.3, 0.52], arm: [2.0, 0.56], look: [5.5, 0.92], face: [4.0, 0.95] };
  const G = { x: "pos", y: "pos", h: "pos", yaw: "body", pitch: "body", roll: "body", hYaw: "head", hPitch: "head", hRoll: "head",
    lR: "arm", lF: "arm", lB: "arm", lY: "arm", rR: "arm", rF: "arm", rB: "arm", rY: "arm", lookX: "look", lookY: "look",
    happy: "face", xe: "face", smile: "face", mo: "face", squint: "face", rim: "face", sh: "face", chest: "face" };
  const F = (ch, t) => (RAW[ch] ? raw(ch, t) : filt(ch, t, GRP[G[ch]][0], GRP[G[ch]][1]));
  const hover = (t, h) => Math.sin((2 * Math.PI * t) / 1.9) * 0.012 * h;
  const BLINKS = [0.42, 2.0, 3.9, 5.2, 7.05, 9.4, 11.6, 13.0, 15.6, 17.25, 18.9, 20.8, 23.1, 25.25, 26.95, 28.6, 31.2, 33.0, 34.8, 36.6, 38.0];
  function blink(t) { let b = 0; for (const t0 of BLINKS) { const u = (t - t0) / 0.15; if (u > 0 && u < 1) b = Math.max(b, Math.sin(Math.PI * u)); } return b; }
  const LS = window.LIPSYNC || { fps: 60, open: [], wide: [] };
  const lip = (arr, t) => { const f = t * LS.fps, i = Math.floor(f), u = f - i; const a = arr[i] || 0, b = arr[i + 1] || 0; return a + (b - a) * u; };

  // ---------------- choreography ----------------
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const LIGHT = { sh: 0.3, rim: 1 }, NAVY = { sh: 0.5, rim: 2.0 };

  // S1 · 0–3.40 "Pesanan rame, tapi kok uang yang masuk beda?" — rises talking, looks at the cards, scratches its head
  pose(0, Object.assign({ x: 790, y: 2250, h: 560 }, LIGHT));
  pose(0.02, { y: 2250 }); pose(0.5, { y: 1600 }, "o");
  armL(0, 30, 0, 10, 0); armR(0, 30, 0, 10, 0); armL(0.6, 10, 0, 8, 0); armR(0.6, 10, 0, 8, 0);
  pose(0.0, { hYaw: 0, hPitch: 0, yaw: 0, lookX: 0, lookY: 0 });
  pose(0.75, { hYaw: -18, hPitch: -10, yaw: -12, lookX: -0.9, lookY: 0.7 });
  pose(1.75, { hRoll: 10, lookY: 0.4 });
  armL(1.0, 10, 0, 8, 0); armL(1.4, 60, 25, 40, 0); armL(1.9, 12, 0, 10, 0);          // small "explaining" beat on "tapi kok"
  armR(2.4, 10, 0, 8, 0); armR(2.66, 142, 12, 118, -80);
  armR(2.8, 142, 12, 128, -80); armR(2.92, 142, 12, 112, -80);
  pose(2.6, { hRoll: 14, smile: 0 });
  pose(2.85, { hYaw: 22, lookX: 1, lookY: 0.1, yaw: 6 });
  // T1 -> S2 hop
  pose(2.9, { x: 790, y: 1600, h: 560 }); armR(2.95, 60, 0, 40, -70);
  pose(3.18, { x: 520, y: 1420 }, "o"); pose(3.46, { x: 300, y: 1690, h: 470 }, "i");
  pose(3.0, { hRoll: 14 }); pose(3.25, { hRoll: -6, smile: 0.4 });
  armL(3.0, 70, 10, 26, 0); armR(3.06, 70, 10, 14, -20); armL(3.46, 15, 0, 10, 0); armR(3.46, 15, 0, 10, 0);
  pose(2.9, LIGHT); pose(3.4, NAVY);
  // S2 · 3.40–8.85 "Tiap tutup bulan masih cocok-cocokin 3 file. Pesanan, pencairan, mutasi bank."
  pose(3.6, { hYaw: 18, hPitch: -16, yaw: 10, lookX: 0.6, lookY: 1, smile: 0.2, hRoll: 0 });
  armL(4.3, 15, 0, 10, 0); armL(4.55, 80, 20, 60, 90); armL(4.85, 18, 0, 10, 90);     // "masih"
  pose(5.75, { xe: 0 }); pose(5.9, { xe: 1 });
  [[5.88, 120, 40], [6.04, 150, 80], [6.2, 115, 30], [6.36, 150, 70]].forEach(([t, a, b], i) => {
    armL(t, i % 2 ? a : 150 - (a - 115), 10, b, 90); armR(t, i % 2 ? 150 - (a - 115) : a, 10, 110 - b, 90); });
  [[5.88, -6], [6.0, 6], [6.12, -5], [6.24, 6], [6.36, -4]].forEach(([t, r]) => pose(t, { roll: r, hRoll: -r * 0.8 }));
  pose(6.5, { roll: 0, hRoll: 0, xe: 0 });
  armL(6.55, 22, 0, 10, 90); armR(6.55, 22, 0, 10, 90); armL(6.95, 20, 0, 10, 0); armR(6.95, 20, 0, 10, 0);
  // looks at each file as it lands, counting with a little lift of the arm
  pose(6.62, { hYaw: -4, hPitch: -10, lookX: -0.2, lookY: 0.6 }); pose(7.36, { hYaw: 12, lookX: 0.4 }); pose(8.08, { hYaw: 26, lookX: 1, hPitch: -6 });
  armL(7.0, 20, 0, 10, 0); armL(7.3, 55, 25, 30, 0); armL(7.6, 20, 0, 10, 0); armL(8.02, 60, 30, 30, 0); armL(8.35, 20, 0, 10, 0);
  // T2 -> S3 glide bottom-right
  pose(8.4, { x: 300, y: 1690, h: 470 }); pose(9.0, { x: 840, y: 1700, h: 460 });
  pose(8.4, { yaw: 0 }); pose(8.65, { yaw: 25, roll: -8 }); pose(9.0, { yaw: -15, roll: 0 });
  pose(8.7, NAVY); pose(8.85, LIGHT);
  // S3 · 8.85–10.90 "Padahal itu uang yang sama." — points at the coin
  pose(9.05, { hYaw: -22, hPitch: -14, lookX: -1, lookY: 1, smile: 0.8 });
  armR(8.95, 20, 0, 12, 0); armR(9.4, 128, 28, 10, 0, "o");
  pose(10.0, { y: 1700 }); pose(10.14, { y: 1660 }, "o"); pose(10.34, { y: 1700 });
  armL(10.0, 12, 0, 10, 0); armL(10.16, 60, 20, 40, 90); armL(10.45, 15, 0, 10, 0);
  // T3 -> S4 half-body (explaining)
  armR(10.4, 128, 28, 10, 0); armR(10.66, 25, 0, 15, 0);
  pose(10.45, { x: 840, y: 1700, h: 460 }); pose(11.02, { x: 290, y: 1640, h: 820 });
  pose(10.45, { roll: 0, yaw: -15 }); pose(10.7, { roll: 12, yaw: -28 }); pose(11.05, { roll: 0, yaw: 16 });
  // S4 · 10.90–14.95 "Ada potongan, ada retur, dan masih ada selisih yang perlu dicek."
  pose(11.1, { hYaw: 14, hPitch: -16, lookX: 0.6, lookY: 1 });
  armL(11.0, 15, 0, 10, 0); armL(11.25, 150, 22, 10, 0, "o"); armL(11.75, 150, 22, 10, 0); armL(12.05, 20, 0, 10, 0);   // points up at "− Potongan"
  armR(12.0, 15, 0, 10, 0); armR(12.25, 135, 25, 15, 0, "o"); armR(12.7, 135, 25, 15, 0); armR(12.95, 18, 0, 10, 0);  // "− Retur"
  pose(12.2, { hYaw: -6, lookX: -0.3 }); pose(12.9, { hYaw: 16, lookX: 0.6 });
  pose(13.4, { hPitch: -6, lookY: 0.3, squint: 0.35, smile: 0 }); armR(13.3, 18, 0, 10, 0); armR(13.6, 22, 72, 118, 0);   // hand to chin at "selisih"
  pose(14.2, { squint: 0, hPitch: -10, lookY: 0.6 }); armR(14.15, 22, 72, 118, 0); armR(14.4, 18, 0, 12, 0);
  armL(14.15, 15, 0, 10, 0); armL(14.38, 120, 30, 8, 0, "o");                                                            // points at "Perlu dicek"
  pose(14.45, { hPitch: -16 }); pose(14.6, { hPitch: -4 }); pose(14.75, { hPitch: -12 });
  // T4 -> S5 half-body, bottom-left, turned toward the hologram side
  armL(14.6, 120, 30, 8, 0); armL(14.85, 15, 0, 12, 0);
  pose(14.5, { x: 290, y: 1640, h: 820 }); pose(15.08, { x: 200, y: 1660, h: 900 });
  pose(14.5, LIGHT); pose(14.95, NAVY);
  pose(14.6, { yaw: 16 }); pose(15.15, { yaw: 30 });
  // S5 · 14.95–22.70 "Kenalin, MasterPajak AI." -> chest projects the logo hologram (reveal 1.2 s, then on screen ~7 s)
  pose(15.15, { hYaw: 6, hPitch: 0, lookX: 0.2, lookY: 0, smile: 1, squint: 0 });
  armR(15.0, 15, 0, 12, 0); armR(15.3, 85, 35, 40, 0, "o"); armR(15.95, 85, 35, 40, 0); armR(16.3, 18, 0, 12, 0);          // "kenalin" presenting
  armL(15.0, 15, 0, 12, 0); armL(15.3, 20, -50, 14, 0);
  pose(15.9, { hYaw: 26, hPitch: 4, lookX: 1, lookY: -0.3, happy: 1 }); pose(16.8, { hYaw: 6, hPitch: 0, lookX: 0, lookY: 0, happy: 0 });
  key("hx", 0, 720, "hold"); key("hy", 0, 1520, "hold"); key("hw", 0, 420, "hold");
  pose(15.05, { chest: 0 }); pose(15.3, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", 15.2, 0, "hold"); key("holoA", 15.42, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", 15.26, 0, "hold"); key("holoRev", 16.46, 1.1, "o");
  key("holoGl", 0, 0, "hold");
  for (const g0 of [18.6, 21.2]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  // "Catatan jualan kamu dirapikan jadi pembukuan yang bisa ditelusuri, sampai ke persiapan pajak."
  pose(17.5, { hYaw: 14, hPitch: -22, lookX: 0.4, lookY: 1 });
  armR(18.3, 18, 0, 12, 0); armR(18.5, 70, 40, 60, 0); armR(18.85, 60, 40, 30, 0); armR(19.1, 18, 0, 12, 0);             // "dirapikan"
  pose(19.3, { hYaw: 20, hPitch: -24 }); pose(20.35, { hYaw: 22, lookX: 1 }); pose(20.95, { hYaw: 30, lookX: 1 });         // follows the trace
  pose(21.0, { happy: 0 }); pose(22.1, { happy: 1, hPitch: -10 }); pose(22.25, { hPitch: -20 });
  armR(21.9, 18, 0, 12, 0); armR(22.15, 140, 0, 30, 90, "o");
  // T5 · zoom-through: flies into the camera, hologram powers down
  pose(22.2, { x: 200, y: 1660, h: 900 }); pose(22.68, { x: 420, y: 1250, h: 3200 }, "i");
  key("op", 0, 1, "hold"); key("op", 22.56, 1, "hold"); key("op", 22.67, 0, "lin");
  key("holoA", 22.2, 1, "hold"); key("holoA", 22.42, 0, "i"); pose(22.2, { chest: 1 }); pose(22.42, { chest: 0 });
  // S6a · 22.70–24.45 "Bingung angka pajaknya dari mana?" — slides in, confused, looks at the "?"
  pose(22.7, Object.assign({ x: 1320, y: 1000, h: 440, happy: 0, smile: 0.4, chest: 0, hYaw: -18, hPitch: 0, lookX: -0.6, lookY: 0 }, LIGHT), "hold"); key("op", 22.72, 1, "hold");
  pose(23.12, { x: 920, y: 1000, h: 440 }, "o");
  pose(22.7, { roll: -14, yaw: -25 }, "hold"); pose(23.2, { roll: 0, yaw: -12 });
  armR(22.7, 20, 0, 15, 0, "hold"); armL(22.7, 20, 0, 15, 0, "hold");
  armR(23.2, 142, 12, 118, -80); armR(23.36, 142, 12, 128, -80); armR(23.5, 142, 12, 112, -80); armR(23.64, 142, 12, 126, -80); armR(23.9, 25, 0, 15, 0);
  pose(23.25, { hRoll: 14, hYaw: -22, lookX: -1, lookY: 0.3 }); pose(23.95, { hRoll: 0 });
  // T5b · iris: comes forward to half-body bottom-right for the chat
  pose(24.02, { x: 920, y: 1000, h: 440 }); pose(24.62, { x: 850, y: 1660, h: 980 });
  pose(24.02, { yaw: -12 }); pose(24.6, { yaw: -25 });
  pose(24.1, LIGHT); pose(24.45, NAVY);
  // S6b · 24.45–30.30 "Asisten AI-nya bantu jelasin. Kasusnya rumit? Ada tim ahli yang siap bantu, sesuai layanan."
  pose(24.65, { hYaw: -20, hPitch: -14, lookX: -1, lookY: 0.8, smile: 1 });
  armR(24.5, 20, 0, 12, 0); armR(24.85, 138, 22, 12, 0, "o"); armR(25.6, 138, 22, 12, 0); armR(25.9, 20, 0, 12, 0);     // points at the chat
  armL(25.4, 18, 0, 12, 0); armL(25.7, 60, 40, 50, 0); armL(26.1, 50, 40, 25, 0); armL(26.4, 18, 0, 12, 0);              // "bantu jelasin"
  pose(26.0, { hYaw: -6, hPitch: 0, lookX: 0, lookY: 0 });
  pose(26.7, { hRoll: -12, smile: 0.3 }); armL(26.6, 18, 0, 12, 0); armL(26.85, 75, 10, 70, 90); armR(26.6, 20, 0, 12, 0); armR(26.85, 75, 10, 70, 90);   // shrug
  armL(27.3, 18, 0, 12, 0); armR(27.3, 20, 0, 12, 0); pose(27.35, { hRoll: 0 });
  pose(27.6, { hYaw: -20, hPitch: -6, lookX: -1, lookY: 0.2, happy: 1, smile: 1 });
  armR(27.5, 20, 0, 12, 0); armR(27.85, 110, 25, 10, 0, "o"); armR(28.9, 110, 25, 10, 0); armR(29.2, 20, 0, 12, 0);     // points at "Tim ahli"
  pose(28.85, { hPitch: -12 }); pose(29.0, { hPitch: 2 }); pose(29.15, { hPitch: -8 }); pose(29.4, { happy: 0, hYaw: -4, lookX: 0, lookY: 0 });
  // T6 · ducks out as the beam floods
  pose(29.8, { x: 850, y: 1660, h: 980 }); pose(30.24, { x: 850, y: 2700, h: 980 }, "i");
  // S7 · 30.30–38.50 half-body bottom-right; the logo hologram builds to its left and stays to the end
  pose(30.29, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0 }, NAVY), "hold");
  armL(30.29, 18, 0, 14, 0, "hold"); armR(30.29, 20, -50, 14, 0, "hold");
  pose(30.78, { y: 1660 }, "o");
  key("hx", 30.29, 360, "hold"); key("hy", 30.29, 1500, "hold"); key("hw", 30.29, 420, "hold");
  pose(30.7, { chest: 0 }); pose(30.95, { chest: 1 });
  key("holoA", 30.82, 0, "hold"); key("holoA", 31.05, 1, "o");
  key("holoRev", 30.86, 0, "hold"); key("holoRev", 32.06, 1.1, "o");
  for (const g0 of [34.3, 37.4]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(30.8, 18, 0, 14, 0); armL(31.0, 95, 30, 45, 0); armL(31.5, 18, 0, 14, 0);                                        // "jualan jalan terus"
  pose(31.85, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 1 }); pose(33.2, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0, happy: 0 });
  armL(33.3, 18, 0, 14, 0); armL(33.62, 165, 25, 8, 0, "o"); armL(35.2, 165, 25, 8, 0); armL(35.5, 18, 0, 14, 0);       // points up at the CTA
  pose(33.65, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(35.3, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6 });
  armL(36.3, 18, 0, 14, 0); armL(36.55, 145, 0, 30, 90, "o"); armL(36.78, 145, 0, 62, 90); armL(37.0, 145, 0, 30, 90); armL(37.22, 145, 0, 60, 90); armL(37.44, 145, 0, 32, 90); armL(37.9, 18, 0, 14, 0);   // waves
  pose(36.4, { happy: 1, hRoll: 6 }); pose(37.2, { hRoll: -5 }); pose(37.9, { hRoll: 0 });

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
  const ready = window.RobotMP.create(cv, { url: "assets/robot/robot_mp.glb", width: 1080, height: 1920 }).then((r) => { robot = r; robot.render(state(lastT)); return 1; });
  window.__robotReady = ready;
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady["robot"] = ready;
  window.ROBOT_APPLY = (t) => { lastT = t; if (robot) robot.render(state(t)); };
  window.addEventListener("hf-seek", (e) => { const t = e.detail.time; if (robot) window.ROBOT_APPLY(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => window.ROBOT_APPLY(t))); });
})();
