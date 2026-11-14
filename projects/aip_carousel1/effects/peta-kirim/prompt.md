Bikin peta pengiriman Indonesia yang hidup: jalur paket melengkung keluar dari kota asal ke kota-kota tujuan, ikon paket ikut meluncur di ujung jalurnya, dan label estimasi muncul saat sampai. Untuk landing page toko batik. Satu file HTML, pakai HTML + CSS + SVG + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih kebiruan sangat muda):
- Navbar: logo bulat indigo dengan ikon baju + "Batik Sekar Jogja", menu "Koleksi  Ukuran  Kontak".
- Kiri atas: label "PENGIRIMAN" (ikon truk), judul "Dikirim dari Jogja," / "sampai ke rumahmu." (baris kedua indigo). Kanan atas: 2 chip putih "Kirim tiap hari jam 16.00" (ikon jam) dan "Resi dikirim lewat WhatsApp" (ikon chat).
- Peta Indonesia sebagai SVG inline (outline pulau-pulau, isi biru keabuan #dfe5f5, garis putih tipis; negara tetangga lebih pucat). Pakai data outline Indonesia yang sederhana (misalnya dari Natural Earth, domain publik) dan proyeksi sederhana: x = (bujur − 94,6) × k, y = (6,3 − lintang) × k, dengan k = lebar peta / 46,6.
- Titik asal Yogyakarta (110,37; −7,80): lingkaran navy dengan cincin yang berdenyut, plus chip gelap "Gudang Jogja" dengan ikon paket di bawahnya.
- 6 kota tujuan: Medan (98,67; 3,59) "3–4 hari", Jakarta (106,85; −6,21) "1–2 hari", Balikpapan (116,83; −1,27) "3–5 hari", Makassar (119,43; −5,15) "3–4 hari", Denpasar (115,22; −8,65) "2–3 hari", Jayapura (140,72; −2,53) "5–8 hari".
- Jalur = kurva kuadratik dari Jogja ke tiap kota yang melengkung ke atas (titik kontrol di tengah garis, digeser tegak lurus sejauh 32% panjang garis, maksimal 150 px), garis indigo 2,6 px ujung bulat.
- Legenda kecil di bawah: titik gelap "Gudang", titik indigo "Kota tujuan", "Estimasi kurir reguler, contoh".

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. Cincin di Jogja berdenyut tiap 1,5 detik (radius 9 → 26 px sambil memudar).
2. Jalur ke-6 kota digambar bergantian mulai 0,3 dtk dengan jeda 0,25 dtk: stroke-dashoffset dari panjang jalur ke 0 (sekitar 0,8–1,2 dtk tergantung panjang, power1.inOut).
3. Lencana paket bulat putih (ikon paket) bergerak tepat di ujung garis yang sedang digambar (ambil titik-titik di sepanjang kurva dan atur waktunya dengan easing yang sama), lalu hilang saat sampai.
4. Saat sampai: titik kota muncul (pop), cincin menyebar sekali, dan label putih "Medan · 3–4 hari" (dst.) muncul dengan pop di dekat kotanya tanpa saling menutupi.
5. 4,7 dtk: label, jalur, dan titik kota memudar; semuanya di-reset saat sudah tidak terlihat. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
