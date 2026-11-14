// 12 · Tombol nempel: the page scrolls down past the hero's order button; a sticky order bar slides up and stays at the bottom while
// the visitor reads; its button gets pressed; scrolling back to the top hides the bar again (loop). Fictional: "Servis AC Sejuk".
CAR.def("sticky-cta", {
  build(K) {
    const { svg, I, ft, tap } = K;
    const feats = [["shield-check", "Garansi 30 hari", "AC bermasalah lagi?<br>Kami datang gratis."], ["clock", "Datang &lt; 3 jam", "Teknisi terdekat langsung<br>meluncur ke rumahmu."], ["wallet", "Harga jelas di awal", "Biaya dicek dan disepakati<br>sebelum dikerjakan."]];
    const prices = [["Cuci AC 0,5–1 PK", "Rp 75.000"], ["Isi freon R32", "mulai Rp 150.000"], ["Bongkar pasang AC", "Rp 250.000"], ["Cek kerusakan", "gratis"]];
    K.root.innerHTML =
      `<div class="pg">` +
      `<div class="tg">${svg("wind", 2.2)}SERVIS AC PANGGILAN · BEKASI</div>` +
      `<div class="h1">AC kurang dingin?<br><span>Teknisi datang hari ini.</span></div>` +
      `<div class="p">Cuci, isi freon, sampai bongkar pasang.<br>Harga jelas sebelum dikerjakan.</div>` +
      `<div class="hb k-btn">${svg("calendar", 2.2)}Pesan teknisi</div>` +
      `<div class="rt">${K.stars(5)}<span><b>4,9</b> · 1.800+ servis selesai</span></div>` +
      `<div class="bk"><h6>Jadwal teknisi hari ini</h6><small>Pilih jam, teknisi konfirmasi lewat WA</small>` +
      [["09.00", "PENUH", "full"], ["13.00", "TERSEDIA", "ok"], ["16.00", "TERSEDIA", "ok"]].map(([j, s, c], i) => `<div class="sl" style="top:${80 + i * 70}px"><b>${j}</b><span class="${c}">${s}</span></div>`).join("") +
      `<div class="ar">${svg("map-pin", 2.2)}Area: Bekasi, Cikarang, Tambun</div></div>` +
      `<div class="s2">Kenapa pilih Servis AC Sejuk?</div>` +
      feats.map(([ic, b, p], i) => `<div class="ftc" style="left:${40 + i * 290}px"><i>${svg(ic, 2.2)}</i><b>${b}</b><p>${p}</p></div>`).join("") +
      `<div class="s3">Daftar harga</div>` +
      prices.map(([b, s], i) => `<div class="pl" style="top:${884 + i * 76}px"><b>${b}</b><span>${s}</span></div>`).join("") +
      `</div>` +
      `<div class="nav"><i class="lg">${svg("wind", 2.2)}</i><div class="bn">Servis AC Sejuk</div><div class="mn">Layanan Harga Area</div></div>` +
      `<i class="sbar"></i>` +
      `<div class="sb"><i>${svg("wind", 2.2)}</i><b>Cuci AC mulai Rp 75.000</b><small>Teknisi bisa datang hari ini</small><div class="go k-btn">Pesan teknisi${svg("arrow-right", 2.4)}</div></div>`;
    const pg = K.q(".pg"), sb = K.q(".sb"), go = K.q(".sb .go"), bar = K.q(".sbar");
    const S = 700;                                    // scroll distance
    I(pg, { y: 0 }); I(bar, { y: 0 }); I(sb, { y: 110, opacity: 0 });
    // scroll down, read, scroll back up
    ft(pg, { y: 0 }, { y: -S, duration: 1.8, ease: "power2.inOut" }, 0.7);
    ft(bar, { y: 0 }, { y: 380, duration: 1.8, ease: "power2.inOut" }, 0.7);
    ft(pg, { y: -S }, { y: 0, duration: 1.6, ease: "power2.inOut" }, 3.7);
    ft(bar, { y: 380 }, { y: 0, duration: 1.6, ease: "power2.inOut" }, 3.7);
    // the bar appears once the hero button has scrolled out of view, hides when it comes back
    ft(sb, { y: 110, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.3)" }, 1.55);
    tap(go, 3.0, { color: "rgba(255,255,255,.5)" });
    ft(sb, { y: 0, opacity: 1 }, { y: 110, opacity: 0, duration: 0.35, ease: "power2.in" }, 4.5);
  },
});
