// 09 · Paket unggulan: three price plans; the recommended plan lifts forward with a rotating gradient frame (one full turn per
// loop = seamless) and a glow, its feature checks turn green one by one, the ribbon shines, the CTA nudges; then it settles back.
// Fictional: "Studio Kilau" (foto produk UMKM).
CAR.def("paket-harga", {
  build(K) {
    const { svg, I, ft, D } = K;
    const PL = [
      ["Hemat", "Buat mulai jualan", "Rp 350rb", ["10 foto produk", "Latar putih polos", "Edit warna dasar", "Selesai 3 hari"], "Pilih Hemat"],
      ["Laris", "Paling sering dipilih UMKM", "Rp 650rb", ["25 foto produk", "Latar putih + 5 foto gaya", "Edit warna detail", "Selesai 2 hari"], "Pilih paket Laris"],
      ["Lengkap", "Buat katalog lengkap", "Rp 1,2 jt", ["50 foto produk", "Foto gaya + model tangan", "Video pendek 15 detik", "Selesai 4 hari"], "Pilih Lengkap"],
    ];
    const card = ([n, d, pr, f, b], i) => `<div class="cd c${i}${i === 1 ? " mid" : ""}" style="${i === 1 ? "" : `left:${46 + i * 286}px`}"><b class="n">${n}</b><span class="d">${d}</span>` +
      `<div class="pr">${pr} <span>/ sesi</span></div><ul>${f.map((s) => `<li><i>${i === 1 ? "<u></u>" : ""}${svg("check", 3)}</i>${s}</li>`).join("")}</ul><div class="bt k-btn">${b}</div></div>`;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("camera", 2.2)}</i><div class="bn">Studio Kilau</div><div class="mn">Portofolio Paket Kontak</div><div class="nb">Konsultasi gratis</div></div>` +
      `<div class="hd"><small>PAKET FOTO PRODUK</small><h3>Foto produk siap jualan</h3></div>` +
      card(PL[0], 0) + card(PL[2], 2) +
      `<div class="glow"></div><div class="ring"><i></i></div>` + card(PL[1], 1) +
      `<div class="rb">PALING LARIS<u></u></div>`;
    const ring = K.q(".ring i"), mid = K.q(".cd.mid"), ringBox = K.q(".ring"), glow = K.q(".glow"), rb = K.q(".rb"), shine = K.q(".rb u");
    const sides = [K.q(".c0"), K.q(".c2")], ticks = K.qa(".cd.mid li i u"), cta = K.q(".cd.mid .bt");
    // the frame turns once per loop
    I(ring, { rotation: 0 });
    ft(ring, { rotation: 0 }, { rotation: 360, duration: D, ease: "none" }, 0);
    // lift forward / settle back (same tweens on the card, its frame, glow and ribbon)
    const group = [mid, ringBox, rb];
    group.forEach((e) => I(e, { y: 0, scale: 1 }));
    I(glow, { opacity: 0.35, scale: 0.9 });
    sides.forEach((s) => I(s, { opacity: 1, scale: 1 }));
    group.forEach((e) => ft(e, { y: 0, scale: 1 }, { y: -12, scale: 1.04, duration: 0.6, ease: "power3.out" }, 0.3));
    ft(glow, { opacity: 0.35, scale: 0.9 }, { opacity: 1, scale: 1.08, duration: 0.6, ease: "power2.out" }, 0.3);
    sides.forEach((s) => ft(s, { opacity: 1, scale: 1 }, { opacity: 0.62, scale: 0.97, duration: 0.6, ease: "power2.out" }, 0.3));
    ticks.forEach((tk, i) => { I(tk, { scale: 0 }); ft(tk, { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.6)" }, 0.75 + i * 0.22); });
    I(shine, { x: 0 });
    ft(shine, { x: 0 }, { x: 220, duration: 0.7, ease: "power2.inOut" }, 1.9);
    ft(cta, { scale: 1 }, { scale: 1.05, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: 3 }, 2.6);
    // settle back
    group.forEach((e) => ft(e, { y: -12, scale: 1.04 }, { y: 0, scale: 1, duration: 0.55, ease: "power3.inOut" }, 5.1));
    ft(glow, { opacity: 1, scale: 1.08 }, { opacity: 0.35, scale: 0.9, duration: 0.55, ease: "power2.inOut" }, 5.1);
    sides.forEach((s) => ft(s, { opacity: 0.62, scale: 0.97 }, { opacity: 1, scale: 1, duration: 0.55, ease: "power2.inOut" }, 5.1));
    ticks.forEach((tk, i) => ft(tk, { scale: 1 }, { scale: 0, duration: 0.2, ease: "power2.in" }, 4.85 + i * 0.04));
  },
});
