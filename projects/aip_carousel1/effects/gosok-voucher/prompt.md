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
