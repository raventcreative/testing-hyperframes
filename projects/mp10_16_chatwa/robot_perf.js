// MasterPajak AI robot host — Video 16 'Dari Chat ke Catatan Rapi'. Beat times come from window.TM (real VO word times + 0.30 s).
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
  // hard cuts (robot hidden / off-frame when it jumps): springs never look back across them. The end cut sits at end+0.1
  // because this film's beam/iris runs 0.15 s later than the series default (the trace beat needs the time).
  const CUTS = [window.TM.sol - 0.05, window.TM.end + 0.1];
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

  // ---------------- choreography (all times from window.TM = real VO word times) ----------------
  const TM = window.TM;
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const NAVY = { sh: 0.5, rim: 2.0 }, LIGHT = { sh: 0.34, rim: 1.25 };
  const REST = (t, e) => { armL(t, 15, 0, 10, 0, e); armR(t, 15, 0, 10, 0, e); };
  const RX = 905, RY = 1585, RH = 520;   // paper studio: small full-body host, bottom-right, beside the phone / the sheet

  // S1 · hook: rises in at the bottom-right, eyes on the flooding phone; shrug on "tapi, dicatat di mana?"
  pose(0, Object.assign({ x: RX, y: 2480, h: RH, yaw: -22, pitch: 0, hYaw: -12, hPitch: -6, hRoll: 0, lookX: -0.7, lookY: 0.4, happy: 0, xe: 0, smile: 1, mo: 0, squint: 0, chest: 0 }, LIGHT)); REST(0);
  pose(0.3, { y: 2480 }, "hold"); pose(1.05, { y: RY }, "o");
  pose(0.95, { hYaw: -20, hPitch: -12, lookX: -0.9, lookY: 0.6, hRoll: 5 });
  pose(TM.chatw, { lookX: -0.5, lookY: 0.85 }); pose(TM.chatw + 0.45, { lookX: -1, lookY: 0.35 }); pose(TM.chatw + 0.9, { lookX: -0.65, lookY: 0.7, hRoll: 0 });
  armL(TM.dicatat - 0.05, 15, 0, 10, 0); armR(TM.dicatat - 0.05, 15, 0, 10, 0);
  armL(TM.mana - 0.05, 58, 28, 78, 0, "o"); armR(TM.mana - 0.05, 58, 28, 78, 0, "o");
  pose(TM.mana - 0.05, { hRoll: 14, hYaw: -4, hPitch: -2, lookX: -0.15, lookY: 0.15 });
  armL(TM.b1 - 0.1, 58, 28, 78, 0); armR(TM.b1 - 0.1, 58, 28, 78, 0); armL(TM.b1 + 0.3, 15, 0, 10, 0); armR(TM.b1 + 0.3, 15, 0, 10, 0);
  // S2 · follows each read-out bubble as it lifts off the screen; happy on "mau dua", curious tilt on "ongkirnya berapa?"
  [TM.b1, TM.b2, TM.b3].forEach((t, k) => pose(t + 0.12, { hYaw: -19 + 2 * k, hPitch: -15 + 7 * k, hRoll: k === 2 ? 11 : 0, lookX: -0.9, lookY: 0.75 - 0.35 * k }));
  pose(TM.b1 + 0.35, { happy: 1 }); pose(TM.b1 + 0.95, { happy: 0 });
  pose(TM.b2 + 0.1, { mo: 0 }); pose(TM.b3 + 0.3, { mo: 0.3 }); pose(TM.b3 + 0.9, { mo: 0 });
  // S3 · the sigh: slumps; "numpuk": dizzy x-eyes at the pile; "kelewat": reaches for the falling bubble, too late
  pose(TM.sigh + 0.12, { y: RY + 16, pitch: 7, hPitch: 14, hRoll: 0, hYaw: -10, lookX: -0.4, lookY: -0.5, squint: 0.4 });
  armL(TM.sigh + 0.2, 7, 0, 5, 0); armR(TM.sigh + 0.2, 7, 0, 5, 0);
  pose(TM.numpuk + 0.35, { y: RY, pitch: 0, hPitch: -10, hYaw: -16, lookX: -0.85, lookY: 0.6, squint: 0 });
  armL(TM.numpuk + 0.35, 15, 0, 10, 0); armR(TM.numpuk + 0.35, 15, 0, 10, 0);
  pose(TM.numpukw + 0.1, { xe: 1 }); pose(TM.numpukw + 0.95, { xe: 0 });
  pose(TM.lostw - 0.12, { hYaw: -10, hPitch: -16, lookX: -0.35, lookY: 0.9 });
  armR(TM.lostw + 0.05, 15, 0, 10, 0); armR(TM.lostw + 0.38, 122, 30, 22, 0, "o"); armR(TM.lostw + 0.95, 122, 30, 22, 0); armR(TM.lostw + 1.25, 15, 0, 10, 0);
  pose(TM.lostw + 0.4, { hYaw: 6, hPitch: 12, lookX: 0.5, lookY: -0.7, mo: 0.5 }); pose(TM.lostw + 1.15, { mo: 0, hYaw: -10, hPitch: 0, lookX: -0.4, lookY: 0 });
  // S4 · "biasain catat": perks up and points at the sheet; little nods on "tanggal, pesanan, nominal"
  pose(TM.catat + 0.15, { hYaw: -18, hPitch: -14, lookX: -0.8, lookY: 0.6, happy: 1 }); pose(TM.catat + 0.85, { happy: 0 });
  pose(TM.catat + 0.7, { x: 935, y: 1655, h: 470 });   // steps down a little: the big sheet needs the room
  pose(TM.sol - 0.75, { x: 935, y: 1655, h: 470 });
  armR(TM.catat + 0.4, 15, 0, 10, 0); armR(TM.catat + 0.8, 118, 30, 18, 0, "o"); armR(TM.catat + 1.9, 118, 30, 18, 0); armR(TM.catat + 2.2, 15, 0, 10, 0);
  [TM.tgl, TM.psn, TM.nom].forEach((t, k) => { pose(t + 0.02, { hPitch: -8, lookX: -0.95 + 0.25 * k, lookY: 0.5 }); pose(t + 0.28, { hPitch: -15 }); });
  // S5 · rows land: eyes follow; "rapi": happy; "dicek": yes arm pump
  pose(TM.satu, { hYaw: -16, hPitch: -10, lookX: -0.9, lookY: 0.4 });
  pose(TM.satu2, { hYaw: -20, hPitch: -6, lookX: -0.7, lookY: 0.2 });
  pose(TM.rapi + 0.1, { happy: 1, hPitch: -12, hYaw: -14, lookX: -0.6, lookY: 0.5 });
  armR(TM.cek - 0.12, 15, 0, 10, 0); armR(TM.cek + 0.16, 92, 18, 82, 0, "o"); armR(TM.cek + 0.6, 92, 18, 82, 0); armR(TM.cek + 0.9, 15, 0, 10, 0);
  pose(TM.cek + 0.95, { happy: 0 });
  // ducks out before the band sweep
  pose(TM.sol - 0.28, { y: 2560 }, "i");

  // S6 · brand: half-body bottom-left, chest hologram to the right (build ~1.2 s, full alpha > 4 s), points at the sheet, the flip, the trace
  pose(TM.sol - 0.05, Object.assign({ x: 200, y: 2700, h: 900, yaw: 30, pitch: 0, roll: 0, hRoll: 0, xe: 0, squint: 0, mo: 0, happy: 0 }, NAVY), "hold");
  REST(TM.sol - 0.05, "hold");
  pose(TM.sol + 0.45, { x: 200, y: 1660, h: 900 }, "o");
  pose(TM.sol + 0.2, { hYaw: 6, hPitch: 0, lookX: 0.2, lookY: 0, smile: 1, happy: 0 }, "hold");
  armR(TM.sol + 0.25, 15, 0, 12, 0); armR(TM.sol + 0.6, 85, 35, 40, 0, "o"); armR(TM.sol + 1.2, 85, 35, 40, 0); armR(TM.sol + 1.45, 18, 0, 12, 0);
  armL(TM.sol + 0.25, 20, -50, 14, 0);
  key("hx", 0, 720, "hold"); key("hy", 0, 1520, "hold"); key("hw", 0, 420, "hold");
  pose(TM.sol + 0.12, { chest: 0 }); pose(TM.sol + 0.4, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", TM.sol + 0.15, 0, "hold"); key("holoA", TM.sol + 0.35, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", TM.sol + 0.2, 0, "hold"); key("holoRev", TM.sol + 1.4, 1.1, "o");
  key("holoGl", 0, 0, "hold");
  for (const g0 of [TM.sol + 2.6, TM.telusur + 0.2]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  pose(TM.sol + 0.9, { hYaw: 20, hPitch: -14, lookX: 0.8, lookY: 0.9, happy: 1 }); pose(TM.sol + 1.6, { happy: 0 });
  // series pattern: the far arm points up at the card; the near arm stays low so it never crosses the hologram
  armR(TM.catj - 0.3, 18, 0, 12, 0); armR(TM.catj + 0.05, 150, 25, 10, 0, "o"); armR(TM.pemb + 0.3, 150, 25, 10, 0); armR(TM.pemb + 0.6, 18, 0, 12, 0);
  pose(TM.pemb + 0.05, { happy: 1, hPitch: -12 }); pose(TM.pemb + 0.5, { happy: 0, hYaw: 14, hPitch: -6, lookX: 0.6, lookY: 0.4 });
  armR(TM.bisa, 18, 0, 12, 0); armR(TM.bisa + 0.3, 118, 30, 14, 0, "o"); armR(TM.end - 0.45, 118, 30, 14, 0); armR(TM.end - 0.2, 18, 0, 12, 0);   // the source chip
  pose(TM.telusur, { hYaw: 22, hPitch: -2, lookX: 0.9, lookY: 0.1, happy: 1 });
  key("holoA", TM.end - 0.3, 1, "hold"); key("holoA", TM.end - 0.08, 0, "i"); pose(TM.end - 0.3, { chest: 1 }); pose(TM.end - 0.08, { chest: 0 });
  // T · ducks out under the beam
  pose(TM.end - 0.3, { x: 200, y: 1660, h: 900 }); pose(TM.end + 0.09, { x: 200, y: 2700, h: 900 }, "i");
  // S7 · end card: half-body bottom-right, logo hologram left, waves, points at the CTA (series template)
  const E = TM.end + 0.1;
  pose(E, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0 }, NAVY), "hold");
  armL(E, 18, 0, 14, 0, "hold"); armR(E, 20, -50, 14, 0, "hold");
  pose(E + 0.5, { y: 1660 }, "o");
  key("hx", E, 360, "hold"); key("hy", E, 1500, "hold"); key("hw", E, 420, "hold");
  pose(E + 0.4, { chest: 0 }); pose(E + 0.65, { chest: 1 });
  key("holoA", E + 0.52, 0, "hold"); key("holoA", E + 0.75, 1, "o");
  key("holoRev", E + 0.56, 0, "hold"); key("holoRev", E + 1.76, 1.1, "o");
  for (const g0 of [TM.cta + 1.2, TM.bio + 1.2]) { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); }
  armL(E + 0.6, 18, 0, 14, 0); armL(E + 0.85, 145, 0, 30, 90, "o"); armL(E + 1.07, 145, 0, 62, 90); armL(E + 1.29, 145, 0, 30, 90); armL(E + 1.51, 145, 0, 58, 90); armL(E + 1.9, 18, 0, 14, 0);
  pose(E + 1.2, { happy: 1 }); pose(E + 2.0, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(TM.cta - 0.4, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  armL(TM.cta - 0.2, 18, 0, 14, 0); armL(TM.cta + 0.15, 165, 25, 8, 0, "o"); armL(TM.cta + 1.1, 165, 25, 8, 0); armL(TM.cta + 1.35, 18, 0, 14, 0);
  pose(TM.cta + 0.2, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.cta + 1.2, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.bio - 0.05, 18, 0, 14, 0); armL(TM.bio + 0.2, 145, 0, 30, 90, "o"); armL(TM.bio + 0.42, 145, 0, 62, 90); armL(TM.bio + 0.64, 145, 0, 30, 90); armL(TM.bio + 0.86, 145, 0, 58, 90); armL(TM.bio + 1.25, 18, 0, 14, 0);
  pose(TM.bio + 1.4, { happy: 0 });

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
