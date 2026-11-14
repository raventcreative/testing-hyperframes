Bikin tombol pesan yang "nempel" di bawah layar: muncul saat tombol utama di hero sudah ter-scroll lewat, dan hilang lagi saat kembali ke atas. Untuk landing page jasa servis AC. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px):
- Navbar putih tetap di atas: logo bulat biru dengan ikon angin + "Servis AC Sejuk", menu "Layanan  Harga  Area".
- Hero (latar biru sangat muda): label "SERVIS AC PANGGILAN · BEKASI", judul "AC kurang dingin?" / "Teknisi datang hari ini." (baris kedua biru), paragraf "Cuci, isi freon, sampai bongkar pasang. Harga jelas sebelum dikerjakan.", tombol biru "Pesan teknisi" (ikon kalender), 5 bintang + "4,9 · 1.800+ servis selesai". Di kanan: kartu "Jadwal teknisi hari ini" dengan 3 slot jam: 09.00 PENUH (abu), 13.00 TERSEDIA (hijau), 16.00 TERSEDIA, dan "Area: Bekasi, Cikarang, Tambun".
- Bagian 2: "Kenapa pilih Servis AC Sejuk?" + 3 kartu fitur dengan ikon: "Garansi 30 hari", "Datang < 3 jam", "Harga jelas di awal" (masing-masing 2 baris penjelasan).
- Bagian 3: "Daftar harga" + 4 baris: Cuci AC 0,5–1 PK · Rp 75.000; Isi freon R32 · mulai Rp 150.000; Bongkar pasang AC · Rp 250.000; Cek kerusakan · gratis.
- Bar melekat di bawah layar (lebar penuh dikurangi 20 px kiri-kanan, tinggi 74 px, sudut 22 px, gradien biru tua): ikon angin dalam kotak, "Cuci AC mulai Rp 75.000", teks kecil "Teknisi bisa datang hari ini", dan tombol biru terang "Pesan teknisi →" di kanan.

Perilaku di web asli: pakai IntersectionObserver pada tombol "Pesan teknisi" di hero. Saat tombol itu keluar dari layar, bar melekat naik masuk dari bawah (y 110 → 0, opacity 0 → 1, 0,45 dtk, back.out); saat tombol hero terlihat lagi, bar turun keluar (0,35 dtk).

Mode demo (supaya bisa dilihat tanpa scroll manual): halaman di dalam wadah 588 px dengan overflow hidden, lalu timeline GSAP repeat: -1 selama 6 detik:
1. 0,7–2,5 dtk: konten halaman bergeser ke atas 700 px (power2.inOut), indikator scrollbar tipis di kanan ikut turun.
2. 1,55 dtk: bar melekat muncul. 3,0 dtk: tombol di bar ditekan (riak + memantul).
3. 3,7–5,3 dtk: halaman kembali ke atas; 4,5 dtk bar turun keluar.
Detik 6 sama dengan detik 0, jadi loop-nya mulus.
