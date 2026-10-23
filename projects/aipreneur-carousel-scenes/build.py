"""Builds the carousel slides (slides/sNN/index.html) from one shared shell.
Edit copy here, then run: python3 build.py"""
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

SHELL = """<!doctype html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1350" />
<title>AIpreneur — {name}</title>
<script src="vendor/gsap/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/shared.css" />
<style>
{css}
</style>
</head>
<body>
<div id="root" data-composition-id="{cid}" data-start="0" data-duration="6" data-width="1080" data-height="1350" data-fps="30">
  <div id="stage" class="clip" data-start="0" data-duration="6" data-track-index="0" data-track-kind="graphics" style="position:absolute;inset:0">
    <div class="bg"></div>
    <div class="logo" id="logo"></div>
    <div class="eyebrow g b" id="eyebrow">SCENE · {num} DARI 16</div>
    <div class="title" id="title"><span class="g b">{w1}</span><svg class="arrow" width="78" height="52" viewBox="0 0 78 52"><defs><linearGradient id="ag" x1="0" x2="1"><stop offset="0" stop-color="#121532"/><stop offset="1" stop-color="#274976"/></linearGradient></defs><path d="M4 26H70M48 6l22 20-22 20" fill="none" stroke="url(#ag)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" opacity="0.5"/></svg><span class="g r">{w2}</span></div>
    <div class="sub g r" id="sub">{sub}</div>
    <div class="card" id="card">
      <div class="panel {panel}" id="panel">
{visual}
      </div>
    </div>
    <div class="swap" id="swap">
      <div class="lbl g b">GANTI DI SCENE INI</div>
      <div class="txt g r">{body}</div>{used}
    </div>
    <div class="foot" id="foot">
      <div class="who"><div class="dot">FK</div><span class="g b">FREDDIE KASHAWAN</span><span class="g r">AIpreneur</span></div>
      <div class="pg g b">{page} / 18 &nbsp;&nbsp; GESER &rarr;</div>
    </div>
  </div>
</div>
<script>
(function () {{
  const D = 6, TAU = Math.PI * 2;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const smooth = (p) => {{ p = clamp(p, 0, 1); return p * p * (3 - 2 * p); }};
  const tl = gsap.timeline({{ paused: true }});
  const st = {{ t: 0 }};
{js}
  tl.to(st, {{ t: D, duration: D, ease: "none", onUpdate: () => render(st.t) }}, 0);
  render(0);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["{cid}"] = tl;
}})();
</script>
</body>
</html>
"""

# ---------------------------------------------------------------- 09 number roll
S09_CSS = """
.lab { position:absolute; left:70px; top:66px; font-size:36px; display:flex; align-items:center; gap:18px; }
.live { width:16px; height:16px; border-radius:50%; background:#4f86e8; box-shadow:0 0 0 6px rgba(79,134,232,0.18); }
.num { position:absolute; left:66px; top:124px; height:120px; display:flex; font-size:88px; line-height:120px; letter-spacing:-0.02em; }
.num .s { display:block; height:120px; }
.dg { display:block; height:120px; overflow:hidden; width:0.62em; text-align:center; }
.col { display:block; will-change:transform; }
.col span { display:block; height:120px; }
.sep { width:0.26em; text-align:center; }
.cur { margin-right:0.18em; }
.chip { position:absolute; left:70px; top:272px; padding:12px 26px; border-radius:16px; background:rgba(79,134,232,0.14); font-size:30px; }
.bars { position:absolute; left:70px; right:70px; bottom:62px; height:240px; display:flex; align-items:flex-end; gap:16px; }
.bar { flex:1; border-radius:9px 9px 4px 4px; transform-origin:50% 100%; }
"""
_bar_h = [70, 98, 84, 128, 116, 160, 146, 188, 176, 216, 206, 236]
_bar_html = "".join(
    f'<div class="bar" id="bar{i}" style="height:{h}px;background:{"linear-gradient(180deg,#8fb4ec,#4f86e8 45%,#274976)" if i == 11 else f"rgba(79,134,232,{0.16 + i * 0.035:.3f})"}"></div>'
    for i, h in enumerate(_bar_h)
)
_digits = "".join(f"<span class='g'>{d}</span>" for d in "01234567890")
_num = '<span class="s cur g r">Rp</span>'
for k in range(9):  # 9 digits, most significant first
    _num += f'<span class="dg" data-layout-allow-overflow data-layout-allow-overlap><span class="col" id="d{8 - k}">{_digits}</span></span>'
    if k in (2, 5):
        _num += '<span class="s sep g r">.</span>'
S09_VIS = f"""        <div class="lab"><span class="g r">Pendapatan tahun ini</span><span class="live" id="live"></span></div>
        <div class="num r" id="num">{_num}</div>
        <div class="chip" id="chip"><span class="g b">+24% year on year</span></div>
        <div class="bars" id="bars">{_bar_html}</div>"""
S09_JS = """
  const B0 = 128497300, STEP = 0.32, ROLL = 0.18, INC = 7;
  const tick = (dt) => INC * (Math.floor(dt / STEP) + smooth((dt % STEP) / ROLL));
  const vA = B0 + tick(3.6);
  function val(t) {
    if (t < 1.9) return B0 + tick(t + 1.7);
    if (t < 2.5) { const p = (t - 1.9) / 0.6; return vA * (1 - p * p * p); }
    if (t < 4.3) { const p = (t - 2.5) / 1.8; return B0 * (1 - Math.pow(1 - p, 4)); }
    return B0 + tick(t - 4.3);
  }
  const cols = [...Array(9)].map((_, k) => document.getElementById("d" + k));
  function digitPos(v, k) {
    const p = Math.pow(10, k), q = Math.floor(v / p);
    const carry = clamp((v % p) - (p - 1), 0, 1);
    return k === 0 ? (v % 10) : (q % 10) + carry;
  }
  function render(t) {
    const v = val(t), v0 = val(Math.max(0, t - 1 / 30));
    const speed = Math.abs(v - v0) * 30;
    for (let k = 0; k < 9; k++) {
      const pos = digitPos(v, k);
      const blur = clamp(speed / Math.pow(10, k) / 18, 0, 9);
      cols[k].style.transform = "translateY(" + (-pos * 120).toFixed(2) + "px)";
      cols[k].style.filter = blur > 0.3 ? "blur(" + blur.toFixed(2) + "px)" : "none";
    }
    const pulse = 0.5 + 0.5 * Math.sin(TAU * t / 1.5);
    document.getElementById("live").style.boxShadow = "0 0 0 " + (4 + 6 * pulse).toFixed(1) + "px rgba(79,134,232," + (0.28 - 0.18 * pulse).toFixed(3) + ")";
  }
  const bars = gsap.utils.toArray(".bar");
  tl.to("#chip", { opacity: 0, y: 8, duration: 0.25, ease: "power2.in" }, 1.75);
  tl.to(bars, { scaleY: 0.04, duration: 0.5, ease: "power3.in", stagger: { each: 0.015, from: "end" } }, 1.9);
  tl.to(bars, { scaleY: 1, duration: 0.9, ease: "power3.out", stagger: 0.07 }, 2.55);
  tl.fromTo("#chip", { opacity: 0, y: 14, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(2)", immediateRender: false }, 4.1);
"""

# ---------------------------------------------------------------- 10 ribbon twist
S10_CSS = "#cv { position:absolute; inset:0; }"
S10_VIS = '        <canvas id="cv" width="1608" height="1404" style="width:804px;height:702px"></canvas>'
S10_JS = """
  const cv = document.getElementById("cv"), ctx = cv.getContext("2d");
  const W = 804, H = 702, N = 26;
  const stops = [[0, [127, 208, 255]], [0.5, [79, 134, 232]], [1, [214, 228, 255]]];
  function col(u) {
    u = clamp(u, 0, 1);
    const i = u < 0.5 ? 0 : 1, a = stops[i], b = stops[i + 1], p = (u - a[0]) / (b[0] - a[0]);
    return a[1].map((c, j) => c + (b[1][j] - c) * p);
  }
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.globalCompositeOperation = "lighter";
    ctx.lineWidth = 1.5; ctx.lineCap = "round";
    const ph = TAU * t / D;
    for (let i = 0; i < N; i++) {
      const s = -1 + 2 * i / (N - 1);
      let px = null, py = 0;
      for (let x = -24; x <= W + 24; x += 5) {
        const u = x / W;
        const cy = H * 0.5 + 118 * Math.sin(TAU * u * 1.05 - ph);
        const th = TAU * u * 0.85 + ph;
        const amp = 104 * (0.7 + 0.3 * Math.sin(Math.PI * clamp(u, 0, 1)));
        const y = cy + s * amp * Math.cos(th);
        if (px !== null) {
          const front = Math.cos(th) >= 0;
          const c = col(u), lit = front ? 1 : 0.55;
          const edge = 0.55 + 0.45 * Math.abs(Math.sin(th));
          ctx.strokeStyle = "rgba(" + (c[0] * lit) + "," + (c[1] * lit) + "," + (c[2] * (front ? 1 : 0.8)) + "," + (0.5 * edge + 0.24).toFixed(3) + ")";
          ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(x, y); ctx.stroke();
        }
        px = x; py = y;
      }
    }
    ctx.globalCompositeOperation = "source-over";
  }
"""

# ---------------------------------------------------------------- 11 liquid merge
S11_CSS = "#sv { position:absolute; inset:0; }"
S11_VIS = """        <svg id="sv" width="804" height="702" viewBox="0 0 804 702">
          <defs>
            <filter id="goo" x="-30%" y="-30%" width="160%" height="160%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="16" result="b" />
              <feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 30 -13" />
            </filter>
            <radialGradient id="metal" cx="34%" cy="30%" r="78%">
              <stop offset="0" stop-color="#d4e4ff" />
              <stop offset="0.28" stop-color="#6f9ff0" />
              <stop offset="0.62" stop-color="#274976" />
              <stop offset="1" stop-color="#121532" />
            </radialGradient>
            <radialGradient id="hl"><stop offset="0" stop-color="#fff" stop-opacity="0.95" /><stop offset="1" stop-color="#fff" stop-opacity="0" /></radialGradient>
            <radialGradient id="rim"><stop offset="0" stop-color="#9cc2ff" stop-opacity="0.55" /><stop offset="1" stop-color="#9cc2ff" stop-opacity="0" /></radialGradient>
            <radialGradient id="shg"><stop offset="0" stop-color="#121532" stop-opacity="0.32" /><stop offset="1" stop-color="#121532" stop-opacity="0" /></radialGradient>
            <filter id="soft"><feGaussianBlur stdDeviation="6" /></filter>
          </defs>
          <ellipse id="shd" cx="402" cy="590" rx="200" ry="30" fill="url(#shg)" />
          <g filter="url(#goo)">
            <ellipse id="b1" fill="url(#metal)" />
            <ellipse id="b2" fill="url(#metal)" />
            <ellipse id="b0" fill="url(#metal)" />
          </g>
          <g filter="url(#soft)">
            <ellipse id="r0" fill="url(#rim)" /><ellipse id="r1" fill="url(#rim)" /><ellipse id="r2" fill="url(#rim)" />
            <ellipse id="h0" fill="url(#hl)" /><ellipse id="h1" fill="url(#hl)" /><ellipse id="h2" fill="url(#hl)" />
          </g>
        </svg>"""
S11_JS = """
  const drops = [
    { r: 118, ox: 40, oy: 0 },
    { r: 78, ox: -120, oy: -48 },
    { r: 54, ox: -96, oy: 92 },
  ];
  const $ = (id) => document.getElementById(id);
  const set = (el, o) => { for (const k in o) el.setAttribute(k, typeof o[k] === "number" ? o[k].toFixed(2) : o[k]); };
  function merged(t) {
    const tt = t < 0.4 ? t + D : t;
    if (tt < 1.6) return smooth((tt - 0.4) / 1.2);
    if (tt < 3.8) return 1;
    return 1 - smooth((tt - 3.8) / 2.6);
  }
  function render(t) {
    const m = merged(t), spread = 1 - m;
    const ang = 0.45 * Math.sin(TAU * t / D);
    const cx = 402, cy = 300 + 9 * Math.sin(TAU * t / 3);
    const wob = m * 0.045 * Math.sin(TAU * t / 1.2);
    drops.forEach((d, i) => {
      const k = 1 + 0.55 * spread * spread * (i ? 1 : 0);
      const ox = d.ox * spread * k, oy = d.oy * spread * k;
      const x = cx + ox * Math.cos(ang) - oy * Math.sin(ang);
      const y = cy + ox * Math.sin(ang) + oy * Math.cos(ang);
      const r = i === 0 ? d.r + 34 * m : d.r * (1 - 0.35 * m);
      const rx = r * (1 + wob), ry = r * (1 - wob);
      set($("b" + i), { cx: x, cy: y, rx: rx, ry: ry });
      const vis = i === 0 ? 1 : spread;
      set($("h" + i), { cx: x - 0.36 * r, cy: y - 0.42 * r, rx: 0.34 * r, ry: 0.2 * r, transform: "rotate(-32 " + (x - 0.36 * r).toFixed(1) + " " + (y - 0.42 * r).toFixed(1) + ")", opacity: vis });
      set($("r" + i), { cx: x + 0.3 * r, cy: y + 0.48 * r, rx: 0.5 * r, ry: 0.2 * r, opacity: 0.8 * vis });
    });
    set($("shd"), { cx: cx - 10 * spread, cy: 560, rx: 175 + 70 * spread, ry: 26 + 4 * spread, opacity: 0.85 + 0.15 * m });
  }
"""

# ---------------------------------------------------------------- 12 phone explode
S12_CSS = """
.shadow { position:absolute; left:262px; top:540px; width:280px; height:60px; border-radius:50%;
  background:radial-gradient(ellipse, rgba(18,21,50,0.30), rgba(18,21,50,0) 70%); }
.f2d { position:absolute; left:262px; top:150px; width:280px; height:380px; }
.iso { position:absolute; left:10px; top:-60px; width:260px; height:460px; transform-style:preserve-3d; transform:rotateX(57deg) rotateZ(-40deg); }
.L { position:absolute; inset:0; transform-style:preserve-3d; }
.body, .thick { position:absolute; inset:0; border-radius:40px; background:linear-gradient(160deg,#274976,#121532); }
.screen { position:absolute; inset:12px; border-radius:30px; background:#fbfcff; box-shadow:inset 0 0 0 2px rgba(39,73,118,0.08); }
.hdr { position:absolute; left:26px; right:26px; top:40px; height:120px; border-radius:20px; background:linear-gradient(120deg,#8fd0ff,#4f86e8 55%,#274976); filter:blur(3px); }
.lines { position:absolute; left:30px; right:30px; top:190px; }
.lines i { display:block; height:16px; border-radius:8px; background:#d6e0ee; margin-bottom:18px; }
.cards { position:absolute; left:24px; right:24px; top:180px; height:140px; border-radius:18px; background:linear-gradient(160deg,#274976,#121532); }
.cards i { position:absolute; top:22px; width:70px; height:96px; border-radius:12px; background:rgba(143,180,236,0.35); }
.btn { position:absolute; left:50px; right:50px; bottom:56px; height:56px; border-radius:28px; background:linear-gradient(90deg,#4f86e8,#8fb4ec); filter:blur(1.5px); }
"""
_thick = "".join(f'<div class="thick" style="transform:translateZ(-{k * 3}px)"></div>' for k in range(1, 7))
S12_VIS = f"""        <div class="shadow" id="shadow"></div>
        <div class="f2d" id="f2d">
          <div class="iso" data-layout-allow-overflow>
            <div class="L" id="L0">{_thick}<div class="body"></div></div>
            <div class="L" id="L1"><div class="cards"><i style="left:22px"></i><i style="left:112px"></i><i style="left:202px;width:48px"></i></div></div>
            <div class="L" id="L2"><div class="screen"></div></div>
            <div class="L" id="L3"><div class="hdr"></div><div class="lines"><i></i><i style="width:80%"></i><i style="width:60%"></i></div></div>
            <div class="L" id="L4"><div class="btn"></div></div>
          </div>
        </div>"""
S12_JS = """
  const L = [0, 1, 2, 3, 4].map((i) => document.getElementById("L" + i));
  const GAP = [0, 64, 118, 176, 236];
  const BASE = [0, 1, 2, 4, 6];
  function ex(t) {
    if (t < 1.5) return 0;
    if (t < 2.5) { const p = (t - 1.5) / 1.0; return 1 - Math.pow(1 - p, 3); }
    if (t < 4.5) return 1;
    if (t < 4.95) { const p = (t - 4.5) / 0.45; return 1 - p * p * p; }
    if (t < 5.5) { const p = (t - 4.95) / 0.55; return 0.06 * Math.sin(Math.PI * p) * (1 - p); }
    return 0;
  }
  function render(t) {
    const e = ex(t);
    const hold = (t > 2.5 && t < 4.5) ? Math.sin(Math.PI * (t - 2.5) / 2) : 0;
    L.forEach((el, i) => {
      const z = BASE[i] + GAP[i] * e + (i ? 10 * hold * Math.sin(TAU * (t / 2) + i * 0.9) * 0.5 : 0);
      gsap.set(el, { z: z });
    });
    const bob = 10 * Math.sin(TAU * t / 3);
    gsap.set("#f2d", { y: bob + 110 * e });
    gsap.set("#shadow", { scaleX: 1 - 0.12 * e + 0.03 * Math.sin(TAU * t / 3), opacity: 0.9 - 0.3 * e });
  }
"""

# ---------------------------------------------------------------- 13 rings orbit
S13_CSS = "#cv { position:absolute; inset:0; }"
S13_VIS = S10_VIS
S13_JS = """
  const cv = document.getElementById("cv"), ctx = cv.getContext("2d");
  const W = 804, H = 702, CX = 402, CY = 344, ROT = -0.24, RY = 0.3;
  const rings = [205, 272, 338];
  const moons = [
    { ring: 0, n: 3, a0: 0.4, r: 11, c: [143, 180, 236] },
    { ring: 1, n: 2, a0: 2.2, r: 14, c: [214, 228, 255] },
    { ring: 1, n: 2, a0: 5.3, r: 9, c: [79, 134, 232] },
    { ring: 2, n: 1, a0: 4.1, r: 17, c: [127, 208, 255] },
  ];
  function pos(ring, a) {
    const lx = rings[ring] * Math.cos(a), ly = rings[ring] * RY * Math.sin(a);
    return [CX + lx * Math.cos(ROT) - ly * Math.sin(ROT), CY + lx * Math.sin(ROT) + ly * Math.cos(ROT), Math.sin(a)];
  }
  function ringHalf(front) {
    ctx.lineWidth = 2;
    rings.forEach((r) => {
      ctx.strokeStyle = front ? "rgba(214,228,255,0.42)" : "rgba(214,228,255,0.22)";
      ctx.beginPath(); ctx.ellipse(CX, CY, r, r * RY, ROT, front ? 0 : Math.PI, front ? Math.PI : TAU); ctx.stroke();
    });
  }
  function moon(m, t, front) {
    const a = m.a0 + TAU * m.n * t / D;
    const p = pos(m.ring, a);
    if ((p[2] >= 0) !== front) return;
    const s = m.r * (0.82 + 0.18 * p[2]);
    const g = ctx.createRadialGradient(p[0] - s * 0.35, p[1] - s * 0.35, s * 0.1, p[0], p[1], s * 2.4);
    const c = m.c.join(",");
    g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.3, "rgba(" + c + ",1)"); g.addColorStop(0.42, "rgba(" + c + ",0.35)"); g.addColorStop(1, "rgba(" + c + ",0)");
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p[0], p[1], s * 2.4, 0, TAU); ctx.fill();
  }
  function core(t) {
    const pulse = 1 + 0.03 * Math.sin(TAU * t / 3);
    let g = ctx.createRadialGradient(CX, CY, 0, CX, CY, 230 * pulse);
    g.addColorStop(0, "rgba(143,180,236,0.45)"); g.addColorStop(1, "rgba(143,180,236,0)");
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(CX, CY, 230 * pulse, 0, TAU); ctx.fill();
    const R = 78 * pulse;
    g = ctx.createRadialGradient(CX - R * 0.35, CY - R * 0.4, R * 0.05, CX, CY, R);
    g.addColorStop(0, "#ffffff"); g.addColorStop(0.35, "#bcd6ff"); g.addColorStop(0.75, "#4f86e8"); g.addColorStop(1, "#2b5cb8");
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(CX, CY, R, 0, TAU); ctx.fill();
  }
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ringHalf(false);
    moons.forEach((m) => moon(m, t, false));
    core(t);
    ringHalf(true);
    moons.forEach((m) => moon(m, t, true));
  }
"""

SLIDES = [
    dict(file="slide-09.html", cid="s09", num="09", page="10", name="Number roll", w1="Number", w2="roll",
         sub="Angka yang naik terus, nggak berhenti", panel="light", css=S09_CSS, visual=S09_VIS, js=S09_JS,
         body='Kartu revenue <b class="b">&ldquo;[label kamu]&rdquo;</b>. Angka <b class="b">&ldquo;[angka kamu]&rdquo;</b> naik dari nol kayak odometer, dengan motion blur di digit yang cepat, lalu terus bertambah live. Chip <b class="b">&ldquo;[+x% year on year]&rdquo;</b> dan deretan bar kecil di bawahnya.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> Pendapatan tahun ini, Rp128.497.300, +24% year on year.</div>'),
    dict(file="slide-10.html", cid="s10", num="10", page="11", name="Ribbon twist", w1="Ribbon", w2="twist",
         sub="Pita sutra yang berputar", panel="dark", css=S10_CSS, visual=S10_VIS, js=S10_JS,
         body="Pita sutra dari sekitar 26 helai gradasi tipis yang berputar di ruang 3D di atas navy gelap, dengan cahaya berbeda di sisi depan dan belakang.", used=""),
    dict(file="slide-11.html", cid="s11", num="11", page="12", name="Liquid merge", w1="Liquid", w2="merge",
         sub="Logam cair yang menyatu", panel="light", css=S11_CSS, visual=S11_VIS, js=S11_JS,
         body="Tetesan logam cair glossy warna biru, disinari dari kiri atas. Mereka melayang, menyatu jadi satu tetesan, lalu pecah lagi. Bayangan halus di bawahnya.", used=""),
    dict(file="slide-12.html", cid="s12", num="12", page="13", name="Phone explode", w1="Phone", w2="explode",
         sub="HP yang terurai jadi layer", panel="light", css=S12_CSS, visual=S12_VIS, js=S12_JS,
         body="HP isometrik terpecah jadi layer-layernya (layar, kartu, tombol). Layer melayang di udara, lalu nyatu lagi dengan cepat. Bayangan halus di bawahnya.", used=""),
    dict(file="slide-13.html", cid="s13", num="13", page="14", name="Rings orbit", w1="Rings", w2="orbit",
         sub="Cincin yang mengorbit", panel="dark", css=S13_CSS, visual=S13_VIS, js=S13_JS,
         body="Inti biru bercahaya di atas navy gelap dengan tiga orbit miring. Bulan-bulan kecil lewat di depan dan di belakang inti.", used=""),
]

from scenes_a import SLIDES_A
SLIDES = SLIDES_A + SLIDES

for s in SLIDES:
    if s["used"]:
        s["used"] = "\n      " + s["used"]
    d = ROOT / "slides" / s["cid"]
    d.mkdir(parents=True, exist_ok=True)
    for sub in ("assets", "vendor"):
        if (d / sub).exists():
            shutil.rmtree(d / sub)
        shutil.copytree(ROOT / sub, d / sub)
    (d / "index.html").write_text(SHELL.format(**s))
    print("wrote", d / "index.html")
