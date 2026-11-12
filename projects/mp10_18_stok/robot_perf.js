// MasterPajak AI robot host — Video 18 'Stok Itu Uang yang Lagi Diam'. Beat times come from window.TM (real VO word times).
// Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle layers (hover,
// breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived secondary
// motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
// Placement note: x = horizontal centre, y = body centre (top of the antenna ~ y - h/2, feet ~ y + h/2), h = height in px.
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

  // ---------------- choreography (all times from window.TM = real VO word times, so a re-voice moves everything) ----------------
  const TM = window.TM;
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const NAVY = { sh: 0.5, rim: 2.0 }, LIGHT = { sh: 0.34, rim: 1.25 };
  const REST = (t, e) => { armL(t, 15, 0, 10, 0, e); armR(t, 15, 0, 10, 0, e); };
  const R0 = (t) => armR(t, 15, 0, 10, 0), L0 = (t) => armL(t, 15, 0, 10, 0);
  const POINT = (t0, t1) => { R0(t0 - 0.05); armR(t0 + 0.3, 112, 30, 14, 0, "o"); armR(t1, 112, 30, 14, 0); R0(t1 + 0.3); };   // points left/up at the shelf
  const RX = 905, RY = 1585, RH = 520;   // warehouse: small full-body host, bottom-right, beside the shelf

  // S1 · hook: rises in at the bottom-right, looks at the full shelf, then up at the saldo card; shrugs on "tipis"
  pose(0, Object.assign({ x: RX, y: 2480, h: RH, yaw: -20, hYaw: -14, hPitch: -6, hRoll: 0, lookX: -0.6, lookY: 0.3 }, LIGHT)); REST(0);
  pose(0.08, { y: 2480 }, "hold"); pose(0.85, { y: RY }, "o");
  pose(0.8, { hYaw: -24, hPitch: -10, lookX: -0.9, lookY: 0.5, hRoll: 6 });
  pose(TM.saldo + 0.15, { hYaw: 2, hPitch: -22, lookX: 0.1, lookY: 1, hRoll: 0, yaw: -10 });
  L0(TM.tipis - 0.1); R0(TM.tipis - 0.1);
  armL(TM.tipis + 0.25, 46, 26, 96, 0, "o"); armR(TM.tipis + 0.25, 46, 26, 96, 0, "o");
  armL(TM.tipis + 0.75, 46, 26, 96, 0); armR(TM.tipis + 0.75, 46, 26, 96, 0); L0(TM.tipis + 1.05); R0(TM.tipis + 1.05);
  pose(TM.tipis + 0.2, { hRoll: 13, mo: 0.35, hPitch: -8, hYaw: -6 }); pose(TM.tipis + 0.95, { hRoll: 0, mo: 0 });
  // S2 · "coba balik kardusnya": points at the hero box; "uang": surprised and happy; "diam": a flat "pause" palm
  pose(TM.balik + 0.1, { hYaw: -26, hPitch: 0, lookX: -1, lookY: 0.1, yaw: -26 });
  POINT(TM.balik, TM.balik + 1.3);
  pose(TM.isi, { hYaw: -20, hPitch: -6, lookX: -0.8, lookY: 0.4, hRoll: 8 });
  pose(TM.uang + 0.05, { happy: 1, mo: 0.45, hPitch: -12, hYaw: -18, hRoll: 0 }); pose(TM.uang + 0.8, { mo: 0 });
  L0(TM.uang - 0.05); armL(TM.uang + 0.3, 70, 20, 60, 0, "o"); armL(TM.uang + 0.85, 70, 20, 60, 0); L0(TM.uang + 1.1);
  pose(TM.diam, { happy: 0 });
  R0(TM.diam - 0.2); armR(TM.diam + 0.15, 88, 40, 92, 0, "o"); armR(TM.diam + 0.7, 88, 40, 92, 0); R0(TM.diam + 0.95);
  // S3 · "bukan uang hangus / bukan untung": watches the floating box, shakes its head at each sticker
  pose(TM.bel + 0.3, { hYaw: -22, hPitch: -8, lookX: -0.8, lookY: 0.4, yaw: -24 });
  for (const t0 of [TM.hangus + 0.1, TM.untung + 0.1]) {
    pose(t0, { hYaw: -38 }); pose(t0 + 0.24, { hYaw: -6 }); pose(t0 + 0.48, { hYaw: -36 }); pose(t0 + 0.74, { hYaw: -20 });
  }
  // S4 · "itu modal yang nyangkut": a nod and a point at the box going back; "biaya": looks up at the BIAYA card; "laku": arm pump
  pose(TM.modal + 0.1, { hPitch: 8, hYaw: -24, happy: 1 }); pose(TM.modal + 0.4, { hPitch: -6 }); pose(TM.modal + 1.0, { happy: 0 });
  POINT(TM.modal + 0.2, TM.nyangkut + 0.6);
  pose(TM.biaya + 0.15, { hYaw: -2, hPitch: -24, lookX: -0.2, lookY: 1, yaw: -12 });
  R0(TM.laku + 0.2); armR(TM.laku + 0.5, 92, 18, 82, 0, "o"); armR(TM.laku + 0.95, 92, 18, 82, 0); R0(TM.laku + 1.25);
  pose(TM.laku + 0.45, { happy: 1, mo: 0.35 }); pose(TM.laku + 1.1, { happy: 0, mo: 0 });
  // S5 · "dianggap biaya": watches the chips fly up; "jeblok": x-eyes and a recoil; "padahal barangnya masih ada": points at the shelf
  pose(TM.semua + 0.2, { hYaw: -8, hPitch: -22, lookX: -0.3, lookY: 0.9 });
  pose(TM.jeblok + 0.62, { xe: 0, roll: 0, hRoll: 0, mo: 0, y: RY }); pose(TM.jeblok + 0.95, { xe: 1, roll: -7, hRoll: -10, y: RY + 22, mo: 0.5 }, "o");
  L0(TM.jeblok + 0.62); R0(TM.jeblok + 0.62); armL(TM.jeblok + 0.95, 38, -18, 24, 0, "o"); armR(TM.jeblok + 0.95, 38, -18, 24, 0, "o");
  pose(TM.padahal - 0.05, { xe: 1, roll: -7, hRoll: -10, y: RY + 22, mo: 0.5 }); pose(TM.padahal + 0.3, { xe: 0, roll: 0, hRoll: 0, y: RY, mo: 0, happy: 1 });
  L0(TM.padahal + 0.3);
  pose(TM.padahal + 0.35, { hYaw: -24, hPitch: -4, lookX: -1, lookY: 0.2, yaw: -26 });
  POINT(TM.padahal + 0.2, TM.padahal + 1.4); pose(TM.padahal + 1.3, { happy: 0 });
  // ducks out before the band sweep
  pose(TM.sol - 0.75, { y: RY }); pose(TM.sol - 0.28, { y: 2560 }, "i");

  // S6 · brand: half-body bottom-left, chest hologram to the right (build 1.2 s, on screen > 4 s), points at the pembukuan, then the laba rugi
  pose(TM.sol - 0.05, Object.assign({ x: 200, y: 2700, h: 900, yaw: 30, pitch: 0, roll: 0, hRoll: 0, xe: 0, squint: 0, mo: 0, happy: 0 }, NAVY), "hold");
  REST(TM.sol - 0.05, "hold");
  pose(TM.sol + 0.55, { x: 200, y: 1660, h: 900 }, "o");
  pose(TM.sol + 0.3, { hYaw: 6, hPitch: 0, lookX: 0.2, lookY: 0, smile: 1, happy: 0 }, "hold");
  armR(TM.sol + 0.3, 15, 0, 12, 0); armR(TM.sol + 0.65, 85, 35, 40, 0, "o"); armR(TM.sol + 1.3, 85, 35, 40, 0); armR(TM.sol + 1.55, 18, 0, 12, 0);
  armL(TM.sol + 0.3, 20, -50, 14, 0);
  key("hx", 0, 720, "hold"); key("hy", 0, 1520, "hold"); key("hw", 0, 420, "hold");
  pose(TM.sol + 0.35, { chest: 0 }); pose(TM.sol + 0.6, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", TM.sol + 0.5, 0, "hold"); key("holoA", TM.sol + 0.72, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", TM.sol + 0.56, 0, "hold"); key("holoRev", TM.sol + 1.76, 1.1, "o");
  key("holoGl", 0, 0, "hold");
  for (const g0 of [TM.pemb + 0.9, TM.lr + 1.7]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  pose(TM.sol + 1.0, { hYaw: 20, hPitch: -14, lookX: 0.8, lookY: 0.9, happy: 1 }); pose(TM.sol + 1.7, { happy: 0 });
  // series pattern (Videos 1/5/14): the far arm points up at the cards; the near arm stays low so it never crosses the hologram
  armR(TM.catat - 0.3, 18, 0, 12, 0); armR(TM.catat + 0.05, 150, 25, 10, 0, "o"); armR(TM.pemb + 0.7, 150, 25, 10, 0); armR(TM.pemb + 0.95, 18, 0, 12, 0);   // pembukuan
  pose(TM.pemb + 0.1, { happy: 1, hPitch: -10 }); pose(TM.pemb + 0.75, { happy: 0, hYaw: 10, hPitch: -4, lookX: 0.3, lookY: 0.2 });
  armR(TM.lr + 0.3, 18, 0, 12, 0); armR(TM.lr + 0.7, 138, 28, 12, 0, "o"); armR(TM.bener + 0.6, 138, 28, 12, 0); armR(TM.bener + 0.9, 18, 0, 12, 0);   // laporan laba rugi
  pose(TM.lr + 0.55, { hYaw: 18, hPitch: -10, lookX: 0.8, lookY: 0.6 }); pose(TM.bener + 0.3, { happy: 1 }); pose(TM.bener + 1.0, { happy: 0, hYaw: 8, hPitch: 0, lookX: 0.1, lookY: 0 });
  key("holoA", TM.end - 0.55, 1, "hold"); key("holoA", TM.end - 0.3, 0, "i"); pose(TM.end - 0.55, { chest: 1 }); pose(TM.end - 0.3, { chest: 0 });
  // T · ducks out under the beam
  pose(TM.end - 0.5, { x: 200, y: 1660, h: 900 }); pose(TM.end - 0.06, { x: 200, y: 2700, h: 900 }, "i");
  // S7 · end card: half-body bottom-right, logo hologram left, waves, points at the CTA (series template)
  pose(TM.end - 0.01, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0 }, NAVY), "hold");
  armL(TM.end - 0.01, 18, 0, 14, 0, "hold"); armR(TM.end - 0.01, 20, -50, 14, 0, "hold");
  pose(TM.end + 0.5, { y: 1660 }, "o");
  key("hx", TM.end - 0.01, 360, "hold"); key("hy", TM.end - 0.01, 1500, "hold"); key("hw", TM.end - 0.01, 420, "hold");
  pose(TM.end + 0.4, { chest: 0 }); pose(TM.end + 0.65, { chest: 1 });
  key("holoA", TM.end + 0.52, 0, "hold"); key("holoA", TM.end + 0.75, 1, "o");
  key("holoRev", TM.end + 0.56, 0, "hold"); key("holoRev", TM.end + 1.76, 1.1, "o");
  for (const g0 of [TM.cta + 1.2, TM.bio + 1.4]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(TM.end + 0.6, 18, 0, 14, 0); armL(TM.end + 0.85, 145, 0, 30, 90, "o"); armL(TM.end + 1.07, 145, 0, 62, 90); armL(TM.end + 1.29, 145, 0, 30, 90); armL(TM.end + 1.51, 145, 0, 58, 90); armL(TM.end + 1.9, 18, 0, 14, 0);
  pose(TM.end + 1.2, { happy: 1 }); pose(TM.end + 2.0, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(TM.cta - 0.4, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  armL(TM.cta - 0.2, 18, 0, 14, 0); armL(TM.cta + 0.15, 165, 25, 8, 0, "o"); armL(TM.cta + 1.4, 165, 25, 8, 0); armL(TM.cta + 1.7, 18, 0, 14, 0);
  pose(TM.cta + 0.2, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.cta + 1.5, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.bio + 0.3, 18, 0, 14, 0); armL(TM.bio + 0.55, 145, 0, 30, 90, "o"); armL(TM.bio + 0.77, 145, 0, 62, 90); armL(TM.bio + 0.99, 145, 0, 30, 90); armL(TM.bio + 1.5, 18, 0, 14, 0);

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
