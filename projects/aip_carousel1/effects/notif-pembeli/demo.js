// 03 · Notif pembeli: "X di Kota baru saja beli" toasts slide in at the bottom-left one after another (with a countdown bar),
// plus a live "lagi lihat" chip whose red dot pulses. Fictional: "Sambal Bu Ratmi" (sambal ijo teri).
CAR.def("notif-pembeli", {
  build(K) {
    const { svg, I, ft, D } = K;
    const toast = (cls, who, city, qty, ago) => `<div class="to ${cls}"><i class="th" style="background-image:url(${K.img("cabai")})"></i>` +
      `<p><b>${who}</b> di ${city} baru saja beli <b>${qty}</b></p><em>${svg("badge-check", 2.2)}${ago} · pembeli terverifikasi</em><i class="x">${svg("x", 2.2)}</i><i class="bar"></i></div>`;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("flame", 2.2)}</i><div class="bn">Sambal Bu Ratmi</div><div class="mn">Produk Resep Kontak</div><i class="ct">${svg("shopping-bag", 2)}</i></div>` +
      `<div class="tg">${svg("flame", 2.2)}BEST SELLER · DIBUAT TIAP PAGI</div>` +
      `<div class="h1">Sambal Ijo Teri,<br><span>pedasnya bikin nagih.</span></div>` +
      `<div class="p">Cabai hijau segar + teri Medan, tanpa pengawet.<br>Tahan 2 minggu di kulkas.</div>` +
      `<div class="pr">Rp 45.000 <span>/ botol 200 gr</span></div>` +
      `<div class="b1 k-btn">${svg("shopping-cart", 2.2)}Beli sekarang</div><div class="b2 k-btn">Lihat resep</div>` +
      `<div class="ph k-photo" style="background-image:url(${K.img("cabai")})"></div>` +
      `<div class="vw"><i><u></u></i><b>18 orang</b> lagi lihat produk ini</div>` +
      `<div class="bs">${svg("star", 2)}Terlaris minggu ini</div>` +
      toast("t1", "Rina", "Bandung", "2 botol", "3 menit lalu") + toast("t2", "Dimas", "Surabaya", "1 botol", "8 menit lalu");
    const dot = K.q(".vw i u");
    I(dot, { scale: 0.5, opacity: 0 });
    for (let k = 0; k < 4; k++) ft(dot, { scale: 0.5, opacity: 0.9 }, { scale: 2, opacity: 0, duration: 1.2, ease: "power2.out" }, k * 1.5);
    // two toasts: slide in from the left with a little overshoot, countdown bar empties, slide down + fade out
    [[".t1", 0.35], [".t2", 3.15]].forEach(([sel, t]) => {
      const el = K.q(sel), bar = K.q(sel + " .bar");
      I(el, { x: -440, opacity: 0, y: 0 });
      I(bar, { scaleX: 1 });
      ft(el, { x: -440, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(1.3)" }, t);
      ft(bar, { scaleX: 1 }, { scaleX: 0, duration: 1.75, ease: "none" }, t + 0.45);
      ft(el, { y: 0, opacity: 1 }, { y: 40, opacity: 0, duration: 0.35, ease: "power2.in" }, t + 2.2);
      K.set(el, { x: -440, y: 0 }, t + 2.6);
      K.set(bar, { scaleX: 1 }, t + 2.6);
    });
    void D;
  },
});
