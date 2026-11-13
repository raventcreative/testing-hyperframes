/* AIpreneur reel FX kit (motion style v3, client reference "MasterPajak"-like explainer motion):
   - robot co-star: moves between poses (home / center / right / close-up), hops, dips out and pops back in through
     transitions, shivers, side-aware point / wave / beat gestures, eye expressions (happy, x, wide, excited)
   - scene themes inside one reel (light <-> dark) switched under full-frame wipes (stripes, blocks, diagonal sweep)
   - kinetic text helpers: letter drop, stickers, marker sweep
   Usage (after the robot rig setup, inside the composition IIFE):
     const FX = REEL_FX({ tl, ft, st, $, $$, D, rob, lh, rh, headIn, RG });
   Requirements in the page: #rmove wrapping #robot (full-frame box), #scene, #bgD (dark bg), #logoD/#logoL,
   #main[data-sc] caption styles. All tweens are deterministic (seek-safe). */
window.REEL_FX = function (c) {
  const { tl, ft, st, $, $$, rob, lh, rh, headIn, RG } = c;
  // ONE background theme per reel (client rule): c.base = "light" (white reels) or "dark" (blue reels).
  // Wipes only use shades of that theme; theme() never mixes backgrounds.
  const BASE = c.base || "light";
  const PAL = BASE === "dark" ? { a: "#132650", b: "#1f3f7a", acc: "#01ccf7" } : { a: "#ffffff", b: "#e4ecf8", acc: "#c3d4ee" };
  const NAVY = PAL.a, LIGHT = PAL.b, CYAN = PAL.acc;
  const rm = $("#rmove");
  const ns = "http://www.w3.org/2000/svg";

  /* ---------------- robot poses ---------------- */
  const POSE = { home: { x: 0, y: 0, scale: 1 }, center: { x: 222, y: 0, scale: 1 }, right: { x: 440, y: 0, scale: 1 },
    close: { x: 300, y: 250, scale: 1.4 }, closeL: { x: 40, y: 250, scale: 1.4 } };
  let cur = Object.assign({}, POSE.home);
  const track = [{ t: 0, p: cur }];
  const poseAt = (t) => { let p = track[0].p; track.forEach((k) => { if (k.t <= t) p = k.p; }); return p; };
  const side = (t) => (poseAt(t).x > 300 ? "R" : "L");
  st(rm, Object.assign({ transformOrigin: "318px 1990px" }, cur, { y: 700 }), 0);
  const squash = (at) => ft(rob, { scaleX: 1, scaleY: 1 }, { keyframes: [{ scaleX: 1.06, scaleY: 0.92, duration: 0.07, ease: "power1.out" }, { scaleX: 1, scaleY: 1, duration: 0.3, ease: "back.out(2.5)" }] }, at);
  const enter = (pose, at) => { const n = POSE[pose || "home"]; ft(rm, Object.assign({}, n, { y: 700 }), Object.assign({}, n, { duration: 0.55, ease: "back.out(1.4)" }), at); cur = n; track.push({ t: at, p: n }); squash(at + 0.5); };
  const go = (pose, at, dur) => { const n = POSE[pose]; dur = dur || 0.7; const dir = n.x > cur.x ? 1 : -1;
    ft(rm, { x: cur.x, scale: cur.scale }, { x: n.x, scale: n.scale, duration: dur, ease: "power2.inOut" }, at);
    ft(rm, { y: cur.y }, { keyframes: [{ y: Math.min(cur.y, n.y) - 70, duration: dur * 0.5, ease: "power2.out" }, { y: n.y, duration: dur * 0.5, ease: "power2.in" }] }, at);
    ft(rm, { rotation: 0 }, { keyframes: [{ rotation: 7 * dir, duration: dur * 0.35, ease: "power2.out" }, { rotation: -3 * dir, duration: dur * 0.4, ease: "sine.inOut" }, { rotation: 0, duration: dur * 0.25 }] }, at);
    squash(at + dur - 0.02); cur = n; track.push({ t: at + dur * 0.5, p: n }); };
  const dip = (pose, at, gap) => { const n = POSE[pose]; gap = gap == null ? 0.25 : gap;
    ft(rm, Object.assign({}, cur), { keyframes: [{ y: 700, duration: 0.28, ease: "power2.in" }, { x: n.x, scale: n.scale, duration: 0.01 }, { y: n.y, duration: 0.5, delay: gap, ease: "back.out(1.5)" }] }, at);
    squash(at + 0.28 + gap + 0.47); cur = n; track.push({ t: at + 0.3, p: n }); };
  const hop = (at, h) => { const y = cur.y; ft(rm, { y }, { keyframes: [{ y: y - (h || 55), duration: 0.18, ease: "power2.out" }, { y, duration: 0.2, ease: "power2.in" }] }, at); squash(at + 0.37); };
  const shiver = (at, dur) => { const x = cur.x, k = []; for (let i = 0; i < Math.round((dur || 0.5) / 0.05); i++) k.push({ x: x + (i % 2 ? -9 : 9), duration: 0.05 }); k.push({ x, duration: 0.05 });
    ft(rm, { x }, { keyframes: k }, at); };

  /* ---------------- eye expressions ---------------- */
  const EX = { happy: '<path d="M5 47 Q22 12 39 47" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/>',
    x: '<path d="M8 19 L36 51 M36 19 L8 51" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>',
    wide: '<ellipse cx="22" cy="35" rx="25" ry="38" fill="#fff"/><circle cx="22" cy="35" r="7" fill="#0b1020"/>',
    exL: '<path d="M7 17 L37 35 L7 53" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
    exR: '<path d="M37 17 L7 35 L37 53" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
    flat: '<path d="M5 36 L39 36" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>' };
  const covs = [], exs = [];
  RG.eyes.forEach((e, i) => {
    const x = e[0] - RG.head[0], y = e[1] - RG.head[1];
    const cv = document.createElement("i"); cv.className = "ecov";
    Object.assign(cv.style, { position: "absolute", left: x - 6 + "px", top: y - 6 + "px", width: e[2] + 12 + "px", height: e[3] + 12 + "px", borderRadius: "50%", background: "#030407", opacity: 0, display: "block" });
    headIn.appendChild(cv); covs.push(cv);
    const sv = document.createElementNS(ns, "svg"); sv.setAttribute("viewBox", "0 0 44 70"); sv.setAttribute("class", "eex");
    Object.assign(sv.style, { position: "absolute", left: x + "px", top: y + "px", width: e[2] + "px", height: e[3] + "px", overflow: "visible",
      filter: "drop-shadow(0 0 3px rgba(220,240,255,0.95)) drop-shadow(0 0 9px rgba(120,190,255,0.6))" });
    const keys = ["happy", "x", "wide", i === 0 ? "exL" : "exR", "flat"];
    sv.innerHTML = keys.map((k) => `<g data-k="${k === "exL" || k === "exR" ? "excited" : k}" style="opacity:0;transform-origin:22px 35px">${EX[k]}</g>`).join("");
    headIn.appendChild(sv); exs.push(sv);
  });
  const face = (name, at, dur) => { const gs = exs.map((s) => s.querySelector(`[data-k="${name}"]`));
    ft(covs, { opacity: 0 }, { opacity: 1, duration: 0.06 }, at);
    ft(gs, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.18, ease: "back.out(2.2)" }, at + 0.02);
    ft(gs, { opacity: 1 }, { opacity: 0, duration: 0.1 }, at + dur);
    ft(covs, { opacity: 1 }, { opacity: 0, duration: 0.08 }, at + dur + 0.04); };

  /* ---------------- side-aware gestures (scheduled, never overlapping) ---------------- */
  const G = [];
  const point = (at) => G.push({ t: at, k: "point", d: 1.5 });
  const wave = (at) => G.push({ t: at, k: "wave", d: 1.4 });
  const beat = (at) => G.push({ t: at, k: "beat", d: 0.55 });
  const runGestures = () => {
    G.sort((a, b) => a.t - b.t); let busy = -1, n = 0;
    G.forEach((g) => { if (g.t < busy + 0.05) return; busy = g.t + g.d; const R = side(g.t + 0.2) === "R";
      if (g.k === "wave") { const h = R ? rh : lh, m = R ? -1 : 1;
        ft(h, { x: 0, y: 0, rotation: 0 }, { keyframes: [{ x: 10 * m, y: -95, rotation: 20 * m, duration: 0.28, ease: "power2.out" }, { rotation: -18 * m, duration: 0.2 }, { rotation: 20 * m, duration: 0.2 },
          { rotation: -15 * m, duration: 0.2 }, { x: 0, y: 0, rotation: 0, duration: 0.45, ease: "power2.inOut" }] }, g.t); }
      if (g.k === "point") { const h = R ? lh : rh, m = R ? -1 : 1;
        ft(h, { x: 0, y: 0, rotation: 0 }, { keyframes: [{ x: 40 * m, y: -150, rotation: -38 * m, duration: 0.33, ease: "power2.out" }, { x: 40 * m, y: -150, rotation: -38 * m, duration: 0.7 },
          { x: 0, y: 0, rotation: 0, duration: 0.45, ease: "power2.inOut" }] }, g.t);
        ft(rob, { rotation: 0 }, { keyframes: [{ rotation: 3 * m, duration: 0.33, ease: "power2.out" }, { rotation: 3 * m, duration: 0.7 }, { rotation: 0, duration: 0.45, ease: "power2.inOut" }] }, g.t); }
      if (g.k === "beat") { const hand = n++ % 2 ? lh : rh, dir = hand === lh ? 1 : -1;
        ft(hand, { x: 0, y: 0, rotation: 0 }, { keyframes: [{ y: -40, rotation: 12 * dir, duration: 0.2, ease: "power2.out" }, { y: 0, rotation: 0, duration: 0.32, ease: "power2.in" }] }, g.t); } });
  };

  /* ---------------- scene themes + full-frame wipes ---------------- */
  const scene = $("#scene");
  const fx = document.createElement("div"); fx.id = "fx"; Object.assign(fx.style, { position: "absolute", inset: "0", zIndex: 45, pointerEvents: "none", overflow: "hidden" }); scene.appendChild(fx);
  const theme = (name, at) => { name = BASE; const d = name === "dark";
    st("#bgD", { opacity: d ? 1 : 0 }, at); st("#dots", { opacity: d ? 0.12 : 0.6 }, at);
    st("#logoD", { opacity: d ? 0 : 1 }, at); st("#logoL", { opacity: d ? 1 : 0 }, at);
    st("#main", { attr: { "data-sc": name } }, at); };
  const colOf = () => PAL.a;
  const mk = (css) => { const el = document.createElement("div"); Object.assign(el.style, { position: "absolute" }, css); fx.appendChild(el); return el; };
  // vertical bars slide in from alternate ends, scene switches under them, bars continue out
  const stripes = (at, to, onMid) => { const n = 7, w = 1080 / n, bars = [];
    for (let i = 0; i < n; i++) bars.push(mk({ left: i * w - 1 + "px", top: "0px", width: w + 2 + "px", height: "1920px", background: i % 2 ? LIGHT : NAVY, opacity: 0 }));
    bars.forEach((b, i) => { const s = i % 2 ? 1 : -1; const t0 = at + i * 0.035;
      ft(b, { yPercent: 100 * s, opacity: 1 }, { yPercent: 0, duration: 0.3, ease: "power3.in" }, t0);
      ft(b, { yPercent: 0 }, { yPercent: -100 * s, duration: 0.34, ease: "power3.out" }, at + 0.58 + i * 0.035);
      st(b, { opacity: 0 }, at + 0.58 + i * 0.035 + 0.35); st(b, { opacity: 0 }, 0); });
    const mid = at + 0.3 + (n - 1) * 0.035 + 0.02; theme(to, mid); if (onMid) onMid(mid); return mid; };
  // block grid pops in (pseudo-random order), switch, pops out
  const blocks = (at, to, onMid) => { const cols = 6, rows = 10, bw = 180, bh = 192, list = [];
    let seed = 7; const rnd = () => ((seed = (seed * 9301 + 49297) % 233280) / 233280);
    for (let r = 0; r < rows; r++) for (let q = 0; q < cols; q++) { const k = rnd(); const acc = k > 0.86;
      list.push({ el: mk({ left: q * bw + "px", top: r * bh + "px", width: bw + 1 + "px", height: bh + 1 + "px", background: acc ? PAL.b : colOf(to), opacity: 0 }), o: rnd() }); }
    list.forEach(({ el, o }) => { st(el, { opacity: 0 }, 0);
      ft(el, { scale: 0, opacity: 1 }, { scale: 1, duration: 0.16, ease: "power2.out" }, at + o * 0.32);
      ft(el, { scale: 1 }, { scale: 0, duration: 0.16, ease: "power2.in" }, at + 0.6 + o * 0.32); st(el, { opacity: 0 }, at + 0.6 + o * 0.32 + 0.17); });
    const mid = at + 0.5; theme(to, mid); if (onMid) onMid(mid); return mid; };
  // rotated band sweeps across with a cyan leading edge
  const sweep = (at, to, onMid) => {
    const band = mk({ left: "-760px", top: "-700px", width: "2600px", height: "3320px", background: colOf(to), opacity: 0 });
    const edge = mk({ left: "-760px", top: "-700px", width: "120px", height: "3320px", background: CYAN, opacity: 0 });
    [band, edge].forEach((e) => st(e, { opacity: 0, rotation: 18 }, 0));
    ft(edge, { x: 2050, rotation: 18, opacity: 1 }, { x: -60, duration: 0.42, ease: "power3.in" }, at - 0.05);
    ft(band, { x: 2150, rotation: 18, opacity: 1 }, { x: 0, duration: 0.42, ease: "power3.in" }, at);
    ft([band, edge], { x: (i) => (i ? -60 : 0) }, { x: (i) => (i ? -2900 : -2700), duration: 0.45, ease: "power3.out" }, at + 0.5);
    st([band, edge], { opacity: 0 }, at + 0.97);
    const mid = at + 0.44; theme(to, mid); if (onMid) onMid(mid); return mid; };

  /* ---------------- kinetic text helpers ---------------- */
  const split = (el) => { const t = el.textContent; el.textContent = ""; const cls = el.dataset.letter || "";
    return Array.from(t).map((ch) => { const s = document.createElement("span"); s.textContent = ch === " " ? " " : ch; s.className = cls; s.style.display = "inline-block"; el.appendChild(s); return s; }); };
  const drop = (el, at, gapS) => { const L = split(el); let k = 3;
    L.forEach((s, i) => { k = (k * 7 + 3) % 11; ft(s, { y: -110, rotation: (k - 5) * 6, opacity: 0 }, { y: 0, rotation: 0, opacity: 1, duration: 0.42, ease: "back.out(2)" }, at + i * (gapS || 0.04)); st(s, { opacity: 0 }, 0); }); return L; };
  const sticker = (el, at, rot) => { st(el, { opacity: 0 }, 0); ft(el, { opacity: 0, scale: 0.3, rotation: rot * 3 }, { opacity: 1, scale: 1, rotation: rot, duration: 0.35, ease: "back.out(2.4)" }, at); };
  const marker = (el, at, dur) => ft(el, { scaleX: 0 }, { scaleX: 1, duration: dur || 0.35, ease: "power2.inOut", transformOrigin: "0% 50%" }, at);

  return { POSE, enter, go, dip, hop, shiver, face, point, wave, beat, runGestures, poseAt, side, theme, stripes, blocks, sweep, drop, sticker, marker, split };
};
