# AIpreneur carousel "7 AI Agent" (ATM remake of a 9-slide reference, condensed to 6), white theme, feed-carousel format.
# Declarative animation: data-in / data-show / data-type / data-cnt / data-on / data-grow / data-ring / data-draw (see anim.js).
import re, pathlib
D = pathlib.Path(__file__).parent
TOTAL = 6

def ic(name, size=24):
    s = (D / "assets/icons" / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    s = re.sub(r"<svg[^>]*>", lambda m: re.sub(r'\s(width|height|class)="[^"]*"', "", m.group(0)), s, count=1)
    return s.replace("<svg", f'<svg class="ic" width="{size}" height="{size}"', 1)

BRANDC = {"claude": "#D97757", "whatsapp": "#25D366", "instagram": "#E4405F", "gmail": "#EA4335", "googlecalendar": "#4285F4",
          "google": "#4285F4", "googlesheets": "#34A853", "googlemaps": "#4285F4", "facebook": "#0866FF", "meta": "#0467DF"}
MULTI = {"google": "google-icon", "gmail": "google-gmail", "googlecalendar": "google-calendar", "googlemaps": "google-maps",
         "whatsapp": "whatsapp-icon", "claude": "claude-icon", "meta": "meta-icon"}
def glyph(name, size, color=None):
    if name in MULTI and color is None:   # official full-colour logo (gilbarbara/logos, CC0)
        return f'<img class="ml" src="assets/mlogos/{MULTI[name]}.svg" style="height:{size}px;width:auto;max-width:{size}px;object-fit:contain;display:block">'
    p = re.search(r'<path d="([^"]+)"', (D / "assets/logos" / f"{name}.svg").read_text()).group(1)
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" style="display:block"><path fill="{color or BRANDC[name]}" d="{p}"/></svg>'
def ig_grad(size):
    """Simple Icons Instagram glyph filled with the official IG gradient."""
    p = re.search(r'<path d="([^"]+)"', (D / "assets/logos/instagram.svg").read_text()).group(1)
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" style="display:block"><defs><radialGradient id="igg" cx="30%" cy="107%" r="150%">'
            '<stop offset="0" stop-color="#fdf497"/><stop offset=".05" stop-color="#fdf497"/><stop offset=".45" stop-color="#fd5949"/>'
            '<stop offset=".6" stop-color="#d6249f"/><stop offset=".9" stop-color="#285AEB"/></radialGradient></defs>'
            f'<path fill="url(#igg)" d="{p}"/></svg>')
def tile(name, s=56):
    if name == "instagram" and s >= 60:   # cover: same white app tile as the others, official IG mark inside
        return f'<div class="app" style="width:{s}px;height:{s}px;border-radius:{int(s*.26)}px">{ig_grad(int(s*.6))}</div>'
    if name == "instagram":
        return (f'<div class="app" style="width:{s}px;height:{s}px;border-radius:{int(s*.26)}px;background:radial-gradient(circle at 30% 107%,#fdf497 0%,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285AEB 90%)">'
                f'{glyph(name, int(s*.56), "#fff")}</div>')
    return f'<div class="app" style="width:{s}px;height:{s}px;border-radius:{int(s*.26)}px">{glyph(name, int(s*.58))}</div>'

def frame(n, body):
    dots = "".join(f'<i class="{"on" if k == n else ("done" if k < n else "")}"></i>' for k in range(1, TOTAL + 1))
    return f'''<section class="slide" id="s{n}"><img class="logo" src="../../brand/feed/logo-dark.png">
<div class="count">{n:02d} / {TOTAL:02d}</div><div class="content">{body}</div>
<div class="dots">{dots}</div><div class="next">{ic("arrow-right", 30)}</div></section>'''

def status(steps):
    """AI status pill: [(a, b, text)]"""
    return '<div class="stat"><img src="assets/a-mark-white.png"><div class="stx">' + "".join(
        f'<span data-show="{a},{b}">{t}</span>' for a, b, t in steps) + "</div></div>"

def sec(no, day, title, desc, mock, dk=False):
    return (f'<div class="ag"><span class="agt">AGENT {no:02d} <i></i> HARI {day}</span><h2>{title}</h2>'
            f'<p class="desc">{desc}</p><div class="mock{" dk" if dk else ""}">{mock}</div></div>')

def typ(t, dur, text):
    return f'<span data-type="{t},{dur}" data-full="{text}"></span>'

SEP = '<div class="sep"></div>'

# ---------------------------------------------------------------- slide 1 (cover)
apps = [("whatsapp", 120, 70), ("instagram", 120, 290), ("gmail", 760, 60), ("googlecalendar", 800, 190), ("googlesheets", 760, 320), ("google", 330, 330)]
HX, HY = 440, 190
paths = "".join(f'<path class="flow" d="M{HX},{HY} C{(HX + x) / 2},{HY} {(HX + x) / 2},{y} {x},{y}"/>' for _, x, y in apps)
dotsv = "".join(f'<circle class="fd" data-p="{i}" r="6"/>' for i in range(len(apps)))
appt = "".join(f'<div class="capp" data-in="{.5 + i * .18}" style="left:{x - 40}px;top:{y - 40}px">{tile(n, 80)}</div>' for i, (n, x, y) in enumerate(apps))
AG = ["Website + SEO", "Leads + follow-up", "WhatsApp + kalender", "Konten", "Editor reels", "Auto-posting", "Mission control"]
chips = "".join(f'<span data-in="{2.2 + i * .25}"><b>{i + 1:02d}</b>{a}</span>' for i, a in enumerate(AG))
s1 = frame(1, f'''<span class="tag">CLAUDE × BISNIS</span>
<h1 style="font-size:68px">7 AI Agent yang Bisa<br>Kamu <u>Bangun Minggu Ini</u></h1>
<p class="lead" style="margin-top:12px;font-size:29px">Hubungkan Claude ke WhatsApp, Instagram, dan Gmail.</p>
<div class="cviz"><svg width="880" height="390">{paths}{dotsv}</svg>
<div class="chub" data-in=".2">{glyph("claude", 70)}</div>{appt}</div>
<div class="card clist"><label>7 AGENT · 1 MINGGU</label><div class="chips">{chips}</div>
<p data-in="4.4">{ic("sparkles", 22)}Plus <b>10 agent bonus</b> yang tinggal kamu nyalain.</p></div>''')

# ---------------------------------------------------------------- slide 2: agents 1-2
checks = [("Meta title", 2.7), ("Alt text gambar", 3.3), ("Kecepatan mobile", 3.9), ("Sitemap", 4.5)]
m1 = f'''<div class="win site"><div class="wbar"><b>Roti Pagi</b><span>Menu · Pesan · Lokasi</span>
<em class="draft" data-show="0,1.9">Draft</em><em class="live" data-in="1.9">{ic("check", 14)}Live</em></div>
<div class="hero"><div><h4>Roti hangat tiap pagi,<br><span>di Dago.</span></h4><p>Pesan sebelum jam 6, diantar jam 7.</p><i class="btnp">Pesan sekarang</i></div>
<div class="himg">{ic("croissant", 64)}</div></div><div class="url">{ic("globe", 14)}rotipagi.pages.dev</div></div>
<div class="win seo"><div class="wh">{glyph("google", 18)}<b>Audit SEO</b></div>
<div class="ring"><svg width="96" height="96"><circle cx="48" cy="48" r="40" class="rb"/><circle cx="48" cy="48" r="40" class="rf" data-ring="2.5,4.9,54,92"/></svg>
<b data-cnt="2.5,4.9,54,92">54</b><small>/100</small></div>
<ul>{"".join(f'<li data-on="{t}"><i>{ic("check", 12)}</i>{n}</li>' for n, t in checks)}</ul></div>
{status([(0.2, 1.8, "Bikin website…"), (1.8, 2.5, "Publish ke rotipagi.pages.dev"), (2.5, 5.0, "Benerin SEO…"), (5.0, 9, "Website live, SEO beres ✓")])}'''
HOT = lambda i: f'<em class="hot" data-in="{3.0 + i * .2}">HOT</em>'
rows = [("PT Arunika Digital", 120, "9.1", 1), ("Nusa Fintech", 90, "8.8", 1), ("Kopiloka Group", 60, "8.4", 0), ("Sinar Legal", 35, "7.2", 0)]
tr = "".join(f'''<tr><td>{c}</td><td><i class="sk" data-show="0,{1.0 + i * .45}"></i><span data-in="{1.0 + i * .45}">{n}</span></td>
<td><i class="sk" data-show="0,{1.2 + i * .45}"></i><b data-in="{1.2 + i * .45}">{sc}</b></td><td>{HOT(i) if hot else ''}</td></tr>''' for i, (c, n, sc, hot) in enumerate(rows))
m2 = f'''<div class="win leads"><div class="wh">{glyph("googlemaps", 18)}<b>Leads · kantor di Dago, Bandung</b>{glyph("googlesheets", 16)}</div>
<table><tr><th>Perusahaan</th><th>Karyawan</th><th>Skor</th><th></th></tr>{tr}</table></div>
<div class="win mail"><div class="wh">{glyph("gmail", 18)}<b>Pesan baru</b></div><p class="to">Ke: Rina, HR · PT Arunika</p>
<p class="subj">Snack box buat meeting pagi?</p><p class="body">{typ(3.4, 1.6, "Halo Bu Rina, selamat atas kantor barunya! Kami bisa siapkan snack box buat meeting pagi tim Anda. 10 box pertama gratis, mau coba Jumat ini?")}</p>
<div class="mrow"><i class="send" id="send2" data-on="5.4">Kirim</i><em data-in="5.6">{ic("clock", 13)}Follow-up 3 hari</em></div></div>
{status([(0.2, 1.0, "Cari kantor di Maps…"), (1.0, 3.3, "Riset & kasih skor…"), (3.3, 5.4, "Nulis email…"), (5.4, 9, "Email terkirim ✓")])}'''
s2 = frame(2, sec(1, 1, "Website Jadi, <u>SEO Beres</u>", "Bikin website, benerin SEO-nya, lalu cek di Google.", m1) + SEP +
          sec(2, 2, "Mesin Cari <u>Leads + Follow-up</u>", "Cari calon klien, kasih skor, lalu kirim email ke tiap lead.", m2)
          + '<div class="cursor" data-keys=\'[[4.6,"#send2",60,40],[5.4,"#send2"],[6.4,"#send2",-30,50]]\'>' + ic("mouse-pointer-2", 40) + '</div>')

# ---------------------------------------------------------------- slide 3: agents 3-4
m3 = f'''<div class="win wa"><div class="wh">{glyph("whatsapp", 20)}<b>Rina · Arunika</b><small>online</small></div><div class="chat">
<p class="in" data-in=".4">Kak, Jumat bisa 50 snack box jam 9?</p>
<p class="out dots3" data-show="1.1,2.0"><i></i><i></i><i></i></p>
<p class="out" data-in="2.0">Bisa kak, jam 9 masih kosong. Aku catat ya?</p>
<p class="in" data-in="3.0">Boleh, atas nama Rina ya</p>
<p class="out" data-in="4.4">Siap, sudah masuk jadwal ✓</p></div></div>
<div class="col"><div class="win cal"><div class="wh">{glyph("googlecalendar", 18)}<b>Jumat, 27 Nov</b></div>
<div class="slots"><span>07.00</span><span>08.00</span><span>09.00</span><span>10.00</span>
<i class="ev1">Produksi pagi</i><i class="ev2" data-in="3.8">Antar 50 box · Arunika</i></div></div>
<div class="win inbox"><div class="wh">{glyph("gmail", 16)}<b>Inbox</b><small><b data-cnt="4.6,6.2,4,0">4</b> belum dibaca</small></div>
{"".join(f'<p data-on="{4.7 + i * .4}"><i></i>{t}</p>' for i, t in enumerate(["Harga paket catering?", "Bisa kirim ke Cimahi?", "Minta invoice bulan ini"]))}</div></div>
{status([(0.2, 2.0, "Balas WhatsApp…"), (2.0, 3.8, "Cek kalender…"), (3.8, 4.6, "Booking jadwal antar ✓"), (4.6, 9, "Rapikan inbox…")])}'''
grid = [("croissant", "3,1rb", 0), ("cake-slice", "18,2rb", 1), ("coffee", "2,4rb", 0), ("cookie", "12,7rb", 2), ("sandwich", "1,9rb", 0), ("croissant", "9,8rb", 3)]
def gtile(i, n, v, top):
    badge = f'<em data-in="{0.9 + top * .4}">TOP {top}</em>' if top else ""
    return f'<div class="gt g{i % 3}">{ic(n, 34)}<small>{ic("play", 11)}{v}</small>{badge}</div>'
gh = "".join(gtile(i, n, v, top) for i, (n, v, top) in enumerate(grid))
m4 = f'''<div class="win ig"><div class="wh">{tile("instagram", 26)}<b>@rotipagi.bdg</b><small>8,2rb followers</small></div><div class="ggrid">{gh}</div></div>
<div class="col"><div class="win trend"><div class="wh">{ic("trending-up", 18)}<b>Tren: “roti sourdough”</b></div>
<svg width="300" height="62"><path data-draw="1.6,3.0" d="M4,54 C40,50 60,52 90,46 S150,44 180,34 S240,22 296,6"/></svg></div>
<div class="win doc"><div class="wh">{ic("file-text", 18)}<b>Rencana reels minggu ini</b></div><ol>
<li>{typ(3.0, .9, "Kenapa sourdough kami agak asam?")}</li><li>{typ(4.0, .9, "3 roti yang habis duluan tiap pagi")}</li><li>{typ(5.0, .8, "Dapur kami jam 3 pagi")}</li></ol></div></div>
{status([(0.2, 2.2, "Pelajari postingan kamu…"), (2.2, 3.0, "Format terbaik: behind the scene"), (3.0, 9, "Nulis hook…")])}'''
s3 = frame(3, sec(3, 3, "WhatsApp, Kalender, <u>Inbox Beres</u>", "Balas chat, booking jadwal, dan rapikan email, bahkan pas kamu tidur.", m3) + SEP +
          sec(4, 4, "Agent Konten yang <u>Ngerti Datamu</u>", "Pelajari konten yang works, cek tren, lalu tulis ide reels.", m4))

# ---------------------------------------------------------------- slide 4: agents 5-6
tools = "".join(f'<span data-on="{t}">{n}</span>' for n, t in [("Potong", 1.0), ("Caption", 2.6), ("B-roll", 3.6), ("Export", 4.6)])
cuts = "".join(f'<i data-in="{1.0 + k * .12}" style="left:{x}%"></i>' for k, x in enumerate([12, 23, 31, 44, 52, 63, 71, 84]))
caps = "".join(f'<i data-in="{2.6 + k * .1}" style="left:{2 + k * 10.5}%"></i>' for k in range(9))
brol = "".join(f'<i data-in="{3.6 + k * .15}" style="left:{x}%"></i>' for k, x in enumerate([8, 30, 55, 78]))
m5 = f'''<div class="win editor"><div class="prev">{ic("croissant", 54)}<em data-in="2.9">DAPUR JAM 3 PAGI</em><span>9:16</span></div>
<div class="tracks"><div class="tools">{tools}</div>
<div class="trk"><label>Video</label><div class="lane v">{cuts}</div></div>
<div class="trk"><label>Caption</label><div class="lane c">{caps}</div></div>
<div class="trk"><label>B-roll</label><div class="lane b">{brol}</div></div>
<div class="trk"><label>Musik</label><div class="lane m"><i data-grow="0.6,1.4"></i></div></div>
<div class="ph" data-ph="0.8,6.0"></div><p class="meta">2:14 mentah → 0:30 · 41 jeda dipotong · 4 b-roll</p></div></div>
{status([(0.2, 1.0, "Ambil klip mentah…"), (1.0, 2.6, "Potong 41 jeda…"), (2.6, 4.6, "Tambah caption & b-roll…"), (4.6, 9, "Export 9:16 ✓")])}'''
DAYS = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
def pday(k, d):
    inner = f'<div class="pt" data-in="{0.6 + [0, 2, 4].index(k) * .5}">{ic("play", 16)}<small>19.00</small></div>' if k in (0, 2, 4) else ""
    return f'<div class="pd"><span>{d}</span>{inner}</div>'
plan = "".join(pday(k, d) for k, d in enumerate(DAYS))
LIKES = {"Instagram": 1240, "Facebook": 312, "Google Bisnis": 86}
def post(logo, name, a, b):
    return (f'<div class="win pp"><div class="wh">{logo}<b>{name}</b></div><div class="pthumb">{ic("croissant", 28)}</div>'
            f'<em class="q" data-show="0,{a}">{ic("clock", 12)}Terjadwal 19.00</em><em class="ok" data-in="{a}">{ic("check", 12)}Tayang</em>'
            f'<small data-in="{b}">{ic("heart", 12)}<b data-cnt="{b},{b + 1.4},0,{LIKES[name]}">0</b></small></div>')
m6 = f'''<div class="win planner"><div class="wh">{glyph("meta", 18)}<b>Planner minggu ini</b><small>3 reels · 3 platform</small></div><div class="pdays">{plan}</div></div>
<div class="posts">{post(tile("instagram", 22), "Instagram", 3.0, 3.4)}{post(glyph("facebook", 22), "Facebook", 3.8, 4.2)}{post(glyph("google", 20), "Google Bisnis", 4.6, 5.0)}</div>
{status([(0.2, 2.4, "Jadwalkan 3 reels…"), (2.4, 3.6, "Posting ke Instagram…"), (3.6, 4.4, "Tayang di Facebook"), (4.4, 9, "Update Google Bisnis ✓")])}'''
s4 = frame(4, sec(5, 5, "Editor Reels <u>Tanpa Begadang</u>", "Klip mentah masuk, reels 30 detik lengkap caption keluar.", m5, dk=True) + SEP +
          sec(6, 6, "Sekali Jadwal, <u>Tayang di Semua</u>", "Satu reels, tayang di Instagram, Facebook, dan Google Bisnis.", m6))

# ---------------------------------------------------------------- slide 5: agent 7 + bonus
kpi = "".join(f'<div><b data-cnt="0.4,2.6,0,{v}">0</b><span>{n}</span></div>' for n, v in [("Leads ditemukan", 48), ("Chat dibalas", 23), ("Pesanan masuk", 6), ("Konten tayang", 3)])
agents = ["SEO bot", "Leads", "Follow-up", "Inbox", "Kalender", "WhatsApp", "Konten", "Editor reels", "Auto-post"]
agh = "".join(f'<span data-in="{0.3 + i * .08}"><i></i>{a}</span>' for i, a in enumerate(agents))
m7 = f'''<div class="win mc"><div class="mch"><b>Mission control</b><em>{ic("zap", 13)}9 agent jalan</em></div><div class="kpi">{kpi}</div>
<div class="agrid">{agh}</div><div class="appr"><span>{ic("bell", 16)}Follow-up ke PT Arunika nunggu persetujuanmu</span>
<i class="ok1" id="appr" data-show="0,4.6">Setujui</i><i class="ok2" data-in="4.6">{ic("check", 14)}Disetujui</i></div></div>'''
BON = [("star", "Balas review Google"), ("receipt", "Tagih invoice"), ("message-circle", "Balas komentar IG"), ("newspaper", "Penulis newsletter"),
       ("magnet", "Pembuat lead magnet"), ("binoculars", "Pantau kompetitor"), ("notebook-pen", "Notulen meeting"), ("file-text", "Penulis proposal"),
       ("layers", "Reels jadi story"), ("bell", "Laporan mingguan")]
bon = "".join(f'<div class="bn">{ic(i, 20)}<b>{n}</b><div class="tg" data-on="{1.2 + k * .32}"><i></i></div></div>' for k, (i, n) in enumerate(BON))
s5 = frame(5, sec(7, 7, "Semua Agent, <u>Satu Layar</u>", "Pantau semua agent di satu dashboard. Yang penting, kamu yang approve.", m7) + SEP +
          f'<div class="ag"><span class="agt">BONUS <i></i> SIAP PAKAI</span><h2>+10 Agent, <u>Tinggal Nyalain</u></h2><div class="bgrid">{bon}</div></div>'
          + '<div class="cursor" data-keys=\'[[3.6,"#appr",70,60],[4.55,"#appr"],[5.6,"#appr",-40,70]]\'>' + ic("mouse-pointer-2", 40) + '</div>')

css = (D / "base.css").read_text() + (D / "style.css").read_text()
js = (D / "anim.js").read_text()
(D / "index.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{s1}{s2}{s3}{s4}{s5}<script>{js}</script></body></html>')
print("ok")
