// 14 · Peta kirim: on an Indonesia outline (Natural Earth, public domain) parcel routes draw out of Yogyakarta one by one; a parcel
// badge rides the head of each curve, the destination pin pops with its ETA label; then the routes fade for the loop.
// Fictional: "Batik Sekar Jogja". City ETAs are illustrative.
CAR.def("peta-kirim", {
  build(K) {
    const { svg, I, ft, pop, hide, D } = K;
    const M = window.MAP_IDN, MX = 36, MY = 196;
    const P = (lon, lat) => [(lon - M.lonMin) * M.k, (M.latMax - lat) * M.k];
    const O = P(110.37, -7.8);
    const C = [
      ["Medan", "3–4 hari", P(98.67, 3.59), [-26, -44], 0.3],
      ["Jakarta", "1–2 hari", P(106.85, -6.21), [-120, -46], 0.55],
      ["Balikpapan", "3–5 hari", P(116.83, -1.27), [-50, -46], 0.8],
      ["Makassar", "3–4 hari", P(119.43, -5.15), [14, -14], 1.05],
      ["Denpasar", "2–3 hari", P(115.22, -8.65), [-6, 14], 1.3],
      ["Jayapura", "5–8 hari", P(140.72, -2.53), [-128, 16], 1.55],
    ];
    const curve = (a, b) => {
      const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy);
      let nx = -dy / L, ny = dx / L; if (ny > 0) { nx = -nx; ny = -ny; }           // bulge upwards
      const k = Math.min(0.32 * L, 150), c = [mx + nx * k, my + ny * k];
      const pts = []; for (let i = 0; i <= 24; i++) { const t = i / 24, u = 1 - t; pts.push([u * u * a[0] + 2 * u * t * c[0] + t * t * b[0], u * u * a[1] + 2 * u * t * c[1] + t * t * b[1]]); }
      let len = 0; for (let i = 1; i < pts.length; i++) len += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
      return { d: `M${a[0].toFixed(1)} ${a[1].toFixed(1)}Q${c[0].toFixed(1)} ${c[1].toFixed(1)} ${b[0].toFixed(1)} ${b[1].toFixed(1)}`, pts, len };
    };
    const R = C.map((c) => curve(O, c[2]));
    K.root.innerHTML =
      `<svg class="map" viewBox="0 0 ${M.w} ${M.h}"><path d="${M.nb}" fill="#eef1f8"/><path d="${M.d}" fill="#dfe5f5" stroke="#ffffff" stroke-width="1.2" stroke-linejoin="round"/>` +
      R.map((r, i) => `<path class="rt r${i}" d="${r.d}" fill="none" stroke="#3949ab" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="${r.len.toFixed(1)}" stroke-dashoffset="${r.len.toFixed(1)}"/>`).join("") +
      C.map((c, i) => `<circle class="dp d${i}" cx="${c[2][0].toFixed(1)}" cy="${c[2][1].toFixed(1)}" r="6" fill="#3949ab" stroke="#fff" stroke-width="2.5"/>` +
        `<circle class="dr d${i}r" cx="${c[2][0].toFixed(1)}" cy="${c[2][1].toFixed(1)}" r="6" fill="none" stroke="#3949ab" stroke-width="2"/>`).join("") +
      `<circle class="orr" cx="${O[0].toFixed(1)}" cy="${O[1].toFixed(1)}" r="9" fill="none" stroke="#141a3d" stroke-width="2"/>` +
      `<circle cx="${O[0].toFixed(1)}" cy="${O[1].toFixed(1)}" r="9" fill="#141a3d" stroke="#fff" stroke-width="3"/></svg>` +
      `<div class="nav"><i class="lg">${svg("shirt", 2.2)}</i><div class="bn">Batik Sekar Jogja</div><div class="mn">Koleksi Ukuran Kontak</div></div>` +
      `<div class="tg">${svg("truck", 2.2)}PENGIRIMAN</div>` +
      `<div class="h1">Dikirim dari Jogja,<br><span>sampai ke rumahmu.</span></div>` +
      `<div class="ch" style="left:520px;top:100px">${svg("clock", 2.2)}Kirim tiap hari <b>jam 16.00</b></div>` +
      `<div class="ch" style="left:520px;top:148px">${svg("message-circle", 2.2)}Resi dikirim <b>lewat WhatsApp</b></div>` +
      `<div class="og" style="left:${MX + O[0] - 70}px;top:${MY + O[1] + 18}px">${svg("package", 2.2)}Gudang Jogja</div>` +
      C.map((c, i) => `<div class="lb l${i}" style="left:${MX + c[2][0] + c[3][0]}px;top:${MY + c[2][1] + c[3][1]}px">${c[0]} <span>· ${c[1]}</span></div>`).join("") +
      C.map((c, i) => `<i class="pc p${i}">${svg("package", 2.4)}</i>`).join("") +
      `<div class="lgd"><span><i style="background:#141a3d"></i>Gudang</span><span><i style="background:#3949ab"></i>Kota tujuan</span><span>Estimasi kurir reguler, contoh</span></div>`;
    // origin pulse (4 per loop)
    const orr = K.q(".orr");
    I(orr, { attr: { r: 9 }, opacity: 0 });
    for (let k = 0; k < 4; k++) ft(orr, { attr: { r: 9 }, opacity: 0.8 }, { attr: { r: 26 }, opacity: 0, duration: 1.2, ease: "power2.out" }, k * 1.5);
    C.forEach((c, i) => {
      const r = R[i], rt = K.q(".r" + i), pc = K.q(".p" + i), dp = K.q(".d" + i), dr = K.q(`.d${i}r`), lb = K.q(".l" + i);
      const t0 = c[4], dur = 0.75 + Math.min(0.5, r.len / 900);
      I(rt, { attr: { "stroke-dashoffset": r.len }, opacity: 1 });
      I(dp, { attr: { r: 0 } }); I(dr, { attr: { r: 6 }, opacity: 0 });
      ft(rt, { attr: { "stroke-dashoffset": r.len } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: "power1.inOut" }, t0);
      // parcel rides the head of the curve (same easing as the stroke)
      const kf = r.pts.map((p) => ({ x: MX + p[0] - 13, y: MY + p[1] - 13 }));
      I(pc, { x: kf[0].x, y: kf[0].y, opacity: 0, scale: 0.6 });
      ft(pc, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.15 }, t0);
      const prox = { p: 0 };
      void prox;
      const segs = kf.length - 1;
      // piecewise-linear keyframes, timed through the stroke's power1.inOut so badge and stroke head stay together
      const ease = gsap.parseEase("power1.inOut");
      const inv = (y) => { let lo = 0, hi = 1; for (let j = 0; j < 30; j++) { const m = (lo + hi) / 2; if (ease(m) < y) lo = m; else hi = m; } return (lo + hi) / 2; };
      let cum = [0]; for (let j = 1; j <= segs; j++) cum.push(cum[j - 1] + Math.hypot(r.pts[j][0] - r.pts[j - 1][0], r.pts[j][1] - r.pts[j - 1][1]));
      for (let j = 1; j <= segs; j++) {
        const ta = t0 + dur * inv(cum[j - 1] / r.len), tb = t0 + dur * inv(cum[j] / r.len);
        ft(pc, { x: kf[j - 1].x, y: kf[j - 1].y }, { x: kf[j].x, y: kf[j].y, duration: Math.max(0.001, tb - ta), ease: "none" }, ta);
      }
      const ta = t0 + dur;
      ft(pc, { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.4, duration: 0.2, ease: "power2.in" }, ta);
      ft(dp, { attr: { r: 0 } }, { attr: { r: 6 }, duration: 0.35, ease: "back.out(3)" }, ta);
      ft(dr, { attr: { r: 6 }, opacity: 0.9 }, { attr: { r: 20 }, opacity: 0, duration: 0.8, ease: "power2.out" }, ta);
      pop(lb, ta + 0.05, { scale: 0.7, y: 8 }, 0.35, "back.out(2)");
      // loop: everything fades out and resets
      ft(rt, { opacity: 1 }, { opacity: 0, duration: 0.4, ease: "power1.in" }, 4.75 + i * 0.05);
      hide(lb, 4.7 + i * 0.05, { scale: 0.8, y: 6 }, 0.25);
      ft(dp, { attr: { r: 6 } }, { attr: { r: 0 }, duration: 0.25, ease: "power2.in" }, 4.9 + i * 0.05);
      K.set(rt, { attr: { "stroke-dashoffset": r.len } }, 5.5);
      K.set(rt, { opacity: 1 }, 5.55);
      K.set(pc, { x: kf[0].x, y: kf[0].y, scale: 0.6 }, 5.5);
    });
    void D;
  },
});
