---
tags: [motion, transisi, skill-bank, editorial, masterpajak, preview]
date: 2026-11-11
project: projects/motionlab_2026
---
# Motion Lab 01: transisi editorial-collage (preview MasterPajak AI, 15 detik)

**Status:** video coba-coba buat preview ke client MasterPajak AI. **Bukan template** buat video berikutnya. Robot 3D dari user juga cuma buat preview ini.

## Asal skill
- Referensi dari user: showreel "Premium Motion Graphics" bergaya editorial collage. Isinya kertas krem, serif italic tebal, aksen oranye, jam pasir, objek dipotong-potong, chip label, puzzle, "?" + barcode, dan sinar diagonal.
- Ide dan gerakannya dipelajari lalu digabung dengan kit navy kita (grid, zoom-through, iris). Bentuk visual referensinya nggak disalin.

## 6 transisi baru (semua di grid 120 BPM, cut di 2/4/6/8/10/12 s)
| # | Nama | Cara bikin (HyperFrames + GSAP) |
|---|---|---|
| T1 | Panel slide-over + parallax push | Scene berikutnya `x 1096→0` (power4.inOut 0,47 s), tepi kirinya strip aksen 16 px. Isi scene lama `x 0→-320` + shade 0→0,7 |
| T2 | Blinds | 6 strip vertikal 180 px warna bg scene berikutnya, ganjil dari atas dan genap dari bawah, stagger kecil dari tengah. Scene baru di-show pas strip nutup |
| T3 | Diagonal slice wipe | Kontainer luar 3200×4200 `rotation -24` digeser `d·(cos,sin)`. Kontainer dalam `rotation 24, x -d` biar isinya tetap lurus. Tepi luar diberi stripe aksen 40 px + garis 8 px. Cuma tween transform, aman di render |
| T4 | Band sweep bergantian | 6 band horizontal 320 px masuk kiri/kanan selang-seling (stagger 0,03), satu band bawa marquee tagline |
| T5 | Zoom-through + flash | Scene lama `scale 1→9` (power4.in) + blur 10, flash putih 0,12 s, scene baru `scale 1,3→1` |
| T6 | Beam flood + circle iris | Disc pop di pojok, beam `scaleX 0→1` lalu `scaleY 1→16` membanjiri layar, end card dibuka `clip-path circle(0%→82%)` |

## Gerakan di dalam scene (bank efek)
- Huruf jatuh per karakter dalam mask (`.m` overflow hidden + padding .1em/.18em biar italic nggak kepotong).
- Chip highlight dibuka `clip-path inset(0 100% 0 0)→inset(0 0 0 0)` + `scale .7→1 back.out(2.6)`.
- **Teks dua warna di atas kolom terang**: dua salinan teks, yang navy di-clip ke kolom (`inset` ikut tumbuh bareng kolom). Ini pengganti `mix-blend-mode: difference` yang warnanya jadi khaki di navy.
- Objek dibelah 3 wedge (SVG, `svgOrigin` pusat) + leader line digambar (`strokeDashoffset`) + label.
- Angka diiris: dua salinan teks dengan `clip-path polygon` statis di garis miring, lalu stripe aksen dan kedua belahan geser berlawanan. **Origin stripe di ujung kiri, jadi `top` = y_tengah + 650·tan(sudut)**, kalau nggak, stripe meleset dari garis potong.
- Chaos jitter: `tl.set` acak (seeded) tiap 1/12 s ke huruf + chip.
- Puzzle snap: masuk 0,45 s ke celah 70 px, snap 0,13 s power4.in, ring + elastic bounce.
- "?" digambar sebagai path stroke membulat + titik kuning bounce. Barcode digambar per batang. Typewriter pakai `display` per karakter + caret.

## Gotcha
- Playwright `page.evaluate(() => tl.seek(t))` **nge-hang** karena mencoba serialisasi objek timeline. Selalu `return 1`. Begitu juga `waitForFunction` → pakai `!!(...)`.
- Brand MasterPajak AI (Design System v1.0): navy #212C5F, royal #26367A, kuning #FED111 (maks 1 sorotan/layar, teks gelap di kuning atau kuning di navy), awan #F6F7FB, Rubik + Public Sans tabular. Brief bilang hindari robot/3D/partikel/gradasi. Untuk preview ini robot tetap dipakai atas permintaan user.
- Angka contoh harus diberi label **ILUSTRASI DATA**. Tagline resmi: "Jualan jalan terus, pajaknya AI yang urus." CTA: "Coba kalkulator gratis" + "Link di bio".

## v2: robot 3D MasterPajak AI (model Tripo dari user, cuma buat preview ini)
**File:** `assets/robot/robot_mp.glb`, runtime `tools/robot/src/robot_mp.js` → `vendor/robot_mp.js`, koreografi `robot_perf.js`.

1. **Optimasi:** GLB Tripo (971 ribu vertex, Draco, 1 mesh, tanpa rig) → `mascot-bizman/tools/prep.mjs` rasio 0,06 → ±71 ribu vertex, tekstur webp 2K.
2. **Lengan nyatu sama badan** (khas Tripo), jadi kalau di-skin pasti sobek. Solusinya `tools/robot/cut_arms.py`:
   - Lengan + tangan dibuang lewat kapsul di sumbu lengan (r 0,047 + margin) dan bola tangan.
   - Pulau sisa dibuang.
   - Lubang di badan ditambal: 4 cincin konsentris yang agak menggembung, semua UV ke texel navy, tepinya diduplikasi biar nggak ada interpolasi lintas pulau UV (sebelumnya muncul garis putih).
3. **Lengan baru prosedural** ("rubber hose"):
   - Tabung di kurva bezier kuadrat bahu → siku → pergelangan, frame parallel transport, dibangun ulang tiap frame. Tambah bola bahu dan bola tangan putih, ukuran dan warna sama persis dengan aslinya.
   - Parameter: raise / fwd / bend / bendYaw.
   - **Jangan ubah bendYaw saat siku masih ketekuk**, nanti lengan bawah muter liar. Ganti bidang tekuk hanya waktu lengan lurus.
4. **Skin 3 tulang dihitung saat load:** body, head (pivot leher y 0,445, blend 0,43–0,468), antena (y > 0,85).
5. **Wajah prosedural di shader** (`onBeforeCompile`, SDF di ruang bind pose):
   - Layar = rounded box (0, 0,6425) ukuran 0,201 × 0,117, r 0,082.
   - Mata oval bisa blink/look, "^ ^" happy, "x x", mulut senyum/datar/"o", ditambah glow emisif dan roughness 0,16 biar kayak kaca.
6. **Gerak halus:**
   - Key per channel → filter pegas orde-2 (konvolusi impulse response, dt 1/90, gain DC 1), jadi tiap frame murni fungsi waktu dan aman di-seek.
   - Grup pegas: pos 1,5 Hz ζ .74 · body 1,7/.6 · head 2,3/.52 · arm 2,0/.56 · look 5,5/.92.
   - Di atasnya: hover, napas, kedip terjadwal, squash dari percepatan vertikal, dan antena = pegas lambat (2,4 Hz ζ .2) dikurangi gerak kepala.
   - **Hard cut** (saat robot hilang/pindah instan): pegas, antena, dan squash **nggak boleh lihat ke belakang melewati cut**. Kalau lihat, antena loncat 39°/frame.
7. **Audit kehalusan:** `ROBOT_STATE(t)` dicek per frame (step dan percepatan per sendi) sebelum render.
8. **Robot jadi host di semua scene:**
   - S1 muncul + garuk kepala, S2 panik "x x", S3 nunjuk koin + kaget.
   - S4 mikir lalu nunjuk "Perlu dicek", S5 selebrasi, T5 terbang ke kamera.
   - S6 nunjuk "?" + baca teks, S7 melambai lalu nunjuk CTA.

## v4: preview 38,5 detik dengan VO klien + lip-sync (`projects/masterpajak_preview30_2026`)
- **VO** (ElevenLabs, 36,7 s) → `fw_transcribe.py` (faster-whisper small, id) → `production/vo_words.json`. Tiap beat dikunci ke timestamp kata. Cut di 3,40 · 8,85 · 10,90 · 14,95 · 22,70 · 24,45 · 30,30.
- **Lip-sync** `tools/lipsync.py` → `lipsync.js` (60 fps):
  - OPEN = loudness yang dinormalisasi ke min/max bergulir 0,3 s. Audio ElevenLabs terkompres, jadi kalau pakai level absolut mulut nganga terus. Ada gerbang diam, attack 0,7 / release 0,35, dan bibir maju 2 frame dari suara.
  - WIDE = rasio energi 1,8–4,5 kHz / 0,25–1 kHz (vokal e/i lebar, o/u bulat).
  - Shader: mulut "bicara" berupa rounded box terisi dengan bagian dalam redup (kesan mulut terbuka). Waktu jeda balik ke mulut ekspresi (senyum dll).
  - Kepala ikut "beat" suku kata (pitch/roll kecil dari envelope).
- **Hologram:** wajib di dalam safe zone 120 px dari sisi dan nggak nabrak kepala (lebar ±420 px). Build 1,2 s, tampil ≥ 4 s (permintaan user).
- **Scene baru:**
  - Kartu file yang nongol pas kata "Pesanan, pencairan, mutasi bank".
  - Tag "− Potongan / − Retur" terserap ke kartu, lalu angka roll Rp10 jt → Rp9 jt.
  - Alur puzzle 3 keping JUALAN → PEMBUKUAN → PAJAK + garis jejak di "ditelusuri".
  - Transisi iris titik "?" ke chat.
  - Chat asisten AI (typing dots, bar omzet/biaya/laba) + kartu "Tim ahli Muamalah Pajak, pendampingan sesuai layanan" (label Simulasi alur / Ilustrasi percakapan).
- **Mix:** VO loudnorm −16, SFX ×0,32, amix tanpa normalize, lalu loudnorm −14 / TP −1,5.
- **Gotcha:**
  - Elemen yang belum masuk harus mulai cukup jauh di luar frame (offset ±900–1100 px). Offset 700 masih ngintip di pojok.
  - Elemen `#id` yang dikasih `top` wajib `position: absolute`.
