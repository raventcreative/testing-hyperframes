# Builds carousel.html (AIpreneur "Tim AI" carousel, 1080x1350) -> render with render.js
import re
from pathlib import Path

D = Path(__file__).parent


def brand(name):
    d = re.search(r'd="([^"]+)"', (D / "assets/icons" / f"{name}.svg").read_text()).group(1)
    return f'<svg viewBox="0 0 24 24"><path fill="currentColor" d="{d}"/></svg>'


# Line icons (24x24, stroke)
def line(body):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


I = {
    "script": line('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M8.5 12.5h7M8.5 16h4.5"/>'),
    "bolt": line('<path d="M13 2.5 4.5 13.5H12l-1 8 8.5-11H12z"/>'),
    "target": line('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".8"/><path d="M12 12 19 5M16.5 4.5 19 5l.5 2.5"/>'),
    "deal": line('<path d="m3 11 3.5-3.5 4 1.2L13 7l4.5 1.5L21 11"/><path d="m3 11 5.5 5.5a1.6 1.6 0 0 0 2.2 0l.3-.3M21 11l-6.6 6.6a1.6 1.6 0 0 1-2.2 0L8.5 14"/><path d="m10.5 8.7 3.3 3.3"/>'),
    "funnel": line('<path d="M3.5 4.5h17l-6.5 8v6l-4 2v-8z"/>'),
    "mega": line('<path d="M4 10v4a1 1 0 0 0 1 1h2l6 4V5L7 9H5a1 1 0 0 0-1 1z"/><path d="M17 9a4 4 0 0 1 0 6M19.5 6.5a7.5 7.5 0 0 1 0 11"/>'),
    "mail": line('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>'),
    "db": line('<ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/>'),
    "headset": line('<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19c0 1.5-1.5 2.5-4 2.5h-2"/>'),
    "chart": line('<path d="M4 20h16"/><rect x="5" y="12" width="3" height="5" rx=".6"/><rect x="10.5" y="8.5" width="3" height="8.5" rx=".6"/><rect x="16" y="5" width="3" height="12" rx=".6"/>'),
    "chat": line('<path d="M20.5 11.5a7.5 7.5 0 0 1-11 6.6L4 19.5l1.4-4.6A7.5 7.5 0 1 1 20.5 11.5z"/><path d="M9 11.5h.01M12.5 11.5h.01M16 11.5h.01" stroke-width="2.6"/>'),
    "invoice": line('<path d="M6 2.5h12v19l-3-2-3 2-3-2-3 2z"/><path d="M9 7.5h6M9 11h6M9 14.5h3.5"/>'),
    "calendar": line('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4M8 14h.01M12 14h.01M16 14h.01M8 17.3h.01M12 17.3h.01" />'),
    "gear": line('<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M2.5 12h3M18.5 12h3M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>'),
    "cv": line('<rect x="4" y="3" width="16" height="18" rx="2.5"/><circle cx="12" cy="9.5" r="2.6"/><path d="M7.5 17c.6-2.2 2.4-3.3 4.5-3.3s3.9 1.1 4.5 3.3"/>'),
    "users": line('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5"/><circle cx="17.5" cy="9" r="2.6"/><path d="M17 14.6c2.4.2 4 1.8 4.6 4.6"/>'),
    "check": line('<path d="m5 12.5 4.5 4.5L19 7.5"/>'),
}

SPARK = ('<svg class="spark" viewBox="0 0 100 100"><path fill="#fff" d="M50 4C53 34 66 47 96 50 66 53 53 66 50 96 47 66 34 53 4 50 34 47 47 34 50 4Z"/>'
         '<path fill="#fff" opacity=".55" d="M80 12c1 7 4 10 11 11-7 1-10 4-11 11-1-7-4-10-11-11 7-1 10-4 11-11Z"/></svg>')


def hub(cls=""):
    return f'<div class="hub {cls}"><div class="hub-in">{SPARK}</div></div>'


def head(tag, title, sub):
    return f'''<div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  <div class="tag">{tag}</div>
  <h1>{title}</h1>
  <p class="sub">{sub}</p>'''


FOOT = '<div class="bot">Geser →</div>'

# ---------- 1. COVER ----------
DIVS = [("Social Media", "9 peran", "users"), ("Business Growth", "6 peran", "chart"),
        ("Sales &amp; Comms", "2 peran", "chat"), ("Finance &amp; Ops", "4 peran", "invoice")]
cover_nodes = "".join(
    f'<div class="node n{i}"><div class="ic">{I[ic]}</div><div><b>{t}</b><span>{n}</span></div></div>'
    for i, (t, n, ic) in enumerate(DIVS))
cover = f'''<section class="slide cover">
  <div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  <div class="tag">Claude untuk Bisnis</div>
  <h1>Rekrut <span class="c">21 Karyawan AI</span><br>Buat Bisnis Lu.</h1>
  <p class="sub">4 divisi. Kerja 24 jam. Lu tinggal kasih arahan.</p>
  <div class="orbit">
    <svg class="rings" viewBox="0 0 860 700"><ellipse cx="430" cy="350" rx="360" ry="250"/><ellipse cx="430" cy="350" rx="215" ry="150"/>
      <path class="wire" d="M430 350C300 350 220 240 200 90M430 350C560 350 640 240 660 90M430 350C300 350 220 460 200 610M430 350C560 350 640 460 660 610"/></svg>
    {hub("big")}
    {cover_nodes}
  </div>
  {FOOT}
</section>'''

# ---------- 2. SOCIAL MEDIA ----------
SOC = [("youtube", "#FF0033", "YouTube Growth", "Strategi channel"),
       ("instagram", "ig", "Social Media Manager", "Kalender &amp; posting"),
       ("script", "#00c9ff", "Script Viral &amp; SEO", "Naskah YouTube"),
       ("tiktok", "#111", "Repurpose Konten", "1 ide, banyak format"),
       ("facebook", "#0866FF", "Facebook Growth", "Organic reach"),
       ("instagram", "ig", "Instagram Growth", "Reels &amp; engagement"),
       ("linkedin", "#0A66C2", "LinkedIn Growth", "Personal branding"),
       ("x", "#111", "X / Twitter Growth", "Thread &amp; insight"),
       ("bolt", "#00c9ff", "Hook Viral", "3 detik pertama")]


def soc_card(icon, color, t, d):
    svg = I[icon] if icon in I else brand(icon)
    style = 'class="tile ig"' if color == "ig" else f'class="tile" style="--b:{color}"'
    return f'<div class="card"><div {style}>{svg}</div><div class="tx"><b>{t}</b><span>{d}</span></div></div>'


social = f'''<section class="slide team social">
  {head("Divisi 01", 'Social Media <span class="c">Growth Team.</span>', "Bangun audiens. Perluas jangkauan. Bikin brand lu dilirik.")}
  <div class="tree">
    <svg class="wires" viewBox="0 0 860 120"><path d="M430 0V60M136 120V80q0-20 20-20h548q20 0 20 20v40M430 60v60"/>
      <circle cx="136" cy="116" r="6"/><circle cx="430" cy="116" r="6"/><circle cx="724" cy="116" r="6"/></svg>
    {hub("sm")}
    <div class="grid g3">{"".join(soc_card(*s) for s in SOC)}</div>
  </div>
  {FOOT}
</section>'''

# ---------- 3. BUSINESS GROWTH ----------
BIZ = [("target", "Offer Bisnis", "Racik penawaran yang bikin orang mikir dua kali buat nolak."),
       ("deal", "Negosiasi Sales", "Siapin argumen &amp; jawab keberatan calon pembeli."),
       ("funnel", "Sales Funnel", "Alur dari baru kenal sampai transfer."),
       ("mega", "Branding", "Positioning, tone, dan cara brand lu ngomong."),
       ("mail", "Email List Growth", "Bangun &amp; rawat database pelanggan."),
       ("db", "CRM &amp; Sistem", "Rapihin data pelanggan dan SOP bisnis.")]


def biz_card(ic, t, d, side):
    return f'<div class="card {side}"><div class="tile">{I[ic]}</div><b>{t}</b><span>{d}</span></div>'


bl = "".join(biz_card(*b, "l") for b in BIZ[:3])
br = "".join(biz_card(*b, "r") for b in BIZ[3:])
business = f'''<section class="slide team biz">
  {head("Divisi 02", 'Business <span class="c">Growth Team.</span>', "Offer lebih kuat, brand lebih tajam, sistem sales yang jalan.")}
  <div class="split">
    <svg class="wires" viewBox="0 0 860 640"><path d="M430 320C380 320 360 104 300 104M430 320H300M430 320C380 320 360 536 300 536M430 320C480 320 500 104 560 104M430 320H560M430 320C480 320 500 536 560 536"/>
      <circle cx="300" cy="104" r="6"/><circle cx="300" cy="320" r="6"/><circle cx="300" cy="536" r="6"/><circle cx="560" cy="104" r="6"/><circle cx="560" cy="320" r="6"/><circle cx="560" cy="536" r="6"/></svg>
    <div class="col">{bl}</div>{hub("md")}<div class="col">{br}</div>
  </div>
  {FOOT}
</section>'''

# ---------- 4. SALES & COMMUNICATION ----------
def sales_card(ic, t, d, tasks):
    li = "".join(f'<li>{I["check"]}{x}</li>' for x in tasks)
    return f'<div class="card"><div class="tile big">{I[ic]}</div><div class="pill">{t}</div><p>{d}</p><ul>{li}</ul></div>'


sales = f'''<section class="slide team sales">
  {head("Divisi 03", 'Sales &amp; <span class="c">Communication Team.</span>', "Ubah obrolan jadi klien.")}
  <div class="bubbles"><div class="bb a">{I["chat"]}</div><div class="bb b"><i></i><i></i><i></i></div></div>
  <svg class="wires" viewBox="0 0 860 90"><path d="M380 10C250 10 215 40 215 86M480 10C610 10 645 40 645 86"/><circle cx="215" cy="84" r="6"/><circle cx="645" cy="84" r="6"/></svg>
  <div class="duo">
    {sales_card("headset", "Client Advisor", "Pendampingan klien &amp; jaga hubungan jangka panjang.", ["Balas chat cepat", "Jawab pertanyaan", "Jaga klien lama"])}
    {sales_card("chart", "Sales Advisor", "Support tim sales &amp; dorong deal sampai closing.", ["Kualifikasi leads", "Follow-up rapi", "Dorong ke closing"])}
  </div>
  <div class="flow"><span>Chat masuk</span><em>→</em><span>Dibalas</span><em>→</em><span>Follow-up</span><em>→</em><span class="hl">Closing</span></div>
  {FOOT}
</section>'''

# ---------- 5. FINANCE & OPS ----------
FIN = [("invoice", "Invoicing Specialist", "Invoice &amp; catatan pembayaran."),
       ("calendar", "Management Assistant", "Jadwal, dokumen &amp; support admin."),
       ("gear", "Business Operations", "Asisten bisnis &amp; operasional harian."),
       ("cv", "Recruitment Assistant", "CV, resume &amp; seleksi lamaran.")]
fin_cards = "".join(f'<div class="card c{i}"><div class="tile">{I[ic]}</div><b>{t}</b><span>{d}</span></div>'
                    for i, (ic, t, d) in enumerate(FIN))
finance = f'''<section class="slide team fin">
  {head("Divisi 04", 'Finance &amp; <span class="c">Operations Team.</span>', "Operasional rapi. Lu fokus jualan.")}
  <div class="quad">{fin_cards}{hub("md")}</div>
  {FOOT}
</section>'''

CSS = (D / "style.css").read_text()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><title>Tim AI Carousel</title>
<style>{CSS}</style></head><body>
{cover}
{social}
{business}
{sales}
{finance}
</body></html>'''
(D / "carousel.html").write_text(html)
print("ok")
