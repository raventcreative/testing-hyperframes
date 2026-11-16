# Anthropic: pekerjaan paling terdampak AI (AIpreneur navy, 5 slides).
# Data: Anthropic labor market report (Mar 2026), "observed exposure", US occupations.
# Photo: Dario Amodei at TechCrunch Disrupt 2023, TechCrunch via Wikimedia Commons, CC BY 2.0.
from pathlib import Path
D = Path(__file__).parent
SRC = "Sumber: Anthropic, laporan dampak AI ke pasar kerja (Maret 2026) · skor “observed exposure”, data pekerjaan di AS"

def frame(cls, body, swipe=False):
    sw = '<div class="bot">Geser →</div>' if swipe else ''
    return f'<section class="slide {cls}"><img class="logo" src="assets/logo_white.png" alt="AIpreneur">{body}{sw}</section>'

def chart(data, hi=0, ymax=80):
    W, H, PL, PB, PT = 860, 700, 44, 96, 46   # svg size, left pad, bottom label area, top pad
    cw = (W - PL) / len(data); bw = cw * 0.56
    ph = H - PB - PT
    y = lambda v: PT + ph * (1 - v / ymax)
    g = ""
    for t in range(0, ymax + 1, 20):
        g += f'<line x1="{PL}" x2="{W}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="gl{" base" if t == 0 else ""}"/><text x="{PL-10}" y="{y(t)+5:.1f}" class="yl">{t}%</text>'
    bars = ""; pts = []
    for i, (name, v) in enumerate(data):
        cx = PL + cw * i + cw / 2; top = y(v); h = max(y(0) - top, 3)
        pts.append((cx, top))
        cls = "b hi" if i == hi else "b"
        bars += f'<rect x="{cx-bw/2:.1f}" y="{y(0)-h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="6" class="{cls}"/>'
        bars += f'<text x="{cx:.1f}" y="{top-30:.1f}" class="vl{" vh" if i == hi else ""}">{str(v).replace(".", ",")}%</text>'
        words = name.split(); lines = []; cur = ""
        for w in words:
            if len(cur + " " + w) > 9 and cur: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur)
        bars += "".join(f'<text x="{cx:.1f}" y="{y(0)+24+k*16:.1f}" class="xl">{ln}</text>' for k, ln in enumerate(lines[:4]))
    line = " ".join(f"{x:.1f},{t-12:.1f}" for x, t in pts)
    dots = "".join(f'<circle cx="{x:.1f}" cy="{t-12:.1f}" r="5" class="dt"/>' for x, t in pts)
    return f'<svg class="ch" viewBox="0 0 {W} {H}">{g}{bars}<polyline points="{line}" class="tr"/>{dots}</svg>'

def slide(label, a, b, sub, data, note, hi=0):
    return frame("cs", f'''<div class="label">{label}</div>
  <h1>{a}<br><span>{b}</span></h1><p class="sub">{sub}</p>
  <div class="cw">{chart(data, hi)}</div>
  <div class="ft"><p class="nt">{note}</p><p class="src">{SRC}</p></div>''')

TOP = [("Programmer",74.5),("Customer service",70.1),("Petugas entri data",67.1),("Petugas rekam medis",66.7),("Riset pasar",64.8),
       ("Transkripsi medis",63.7),("Sales grosir",62.8),("Arsitek database",57.9),("Analis keuangan",57.2),("Tester software",52.0)]
POP = [("Admin & sekretaris",45.3),("Penerjemah",43.0),("Staf HR",40.3),("Desainer grafis",36.7),("Akuntan & auditor",34.8),("Marketing manager",32.0),
       ("Guru SMA",29.0),("Software developer",28.8),("Penulis",24.6),("Jurnalis",21.0),("Pengacara",16.7),("Kasir",8.5)]
FIN = [("Analis keuangan",57.2),("Sales sekuritas",44.1),("Manajer keuangan",39.1),("Penasihat keuangan",35.0),("Akuntan & auditor",34.8),("Agen asuransi",31.9),
       ("Staf pembukuan",31.0),("Debt collector",29.9),("Analis risiko",26.5),("Petugas kredit",18.6),("Analis kredit",16.9),("Teller bank",2.3)]
LAP = [("Programmer",74.5),("Perawat",6.0),("Kurir",4.1),("Kuli bangunan",2.8),("Koki restoran",1.2),("Tukang ledeng",1.2),
       ("Pelayan restoran",0),("Satpam",0),("Tukang listrik",0),("Montir mobil",0),("Sopir truk",0)]

cover = frame("cover", f'''<div class="ph"><span class="cred">Foto: Dario Amodei, CEO Anthropic · TechCrunch via Wikimedia Commons (CC BY 2.0)</span>
  <img src="assets/dario.jpg" alt="Dario Amodei"></div>
  <div class="label">Data Anthropic · Maret 2026</div>
  <h1>Anthropic bongkar pekerjaan<br><span>yang paling terdampak AI.</span></h1>
  <p class="sub">Kerjaan lo masuk daftarnya? Geser dan cek skornya.</p>''', swipe=True)
s1 = slide("Semua pekerjaan", "10 pekerjaan", "paling terdampak AI.", "Makin tinggi skor, makin banyak tugasnya yang sudah dikerjakan pakai AI.", TOP,
           "Programmer di puncak: hampir 3 dari 4 tugasnya sudah tersentuh AI.")
s2 = slide("Pekerjaan populer lain", "Seberapa terdampak", "kerjaan lo?", "Kerjaan kantoran dan kreatif ada di tengah.", POP,
           "Admin, penerjemah dan HR paling tinggi. Kasir paling rendah.")
s3 = slide("Dunia finance", "Analis paling", "terdampak AI.", "Kerja analisa data kena duluan, kerja tatap muka belakangan.", FIN,
           "Analis keuangan 57,2%. Teller bank cuma 2,3%.")
s4 = slide("Kerja lapangan", "Kerja fisik,", "minim terdampak AI.", "Dibanding programmer, kerja lapangan nyaris belum tersentuh AI.", LAP,
           "Banyak kerja lapangan masih 0%. Skill tangan belum tergantikan.")
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Anthropic jobs AI</title><style>{CSS}</style></head><body>{cover}{s1}{s2}{s3}{s4}</body></html>')
print("ok")
