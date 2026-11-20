# 8 Workflow AI carousel (ID), feed-carousel white format -> node render.cjs
import re, pathlib
D = pathlib.Path(__file__).parent
TOTAL = 6

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

def flow(items, dark=()):
    w = 150 if len(items) > 4 else 190
    parts = [f'<div class="node" style="width:{w}px"><div class="ring{" dark" if k in dark else ""}">{ic(i, 32)}</div><span>{t}</span></div>'
             for k, (i, t) in enumerate(items)]
    return '<div class="flow">' + "<i></i>".join(parts) + "</div>"

def foot(label=None, pills=(), loop=None):
    h = f'<label>{label}</label>' if label else ""
    h += f'<span class="loop">{ic("repeat", 22)}{loop}</span>' if loop else ""
    h += "".join(f'<span class="pill">{p}</span>' for p in pills)
    return f'<div class="foot">{h}</div>'

def sec(tag, title, desc, card):
    return f'<span class="tag">{tag}</span><h2>{title}</h2><p class="desc">{desc}</p><div class="card">{card}</div>'

SEP = '<div class="sep"></div>'

# ---- slide 1: map (snake order = slide order)
X = [60, 295, 530, 765]
top = [("phone", "Resepsionis AI"), ("users", "Cari leads"), ("megaphone", "Bedah iklan"), ("video", "Faceless")]
bot = [("user", "Avatar AI"), ("lightbulb", "Ide YouTube"), ("languages", "CS bot"), ("workflow", "Agent konten")]
m = ""
for row, (y, items) in enumerate([(0, top), (270, bot)]):
    for k, (i, t) in enumerate(items):
        m += f'<div class="n" style="left:{X[k]}px;top:{y}px"><div class="disc">{ic(i, 36)}</div>{t}</div>'
    for k in range(3):
        m += f'<div class="ln" style="left:{X[k]+52}px;width:{X[k+1]-X[k]-104}px;top:{y+47}px"></div>'
m += f'<div class="vl" style="left:{X[3]-1}px;top:150px;height:116px"></div>'
s1 = frame(1, f'''<span class="tag">AI + AUTOMATION</span>
<h1>8 Workflow AI yang<br><u>Wajib</u> Dicoba Pebisnis</h1>
<p class="lead">Otomasi nyata buat sales, konten, dan customer service. Geser buat lihat cara kerjanya satu per satu.</p>
<div class="map">{m}</div>''')

# ---- slide 2
chev = f'<b>{ic("chevron-right", 26)}</b>'
acts = "".join(f'<span>{a}</span>{chev}<span>{b}</span>' for a, b in
               [("Cek jadwal kosong", "Booking slot"), ("Jawab pertanyaan", "Email konfirmasi"), ("Oper ke tim", "Simpan ke CRM")])
recep = f'''<div class="recep"><div class="who">
<div class="node"><div class="ring">{ic("phone", 32)}</div><span>Telepon masuk</span></div>
<div class="node"><div class="ring dark">{ic("bot", 32)}</div><span>AI jawab</span></div></div>
<div class="acts">{acts}</div></div>'''
s2 = frame(2, sec("TELEPON PELANGGAN", "Resepsionis AI <u>Anti Libur</u>",
                  "Angkat telepon 24 jam, bisa handle 10 panggilan sekaligus, dan nggak bikin pelanggan nunggu.", recep)
           + SEP + sec("SALES", "Mesin Cari Leads <u>Otomatis</u>",
                  "Cari calon pembeli, riset satu per satu, saring yang nggak cocok, lalu kirim email pertama sampai follow-up.",
                  flow([("search", "Cari leads"), ("brain", "Riset"), ("filter", "Saring"), ("mail", "Kirim email"), ("clock", "Follow-up")])
                  + foot(loop="Berulang tiap ada lead baru")))

# ---- slide 3
def col(icon, t, items):
    return f'<div><h4>{ic(icon, 28)}{t}</h4><ul>' + "".join(f'<li>{ic("check", 20)}{x}</li>' for x in items) + "</ul></div>"
s3 = frame(3, sec("IKLAN", "Bongkar Resep <u>Iklan Laris</u>",
                  "Masukin iklan yang lagi perform, pahami kenapa bisa laku, terus dapat 5 prompt video yang disesuaikan sama brand kamu.",
                  flow([("link", "Tempel iklan"), ("search", "Analisis"), ("target", "Temukan hook"), ("file-pen-line", "Tulis 5 prompt"), ("clapperboard", "Siap jadi UGC")])
                  + foot("BISA BUAT", ["TikTok", "Instagram", "YouTube"]))
           + SEP + sec("VIDEO", "Channel <u>Faceless</u> Autopilot",
                  "Jalanin channel video pendek tanpa kamu harus tampil: dia yang nulis, bikin, sampai posting.",
                  '<div class="cols">' + col("file-pen-line", "Tulis", ["Topik trending", "Draft script", "Prompt kamu"])
                  + col("video", "Bikin", ["Voiceover", "Stock footage", "Visual animasi"])
                  + col("send", "Posting", ["Auto-posting", "Banyak platform", "Pantau hasil"]) + "</div>"))

# ---- slide 4
s4 = frame(4, sec("KONTEN", "Satu Agent, <u>Semua Urusan</u> Konten",
                  "Dari ide pertama sampai posting, lalu ngulang lagi sendiri.",
                  flow([("search", "Riset topik"), ("file-pen-line", "Tulis script"), ("video", "Bikin video"), ("captions", "Subtitle"), ("send", "Posting")])
                  + foot(pills=["TikTok", "Instagram", "YouTube", "X"], loop="Berulang otomatis"))
           + SEP + sec("CUSTOMER SERVICE", "CS Bot yang Fasih <u>Banyak Bahasa</u>",
                  "Jawab pelanggan detik itu juga, dalam bahasa mereka sendiri.",
                  flow([("message-square-text", "Pelanggan tanya"), ("languages", "Deteksi bahasa"), ("bot", "AI jawab"), ("send", "Kirim balasan")])
                  + foot("BALAS DALAM", ["Indonesia", "Inggris", "Mandarin", "Arab", "+20 lainnya"])))

# ---- slide 5
s5 = frame(5, sec("RISET", "Mesin Ide <u>YouTube</u> Berbasis Data",
                  "Bedah video teratas di niche kamu, jadi ide segar berbasis data.",
                  flow([("trending-up", "Ambil video top"), ("chart-column", "Analisis"), ("lightbulb", "Bikin ide"), ("list-checks", "Siap syuting")])
                  + foot("KAMU DAPAT", ["Topik trending", "Keyword pencarian", "Angle terbukti"]))
           + SEP + sec("VIDEO", "Video Presenter <u>Tanpa Kamera</u>",
                  "Script jadi video presenter pakai avatar + suara AI. Tanpa kamera.",
                  flow([("file-pen-line", "Tulis script"), ("user", "Bikin avatar"), ("mic", "Tambah suara"), ("upload", "Export video")])
                  + foot("COCOK BUAT", ["Avatar realistis", "Banyak bahasa", "Tanpa ribet"])))

css = (D / "style.css").read_text()
(D / "feed.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{s1}{s2}{s3}{s4}{s5}</body></html>')
print("ok")
