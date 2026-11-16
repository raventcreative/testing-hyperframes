// Time-driven animation for the concept sites. window.seek(t) draws the frame at t seconds (deterministic, used for MP4 export).
(function () {
  let s = 7; const R = () => (s = (s * 16807) % 2147483647) / 2147483647;
  const E = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2), cl = (x) => Math.max(0, Math.min(1, x));
  const $ = (r, q) => r.querySelector(q), $$ = (r, q) => [...r.querySelectorAll(q)];
  const CV = [...document.querySelectorAll("canvas.pc")].map((c) => {
    const W = c.clientWidth * 2, H = c.clientHeight * 2; c.width = W; c.height = H;
    const pts = []; const n = c.dataset.k === "x" ? 4200 : 5200; for (let i = 0; i < n; i++) pts.push([R(), R(), R(), R(), R()]);
    return { g: c.getContext("2d"), W, H, pts, k: c.dataset.k };
  });
  function drawX(o, t) {
    const { g, W, H, pts } = o; g.clearRect(0, 0, W, H); const form = t < 1.4 ? E(t / 1.4) : 1, spin = t * 0.06;
    for (const p of pts) {
      const tt = p[0], arm = p[1] < 0.5 ? 1 : -1, sp = (p[2] - 0.5) * 0.17;
      let x = (tt - 0.5) * H * 0.95 + sp * H, y = arm * (tt - 0.5) * H * 0.95 + (p[3] - 0.5) * H * 0.17;
      const c = Math.cos(spin), sn = Math.sin(spin); [x, y] = [x * c - y * sn, x * sn + y * c];
      const rx = (p[3] - 0.5) * W * 1.2, ry = (p[4] - 0.5) * H * 1.2; x = rx + (x - rx) * form; y = ry + (y - ry) * form;
      const dr = Math.sin(t * 1.5 + p[4] * 20) * 4;
      g.fillStyle = `rgba(${(220 + p[2] * 35) | 0},${(195 + p[4] * 40) | 0},255,${0.25 + p[4] * 0.65})`;
      g.beginPath(); g.arc(W / 2 + x + dr, H / 2 + y - dr, p[2] * 2.4 + 0.4, 0, 7); g.fill();
    }
  }
  function drawHead(o, t) {
    const { g, W, H, pts } = o; g.clearRect(0, 0, W, H); const rot = t * 0.55;
    for (const p of pts) {
      const u0 = p[0] * Math.PI * 2, u = u0 + rot, v = Math.acos(2 * p[1] - 1);
      if (Math.cos(v) > 0.6 && Math.abs(Math.sin(v) * Math.cos(u0)) > 0.5) continue;
      const x = Math.sin(v) * Math.cos(u), y = Math.cos(v), z = Math.sin(v) * Math.sin(u);
      const sx = W * 0.62 + x * H * 0.26 * (1 - 0.25 * y), sy = H * 0.44 + y * H * 0.36, d = (z + 1) / 2, m = (x + 1) / 2;
      g.fillStyle = `rgba(${(80 + m * 170) | 0},${(120 - m * 60) | 0},255,${0.15 + d * 0.7})`;
      g.beginPath(); g.arc(sx, sy, p[2] * 2 + 0.4 + d, 0, 7); g.fill();
    }
  }
  window.seek = function (t) {
    const SC0 = 3.1, SC1 = 4.4, sp = E(cl((t - SC0) / (SC1 - SC0)));
    document.querySelectorAll(".br").forEach((br) => {
      const pg = $(br, ".pg"); if (!pg) return;
      pg.style.transform = `translateY(${-606 * sp}px)`;
      const k = t - 3.45;
      const rise = (el, i) => { const a = E(cl((k - i * 0.15) / 0.5)); el.style.opacity = a; el.style.transform = `translateY(${(1 - a) * 40}px)`; };
      $$(br, ".s2 h5").forEach((e) => rise(e, 0));
      $$(br, ".k,.mi,.pl>div,.nm>div,.dr>div,.tvb").forEach((e, i) => rise(e, i + 1));
      const w = $(br, ".w");
      if (w.classList.contains("w1")) { const a = E(cl((t - 0.6) / 0.8)); $$(w, ".l,.r").forEach((e) => (e.style.opacity = a)); }
      if (w.classList.contains("w2")) {
        const f = Math.sin(t * 1.6);
        $(w, ".cup").style.transform = `rotate(${-6 + f * 2}deg) translateY(${f * 8}px)`;
        $(w, ".bag").style.transform = `rotate(${7 - f * 2}deg) translateY(${-f * 10}px)`;
        $(w, ".hero h3").style.clipPath = `inset(0 ${100 - E(cl(t / 0.9)) * 100}% 0 0)`;
      }
      if (w.classList.contains("w3")) {
        $$(w, ".hero .tv").forEach((tv, i) => (tv.style.translate = `${Math.sin(t * 0.9 + i) * 14}px ${Math.cos(t * 1.1 + i * 1.7) * 12}px`));
        const a = E(cl(t / 0.8)); $(w, ".hero h3").style.opacity = a; $(w, ".hero h3").style.letterSpacing = `${(1 - a) * 14 + 1}px`;
      }
      if (w.classList.contains("w4")) {
        $$(w, ".dna path").forEach((p) => (p.style.strokeDashoffset = -t * 30));
        $$(w, ".hero .cards>div").forEach((c, i) => { const a = E(cl((t - 0.4 - i * 0.2) / 0.6)); c.style.opacity = a; c.style.transform = `translateY(${(1 - a) * 20}px)`; });
        $$(w, "[data-n]").forEach((b) => { const a = E(cl((t - 3.6) / 1.6)); b.textContent = Math.round(+b.dataset.n * a).toLocaleString("id-ID"); });
      }
      if (w.classList.contains("w5")) {
        const a = E(cl(t / 0.9)); $(w, ".hero h3").style.opacity = a; $(w, ".hero h3").style.transform = `translateX(${(1 - a) * -30}px)`;
        $(w, ".hero h4").style.opacity = E(cl((t - 0.5) / 0.9));
      }
    });
    CV.forEach((o) => (o.k === "x" ? drawX(o, t) : drawHead(o, t)));
  };
  window.seek(2.8);
})();
