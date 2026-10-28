# Instruksi Render

Semua perintah dijalankan dari folder `03_SOURCE_PROJECT/`.

## Setup sekali
```bash
npm install
```
Playwright dan Chromium harus tersedia (lihat `SOFTWARE_REQUIREMENTS.md`).

## Render final (ketiga video)
```bash
bash render/render_all.sh out/final
```
Atau per video:
```bash
node render/render.mjs v1 --q final --out out/final
```
Output per video:
- `<NAMA>.mp4`: H.264, 1080×1080, 60 fps, background #00FF00, tanpa audio (`-an`)
- `<NAMA>_ALPHA.webm`: VP9 dengan alpha asli (background transparan)
- tambahkan `--prores` untuk master ProRes 4444 + alpha (`.mov`, file besar)

Waktu render di CPU 4 core tanpa GPU (WebGL SwiftShader): sekitar 1,5–7 dtk/frame. Frame diam ±1,5 dtk karena jumlah sub-frame motion blur adaptif. Di mesin dengan GPU, jauh lebih cepat.

## Draft cepat & QC
```bash
# draft: tanpa supersampling, 1 sub-frame
node render/render.mjs v3 --q draft --out out/draft
# still di waktu tertentu (PNG di atas hijau)
node render/render.mjs v3 --q final --stills 6.45,8.0,10.95 --out out/qc
# probe motion (tanpa render): lintasan layar tiap dokumen -> JSON -> grafik kecepatan
node render/render.mjs v3 --probe --out out/qc && python3 render/motion_plot.py out/qc/v3_motion.json out/qc/v3_motion.png
# contact sheet dari video
python3 render/contact_sheet.py sheet.jpg --video out/final/03_....mp4 --times 0,1,2,3
# verifikasi teknis delivery
python3 render/verify.py out/final/*.mp4
# rakit paket ZIP
bash render/build_package.sh
```

## Mengubah timing, desain, brand
| Mau mengubah | File |
|---|---|
| Warna, font, ukuran dokumen, fps, kualitas render | `src/tokens.js` |
| Timing tiap beat (objek `TIMING` di atas tiap file) | `src/shots/v1.js`, `v2.js`, `v3.js` |
| Kurva easing, spring, profil kecepatan orbit, float | `src/lib/motion.js` |
| Desain/teks/angka dokumen | `src/docs/receipt.js`, `statement.js`, `report.js` |
| Logo mark | `src/docs/draw.js → mark()` + `assets/brand/masterpajak-mark.svg` |
| Geometri kertas (tebal, bevel, sudut, zigzag, lipatan) | `src/lib/PaperSheet.js`, `src/lib/folds.js` |
| Lighting, tone mapping, motion blur, supersampling | `src/lib/stage.js` |
| Kamera | bagian `camera` di tiap file shot (V3 memakai satu spline dolly kontinu) |

Animasi objek, kamera, dan efek dokumen (marker/reveal) dikontrol terpisah di tiap shot. Semua adalah fungsi murni dari waktu, jadi frame mana pun bisa dirender ulang secara identik.
