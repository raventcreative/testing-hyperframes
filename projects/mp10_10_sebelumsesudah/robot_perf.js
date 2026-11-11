// MasterPajak AI robot host — Video 10 'Sebelum vs Sesudah'. Beat times come from window.TM, drag geometry from window.RIG
// (index.html head). Keyframed channels -> hold-then-move -> per-group 2nd-order spring filter (convolution, seek-safe) -> idle
// layers (hover, breathing, blinks) -> lip-sync from lipsync.js + speech head beats -> derived secondary motion (squash, antenna lag).
// The robot hosts every scene: presents the SEBELUM world, grabs the divider knob and drags it (the knob follows the robot's hand,
// sampled from ROBOT_POS in index.html), then presents the SESUDAH world. Hologram panels stay inside the 120 px side safe zone.
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
  const CUTS = [window.TM.l5 - 0.01];
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

  // ---------------- choreography (all times from window.TM / window.RIG, so a VO re-time moves everything) ----------------
  const TM = window.TM, RIG = window.RIG, [D1, D2, D3] = RIG.drags, H = RIG.H, Y = RIG.Y, EN = TM.l5;
  const pose = (t, o, e) => { for (const k in o) key(k, t, o[k], e); };
  const armL = (t, r, f, b, y, e) => pose(t, { lR: r, lF: f, lB: b, lY: y }, e), armR = (t, r, f, b, y, e) => pose(t, { rR: r, rF: f, rB: b, rY: y }, e);
  const NAVY = { sh: 0.5, rim: 2.0 }, LIGHT = { sh: 0.32, rim: 1.0 };
  const REST = (t, e) => { armL(t, 15, 0, 10, 0, e); armR(t, 15, 0, 10, 0, e); };
  // drag: look at the knob, turn, reach back and grab, walk it across, let go (the divider then snaps open on its own)
  const DRAG = (g, after) => {
    const s = g.side, arm = s > 0 ? armL : armR;
    pose(g.reach - 0.25, { hYaw: 32 * s, hPitch: 0, hRoll: 0, lookX: s, lookY: 0.1, happy: 0, xe: 0, smile: 1 });
    pose(g.reach + 0.3, { yaw: -20 * s });
    arm(g.reach, 15, 0, 10, 0, "hold"); arm(g.grab, 115, -20, 5, 0, "o"); arm(g.rel, 115, -20, 5, 0, "hold");
    pose(g.t0, { x: g.rx0 }, "hold"); pose(g.t1, { x: g.rx1 }, "io");
    pose(g.t0 + 0.1, { hYaw: -8 * s, lookX: -0.5 * s, lookY: 0 });
    pose(g.t1 - 0.25, LIGHT); pose(g.t1 + 0.15, NAVY);                       // the SESUDAH world lights the robot navy
    after(arm, s);
  };
  key("hx", 0, 750, "hold"); key("hy", 0, 1440, "hold"); key("hw", 0, 420, "hold");
  key("holoA", 0, 0, "hold"); key("holoRev", 0, 0, "hold"); key("holoGl", 0, 0, "hold");
  const glitch = (g0) => { key("holoGl", g0, 0, "hold"); key("holoGl", g0 + 0.04, 0.7, "lin"); key("holoGl", g0 + 0.12, 0, "lin"); };

  // C1 · SEBELUM: rises in at the bottom centre, presents the files, x-eyes at "nggak pernah cocok"
  pose(0, Object.assign({ x: D1.rx0, y: 2700, h: H, yaw: -14, hYaw: 0, hPitch: 0, hRoll: 0, lookX: 0, lookY: 0, smile: 1, happy: 0, xe: 0, squint: 0, chest: 0 }, LIGHT)); REST(0);
  // (rises with the camera pull-back, so it never sits on the close-up of the files)
  const RZ = TM.tf - 0.5;
  pose(RZ, { y: 2700 }, "hold"); pose(RZ + 0.7, { y: Y }, "o");
  pose(RZ + 0.45, { happy: 1 }); pose(RZ + 0.95, { happy: 0 });
  pose(RZ + 0.6, { hYaw: -16, hPitch: -12, lookX: -0.7, lookY: 0.8 }); pose(TM.tf + 0.5, { hYaw: 12, hPitch: -10, lookX: 0.5, lookY: 0.7 });
  armR(RZ + 0.5, 15, 0, 10, 0, "hold"); armR(RZ + 0.9, 128, 25, 18, 0, "o"); armR(TM.nc - 0.05, 128, 25, 18, 0); armR(TM.nc + 0.3, 15, 0, 10, 0);
  pose(3.4, { xe: 0, smile: 1 }); pose(3.6, { xe: 1, smile: 0 }); pose(4.45, { xe: 1, smile: 0 }); pose(4.7, { xe: 0, smile: 1 });
  pose(3.5, { hYaw: -30, hPitch: -4 }); pose(3.75, { hYaw: 30 }); pose(4.0, { hYaw: -24 }); pose(4.25, { hYaw: 18 }); pose(4.5, { hYaw: 0, lookX: 0, lookY: 0.2 });
  // C1 · drag -> SESUDAH (brand moment): faces right, chest hologram, points along the flow with the near arm
  DRAG(D1, (arm) => {
    pose(D1.rel + 0.1, { yaw: 26, hYaw: 0, hPitch: 0, lookX: 0, lookY: 0 }); pose(D1.rel + 0.5, { happy: 1 }); pose(D1.rel + 1.1, { happy: 0 });
  });
  const HB = D1.rel + 0.15, HE = TM.l3 - 0.35;
  pose(HB - 0.1, { chest: 0 }); pose(HB + 0.15, { chest: 1 });
  key("holoA", HB, 0, "hold"); key("holoA", HB + 0.22, 1, "o"); key("holoRev", HB + 0.06, 0, "hold"); key("holoRev", HB + 1.26, 1.1, "o");
  glitch(HB + 1.9); glitch(HB + 3.4);
  pose(TM.cj - 0.1, { hYaw: 4, hPitch: -22, lookX: 0.2, lookY: 1 });
   armL(TM.cj + 0.05, 174, 4, 6, 0, "o"); armL(TM.pb - 0.25, 174, 4, 6, 0);
  pose(TM.pb, { hYaw: 14, hPitch: -14, lookX: 0.6, lookY: 0.8 }); armL(TM.pb + 0.05, 168, 8, 6, 0, "o"); armL(TM.lp - 0.2, 168, 8, 6, 0);
  pose(TM.lp, { hYaw: 22, hPitch: -6, lookX: 0.9, lookY: 0.4 }); armL(TM.lp + 0.05, 163, 12, 6, 0, "o"); armL(TM.sa + 0.2, 163, 12, 6, 0); armL(TM.sa + 0.55, 15, 0, 10, 0);
  pose(TM.sa + 0.15, { happy: 1, hPitch: -8, hYaw: 6, lookX: 0, lookY: 0 }); pose(TM.sa + 0.45, { hPitch: 4 }); pose(TM.sa + 0.7, { hPitch: -4 }); pose(TM.sa + 1.2, { happy: 0, hPitch: 0 });
  key("holoA", HE, 1, "hold"); key("holoA", HE + 0.2, 0, "i"); pose(HE, { chest: 1 }); pose(HE + 0.25, { chest: 0 });

  // whip C1 -> C2: glides to the centre with the camera, light again
  const W1 = TM.l3 - 0.3, W2 = TM.l4 - 0.3;
  pose(W1, Object.assign({ x: D1.rx1, yaw: 26 }, NAVY), "hold"); pose(W1 + 0.6, Object.assign({ x: D2.rx0, yaw: 0 }, LIGHT), "io");
  // C2 · SEBELUM: nebak-nebak — scratches its head, head tilts side to side
  armL(TM.l3 + 0.1, 15, 0, 10, 0, "hold"); armL(TM.l3 + 0.5, 155, 20, 110, 0, "o"); armL(TM.l3 + 1.0, 155, 20, 110, 0); armL(TM.l3 + 1.35, 15, 0, 10, 0);
  pose(TM.l3 + 0.45, { hRoll: -11, hYaw: -6, hPitch: -8, lookX: -0.4, lookY: 0.8, smile: 0.3 }); pose(TM.l3 + 0.85, { hRoll: 9, hYaw: 6, lookX: 0.4 });
  DRAG(D2, (arm) => {
    pose(D2.rel + 0.1, { yaw: -25, hYaw: -14, hPitch: -10, lookX: -0.8, lookY: 0.7 });
    arm(TM.jl + 0.05, 132, 22, 12, 0, "o"); arm(TM.jl + 0.95, 132, 22, 12, 0); arm(TM.jl + 1.3, 15, 0, 10, 0);
    pose(TM.jl + 0.25, { happy: 1 }); pose(TM.jl + 1.2, { happy: 0, hYaw: -6, hPitch: 0, lookX: 0, lookY: 0 });
  });
  // whip C2 -> C3
  pose(W2, Object.assign({ x: D2.rx1, yaw: -25 }, NAVY), "hold"); pose(W2 + 0.6, Object.assign({ x: D3.rx0, yaw: 0 }, LIGHT), "io");
  // C3 · SEBELUM: bingung — shrug, flat mouth
  armL(TM.l4 + 0.1, 15, 0, 10, 0, "hold"); armL(TM.l4 + 0.45, 45, 30, 100, -40, "o"); armL(TM.l4 + 0.95, 45, 30, 100, -40); armL(TM.l4 + 1.3, 15, 0, 10, 0);
  armR(TM.l4 + 0.1, 15, 0, 10, 0, "hold"); armR(TM.l4 + 0.45, 45, 30, 100, -40, "o"); armR(TM.l4 + 0.95, 45, 30, 100, -40); armR(TM.l4 + 1.3, 15, 0, 10, 0);
  pose(TM.l4 + 0.45, { hRoll: 13, hYaw: 0, hPitch: -4, lookY: 0.3, lookX: 0, smile: 0, squint: 0.15 }); pose(TM.l4 + 1.1, { hRoll: 0, squint: 0 });
  DRAG(D3, (arm) => {
    pose(D3.rel + 0.1, { yaw: 26, hYaw: 6, hPitch: -16, lookX: 0.3, lookY: 0.9 });
    arm(D3.rel + 0.45, 150, 15, 10, 0, "o"); arm(TM.ta - 0.15, 150, 15, 10, 0); arm(TM.ta + 0.2, 120, 26, 8, 0, "o"); arm(TM.ta + 1.0, 120, 26, 8, 0); arm(TM.ta + 1.35, 15, 0, 10, 0);
    pose(TM.ta, { hYaw: 20, hPitch: -4, lookX: 0.9, lookY: 0.3 }); pose(TM.ta + 0.6, { happy: 1 }); pose(TM.ta + 1.4, { happy: 0, hYaw: 4, hPitch: 0, lookX: 0, lookY: 0 });
  });
  // T · ducks out under the beam
  pose(EN - 0.5, { x: D3.rx1, y: Y, h: H }); pose(EN - 0.06, { x: D3.rx1, y: 2700, h: H }, "i");
  // END · series end card: half-body bottom-right, logo hologram left, waves, points at the CTA
  pose(EN - 0.01, Object.assign({ x: 870, y: 2700, h: 960, roll: 0, yaw: -30, hYaw: 0, hPitch: 0, hRoll: 0, lookX: 0, lookY: 0, happy: 0, smile: 1, xe: 0, squint: 0, chest: 0 }, NAVY), "hold");
  armL(EN - 0.01, 18, 0, 14, 0, "hold"); armR(EN - 0.01, 20, -50, 14, 0, "hold");
  pose(EN + 0.5, { y: 1660 }, "o");
  key("hx", EN - 0.01, 360, "hold"); key("hy", EN - 0.01, 1500, "hold"); key("hw", EN - 0.01, 420, "hold");
  pose(EN + 0.4, { chest: 0 }); pose(EN + 0.65, { chest: 1 });
  key("holoA", EN + 0.52, 0, "hold"); key("holoA", EN + 0.75, 1, "o");
  key("holoRev", EN + 0.56, 0, "hold"); key("holoRev", EN + 1.76, 1.1, "o");
  glitch(EN + 4.4); glitch(EN + 7.0);
  armL(EN + 0.6, 18, 0, 14, 0); armL(EN + 0.85, 145, 0, 30, 90, "o"); armL(EN + 1.07, 145, 0, 62, 90); armL(EN + 1.29, 145, 0, 30, 90); armL(EN + 1.51, 145, 0, 58, 90); armL(EN + 1.9, 18, 0, 14, 0);
  pose(EN + 1.2, { happy: 1 }); pose(EN + 2.0, { hYaw: -24, hPitch: 6, lookX: -1, lookY: -0.4, happy: 0 }); pose(EN + 3.2, { hYaw: -4, hPitch: 0, lookX: 0, lookY: 0 });
  const CT = TM.cta - 0.2;
  armL(CT - 0.2, 18, 0, 14, 0); armL(CT + 0.15, 165, 25, 8, 0, "o"); armL(CT + 1.8, 165, 25, 8, 0); armL(CT + 2.1, 18, 0, 14, 0);
  pose(CT + 0.2, { hPitch: -22, lookY: 1, lookX: -0.4, hYaw: -10 }); pose(CT + 1.9, { hPitch: 0, lookY: 0, lookX: 0, hYaw: -6, happy: 1 });
  const WV = TM.bio + 0.4;
  armL(WV, 18, 0, 14, 0); armL(WV + 0.25, 145, 0, 30, 90, "o"); armL(WV + 0.47, 145, 0, 62, 90); armL(WV + 0.69, 145, 0, 30, 90); armL(WV + 0.91, 145, 0, 58, 90); armL(WV + 1.3, 18, 0, 14, 0);
  pose(WV + 1.6, { happy: 0 });

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
  // light-weight position probe for the slider rig (filtered x / y + hover / h, exactly what the render uses)
  window.ROBOT_POS = (t) => { const h = F("h", t); return { x: F("x", t), y: F("y", t) + hover(t, h), h }; };
  const cv = document.getElementById("robot");
  let robot = null, lastT = 0;
  const ready = window.RobotMP.create(cv, { url: "assets/robot/robot_mp.glb", width: 1080, height: 1920 }).then((r) => { robot = r; robot.render(state(lastT)); lastDrawn = lastT; return 1; });
  window.__robotReady = ready;
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {}; window.__hf.buildReady["robot"] = ready;
  let lastDrawn = -1;   // render once per frame (the timeline onUpdate and hf-seek both call this)
  window.ROBOT_APPLY = (t) => { lastT = t; if (robot && Math.abs(t - lastDrawn) > 1e-7) { robot.render(state(t)); lastDrawn = t; } };
  window.addEventListener("hf-seek", (e) => { const t = e.detail.time; if (robot) window.ROBOT_APPLY(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => window.ROBOT_APPLY(t))); });
})();
