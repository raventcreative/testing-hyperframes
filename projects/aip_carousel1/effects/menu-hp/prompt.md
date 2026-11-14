Bikin menu HP: ikon tiga garis berubah jadi X lalu panel menu turun dan link-nya masuk berurutan, untuk web jasa cuci sepatu. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan:
- Halaman latar lembut dengan mockup HP di tengah (280 x 566 px, bingkai gelap sudut 44 px, layar putih sudut 35 px, notch kecil, status bar "09.41" + baterai).
- Di layar HP: header putih (54 px) berisi logo kotak teal dengan ikon jejak kaki + "Bersih Lagi", dan tombol menu tiga garis (3 garis 20 x 2,6 px) di kanan. Di bawahnya: foto sepatu sudut 20 px (pakai kotak gradien sebagai pengganti foto), judul "Sepatu kusam?" / "Kami bikin bersih lagi." (baris kedua teal), teks "Jemput-antar gratis se-Surabaya. Selesai 2–3 hari.", tombol teal "Jemput sepatuku" (ikon truk), chip "Cuci reguler / Repaint / Anti-kuning", dan kotak ulasan "4,9 dari 870 ulasan" + "\"Sepatu putihku balik kayak baru.\"".
- Panel menu (di bawah header sampai bawah layar, gradien teal tua ke hampir hitam): 5 link besar putih dengan panah kanan dan garis pemisah tipis: "Layanan", "Harga" (warna teal muda), "Cara kerja", "Lokasi", "Testimoni"; tombol putih "Chat admin" (ikon chat) dan teks kecil "Buka setiap hari 08.00–20.00".
- Di kiri dan kanan HP ada kartu keterangan putih dengan garis putus-putus ke HP: "LANGKAH 1 · Tombol menu jadi X · Tiga garis berputar halus membentuk tanda silang." dan "LANGKAH 2 · Menu turun berurutan · Panel turun dari atas, link masuk satu per satu."

Animasi (satu timeline GSAP, repeat: -1, total 6 detik, klik disimulasikan otomatis):
1. 0,55 dtk: tombol menu ditekan (riak). 0,6 dtk: garis atas turun 7 px + rotasi 45°, garis bawah naik 7 px + rotasi -45°, garis tengah menghilang (scaleX 0,2) → jadi X (0,38 dtk, power3.inOut). Kartu "LANGKAH 1" menyala (bingkai teal) dan membesar sedikit.
2. 0,68 dtk: panel menu turun dengan clip-path inset(0 0 100% 0) → inset(0 0 0 0) (0,55 dtk, power3.inOut). 0,95 dtk: link masuk dari kiri 26 px satu per satu (jeda 0,07 dtk), lalu tombol "Chat admin" dan teks jam buka. Kartu "LANGKAH 2" menyala.
3. 3,3 dtk: tombol X ditekan → link keluar dari bawah ke atas, panel naik tertutup (clip-path kembali), X kembali jadi tiga garis.
4. 4,6 dtk: tombol "Jemput sepatuku" berdenyut sekali. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
Di web asli: tombol menu benar-benar membuka/menutup panel dengan animasi yang sama.
