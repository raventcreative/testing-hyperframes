// MasterPajak AI robot host — Video 7 'Kalkulator Gratis 3 Langkah'. Beat times come from window.TM (re-time to the VO word stamps).
// Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle layers (hover,
// breathing, blinks) -> lip-sync from lipsync.js (mouth open/wide per 1/60 s) + speech head beats -> derived secondary
// motion (squash from vertical acceleration, antenna lag). Hologram panels stay inside the 120 px side safe zone.
// Arms: armR = the robot's right arm (screen-left when it faces us), armL = its left arm (screen-right).
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
  const CUTS = [window.TM.brand - 0.05, window.TM.end - 0.01];
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
  const holoGlitch = (g0) => { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); };
  key("holoA", 0, 0, "hold"); key("holoRev", 0, 0, "hold"); key("holoGl", 0, 0, "hold");

  // S0 · hook (paper): the host peeks in bottom-right, tilts its head at the question, ducks under the band sweep
  pose(0, Object.assign({ x: 880, y: 2700, h: 800, yaw: -24, hYaw: -6, hPitch: 0, hRoll: 0, lookX: -0.3, lookY: 0, smile: 1, happy: 0, chest: 0 }, LIGHT)); REST(0);
  pose(TM.hook + 0.3, { y: 2700 }, "hold"); pose(TM.hook + 0.95, { y: 1800 }, "o");
  pose(TM.hook + 1.35, { hYaw: -20, hPitch: -10, hRoll: 9, lookX: -1, lookY: 0.8 });
  armR(TM.hook + 1.0, 15, 0, 10, 0); armR(TM.hook + 1.5, 62, 55, 105, 0, "o");                 // hand up to the chin: "hmm?"
  armR(TM.brand - 0.5, 62, 55, 105, 0); armR(TM.brand - 0.15, 15, 0, 10, 0);
  pose(TM.brand - 0.55, { y: 1800 }); pose(TM.brand - 0.1, { y: 2700 }, "i");

  // S1 · brand: rises half-body bottom-left, chest hologram to the right (on screen > 4 s)
  pose(TM.brand - 0.05, Object.assign({ x: 200, y: 2700, h: 900, yaw: 30, hYaw: 6, hPitch: 0, hRoll: 0, lookX: 0.2, lookY: 0, smile: 1, happy: 0, chest: 0 }, NAVY), "hold");
  armL(TM.brand - 0.05, 20, -50, 14, 0, "hold"); armR(TM.brand - 0.05, 15, 0, 12, 0, "hold");
  pose(TM.brand + 0.55, { y: 1660 }, "o");
  armR(TM.brand + 0.3, 15, 0, 12, 0); armR(TM.brand + 0.65, 85, 35, 40, 0, "o"); armR(TM.brand + 1.3, 85, 35, 40, 0); armR(TM.brand + 1.6, 18, 0, 12, 0);
  key("hx", 0, 740, "hold"); key("hy", 0, 1500, "hold"); key("hw", 0, 420, "hold");
  pose(TM.brand + 0.35, { chest: 0 }); pose(TM.brand + 0.6, { chest: 1 });
  key("holoA", TM.brand + 0.5, 0, "hold"); key("holoA", TM.brand + 0.72, 1, "o");
  key("holoRev", TM.brand + 0.56, 0, "hold"); key("holoRev", TM.brand + 1.76, 1.1, "o");
  holoGlitch(TM.brand + 2.9);
  pose(TM.brand + 1.2, { hYaw: 26, hPitch: 4, lookX: 1, lookY: -0.3, happy: 1 });           // admires its logo
  pose(TM.brand + 2.2, { hYaw: 18, hPitch: -14, lookX: 0.8, lookY: 0.7, happy: 0 });          // looks up at the phone
  // (no arm point here: from bottom-left the hand would cross the hologram logo) — it glances at the phone and nods at the tap
  pose(TM.s1 - 0.85, { hPitch: -8, lookY: 0.5 }); pose(TM.s1 - 0.6, { hPitch: -18, lookY: 0.8, happy: 1 }); pose(TM.s1 - 0.35, { hPitch: -10 });
  key("holoA", TM.s1 - 0.2, 1, "hold"); key("holoA", TM.s1 + 0.05, 0, "i"); pose(TM.s1 - 0.2, { chest: 1 }); pose(TM.s1 + 0.05, { chest: 0 });   // full-alpha hologram ~4.1 s

  // steps: stays bottom-left (a bit smaller/lower so the phone keeps clear), guides each step
  const SP = { x: 185, y: 1730, h: 850 };
  pose(TM.s1 - 0.5, { x: 200, y: 1660, h: 900 }); pose(TM.s1 + 0.3, SP);
  pose(TM.s1 - 0.3, { yaw: 30 }); pose(TM.s1 + 0.3, { yaw: 26, happy: 0 });
  // step 1 · isi data usaha
  armL(TM.s1 - 0.2, 20, -10, 14, 0); armL(TM.s1 + 0.4, 135, 30, 12, 0, "o"); armL(TM.s1 + 1.5, 135, 30, 12, 0); armL(TM.s1 + 1.9, 25, 0, 14, 0);
  pose(TM.s1 + 0.4, { hYaw: 24, hPitch: -12, lookX: 1, lookY: 0.6 });
  pose(TM.s1 + 2.3, { hPitch: -4, lookY: 0.3 }); pose(TM.s1 + 2.6, { hPitch: -12, lookY: 0.5 }); pose(TM.s1 + 2.9, { hPitch: -6 });   // nods along with the chips
  armL(TM.s1 + 3.0, 25, 0, 14, 0); armL(TM.s1 + 3.4, 100, 30, 18, 0, "o"); armL(TM.s1 + 3.9, 100, 30, 18, 0); armL(TM.s1 + 4.2, 22, 0, 14, 0);   // "Lanjut"
  // step 2 · masukkan omzet
  pose(TM.s2 - 0.3, { hPitch: -8, hYaw: 20, happy: 0 });
  armL(TM.s2 + 0.2, 22, 0, 14, 0); armL(TM.s2 + 0.6, 125, 35, 14, 0, "o"); armL(TM.s2 + 2.0, 125, 35, 14, 0); armL(TM.s2 + 2.4, 22, 0, 14, 0);
  pose(TM.s2 + 0.6, { hYaw: 22, hPitch: -10, lookX: 1, lookY: 0.4 });
  pose(TM.s2 + 2.35, { happy: 1, hPitch: -4 }); pose(TM.s2 + 3.0, { happy: 0 });
  armL(TM.s2 + 3.0, 22, 0, 14, 0); armL(TM.s2 + 3.3, 100, 30, 18, 0, "o"); armL(TM.s2 + 3.7, 100, 30, 18, 0); armL(TM.s2 + 4.0, 22, 0, 14, 0);   // "Hitung estimasi"
  // step 3 · lihat estimasi
  pose(TM.s3 - 0.2, { hYaw: 22, hPitch: -12, lookX: 1, lookY: 0.5 });
  armL(TM.s3 + 0.9, 22, 0, 14, 0); armL(TM.s3 + 1.3, 140, 28, 10, 0, "o"); armL(TM.s3 + 2.4, 140, 28, 10, 0); armL(TM.s3 + 2.8, 22, 0, 14, 0);
  pose(TM.s3 + 1.8, { happy: 1, hPitch: -6 }); pose(TM.s3 + 2.8, { happy: 0 });

  // S2 · result: glides to bottom-right, points at the lifted result card, then at the consult card
  pose(TM.res - 0.55, SP); pose(TM.res + 0.35, { x: 868, y: 1700, h: 900 });
  pose(TM.res - 0.4, { yaw: 26 }); pose(TM.res + 0.35, { yaw: -26 });
  pose(TM.res + 0.2, { hYaw: -22, hPitch: -14, lookX: -1, lookY: 0.7, happy: 0 });
  armR(TM.res + 0.3, 18, 0, 12, 0); armR(TM.res + 0.75, 140, 22, 12, 0, "o"); armR(TM.res + 2.0, 140, 22, 12, 0); armR(TM.res + 2.4, 18, 0, 12, 0);
  pose(TM.res + 0.9, { happy: 1 }); pose(TM.res + 1.8, { happy: 0 });
  pose(TM.kon + 0.1, { hYaw: -24, hPitch: -2, lookX: -1, lookY: 0.2 });
  armR(TM.kon + 0.1, 18, 0, 12, 0); armR(TM.kon + 0.5, 128, 25, 10, 0, "o"); armR(TM.kon + 1.7, 128, 25, 10, 0); armR(TM.kon + 2.1, 18, 0, 12, 0);
  pose(TM.kon + 1.2, { happy: 1, hPitch: -6 }); pose(TM.kon + 2.2, { happy: 0, hPitch: 0, hYaw: -6, lookX: 0, lookY: 0 });
  // T · ducks out under the beam
  pose(TM.end - 0.5, { x: 868, y: 1700, h: 900 }); pose(TM.end - 0.06, { x: 868, y: 2700, h: 900 }, "i");

  // S5 · end card: half-body bottom-right, logo hologram left, waves, points at the CTA
  pose(TM.end - 0.01, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, hRoll: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, chest: 0 }, NAVY), "hold");
  armL(TM.end - 0.01, 18, 0, 14, 0, "hold"); armR(TM.end - 0.01, 20, -50, 14, 0, "hold");
  pose(TM.end + 0.5, { y: 1660 }, "o");
  key("hx", TM.end - 0.01, 360, "hold"); key("hy", TM.end - 0.01, 1500, "hold"); key("hw", TM.end - 0.01, 420, "hold");
  pose(TM.end + 0.4, { chest: 0 }); pose(TM.end + 0.65, { chest: 1 });
  key("holoA", TM.end + 0.52, 0, "hold"); key("holoA", TM.end + 0.75, 1, "o");
  key("holoRev", TM.end + 0.56, 0, "hold"); key("holoRev", TM.end + 1.76, 1.1, "o");
  holoGlitch(TM.end + 3.9); holoGlitch(TM.end + 5.8);
  armL(TM.end + 0.6, 18, 0, 14, 0); armL(TM.end + 0.85, 145, 0, 30, 90, "o"); armL(TM.end + 1.07, 145, 0, 62, 90); armL(TM.end + 1.29, 145, 0, 30, 90); armL(TM.end + 1.51, 145, 0, 58, 90); armL(TM.end + 1.9, 18, 0, 14, 0);
  pose(TM.end + 1.2, { happy: 1 }); pose(TM.end + 1.9, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(TM.end + 2.6, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  armL(TM.end + 2.5, 18, 0, 14, 0); armL(TM.end + 2.85, 165, 25, 8, 0, "o"); armL(TM.end + 4.3, 165, 25, 8, 0); armL(TM.end + 4.6, 18, 0, 14, 0);
  pose(TM.end + 2.9, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(TM.end + 4.4, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  armL(TM.end + 4.9, 18, 0, 14, 0); armL(TM.end + 5.15, 145, 0, 30, 90, "o"); armL(TM.end + 5.37, 145, 0, 62, 90); armL(TM.end + 5.59, 145, 0, 30, 90); armL(TM.end + 6.1, 18, 0, 14, 0);

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
