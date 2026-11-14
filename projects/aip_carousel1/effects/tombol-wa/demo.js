// 02 · Tombol bernapas: a WhatsApp order button that "breathes" (slow scale + glow) every 1.5 s, with a soft ring spreading out of it,
// an online dot pulsing in sync, and a preview chat bubble + unread badge in the middle of the loop. Fictional: "Catering Mama Rina".
CAR.def("tombol-wa", {
  build(K) {
    const { svg, I, ft, pop, hide, D } = K;
    const av = [["#f08a4b", "RA"], ["#4f86e8", "DS"], ["#16934a", "YT"]].map(([c, t]) => `<i style="background:${c}">${t}</i>`).join("");
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("utensils", 2.2)}</i><div class="bn">Catering Mama Rina</div><div class="mn">Menu Paket Testimoni</div></div>` +
      `<div class="tg">${svg("calendar", 2.2)}KATERING HARIAN · JAKARTA SELATAN</div>` +
      `<div class="h1">Makan siang kantor,<br><span>rasa masakan rumah.</span></div>` +
      `<div class="p">Menu ganti tiap hari. Minimal 10 porsi,<br>diantar sebelum jam 11.30.</div>` +
      `<div class="on"><i><u></u></i><span><b>Admin online</b> · biasanya balas &lt; 5 menit</span></div>` +
      `<div class="rg"></div>` +
      `<div class="wa"><i class="ic">${svg("message-circle", 2.2)}</i><span>Pesan via WhatsApp</span></div>` +
      `<div class="nb">1</div>` +
      `<div class="lk">Lihat menu minggu ini ${svg("arrow-right", 2.4)}</div>` +
      `<div class="tr"><span class="av">${av}</span><span><b>120+ kantor</b> langganan tiap minggu</span></div>` +
      `<div class="ph k-photo" style="background-image:url(${K.img("nasi")})"></div>` +
      `<div class="rt">${svg("star", 1.5)}4,8 · 320 ulasan</div>` +
      `<div class="pc"><small>PAKET HARIAN</small><b>Rp 28.000 <span>/ porsi</span></b><em>Nasi + 3 lauk + buah potong</em></div>` +
      `<div class="bb"><small>PESAN BARU</small><p>Halo kak, mau pesan 20 porsi<br>buat Jumat ini ya.</p><em>11.02</em></div>`;
    const wa = K.q(".wa"), rg = K.q(".rg"), dot = K.q(".on i u"), bb = K.q(".bb"), nb = K.q(".nb");
    const P = 1.5;                                  // breath period: 4 per loop
    I(wa, { scale: 1, boxShadow: "0 18px 30px -14px rgba(20,162,77,.9), inset 0 2px 0 rgba(255,255,255,.28)" });
    I(rg, { boxShadow: "0 0 0 0px rgba(34,195,94,0)" });
    I(dot, { scale: 0.5, opacity: 0 });
    for (let k = 0; k < D / P; k++) {
      const t = k * P;
      ft(wa, { scale: 1, boxShadow: "0 18px 30px -14px rgba(20,162,77,.9), inset 0 2px 0 rgba(255,255,255,.28)" },
        { scale: 1.055, boxShadow: "0 26px 44px -12px rgba(20,162,77,1), inset 0 2px 0 rgba(255,255,255,.28)", duration: P / 2, ease: "sine.inOut", yoyo: true, repeat: 1 }, t);
      ft(rg, { boxShadow: "0 0 0 0px rgba(34,195,94,.55)" }, { boxShadow: "0 0 0 30px rgba(34,195,94,0)", duration: 1.2, ease: "power2.out" }, t + 0.25);
      ft(dot, { scale: 0.5, opacity: 0.9 }, { scale: 1.8, opacity: 0, duration: 1.1, ease: "power2.out" }, t + 0.25);
    }
    // a chat comes in: unread badge + preview bubble, then they clear before the loop ends
    pop(nb, 2.15, { scale: 0, y: 6 }, 0.35, "back.out(2.6)");
    pop(bb, 2.3, { scale: 0.6, y: 14 }, 0.45, "back.out(1.6)");
    hide(bb, 4.85, { scale: 0.85, y: 8 }, 0.3);
    hide(nb, 4.95, { scale: 0 }, 0.25);
  },
});
