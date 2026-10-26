// Mini diagrams (Harness / Loop / Graph) shared by the cover and CTA slides.
// Every frame is a pure function of t (seconds, 0..7).
window.Minis = (function () {
  const TAU = Math.PI * 2, D = 7;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const sm = (p) => { p = clamp(p, 0, 1); return p * p * (3 - 2 * p); };
  const mix = (a, b, k) => a.map((v, i) => Math.round(v + (b[i] - v) * k));
  const $ = (id) => document.getElementById(id);
  const cache = {};
  function at(id, p) {
    if (!cache[id]) { const el = $(id); cache[id] = { el, L: el.getTotalLength() }; }
    const r = cache[id];
    return r.el.getPointAtLength(clamp(p, 0, 1) * r.L);
  }
  function dot(id, pt, o) {
    const c = $(id);
    c.setAttribute("cx", pt.x.toFixed(1)); c.setAttribute("cy", pt.y.toFixed(1)); c.setAttribute("opacity", clamp(o, 0, 1).toFixed(3));
  }
  const WHITE = [255, 255, 255], ICE = [219, 231, 255], ICE2 = [188, 210, 250], AZ = [79, 134, 232];

  function harness(p, t) {
    const s = 1 + 0.05 * Math.sin(TAU * t / 3.5);
    $(p + "-br").setAttribute("transform", "translate(150 150) scale(" + s.toFixed(4) + ") translate(-150 -150)");
    let glow = 0;
    for (let i = 0; i < 4; i++) {
      const tt = (((t - i * 1.75) % D) + D) % D, q = tt / 0.9;
      const o = tt < 0.9 ? Math.min(1, q * 6) * (1 - sm((q - 0.85) / 0.15)) : 0;
      dot(p + "-d" + i, at(p + "-r" + i, sm(q)), o);
      if (tt > 0.8 && tt < 1.6) glow = Math.max(glow, 1 - (tt - 0.8) / 0.8);
    }
    $(p + "-llm").setAttribute("fill", "rgb(" + mix(ICE, ICE2, glow) + ")");
    $(p + "-llm").setAttribute("stroke", "rgb(" + mix([18, 21, 50], AZ, glow) + ")");
  }

  function loop(p, t) {
    const C = 2 * Math.PI * 95;
    const frac = (t % 3.5) / 3.5, a = -90 + 360 * frac;
    const arc = $(p + "-arc"), len = C * 100 / 360;
    arc.setAttribute("stroke-dasharray", len.toFixed(1) + " " + (C - len).toFixed(1));
    const s = ((frac - 100 / 360) % 1 + 1) % 1;
    arc.setAttribute("stroke-dashoffset", (-s * C).toFixed(1));
    const r = a * Math.PI / 180;
    dot(p + "-hd", { x: 150 + 95 * Math.cos(r), y: 150 + 95 * Math.sin(r) }, 1);
    [-90, 0, 90, 180].forEach((th, i) => {
      const d = ((a - th) % 360 + 360) % 360;
      const lit = d < 140 ? 1 - d / 140 : 0;
      $(p + "-n" + i).setAttribute("fill", "rgb(" + mix(WHITE, AZ, lit) + ")");
    });
  }

  const gfrac = {};
  function graphInit(p) {
    const nodes = [[95, 100], [205, 100], [60, 175], [150, 175], [240, 175], [150, 252]];
    ["ra", "rb"].forEach((r) => {
      const el = $(p + "-" + r), L = el.getTotalLength();
      gfrac[p + r] = nodes.map(([x, y]) => {
        let best = 1e9, bf = 2;
        for (let i = 0; i <= 200; i++) {
          const q = el.getPointAtLength(L * i / 200), dd = Math.hypot(q.x - x, q.y - y);
          if (dd < best) { best = dd; bf = i / 200; }
        }
        return best < 16 ? bf : 2;
      });
    });
  }
  function graph(p, t) {
    if (!gfrac[p + "ra"]) graphInit(p);
    const r = t < 3.5 ? "ra" : "rb", tt = t % 3.5;
    const q = sm((tt - 0.25) / 2.6);
    const fade = 1 - sm((tt - 3.05) / 0.35);
    dot(p + "-tk", at(p + "-" + r, q), Math.min(1, tt * 5) * fade);
    gfrac[p + r].forEach((f, i) => {
      const lit = q >= f - 0.01 ? fade : 0;
      const el = $(p + "-n" + i);
      if (i === 5) el.setAttribute("opacity", (0.82 + 0.18 * lit).toFixed(3));
      else el.setAttribute("fill", "rgb(" + mix(WHITE, ICE2, lit) + ")");
    });
    const rq = ((t % 3.5) / 3.5);
    dot(p + "-rt", at(p + "-retry", rq), Math.sin(Math.PI * rq) * 0.9);
  }

  return { harness, loop, graph };
})();
