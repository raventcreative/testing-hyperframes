# Riset audiens dari kolom komentar: AIpreneur navy remake, 5 slides 1080x1350 (old house style: Poppins, 110px safe zone).
# Build: python3 build.py && node render.js && node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
def ph(f, st="", pos="center"): return f'<div class="ph" style="{st}"><img src="assets/photos/{f}.jpg" style="object-position:{pos}"></div>'
def cm(u, t, meta, st="", hl=False): return f'<div class="cm{" hl" if hl else ""}" style="{st}"><i></i><div><small>{u}</small><span>{t}</span><em>{meta}</em></div></div>'
def lg(f, st): return f'<img class="lg" src="assets/3d/{f}.png" style="{st}">'
def frame(body, swipe=False):
    sw = '<div class="swipe">Swipe →</div>' if swipe else ''
    return f'<section class="slide"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>{body}{sw}</section>'

S = []
# 1 cover
S.append(frame(
  '<div class="vis" style="height:560px">' + ph("80e46647", "inset:0", "center 30%")
  + cm("rina.jualan", "Kak, ini bisa buat jualan skincare gak?", "2 hari · 248 suka", "left:26px;top:30px")
  + cm("budi_umkm", "Aku masih bingung mulai AI dari mana…", "1 hari · 131 suka", "left:26px;top:170px", True)
  + lg("instagram", "right:30px;top:28px;width:118px;transform:rotate(8deg)")
  + lg("tiktok", "right:44px;bottom:30px;width:92px;transform:rotate(-8deg)") + '</div>'
  + '<h1 class="cv">Capek <b>screenshot</b> komentar<br>satu-satu buat riset?<br>Tarik <b class="ac">ratusan komentar</b><br>dalam <b>hitungan menit</b> pakai <b>Apify.</b></h1>', swipe=True))
# 2 banyak tim ngerasa udah riset
S.append(frame(
  '<div class="vis" style="height:600px">' + ph("77477944", "left:0;top:0;bottom:0;width:390px", "center 55%")
  + cm("andi.coffee", "Kalau tim cuma 2 orang, AI-nya kepake gak?", "67 suka", "left:420px;top:40px;width:440px")
  + cm("sari.olshop", "Capek bales chat satu-satu tiap malam", "212 suka", "left:440px;top:225px;width:420px", True)
  + cm("dewi.creator", "Prompt-nya dong kak", "96 suka", "left:420px;top:410px;width:440px") + '</div>'
  + '<h2>Banyak tim ngerasa udah riset,</h2>'
  + '<p class="bd">padahal cuma <b>download konten dan screenshot komentar</b> satu per satu sampai capek. <b>Tenaganya habis buat ngumpulin,</b> bukan buat mikir. Padahal suara audiens <b>yang paling jujur ada di kolom komentar.</b></p>'
  + '<p class="bd"><b>Langkah ini bikin riset audiens berhenti jadi kerja berat</b> dan mulai jadi sumber ide. Contohnya pakai <b class="ac">Apify dan Claude.</b></p>'))
# 3 riset paling jujur ada di kolom komentar
lst = "".join(f'<div class="li"><i></i><div><small>{u}</small><span>{t}</span></div><em>♡ {n}</em></div>' for u, t, n in [
  ("andi.coffee", "Kalau tim cuma 2 orang, AI-nya kepake gak?", 67), ("sari.olshop", "Capek bales chat satu-satu tiap malam", 212),
  ("rina.jualan", "Bisa buat jualan skincare gak kak?", 248), ("dewi.creator", "Prompt-nya dong kak", 96), ("yoga.kopi", "Takut mahal langganannya", 41)])
S.append(frame(
  '<h2 style="font-size:50px">Riset audiens paling jujur<br>udah ada di kolom komentar,<br><span class="ac">tinggal diangkat.</span></h2>'
  + '<p class="bd"><b>Orang mikir riset itu harus mahal dan ribet,</b> padahal audiens udah nulis isi kepalanya gratis tiap hari. Yang bikin <b>suara itu jarang kepake cuma satu:</b> jumlahnya kebanyakan buat dibaca manual.</p>'
  + '<p class="bd">Begitu <b>AI yang bacain, tumpukan komentar berubah jadi sumber ide</b> paling murah yang kamu punya.</p>'
  + f'<div class="vis" style="flex:1;margin-top:34px"><div class="list"><div class="lh">Komentar (318)</div>{lst}</div>'
  + cm("sari.olshop", "Capek bales chat satu-satu tiap malam", "212 suka", "left:426px;top:40px;width:420px;transform:rotate(-2deg)", True)
  + cm("yoga.kopi", "Takut mahal langganannya", "41 suka", "left:480px;top:220px;width:360px;transform:rotate(1.5deg)") + '</div>'))
# 4 step 01 Apify
act = lambda t, slug, d: f'<div class="act"><div><h4>{t}</h4><code>{slug}</code><p>{d}</p></div><span class="btn">Try for free</span></div>'
S.append(frame(
  '<div class="num"><b>01</b><h2 style="margin:0">Tarik ratusan komentar<br>pakai Apify</h2></div>'
  + '<div style="margin-top:56px">' + act("Instagram Comments Scraper", "apify/instagram-comment-scraper", "Tempel link post atau reels, dapat teks komentar, username, jumlah suka, dan waktunya.")
  + act("TikTok Comments Scraper", "clockworks/tiktok-comments-scraper", "Tempel link video TikTok, dapat semua komentarnya. Bisa di-export ke CSV, JSON, atau Excel.") + '</div>'
  + '<p class="bd" style="margin-top:60px"><b>Buka Apify, pilih actor comment scraper</b> buat <b>Instagram atau TikTok,</b> lalu tempel link konten kamu dan kompetitor. Dalam hitungan menit, ratusan komentar terkumpul sekaligus.</p>'
  + '<p class="bd">Kerjaan yang tadinya <b>berjam-jam screenshot satu-satu sekarang kelar cepat,</b> dan tenagamu bisa dipindah ke mikirnya.</p>'))
# 5 hasil mentah perlu diolah
S.append(frame(
  '<h2 class="w">Hasil scrape mentah<br>masih perlu diolah jadi<br><span class="ac">insight yang kepake.</span></h2>'
  + '<div class="two"><div><p class="bd" style="margin-top:0"><b>Di sinilah Claude masuk:</b> ratusan komentar dikelompokkan jadi pertanyaan, keluhan, keinginan, dan kata-kata asli audiens.</p>'
  + '<p class="bd"><b>Kata-kata asli itulah yang langsung jadi hook.</b> Satu file CSV, satu prompt, dan stok ide kontenmu datang langsung dari audiens.</p></div>'
  + '<div class="vis" style="height:700px">' + lg("claude", "left:50%;top:0;width:220px;transform:translateX(-50%) rotate(-6deg)")
  + '<div class="out"><div class="lh">Insight dari 318 komentar</div>'
  + "".join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a, b in [("Keluhan", "capek bales chat"), ("Pertanyaan", "mulai AI dari mana"), ("Keinginan", "minta prompt"), ("Keraguan", "takut mahal")])
  + '</div></div></div>'))

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Riset Komentar</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print("ok", len(S))
