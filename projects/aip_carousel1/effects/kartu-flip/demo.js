// 05 · Kartu balik 3D: the featured menu card tilts in 3D (light glare follows), flips over to show what is inside, the "add" button
// on the back gets pressed, then it flips on round to the front (one full 360 per loop = seamless). Fictional: "Mie Pedas Mas Bayu".
CAR.def("kartu-flip", {
  build(K) {
    const { svg, I, ft, tap } = K;
    const lv = (n) => `<span class="lv">${[0, 1, 2, 3, 4].map((i) => svg("flame", 2.2, i < n ? "" : "off")).join("")}</span>`;
    const side = (x, img, nm, ds, pr, n) => `<div class="sd" style="left:${x}px"><i class="im" style="background-image:url(${K.img(img)})"></i>` +
      `<div class="nm" style="top:166px;font-size:16px">${nm}</div><div class="ds" style="top:192px">${ds}</div>${lv(n).replace('class="lv"', 'class="lv" style="left:18px;top:222px"')}` +
      `<div class="pr" style="top:284px">${pr}</div><i class="ad" style="left:162px;top:278px">${svg("plus", 2.4)}</i></div>`;
    K.root.innerHTML =
      `<div class="nav"><i class="lg">${svg("flame", 2.2)}</i><div class="bn">Mie Pedas Mas Bayu</div><div class="mn">Menu Lokasi Kemitraan</div></div>` +
      `<div class="hd"><small>MENU ANDALAN</small><h3>Pilih level pedasmu</h3></div>` +
      side(70, "nasgor", "Nasi Goreng Kampung", "Telur ceplok + kerupuk", "Rp 22.000", 2) +
      side(642, "esteh", "Es Teh Lemon", "Segar, gula bisa diatur", "Rp 8.000", 0) +
      `<i class="sh"></i>` +
      `<div class="stage"><div class="card">` +
      `<div class="face fr"><i class="im" style="background-image:url(${K.img("mie")})"></i><span class="bdg">FAVORIT</span>` +
      `<div class="nm" style="top:194px;font-size:20px">Mie Kuah Pedas</div><div class="ds" style="top:222px">Telur ajitama · level 1–5</div>` +
      `${lv(4).replace('class="lv"', 'class="lv" style="left:18px;top:254px"')}<div class="pr" style="top:322px;font-size:23px">Rp 25.000</div>` +
      `<i class="ad" style="left:192px;top:318px">${svg("plus", 2.4)}</i><i class="gl"></i></div>` +
      `<div class="face bk"><small>ISI SEMANGKUK</small><h4>Mie Kuah Pedas</h4><ul>` +
      ["Mie kenyal buatan sendiri", "Telur ajitama", "Kuah cabai rawit segar", "Sawi + daun bawang"].map((s) => `<li>${svg("circle-check", 2.2)}${s}</li>`).join("") +
      `</ul><div class="tm">${svg("timer", 2.2)}Siap dalam 10 menit</div>` +
      `<div class="go k-btn">${svg("plus", 2.4)}Tambah ke pesanan<div class="ok">${svg("check", 2.6)}Masuk pesanan</div></div></div>` +
      `</div></div>`;
    const card = K.q(".card"), gl = K.q(".gl"), go = K.q(".go"), ok = K.q(".go .ok"), sh = K.q(".sh"), sides = K.qa(".sd");
    // rotationY runs -12 -> 348 over the loop (one full turn): the last frame flows into the first
    I(card, { rotationY: -12, rotationX: 7, y: 0, scale: 1 });
    I(gl, { x: -120 });
    I(ok, { opacity: 0 });
    I(sh, { scaleX: 1, opacity: 1 });
    ft(card, { rotationY: -12, rotationX: 7 }, { rotationY: 14, rotationX: -5, duration: 1.25, ease: "sine.inOut" }, 0);
    ft(gl, { x: -120 }, { x: 110, duration: 1.25, ease: "sine.inOut" }, 0);
    K.set(gl, { x: -120 }, 3.0);                    // glare reset while the back is showing
    // flip to the back
    ft(card, { rotationY: 14, rotationX: -5 }, { rotationY: 180, rotationX: 0, duration: 0.85, ease: "power3.inOut" }, 1.35);
    ft(card, { y: 0, scale: 1 }, { y: -14, scale: 1.05, duration: 0.42, ease: "power2.out", yoyo: true, repeat: 1 }, 1.35);
    ft(sh, { scaleX: 1, opacity: 1 }, { scaleX: 0.8, opacity: 0.6, duration: 0.42, ease: "power2.out", yoyo: true, repeat: 1 }, 1.35);
    ft(card, { rotationY: 180 }, { rotationY: 190, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: 1 }, 2.25);   // ends 4.05, before the flip back (no overlapping rotationY tweens)
    // press "Tambah ke pesanan" on the back
    tap(go, 3.05, { color: "rgba(0,0,0,.18)" });
    ft(ok, { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "power1.out" }, 3.2);
    K.set(ok, { opacity: 0 }, 5.0);                  // hidden again (back face no longer visible by then)
    // flip on to the front and settle into the start pose
    ft(card, { rotationY: 180, rotationX: 0 }, { rotationY: 348, rotationX: 7, duration: 0.9, ease: "power3.inOut" }, 4.1);
    ft(card, { y: 0, scale: 1 }, { y: -14, scale: 1.05, duration: 0.45, ease: "power2.out", yoyo: true, repeat: 1 }, 4.1);
    ft(sh, { scaleX: 1, opacity: 1 }, { scaleX: 0.8, opacity: 0.6, duration: 0.45, ease: "power2.out", yoyo: true, repeat: 1 }, 4.1);
    // side cards float gently (2 cycles per loop)
    sides.forEach((s, i) => { I(s, { y: 0 }); ft(s, { y: 0 }, { y: -7, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0); void i; });
  },
});
