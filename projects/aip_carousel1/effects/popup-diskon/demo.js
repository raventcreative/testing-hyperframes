// 11 · Popup diskon: the page dims and softly blurs, a first-order discount popup rises in, a WhatsApp number types in, the button
// turns into "Kode terkirim", the popup closes and a confirmation toast shows on the page (loop). Fictional: "Bunga Kirana".
CAR.def("popup-diskon", {
  build(K) {
    const { svg, I, ft, tap, typeText, pop, hide } = K;
    K.root.innerHTML =
      `<div class="pg"><div class="nav"><i class="lg">${svg("flower-2", 2.2)}</i><div class="bn">Bunga Kirana</div><div class="mn">Buket Papan-bunga Kontak</div><i class="ct">${svg("shopping-bag", 2)}</i></div>` +
      `<div class="tg">${svg("truck", 2.2)}FLORIST · DIANTAR HARI INI</div>` +
      `<div class="h1">Buket segar,<br><span>sampai hari ini juga.</span></div>` +
      `<div class="p">Pesan sebelum jam 14.00,<br>diantar ke seluruh Kota Malang.</div>` +
      `<div class="pr">mulai<b>Rp 175.000</b></div>` +
      `<div class="b1 k-btn">${svg("flower-2", 2.2)}Pesan buket</div><div class="b2 k-btn">Lihat katalog</div>` +
      `<div class="ph k-photo" style="background-image:url(${K.img("buket")})"></div></div>` +
      `<div class="ov"></div>` +
      `<div class="md"><i class="im" style="background-image:url(${K.img("buket")})"></i><i class="x">${svg("x", 2.4)}</i>` +
      `<small>KHUSUS PEMBELI BARU</small><h4>Diskon 15%</h4><h5>untuk pesanan pertamamu</h5>` +
      `<p>Tulis nomor WhatsApp-mu,<br>kode diskonnya langsung kami kirim.</p>` +
      `<div class="in">${svg("phone", 2.2)}<span class="phd">Nomor WhatsApp</span><span class="ty"></span></div>` +
      `<div class="go k-btn">Kirim kode diskon${svg("send", 2.2)}<span class="ok">${svg("circle-check", 2.4)}Kode terkirim ke WhatsApp</span></div>` +
      `<div class="no">Nggak dulu, makasih</div></div>` +
      `<div class="tst">${svg("circle-check", 2.2)}Kode <b>KIRANA15</b> sudah dikirim ke WhatsApp-mu</div>`;
    const pg = K.q(".pg"), ov = K.q(".ov"), md = K.q(".md"), phd = K.q(".phd"), go = K.q(".go"), ok = K.q(".go .ok"), tst = K.q(".tst");
    I(pg, { filter: "blur(0px)" });
    I(ov, { opacity: 0 });
    I(md, { opacity: 0, y: 46, scale: 0.94 });
    I(phd, { opacity: 1 });
    I(ok, { opacity: 0 });
    // popup in
    ft(ov, { opacity: 0 }, { opacity: 1, duration: 0.45, ease: "power1.out" }, 0.45);
    ft(pg, { filter: "blur(0px)" }, { filter: "blur(3px)", duration: 0.45, ease: "power1.out" }, 0.45);
    ft(md, { opacity: 0, y: 46, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }, 0.6);
    // number + send
    K.set(phd, { opacity: 0 }, 1.35);
    const clear = typeText(K.q(".ty"), "0812 3456 7890", 1.4, 2.2, true);
    tap(go, 2.55, { color: "rgba(255,255,255,.5)" });
    ft(ok, { opacity: 0 }, { opacity: 1, duration: 0.15 }, 2.68);
    // popup out, confirmation toast
    ft(md, { opacity: 1, y: 0, scale: 1 }, { opacity: 0, y: 24, scale: 0.96, duration: 0.35, ease: "power2.in" }, 3.85);
    ft(ov, { opacity: 1 }, { opacity: 0, duration: 0.4, ease: "power1.in" }, 4.0);
    ft(pg, { filter: "blur(3px)" }, { filter: "blur(0px)", duration: 0.4, ease: "power1.in" }, 4.0);
    pop(tst, 4.25, { y: -16, scale: 0.9 }, 0.45, "back.out(1.6)");
    hide(tst, 5.3, { y: -12 }, 0.3);
    clear(4.3); K.set(phd, { opacity: 1 }, 4.3); K.set(ok, { opacity: 0 }, 4.3);
  },
});
