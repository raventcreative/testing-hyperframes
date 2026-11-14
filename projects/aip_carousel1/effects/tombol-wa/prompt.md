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
