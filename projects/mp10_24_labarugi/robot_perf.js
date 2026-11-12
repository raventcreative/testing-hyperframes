// MasterPajak AI robot host — Video 24 'Laporan Laba Rugi dalam 30 Detik' (the cooking-show host). Beat times come from window.TM
// (real VO word times + 0.30 s). Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe)
// -> idle layers (hover, breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived
// secondary motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
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

  // ---------------- choreography (all times from window.TM = real VO word times + 0.30 s) ----------------
  const TM = window.TM;
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const NAVY = { sh: 0.5, rim: 2.0 }, LIGHT = { sh: 0.34, rim: 1.25 };
  const REST = (t, e) => { armL(t, 15, 0, 10, 0, e); armR(t, 15, 0, 10, 0, e); };
  const RX = 925, RY = 1595, RH = 520;   // kitchen host: small full-body figure bottom-right of the counter (armR = the screen-left arm)
  const pointR = (t0, t1, r, f, b) => { armR(t0 - 0.05, 15, 0, 10, 0); armR(t0 + 0.3, r, f, b, 0, "o"); armR(t1, r, f, b, 0); armR(t1 + 0.3, 15, 0, 10, 0); };
  const nod = (t, base, d) => { pose(t + 0.06, { hPitch: base + (d || 7) }); pose(t + 0.34, { hPitch: base }); };

  // S1 · hook "Resep laporan laba rugi": rises in with a host flourish; "tiga puluh detik": points up at the timer; "Yuk, masak!": hop + both arms up
  pose(0, Object.assign({ x: RX, y: 2480, h: RH, yaw: -18, hYaw: -10, hPitch: -6, hRoll: 0, lookX: -0.3, lookY: 0.3, happy: 0, xe: 0, mo: 0, squint: 0, smile: 1, chest: 0 }, LIGHT)); REST(0);
  pose(0.15, { y: 2480 }, "hold"); pose(0.85, { y: RY }, "o");
  armL(0.45, 15, 0, 10, 0); armR(0.45, 15, 0, 10, 0); armL(0.9, 128, 22, 30, 0, "o"); armR(0.9, 128, 22, 30, 0, "o");
  pose(0.85, { happy: 1, mo: 0.2 }); pose(TM.lap + 0.6, { happy: 0, mo: 0 });
  armL(TM.lap + 0.5, 128, 22, 30, 0); armL(TM.lap + 0.85, 15, 0, 10, 0);
  pointR(TM.dtk - 0.1, TM.yuk - 0.35, 160, 22, 12);
  pose(TM.dtk, { hYaw: -14, hPitch: -24, lookX: -0.4, lookY: 1 });
  pose(TM.yuk - 0.12, { y: RY }); pose(TM.yuk + 0.12, { y: RY - 50 }, "o"); pose(TM.yuk + 0.42, { y: RY }, "i");
  armL(TM.yuk - 0.1, 15, 0, 10, 0); armL(TM.yuk + 0.2, 150, 14, 34, 0, "o"); armR(TM.yuk + 0.2, 150, 14, 34, 0, "o");
  pose(TM.yuk + 0.05, { happy: 1, mo: 0.35, hPitch: -6, hYaw: -6, lookX: 0, lookY: 0 });
  REST(TM.bahan + 0.1); pose(TM.bahan, { happy: 0, mo: 0 });
  // S2 · bahan: looks over at the recipe card (left), points at each row as it is named
  pose(TM.bahan + 0.2, { hYaw: -30, hPitch: -6, lookX: -1, lookY: 0.2, yaw: -26 });
  pointR(TM.pj - 0.1, TM.by + 0.3, 104, 34, 18);
  nod(TM.pj, -6); nod(TM.mb, -6); nod(TM.by, -6);
  pose(TM.by + 0.3, { happy: 1 }); pose(TM.l1, { happy: 0 });
  // S3 · Langkah 1: the jar pours (watches it), the modal portion flies to its cup (head follows it up), "laba kotor": a pleased nod
  pose(TM.l1 + 0.3, { hYaw: -24, hPitch: -14, lookX: -0.8, lookY: 0.6, yaw: -22 });
  pointR(TM.pj2 - 0.3, TM.krg, 132, 30, 16);
  pose(TM.krg + 0.2, { hYaw: -20, hPitch: -24, lookX: -0.6, lookY: 1 });
  pose(TM.mb2 + 0.3, { hYaw: -30, hPitch: -22, lookX: -1, lookY: 1 });
  pose(TM.lk - 0.05, { hYaw: -16, hPitch: -8, lookX: -0.4, lookY: 0.2, happy: 1 }); nod(TM.lk, -8, 9);
  armL(TM.lk - 0.1, 15, 0, 10, 0); armL(TM.lk + 0.25, 120, 30, 60, 0, "o"); armL(TM.l2 - 0.2, 120, 30, 60, 0); armL(TM.l2 + 0.15, 15, 0, 10, 0);
  pose(TM.l2 - 0.1, { happy: 0 });
  // S4 · Langkah 2: "satu-satu" head bobs; each cost portion: points and follows it to its cup
  pose(TM.l2 + 0.2, { hYaw: -20, hPitch: -12, lookX: -0.6, lookY: 0.5, yaw: -20 });
  for (let k = 0; k < 3; k++) { pose(TM.satu + k * 0.24, { hRoll: k % 2 ? -7 : 7 }); } pose(TM.satu + 0.8, { hRoll: 0 });
  pointR(TM.ong - 0.25, TM.kem + 0.4, 140, 26, 14);
  [[TM.ong, -0.9], [TM.ikl, -0.5], [TM.kem, -0.15]].forEach(([t, lx]) => { pose(t + 0.15, { lookX: lx, lookY: 1, hYaw: -16 + lx * 14, hPitch: -22 }); });
  // S5 · Hasil: the timer dings -> hop; "laba": both arms up, happy; "untung kamu yang sebenarnya": points at the scale
  pose(TM.has + 0.05, { hYaw: -10, hPitch: -6, lookX: -0.2, lookY: -0.3 });
  pose(TM.has - 0.1, { y: RY }); pose(TM.has + 0.15, { y: RY - 44 }, "o"); pose(TM.has + 0.45, { y: RY }, "i");
  REST(TM.laba - 0.15); armL(TM.laba + 0.15, 150, 14, 34, 0, "o"); armR(TM.laba + 0.15, 150, 14, 34, 0, "o"); armL(TM.unt - 0.2, 150, 14, 34, 0); armR(TM.unt - 0.2, 150, 14, 34, 0);
  pose(TM.laba, { happy: 1, mo: 0.35, hPitch: -4 }); pose(TM.unt - 0.1, { mo: 0 });
  armL(TM.unt + 0.15, 15, 0, 10, 0); pointR(TM.unt + 0.05, TM.sol - 1.0, 118, 36, 20);
  pose(TM.unt + 0.2, { hYaw: -22, hPitch: -14, lookX: -0.8, lookY: 0.6 }); pose(TM.sbn + 0.3, { hYaw: -8, hPitch: -4, lookX: 0, lookY: 0 });
  pose(TM.sol - 0.75, { y: RY }); pose(TM.sol - 0.28, { y: 2560 }, "i");

  // S6 · brand: half-body bottom-left, chest hologram to the right (build 1.2 s, full alpha > 4 s), points at the laporan card
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
  for (const g0 of [TM.lr + 0.3, TM.bia + 0.6]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  pose(TM.sol + 1.0, { hYaw: 20, hPitch: -14, lookX: 0.8, lookY: 0.9, happy: 1 }); pose(TM.sol + 1.7, { happy: 0 });
  // series pattern (Videos 1/5/14/20): the far arm points up at the card; the near arm stays low so it never crosses the hologram
  armR(TM.lr - 0.2, 18, 0, 12, 0); armR(TM.lr + 0.15, 150, 25, 10, 0, "o"); armR(TM.cat - 0.1, 150, 25, 10, 0); armR(TM.cat + 0.2, 18, 0, 12, 0);   // the flip
  pose(TM.lr + 0.3, { happy: 1, hPitch: -10 }); pose(TM.cat, { happy: 0, hYaw: 10, hPitch: -4, lookX: 0.3, lookY: 0.2 });
  armR(TM.bia - 0.1, 18, 0, 12, 0); armR(TM.bia + 0.25, 138, 28, 12, 0, "o"); armR(TM.bln + 0.3, 138, 28, 12, 0); armR(TM.bln + 0.6, 18, 0, 12, 0);    // the rows / tiap bulan
  pose(TM.bia + 0.1, { hYaw: 18, hPitch: -10, lookX: 0.8, lookY: 0.6 }); pose(TM.bln + 0.1, { hYaw: 24, hPitch: -18, lookX: 1, lookY: 1 }); pose(TM.bln + 0.4, { happy: 1 });
  key("holoA", TM.end - 0.55, 1, "hold"); key("holoA", TM.end - 0.3, 0, "i"); pose(TM.end - 0.55, { chest: 1 }); pose(TM.end - 0.3, { chest: 0 });
  // T · ducks out under the beam
  pose(TM.end - 0.5, { x: 200, y: 1660, h: 900, happy: 0 }); pose(TM.end - 0.06, { x: 200, y: 2700, h: 900 }, "i");
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
  armL(TM.cta - 0.2, 18, 0, 14, 0); armL(TM.cta + 0.15, 165, 25, 8, 0, "o"); armL(TM.cta + 1.1, 165, 25, 8, 0); armL(TM.cta + 1.4, 18, 0, 14, 0);
  pose(TM.cta + 0.2, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.cta + 1.2, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.bio + 0.25, 18, 0, 14, 0); armL(TM.bio + 0.5, 145, 0, 30, 90, "o"); armL(TM.bio + 0.72, 145, 0, 62, 90); armL(TM.bio + 0.94, 145, 0, 30, 90); armL(TM.bio + 1.35, 18, 0, 14, 0);

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
