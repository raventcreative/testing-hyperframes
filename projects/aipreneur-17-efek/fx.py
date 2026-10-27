"""17 effect demos. Each: (css, html_inside_panel, js). Panel coords 470x836.
The presenter is a stylised avatar (stand-in for the talking head)."""

FIG_PATH = ("M235 228 C270 228 293 258 293 300 C293 338 277 360 263 371 L263 404 C332 414 393 452 405 560 "
            "L414 836 L56 836 L65 560 C77 452 138 414 207 404 L207 371 C193 360 177 338 177 300 C177 258 200 228 235 228 Z")
TORSO = "M207 396 C138 410 77 452 65 560 L56 836 L414 836 L405 560 C393 452 332 410 263 396 C255 418 215 418 207 396 Z"


def fig(fid="fg", style="", outline=False, z=10):
    o = f'<path d="{FIG_PATH}" fill="none" stroke="#fff" stroke-width="28" stroke-linejoin="round"/>' if outline else ""
    return f"""<svg class="fig" id="{fid}" viewBox="0 0 470 836" style="z-index:{z};{style}">
  <defs><linearGradient id="{fid}sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f7fc"/><stop offset="1" stop-color="#c9d6ea"/></linearGradient>
  <linearGradient id="{fid}sk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3d2b8"/><stop offset="1" stop-color="#d9a98a"/></linearGradient></defs>
  {o}
  <rect x="210" y="350" width="50" height="70" rx="20" fill="url(#{fid}sk)"/>
  <path d="{TORSO}" fill="url(#{fid}sh)"/>
  <path d="M207 396 C215 418 255 418 263 396" fill="none" stroke="#00c9ff" stroke-width="5"/>
  <ellipse cx="235" cy="300" rx="58" ry="70" fill="url(#{fid}sk)"/>
  <path d="M177 296 C175 250 200 222 238 222 C276 222 298 250 293 292 C285 270 262 258 235 258 C208 258 186 270 177 296 Z" fill="#1b1f33"/>
  <circle cx="214" cy="304" r="5" fill="#1b1f33"/><circle cx="256" cy="304" r="5" fill="#1b1f33"/>
  <path d="M218 334 C228 342 242 342 252 334" fill="none" stroke="#9a5a45" stroke-width="4" stroke-linecap="round"/>
</svg>"""


def card_thumb(i):
    g = ["linear-gradient(140deg,#5fe0ff,#0078ff)", "linear-gradient(140deg,#ffffff,#c7d6f2)", "linear-gradient(140deg,#2a5bd7,#0b1440)",
         "linear-gradient(140deg,#00c9ff,#2a5bd7)", "linear-gradient(140deg,#9cc2ff,#4f86e8)"][i % 5]
    return g


# ------------------------------------------------------------------ 01 orbit
E1 = ("""
.oc { position:absolute; left:0; top:0; width:78px; height:100px; border-radius:14px; box-shadow:0 10px 20px -8px rgba(0,0,0,0.6); border:2px solid rgba(255,255,255,0.7); overflow:hidden; }
.oc i { position:absolute; left:10px; right:10px; bottom:12px; height:7px; border-radius:4px; background:rgba(255,255,255,0.75); }
.oc b { position:absolute; left:10px; width:34px; bottom:26px; height:7px; border-radius:4px; background:rgba(255,255,255,0.5); }
""", "".join(f'<div class="oc" id="oc{i}" style="background:{card_thumb(i)}"><b></b><i></i></div>' for i in range(5)) + fig(), """
  function render(t) {
    const on = backOut((t - 0.4) / 0.5, 1.6) * (1 - io3((t - 5.2) / 0.5));
    for (let i = 0; i < 5; i++) {
      const a = TAU * (t / 1.3) + i * TAU / 5, s = Math.sin(a);
      const k = clamp(on, 0, 1.1);
      const x = 235 + 190 * k * Math.cos(a), y = 540 + 62 * k * s;
      const sc = (s > 0 ? mix(0.78, 1.05, s) : mix(0.78, 0.78, 0)) * k;
      gsap.set("#oc" + i, { x: x - 39, y: y - 50, scale: s > 0 ? mix(0.9, 1.05, s) * k : 0.78 * k, rotation: 14 * Math.cos(a), zIndex: s > 0 ? 15 : 5, opacity: k > 0.02 ? 1 : 0 });
    }
  }
""")

# ------------------------------------------------------------------ 02 couch wall
_cw = []
for r in range(4):
    for c in range(3):
        i = r * 3 + c
        x, y = 26 + c * 144, 36 + r * 124
        inner = '<svg width="34" height="34" viewBox="0 0 34 34"><circle cx="17" cy="17" r="16" fill="rgba(255,255,255,0.9)"/><path d="M13 10l11 7-11 7z" fill="#0b1440"/></svg>' if i % 2 == 0 else \
                '<div style="position:absolute;left:12px;right:12px;top:16px"><i class="ln"></i><i class="ln" style="width:70%"></i><i class="ln" style="width:85%"></i></div>'
        bg = card_thumb(i) if i % 2 == 0 else "rgba(255,255,255,0.92)"
        _cw.append(f'<div class="cw" id="cw{i}" style="left:{x}px;top:{y}px;background:{bg}">{inner}</div>')
E2 = ("""
.cw { position:absolute; width:130px; height:110px; border-radius:14px; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 20px -10px rgba(0,0,0,0.6); z-index:5; }
.ln { display:block; height:8px; border-radius:4px; background:#c7d3e8; margin-bottom:10px; }
.big2 { position:absolute; left:0; right:0; top:640px; text-align:center; z-index:20; font-size:40px; }
""", "".join(_cw) + fig() + '<div class="big2"><span class="hb" id="bg2">365 konten / tahun</span></div>', """
  const order = [...Array(12).keys()].sort((a, b) => { const d = (i) => Math.hypot(i % 3 - 1, Math.floor(i / 3) - 1.5); return d(a) - d(b); });
  let seed = 9; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const tilt = [...Array(12)].map(() => (rnd() * 2 - 1) * 3);
  function render(t) {
    const out = smooth((t - 5.2) / 0.4);
    order.forEach((i, k) => { const p = backOut((t - 0.5 - k * 0.035) / 0.4, 1.8); gsap.set("#cw" + i, { scale: Math.max(0, p) * (1 - out), rotation: tilt[i] }); });
    gsap.set("#bg2", { scale: Math.max(0, backOut((t - 1.2) / 0.45, 2.2)) * (1 - out) });
  }
""")

# ------------------------------------------------------------------ 03 ui world
E3 = ("""
.uiw { position:absolute; inset:0; background:#f3eee5; z-index:2; }
.uibar { position:absolute; left:0; right:0; top:0; height:48px; border-bottom:1.5px solid rgba(11,20,64,0.1); display:flex; align-items:center; gap:8px; padding:0 18px; }
.uibar i { width:11px; height:11px; border-radius:50%; display:block; }
.uibar span { margin-left:10px; font-size:15px; font-weight:700; color:#0b1440; }
.th3 { position:absolute; top:66px; width:96px; height:70px; border-radius:12px; z-index:3; box-shadow:0 8px 16px -8px rgba(0,0,0,0.4); }
.bb { position:absolute; max-width:330px; padding:12px 16px; border-radius:18px; font-size:16px; line-height:1.35; z-index:3; }
.bb.me { right:18px; background:#00c9ff; color:#0b1440; font-weight:700; border-bottom-right-radius:5px; }
.bb.ai { left:18px; background:#fff; color:#0b1440; border-bottom-left-radius:5px; box-shadow:0 6px 14px -8px rgba(0,0,0,0.25); }
.cap3 { position:absolute; left:18px; right:18px; bottom:18px; height:60px; border-radius:16px; background:#0b1440; z-index:20; }
.cap3 span { position:absolute; left:0; right:0; top:0; line-height:60px; text-align:center; font-size:22px; font-weight:700; }
""", '<div class="uiw"><div class="uibar"><i style="background:#ff6b6b"></i><i style="background:#ffd166"></i><i style="background:#00c9ff"></i><span>AI Editor</span></div></div>' +
    "".join(f'<div class="th3" id="t3{i}" style="left:{18 + i * 110}px;background:{card_thumb(i)}"></div>' for i in range(4)) +
    '<div class="bb me" id="b31" style="top:160px">Potong jeda &amp; kasih 4 hook dari video ini</div>'
    '<div class="bb ai" id="b32" style="top:236px">Siap! Ini 4 hook-nya, jeda udah dipotong &#10003;</div>' +
    fig(style="transform-origin:235px 836px") +
    '<div class="cap3"><span class="w" id="c31">Ngedit 3 jam</span><span id="c32" style="opacity:0"><span class="hb" style="font-size:22px">Ngedit 10 menit</span></span></div>', """
  function render(t) {
    for (let i = 0; i < 4; i++) { const p = backOut((t - 0.4 - i * 0.08) / 0.45, 1.6); gsap.set("#t3" + i, { y: -140 * (1 - Math.min(1, p)) + (p > 1 ? 0 : 0), opacity: t > 0.4 + i * 0.08 ? 1 : 0 }); }
    gsap.set("#b31", { opacity: smooth((t - 1.0) / 0.2), y: 12 * (1 - smooth((t - 1.0) / 0.25)) });
    gsap.set("#b32", { opacity: smooth((t - 1.7) / 0.2), y: 12 * (1 - smooth((t - 1.7) / 0.25)) });
    gsap.set("#fg", { scale: 0.62, y: 0 });
    const sw = smooth((t - 3.0) / 0.25) * (1 - smooth((t - 5.4) / 0.25));
    gsap.set("#c31", { opacity: 1 - sw }); gsap.set("#c32", { opacity: sw, scale: 0.9 + 0.1 * sw });
  }
""")

# ------------------------------------------------------------------ 04 frame break
FT, FB = 250, 800
E4 = (f"""
.dark4 {{ position:absolute; inset:0; background:#050a22; z-index:1; }}
.frm {{ position:absolute; left:70px; top:{FT}px; width:330px; height:{FB - FT}px; border-radius:40px; border:10px solid #dfe8f6; z-index:12; box-shadow:0 0 40px rgba(0,201,255,0.25); }}
.scr4 {{ position:absolute; left:80px; top:{FT + 10}px; width:310px; height:{FB - FT - 20}px; border-radius:30px; background:linear-gradient(170deg,#2a5bd7,#0b1440); z-index:3; }}
.in4 {{ clip-path: inset({FT + 10}px 80px {836 - FB + 10}px 80px round 30px); }}
.out4 {{ clip-path: inset(0 0 {836 - FT - 6}px 0); filter: drop-shadow(0 14px 14px rgba(0,0,0,0.6)); }}
""", '<div class="dark4"></div><div class="scr4"></div><div class="frm"></div>' + fig("fa", z=11).replace('class="fig"', 'class="fig in4"') + fig("fb", z=13).replace('class="fig"', 'class="fig out4"'), """
  function render(t) {
    const up = backOut((t - 1.0) / 0.3, 1.6) * (1 - io3((t - 5.0) / 0.4));
    const y = 70 - 110 * clamp(up, 0, 1.1);
    gsap.set(["#fa", "#fb"], { y: y });
    gsap.set("#fb", { opacity: up > 0.02 ? 1 : 0 });
  }
""")

# ------------------------------------------------------------------ 05 digital zoom
E5 = ("""
.kw5 { position:absolute; left:0; right:0; top:560px; text-align:center; z-index:20; font-size:76px; }
""", fig(style="transform-origin:235px 300px") + '<div class="kw5"><span class="hb" id="kw5">CUAN</span></div>', """
  function render(t) {
    const z = smooth((t - 1.0) / 0.1) * (1 - io3((t - 4.2) / 0.35));
    const sh = t > 1.1 && t < 1.25 ? 3 * Math.sin((t - 1.1) * 130) : 0;
    gsap.set("#fg", { scale: 1 + 0.7 * z, x: sh });
    const k = smooth((t - 1.05) / 0.18);
    gsap.set("#kw5", { scale: mix(1.8, 1, k), opacity: k * (1 - smooth((t - 4.1) / 0.2)) });
  }
""")

# ------------------------------------------------------------------ 06 phone mockup
E6 = ("""
.pm { position:absolute; left:296px; top:120px; width:160px; height:300px; border-radius:26px; background:#050a22; border:4px solid #dfe8f6; z-index:20; box-shadow:0 20px 40px -14px rgba(0,0,0,0.7); overflow:hidden; }
.pm .nt { position:absolute; left:55px; top:8px; width:44px; height:12px; border-radius:6px; background:#000; }
.pm .bub { position:absolute; max-width:118px; padding:7px 10px; border-radius:12px; font-size:11.5px; line-height:1.3; }
.pm .me { right:8px; background:#00c9ff; color:#0b1440; font-weight:700; }
.pm .rp { left:8px; background:#fff; color:#0b1440; }
""", fig() + '<div class="pm" id="pm6"><div class="nt"></div>'
    '<div class="bub me" id="m1" style="top:34px">Kak, kelasnya masih buka?</div>'
    '<div class="bub rp" id="m2" style="top:86px">Masih! Sisa 5 kursi &#128073;</div>'
    '<div class="bub me" id="m3" style="top:138px">Langsung daftar ya</div>'
    '<div class="bub rp" id="m4" style="top:178px">Sip, link-nya udah aku kirim &#10003;</div></div>', """
  function render(t) {
    const p = io3((t - 0.6) / 0.32), out = io3((t - 5.2) / 0.35);
    gsap.set("#pm6", { x: 220 * (1 - p) + 220 * out, rotation: mix(12, -8, p), y: 5 * Math.sin(TAU * t / 2) });
    for (let i = 1; i <= 4; i++) gsap.set("#m" + i, { opacity: smooth((t - 1.1 - (i - 1) * 0.55) / 0.15), scale: 0.9 + 0.1 * smooth((t - 1.1 - (i - 1) * 0.55) / 0.2) });
  }
""")

# ------------------------------------------------------------------ 07 checklist
E7 = ("""
.ck { position:absolute; left:50px; top:36px; width:370px; padding:18px 20px; border-radius:20px; background:rgba(5,10,34,0.72); border:1.5px solid rgba(255,255,255,0.2); z-index:20; }
.ck .hd { font-size:13px; letter-spacing:0.16em; font-weight:700; color:#00c9ff; }
.ck .cnt { position:absolute; right:20px; top:16px; font-size:14px; font-weight:700; }
.ck .it { display:flex; align-items:center; gap:12px; margin-top:12px; font-size:19px; font-weight:700; }
.ck .bx { width:28px; height:28px; border-radius:8px; border:2px solid rgba(255,255,255,0.5); display:flex; align-items:center; justify-content:center; color:#0b1440; font-size:17px; }
""", fig() + '<div class="ck" id="ck7"><div class="hd">CHECKLIST</div><div class="cnt w" id="cn7">0 dari 3</div>' +
    "".join(f'<div class="it w"><div class="bx" id="bx{i}">&#10003;</div><span>{s}</span></div>' for i, s in enumerate(["Rekam talking head", "Transkrip &amp; potong jeda", "Render 1080p"])) + '</div>', """
  function render(t) {
    gsap.set("#ck7", { opacity: smooth((t - 0.3) / 0.25) * (1 - smooth((t - 5.3) / 0.3)), y: -14 * (1 - smooth((t - 0.3) / 0.3)) });
    let n = 0;
    for (let i = 0; i < 3; i++) {
      const at = 1.0 + i * 0.6, on = t >= at && t < 5.3;
      if (on) n++;
      const b = $("bx" + i);
      b.style.background = on ? "#00c9ff" : "transparent"; b.style.borderColor = on ? "#00c9ff" : "rgba(255,255,255,0.5)"; b.style.color = on ? "#0b1440" : "transparent";
      gsap.set(b, { scale: 1 + 0.35 * Math.sin(Math.PI * clamp((t - at) / 0.25, 0, 1)) });
    }
    $("cn7").textContent = n + " dari 3";
  }
""")

# ------------------------------------------------------------------ 08 headline wall
PAPERS = [(24, 60, 150, 120, -6, "a", "AI bakal gantiin editor?"), (300, 40, 140, 140, 5, "s", "overrated!"), (150, 20, 130, 90, 3, "a", "Konten AI dibanjiri"),
          (20, 220, 120, 120, 7, "s", "setuju 100%"), (330, 220, 120, 130, -4, "a", "Kreator panik"), (36, 400, 110, 110, -3, "s", "coba dulu"), (330, 410, 116, 110, 6, "s", "hype doang?")]
E8 = ("""
.pp { position:absolute; z-index:5; padding:12px; box-shadow:0 10px 18px -8px rgba(0,0,0,0.55); }
.pp.a { background:#f7f4ee; color:#0b1440; font-size:13px; font-weight:700; line-height:1.25; }
.pp.a i { display:block; height:5px; background:#c9cfda; margin-top:7px; border-radius:2px; }
.pp.s { background:#00c9ff; color:#0b1440; font-size:17px; font-weight:700; display:flex; align-items:center; justify-content:center; text-align:center; }
""", "".join(f'<div class="pp {k}" id="pp{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{tx}{"<i></i><i style=width:80%></i><i style=width:60%></i>" if k == "a" else ""}</div>'
             for i, (x, y, w, h, r, k, tx) in enumerate(PAPERS)) + fig(), """
  const ROT = %s;
  function render(t) {
    const out = smooth((t - 5.2) / 0.35);
    for (let i = 0; i < 7; i++) { const k = smooth((t - 0.5 - i * 0.06 * 3) / 0.18); gsap.set("#pp" + i, { scale: mix(1.4, 1, k), opacity: k * (1 - out), rotation: ROT[i] }); }
  }
""" % [p[4] for p in PAPERS])

# ------------------------------------------------------------------ 09 zoom cut
E9 = ("""
.shotB { position:absolute; inset:0; z-index:1; background:radial-gradient(circle at 70% 25%, rgba(0,201,255,0.45), rgba(0,201,255,0) 55%), linear-gradient(170deg,#0e5a8a,#0b1440); opacity:0; }
.zw { position:absolute; left:0; right:0; top:390px; text-align:center; z-index:25; font-size:64px; transform-origin:50% 50%; }
.flash { position:absolute; inset:0; background:#fff; z-index:40; opacity:0; }
.tagB { position:absolute; left:18px; bottom:20px; z-index:25; font-size:18px; opacity:0; }
""", '<div class="shotB" id="sb9"></div>' + fig(style="transform-origin:235px 400px") + '<div class="zw"><span class="hb" id="zw9">BABAK 2</span></div><div class="flash" id="fl9"></div><div class="tagB" id="tb9"><span class="hb">Shot berikutnya</span></div>', """
  function render(t) {
    const ap = smooth((t - 1.0) / 0.2);
    const zp = clamp((t - 1.6) / 0.25, 0, 1), zs = Math.pow(16, zp * zp);
    const cut = t >= 1.85 && t < 5.5;
    gsap.set("#zw9", { scale: t < 1.85 ? zs : 1, opacity: t < 1.85 ? ap : 0 });
    gsap.set("#fl9", { opacity: (t >= 1.85 && t < 1.91) ? 1 : (t >= 5.5 && t < 5.56 ? 1 : 0) });
    gsap.set("#sb9", { opacity: cut ? 1 : 0 });
    const k = cut ? io3((t - 1.91) / 0.3) : 1;
    gsap.set("#fg", { scale: (t < 1.85 ? 1 + 0.15 * zp : mix(1.25, 1, k)), x: cut ? 30 : 0 });
    gsap.set("#tb9", { opacity: cut ? smooth((t - 2.2) / 0.2) : 0 });
  }
""")

# ------------------------------------------------------------------ 10 chart grow
_cx = [40 + i * 65 for i in range(7)]
_cy = [210, 196, 200, 170, 150, 118, 76]
_days = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
E10 = ("""
#ch10 { position:absolute; left:0; top:30px; z-index:5; }
.lb10 { position:absolute; z-index:6; font-size:17px; padding:4px 10px; opacity:0; }
""", f'<svg id="ch10" width="470" height="300" viewBox="0 0 470 300">'
    + "".join(f'<text x="{x}" y="40" font-size="14" font-weight="700" fill="rgba(255,255,255,0.7)" text-anchor="middle">{d}</text><line x1="{x}" y1="52" x2="{x}" y2="240" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>' for x, d in zip(_cx, _days))
    + f'<path id="ln10" d="M{" L".join(f"{x} {y}" for x, y in zip(_cx, _cy))}" fill="none" stroke="#00c9ff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<circle id="dt10" cx="{_cx[-1]}" cy="{_cy[-1]}" r="11" fill="#fff" stroke="#00c9ff" stroke-width="5" opacity="0"/></svg>'
    + fig() + f'<div class="lb10 hb" id="lb10" style="left:{_cx[-1] - 118}px;top:{_cy[-1] + 12}px">+48%</div>', """
  const ln = $("ln10"), L = ln.getTotalLength();
  function render(t) {
    const d = io3((t - 0.8) / 0.55) * (1 - smooth((t - 5.2) / 0.35));
    ln.setAttribute("stroke-dasharray", (d * L).toFixed(1) + " " + (L + 5)); ln.style.opacity = d > 0.01 ? 1 : 0;
    const e = backOut((t - 1.35) / 0.35, 2.4) * (1 - smooth((t - 5.2) / 0.3));
    $("dt10").setAttribute("opacity", e > 0.02 ? 1 : 0); gsap.set("#dt10", { scale: Math.max(0, e), transformOrigin: "50% 50%" });
    gsap.set("#lb10", { opacity: e > 0.02 ? 1 : 0, scale: Math.max(0, e) });
  }
""")

# ------------------------------------------------------------------ 11 pull-back reveal
E11 = ("""
#g11 { position:absolute; inset:0; z-index:2; transform-origin:318px 376px; }
.app11 { position:absolute; inset:0; background:#eef3fb; }
.app11 .top { position:absolute; left:0; right:0; top:0; height:44px; background:#fff; border-bottom:1.5px solid #dbe3f0; display:flex; align-items:center; gap:7px; padding:0 14px; }
.app11 .top i { width:10px; height:10px; border-radius:50%; display:block; }
.side11 { position:absolute; left:12px; top:60px; width:156px; bottom:16px; border-radius:16px; background:#fff; padding:14px 12px; }
.side11 .k { font-size:11px; letter-spacing:0.14em; font-weight:700; color:#274976; }
.side11 .s { display:flex; align-items:center; gap:7px; font-size:12.5px; font-weight:700; color:#0b1440; margin-top:12px; }
.side11 .s b { width:18px; height:18px; border-radius:50%; background:#00c9ff; color:#0b1440; font-size:11px; display:flex; align-items:center; justify-content:center; }
.side11 .pb { margin-top:22px; height:10px; border-radius:5px; background:#dbe3f0; overflow:hidden; }
.side11 .pb i { display:block; width:62%; height:100%; background:#00c9ff; }
.vid11 { position:absolute; left:180px; top:60px; width:278px; bottom:16px; border-radius:16px; overflow:hidden; background:linear-gradient(170deg,#22407e,#0a1236); }
""", '<div id="g11"><div class="app11"><div class="top"><i style="background:#ff6b6b"></i><i style="background:#ffd166"></i><i style="background:#00c9ff"></i></div>'
    '<div class="side11"><div class="k">PROGRES</div>' + "".join(f'<div class="s"><b>&#10003;</b>{s}</div>' for s in ["Riset ide", "Tulis naskah", "Rekam", "Edit AI"]) +
    '<div class="pb"><i></i></div><div class="s" style="margin-top:8px;color:#274976">62% selesai</div></div>'
    '<div class="vid11">' + fig(style="width:278px;height:494px;top:256px") + '</div></div></div>', """
  function render(t) {
    const k = io3((t - 0.6) / 0.55) * (1 - io3((t - 5.0) / 0.6));
    gsap.set("#g11", { scale: mix(2.05, 1, k), x: mix(235 - 318, 0, k), y: mix(330 - 376, 0, k) });
  }
""")

# ------------------------------------------------------------------ 12 green screen
E12 = ("""
.ui12 { position:absolute; inset:0; z-index:2; background:linear-gradient(170deg,#0d2a66,#071033); }
.tm12 { position:absolute; left:22px; top:22px; font-size:76px; font-weight:700; letter-spacing:-0.03em; line-height:1; }
.tm12s { position:absolute; left:26px; top:104px; font-size:14px; letter-spacing:0.14em; color:#00c9ff; font-weight:700; }
.tk12 { position:absolute; left:22px; right:22px; height:52px; border-radius:14px; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.15); display:flex; align-items:center; gap:12px; padding:0 14px; font-size:17px; font-weight:700; }
.tk12 b { width:24px; height:24px; border-radius:7px; border:2px solid #00c9ff; display:flex; align-items:center; justify-content:center; font-size:14px; }
.ln12 { position:absolute; left:22px; right:22px; top:350px; font-size:18px; color:rgba(255,255,255,0.8); }
""", '<div class="ui12" id="ui12"><div class="tm12 w" id="tm12">25:00</div><div class="tm12s">FOKUS MODE</div>' +
    "".join(f'<div class="tk12 w" style="top:{150 + i * 62}px"><b id="tb{i}"></b>{s}</div>' for i, s in enumerate(["Tulis 3 hook", "Rekam 1 video", "Jadwalin posting"])) +
    '<div class="ln12">Satu sesi, satu konten selesai.</div></div>' + fig(style="transform-origin:235px 836px"), """
  function render(t) {
    const w = smooth((t - 0.5) / 0.35) * (1 - smooth((t - 5.3) / 0.35));
    $("ui12").style.clipPath = "inset(0 " + (470 * (1 - w)).toFixed(1) + "px 0 0)";
    gsap.set("#fg", { y: 150 * w, scale: 1 - 0.12 * w });
    const s = Math.max(0, 1500 - Math.floor(Math.max(0, t - 0.8) * 37));
    $("tm12").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
    for (let i = 0; i < 3; i++) { const on = t > 1.6 + i * 0.7 && t < 5.3; const b = $("tb" + i); b.style.background = on ? "#00c9ff" : "transparent"; b.style.color = on ? "#0b1440" : "transparent"; b.textContent = "\\u2713"; }
  }
""")

# ------------------------------------------------------------------ 13 paper cut
RANSOM = [("C", "#0b1440", "#fff", "Poppins", 700), ("U", "#00c9ff", "#0b1440", "'Playfair Display'", 700), ("A", "#fff", "#0b1440", "Poppins", 400), ("N", "#1b1f33", "#00c9ff", "'Playfair Display'", 700)]
E13 = ("""
.pap { position:absolute; inset:0; z-index:1; background:#efe6d6; background-image:repeating-linear-gradient(0deg, rgba(120,100,70,0.06) 0 1px, transparent 1px 22px); }
.blk { position:absolute; left:120px; top:330px; width:240px; height:300px; background:#00c9ff; z-index:3; transform:rotate(-6deg); }
#scr13 { position:absolute; left:0; top:0; z-index:4; }
.rs { position:absolute; top:60px; width:72px; height:86px; display:flex; align-items:center; justify-content:center; font-size:58px; z-index:15; box-shadow:0 6px 10px rgba(0,0,0,0.25); }
#fg { filter: drop-shadow(0 10px 12px rgba(0,0,0,0.35)); }
""", '<div class="pap"></div><div class="blk"></div>'
    '<svg id="scr13" width="470" height="836"><path d="M40 260 C80 240 60 300 110 280 S150 250 160 290" fill="none" stroke="#1b1f33" stroke-width="3"/><path d="M330 600 C360 560 400 640 430 590" fill="none" stroke="#1b1f33" stroke-width="3"/><path d="M50 700 l40 -10 M55 715 l40 -10" stroke="#1b1f33" stroke-width="3"/></svg>' +
    "".join(f'<div class="rs" id="rs{i}" style="left:{70 + i * 86}px;background:{bg};color:{fg};font-family:{ff};font-weight:{fw}">{ch}</div>' for i, (ch, bg, fg, ff, fw) in enumerate(RANSOM)) + fig(outline=True), """
  let seed = 4; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const J = [...Array(80)].map(() => rnd() * 2 - 1);
  const RR = [-7, 5, -3, 8];
  function render(t) {
    const st = Math.floor(t / 0.1);
    gsap.set("#fg", { rotation: J[st % 80], transformOrigin: "50% 90%" });
    for (let i = 0; i < 4; i++) gsap.set("#rs" + i, { scale: Math.max(0, backOut((t - 0.5 - i * 0.18) / 0.35, 2.4)) * (1 - smooth((t - 5.3) / 0.3)), rotation: RR[i] + J[(st + i * 7) % 80] * 2 });
  }
""")

# ------------------------------------------------------------------ 14 doodle boil
E14 = ("""
.dim14 { position:absolute; inset:0; z-index:2; background:rgba(0,0,0,0.35); }
#dd14 { position:absolute; left:0; top:0; z-index:12; overflow:visible; }
""", '<div class="dim14" id="dm14"></div>' + fig() +
    f'<svg id="dd14" width="470" height="836" viewBox="0 0 470 836"><path id="src14" d="{FIG_PATH}" fill="none" stroke="none"/>'
    '<path id="o0" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
    '<path id="o1" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0"/>'
    '<path id="o2" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0"/>'
    '<g id="ic14a"><path d="M70 90 l10 24 26 2 -20 16 7 25 -23 -14 -23 14 7 -25 -20 -16 26 -2z" fill="none" stroke="#00c9ff" stroke-width="5" stroke-linejoin="round"/></g>'
    '<g id="ic14b"><path d="M392 70 l-28 54 h26 l-14 50 40 -64 h-26 l16 -40z" fill="none" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g></svg>', """
  const src = $("src14"), SL = src.getTotalLength(), N = 140;
  let seed = 21; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const base = [];
  for (let i = 0; i < N; i++) {
    const p = src.getPointAtLength(SL * i / N), q = src.getPointAtLength(SL * ((i + 1) % N) / N);
    let nx = -(q.y - p.y), ny = q.x - p.x; const l = Math.hypot(nx, ny) || 1; nx /= l; ny /= l;
    const test = new DOMPoint(p.x + nx * 6, p.y + ny * 6);
    if (src.isPointInFill(test)) { nx = -nx; ny = -ny; }
    base.push([p.x, p.y, nx, ny]);
  }
  const variants = [0, 1, 2].map(() => {
    const pts = base.filter((b) => b[1] < 832).map(([x, y, nx, ny]) => { const o = 14 + (rnd() * 2 - 1) * 4; return [x + nx * o + (rnd() - 0.5) * 3, y + ny * o + (rnd() - 0.5) * 3]; });
    return "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L");
  });
  for (let v = 0; v < 3; v++) $("o" + v).setAttribute("d", variants[v]);
  function render(t) {
    const on = smooth((t - 0.4) / 0.3) * (1 - smooth((t - 5.3) / 0.3));
    const f = Math.floor(t / 0.1) % 3;
    for (let v = 0; v < 3; v++) $("o" + v).setAttribute("opacity", v === f ? on : 0);
    $("dm14").style.opacity = on;
    const j = [[2, -1], [-1, 2], [1, 1]][f];
    gsap.set("#ic14a", { x: j[0], y: j[1], rotation: j[0] * 2, transformOrigin: "80px 120px", opacity: on });
    gsap.set("#ic14b", { x: -j[1], y: j[0], rotation: -j[1] * 2, transformOrigin: "380px 120px", opacity: on });
  }
""")

# ------------------------------------------------------------------ 15 vertigo
E15 = ("""
#rm15 { position:absolute; inset:0; z-index:2; transform-origin:235px 330px; }
.rm { position:absolute; inset:0; background:linear-gradient(170deg,#2a4f96,#0f1c4d); }
.win15 { position:absolute; left:290px; top:90px; width:150px; height:200px; border:6px solid rgba(255,255,255,0.7); background:linear-gradient(180deg,#7fd3ff,#2a7bff); }
.win15::before { content:""; position:absolute; left:66px; top:0; bottom:0; width:6px; background:rgba(255,255,255,0.7); }
.win15::after { content:""; position:absolute; top:94px; left:0; right:0; height:6px; background:rgba(255,255,255,0.7); }
.shelf { position:absolute; left:28px; top:200px; width:150px; height:8px; background:rgba(255,255,255,0.6); }
.bk { position:absolute; bottom:628px; width:20px; border-radius:3px; }
.flr { position:absolute; left:0; right:0; top:620px; bottom:0; background:repeating-linear-gradient(90deg, rgba(255,255,255,0.08) 0 2px, transparent 2px 60px), #0a1236; }
.plant { position:absolute; left:34px; top:470px; width:70px; height:150px; }
""", '<div id="rm15"><div class="rm"></div><div class="win15"></div><div class="shelf"></div>' +
    "".join(f'<div class="bk" style="left:{36 + i * 26}px;height:{50 + (i * 17) % 30}px;background:{["#00c9ff", "#fff", "#4f86e8", "#9cc2ff", "#00c9ff"][i]}"></div>' for i in range(5)) +
    '<div class="flr"></div><svg class="plant" viewBox="0 0 70 150"><path d="M35 150 V60" stroke="#7fe6ff" stroke-width="4"/><ellipse cx="22" cy="60" rx="18" ry="34" fill="#00c9ff" transform="rotate(-25 22 60)"/><ellipse cx="48" cy="55" rx="16" ry="30" fill="#4f86e8" transform="rotate(25 48 55)"/><rect x="14" y="118" width="42" height="32" rx="6" fill="#fff"/></svg></div>' + fig(), """
  function render(t) {
    const k = io3((t - 1.0) / 0.85) * (1 - io3((t - 4.4) / 0.8));
    gsap.set("#rm15", { scale: 1 + 0.55 * k });
  }
""")

# ------------------------------------------------------------------ 16 cover story
E16 = ("""
.mag { position:absolute; inset:0; z-index:1; background:linear-gradient(170deg,#1d3d82,#0a1236); }
.ttl16 { position:absolute; left:0; right:0; top:150px; text-align:center; z-index:5; font-family:'Playfair Display', serif; font-weight:700; font-size:118px; line-height:1; color:#fff; white-space:nowrap; }
.ml { position:absolute; top:22px; z-index:20; font-size:13px; letter-spacing:0.18em; font-weight:700; color:#00c9ff; }
.it16 { position:absolute; left:20px; bottom:24px; z-index:20; font-family:'Playfair Display', serif; font-style:italic; font-size:24px; color:#fff; max-width:260px; line-height:1.25; }
""", '<div class="mag"></div><div class="ttl16" id="tt16">FOKUS</div><div class="ml" style="left:20px">EDISI 01</div><div class="ml" style="right:20px">OKT 2026</div>' + fig() +
    '<div class="it16" id="it16">cara kerja yang nggak bikin capek</div>', """
  function render(t) {
    const k = io3((t - 0.5) / 0.45);
    $("tt16").style.letterSpacing = mix(30, 3, k).toFixed(1) + "px";
    gsap.set("#tt16", { opacity: smooth((t - 0.45) / 0.15) * (1 - smooth((t - 5.3) / 0.3)) });
    gsap.set("#it16", { opacity: smooth((t - 1.1) / 0.3) * (1 - smooth((t - 5.3) / 0.3)), x: -14 * (1 - smooth((t - 1.1) / 0.35)) });
  }
""")

# ------------------------------------------------------------------ 17 glass type
E17 = ("""
.gw17 { position:absolute; left:0; right:0; top:120px; height:200px; z-index:5; perspective:900px; }
#gl17 { position:absolute; left:0; right:0; top:0; text-align:center; font-size:104px; font-weight:700; letter-spacing:-0.02em; line-height:1.3;
  background:linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.15)); -webkit-background-clip:text; background-clip:text; color:transparent;
  -webkit-text-stroke:1.5px rgba(255,255,255,0.9); filter:drop-shadow(0 10px 16px rgba(0,0,0,0.45)); }
""", '<div class="gw17"><div id="gl17">SISTEM</div></div>' + fig(), """
  function render(t) {
    const k = smooth((t - 0.4) / 5.0);
    gsap.set("#gl17", { rotationY: mix(-24, -2, k), rotationX: 6, opacity: smooth((t - 0.3) / 0.3) * (1 - smooth((t - 5.4) / 0.3)), transformOrigin: "50% 50%" });
  }
""")

EFFECTS = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16, E17]
