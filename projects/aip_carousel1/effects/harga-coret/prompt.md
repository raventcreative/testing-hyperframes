Bikin animasi harga coret di kartu produk: harga lama tercoret, harga promo muncul, dan badge diskon menempel seperti stempel. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih-krem):
- Navbar tipis: logo kotak oranye membulat + nama toko "Dapur Kue Laras", menu "Produk  Hampers  Kontak", ikon tas belanja di kanan.
- Dua kolom. Kiri: foto produk rasio 4:5, sudut membulat 26 px, bayangan lembut (pakai kotak gradien krem-oranye sebagai pengganti foto, nanti aku ganti foto produkku).
- Kanan: label kecil "HAMPERS LEBARAN" dengan ikon kado, nama produk "Hampers Kue Kering" (tebal) + baris kedua "isi 3 toples", 5 bintang kuning + "4,9 · 1.240 terjual", harga lama "Rp 285.000" (besar, tebal), tempat harga promo "Rp 199.000" (merah-oranye #e0472b, lebih besar) di bawahnya, chip hijau "Hemat Rp 86.000", tulisan "Stok promo: sisa 12 paket" + bar stok 30%, tombol oranye "Tambah ke keranjang" dengan ikon keranjang, tombol hati kotak, dan baris kecil "Kirim se-Jabodetabek · gratis kartu ucapan".
- Badge bulat merah-oranye "HEMAT 30%" menempel di pojok kiri atas foto.

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. 0,45 dtk: garis merah tebal 6 px menggores harga lama dari kiri ke kanan (scaleX 0 → 1, 0,4 dtk).
2. 0,95 dtk: harga lama mengecil ke 52%, naik 18 px, warnanya jadi abu-abu (0,55 dtk).
3. 1,1 dtk: harga promo naik dari 46 px di bawah, dari blur 8 px jadi tajam, opacity 0 → 1 (0,55 dtk, power3.out).
4. 1,5 dtk: badge jatuh seperti stempel: dari skala 2,2 dan rotasi -32° ke skala 1 dan rotasi -10° (back.out), lalu fotonya bergetar kecil 4 langkah.
5. 1,95 dtk: chip "Hemat Rp 86.000" muncul dengan pop (skala 0,6 → 1).
6. 2,5 dtk: kilau putih diagonal menyapu badge; 3,0 dtk tombol keranjang berdenyut pelan (skala 1,04) dua kali.
7. 4,7 sampai 5,6 dtk: semuanya kembali ke kondisi awal: chip dan badge menghilang, harga promo turun dan hilang, harga lama balik ke ukuran dan warna semula, garis coret ditarik habis ke arah kanan.
Kondisi di detik 6 harus sama persis dengan detik 0, jadi loop-nya mulus tanpa loncatan.
