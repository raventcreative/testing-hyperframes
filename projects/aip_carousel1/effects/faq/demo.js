// 13 · FAQ buka-tutup: an accordion where one answer opens at a time: height grows smoothly, the answer slides in, the + turns into
// a coloured x and the card gets a highlight border; the next question opens as the previous closes (loop). Fictional: "Hijab Nara".
CAR.def("faq", {
  build(K) {
    const { svg, I, ft } = K;
    const QA = [
      ["Bisa bayar di tempat (COD)?", "Bisa. COD tersedia untuk Jabodetabek dan Bandung,<br>bayar ke kurir saat paket sampai."],
      ["Berapa lama pengirimannya?", "Pulau Jawa 2–3 hari kerja, luar Jawa 3–6 hari.<br>Nomor resi dikirim lewat WhatsApp."],
      ["Kalau ukurannya nggak pas?", "Tukar ukuran gratis maksimal 7 hari setelah paket<br>diterima, asal label masih terpasang."],
      ["Ada harga khusus reseller?", "Ada, mulai beli 12 pcs. Chat admin untuk daftar<br>harga reseller."],
    ];
    const H0 = 66, H1 = 140;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("sparkles", 2.2)}</i><div class="bn">Hijab Nara</div><div class="mn">Koleksi Ukuran Kontak</div></div>` +
      `<div class="tg">${svg("circle-help", 2.2)}PERTANYAAN UMUM</div>` +
      `<div class="h1">Masih ragu?<br><span>Cek dulu di sini.</span></div>` +
      `<div class="p">Jawaban dari pertanyaan yang paling<br>sering masuk ke admin kami.</div>` +
      `<div class="hc"><b>Belum ketemu jawabannya?</b><small>Admin siap bantu pilih ukuran.</small><div class="bt k-btn">${svg("message-circle", 2.2)}Tanya admin</div><em>Biasanya balas &lt; 10 menit</em></div>` +
      `<div class="ls">` + QA.map(([q, a], i) => `<div class="it i${i}"><i class="hl"></i><b>${q}</b><p>${a}</p>` +
        `<i class="ic"><i class="on"></i><span class="pl">${svg("plus", 2.6)}</span><span class="pl w">${svg("plus", 2.6)}</span></i></div>`).join("") + `</div>`;
    const items = QA.map((_, i) => ({ el: K.q(".i" + i), hl: K.q(`.i${i} .hl`), p: K.q(`.i${i} p`), on: K.q(`.i${i} .on`), w: K.q(`.i${i} .pl.w`), ic: K.q(`.i${i} .ic`) }));
    items.forEach((it) => {
      I(it.el, { height: H0 }); I(it.hl, { opacity: 0 }); I(it.p, { opacity: 0, y: -8 }); I(it.on, { scale: 0 }); I(it.w, { opacity: 0 }); I(it.ic, { rotation: 0 });
    });
    const open = (it, t) => {
      ft(it.el, { height: H0 }, { height: H1, duration: 0.5, ease: "power3.inOut" }, t);
      ft(it.hl, { opacity: 0 }, { opacity: 1, duration: 0.3 }, t);
      ft(it.p, { opacity: 0, y: -8 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }, t + 0.18);
      ft(it.ic, { rotation: 0 }, { rotation: 135, duration: 0.45, ease: "back.out(1.6)" }, t);
      ft(it.on, { scale: 0 }, { scale: 1, duration: 0.3, ease: "power2.out" }, t);
      ft(it.w, { opacity: 0 }, { opacity: 1, duration: 0.2 }, t + 0.05);
    };
    const close = (it, t) => {
      ft(it.p, { opacity: 1, y: 0 }, { opacity: 0, y: -6, duration: 0.2, ease: "power1.in" }, t);
      ft(it.el, { height: H1 }, { height: H0, duration: 0.45, ease: "power3.inOut" }, t);
      ft(it.hl, { opacity: 1 }, { opacity: 0, duration: 0.3 }, t + 0.1);
      ft(it.ic, { rotation: 135 }, { rotation: 0, duration: 0.4, ease: "power2.inOut" }, t);
      ft(it.on, { scale: 1 }, { scale: 0, duration: 0.25, ease: "power2.in" }, t);
      ft(it.w, { opacity: 1 }, { opacity: 0, duration: 0.2 }, t);
    };
    open(items[0], 0.35);
    close(items[0], 1.85); open(items[1], 1.85);
    close(items[1], 3.35); open(items[2], 3.35);
    close(items[2], 4.85);
  },
});
