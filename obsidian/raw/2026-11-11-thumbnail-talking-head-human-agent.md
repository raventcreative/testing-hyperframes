---
tags: [aipreneur, thumbnail, talking-head, cover, navy]
date: 2026-11-11
project: projects/humanagent_thumb
---
# Thumbnail: "1 Orang Setara 10 Orang" (Human Agent + AI) · talking head · NAVY

**Final yang di-approve**: `thumbnail/COVER_HUMANAGENT_GRID_B_teks.png` / `_bersih.png` (pose nunjuk) dan varian A (pose gestur).

## Selera klien (penting buat thumbnail berikutnya)
- **Jangan cutout setengah badan** di atas background buatan → kata klien "aneh / jelek". Untuk foto orang asli: **pakai background asli, full frame**, cukup dimainin **gradient navy atas + bawah**.
- **Harus HD**, frame video mentah dianggap "burik".
- **Hapus semua tulisan bawaan video** (judul, subtitle, watermark).
- Grid kotak-kotak di belakang orang: **tipis (opacity ±12%)** dan **memudar ke bawah** (habis sekitar dada), jangan full sampai bawah.
- Elegan, nggak norak: navy + satu aksen biru lembut, Poppins, judul pendek.

## Pipeline (semua lokal, foto nggak dikirim ke luar)
1. Pilih frame: scan per 1/30 s, skor ketajaman wajah + badan (Laplacian). Hindari tangan yang lagi gerak (motion blur nggak bisa dibenerin). Pose yang "nyeritain" (nunjuk konsep di layar) > pose random.
2. Hapus tulisan: masker per frame (pita penuh untuk subtitle, termasuk outline gelapnya), isi **per kolom dari piksel atas–bawah di region yang sama** (badan vs layar) → nggak ada pita/noda. Matte badan dibuat dari frame yang subtitle-nya sudah dibersihkan dulu (subtitle bikin matte ngaco).
3. HD: Real-ESRGAN x2 (tiled ONNX) → GFPGAN 1.4 di wajah (landmark 5 titik, blend 0,7 biar identitas tetap) → Lanczos balik ke 1080×1920. Model: huggingface `facefusion/models-3.0.0`.
4. Grade: split-tone bayangan ke navy, sedikit kontras; "portrait mode" halus (background blur 2,4 + gelap 12% lewat matte).
5. Layout HTML (`thumbnail/cover3.html`, `?v=a|b&text=0|1`): gradient navy atas/bawah, grid di-mask keluar dari siluet + fade vertikal, judul di gradient atas.

Script: `tools/build_bg.py <frame> <matte> <models_dir> <out.jpg> [face_weight] [f5083|f4667]`, render `HTTP=<port> COVER=cover3.html node thumbnail/render_cover.cjs`.

## Gotcha
- Teks gradient (`background-clip: text`) dengan `line-height: 1` **motong ekor huruf g/p/y** → kasih `padding-bottom: .26em`.
- CSS `mask-image` dari file PNG **nggak jalan di file://** → render lewat server lokal (http).
- Model hapus background (u2net) nganggap subtitle putih sebagai bagian badan.
