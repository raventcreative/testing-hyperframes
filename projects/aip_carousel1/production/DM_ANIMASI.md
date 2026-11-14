# Paket Animasi Landing Page · 15 prompt buat Claude

Halo! Ini 15 prompt dari carousel AI PRENEUR. Tiap prompt = satu animasi landing page seperti yang kamu lihat di slide-nya (detail warna atau ukuran hasil Claude bisa sedikit beda, tinggal minta revisi).

**Cara pakai**
1. Buka Claude (claude.ai), mulai chat baru.
2. Salin SATU prompt di bawah (semua teks di dalam kotak), tempel, kirim.
3. Claude bikin satu file HTML. Lihat hasilnya di panel preview, atau simpan sebagai `.html` lalu buka di browser.
4. Ganti nama toko, harga, teks, dan link WhatsApp dengan punyamu. Foto produk di prompt pakai kotak warna sebagai pengganti: tinggal ganti dengan foto produkmu sendiri.

Semua prompt minta satu file HTML (HTML + CSS + JavaScript, animasinya pakai GSAP 3 dari CDN cdnjs). Di demo, klik-kliknya dijalankan otomatis dan berulang tiap 6 detik supaya kelihatan; kalau mau dipakai di web asli, minta Claude: "jalankan animasinya saat tombolnya diklik, bukan otomatis".

## 01 · Harga coret

**HARGA PROMO** · cocok buat: Halaman promo, flash sale, hampers musiman.

```text
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
```

## 02 · Tombol bernapas

**TOMBOL CHAT** · cocok buat: Jasa & katering yang order-nya lewat chat.

```text
Bikin tombol "Pesan via WhatsApp" yang bernapas di hero landing page katering. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat hijau sangat tipis):
- Navbar: logo bulat hijau dengan ikon sendok-garpu + "Catering Mama Rina", menu "Menu  Paket  Testimoni".
- Kolom kiri: label kecil hijau "KATERING HARIAN · JAKARTA SELATAN", judul 2 baris "Makan siang kantor," / "rasa masakan rumah." (baris kedua hijau), paragraf "Menu ganti tiap hari. Minimal 10 porsi, diantar sebelum jam 11.30.", status "Admin online · biasanya balas < 5 menit" dengan titik hijau, tombol hijau besar berbentuk pil "Pesan via WhatsApp" (ikon chat di lingkaran putih di kiri tombol), link "Lihat menu minggu ini →", dan baris 3 avatar inisial + "120+ kantor langganan tiap minggu".
- Kolom kanan: foto makanan sudut membulat 30 px (pakai kotak gradien hijau-krem sebagai pengganti foto), chip putih "★ 4,8 · 320 ulasan" di pojok kanan atas foto, dan kartu harga putih yang menumpuk di kiri bawah foto: "PAKET HARIAN", "Rp 28.000 / porsi", "Nasi + 3 lauk + buah potong".
- Tombol WhatsApp di sini cuma teks + ikon chat biasa (jangan pakai logo WhatsApp asli). Link tombolnya https://wa.me/62xxxxxxxxxx (nanti aku ganti).

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. Tombol "bernapas" 4 kali per loop (tiap 1,5 detik): skala 1 → 1,055 → 1 dengan sine.inOut, bayangan hijaunya ikut membesar lalu mengecil.
2. Di tiap napas, cincin hijau menyebar keluar dari tombol: box-shadow 0 → 30 px, dari hijau transparan 55% jadi 0 (1,2 detik), dan titik "Admin online" ikut berdenyut (lingkaran membesar 1,8x lalu hilang).
3. 2,15 dtk: badge merah "1" muncul di ikon chat (pop). 2,3 dtk: gelembung chat hijau muda muncul dari kiri bawah (skala 0,6 → 1, back.out): "PESAN BARU / Halo kak, mau pesan 20 porsi buat Jumat ini ya. / 11.02".
4. 4,85 dtk: gelembung chat dan badge menghilang, jadi detik 6 sama persis dengan detik 0 dan loop-nya mulus.
```

## 03 · Notif pembeli

**NOTIFIKASI** · cocok buat: Toko online, produk best seller, pre-order.

```text
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
```

## 04 · Dinding ulasan

**ULASAN** · cocok buat: Bagian testimoni di landing page jasa & produk.

```text
Bikin "dinding ulasan" pelanggan: tiga kolom kartu testimoni yang bergerak terus (naik, turun, naik) di landing page laundry. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat biru muda):
- Navbar putih: logo bulat biru dengan ikon baju + "Laundry Wangi Kilat", menu "Layanan  Harga  Ulasan", tombol biru kecil "Jemput gratis".
- Kolom kiri (lebar sekitar 270 px): label "KATA PELANGGAN" dengan ikon kutip, judul 3 baris "Wangi, rapi," / "pelanggan" / "balik lagi." (baris terakhir biru), kartu ringkasan rating: angka besar "4,9", 5 bintang kuning, "dari 2.300+ ulasan", lalu 3 bar distribusi (5 = 94%, 4 = 5%, 3 = 1%), tombol biru "Jemput cucian" (ikon truk), dan teks kecil "Ulasan asli dari pelanggan terverifikasi".
- Kanan: area dinding setinggi halaman berisi 3 kolom kartu (lebar kartu 180 px, jarak 14 px). Atas dan bawah area ini memudar halus pakai mask-image linear-gradient (70 px).
- Tiap kartu putih sudut 18 px: avatar bulat berwarna dengan inisial, nama tebal, kota kecil di bawahnya, 5 bintang, lalu kutipan 2 sampai 3 baris pendek. Isi 12 ulasan, contoh: "Bu Sari, Bekasi: Kemeja kantor rapi, wangi, besok pagi sudah sampai.", "Andi P., Depok: Antar-jemputnya selalu tepat waktu.", "Mbak Yuni, Jakarta Timur: Noda kopi di blus putih hilang total!", "Pak Hendra, Bekasi: Langganan 2 tahun, belum pernah ada baju yang hilang.", "Rara, Cikarang: Selimut tebal jadi lembut lagi.", "Bu Lina, Bekasi: Setrikaannya rapi, dilipat per jenis, gampang disimpan.", "Fajar, Tambun: Harga per kilo jelas, nggak ada biaya tambahan.", "Dewi A., Bekasi: Adminnya ramah, balasnya cepat.", "Kak Mira, Jatiasih: Gorden ruang tamu bersih dan wangi.", "Rizky, Bekasi: Sepatu putihku balik kinclong.", "Bu Ningsih, Bekasi: Pesan pagi, sore sudah diantar. Kilat beneran!", "Yoga, Jakarta Timur: Packing-nya rapi, plastiknya tebal."

Animasi:
- Tiap kolom berisi 4 kartu, lalu 4 kartu yang sama diulang sekali lagi di bawahnya (jadi isinya 2 set).
- Kolom 1 dan 3 bergerak ke atas, kolom 2 ke bawah, kecepatan konstan (ease: "none"). Dalam 6 detik tiap kolom bergeser tepat sejauh tinggi 1 set (tinggi 4 kartu + jaraknya), lalu timeline diulang (repeat: -1). Karena geserannya pas 1 set, sambungannya tidak kelihatan dan dindingnya terlihat jalan terus tanpa putus.
- Hitung tinggi set dari tinggi kartu di JavaScript (jangan pakai angka tebakan), supaya kalau ulasannya diganti loop-nya tetap mulus.
```

## 05 · Kartu balik 3D

**KARTU PRODUK** · cocok buat: Menu andalan, katalog produk, isi paket hampers.

```text
Bikin kartu menu yang miring 3D lalu berbalik nunjukin isi menunya, untuk landing page warung mie. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat oranye muda di tengah):
- Navbar: logo bulat merah dengan ikon api + "Mie Pedas Mas Bayu", menu "Menu  Lokasi  Kemitraan".
- Judul tengah: label kecil merah "MENU ANDALAN" lalu "Pilih level pedasmu".
- Tiga kartu berjajar. Kiri dan kanan kartu biasa (220 x 336 px): foto di atas, nama, deskripsi, ikon api level pedas, harga merah, tombol "+" gelap. Isi: "Nasi Goreng Kampung · Telur ceplok + kerupuk · Rp 22.000" dan "Es Teh Lemon · Segar, gula bisa diatur · Rp 8.000".
- Kartu tengah lebih besar (250 x 392 px), di dalam wadah dengan perspective 1100px dan transform-style: preserve-3d, dua sisi dengan backface-visibility: hidden:
  - Depan: foto mie, badge merah "FAVORIT", "Mie Kuah Pedas", "Telur ajitama · level 1–5", 4 dari 5 ikon api menyala, "Rp 25.000", tombol "+", plus lapisan kilau putih diagonal (glare).
  - Belakang (rotateY 180°, gradien merah tua ke hampir hitam, teks putih): "ISI SEMANGKUK", "Mie Kuah Pedas", daftar dengan ikon centang hijau: "Mie kenyal buatan sendiri", "Telur ajitama", "Kuah cabai rawit segar", "Sawi + daun bawang", chip "Siap dalam 10 menit", dan tombol putih "+ Tambah ke pesanan".
- Bayangan elips lembut di bawah kartu tengah.
- Pakai kotak gradien sebagai pengganti foto (nanti aku ganti foto menuku).

Animasi kartu tengah (satu timeline GSAP, repeat: -1, total 6 detik). rotationY berjalan dari -12° sampai 348° (pas satu putaran penuh) supaya loop-nya mulus:
1. 0–1,25 dtk: kartu miring pelan dari rotationY -12° / rotationX 7° ke 14° / -5° (sine.inOut), kilau di depan ikut bergeser.
2. 1,35 dtk: kartu berbalik ke 180° (0,85 dtk, power3.inOut), sambil terangkat 14 px dan membesar 1,05 lalu turun lagi; bayangan di bawahnya mengecil lalu kembali.
3. 2,25–4,05 dtk: sisi belakang goyang halus sampai 190° lalu kembali ke 180°. 3,05 dtk: tombol "Tambah ke pesanan" ditekan (efek riak + mengecil 0,95 lalu memantul), 3,2 dtk berubah hijau "✓ Masuk pesanan".
4. 4,1 dtk: kartu berbalik lagi ke depan sampai 348° dan rotationX 7° (sama dengan posisi awal), terangkat lalu turun seperti langkah 2. Label tombol belakang kembali normal saat sudah tidak terlihat.
5. Kartu kiri dan kanan mengambang naik-turun 7 px, dua kali per loop.
```

## 06 · Tab menu

**MENU** · cocok buat: Kafe, resto, dan katalog yang produknya banyak.

```text
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
```

## 07 · Masuk keranjang

**KERANJANG** · cocok buat: Toko online yang jual banyak produk satuan.

```text
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
```

## 08 · Gosok voucher

**VOUCHER** · cocok buat: Promo pembukaan, ulang tahun toko, pembeli pertama.

```text
Bikin kartu voucher "gosok dan dapat diskon": lapisan perak di atas voucher terhapus mengikuti koin yang bergerak zig-zag, lalu kode diskonnya muncul. Satu file HTML, pakai HTML + CSS + SVG + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan (lebar sekitar 930 px, latar putih dengan semburat jingga muda di kanan atas):
- Navbar: logo bulat jingga-cokelat dengan ikon api + "Martabak Bang Udin", menu "Menu  Cabang  Promo".
- Kolom kiri: label "PROMO CABANG BARU · MARGONDA" dengan ikon tiket, judul "Gosok kartunya," / "dapat diskonnya." (baris kedua jingga), paragraf "Berlaku untuk pesanan online cabang Margonda. Satu kode untuk satu pembeli.", 3 langkah bernomor (lingkaran krem): "Gosok kartu di sebelah kanan", "Salin kode diskonnya", "Pakai saat checkout", dan catatan kecil "S&K berlaku · promo sampai 31 Desember".
- Kolom kanan: kartu voucher 420 x 262 px, sudut 24 px, gradien krem ke jingga muda, bingkai dalam garis putus-putus. Isinya (rata tengah): "SELAMAT! KAMU DAPAT", "DISKON 20%" (besar, jingga tua), kotak putih berisi kode "UDIN20" (huruf berjarak lebar), dan "min. belanja Rp 50.000".
- Di atas voucher ada lapisan SVG perak (gradien abu-abu perak + garis-garis diagonal tipis) dengan teks "GOSOK DI SINI", ikon tangan, dan "dapatkan diskon kejutan".
- Lapisan perak memakai <mask>: persegi putih + satu path zig-zag hitam (8 titik dari kiri ke kanan bergantian, stroke 62 px, ujung bulat). Bagian yang kena path hitam jadi transparan.
- Koin emas bulat 54 px bertuliskan "Rp".
- Di bawah voucher: tombol gelap "Salin kode" (ikon salin) dan tombol garis "Pakai sekarang →", lalu chip hijau "✓ Kode UDIN20 disalin" yang awalnya tersembunyi.

Animasi (satu timeline GSAP, repeat: -1, total 6 detik):
1. 0,15 dtk: koin masuk dari kiri bawah ke titik awal zig-zag; teks "GOSOK DI SINI" memudar.
2. 0,45 sampai 2,35 dtk: stroke-dashoffset path di mask turun dari panjang total ke 0 (ease "none"), dan koin bergerak di sepanjang titik zig-zag yang sama dengan kecepatan yang sama (durasi tiap segmen sebanding panjangnya) sambil sedikit bergoyang, jadi perak terlihat tergosok koin.
3. Setelah zig-zag selesai: koin hilang dan sisa lapisan perak memudar (0,35 dtk) sehingga voucher terlihat bersih.
4. 3,0 dtk: tombol "Salin kode" ditekan (riak + memantul), 3,15 dtk chip "Kode UDIN20 disalin" muncul, 4,55 dtk hilang. Kalau tombolnya diklik beneran, salin "UDIN20" ke clipboard.
5. 4,9 dtk: reset mask (path kembali tertutup) selagi lapisan perak masih transparan, lalu 5,0 dtk lapisan perak muncul lagi pelan-pelan dan teks "GOSOK DI SINI" kembali. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
```

## 09 · Paket unggulan

**PAKET HARGA** · cocok buat: Jasa dengan beberapa pilihan paket harga.

```text
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
```

## 10 · Form bertahap

**FORM PESANAN** · cocok buat: Kue custom, katering, jasa yang butuh detail pesanan.

```text
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
```

## 11 · Popup diskon

**POPUP** · cocok buat: Kumpulin nomor WhatsApp calon pembeli.

```text
Bikin pop-up diskon pembeli pertama yang muncul halus (latar meredup dan blur) di landing page toko bunga. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan halaman (lebar sekitar 930 px, latar putih dengan semburat pink muda):
- Navbar: logo bulat pink dengan ikon bunga + "Bunga Kirana", menu "Buket  Papan-bunga  Kontak", ikon tas belanja.
- Hero kiri: label "FLORIST · DIANTAR HARI INI" (ikon truk), judul "Buket segar," / "sampai hari ini juga." (baris kedua pink tua), paragraf "Pesan sebelum jam 14.00, diantar ke seluruh Kota Malang.", "mulai Rp 175.000", tombol pink "Pesan buket" dan tombol garis "Lihat katalog". Hero kanan: foto buket sudut membulat 28 px (pakai kotak gradien pink sebagai pengganti foto).
- Lapisan gelap di atas halaman: rgba(40,12,24,.46).
- Pop-up (580 x 344 px, putih, sudut 26 px, bayangan besar): kiri strip foto 196 px; kanan: tombol × bulat, "KHUSUS PEMBELI BARU", "Diskon 15%" (besar, pink tua), "untuk pesanan pertamamu", "Tulis nomor WhatsApp-mu, kode diskonnya langsung kami kirim.", kolom input dengan ikon telepon dan placeholder "Nomor WhatsApp", tombol pink "Kirim kode diskon" (ikon kirim), dan link kecil "Nggak dulu, makasih".
- Toast hijau di atas halaman (awalnya tersembunyi): "✓ Kode KIRANA15 sudah dikirim ke WhatsApp-mu".

Animasi (satu timeline GSAP, repeat: -1, total 6 detik, semua otomatis seperti demo):
1. 0,45 dtk: lapisan gelap muncul (0,45 dtk) dan halaman di belakangnya blur 0 → 3 px.
2. 0,6 dtk: pop-up naik 46 px sambil membesar 0,94 → 1 dan muncul (0,6 dtk, power3.out).
3. 1,4–2,2 dtk: nomor "0812 3456 7890" terketik huruf per huruf (placeholder hilang, ada kursor).
4. 2,55 dtk: tombol ditekan (riak + memantul), lalu berubah hijau "✓ Kode terkirim ke WhatsApp".
5. 3,85 dtk: pop-up turun 24 px dan hilang; 4,0 dtk lapisan gelap dan blur hilang. 4,25 dtk toast hijau turun masuk dari atas (back.out), 5,3 dtk hilang.
6. Input dan tombol di-reset saat pop-up sudah tertutup. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
Catatan: di web asli, tampilkan pop-up ini sekali saja per pengunjung (simpan tanda di localStorage) dan biarkan tombol × / "Nggak dulu" menutupnya.
```

## 12 · Tombol nempel

**TOMBOL MELEKAT** · cocok buat: Landing page panjang yang dibuka lewat HP.

```text
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
```

## 13 · FAQ buka-tutup

**FAQ** · cocok buat: Jawab keraguan pembeli sebelum mereka nge-chat.

```text
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
```

## 14 · Peta kirim

**PENGIRIMAN** · cocok buat: Toko online yang kirim ke luar kota & luar pulau.

```text
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
```

## 15 · Menu HP

**NAVIGASI HP** · cocok buat: Web yang paling sering dibuka pembeli lewat HP.

```text
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
```

---
Mau dibantu pasang di web bisnismu? Balas DM ini aja. Simpan file ini biar gampang dicari lagi.

**Freddie Kashawan · AI PRENEUR**
