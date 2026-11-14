Bikin FAQ akordeon yang membuka jawaban satu per satu dengan mulus, untuk landing page toko hijab. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat dusty pink di atas):
- Navbar: logo bulat dusty pink dengan ikon kilau + "Hijab Nara", menu "Koleksi  Ukuran  Kontak".
- Kolom kiri (sekitar 290 px): label "PERTANYAAN UMUM" (ikon tanda tanya), judul "Masih ragu?" / "Cek dulu di sini." (baris kedua dusty pink tua), teks "Jawaban dari pertanyaan yang paling sering masuk ke admin kami.", kartu putih "Belum ketemu jawabannya?" / "Admin siap bantu pilih ukuran." dengan tombol "Tanya admin" (ikon chat) dan teks kecil "Biasanya balas < 10 menit".
- Kolom kanan: daftar 4 kartu FAQ (lebar 540 px, tinggi tertutup 66 px, jarak 12 px, sudut 18 px, overflow hidden). Tiap kartu: pertanyaan tebal di kiri, ikon "+" dalam lingkaran di kanan, jawaban 2 baris di bawahnya.
  1. Bisa bayar di tempat (COD)? → Bisa. COD tersedia untuk Jabodetabek dan Bandung, bayar ke kurir saat paket sampai.
  2. Berapa lama pengirimannya? → Pulau Jawa 2–3 hari kerja, luar Jawa 3–6 hari. Nomor resi dikirim lewat WhatsApp.
  3. Kalau ukurannya nggak pas? → Tukar ukuran gratis maksimal 7 hari setelah paket diterima, asal label masih terpasang.
  4. Ada harga khusus reseller? → Ada, mulai beli 12 pcs. Chat admin untuk daftar harga reseller.
- Kartu yang terbuka: tinggi 140 px, bingkai dusty pink 2 px, latar sedikit merah muda, lingkaran ikon jadi dusty pink dengan "+" putih yang berputar 135° (jadi tanda ×).

Animasi (satu timeline GSAP, repeat: -1, total 6 detik, otomatis seperti demo):
- Buka: tinggi 66 → 140 px (0,5 dtk, power3.inOut), bingkai muncul, jawaban turun 8 px sambil muncul (mulai 0,18 dtk kemudian), ikon berputar 135° (back.out).
- Tutup: kebalikannya (jawaban memudar dulu, tinggi kembali 66 px).
- Urutan: 0,35 dtk buka nomor 1 → 1,85 dtk tutup 1 sambil buka 2 → 3,35 dtk tutup 2 sambil buka 3 → 4,85 dtk tutup 3. Kartu di bawahnya ikut bergeser karena daftar memakai flex column.
- Detik 6 semua tertutup (sama dengan detik 0), jadi loop-nya mulus. Di web asli, klik pertanyaan juga membuka/menutup dengan animasi yang sama (hanya satu yang terbuka).
