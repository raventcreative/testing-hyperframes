// 01 · Harga coret: old price gets struck through, shrinks + greys out, promo price rises in, discount badge stamps on the photo,
// "Hemat" chip pops; then everything rewinds to the start state (loop). Fictional UMKM: "Dapur Kue Laras" (hampers kue kering).
CAR.def("harga-coret", {
  build(K) {
    const { svg, I, ft, pop, hide } = K;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("cake-slice", 2.2)}</i><div class="bn">Dapur Kue Laras</div><div class="mn">Produk Hampers Kontak</div><i class="ct">${svg("shopping-bag", 2)}</i></div>` +
      `<div class="ph k-photo" style="background-image:url(${K.img("hampers")})"></div>` +
      `<div class="bd"><small>HEMAT</small><b>30%</b><i></i></div>` +
      `<div class="tg">${svg("gift", 2.2)}HAMPERS LEBARAN</div>` +
      `<div class="nm">Hampers Kue Kering<br><span>isi 3 toples</span></div>` +
      `<div class="rt">${K.stars(5)}<span>4,9 · 1.240 terjual</span></div>` +
      `<div class="op">Rp 285.000<i class="st"></i></div>` +
      `<div class="np">Rp 199.000</div>` +
      `<div class="sv">${svg("badge-percent", 2.2)}Hemat Rp 86.000</div>` +
      `<div class="sk"><p>Stok promo: <b>sisa 12 paket</b></p><div class="bar"><i></i></div></div>` +
      `<div class="add k-btn">${svg("shopping-cart", 2.2)}Tambah ke keranjang</div>` +
      `<div class="lv">${svg("heart", 2.2)}</div>` +
      `<div class="inf">${svg("truck", 2)}Kirim se-Jabodetabek · gratis kartu ucapan</div>`;
    const op = K.q(".op"), st = K.q(".op .st"), np = K.q(".np"), bd = K.q(".bd"), sh = K.q(".bd i"), sv = K.q(".sv"), ph = K.q(".ph"), add = K.q(".add");
    // start state
    I(st, { scaleX: 0, transformOrigin: "0% 50%" });
    I(op, { scale: 1, y: 0, color: "#2a1a0e" });
    I(np, { opacity: 0, y: 46, filter: "blur(8px)" });
    I(bd, { opacity: 0, scale: 2.2, rotation: -32 });
    I(sh, { x: 0 });
    I(sv, { opacity: 0, scale: 0.6, x: -10 });
    // 1) strike-through draws
    ft(st, { scaleX: 0 }, { scaleX: 1, duration: 0.42, ease: "power2.inOut" }, 0.45);
    // 2) old price steps back
    ft(op, { scale: 1, y: 0, color: "#2a1a0e" }, { scale: 0.52, y: -18, color: "#a3acbd", duration: 0.55, ease: "power3.inOut" }, 0.95);
    // 3) promo price rises in
    ft(np, { opacity: 0, y: 46, filter: "blur(8px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.55, ease: "power3.out" }, 1.08);
    // 4) badge stamps on the photo (+ tiny jolt of the photo)
    ft(bd, { opacity: 0, scale: 2.2, rotation: -32 }, { opacity: 1, scale: 1, rotation: -10, duration: 0.42, ease: "back.out(1.5)" }, 1.5);
    [[5, -3], [-4, 2], [2, -1], [0, 0]].forEach(([x, y], k) => K.set(ph, { x, y }, 1.86 + k * 0.035));
    I(ph, { x: 0, y: 0 });
    // 5) savings chip
    ft(sv, { opacity: 0, scale: 0.6, x: -10 }, { opacity: 1, scale: 1, x: 0, duration: 0.38, ease: "back.out(2)" }, 1.95);
    // 6) shine across the badge, gentle nudge on the cart button
    ft(sh, { x: 0 }, { x: 200, duration: 0.7, ease: "power2.inOut" }, 2.5);
    ft(add, { scale: 1 }, { scale: 1.04, duration: 0.32, ease: "sine.inOut", yoyo: true, repeat: 3 }, 3.0);
    // 7) rewind to the start state (loop)
    ft(sv, { opacity: 1, scale: 1, x: 0 }, { opacity: 0, scale: 0.7, x: -6, duration: 0.25, ease: "power2.in" }, 4.7);
    ft(bd, { opacity: 1, scale: 1, rotation: -10 }, { opacity: 0, scale: 0.6, rotation: -10, duration: 0.3, ease: "power2.in" }, 4.78);
    ft(np, { opacity: 1, y: 0, filter: "blur(0px)" }, { opacity: 0, y: 30, filter: "blur(6px)", duration: 0.35, ease: "power2.in" }, 4.85);
    ft(op, { scale: 0.52, y: -18, color: "#a3acbd" }, { scale: 1, y: 0, color: "#2a1a0e", duration: 0.5, ease: "power3.inOut" }, 5.0);
    K.set(st, { transformOrigin: "100% 50%" }, 5.31);
    ft(st, { scaleX: 1 }, { scaleX: 0, duration: 0.32, ease: "power2.inOut" }, 5.32);
    K.set(st, { transformOrigin: "0% 50%" }, 5.7);
    void pop; void hide;
  },
});
