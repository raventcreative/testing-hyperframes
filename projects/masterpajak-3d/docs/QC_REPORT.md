# Laporan Quality Control

Render pertama tidak diterima begitu saja. Setiap putaran memakai still kualitas final, contact sheet, dan **probe kecepatan layar per frame** (grafik di `QC_MOTION_VELOCITY_PLOTS.png`). Tabel di bawah mencatat temuan nyata dan perbaikannya.

## Iterasi & perbaikan

| # | Review | Temuan | Perbaikan |
|---|---|---|---|
| 1 | Rendering | Akumulasi motion blur hanya menyimpan sub-frame terakhir (objek jadi transparan 1/8). Penyebabnya `autoClear` renderer | `autoClear=false` dan clear dikelola manual. Diverifikasi ulang di still final |
| 2 | Material | Kertas terlihat flat seperti kartu, karena cahaya directional seragam | Key diganti spotlight dengan falloff fisik, ditambah softbox (RectAreaLight) untuk gradien kilau. Bow kertas lengkung diperkuat |
| 3 | Rendering | Teks sekunder resi terlalu pucat di ukuran kecil | Tinta digelapkan, berat font mono dinaikkan, ukuran +10–15% |
| 4 | Komposisi (V2) | Halaman 2 mengintip dan menembus panel rekening yang sedang membuka (penetrasi geometri) | Halaman 2 parkir tertutup penuh di belakang lembar yang sudah terbuka, lalu bergeser keluar |
| 5 | Motion (semua) | Probe: entrance memuncak di **76 px/frame** lalu hampir diam dalam 0,25 dtk (whip, tidak premium) | Kurva cubic-out dan durasi lebih panjang. Puncak turun ke 12–22 px/frame dengan deselerasi panjang |
| 6 | Motion (semua) | Patahan kecepatan di batas segmen jalur (parameter Catmull-Rom bukan arc-length) | `getPointAt` (parameter panjang busur). Probe: **tidak ada diskontinuitas > 3 px/frame** di V1 & V2 |
| 7 | Motion (V2, V3) | Kecepatan berbentuk "V" (arah gerak berbalik) saat lipat/buka, akibat kompensasi posisi yang bertabrakan dengan pergeseran titik berat kertas | Setiap dokumen mengunci titik berat visualnya sendiri (centroid mesh). Lipat dan geser dibuat overlap jadi satu gestur |
| 8 | Komposisi (V3) | Orbit dan rekonsiliasi terlalu mepet ke tepi frame; tumpukan dan flip terlalu kecil | Satu spline dolly kamera (Hermite monoton, kecepatan kontinu): mundur saat orbit, maju saat tumpukan/flip, mundur halus saat laporan terbuka, lalu push-in akhir |
| 9 | Rendering | Frame 0 V1 belum hijau bersih (ujung resi terlihat) | Titik awal jalur dipindah lebih jauh. Verifikasi otomatis: frame 0 ketiga video = 0 piksel non-hijau |
| 10 | Cerita (V3) | Benang rekonsiliasi menimpa angka "721.500" | Benang keluar dari tepi resi dan mendarat di tepi baris rekening yang cocok |
| 11 | Tipografi | Kolom KREDIT dan SALDO di rekening koran saling menempel | Kolom digeser, sekarang ada jarak tegas |

## Checklist review (status akhir)

**Komposisi**: objek jelas dan besar (hero ±72–78% tinggi frame), tidak ada konten penting terpotong, komposisi didesain khusus 1:1, ada margin untuk reposition di CapCut.

**Motion**: easing custom (bezier, spring teredam, profil kecepatan), tidak ada lonjakan kecepatan, float tidak berulang, orbit ±0,35 putaran/dtk dengan akselerasi → cruise → deselerasi, transformasi tanpa teleport (swap tepat edge-on).

**Rendering**: tepi bersih (SSAA 2×), teks tajam, arah cahaya sama di ketiga video, tidak ada bayangan atau gradien di background, tidak ada pantulan hijau di material.

**Dampak kreatif**: cerita "resi + rekening → laporan" tersampaikan lewat objek (rekonsiliasi → lipat → flip → buka), tanpa simbol + / =.

## Inspeksi video final
Lihat `VERIFICATION_REPORT.md` (pengecekan teknis otomatis) dan `02_PREVIEW/contact_sheets/` (frame yang diambil dari MP4 final, bukan dari still).
