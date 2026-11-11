// MasterPajak AI trial robot — performance for the 15 s preview (host character present in every scene).
// Keyframed channels -> per-group 2nd-order spring filter (convolution with the spring's impulse response, so every
// frame is a pure function of time: seek-safe, identical in preview and render) -> idle layers (hover, breathing,
// blinks) -> derived secondary motion (squash from vertical acceleration, antenna lag + wobble). Then RobotMP.render().
(function () {
  const KEYS = {};
  const RAW = { op: 1, holoA: 1, holoRev: 1, holoGl: 1, hx: 1, hy: 1, hw: 1 };
  const key = (ch, t, v, e) => { (KEYS[ch] = KEYS[ch] || []).push([t, v, e || "io"]); };
  const EASE = {
    io: (p) => p * p * p * (p * (p * 6 - 15) + 10),            // smootherstep
    o: (p) => 1 - Math.pow(1 - p, 3), i: (p) => p * p * p, lin: (p) => p, hold: (p) => (p < 1 ? 0 : 1),
  };
  const DEF = { x: 790, y: 2250, h: 500, op: 1, yaw: 0, pitch: 0, roll: 0, hYaw: 0, hPitch: 0, hRoll: 0,
    lR: 6, lF: 0, lB: 6, lY: 0, rR: 6, rF: 0, rB: 6, rY: 0, lookX: 0, lookY: 0, happy: 0, xe: 0, smile: 1, mo: 0, squint: 0, rim: 1, sh: 0.32, chest: 0, holoA: 0, holoRev: 0, holoGl: 0, hx: 540, hy: 1700, hw: 560 };
  function raw(ch, t) {
    const ks = KEYS[ch]; if (!ks) return DEF[ch];
    if (t <= ks[0][0]) return ks[0][1];
    for (let i = 0; i < ks.length - 1; i++) {
      const a = ks[i], b = ks[i + 1];
      if (t < b[0]) { const p = (t - a[0]) / (b[0] - a[0]); return a[1] + (b[1] - a[1]) * EASE[b[2]](p); }
    }
    return ks[ks.length - 1][1];
  }
  // spring kernels (unit DC gain), dt = 1/90 s
  const DT = 1 / 90, KER = {};
  function kernel(f, z) {
    const id = f + "_" + z; if (KER[id]) return KER[id];
    const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - z * z), n = Math.min(160, Math.ceil(5 / (z * w) / DT));
    const k = []; let s = 0;
    for (let i = 0; i < n; i++) { const tau = i * DT, h = Math.exp(-z * w * tau) * Math.sin(wd * tau); k.push(h); s += h; }
    for (let i = 0; i < n; i++) k[i] /= s; return (KER[id] = k);
  }
  // hard cuts: the springs never look back across these (the robot is hidden / off-frame when it jumps)
  const CUTS = [10.0, 11.99];
  function filt(ch, t, f, z) { let c = -1e9; for (const q of CUTS) if (q <= t) c = q; const k = kernel(f, z); let y = 0; for (let i = 0; i < k.length; i++) y += k[i] * raw(ch, Math.max(c, t - i * DT)); return y; }
  const GRP = { pos: [1.5, 0.74], body: [1.7, 0.6], head: [2.3, 0.52], arm: [2.0, 0.56], look: [5.5, 0.92], face: [4.0, 0.95] };
  const G = { x: "pos", y: "pos", h: "pos", yaw: "body", pitch: "body", roll: "body", hYaw: "head", hPitch: "head", hRoll: "head",
    lR: "arm", lF: "arm", lB: "arm", lY: "arm", rR: "arm", rF: "arm", rB: "arm", rY: "arm", lookX: "look", lookY: "look",
    happy: "face", xe: "face", smile: "face", mo: "face", squint: "face", rim: "face", sh: "face", chest: "face" };
  const F = (ch, t) => (RAW[ch] ? raw(ch, t) : filt(ch, t, GRP[G[ch]][0], GRP[G[ch]][1]));
  const hover = (t, h) => Math.sin((2 * Math.PI * t) / 1.9) * 0.014 * h;
  const BLINKS = [0.42, 1.25, 2.3, 3.86, 5.45, 7.15, 8.3, 9.25, 11.02, 12.5, 13.95, 14.6];
  function blink(t) { let b = 0; for (const t0 of BLINKS) { const u = (t - t0) / 0.15; if (u > 0 && u < 1) b = Math.max(b, Math.sin(Math.PI * u)); } return b; }

  // ---------------- choreography ----------------
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  // S1 · hook (0–2): rises from below, looks at the cards, "≠" -> scratches head, glances at the panel, hops left
  pose(0, { x: 790, y: 2250, h: 560, sh: 0.3, rim: 1 });
  pose(0.12, { y: 2250 }); pose(0.5, { y: 1600 }, "o");
  armL(0, 30, 0, 10, 0); armR(0, 30, 0, 10, 0); armL(0.55, 8, 0, 8, 0); armR(0.55, 8, 0, 8, 0);
  pose(0.0, { hYaw: 0, hPitch: 0, yaw: 0, lookX: 0, lookY: 0 });
  pose(0.55, { hYaw: -18, hPitch: -10, yaw: -12, lookX: -0.9, lookY: 0.7 });
  pose(0.82, { hRoll: 0, smile: 1, mo: 0 }); pose(1.0, { hRoll: 14, smile: 0, mo: 0.55 });
  armR(0.8, 8, 0, 8, 0); armR(1.02, 142, 12, 118, -80);   // hand up to the side of the head
  armR(1.18, 142, 12, 128, -80); armR(1.32, 142, 12, 112, -80); armR(1.44, 142, 12, 126, -80);   // scratch scratch
  pose(1.32, { hYaw: -18, lookX: -0.9 }); pose(1.45, { hYaw: 22, lookX: 1, lookY: 0.1, yaw: 6 });   // the panel is coming
  // T1 -> S2: hop to the bottom-left
  pose(1.5, { x: 790, y: 1600, h: 560 }); armR(1.52, 60, 0, 40, -70);
  pose(1.78, { x: 520, y: 1420 }, "o"); pose(2.06, { x: 300, y: 1690, h: 470 }, "i");
  pose(1.5, { hRoll: 14, mo: 0.55 }); pose(1.8, { hRoll: -6, mo: 0, smile: 0.4 });
  armL(1.6, 70, 10, 26, 0); armR(1.66, 70, 10, 14, -20); armL(2.06, 15, 0, 10, 0); armR(2.06, 15, 0, 10, 0);
  pose(1.5, { sh: 0.3, rim: 1 }); pose(2.0, { sh: 0.5, rim: 2.0 });
  // S2 · chaos (2–4): looks up at the words, chips fly -> panic (X eyes, flailing), blinds -> shakes it off
  pose(2.2, { hYaw: 18, hPitch: -16, yaw: 10, lookX: 0.6, lookY: 1, smile: 0.2, hRoll: 0 });
  pose(2.6, { hYaw: 8, lookX: 0.2 });
  pose(2.9, { xe: 0, mo: 0 }); pose(3.05, { xe: 1, mo: 0.9, smile: 0 });
  const FL = [[2.98, 120, 40], [3.14, 150, 80], [3.3, 115, 30], [3.46, 150, 70]];
  FL.forEach(([t, a, b], i) => { armL(t, i % 2 ? a : 150 - (a - 115), 10, b, 90); armR(t, i % 2 ? 150 - (a - 115) : a, 10, 110 - b, 90); });
  [[2.98, -6], [3.1, 6], [3.22, -5], [3.34, 6], [3.46, -4]].forEach(([t, r]) => pose(t, { roll: r, hRoll: -r * 0.8 }));
  pose(3.58, { roll: 0, hRoll: 0 });
  [[3.58, -20], [3.7, 18], [3.82, -12], [3.94, 0]].forEach(([t, v]) => pose(t, { hYaw: v }));
  pose(3.7, { xe: 1 }); pose(3.95, { xe: 0, mo: 0, smile: 0.6, hPitch: 0, lookX: 0, lookY: 0 });
  armL(3.6, 22, 0, 10, 90); armR(3.6, 22, 0, 10, 90); armL(4.0, 20, 0, 10, 0); armR(4.0, 20, 0, 10, 0);
  // T2 -> S3: glide to the bottom-right
  pose(3.6, { x: 300, y: 1690, h: 470 }); pose(4.12, { x: 840, y: 1700, h: 460 });
  pose(3.6, { yaw: 0 }); pose(3.85, { yaw: 25, roll: -8 }); pose(4.15, { yaw: -15, roll: 0 });
  pose(3.9, { sh: 0.5, rim: 2.0 }); pose(4.05, { sh: 0.3, rim: 1 });
  // S3 · points at the coin, surprised by the split, nods
  pose(4.15, { hYaw: -22, hPitch: -14, lookX: -1, lookY: 1 });
  armR(4.05, 20, 0, 12, 0); armR(4.4, 128, 28, 10, 0, "o");
  pose(4.75, { mo: 0, smile: 0.6 }); pose(4.88, { mo: 1, smile: 0 });
  pose(4.78, { y: 1700 }); pose(4.92, { y: 1650 }, "o"); pose(5.15, { y: 1700 });
  armL(4.78, 12, 0, 10, 0); armL(4.95, 60, 20, 40, 90); armL(5.3, 15, 0, 10, 0);
  pose(5.15, { mo: 0, smile: 1, hPitch: -14 }); pose(5.3, { hPitch: -4 }); pose(5.45, { hPitch: -14 });
  // T3 -> S4: slides down-left with the diagonal wipe and comes forward to HALF-BODY (explaining)
  armR(5.5, 128, 28, 10, 0); armR(5.75, 25, 0, 15, 0);
  pose(5.55, { x: 840, y: 1700, h: 460 }); pose(6.12, { x: 290, y: 1640, h: 820 });
  pose(5.55, { roll: 0, yaw: -15 }); pose(5.8, { roll: 12, yaw: -28 }); pose(6.15, { roll: 0, yaw: 16 });
  // S4 · half-body: thinking (hand to chin, squint) -> flinch at the slice -> points up at "Perlu dicek", nods
  pose(6.15, { hYaw: 16, hPitch: -10, lookX: 1, lookY: 0.6, squint: 0.4, smile: 0 });
  armR(6.0, 25, 0, 15, 0); armR(6.3, 22, 72, 118, 0);
  pose(6.4, { y: 1640 }); pose(6.5, { y: 1656 }); pose(6.62, { y: 1640 });
  pose(6.72, { squint: 0.4, mo: 0 }); pose(6.85, { squint: 0, mo: 0.5, hPitch: -6, lookY: 0.6 });
  armL(6.7, 12, 0, 10, 0); armL(6.95, 118, 30, 8, 0, "o");
  pose(7.2, { mo: 0, smile: 0.8 }); pose(7.3, { hPitch: -14 }); pose(7.42, { hPitch: -2 }); pose(7.55, { hPitch: -10 });
  // T4 -> S5: stays half-body, settles bottom-left and turns toward the right (where the hologram will appear)
  armR(7.4, 22, 72, 118, 0); armR(7.7, 18, 0, 14, 0); armL(7.45, 118, 30, 8, 0); armL(7.75, 15, 0, 12, 0);
  pose(7.5, { x: 290, y: 1640, h: 820 }); pose(8.12, { x: 250, y: 1620, h: 1000 });
  pose(7.5, { sh: 0.3, rim: 1 }); pose(7.95, { sh: 0.5, rim: 2.0 });
  pose(7.6, { yaw: 16 }); pose(8.15, { yaw: 30 });
  // S5 · watches the puzzle snap above, celebrates, then the chest M projects the MasterPajak AI hologram
  pose(8.12, { hYaw: 6, hPitch: -22, lookX: 0.3, lookY: 1, smile: 0.6, squint: 0 });
  pose(8.74, { happy: 0, smile: 0.6 }); pose(8.9, { happy: 1, smile: 1 });
  pose(8.76, { y: 1620 }); pose(8.95, { y: 1592 }, "o"); pose(9.15, { y: 1620 });
  armR(8.15, 15, 0, 12, 0); armR(8.92, 145, 0, 30, 90, "o"); armR(9.12, 145, 0, 62, 90); armR(9.32, 145, 0, 30, 90);
  armL(8.15, 15, 0, 12, 0); armL(8.7, 20, -50, 14, 0);
  pose(9.0, { hYaw: 24, hPitch: 0, lookX: 1, lookY: -0.4 });
  key("hx", 0, 808, "hold"); key("hy", 0, 1560, "hold"); key("hw", 0, 500, "hold");
  pose(8.6, { chest: 0 }); pose(8.8, { chest: 1 });
  key("holoA", 0, 0, "hold"); key("holoA", 8.78, 0, "hold"); key("holoA", 8.92, 1, "o");
  key("holoRev", 0, 0, "hold"); key("holoRev", 8.82, 0, "hold"); key("holoRev", 9.3, 1.1, "o");
  key("holoGl", 0, 0, "hold"); key("holoGl", 9.38, 0, "hold"); key("holoGl", 9.42, 0.8, "lin"); key("holoGl", 9.5, 0, "lin");
  // T5 · flies into the camera with the zoom-through (hologram powers down), fades under the flash
  armR(9.5, 145, 0, 30, 90); armR(9.78, 60, 40, 20, 0);
  pose(9.5, { x: 250, y: 1620, h: 1000 }); pose(9.98, { x: 420, y: 1250, h: 3200 }, "i");
  key("op", 0, 1, "hold"); key("op", 9.86, 1, "hold"); key("op", 9.97, 0, "lin");
  key("holoA", 9.52, 1, "hold"); key("holoA", 9.72, 0, "i"); pose(9.5, { chest: 1 }); pose(9.72, { chest: 0 });
  pose(9.5, { happy: 1 }); pose(9.7, { happy: 0, mo: 0.8, hPitch: 0, lookY: 0, hYaw: 0 });
  // S6 · full body: slides in from the right, points at the "?", reads the typewriter line, nods
  pose(10.0, { x: 1320, y: 1000, h: 440, mo: 0, smile: 1, chest: 0 }, "hold"); key("op", 10.02, 1, "hold");
  pose(10.45, { x: 920, y: 1000, h: 440 }, "o");
  pose(10.0, { roll: -14, yaw: -25 }, "hold"); pose(10.5, { roll: 0, yaw: -12 });
  pose(10.0, { sh: 0.3, rim: 1 }, "hold");
  armR(10.0, 20, 0, 15, 0, "hold"); armL(10.0, 20, 0, 15, 0, "hold");
  armR(10.6, 86, 22, 6, 0, "o");
  pose(10.55, { hYaw: -22, hPitch: -4, lookX: -1, lookY: 0.2 });
  pose(10.85, { hPitch: 14, lookY: -1, lookX: -0.6, hYaw: -14 });
  armR(10.95, 86, 22, 6, 0); armR(11.15, 22, 0, 12, 0);
  pose(11.1, { hPitch: 6 }); pose(11.22, { hPitch: 16 }); pose(11.34, { hPitch: 6 });
  pose(11.4, { hYaw: -26, lookX: -1, lookY: -1, smile: 1, happy: 0.6 });
  // T6 · ducks out of the frame as the beam floods
  pose(11.55, { x: 920, y: 1000, h: 440 }); pose(11.92, { x: 920, y: 2400, h: 440 }, "i");
  pose(11.55, { roll: 0 }); pose(11.8, { roll: 10 });
  // S7 · HALF-BODY end card: rises bottom-right, waves, projects the logo hologram to the left, points at the CTA
  pose(11.99, { x: 830, y: 2650, h: 1000, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0, happy: 0, chest: 0 }, "hold");
  pose(11.99, { sh: 0.5, rim: 2.0 }, "hold");
  armL(11.99, 18, 0, 14, 0, "hold"); armR(11.99, 20, -50, 14, 0, "hold");
  pose(12.48, { y: 1620 }, "o");
  pose(12.5, { happy: 1, smile: 1 });
  armL(12.5, 145, 0, 30, 90, "o"); armL(12.72, 145, 0, 62, 90); armL(12.94, 145, 0, 30, 90); armL(13.16, 145, 0, 60, 90); armL(13.36, 145, 0, 32, 90);
  key("hx", 11.99, 272, "hold"); key("hy", 11.99, 1560, "hold"); key("hw", 11.99, 500, "hold");
  pose(12.62, { chest: 0 }); pose(12.8, { chest: 1 });
  key("holoA", 12.74, 0, "hold"); key("holoA", 12.9, 1, "o");
  key("holoRev", 12.78, 0, "hold"); key("holoRev", 13.42, 1.1, "o");
  key("holoGl", 13.86, 0, "hold"); key("holoGl", 13.9, 0.85, "lin"); key("holoGl", 13.98, 0, "lin");
  key("holoGl", 14.56, 0, "hold"); key("holoGl", 14.6, 0.6, "lin"); key("holoGl", 14.67, 0, "lin");
  pose(12.85, { hYaw: -22, hPitch: 8, lookX: -1, lookY: -0.5, happy: 0 }); pose(13.4, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0, happy: 1 });
  armL(13.55, 162, 18, 8, 0, "o"); pose(13.62, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10, happy: 0 });
  armL(14.35, 162, 18, 8, 0); armL(14.7, 18, 0, 14, 0);
  pose(14.4, { hPitch: -22 }); pose(14.7, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });

  // sort keys (they are added out of order)
  for (const ch in KEYS) KEYS[ch].sort((a, b) => a[0] - b[0]);
  // hold-then-move: a key is the moment a pose is REACHED; the move into it takes at most MAXD[group] seconds and the
  // previous pose is held until then (sparse keys would otherwise drift for seconds, e.g. a mouth slowly opening)
  const MAXD = { pos: 0.75, body: 0.55, head: 0.45, arm: 0.5, look: 0.3, face: 0.3 };
  for (const ch in KEYS) {
    if (RAW[ch]) continue; const md = MAXD[G[ch]] || 0.5, ks = KEYS[ch], out = [ks[0]];
    for (let i = 1; i < ks.length; i++) {
      const a = out[out.length - 1], b = ks[i];
      if (b[0] - a[0] > md + 1e-6 && b[2] !== "hold" && a[1] !== b[1]) out.push([b[0] - md, a[1], "hold"]);
      out.push(b);
    }
    KEYS[ch] = out;
  }

  // ---------------- per-frame state ----------------
  function state(t) {
    const v = {}; for (const ch in DEF) v[ch] = F(ch, t);
    const h = v.h, y = v.y + hover(t, h);
    // squash & stretch from the vertical acceleration of the (filtered) path
    let cut = -1e9; for (const q of CUTS) if (q <= t) cut = q;
    const dd = 1 / 60, yA = F("y", Math.max(cut, t - dd)), yB = F("y", t + dd), ay = (yB - 2 * v.y + yA) / (dd * dd);
    const squash = Math.max(-0.07, Math.min(0.07, (-ay / h) * 0.0022)) + Math.sin((2 * Math.PI * t) / 1.9 + 1.2) * 0.006;
    // antenna: lags behind the head (difference between a slow wobbly spring and the head motion)
    const sig = (ch, tt) => (ch === "z" ? (F("x", tt) / F("h", tt)) * 55 + F("roll", tt) + F("hRoll", tt) : -(F("y", tt) / F("h", tt)) * 55 + F("pitch", tt) + F("hPitch", tt));
    const kA = kernel(2.4, 0.2), step = 3;
    let az = 0, ax = 0, wsum = 0;
    for (let i = 0; i < kA.length; i += step) { const tt = Math.max(cut, t - i * DT); az += kA[i] * sig("z", tt); ax += kA[i] * sig("x", tt); wsum += kA[i]; }
    az = az / wsum - sig("z", t); ax = ax / wsum - sig("x", t);
    const clamp = (a, m) => Math.max(-m, Math.min(m, a));
    const idleL = Math.sin(t * 2.1) * 3, idleR = Math.sin(t * 2.1 + 1.7) * 3;
    return {
      x: v.x, y, h, opacity: Math.max(0, Math.min(1, v.op)), yaw: v.yaw, pitch: v.pitch, roll: v.roll + Math.sin((2 * Math.PI * t) / 2.7) * 1.2, squash,
      headYaw: v.hYaw, headPitch: v.hPitch, headRoll: v.hRoll, antZ: clamp(az * 0.9, 28), antX: clamp(ax * 0.9, 22),
      aL: { raise: v.lR + idleL, fwd: v.lF, bend: v.lB + idleL, bendYaw: v.lY }, aR: { raise: v.rR + idleR, fwd: v.rF, bend: v.rB + idleR, bendYaw: v.rY },
      face: { blink: Math.max(blink(t), v.squint), lookX: v.lookX, lookY: v.lookY, happy: Math.max(0, Math.min(1, v.happy)), x: Math.max(0, Math.min(1, v.xe)),
              smile: v.smile, o: Math.max(0, Math.min(1, v.mo)) },
      rim: v.rim, shadow: v.sh, t, chest: Math.max(0, Math.min(1, v.chest)),
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
