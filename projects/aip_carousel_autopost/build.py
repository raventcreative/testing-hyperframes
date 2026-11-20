# AIpreneur carousel "1 konten -> 8 platform" (ATM remake), white theme, feed-carousel format.
# Slides 1-2 animate via window.setT(t) (pure function of time); render.cjs captures frames -> MP4.
import re, pathlib
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

# Real app-icon look: official glyph + official colour on the platform's own tile
PL = {
 "ig": ("Instagram", "instagram"), "yt": ("YouTube", "youtube"), "tt": ("TikTok", "tiktok"), "li": ("LinkedIn", "linkedin"),
 "fb": ("Facebook", "facebook"), "x": ("X", "x"), "th": ("Threads", "threads"), "pi": ("Pinterest", "pinterest")}
def logo(k, s=64):
    g = int(s * .58); r = int(s * .24)
    tile = f'width:{s}px;height:{s}px;border-radius:{r}px'
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

def frame(n, body, cls=""):
    dots = "".join(f'<i class="{"on" if k == n else ("done" if k < n else "")}"></i>' for k in range(1, TOTAL + 1))
    return f'''<section class="slide {cls}" id="s{n}"><img class="logo" src="../../brand/feed/logo-dark.png">
<div class="count">{n:02d} / {TOTAL:02d}</div><div class="content">{body}</div>
<div class="dots">{dots}</div><div class="next">{ic("arrow-right", 30)}</div></section>'''

ORDER = ["ig", "yt", "tt", "li", "fb", "x", "th", "pi"]
RATIO = {"ig": "9:16", "yt": "16:9", "tt": "9:16", "li": "1:1", "fb": "4:5", "x": "16:9", "th": "4:5", "pi": "2:3"}

# ---------- slide 1 (video): one file -> distributor with 8 tiles
tiles = "".join(f'''<div class="tile" data-i="{i}">{logo(k, 70)}<b>{PL[k][0]}</b><span class="ratio">{RATIO[k]}</span>
<span class="st"><em class="wait">Menunggu</em><em class="ok">{ic("check", 18)}Tayang</em></span></div>''' for i, k in enumerate(ORDER))
s1 = frame(1, f'''<span class="tag">1 KONTEN · 8 PLATFORM</span>
<h1 style="font-size:66px">Sekali Upload,<br><u>Tayang di 8 Platform</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Tiap aplikasi dapat format, caption, dan jamnya sendiri.</p>
<div class="src" id="src"><div class="vid"><img class="clipf" src="assets/clip/f_180.jpg"><span>0:32</span></div><div><b>konten_final.mp4</b><span>1 file · 0:32</span></div>
<div class="cnt"><b id="cnt">0</b>/8 tayang</div></div>
<div class="trunk"><i id="trunk"></i><s id="pulse"></s></div>
<div class="dist card"><div class="tiles">{tiles}</div></div>''', "s1")

# ---------- slide 2 (video): per-platform table, cursor flips toggles
FR = {r: (lambda w, h: f"width:{round(64 * w / h) if w < h else 112}px;height:{64 if w <= h else round(112 * h / w)}px")(*map(int, r.split(":"))) for r in ["9:16", "16:9", "1:1", "4:5", "2:3"]}
ROWS = [("ig", "Reels · 9:16", "Direkam sekali, tayang di 8 tempat.", "18.30"),
        ("yt", "Video · 16:9", "Judul, deskripsi, dan tag dibikinin.", "19.00"),
        ("tt", "Video · 9:16", "satu take, 8 aplikasi #fyp", "20.00"),
        ("li", "Post · 1:1", "Dulu upload 8 kali. Sekarang sekali.", "09.00"),
        ("fb", "Reels · 4:5", "Konten sama, feed beda. Ini caranya.", "12.30"),
        ("x", "Post · 16:9", "rekam sekali. tayang di mana-mana.", "10.00"),
        ("th", "Post · 4:5", "1 video, 8 aplikasi. tanya caranya", "18.00"),
        ("pi", "Pin · 2:3", "Panduan posting ke semua platform", "21.00")]
rows = "".join(f'''<div class="row" data-i="{i}">{logo(k, 44)}<div class="th"><div class="fr" style="{FR[RATIO[k]]}"><img class="clipf" src="assets/clip/f_180.jpg"></div></div><div class="nm"><b>{PL[k][0]}</b><span>{f}</span></div>
<div class="cap">{c}</div><div class="tm">{t}</div><div class="tg"><i></i></div></div>''' for i, (k, f, c, t) in enumerate(ROWS))
s2 = frame(2, f'''<span class="tag">AUTO-FORMAT</span>
<h1 style="font-size:66px">Satu Konten,<br><u>8 Versi Berbeda</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Ukuran, caption, dan jam tayang menyesuaikan tiap aplikasi.</p>
<div class="card table">{rows}</div>
<div class="cursor" id="cur">{ic("mouse-pointer-2", 44)}</div>''', "s2")

# ---------- slide 3 (static): connect once
cells = "".join(f'<div class="conn">{logo(k, 72)}<b>{PL[k][0]}</b><span>{ic("circle-check", 20)}Terhubung</span></div>' for k in ORDER)
mini = "".join(f'<div class="mini">{logo(k, 40)}<div class="tg on"><i></i></div></div>' for k in ORDER)
s3 = frame(3, f'''<span class="tag">SETUP SEKALI</span>
<h1 style="font-size:66px">Hubungkan Sekali,<br><u>Biar Jalan Sendiri</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Tiap platform jalan dengan pengaturannya masing-masing.</p>
<div class="conns">{cells}</div>
<div class="card auto"><label>AUTOPILOT PER PLATFORM</label><div class="minis">{mini}</div>
<p>Mau jeda satu platform? Matikan toggle-nya, yang lain tetap jalan.</p></div>''', "s3")

# ---------- slide 4 (static): December 2026 calendar (1 Dec = Tuesday)
import itertools
cyc = itertools.cycle(ORDER)
days = ['<div class="d blank"></div>']
for d in range(1, 32):
    ks = [next(cyc)] + ([next(cyc)] if d % 3 == 0 else [])
    days.append(f'<div class="d"><span>{d}</span><div class="ch">{"".join(logo(k, 26) for k in ks)}</div></div>')
days += ['<div class="d blank"></div>'] * (35 - len(days))
s4 = frame(4, f'''<span class="tag">KALENDER KONTEN</span>
<h1 style="font-size:66px">Sebulan Penuh,<br><u>Udah Terjadwal</u></h1>
<div class="card cal"><div class="ch1"><b>Desember 2026</b><span class="pillon">{ic("circle-check", 20)}Autopilot aktif</span></div>
<div class="wk">{"".join(f"<span>{w}</span>" for w in ["Sen","Sel","Rab","Kam","Jum","Sab","Min"])}</div>
<div class="grid">{"".join(days)}</div></div>
<div class="stats"><div><b>{31 + 31 // 3}</b><span>konten terjadwal</span></div><div><b>8</b><span>platform</span></div><div><b>0</b><span>upload manual</span></div></div>''', "s4")

# ---------- slide 5 (static): daily timeline
SCHED = [("06.30", "ig", 1), ("07.00", "yt", 1), ("08.00", "tt", 1), ("09.00", "li", 1),
         ("10.00", "x", 0), ("12.30", "fb", 0), ("18.00", "th", 0), ("21.00", "pi", 0)]
tl = ""
for i, (t, k, done) in enumerate(SCHED):
    if i == 4:
        tl += '<div class="now"><span>Sekarang · 09.42</span></div>'
    tl += (f'<div class="ev {"done" if done else ""}"><time>{t}</time><i></i>{logo(k, 44)}<b>{PL[k][0]}</b>'
           f'<span>{ic("check", 18) + "Tayang" if done else ic("clock", 18) + "Terjadwal"}</span></div>')
s5 = frame(5, f'''<span class="tag">JADWAL HARIAN</span>
<h1 style="font-size:66px">Atur Jamnya Sekali,<br><u>Sisanya Autopilot</u></h1>
<p class="lead" style="margin-top:10px;font-size:29px">Tiap platform tayang di jam terbaiknya, tiap hari.</p>
<div class="card tl">{tl}</div>''', "s5")

css = (D / "base.css").read_text() + (D / "style.css").read_text()
js = (D / "anim.js").read_text()
(D / "index.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{s1}{s2}{s3}{s4}{s5}<script>{js}</script></body></html>')
print("ok")
