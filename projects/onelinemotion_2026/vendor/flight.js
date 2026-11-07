// Shared, deterministic flight of the rocket (and its rider) — a pure function of global time.
// Used by compositions/rocket.html (rocket + "one line" trail) and compositions/robot.html (robot riding the rocket).
// Screen space 1080x1920. Rocket art points RIGHT; its centre is (x, y); rot in degrees (CSS: + = clockwise = nose down).
(function () {
  const SC = window.VO_SCENES, VW = window.VO_WORDS;
  const S = (id) => SC.find((s) => s.id === id);
  const wt = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after); return w ? w[1] : -99; };
  const one = (x) => Math.max(0, Math.min(1, x));
  const sm = (u) => { u = one(u); return u * u * (3 - 2 * u); };
  const e3 = (u) => { u = one(u); return 1 - Math.pow(1 - u, 3); };
  const ei3 = (u) => { u = one(u); return u * u * u; };
  const io3 = (u) => { u = one(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const L = (a, b, u) => a + (b - a) * u;
  const bump = (t, c, w) => Math.exp(-Math.pow((t - c) / w, 2));
  const WIDS = ["w01", "w02", "w03", "w04", "w05", "w06", "w07", "w08", "w09", "w10"];
  const WORLDS = WIDS.map((id) => S(id));
  const s02 = S("s02"), s13 = S("s13"), s16 = S("s16");
  const T = {
    arrive: wt("dan", s02.start) - 0.12,          // "dan satu garis…": the rocket swoops in
    launch: wt("terbang", s02.start) - 0.06,       // "terbang": lift-off
    w1: WORLDS[0].start, wEnd: s13.start,
    hop: wt("nggak", s13.start) - 0.15,            // the robot hops off in s13
    loop0: s16.start + 0.35, loop1: s16.start + 3.55,
  };
  const ANCHOR = { x: 600, y: 900 };               // rocket centre while crossing the worlds
  const HOVER = { x: 560, y: 760 };                // s02 hover point (above the caption band, above the mascot)
  const LAND = { x: 650, y: 800 };                 // s13 arrival point
  const SCROLL = 900;                              // px/s world scroll (the line flows left behind the rocket)
  function worldAt(t) { for (let i = WORLDS.length - 1; i >= 0; i--) if (t >= WORLDS[i].start && t < WORLDS[i].start + WORLDS[i].dur) return i; return -1; }
  // state: {vis, x, y, rot, s, flame, scroll, riding, world}
  function state(t) {
    const o = { vis: false, x: 0, y: 0, rot: 0, s: 1, flame: 1, scroll: 0, riding: false, world: worldAt(t) };
    if (t < T.arrive) return o;
    o.vis = true;
    if (t < T.launch) {                                           // swoop in from the left, settle into a hover
      const u = e3((t - T.arrive) / 0.8);
      o.x = L(-260, HOVER.x, u); o.y = L(1000, HOVER.y, u) - Math.sin(Math.PI * u) * 90; o.rot = L(-14, 0, u) + 2.5 * Math.sin((t - T.arrive) * 4.2);
      o.y += 10 * Math.sin((t - T.arrive) * 3.4) * u; o.s = 1; o.riding = t > T.arrive + 0.55; o.flame = 0.6 + 0.4 * (1 - u);
      o.scroll = 320 * sm((t - T.arrive - 0.45) / 0.45);          // hovering: the line keeps streaming left (flying in place)
      return o;
    }
    if (t < T.w1 - 0.18) {                                        // lift-off: accelerates out to the upper right, camera rushes along
      const u = (t - T.launch) / (T.w1 - 0.18 - T.launch), a = ei3(u);
      o.x = L(HOVER.x, 1500, a); o.y = L(HOVER.y, 380, a) + 14 * Math.sin(u * 9) * (1 - u); o.rot = L(0, -16, sm(u * 2)); o.s = L(1, 1.7, a);
      o.flame = 1 + 1.2 * sm(u * 3); o.riding = true; return o;
    }
    if (t < T.wEnd - 0.2) {                                       // the ten worlds: anchored, bobbing, the worlds scroll by
      const u = e3((t - (T.w1 - 0.18)) / 0.62);
      const bx = ANCHOR.x + 16 * Math.sin(t * 1.7), by = ANCHOR.y + 14 * Math.sin(t * 3.6);
      o.x = L(-280, bx, u); o.y = L(ANCHOR.y + 60, by, u); o.s = L(1.35, 1, u); o.rot = L(-10, 3 * Math.sin(t * 3.6 + 1), u);
      let b = 0; for (const w of WORLDS) b += bump(t, w.start + 0.05, 0.16);
      o.x += 36 * b; o.s *= 1 + 0.07 * b; o.rot -= 7 * b; o.flame = 1 + 0.9 * b;
      o.scroll = SCROLL * u; o.riding = true; return o;
    }
    if (t < T.hop + 0.45) {                                       // back in the navy world: flies in and settles beside the mascot
      if (t < T.wEnd + 0.02) { const u = ei3((t - (T.wEnd - 0.2)) / 0.22); o.x = L(ANCHOR.x, 1420, u); o.y = L(ANCHOR.y, 760, u); o.rot = L(0, -8, u); o.s = 1; o.riding = true; o.flame = 1.8; return o; }
      const u = e3((t - T.wEnd) / 0.75);
      o.x = L(-260, LAND.x, u); o.y = L(980, LAND.y, u) - Math.sin(Math.PI * u) * 70; o.rot = L(-12, 0, u) + 2 * Math.sin(t * 4); o.y += 9 * Math.sin(t * 3.4) * u;
      o.riding = t < T.hop + 0.1; o.flame = L(1.4, 0.6, u); o.scroll = 300 * sm((t - T.wEnd - 0.5) / 0.4); return o;
    }
    if (t < T.hop + 1.25) {                                       // the robot has hopped off: the rocket zooms away (upper right)
      const u = ei3((t - (T.hop + 0.45)) / 0.8);
      o.x = L(LAND.x, 1450, u); o.y = L(LAND.y + 9 * Math.sin((T.hop + 0.45) * 3.4), 420, u); o.rot = L(0, -18, sm(u * 2)); o.s = L(1, 0.8, u); o.flame = 1 + u; return o;
    }
    if (t >= T.loop0 - 0.55 && t < T.loop0) {                      // s16: swoops in from the lower left into the loop
      const u = e3((t - (T.loop0 - 0.55)) / 0.55);
      o.x = L(-240, 540 - 470, u); o.y = L(1180, 655, u) + Math.sin(Math.PI * u) * 40; o.rot = L(-35, -90, u); o.s = 0.72; o.flame = 1.4; return o;
    }
    if (t >= T.loop0 && t < T.loop1 + 0.6) {                      // s16: one big loop around the grid of the ten worlds, then off
      const u = io3((t - T.loop0) / (T.loop1 - T.loop0));
      const th = Math.PI + u * 2 * Math.PI * 1.0;
      const cx = 540, cy = 655, rx = 470, ry = 330;
      if (t < T.loop1) {
        o.x = cx + rx * Math.cos(th); o.y = cy + ry * Math.sin(th);
        const dx = -rx * Math.sin(th), dy = ry * Math.cos(th);
        o.rot = Math.atan2(dy, dx) * 180 / Math.PI; o.s = 0.72; o.flame = 1.2; return o;
      }
      const v = ei3((t - T.loop1) / 0.6);                        // loop closed at the left of the grid, heading up: exits up-left
      o.x = L(cx - rx, cx - rx - 120, v); o.y = L(cy, -260, v); o.rot = L(-90, -100, v); o.s = 0.72; o.flame = 1.6; return o;
    }
    o.vis = false; return o;
  }
  // rocket tail point (where the line attaches) for a state
  function tail(o) { const r = (o.rot * Math.PI) / 180, k = 150 * o.s; return { x: o.x - Math.cos(r) * k, y: o.y - Math.sin(r) * k }; }
  // the line: past tail positions, shifted left by the world scroll (so in the worlds it streams off to the left as a wave)
  function trail(t, N = 64, span = 1.3) {
    const pts = []; let shift = 0;
    for (let k = 0; k <= N; k++) {
      const tau = (k / N) * span, tt = t - tau;
      if (tt < T.arrive) break;
      const o = state(tt); if (!o.vis) break;
      if (k > 0) shift += state(t - ((k - 0.5) / N) * span).scroll * (span / N);
      const p = tail(o); pts.push({ x: p.x - shift, y: p.y, a: 1 - k / N });
      if (p.x - shift < -120) break;
    }
    return pts;
  }
  window.FLIGHT = { state, tail, trail, T, ANCHOR, HOVER, LAND, WIDS, worldAt };
})();
