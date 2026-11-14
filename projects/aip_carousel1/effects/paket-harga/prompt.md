Bikin bagian paket harga dengan "paket unggulan" yang maju ke depan dan bingkainya bercahaya berputar, untuk jasa foto produk. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat ungu sangat muda di tengah):
- Navbar: logo bulat ungu dengan ikon kamera + "Studio Kilau", menu "Portofolio  Paket  Kontak", tombol gelap "Konsultasi gratis".
- Judul tengah: label kecil "PAKET FOTO PRODUK" lalu "Foto produk siap jualan".
- Tiga kartu harga berjajar (268 px, sudut 24 px): nama paket, deskripsi kecil, harga besar "/ sesi", 4 fitur dengan ikon centang dalam lingkaran, tombol di bawah.
  - Hemat · Buat mulai jualan · Rp 350rb · 10 foto produk, Latar putih polos, Edit warna dasar, Selesai 3 hari · tombol garis "Pilih Hemat"
  - Laris · Paling sering dipilih UMKM · Rp 650rb · 25 foto produk, Latar putih + 5 foto gaya, Edit warna detail, Selesai 2 hari · tombol ungu "Pilih paket Laris"
  - Lengkap · Buat katalog lengkap · Rp 1,2 jt · 50 foto produk, Foto gaya + model tangan, Video pendek 15 detik, Selesai 4 hari · tombol garis "Pilih Lengkap"
- Kartu tengah (Laris) sedikit lebih tinggi, punya bingkai gradien 6 px: wadah overflow hidden bersudut 28 px berisi persegi besar dengan conic-gradient (ungu, biru muda, lavender, pink, kembali ungu) di belakang kartu putih. Di atasnya pita "PALING LARIS" ungu, dan di belakangnya cahaya ungu blur.

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. Conic-gradient di bingkai berputar 360° penuh selama 6 detik (ease "none"), jadi cahayanya terlihat mengalir terus tanpa sambungan.
2. 0,3 dtk: kartu tengah + bingkai + pita naik 12 px dan membesar 1,04 (power3.out), cahaya ungu menguat, kartu kiri dan kanan meredup ke opacity 0,62 dan skala 0,97.
3. 0,75 dtk: lingkaran centang fitur di kartu tengah berubah hijau satu per satu (jeda 0,22 dtk, pop back.out).
4. 1,9 dtk: kilau putih menyapu pita "PALING LARIS". 2,6 dtk: tombol "Pilih paket Laris" berdenyut pelan dua kali.
5. 4,85 sampai 5,65 dtk: centang hijau kembali abu, kartu tengah turun ke posisi awal, kartu samping kembali normal. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
