// 06 · Tab menu: a café menu with three category tabs. The dark pill slides to the next tab (with a tap ripple), the current cards
// lift away and the new cards rise in one by one; Kopi -> Non-Kopi -> Camilan -> back to Kopi in one loop. Fictional: "Kopi Teras Senja".
CAR.def("tab-menu", {
  build(K) {
    const { svg, I, ft, tap } = K;
    const TABS = [
      ["Kopi", "coffee", [["kopisusu", "Kopi Susu Aren", "Espresso, susu segar, gula aren", "Rp 22.000", "TERLARIS"], ["americano", "Es Americano", "Double shot, tanpa gula", "Rp 20.000", ""], ["cappuccino", "Cappuccino", "Busa susu lembut, latte art", "Rp 26.000", ""]]],
      ["Non-Kopi", "leaf", [["matcha", "Matcha Latte", "Matcha + susu, dingin", "Rp 27.000", "BARU"], ["cokelat", "Es Cokelat", "Cokelat pekat, krim kocok", "Rp 24.000", ""], ["semangka", "Jus Semangka", "Buah segar tanpa sirup", "Rp 18.000", ""]]],
      ["Camilan", "cookie", [["donat", "Donat Cokelat", "Taburan meses warna-warni", "Rp 12.000", ""], ["croissant", "Croissant Mentega", "Dipanggang tiap pagi", "Rp 18.000", "HANGAT"], ["cookies", "Cookies Cokelat", "Renyah luar, lembut dalam", "Rp 15.000", ""]]],
    ];
    let cards = "";
    TABS.forEach(([, , items], g) => items.forEach(([img, nm, ds, pr, tg], i) => {
      cards += `<div class="cd g${g}" style="left:${40 + i * 290}px"><i class="im" style="background-image:url(${K.img(img)})"></i>${tg ? `<span class="tg">${tg}</span>` : ""}` +
        `<b>${nm}</b><p>${ds}</p><em>${pr}</em><i class="ad">${svg("plus", 2.4)}</i></div>`;
    }));
    const tabs = TABS.map(([n, ic], i) => `<div class="tb t${i}" style="left:${4 + i * 134}px"><span class="w d">${svg(ic, 2.2)}${n}</span><span class="w l">${svg(ic, 2.2)}${n}</span></div>`).join("");
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("coffee", 2.2)}</i><div class="bn">Kopi Teras Senja</div><div class="mn">Menu Lokasi Promo</div><div class="nb">${svg("truck", 2.2)}Pesan antar</div></div>` +
      `<div class="ht">Menu hari ini</div><div class="hs">Diseduh dari biji kopi Temanggung</div>` +
      `<div class="tabs"><i class="ind"></i>${tabs}</div>` + cards;
    const ind = K.q(".ind");
    const groups = [0, 1, 2].map((g) => K.qa(".cd.g" + g));
    const light = [0, 1, 2].map((i) => K.q(`.t${i} .l`)), dark = [0, 1, 2].map((i) => K.q(`.t${i} .d`));
    // start: tab 0 active
    I(ind, { x: 0 });
    light.forEach((l, i) => { I(l, { opacity: i === 0 ? 1 : 0 }); I(dark[i], { opacity: i === 0 ? 0 : 1 }); });
    groups.forEach((cs, g) => cs.forEach((c) => I(c, { opacity: g === 0 ? 1 : 0, y: 0 })));
    // switches: [time, from, to]
    [[1.55, 0, 1], [3.3, 1, 2], [5.05, 2, 0]].forEach(([t, a, b]) => {
      tap(K.q(".t" + b), t, { color: "rgba(255,255,255,.5)", press: false });
      ft(ind, { x: a * 134 }, { x: b * 134, duration: 0.45, ease: "power3.inOut" }, t);
      ft(light[a], { opacity: 1 }, { opacity: 0, duration: 0.25 }, t + 0.05);
      ft(dark[a], { opacity: 0 }, { opacity: 1, duration: 0.25 }, t + 0.05);
      ft(light[b], { opacity: 0 }, { opacity: 1, duration: 0.25 }, t + 0.2);
      ft(dark[b], { opacity: 1 }, { opacity: 0, duration: 0.25 }, t + 0.2);
      groups[a].forEach((c, i) => ft(c, { opacity: 1, y: 0 }, { opacity: 0, y: -22, duration: 0.24, ease: "power2.in" }, t + i * 0.04));
      groups[b].forEach((c, i) => ft(c, { opacity: 0, y: 34 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, t + 0.24 + i * 0.08));
    });
  },
});
