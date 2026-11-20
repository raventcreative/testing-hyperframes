# Automation AI buat pemula (RTO) carousel (ID), feed-carousel white format -> node render.cjs
import re, pathlib
D = pathlib.Path(__file__).parent
TOTAL = 5

def ic(name, size=28):
    s = (D / "assets/icons" / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    s = re.sub(r"<svg[^>]*>", lambda m: re.sub(r'\s(width|height|class)="[^"]*"', "", m.group(0)), s, count=1)
    return s.replace("<svg", f'<svg class="ic" width="{size}" height="{size}"', 1)

def frame(n, body):
    dots = "".join(f'<i class="{"on" if k == n else ("done" if k < n else "")}"></i>' for k in range(1, TOTAL + 1))
    return f'''<section class="slide" id="s{n}"><img class="logo" src="../../brand/feed/logo-dark.png">
<div class="count">{n:02d} / {TOTAL:02d}</div><div class="content">{body}</div>
<div class="dots">{dots}</div><div class="next">{ic("arrow-right", 30)}</div></section>'''

note = lambda t: f'<div class="note">{ic("sparkles", 28)}<span>{t}</span></div>'

nodes = "<i></i>".join(f'<div class="node"><div class="ring">{ic(i, 36)}</div><span>{t}</span></div>'
                       for i, t in [("clipboard-list", "Tentukan RTO"), ("message-square-text", "Tulis prompt"), ("zap", "Jalankan di tool")])
s1 = frame(1, f'''<span class="tag">AUTOMATION AI BUAT PEMULA</span>
<h1>Bikin <u>Automation AI</u><br>Pertamamu, Tanpa<br>Ngoding Sedikit Pun</h1>
<p class="lead">Cuma 3 langkah simpel. Nggak perlu background teknis.</p>
<div class="card flow3"><div class="flow">{nodes}</div></div>''')

def rto(l, t, d, ex):
    return f'''<div class="card rto"><div class="letter">{l}</div><div><h3>{t}</h3><p>{d}</p>
<div class="ex">{ic("lightbulb", 22)}<small>CONTOH</small><span>{ex}</span></div></div></div>'''
s2 = frame(2, f'''<span class="tag">LANGKAH 1</span>
<h1 style="font-size:66px">Petakan Kerjaanmu<br>Pakai Rumus <u>RTO</u></h1>
<p class="lead" style="margin-top:12px">Sebelum buka tool apa pun, tulis dulu 3 hal ini.</p>
{rto("R", "Rutinitas", "Kerjaan yang kamu ulang terus-terusan.", "Update berita AI tiap hari")}
{rto("T", "Tools &amp; langkah", "Apa aja yang dipakai dan dikerjain di prosesnya.", "Cek Google, Reddit, X, dan newsletter")}
{rto("O", "Output", "Hasil akhir yang kamu mau.", "Satu rangkuman update buat ide konten")}
{note("Makin jelas RTO-mu, makin jago automation-nya.")}''')

s3 = frame(3, f'''<span class="tag">LANGKAH 2</span>
<h1 style="font-size:66px">Racik RTO-mu Jadi<br><u>Satu Prompt</u></h1>
<p class="lead" style="margin-top:12px">Gabungin ketiganya dalam satu pesan, dan spesifik soal apa yang kamu mau.</p>
<div class="card pbox">Buatin automation yang bikin aku selalu update soal berita AI.
<mark><b>R</b>Tiap pagi, cari berita AI terbaru, peluncuran produk, paper riset, dan pendanaan</mark>
<mark><b>T</b>dari Google News, Reddit, blog perusahaan, dan newsletter.</mark> Skip yang berulang atau kurang penting.
<mark><b>O</b>Rangkum tiap item jadi poin-poin, lalu masukin ke Google Sheet "Daily AI News" dengan kolom Tanggal, Ringkasan, dan Link Sumber.</mark></div>
{note("Bingung nyusunnya? Minta ChatGPT atau Claude bikinin draft.")}''')

def tool(icon, t, d):
    return f'<div class="card tool"><div class="disc">{ic(icon, 30)}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
checks = "".join(f'<li>{ic("check", 22)}<span>{x}</span></li>' for x in
                 ["Cari dari sumber berita kamu", "Saring yang kurang penting", "Tulis ringkasan poin singkat", "Simpan hasilnya ke Google Sheet"])
s4 = frame(4, f'''<span class="tag">LANGKAH 3</span>
<h1 style="font-size:66px">Tinggal Tempel,<br><u>Biar AI yang Jalan</u></h1>
<p class="lead" style="margin-top:12px;font-size:29px">Claude Routines dan Codex Automations paling gampang buat mulai. Nggak perlu n8n, Make, atau Zapier.</p>
<div class="tools">{tool("repeat", "Claude Routines", "Jalan sesuai jadwal")}{tool("terminal", "Codex Automations", "Setup langsung dari chat")}</div>
<div class="down">{ic("arrow-down", 28)}</div>
<div class="card res"><div class="hd">{ic("circle-check", 34)}Automation berhasil dibuat<span class="act">Aktif</span></div>
<h2>Daily AI Morning Brief</h2><div class="when">{ic("clock", 22)}Jalan tiap hari jam 08.00</div><ul>{checks}</ul></div>
<div class="call">{ic("plug", 34)}<div><h3>Tool-nya butuh akses?</h3><p>Buka menu Plugins, lalu sambungkan yang diminta.</p></div></div>''')

css = (D / "style.css").read_text()
(D / "feed.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{s1}{s2}{s3}{s4}</body></html>')
print("ok")
