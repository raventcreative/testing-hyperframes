"""Scene 05 (Line -> draw) and the carousel cover (slide 01) — imported by build.py."""
import shutil
from pathlib import Path

# ---------------------------------------------------------------- 05 line -> draw
S05_CSS = """
.wid { position:absolute; left:36px; top:36px; right:36px; bottom:44px; border-radius:30px;
  background:linear-gradient(170deg,#ffffff,#f7f9fd); box-shadow:0 30px 60px -24px rgba(18,21,50,0.30), 0 4px 14px rgba(39,73,118,0.08); overflow:hidden; }
.wlab { position:absolute; left:46px; top:40px; font-size:32px; }
.wval { position:absolute; left:44px; top:86px; font-size:70px; letter-spacing:-0.02em; line-height:1; }
.gl { position:absolute; left:0; right:0; height:0; border-top:2px dashed rgba(39,73,118,0.13); }
.lchip { position:absolute; right:34px; top:36px; padding:12px 24px; border-radius:16px; background:rgba(79,134,232,0.15); font-size:32px; }
#chart { position:absolute; left:0; bottom:40px; overflow:visible; }
"""
S05_VIS = """        <div class="wid" id="wid">
          <div class="gl" style="top:212px"></div><div class="gl" style="top:330px"></div><div class="gl" style="top:448px"></div>
          <div class="wlab g r">Pendapatan bulanan</div>
          <div class="wval g r" id="wval">Rp48.240.000</div>
          <div class="lchip" id="lchip"><span class="g b">+128%</span></div>
          <svg id="chart" width="732" height="360" viewBox="0 0 732 360">
            <defs>
              <linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#274976"/><stop offset="0.55" stop-color="#4f86e8"/><stop offset="1" stop-color="#7fd0ff"/></linearGradient>
              <linearGradient id="areag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4f86e8" stop-opacity="0.38"/><stop offset="1" stop-color="#4f86e8" stop-opacity="0"/></linearGradient>
              <clipPath id="ac"><rect id="acr" x="0" y="0" width="732" height="360"/></clipPath>
              <filter id="glow" x="-1" y="-1" width="3" height="3"><feGaussianBlur stdDeviation="7"/></filter>
            </defs>
            <path id="area" clip-path="url(#ac)" fill="url(#areag)" d="M0 300 C 90 300, 140 215, 230 220 S 340 285, 420 248 S 540 130, 610 96 S 676 30, 704 22 L 704 360 L 0 360 Z"/>
            <path id="ln" fill="none" stroke="url(#lg)" stroke-width="8" stroke-linecap="round" d="M0 300 C 90 300, 140 215, 230 220 S 340 285, 420 248 S 540 130, 610 96 S 676 30, 704 22"/>
            <circle id="hglow" r="22" fill="#7fd0ff" opacity="0.7" filter="url(#glow)"/>
            <circle id="head" r="11" fill="#ffffff" stroke="#4f86e8" stroke-width="6"/>
          </svg>
        </div>"""
S05_JS = """
  const ln = document.getElementById("ln"), L = ln.getTotalLength();
  const FULL = 48240000;
  const io = (p) => { p = clamp(p, 0, 1); return p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; };
  const fmt = (v) => "Rp" + Math.round(v).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, ".");
  function seg(t) {
    if (t < 2.0) return [0, 1];
    if (t < 2.85) return [io((t - 2.0) / 0.85), 1];
    if (t < 3.0) return [1, 1];
    if (t < 5.3) return [0, io((t - 3.0) / 2.3)];
    return [0, 1];
  }
  function render(t) {
    const [a, b] = seg(t);
    ln.setAttribute("stroke-dasharray", "0 " + (a * L).toFixed(2) + " " + Math.max(0, (b - a) * L).toFixed(2) + " " + (L + 10).toFixed(1));
    ln.setAttribute("opacity", b - a > 0.002 ? 1 : 0);
    const x0 = ln.getPointAtLength(a * L).x, x1 = ln.getPointAtLength(b * L).x;
    const r = document.getElementById("acr");
    r.setAttribute("x", x0.toFixed(1)); r.setAttribute("width", Math.max(0, x1 - x0).toFixed(1));
    const drawing = t >= 3.0 && t < 5.45;
    const hp = ln.getPointAtLength(b * L);
    const ho = drawing ? clamp((t - 3.0) / 0.15, 0, 1) * (t > 5.3 ? 1 - (t - 5.3) / 0.15 : 1) : (t < 2.0 || t >= 5.45 ? 1 : 0);
    ["head", "hglow"].forEach((id) => { const c = document.getElementById(id); c.setAttribute("cx", hp.x.toFixed(1)); c.setAttribute("cy", hp.y.toFixed(1)); c.setAttribute("opacity", ((id === "hglow" ? 0.7 : 1) * clamp(ho, 0, 1) * (b > a ? 1 : 0)).toFixed(3)); });
    let v = FULL;
    if (t >= 2.0 && t < 3.0) v = FULL * (1 - a);
    else if (t >= 3.0 && t < 5.3) v = FULL * Math.pow(b, 1.3);
    document.getElementById("wval").textContent = fmt(v);
  }
  tl.to("#lchip", { opacity: 0, scale: 0.85, duration: 0.25, ease: "power2.in" }, 1.9);
  tl.fromTo("#lchip", { opacity: 0, scale: 0.6, y: 10 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(2.2)", immediateRender: false }, 5.3);
"""

SLIDES_C = [
    dict(cid="s05", num="05", page="06", name="Line draw", w1="Line", w2="draw",
         sub="Grafik yang menggambar dirinya sendiri", panel="light", css=S05_CSS, visual=S05_VIS, js=S05_JS,
         body='Widget revenue frosted <b class="b">&ldquo;[metrik kamu]&rdquo;</b> dengan angka live <b class="b">&ldquo;[angka kamu]&rdquo;</b>. Satu garis gradasi menggambar grafik dari kiri ke kanan dengan ujung bercahaya, area di bawahnya terisi, dan chip <b class="b">&ldquo;[+x%]&rdquo;</b> mendarat di akhir.',
         used='<div class="used g r"><b class="b">Aku pakai:</b> Pendapatan bulanan, Rp48.240.000, +128%.</div>'),
]

# ---------------------------------------------------------------- cover (slide 01)
SCENES = [
    ("01", "Particles", "logo"), ("02", "Gradient", "flow"), ("03", "Glass", "tilt"), ("04", "Globe", "arcs"),
    ("05", "Line", "draw"), ("06", "Shape", "morph"), ("07", "Grid", "wave"), ("08", "Cards", "shuffle"),
    ("09", "Number", "roll"), ("10", "Ribbon", "twist"), ("11", "Liquid", "merge"), ("12", "Phone", "explode"),
    ("13", "Rings", "orbit"), ("14", "Words", "kinetic"), ("15", "Button", "pay"), ("16", "Confetti", "burst"),
]
GX, GY, TW, TH, GAP = 62, 300, 230, 232, 12
MX, MY, MW, MH = 10, 10, 210, 183  # media box inside tile

COVER = """<!doctype html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1350" />
<title>AIpreneur — Cover</title>
<script src="vendor/gsap/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/shared.css" />
<style>
.ctitle { position:absolute; left:60px; top:110px; height:104px; font-size:84px; line-height:104px; letter-spacing:-0.04em; white-space:nowrap; display:flex; }
.cw { position:relative; display:inline-block; height:104px; overflow:hidden; margin-left:22px; width:440px; }
.cw span { position:absolute; left:0; top:0; display:block; }
.csub { position:absolute; left:63px; top:222px; font-size:27px; display:flex; align-items:center; gap:14px; }
.csub .dot { width:36px; height:36px; border-radius:50%; background:var(--ink-grad); color:#fff; font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; }
.tile { position:absolute; width:{TW}px; height:{TH}px; border-radius:20px; background:rgba(255,255,255,0.9);
  box-shadow:0 16px 30px -18px rgba(18,21,50,0.35), 0 2px 8px rgba(39,73,118,0.08); }
.tile .lb { position:absolute; left:14px; bottom:11px; font-size:17px; white-space:nowrap; }
.tile .lb .no { font-size:13px; letter-spacing:0.1em; margin-right:8px; }
.tile .lb .ar { margin:0 6px; opacity:0.6; }
.tv { position:absolute; width:{MW}px; height:{MH}px; border-radius:13px; object-fit:cover; }
</style>
</head>
<body>
<div id="root" data-composition-id="s00" data-start="0" data-duration="6" data-width="1080" data-height="1350" data-fps="30">
  <div id="ui" class="clip" data-start="0" data-duration="6" data-track-index="0" data-track-kind="graphics" style="position:absolute;inset:0">
    <div class="bg"></div>
    <div class="logo" id="logo"></div>
    <div class="eyebrow g b" id="eyebrow">16 SCENE</div>
    <div class="ctitle" id="ctitle"><span class="g b">Claude Motion</span><span class="cw" data-layout-allow-overflow data-layout-allow-overlap>
      <span class="g r" id="w0">Graphics</span><span class="g r" id="w1">Effects</span><span class="g r" id="w2">Particles</span><span class="g r" id="w3">Physics</span></span></div>
    <div class="csub"><span class="g r">16 animasi premium yang bisa kamu clone.</span><span class="dot">FK</span><span class="g b">Freddie Kashawan</span></div>
{tiles}
    <div class="foot" id="foot">
      <div class="who"><div class="dot">FK</div><span class="g b">FREDDIE KASHAWAN</span><span class="g r">AIpreneur</span></div>
      <div class="pg g b">01 / 18 &nbsp;&nbsp; GESER &rarr;</div>
    </div>
  </div>
{videos}
</div>
<script>
(function () {
  const tl = gsap.timeline({ paused: true });
  const W = ["#w0", "#w1", "#w2", "#w3"];
  gsap.set(W.slice(1), { yPercent: 110 });
  for (let i = 0; i < 4; i++) {
    const at = 1.5 * (i + 1) - 0.25, cur = W[i], nxt = W[(i + 1) % 4];
    tl.to(cur, { yPercent: -110, duration: 0.3, ease: "power3.in" }, at);
    tl.fromTo(nxt, { yPercent: 110 }, { yPercent: 0, duration: 0.42, ease: "back.out(1.6)", immediateRender: false }, at + 0.22);
  }
  tl.set({}, {}, 6);
  window.__timelines = window.__timelines || {};
  window.__timelines["s00"] = tl;
})();
</script>
</body>
</html>
"""


def tile_xy(i):
    r, c = divmod(i, 4)
    return GX + c * (TW + GAP), GY + r * (TH + GAP)


def build_cover(root: Path):
    tiles, videos = [], []
    for i, (no, w1, w2) in enumerate(SCENES):
        x, y = tile_xy(i)
        tiles.append(
            f'    <div class="tile" id="t{no}" style="left:{x}px;top:{y}px" data-layout-allow-overlap>'
            f'<div class="lb"><span class="no g r">{no}</span><span class="g b">{w1}</span><span class="ar g r">&rarr;</span><span class="g r">{w2}</span></div></div>')
        videos.append(
            f'  <video id="v{no}" class="clip tv" data-start="0" data-duration="6" data-track-index="{i + 1}" '
            f'src="assets/tiles/s{no}.mp4" muted playsinline style="left:{x + MX}px;top:{y + MY}px;z-index:5"></video>')
    html = COVER.replace("{TW}", str(TW)).replace("{TH}", str(TH)).replace("{MW}", str(MW)).replace("{MH}", str(MH))
    html = html.replace("{tiles}", "\n".join(tiles)).replace("{videos}", "\n".join(videos))
    d = root / "slides" / "s00"
    d.mkdir(parents=True, exist_ok=True)
    for sub in ("assets", "vendor"):
        if (d / sub).exists():
            shutil.rmtree(d / sub)
        shutil.copytree(root / sub, d / sub)
    if (root / "cover_tiles").exists():
        shutil.copytree(root / "cover_tiles", d / "assets" / "tiles")
    (d / "index.html").write_text(html)
    print("wrote", d / "index.html")
