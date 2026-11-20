# VO — R29 · Bisnis itu lempar dadu: pilih dadu, pilih nampan · tema WHITE · VO 162,8 dtk (video 164,4 dtk, mulai 0,3 dtk)
Referensi: batch 7 · `projects/aip_remake_batch7/refs/ref3.mp4` (161,6 dtk, bahasa Inggris, kreator lain: talking head + papan
tulis digital berisi foto dadu & nampan, garis ungu, ikon target "shiny object syndrome", tangan melempar dadu ke nampan navy).
Klien: **jangan dipotong** → panjang kita 164,4 dtk (+1,7 %).

## ATM: what we changed
**Amati** — ide berguna: peluang dapat 6 naik kalau lemparan ditambah (1× / 10× / 100×), tapi di dunia nyata banyak hal bikin
lemparan sia-sia (cara kegedean/kekecilan, ide salah = dadu tanpa 6, terlalu banyak yang belum diketahui, pasar terlalu kecil,
masalah yang tidak ada, jatah lemparan sedikit); dua cara main (ganti-ganti dadu & nampan vs kunci variabel, ubah lemparan);
pilih ide yang tepat + perbaiki pendekatan, tetap di satu pasar yang cukup besar & tumbuh; ganti ide setelah meleset sekali =
shiny object syndrome; pebisnis berhasil memilih pasar & ide dengan hati-hati lalu memperbaiki produk/penawaran/harga/distribusi;
penutup "dadu = ide + pendekatan, nampan = pasar, ganti lemparan sebelum ganti nampan".
**Tiru** — SEMUA ide di atas dipertahankan (permintaan brief), plus metafora inti dadu/nampan (itu inti materinya).
**Modifikasi**:
1. **Hook sendiri** — angka peluang dibuka sebagai kartu statistik yang menghitung naik (16,7 % → 83,8 % → 99,99999 %), dadu 3D
   jatuh ke nampan kita; pertanyaan "asal nyoba terus, semua pasti sukses?" lalu "di atas kertas iya, di dunia nyata beda cerita".
2. **Urutan & metafora sendiri** — kita definisikan meja (dadu = ide + cara jalanin, nampan = pasar) DI DEPAN, lalu 6 masalah
   bernomor (chip MASALAH n/6) dengan alat visual berbeda: dadu raksasa "ruko 3 lantai" menghantam tepi nampan vs dadu mini
   "grup keluarga 1× sebulan"; dadu yang **dibuka jadi jaring** (1-2-3-4-5-5, slot "6?" kosong); penghitung 1.000 lemparan
   "angka 6: 0×"; **kubus tanda tanya** yang jatuh per kata lalu berubah jadi dadu → 5 dadu harus 6 semua (matematika kita
   sendiri: (1/6)^5 = 1 : 7.776 ≈ 0,013 %, tidak ada di referensi); nampan **menyusut**; nampan **tanpa lantai** (lantai jatuh,
   lubang gelap); jatah lemparan = 3 dadu "nyawa" + bar modal/waktu/tenaga. Contoh UMKM Indonesia (semua berlabel contoh/
   ilustrasi): kopi susu → langsung sewa ruko 3 lantai; nawarin ke grup keluarga sebulan sekali; servis mesin ketik di satu
   kecamatan; aplikasi antre online untuk warteg yang tidak pernah antre.
3. **Sudut praktisi** — tidak ada klaim hasil pribadi. Nilai tambah kita: bagian AI (ringkas ulasan pembeli, cari keluhan
   berulang, bikin beberapa versi penawaran untuk diuji) — kemampuan umum model AI, tanpa nama produk/angka hasil.
4. **Nilai untuk penonton Indonesia** — contoh lokal di atas, kalimat penutup sendiri ("ganti lemparanmu, sebelum ganti nampan"
   diucapkan dengan kata kita; di layar "Ganti lemparan dulu, baru (kalau perlu) ganti nampan"), lembar kerja di DM.
5. **CTA sendiri** — "Komen dadu, aku kirim lewat DM." (kata kunci DADU; dikirim huruf kecil supaya tidak dieja, caption DADU).
- **Dibuang dari referensi**: wajah/rekaman kreator, papan tulis + foto dadu/nampan mereka, garis ungu, ikon target mereka, angka
  "16 %" yang dibulatkan ke bawah (kita pakai 16,7 %), "more shots" sebagai frasa. Tidak ada >3 kata berurutan dari skrip
  referensi (referensi berbahasa Inggris; satu-satunya frasa Inggris yang sama adalah istilah "shiny object syndrome").

## Fakta yang dicek (2026-11-20)
- **Matematika (dihitung ulang di Python)**: 1 lempar P(6) = 1/6 = 16,67 % → "16,7 %"; 10 lempar 1 − (5/6)^10 = 0,83849 →
  "83,8 %"; 100 lempar 1 − (5/6)^100 = 0,9999999879 → "99,99999 %" (dipotong, bukan dibulatkan ke atas; VO: "hampir 100 %");
  5 dadu harus 6 semua (1/6)^5 = 1/7.776 = 0,0129 % → VO "nggak sampai 0,02 %", layar "1 : 7.776 · 0,013 %".
- **Shiny object syndrome** — istilah umum (bukan diagnosis klinis): kecenderungan mengejar ide/peluang baru dan meninggalkan
  yang sedang dikerjakan. Sumber: [Wikipedia](https://en.wikipedia.org/wiki/Shiny_object_syndrome),
  [Entrepreneur.com](https://entrepreneur.com/article/288370), [EOS Worldwide](https://www.eosworldwide.com/blog/shiny-object-syndrome-what-it-is-and-how-to-overcome-it).
- AI: hanya kemampuan umum (meringkas teks, mengelompokkan keluhan, menulis variasi penawaran); angka "120 ulasan" dan kutipan
  keluhan di kartu = contoh, berlabel "AI BANTU · CONTOH TUGAS". Tidak ada janji hasil/penghasilan.
- Tidak ada logo merek di reel (topik tanpa merek); "logo topik" di cover = dadu 3D buatan kita sendiri.

## Resep (mascot_robot_recipes.md) yang dipakai — 6
1. **Accent-dot journey (guide object)** — titik #294b77 = pip dari sisi 6 dadu: terangkat dari dadu ke kartu peluang (jadi ujung
   meter), menggambar grafik "pelajaran tiap lempar" (s30), lalu dari pip dadu 6 di s40 membanjiri layar (flood) jadi latar
   kartu AI. (technique_bank: ultimaxbt-bbebf5, rossaxbt-94583b)
2. **Spinning pain list** — daftar masalah berputar cepat (ide salah, pasar sempit, modal habis, …) lalu melambat dan berhenti di
   "DUNIA NYATA: BEDA" pada "beda cerita". (jake11moran-f60e35)
3. **Process fill** — produk / penawaran / harga / cara jualan masing-masing mengalir ke tangki "PELUANG DAPAT 6" (0/4 → 4/4),
   lalu lemparan berikutnya dapat 6. (ror-fly-9950f1)
4. **Chaos → control → clarity → brand** — cara A (dadu & nampan gonta-ganti, hasil acak) → cara B (gembok di dadu & nampan,
   busur lemparan menyempit) → tiga aturan + dadu 6 → kartu DM + logo AI PRENEUR. (daniel-haida-8691d4)
5. **Camera push 1.0 → 1.04** — kamera dunia 3D mendorong pelan per grup shot, satu gerak eased antar grup, tidak pernah zoom
   balik. (technique_bank Camera)
6. **Small-overshoot springs + beat-locked changes** — nampan/dadu/kartu masuk dengan pegas overshoot kecil; setiap kata kunci
   memicu perubahan (45 beat, rata-rata 3,6 dtk; wipe garis, iris, flip, blur, flood berganti-ganti).
(+ VO ducking dari `render_aip.sh`: musik bed di-duck di bawah VO, −14 LUFS.)

## Naskah (ElevenLabs, voice Dakocan, eleven_v4, auto tags; `production/vo_lines.txt`)
Lempar satu dadu sekali, peluang dapat angka enam cuma enam belas koma tujuh persen.
Lempar sepuluh kali, peluangnya naik jadi delapan puluh tiga koma delapan persen.
Lempar seratus kali? Hampir seratus persen.
Berarti asal nyoba terus, semua orang pasti bisa sukses bisnis?
Di atas kertas, iya. Di dunia nyata, beda cerita.
Lihat meja ini. Dadunya itu ide kamu, plus cara kamu jalaninnya. Nampannya itu pasar.
Masalah pertama: caranya kegedean, atau kekecilan.
Baru mau jualan kopi susu, langsung sewa ruko tiga lantai. Atau sebaliknya, cuma nawarin ke grup keluarga, sebulan sekali.
Masalah kedua: idenya salah. Dadunya memang nggak punya angka enam. Dilempar seribu kali pun, enamnya nggak bakal keluar.
Masalah ketiga: terlalu banyak yang belum kamu tahu. Produk baru, pasar baru, harga baru, cara jualan baru, semuanya sekaligus.
Tiap hal yang belum pasti itu kayak satu dadu tambahan yang harus ikut dapat enam. Lima dadu sekaligus? Peluangnya nggak sampai nol koma nol dua persen.
Masalah keempat: nampannya kekecilan. Contohnya servis mesin ketik, cuma di satu kecamatan. Pasarnya sempit, dadunya mental keluar.
Masalah kelima: nampan tanpa lantai. Kamu jual solusi buat masalah yang nggak dirasain siapa-siapa, kayak aplikasi antre online buat warteg yang nggak pernah antre. Dadunya lolos lewat.
Masalah keenam, yang paling berat: lemparanmu terbatas. Modal, waktu, dan tenaga cuma cukup buat beberapa kali coba.
Terus gimana? Ada dua cara main.
Cara pertama: tiap gagal, ganti dadu dan ganti nampan. Hasilnya acak, dan kamu hampir nggak belajar apa-apa.
Cara kedua: kunci variabelnya. Dadu yang sama, nampan yang sama, yang kamu ubah cuma cara lemparnya. Tiap lemparan ngasih pelajaran, jadi peluangmu naik.
Jadi, pilih ide yang tepat, terus perbaiki pendekatannya. Dan tetap di satu pasar, idealnya yang cukup besar dan lagi tumbuh.
Kesalahan paling umum? Ganti ide begitu meleset sekali.
Namanya shiny object syndrome. Kamu udah punya target, terus muncul sesuatu yang kinclong, dan kamu banting setir ke sana. Semuanya mulai dari nol lagi.
Pebisnis yang berhasil biasanya main kebalikannya.
Mereka milih pasar dengan hati-hati, diteliti dulu. Milih ide juga hati-hati.
Habis itu yang diutak-atik: produknya, penawarannya, harganya, sama cara jualannya. Sampai dapat angka enam.
Di sini AI bisa bantu: ringkas ulasan pembeli, cari keluhan yang berulang, dan bikin beberapa versi penawaran buat kamu uji.
Jadi, bisnis itu bukan soal banyak-banyakan lemparan.
Pilih dadu yang tepat. Pilih nampan yang tepat. Dan ganti lemparanmu, sebelum ganti nampan.
Mau lembar kerja buat milih dadu dan nampanmu, plus perintah AI siap pakai?
Komen dadu, aku kirim lewat DM.

## Take & cek dengar (faster-whisper small + medium, id)
- **Take 1** (162,8 dtk): kata yang salah di KEDUA model → "pakai riset" ("reset"), "lempar sebanyak-banyaknya" ("lempan"),
  "prompt" ("prom") → diganti: "diteliti dulu", "banyak-banyakan lemparan", "perintah AI siap pakai".
- **Take 2** (teks baru): kedua model salah di "sewa ruko" (sewarukot / sewarung ke), "idenya" (IB-nya) dan "kebalikannya"
  (kebarikannya) — baris-baris itu benar di take 1 → **VO final = take 2 + baris 8, 9, 21 dari take 1** (`tools/splice_vo.py`,
  potongan di tengah jeda antarbaris, level per baris −14,7 … −17,0 dB, sama). Cek ulang potongan sambungan: medium benar semua
  ("sewa ruko tiga lantai", "ide nya salah", "pebisnis … kebalikannya"); small hanya "ideya" / "namanya" (medium benar).
- Sisa salah tulis small-saja (medium benar): kinclong/kincelong, nol/enol. "antre" ditulis "antri" (ejaan), "shiny object
  syndrome" benar di kedua model. Tag tidak ikut terbaca. Kredit terpakai ≈ 3 × 2,7 k karakter.
