// MasterPajak AI robot host — Video 4 '3 Tanda Pembukuanmu Berantakan'. Beat times come from window.TM (re-timed to the VO).
// Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle layers (hover,
// breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived secondary
// motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
// The robot hosts the whole listicle from the bottom-right corner (head only above the IG UI line, never over text),
// reacts to each sign (x-eyes on the ≠ slam, looking around at the flying papers, shrug on "nggak tahu"), ducks out under
// the brand bands and rises half-body with the chest hologram for the brand beat and the series end card.
(function () {
  const KEYS = {};
  const RAW = { op: 1, holoA: 1, holoRev: 1, holoGl: 1, hx: 1, hy: 1, hw: 1 };
  const key = (ch, t, v, e) => { (KEYS[ch] = KEYS[ch] || []).push([t, v, e || "io"]); };
  const EASE = { io: (p) => p * p * p * (p * (p * 6 - 15) + 10), o: (p) => 1 - Math.pow(1 - p, 3), i: (p) => p * p * p, lin: (p) => p, hold: (p) => (p < 1 ? 0 : 1) };
  const DEF = { x: 870, y: 2700, h: 760, op: 1, yaw: 0, pitch: 0, roll: 0, hYaw: 0, hPitch: 0, hRoll: 0,
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
  // armR = the arm on the SCREEN-LEFT side, armL = the arm on the screen-right side (robot faces the camera)
  const NAVY = { sh: 0.5, rim: 2.0 }, PAPER = { sh: 0.3, rim: 1.1 };
  const REST = (t) => { armL(t, 15, 0, 10, 0); armR(t, 15, 0, 10, 0); };
  const W1 = TM.s1 - 0.1, W2 = TM.s2 - 0.1, W3 = TM.s3 - 0.1, W4 = TM.kal - 0.1;
  const HOST = { x: 872, y: 1830, h: 760 };   // head + shoulders above the IG UI, bottom-right, clear of every text block

  // HOOK: pops up from the bottom-right, looks at the giant 3, points at it on "paling sering"
  pose(0, Object.assign({ x: HOST.x, y: 2700, h: HOST.h, yaw: -18, hYaw: -10, hPitch: -6, lookX: -0.6, lookY: -0.4 }, PAPER)); REST(0);
  pose(0.15, { y: 2700 }, "hold"); pose(0.85, { y: HOST.y }, "o");
  pose(0.9, { hYaw: -24, hPitch: -14, lookX: -1, lookY: -0.7 });
  armR(0.95, 15, 0, 10, 0); armR(1.3, 150, 30, 12, 0, "o"); armR(2.0, 150, 30, 12, 0); armR(2.3, 18, 0, 12, 0);
  pose(2.2, { hYaw: -6, hPitch: 0, lookX: -0.1, lookY: 0, happy: 0 });
  pose(TM.hook + 2.6, { squint: 0.25, smile: 0.4 }); pose(TM.h3 - 0.1, { squint: 0, smile: 1 });   // "berantakan": a little wince
  pose(TM.h3 + 0.1, { hYaw: -22, hPitch: -12, lookX: -1, lookY: -0.8 });
  armR(TM.h3 + 0.2, 18, 0, 12, 0); armR(TM.h3 + 0.55, 158, 34, 8, 0, "o"); armR(TM.h3 + 1.3, 158, 34, 8, 0); armR(TM.h3 + 1.6, 18, 0, 12, 0);
  pose(TM.h3 + 0.7, { happy: 1, hPitch: -6 }); pose(TM.h3 + 1.5, { happy: 0, hYaw: -6, hPitch: 0, lookX: 0, lookY: 0 });
  // whip: the robot leans into the pan
  for (const w of [W1, W2, W3, W4]) { pose(w - 0.25, { roll: 0, yaw: -18 }); pose(w, { roll: 7, yaw: -4 }); pose(w + 0.4, { roll: 0, yaw: -18 }); }

  // SIGN 1: watches the two totals, x-eyes + head shake on the ≠ slam
  pose(TM.s1 + 0.6, { hYaw: -26, hPitch: -10, lookX: -1, lookY: -0.5 });
  pose(TM.s1 + 1.5, { hYaw: -20, hPitch: -2, lookX: -0.8, lookY: 0.1 });
  pose(TM.s1 + 2.4, { xe: 0, happy: 0, smile: 1 }); pose(TM.s1 + 2.7, { xe: 1, smile: 0 }, "o"); pose(TM.s1 + 3.7, { xe: 1, smile: 0 }); pose(TM.s1 + 3.95, { xe: 0, smile: 1 });
  [16, -16, 13, -12, 8, 0].forEach((v, k) => pose(TM.s1 + 2.75 + k * 0.13, { hYaw: v - 6, hRoll: v * 0.4 }, "io"));
  pose(TM.s1 + 2.7, { hPitch: 4, lookX: 0, lookY: 0 });
  armL(TM.s1 + 2.6, 15, 0, 10, 0); armL(TM.s1 + 2.85, 70, 25, 95, 90, "o"); armR(TM.s1 + 2.6, 15, 0, 10, 0); armR(TM.s1 + 2.85, 70, 25, 95, 90, "o");
  armL(TM.s1 + 3.5, 70, 25, 95, 90); armR(TM.s1 + 3.5, 70, 25, 95, 90); REST(TM.s1 + 3.85);
  pose(TM.s1 + 4.0, { hYaw: -8, hPitch: 0, hRoll: 0, lookX: 0, lookY: 0 });

  // SIGN 2: papers everywhere: head darts around, a sweeping point over the mess
  pose(TM.s2 + 0.5, { hYaw: -30, hPitch: -12, lookX: -1, lookY: -0.6 });
  pose(TM.s2 + 1.2, { hYaw: 4, hPitch: -16, lookX: 0.6, lookY: -1 });
  pose(TM.s2 + 1.9, { hYaw: -34, hPitch: -4, lookX: -1, lookY: 0.2 });
  pose(TM.s2 + 2.6, { hYaw: -12, hPitch: -10, lookX: -0.4, lookY: -0.6, mo: 0.35, smile: 0.2 });
  armR(TM.s2 + 1.9, 18, 0, 12, 0); armR(TM.s2 + 2.25, 120, 50, 20, 0, "o"); armR(TM.s2 + 2.85, 150, 10, 10, 0); armR(TM.s2 + 3.3, 120, 50, 20, 0); armR(TM.s2 + 3.6, 18, 0, 12, 0);
  pose(TM.s2 + 3.6, { hYaw: -6, hPitch: 0, lookX: 0, lookY: 0, mo: 0, smile: 1 });

  // SIGN 3: nods at the stamp, looks at omzet, tilts at the "?", shrugs on "nggak tahu"
  pose(TM.s3 + 0.35, { hPitch: 10, happy: 1 }); pose(TM.s3 + 0.65, { hPitch: -2 }); pose(TM.s3 + 1.0, { happy: 0 });
  pose(TM.s3 + 1.0, { hYaw: -24, hPitch: -8, lookX: -1, lookY: -0.2 });
  pose(TM.s3u + 0.8, { hYaw: -18, hPitch: -6, hRoll: 14, lookX: -0.7, lookY: -0.3, smile: 0, mo: 0.4 });
  pose(TM.s3u + 1.5, { hRoll: -10, hYaw: -4, hPitch: 2, lookX: 0, lookY: 0 });
  armL(TM.s3u + 1.3, 15, 0, 10, 0); armL(TM.s3u + 1.6, 72, 30, 100, 90, "o"); armR(TM.s3u + 1.3, 15, 0, 10, 0); armR(TM.s3u + 1.6, 72, 30, 100, 90, "o");
  armL(TM.s3u + 2.4, 72, 30, 100, 90); armR(TM.s3u + 2.4, 72, 30, 100, 90); REST(TM.s3u + 2.7);
  pose(TM.s3u + 2.6, { hRoll: 0, mo: 0, smile: 1 });

  // KALAU ADA SATU AJA: one arm up ("satu"), then a tidy-up sweep and a happy nod
  pose(TM.kal + 0.4, { hYaw: -8, hPitch: -4, lookX: 0, lookY: 0 });
  armL(TM.kal + 0.5, 15, 0, 10, 0); armL(TM.kal + 0.85, 168, 8, 4, 0, "o"); armL(TM.kal + 1.45, 168, 8, 4, 0); armL(TM.kal + 1.75, 15, 0, 10, 0);
  armR(TM.kal + 1.5, 15, 0, 10, 0); armR(TM.kal + 1.8, 120, 55, 20, 0, "o"); armR(TM.kal + 2.15, 95, 70, 30, 0); armR(TM.kal + 2.45, 18, 0, 12, 0);
  pose(TM.kal + 1.8, { happy: 1, hPitch: -8, hYaw: -18, lookX: -0.8, lookY: 0.4 }); pose(TM.kal + 2.4, { hPitch: 0, hYaw: -6, lookX: 0, lookY: 0 });
  // ducks out under the band sweep
  pose(TM.sol - 0.7, { y: HOST.y }); pose(TM.sol - 0.12, { y: 2700 }, "i");

  // SOLUTION: half-body bottom-left, chest hologram to the right (build 1.2 s, on screen ~5.7 s)
  pose(TM.sol - 0.05, Object.assign({ x: 200, y: 2700, h: 900, yaw: 30, roll: 0, hYaw: 6, hPitch: 0, hRoll: 0, lookX: 0.2, lookY: 0, happy: 0, smile: 1, mo: 0, xe: 0, squint: 0, chest: 0 }, NAVY), "hold");
  armL(TM.sol - 0.05, 20, -50, 14, 0, "hold"); armR(TM.sol - 0.05, 15, 0, 12, 0, "hold");
  pose(TM.sol + 0.55, { y: 1660 }, "o");
  armR(TM.sol + 0.3, 15, 0, 12, 0); armR(TM.sol + 0.65, 85, 35, 40, 0, "o"); armR(TM.sol + 1.3, 85, 35, 40, 0); armR(TM.sol + 1.6, 18, 0, 12, 0);
  key("hx", 0, 720, "hold"); key("hy", 0, 1495, "hold"); key("hw", 0, 420, "hold");
  pose(TM.sol + 0.35, { chest: 0 }); pose(TM.sol + 0.6, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", TM.sol + 0.5, 0, "hold"); key("holoA", TM.sol + 0.72, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", TM.sol + 0.56, 0, "hold"); key("holoRev", TM.sol + 1.76, 1.1, "o");
  key("holoGl", 0, 0, "hold");
  for (const g0 of [TM.sol + 3.0, TM.sol + 5.6]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  pose(TM.sol + 1.2, { hYaw: 26, hPitch: 4, lookX: 1, lookY: -0.3, happy: 1 });
  // follows the chips into the card, then reads the report
  pose(TM.sol + 1.8, { hYaw: 14, hPitch: -22, lookX: 0.5, lookY: 1, happy: 0 });
  armR(TM.sol + 2.6, 18, 0, 12, 0); armR(TM.sol + 2.95, 128, 28, 14, 0, "o"); armR(TM.sol + 3.6, 128, 28, 14, 0); armR(TM.sol + 3.9, 18, 0, 12, 0);
  pose(TM.sol + 3.9, { hYaw: 10, hPitch: -20, lookX: 0.4, lookY: 1 });
  pose(TM.sol + 4.9, { happy: 1, hPitch: -10 }); pose(TM.sol + 5.8, { happy: 0, hPitch: -2, hYaw: 4, lookX: 0, lookY: 0 });
  key("holoA", TM.end - 0.55, 1, "hold"); key("holoA", TM.end - 0.3, 0, "i"); pose(TM.end - 0.55, { chest: 1 }); pose(TM.end - 0.3, { chest: 0 });
  // ducks out under the beam
  pose(TM.end - 0.5, { y: 1660 }); pose(TM.end - 0.06, { y: 2700 }, "i");

  // END CARD (series template): half-body bottom-right, logo hologram left, waves, points at the CTA
  pose(TM.end - 0.01, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0 }, NAVY), "hold");
  armL(TM.end - 0.01, 18, 0, 14, 0, "hold"); armR(TM.end - 0.01, 20, -50, 14, 0, "hold");
  pose(TM.end + 0.5, { y: 1660 }, "o");
  key("hx", TM.end - 0.01, 360, "hold"); key("hy", TM.end - 0.01, 1490, "hold"); key("hw", TM.end - 0.01, 420, "hold");
  pose(TM.end + 0.4, { chest: 0 }); pose(TM.end + 0.65, { chest: 1 });
  key("holoA", TM.end + 0.52, 0, "hold"); key("holoA", TM.end + 0.75, 1, "o");
  key("holoRev", TM.end + 0.56, 0, "hold"); key("holoRev", TM.end + 1.76, 1.1, "o");
  for (const g0 of [TM.end + 4.3, TM.end + 6.3]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(TM.end + 0.6, 18, 0, 14, 0); armL(TM.end + 0.85, 145, 0, 30, 90, "o"); armL(TM.end + 1.07, 145, 0, 62, 90); armL(TM.end + 1.29, 145, 0, 30, 90); armL(TM.end + 1.51, 145, 0, 58, 90); armL(TM.end + 1.9, 18, 0, 14, 0);
  pose(TM.end + 1.2, { happy: 1 }); pose(TM.end + 2.0, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(TM.end + 3.0, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  armL(TM.end + 3.2, 18, 0, 14, 0); armL(TM.end + 3.55, 165, 25, 8, 0, "o"); armL(TM.end + 5.0, 165, 25, 8, 0); armL(TM.end + 5.3, 18, 0, 14, 0);
  pose(TM.end + 3.6, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.end + 5.1, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.end + 5.5, 18, 0, 14, 0); armL(TM.end + 5.75, 145, 0, 30, 90, "o"); armL(TM.end + 5.97, 145, 0, 62, 90); armL(TM.end + 6.19, 145, 0, 30, 90); armL(TM.end + 6.6, 18, 0, 14, 0);

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
