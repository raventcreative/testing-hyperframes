// 04 · Dinding ulasan: three columns of customer review cards scroll endlessly (up · down · up) behind soft top/bottom fades,
// next to a rating summary. Each column moves exactly one set of cards per loop = seamless. Fictional: "Laundry Wangi Kilat".
CAR.def("dinding-ulasan", {
  build(K) {
    const { svg, I, ft, D } = K;
    const COLS = [
      { dir: -1, items: [["Bu Sari", "Bekasi", "Kemeja kantor rapi,<br>wangi, besok pagi<br>sudah sampai.", "#f08a4b"], ["Andi P.", "Depok", "Antar-jemputnya<br>selalu tepat waktu.", "#4f86e8"],
        ["Mbak Yuni", "Jakarta Timur", "Noda kopi di blus<br>putih hilang total!", "#16934a"], ["Pak Hendra", "Bekasi", "Langganan 2 tahun,<br>belum pernah ada<br>baju yang hilang.", "#8e5cd9"]] },
      { dir: 1, items: [["Rara", "Cikarang", "Selimut tebal jadi<br>lembut lagi.", "#e2557a"], ["Bu Lina", "Bekasi", "Setrikaannya rapi,<br>dilipat per jenis,<br>gampang disimpan.", "#0b6fd0"],
        ["Fajar", "Tambun", "Harga per kilo jelas,<br>nggak ada biaya<br>tambahan.", "#d9821f"], ["Dewi A.", "Bekasi", "Adminnya ramah,<br>balasnya cepat.", "#1e9e8c"]] },
      { dir: -1, items: [["Kak Mira", "Jatiasih", "Gorden ruang tamu<br>bersih dan wangi.", "#c2410c"], ["Rizky", "Bekasi", "Sepatu putihku<br>balik kinclong.", "#3d7a1f"],
        ["Bu Ningsih", "Bekasi", "Pesan pagi, sore<br>sudah diantar. Kilat<br>beneran!", "#4f86e8"], ["Yoga", "Jakarta Timur", "Packing-nya rapi,<br>plastiknya tebal.", "#8e5cd9"]] },
    ];
    const GAP = 14, Y0 = 26;
    const ini = (n) => n.replace(/^(Bu|Pak|Mbak|Kak) /, "").split(" ").map((w) => w[0]).join("").slice(0, 2).toUpperCase();
    const card = ([n, c, txt, col], y) => {
      const lines = txt.split("<br>").length, h = 94 + lines * 20;
      return [`<div class="cd" style="top:${y}px;height:${h}px"><i class="av" style="background:${col}">${ini(n)}</i><b>${n}</b><small>${c}</small>` +
        `<span class="st">${K.stars(5)}</span><p>${txt}</p></div>`, h];
    };
    let wall = "";
    const sets = COLS.map((c, ci) => {
      let y = 0, html = "";
      for (let rep = 0; rep < 2; rep++) c.items.forEach((it) => { const [h, hh] = card(it, y); html += h; y += hh + GAP; });
      wall += `<div class="col c${ci}" style="left:${ci * 198}px">${html}</div>`;
      return y / 2;                                           // height of one set (cards + gaps)
    });
    const bars = [["5", 94], ["4", 5], ["3", 1]].map(([s, p], i) => `<div class="r" style="top:${84 + i * 20}px">${s}${svg("star", 1.5)}<i><u style="width:${p}%"></u></i><em>${p}%</em></div>`);
    K.root.innerHTML =
      `<div class="wall">${wall}</div>` +
      `<div class="nav"><i class="lg">${svg("shirt", 2.2)}</i><div class="bn">Laundry Wangi Kilat</div><div class="mn">Layanan Harga Ulasan</div><div class="nb">Jemput gratis</div></div>` +
      `<div class="tg">${svg("quote", 2.2)}KATA PELANGGAN</div>` +
      `<div class="h1">Wangi, rapi,<br>pelanggan<br><span>balik lagi.</span></div>` +
      `<div class="sc"><div class="big">4,9</div><span class="st">${K.stars(5)}</span><div class="n">dari 2.300+ ulasan</div>${bars.join("")}</div>` +
      `<div class="bt k-btn">${svg("truck", 2.2)}Jemput cucian</div>` +
      `<div class="ft">${svg("badge-check", 2.2)}Ulasan asli dari pelanggan terverifikasi</div>`;
    COLS.forEach((c, ci) => {
      const col = K.q(".c" + ci), H = sets[ci];
      const a = c.dir < 0 ? Y0 : Y0 - H, b = c.dir < 0 ? Y0 - H : Y0;
      I(col, { y: a });
      ft(col, { y: a }, { y: b, duration: D, ease: "none" }, 0);
    });
  },
});
