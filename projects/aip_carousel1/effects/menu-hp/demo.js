// 15 · Menu HP: a phone-sized page; the three-line menu button morphs into an X, a full-height menu panel drops down (clip-path)
// and its links slide in one after another; then it all closes in reverse (loop). Two callouts light up with each step.
// Fictional: "Bersih Lagi" (cuci sepatu).
CAR.def("menu-hp", {
  build(K) {
    const { svg, I, ft, tap } = K;
    const L = ["Layanan", "Harga", "Cara kerja", "Lokasi", "Testimoni"];
    K.root.innerHTML =
      `<div class="cl c1" style="left:44px;top:120px"><small>LANGKAH 1</small><b>Tombol menu jadi X</b><span>Tiga garis berputar halus<br>membentuk tanda silang.</span><i class="hl"></i></div>` +
      `<div class="cl c2" style="left:652px;top:300px"><small>LANGKAH 2</small><b>Menu turun berurutan</b><span>Panel turun dari atas,<br>link masuk satu per satu.</span><i class="hl"></i></div>` +
      `<i class="ln" style="left:280px;top:153px;width:58px"></i><i class="ln" style="left:596px;top:333px;width:56px"></i>` +
      `<div class="ph"><div class="scr">` +
      `<div class="sbr">09.41<i></i></div><i class="nt"></i>` +
      `<i class="hero" style="background-image:url(${K.img("sepatu")})"></i>` +
      `<div class="h1">Sepatu kusam?<br><span>Kami bikin bersih lagi.</span></div>` +
      `<div class="p">Jemput-antar gratis se-Surabaya.<br>Selesai 2–3 hari.</div>` +
      `<div class="bt k-btn">${svg("truck", 2.2)}Jemput sepatuku</div>` +
      `<div class="sv"><span>Cuci reguler</span><span>Repaint</span><span>Anti-kuning</span></div>` +
      `<div class="rv"><b>4,9 dari 870 ulasan</b><span>"Sepatu putihku balik kayak baru."</span></div>` +
      `<div class="mn">` + L.map((s, i) => `<div class="li l${i}${i === 1 ? " on" : ""}" style="top:${24 + i * 56}px">${s}${svg("chevron-right", 2.4)}</div>`).join("") +
      `<div class="ca k-btn">${svg("message-circle", 2.2)}Chat admin</div><small>Buka setiap hari 08.00–20.00</small></div>` +
      `<div class="hd"><i class="lo">${svg("footprints", 2.2)}</i><b>Bersih Lagi</b><div class="hb"><u class="u0" style="top:10px"></u><u class="u1" style="top:17px"></u><u class="u2" style="top:24px"></u></div></div>` +
      `</div></div>`;
    const hb = K.q(".hb"), u = [K.q(".u0"), K.q(".u1"), K.q(".u2")], mn = K.q(".mn"), li = K.qa(".mn .li"), ca = K.q(".mn .ca"), sm = K.q(".mn small");
    const h1 = K.q(".c1 .hl"), h2 = K.q(".c2 .hl"), c1 = K.q(".c1"), c2 = K.q(".c2");
    I(u[0], { y: 0, rotation: 0 }); I(u[1], { opacity: 1, scaleX: 1 }); I(u[2], { y: 0, rotation: 0 });
    I(mn, { clipPath: "inset(0% 0% 100% 0%)" });
    li.forEach((l) => I(l, { x: -26, opacity: 0 }));
    I(ca, { y: 14, opacity: 0 }); I(sm, { opacity: 0 });
    [h1, h2].forEach((h) => I(h, { opacity: 0 })); [c1, c2].forEach((c) => I(c, { scale: 1 }));
    // open
    tap(hb, 0.55, { color: "rgba(0,105,92,.25)", s: 2.4 });
    ft(u[0], { y: 0, rotation: 0 }, { y: 7, rotation: 45, duration: 0.38, ease: "power3.inOut" }, 0.6);
    ft(u[2], { y: 0, rotation: 0 }, { y: -7, rotation: -45, duration: 0.38, ease: "power3.inOut" }, 0.6);
    ft(u[1], { opacity: 1, scaleX: 1 }, { opacity: 0, scaleX: 0.2, duration: 0.2 }, 0.6);
    ft(h1, { opacity: 0 }, { opacity: 1, duration: 0.25 }, 0.6); ft(c1, { scale: 1 }, { scale: 1.04, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 1 }, 0.6);
    ft(mn, { clipPath: "inset(0% 0% 100% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.55, ease: "power3.inOut" }, 0.68);
    li.forEach((l, i) => ft(l, { x: -26, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: "power3.out" }, 0.95 + i * 0.07));
    ft(ca, { y: 14, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "back.out(1.6)" }, 1.35);
    ft(sm, { opacity: 0 }, { opacity: 1, duration: 0.3 }, 1.45);
    ft(h1, { opacity: 1 }, { opacity: 0, duration: 0.3 }, 1.3);
    ft(h2, { opacity: 0 }, { opacity: 1, duration: 0.25 }, 0.95); ft(c2, { scale: 1 }, { scale: 1.04, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 1 }, 0.95);
    ft(h2, { opacity: 1 }, { opacity: 0, duration: 0.3 }, 1.9);
    // close (reverse)
    tap(hb, 3.3, { color: "rgba(0,105,92,.25)", s: 2.4 });
    [...li].reverse().forEach((l, i) => ft(l, { x: 0, opacity: 1 }, { x: -18, opacity: 0, duration: 0.22, ease: "power2.in" }, 3.35 + i * 0.04));
    ft(ca, { y: 0, opacity: 1 }, { y: 10, opacity: 0, duration: 0.2, ease: "power2.in" }, 3.35);
    ft(sm, { opacity: 1 }, { opacity: 0, duration: 0.2 }, 3.35);
    ft(mn, { clipPath: "inset(0% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 100% 0%)", duration: 0.45, ease: "power3.inOut" }, 3.55);
    ft(u[0], { y: 7, rotation: 45 }, { y: 0, rotation: 0, duration: 0.38, ease: "power3.inOut" }, 3.4);
    ft(u[2], { y: -7, rotation: -45 }, { y: 0, rotation: 0, duration: 0.38, ease: "power3.inOut" }, 3.4);
    ft(u[1], { opacity: 0, scaleX: 0.2 }, { opacity: 1, scaleX: 1, duration: 0.25 }, 3.55);
    // the page's main button breathes once while the menu is closed
    const bt = K.q(".bt");
    ft(bt, { scale: 1 }, { scale: 1.04, duration: 0.35, ease: "sine.inOut", yoyo: true, repeat: 1 }, 4.6);
  },
});
