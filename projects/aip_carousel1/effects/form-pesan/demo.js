// 10 · Form bertahap: a 3-step custom-cake order form (size -> writing -> pick-up), with a progress bar that fills between steps,
// panels sliding left, the order summary filling in live, then "Pesanan terkirim" and a reset (loop). Fictional: "Kue Nisa".
CAR.def("form-pesan", {
  build(K) {
    const { svg, I, ft, set, tap, typeText } = K;
    const SX = [44, 274, 504];                                    // step circle centres (x in the form)
    const opt = (i, b, s, p) => `<div class="op o${i}" style="left:${i * 171}px"><b>${b}</b><span>${s}</span><em>${p}</em><i class="sel"></i><i class="ck">${svg("check", 3)}</i></div>`;
    const date = (i, d, n) => `<div class="dt d${i}" style="left:${i * 128}px"><small>${d}</small><b>${n}</b><i class="sel"></i></div>`;
    const tm = (i, t) => `<div class="tm m${i}" style="left:${i * 128}px">${t}<i class="sel"></i></div>`;
    const row = (cls, lab, y, v) => `<div class="rw" style="top:${y}px"><small>${lab}</small><span class="e ${cls}0">belum diisi</span><span class="${cls}1">${v}</span></div>`;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("cake-slice", 2.2)}</i><div class="bn">Kue Nisa</div><div class="mn">Katalog Cara-pesan Kontak</div></div>` +
      `<div class="fm"><div class="fh">Pesan kue ulang tahun</div><div class="fs">3 langkah, kurang dari 1 menit</div>` +
      `<i class="trk" style="left:${SX[0]}px;width:${SX[2] - SX[0]}px"></i>` +
      `<i class="fil f1" style="left:${SX[0]}px;width:${SX[1] - SX[0]}px"></i><i class="fil f2" style="left:${SX[1]}px;width:${SX[2] - SX[1]}px"></i>` +
      ["Ukuran", "Tulisan", "Ambil"].map((l, i) => `<div class="sc s${i}" style="left:${SX[i] - 17}px">${i + 1}<i class="on">${i + 1}</i></div><div class="sl" style="left:${SX[i] - 17}px">${l.toUpperCase()}</div>`).join("") +
      `<div class="vp"><div class="strip">` +
      `<div class="pn" style="left:0"><h6>Pilih ukuran kue</h6>${opt(0, "Ø 16 cm", "8 orang", "Rp 240.000")}${opt(1, "Ø 20 cm", "12 orang", "Rp 320.000")}${opt(2, "Ø 24 cm", "20 orang", "Rp 450.000")}</div>` +
      `<div class="pn" style="left:496px"><h6>Tulisan di atas kue</h6><div class="in"><span class="ty"></span></div><span class="cn">maks. 40 huruf</span>` +
      `<span class="tp" style="left:0">Krim putih</span><span class="tp on" style="left:124px">Krim pink</span><span class="tp" style="left:244px">Cokelat</span></div>` +
      `<div class="pn" style="left:992px"><h6>Tanggal ambil</h6>${date(0, "JUM", "12")}${date(1, "SAB", "13")}${date(2, "MIN", "14")}${tm(0, "10.00")}${tm(1, "13.00")}${tm(2, "16.00")}</div>` +
      `</div></div>` +
      `<div class="bk k-btn">${svg("chevron-left", 2.4)}Kembali</div>` +
      `<div class="nx k-btn">Lanjut${svg("arrow-right", 2.4)}<span class="l2">${svg("send", 2.2)}Kirim pesanan</span></div>` +
      `<div class="ok"><i>${svg("check", 3)}</i><b>Pesanan terkirim!</b><span>Admin konfirmasi lewat WhatsApp dalam 10 menit.</span></div>` +
      `</div>` +
      `<div class="sm"><h5>Ringkasan pesanan</h5><div class="tile">${svg("cake", 1.6)}</div>` +
      row("u", "UKURAN", 182, "Ø 20 cm · 12 orang") + row("w", "TULISAN", 240, "Selamat ulang tahun, Bunda!") + row("a", "AMBIL", 298, "Sabtu 13 · jam 10.00") +
      `<div class="tt">Total<b class="e t0">Rp 0</b><b class="t1">Rp 320.000</b></div>` +
      `<div class="nt">${svg("shield-check", 2.2)}Bayar setelah dikonfirmasi admin</div></div>`;
    const q = K.q;
    const strip = q(".strip"), f1 = q(".f1"), f2 = q(".f2"), on = [0, 1, 2].map((i) => q(`.s${i} .on`)), nx = q(".nx"), l2 = q(".nx .l2"), ok = q(".ok");
    const o1sel = [q(".o1 .sel"), q(".o1 .ck")], dsel = q(".d1 .sel"), msel = q(".m0 .sel");
    const sw = (a, b, t) => { ft(q(a), { opacity: 1 }, { opacity: 0, duration: 0.2 }, t); ft(q(b), { opacity: 0 }, { opacity: 1, duration: 0.25 }, t + 0.1); };
    const swBack = (a, b, t) => { ft(q(b), { opacity: 1 }, { opacity: 0, duration: 0.2 }, t); ft(q(a), { opacity: 0 }, { opacity: 1, duration: 0.25 }, t + 0.1); };
    // start state
    I(strip, { x: 0 }); I(f1, { scaleX: 0 }); I(f2, { scaleX: 0 });
    on.forEach((o, i) => I(o, { opacity: i === 0 ? 1 : 0, scale: 1 }));
    I(l2, { opacity: 0 }); I(ok, { opacity: 0 });
    K.qa(".op .sel, .op .ck, .dt .sel, .tm .sel").forEach((e) => I(e, { opacity: 0, scale: 1 }));
    ["u", "w", "a", "t"].forEach((c) => { I(q(`.${c}0`), { opacity: 1 }); I(q(`.${c}1`), { opacity: 0 }); });
    // step 1: choose Ø 20 cm
    tap(q(".o1"), 0.5, { color: "rgba(214,51,108,.25)" });
    ft(o1sel[0], { opacity: 0 }, { opacity: 1, duration: 0.2 }, 0.58);
    ft(o1sel[1], { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.5)" }, 0.6);
    sw(".u0", ".u1", 0.7); sw(".t0", ".t1", 0.75);
    // next -> step 2
    tap(nx, 1.12, { color: "rgba(255,255,255,.5)" });
    ft(strip, { x: 0 }, { x: -496, duration: 0.5, ease: "power3.inOut" }, 1.25);
    ft(f1, { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: "power2.inOut" }, 1.25);
    ft(on[1], { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, 1.62);
    const clear = typeText(q(".ty"), "Selamat ulang tahun, Bunda!", 1.85, 2.6, true);
    sw(".w0", ".w1", 2.65);
    // next -> step 3
    tap(nx, 2.85, { color: "rgba(255,255,255,.5)" });
    ft(strip, { x: -496 }, { x: -992, duration: 0.5, ease: "power3.inOut" }, 2.98);
    ft(f2, { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: "power2.inOut" }, 2.98);
    ft(on[2], { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, 3.35);
    ft(l2, { opacity: 0 }, { opacity: 1, duration: 0.2 }, 3.05);
    tap(q(".d1"), 3.4, { color: "rgba(214,51,108,.25)" }); ft(dsel, { opacity: 0 }, { opacity: 1, duration: 0.2 }, 3.48);
    tap(q(".m0"), 3.65, { color: "rgba(214,51,108,.25)" }); ft(msel, { opacity: 0 }, { opacity: 1, duration: 0.2 }, 3.72);
    sw(".a0", ".a1", 3.8);
    // send
    tap(nx, 4.1, { color: "rgba(255,255,255,.5)" });
    ft(ok, { opacity: 0 }, { opacity: 1, duration: 0.3 }, 4.25);
    const okI = q(".ok i");
    I(okI, { scale: 0 });
    ft(okI, { scale: 0 }, { scale: 1, duration: 0.45, ease: "back.out(2.4)" }, 4.3);
    // reset behind the success panel, then reveal step 1 again
    set(strip, { x: 0 }, 5.1); clear(5.1); set(l2, { opacity: 0 }, 5.1);
    [...o1sel, dsel, msel].forEach((e) => set(e, { opacity: 0 }, 5.1));
    ft(f2, { scaleX: 1 }, { scaleX: 0, duration: 0.3, ease: "power2.inOut" }, 5.1);
    ft(f1, { scaleX: 1 }, { scaleX: 0, duration: 0.3, ease: "power2.inOut" }, 5.3);
    ft(on[2], { opacity: 1 }, { opacity: 0, duration: 0.2 }, 5.15); ft(on[1], { opacity: 1 }, { opacity: 0, duration: 0.2 }, 5.35);
    ["u", "w", "a", "t"].forEach((c, i) => swBack(`.${c}0`, `.${c}1`, 5.1 + i * 0.05));
    ft(ok, { opacity: 1 }, { opacity: 0, duration: 0.3 }, 5.35);
    set(okI, { scale: 0 }, 5.7);
  },
});
