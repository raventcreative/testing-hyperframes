"""Builds the 5-slide 'Agent Architecture' carousel into slides/sN/index.html.
Run: python3 build.py"""
import math
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

SHELL = """<!doctype html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1350" />
<title>AIpreneur — %%NAME%%</title>
<script src="vendor/gsap/dist/gsap.min.js"></script>
<script src="assets/minis.js"></script>
<link rel="stylesheet" href="assets/shared.css" />
<style>
%%CSS%%
</style>
</head>
<body>
<div id="root" data-composition-id="%%CID%%" data-start="0" data-duration="7" data-width="1080" data-height="1350" data-fps="30">
  <div id="stage" class="clip" data-start="0" data-duration="7" data-track-index="0" data-track-kind="graphics" style="position:absolute;inset:0">
    <div class="bg"></div>
    <div class="logo" id="logo"></div>
    <div class="eyebrow g b" id="eyebrow">%%EYEBROW%%</div>
%%BODY%%
    <div class="foot" id="foot">
      <div class="who"><div class="av">FK</div><span class="g b">Freddie Kashawan</span></div>
      <div class="pg g b">%%RIGHT%%</div>
    </div>
    <div class="strip"></div>
  </div>
</div>
<script>
(function () {
  const D = 7, TAU = Math.PI * 2;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const smooth = (p) => { p = clamp(p, 0, 1); return p * p * (3 - 2 * p); };
  const env = (t, a, b, f) => { f = f || 0.18; return smooth((t - a) / f) * (1 - smooth((t - b) / f)); };
  const mixc = (a, b, k) => a.map((v, i) => Math.round(v + (b[i] - v) * k));
  const $ = (id) => document.getElementById(id);
  const WHITE = [255, 255, 255], ICE = [219, 231, 255], ICE2 = [196, 216, 252], NAVY = [18, 21, 50], AZ = [79, 134, 232];
  function hl(el, k, base) {
    k = clamp(k, 0, 1); base = base || WHITE;
    el.style.background = "rgb(" + mixc(base, base === WHITE ? ICE : ICE2, k) + ")";
    el.style.borderColor = "rgb(" + mixc(NAVY, AZ, k) + ")";
    el.style.boxShadow = k > 0.01 ? "0 0 0 " + (5 * k).toFixed(1) + "px rgba(79,134,232," + (0.2 * k).toFixed(3) + "), 0 14px 28px -12px rgba(79,134,232," + (0.75 * k).toFixed(3) + ")" : "none";
  }
  function glow(el, k) {
    k = clamp(k, 0, 1);
    el.style.boxShadow = k > 0.01 ? "0 0 0 " + (6 * k).toFixed(1) + "px rgba(79,134,232," + (0.28 * k).toFixed(3) + "), 0 16px 30px -10px rgba(79,134,232," + (0.8 * k).toFixed(3) + ")" : "none";
  }
  const pcache = {};
  function along(id, p) {
    if (!pcache[id]) { const el = $(id); pcache[id] = { el, L: el.getTotalLength() }; }
    const r = pcache[id];
    return r.el.getPointAtLength(clamp(p, 0, 1) * r.L);
  }
  function dot(id, pathId, p, o) {
    const pt = along(pathId, p), c = $(id);
    c.setAttribute("cx", pt.x.toFixed(1)); c.setAttribute("cy", pt.y.toFixed(1)); c.setAttribute("opacity", clamp(o, 0, 1).toFixed(3));
  }
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

INK_DEF = '<linearGradient id="{p}-ink" x1="0" x2="1"><stop offset="0" stop-color="#121532"/><stop offset="1" stop-color="#274976"/></linearGradient>'


def txt(x, y, s, size, p, bold=True, anchor="middle", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="url(#{p}-ink)" {extra}>{s}</text>'


def spill(cx, cy, w, h, label, p, size=12, dark=False):
    x, y = cx - w / 2, cy - h / 2
    if dark:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="url(#{p}-ink)"/>'
                f'<text x="{cx}" y="{cy + size*0.36}" font-size="{size}" font-weight="700" text-anchor="middle" fill="#fff" letter-spacing="1">{label}</text>')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#fff" stroke="#121532" stroke-width="2"/>'
            + txt(cx, cy + size * 0.36, label, size, p, extra='letter-spacing="1"'))


def mini_harness(p, size):
    s = [f'<svg width="{size}" height="{size}" viewBox="0 0 300 300"><defs>{INK_DEF.format(p=p)}</defs>']
    s.append('<rect x="78" y="78" width="144" height="144" fill="none" stroke="#121532" stroke-width="2" stroke-dasharray="6 5"/>')
    br = []
    for (x, y, dx, dy) in [(60, 60, 1, 1), (240, 60, -1, 1), (60, 240, 1, -1), (240, 240, -1, -1)]:
        br.append(f'<path d="M{x} {y + 26*dy} V{y} H{x + 26*dx}" fill="none" stroke="#4f86e8" stroke-width="5" stroke-linecap="round"/>')
    s.append(f'<g id="{p}-br">{"".join(br)}</g>')
    routes = ["M150 44 V105", "M58 150 H105", "M242 150 H195", "M150 256 V195"]
    for i, d in enumerate(routes):
        s.append(f'<path id="{p}-r{i}" d="{d}" stroke="#121532" stroke-width="2" fill="none"/>')
    s.append(f'<rect id="{p}-llm" x="105" y="105" width="90" height="90" rx="18" fill="#dbe7ff" stroke="#121532" stroke-width="3"/>')
    s.append(txt(150, 159, "LLM", 26, p))
    s.append(spill(150, 30, 74, 26, "TOOLS", p))
    s.append(spill(150, 270, 74, 26, "EVALS", p))
    s.append(spill(36, 150, 68, 26, "RULES", p))
    s.append(spill(262, 150, 76, 26, "MEMORY", p, size=11))
    for i in range(4):
        s.append(f'<circle id="{p}-d{i}" r="6" fill="#4f86e8" stroke="#fff" stroke-width="2" opacity="0"/>')
    s.append("</svg>")
    return "".join(s)


def mini_loop(p, size):
    s = [f'<svg width="{size}" height="{size}" viewBox="0 0 300 300"><defs>{INK_DEF.format(p=p)}</defs>']
    s.append('<circle cx="150" cy="150" r="95" fill="none" stroke="#e1e9f6" stroke-width="14"/>')
    s.append('<circle cx="150" cy="150" r="95" fill="none" stroke="#121532" stroke-width="1.6" stroke-dasharray="2 6" opacity="0.6"/>')
    s.append(f'<circle id="{p}-arc" cx="150" cy="150" r="95" fill="none" stroke="#4f86e8" stroke-width="7" stroke-linecap="round" transform="rotate(-90 150 150)"/>')
    for i, (x, y) in enumerate([(150, 55), (245, 150), (150, 245), (55, 150)]):
        s.append(f'<circle id="{p}-n{i}" cx="{x}" cy="{y}" r="8" fill="#fff" stroke="#121532" stroke-width="2.5"/>')
    s.append(txt(150, 36, "PLAN", 13, p))
    s.append(txt(268, 155, "ACT", 13, p, anchor="start"))
    s.append(txt(150, 276, "CHECK", 13, p))
    s.append(txt(32, 155, "FIX", 13, p, anchor="end"))
    s.append(spill(150, 142, 92, 32, "AGENT", p, size=14, dark=True))
    s.append(txt(150, 182, "SAMPAI SELESAI", 10, p, extra='letter-spacing="1.2"'))
    s.append(f'<circle id="{p}-hd" r="9" fill="#ffffff" stroke="#4f86e8" stroke-width="4"/>')
    s.append("</svg>")
    return "".join(s)


def mini_graph(p, size):
    s = [f'<svg width="{size}" height="{size}" viewBox="0 0 300 300"><defs>{INK_DEF.format(p=p)}</defs>']
    edges = ["M150 42 C150 65,95 62,95 85", "M150 42 C150 65,205 62,205 85", "M95 115 C95 140,60 135,60 160",
             "M95 115 C95 140,150 135,150 160", "M205 115 C205 140,150 135,150 160", "M205 115 C205 140,240 135,240 160",
             "M60 190 C60 225,150 215,150 240", "M150 190 V240", "M240 190 C240 225,150 215,150 240"]
    for d in edges:
        s.append(f'<path d="{d}" stroke="#121532" stroke-width="2" fill="none"/>')
    s.append(f'<path id="{p}-retry" d="M256 175 C292 160,292 112,221 100" stroke="#4f86e8" stroke-width="2" fill="none" stroke-dasharray="4 4"/>')
    s.append(txt(287, 138, "RETRY", 9, p, bold=True, extra='transform="rotate(90 287 138)" letter-spacing="1.5"'))
    s.append(f'<path id="{p}-ra" d="M150 42 C150 65,95 62,95 85 L95 115 C95 140,150 135,150 160 L150 240" fill="none" stroke="none"/>')
    s.append(f'<path id="{p}-rb" d="M150 42 C150 65,205 62,205 85 L205 115 C205 140,240 135,240 160 L240 190 C240 225,150 215,150 240" fill="none" stroke="none"/>')
    s.append(spill(150, 30, 74, 26, "START", p, dark=True))
    for i, (x, y) in enumerate([(95, 100), (205, 100), (60, 175), (150, 175), (240, 175)]):
        s.append(f'<rect id="{p}-n{i}" x="{x-15}" y="{y-15}" width="30" height="30" rx="7" fill="#fff" stroke="#121532" stroke-width="2.5"/>'
                 f'<circle cx="{x}" cy="{y}" r="4" fill="#121532"/>')
    s.append(f'<g id="{p}-n5" opacity="0.82"><rect x="116" y="240" width="68" height="26" rx="13" fill="#4f86e8"/>'
             f'<text x="150" y="257.5" font-size="12" font-weight="700" text-anchor="middle" fill="#fff" letter-spacing="1">END</text></g>')
    s.append(f'<circle id="{p}-tk" r="7" fill="#4f86e8" stroke="#fff" stroke-width="2.5"/>')
    s.append(f'<circle id="{p}-rt" r="4" fill="#4f86e8" opacity="0"/>')
    s.append("</svg>")
    return "".join(s)


def box(id_, x, y, w, h, t, s="", cls=""):
    sub = f'<div class="s g r">{s}</div>' if s else ""
    tcls = "t" if "eval" in cls else "t g"
    scls = "s" if "eval" in cls else "s g r"
    sub = f'<div class="{scls}">{s}</div>' if s else ""
    return f'    <div class="box {cls}" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="{tcls}">{t}</div>{sub}</div>'


# ======================================================================== S1 cover
S1_CSS = """
.card .kick { position:absolute; left:26px; top:334px; font-size:16px; letter-spacing:0.18em; }
.card .nm { position:absolute; left:24px; top:360px; font-size:50px; letter-spacing:-0.03em; }
.card .ds { position:absolute; left:26px; top:430px; font-size:20px; }
.card .dg { position:absolute; left:8px; top:10px; }
"""
_cards = [("h", 74, "#274976", "THE SCAFFOLD", "Harness", "membungkus model", mini_harness),
          ("l", 392, "#4f86e8", "THE CYCLE", "Loop", "ulang sampai selesai", mini_loop),
          ("g", 710, "#121532", "THE MAP", "Graph", "atur tiap langkah", mini_graph)]
S1_BODY = "".join(
    f'    <div class="card" id="c{p}" style="left:{x}px;top:170px;width:296px;height:490px;box-shadow:12px 12px 0 {sh}">'
    f'<div class="dg">{fn(p, 274)}</div><div class="kick g b">{k}</div><div class="nm g b">{n}</div><div class="ds g r">{d}</div></div>\n'
    for p, x, sh, k, n, d, fn in _cards)
S1_BODY += """    <div class="vs" style="left:353px;top:400px">vs</div>
    <div class="vs" style="left:671px;top:400px">vs</div>
    <div class="headline" style="top:712px;font-size:104px;line-height:1.15"><span class="g b">Harness</span> <span class="g r dim">vs</span> <span class="g b">Loop</span> <span class="g r dim">vs</span></div>
    <div class="headline" style="top:830px;font-size:104px;line-height:1.15"><span class="hlbar"><span class="g b">Graph Engineering.</span></span></div>
    <div class="headline" style="top:985px;font-size:34px"><span class="g r">3 cara membangun AI agent.</span> <span class="g b">Kamu pakai yang mana? &rarr;</span></div>
    <div style="position:absolute;left:0;right:0;top:1066px;display:flex;justify-content:center;gap:14px">
      <div class="chip" style="position:static"><span class="g r">context + tools</span></div>
      <div class="chip" style="position:static"><span class="g r">plan &rarr; act &rarr; check</span></div>
      <div class="chip" style="position:static"><span class="g r">nodes + edges</span></div>
    </div>
"""
S1_JS = """
  function render(t) { Minis.harness("h", t); Minis.loop("l", t); Minis.graph("g", t); }
"""

# ======================================================================== S2 harness
S2_CSS = """
.eq { position:absolute; top:198px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:18px; font-size:28px; }
.eq .p { height:58px; padding:0 30px; border-radius:29px; border:3px solid #121532; display:flex; align-items:center; background:#fff; }
.eq .p.m { background:#dbe7ff; }
.eq .p.h { background:linear-gradient(100deg,#121532,#274976); border-color:transparent; color:#fff; }
.sub2 { position:absolute; left:70px; right:70px; top:284px; text-align:center; font-size:24px; line-height:1.45; }
#model { position:absolute; left:410px; top:630px; width:260px; height:200px; border-radius:26px; border:4px solid #121532; background:#dbe7ff; }
#model .mt { position:absolute; left:0; right:0; top:34px; text-align:center; font-size:60px; line-height:1; letter-spacing:-0.01em; }
#model .ms { position:absolute; left:0; right:0; top:104px; text-align:center; font-size:17px; }
.status { position:absolute; left:50%; top:142px; height:32px; margin-left:-90px; width:180px; border-radius:16px; background:linear-gradient(100deg,#121532,#274976); }
.status span { position:absolute; left:0; right:0; top:0; line-height:32px; text-align:center; color:#fff; font-weight:700; font-size:14px; letter-spacing:0.14em; opacity:0; }
#fail { position:absolute; left:732px; top:902px; width:30px; height:30px; border-radius:50%; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-size:17px; font-weight:700; display:flex; align-items:center; justify-content:center; opacity:0; z-index:4; }
.retry { position:absolute; left:330px; top:850px; font-size:15px; }
#wires { position:absolute; left:0; top:0; }
"""
S2_BODY = """    <div class="headline" style="top:96px;font-size:80px;line-height:1.2"><span class="g b">Harness</span> <span class="hlbar"><span class="g r">Engineering</span></span></div>
    <div class="eq"><div class="p"><span class="g b">Agent</span></div><span class="g r">=</span><div class="p m"><span class="g b">Model</span></div><span class="g r">+</span><div class="p h b">Harness</div></div>
    <div class="sub2"><span class="g r">Model yang berpikir. Harness yang menentukan </span><span class="g b">apa yang dilihat</span><span class="g r">, </span><span class="g b">apa yang bisa disentuh</span><span class="g r">, dan </span><span class="g b">bagaimana hasilnya dicek.</span></div>
    <div class="frame" style="left:64px;top:412px;width:952px;height:698px;box-shadow:12px 12px 0 #4f86e8"></div>
    <div class="band" style="left:92px;top:445px;width:896px;height:116px"></div>
    <div class="band" style="left:92px;top:898px;width:896px;height:104px"></div>
    <div class="lbl g b" style="left:114px;top:470px">GUIDES</div><div class="lbl" style="left:114px;top:496px"><span class="g r" style="margin-left:0">yang diikuti</span></div>
    <div class="lbl g b" style="left:96px;top:586px">CONTEXT<span class="r">yang dilihat</span></div>
    <div class="lbl g b" style="left:738px;top:586px">TOOLS<span class="r">yang disentuh</span></div>
    <div class="lbl g b" style="left:96px;top:866px">SENSORS<span class="r">cara dicek</span></div>
    <svg id="wires" width="1080" height="1350">
      <g fill="none" stroke="#121532" stroke-width="2.5">
        <path d="M540 440 V630"/>
        <path id="c0" d="M342 653 C380 653,376 730,410 730"/><path id="c1" d="M342 731 C376 731,376 730,410 730"/><path id="c2" d="M342 809 C380 809,376 730,410 730"/>
        <path id="t0" d="M670 730 C704 730,700 653,738 653"/><path id="t1" d="M670 730 C704 730,704 731,738 731"/><path id="t2" d="M670 730 C704 730,700 809,738 809"/>
        <path id="oc" d="M600 830 V915"/>
        <path d="M352 950 H520"/><path d="M750 950 H800"/><path d="M885 842 V915"/>
        <path id="vo" d="M232 985 V1062 H330 V1090"/>
      </g>
      <g fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-dasharray="6 6">
        <path id="g0" d="M410 541 C410 590,470 590,470 630"/><path id="g1" d="M690 541 C690 585,610 590,610 630"/><path id="g2" d="M885 541 V566 H660 C642 566,640 590,640 630"/>
        <path id="rt" d="M540 915 V830"/>
      </g>
      <g fill="#4f86e8" stroke="#fff" stroke-width="2.5">
        <circle id="dc0" r="7" opacity="0"/><circle id="dc1" r="7" opacity="0"/><circle id="dc2" r="7" opacity="0"/>
        <circle id="dg0" r="7" opacity="0"/><circle id="dg1" r="7" opacity="0"/><circle id="dg2" r="7" opacity="0"/>
        <circle id="dt0" r="7" opacity="0"/><circle id="dt1" r="7" opacity="0"/><circle id="dt2" r="7" opacity="0"/>
        <circle id="doc" r="7" opacity="0"/><circle id="drt" r="7" opacity="0"/><circle id="dvo" r="7" opacity="0"/>
      </g>
    </svg>
""" + "\n".join([
    box("bsys", 300, 470, 220, 70, "System prompt", "peran + aturan"),
    box("bagt", 600, 470, 180, 70, "AGENTS.md", "konvensi tim"),
    box("bcon", 800, 470, 170, 70, "Constraints", "batas keras"),
    box("bmem", 92, 620, 250, 66, "Memory", "sesi sebelumnya"),
    box("bret", 92, 698, 250, 66, "Retrieval", "dokumen yang tepat"),
    box("bfil", 92, 776, 250, 66, "Files &amp; state", "working set"),
    box("btoo", 738, 620, 250, 66, "Tool registry", "yang bisa dipanggil"),
    box("bsan", 738, 698, 250, 66, "Sandbox", "eksekusi aman"),
    box("bper", 738, 776, 250, 66, "Permissions", "izin sebelum berisiko"),
    box("btes", 112, 915, 240, 70, "Tests &amp; evals", "berhasil?"),
    box("bout", 520, 915, 230, 70, "Output checks", "schema + lint"),
    box("btra", 800, 915, 170, 70, "Traces", "log tiap langkah"),
]) + """
    <div id="model"><div class="mt g b">MODEL</div><div class="ms g r">berpikir + memutuskan</div>
      <div class="status"><span id="s0">MEMBACA</span><span id="s1">BERPIKIR</span><span id="s2">PAKAI TOOLS</span><span id="s3">MENGECEK</span><span id="s4">MEMPERBAIKI</span><span id="s5">MENGIRIM</span></div></div>
    <div id="fail">&times;</div>
    <div class="retry g r">&#8635; retry + feedback</div>
    <div class="tag" style="left:92px;top:395px">THE HARNESS</div>
    <div class="pill" style="left:445px;top:392px;width:190px"><span class="g b">USER TASK &darr;</span></div>
    <div class="pill" id="pver" style="left:205px;top:1090px;width:250px"><span class="g b">&#10003; VERIFIED OUTPUT</span></div>
    <div class="headline" style="top:1160px;font-size:36px"><span class="g b">Model sama.</span> <span class="g r dim">Harness lebih baik.</span> <span class="hlbar"><span class="g b">Agent lebih baik.</span></span></div>
"""
S2_JS = """
  const PH = [0, 1.15, 2.3, 3.45, 4.6, 5.75, 7];
  const ctxB = ["bmem", "bret", "bfil"].map($), tooB = ["btoo", "bsan", "bper"].map($), guiB = ["bsys", "bagt", "bcon"].map($);
  const model = $("model");
  function flow(ids, paths, t0, rev) {
    ids.forEach((id, i) => {
      const q = (st.t - t0 - 0.1 - i * 0.1) / 0.75;
      const o = q > 0 && q < 1 ? Math.min(1, q * 6) * (1 - smooth((q - 0.85) / 0.15)) : 0;
      dot(id, paths[i], rev ? 1 - smooth(q) : smooth(q), o);
    });
  }
  function render(t) {
    const ph = PH.findIndex((v, i) => t >= v && t < PH[i + 1]);
    for (let i = 0; i < 6; i++) gsap.set("#s" + i, { opacity: i === ph ? 1 : 0 });
    const e = (i) => env(t, PH[i], PH[i + 1] - 0.05);
    ctxB.forEach((el) => hl(el, e(0)));
    guiB.forEach((el) => hl(el, e(1)));
    tooB.forEach((el) => hl(el, e(2)));
    hl($("bout"), Math.max(e(3), e(5)));
    hl($("btes"), e(5));
    hl($("btra"), e(2) * 0.6 + e(5) * 0.6);
    const pulse = 0.5 + 0.5 * Math.sin(TAU * t * 1.6);
    model.style.boxShadow = "0 0 0 " + (8 * Math.max(e(1), e(4)) * (0.6 + 0.4 * pulse)).toFixed(1) + "px rgba(79,134,232,0.25), 0 20px 40px -16px rgba(79,134,232," + (0.3 + 0.5 * Math.max(e(1), e(4))).toFixed(3) + ")";
    model.style.borderColor = "rgb(" + mixc(NAVY, AZ, Math.max(e(1), e(4))) + ")";
    flow(["dc0", "dc1", "dc2"], ["c0", "c1", "c2"], PH[0]);
    flow(["dg0", "dg1", "dg2"], ["g0", "g1", "g2"], PH[1]);
    flow(["dt0", "dt1", "dt2"], ["t0", "t1", "t2"], PH[2]);
    flow(["doc"], ["oc"], PH[3]);
    flow(["drt"], ["rt"], PH[4] + 0.15);
    flow(["dvo"], ["vo"], PH[5] + 0.2);
    gsap.set("#fail", { opacity: env(t, 3.9, PH[4] - 0.05, 0.12), scale: 0.6 + 0.4 * smooth((t - 3.9) / 0.15) });
    glow($("pver"), env(t, 6.3, 7.2));
  }
"""

# ======================================================================== S3 loop
CX, CY, R = 540, 690, 215
ANG = [-90, -18, 54, 126, 198]


def _pt(a, r=R):
    return CX + r * math.cos(math.radians(a)), CY + r * math.sin(math.radians(a))


_chev = []
for a in [-54, 18, 90, 162, 234]:
    x, y = _pt(a)
    _chev.append(f'<path d="M-6 -7 L4 0 L-6 7" transform="translate({x:.1f} {y:.1f}) rotate({a + 90})" fill="none" stroke="#121532" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
_marks = "".join(f'<circle id="mk{i}" cx="{_pt(a)[0]:.1f}" cy="{_pt(a)[1]:.1f}" r="11" fill="#fff" stroke="#121532" stroke-width="3"/>' for i, a in enumerate(ANG))
S3_CSS = """
.code { position:absolute; left:50%; top:196px; transform:translateX(-50%); height:60px; padding:0 30px; border-radius:16px; background:#fff; border:2.5px solid #121532; display:flex; align-items:center; font-size:25px; white-space:nowrap; box-shadow:6px 6px 0 #4f86e8; }
.sub3 { position:absolute; left:70px; right:70px; top:284px; text-align:center; font-size:25px; line-height:1.45; }
#ring { position:absolute; left:0; top:0; }
.disc { position:absolute; left:410px; top:560px; width:260px; height:260px; border-radius:50%; background:#fff; border:3px solid #121532; box-shadow:0 20px 50px -20px rgba(18,21,50,0.35); }
.disc .k { position:absolute; left:0; right:0; top:44px; text-align:center; font-size:15px; letter-spacing:0.24em; }
.disc .n { position:absolute; left:58px; top:62px; width:110px; height:96px; overflow:hidden; }
.disc .n span { position:absolute; right:0; top:0; font-size:86px; line-height:96px; letter-spacing:-0.03em; }
.disc .of { position:absolute; left:170px; top:116px; font-size:24px; }
.disc .gl { position:absolute; left:0; right:0; top:166px; text-align:center; font-size:15px; }
.bar { position:absolute; left:40px; width:180px; top:194px; height:12px; border-radius:6px; background:#e1e9f6; overflow:hidden; }
.bar i { position:absolute; left:0; top:0; bottom:0; width:180px; border-radius:6px; background:linear-gradient(90deg,#274976,#4f86e8); transform-origin:0 50%; }
.dots3 { position:absolute; left:0; right:0; top:216px; display:flex; justify-content:center; gap:9px; }
.dots3 b { width:12px; height:12px; border-radius:50%; border:2px solid #274976; background:#fff; }
.sc { position:absolute; width:226px; height:86px; background:#fff; border:2.5px solid #121532; border-radius:16px; padding:10px 16px; }
.sc .no { font-size:14px; }
.sc .t { font-size:25px; line-height:1.1; letter-spacing:0.02em; }
.sc .s { font-size:14px; opacity:0.85; }
.donep { position:absolute; left:84px; top:420px; width:160px; height:58px; border-radius:29px; border:3px solid #121532; background:#fff; font-size:22px; letter-spacing:0.14em; display:flex; align-items:center; justify-content:center; }
#doneOn { position:absolute; left:84px; top:420px; width:160px; height:58px; border-radius:29px; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-weight:700; font-size:22px; letter-spacing:0.14em; display:flex; align-items:center; justify-content:center; opacity:0; }
.dchip { position:absolute; left:200px; top:571px; height:30px; padding:0 12px; border-radius:15px; font-weight:700; font-size:13px; letter-spacing:0.12em; display:flex; align-items:center; color:#fff; background:linear-gradient(100deg,#121532,#274976); opacity:0; z-index:3; }
.panel3 { position:absolute; top:990px; height:172px; background:#fff; border:2.5px solid #121532; border-radius:20px; padding:16px 22px; }
.panel3 .h { font-size:16px; letter-spacing:0.18em; margin-bottom:8px; }
.panel3 .row { display:flex; align-items:center; gap:12px; font-size:20px; height:36px; white-space:nowrap; }
.panel3 .ic { width:28px; height:28px; border-radius:8px; background:#dbe7ff; border:2px solid #274976; display:flex; align-items:center; justify-content:center; font-size:15px; font-weight:700; }
"""


def _sc(i, x, y, no, t, s):
    return f'    <div class="sc" id="sc{i}" style="left:{x}px;top:{y}px"><div class="no g r">{no}</div><div class="t g b">{t}</div><div class="s g r">{s}</div></div>'


S3_BODY = f"""    <div class="headline" style="top:96px;font-size:80px;line-height:1.2"><span class="g b">Loop</span> <span class="hlbar"><span class="g r">Engineering</span></span></div>
    <div class="code"><span class="g b">while</span><span class="g r">&nbsp;(!goal_met) {{ observe &rarr; reason &rarr; act &rarr; check }}</span></div>
    <div class="sub3"><span class="g r">Berhenti nge-prompt tiap langkah. Desain loop-nya: </span><span class="g b">goal yang jelas</span><span class="g r">, </span><span class="g b">cek tiap putaran</span><span class="g r">, dan </span><span class="g b">batas keras.</span></div>
    <svg id="ring" width="1080" height="1350">
      <circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="rgba(219,231,255,0.8)" stroke-width="40"/>
      <circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#121532" stroke-width="2.2" stroke-dasharray="2 8" stroke-linecap="round" opacity="0.7"/>
      {''.join(_chev)}
      <circle id="parc" cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#4f86e8" stroke-width="7" stroke-linecap="round" transform="rotate(-90 {CX} {CY})"/>
      <path id="dn" d="M296 600 L196 478" fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-dasharray="6 6"/>
      {_marks}
      <circle id="hd" r="12" fill="#fff" stroke="#4f86e8" stroke-width="5"/>
      <circle id="dtk" r="8" fill="#4f86e8" stroke="#fff" stroke-width="2.5" opacity="0"/>
    </svg>
""" + "\n".join([
    _sc(0, 427, 384, "01", "OBSERVE", "state + error"),
    _sc(1, 786, 584, "02", "REASON", "rencanakan langkah"),
    _sc(2, 700, 884, "03", "ACT", "edit &middot; run &middot; tools"),
    _sc(3, 154, 884, "04", "CHECK", "tests &middot; evals"),
    _sc(4, 70, 584, "05", "DECIDE", "goal? stop : loop"),
]) + """
    <div class="lbl" style="left:90px;top:388px;font-size:15px;letter-spacing:0.02em;font-weight:400"><span class="g r" style="margin:0;font-size:15px">keluar saat goal tercapai</span></div>
    <div class="donep"><span class="g b">DONE &#10003;</span></div><div id="doneOn">DONE &#10003;</div>
    <div class="dchip" id="chLoop">LOOP &#8635;</div><div class="dchip" id="chStop">STOP &#10003;</div>
    <div class="disc"><div class="k g b">ITERASI</div>
      <div class="n"><span class="g b" id="it0">01</span><span class="g b" id="it1">02</span><span class="g b" id="it2">03</span></div><div class="of g r">/ 10</div>
      <div class="gl"><span class="g r">goal: tests passing </span><span class="g b" id="pass">0/12</span></div>
      <div class="bar"><i id="barf"></i></div>
      <div class="dots3"><b id="lp0"></b><b id="lp1"></b><b id="lp2"></b></div></div>
    <div class="panel3" style="left:64px;width:456px;box-shadow:9px 9px 0 #4f86e8"><div class="h g b">STOP CONDITIONS</div>
      <div class="row"><div class="ic"><span class="g b">&#10003;</span></div><span class="g b">Goal:</span><span class="g r">semua test hijau</span></div>
      <div class="row"><div class="ic"><span class="g b">&#8635;</span></div><span class="g b">Max</span><span class="g r">10 putaran / 30 menit</span></div>
      <div class="row"><div class="ic"><span class="g b">$</span></div><span class="g b">Hard</span><span class="g r">token budget</span></div></div>
    <div class="panel3" style="left:552px;width:464px;box-shadow:9px 9px 0 #121532"><div class="h g b">MEMORY ANTAR PUTARAN</div>
      <div class="row"><div class="ic"><span class="g b">&#9998;</span></div><span class="g r">progress.md</span><span class="g b">yang sudah selesai</span></div>
      <div class="row"><div class="ic"><span class="g b">&#8916;</span></div><span class="g r">git commit</span><span class="g b">tiap putaran</span></div>
      <div class="row"><div class="ic"><span class="g b">&#9675;</span></div><span class="g b">Context baru tiap putaran</span></div></div>
    <div class="headline" style="top:1196px;font-size:36px"><span class="g b">Prompt memulai.</span> <span class="hlbar"><span class="g b">Loop menyelesaikan.</span></span></div>
"""
S3_JS = f"""
  const CX = {CX}, CY = {CY}, R = {R}, C = 2 * Math.PI * R;
  const ANG = {ANG}, F = [0, 0.2, 0.4, 0.6, 0.8];
  const sc = [0, 1, 2, 3, 4].map((i) => $("sc" + i));
  function render(t) {{
    const lap = t < 6 ? Math.floor(t / 2) : 2;
    const frac = t < 6 ? (t % 2) / 2 : 1;
    const a = (-90 + 360 * frac) * Math.PI / 180;
    $("parc").setAttribute("stroke-dasharray", (frac * C).toFixed(1) + " " + C.toFixed(1));
    const hd = $("hd");
    hd.setAttribute("cx", (CX + R * Math.cos(a)).toFixed(1)); hd.setAttribute("cy", (CY + R * Math.sin(a)).toFixed(1));
    hd.setAttribute("opacity", t < 6 ? 1 : 1 - smooth((t - 6) / 0.2));
    const idx = Math.min(4, Math.floor(frac * 5 + 1e-6));
    sc.forEach((el, i) => hl(el, t < 6 ? (i === idx ? smooth((frac - F[i]) * 5 / 0.25) : 0) : (i === 4 ? 1 - smooth((t - 6.5) / 0.3) : 0)));
    F.forEach((f, i) => $("mk" + i).setAttribute("fill", frac >= f && !(t >= 6.6) ? "#4f86e8" : "#ffffff"));
    for (let i = 0; i < 3; i++) gsap.set("#it" + i, {{ yPercent: i === lap ? 0 : (i < lap ? -110 : 110) }});
    const passing = lap * 4 + (frac >= 0.6 ? 4 : 0);
    $("pass").textContent = passing + "/12";
    const prevPass = lap * 4, k = smooth((frac - 0.6) * 5 / 0.6);
    const shown = frac >= 0.6 ? prevPass + 4 * k : prevPass;
    gsap.set("#barf", {{ scaleX: Math.max(0.001, shown / 12) }});
    for (let i = 0; i < 3; i++) $("lp" + i).style.background = (i < lap || (i === lap && frac >= 0.8)) ? "#4f86e8" : "#ffffff";
    const atDecide = frac >= 0.8 && t < 6.9;
    gsap.set("#chLoop", {{ opacity: atDecide && lap < 2 ? 1 : 0 }});
    gsap.set("#chStop", {{ opacity: atDecide && lap === 2 ? 1 : 0 }});
    const dq = (t - 6.0) / 0.45;
    dot("dtk", "dn", smooth(dq), dq > 0 && dq < 1.2 ? 1 - smooth((dq - 1) / 0.2) : 0);
    const dk = smooth((t - 6.35) / 0.2) * (1 - smooth((t - 6.85) / 0.12));
    gsap.set("#doneOn", {{ opacity: dk, scale: 1 + 0.06 * Math.sin(Math.PI * clamp((t - 6.35) / 0.3, 0, 1)) }});
  }}
"""

# ======================================================================== S4 graph
R1 = [(540, 427), (540, 502), (540, 600), (250, 600), (250, 712), (250, 822), (250, 912), (250, 978), (540, 978)]
K1 = [(0.2, 0), (0.55, 1), (0.85, 1), (1.15, 2), (1.35, 3), (1.55, 4), (1.9, 4), (2.15, 5), (2.55, 5), (2.8, 6), (3.0, 6), (3.15, 7), (3.35, 8)]
R2 = [(540, 427), (540, 502), (540, 600), (650, 600), (650, 712), (650, 768), (760, 768), (760, 822), (760, 916), (860, 916),
      (960, 916), (960, 822), (860, 822), (760, 822), (760, 916), (760, 978), (540, 978)]
K2 = [(3.55, 0), (3.8, 1), (4.0, 1), (4.2, 2), (4.3, 3), (4.5, 4), (4.7, 4), (4.8, 5), (4.9, 6), (5.05, 7), (5.25, 7), (5.45, 8), (5.7, 8),
      (5.8, 9), (5.9, 10), (6.0, 11), (6.1, 12), (6.2, 13), (6.35, 13), (6.5, 14), (6.6, 14), (6.7, 15), (6.85, 16)]
R3 = [(540, 600), (870, 600), (870, 712), (870, 768), (760, 768)]
K3 = [(4.2, 0), (4.45, 1), (4.6, 2), (4.7, 2), (4.8, 3), (4.9, 4)]
N1 = {0: "nst", 1: "ncl", 2: "nrt", 4: "npo", 5: "nhu", 6: "nrf", 8: "nen"}
N2 = {0: "nst", 1: "ncl", 2: "nrt", 4: "nsd", 7: "ndr", 8: "nqc", 13: "ndr", 14: "nqc", 16: "nen"}
N3 = {2: "npt"}
S4_CSS = """
.sub4 { position:absolute; left:60px; right:60px; top:206px; text-align:center; font-size:24px; line-height:1.45; }
.leg { position:absolute; top:298px; left:0; right:0; display:flex; justify-content:center; gap:10px; }
.leg div { height:44px; padding:0 16px; border-radius:22px; background:#fff; border:2px solid rgba(18,21,50,0.14); display:flex; align-items:center; gap:9px; font-size:17px; }
.leg i { width:18px; height:18px; border-radius:5px; border:2.5px solid #121532; display:inline-block; }
#gw { position:absolute; left:0; top:0; }
.ticket { position:absolute; left:372px; top:752px; width:268px; height:104px; border-radius:16px; background:#fff; border:2px solid rgba(18,21,50,0.16); padding:12px 16px; }
.ticket .h { font-size:13px; letter-spacing:0.14em; }
.ticket .q { font-size:18px; line-height:1.3; margin-top:4px; }
.qchip { position:absolute; left:868px; top:868px; height:28px; padding:0 10px; border-radius:14px; font-size:14px; font-weight:700; display:flex; align-items:center; opacity:0; background:#dbe7ff; border:2px solid #4f86e8; z-index:3; white-space:nowrap; }
.state { position:absolute; left:64px; top:1040px; width:952px; height:124px; border-radius:20px; background:rgba(219,231,255,0.7); border:2.5px solid #121532; padding:12px 20px; }
.state .h { font-size:16px; letter-spacing:0.18em; }
.state .cp { position:absolute; right:22px; top:13px; font-size:15px; }
.cells { position:absolute; left:20px; right:20px; top:46px; display:flex; gap:12px; }
.cell { flex:1; height:62px; border-radius:12px; background:#fff; border:2px solid rgba(18,21,50,0.14); padding:6px 14px; }
.cell .k { font-size:13px; }
.cell .v { font-size:19px; white-space:nowrap; }
.pillx { position:absolute; height:44px; border-radius:22px; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:17px; letter-spacing:0.16em; background:linear-gradient(100deg,#121532,#274976); }
.diam { position:absolute; left:512px; top:572px; width:56px; height:56px; }
.cpk { position:absolute; width:24px; height:24px; border-radius:6px; background:#121532; }
.cpk::after { content:""; position:absolute; left:7px; top:7px; width:10px; height:10px; border-radius:3px; background:#8fb4ec; }
.elab { position:absolute; font-size:15px; padding:2px 10px; border-radius:10px; background:#fff; border:1.5px solid rgba(18,21,50,0.15); white-space:nowrap; }
"""


def _poly(pts):
    return "M" + " L".join(f"{x} {y}" for x, y in pts)


S4_BODY = ("""    <div class="headline" style="top:96px;font-size:80px;line-height:1.2"><span class="g b">Graph</span> <span class="hlbar"><span class="g r">Engineering</span></span></div>
    <div class="sub4"><span class="g b">Node</span><span class="g r"> mengerjakan tugas. </span><span class="g b">Edge</span><span class="g r"> menentukan apa yang jalan berikutnya. </span><span class="g b">Shared state</span><span class="g r"> membawa semuanya di antara mereka.</span></div>
    <div class="leg">
      <div><i style="background:#dbe7ff"></i><span class="g r">LLM</span></div><div><i></i><span class="g r">Tool</span></div>
      <div><i style="border-style:dashed"></i><span class="g r">Human</span></div><div><i style="transform:rotate(45deg) scale(0.8);background:#121532"></i><span class="g r">Router</span></div>
      <div><i style="background:#121532"></i><span class="g r">Eval</span></div><div><i style="background:#121532;box-shadow:inset 0 0 0 4px #121532, inset 0 0 0 9px #8fb4ec"></i><span class="g r">Checkpoint</span></div>
    </div>
    <div class="frame" style="left:64px;top:380px;width:952px;height:636px;box-shadow:12px 12px 0 #4f86e8"></div>
    <div class="tag" style="left:92px;top:363px">CONTOH &middot; SUPPORT AGENT</div>
    <svg id="gw" width="1080" height="1350">
      <g fill="none" stroke="#121532" stroke-width="2.5">
        <path d="M540 449 V470"/><path d="M540 534 V572"/>
        <path d="M512 600 H250 V680"/><path d="M568 600 H870 V680"/><path d="M650 600 V680"/>
        <path d="M250 744 V790"/><path d="M250 854 V880"/><path d="M250 944 V978 H480"/>
        <path d="M650 744 V768 H870 V744"/><path d="M760 768 V790"/>
        <path d="M760 854 V884"/><path d="M760 948 V978 H600"/>
      </g>
      <path d="M860 916 H960 V822 H860" fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-dasharray="6 6"/>
      <path id="r1" d="%%R1%%" fill="none" stroke="none"/><path id="r2" d="%%R2%%" fill="none" stroke="none"/><path id="r3" d="%%R3%%" fill="none" stroke="none"/>
      <circle id="tk1" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
      <circle id="tk2" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
      <circle id="tk3" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
    </svg>
    <div class="pillx" id="nst" style="left:480px;top:405px;width:120px">START</div>
    <div class="pillx" id="nen" style="left:480px;top:956px;width:120px">END</div>
    <svg class="diam" id="nrt" viewBox="0 0 56 56"><path id="nrtp" d="M28 2 L54 28 L28 54 L2 28 Z" fill="#121532"/></svg>
    <div class="cpk" style="left:528px;top:541px"></div><div class="cpk" style="left:238px;top:755px"></div><div class="cpk" style="left:748px;top:857px"></div>
    <div class="elab" style="left:388px;top:572px"><span class="g r">refund</span></div>
    <div class="elab" style="left:612px;top:572px"><span class="g r">question</span></div>
    <div class="elab" style="left:440px;top:640px"><span class="g r">route(state.intent) &rarr;</span></div>
    <div class="elab" style="left:712px;top:632px"><span class="g r">parallel &rArr;</span></div>
    <div class="elab" style="left:905px;top:856px"><span class="g r">retry</span></div>
""" + "\n".join([
    box("ncl", 440, 470, 200, 64, "Classify ticket", "llm &middot; tentukan intent", "llm"),
    box("npo", 150, 680, 200, 64, "Check policy", "tool &middot; eligible?"),
    box("nhu", 124, 790, 252, 64, "&#10074;&#10074; Human approval", "interrupt &middot; menunggu", "human"),
    box("nrf", 150, 880, 200, 64, "Issue refund", "tool &middot; payments"),
    box("nsd", 560, 680, 180, 64, "Search docs", "tool &middot; retrieval"),
    box("npt", 780, 680, 180, 64, "Past tickets", "tool &middot; history"),
    box("ndr", 660, 790, 200, 64, "Draft reply", "llm &middot; gabungkan", "llm"),
    box("nqc", 660, 884, 200, 64, "Quality check", "eval &middot; score &ge; 0.85", "eval"),
]) + """
    <div class="ticket"><div class="h g b" id="th1">TIKET MASUK &middot; RUN 1</div><div class="h g b abs" id="th2" style="top:12px;left:16px;opacity:0">TIKET MASUK &middot; RUN 2</div>
      <div class="q g r" id="tq1">&ldquo;Aku kena charge dua kali. Tolong refund.&rdquo;</div><div class="q g r abs" id="tq2" style="top:34px;left:16px;right:16px;opacity:0">&ldquo;Gimana cara export data ke CSV?&rdquo;</div></div>
    <div class="qchip" id="qf"><span class="g b">&lt; 0.85 &times;</span></div><div class="qchip" id="qp"><span class="g b">&ge; 0.85 &#10003;</span></div>
    <div class="state"><div class="h g b">SHARED STATE</div><div class="cp g r" id="cpn">checkpoint #0 &middot; tersimpan</div>
      <div class="cells">
        <div class="cell" id="ce0"><div class="k g r">intent</div><div class="v g b" id="sv0">&mdash;</div></div>
        <div class="cell" id="ce1"><div class="k g r">context</div><div class="v g b" id="sv1">&mdash;</div></div>
        <div class="cell" id="ce2"><div class="k g r">review</div><div class="v g b" id="sv2">&mdash;</div></div>
        <div class="cell" id="ce3"><div class="k g r">result</div><div class="v g b" id="sv3">&mdash;</div></div>
      </div></div>
    <div class="headline" style="top:1196px;font-size:36px"><span class="g b">Prompt menyarankan.</span> <span class="hlbar"><span class="g b">Edge yang memaksa.</span></span></div>
""").replace("%%R1%%", _poly(R1)).replace("%%R2%%", _poly(R2)).replace("%%R3%%", _poly(R3))


def _cum(pts):
    out, s = [0.0], 0.0
    for (a, b), (c, d) in zip(pts, pts[1:]):
        s += math.hypot(c - a, d - b)
        out.append(s)
    return [round(v / s, 5) for v in out]


S4_JS = """
  const RUNS = [
    { path: "r1", tok: "tk1", F: %%F1%%, K: %%K1%%, N: %%N1%% },
    { path: "r2", tok: "tk2", F: %%F2%%, K: %%K2%%, N: %%N2%% },
    { path: "r3", tok: "tk3", F: %%F3%%, K: %%K3%%, N: %%N3%% },
  ];
  const BASE = { ncl: ICE, ndr: ICE };
  const EV = [
    [0.0, null, ["\\u2014", "\\u2014", "\\u2014", "\\u2014"], 0],
    [0.6, 0, "\\"refund\\"", 1], [1.6, 1, "policy_ok: true", 2], [2.2, 2, "human: approved", 3], [2.85, 3, "refunded \\u2713", 4],
    [3.5, null, ["\\u2014", "\\u2014", "\\u2014", "\\u2014"], 0],
    [3.85, 0, "\\"question\\"", 1], [4.95, 1, "docs: 2 \\u00b7 tickets: 3", 2], [5.3, 2, "draft v1", 3], [6.3, 2, "draft v2", 4], [6.8, 3, "terkirim \\u2713", 5],
  ];
  function prog(K, F, t) {
    if (t < K[0][0] || t > K[K.length - 1][0] + 0.25) return null;
    for (let i = 0; i < K.length - 1; i++) {
      const [ta, ia] = K[i], [tb, ib] = K[i + 1];
      if (t >= ta && t <= tb) { const k = (t - ta) / (tb - ta); return F[ia] + (F[ib] - F[ia]) * k; }
    }
    return F[K[K.length - 1][1]];
  }
  const nodeIds = ["nst", "ncl", "npo", "nhu", "nrf", "nsd", "npt", "ndr", "nqc", "nen", "nrt"];
  function render(t) {
    const act = {};
    RUNS.forEach((r) => {
      const p = prog(r.K, r.F, t);
      const o = p === null ? 0 : Math.min(1, (t - r.K[0][0]) * 8) * (1 - smooth((t - r.K[r.K.length - 1][0]) / 0.25));
      dot(r.tok, r.path, p === null ? 0 : p, o);
      const seen = {};
      r.K.forEach(([tk, ix]) => { const id = r.N[ix]; if (!id) return; const s = seen[id + ix] || (seen[id + ix] = [tk, tk]); s[0] = Math.min(s[0], tk); s[1] = Math.max(s[1], tk); });
      Object.keys(seen).forEach((key) => { const id = key.replace(/[0-9]+$/, ""); const [a, b] = seen[key]; act[id] = Math.max(act[id] || 0, env(t, a - 0.05, b + 0.3, 0.12)); });
    });
    nodeIds.forEach((id) => {
      const k = act[id] || 0, el = $(id);
      if (id === "nst" || id === "nen" || id === "nqc") glow(el, k);
      else if (id === "nrt") $("nrtp").setAttribute("fill", "rgb(" + mixc(NAVY, AZ, k) + ")");
      else hl(el, k, BASE[id] || WHITE);
    });
    const run2 = t >= 3.45;
    gsap.set(["#th1", "#tq1"], { opacity: run2 ? 0 : 1 }); gsap.set(["#th2", "#tq2"], { opacity: run2 ? 1 : 0 });
    let vals = ["\\u2014", "\\u2014", "\\u2014", "\\u2014"], cp = 0; const last = [-9, -9, -9, -9];
    EV.forEach(([te, ci, v, n]) => { if (t < te) return; if (ci === null) { vals = v.slice(); cp = n; last.fill(-9); } else { vals[ci] = v; last[ci] = te; cp = n; } });
    for (let i = 0; i < 4; i++) {
      $("sv" + i).textContent = vals[i];
      const k = env(t, last[i], last[i] + 0.8, 0.1);
      const c = $("ce" + i);
      c.style.borderColor = "rgba(" + mixc([200, 205, 220], AZ, k) + ",1)"; c.style.background = "rgb(" + mixc(WHITE, ICE, k) + ")";
    }
    $("cpn").textContent = "checkpoint #" + cp + " \\u00b7 tersimpan";
    gsap.set("#qf", { opacity: env(t, 5.5, 5.85, 0.08) }); gsap.set("#qp", { opacity: env(t, 6.6, 6.95, 0.08) });
  }
""".replace("%%F1%%", str(_cum(R1))).replace("%%F2%%", str(_cum(R2))).replace("%%F3%%", str(_cum(R3))) \
   .replace("%%K1%%", str([list(k) for k in K1])).replace("%%K2%%", str([list(k) for k in K2])).replace("%%K3%%", str([list(k) for k in K3])) \
   .replace("%%N1%%", str({str(k): v for k, v in N1.items()}).replace("'", '"')) \
   .replace("%%N2%%", str({str(k): v for k, v in N2.items()}).replace("'", '"')) \
   .replace("%%N3%%", str({str(k): v for k, v in N3.items()}).replace("'", '"'))

# ======================================================================== S5 CTA
S5_CSS = """
.mc { position:absolute; top:130px; width:268px; height:300px; background:#fff; border:3px solid #121532; border-radius:24px; }
.mc .dg { position:absolute; left:19px; top:4px; }
.mc .lb { position:absolute; left:0; right:0; bottom:16px; text-align:center; font-size:30px; }
.mc .lb .r { font-size:17px; margin-right:6px; }
.comment { position:absolute; left:0; right:0; top:486px; text-align:center; font-size:58px; letter-spacing:-0.02em; }
#send { position:absolute; left:250px; top:576px; width:580px; height:210px; border-radius:38px; background:#dbe7ff; border:5px solid #121532; box-shadow:14px 14px 0 #4f86e8; display:flex; align-items:center; justify-content:center; }
#send span { font-size:180px; line-height:1; letter-spacing:-0.02em; margin-top:14px; }
.dm { position:absolute; left:0; right:0; top:826px; text-align:center; font-size:34px; }
#inp { position:absolute; left:150px; top:908px; width:780px; height:84px; border-radius:42px; background:#fff; border:3px solid #121532; }
#inp .av { position:absolute; left:14px; top:13px; width:52px; height:52px; box-shadow:none; }
.ph { position:absolute; left:86px; top:0; line-height:78px; font-size:28px; }
.typed { position:absolute; left:86px; top:0; line-height:78px; font-size:28px; display:flex; }
.typed span { opacity:0; }
#caret { width:3px; height:34px; margin-top:22px; margin-left:3px; background:#274976; opacity:0; }
#sbtn { position:absolute; right:14px; top:13px; width:52px; height:52px; border-radius:50%; background:#eef3fb; display:flex; align-items:center; justify-content:center; }
#sbtnOn { position:absolute; right:14px; top:13px; width:52px; height:52px; border-radius:50%; background:linear-gradient(135deg,#4f86e8,#274976); display:flex; align-items:center; justify-content:center; opacity:0; }
#fol { position:absolute; left:150px; top:1032px; width:780px; height:150px; border-radius:26px; background:#fff; border:3px solid #121532; box-shadow:10px 10px 0 #121532; }
#fol .av { position:absolute; left:26px; top:31px; width:88px; height:88px; font-size:28px; }
#fol .n { position:absolute; left:140px; top:30px; font-size:32px; }
#fol .d { position:absolute; left:140px; top:80px; font-size:18px; line-height:1.35; width:400px; }
.fb { position:absolute; right:26px; top:47px; height:56px; width:172px; border-radius:28px; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:700; }
#fb1 { background:linear-gradient(100deg,#121532,#274976); color:#fff; }
#fb2 { background:#fff; border:2.5px solid #121532; opacity:0; }
"""
S5_BODY = (
    f'    <div class="mc" style="left:116px;box-shadow:9px 9px 0 #274976"><div class="dg">{mini_harness("a", 226)}</div><div class="lb"><span class="g r">01</span><span class="g b">Harness</span></div></div>\n'
    f'    <div class="mc" style="left:406px;box-shadow:9px 9px 0 #4f86e8"><div class="dg">{mini_loop("b", 226)}</div><div class="lb"><span class="g r">02</span><span class="g b">Loop</span></div></div>\n'
    f'    <div class="mc" style="left:696px;box-shadow:9px 9px 0 #121532"><div class="dg">{mini_graph("c", 226)}</div><div class="lb"><span class="g r">03</span><span class="g b">Graph</span></div></div>\n'
    """    <div class="vs" style="left:375px;top:372px">vs</div><div class="vs" style="left:665px;top:372px">vs</div>
    <div class="comment g b">Comment</div>
    <div id="send"><span class="g b">SEND</span></div>
    <div class="dm"><span class="g r">dan aku DM link buat paham </span><span class="hlbar"><span class="g b">ketiganya</span></span><span class="g r"> &rarr;</span></div>
    <div id="inp"><div class="av">FK</div><div class="ph g r dim" id="ph">Tambah komentar...</div>
      <div class="typed"><span class="g b" id="k0">S</span><span class="g b" id="k1">E</span><span class="g b" id="k2">N</span><span class="g b" id="k3">D</span><i id="caret"></i></div>
      <div id="sbtn"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 11 L21 3 L14 21 L11 13 Z" fill="none" stroke="#274976" stroke-width="2.2" stroke-linejoin="round"/></svg></div>
      <div id="sbtnOn"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 11 L21 3 L14 21 L11 13 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg></div></div>
    <div id="fol"><div class="av">FK</div><div class="n g b">Follow Freddie Kashawan</div><div class="d g r">AI agent, Claude &amp; workflow bisnis, dijelaskan visual.</div>
      <div class="fb" id="fb1">+ Follow</div><div class="fb" id="fb2"><span class="g b">Following &#10003;</span></div></div>
""")
S5_JS = """
  function render(t) {
    Minis.harness("a", t); Minis.loop("b", t); Minis.graph("c", t);
    const beat = (t % 1.75) / 1.75;
    gsap.set("#send", { rotation: -2.5, scale: 1 + 0.035 * Math.exp(-7 * beat) * Math.sin(Math.PI * Math.min(1, beat * 5)) });
    const typing = t >= 0.6 && t < 2.35;
    for (let i = 0; i < 4; i++) gsap.set("#k" + i, { opacity: typing && t >= 0.7 + i * 0.17 ? 1 : 0 });
    gsap.set("#ph", { opacity: typing ? 0 : 1 });
    gsap.set("#caret", { opacity: typing && Math.floor(t * 3.2) % 2 === 0 ? 1 : 0 });
    const on = t >= 1.4 && t < 2.35;
    gsap.set("#sbtnOn", { opacity: on ? 1 : 0, scale: t > 2.05 && t < 2.25 ? 0.86 : 1 });
    $("inp").style.borderColor = typing ? "#4f86e8" : "#121532";
    $("inp").style.boxShadow = typing ? "0 0 0 6px rgba(79,134,232,0.18)" : "none";
    const f = smooth((t - 2.8) / 0.2) * (1 - smooth((t - 6.6) / 0.2));
    gsap.set("#fb1", { opacity: 1 - f, scale: 1 - 0.08 * f });
    gsap.set("#fb2", { opacity: f, scale: 0.92 + 0.08 * f + 0.06 * Math.sin(Math.PI * clamp((t - 2.8) / 0.35, 0, 1)) });
  }
"""

SLIDES = [
    dict(cid="s1", name="Cover", eyebrow="AGENT ARCHITECTURE", right="GESER &rarr;", css=S1_CSS, body=S1_BODY, js=S1_JS),
    dict(cid="s2", name="Harness", eyebrow="THE SCAFFOLD &middot; HARNESS", right="GESER &rarr;", css=S2_CSS, body=S2_BODY, js=S2_JS),
    dict(cid="s3", name="Loop", eyebrow="THE CYCLE &middot; LOOP", right="GESER &rarr;", css=S3_CSS, body=S3_BODY, js=S3_JS),
    dict(cid="s4", name="Graph", eyebrow="THE MAP &middot; GRAPH", right="GESER &rarr;", css=S4_CSS, body=S4_BODY, js=S4_JS),
    dict(cid="s5", name="CTA", eyebrow="MAU LEBIH DALAM?", right="SAVE &middot; SHARE", css=S5_CSS, body=S5_BODY, js=S5_JS),
]

if __name__ == "__main__":
    for s in SLIDES:
        html = SHELL
        for k in ("cid", "name", "eyebrow", "right", "css", "body", "js"):
            html = html.replace("%%" + k.upper() + "%%", s[k])
        d = ROOT / "slides" / s["cid"]
        d.mkdir(parents=True, exist_ok=True)
        for sub in ("assets", "vendor"):
            if (d / sub).exists():
                shutil.rmtree(d / sub)
            shutil.copytree(ROOT / sub, d / sub)
        (d / "index.html").write_text(html)
        print("wrote", d / "index.html")
