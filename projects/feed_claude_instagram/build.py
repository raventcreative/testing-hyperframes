# Build feed.html (5 slides, white theme, feed-carousel format) -> render with render.cjs
import re, pathlib
D = pathlib.Path(__file__).parent
TOTAL = 8

def ic(name, size=28, cls=""):
    s = (D / "assets/icons" / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    s = re.sub(r"<svg[^>]*>", lambda m: re.sub(r'\s(width|height|class)="[^"]*"', "", m.group(0)), s, count=1)
    s = re.sub(r"<title>.*?</title>", "", s)
    fill = ' fill="currentColor"' if name.startswith("si-") else ""
    return s.replace("<svg", f'<svg class="ic {cls}" width="{size}" height="{size}"{fill}', 1)

def frame(n, body):
    dots = "".join(f'<i class="{"on" if k == n else ("done" if k < n else "")}"></i>' for k in range(1, TOTAL + 1))
    return f'''<section class="slide" id="s{n}">
<img class="logo" src="../../brand/feed/logo-dark.png">
<div class="count">{n:02d} / {TOTAL:02d}</div>
<div class="content">{body}</div>
<div class="dots">{dots}</div>
<div class="next">{ic("arrow-right", 30)}</div>
</section>'''

note = lambda icon, t: f'<div class="note">{ic(icon, 26)}<span>{t}</span></div>'

s1 = frame(1, f'''
<div class="eyebrow">CLAUDE + INSTAGRAM</div>
<h1>Urus <u>Instagram</u> Cukup<br>dari Satu Chat Claude</h1>
<p class="lead">Cari ide, tulis caption, sampai posting, semua dari satu tempat. Nggak perlu bolak-balik buka belasan tab.</p>
<div class="card chat">
  <div class="bub me">Bikinin 5 ide reels buat minggu depan dong.</div>
  <div class="bub ai">Siap. Ini 5 ide lengkap dengan hook dan caption. Mau sekalian dijadwalin?</div>
  <div class="bub me">Boleh, posting yang pertama besok jam 9 pagi.</div>
</div>
<div class="chips"><span>Cari ide</span><span>Caption</span><span>Script reels</span><span>Posting</span></div>
{note("info", "Cukup setup sekali, cuma 6 langkah. Geser buat mulai.")}''')

def opt(icon, t, d):
    return f'<div class="card opt"><div class="disc big">{ic(icon, 44)}</div><h3>{t}</h3><p>{d}</p></div>'
s2 = frame(2, f'''
<div class="eyebrow">LANGKAH 1</div>
<h1>Buka <u>Claude</u>, Kita Mulai</h1>
<p class="lead">Bisa lewat aplikasi desktop atau langsung buka claude.ai di browser. Dua-duanya bisa buat setup ini.</p>
<div class="grid2">{opt("monitor", "Aplikasi desktop", "Download, lalu login.")}{opt("globe", "Lewat browser", "Buka claude.ai, lalu login.")}</div>
{note("circle-check", "Kalau kolom chat udah muncul, berarti kamu siap.")}''')

s3 = frame(3, f'''
<div class="eyebrow">LANGKAH 2</div>
<h1>Pasang <u>Ootto</u>, Jembatan<br>ke Instagram-mu</h1>
<div class="crumbs"><span>Customize</span><b>›</b><span>Connectors</span><b>›</b><span>Add custom connector</span></div>
<div class="card form">
  <label>NAME</label><div class="field">Ootto</div>
  <label>REMOTE MCP SERVER URL</label><div class="field act">https://mcp.ootto.ai/mcp {ic("copy", 30)}</div>
  <div class="btnrow"><span class="btn">Add</span></div>
</div>
{note("info", "Tempel URL-nya persis seperti di atas, lalu klik Add.")}''')

def step(icon, t, d):
    return f'<div class="st"><div class="disc">{ic(icon, 30)}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
def node(icon, t):
    return f'<div class="node"><div class="ring">{ic(icon, 34)}</div><span>{t}</span></div>'
s4 = frame(4, f'''
<div class="eyebrow">LANGKAH 3</div>
<h1>Tinggal Sambungin<br>Akun <u>Instagram</u>-mu</h1>
<div class="steps">{step("log-in", "Login ke Ootto", "Pakai akun Ootto kamu.")}{step("si-instagram", "Pilih Instagram", "Ada di daftar platform.")}{step("shield-check", "Kasih izin akses", "Tap Allow pas Instagram minta izin.")}</div>
<div class="card flow">
  <div class="nodes">{node("si-claude", "Claude")}<i></i>{node("plug", "Ootto")}<i></i>{node("si-instagram", "Instagram")}</div>
  <div class="ok">{ic("circle-check", 28)}<b>Terhubung · @akunkamu</b></div>
</div>''')

def idea(n, t, tag):
    return f'<div class="card idea"><span class="num">{n}</span><span class="t">{t}</span><span class="tag">{tag}</span></div>'
s5 = frame(5, f'''
<div class="eyebrow">LANGKAH 4</div>
<h1>Intip Topik yang Lagi<br><u>Naik</u> di Niche-mu</h1>
<div class="card prompt"><label>PROMPT KAMU</label><p>Analisis Instagram dan niche aku. Tunjukin topik, hook, dan format yang lagi paling perform sekarang, terus kasih 20 ide reels buat aku.</p></div>
<div class="eyebrow sm">YANG DIKERJAIN CLAUDE</div>
<ul class="checks"><li>{ic("check", 22)}Bandingin 30 reels terbaik &amp; terburukmu</li><li>{ic("check", 22)}Nemuin hook dan format yang konsisten menang</li><li>{ic("check", 22)}Ngurutin 20 ide reels khusus buat kamu</li></ul>
{idea(1, "Tes hook kamu dalam 3 detik", "Lagi naik")}{idea(2, "Reels yang sama, sebelum &amp; sesudah", "Paling disimpan")}{idea(3, "5 kebiasaan yang bikin reach anjlok", "Paling dibagikan")}''')


DAYS = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
def checks(items):
    return '<ul class="checks">' + "".join(f'<li>{ic("check", 22)}{t}</li>' for t in items) + "</ul>"

reels = "".join(f'<div class="reel"><span>{d}</span><div class="play">{ic("play", 26)}</div><i></i><i class="s"></i></div>' for d in DAYS)
s6 = frame(6, f'''
<div class="eyebrow">LANGKAH 5</div>
<h1>Sulap Ide Terbaik<br>Jadi <u>7 Reels</u> Sekaligus</h1>
<div class="card prompt"><label>PROMPT KAMU</label><p>Ubah ide teratas tadi jadi 7 reels pakai gaya brand aku.</p></div>
<div class="eyebrow sm">YANG DIKERJAIN CLAUDE</div>
{checks(["Nulis script dan hook buat tiap reels", "Nambahin voiceover dan subtitle di ketujuhnya"])}
<div class="reels">{reels}</div>''')

def day(d, done):
    return f'<div class="day"><span>{d}</span><div class="dot {"done" if done else ""}">{ic("check" if done else "clock", 34)}</div><small>09.00</small></div>'
s7 = frame(7, f'''
<div class="eyebrow">LANGKAH 6</div>
<h1>Posting Terjadwal,<br>Komen Dibalas <u>Otomatis</u></h1>
<div class="card prompt"><label>PROMPT KAMU</label><p>Posting satu reels tiap hari jam 9 pagi. Kalau ada yang komen PANDUAN, balas komennya dan kirim link aku lewat DM.</p></div>
<div class="eyebrow sm">YANG DIKERJAIN CLAUDE</div>
{checks(["7 reels masuk antrean, satu per hari jam 09.00", "Auto-reply aktif buat keyword PANDUAN", "Link dikirim lewat DM, bukan di kolom komentar"])}
<div class="card week"><div class="days">{"".join(day(d, k < 2) for k, d in enumerate(DAYS))}</div>
<div class="legend"><span><b class="f"></b>Sudah tayang</span><span><b></b>Terjadwal</span></div></div>''')

css = (D / "style.css").read_text()
(D / "feed.html").write_text(f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body>{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>''')
print("ok")
