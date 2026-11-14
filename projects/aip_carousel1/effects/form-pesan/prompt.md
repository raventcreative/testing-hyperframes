Bikin form pesanan bertahap (3 langkah) dengan progress bar dan ringkasan pesanan yang terisi otomatis, untuk toko kue ulang tahun. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat pink muda):
- Navbar: logo bulat pink dengan ikon kue + "Kue Nisa", menu "Katalog  Cara-pesan  Kontak".
- Kartu form di kiri (548 x 486 px, sudut 24 px): judul "Pesan kue ulang tahun", teks kecil "3 langkah, kurang dari 1 menit", stepper 3 lingkaran bernomor (UKURAN, TULISAN, AMBIL) yang dihubungkan garis abu; garis pink mengisi dari kiri saat pindah langkah dan lingkaran langkah aktif jadi pink.
- Di bawah stepper ada jendela konten (overflow hidden) berisi 3 panel berjajar horizontal:
  1. "Pilih ukuran kue": 3 kartu pilihan "Ø 16 cm · 8 orang · Rp 240.000", "Ø 20 cm · 12 orang · Rp 320.000", "Ø 24 cm · 20 orang · Rp 450.000". Yang dipilih dapat bingkai pink 3 px + centang bulat pink.
  2. "Tulisan di atas kue": kolom input dengan teks yang terketik "Selamat ulang tahun, Bunda!" (ada kursor), keterangan "maks. 40 huruf", dan chip pilihan krim "Krim putih / Krim pink (terpilih) / Cokelat".
  3. "Tanggal ambil": 3 kotak tanggal "JUM 12", "SAB 13", "MIN 14" dan 3 pilihan jam "10.00", "13.00", "16.00".
- Tombol bawah: "‹ Kembali" (garis) dan tombol pink "Lanjut →" yang di langkah terakhir berubah jadi "Kirim pesanan".
- Panel sukses yang menutupi form: lingkaran hijau dengan centang, "Pesanan terkirim!", "Admin konfirmasi lewat WhatsApp dalam 10 menit."
- Kartu "Ringkasan pesanan" di kanan (300 px): kotak gradien pink dengan ikon kue, baris UKURAN / TULISAN / AMBIL (awalnya "belum diisi" abu-abu), Total (awalnya "Rp 0"), dan catatan "Bayar setelah dikonfirmasi admin".

Animasi (satu timeline GSAP, repeat: -1, total 6 detik; klik disimulasikan otomatis dengan efek riak):
1. 0,5 dtk: pilih "Ø 20 cm" → bingkai pink + centang pop; ringkasan UKURAN jadi "Ø 20 cm · 12 orang" dan Total jadi "Rp 320.000" (crossfade).
2. 1,12 dtk: tekan "Lanjut" → deretan panel geser ke kiri 1 panel (0,5 dtk, power3.inOut), garis progres pertama terisi, lingkaran 2 jadi pink. 1,85–2,6 dtk: teks tulisan terketik huruf per huruf; ringkasan TULISAN terisi.
3. 2,85 dtk: tekan "Lanjut" → geser ke panel 3, garis progres kedua terisi, lingkaran 3 pink, tombol berubah jadi "Kirim pesanan". 3,4 dtk pilih "SAB 13", 3,65 dtk pilih "10.00"; ringkasan AMBIL jadi "Sabtu 13 · jam 10.00".
4. 4,1 dtk: tekan "Kirim pesanan" → panel sukses muncul, centang hijau pop (back.out).
5. 5,1 dtk: di belakang panel sukses semua di-reset (panel ke langkah 1, pilihan & teks dihapus, tombol kembali "Lanjut"), garis progres mengosong, ringkasan kembali "belum diisi" / "Rp 0", lalu panel sukses memudar. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
