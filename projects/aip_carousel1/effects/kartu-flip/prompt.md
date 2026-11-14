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
