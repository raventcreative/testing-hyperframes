"""Agent Architecture carousel, v2 layouts (own composition, not a copy of the reference).
Run: python3 build.py  ->  slides/sN/index.html"""
import math
import shutil
from pathlib import Path

from common import SHELL, mini_harness, mini_loop, mini_graph, box

ROOT = Path(__file__).parent


def hb(s, extra=""):
    return f'<span class="hb" {extra}>{s}</span>'


# ======================================================================== S1 cover: headline top-left, 3 stacked row cards
S1_CSS = """
.row { position:absolute; left:64px; width:952px; height:236px; background:#fff; border:3px solid #121532; border-radius:26px; overflow:hidden; }
.row .strip { position:absolute; left:0; top:0; bottom:0; width:14px; background:linear-gradient(180deg,#121532,#274976); }
.row .dg { position:absolute; left:34px; top:10px; }
.row .kick { position:absolute; left:290px; top:34px; font-size:16px; letter-spacing:0.2em; }
.row .nm { position:absolute; left:288px; top:56px; font-size:56px; letter-spacing:-0.03em; line-height:1.2; }
.row .ds { position:absolute; left:290px; top:128px; font-size:22px; }
.row .ch { position:absolute; left:290px; top:170px; height:40px; padding:0 18px; border-radius:20px; border:2px solid rgba(18,21,50,0.16); font-size:17px; display:flex; align-items:center; }
.row .no { position:absolute; right:34px; top:40px; font-size:132px; line-height:1; letter-spacing:-0.04em; opacity:0.13; }
"""
_rows = [("h", 430, "01", "THE SCAFFOLD", "Harness", "membungkus model", "context + tools", mini_harness),
         ("l", 686, "02", "THE CYCLE", "Loop", "ulang sampai selesai", "plan &rarr; act &rarr; check", mini_loop),
         ("g", 942, "03", "THE MAP", "Graph", "atur tiap langkah", "nodes + edges", mini_graph)]
S1_BODY = f"""    <div class="htitle" style="top:118px;font-size:80px"><span class="g b">Harness</span> <span class="g r dim">vs</span> <span class="g b">Loop</span> <span class="g r dim">vs</span></div>
    <div class="htitle" style="top:218px;font-size:80px">{hb("Graph Engineering.")}</div>
    <div class="lsub" style="top:346px;font-size:29px"><span class="g r">3 cara membangun AI agent.</span> {hb("Kamu pakai yang mana? &rarr;", 'style="font-size:27px"')}</div>
""" + "".join(
    f'    <div class="row" id="r{p}" style="top:{y}px"><div class="strip"></div><div class="dg">{fn(p, 214)}</div>'
    f'<div class="kick g b">{k}</div><div class="nm g b">{n}</div><div class="ds g r">{d}</div>'
    f'<div class="ch"><span class="g r">{c}</span></div><div class="no g b">{no}</div></div>\n'
    for p, y, no, k, n, d, c, fn in _rows)
S1_JS = """
  const rows = ["rh", "rl", "rg"].map($);
  function render(t) {
    Minis.harness("h", t); Minis.loop("l", t); Minis.graph("g", t);
    rows.forEach((el, i) => {
      const ph = ((t / 7 * 3) % 3 + 3) % 3, d = Math.min(Math.abs(ph - i - 0.5), 3 - Math.abs(ph - i - 0.5));
      const k = clamp(1 - d / 0.9, 0, 1);
      el.style.boxShadow = "0 " + (18 * k).toFixed(1) + "px " + (40 * k).toFixed(1) + "px -16px rgba(79,134,232," + (0.7 * k).toFixed(3) + ")";
      el.style.borderColor = "rgb(" + mixc(NAVY, AZ, k) + ")";
    });
  }
"""

# ======================================================================== S2 harness: vertical layered stack
RY = {"gui": 445, "ctx": 557, "mdl": 669, "too": 817, "sen": 929}
BX = [300, 535, 770]


def _row(key, label, sub, items, h=84):
    y = RY[key]
    out = [f'    <div class="secl g" style="left:92px;top:{y + 18}px">{label}</div>',
           f'    <div class="lbl" style="left:92px;top:{y + 44}px"><span class="g r" style="margin:0;font-size:15px">{sub}</span></div>']
    for i, (bid, t, s) in enumerate(items):
        out.append(box(bid, BX[i], y, 220, h, t, s))
    return "\n".join(out)


S2_CSS = """
.eq2 { position:absolute; left:63px; top:216px; display:flex; align-items:center; gap:14px; font-size:26px; }
.eq2 .p { height:54px; padding:0 26px; border-radius:27px; border:3px solid #121532; display:flex; align-items:center; background:#fff; }
.eq2 .p.m { background:#dbe7ff; }
.eq2 .p.h { background:linear-gradient(100deg,#121532,#274976); border-color:transparent; color:#fff; font-weight:700; }
#mdl { position:absolute; left:300px; top:669px; width:690px; height:120px; border-radius:22px; background:linear-gradient(100deg,#121532,#274976); color:#fff; }
#mdl .mt { position:absolute; left:34px; top:18px; font-size:54px; font-weight:700; line-height:1.1; letter-spacing:-0.01em; }
#mdl .ms { position:absolute; left:36px; top:80px; font-size:17px; opacity:0.85; }
#mdl .stat { position:absolute; right:26px; top:38px; width:250px; height:44px; border-radius:22px; background:#fff; }
#mdl .stat span { position:absolute; left:0; right:0; top:0; line-height:44px; text-align:center; font-weight:700; font-size:16px; letter-spacing:0.14em; opacity:0; }
#spine { position:absolute; left:0; top:0; }
#fail { position:absolute; left:968px; top:917px; width:32px; height:32px; border-radius:50%; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-size:18px; font-weight:700; display:flex; align-items:center; justify-content:center; opacity:0; z-index:4; }
#pass { position:absolute; left:968px; top:917px; width:32px; height:32px; border-radius:50%; background:#4f86e8; color:#fff; font-size:16px; font-weight:700; display:flex; align-items:center; justify-content:center; opacity:0; z-index:4; }
"""
_spine_nodes = "".join(f'<circle id="sn{i}" cx="268" cy="{y + (60 if k == "mdl" else 42)}" r="9" fill="#fff" stroke="#121532" stroke-width="2.5"/>'
                       for i, (k, y) in enumerate(RY.items()))
S2_BODY = f"""    <div class="htitle"><span class="g b">Harness</span> {hb("Engineering")}</div>
    <div class="eq2"><div class="p"><span class="g b">Agent</span></div><span class="g r">=</span><div class="p m"><span class="g b">Model</span></div><span class="g r">+</span><div class="p h">Harness</div></div>
    <div class="lsub" style="top:292px;font-size:24px"><span class="g r">Model yang berpikir. Harness yang menentukan </span><span class="g b">apa yang dilihat</span><span class="g r">, </span><span class="g b">apa yang bisa disentuh</span><span class="g r">, dan </span><span class="g b">bagaimana hasilnya dicek.</span></div>
    <div class="frame" style="left:64px;top:410px;width:952px;height:648px;box-shadow:-12px 12px 0 #4f86e8"></div>
    <svg id="spine" width="1080" height="1350">
      <path d="M268 430 V1040" stroke="#121532" stroke-width="2.5" fill="none"/>
      <path d="M1006 971 V729" stroke="#4f86e8" stroke-width="2.5" fill="none" stroke-dasharray="6 6"/>
      <path id="rt" d="M990 971 C1006 971,1006 960,1006 945 V755 C1006 740,1006 729,990 729" fill="none" stroke="none"/>
      <text x="1030" y="850" font-size="14" font-weight="700" fill="#274976" transform="rotate(90 1030 850)" text-anchor="middle" letter-spacing="2">RETRY + FEEDBACK</text>
      {_spine_nodes}
      <circle id="tok" cx="268" cy="430" r="11" fill="#4f86e8" stroke="#fff" stroke-width="3"/>
      <circle id="rtok" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
    </svg>
""" + "\n".join([
    _row("gui", "GUIDES", "yang diikuti", [("bsys", "System prompt", "peran + aturan"), ("bagt", "AGENTS.md", "konvensi tim"), ("bcon", "Constraints", "batas keras")]),
    _row("ctx", "CONTEXT", "yang dilihat", [("bmem", "Memory", "sesi sebelumnya"), ("bret", "Retrieval", "dokumen yang tepat"), ("bfil", "Files &amp; state", "working set")]),
    '    <div class="secl g" style="left:92px;top:705px">MODEL</div><div class="lbl" style="left:92px;top:731px"><span class="g r" style="margin:0;font-size:15px">otak agent</span></div>',
    _row("too", "TOOLS", "yang disentuh", [("btoo", "Tool registry", "yang bisa dipanggil"), ("bsan", "Sandbox", "eksekusi aman"), ("bper", "Permissions", "izin sebelum berisiko")]),
    _row("sen", "SENSORS", "cara dicek", [("btes", "Tests &amp; evals", "berhasil?"), ("btra", "Traces", "log tiap langkah"), ("bout", "Output checks", "schema + lint")]),
]) + """
    <div id="mdl"><div class="mt">MODEL</div><div class="ms">berpikir + memutuskan</div>
      <div class="stat"><span class="g" id="s0">BACA ATURAN</span><span class="g" id="s1">BACA CONTEXT</span><span class="g" id="s2">BERPIKIR</span><span class="g" id="s3">PAKAI TOOLS</span><span class="g" id="s4">MENGECEK</span><span class="g" id="s5">MEMPERBAIKI</span><span class="g" id="s6">MENGIRIM</span></div></div>
    <div id="fail">&times;</div><div id="pass">&#10003;</div>
    <div class="tag" style="left:92px;top:393px">THE HARNESS</div>
    <div class="pill" id="ptask" style="left:400px;top:390px;width:200px"><span class="g b">USER TASK &darr;</span></div>
    <div class="pill" id="pver" style="left:143px;top:1038px;width:250px"><span class="g b">&#10003; VERIFIED OUTPUT</span></div>
    <div class="lsub" style="top:1104px;font-size:34px"><span class="g b">Model sama.</span> <span class="g r dim">Harness lebih baik.</span> """ + hb("Agent lebih baik.") + """</div>
"""
S2_JS = """
  const ROWS = { 0: ["bsys", "bagt", "bcon"], 1: ["bmem", "bret", "bfil"], 3: ["btoo", "bsan", "bper"] };
  const CY = [487, 599, 729, 859, 971];
  function render(t) {
    const ph = Math.min(6, Math.floor(t));
    const f = t - ph;
    for (let i = 0; i < 7; i++) gsap.set("#s" + i, { opacity: i === ph ? 1 : 0 });
    const e = (i) => env(t, i, i + 0.95, 0.15);
    [0, 1, 3].forEach((r) => ROWS[r].forEach((id) => hl($(id), e(r))));
    hl($("btes"), Math.max(e(4), e(6) * 0.9)); hl($("bout"), Math.max(e(4), e(6))); hl($("btra"), Math.max(e(4), e(6)) * 0.7);
    const mk = Math.max(e(2), e(5));
    $("mdl").style.boxShadow = "0 0 0 " + (8 * mk).toFixed(1) + "px rgba(79,134,232,0.28), 0 22px 44px -14px rgba(79,134,232," + (0.25 + 0.6 * mk).toFixed(3) + ")";
    let y, o = 1;
    if (t < 0.3) y = 430 + (CY[0] - 430) * smooth(t / 0.3);
    else if (ph <= 4) y = ph === 0 ? CY[0] : CY[ph - 1] + (CY[ph] - CY[ph - 1]) * smooth(f / 0.35);
    else if (ph === 5) { y = CY[4]; o = 1 - smooth(f / 0.1); }
    else { y = f < 0.45 ? CY[4] : CY[4] + (1050 - CY[4]) * smooth((f - 0.45) / 0.35); o = smooth(f / 0.1); }
    $("tok").setAttribute("cy", y.toFixed(1)); $("tok").setAttribute("opacity", o.toFixed(3));
    for (let i = 0; i < 5; i++) $("sn" + i).setAttribute("fill", (y >= CY[i] - 1 && !(ph === 5 && i === 4)) ? "#4f86e8" : "#ffffff");
    const rq = (t - 5.05) / 0.6;
    dot("rtok", "rt", smooth(rq), rq > 0 && rq < 1.15 ? 1 - smooth((rq - 1) / 0.15) : 0);
    gsap.set("#fail", { opacity: env(t, 4.45, 5.0, 0.1) }); gsap.set("#pass", { opacity: env(t, 6.2, 6.95, 0.1) });
    glow($("pver"), env(t, 6.75, 7.3, 0.12)); glow($("ptask"), env(t, -0.2, 0.35, 0.12));
  }
"""

# ======================================================================== S3 loop: counter panel + vertical step list
STEP_Y = [400, 474, 548, 622, 696]
_steps = [("01", "OBSERVE", "state + error"), ("02", "REASON", "rencanakan langkah"), ("03", "ACT", "edit &middot; run &middot; tools"),
          ("04", "CHECK", "tests &middot; evals"), ("05", "DECIDE", "goal? stop : loop")]
S3_CSS = """
.code2 { position:absolute; left:63px; top:214px; height:58px; padding:0 26px; border-radius:12px; background:linear-gradient(100deg,#121532,#274976); color:#fff; display:flex; align-items:center; font-size:24px; white-space:nowrap; }
.code2 b { color:#9cc2ff; margin-right:10px; }
#ip { position:absolute; left:64px; top:400px; width:300px; height:358px; border-radius:26px; background:linear-gradient(160deg,#121532,#274976); color:#fff; box-shadow:0 26px 50px -22px rgba(18,21,50,0.55); }
#ip .k { position:absolute; left:30px; top:30px; font-size:16px; letter-spacing:0.24em; font-weight:700; opacity:0.85; }
#ip .n { position:absolute; left:26px; top:62px; width:170px; height:140px; overflow:hidden; }
#ip .n span { position:absolute; left:0; top:0; font-size:124px; line-height:140px; font-weight:700; letter-spacing:-0.04em; }
#ip .of { position:absolute; left:196px; top:150px; font-size:28px; opacity:0.75; }
#ip .gl { position:absolute; left:30px; top:226px; font-size:17px; opacity:0.9; }
#ip .bar { position:absolute; left:30px; top:262px; width:240px; height:12px; border-radius:6px; background:rgba(255,255,255,0.2); overflow:hidden; }
#ip .bar i { position:absolute; left:0; top:0; bottom:0; width:240px; background:#fff; border-radius:6px; transform-origin:0 50%; }
#ip .dots { position:absolute; left:30px; top:300px; display:flex; gap:10px; }
#ip .dots b { width:14px; height:14px; border-radius:50%; border:2px solid #fff; }
.st { position:absolute; left:392px; width:560px; height:62px; background:#fff; border:2.5px solid #121532; border-radius:16px; }
.st .num { position:absolute; left:14px; top:12px; width:34px; height:34px; border-radius:50%; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-size:14px; font-weight:700; display:flex; align-items:center; justify-content:center; }
.st .nm { position:absolute; left:64px; top:13px; font-size:25px; letter-spacing:0.03em; }
.st .ds { position:absolute; right:20px; top:18px; font-size:17px; }
#ring3 { position:absolute; left:0; top:0; }
.dn { position:absolute; left:806px; top:784px; width:146px; height:46px; border-radius:23px; border:3px solid #121532; background:#fff; font-size:19px; letter-spacing:0.14em; display:flex; align-items:center; justify-content:center; }
#dnOn { position:absolute; left:806px; top:784px; width:146px; height:46px; border-radius:23px; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-weight:700; font-size:19px; letter-spacing:0.14em; display:flex; align-items:center; justify-content:center; opacity:0; }
.mini { position:absolute; width:304px; height:76px; background:#fff; border:2.5px solid #121532; border-radius:16px; }
.mini .ic { position:absolute; left:14px; top:18px; width:38px; height:38px; border-radius:10px; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-weight:700; font-size:17px; display:flex; align-items:center; justify-content:center; }
.mini .a { position:absolute; left:66px; top:10px; font-size:20px; }
.mini .c { position:absolute; left:66px; top:40px; font-size:16px; white-space:nowrap; }
"""


def _mini(id_, x, y, ic, a, c):
    return f'    <div class="mini" id="{id_}" style="left:{x}px;top:{y}px"><div class="ic">{ic}</div><div class="a g b">{a}</div><div class="c g r">{c}</div></div>'


S3_BODY = f"""    <div class="htitle"><span class="g b">Loop</span> {hb("Engineering")}</div>
    <div class="code2"><b>while</b>(!goal_met) {{ observe &rarr; reason &rarr; act &rarr; check }}</div>
    <div class="lsub" style="top:292px;font-size:24px"><span class="g r">Berhenti nge-prompt tiap langkah. Desain loop-nya: </span><span class="g b">goal yang jelas</span><span class="g r">, </span><span class="g b">cek tiap putaran</span><span class="g r">, dan </span><span class="g b">batas keras.</span></div>
    <div id="ip"><div class="k">ITERASI</div>
      <div class="n" data-layout-allow-overflow data-layout-allow-overlap><span id="it0">01</span><span id="it1">02</span><span id="it2">03</span></div><div class="of">/ 10</div>
      <div class="gl">tests passing <b id="pass">0/12</b></div><div class="bar"><i id="barf"></i></div>
      <div class="dots"><b id="lp0"></b><b id="lp1"></b><b id="lp2"></b></div></div>
    <svg id="ring3" width="1080" height="1350">
      <path d="M952 727 H972 C988 727,992 715,992 700 V458 C992 443,988 431,972 431 H962" fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-dasharray="6 6"/>
      <path d="M966 424 L956 431 L966 438" fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-linecap="round"/>
      <path id="ret" d="M952 727 H972 C988 727,992 715,992 700 V458 C992 443,988 431,972 431 H952" fill="none" stroke="none"/>
      <path d="M879 758 V784" stroke="#121532" stroke-width="2.5" stroke-dasharray="4 4"/>
      <path id="dnp" d="M879 758 V800" fill="none" stroke="none"/>
      <circle id="rtk" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
    </svg>
""" + "\n".join(f'    <div class="st" id="st{i}" style="top:{STEP_Y[i]}px"><div class="num">{n}</div><div class="nm g b">{a}</div><div class="ds g r">{d}</div></div>'
                for i, (n, a, d) in enumerate(_steps)) + f"""
    <div class="lbl" style="left:560px;top:796px"><span class="g r" style="margin:0;font-size:16px">keluar saat goal tercapai &rarr;</span></div>
    <div class="dn"><span class="g b">DONE &#10003;</span></div><div id="dnOn">DONE &#10003;</div>
    <div class="secl g" style="left:64px;top:850px">STOP CONDITIONS</div>
{_mini("m0", 64, 880, "&#10003;", "Goal", "semua test hijau")}
{_mini("m1", 388, 880, "&#8635;", "Max", "10 putaran / 30 menit")}
{_mini("m2", 712, 880, "$", "Hard", "token budget")}
    <div class="secl g" style="left:64px;top:978px">MEMORY ANTAR PUTARAN</div>
{_mini("m3", 64, 1008, "&#9998;", "progress.md", "yang sudah selesai")}
{_mini("m4", 388, 1008, "&#8916;", "git commit", "tiap putaran")}
{_mini("m5", 712, 1008, "&#9675;", "Context baru", "tiap putaran")}
    <div class="lsub" style="top:1120px;font-size:34px"><span class="g b">Prompt memulai.</span> {hb("Loop menyelesaikan.")}</div>
"""
S3_JS = """
  const sts = [0, 1, 2, 3, 4].map((i) => $("st" + i));
  function render(t) {
    const lap = t < 6 ? Math.floor(t / 2) : 2, frac = t < 6 ? (t % 2) / 2 : 1;
    const idx = Math.min(4, Math.floor(frac / 0.18));
    sts.forEach((el, i) => hl(el, t < 6 ? (i === idx && frac < 0.9 ? smooth((frac - i * 0.18) / 0.05) : 0) : (i === 4 ? 1 - smooth((t - 6.5) / 0.3) : 0)));
    for (let i = 0; i < 3; i++) gsap.set("#it" + i, { yPercent: i === lap ? 0 : (i < lap ? -110 : 110) });
    const done = lap * 4 + (frac >= 0.54 ? 4 * smooth((frac - 0.54) / 0.12) : 0);
    $("pass").textContent = Math.round(lap * 4 + (frac >= 0.6 ? 4 : 0)) + "/12";
    gsap.set("#barf", { scaleX: Math.max(0.001, done / 12) });
    for (let i = 0; i < 3; i++) $("lp" + i).style.background = (i < lap || (i === lap && frac >= 0.72)) ? "#ffffff" : "transparent";
    const rq = (frac - 0.9) / 0.1;
    const back = t < 6 && lap < 2 && rq > 0;
    if (back) dot("rtk", "ret", smooth(rq), 1);
    else { const dq = (t - 6.0) / 0.35; dot("rtk", "dnp", smooth(dq), dq > 0 && dq < 1.2 ? 1 - smooth((dq - 1) / 0.2) : 0); }
    const dk = smooth((t - 6.3) / 0.2) * (1 - smooth((t - 6.85) / 0.12));
    gsap.set("#dnOn", { opacity: dk });
    hl($("m0"), dk); hl($("m1"), env(t, 0.05, 0.6, 0.15) * 0.8);
    let gk = 0; for (let l = 0; l < 3; l++) gk = Math.max(gk, env(t, l * 2 + 1.44, l * 2 + 1.9, 0.1));
    hl($("m3"), gk); hl($("m4"), gk); hl($("m5"), env(t, 0, 0.35, 0.1) + env(t, 2, 2.35, 0.1) + env(t, 4, 4.35, 0.1));
  }
"""

# ======================================================================== S4 graph: left-to-right flow
NODES = {"nst": (112, 655), "ncl": (245, 655), "nrt": (360, 655), "npo": (525, 520), "nhu": (700, 520), "nrf": (872, 520),
         "nsd": (525, 742), "npt": (525, 836), "ndr": (700, 790), "nqc": (872, 790), "nen": (975, 655)}
DWELL = {"nhu": 0.45, "nqc": 0.3}


def _route(pts, t0, speed=None, t1=None):
    seg = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    L = sum(seg)
    dw = [DWELL.get(p[2], 0.2) if p[2] else 0 for p in pts]
    dw[0] = 0.15
    if speed is None:
        speed = L / ((t1 - t0) - sum(dw))
    t, K, arr, s = t0, [], [], 0.0
    F = [0.0]
    for d in seg:
        s += d
        F.append(round(s / L, 5))
    for i, p in enumerate(pts):
        if i:
            t += seg[i - 1] / speed
        K.append([round(t, 3), i])
        if p[2]:
            arr.append((p[2], round(t, 3)))
        if dw[i]:
            t += dw[i]
            K.append([round(t, 3), i])
    N = {str(i): p[2] for i, p in enumerate(pts) if p[2]}
    return F, K, N, arr, speed


def P(name):
    x, y = NODES[name]
    return (x, y, name)


R1 = [P("nst"), P("ncl"), P("nrt"), (360, 520, None), P("npo"), P("nhu"), P("nrf"), (975, 520, None), P("nen")]
R2 = [P("nst"), P("ncl"), P("nrt"), (360, 790, None), (415, 790, None), (415, 742, None), P("nsd"), (612, 742, None), (612, 790, None),
      P("ndr"), P("nqc"), (872, 880, None), (700, 880, None), P("ndr"), P("nqc"), (975, 790, None), P("nen")]
F1, K1, N1, A1, _ = _route(R1, 0.15, t1=3.35)
F2, K2, N2, A2, SP2 = _route(R2, 3.55, t1=6.85)
t_router_out = [k[0] for k in K2 if k[1] == 2][-1]
R3 = [(360, 655, None), (360, 790, None), (415, 790, None), (415, 836, None), P("npt"), (612, 836, None), (612, 790, None), (700, 790, None)]
F3, K3, N3, A3, _ = _route(R3, t_router_out, speed=SP2)


def _arr(A, name, n=0):
    return [t for nm, t in A if nm == name][n]


EVENTS = [
    [0.0, None, None, 0],
    [_arr(A1, "ncl") + 0.1, 0, '"refund"', 1], [_arr(A1, "npo") + 0.1, 1, "policy_ok: true", 2],
    [_arr(A1, "nhu") + 0.35, 2, "human: approved", 3], [_arr(A1, "nrf") + 0.1, 3, "refunded &#10003;", 4],
    [3.5, None, None, 0],
    [_arr(A2, "ncl") + 0.1, 0, '"question"', 1], [_arr(A2, "ndr") + 0.05, 1, "docs: 2 &middot; tickets: 3", 2],
    [_arr(A2, "ndr") + 0.15, 2, "draft v1", 3], [_arr(A2, "ndr", 1) + 0.1, 2, "draft v2", 4], [_arr(A2, "nen") + 0.02, 3, "terkirim &#10003;", 5],
]
QF = (_arr(A2, "nqc"), _arr(A2, "nqc") + 0.45)
QP = (_arr(A2, "nqc", 1), _arr(A2, "nqc", 1) + 0.45)


def _poly(pts):
    return "M" + " L".join(f"{p[0]} {p[1]}" for p in pts)


def _nb(id_, w, t, s, cls=""):
    x, y = NODES[id_]
    return box(id_, x - w // 2, y - 32, w, 64, t, s, cls)


S4_CSS = """
.box { padding:6px 12px; }
.box .t { font-size:18px; }
.box .s { font-size:13px; }
.tix { position:absolute; left:64px; top:298px; width:952px; height:74px; border-radius:18px; background:#fff; border:2px solid rgba(18,21,50,0.16); }
.tix .tg { position:absolute; left:14px; top:17px; height:38px; width:250px; border-radius:19px; background:linear-gradient(100deg,#121532,#274976); color:#fff; font-weight:700; font-size:15px; letter-spacing:0.14em; }
.tix .tg span { position:absolute; left:0; right:0; line-height:38px; text-align:center; }
.tix .q { position:absolute; left:284px; top:20px; font-size:23px; white-space:nowrap; }
#gw2 { position:absolute; left:0; top:0; }
.pillx { position:absolute; height:40px; border-radius:20px; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:15px; letter-spacing:0.14em; background:linear-gradient(100deg,#121532,#274976); }
.diam2 { position:absolute; left:334px; top:629px; width:52px; height:52px; }
.elab { position:absolute; font-size:15px; padding:2px 10px; border-radius:10px; background:#fff; border:1.5px solid rgba(18,21,50,0.15); white-space:nowrap; }
.qchip { position:absolute; left:830px; top:706px; height:30px; padding:0 12px; border-radius:15px; font-size:14px; font-weight:700; display:flex; align-items:center; opacity:0; z-index:3; white-space:nowrap; background:linear-gradient(100deg,#121532,#274976); color:#fff; }
.ss { position:absolute; left:64px; top:956px; width:952px; height:148px; border-radius:20px; background:rgba(255,255,255,0.9); border:2.5px solid #121532; }
.ss .h { position:absolute; left:22px; top:16px; font-size:16px; letter-spacing:0.18em; font-weight:700; }
.ss .cp { position:absolute; right:22px; top:16px; font-size:15px; }
.kv { position:absolute; width:444px; height:42px; border-radius:12px; background:#eef3fb; border:2px solid transparent; }
.kv .k { position:absolute; left:16px; top:9px; font-size:16px; }
.kv .v { position:absolute; right:16px; top:7px; font-size:19px; white-space:nowrap; }
"""
S4_BODY = f"""    <div class="htitle"><span class="g b">Graph</span> {hb("Engineering")}</div>
    <div class="lsub" style="top:204px;font-size:24px"><span class="g b">Node</span><span class="g r"> mengerjakan tugas. </span><span class="g b">Edge</span><span class="g r"> menentukan apa yang jalan berikutnya. </span><span class="g b">Shared state</span><span class="g r"> membawa semuanya di antara mereka.</span></div>
    <div class="tix"><div class="tg"><span id="th1">TIKET MASUK &middot; RUN 1</span><span id="th2" style="opacity:0">TIKET MASUK &middot; RUN 2</span></div>
      <div class="q g r" id="tq1">&ldquo;Aku kena charge dua kali. Tolong refund.&rdquo;</div><div class="q g r" id="tq2" style="opacity:0">&ldquo;Gimana cara export data ke CSV?&rdquo;</div></div>
    <div class="frame" style="left:64px;top:404px;width:952px;height:524px;box-shadow:-12px 12px 0 #4f86e8"></div>
    <div class="tag" style="left:92px;top:387px">CONTOH &middot; SUPPORT AGENT</div>
    <svg id="gw2" width="1080" height="1350">
      <g fill="none" stroke="#121532" stroke-width="2.5">
        <path d="M154 655 H170"/><path d="M320 655 H334"/>
        <path d="M360 629 V520 H450"/><path d="M360 681 V790 H415"/><path d="M415 742 V836"/><path d="M415 742 H450"/><path d="M415 836 H450"/>
        <path d="M600 520 H615"/><path d="M785 520 H797"/><path d="M947 520 H975 V635"/>
        <path d="M600 742 H612 V836 H600"/><path d="M612 790 H625"/><path d="M775 790 H797"/><path d="M947 790 H975 V675"/>
      </g>
      <path d="M872 822 V880 H700 V822" fill="none" stroke="#4f86e8" stroke-width="2.5" stroke-dasharray="6 6"/>
      <path id="r1" d="{_poly(R1)}" fill="none" stroke="none"/><path id="r2" d="{_poly(R2)}" fill="none" stroke="none"/><path id="r3" d="{_poly(R3)}" fill="none" stroke="none"/>
      <circle id="tk1" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
      <circle id="tk2" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
      <circle id="tk3" r="9" fill="#4f86e8" stroke="#fff" stroke-width="3" opacity="0"/>
    </svg>
    <div class="pillx" id="nst" style="left:70px;top:635px;width:84px">START</div>
    <div class="pillx" id="nen" style="left:940px;top:635px;width:70px">END</div>
    <svg class="diam2" id="nrt" viewBox="0 0 52 52"><path id="nrtp" d="M26 2 L50 26 L26 50 L2 26 Z" fill="#121532"/></svg>
    <div class="elab" style="left:296px;top:560px"><span class="g r">refund</span></div>
    <div class="elab" style="left:280px;top:735px"><span class="g r">question</span></div>
    <div class="elab" style="left:170px;top:700px"><span class="g r">route(state.intent)</span></div>
    <div class="elab" style="left:432px;top:880px"><span class="g r">parallel &rArr;</span></div>
    <div class="elab" style="left:752px;top:866px"><span class="g r">retry</span></div>
""" + "\n".join([
    _nb("ncl", 150, "Classify", "llm &middot; intent", "llm"),
    _nb("npo", 150, "Check policy", "tool &middot; eligible?"),
    _nb("nhu", 170, "&#10074;&#10074; Approval", "human &middot; menunggu", "human"),
    _nb("nrf", 150, "Issue refund", "tool &middot; payments"),
    _nb("nsd", 150, "Search docs", "tool &middot; retrieval"),
    _nb("npt", 150, "Past tickets", "tool &middot; history"),
    _nb("ndr", 150, "Draft reply", "llm &middot; gabungkan", "llm"),
    _nb("nqc", 150, "Quality check", "eval &middot; &ge; 0.85", "eval"),
]) + f"""
    <div class="qchip" id="qf">&lt; 0.85 &times; retry</div><div class="qchip" id="qp">&ge; 0.85 &#10003;</div>
    <div class="ss"><div class="h g">SHARED STATE</div><div class="cp g r" id="cpn">checkpoint #0 &middot; tersimpan</div>
      <div class="kv" id="ce0" style="left:20px;top:46px"><div class="k g r">intent</div><div class="v g b" id="sv0">&mdash;</div></div>
      <div class="kv" id="ce1" style="left:484px;top:46px"><div class="k g r">context</div><div class="v g b" id="sv1">&mdash;</div></div>
      <div class="kv" id="ce2" style="left:20px;top:96px"><div class="k g r">review</div><div class="v g b" id="sv2">&mdash;</div></div>
      <div class="kv" id="ce3" style="left:484px;top:96px"><div class="k g r">result</div><div class="v g b" id="sv3">&mdash;</div></div></div>
    <div class="lsub" style="top:1150px;font-size:34px"><span class="g b">Prompt menyarankan.</span> {hb("Edge yang memaksa.")}</div>
"""
_ev = ",\n    ".join(f'[{e[0]}, {"null" if e[1] is None else e[1]}, {"null" if e[2] is None else repr(e[2]).replace(chr(39), chr(96))}, {e[3]}]' for e in EVENTS)
S4_JS = f"""
  const RUNS = [
    {{ path: "r1", tok: "tk1", F: {F1}, K: {K1}, N: {str(N1).replace("'", '"')} }},
    {{ path: "r2", tok: "tk2", F: {F2}, K: {K2}, N: {str(N2).replace("'", '"')} }},
    {{ path: "r3", tok: "tk3", F: {F3}, K: {K3}, N: {str(N3).replace("'", '"')} }},
  ];
  const EV = [
    {_ev}
  ];
  const QF = {list(QF)}, QP = {list(QP)};
  const BASE = {{ ncl: ICE, ndr: ICE }};
  function prog(K, F, t) {{
    if (t < K[0][0] || t > K[K.length - 1][0] + 0.25) return null;
    for (let i = 0; i < K.length - 1; i++) {{
      const [ta, ia] = K[i], [tb, ib] = K[i + 1];
      if (t >= ta && t <= tb) {{ const k = tb > ta ? (t - ta) / (tb - ta) : 1; return F[ia] + (F[ib] - F[ia]) * k; }}
    }}
    return F[K[K.length - 1][1]];
  }}
  const nodeIds = ["nst", "ncl", "npo", "nhu", "nrf", "nsd", "npt", "ndr", "nqc", "nen", "nrt"];
  function render(t) {{
    const act = {{}};
    RUNS.forEach((r) => {{
      const p = prog(r.K, r.F, t), last = r.K[r.K.length - 1][0];
      const o = p === null ? 0 : Math.min(1, (t - r.K[0][0]) * 8) * (1 - smooth((t - last) / 0.25));
      dot(r.tok, r.path, p === null ? 0 : p, o);
      const span = {{}};
      r.K.forEach(([tk, ix]) => {{ const id = r.N[ix]; if (!id) return; const key = id + "|" + ix; const s = span[key] || (span[key] = [tk, tk]); s[1] = Math.max(s[1], tk); }});
      Object.keys(span).forEach((key) => {{ const id = key.split("|")[0], [a, b] = span[key]; act[id] = Math.max(act[id] || 0, env(t, a - 0.05, b + 0.3, 0.12)); }});
    }});
    nodeIds.forEach((id) => {{
      const k = act[id] || 0, el = $(id);
      if (id === "nst" || id === "nen" || id === "nqc") glow(el, k);
      else if (id === "nrt") $("nrtp").setAttribute("fill", "rgb(" + mixc(NAVY, AZ, k) + ")");
      else hl(el, k, BASE[id] || WHITE);
    }});
    const run2 = t >= 3.45;
    gsap.set(["#th1", "#tq1"], {{ opacity: run2 ? 0 : 1 }}); gsap.set(["#th2", "#tq2"], {{ opacity: run2 ? 1 : 0 }});
    let vals = ["\\u2014", "\\u2014", "\\u2014", "\\u2014"], cp = 0; const last = [-9, -9, -9, -9];
    EV.forEach(([te, ci, v, n]) => {{ if (t < te) return; if (ci === null) {{ vals = ["\\u2014", "\\u2014", "\\u2014", "\\u2014"]; cp = n; last.fill(-9); }} else {{ vals[ci] = v; last[ci] = te; cp = n; }} }});
    for (let i = 0; i < 4; i++) {{
      $("sv" + i).innerHTML = vals[i];
      const k = env(t, last[i], last[i] + 0.8, 0.1), c = $("ce" + i);
      c.style.borderColor = "rgba(79,134,232," + k.toFixed(3) + ")"; c.style.background = "rgb(" + mixc([238, 243, 251], ICE2, k) + ")";
    }}
    $("cpn").textContent = "checkpoint #" + cp + " \\u00b7 tersimpan";
    gsap.set("#qf", {{ opacity: env(t, QF[0], QF[1], 0.08) }}); gsap.set("#qp", {{ opacity: env(t, QP[0], QP[1], 0.08) }});
  }}
"""

# ======================================================================== S5 CTA: split layout
S5_CSS = """
.mc2 { position:absolute; left:600px; width:416px; height:200px; background:#fff; border:3px solid #121532; border-radius:24px; overflow:hidden; }
.mc2 .dg { position:absolute; left:12px; top:10px; }
.mc2 .no { position:absolute; left:212px; top:44px; font-size:18px; letter-spacing:0.14em; }
.mc2 .nm { position:absolute; left:210px; top:68px; font-size:44px; letter-spacing:-0.02em; line-height:1.15; }
.mc2 .ds { position:absolute; left:212px; top:126px; font-size:17px; }
.cm { position:absolute; left:63px; top:372px; font-size:66px; letter-spacing:-0.03em; }
#send { position:absolute; left:63px; top:466px; width:492px; height:196px; border-radius:30px; background:linear-gradient(110deg,#121532,#274976); box-shadow:12px 14px 0 #4f86e8; display:flex; align-items:center; justify-content:center; }
#send span { color:#fff; font-weight:700; font-size:150px; line-height:1; letter-spacing:-0.02em; margin-top:12px; }
.dm2 { position:absolute; left:63px; top:706px; width:500px; font-size:31px; line-height:1.4; }
.arrowd { position:absolute; left:63px; top:900px; font-size:22px; letter-spacing:0.16em; }
#inp { position:absolute; left:64px; top:1010px; width:620px; height:84px; border-radius:42px; background:#fff; border:3px solid #121532; }
#inp .av { position:absolute; left:14px; top:13px; width:52px; height:52px; box-shadow:none; }
.ph { position:absolute; left:86px; top:0; line-height:78px; font-size:27px; }
.typed { position:absolute; left:86px; top:0; line-height:78px; font-size:27px; display:flex; }
.typed span { opacity:0; }
#caret { width:3px; height:34px; margin-top:22px; margin-left:3px; background:#274976; opacity:0; }
#sbtnOn { position:absolute; right:14px; top:13px; width:52px; height:52px; border-radius:50%; background:linear-gradient(135deg,#4f86e8,#274976); display:flex; align-items:center; justify-content:center; opacity:0; }
#sbtn { position:absolute; right:14px; top:13px; width:52px; height:52px; border-radius:50%; background:#eef3fb; display:flex; align-items:center; justify-content:center; }
.fb { position:absolute; left:706px; top:1010px; width:310px; height:84px; border-radius:42px; display:flex; align-items:center; justify-content:center; font-size:25px; font-weight:700; }
#fb1 { background:linear-gradient(100deg,#121532,#274976); color:#fff; }
#fb2 { background:#fff; border:3px solid #121532; opacity:0; }
.fsub { position:absolute; left:706px; top:1108px; width:310px; text-align:center; font-size:17px; }
"""
_mc = [("a", 330, "01", "Harness", "membungkus model", mini_harness), ("b", 550, "02", "Loop", "ulang sampai selesai", mini_loop),
       ("c", 770, "03", "Graph", "atur tiap langkah", mini_graph)]
S5_BODY = f"""    <div class="htitle" style="top:116px;font-size:58px"><span class="g r">Mau paham lebih dalam</span></div>
    <div class="htitle" style="top:196px;font-size:58px">{hb("Harness, Loop &amp; Graph?")}</div>
""" + "".join(f'    <div class="mc2" id="mc{p}" style="top:{y}px"><div class="dg">{fn(p, 180)}</div><div class="no g b">{no}</div><div class="nm g b">{n}</div><div class="ds g r">{d}</div></div>\n'
              for p, y, no, n, d, fn in _mc) + """    <div class="cm g b">Comment</div>
    <div id="send"><span>SEND</span></div>
    <div class="dm2"><span class="g r">dan aku DM link materinya biar kamu paham </span><span class="g b">ketiganya.</span></div>
    <div class="arrowd g b">KETIK DI KOLOM KOMENTAR &darr;</div>
    <div id="inp"><div class="av">FK</div><div class="ph g r dim" id="ph">Tambah komentar...</div>
      <div class="typed"><span class="g b" id="k0">S</span><span class="g b" id="k1">E</span><span class="g b" id="k2">N</span><span class="g b" id="k3">D</span><i id="caret"></i></div>
      <div id="sbtn"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 11 L21 3 L14 21 L11 13 Z" fill="none" stroke="#274976" stroke-width="2.2" stroke-linejoin="round"/></svg></div>
      <div id="sbtnOn"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 11 L21 3 L14 21 L11 13 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg></div></div>
    <div class="fb" id="fb1">+ Follow</div><div class="fb" id="fb2"><span class="g b">Following &#10003;</span></div>
    <div class="fsub g r">AI agent &amp; workflow bisnis, dijelaskan visual.</div>
"""
S5_JS = """
  const mcs = ["mca", "mcb", "mcc"].map($);
  function render(t) {
    Minis.harness("a", t); Minis.loop("b", t); Minis.graph("c", t);
    const beat = (t % 1.75) / 1.75;
    gsap.set("#send", { rotation: -3, scale: 1 + 0.035 * Math.exp(-7 * beat) * Math.sin(Math.PI * Math.min(1, beat * 5)) });
    mcs.forEach((el, i) => { const k = env(t, 3.4 + i * 0.35, 3.4 + i * 0.35 + 0.5, 0.15); el.style.borderColor = "rgb(" + mixc(NAVY, AZ, k) + ")"; el.style.boxShadow = "0 " + (16 * k).toFixed(1) + "px 34px -14px rgba(79,134,232," + (0.7 * k).toFixed(3) + ")"; });
    const typing = t >= 0.6 && t < 2.35;
    for (let i = 0; i < 4; i++) gsap.set("#k" + i, { opacity: typing && t >= 0.7 + i * 0.17 ? 1 : 0 });
    gsap.set("#ph", { opacity: typing ? 0 : 1 });
    gsap.set("#caret", { opacity: typing && Math.floor(t * 3.2) % 2 === 0 ? 1 : 0 });
    gsap.set("#sbtnOn", { opacity: t >= 1.4 && t < 2.35 ? 1 : 0, scale: t > 2.05 && t < 2.25 ? 0.86 : 1 });
    $("inp").style.borderColor = typing ? "#4f86e8" : "#121532";
    $("inp").style.boxShadow = typing ? "0 0 0 6px rgba(79,134,232,0.18)" : "none";
    const f = smooth((t - 2.8) / 0.2) * (1 - smooth((t - 6.6) / 0.2));
    gsap.set("#fb1", { opacity: 1 - f, scale: 1 - 0.06 * f });
    gsap.set("#fb2", { opacity: f, scale: 0.94 + 0.06 * f + 0.05 * Math.sin(Math.PI * clamp((t - 2.8) / 0.35, 0, 1)) });
  }
"""

SLIDES = [
    dict(cid="s1", name="Cover", eyebrow="AGENT ARCHITECTURE", right="GESER &rarr;", css=S1_CSS, body=S1_BODY, js=S1_JS),
    dict(cid="s2", name="Harness", eyebrow="01 &middot; THE SCAFFOLD", right="GESER &rarr;", css=S2_CSS, body=S2_BODY, js=S2_JS),
    dict(cid="s3", name="Loop", eyebrow="02 &middot; THE CYCLE", right="GESER &rarr;", css=S3_CSS, body=S3_BODY, js=S3_JS),
    dict(cid="s4", name="Graph", eyebrow="03 &middot; THE MAP", right="GESER &rarr;", css=S4_CSS, body=S4_BODY, js=S4_JS),
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
