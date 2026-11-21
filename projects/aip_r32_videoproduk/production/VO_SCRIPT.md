# R32 · Foto produk jadi video promo (contoh alur) · tema NAVY · voxel 3D + maskot host + robot co-host · 55,6 dtk (VO 53,7 dtk, mulai 0,3 dtk)
Referensi: `projects/aip_remake_batch8/refs/ref2.mp4` (52,1 dtk, kreator lain): tempel foto produk kosmetik ke AI → keluar video promo
dengan suara marketer. Tool-nya tidak disebut, brand kosmetiknya pihak ketiga → TIDAK ditampilkan sama sekali.

## VO (ElevenLabs, Dakocan, eleven_v4, auto tags `[playful] [excited]` + `[confident]` di CTA) — SATU take utuh (take 2), tanpa potong/pad/stretch
1. Cuma modal foto produk, AI bisa bikinin video promo, lengkap dengan suara marketer.
2. Ini contoh alurnya, cocok buat UMKM, online shop, sampai affiliator.
3. Satu. Foto produkmu di tempat terang: tampak depan, samping, dan detail kemasan.
4. Dua. Kirim fotonya ke asisten AI, minta dia nulis naskah dan susunan adegan, detik per detik.
5. Sertakan juga harga, ukuran, dan siapa target pembelinya.
6. Hook di awal, manfaat produk satu per satu, lalu ajakan beli lewat keranjang kuning.
7. Tiga. Naskah itu dibacakan suara AI, dengan gaya marketer yang lagi jualan.
8. Empat. Adegan, foto, dan suara dirender jadi video vertikal, siap diunggah.
9. Video yang lagi kamu tonton ini juga dibikin pakai alur yang mirip.
10. Tapi ingat, ini alat bantu produksi, bukan jaminan laku. Cek dulu klaim produkmu sebelum posting.
11. Komen promo, aku kirim prompt dan checklist foto produknya lewat DM.

Listen-check (faster-whisper small + medium): take 1 → "Claude" terdengar "cloud" dan "keranjang" → "ranjang" di KEDUA model, jadi
diganti ("ke asisten AI", "lewat keranjang kuning") dan seluruh take dibuat ulang (take 2). Take 2: medium bersih (hanya beda ejaan
"afiliator", "persatu", angka "3."/"4."); small salah dengar "Huk/alak/klien" (hanya satu model → dibiarkan sesuai aturan).
File take: `production/vo_takes/` (take1 + take2 + transkrip whisper).

## ATM: what we changed
- **Amati**: ide inti "foto produk → AI → video promo + suara marketer", sasaran UMKM / online shop / affiliator, ajakan keranjang kuning.
- **Tiru**: hanya ide inti + sasaran penonton.
- **Modifikasi**: hook, urutan, dan kalimat sendiri (tidak ada >3 kata berurutan dari referensi); referensi cuma pamer hasil, kita
  jelaskan ALUR yang jujur 4 langkah (foto → naskah/adegan dari asisten AI (Claude di layar) → suara AI → render) + info yang harus
  disertakan (harga, ukuran, target) + struktur naskah (hook → manfaat → ajakan) + peringatan "alat bantu, bukan jaminan laku, cek klaim";
  fakta autentik: reels ini sendiri dibuat dengan alur mirip (Claude nulis adegan, ElevenLabs suara, HyperFrames render).
  Produk ilustrasi tanpa merek (botol kopi susu, toples sambal, tube madu, semua berlabel CONTOH) — bukan kosmetik referensi.
  Harga/ukuran/target di layar = contoh. Tidak ada janji penjualan.

## Teknik yang dipakai (skill eksternal → teknik saja)
1. **Through-line object** (`throughline-explainer`): KARTU FOTO PRODUK (polaroid) lahir dari jepretan di hook, masuk ke kubus AI,
   jadi lampiran chat (match cut: foto terbang ke lensa → keluar sebagai thumbnail chat), jadi wajah blok HOOK di menara naskah,
   jadi bahan "FOTO" yang masuk mesin render, dan akhirnya jadi lampiran DM di CTA.
2. **html-demo View(t)**: jendela chat "Claude · CONTOH ALUR" digambar per frame di layar 3D dunia voxel — robot mengetik di holo
   keyboard, kursor scripted (datang lebih awal, tekan 0,15 dtk), status "mengetik…" → balasan baris per baris, timecode menyala
   "detik per detik", chip harga/ukuran/target muncul pada kata-nya.
3. **Shared-element transformations + closed-form springs** (`product-launch-film`): kubus AI membuka jadi layar promo; layar chat
   terbelah jadi pintu lift memperlihatkan menara naskah; mesin render mengeluarkan HP vertikal; semua pop pakai spring overshoot kecil.
4. **Business-explainer structure** (`business-explainer-30s`): masalah/hasil (hook) → untuk siapa → 4 langkah → bukti (video ini
   sendiri) → nama/CTA.
5. **Mascot+robot recipes**: robot = co-host (masuk melambai, mengetik prompt, layar wajahnya menampilkan bar suara dari envelope VO
   asli saat "suara AI", menggeleng di "bukan jaminan", tepuk tangan saat render selesai); process fill (3 bahan masuk mesin render);
   words-as-architecture (blok naskah ditumpuk jadi menara); camera push pelan tiap scene.
Transisi (semua beda): zoom-out reveal ke peta 4 pulau → pan ke 3 pulau audiens → island-hop flight → foto terbang ke lensa (match cut,
flash putih) → pintu lift (layar chat terbelah) → whip tilt vertikal → orbit 180° → dolly zoom (vertigo) → iris → shockwave tombol.

## Sumber / catatan kejujuran
- Alur produksi = cara reels AIpreneur ini dibuat (Claude menulis adegan HTML/GSAP, suara ElevenLabs voice Dakocan, render HyperFrames).
- Logo 3D (Claude, ElevenLabs, Instagram): Simple Icons 16.38.0 (CC0) — lihat production/asset_credits.json.
- Tidak menampilkan brand/kemasan asli mana pun; keranjang kuning = gerobak voxel kuning generik (bukan logo platform).
