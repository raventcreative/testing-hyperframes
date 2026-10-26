"""AIpreneur 'Motion brief' carousel (5 slides, dark navy, cyan + white type).
Own layout: visual on top, title + white highlight box below, cyan-ruled explainer.
Run: python3 build.py -> slides/sN/index.html"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
APTS = json.loads((ROOT / "apts.json").read_text())
TOTAL = 19

SHELL = """<!doctype html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1350" />
<title>AIpreneur — %%NAME%%</title>
<script src="vendor/gsap/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/shared.css" />
<style>
%%CSS%%
</style>
</head>
<body>
<div id="root" data-composition-id="%%CID%%" data-start="0" data-duration="6" data-width="1080" data-height="1350" data-fps="30">
  <div id="stage" class="clip" data-start="0" data-duration="6" data-track-index="0" data-track-kind="graphics" style="position:absolute;inset:0">
    <div class="bg"></div>
    <div class="logo"></div>
    <div class="eyebrow">%%EYEBROW%%</div>
%%BODY%%
    <div class="foot"><div class="who"><div class="av">FK</div><span>Freddie Kashawan</span></div>
      <div class="pg"><span class="c">%%PAGE%% / %%TOTAL%%</span>%%RIGHT%%</div></div>
  </div>
%%EXTRA%%
</div>
<script>
(function () {
  const D = 6, TAU = Math.PI * 2;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const smooth = (p) => { p = clamp(p, 0, 1); return p * p * (3 - 2 * p); };
  const env = (t, a, b, f) => { f = f || 0.18; return smooth((t - a) / f) * (1 - smooth((t - b) / f)); };
  const backOut = (p, s) => { p = clamp(p, 0, 1); s = s === undefined ? 1.7 : s; const q = p - 1; return q * q * ((s + 1) * q + s) + 1; };
  const io3 = (p) => { p = clamp(p, 0, 1); return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
  const mix = (a, b, k) => a + (b - a) * k;
  const $ = (id) => document.getElementById(id);
  const tl = gsap.timeline({ paused: true });
  const st = { t: 0 };
%%JS%%
  tl.to(st, { t: D, duration: D, ease: "none", onUpdate: () => render(st.t) }, 0);
  render(0);
  window.__timelines = window.__timelines || {};
  window.__timelines["%%CID%%"] = tl;
})();
</script>
</body>
</html>
"""

ARROW = '<svg class="ar" viewBox="0 0 70 46"><path d="M4 23H62M42 5l20 18-20 18" fill="none" stroke="#00c9ff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def scene_body(w1, w2, sub, body, used, visual):
    used_html = f'<div class="used"><span class="w b">Aku pakai:</span>{"".join(f"<span class=\"hb\">{u}</span>" for u in used)}</div>' if used else ""
    return f"""    <div class="glass" id="vis" style="left:64px;top:128px;width:952px;height:620px;overflow:hidden">
{visual}
    </div>
    <div class="ttl"><span class="w b">{w1}</span>{ARROW}<span class="hb">{w2}</span></div>
    <div class="sub r">{sub}</div>
    <div class="swap"><div class="lbl">GANTI DI SCENE INI</div><div class="txt r">{body}</div>{used_html}</div>
"""


# ======================================================================== 1 · brief template (grid of rule cards)
RULES = [
    ("STANDAR", "Kualitas keynote Apple. Kalau nggak layak tampil di keynote, berarti belum selesai."),
    ("FORMAT", "1080 x 1350. Tepat 6 detik. Frame terakhir sama dengan frame pertama."),
    ("SATU ATURAN", "Satu objek utama isi 60&ndash;70% frame. Satu perubahan yang memuaskan, lalu reset."),
    ("LOOK", "Bersih &amp; tajam. Kaca frosted, bayangan lembut, depth nyata. Maksimal dua warna."),
    ("TIPOGRAFI", "Weight tebal. Maksimal 5 kata. Angka utama minimal 120px."),
    ("MOTION", "Spring physics di semua elemen. Tahan state akhir 1,2 detik."),
    ("JANGAN", "Placeholder abu-abu, stock icon, emoji, teks kepanjangan."),
]
SCENES = ["Bar yang berubah jadi tren", "Switch harga bulanan ke tahunan", "Titik yang menyatu jadi logo", "Island yang berubah jadi live"]
S1_CSS = """
.btitle { position:absolute; left:63px; top:112px; font-size:92px; line-height:1.15; letter-spacing:-0.035em; white-space:nowrap; }
.bsub { position:absolute; left:66px; top:232px; font-size:27px; }
.strip { position:absolute; left:64px; top:300px; width:952px; height:66px; border-radius:18px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.16); display:flex; align-items:center; gap:18px; padding:0 22px; font-size:21px; white-space:nowrap; }
.strip .f { height:38px; padding:0 16px; border-radius:19px; border:1.5px solid rgba(0,201,255,0.6); color:#00c9ff; font-weight:700; font-size:17px; display:flex; align-items:center; gap:10px; }
.strip .f i { width:9px; height:9px; border-radius:50%; background:#00c9ff; display:block; }
.cell { position:absolute; width:460px; height:146px; border-radius:22px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.16); padding:20px 24px; }
.cell .k { font-size:15px; letter-spacing:0.2em; font-weight:700; color:#00c9ff; }
.cell .k b { color:rgba(255,255,255,0.5); margin-right:10px; }
.cell .v { margin-top:8px; font-size:19px; line-height:1.45; }
#scn { background:#fff; border-color:#fff; }
#scn .k { color:#0b1440; }
#scn .k b { color:rgba(11,20,64,0.5); }
#scn .v { color:#0b1440; font-weight:700; font-size:25px; line-height:1.3; margin-top:12px; display:flex; align-items:center; }
#caret { display:inline-block; width:3px; height:30px; background:#00c9ff; margin-left:4px; }
.nxt { position:absolute; left:64px; top:1072px; font-size:30px; }
"""
_cells = []
for i, (k, v) in enumerate(RULES):
    x = 64 if i % 2 == 0 else 556
    y = 390 + (i // 2) * 162
    _cells.append(f'    <div class="cell" id="c{i}" style="left:{x}px;top:{y}px"><div class="k"><b>{i + 1:02d}</b>{k}</div><div class="v w r">{v}</div></div>')
_cells.append('    <div class="cell" id="scn" style="left:556px;top:876px"><div class="k"><b>08</b>SCENE KAMU</div><div class="v"><span id="typed"></span><i id="caret"></i></div></div>')
S1_BODY = """    <div class="btitle"><span class="w b">Motion</span> <span class="hb">brief</span> <span class="c r">ku</span></div>
    <div class="bsub w r">Paste ini dulu, lalu tambahkan <span class="c b">satu scene</span> di akhir.</div>
    <div class="strip"><div class="f"><i></i>motion-brief.md</div><span class="w r">Buat motion graphic. Ikuti brief ini persis:</span></div>
""" + "\n".join(_cells) + """
    <div class="nxt"><span class="hb">16 scene</span> <span class="w r">yang aku pakai ada di slide berikutnya</span> <span class="c b">&rarr;</span></div>
"""
S1_JS = """
  const SC = %s;
  const cells = [0, 1, 2, 3, 4, 5, 6].map((i) => $("c" + i));
  function render(t) {
    const ph = t / D * 7;
    cells.forEach((el, i) => {
      const d = Math.min(Math.abs(ph - i - 0.5), 7 - Math.abs(ph - i - 0.5));
      const k = clamp(1 - d / 0.8, 0, 1);
      el.style.borderColor = "rgba(" + Math.round(mix(255, 0, k)) + "," + Math.round(mix(255, 201, k)) + ",255," + (0.16 + 0.7 * k).toFixed(3) + ")";
      el.style.background = "rgba(0,201,255," + (0.03 + 0.09 * k).toFixed(3) + ")";
      el.style.boxShadow = "0 18px 40px -18px rgba(0,201,255," + (0.6 * k).toFixed(3) + ")";
    });
    const idx = Math.floor(t / 1.5) %% 4, f = (t %% 1.5);
    const s = SC[idx], n = Math.round(s.length * clamp(f / 0.65, 0, 1));
    $("typed").textContent = s.slice(0, n);
    $("caret").style.opacity = (n < s.length || Math.floor(t * 3) %% 2 === 0) ? 1 : 0;
  }
""" % json.dumps(SCENES)

# ======================================================================== 2 · bars -> trend
BAR_H = [118, 168, 140, 214, 250, 300, 344]
BAR_X = [i * 66 for i in range(7)]
_tops = [(x + 23, 360 - h) for x, h in zip(BAR_X, BAR_H)]


def _smooth_path(pts):
    d = f"M{pts[0][0]} {pts[0][1]}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f},{c2[0]:.1f} {c2[1]:.1f},{p2[0]} {p2[1]}"
    return d


S2_CSS = """
.wd { position:absolute; left:36px; top:36px; width:880px; height:548px; border-radius:26px; background:rgba(255,255,255,0.07); border:1.5px solid rgba(255,255,255,0.16); }
.ico { position:absolute; left:36px; top:34px; width:56px; height:56px; border-radius:15px; background:linear-gradient(140deg,#5fe0ff,#00a2ff); display:flex; align-items:center; justify-content:center; box-shadow:0 10px 24px -8px rgba(0,201,255,0.8); }
.wl { position:absolute; left:108px; top:42px; font-size:30px; }
#chart { position:absolute; left:46px; top:130px; overflow:visible; }
.big { position:absolute; left:536px; top:190px; font-size:100px; line-height:1; letter-spacing:-0.04em; color:#00c9ff; font-weight:700; transform-origin:0 70%; }
.bigl { position:absolute; left:542px; top:312px; font-size:24px; }
.chipw { position:absolute; left:542px; top:370px; font-size:22px; }
"""
_bars = "".join(f'<rect id="b{i}" x="{x}" y="{360 - h}" width="46" height="{h}" rx="14" fill="url(#bg2)"/>'
                f'<rect x="{x + 8}" y="{360 - h + 10}" width="8" height="{max(10, h - 30)}" rx="4" fill="#fff" opacity="0.28" id="bh{i}"/>' for i, (x, h) in enumerate(zip(BAR_X, BAR_H)))
S2_VIS = f"""      <div class="wd">
        <div class="ico"><svg width="30" height="30" viewBox="0 0 30 30"><rect x="4" y="16" width="5" height="10" rx="2" fill="#fff"/><rect x="12.5" y="10" width="5" height="16" rx="2" fill="#fff"/><rect x="21" y="4" width="5" height="22" rx="2" fill="#fff"/></svg></div>
        <div class="wl w b">Pendaftar mingguan</div>
        <svg id="chart" width="440" height="380" viewBox="0 0 440 380">
          <defs><linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fe0ff"/><stop offset="1" stop-color="#0068ff"/></linearGradient>
            <filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter></defs>
          <line x1="0" y1="361" x2="440" y2="361" stroke="rgba(255,255,255,0.18)" stroke-width="2"/>
          {_bars}
          <path id="lng" d="{_smooth_path(_tops)}" fill="none" stroke="#00c9ff" stroke-width="12" stroke-linecap="round" filter="url(#gl)" opacity="0.8"/>
          <path id="ln" d="{_smooth_path(_tops)}" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
          <circle id="hd" r="11" fill="#0b1440" stroke="#fff" stroke-width="5"/>
        </svg>
        <div class="big" id="big">+0%</div>
        <div class="bigl w r">dalam 7 minggu terakhir</div>
        <div class="chipw"><span class="hb" id="chip" style="font-size:20px;padding:6px 16px">tren naik terus</span></div>
      </div>"""
S2_JS = """
  const ln = $("ln"), lng = $("lng"), L = ln.getTotalLength();
  for (let i = 0; i < 7; i++) {
    gsap.set(["#b" + i, "#bh" + i], { scaleY: 0, transformOrigin: "50% 100%" });
    tl.to(["#b" + i, "#bh" + i], { scaleY: 1, duration: 0.6, ease: "back.out(2.2)" }, 0.3 + i * 0.13);
    tl.to(["#b" + i, "#bh" + i], { scaleY: 0, duration: 0.4, ease: "power3.in" }, 5.25 + (6 - i) * 0.04);
  }
  function render(t) {
    const draw = smooth((t - 1.55) / 1.0) * (1 - smooth((t - 5.15) / 0.35));
    [ln, lng].forEach((p) => { p.setAttribute("stroke-dasharray", (draw * L).toFixed(1) + " " + (L + 5).toFixed(1)); });
    const hp = ln.getPointAtLength(draw * L), hd = $("hd");
    hd.setAttribute("cx", hp.x.toFixed(1)); hd.setAttribute("cy", hp.y.toFixed(1));
    hd.setAttribute("opacity", draw > 0.01 ? 1 : 0);
    const n = Math.round(200 * io3((t - 2.55) / 0.6));
    $("big").textContent = "+" + n + "%";
    const pop = t > 3.1 ? Math.exp(-6 * (t - 3.1)) * Math.sin(Math.min(Math.PI, (t - 3.1) * 10)) : 0;
    gsap.set("#big", { scale: 1 + 0.08 * pop, opacity: smooth((t - 2.45) / 0.2) * (1 - smooth((t - 5.2) / 0.3)) });
    gsap.set("#chip", { scale: backOut((t - 3.25) / 0.45, 2.5) * (1 - smooth((t - 5.15) / 0.25)), opacity: (t > 3.25 ? 1 : 0) * (1 - smooth((t - 5.15) / 0.25)) });
  }
"""

# ======================================================================== 3 · monthly -> yearly
MON, YR = "  149.000", "1.490.000"
S3_CSS = """
.tg { position:absolute; left:256px; top:44px; width:440px; height:76px; border-radius:38px; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.18); }
#pill { position:absolute; left:6px; top:6px; width:212px; height:61px; border-radius:31px; background:#fff; box-shadow:0 10px 24px -8px rgba(0,201,255,0.7); }
.tl { position:absolute; top:0; width:220px; line-height:73px; text-align:center; font-size:25px; font-weight:700; }
.pc { position:absolute; left:84px; top:160px; width:784px; height:400px; border-radius:32px; background:linear-gradient(150deg,rgba(255,255,255,0.13),rgba(255,255,255,0.05)); border:1.5px solid rgba(255,255,255,0.22); box-shadow:inset 0 1px 0 rgba(255,255,255,0.25), 0 40px 70px -30px rgba(0,0,0,0.6); }
.pico { position:absolute; left:44px; top:44px; width:84px; height:84px; border-radius:22px; background:#fff; display:flex; align-items:center; justify-content:center; box-shadow:0 14px 30px -10px rgba(0,201,255,0.7); }
.pn { position:absolute; left:148px; top:52px; font-size:46px; }
.pd { position:absolute; left:150px; top:110px; font-size:20px; color:#00c9ff; }
#badge { position:absolute; right:44px; top:58px; font-size:22px; padding:8px 18px; transform-origin:100% 50%; }
.price { position:absolute; right:44px; top:186px; display:flex; align-items:flex-start; }
.price .rp { font-size:40px; color:#00c9ff; font-weight:700; margin-top:20px; margin-right:8px; }
.dg { display:inline-block; height:130px; overflow:hidden; text-align:center; font-size:112px; line-height:130px; font-weight:700; letter-spacing:-0.03em; }
.dg span { display:block; height:130px; }
.per { position:absolute; right:44px; top:322px; width:200px; height:34px; font-size:24px; }
.per span { position:absolute; right:0; top:0; }
"""
_cols = "".join(f'<span class="dg" id="d{i}" data-layout-allow-overflow data-layout-allow-overlap><span class="w">{m if m != " " else "&nbsp;"}</span><span class="w">{y}</span></span>' for i, (m, y) in enumerate(zip(MON, YR)))
S3_VIS = f"""      <div class="tg"><div id="pill"></div><div class="tl" id="l0" style="left:2px">Bulanan</div><div class="tl" id="l1" style="left:218px">Tahunan</div></div>
      <div class="pc">
        <div class="pico"><svg width="44" height="40" viewBox="0 0 44 40"><path d="M10 2 H34 L42 13 L22 38 L2 13 Z" fill="#0b1440"/><path d="M2 13 H42 M14 2 L22 38 L30 2" fill="none" stroke="#00c9ff" stroke-width="2.5" stroke-linejoin="round"/></svg></div>
        <div class="pn w b">Pro</div><div class="pd r">Kelas AIpreneur</div>
        <span class="hb" id="badge">Gratis 2 bulan</span>
        <div class="price"><span class="rp">Rp</span>{_cols}</div>
        <div class="per r"><span class="w" id="pm">/ bulan</span><span class="w" id="py">/ tahun</span></div>
      </div>"""
S3_JS = """
  const MON = %s, YR = %s, N = MON.length;
  const W = (ch) => ch === " " ? 0 : (ch === "." ? 0.3 : 0.62);
  function rollK(t, i) {
    const r = N - 1 - i;
    const a = (t - 0.8 - r * 0.05) / 0.5, b = (t - 3.8 - r * 0.05) / 0.5;
    return clamp(backOut(a, 1.3), -0.2, 1.2) - clamp(backOut(b, 1.3), -0.2, 1.2);
  }
  function render(t) {
    const pk = backOut((t - 0.6) / 0.5, 1.2) - backOut((t - 3.6) / 0.5, 1.2);
    gsap.set("#pill", { x: 206 * pk });
    const c = clamp(pk, 0, 1);
    $("l0").style.color = "rgb(" + [mix(11, 255, c), mix(20, 255, c), mix(64, 255, c)].map(Math.round) + ")";
    $("l1").style.color = "rgb(" + [mix(255, 11, c), mix(255, 20, c), mix(255, 64, c)].map(Math.round) + ")";
    for (let i = 0; i < N; i++) {
      const k = rollK(t, i), el = $("d" + i), kk = clamp(k, 0, 1);
      el.style.width = (mix(W(MON[i]), W(YR[i]), kk) * 112).toFixed(1) + "px";
      gsap.set(el.children, { y: -130 * k });
      const blur = Math.abs(k - Math.round(k)) > 0.05 && k > 0.02 && k < 0.98 ? 3 : 0;
      el.style.filter = blur ? "blur(" + blur + "px)" : "none";
    }
    const y = smooth((t - 1.0) / 0.25) * (1 - smooth((t - 4.0) / 0.25));
    gsap.set("#pm", { opacity: 1 - y, y: -10 * y }); gsap.set("#py", { opacity: y, y: 10 * (1 - y) });
    const bk = backOut((t - 1.55) / 0.45, 2.6) * (1 - smooth((t - 3.65) / 0.2));
    gsap.set("#badge", { scale: Math.max(0, bk), opacity: t > 1.55 && t < 3.9 ? 1 : 0 });
  }
""" % (json.dumps(MON), json.dumps(YR))

# ======================================================================== 4 · dots -> logo
S4_CSS = """
#cv { position:absolute; left:0; top:0; }
#mark { position:absolute; left:%dpx; top:%dpx; width:%dpx; height:380px; overflow:hidden;
  background:linear-gradient(140deg,#7fe6ff,#00c9ff 45%%,#0a6cff);
  -webkit-mask:url("assets/amark.png") center / contain no-repeat; mask:url("assets/amark.png") center / contain no-repeat; opacity:0; }
#glint { position:absolute; top:-60px; left:0; width:140px; height:500px; background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,0.95),rgba(255,255,255,0)); transform:rotate(18deg); }
.halo { position:absolute; left:226px; top:110px; width:500px; height:400px; border-radius:50%%; background:radial-gradient(closest-side, rgba(0,201,255,0.32), rgba(0,201,255,0)); }
""" % (476 - 248, 310 - 190, 497)
S4_VIS = """      <div class="halo" id="halo"></div>
      <canvas id="cv" width="1904" height="1240" style="width:952px;height:620px"></canvas>
      <div id="mark"><div id="glint"></div></div>"""
S4_JS = """
  const PT = %s;
  const cv = $("cv"), ctx = cv.getContext("2d");
  const CX = 476, CY = 310, N = PT.length;
  let seed = 7; const rnd = () => { seed = (seed * 16807) %% 2147483647; return (seed - 1) / 2147483646; };
  const S = PT.map((p, i) => ({ tx: CX + p[0], ty: CY + p[1], a: i / N * TAU + rnd() * 0.3, rr: 220 + rnd() * 90, r: 10 + rnd() * 6, ph: rnd() * TAU, tone: rnd() }));
  S.sort((a, b) => a.r - b.r);
  function m(t) {
    if (t < 1.0) return 0;
    if (t < 2.1) return clamp(backOut((t - 1.0) / 1.1, 1.1), 0, 1.08);
    if (t < 4.9) return 1;
    return 1 - io3((t - 4.9) / 1.0);
  }
  function sphere(x, y, r, tone, a) {
    const g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.4, r * 0.1, x, y, r);
    g.addColorStop(0, "rgba(255,255,255," + a + ")");
    g.addColorStop(0.35, tone < 0.6 ? "rgba(0,201,255," + a + ")" : "rgba(70,150,255," + a + ")");
    g.addColorStop(1, tone < 0.6 ? "rgba(0,80,190," + a + ")" : "rgba(20,50,150," + a + ")");
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
  }
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0); ctx.clearRect(0, 0, 952, 620);
    const mk = m(t), rot = TAU * t / D;
    const solid = smooth((t - 2.1) / 0.35) * (1 - smooth((t - 4.6) / 0.3));
    for (const s of S) {
      const ang = s.a + rot, rr = s.rr + 12 * Math.sin(s.ph + t * 2);
      const rx = CX + rr * Math.cos(ang), ry = CY + rr * 0.82 * Math.sin(ang);
      const sw = Math.sin(Math.PI * clamp(mk, 0, 1)) * 50;
      const x = mix(rx, s.tx, mk) - sw * Math.sin(ang), y = mix(ry, s.ty, mk) + sw * Math.cos(ang);
      const r = mix(s.r, 9, clamp(mk, 0, 1)) * (1 - 0.6 * solid);
      sphere(x, y, Math.max(1, r), s.tone, (1 - solid).toFixed(3));
    }
    gsap.set("#mark", { opacity: solid, scale: 0.94 + 0.06 * solid });
    gsap.set("#glint", { x: -200 + 900 * io3((t - 2.75) / 0.8) });
    gsap.set("#halo", { opacity: 0.35 + 0.65 * smooth(clamp(mk, 0, 1)), scale: 0.9 + 0.1 * clamp(mk, 0, 1) });
  }
""" % json.dumps(APTS)

# ======================================================================== 5 · island -> live
STEPS5 = [("01", "Pill diam", "status kecil di atas layar"), ("02", "Hitung mundur", "3 &middot; 2 &middot; 1"),
          ("03", "LIVE", "kelas dimulai"), ("04", "Kembali ke pill", "siap untuk berikutnya")]
S5_CSS = """
.phone { position:absolute; left:84px; top:40px; width:320px; height:560px; border-radius:58px; background:#050a20; padding:10px; box-shadow:0 30px 60px -20px rgba(0,0,0,0.7), 0 0 0 2px rgba(255,255,255,0.12); }
.scr { position:absolute; left:10px; top:10px; right:10px; bottom:10px; border-radius:48px; overflow:hidden;
  background:radial-gradient(circle at 25% 30%, rgba(0,201,255,0.55), rgba(0,201,255,0) 45%), radial-gradient(circle at 80% 70%, rgba(40,90,255,0.6), rgba(40,90,255,0) 50%), linear-gradient(170deg,#183a7a,#0b1440); }
#isl { position:absolute; left:0px; top:12px; width:300px; height:212px; background:#040716; clip-path:inset(0 88px 176px 88px round 18px); }
.mini1 { position:absolute; left:100px; top:8px; width:20px; height:20px; border-radius:6px; background:#00c9ff; }
.mini2 { position:absolute; left:180px; top:8px; width:20px; height:20px; border-radius:50%; border:3.5px solid #00c9ff; border-right-color:transparent; }
.lab5 { position:absolute; left:26px; top:30px; font-size:17px; color:#00c9ff; font-weight:700; letter-spacing:0.12em; }
.flip { position:absolute; left:100px; top:62px; width:100px; height:124px; border-radius:18px; background:#fff; overflow:hidden; }
.flip span { display:block; height:124px; line-height:128px; text-align:center; font-size:96px; font-weight:700; color:#0b1440; }
.live { position:absolute; left:0; right:0; top:62px; display:flex; align-items:center; justify-content:center; gap:16px; font-size:60px; font-weight:700; letter-spacing:0.02em; }
.ldot { width:30px; height:30px; border-radius:50%; background:#00c9ff; }
.lsub { position:absolute; left:0; right:0; top:150px; text-align:center; font-size:18px; color:#00c9ff; }
.dock { position:absolute; left:20px; right:20px; bottom:20px; height:96px; border-radius:30px; background:rgba(255,255,255,0.14); display:flex; align-items:center; justify-content:space-around; }
.app { width:62px; height:62px; border-radius:17px; }
.tlv { position:absolute; left:500px; top:80px; }
.tlv .line { position:absolute; left:16px; top:20px; width:3px; height:390px; background:rgba(255,255,255,0.18); }
.stp { position:absolute; left:0; width:400px; height:110px; }
.stp .dt { position:absolute; left:4px; top:12px; width:27px; height:27px; border-radius:50%; border:3px solid rgba(255,255,255,0.5); background:#0b1440; }
.stp .n { position:absolute; left:58px; top:4px; font-size:16px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.stp .t { position:absolute; left:54px; top:28px; font-size:34px; font-weight:700; padding:0 10px; border-radius:8px; line-height:1.3; }
.stp .s { position:absolute; left:64px; top:78px; font-size:18px; color:rgba(255,255,255,0.7); }
"""
_steps5 = "".join(f'<div class="stp" id="p{i}" style="top:{i * 130}px"><div class="dt" id="pd{i}"></div><div class="n">{n}</div><div class="t" id="pt{i}">{t}</div><div class="s">{s}</div></div>'
                  for i, (n, t, s) in enumerate(STEPS5))
S5_VIS = f"""      <div class="phone"><div class="scr">
        <div id="isl">
          <div class="mini1" id="mi1"></div><div class="mini2" id="mi2"></div>
          <div id="cd"><div class="lab5">MULAI DALAM</div><div class="flip" data-layout-allow-overflow data-layout-allow-overlap><div id="fl"><span>3</span><span>2</span><span>1</span></div></div></div>
          <div id="lv"><div class="live"><div class="ldot" id="ld"></div><span class="w">LIVE</span></div><div class="lsub r">Kelas AIpreneur mulai sekarang</div></div>
        </div>
        <div class="dock"><div class="app" style="background:linear-gradient(140deg,#5fe0ff,#00a2ff)"></div><div class="app" style="background:linear-gradient(140deg,#ffffff,#c7d6f2)"></div><div class="app" style="background:linear-gradient(140deg,#2a5bd7,#0b1440)"></div><div class="app" style="background:linear-gradient(140deg,#00c9ff,#2a5bd7)"></div></div>
      </div></div>
      <div class="tlv"><div class="line"></div>{_steps5}</div>"""
S5_JS = """
  const ROUND = (k) => mix(18, 40, k);
  function render(t) {
    const open = backOut((t - 0.5) / 0.45, 1.3) * (1 - io3((t - 4.8) / 0.45));
    const k = clamp(open, 0, 1.06);
    const side = mix(88, 0, k), bot = mix(176, 0, k);
    $("isl").style.clipPath = "inset(0px " + side.toFixed(1) + "px " + bot.toFixed(1) + "px " + side.toFixed(1) + "px round " + ROUND(clamp(k, 0, 1)).toFixed(1) + "px)";
    const mini = 1 - smooth((k - 0.05) / 0.2);
    gsap.set(["#mi1", "#mi2"], { opacity: mini });
    gsap.set("#mi2", { rotation: t * 360 });
    const cdOn = env(t, 0.85, 2.95, 0.12), lvOn = env(t, 3.0, 4.75, 0.15);
    gsap.set("#cd", { opacity: cdOn });
    const f = t < 1.6 ? 0 : (t < 2.3 ? backOut((t - 1.6) / 0.35, 1.5) : 1 + backOut((t - 2.3) / 0.35, 1.5));
    gsap.set("#fl", { y: -124 * f });
    gsap.set("#lv", { opacity: lvOn, scale: 0.85 + 0.15 * backOut((t - 3.0) / 0.4, 2) });
    const pulse = 0.5 + 0.5 * Math.sin(TAU * t * 1.5);
    $("ld").style.boxShadow = "0 0 0 " + (6 + 10 * pulse).toFixed(1) + "px rgba(0,201,255," + (0.35 - 0.25 * pulse).toFixed(3) + ")";
    const act = [Math.max(env(t, -1, 0.85, 0.12)), env(t, 0.85, 3.0, 0.12), env(t, 3.0, 4.8, 0.12), env(t, 4.8, 7, 0.12)];
    act.forEach((a, i) => {
      const tt = $("pt" + i);
      tt.style.background = "rgba(255,255,255," + a.toFixed(3) + ")";
      tt.style.color = "rgb(" + [mix(255, 11, a), mix(255, 20, a), mix(255, 64, a)].map(Math.round) + ")";
      $("pd" + i).style.background = a > 0.5 ? "#00c9ff" : "#0b1440";
      $("pd" + i).style.borderColor = a > 0.5 ? "#00c9ff" : "rgba(255,255,255,0.5)";
      $("p" + i).style.opacity = (0.55 + 0.45 * a).toFixed(3);
    });
  }
"""

SLIDES = [
    dict(cid="s1", name="Motion brief", eyebrow="TEMPLATE &middot; PASTE DULUAN", page="01", css=S1_CSS, body=S1_BODY, js=S1_JS),
    dict(cid="s2", name="Bars trend", eyebrow="SCENE 01", page="02", css=S2_CSS, js=S2_JS,
         body=scene_body("Bars", "trend", "Bar yang berubah jadi tren",
                         'Widget chart kaca frosted <span class="ph">&ldquo;[metrik kamu]&rdquo;</span>. Tujuh bar muncul satu per satu dengan sedikit pantulan, garis bercahaya menggambar di atasnya, lalu <span class="ph">&ldquo;[angka growth kamu]&rdquo;</span> muncul besar.',
                         ["Pendaftar mingguan", "+200%"], S2_VIS)),
    dict(cid="s3", name="Monthly yearly", eyebrow="SCENE 02", page="03", css=S3_CSS, js=S3_JS,
         body=scene_body("Monthly", "yearly", "Switch harga bulanan ke tahunan",
                         'Toggle ala iOS (Bulanan | Tahunan) di atas kartu harga <span class="ph">&ldquo;[nama paket]&rdquo;</span>. Pill-nya meluncur dengan spring, harga berputar kayak odometer dari <span class="ph">[harga bulanan]</span> ke <span class="ph">[harga tahunan]</span>, dan badge <span class="ph">&ldquo;[promo]&rdquo;</span> muncul.',
                         ["Pro", "Rp149rb &rarr; Rp1,49jt", "Gratis 2 bulan"], S3_VIS)),
    dict(cid="s4", name="Dots logo", eyebrow="SCENE 03", page="04", css=S4_CSS, js=S4_JS,
         body=scene_body("Dots", "logo", "Titik yang menyatu jadi logo",
                         'Sekitar 150 bola glossy kecil masuk dari tepi, berputar sekali, lalu menyatu jadi <span class="ph">[logo kamu dalam satu kalimat]</span> yang berkilau kena cahaya.',
                         ["Logo AIpreneur"], S4_VIS)),
    dict(cid="s5", name="Island live", eyebrow="SCENE 04", page="05", css=S5_CSS, js=S5_JS,
         body=scene_body("Island", "live", "Hitung mundur live yang tumbuh dari pill",
                         'Pill hitam di atas layar HP membesar jadi live activity: hitung mundur 3, 2, 1, lalu titik berdenyut dan &ldquo;LIVE&rdquo; dengan <span class="ph">&ldquo;[nama event kamu]&rdquo;</span>. Setelah itu mengecil lagi jadi pill.',
                         ["Kelas AIpreneur mulai sekarang"], S5_VIS)),
]

import scenes2
SLIDES += scenes2.make(scene_body)
import scenes3
SLIDES += scenes3.make(scene_body)
import scenes4
_cover, _tail = scenes4.make(scene_body)
SLIDES = [_cover] + SLIDES + _tail
for _i, _s in enumerate(SLIDES):
    _s["page"] = f"{_i + 1:02d}"
    _s.setdefault("right", "GESER &rarr;")
    _s.setdefault("extra", "")

if __name__ == "__main__":
    for s in SLIDES:
        html = SHELL
        for k in ("cid", "name", "eyebrow", "page", "css", "body", "js", "right", "extra"):
            html = html.replace("%%" + k.upper() + "%%", s[k])
        html = html.replace("%%TOTAL%%", f"{TOTAL:02d}")
        d = ROOT / "slides" / s["cid"]
        d.mkdir(parents=True, exist_ok=True)
        for sub in ("assets", "vendor"):
            if (d / sub).exists():
                shutil.rmtree(d / sub)
            shutil.copytree(ROOT / sub, d / sub)
        if s["cid"] == "s0" and (ROOT / "cover_tiles").exists():
            shutil.copytree(ROOT / "cover_tiles", d / "assets" / "tiles")
        (d / "index.html").write_text(html)
        print("wrote", d / "index.html")
