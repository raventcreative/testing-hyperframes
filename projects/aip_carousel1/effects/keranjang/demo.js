// 07 · Masuk keranjang: three "+ Keranjang" presses; each time the product photo flies in a curve into the cart icon, the cart
// bumps and its badge counts 1 -> 2 -> 3. The mini cart drops open, "Checkout" is pressed, then cart + buttons reset (loop).
// Fictional: "Teras Hijau" (tanaman meja).
CAR.def("keranjang", {
  build(K) {
    const { svg, I, ft, tap, pop, hide } = K;
    const P = [["bonsai", "Bonsai Meja", "Pot keramik putih · 20 cm", "Rp 85.000"], ["syngonium", "Syngonium Pink", "Pot hitam minimalis", "Rp 65.000"], ["palem", "Palem Kipas", "Pot tanah liat · 45 cm", "Rp 87.000"]];
    const cx = (i) => 40 + i * 290;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("sprout", 2.2)}</i><div class="bn">Teras Hijau</div><div class="mn">Tanaman Pot Perawatan</div></div>` +
      `<div class="ht">Tanaman meja paling dicari</div><div class="hs">Gratis pupuk cair + panduan rawat di setiap pesanan</div>` +
      P.map(([img, nm, ds, pr], i) => `<div class="cd c${i}" style="left:${cx(i)}px"><i class="im" style="background-image:url(${K.img(img)})"></i><b>${nm}</b><p>${ds}</p><em>${pr}</em>` +
        `<div class="bt k-btn">${svg("plus", 2.4)}Keranjang<span class="ok">${svg("check", 2.6)}Ditambahkan</span></div></div>`).join("") +
      P.map(([img], i) => `<i class="fly f${i}" style="background-image:url(${K.img(img)})"></i>`).join("") +
      `<div class="cart">${svg("shopping-cart", 2.2)}</div><div class="bdg"><i class="n1">1</i><i class="n2">2</i><i class="n3">3</i></div>` +
      `<div class="dr"><h5>Keranjang (3)</h5>` +
      P.map(([img, nm, ds, pr], i) => `<div class="row" style="top:${62 + i * 58}px"><i style="background-image:url(${K.img(img)})"></i><b>${nm}</b><span>1 x ${pr}</span><em>${pr}</em></div>`).join("") +
      `<hr><div class="tot">Total<b>Rp 237.000</b></div><div class="co k-btn">Checkout${svg("arrow-right", 2.4)}<span class="ok">${svg("circle-check", 2.4)}Pesanan dibuat</span></div></div>`;
    const cart = K.q(".cart"), bdg = K.q(".bdg"), nums = [K.q(".n1"), K.q(".n2"), K.q(".n3")], dr = K.q(".dr"), co = K.q(".co"), coOk = K.q(".co .ok");
    const okBtn = P.map((_, i) => K.q(`.c${i} .bt .ok`));
    I(bdg, { scale: 0, opacity: 0 });
    nums.forEach((n, i) => I(n, { y: i === 0 ? 0 : 24 }));
    okBtn.forEach((o) => I(o, { opacity: 0 }));
    I(cart, { scale: 1, rotation: 0 });
    I(coOk, { opacity: 0 });
    // three adds
    [0.35, 1.3, 2.25].forEach((t, i) => {
      const btn = K.q(`.c${i} .bt`), fly = K.q(".f" + i);
      tap(btn, t, { color: "rgba(255,255,255,.6)" });
      ft(okBtn[i], { opacity: 0 }, { opacity: 1, duration: 0.12 }, t + 0.12);
      const x0 = cx(i) + 136 - 35, y0 = 160 + 112 - 35, x1 = 864 + 22 - 35, y1 = 12 + 21 - 35;
      I(fly, { x: x0, y: y0, scale: 0, opacity: 0 });
      ft(fly, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.12, ease: "back.out(2)" }, t + 0.05);
      ft(fly, { x: x0 }, { x: x1, duration: 0.62, ease: "power1.in" }, t + 0.18);
      ft(fly, { y: y0 }, { y: y1, duration: 0.62, ease: "power2.out" }, t + 0.18);
      ft(fly, { scale: 1, opacity: 1 }, { scale: 0.3, opacity: 0.2, duration: 0.6, ease: "power2.in" }, t + 0.2);
      K.set(fly, { opacity: 0 }, t + 0.8);
      const ta = t + 0.8;                                 // arrival
      ft(cart, { scale: 1, rotation: 0 }, { scale: 1.2, rotation: -10, duration: 0.12, ease: "power2.out" }, ta);
      ft(cart, { scale: 1.2, rotation: -10 }, { scale: 1, rotation: 0, duration: 0.4, ease: "elastic.out(1.2, 0.45)" }, ta + 0.12);
      if (i === 0) ft(bdg, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.6)" }, ta);
      else {
        ft(nums[i - 1], { y: 0 }, { y: -24, duration: 0.25, ease: "power2.in" }, ta);
        ft(nums[i], { y: 24 }, { y: 0, duration: 0.3, ease: "back.out(2)" }, ta + 0.08);
        ft(bdg, { scale: 1 }, { scale: 1.25, duration: 0.15, ease: "power2.out", yoyo: true, repeat: 1 }, ta);
      }
    });
    // mini cart opens, checkout, closes; everything resets for the loop
    pop(dr, 3.35, { scale: 0.86, y: -10 }, 0.4, "back.out(1.4)");
    tap(co, 4.3, { color: "rgba(255,255,255,.5)" });
    ft(coOk, { opacity: 0 }, { opacity: 1, duration: 0.12 }, 4.4);
    hide(dr, 5.0, { scale: 0.9, y: -8 }, 0.3);
    K.set(coOk, { opacity: 0 }, 5.35);
    ft(bdg, { scale: 1, opacity: 1 }, { scale: 0, opacity: 0, duration: 0.25, ease: "power2.in" }, 5.2);
    nums.forEach((n, i) => K.set(n, { y: i === 0 ? 0 : 24 }, 5.5));
    okBtn.forEach((o, i) => ft(o, { opacity: 1 }, { opacity: 0, duration: 0.25 }, 5.25 + i * 0.07));
  },
});
