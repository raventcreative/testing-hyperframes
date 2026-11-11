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
