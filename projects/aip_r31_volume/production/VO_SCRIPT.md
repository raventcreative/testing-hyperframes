# R31 · Aturan volume: banyakin percobaan — AIpreneur (tema PUTIH) · 57,0 dtk
Referensi: `projects/aip_remake_batch8/refs/ref1.mp4` (52,7 dtk, kreator lain, animasi stick figure oranye di latar ungu: lempar bola
ke keranjang, lamaran kerja, cold call, grid konten, tangga hari). Format kita: dunia voxel 3D putih + maskot 3D klien (host) + robot
AIpreneur (co-host).

## VO (ElevenLabs, Dakocan `plgKUYgnlZ1DCNh54DwJ`, eleven_v4, stab 0,41 / sim 0,75 / style 0, auto tags) — SATU take utuh
File: `assets/audio/vo.mp3` (55,56 dtk, take 4 = `production/takes/take4_FINAL.mp3`), mulai di 0,3 dtk video. Tidak dipotong,
tidak di-pad, tidak di-stretch. Semua timing scene mengikuti alignment take ini (`production/words.json`).
1. Posting tiga kali, sepi, langsung nyerah?
2. Masalahnya bukan bakat. Masalahnya jumlah percobaan.
3. Aturan yang dipopulerkan Alex Hormozi: bikin volume sebanyak itu, sampai nggak masuk akal kalau hasilnya nggak datang.
4. Konten: jangan berhenti di lima video. Bikin seratus, biar peluangnya makin besar.
5. Jualan: banyak yang follow-up sekali, lalu berhenti. Follow-up semua yang pernah nanya, tetap sopan.
6. Iklan: jangan taruh semua budget di satu materi. Uji sepuluh variasi, biar data yang milih pemenangnya.
7. Olahraga: tiga puluh hari berturut-turut, bukan cuma pas semangat.
8. Tiap percobaan dicatat, yang berikutnya diperbaiki.
9. Di sini AI bikin volume jadi murah: draf naskah, variasi iklan, pesan follow-up, keluar sekali duduk.
10. Tapi yang klik posting dan yang kirim chat, tetap kamu.
11. Anggap tiap hari satu anak tangga. Isi dengan percobaan, dan targetmu makin dekat.
12. Komen volume, aku kirim tracker tiga puluh hari dan prompt-nya lewat DM.

Riwayat take: take1 (59 dtk, terlalu panjang) → take2 (57,4) → take3 (55,4; "prinsip" salah dengar di whisper small DAN medium →
diganti "Aturan") → take4 = final. Listen-check take4: small 6 beda / medium 4 beda, semuanya ejaan saja (hormozzi/hormuzi,
content, draft, promnya).

## ATM: what we changed
- **Amati**: ide "volume yang begitu besar sampai nggak masuk akal kalau gagal" + contoh-contoh sehari-hari + tangga hari ke tujuan.
- **Tiru**: hanya kerangkanya (dipopulerkan Alex Hormozi — diatribusikan, tanpa tanda kutip terjemahan) dan pola "contoh → contoh → contoh".
- **Modifikasi**: hook sendiri (posting 3x lalu nyerah), urutan & contoh sendiri untuk pebisnis/kreator Indonesia (konten 5→100,
  follow-up semua calon pembeli dengan sopan, uji 10 variasi iklan, olahraga 30 hari), tambahan "catat → perbaiki", sudut AI
  (AI bikin volume murah: draf naskah, variasi iklan, pesan follow-up — tapi yang klik posting tetap kamu), CTA sendiri.
  Tidak ada stick figure, keranjang, lamaran kerja, cold call, palet oranye-ungu. Metafora visual sendiri: meriam kubus menembak
  pulau target (3 meleset → bendera putih → 100 percobaan, kubus yang kena menempel di target), dinding 100 konten, hub toko + 6
  rumah dengan gelembung follow-up, 10 billboard + data memilih pemenang, grid 30 hari → batang per hari, meja AI dengan layar chat,
  tombol POSTING/KIRIM, tangga spiral 30 hari ke target yang sama dengan hook (callback: kali ini kena).
- Klaim: tidak ada hasil yang dikarang. Semua angka hitungan di layar ditandai "ilustrasi" (kena, balasan, data iklan).
  Sumber kerangka: Alex Hormozi, *The Game* podcast ("…it becomes unreasonable that you won't succeed", tema "volume") —
  diverifikasi lewat transkrip/ringkasan episode (mis. podscripts.co "The Reason You're Not Successful", medium.com/hormozi-transcripts).

## Teknik (skill baru 2026-11-20 — teknik saja, bukan produk/brief orang lain)
1. **throughline-explainer** — satu objek through-line: kubus cyan "satu percobaan" (peluru meriam → tile konten → gelembung →
   koin budget → hari → kartu draf → naik tangga spiral → mengenai bullseye di CTA, callback ke hook yang meleset).
2. **beat-promo-film** — grid ketukan dari music bed (108 BPM, seed 11): 3 tembakan hook di ketukan 1-2-3, perpindahan scene di
   ketukan (7,22 · 13,33/13,89 · 18,89 · 25,0 · 30,56 · 37,78 · 44,44 · 51,67); motion blur 3-subframe (t ± 1/90 dtk) di semua
   gerakan cepat (snap, flight, whip, orbit, dive, vertigo).
3. **html-demo** — layar monitor di dunia voxel digambar live sebagai jendela chat View(t): prompt diketik ~42 karakter/dtk,
   kursor datang lebih awal, klik "Kirim", status "AI sedang menulis…", hasil 10/10 muncul berurutan.
4. **product-launch-film** — pegas closed-form (overshoot kecil) untuk semua kemunculan; shared element: tombol POSTING → kubus
   lepas dari tombol → naik tangga.
5. **business-explainer-30s** — masalah (3x nyerah) → apa (aturan volume) → langkah (4 contoh) → bukti/peran AI → nama (CTA).
Transisi (beda tiap beat): zoom-out reveal · snap cut · island-hop flight · whip tilt · orbit 180° · dive-into-object + flash ·
iris lewat wajah robot (portal layar robot) · dolly-zoom (vertigo) · crane spiral mengikuti kubus.
Resep maskot/robot: guide object (kubus), robot-screen portal (iris), button → page, process fill (stack draf), push kamera pelan.

## Revisi 2026-11-21 (koordinator / klien)
- **Rekaman layar asli** (aturan klien): beat KONTEN (13,9–18,75 dtk) sekarang memutar feed Instagram asli @aipreneur_academy
  (brand/rec/ig_aipreneur_academy_profile.mp4) di layar besar dalam dunia voxel, menggantikan dinding konten tiruan. Crop hanya kolom IG
  tengah (tanpa tab/address bar/bookmark/sidebar/widget Messages); header profil + baris pertama 5 postingan disorot cyan di
  "lima video", lalu grid di-scroll ±4x (kecepatan scroll dihaluskan dari offset yang diukur) dan zoom tepat ke 3 kolom tengah di
  "peluangnya makin besar". Tag "feed asli @aipreneur_academy". Frame turunan di assets/rec/ (gitignored, repo publik).
- **Background hanya plate brand**: WebGL transparan, tanpa langit gradien/awan voxel; di bawah canvas `assets/brand/bg_light_1080x1920.png`
  (brand/bg-light.png cover-fit). Fog tipis warna plate (#eef3fb). Iris transisi putih.
- **SFX lebih terasa** (permintaan klien): whoosh di setiap transisi, impact di cut/blok kena target/tombol, riser lembut sebelum reveal,
  pop/klik UI + klik caption-in, tick counter, swipe di scroll IG; level −8 dB (hit besar) / −11 dB / −15 dB di bawah puncak VO,
  tanpa sidechain/kompresor di SFX, tidak ada transient di onset kata (dipindah/di-drop otomatis).

## Teknis
Three.js (`vendor/vx.js` + `vendor/vxlib.js`, render deterministik per frame lewat hf-seek), maskot klien (`vendor/mascot3d.js` +
`vendor/mascot_host.js`, lip-sync dari VO), robot AIpreneur (`vendor/robot3d.js` + `vendor/robot_host.js`, port dari R24),
overlay HTML/GSAP (`tools/index.src.html` → `tools/build.py`), SFX `tools/sfx.py` (set vo_safe; event yang jatuh di onset kata
dipindah/di-drop), mix akhir `tools/remix_audio.sh` (VO utuh + SFX level tetap + bed di-duck, loudnorm 2-pass −14 LUFS).
Cek VO: `tools/vo_check.py <file> small|medium` (diff kata per kata terhadap vo_lines.txt).
