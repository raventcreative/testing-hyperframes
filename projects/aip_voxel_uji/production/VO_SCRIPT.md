# Uji gaya voxel 3D + maskot host — AIpreneur (tema PUTIH) · 18 dtk
Referensi gaya: video carousel "7 AI nolak CV kamu" (kreator lain, 56 dtk, diorama voxel oranye-navy, karakter anak ber-beanie).
Ini UJI COBA format (hook + 2 beat pertama), bukan video penuh.

## VO (ElevenLabs, Dakocan, eleven_v4, auto tags) — 16,85 dtk, mulai di 0,3 dtk
1. Kirim CV ke lima puluh perusahaan, balasannya cuma sunyi?
2. Nggak ada yang jelasin salahnya di mana.
3. Coba bikin tujuh AI jadi panel penilai CV kamu, biar alasannya kebongkar duluan.
4. Penilai pertama, sistem ATS: dia nyaring CV pakai kata kunci, sebelum manusia sempat baca.

## ATM: what we changed
- **Amati**: diorama voxel 3D, chip counter, judul per bagian, subtitle per kata, ide "panel 7 AI menilai CV".
- **Tiru**: hanya mekanismenya (dunia voxel + counter + bagian bernomor).
- **Modifikasi**: hook & kalimat sendiri (tidak ada >3 kata berurutan dari skrip referensi); semua karakter/aset buatan kita
  (pelamar berkacamata + hoodie biru, 7 robot AI warna peran, HR berkuncir) — bukan anak beanie mereka; palet putih–navy–cyan
  AIpreneur (bukan oranye); struktur visual sendiri: kota diorama + amplop CV terbang, kotak surat kosong, "?" dari kubus,
  **zoom out ke dunia mini melayang lalu maskot AIpreneur masuk jadi host** (permintaan klien), tribun juri 3 tingkat,
  match-cut menyelam ke CV → scanner ATS dengan conveyor, tag kata kunci, pintu jebakan ke kotak TOLAK sebelum HR membaca.
- Klaim dijaga: ATS digambarkan sebagai penyaring kata kunci (umum dipakai perusahaan), contoh kata kunci = ilustrasi.

## Teknis
Three.js (vendor/vx.js, render deterministik per frame lewat hf-seek), maskot klien via runtime R-series (vendor/mascot3d.js +
vendor/mascot_host.js, lip-sync dari VO), overlay HTML/GSAP (tools/index.src.html → tools/build.py), SFX tools/sfx.py (set vo_safe repo).
