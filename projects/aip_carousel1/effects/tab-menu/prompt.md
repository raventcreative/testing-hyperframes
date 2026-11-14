Bikin tab menu kafe yang ganti kategori dengan indikator pil yang meluncur dan kartu menu yang masuk satu per satu. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar krem sangat muda ke putih):
- Navbar: logo bulat cokelat dengan ikon kopi + "Kopi Teras Senja", menu "Menu  Lokasi  Promo", tombol cokelat tua "Pesan antar" dengan ikon truk.
- Kiri atas: judul "Menu hari ini" dan teks kecil "Diseduh dari biji kopi Temanggung". Kanan atas: grup tab berbentuk pil (latar krem) berisi 3 tab dengan ikon: "Kopi", "Non-Kopi", "Camilan". Tab aktif ditandai pil cokelat tua yang bisa bergeser, teks tab aktif putih.
- Di bawahnya 3 kartu menu (272 x 384 px, sudut 22 px): foto 252 x 210 px (pakai kotak gradien sebagai pengganti foto), label kecil opsional di pojok foto, nama menu tebal, deskripsi pendek, harga, tombol "+" cokelat tua.
- Data menu:
  - Kopi: Kopi Susu Aren (Espresso, susu segar, gula aren · Rp 22.000 · label TERLARIS), Es Americano (Double shot, tanpa gula · Rp 20.000), Cappuccino (Busa susu lembut, latte art · Rp 26.000)
  - Non-Kopi: Matcha Latte (Matcha + susu, dingin · Rp 27.000 · label BARU), Es Cokelat (Cokelat pekat, krim kocok · Rp 24.000), Jus Semangka (Buah segar tanpa sirup · Rp 18.000)
  - Camilan: Donat Cokelat (Taburan meses warna-warni · Rp 12.000), Croissant Mentega (Dipanggang tiap pagi · Rp 18.000 · label HANGAT), Cookies Cokelat (Renyah luar, lembut dalam · Rp 15.000)

Animasi (satu timeline GSAP, repeat: -1, total 6 detik, tab berganti otomatis seperti demo):
- 1,55 dtk pindah ke Non-Kopi, 3,3 dtk ke Camilan, 5,05 dtk kembali ke Kopi.
- Tiap pindah tab: riak putih kecil di tab yang dipilih, pil indikator meluncur ke tab itu (0,45 dtk, power3.inOut), warna teks tab bertukar (putih/cokelat) dengan fade 0,25 dtk.
- Kartu lama naik 22 px sambil memudar (0,24 dtk, jeda 0,04 dtk antar kartu), lalu kartu baru naik dari 34 px di bawah sambil muncul (0,45 dtk, power3.out, jeda 0,08 dtk antar kartu).
- Di detik 6 kondisinya sama dengan detik 0 (tab Kopi aktif), jadi loop-nya mulus.
- Tab juga bisa diklik manual: klik tab menjalankan animasi pindah yang sama.
