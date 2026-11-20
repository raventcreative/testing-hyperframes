/* R29 UI layer: section tabs, problem chip, cards, stamps, wipes, captions — one paused GSAP timeline ("main") + per-seek text
   (pure functions of t). Every initial state is pinned at 0 in the nested timeline P0; fromTo without immediate render. */
(function () {
  const R = window.R29, W = R.W, WE = R.WE, S = R.S, E = R.E, D = R.D;
  const VW = window.VO_WORDS, CAPS = window.VO_CAPS;
  const $ = (id) => { const e = document.getElementById(id); if (!e) throw new Error("ui: missing #" + id); return e; };
  const tl = gsap.timeline({ paused: true });
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }
  const P0 = gsap.timeline(); tl.add(P0, 0);
  const pin = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
  const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
  const mk = (tag, cls, parent, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; if (parent) parent.appendChild(e); return e; };
  const BASE = {};   // resting transform per element (rotation for stamps, xPercent for tabs)
  const IN = {
    pop: [{ opacity: 0, scale: 0.84, y: 24 }, { opacity: 1, scale: 1, y: 0, duration: 0.42, ease: "back.out(1.4)" }],
    up: [{ opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }],
    left: [{ opacity: 0, x: -110 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }],
    right: [{ opacity: 0, x: 110 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }],
    flip: [{ opacity: 0, rotationX: -85, transformPerspective: 900, transformOrigin: "50% 0%" }, { opacity: 1, rotationX: 0, duration: 0.5, ease: "back.out(1.3)" }],
    stamp: [{ opacity: 0, scale: 1.9 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power2.in" }],
    grow: [{ opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.5)" }],
  };
  const OUT = {
    fade: [{ opacity: 1 }, { opacity: 0, duration: 0.25, ease: "power1.in" }],
    up: [{ opacity: 1, y: 0 }, { opacity: 0, y: -50, duration: 0.3, ease: "power2.in" }],
    left: [{ opacity: 1, x: 0 }, { opacity: 0, x: -140, duration: 0.32, ease: "power2.in" }],
    right: [{ opacity: 1, x: 0 }, { opacity: 0, x: 140, duration: 0.32, ease: "power2.in" }],
    down: [{ opacity: 1, y: 0 }, { opacity: 0, y: 70, duration: 0.3, ease: "power2.in" }],
    shrink: [{ opacity: 1, scale: 1 }, { opacity: 0, scale: 0.6, duration: 0.28, ease: "power2.in" }],
  };
  const pinned = new Set();
  function vis(id, a, b, kin = "pop", kout = "fade") {
    const el = typeof id === "string" ? $(id) : id, base = BASE[el.id] || {};
    if (!pinned.has(el)) { pin(el, Object.assign({ opacity: 0 }, base)); pinned.add(el); }
    const [f, t] = IN[kin]; ft(el, Object.assign({}, base, f), Object.assign({}, base, t), a);
    if (kin === "stamp") ft(el, { x: 0 }, { x: 6, duration: 0.05, yoyo: true, repeat: 3, ease: "none" }, a + 0.2);
    if (b != null) { const [f2, t2] = OUT[kout]; ft(el, Object.assign({}, base, f2), Object.assign({}, base, t2), b - (t2.duration || 0.25)); }
  }
  // stamps keep their tilt
  document.querySelectorAll(".stamp").forEach((s) => { const m = /rotate\((-?\d+(?:\.\d+)?)deg\)/.exec(s.getAttribute("style") || ""); if (m) { s.style.transform = ""; BASE[s.id] = { rotation: +m[1] }; } });

  /* ------------------------------------------------------------ captions (per-word boxes) */
  const capRoot = $("caps");
  CAPS.forEach(([cs, ce, a, b], ci) => {
    const d = mk("div", "cap", capRoot); d.id = "cap" + ci;
    pin(d, { opacity: 0 }); ft(d, { opacity: 0 }, { opacity: 1, duration: 0.08, ease: "none" }, cs);
    ft(d, { opacity: 1, y: 0 }, { opacity: 0, y: -10, duration: 0.12, ease: "power2.in" }, Math.max(cs + 0.2, ce - 0.12));
    for (let i = a; i <= b; i++) {
      const m = mk("span", "m", d), w = mk("span", "w" + (VW[i][3] ? " k" : ""), m, VW[i][0]);
      if (i < b) d.appendChild(document.createTextNode(" "));
      const t = Math.max(cs, VW[i][1] - 0.06);
      pin(m, { opacity: 0 }); ft(m, { opacity: 0 }, { opacity: 1, duration: 0.06, ease: "none" }, t + 0.03);
      pin(w, { yPercent: 118 }); ft(w, { yPercent: 118 }, { yPercent: 0, duration: 0.3, ease: "power4.out" }, t - 0.03);
      if (VW[i][3]) { const h = mk("span", "hl", w); pin(h, { scaleX: 0 }); ft(h, { scaleX: 0 }, { scaleX: 1, duration: 0.26, ease: "power2.out" }, VW[i][1] + 0.08); }
    }
  });

  /* ------------------------------------------------------------ section tabs */
  const TABS = [
    [0.12, S(4), 'PELUANG DAPAT ANGKA <b>6</b>'], [S(4), S(6), 'TEORI vs <b>DUNIA NYATA</b>'], [S(6), S(7), 'MEJA <b>BISNIS</b>'],
    [S(7), S(10), '1 · CARA <b>KEGEDEAN / KEKECILAN</b>'], [S(10), S(12), '2 · <b>IDE SALAH</b>'], [S(12), S(16), '3 · <b>KEBANYAKAN TEBAKAN</b>'],
    [S(16), S(19), '4 · PASAR <b>KESEMPITAN</b>'], [S(19), S(23), '5 · <b>MASALAHNYA NGGAK NYATA</b>'], [S(23), S(25), '6 · <b>LEMPARAN TERBATAS</b>'],
    [S(25), S(26), 'ADA <b>2</b> CARA MAIN'], [S(26), S(28), 'CARA A · <b>GANTI SEMUA</b>'], [S(28), S(31), 'CARA B · <b>KUNCI VARIABEL</b>'],
    [S(31), S(33), 'PILIH <b>IDE</b> · TETAP DI <b>1 PASAR</b>'], [S(33), S(34), 'KESALAHAN <b>PALING UMUM</b>'], [S(35), S(37), '<b>SHINY OBJECT</b> SYNDROME'],
    [S(37), S(41), 'CARA PEBISNIS <b>YANG BERHASIL</b>'], [S(41), S(42), '<b>AI</b> BANTU NGUTAK-ATIK'], [S(42), S(44), '<b>INTINYA</b>'],
  ];
  const tabRoot = $("tabs");
  TABS.forEach(([a, b, h], i) => { const e = mk("div", "tt", tabRoot, `<span class="bar"></span><span class="x">${h}</span>`); e.id = "tab" + i; BASE[e.id] = { xPercent: -50 };
    vis(e, a + (i ? 0.08 : 0), b, "flip", "up"); });

  /* ------------------------------------------------------------ problem chip */
  pin("#chip", { opacity: 0, scale: 0.6 });
  ft("#chip", { opacity: 0, scale: 0.6, x: -30 }, { opacity: 1, scale: 1, x: 0, duration: 0.38, ease: "back.out(2)" }, S(7) + 0.05);
  [S(10), S(12), S(16), S(19), S(23)].forEach((t) => ft("#chip", { scale: 1 }, { scale: 1.14, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out" }, t + 0.05));
  ft("#chip", { opacity: 1 }, { opacity: 0, duration: 0.25 }, S(25) - 0.25);
  // during the big CTA / AI / rule beats the chip is not needed; the tab is enough

  /* ------------------------------------------------------------ s01-s05 */
  vis("stat", W("peluang") - 0.15, S(4) + 0.05, "right", "right");
  pin("#statd", { opacity: 0 }); ft("#statd", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.15 }, W("16,7%.") + 0.32);
  vis("q4", S(4) + 0.12, S(5) + 0.05, "pop", "up"); ft("#q4 .b", { scale: 1 }, { scale: 1.06, duration: 2.6, ease: "sine.inOut" }, S(4) + 0.5); pin("#q4 .b", { scale: 1 }); vis("st4", W("bisnis?") - 0.05, S(5) + 0.05, "stamp", "fade");
  pin("#world", { filter: "blur(0px)" }); ft("#world", { filter: "blur(0px)" }, { filter: "blur(9px)", duration: 0.4 }, S(4)); ft("#world", { filter: "blur(9px)" }, { filter: "blur(0px)", duration: 0.45 }, S(6) - 0.2);
  vis("paper", S(5) + 0.02, W("dunia") - 0.05, "left", "down");
  ["p1", "p2", "p3"].forEach((id, i) => vis(id, S(5) + 0.15 + i * 0.16, null, "up"));
  vis("pok", W("iya.") - 0.08, null, "stamp");
  vis("spin", W("dunia") - 0.1, S(6) + 0.05, "pop", "shrink");
  { const reel = $("reel"); const L = ["IDE SALAH", "PASAR SEMPIT", "MODAL HABIS", "CARA KEGEDEAN", "NGGAK ADA MASALAH", "KEBANYAKAN TEBAKAN", "CARA KEKECILAN"];
    for (let i = 0; i < 20; i++) mk("div", "it", reel, L[i % L.length]); mk("div", "it k", reel, "DUNIA NYATA: BEDA"); mk("div", "it", reel, "IDE SALAH"); }
  /* ------------------------------------------------------------ s08-s11 */
  vis("ex8", W("jualan") - 0.15, S(9) - 0.02, "right", "right"); vis("st8", W("ruko") + 0.25, S(9) - 0.02, "stamp", "fade");
  vis("ex9", W("grup") - 0.35, S(10) - 0.02, "left", "left"); vis("st9", W("sekali.", S(9)) - 0.1, S(10) - 0.02, "stamp", "fade");
  vis("st10", W("6.", S(10)) - 0.2, S(11) + 0.02, "stamp", "fade");
  vis("cnt", S(11) + 0.02, S(12) - 0.02, "right", "right");
  vis("unk", W("Produk") - 0.2, S(14) + 0.1, "right", "right");
  ["u1", "u2", "u3", "u4"].forEach((id, i) => vis(id, [W("Produk"), W("pasar", S(13)), W("harga"), W("cara", S(13))][i] - 0.08, null, "left"));
  ft("#unk", { x: 0 }, { x: 8, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }, W("semuanya") + 0.05);
  vis("odds", W("Peluangnya") - 0.2, S(16) - 0.02, "flip", "up");
  /* ------------------------------------------------------------ s17-s24 */
  vis("pin", W("servis") - 0.25, S(19) - 0.05, "right", "right"); vis("st18", W("mental") + 0.02, S(19) - 0.05, "stamp", "fade");
  vis("survey", S(20) + 0.08, S(21) - 0.02, "up", "up");
  document.querySelectorAll("#survey .ans span").forEach((e, i) => { pin(e, { opacity: 0, scale: 0.6 }); ft(e, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, W("dirasain") - 0.2 + i * 0.35); });
  ft("#survey .m b", { scale: 1 }, { scale: 1.35, duration: 0.14, yoyo: true, repeat: 3, ease: "power2.out" }, W("siapa-siapa,") - 0.1); pin("#survey .m b", { scale: 1 });
  pin("#phone", { opacity: 0, x: 380 }); ft("#phone", { opacity: 0, x: 380, rotation: 8 }, { opacity: 1, x: 0, rotation: 0, duration: 0.5, ease: "back.out(1.2)" }, S(21) + 0.02);
  ft("#phone", { opacity: 1, y: 0 }, { opacity: 0, y: 120, duration: 0.3, ease: "power2.in" }, S(22) + 0.2);
  ft("#phone .big .n", { scale: 1 }, { scale: 1.25, duration: 0.15, yoyo: true, repeat: 3, ease: "power2.out" }, W("warteg") - 0.1); pin("#phone .big .n", { scale: 1 });
  ft("#phone .btn", { scale: 1 }, { scale: 0.9, duration: 0.1, yoyo: true, repeat: 1 }, W("pernah") - 0.05); pin("#phone .btn", { scale: 1 });
  vis("st22", W("lolos") + 0.2, S(23) - 0.02, "stamp", "fade");
  vis("res", W("lemparanmu") - 0.2, S(25) - 0.02, "flip", "up");
  ["rb0", "rb1", "rb2"].forEach((id, i) => { pin("#" + id, { width: "100%" }); ft("#" + id, { width: "100%" }, { width: "6%", duration: 0.55, ease: "power2.inOut" }, W(["Modal,", "waktu,", "tenaga"][i]) + 0.05); });
  vis("spA", W("Ada") - 0.1, S(26) + 0.02, "left", "left"); vis("spB", W("dua") - 0.1, S(26) + 0.02, "right", "right");
  /* ------------------------------------------------------------ s27-s33 */
  vis("scat", W("Hasilnya") - 0.1, S(28) - 0.02, "right", "right");
  { const pl = $("scpl"); for (let i = 0; i < 16; i++) { const d = mk("i", "", pl); const h = (n) => { const s = Math.sin(n * 91.7 + 13.1) * 43758.5; return s - Math.floor(s); };
      d.style.left = (8 + 84 * h(i)) + "%"; d.style.top = (12 + 76 * h(i + 40)) + "%"; pin(d, { opacity: 0, scale: 0 }); ft(d, { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)" }, W("Hasilnya") + 0.15 + i * 0.1); } }
  vis("ctrl", S(29) + 0.05, S(31) - 0.02, "right", "right");
  vis("learn", W("Tiap", S(30)) - 0.1, S(31) - 0.02, "left", "left");
  vis("chk1", W("pilih", S(31)) - 0.2, S(33) - 0.02, "right", "right");
  vis("c1a", W("tepat,") - 0.05, null, "left"); vis("c1b", W("perbaiki") - 0.05, null, "left"); vis("c1c", W("pasar,", S(32)) - 0.05, null, "left");
  vis("ex33", S(33) + 0.08, S(34) - 0.02, "right", "right");
  /* ------------------------------------------------------------ s34-s38 */
  vis("slama", W("shiny") - 0.12, S(35) + 0.05, "stamp", "up"); vis("slamb", W("syndrome.") - 0.05, S(35) + 0.05, "up", "up");
  vis("prog", S(35) + 0.1, S(37) - 0.02, "flip", "up");
  vis("flip", S(37) + 0.05, S(38) - 0.02, "pop", "up");
  pin("#flipin", { rotationX: 0 }); ft("#flipin", { rotationX: 0 }, { rotationX: 180, duration: 0.6, ease: "back.out(1.2)" }, W("kebalikannya.") - 0.3);
  pin("#flip .f2", { autoAlpha: 0 }); tl.set("#flip .f2", { autoAlpha: 1 }, W("kebalikannya.") - 0.1); tl.set("#flip .f1", { autoAlpha: 0 }, W("kebalikannya.") - 0.1); pin("#flip .f1", { autoAlpha: 1 });
  vis("chk2", W("milih", S(38)) - 0.2, S(39) - 0.02, "left", "left");
  vis("c2a", W("pasar", S(38)) - 0.05, null, "left"); vis("c2b", W("ide", S(38) + 2.5) - 0.05, null, "left");
  /* ------------------------------------------------------------ s39-s41 process fill, flood, AI */
  pin("#fill", { opacity: 0 }); ft("#fill", { opacity: 0 }, { opacity: 1, duration: 0.2 }, S(39) - 0.02); ft("#fill", { opacity: 1, y: 0 }, { opacity: 0, y: -40, duration: 0.3, ease: "power2.in" }, W("6.", S(40)) + 0.25);
  { const tiles = document.querySelectorAll("#fill .tile"), sts = document.querySelectorAll("#fill .st");
    tiles.forEach((e, i) => { pin(e, { opacity: 0, y: -30 }); ft(e, { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.6)" }, S(39) + 0.05 + i * 0.1); });
    const tw = [W("produknya,"), W("penawarannya,"), W("harganya,"), W("jualannya.")];
    sts.forEach((e, i) => { pin(e, { height: 0, opacity: 1 }); ft(e, { height: 0 }, { height: 84, duration: 0.22, ease: "power2.in" }, tw[i] - 0.05);
      ft(e, { opacity: 1 }, { opacity: 0, duration: 0.2 }, tw[i] + 0.45); ft(tiles[i], { scale: 1 }, { scale: 1.08, duration: 0.12, yoyo: true, repeat: 1 }, tw[i] - 0.05); });
    pin("#flv", { width: "0%" }); tw.forEach((t, i) => ft("#flv", { width: (i * 25) + "%" }, { width: ((i + 1) * 25) + "%", duration: 0.4, ease: "power2.out" }, t + 0.15)); }
  pin("#flood", { opacity: 0 }); ft("#flood", { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "none" }, W("6.", S(40)) + 1.0); ft("#flood", { opacity: 1 }, { opacity: 0, duration: 0.4 }, S(42) + 0.05);
  vis("aitag", S(41) + 0.2, S(42) - 0.02, "up", "up");
  vis("ai1", W("ringkas") - 0.25, S(42) - 0.02, "left", "left"); vis("ai2", W("cari", S(41)) - 0.25, S(42) - 0.02, "right", "right"); vis("ai3", W("bikin", S(41)) - 0.25, S(42) - 0.02, "left", "left");
  /* ------------------------------------------------------------ s42-s45 */
  pin("#k42", { opacity: 1 });
  vis(document.querySelector("#k42 .a"), S(42) + 0.05, S(43) + 0.12, "up", "up");
  vis(document.querySelector("#k42 .b"), W("banyak-banyakan") - 0.1, S(43) + 0.12, "up", "up");
  pin("#k42s", { scaleX: 0 }); ft("#k42s", { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power2.inOut" }, W("lemparan.", S(42)) - 0.15);
  vis("k42c", W("lemparan.", S(42)) + 0.12, S(43) + 0.12, "up", "up");
  vis("r1", W("Pilih", S(43)) - 0.1, S(44) - 0.02, "left", "up"); vis("r2", W("Pilih", S(43) + 1) - 0.1, S(44) - 0.02, "left", "up");
  vis("r3", W("Dan", S(43)) - 0.05, S(44) - 0.02, "left", "up"); vis("r4", W("sebelum") - 0.1, S(44) - 0.02, "left", "up");
  vis("ctaveil", S(44) - 0.05, null, "up");
  vis("ws", S(44) + 0.05, W("Komen") - 0.1, "up", "up");
  ["w1", "w2", "w3", "w4", "w5"].forEach((id, i) => vis(id, [W("lembar"), W("dadu", S(44)), W("nampanmu,"), W("nampanmu,") + 0.3, W("perintah")][i] - 0.05, null, "left"));
  vis("cbox", W("Komen") - 0.15, D - 1.15, "up", "up");
  ft("#send", { scale: 1 }, { scale: 0.86, duration: 0.08, yoyo: true, repeat: 1 }, W("aku", S(45)) + 0.05);
  vis("dm", W("kirim", S(45)) - 0.1, D - 1.15, "right", "up");
  vis("endlogo", D - 1.0, null, "grow"); ft("#ctaveil", { opacity: 1 }, { opacity: 1, backgroundColor: "rgba(244,248,254,.93)", duration: 0.3 }, D - 1.15);
  ft("#brandlogo", { opacity: 0.95 }, { opacity: 0, duration: 0.3 }, D - 1.2); pin("#brandlogo", { opacity: 0.95 });
  pin("#gdot", { opacity: 0 });

  /* ------------------------------------------------------------ wipes (different per section change) */
  const wipe = $("wipe"), COLS = ["#ffffff", "#e3edfa", "#294b77", "#ffffff", "#e3edfa", "#ffffff"];
  const WIPES = [[S(7) - 0.18, 1], [S(16) - 0.18, -1], [S(23) - 0.18, 1], [S(28) - 0.18, -1], [S(31) - 0.18, 1], [S(42) - 0.18, -1]];
  WIPES.forEach(([t, dir], k) => { COLS.forEach((c, i) => { const s = mk("i", "", wipe); s.style.background = c; s.style.width = (c === "#294b77" ? 60 : 250) + "px";
    const x0 = dir > 0 ? -420 - i * 250 : 1080 + 170 + i * 250, x1 = dir > 0 ? 1500 + (5 - i) * 250 : -420 - (5 - i) * 250;
    pin(s, { x: x0, opacity: 1 }); ft(s, { x: x0 }, { x: x1, duration: 0.62, ease: "power2.inOut" }, t - 0.12 + 0.02 * i); }); });
  // iris on problem 5 (the floor vanishes) and on "kebalikannya"
  pin("#iris", { "--r": "1300px", autoAlpha: 0 });
  [S(19), S(37)].forEach((t) => { tl.set("#iris", { autoAlpha: 1 }, t - 0.36); tl.set("#iris", { autoAlpha: 0 }, t + 0.42);
    ft("#iris", { "--r": "1300px" }, { "--r": "0px", duration: 0.34, ease: "power3.in" }, t - 0.36); ft("#iris", { "--r": "0px" }, { "--r": "1300px", duration: 0.4, ease: "power3.out" }, t + 0.0); });

  /* ------------------------------------------------------------ ambient */
  tl.fromTo("#grid", { x: 0, y: 0 }, { x: 430, y: 430, duration: D, ease: "none", immediateRender: false }, 0); pin("#grid", { x: 0, y: 0 });
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 64, y: 40, duration: D, ease: `steps(${Math.round(D * 15)})`, immediateRender: false }, 0); pin("#grain", { x: 0, y: 0 });
  tl.set({}, {}, D - 0.01);
  (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
  tl.render(0, true, true);
  window.__timelines = window.__timelines || {}; window.__timelines["main"] = tl;

  /* ------------------------------------------------------------ per-seek text (pure functions of t) */
  const one = (x) => Math.max(0, Math.min(1, x)), eo = (x) => 1 - Math.pow(1 - one(x), 3), io = (u) => { u = one(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const fmt = (v, d) => v.toFixed(d).replace(".", ",");
  const lpath = $("lpath"), LL = lpath.getTotalLength(); lpath.style.strokeDasharray = LL + " " + LL;
  function texts(t) {
    // stat card: 1x -> 10x -> 100x
    let lb, v, f, fs = 88;
    if (t < S(2) + 0.1) { lb = "1× LEMPAR"; v = 16.7 * eo((t - (W("16,7%.") - 0.15)) / 0.55); f = v > 0 ? `peluang 1 dari 6` : "peluang dapat 6"; }
    else if (t < S(3) + 0.1) { lb = "10× LEMPAR"; v = 16.7 + (83.8 - 16.7) * eo((t - (W("83,8%.") - 0.25)) / 0.6); f = `1 − (5/6)<sup>10</sup>`; }
    else { lb = "100× LEMPAR"; v = 83.8 + (99.99999 - 83.8) * eo((t - (W("100%.") - 0.3)) / 0.6); f = `1 − (5/6)<sup>100</sup>`; fs = 62; }
    $("statl").textContent = lb; const sn = $("statn"); sn.style.fontSize = fs + "px";
    sn.textContent = t < W("16,7%.") - 0.15 ? "?" : (v >= 99.99999 - 1e-9 ? "99,99999" : fmt(v, t < S(3) + 0.1 ? 1 : (v > 99.9 ? 5 : 1))) + (t < W("16,7%.") - 0.15 ? "" : "%"); $("statf").innerHTML = f;
    const pct = Math.min(100, v); $("statm").style.width = pct + "%"; $("statd").style.left = pct + "%";
    // chip
    const pn = t < S(10) ? 1 : t < S(12) ? 2 : t < S(16) ? 3 : t < S(19) ? 4 : t < S(23) ? 5 : 6; $("chipn").innerHTML = pn + "<small data-layout-allow-occlusion>/6</small>";
    // spinning list (lands on index 20)
    { const a = W("dunia") - 0.1, b = W("cerita.") + 0.1, u = one((t - a) / (b - a)); const pos = 19 * (1 - Math.pow(1 - u, 3.2)); $("reel").style.transform = `translateY(${(-110 * pos + 0).toFixed(1)}px)`; }
    // 1000 throws counter
    { const a = S(11) + 0.1, b = W("keluar.") + 0.1, u = one((t - a) / (b - a)); const n = Math.round(1000 * (u * u * (3 - 2 * u))); $("cntn").textContent = n.toLocaleString("id-ID") + "×"; }
    // map radius
    { const k = io((t - (W("satu", S(17)) - 0.1)) / 0.5); $("pinr").style.width = $("pinr").style.height = (120 - 70 * k).toFixed(1) + "px"; }
    // throw controls: three throws, values settle closer each time
    { const thr = [W("Dadu", S(29)) + 0.1, W("ubah") - 0.1, W("Tiap", S(30)) + 0.1], vals = [[62, 90, 30], [48, 70, 44], [40, 58, 50]];
      let k = 0; for (let j = 0; j < 3; j++) if (t >= thr[j] - 0.9) k = j; const prev = vals[Math.max(0, k - 1)], cur = vals[k], u = io((t - (thr[k] - 0.9)) / 0.5);
      for (let i = 0; i < 3; i++) { const x = prev[i] + (cur[i] - prev[i]) * (k ? u : 1); $("ck" + i).style.left = x + "%"; $("cv" + i).textContent = ["", "", ""][i]; } }
    // learning chart: the guide dot draws it
    { const a = W("Tiap", S(30)) + 0.1, b = W("naik.") + 0.2, u = io((t - a) / (b - a)); lpath.style.strokeDashoffset = (LL * (1 - u)).toFixed(1);
      const p = lpath.getPointAtLength(LL * u); $("ldot").setAttribute("cx", p.x.toFixed(1)); $("ldot").setAttribute("cy", p.y.toFixed(1)); }
    // progress to the target
    { let p = 0; if (t < W("kinclong,")) p = 62 * io((t - (S(35) + 0.15)) / (W("kinclong,") - S(35) - 0.15)); else p = 62;
      if (t > W("Semuanya") - 0.05) p = 62 * (1 - io((t - (W("Semuanya") - 0.05)) / (W("nol") + 0.25 - W("Semuanya")))); $("progn").textContent = Math.round(p) + "%"; $("progb").style.width = p + "%"; }
    // process fill count
    { const tw = [W("produknya,"), W("penawarannya,"), W("harganya,"), W("jualannya.")]; document.querySelectorAll(".fpc").forEach((e) => (e.textContent = tw.filter((x) => t > x + 0.15).length + "/4")); }
    // CTA typing
    { const t0 = W("DADU,") - 0.12, n = Math.max(0, Math.min(4, Math.floor((t - t0) / 0.08) + 1)); $("ctx").textContent = t >= t0 ? "DADU".slice(0, n) : ""; $("cph").style.display = t >= t0 ? "none" : "inline";
      $("cur").style.opacity = Math.floor(t * 3) % 2 ? 1 : 0.2; }
  }
  texts(0); window.addEventListener("hf-seek", (e) => texts(e.detail.time));
})();
