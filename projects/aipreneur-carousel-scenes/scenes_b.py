"""Scenes 07, 08, 14, 15, 16 — imported by build.py."""
from scenes_a import CANVAS, CV_CSS, CV_JS_HEAD

# ---------------------------------------------------------------- 07 grid -> wave
S07_JS = CV_JS_HEAD + """
  const NX = 22, NZ = 15, CX = 402, HOR = 80, CAMH = 470, F = 520, DD = 500;
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const ph = TAU * t / D;
    for (let j = NZ - 1; j >= 0; j--) {
      const Z = j / (NZ - 1) * 720;
      const s = F / (Z + DD);
      for (let i = 0; i < NX; i++) {
        const X = (i / (NX - 1) - 0.5) * 1000;
        const Y = 70 * Math.sin(0.0105 * X + ph) + 42 * Math.sin(0.0125 * Z - 2 * ph + 0.8) + 24 * Math.sin(0.008 * (X + Z) + ph + 2.1);
        const x = CX + X * s, y = HOR + (CAMH - Y) * s;
        if (x < -10 || x > W + 10) continue;
        const u = clamp((Y + 110) / 220, 0, 1);
        const c = [mix(39, 140, u), mix(73, 205, u), mix(118, 255, u)];
        const a = 0.5 + 0.5 * clamp((s - 0.42) / 0.62, 0, 1);
        ctx.fillStyle = "rgba(" + Math.round(c[0]) + "," + Math.round(c[1]) + "," + Math.round(c[2]) + "," + a.toFixed(3) + ")";
        ctx.beginPath(); ctx.arc(x, y, 8.6 * s, 0, TAU); ctx.fill();
      }
    }
  }
"""

# ---------------------------------------------------------------- 08 cards -> shuffle
S08_CSS = """
.deck { position:absolute; left:212px; top:230px; width:380px; height:240px; }
.pc { position:absolute; left:0; top:0; width:380px; height:240px; border-radius:24px; overflow:hidden;
  box-shadow:0 22px 40px -16px rgba(18,21,50,0.45), 0 4px 10px rgba(18,21,50,0.12); }
.pc .chip { position:absolute; left:34px; top:40px; width:56px; height:42px; border-radius:9px; background:linear-gradient(135deg,#f4f7fc,#aab9d1 60%,#dfe7f3); }
.pc .n { position:absolute; left:34px; bottom:36px; font-size:32px; letter-spacing:0.12em; }
.pc.dk .n { color:#ffffff; }
.pc.dk .chip { opacity:0.85; }
"""
_cards = [
    ("c0", "linear-gradient(125deg,#7fd0ff,#4f86e8 55%,#274976)", "dk", "4242"),
    ("c1", "linear-gradient(140deg,#1d2550,#121532)", "dk", "1881"),
    ("c2", "linear-gradient(135deg,#8ea2ff,#6c86f0 60%,#4d63d6)", "dk", "5100"),
    ("c3", "linear-gradient(135deg,#ffffff,#eef3fb)", "lt", "3007"),
    ("c4", "linear-gradient(135deg,#dfe9f8,#b9cbe6 55%,#9fb6da)", "lt", "9424"),
]
S08_VIS = '        <div class="deck" id="deck">' + "".join(
    f'<div class="pc {k}" id="{i}" data-layout-allow-overlap data-layout-allow-overflow style="background:{bg}"><div class="chip"></div>'
    f'<div class="n {"g r" if k == "lt" else "r"}">&bull;&bull;&bull;&bull; {n}</div></div>'
    for i, bg, k, n in _cards) + "</div>"
S08_JS = """
  const N = 5;
  const cards = [0, 1, 2, 3, 4].map((i) => document.getElementById("c" + i));
  const io = (p) => { p = clamp(p, 0, 1); return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
  const T0 = 0.85, TD = 0.84;
  function render(t) {
    const F = t < 0.85 ? 1 - io((t - 0.3) / 0.55) : io((t - 5.2) / 0.65);
    const k = clamp(Math.floor((t - T0) / TD), -1, N);
    const done = clamp(k, 0, N);
    const p = (k >= 0 && k < N) ? clamp((t - T0 - k * TD) / TD, 0, 1) : 0;
    cards.forEach((el, i) => {
      let d = ((i - done) % N + N) % N;
      let x = 0, y = 0, r = 0, z = 0;
      if (k >= 0 && k < N && d === 0) {
        const e = io(p);
        x = 430 * Math.sin(Math.PI * e); y = -30 * Math.sin(Math.PI * e); r = 14 * Math.sin(Math.PI * e);
        d = e * (N - 1);
        z = p < 0.5 ? 50 : -1;
      } else if (k >= 0 && k < N) {
        d = d - io(p);
      }
      const fd = d - 2;
      const zi = z ? z : Math.round(40 - d * 5);
      x += d * 9 - fd * 66 * F;
      y += -d * 8 + Math.abs(fd) * 14 * F;
      r += -fd * 9 * F;
      gsap.set(el, { x: x, y: y, rotation: r, scale: 1 - d * 0.025, zIndex: zi });
    });
  }
"""

# ---------------------------------------------------------------- 14 words -> kinetic
S14_CSS = """
.panel.white { background:#ffffff; }
.kw { position:absolute; left:58px; top:104px; }
.ph { position:absolute; left:0; top:0; }
.ln { display:block; height:128px; overflow:hidden; }
.ln span { display:block; font-size:112px; line-height:128px; letter-spacing:-0.035em; white-space:nowrap; }
.kbar { position:absolute; left:60px; bottom:78px; width:260px; height:10px; border-radius:5px; background:linear-gradient(90deg,#121532,#4f86e8); transform-origin:0 50%; }
.kcount { position:absolute; right:60px; bottom:62px; font-size:34px; letter-spacing:0.12em; }
.kc { position:absolute; right:0; top:0; }
"""
S14_VIS = """        <div class="kw">
          <div class="ph" id="pa" data-layout-allow-overlap>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g b" id="a0">PAKAI</span></div>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g b" id="a1">AI</span></div>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g r" id="a2">SEKARANG.</span></div>
          </div>
          <div class="ph" id="pb" data-layout-allow-overlap>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g b" id="b0">SCALE</span></div>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g b" id="b1">LEBIH</span></div>
            <div class="ln" data-layout-allow-overflow data-layout-allow-overlap><span class="g r" id="b2">CEPAT.</span></div>
          </div>
        </div>
        <div class="kbar" id="kbar"></div>
        <div class="kcount g r" style="width:140px;height:44px"><span class="kc" id="k1">01/02</span><span class="kc" id="k2">02/02</span></div>"""
S14_JS = """
  function render(t) {
    const pa = (((t - 4.15) % D) + D) % D, pb = (((t - 1.15) % D) + D) % D;
    const inA = pa < 3, frac = inA ? pa / 3 : pb / 3;
    gsap.set("#kbar", { scaleX: clamp(frac * 1.05, 0.02, 1) });
    gsap.set("#k1", { opacity: inA ? 1 : 0 });
    gsap.set("#k2", { opacity: inA ? 0 : 1 });
  }
  const A = ["#a0", "#a1", "#a2"], B = ["#b0", "#b1", "#b2"];
  gsap.set(B, { yPercent: 110 });
  // A exits, B slams in
  tl.to(A, { yPercent: -110, duration: 0.24, ease: "power3.in", stagger: 0.04 }, 0.9);
  B.forEach((s, i) => tl.fromTo(s, { yPercent: 110 }, { yPercent: 0, duration: 0.42, ease: "back.out(1.6)", immediateRender: false }, 1.15 + i * 0.15));
  // B exits, A slams back in
  tl.to(B, { yPercent: -110, duration: 0.24, ease: "power3.in", stagger: 0.04 }, 3.9);
  A.forEach((s, i) => tl.fromTo(s, { yPercent: 110 }, { yPercent: 0, duration: 0.42, ease: "back.out(1.6)", immediateRender: false }, 4.15 + i * 0.15));
"""

# ---------------------------------------------------------------- 15 button -> pay
S15_CSS = """
.ctr { position:absolute; left:402px; top:330px; width:0; height:0; }
.btn, .paid { position:absolute; left:-260px; top:-64px; width:520px; height:128px; border-radius:64px; display:flex; align-items:center; justify-content:center; gap:20px;
  font-size:44px; color:#fff; letter-spacing:-0.01em; }
.btn { background:linear-gradient(180deg,#5b93f0,#274976); box-shadow:0 26px 50px -14px rgba(79,134,232,0.7), inset 0 2px 0 rgba(255,255,255,0.35); }
.paid { background:linear-gradient(180deg,#3fd3ab,#14896f); box-shadow:0 26px 50px -14px rgba(31,170,135,0.6), inset 0 2px 0 rgba(255,255,255,0.35); }
.spin { position:absolute; left:-70px; top:-70px; width:140px; height:140px; }
.okc { position:absolute; left:-70px; top:-70px; width:140px; height:140px; border-radius:50%; background:linear-gradient(180deg,#3fd3ab,#14896f); box-shadow:0 0 60px rgba(31,170,135,0.55); }
.ripple { position:absolute; left:-80px; top:-80px; width:160px; height:160px; border-radius:50%; border:4px solid rgba(31,170,135,0.7); }
.spk { position:absolute; left:-6px; top:-6px; width:12px; height:12px; border-radius:50%; }
.cursor { position:absolute; left:0; top:0; }
"""
_spk_cols = ["#4f86e8", "#7fd0ff", "#3fd3ab", "#274976", "#bcd8ff"]
_spk = "".join(f'<div class="spk" id="sp{i}" style="background:{_spk_cols[i % 5]}"></div>' for i in range(12))
_lock = '<svg width="34" height="40" viewBox="0 0 34 40"><rect x="3" y="17" width="28" height="21" rx="5" fill="#fff"/><path d="M9 17v-5a8 8 0 0 1 16 0v5" fill="none" stroke="#fff" stroke-width="4.5"/></svg>'
_tick = '<svg width="38" height="30" viewBox="0 0 38 30"><path d="M4 16l10 10L34 4" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
S15_VIS = f"""        <div class="ctr">
          <div class="ripple" id="ripple"></div>
          {_spk}
          <div class="paid b" id="paid">{_tick}<span>Lunas Rp480.000</span></div>
          <div class="okc" id="okc"></div>
          <svg class="spin" id="spin" viewBox="0 0 140 140">
            <defs><linearGradient id="spg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#7fd0ff"/><stop offset="1" stop-color="#274976"/></linearGradient></defs>
            <circle cx="70" cy="70" r="56" fill="#fff" stroke="#e3eaf5" stroke-width="10"/>
            <circle id="arc" cx="70" cy="70" r="56" fill="none" stroke="url(#spg)" stroke-width="10" stroke-linecap="round" stroke-dasharray="352" stroke-dashoffset="320" transform="rotate(-90 70 70)"/>
          </svg>
          <svg class="spin" id="tick" viewBox="0 0 140 140"><path id="tickp" d="M44 72l18 18 34-38" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="90" stroke-dashoffset="90"/></svg>
          <div class="btn b" id="btn">{_lock}<span>Bayar Rp480.000</span></div>
          <svg class="cursor" id="cur" width="44" height="52" viewBox="0 0 44 52"><path d="M4 3l0 38 10-9 7 16 7-3-7-15 14-1z" fill="#121532" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></svg>
        </div>"""
S15_JS = """
  function render(t) {
    const glow = 0.5 + 0.5 * Math.sin(TAU * t / 1.5);
    document.getElementById("btn").style.boxShadow = "0 26px " + (44 + 16 * glow).toFixed(1) + "px -14px rgba(79,134,232," + (0.55 + 0.25 * glow).toFixed(3) + "), inset 0 2px 0 rgba(255,255,255,0.35)";
    const sp = clamp((t - 1.85) / 1.15, 0, 1);
    gsap.set("#spin", { rotation: 360 * 1.3 * sp });
    document.getElementById("arc").setAttribute("stroke-dashoffset", (320 - 320 * (sp * sp * (3 - 2 * sp))).toFixed(1));
  }
  gsap.set(["#spin", "#okc", "#tick", "#paid", "#ripple"], { opacity: 0, scale: 0.5 });
  gsap.set(".spk", { opacity: 0 });
  gsap.set("#cur", { x: 260, y: 230, opacity: 0 });
  // pointer drifts in, button leans toward it
  tl.to("#cur", { opacity: 1, duration: 0.25 }, 0.25);
  tl.to("#cur", { x: 60, y: 22, duration: 1.0, ease: "power2.inOut" }, 0.25);
  tl.to("#btn", { x: 12, y: 6, rotation: 2.2, duration: 0.5, ease: "power2.out" }, 0.8);
  // press
  tl.to("#btn", { scale: 0.93, duration: 0.12, ease: "power2.in" }, 1.3);
  tl.to("#cur", { scale: 0.85, duration: 0.12 }, 1.3);
  // shrink to spinner
  tl.to("#btn", { scaleX: 0.28, scaleY: 0.9, opacity: 0, x: 0, y: 0, rotation: 0, duration: 0.38, ease: "power3.in" }, 1.45);
  tl.to("#cur", { opacity: 0, y: 70, duration: 0.3 }, 1.5);
  tl.to("#spin", { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }, 1.68);
  // success
  tl.to("#spin", { opacity: 0, duration: 0.15 }, 3.0);
  tl.to("#okc", { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2.4)" }, 3.0);
  tl.to("#tick", { opacity: 1, scale: 1, duration: 0.01 }, 3.05);
  tl.to("#tickp", { attr: { "stroke-dashoffset": 0 }, duration: 0.32, ease: "power2.out" }, 3.08);
  tl.fromTo("#ripple", { opacity: 0.9, scale: 0.8 }, { opacity: 0, scale: 2.4, duration: 0.8, ease: "power2.out", immediateRender: false }, 3.1);
  for (let i = 0; i < 12; i++) {
    const a = TAU * i / 12 + 0.2, rr = 115 + (i % 3) * 22;
    tl.fromTo("#sp" + i, { x: 0, y: 0, opacity: 1, scale: 1 }, { x: rr * Math.cos(a), y: rr * Math.sin(a), opacity: 0, scale: 0.4, duration: 0.65, ease: "power2.out", immediateRender: false }, 3.12);
  }
  // grow back as paid
  tl.to(["#okc", "#tick"], { opacity: 0, scale: 0.8, duration: 0.2 }, 3.85);
  tl.to("#paid", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }, 3.9);
  // reset to pay for the loop
  tl.to("#paid", { opacity: 0, scale: 0.92, duration: 0.3, ease: "power2.in" }, 5.3);
  tl.fromTo("#btn", { opacity: 0, scale: 0.9, scaleX: 0.9 }, { opacity: 1, scale: 1, scaleX: 1, scaleY: 1, duration: 0.4, ease: "back.out(1.7)", immediateRender: false }, 5.5);
  tl.set("#cur", { x: 260, y: 230, scale: 1 }, 5.6);
  tl.set("#tickp", { attr: { "stroke-dashoffset": 90 } }, 5.6);
"""

# ---------------------------------------------------------------- 16 confetti -> burst
S16_CSS = CV_CSS + """
.cbtn { position:absolute; left:302px; top:170px; width:200px; height:200px; border-radius:50%;
  background:linear-gradient(135deg,#7fd0ff,#4f86e8 50%,#274976); display:flex; align-items:center; justify-content:center;
  box-shadow:0 30px 60px -18px rgba(79,134,232,0.75), inset 0 3px 0 rgba(255,255,255,0.35); z-index:2; }
.clive { position:absolute; left:0; right:0; top:418px; text-align:center; font-size:48px; letter-spacing:-0.01em; z-index:2; }
"""
S16_VIS = CANVAS + """
        <div class="cbtn" id="cbtn"><svg width="86" height="66" viewBox="0 0 86 66"><path d="M8 34l22 22L78 8" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div class="clive"><span class="g r" id="clive">Kamu udah live</span></div>"""
S16_JS = CV_JS_HEAD + """
  let seed = 23;
  const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const COLS = ["#121532", "#274976", "#4f86e8", "#7fd0ff", "#bcd8ff", "#6c86f0", "#3a78e6"];
  const PER = 3, POP = 0.5, BX = 402, BY = 270, K = 2.1, G = 1150;
  const C = [...Array(72)].map(() => {
    const a = -Math.PI / 2 + (rnd() - 0.5) * 3.0, v = 440 + rnd() * 560;
    return { vx: Math.cos(a) * v, vy: Math.sin(a) * v, c: COLS[Math.floor(rnd() * COLS.length)], w: 13 + rnd() * 12, h: 7 + rnd() * 7,
      circ: rnd() < 0.3, sp: (rnd() - 0.5) * 16, r0: rnd() * TAU, fl: rnd() * TAU, d: rnd() * 0.06 };
  });
  function drawBurst(tau) {
    if (tau < 0) return;
    for (const p of C) {
      const tt = tau - p.d;
      if (tt < 0) continue;
      const e = 1 - Math.exp(-K * tt);
      const x = BX + p.vx / K * e + 18 * Math.sin(p.fl + tt * 7) * Math.min(1, tt * 2);
      const y = BY + (p.vy - G / K) / K * e + G / K * tt;
      if (y > H + 30) continue;
      const fade = clamp(1.4 - tt / 1.8, 0, 1);
      ctx.save(); ctx.translate(x, y); ctx.rotate(p.r0 + p.sp * tt);
      ctx.globalAlpha = fade; ctx.fillStyle = p.c;
      if (p.circ) { ctx.beginPath(); ctx.arc(0, 0, p.h * 0.75, 0, TAU); ctx.fill(); }
      else { ctx.scale(1, Math.abs(Math.cos(p.fl + tt * 9)) * 0.8 + 0.2); ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h); }
      ctx.restore();
    }
  }
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const tp = t % PER;
    drawBurst(tp - POP);
    drawBurst(tp + PER - POP);
    const sq = tp < POP ? smooth((tp - 0.2) / 0.3) : 0;
    const pop = tp >= POP ? Math.exp(-6 * (tp - POP)) * Math.sin(Math.min(Math.PI, (tp - POP) * 9)) : 0;
    gsap.set("#cbtn", { scale: 1 - 0.1 * sq + 0.16 * pop });
    gsap.set("#clive", { opacity: 1 - 0.45 * sq });
  }
"""

SLIDES_B = [
    dict(cid="s07", num="07", page="08", name="Grid wave", w1="Grid", w2="wave",
         sub="Hamparan titik yang bergelombang kayak laut", panel="light", css=CV_CSS, visual=CANVAS, js=S07_JS,
         body="Permukaan 3D dari titik-titik kecil bergelombang kayak laut tenang di atas putih. Warnanya ikut tinggi gelombang: navy di lembah, biru muda di puncak.",
         used=""),
    dict(cid="s08", num="08", page="09", name="Cards shuffle", w1="Cards", w2="shuffle",
         sub="Kartu yang dikocok", panel="light", css=S08_CSS, visual=S08_VIS, js=S08_JS,
         body="Tumpukan lima kartu pembayaran (desain original, tanpa logo, cuma 4 digit terakhir) terbuka kayak kipas, menutup, lalu kartu teratas meluncur keluar dan masuk ke bawah tumpukan, terus berulang.",
         used=""),
    dict(cid="s14", num="14", page="15", name="Words kinetic", w1="Words", w2="kinetic",
         sub="Kata-kata yang menghantam masuk", panel="white", css=S14_CSS, visual=S14_VIS, js=S14_JS,
         body='<b class="b">&ldquo;[BARIS 1] [BARIS 2] [BARIS 3].&rdquo;</b> masuk baris per baris dengan huruf tebal, keluar ke atas, lalu <b class="b">&ldquo;[kalimat kedua]&rdquo;</b> melakukan hal yang sama. Counter kecil &ldquo;01/02&rdquo; di pojok.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> &ldquo;PAKAI AI SEKARANG.&rdquo; lalu &ldquo;SCALE LEBIH CEPAT.&rdquo;</div>'),
    dict(cid="s15", num="15", page="16", name="Button pay", w1="Button", w2="pay",
         sub="Tombol bayar yang diklik sampai Lunas", panel="light", css=S15_CSS, visual=S15_VIS, js=S15_JS,
         body='Tombol &ldquo;Bayar <b class="b">[nominal kamu]</b>&rdquo; dengan ikon gembok. Kursor mendekat, tombol ditekan, menyusut jadi spinner, centang muncul dengan percikan kecil, lalu tumbuh jadi &ldquo;Lunas <b class="b">[nominal kamu]</b>&rdquo;.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> Rp480.000.</div>'),
    dict(cid="s16", num="16", page="17", name="Confetti burst", w1="Confetti", w2="burst",
         sub="Centang yang meledak jadi confetti", panel="light", css=S16_CSS, visual=S16_VIS, js=S16_JS,
         body='Tombol bulat gradasi dengan centang putih. Tombolnya pop, sekitar 70 confetti meledak keluar, berkibar lalu jatuh, dan <b class="b">&ldquo;[kata-kata kamu]&rdquo;</b> ada di bawahnya.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> &ldquo;Kamu udah live&rdquo;.</div>'),
]
