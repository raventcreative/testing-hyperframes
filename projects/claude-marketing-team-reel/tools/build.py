"""Generates index.html for claude-marketing-team-reel from transcript.json + locked storyboard.
Run from the project root: python3 tools/build.py"""
import json, math, re

W = json.load(open("transcript.json"))
DUR = 70.034

def t(i):  # start time of word index i (see transcript.json)
    return W[i]["start"]

# ---- scene windows (retimed to the real VO; see STORYBOARD.md) -------------------------------
SC = [  # id, start, transition-in kind, transition duration
    ("s01", 0.00, None, 0),
    ("s02", 4.55, "push", 0.36),
    ("s03", 7.55, "push", 0.36),
    ("s04", 15.50, "wipe", 0.42),
    ("s05", 21.50, "cover", 0.42),
    ("s06", 27.38, "push", 0.36),
    ("s07", 35.24, "push", 0.36),
    ("s08", 39.85, "pushup", 0.38),
    ("s09", 46.45, "wipe", 0.42),
    ("s10", 54.90, "cover", 0.42),
    ("s11", 63.00, "push", 0.36),
    ("s12", 66.95, "pushup", 0.36),
]
def win(k):
    s = SC[k][1]
    e = SC[k + 1][1] + SC[k + 1][3] if k + 1 < len(SC) else DUR
    return s, round(e - s, 3)

# ---- captions -------------------------------------------------------------------------------
HIDE = [(29.40, 35.24), (49.00, 54.90), (66.90, DUR)]  # prompt type-on (S06, S09) and CTA (S12) carry the words
HL = re.compile(r"^(16|7|Claude|MCP|Meta|META|SKINKU|Higgsfield)$")
def scene_at(x):
    k = 0
    for i, s in enumerate(SC):
        if x >= s[1]: k = i
    return SC[k][0]
SLOT = {"s01": (470, 980, 430), "s11": (470, 1080, 430)}
DEFAULT_SLOT = (368, 1318, 532)

groups, cur = [], []
def flush():
    global cur
    if cur: groups.append(cur); cur = []
# sentence chunks by punctuation, then balanced 3-5 word groups
chunks, c = [], []
for i, w in enumerate(W):
    c.append(i)
    if w["text"][-1] in ",.:": chunks.append(c); c = []
if c: chunks.append(c)
merged = []
for ch in chunks:
    if merged and len(merged[-1]) < 3: merged[-1] += ch
    else: merged.append(ch)
for ch in merged:
    n = len(ch); k = max(1, math.ceil(n / 5)); base = n // k; extra = n % k; p = 0
    for g in range(k):
        size = base + (1 if g < extra else 0)
        groups.append(ch[p:p + size]); p += size

caps = []
for gi, g in enumerate(groups):
    st = max(0.0, t(g[0]) - 0.06)
    end_word = W[g[-1]]["end"]
    nxt = t(groups[gi + 1][0]) - 0.06 if gi + 1 < len(groups) else DUR
    en = min(nxt, end_word + 0.35)
    if any(a <= st < b for a, b in HIDE): continue
    for a, b in HIDE:  # never run into a hidden window
        if st < a < en: en = a
    words = []
    for i in g:
        raw = W[i]["text"]
        txt = raw.rstrip(",") if i == g[-1] else raw
        core = re.sub(r"[,.:]", "", txt)
        if HL.match(core):
            words.append(f'<b class="hl">{txt}</b>')
        else:
            words.append(txt)
    caps.append(dict(id=f"cap{len(caps):02d}", start=round(st, 3), dur=round(en - st, 3),
                     html=" ".join(words), slot=SLOT.get(scene_at(st), DEFAULT_SLOT)))

cap_html = "\n".join(
    f'<div id="{c["id"]}" class="clip cap" data-start="{c["start"]}" data-duration="{c["dur"]}" data-track-index="20" '
    f'style="left:{c["slot"][0]}px;top:{c["slot"][1]}px;width:{c["slot"][2]}px"><div class="pill" id="{c["id"]}-p">{c["html"]}</div></div>'
    for c in caps)

# ---- helpers ---------------------------------------------------------------------------------
def pwin(sid, imgs, left=90, top=1290, w=250, h=280, dark=False):
    """Portrait window: crop from 2.png / 1.png sits on the window's bottom edge."""
    layers = "".join(
        f'<img id="{sid}-px-{n}" class="px" src="assets/expr/{n}.png" alt="" style="opacity:{1 if j == 0 else 0}">'
        for j, n in enumerate(imgs))
    return (f'<div id="{sid}-pw" class="pwin{" dark" if dark else ""}" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<div id="{sid}-pwi" class="pwin-in">{layers}</div></div>')

def words_spans(sid, text, hl):
    out = []
    for i, w in enumerate(text.split()):
        core = re.sub(r"[,.]", "", w)
        cls = "tw hlw" if core in hl else "tw"
        out.append(f'<span id="{sid}-w{i}" class="{cls}">{w}</span>')
    return " ".join(out)

P1 = "Cek pola iklan SKINKU minggu ini yang paling banyak menghasilkan penjualan."
P1_T = [t(79), t(80), t(81), t(83), t(84), t(85), t(86), t(87), t(88), t(89), t(90)]
P2 = "Bikin 7 materi iklan baru pakai Higgsfield, lalu luncurkan campaign konversi tinggi di Meta."
P2_T = [t(124), t(125), t(126), t(127), t(128), t(129), t(130), t(131), t(132) + 0.2, t(134), t(135), t(136), t(138), t(139)]

ICON_AD = '<svg viewBox="0 0 200 200"><rect x="20" y="34" width="132" height="104" rx="12" fill="#fff" stroke="#18213A" stroke-width="7"/><rect x="38" y="54" width="60" height="12" rx="6" fill="#18213A"/><rect x="38" y="76" width="92" height="10" rx="5" fill="#D9D6CF"/><rect x="38" y="96" width="74" height="10" rx="5" fill="#D9D6CF"/><circle cx="132" cy="128" r="34" fill="#F4F1EA" stroke="#7B1834" stroke-width="9"/><line x1="156" y1="152" x2="182" y2="178" stroke="#7B1834" stroke-width="12" stroke-linecap="round"/></svg>'
ICON_COMP = '<svg viewBox="0 0 200 200"><line x1="24" y1="170" x2="180" y2="170" stroke="#18213A" stroke-width="7" stroke-linecap="round"/><rect x="34" y="96" width="28" height="74" rx="6" fill="#18213A"/><rect x="68" y="60" width="28" height="110" rx="6" fill="#7B1834"/><rect x="112" y="118" width="28" height="52" rx="6" fill="#18213A"/><rect x="146" y="82" width="28" height="88" rx="6" fill="#D9D6CF"/><circle cx="82" cy="36" r="10" fill="#7B1834"/></svg>'
ICON_VIS = '<svg viewBox="0 0 200 200"><rect x="22" y="34" width="156" height="132" rx="14" fill="#fff" stroke="#18213A" stroke-width="7"/><circle cx="136" cy="74" r="16" fill="#7B1834"/><path d="M34 150 L84 92 L116 128 L136 108 L166 150 Z" fill="#18213A"/></svg>'
ICON_UP = '<svg viewBox="0 0 200 200"><path d="M36 120 V160 H164 V120" fill="none" stroke="#18213A" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><line x1="100" y1="132" x2="100" y2="42" stroke="#7B1834" stroke-width="12" stroke-linecap="round"/><path d="M64 76 L100 40 L136 76" fill="none" stroke="#7B1834" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_SET = '<svg viewBox="0 0 200 200"><line x1="34" y1="56" x2="166" y2="56" stroke="#D9D6CF" stroke-width="10" stroke-linecap="round"/><line x1="34" y1="100" x2="166" y2="100" stroke="#D9D6CF" stroke-width="10" stroke-linecap="round"/><line x1="34" y1="144" x2="166" y2="144" stroke="#D9D6CF" stroke-width="10" stroke-linecap="round"/><circle cx="120" cy="56" r="16" fill="#18213A"/><circle cx="70" cy="100" r="16" fill="#7B1834"/><circle cx="140" cy="144" r="16" fill="#18213A"/></svg>'
CHECK = '<svg viewBox="0 0 40 40"><path d="M10 21 L17 28 L30 13" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---- scenes ----------------------------------------------------------------------------------
S = {}
S["s01"] = f'''
<div class="ground paper"></div>
<div id="s01-badge" class="badge">CLAUDE + MCP</div>
<div class="hl-block" style="top:310px">
  <div id="s01-l1" class="serif" style="font-size:138px;line-height:1">1 PLUGIN =</div>
  <div id="s01-l2" class="sans" style="font-size:122px;line-height:.95;margin-top:14px;letter-spacing:-.02em">1 TIM <span class="burg">MARKETING?</span></div>
  <div id="s01-rule" class="rule" style="width:420px;margin-top:26px"></div>
</div>
<div id="s01-char" class="seat" data-layout-allow-overflow style="left:-170px;top:880px;width:820px"><img id="s01-char-img" src="assets/char-seated.png" alt=""></div>
'''
S["s02"] = f'''
<div class="ground paper"></div>
<div class="num-window" style="left:84px;top:500px;width:470px;height:330px"><div id="s02-strip" class="num-strip" data-layout-allow-overflow data-layout-allow-occlusion>{"".join(f"<div>{i}</div>" for i in range(17))}</div></div>
<div id="s02-label" class="sans" style="position:absolute;left:90px;top:860px;font-size:66px;letter-spacing:-.01em">SKILL <span class="burg">SIAP PAKAI</span></div>
<div class="dots" style="left:520px;top:640px">{"".join(f'<i id="s02-d{i}"></i>' for i in range(3))}</div>
<div id="s02-stack" class="stack" style="left:600px;top:500px">
  {"".join(f'<div id="s02-c{i}" class="mini-card"><span class="sq"></span><span class="ln" style="width:70%"></span><span class="ln" style="width:52%"></span><span class="ln" style="width:62%"></span></div>' for i in range(4))}
</div>
{pwin("s02", ["seated-head"])}
'''
cards3 = [("BEDAH IKLAN", ICON_AD), ("RISET KOMPETITOR", ICON_COMP), ("VISUAL CAMPAIGN", ICON_VIS)]
S["s03"] = f'''
<div class="ground paper"></div>
<div class="row3" style="top:300px">
  {"".join(f'<div id="s03-k{i}" class="vcard"><div class="vnum">0{i+1}</div><div class="vicon">{ic}</div><div class="vlabel">{lb}</div><div id="s03-ok{i}" class="okdot">{CHECK}</div></div>' for i,(lb,ic) in enumerate(cards3))}
</div>
<svg id="s03-arrow" class="arrowline" style="left:90px;top:1040px" width="810" height="60" viewBox="0 0 810 60">
  <path id="s03-ap" d="M20 30 H790" stroke="#7B1834" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path id="s03-ah" d="M770 14 L792 30 L770 46" stroke="#7B1834" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
{pwin("s03", ["talk", "smile"])}
'''
# 7 nodes around the hub
HX, HY, RAD = 495, 820, 262
nodes = ""
lines = ""
for i in range(7):
    a = -math.pi / 2 + i * 2 * math.pi / 7
    x, y = HX + RAD * math.cos(a), HY + RAD * math.sin(a)
    nodes += f'<div id="s04-n{i}" class="node" style="left:{x-54:.0f}px;top:{y-54:.0f}px"><div class="agent"><i></i><b></b></div></div>'
    lines += f'<line id="s04-l{i}" x1="{HX}" y1="{HY}" x2="{x:.0f}" y2="{y:.0f}" stroke="#18213A" stroke-width="4" stroke-dasharray="{RAD}" stroke-dashoffset="{RAD}"/>'
S["s04"] = f'''
<div class="ground paper"></div>
<div style="position:absolute;left:90px;top:200px;display:flex;align-items:flex-start;gap:26px">
  <div id="s04-seven" class="sans burg tnum" style="font-size:236px;line-height:.86">7</div>
  <div>
    <div id="s04-title" class="sans" style="font-size:74px;line-height:.98;width:560px;letter-spacing:-.01em;margin-top:10px">KARYAWAN DIGITAL</div>
    <div id="s04-tag" class="tag" style="margin-top:22px">AI AGENTS</div>
  </div>
</div>
<div id="s04-ring" class="ring">
  <svg class="full" viewBox="0 0 1080 1920" width="1080" height="1920">{lines}</svg>
  {nodes}
</div>
<div id="s04-hub" class="hub" style="left:{HX-118}px;top:{HY-118}px">CLAUDE</div>
<div class="chips" style="top:1176px">
  <div id="s04-ch1" class="chip">KERJA BARENG</div>
  <div id="s04-ch2" class="chip solid">KHUSUS AKUN KALIAN</div>
</div>
{pwin("s04", ["smile2", "confident"])}
'''
S["s05"] = f'''
<div class="ground paper"></div>
<div class="hl-block" style="top:210px">
  <div id="s05-l1" class="serif" style="font-size:96px;line-height:1.02">PASANG DALAM</div>
  <div id="s05-l2" class="sans" style="font-size:92px;line-height:1;letter-spacing:-.02em">HITUNGAN <span class="burg">DETIK</span></div>
</div>
<div id="s05-browser" class="browser" style="top:480px">
  <div class="bbar"><i></i><i></i><i></i><span class="addr"></span></div>
  <div class="bbody">
    <div class="code"><span style="width:62%"></span><span style="width:84%"></span><span style="width:48%"></span></div>
    <div id="s05-clip" class="clipbtn"><svg viewBox="0 0 40 40"><rect x="9" y="8" width="22" height="27" rx="4" fill="none" stroke="#fff" stroke-width="3.5"/><rect x="14" y="4" width="12" height="8" rx="3" fill="#fff"/></svg></div>
  </div>
</div>
<div id="s05-ghost" class="ghost"><span style="width:70%"></span><span style="width:50%"></span></div>
<div id="s05-st1" class="step" style="top:800px"><div class="stepnum">01</div><div class="steptx">COPY MCP SERVER</div></div>
<div id="s05-vline" class="vline" style="top:926px;height:86px"></div>
<div id="s05-st2" class="step" style="top:1018px"><div class="stepnum navy">02</div><div class="steptx">CONNECT KE CLAUDE</div>
  <div class="lock"><div id="s05-shackle" class="shackle"></div><div id="s05-lockbody" class="lockbody"></div></div></div>
{pwin("s05", ["seated-head"])}
'''
S["s06"] = f'''
<div class="ground paper"></div>
<div id="s06-card" class="prompt" style="top:300px">
  <div class="phead"><span class="chev">›</span><i></i><i></i><i></i></div>
  <div id="s06-caret" class="caret"></div><div class="ptext" style="font-size:60px">{words_spans("s06", P1, {"SKINKU", "penjualan"})}</div>
  <div id="s06-send" class="send"><svg viewBox="0 0 40 40"><path d="M20 30 V11 M11 19 L20 10 L29 19" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</div>
<div class="dots" style="left:120px;top:1010px">{"".join(f'<i id="s06-d{i}"></i>' for i in range(3))}</div>
{pwin("s06", ["talk2", "talk"])}
'''
S["s07"] = f'''
<div class="ground paper"></div>
<div class="hl-block" style="top:200px">
  <div id="s07-l1" class="sans" style="font-size:80px;line-height:.98;letter-spacing:-.02em">DATA LIVE DARI <span class="burg">META</span></div>
  <div id="s07-l2" class="serif" style="font-size:56px;line-height:1.1;margin-top:12px;color:#7B1834">ANALISIS LANGSUNG DI CLAUDE</div>
</div>
<div class="pipe" style="top:560px">
  <div id="s07-p1" class="pnode">META</div>
  <div id="s07-p2" class="pnode navyfill"><span class="live"></span>DATA LIVE</div>
  <div id="s07-p3" class="pnode burgfill">CLAUDE</div>
</div>
<svg class="full" viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;left:0;top:0">
  <line id="s07-a1" x1="320" y1="636" x2="380" y2="636" stroke="#7B1834" stroke-width="5" stroke-dasharray="60" stroke-dashoffset="60"/>
  <line id="s07-a2" x1="610" y1="636" x2="670" y2="636" stroke="#7B1834" stroke-width="5" stroke-dasharray="60" stroke-dashoffset="60"/>
</svg>
{"".join(f'<div id="s07-pk{i}" class="packet" style="top:628px"></div>' for i in range(4))}
<div id="s07-chart" class="chart" style="top:780px">
  <div class="bars">{"".join(f'<i id="s07-b{i}" style="height:{h}%"></i>' for i,h in enumerate([38,56,47,72,64,88]))}</div>
  <div class="minis"><div id="s07-m1" class="mini"><span style="width:70%"></span><span style="width:46%"></span></div><div id="s07-m2" class="mini"><span style="width:58%"></span><span style="width:80%"></span></div></div>
</div>
{pwin("s07", ["confident"])}
'''
S["s08"] = f'''
<div class="ground navy"></div>
<div class="shutter">{"".join(f'<i id="s08-sh{i}"></i>' for i in range(6))}</div>
<div class="hl-block" style="top:270px">
  <div class="mask"><div id="s08-l1" class="sans" style="font-size:100px;color:#F4F1EA;letter-spacing:-.01em">INI BAGIAN</div></div>
  <div class="mask"><div id="s08-l2" class="serif" style="font-size:158px;line-height:.98;color:#F4F1EA">PALING BRUTAL.</div></div>
  <div id="s08-slash" class="slash"></div>
</div>
<div class="lockup" style="top:900px">
  <div id="s08-c1" class="opill">CLAUDE</div>
  <div id="s08-plus" class="plus">+</div>
  <div id="s08-c2" class="opill"><span id="s08-c2t">HIGGSFIELD</span></div>
</div>
{pwin("s08", ["confident", "yapping"], dark=True)}
'''
tiles = ""
for i in range(7):
    kinds = [
        '<i style="left:18%;top:18%;width:64%;height:40%;background:#18213A;border-radius:10px"></i><i style="left:18%;top:66%;width:50%;height:8%;background:#7B1834;border-radius:4px"></i>',
        '<i style="left:22%;top:22%;width:56%;height:36%;background:#7B1834;border-radius:50%"></i><i style="left:16%;top:70%;width:68%;height:8%;background:#18213A;border-radius:4px"></i>',
        '<i style="left:0;top:0;width:100%;height:52%;background:#7B1834"></i><i style="left:16%;top:64%;width:58%;height:8%;background:#7B1834;border-radius:4px"></i><i style="left:16%;top:78%;width:40%;height:7%;background:#D9D6CF;border-radius:4px"></i>',
        '<i style="left:14%;top:14%;width:72%;height:72%;border:6px solid #7B1834;border-radius:12px;box-sizing:border-box"></i><i style="left:34%;top:34%;width:32%;height:32%;background:#18213A;border-radius:6px"></i>',
        '<i style="left:0;top:48%;width:100%;height:52%;background:#7B1834"></i><i style="left:20%;top:16%;width:44%;height:22%;background:#18213A;border-radius:6px"></i>',
        '<i style="left:16%;top:16%;width:30%;height:30%;background:#18213A;border-radius:6px"></i><i style="left:54%;top:16%;width:30%;height:30%;background:#7B1834;border-radius:6px"></i><i style="left:16%;top:54%;width:68%;height:30%;background:#D9D6CF;border-radius:6px"></i>',
        '<i style="left:30%;top:12%;width:40%;height:46%;background:#18213A;border-radius:40px 40px 8px 8px"></i><i style="left:14%;top:68%;width:72%;height:9%;background:#7B1834;border-radius:4px"></i>',
    ]
    tiles += f'<div id="s09-t{i}" class="tile">{kinds[i]}</div>'
S["s09"] = f'''
<div class="ground navy"></div>
<div id="s09-card" class="prompt light" style="top:220px">
  <div class="phead"><span class="chev">›</span><i></i><i></i><i></i></div>
  <div id="s09-caret" class="caret"></div><div class="ptext" style="font-size:50px">{words_spans("s09", P2, {"7", "Higgsfield", "Meta"})}</div>
</div>
<div id="s09-lbl" class="sans" style="position:absolute;left:90px;top:650px;font-size:62px;color:#F4F1EA;display:flex;align-items:center;gap:18px"><span id="s09-seven" class="sevenchip">7</span>MATERI IKLAN</div>
<div class="tiles" style="top:770px">{tiles}</div>
<svg class="full" viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;left:0;top:0">
  <path id="s09-ar" d="M495 962 V1032" stroke="#F4F1EA" stroke-width="5" fill="none" stroke-dasharray="70" stroke-dashoffset="70" stroke-linecap="round"/>
  <path id="s09-arh" d="M481 1020 L495 1036 L509 1020" stroke="#F4F1EA" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<div id="s09-meta" class="metacard" style="top:1048px"><div class="sans" style="font-size:46px;color:#18213A">META</div>
  <div class="mbars"><span style="width:70%"></span><span style="width:46%"></span></div>
  <div class="toggle"><div id="s09-knob" class="knob"></div></div></div>
{pwin("s09", ["talk2"], dark=True)}
'''
cols = [("BUAT VISUAL", ICON_VIS), ("UPLOAD", ICON_UP), ("ATUR CAMPAIGN", ICON_SET)]
S["s10"] = f'''
<div class="ground paper"></div>
<div id="s10-jm" class="stamp" style="top:220px">JALAN MAKSIMAL</div>
<div class="row3" style="top:390px">
  {"".join(f'<div id="s10-k{i}" class="vcard short"><div class="vnum">0{i+1}</div><div class="vicon">{ic}</div><div class="vlabel">{lb}</div></div>' for i,(lb,ic) in enumerate(cols))}
</div>
<div class="track" style="top:1010px"><div id="s10-fill" class="fill"></div>
  {"".join(f'<div id="s10-ck{i}" class="ck" data-layout-allow-overflow style="left:{125 + i*280}px">{CHECK}</div>' for i in range(3))}
</div>
{pwin("s10", ["smile", "confident"])}
'''
scat = [(130, 560, -9), (420, 530, 6), (690, 575, -4), (210, 720, 5), (520, 700, -7), (760, 735, 8)]
S["s11"] = f'''
<div class="ground paper"></div>
<div class="hl-block" style="top:200px">
  <div id="s11-l1" class="sans" style="font-size:76px;line-height:1;letter-spacing:-.02em">STOP OPERASIONAL <span id="s11-man" class="strike">MANUAL<i id="s11-strk"></i></span></div>
  <div id="s11-l2" class="serif" style="font-size:84px;line-height:1.05;margin-top:18px;color:#7B1834">SCALE UP PAKAI SISTEM</div>
</div>
<div id="s11-cards">{"".join(f'<div id="s11-m{i}" class="task" style="left:{x}px;top:{y}px"><span style="width:64%"></span><span style="width:44%"></span></div>' for i,(x,y,r) in enumerate(scat))}</div>
<div id="s11-sys" class="syscard" style="top:580px"><div class="syscheck">{CHECK}</div><div class="sysl"><span style="width:78%"></span><span style="width:56%"></span><span style="width:66%"></span></div></div>
<div id="s11-char" class="seat" data-layout-allow-overflow style="left:-170px;top:970px;width:760px"><img id="s11-char-img" src="assets/char-seated.png" alt=""></div>
'''
S["s12"] = f'''
<div class="ground paper"></div>
<div class="cta-wrap" style="top:470px">
  <div id="s12-pill" class="cta">KOMEN ‘META’</div>
  <div id="s12-ul" class="rule" style="width:520px;margin:30px auto 0"></div>
  <div id="s12-sub" class="serif" style="font-size:54px;margin-top:40px;text-align:center;color:#111318;white-space:nowrap">Gue kirimin link-nya lewat DM.</div>
</div>
{pwin("s12", ["yapping"], left=90, top=990, w=330, h=370)}
<div id="s12-fade" class="whiteout"></div>
'''

scene_html = ""
for k, (sid, st, kind, tr) in enumerate(SC):
    s, d = win(k)
    scene_html += (f'<section id="{sid}" class="clip scene" data-start="{s}" data-duration="{d}" data-track-index="{1 + k % 2}" style="z-index:{10 + k}">'
                   f'<div id="{sid}-stage" class="stage">{S[sid]}</div></section>\n')

# ---- timeline script -------------------------------------------------------------------------
JS = []
def a(s): JS.append(s)

# transitions
for k in range(1, len(SC)):
    sid, b, kind, tr = SC[k]
    prev = SC[k - 1][0]
    if kind == "push":
        a(f'tl.fromTo("#{sid}-stage",{{x:1080}},{{x:0,duration:{tr},ease:"power3.inOut"}},{b});')
        a(f'tl.fromTo("#{prev}-stage",{{x:0}},{{x:-1080,duration:{tr},ease:"power3.inOut",immediateRender:false}},{b});')
    elif kind == "pushup":
        a(f'tl.fromTo("#{sid}-stage",{{y:1920}},{{y:0,duration:{tr},ease:"power3.inOut"}},{b});')
        a(f'tl.fromTo("#{prev}-stage",{{y:0}},{{y:-1920,duration:{tr},ease:"power3.inOut",immediateRender:false}},{b});')
    elif kind == "wipe":
        a(f'tl.fromTo("#{sid}-stage",{{clipPath:"polygon(150% 0%, 260% 0%, 260% 100%, 190% 100%)"}},{{clipPath:"polygon(-70% 0%, 260% 0%, 260% 100%, -30% 100%)",duration:{tr},ease:"power2.inOut"}},{b});')
        a(f'tl.fromTo("#{sid}-strip",{{clipPath:"polygon(140% 0%, 150% 0%, 190% 100%, 180% 100%)"}},{{clipPath:"polygon(-80% 0%, -70% 0%, -30% 100%, -40% 100%)",duration:{tr},ease:"power2.inOut"}},{b});')
        a(f'tl.fromTo("#{prev}-stage",{{x:0}},{{x:-120,duration:{tr},ease:"power2.inOut",immediateRender:false}},{b});')
    elif kind == "cover":
        a(f'tl.fromTo("#{sid}-stage",{{y:1920,borderRadius:56}},{{y:0,borderRadius:0,duration:{tr},ease:"power3.out"}},{b});')
        a(f'tl.fromTo("#{prev}-stage",{{scale:1,y:0}},{{scale:.92,y:-60,duration:{tr},ease:"power2.inOut",immediateRender:false}},{b});')

def ent(sel, frm, to, at):
    a(f'tl.fromTo("{sel}",{frm},{to},{at:.3f});')

# S01 hook
ent("#s01-char", "{y:80,scale:.96,opacity:0,transformOrigin:'0% 100%'}", "{y:0,scale:1,opacity:1,duration:.6,ease:'power3.out'}", 0.0)
a('tl.to("#s01-char-img",{y:-14,duration:1.1,yoyo:true,repeat:3,ease:"sine.inOut"},0.7);')
ent("#s01-badge", "{scale:.7,opacity:0}", "{scale:1,opacity:1,duration:.32,ease:'back.out(1.6)'}", 0.18)
ent("#s01-l1", "{clipPath:'inset(0% 100% 0% 0%)'}", "{clipPath:'inset(0% 0% 0% 0%)',duration:.5,ease:'power3.inOut'}", 0.18)
ent("#s01-l2", "{x:260,opacity:0}", "{x:0,opacity:1,duration:.45,ease:'power4.out'}", 0.78)
ent("#s01-rule", "{scaleX:0,transformOrigin:'0% 50%'}", "{scaleX:1,duration:.5,ease:'power2.out'}", t(12))

# S02 16 skills
b = SC[1][1]
ent("#s02-c0", "{opacity:0,y:40}", "{opacity:1,y:0,duration:.3,ease:'power2.out'}", b + 0.25)
for i, (r, x) in enumerate([(-10, -20), (-3, 10), (4, 40), (11, 70)]):
    ent(f"#s02-c{i}", "{rotate:0,x:0}", f"{{rotate:{r},x:{x},duration:.42,ease:'back.out(1.4)'}}", b + 0.45 + i * 0.12)
ent("#s02-strip", "{yPercent:0}", "{yPercent:-94.1176,duration:.7,ease:'power3.out'}", t(20) - 0.45)
a(f'tl.set("#s02-strip > div:not(:last-child)",{{opacity:0}},{t(20)+0.27:.3f});')
ent(".num-window", "{opacity:0}", "{opacity:1,duration:.2}", b + 0.2)
a(f'tl.to(".num-window",{{scale:1.06,duration:.16,ease:"power2.out",yoyo:true,repeat:1}},{t(20)+0.28:.3f});')
ent("#s02-label", "{clipPath:'inset(100% 0% 0% 0%)',y:20}", "{clipPath:'inset(0% 0% 0% 0%)',y:0,duration:.4,ease:'power3.out'}", t(21) - 0.1)
for i in range(3):
    ent(f"#s02-d{i}", "{backgroundColor:'#D9D6CF',scale:.6}", "{backgroundColor:'#7B1834',scale:1,duration:.2}", t(21) + 0.15 + i * 0.12)
ent("#s02-pw", "{y:40,opacity:0}", "{y:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.3)

# S03 scope
b = SC[2][1]
ent("#s03-k0", "{x:-300,opacity:0}", "{x:0,opacity:1,duration:.45,ease:'power3.out'}", t(26) - 0.15)
ent("#s03-k1", "{scale:.6,opacity:0}", "{scale:1,opacity:1,duration:.45,ease:'back.out(1.5)'}", t(28) - 0.1)
ent("#s03-k2", "{clipPath:'inset(0% 0% 100% 0%)'}", "{clipPath:'inset(0% 0% 0% 0%)',duration:.5,ease:'power3.inOut'}", t(30))
ent("#s03-ap", "{strokeDasharray:770,strokeDashoffset:770}", "{strokeDashoffset:0,duration:.7,ease:'power2.inOut'}", t(32))
ent("#s03-ah", "{opacity:0,x:-10}", "{opacity:1,x:0,duration:.2}", t(32) + 0.6)
for i in range(3):
    ent(f"#s03-ok{i}", "{scale:0}", "{scale:1,duration:.3,ease:'back.out(2)'}", t(40) + i * 0.14)
ent("#s03-pw", "{x:-60,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.3)
a(f'tl.set("#s03-px-talk",{{opacity:0}},{t(40):.3f}); tl.set("#s03-px-smile",{{opacity:1}},{t(40):.3f});')

# S04 seven agents
b = SC[3][1]
ent("#s04-hub", "{scale:0}", "{scale:1,duration:.45,ease:'back.out(1.6)'}", b + 0.3)
ent("#s04-seven", "{yPercent:60,opacity:0}", "{yPercent:0,opacity:1,duration:.4,ease:'power3.out'}", t(45) - 0.12)
a(f'tl.to("#s04-seven",{{scale:1.06,duration:.18,yoyo:true,repeat:1,ease:"power2.out"}},{t(45)+0.32:.3f});')
ent("#s04-title", "{x:80,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power3.out'}", t(46) - 0.1)
for grp, at in [([0, 1], t(46)), ([2, 3], t(47)), ([4, 5, 6], t(47) + 0.42)]:
    for j, i in enumerate(grp):
        ent(f"#s04-n{i}", "{scale:0,opacity:0}", "{scale:1,opacity:1,duration:.35,ease:'back.out(1.8)'}", at + j * 0.06)
        ent(f"#s04-l{i}", "{strokeDashoffset:262}", "{strokeDashoffset:0,duration:.35,ease:'power2.out'}", at + j * 0.06 - 0.1)
ent("#s04-ring", "{rotate:-4}", "{rotate:4,duration:5.2,ease:'sine.inOut',transformOrigin:'495px 820px'}", b + 0.4)
ent("#s04-tag", "{clipPath:'inset(0% 100% 0% 0%)'}", "{clipPath:'inset(0% 0% 0% 0%)',duration:.35,ease:'power2.out'}", t(48) - 0.05)
ent("#s04-ch1", "{y:30,opacity:0}", "{y:0,opacity:1,duration:.3,ease:'power2.out'}", t(51) - 0.05)
ent("#s04-ch2", "{x:60,opacity:0}", "{x:0,opacity:1,duration:.3,ease:'power2.out'}", t(53) - 0.05)
ent("#s04-pw", "{scale:.8,opacity:0}", "{scale:1,opacity:1,duration:.35,ease:'back.out(1.6)'}", b + 0.35)
a(f'tl.set("#s04-px-smile2",{{opacity:0}},{t(53):.3f}); tl.set("#s04-px-confident",{{opacity:1}},{t(53):.3f});')

# S05 install
b = SC[4][1]
ent("#s05-l1", "{clipPath:'inset(0% 100% 0% 0%)'}", "{clipPath:'inset(0% 0% 0% 0%)',duration:.45,ease:'power3.inOut'}", b + 0.2)
ent("#s05-l2", "{x:200,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power4.out'}", t(60) - 0.1)
ent("#s05-browser", "{scale:.9,opacity:0}", "{scale:1,opacity:1,duration:.45,ease:'power3.out'}", t(62) - 0.2)
ent("#s05-st1", "{x:-120,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power3.out'}", t(63) - 0.1)
a(f'tl.to("#s05-clip",{{scale:1.18,duration:.14,yoyo:true,repeat:1}},{t(63)+0.1:.3f});')
ent("#s05-ghost", "{opacity:0,y:0}", "{opacity:1,y:0,duration:.12}", t(64))
a(f'tl.to("#s05-ghost",{{y:170,x:-340,scale:.5,opacity:0,duration:.55,ease:"power2.in"}},{t(64)+0.14:.3f});')
ent("#s05-vline", "{scaleY:0,transformOrigin:'50% 0%'}", "{scaleY:1,duration:.5,ease:'power2.inOut'}", t(68) - 0.2)
ent("#s05-st2", "{x:120,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power3.out'}", t(69) - 0.1)
ent("#s05-shackle", "{y:-16}", "{y:0,duration:.22,ease:'power4.in'}", t(71))
ent("#s05-lockbody", "{backgroundColor:'#18213A'}", "{backgroundColor:'#7B1834',duration:.15}", t(71) + 0.2)
ent("#s05-pw", "{y:50,opacity:0}", "{y:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.35)

# S06 first command (type-on synced to the spoken words)
b = SC[5][1]
ent("#s06-card", "{x:140,opacity:0}", "{x:0,opacity:1,duration:.45,ease:'power3.out'}", b + 0.25)
for i, at in enumerate(P1_T):
    ent(f"#s06-w{i}", "{opacity:0,y:14}", "{opacity:1,y:0,duration:.14,ease:'power2.out'}", at - 0.04)
ent("#s06-send", "{backgroundColor:'#D9D6CF',scale:.85}", "{backgroundColor:'#7B1834',scale:1,duration:.25,ease:'back.out(2)'}", W[90]["end"] - 0.1)
for i in range(3):
    ent(f"#s06-d{i}", "{scale:.5,opacity:.3}", "{scale:1,opacity:1,duration:.2,yoyo:true,repeat:5}", b + 0.6 + i * 0.12)
ent("#s06-pw", "{x:-60,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.35)
a(f'tl.set("#s06-px-talk2",{{opacity:0}},{t(83):.3f}); tl.set("#s06-px-talk",{{opacity:1}},{t(83):.3f});')

# S07 live data
b = SC[6][1]
ent("#s07-l1", "{clipPath:'inset(0% 100% 0% 0%)'}", "{clipPath:'inset(0% 0% 0% 0%)',duration:.45,ease:'power3.inOut'}", b + 0.3)
ent("#s07-l2", "{y:30,opacity:0}", "{y:0,opacity:1,duration:.4,ease:'power2.out'}", t(93))
for i, at in enumerate([t(94), t(95), t(96)]):
    ent(f"#s07-p{i+1}", "{y:-40,opacity:0}", "{y:0,opacity:1,duration:.32,ease:'power3.out'}", at - 0.1)
ent("#s07-a1", "{strokeDashoffset:60}", "{strokeDashoffset:0,duration:.25}", t(95) - 0.05)
ent("#s07-a2", "{strokeDashoffset:60}", "{strokeDashoffset:0,duration:.25}", t(96) - 0.05)
for i in range(4):
    ent(f"#s07-pk{i}", "{x:300,opacity:0}", "{x:690,opacity:1,duration:.9,ease:'none',repeat:2}", t(96) + 0.2 + i * 0.22)
for i in range(6):
    ent(f"#s07-b{i}", "{scaleY:0,transformOrigin:'50% 100%'}", "{scaleY:1,duration:.5,ease:'power3.out'}", t(97) + i * 0.08)
ent("#s07-chart", "{opacity:0,y:60}", "{opacity:1,y:0,duration:.4,ease:'power2.out'}", t(95))
ent("#s07-m1", "{x:40,opacity:0}", "{x:0,opacity:1,duration:.3}", t(99))
ent("#s07-m2", "{x:40,opacity:0}", "{x:0,opacity:1,duration:.3}", t(99) + 0.15)
ent("#s07-pw", "{scale:.8,opacity:0}", "{scale:1,opacity:1,duration:.35,ease:'back.out(1.6)'}", b + 0.35)

# S08 escalation (navy)
b = SC[7][1]
for i in range(6):
    ent(f"#s08-sh{i}", "{scaleY:1}", "{scaleY:0,duration:.22,ease:'power3.in'}", b + 0.32 + i * 0.035)
ent("#s08-l1", "{yPercent:105}", "{yPercent:0,duration:.3,ease:'power4.out'}", t(102) - 0.05)
ent("#s08-l2", "{yPercent:105}", "{yPercent:0,duration:.34,ease:'power4.out'}", t(104) - 0.05)
ent("#s08-slash", "{scaleX:0,transformOrigin:'0% 50%'}", "{scaleX:1,duration:.3,ease:'power3.out'}", t(105) + 0.3)
ent("#s08-c1", "{x:-80,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power3.out'}", t(108))
ent("#s08-plus", "{scale:0,rotate:-90}", "{scale:1,rotate:0,duration:.3,ease:'back.out(2)'}", t(112))
ent("#s08-c2", "{x:80,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power3.out'}", t(112) + 0.15)
ent("#s08-c2t", "{opacity:0,y:20}", "{opacity:1,y:0,duration:.25,ease:'power2.out'}", t(116) - 0.05)
a(f'tl.to("#s08-c2",{{scale:1.06,duration:.15,yoyo:true,repeat:1}},{t(116)+0.2:.3f});')
ent("#s08-pw", "{y:60,opacity:0}", "{y:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.4)
a(f'tl.set("#s08-px-confident",{{opacity:0}},{t(105):.3f}); tl.set("#s08-px-yapping",{{opacity:1}},{t(105):.3f});')

# S09 second command
b = SC[8][1]
ent("#s09-card", "{y:-80,opacity:0}", "{y:0,opacity:1,duration:.45,ease:'power3.out'}", b + 0.3)
for i, at in enumerate(P2_T):
    ent(f"#s09-w{i}", "{opacity:0,y:14}", "{opacity:1,y:0,duration:.14,ease:'power2.out'}", at - 0.04)
ent("#s09-lbl", "{x:-60,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power3.out'}", t(125) - 0.05)
a(f'tl.to("#s09-seven",{{scale:1.06,duration:.16,yoyo:true,repeat:1}},{t(125)+0.3:.3f});')
for i in range(7):
    ent(f"#s09-t{i}", f"{{x:{(3 - i) * 118},rotate:{(i - 3) * 3},opacity:0}}", "{x:0,rotate:0,opacity:1,duration:.5,ease:'power3.out'}", t(126) + i * 0.07)
ent("#s09-ar", "{strokeDashoffset:70}", "{strokeDashoffset:0,duration:.35}", t(133))
ent("#s09-arh", "{opacity:0}", "{opacity:1,duration:.15}", t(133) + 0.3)
ent("#s09-meta", "{y:60,opacity:0}", "{y:0,opacity:1,duration:.4,ease:'power3.out'}", t(134) - 0.1)
ent("#s09-knob", "{x:0}", "{x:44,duration:.25,ease:'power2.out'}", t(139))
ent(".toggle", "{backgroundColor:'#D9D6CF'}", "{backgroundColor:'#7B1834',duration:.25}", t(139))
ent("#s09-pw", "{x:-60,opacity:0}", "{x:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.4)

# S10 pipeline
b = SC[9][1]
for i in range(3):
    ent(f"#s10-k{i}", "{y:80,opacity:0}" if i != 1 else "{scale:.8,opacity:0}", "{y:0,scale:1,opacity:1,duration:.45,ease:'power3.out'}", b + 0.45 + i * 0.35)
ent("#s10-fill", "{scaleX:0,transformOrigin:'0% 50%'}", "{scaleX:.34,duration:.6,ease:'power2.inOut'}", t(144))
ent("#s10-ck0", "{scale:0}", "{scale:1,duration:.3,ease:'back.out(2)'}", t(144) + 0.5)
a(f'tl.to("#s10-fill",{{scaleX:.67,duration:.6,ease:"power2.inOut"}},{t(147):.3f});')
ent("#s10-ck1", "{scale:0}", "{scale:1,duration:.3,ease:'back.out(2)'}", t(147) + 0.5)
a(f'tl.to("#s10-fill",{{scaleX:1,duration:1.4,ease:"power1.inOut"}},{t(151):.3f});')
ent("#s10-ck2", "{scale:0}", "{scale:1,duration:.3,ease:'back.out(2)'}", t(151) + 1.4)
ent("#s10-jm", "{scale:1.3,opacity:0}", "{scale:1,opacity:1,duration:.32,ease:'power4.out'}", t(156) - 0.08)
ent("#s10-pw", "{y:50,opacity:0}", "{y:0,opacity:1,duration:.35,ease:'power2.out'}", b + 0.4)
a(f'tl.set("#s10-px-smile",{{opacity:0}},{t(156):.3f}); tl.set("#s10-px-confident",{{opacity:1}},{t(156):.3f});')

# S11 payoff
b = SC[10][1]
ent("#s11-char", "{y:120,opacity:0}", "{y:0,opacity:1,duration:.55,ease:'power3.out'}", b + 0.2)
a(f'tl.to("#s11-stage",{{scale:1.015,duration:3.5,ease:"none",transformOrigin:"50% 40%"}},{b+0.4:.3f});')
ent("#s11-l1", "{x:-120,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power3.out'}", t(158) + 0.05)
for i, (x, y, r) in enumerate(scat):
    ent(f"#s11-m{i}", f"{{scale:.5,opacity:0,rotate:{r}}}", f"{{scale:1,opacity:1,rotate:{r},duration:.3,ease:'back.out(1.6)'}}", t(160) + i * 0.08)
ent("#s11-strk", "{scaleX:0,transformOrigin:'0% 50%'}", "{scaleX:1,duration:.3,ease:'power3.out'}", t(164) + 0.1)
for i, (x, y, r) in enumerate(scat):
    a(f'tl.to("#s11-m{i}",{{x:{455 - x - 100},y:{660 - y},rotate:0,scale:.4,opacity:0,duration:.45,ease:"power3.in"}},{t(166)-0.1+i*0.03:.3f});')
ent("#s11-sys", "{scale:.6,opacity:0}", "{scale:1,opacity:1,duration:.4,ease:'back.out(1.6)'}", t(167) - 0.05)
ent("#s11-l2", "{y:40,opacity:0}", "{y:0,opacity:1,duration:.4,ease:'power3.out'}", t(167) - 0.1)

# S12 CTA
b = SC[11][1]
ent("#s12-pill", "{scale:.55,opacity:0}", "{scale:1,opacity:1,duration:.42,ease:'power4.out'}", t(172) - 0.02)
a(f'tl.to("#s12-pill",{{scale:1.06,duration:.16,yoyo:true,repeat:1,ease:"power2.out"}},{t(174):.3f});')
ent("#s12-ul", "{scaleX:0,transformOrigin:'50% 50%'}", "{scaleX:1,duration:.4,ease:'power2.out'}", t(174))
ent("#s12-sub", "{y:30,opacity:0}", "{y:0,opacity:1,duration:.4,ease:'power3.out'}", t(175) - 0.05)
ent("#s12-pw", "{x:-80,opacity:0}", "{x:0,opacity:1,duration:.4,ease:'power3.out'}", b + 0.3)
ent("#s12-fade", "{opacity:0}", "{opacity:1,duration:.45,ease:'power1.in'}", DUR - 0.45)


# ambient: subtle portrait breathing (scale from the bottom edge, no gap), finite
for k,(sid, st, kind, tr) in enumerate(SC):
    if f'id="{sid}-pw"' in S[sid]:
        s0, d0 = win(k)
        reps = max(1, int((d0 - 1.0) / 1.4) - 1)
        a(f'tl.to("#{sid}-pwi",{{scale:1.025,transformOrigin:"50% 100%",duration:.7,yoyo:true,repeat:{reps},ease:"sine.inOut"}},{s0+0.8:.3f});')
# typing caret while waiting for the spoken command
ent("#s06-caret", "{opacity:0}", "{opacity:1,duration:.25,yoyo:true,repeat:6,ease:'steps(1)'}", SC[5][1] + 0.7)
a(f'tl.set("#s06-caret",{{opacity:0}},{P1_T[0]-0.05:.3f});')
ent("#s09-caret", "{opacity:0}", "{opacity:1,duration:.25,yoyo:true,repeat:7,ease:'steps(1)'}", SC[8][1] + 0.8)
a(f'tl.set("#s09-caret",{{opacity:0}},{P2_T[0]-0.05:.3f});')
# S03: cards lift in sequence on "kebutuhan campaign"
for i in range(3):
    a(f'tl.to("#s03-k{i}",{{y:-18,duration:.3,yoyo:true,repeat:1,ease:"power2.out"}},{t(35)+i*0.12:.3f});')

# captions: in = opacity + 12px x-shift; out = the clip window (hard kill)
for c in caps:
    ent(f'#{c["id"]}-p', "{opacity:0,x:12}", "{opacity:1,x:0,duration:.12,ease:'power2.out'}", c["start"])

# wipe strips need clip elements
strips = ""
for k in range(1, len(SC)):
    sid, b, kind, tr = SC[k]
    if kind == "wipe":
        strips += f'<div id="{sid}-strip" class="clip wstrip" data-start="{b}" data-duration="{tr}" data-track-index="9" style="z-index:{11 + k}"></div>\n'

html = open("tools/template.html").read()
html = (html.replace("%%SCENES%%", scene_html).replace("%%STRIPS%%", strips)
        .replace("%%CAPTIONS%%", cap_html).replace("%%JS%%", "\n".join(JS)).replace("%%DUR%%", str(DUR)))
open("index.html", "w").write(html)
json.dump([{k: c[k] for k in ("id", "start", "dur", "html")} for c in caps], open("caption_groups.json", "w"), ensure_ascii=False, indent=0)
print("scenes", len(SC), "captions", len(caps), "tweens", len(JS))
