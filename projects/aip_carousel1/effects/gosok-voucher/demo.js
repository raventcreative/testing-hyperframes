// 08 · Gosok voucher: a silver scratch layer over a voucher is "rubbed off" by a coin moving in a zig-zag (an SVG mask stroke that
// draws along the same path), the code appears, "Salin kode" is pressed -> "Kode disalin" chip; then the silver layer fades back
// on (loop). Fictional: "Martabak Bang Udin".
let GV_UID = 0;
CAR.def("gosok-voucher", {
  build(K) {
    const { svg, I, ft, tap, pop, hide } = K;
    const uid = "gv" + ++GV_UID;
    const W = 420, H = 262;
    const PTS = [[34, 44], [384, 60], [40, 104], [388, 120], [34, 166], [386, 178], [40, 224], [380, 236]];
    const d = "M" + PTS.map((p) => p.join(" ")).join("L");
    const seg = PTS.slice(1).map((p, i) => Math.hypot(p[0] - PTS[i][0], p[1] - PTS[i][1]));
    const LEN = seg.reduce((a, b) => a + b, 0);
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("flame", 2.2)}</i><div class="bn">Martabak Bang Udin</div><div class="mn">Menu Cabang Promo</div></div>` +
      `<div class="tg">${svg("ticket", 2.2)}PROMO CABANG BARU · MARGONDA</div>` +
      `<div class="h1">Gosok kartunya,<br><span>dapat diskonnya.</span></div>` +
      `<div class="p">Berlaku untuk pesanan online cabang Margonda.<br>Satu kode untuk satu pembeli.</div>` +
      [["1", "Gosok kartu di sebelah kanan"], ["2", "Salin kode diskonnya"], ["3", "Pakai saat checkout"]].map(([n, s], i) => `<div class="st" style="top:${318 + i * 50}px"><i>${n}</i>${s}</div>`).join("") +
      `<div class="sk">S&amp;K berlaku · promo sampai 31 Desember</div>` +
      `<div class="vc"><i class="in"></i><small>SELAMAT! KAMU DAPAT</small><div class="big">DISKON 20%</div><div class="code">UDIN20</div><div class="mini">min. belanja Rp 50.000</div></div>` +
      `<svg class="cot" viewBox="0 0 ${W} ${H}"><defs>` +
      `<linearGradient id="${uid}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9edf3"/><stop offset=".45" stop-color="#c3cad6"/><stop offset=".55" stop-color="#d9dee7"/><stop offset="1" stop-color="#aeb6c4"/></linearGradient>` +
      `<pattern id="${uid}p" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="14" height="14" fill="none"/><rect width="2" height="14" fill="rgba(255,255,255,.35)"/></pattern>` +
      `<mask id="${uid}m" maskUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}"><rect width="${W}" height="${H}" fill="#fff"/>` +
      `<path class="scr" d="${d}" fill="none" stroke="#000" stroke-width="62" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="${LEN.toFixed(1)}" stroke-dashoffset="${LEN.toFixed(1)}"/></mask></defs>` +
      `<g class="layer" mask="url(#${uid}m)"><rect width="${W}" height="${H}" rx="24" fill="url(#${uid}g)"/><rect width="${W}" height="${H}" rx="24" fill="url(#${uid}p)"/></g></svg>` +
      `<div class="hint"><i>${svg("hand", 2)}</i><b>GOSOK DI SINI</b><span>dapatkan diskon kejutan</span></div>` +
      `<div class="coin">Rp</div>` +
      `<div class="b1 k-btn">${svg("copy", 2.2)}Salin kode</div><div class="b2 k-btn">Pakai sekarang${svg("arrow-right", 2.4)}</div>` +
      `<div class="ok">${svg("circle-check", 2.2)}Kode UDIN20 disalin</div>`;
    const scr = K.q(".scr"), layer = K.q(".layer"), hint = K.q(".hint"), coin = K.q(".coin"), b1 = K.q(".b1"), ok = K.q(".ok");
    const T0 = 0.45, TS = 1.9;                       // scratching starts / lasts
    I(scr, { attr: { "stroke-dashoffset": LEN, "stroke-opacity": 0 } });   // hidden until it moves (a round cap would show as a dot)
    K.set(scr, { attr: { "stroke-opacity": 1 } }, T0);
    I(layer, { opacity: 1 });
    I(hint, { opacity: 1, scale: 1 });
    const cx = (p) => 470 + p[0] - 27, cy = (p) => 96 + p[1] - 27;
    I(coin, { x: cx(PTS[0]) - 60, y: cy(PTS[0]) + 30, opacity: 0, rotation: -20 });
    ft(hint, { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.9, duration: 0.3, ease: "power2.in" }, T0 - 0.05);
    ft(coin, { x: cx(PTS[0]) - 60, y: cy(PTS[0]) + 30, opacity: 0, rotation: -20 }, { x: cx(PTS[0]), y: cy(PTS[0]), opacity: 1, rotation: 0, duration: 0.3, ease: "power2.out" }, T0 - 0.3);
    ft(scr, { attr: { "stroke-dashoffset": LEN } }, { attr: { "stroke-dashoffset": 0 }, duration: TS, ease: "none" }, T0);
    let t = T0;
    seg.forEach((s, i) => {
      const dur = TS * (s / LEN), a = PTS[i], b = PTS[i + 1];
      ft(coin, { x: cx(a), y: cy(a) }, { x: cx(b), y: cy(b), duration: dur, ease: "none" }, t);
      ft(coin, { rotation: i % 2 ? 8 : -8 }, { rotation: i % 2 ? -8 : 8, duration: dur, ease: "sine.inOut" }, t);
      t += dur;
    });
    ft(coin, { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.6, duration: 0.25, ease: "power2.in" }, t);
    I(coin, { scale: 1 });
    ft(layer, { opacity: 1 }, { opacity: 0, duration: 0.35, ease: "power1.out" }, t + 0.05);
    // copy the code
    tap(b1, 3.0, { color: "rgba(255,255,255,.45)" });
    pop(ok, 3.15, { scale: 0.8, y: 8 });
    hide(ok, 4.55, { y: 6 }, 0.25);
    // silver layer comes back (mask reset while it is invisible)
    K.set(scr, { attr: { "stroke-dashoffset": LEN, "stroke-opacity": 0 } }, 4.9);
    ft(layer, { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.inOut" }, 5.0);
    ft(hint, { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.4, ease: "power2.out" }, 5.35);
    K.set(coin, { x: cx(PTS[0]) - 60, y: cy(PTS[0]) + 30, rotation: -20 }, 5.0);
  },
});
