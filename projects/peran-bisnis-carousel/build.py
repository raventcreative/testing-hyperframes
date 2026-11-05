# Fills <!--ROLES--> in carousel.src.html with one slide per role -> carousel.html
from pathlib import Path

# (name, font-size, nickname, one-liner, [(value, note) x4: audiens, kerjaan, risiko, modal])
ROLES = [
    ("Founder", 124, "Si pembangun", "Mulai dari nol. <b>Dari ide jadi bisnis.</b>", [
        ("Customer &amp; partner", "Yang harus percaya sama visi lu."),
        ("Bangun dari nol", "Produk, tim, sistem, semuanya."),
        ("Perusahaan gagal", "Kalau gagal, ya mulai ulang."),
        ("Ide &amp; modal", "Visi jelas plus modal awal."),
    ]),
    ("CEO", 124, "Si nahkoda", "Yang <b>nentuin arah kapal.</b>", [
        ("Pemegang saham", "Mereka nagih hasil, bukan alasan."),
        ("Ambil keputusan", "Tiap hari, besar maupun kecil."),
        ("Gagal memimpin", "Salah arah, satu perusahaan kena."),
        ("Orang &amp; sistem", "Kerjanya lewat tim, bukan sendirian."),
    ]),
    ("Entrepreneur", 116, "Si pemburu peluang", "Lihat celah, tes, <b>gagal, coba lagi.</b>", [
        ("Target market", "Siapa yang mau bayar solusinya."),
        ("Ngetes peluang", "Validasi dulu, baru gas."),
        ("Usahanya gagal", "Makanya tes kecil dulu."),
        ("Skill &amp; network", "Kenalan sering lebih mahal dari modal."),
    ]),
    ("Business Owner", 104, "Si operator", "Yang mastiin <b>bisnis jalan tiap hari.</b>", [
        ("Customer yang bayar", "Cashflow itu oksigennya."),
        ("Ngurus operasional", "Stok, tim, sampai komplain."),
        ("Rugi finansial", "Salah hitung margin, langsung kerasa."),
        ("Tim &amp; stok", "Aset yang harus diputar terus."),
    ]),
    ("Influencer", 124, "Si penggerak audiens", "Bisnisnya adalah <b>perhatian orang.</b>", [
        ("Followers", "Trust mereka adalah aset utama."),
        ("Bikin konten", "Konsisten, tiap hari."),
        ("Nggak relevan lagi", "Algoritma nggak nunggu siapa-siapa."),
        ("Konten &amp; kreativitas", "Ide adalah bahan bakunya."),
    ]),
    ("Investor", 124, "Si pemodal", "Uangnya yang kerja, <b>bukan tenaganya.</b>", [
        ("Founder &amp; market", "Nyari tim dan pasar yang tepat."),
        ("Evaluasi investasi", "Riset, hitung, baru masuk."),
        ("Modal hilang", "Nggak semua taruhan menang."),
        ("Modal &amp; riset", "Data dan uang, dua-duanya wajib."),
    ]),
]
KEYS = [("i-aud", "Audiens", ""), ("i-work", "Kerjaan harian", ""), ("i-risk", "Risiko terbesar", " risk"), ("i-res", "Modal utama", "")]

def slide(name, size, nick, ess, cards):
    cells = "".join(
        f'<div class="card{cls}"><div class="k"><svg><use href="#{ic}"/></svg>{label}</div>'
        f'<div class="v">{v}</div><div class="n">{n}</div></div>'
        for (ic, label, cls), (v, n) in zip(KEYS, cards))
    return f'''<section class="slide role">
  <div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  <span class="tag">{nick}</span>
  <div class="name" style="font-size:{size}px">{name}<span>.</span></div>
  <p class="sub ess">{ess}</p>
  <div class="grid">{cells}</div>
  <div class="bot"><span class="swipe">Geser →</span></div>
</section>
'''

d = Path(__file__).parent
src = (d / "carousel.src.html").read_text()
(d / "carousel.html").write_text(src.replace("<!--ROLES-->", "\n".join(slide(*r) for r in ROLES)))
print("ok")
