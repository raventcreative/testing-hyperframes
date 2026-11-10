// MICROANIM — the reel's "animation bank": 12 UI micro-animations, all hand-coded SVG (icons: lucide-static, ISC; drawn as paths).
// Every card is a PURE function of time: handle.draw(t) sets the SVG state for time t (seconds, loops seamlessly), so scenes can
// seek any frame. Usage: const h = MicroAnim.mount(parentEl, "check", { size: 200, label: true, id: "s02-c0" }); h.draw(t);
// Styling targets the light reel background: white cards, navy ink (#0a0d2c → #294b77), blue accent, green / coral / gold semantics.
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const C = { ink: "#0a0d2c", ink2: "#294b77", blue: "#3a6fe0", sky: "#e9f0fc", line: "#dbe4f3", green: "#2da44e", coral: "#e5484d", gold: "#f4b400", mute: "#b9c6dc" };
  const one = (x) => Math.max(0, Math.min(1, x));
  const e3 = (u) => { u = one(u); return 1 - Math.pow(1 - u, 3); };
  const e5 = (u) => { u = one(u); return 1 - Math.pow(1 - u, 5); };
  const io = (u) => { u = one(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const back = (u, s = 1.9) => { u = one(u); const c3 = s + 1; return 1 + c3 * Math.pow(u - 1, 3) + s * Math.pow(u - 1, 2); };
  const win = (u, a, b) => one((u - a) / (b - a));
  const ph = (t, P, off = 0) => { const x = (t + off) / P; return x - Math.floor(x); };   // 0..1 loop phase
  const L = (a, b, u) => a + (b - a) * u;
  // fade the last part of each loop so the reset is invisible
  const life = (u, a = 0.9, b = 0.985) => 1 - 0.8 * win(u, a, b);   // short, partial fade: a card never reads as empty

  const TYPES = ["check", "loading", "counter", "bell", "chart", "toggle", "heart", "ring", "typing", "upload", "search", "stars"];
  const LABEL = { check: "Centang", loading: "Loading", counter: "Angka naik", bell: "Notifikasi", chart: "Grafik", toggle: "Toggle",
    heart: "Like", ring: "Progres", typing: "Mengetik", upload: "Upload", search: "Cari", stars: "Rating" };
  const PERIOD = { check: 2.0, loading: 1.25, counter: 2.6, bell: 2.0, chart: 2.6, toggle: 1.8, heart: 1.9, ring: 2.6, typing: 1.2, upload: 2.2, search: 1.8, stars: 2.2 };

  const el = (tag, attrs, parent) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; };
  const set = (e, k, v) => { const s = String(v); if (e.getAttribute(k) !== s) e.setAttribute(k, s); };
  const css = (e, k, v) => { if (e.style[k] !== v) e.style[k] = v; };

  // ---------------------------------------------------------------- builders (svg viewBox 0 0 160 160)
  const B = {
    check(g) {
      const ring = el("circle", { cx: 80, cy: 80, r: 46, fill: C.sky, stroke: C.line, "stroke-width": 8 }, g);
      const arc = el("circle", { cx: 80, cy: 80, r: 46, fill: "none", stroke: C.green, "stroke-width": 8, "stroke-linecap": "round", transform: "rotate(-90 80 80)", "stroke-dasharray": 289.03, "stroke-dashoffset": 289.03 }, g);
      const tick = el("path", { d: "M58 82 L74 97 L104 64", fill: "none", stroke: C.green, "stroke-width": 10, "stroke-linecap": "round", "stroke-linejoin": "round", "stroke-dasharray": 70, "stroke-dashoffset": 70 }, g);
      return (u) => {
        const a = e3(win(u, 0.04, 0.36)), k = e3(win(u, 0.3, 0.52)), f = win(u, 0.5, 0.62), pop = 1 + 0.1 * Math.sin(Math.PI * win(u, 0.5, 0.7));
        set(arc, "stroke-dashoffset", (289.03 * (1 - a)).toFixed(2)); set(tick, "stroke-dashoffset", (70 * (1 - k)).toFixed(2));
        set(ring, "fill", f > 0.5 ? C.green : C.sky); set(tick, "stroke", f > 0.5 ? "#ffffff" : C.green);
        set(g, "transform", `translate(80 80) scale(${pop.toFixed(4)}) translate(-80 -80)`); set(g, "opacity", life(u).toFixed(3));
      };
    },
    loading(g) {
      el("circle", { cx: 80, cy: 80, r: 44, fill: "none", stroke: C.sky, "stroke-width": 10 }, g);
      const arc = el("circle", { cx: 80, cy: 80, r: 44, fill: "none", stroke: C.blue, "stroke-width": 10, "stroke-linecap": "round", "stroke-dasharray": "40 276.5" }, g);
      const dots = [0, 1, 2].map((i) => el("circle", { cx: 62 + i * 18, cy: 132, r: 4.5, fill: C.ink2 }, g));
      return (u, t) => {
        const d = 30 + 170 * (0.5 - 0.5 * Math.cos(2 * Math.PI * u));
        set(arc, "stroke-dasharray", `${d.toFixed(1)} ${(276.5 - d + 1).toFixed(1)}`);
        set(arc, "transform", `rotate(${(-90 + 360 * u + 140 * (0.5 - 0.5 * Math.cos(2 * Math.PI * u))).toFixed(1)} 80 80)`);
        dots.forEach((c, i) => { const v = Math.max(0, Math.sin(2 * Math.PI * (u * 2 - i * 0.18))); set(c, "cy", (132 - 7 * v).toFixed(2)); set(c, "opacity", (0.35 + 0.65 * v).toFixed(3)); });
      };
    },
    counter(g) {
      const tx = el("text", { x: 80, y: 86, "text-anchor": "middle", "font-family": "Poppins, sans-serif", "font-weight": 700, "font-size": 44, fill: C.ink }, g);
      el("rect", { x: 28, y: 108, width: 104, height: 12, rx: 6, fill: C.sky }, g);
      const bar = el("rect", { x: 28, y: 108, width: 0, height: 12, rx: 6, fill: C.blue }, g);
      const up = el("path", { d: "M80 36 l10 12 h-6 v10 h-8 v-10 h-6 z", fill: C.green }, g);
      return (u) => {
        const v = e5(win(u, 0.05, 0.62)), n = Math.round(98 * v);
        if (tx.textContent !== n + "%") tx.textContent = n + "%";
        set(bar, "width", (104 * v).toFixed(2));
        const k = back(win(u, 0.6, 0.72)); set(up, "transform", `translate(80 47) scale(${k.toFixed(3)}) translate(-80 -47)`); set(up, "opacity", one(k).toFixed(3));
        set(g, "opacity", life(u).toFixed(3));
      };
    },
    bell(g) {
      const b = el("g", {}, g);
      const s = el("g", { transform: "translate(32 30) scale(4)", fill: "none", stroke: C.ink, "stroke-width": 2, "stroke-linecap": "round", "stroke-linejoin": "round" }, b);
      el("path", { d: "M10.268 21a2 2 0 0 0 3.464 0" }, s);
      el("path", { d: "M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326", fill: C.sky }, s);
      const badge = el("g", {}, g);
      el("circle", { cx: 112, cy: 46, r: 17, fill: C.coral, stroke: "#ffffff", "stroke-width": 4 }, badge);
      const n = el("text", { x: 112, y: 53, "text-anchor": "middle", "font-family": "Poppins, sans-serif", "font-weight": 700, "font-size": 20, fill: "#ffffff" }, badge);
      n.textContent = "3";
      return (u) => {
        const w = win(u, 0.02, 0.5), sw = 20 * Math.sin(w * Math.PI * 5) * (1 - w);
        set(b, "transform", `rotate(${sw.toFixed(2)} 80 34)`);
        const k = back(win(u, 0.12, 0.3), 2.4); set(badge, "transform", `translate(112 46) scale(${k.toFixed(3)}) translate(-112 -46)`);
        set(badge, "opacity", one(k * 3).toFixed(3)); set(g, "opacity", life(u).toFixed(3));
      };
    },
    chart(g) {
      el("line", { x1: 26, y1: 128, x2: 134, y2: 128, stroke: C.line, "stroke-width": 4, "stroke-linecap": "round" }, g);
      const H = [40, 64, 50, 86], cols = [C.mute, C.ink2, C.blue, C.green];
      const bars = H.map((h, i) => el("rect", { x: 32 + i * 26, y: 128, width: 18, height: 0, rx: 5, fill: cols[i] }, g));
      const line = el("polyline", { points: H.map((h, i) => `${41 + i * 26},${118 - h}`).join(" "), fill: "none", stroke: C.ink, "stroke-width": 4, "stroke-linecap": "round", "stroke-linejoin": "round", "stroke-dasharray": 140, "stroke-dashoffset": 140 }, g);
      return (u) => {
        bars.forEach((r, i) => { const v = back(win(u, 0.05 + i * 0.07, 0.3 + i * 0.07), 1.4) * H[i]; set(r, "y", (128 - v).toFixed(2)); set(r, "height", Math.max(0, v).toFixed(2)); });
        set(line, "stroke-dashoffset", (140 * (1 - e3(win(u, 0.45, 0.72)))).toFixed(2)); set(g, "opacity", life(u).toFixed(3));
      };
    },
    toggle(g) {
      const tr = el("rect", { x: 32, y: 56, width: 96, height: 48, rx: 24, fill: C.mute }, g);
      const kn = el("circle", { cx: 56, cy: 80, r: 18, fill: "#ffffff" }, g);
      el("circle", { cx: 56, cy: 80, r: 18, fill: "none" }, g);
      return (u) => {
        const on = back(win(u, 0.08, 0.3), 1.6) - back(win(u, 0.58, 0.8), 1.6);
        set(kn, "cx", L(56, 104, on).toFixed(2));
        const c = one(on); set(tr, "fill", c > 0.5 ? C.blue : C.mute);
        set(kn, "r", (18 + 3 * Math.sin(Math.PI * (win(u, 0.08, 0.3) + win(u, 0.58, 0.8)))).toFixed(2));
      };
    },
    heart(g) {
      const h = el("g", {}, g);
      const s = el("g", { transform: "translate(32 34) scale(4)" }, h);
      const p = el("path", { d: "M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5", fill: C.sky, stroke: C.coral, "stroke-width": 1.8, "stroke-linejoin": "round" }, s);
      const parts = Array.from({ length: 8 }, (_, i) => el("circle", { cx: 80, cy: 80, r: 5, fill: i % 2 ? C.coral : C.gold, opacity: 0 }, g));
      return (u) => {
        const k = back(win(u, 0.02, 0.22), 2.6); const sc = L(0.7, 1, one(k)) * (1 + 0.22 * Math.sin(Math.PI * win(u, 0.02, 0.22)));
        set(h, "transform", `translate(80 80) scale(${sc.toFixed(4)}) translate(-80 -80)`);
        set(p, "fill", u > 0.06 && u < 0.92 ? C.coral : C.sky);
        const b = win(u, 0.06, 0.42);
        parts.forEach((c, i) => { const a = (i / 8) * 2 * Math.PI, r = 30 + 40 * e3(b); set(c, "cx", (80 + r * Math.cos(a)).toFixed(2)); set(c, "cy", (80 + r * Math.sin(a)).toFixed(2));
          set(c, "r", (5 * (1 - b)).toFixed(2)); set(c, "opacity", (b > 0 && b < 1 ? 1 - b : 0).toFixed(3)); });
        set(g, "opacity", life(u, 0.9, 0.985).toFixed(3));
      };
    },
    ring(g) {
      el("circle", { cx: 80, cy: 80, r: 44, fill: "none", stroke: C.sky, "stroke-width": 12 }, g);
      const a = el("circle", { cx: 80, cy: 80, r: 44, fill: "none", stroke: C.ink2, "stroke-width": 12, "stroke-linecap": "round", transform: "rotate(-90 80 80)", "stroke-dasharray": 276.46, "stroke-dashoffset": 276.46 }, g);
      const tx = el("text", { x: 80, y: 90, "text-anchor": "middle", "font-family": "Poppins, sans-serif", "font-weight": 700, "font-size": 30, fill: C.ink }, g);
      return (u) => {
        const v = e5(win(u, 0.05, 0.6)) * 0.75;
        set(a, "stroke-dashoffset", (276.46 * (1 - v)).toFixed(2)); const n = Math.round(v * 100) + "%"; if (tx.textContent !== n) tx.textContent = n;
        set(a, "stroke", v >= 0.749 ? C.green : C.ink2); set(g, "opacity", life(u).toFixed(3));
      };
    },
    typing(g) {
      el("path", { d: "M34 52 h92 a16 16 0 0 1 16 16 v28 a16 16 0 0 1 -16 16 h-62 l-18 14 v-14 h-12 a16 16 0 0 1 -16 -16 v-28 a16 16 0 0 1 16 -16 z", fill: C.sky, stroke: C.line, "stroke-width": 3 }, g);
      const d = [0, 1, 2].map((i) => el("circle", { cx: 56 + i * 24, cy: 82, r: 8, fill: C.ink2 }, g));
      return (u) => { d.forEach((c, i) => { const v = Math.max(0, Math.sin(2 * Math.PI * (u - i * 0.15))); set(c, "cy", (82 - 10 * v).toFixed(2)); set(c, "opacity", (0.4 + 0.6 * v).toFixed(3)); }); };
    },
    upload(g) {
      const s = el("g", { transform: "translate(32 24) scale(4)", fill: "none", stroke: C.ink, "stroke-width": 2, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      el("path", { d: "M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242" }, s);
      const arw = el("g", {}, s);
      el("path", { d: "M12 13v8", stroke: C.blue }, arw); el("path", { d: "m8 17 4-4 4 4", stroke: C.blue }, arw);
      el("rect", { x: 32, y: 128, width: 96, height: 10, rx: 5, fill: C.sky }, g);
      const bar = el("rect", { x: 32, y: 128, width: 0, height: 10, rx: 5, fill: C.blue }, g);
      return (u) => {
        const lift = -3 * Math.sin(2 * Math.PI * ph(u * 2, 1)); set(arw, "transform", `translate(0 ${lift.toFixed(3)})`);
        const v = e3(win(u, 0.05, 0.75)); set(bar, "width", (96 * v).toFixed(2)); set(bar, "fill", v > 0.995 ? C.green : C.blue); set(g, "opacity", life(u).toFixed(3));
      };
    },
    search(g) {
      const rings = [0, 1].map(() => el("circle", { cx: 76, cy: 76, r: 26, fill: "none", stroke: C.blue, "stroke-width": 3, opacity: 0 }, g));
      const s = el("g", { transform: "translate(36 36) scale(3.4)", fill: "none", stroke: C.ink, "stroke-width": 2.6, "stroke-linecap": "round" }, g);
      el("circle", { cx: 11, cy: 11, r: 8, fill: "#ffffff" }, s); el("path", { d: "m21 21-4.34-4.34" }, s);
      return (u) => {
        rings.forEach((c, i) => { const v = ph(u, 1, -i * 0.5); set(c, "r", (26 + 30 * e3(v)).toFixed(2)); set(c, "opacity", (0.7 * (1 - v)).toFixed(3)); });
        set(s, "transform", `translate(${(36 + 4 * Math.sin(2 * Math.PI * u)).toFixed(2)} ${(36 + 3 * Math.cos(2 * Math.PI * u)).toFixed(2)}) scale(3.4)`);
      };
    },
    stars(g) {
      const P = "M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z";
      const st = [0, 1, 2, 3, 4].map((i) => { const w = el("g", {}, g); el("path", { d: P, fill: C.sky, stroke: C.mute, "stroke-width": 1.6, "stroke-linejoin": "round", transform: `translate(${10 + i * 29} 66) scale(1.15)` }, w); return w; });
      return (u) => {
        st.forEach((w, i) => { const k = win(u, 0.06 + i * 0.09, 0.18 + i * 0.09), p = w.firstChild;
          set(p, "fill", k > 0.3 ? C.gold : C.sky); set(p, "stroke", k > 0.3 ? "#d99a00" : C.mute);
          const s = 1 + 0.3 * Math.sin(Math.PI * k); const cx = 10 + i * 29 + 13.8, cy = 66 + 13.8; set(w, "transform", `translate(${cx} ${cy}) scale(${s.toFixed(3)}) translate(${-cx} ${-cy})`); });
        set(g, "opacity", life(u).toFixed(3));
      };
    },
  };

  // ---------------------------------------------------------------- the card
  const STYLE = `.ma-card{position:absolute;border-radius:28px;background:linear-gradient(180deg,#ffffff,#f6f8fd);box-shadow:0 18px 40px -22px rgba(10,13,44,.45),0 0 0 1.5px rgba(10,13,44,.06);overflow:hidden}
.ma-card svg{position:absolute;left:0;top:0;width:100%;height:100%}
.ma-card .ma-lb{position:absolute;left:0;right:0;bottom:7%;text-align:center;font:700 16px/1 Poppins,sans-serif;letter-spacing:-.01em;background:linear-gradient(172deg,#0a0d2c 8%,#294b77 92%);-webkit-background-clip:text;background-clip:text;color:transparent;white-space:nowrap}`;
  function ensureStyle() { if (!document.getElementById("ma-style")) { const s = document.createElement("style"); s.id = "ma-style"; s.textContent = STYLE; document.head.appendChild(s); } }

  function mount(parent, type, opts = {}) {
    ensureStyle();
    const size = opts.size || 200, card = document.createElement("div");
    card.className = "ma-card" + (opts.className ? " " + opts.className : ""); if (opts.id) card.id = opts.id;
    card.style.width = size + "px"; card.style.height = size + "px";
    const svg = el("svg", { viewBox: opts.label ? "0 -6 160 172" : "0 0 160 160", preserveAspectRatio: "xMidYMid meet" });
    const g = el("g", {}, svg);
    const draw = B[type](g);
    card.appendChild(svg);
    if (opts.label) { const lb = document.createElement("div"); lb.className = "ma-lb"; lb.textContent = opts.labelText || LABEL[type]; lb.style.fontSize = Math.round(size * 0.1) + "px"; card.appendChild(lb); }
    if (parent) parent.appendChild(card);
    const P = PERIOD[type], off = opts.phase || 0;
    return { el: card, type, draw: (t) => draw(ph(t, P, off), t) };
  }
  // the canonical BANK GRID in the hero zone (4 × 3 cards of 190 px): every scene starts and ends on it (seamless hand-over,
  // because the micro-animations are drawn from GLOBAL time). GRID[i] = { x, y } top-left of card i (type TYPES[i]).
  const GS = 190, GG = 22, GX = (1080 - (4 * GS + 3 * GG)) / 2, GY = 300;
  const GRID = TYPES.map((ty, i) => ({ type: ty, x: GX + (i % 4) * (GS + GG), y: GY + Math.floor(i / 4) * (GS + GG), size: GS }));
  // build the 12 cards at their GRID positions inside `parent` (absolute, 1080×1920 space); ids `${prefix}${i}`
  function grid(parent, prefix, opts = {}) {
    return GRID.map((g, i) => { const h = mount(parent, g.type, Object.assign({ size: GS, label: true, id: prefix + i }, opts)); h.el.style.left = g.x + "px"; h.el.style.top = g.y + "px"; h.home = g; return h; });
  }
  // the STRIP (12 mini chips under the logo during the 12 rounds): chip i top-left + size. A GRID card shrinks into its chip with
  // transform-origin 0 0: translate(chip.x - grid.x, chip.y - grid.y) scale(STRIP.size / GS).
  const SS = 66, SG = 10, SX = (1080 - (12 * SS + 11 * SG)) / 2, SY = 300;
  const STRIP = { size: SS, gap: SG, x0: SX, y: SY, scale: SS / GS, chip: (i) => ({ x: SX + i * (SS + SG), y: SY }) };
  window.MicroAnim = { mount, grid, GRID, GRID_SIZE: GS, STRIP, TYPES, LABEL, PERIOD, C };
})();
