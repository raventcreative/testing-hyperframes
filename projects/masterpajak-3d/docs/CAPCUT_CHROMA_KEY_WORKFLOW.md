# Workflow Chroma Key di CapCut

## Opsi A — MP4 hijau (deliverable utama)
1. Import MP4 ke timeline, taruh di **layer atas** (overlay) di atas footage/background.
2. Pilih klip → **Video → Remove BG / Hapus latar → Chroma key**.
3. Klik pipet **Color picker** pada area hijau (pojok frame mana saja; semua piksel background bernilai #00FF00).
4. Setting awal yang disarankan:
   - **Intensity / Kekuatan**: 10–20 (mulai rendah; background sangat bersih jadi tidak perlu tinggi)
   - **Shadow / Bayangan**: 0–10
   - **Edge / feather** (jika ada): 0–5
5. Zoom ke tepi kertas. Kalau ada garis hijau tipis di tepi (efek wajar dari kompresi 4:2:0), naikkan Intensity sedikit. Jangan terlalu tinggi, nanti bagian highlight kuning ikut terkikis.
6. Atur posisi & skala bebas. Objek punya margin aman di dalam frame 1:1, jadi bisa di-scale/reposition tanpa terpotong.
7. Frame pertama tiap video adalah hijau bersih dan frame terakhir adalah hold yang tenang, jadi aman untuk transisi atau freeze frame.

## Opsi B — tanpa chroma key (hasil paling bersih)
Pakai file di `01_FINAL_VIDEOS/BONUS_TRANSPARENT_ALPHA_WEBM/`. Background sudah transparan, jadi tidak ada fringing sama sekali. Di CapCut desktop, import seperti video biasa dan taruh di layer atas. Kalau versi CapCut yang dipakai tidak membaca alpha WebM, kembali ke Opsi A, atau render master ProRes 4444 dengan `--prores` (lihat `RENDER_INSTRUCTIONS.md`).

## Tips
- Video 1 dan 2 cocok sebagai "STEP 1", Video 3 sebagai "STEP 2". Ketiganya punya lighting dan arah cahaya yang sama, jadi bisa ditaruh berurutan.
- Hold di akhir Video 3 (10,25–11,0 dtk) bisa diperpanjang dengan freeze frame.
