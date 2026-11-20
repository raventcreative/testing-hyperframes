# AIpreneur carousel "1 konten -> 8 platform" (ATM remake), white theme, feed-carousel format.
# Every slide animates via window.setT(t) (pure function of time); render.cjs captures frames -> MP4.
import re, itertools, pathlib
D = pathlib.Path(__file__).parent
TOTAL = 6

def ic(name, size=28):
    s = (D / "assets/icons" / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    s = re.sub(r"<svg[^>]*>", lambda m: re.sub(r'\s(width|height|class)="[^"]*"', "", m.group(0)), s, count=1)
    return s.replace("<svg", f'<svg class="ic" width="{size}" height="{size}"', 1)

def glyph(name, size, color, extra=""):
    p = re.search(r'<path d="([^"]+)"', (D / "assets/logos" / f"{name}.svg").read_text()).group(1)
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" style="{extra}"><path fill="{color}" d="{p}"/></svg>'

PL = {"ig": ("Instagram", "instagram"), "yt": ("YouTube", "youtube"), "tt": ("TikTok", "tiktok"), "li": ("LinkedIn", "linkedin"),
      "fb": ("Facebook", "facebook"), "x": ("X", "x"), "th": ("Threads", "threads"), "pi": ("Pinterest", "pinterest")}
def logo(k, s=64):
    """Official glyph + official colour on the platform's own app tile (Simple Icons, CC0)."""
    g = int(s * .58); tile = f'width:{s}px;height:{s}px;border-radius:{int(s * .24)}px'
    if k == "ig":
        return f'<div class="app" style="{tile};background:radial-gradient(circle at 30% 107%,#fdf497 0%,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285AEB 90%)">{glyph("instagram", g, "#fff")}</div>'
    if k == "tt":
        a = max(1, s // 32)
        return (f'<div class="app" style="{tile};background:#000"><div style="position:relative;width:{g}px;height:{g}px">'
                f'{glyph("tiktok", g, "#25F4EE", f"position:absolute;left:{-a}px;top:{-a}px")}'
                f'{glyph("tiktok", g, "#FE2C55", f"position:absolute;left:{a}px;top:{a}px")}'
                f'{glyph("tiktok", g, "#fff", "position:absolute;left:0;top:0")}</div></div>')
    if k in ("x", "th"):
        return f'<div class="app" style="{tile};background:#000">{glyph(PL[k][1], int(g * .9), "#fff")}</div>'
    if k == "li":
        return f'<div class="app" style="{tile};background:#fff">{glyph("linkedin", int(s * .86), "#0A66C2")}</div>'
    col = {"yt": "#FF0000", "fb": "#0866FF", "pi": "#E60023"}[k]
    return f'<div class="app" style="{tile};background:#fff">{glyph(PL[k][1], int(s * .7), col)}</div>'

def frame(n, body):
    dots = "".join(f'<i class="{"on" if k == n else ("done" if k < n else "")}"></i>' for k in range(1, TOTAL + 1))
    return f'''<section class="slide" id="s{n}"><img class="logo" src="../../brand/feed/logo-dark.png">
<div class="count">{n:02d} / {TOTAL:02d}</div><div class="content">{body}</div>
<div class="dots">{dots}</div><div class="next">{ic("arrow-right", 30)}</div></section>'''

def vid(clip, style=""):
    return f'<div class="vid" style="{style}"><img class="clipf" data-clip="{clip}" src="assets/{clip}/f_180.jpg"></div>'

RATIO = {"ig": "9:16", "yt": "16:9", "tt": "9:16", "li": "1:1", "fb": "4:5", "x": "16:9", "th": "4:5", "pi": "2:3"}

# ================= slide 1: hub-and-spoke (layout like the reference)
W, H, HX, HY = 880, 660, 440, 384
LEFT, RIGHT, YS = ["ig", "yt", "li", "tt"], ["th", "x", "pi", "fb"], [258, 374, 490, 606]
SEQ = ["ig", "th", "yt", "x", "li", "pi", "tt", "fb"]           # activation order
paths, chips, apps = [], [], []
for side, keys in ((-1, LEFT), (1, RIGHT)):
    for k, y in zip(keys, YS):
        ax = 50 if side < 0 else W - 50
        p0 = (HX + side * 64, HY + (y - HY) * .22); p3 = (ax - side * 52, y)
        c1 = (p0[0] + side * 130, p0[1]); c2 = (p3[0] - side * 130, p3[1])
        d = f"M{p0[0]:.0f},{p0[1]:.0f} C{c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {p3[0]:.0f},{p3[1]:.0f}"
        i = SEQ.index(k)
        paths.append(f'<path class="sp" data-i="{i}" d="{d}"/>')
        u = .52
        bx = (1-u)**3*p0[0] + 3*(1-u)**2*u*c1[0] + 3*(1-u)*u*u*c2[0] + u**3*p3[0]
        by = (1-u)**3*p0[1] + 3*(1-u)**2*u*c1[1] + 3*(1-u)*u*u*c2[1] + u**3*p3[1]
        chips.append(f'<span class="rchip" style="left:{bx:.0f}px;top:{by:.0f}px">{RATIO[k]}</span>')
        apps.append(f'<div class="papp" data-i="{i}" style="left:{ax - 40}px;top:{y - 40}px">{logo(k, 80)}'
                    f'<span class="lv">{ic("check", 16)}</span><b>{PL[k][0].upper()}</b></div>')
s1 = frame(1, f'''<span class="tag">1 KONTEN · 8 PLATFORM</span>
<h1 style="font-size:66px">Sekali Upload,<br><u>Tayang di Mana-mana.</u></h1>
<div class="viz" style="width:{W}px;height:{H}px">
<svg class="spokes" width="{W}" height="{H}"><path class="trunk1" d="M{HX},228 L{HX},{HY - 62}"/>{"".join(paths)}{"".join(f'<circle class="pdot" data-i="{i}" r="7"/>' for i in range(8))}</svg>
{"".join(chips)}
<div class="post">{vid("clip", "width:118px;height:168px")}<div class="pdots"><i></i><i class="on"></i><i></i><i></i></div><b>1 KONTEN</b></div>
<div class="apil"><span>AUTOPILOT · ON</span><em><i></i><b id="live">0</b>/8 PLATFORM LIVE</em></div>
<div class="hub"><img src="assets/a_mark.png"></div>
{"".join(apps)}
<p class="tagline">Tiap aplikasi dapat <em>format</em>,<br><em>caption</em>, dan <em>jam tayang</em> sendiri.</p>
</div>''')

# ================= slide 2: 2x4 cards with their own video, cursor flips toggles (layout like the reference)
FIT = {"9:16": (56, 100), "16:9": (92, 52), "1:1": (80, 80), "4:5": (72, 90), "2:3": (66, 100)}
CARDS = [("ig", "REELS", "Direkam sekali, tayang di 8 tempat sekaligus.", "18.30"),
         ("yt", "VIDEO", "Judul: Sekali rekam, semua aplikasi + deskripsi &amp; tag", "19.00"),
         ("tt", "VIDEO", "satu take, 8 aplikasi <span class='ht'>#kontenkreator #fyp</span>", "20.00"),
         ("li", "POST", "Dulu upload video yang sama 8 kali. Sekarang nggak lagi.", "09.00"),
         ("fb", "REELS", "Konten sama, tiap feed beda. Begini caranya.", "12.30"),
         ("x", "POST", "rekam sekali.<br>posting di mana-mana.", "10.00"),
         ("th", "POST", "satu video, semua aplikasi. tanya aja caranya", "18.00"),
         ("pi", "PIN", "Posting ke semua platform: panduan kreator", "21.00")]
cards = ""
for i, (k, f, c, t) in enumerate(CARDS):
    w, h = FIT[RATIO[k]]
    cards += f'''<div class="pc" data-i="{i}"><div class="pth">{vid(f"clips/c{i + 1}", f"width:{w}px;height:{h}px")}<span>{RATIO[k]}</span></div>
<div class="pbody"><div class="phd">{logo(k, 36)}<div class="pn"><b>{PL[k][0]}</b><small>{f} · {RATIO[k]}</small></div><div class="tg"><i></i></div></div>
<p>{c}</p><span class="autot">AUTO · {t}</span></div></div>'''
s2 = frame(2, f'''<span class="tag">AUTO-FORMAT</span>
<h1 style="font-size:66px">Tiap Aplikasi,<br><u>Postingannya Sendiri.</u></h1>
<div class="pgrid">{cards}</div>
<p class="tagline2">Sekali rekam. <em>8 postingan, masing-masing pas buat aplikasinya.</em></p>
<div class="cursor" id="cur">{ic("mouse-pointer-2", 44)}</div>''')

# ================= slide 3: connect once
ORDER = ["ig", "yt", "tt", "li", "fb", "x", "th", "pi"]
cells = "".join(f'<div class="conn" data-i="{i}">{logo(k, 72)}<b>{PL[k][0]}</b><span class="cs"><em class="w">Menghubungkan…</em><em class="dn">{ic("circle-check", 20)}Terhubung</em></span></div>' for i, k in enumerate(ORDER))
mini = "".join(f'<div class="mini">{logo(k, 40)}<div class="tg" data-i="{i}"><i></i></div></div>' for i, k in enumerate(ORDER))
s3 = frame(3, f'''<span class="tag">SETUP SEKALI</span>
<h1 style="font-size:66px">Hubungkan Sekali,<br><u>Biar Jalan Sendiri</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Tiap platform jalan dengan pengaturannya masing-masing.</p>
<div class="conns">{cells}</div>
<div class="card auto"><label>AUTOPILOT PER PLATFORM</label><div class="minis">{mini}</div>
<p>Mau jeda satu platform? Matikan toggle-nya, yang lain tetap jalan.</p></div>''')

# ================= slide 4: December 2026 calendar fills up (1 Dec = Tuesday)
cyc = itertools.cycle(ORDER)
days, nchip = ['<div class="d blank"></div>'], 0
for d in range(1, 32):
    ks = [next(cyc)] + ([next(cyc)] if d % 3 == 0 else [])
    chs = ""
    for k in ks:
        chs += f'<span class="cc" data-i="{nchip}">{logo(k, 26)}</span>'; nchip += 1
    days.append(f'<div class="d"><span>{d}</span><div class="ch">{chs}</div></div>')
days += ['<div class="d blank"></div>'] * (35 - len(days))
s4 = frame(4, f'''<span class="tag">KALENDER KONTEN</span>
<h1 style="font-size:66px">Sebulan Penuh,<br><u>Udah Terjadwal</u></h1>
<div class="card cal"><div class="ch1"><b>Desember 2026</b><span class="pillon">{ic("circle-check", 20)}Autopilot aktif</span></div>
<div class="wk">{"".join(f"<span>{w}</span>" for w in ["Sen","Sel","Rab","Kam","Jum","Sab","Min"])}</div>
<div class="grid">{"".join(days)}</div></div>
<div class="stats"><div><b id="queued" data-n="{nchip}">{nchip}</b><span>konten terjadwal</span></div><div><b>8</b><span>platform</span></div><div><b>0</b><span>upload manual</span></div></div>''')

# ================= slide 5: daily timeline, "now" marker sweeps the day
SCHED = [("06.30", "ig"), ("07.00", "yt"), ("08.00", "tt"), ("09.00", "li"), ("10.00", "x"), ("12.30", "fb"), ("18.00", "th"), ("21.00", "pi")]
tl = "".join(f'''<div class="ev" data-h="{int(t[:2]) + int(t[3:]) / 60}"><time>{t}</time><i></i>{logo(k, 44)}<b>{PL[k][0]}</b>
<span class="es"><em class="q">{ic("clock", 18)}Terjadwal</em><em class="ok">{ic("check", 18)}Tayang</em></span></div>''' for t, k in SCHED)
s5 = frame(5, f'''<span class="tag">JADWAL HARIAN</span>
<h1 style="font-size:66px">Atur Jamnya Sekali,<br><u>Sisanya Autopilot</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Tiap platform tayang di jam terbaiknya, tiap hari.</p>
<div class="card tl">{tl}<div class="now" id="now"><span id="nowt">Sekarang · 06.00</span></div></div>''')

css = (D / "base.css").read_text() + (D / "style.css").read_text()
js = (D / "anim.js").read_text()
(D / "index.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{s1}{s2}{s3}{s4}{s5}<script>{js}</script></body></html>')
print("ok")
