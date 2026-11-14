Bikin animasi "masuk keranjang": foto produk terbang melengkung ke ikon keranjang dan angka di keranjang bertambah, untuk toko tanaman online. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat hijau muda):
- Navbar putih: logo bulat hijau dengan ikon tunas + "Teras Hijau", menu "Tanaman  Pot  Perawatan", tombol ikon keranjang di kanan dengan badge angka bulat merah-oranye di pojok kanan atasnya (awalnya tersembunyi).
- Judul "Tanaman meja paling dicari" + teks kecil "Gratis pupuk cair + panduan rawat di setiap pesanan".
- 3 kartu produk (272 x 404 px, sudut 22 px): foto 252 x 204 px (pakai kotak gradien hijau sebagai pengganti foto), nama, deskripsi, harga, tombol hijau "+ Keranjang" yang setelah diklik berubah jadi hijau muda "✓ Ditambahkan". Produk: Bonsai Meja (Pot keramik putih · 20 cm · Rp 85.000), Syngonium Pink (Pot hitam minimalis · Rp 65.000), Palem Kipas (Pot tanah liat · 45 cm · Rp 87.000).
- Dropdown keranjang mini (362 px, putih, sudut 22 px) di bawah ikon keranjang: "Keranjang (3)", 3 baris (thumbnail, nama, "1 x harga", harga), garis putus-putus, "Total Rp 237.000", tombol hijau tua "Checkout →" yang setelah diklik jadi "✓ Pesanan dibuat".

Animasi (satu timeline GSAP, repeat: -1, total 6 detik; klik-kliknya disimulasikan otomatis):
1. 0,35 dtk, 1,3 dtk, 2,25 dtk: tombol produk 1, 2, 3 ditekan bergantian (efek riak putih + tombol mengecil 0,95 lalu memantul), labelnya berubah jadi "✓ Ditambahkan".
2. Tiap kali ditekan, salinan foto produk berbentuk lingkaran 70 px (bingkai putih) muncul di tengah foto, lalu terbang ke ikon keranjang dalam 0,62 dtk dengan lintasan melengkung: tween x pakai ease "power1.in" dan tween y pakai ease "power2.out" secara bersamaan, sambil mengecil ke 0,3 dan memudar.
3. Saat foto sampai: ikon keranjang membesar 1,2 dan miring -10° lalu kembali dengan elastic. Badge muncul (pop) berisi "1"; di tambahan berikutnya angka lama naik keluar dan angka baru naik masuk (2, lalu 3) sambil badge berdenyut.
4. 3,35 dtk: dropdown keranjang terbuka (skala 0,86 → 1 dari pojok kanan atas, back.out). 4,3 dtk: tombol Checkout ditekan → "✓ Pesanan dibuat".
5. 5,0 dtk: dropdown menutup, badge hilang, tombol produk kembali ke "+ Keranjang", angka badge di-reset. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
