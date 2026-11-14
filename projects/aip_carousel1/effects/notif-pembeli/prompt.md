Bikin notifikasi "baru saja beli" yang muncul gantian di pojok kiri bawah halaman produk. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan halaman (lebar sekitar 930 px, latar putih dengan semburat hijau muda di atas):
- Navbar: logo bulat hijau dengan ikon api + "Sambal Bu Ratmi", menu "Produk  Resep  Kontak", ikon tas belanja.
- Kolom kiri: label "BEST SELLER · DIBUAT TIAP PAGI", judul 2 baris "Sambal Ijo Teri," / "pedasnya bikin nagih." (baris kedua hijau), paragraf "Cabai hijau segar + teri Medan, tanpa pengawet. Tahan 2 minggu di kulkas.", harga "Rp 45.000 / botol 200 gr", tombol hijau tua "Beli sekarang" (ikon keranjang) dan tombol garis "Lihat resep".
- Kolom kanan: foto produk sudut membulat 28 px (pakai kotak gradien hijau sebagai pengganti foto), chip putih di pojok kiri atas foto "● 18 orang lagi lihat produk ini" dengan titik merah, dan chip gelap "★ Terlaris minggu ini" di pojok kanan bawah foto.
- Toast notifikasi (lebar 390 px, tinggi 88 px, putih, sudut 20 px, bayangan lembut) di pojok kiri bawah: thumbnail produk kecil, teks "**Rina** di Bandung baru saja beli **2 botol**", baris kecil dengan ikon centang hijau "3 menit lalu · pembeli terverifikasi", tombol × kecil di kanan atas, dan garis progres hijau 4 px di bagian bawah toast.

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. Titik merah di chip "lagi lihat" berdenyut tiap 1,5 detik (lingkaran transparan membesar 2x lalu hilang).
2. 0,35 dtk: toast pertama masuk dari kiri (x -440 → 0, back.out ringan, 0,55 dtk). Garis progres di bawahnya menyusut dari kanan ke kiri selama 1,75 dtk. 2,55 dtk: toast turun 40 px sambil memudar (0,35 dtk).
3. 3,15 dtk: toast kedua masuk dengan cara yang sama: "**Dimas** di Surabaya baru saja beli **1 botol**" · "8 menit lalu · pembeli terverifikasi", lalu keluar di 5,35 dtk.
4. Di detik 6 tidak ada toast yang tampil (sama dengan detik 0), jadi loop-nya mulus.
Simpan data pembeli di array JavaScript supaya gampang ditambah atau diganti.
