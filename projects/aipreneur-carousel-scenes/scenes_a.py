"""Scenes 01, 02, 03, 04, 06 — imported by build.py."""
import json
from pathlib import Path

HERE = Path(__file__).parent
LOGO_PTS = (HERE / "logo_points.json").read_text()
GLOBE_DOTS = (HERE / "globe_dots.json").read_text()

CANVAS = '        <canvas id="cv" width="1608" height="1404" style="width:804px;height:702px"></canvas>'
CV_CSS = "#cv { position:absolute; inset:0; }"
CV_JS_HEAD = """
  const cv = document.getElementById("cv"), ctx = cv.getContext("2d");
  const W = 804, H = 702;
  const mix = (a, b, p) => a + (b - a) * p;
  const STOPS = [[0, [127, 208, 255]], [0.5, [79, 134, 232]], [1, [214, 228, 255]]];
  function col(u) {
    u = clamp(u, 0, 1);
    const i = u < 0.5 ? 0 : 1, a = STOPS[i], b = STOPS[i + 1], p = (u - a[0]) / (b[0] - a[0]);
    return a[1].map((c, j) => Math.round(c + (b[1][j] - c) * p));
  }
"""

# ---------------------------------------------------------------- 01 particles -> logo
S01_JS = CV_JS_HEAD + """
  const PTS = """ + LOGO_PTS + """;
  let seed = 11;
  const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const CX = 402, CY = 351;
  const P = PTS.map(([x, y]) => ({ tx: CX + x * 0.86, ty: CY + y * 0.86, a: rnd() * TAU, rr: 290 + rnd() * 80,
    ph: rnd() * TAU, sz: 2.6 + rnd() * 2.2, d: rnd(), u: clamp((x * 0.86 + 230) / 460, 0, 1) }));
  const outC = (p) => 1 - Math.pow(1 - clamp(p, 0, 1), 3);
  const inOut = (p) => { p = clamp(p, 0, 1); return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const glow = ctx.createRadialGradient(CX, CY, 0, CX, CY, 330);
    glow.addColorStop(0, "rgba(79,134,232,0.30)"); glow.addColorStop(1, "rgba(79,134,232,0)");
    ctx.fillStyle = glow; ctx.fillRect(0, 0, W, H);
    const wave = (t - 0.9) / 0.9 * 1.5 - 0.25;
    for (const p of P) {
      const b = outC((t - 2.4 - 0.15 * p.d) / 0.9);
      const h = inOut((t - 4.15 - 0.3 * p.d) / 1.05);
      const ang = p.a + 0.22 * Math.max(0, t - 2.4);
      const rad = p.rr + 14 * Math.sin(p.ph + 2 * t);
      const rx = CX + rad * Math.cos(ang), ry = CY + rad * 0.9 * Math.sin(ang);
      const jx = 1.6 * Math.sin(p.ph + t * 3.1), jy = 1.6 * Math.cos(p.ph * 1.3 + t * 2.7);
      let x = mix(p.tx + jx, rx, b), y = mix(p.ty + jy, ry, b);
      const swirl = Math.sin(Math.PI * h) * 46;
      x = mix(x, p.tx + jx, h) - swirl * Math.sin(ang);
      y = mix(y, p.ty + jy, h) + swirl * Math.cos(ang);
      const away = b * (1 - h);
      const sh = (t > 0.8 && t < 2.1) ? Math.exp(-Math.pow(p.u - wave, 2) / 0.012) : 0;
      const c = col(p.u);
      const r = p.sz * (1 - 0.25 * away) * (1 + 0.35 * sh);
      const lift = sh * 0.6;
      ctx.fillStyle = "rgba(" + Math.round(mix(c[0], 255, lift)) + "," + Math.round(mix(c[1], 255, lift)) + "," + Math.round(mix(c[2], 255, lift)) + "," + (0.92 - 0.25 * away).toFixed(3) + ")";
      ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
    }
  }
"""

# ---------------------------------------------------------------- 02 gradient -> flow
S02_CSS = CV_CSS + """
.panel.white { background:#ffffff; }
.flowlbl { position:absolute; left:56px; top:44px; font-size:44px; letter-spacing:-0.01em; z-index:2; }
"""
S02_VIS = CANVAS + '\n        <div class="flowlbl g r" id="flowlbl">Flow</div>'
S02_JS = CV_JS_HEAD + """
  const off = document.createElement("canvas"); off.width = 1608 + 320; off.height = 1404 + 320;
  const oc = off.getContext("2d");
  const M = 80;
  const BANDS = [
    { c: "#bcd8ff", y: 0 },
    { c: "#6fb6ff", y: 250, a: 60, f: 0.9, s: 1, p: 0.3 },
    { c: "#3a78e6", y: 360, a: 70, f: 1.1, s: -1, p: 1.9 },
    { c: "#1d3a78", y: 470, a: 55, f: 0.8, s: 1, p: 3.1 },
    { c: "#6c86f0", y: 590, a: 45, f: 1.3, s: -2, p: 4.4 },
  ];
  const TOPL = 240, TOPR = 22;
  function render(t) {
    const ph = TAU * t / D;
    oc.setTransform(2, 0, 0, 2, 2 * M, 2 * M);
    oc.clearRect(-M, -M, W + 2 * M, H + 2 * M);
    oc.filter = "blur(40px)";
    BANDS.forEach((b, k) => {
      oc.fillStyle = b.c;
      oc.beginPath();
      if (k === 0) { oc.rect(-M, -M, W + 2 * M, H + 2 * M); oc.fill(); return; }
      oc.moveTo(-M, H + M);
      for (let x = -M; x <= W + M; x += 12) {
        const u = x / W;
        const y = b.y + (1 - u) * 110 + b.a * Math.sin(TAU * u * b.f + b.s * ph + b.p) + 0.4 * b.a * Math.sin(TAU * u * 2.1 - b.s * ph + b.p * 2);
        oc.lineTo(x, y);
      }
      oc.lineTo(W + M, H + M); oc.closePath(); oc.fill();
    });
    oc.filter = "none";
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, cv.width, cv.height);
    ctx.save();
    ctx.beginPath(); ctx.moveTo(0, TOPL * 2); ctx.lineTo(W * 2, TOPR * 2); ctx.lineTo(W * 2, H * 2); ctx.lineTo(0, H * 2); ctx.closePath(); ctx.clip();
    ctx.drawImage(off, -2 * M, -2 * M);
    ctx.restore();
  }
"""

# ---------------------------------------------------------------- 03 glass -> tilt
S03_CSS = """
.blob { position:absolute; left:0; top:0; border-radius:50%; }
#bA { width:620px; height:620px; margin:-310px 0 0 -310px; background:radial-gradient(circle, rgba(79,134,232,0.95), rgba(79,134,232,0) 68%); }
#bB { width:520px; height:520px; margin:-260px 0 0 -260px; background:radial-gradient(circle, rgba(127,208,255,0.85), rgba(127,208,255,0) 68%); }
#bC { width:440px; height:440px; margin:-220px 0 0 -220px; background:radial-gradient(circle, rgba(140,150,255,0.85), rgba(140,150,255,0) 68%); }
#bD { width:360px; height:360px; margin:-180px 0 0 -180px; background:radial-gradient(circle, rgba(219,231,255,0.75), rgba(219,231,255,0) 68%); }
.persp { position:absolute; inset:0; perspective:1400px; }
.gcard { position:absolute; left:132px; top:196px; width:540px; height:330px; border-radius:30px; overflow:hidden;
  background:linear-gradient(135deg, rgba(255,255,255,0.62), rgba(255,255,255,0.36));
  border:2px solid rgba(255,255,255,0.75);
  -webkit-backdrop-filter:blur(22px) saturate(1.3); backdrop-filter:blur(22px) saturate(1.3);
  box-shadow:0 30px 60px -20px rgba(18,21,50,0.55), inset 0 1px 0 rgba(255,255,255,0.9); }
.chip { position:absolute; left:48px; top:62px; width:70px; height:52px; border-radius:11px; background:linear-gradient(135deg,#f4f7fc,#aab9d1 60%,#dfe7f3); box-shadow:inset 0 0 0 1.5px rgba(39,73,118,0.25); }
.nfc { position:absolute; right:48px; top:62px; }
.cnum { position:absolute; left:48px; bottom:64px; font-size:42px; letter-spacing:0.12em; }
.cexp { position:absolute; right:48px; bottom:66px; font-size:34px; letter-spacing:0.04em; }
.sweep { position:absolute; top:-40px; left:0; width:260px; height:420px; background:linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.65) 50%, rgba(255,255,255,0) 100%); }
"""
S03_VIS = """        <div class="blob" id="bA"></div><div class="blob" id="bB"></div><div class="blob" id="bC"></div><div class="blob" id="bD"></div>
        <div class="persp">
          <div class="gcard" id="gcard">
            <div class="chip"></div>
            <svg class="nfc" width="44" height="52" viewBox="0 0 44 52"><defs><linearGradient id="ng" x1="0" x2="1"><stop offset="0" stop-color="#121532"/><stop offset="1" stop-color="#274976"/></linearGradient></defs><g fill="none" stroke="url(#ng)" stroke-width="4" stroke-linecap="round"><path d="M8 18a12 12 0 0 1 0 16"/><path d="M18 11a22 22 0 0 1 0 30"/><path d="M28 4a32 32 0 0 1 0 44"/></g></svg>
            <div class="cnum g r">&bull;&bull;&bull;&bull; 4242</div>
            <div class="cexp g b">12/29</div>
            <div class="sweep" id="sweep"></div>
          </div>
        </div>"""
S03_JS = """
  const blobs = [
    { id: "#bA", x: 560, y: 210, ax: 120, ay: 80, n: 1, p: 0.0 },
    { id: "#bB", x: 230, y: 420, ax: 110, ay: 90, n: 1, p: 2.1 },
    { id: "#bC", x: 300, y: 200, ax: 90, ay: 110, n: 2, p: 4.0 },
    { id: "#bD", x: 600, y: 520, ax: 80, ay: 70, n: 1, p: 1.2 },
  ];
  function render(t) {
    const ph = TAU * t / D;
    blobs.forEach((b) => gsap.set(b.id, { x: b.x + b.ax * Math.sin(b.n * ph + b.p), y: b.y + b.ay * Math.cos(b.n * ph + b.p * 1.3) }));
    gsap.set("#gcard", { rotationY: 17 * Math.sin(ph), rotationX: 9 * Math.cos(ph), y: 8 * Math.sin(2 * ph) });
    const sp = clamp((t - 2.4) / 1.1, 0, 1);
    const e = sp < 0.5 ? 2 * sp * sp : 1 - Math.pow(-2 * sp + 2, 2) / 2;
    gsap.set("#sweep", { x: -320 + 900 * e, rotation: 0 });
  }
"""

# ---------------------------------------------------------------- 04 globe -> arcs
S04_JS = CV_JS_HEAD + """
  const DOTS = """ + GLOBE_DOTS + """;
  const RAD = Math.PI / 180, R = 268, CX = 402, CY = 351, TILT = 0.36;
  const C0 = 110, SPIN = 360 / D;
  const geo = (lon, lat) => { const f = lat * RAD, l = lon * RAD; return [Math.cos(f) * Math.cos(l), Math.cos(f) * Math.sin(l), Math.sin(f)]; };
  const G = DOTS.map(([lon, lat]) => ({ v: geo(lon, lat), lat }));
  const CITY = { jkt: [106.8, -6.2], tyo: [139.7, 35.7], syd: [151.2, -33.9], dxb: [55.3, 25.2], lon: [-0.1, 51.5], nyc: [-74, 40.7], sao: [-46.6, -23.5], los: [3.4, 6.5], lax: [-118.2, 34] };
  const ARCS = [["jkt", "tyo"], ["jkt", "syd"], ["dxb", "jkt"], ["lon", "dxb"], ["nyc", "lon"], ["sao", "los"], ["lax", "nyc"], ["lax", "tyo"], ["syd", "lax"]].map(([a, b]) => {
    const A = geo(...CITY[a]), B = geo(...CITY[b]);
    const om = Math.acos(clamp(A[0] * B[0] + A[1] * B[1] + A[2] * B[2], -1, 1));
    const mid = (CITY[a][0] + CITY[b][0]) / 2;
    const T = ((((C0 - (mid + 30)) / SPIN) % D) + D) % D;
    return { A, B, om, T };
  });
  function proj(v, c, e) {
    const cl = Math.cos(c * RAD), sl = Math.sin(c * RAD);
    const x = -v[0] * sl + v[1] * cl;
    const z0 = v[0] * cl + v[1] * sl;
    const y0 = v[2];
    const y = y0 * Math.cos(TILT) - z0 * Math.sin(TILT);
    const z = z0 * Math.cos(TILT) + y0 * Math.sin(TILT);
    return [CX + R * e * x, CY - R * e * y, z];
  }
  function slerp(a, b, om, s) {
    const so = Math.sin(om), ka = Math.sin((1 - s) * om) / so, kb = Math.sin(s * om) / so;
    return [a[0] * ka + b[0] * kb, a[1] * ka + b[1] * kb, a[2] * ka + b[2] * kb];
  }
  const vis = (p) => p[2] > 0 || Math.hypot(p[0] - CX, p[1] - CY) > R + 1;
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const c = C0 - SPIN * t;
    let g = ctx.createRadialGradient(CX - 90, CY - 110, 20, CX, CY, R);
    g.addColorStop(0, "rgba(63,105,170,0.75)"); g.addColorStop(1, "rgba(22,34,72,0.6)");
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(CX, CY, R, 0, TAU); ctx.fill();
    for (const d of G) {
      const p = proj(d.v, c, 1);
      if (p[2] <= 0.02) continue;
      const cc = col(0.15 + 0.85 * (d.lat + 60) / 140);
      ctx.fillStyle = "rgba(" + cc[0] + "," + cc[1] + "," + cc[2] + "," + (0.25 + 0.75 * p[2]).toFixed(3) + ")";
      ctx.beginPath(); ctx.arc(p[0], p[1], 1.1 + 1.9 * p[2], 0, TAU); ctx.fill();
    }
    ctx.strokeStyle = "rgba(143,180,236,0.55)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(CX, CY, R, 0, TAU); ctx.stroke();
    ctx.lineCap = "round";
    for (const a of ARCS) {
      const tt = (((t - a.T) % D) + D) % D;
      if (tt > 2.0) continue;
      const head = clamp(tt / 1.3, 0, 1);
      const he = 1 - Math.pow(1 - head, 2);
      const tail = Math.max(clamp((tt - 1.3) / 0.5, 0, 1), he - 0.45);
      const N = 28;
      let prev = null;
      for (let i = 0; i <= N; i++) {
        const s = tail + (he - tail) * i / N;
        const v = slerp(a.A, a.B, a.om, s);
        const p = proj(v, c, 1 + 0.24 * Math.sin(Math.PI * s));
        if (prev && vis(p) && vis(prev)) {
          const k = i / N;
          ctx.strokeStyle = "rgba(127,208,255," + (0.12 * k).toFixed(3) + ")"; ctx.lineWidth = 10;
          ctx.beginPath(); ctx.moveTo(prev[0], prev[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
          const cc = col(0.2 + 0.8 * k);
          ctx.strokeStyle = "rgba(" + cc[0] + "," + cc[1] + "," + cc[2] + "," + (0.25 + 0.75 * k).toFixed(3) + ")"; ctx.lineWidth = 3.4;
          ctx.beginPath(); ctx.moveTo(prev[0], prev[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
        }
        prev = p;
      }
      const pa = proj(a.A, c, 1), pb = proj(a.B, c, 1);
      ctx.fillStyle = "rgba(255,255,255,0.95)";
      if (pa[2] > 0 && tt < 1.6) { ctx.beginPath(); ctx.arc(pa[0], pa[1], 4, 0, TAU); ctx.fill(); }
      if (tt < 1.3 && he > tail) {
        const hp = proj(slerp(a.A, a.B, a.om, he), c, 1 + 0.24 * Math.sin(Math.PI * he));
        if (vis(hp)) { ctx.beginPath(); ctx.arc(hp[0], hp[1], 5, 0, TAU); ctx.fill(); }
      }
      if (tt >= 1.3 && pb[2] > 0) {
        const q = clamp((tt - 1.3) / 0.6, 0, 1);
        ctx.beginPath(); ctx.arc(pb[0], pb[1], 4.5, 0, TAU); ctx.fill();
        ctx.strokeStyle = "rgba(214,228,255," + (1 - q).toFixed(3) + ")"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(pb[0], pb[1], 6 + 22 * q, 0, TAU); ctx.stroke();
      }
    }
  }
"""

# ---------------------------------------------------------------- 06 shape -> morph
S06_CSS = """
#sv { position:absolute; inset:0; }
.slabs { position:absolute; left:0; right:0; top:46px; height:44px; }
.slab { position:absolute; left:0; right:0; text-align:center; font-size:30px; letter-spacing:0.32em; opacity:0; }
#shape { filter: drop-shadow(0 26px 34px rgba(79,134,232,0.35)); }
"""
S06_VIS = """        <div class="slabs">
          <div class="slab g b" id="lab0">LINGKARAN</div>
          <div class="slab g b" id="lab1">KOTAK</div>
          <div class="slab g b" id="lab2">BINTANG</div>
          <div class="slab g b" id="lab3">BLOB</div>
        </div>
        <svg id="sv" width="804" height="702" viewBox="0 0 804 702">
          <defs>
            <linearGradient id="fillg" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#9ad4ff" /><stop offset="0.5" stop-color="#4f86e8" /><stop offset="1" stop-color="#233f8a" />
            </linearGradient>
            <radialGradient id="gloss" cx="32%" cy="26%" r="55%"><stop offset="0" stop-color="#fff" stop-opacity="0.55" /><stop offset="1" stop-color="#fff" stop-opacity="0" /></radialGradient>
            <radialGradient id="shg"><stop offset="0" stop-color="#121532" stop-opacity="0.28" /><stop offset="1" stop-color="#121532" stop-opacity="0" /></radialGradient>
          </defs>
          <ellipse id="shd" cx="402" cy="610" rx="190" ry="26" fill="url(#shg)" />
          <path id="shape" fill="url(#fillg)" />
          <path id="glossp" fill="url(#gloss)" />
        </svg>"""
S06_JS = """
  const M = 240, BASE = 205, CX = 402, CY = 350;
  const SH = [
    (a) => 1,
    (a) => 0.9 * Math.pow(Math.pow(Math.abs(Math.cos(a)), 4.5) + Math.pow(Math.abs(Math.sin(a)), 4.5), -1 / 4.5),
    (a) => { const k = (Math.cos(5 * (a + Math.PI / 2)) + 1) / 2; return 0.62 + 0.5 * Math.pow(k, 1.6); },
    (a) => 0.94 * (1 + 0.13 * Math.sin(3 * a + 0.6) + 0.07 * Math.cos(5 * a - 1) + 0.05 * Math.sin(2 * a)),
  ];
  const TBL = SH.map((f) => [...Array(M)].map((_, i) => f(TAU * i / M)));
  const STEPS = [[0.5, 0, 1], [1.9, 1, 2], [3.3, 2, 3], [4.7, 3, 0]];
  const el = gsap.parseEase("elastic.out(1,0.42)");
  const shapeEl = document.getElementById("shape"), glossEl = document.getElementById("glossp");
  const labs = [0, 1, 2, 3].map((i) => document.getElementById("lab" + i));
  function state(t) {
    let from = 0, to = 0, p = 1;
    for (const [s, a, b] of STEPS) if (t >= s) { from = a; to = b; p = clamp((t - s) / 1.1, 0, 1); }
    return { from, to, e: el(p), p };
  }
  function pathFor(r, sc, dx, dy) {
    let d = "";
    for (let i = 0; i < M; i++) {
      const a = TAU * i / M, rr = BASE * r[i] * sc;
      d += (i ? "L" : "M") + (CX + dx + rr * Math.cos(a)).toFixed(1) + " " + (CY + dy + rr * Math.sin(a)).toFixed(1);
    }
    return d + "Z";
  }
  function render(t) {
    const s = state(t), A = TBL[s.from], B = TBL[s.to];
    const r = A.map((v, i) => v + (B[i] - v) * s.e);
    const bob = 8 * Math.sin(TAU * t / 3);
    shapeEl.setAttribute("d", pathFor(r, 1, 0, bob));
    glossEl.setAttribute("d", pathFor(r, 0.86, -14, bob - 16));
    const avg = r.reduce((x, y) => x + y, 0) / M;
    const sd = document.getElementById("shd");
    sd.setAttribute("rx", (175 * avg - 4 * Math.sin(TAU * t / 3)).toFixed(1));
    sd.setAttribute("opacity", (0.9 - 0.15 * Math.sin(TAU * t / 3)).toFixed(3));
    const cur = s.p < 0.12 ? s.from : s.to;
    const fade = (cur === s.to && s.from !== s.to) ? clamp((s.p - 0.12) / 0.15, 0, 1) : 1;
    labs.forEach((l, i) => { const o = i === cur ? fade : 0; gsap.set(l, { opacity: o, y: (1 - o) * 10 }); });
  }
"""

SLIDES_A = [
    dict(cid="s01", num="01", page="02", name="Particles logo", w1="Particles", w2="logo",
         sub="Titik-titik yang berkumpul jadi logo kamu", panel="dark", css=CV_CSS, visual=CANVAS, js=S01_JS,
         body='Sekitar 500 titik kecil warna gradasi melayang masuk dari tepi, berkumpul jadi <b class="b">[deskripsi logo kamu dalam satu kalimat]</b>, berkilau sekali, lalu meledak jadi cincin dan kembali pulang.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> huruf A dari logo AIpreneur.</div>'),
    dict(cid="s02", num="02", page="03", name="Gradient flow", w1="Gradient", w2="flow",
         sub="Gradasi yang mengalir", panel="white", css=S02_CSS, visual=S02_VIS, js=S02_JS,
         body='Gradasi hero miring memenuhi frame (biru es, biru langit, azure, navy). Pita warna mengalir di dalamnya kayak cairan pelan, dengan <b class="b">&ldquo;[satu kata]&rdquo;</b> teks navy kecil di pojok atas.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> &ldquo;Flow&rdquo;.</div>'),
    dict(cid="s03", num="03", page="04", name="Glass tilt", w1="Glass", w2="tilt",
         sub="Kartu kaca yang miring", panel="dark", css=S03_CSS, visual=S03_VIS, js=S03_JS,
         body='Kartu pembayaran kaca frosted (chip, <b class="b">&ldquo;&bull;&bull;&bull;&bull; [4 digit]&rdquo;</b>, <b class="b">&ldquo;[expiry]&rdquo;</b>, tanpa logo) berputar pelan dalam 3D di atas warna yang bergerak di navy gelap, dan seberkas cahaya menyapu permukaannya.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> 4242 dan 12/29.</div>'),
    dict(cid="s04", num="04", page="05", name="Globe arcs", w1="Globe", w2="arcs",
         sub="Globe dengan transaksi yang terbang mengelilinginya", panel="dark", css=CV_CSS, visual=CANVAS, js=S04_JS,
         body='Globe bertitik di atas navy gelap berputar sekali per loop. Garis lengkung biru bercahaya terbang antar <b class="b">[kota-kota kamu]</b> dan mendarat dengan pulse kecil.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> Jakarta, Tokyo, Sydney, Dubai, London, New York.</div>'),
    dict(cid="s06", num="06", page="07", name="Shape morph", w1="Shape", w2="morph",
         sub="Bentuk yang terus berubah", panel="light", css=S06_CSS, visual=S06_VIS, js=S06_JS,
         body="Satu bentuk gradasi glossy (biru muda ke navy) memantul dari lingkaran ke kotak, ke bintang, ke blob lembut, lalu balik lagi ke lingkaran. Label kecil di atasnya menyebut tiap bentuk. Bayangan halus di bawahnya.",
         used=""),
]
