# MasterPajak AI — Premium 3D Motion Package

**Konsep:** *From Financial Documents to Financial Clarity.* Tiga video motion graphic 3D yang berdiri sendiri, dalam satu identitas visual. Resi dan rekening koran adalah "bahan mentah" yang, di video ketiga, direkonsiliasi lalu berubah menjadi satu laporan keuangan.

## Isi paket

| Folder | Isi |
|---|---|
| `01_FINAL_VIDEOS/` | **3 file MP4 final**: 1080×1080, 60 fps, H.264, background hijau #00FF00, **tanpa audio stream** |
| `01_FINAL_VIDEOS/BONUS_TRANSPARENT_ALPHA_WEBM/` | Bonus: versi background transparan (VP9 + alpha) dari render yang sama |
| `02_PREVIEW/` | Hero frame tiap dokumen, contact sheet dari frame render final, preview gabungan (tanpa suara) |
| `03_SOURCE_PROJECT/` | Source lengkap yang bisa diedit dan di-render ulang secara deterministik |
| `04_ASSETS/` | Font (OFL), logo mark (SVG), tekstur dokumen resolusi tinggi + peta region UV |
| `05_DOCUMENTATION/` | Dokumen ini, instruksi render, requirements, spesifikasi export, workflow CapCut, laporan QC & verifikasi |

## Tiga video

| File | Durasi | Isi |
|---|---|---|
| `01_STEP_1_RESI_FLOATING_3D.mp4` | 7,0 dtk | Resi 3D masuk dari bidang dalam di bawah, curl kertas settle dengan spring, baris PPN di-highlight, hold di pose akhir |
| `02_STEP_1_REKENING_KORAN_FLOATING_3D.mp4` | 7,0 dtk | Rekening koran datang dari kanan dalam keadaan terlipat Z, terbuka lipatan demi lipatan, halaman 2 bergeser dari belakang, baris kredit menyala berurutan |
| `03_STEP_2_DOKUMEN_MENJADI_LAPORAN_KEUANGAN.mp4` | 11,0 dtk | Resi + rekening mengorbit 1 putaran → rekonsiliasi (TOTAL resi ↔ baris debit 721.500) → dilipat & ditumpuk → flip → cover navy "LAPORAN KEUANGAN" → laporan terbuka, data muncul, hero hold |

Setiap video diawali frame hijau bersih dan diakhiri hold yang tenang, jadi gampang dipotong di timeline.

## Breakdown per scene

### Video 1 — RESI (7,0 dtk)
| Waktu | Aksi | Keputusan desain |
|---|---|---|
| 0,00–1,50 | Masuk dari bawah-belakang di jalur melengkung (arc-length), kamera push-in | Kurva cubic-out: start percaya diri, deselerasi panjang. Rotasi sengaja tertinggal dari posisi (follow-through) |
| 0,95–2,85 | Curl tepi atas akibat "hambatan udara" relaks lewat spring teredam (overshoot ke depan, lalu rata) | Curl di sumbu diagonal, jadi sudut kanan atas terangkat lebih banyak, seperti kertas sungguhan |
| 1,15–2,5 | Yaw inertia: wobble kecil yang teredam setelah putaran berhenti | Benda terasa punya massa |
| 1,7–4,5 | Float berlapis (3 sinus dengan frekuensi tak sebanding, tidak pernah berulang) | Tanpa loop yang terlihat mekanis |
| 3,05–3,60 | Marker kuning menyapu baris **PPN 11%** | Motif highlight marker kuning dari website MasterPajak; multiply, jadi tinta tetap tajam |
| 4,45–7,00 | Ke pose hampir-frontal, float meredam ke ~18%, hold | Pose akhir disengaja, bukan berhenti mendadak |

### Video 2 — REKENING KORAN (7,0 dtk)
| Waktu | Aksi | Keputusan desain |
|---|---|---|
| 0,00–1,50 | Datang dari kanan dalam keadaan terlipat Z, header sudah terbaca | Lintasan beda dari resi (samping vs bawah) |
| 0,95–2,6 | Lipatan atas lalu bawah terbuka (stagger 0,18 dtk), spring overshoot sedikit | Kertas "ingat" lipatannya: sisa sudut 6–7° dibiarkan (realistic folds) |
| 1,85–2,95 | Halaman 2 bergeser keluar dari belakang, lalu 3,4–5,4 merapat lagi | Kesan arsip berlapis tanpa bikin komposisi ramai |
| 2,55–3,9 | Tiga baris kredit menyala berurutan (marker 62%) | Tanpa efek "scanning" futuristik |
| 1,6–6,4 | Kamera orbit tipis +9° → −5° | Menegaskan kedalaman |
| 4,4–7,0 | Rotasi ke pose hampir-frontal, hold | Konsisten dengan Video 1 |

### Video 3 — DOKUMEN → LAPORAN KEUANGAN (11,0 dtk)
| Waktu | Aksi | Keputusan desain |
|---|---|---|
| 0,00–1,55 | Resi dari kiri, rekening dari kanan, keduanya lewat kedalaman | Model, material, dan desain sama persis dengan Video 1 & 2 (builder yang sama) |
| 1,35–5,60 | Orbit sinkron 1 putaran mengitari pusat bersama: akselerasi → cruise → deselerasi (integrasi profil kecepatan) | Kecepatan puncak ±0,35 putaran/detik, mudah diikuti. Bidang orbit miring 15°, radius bernafas 0,52→0,62→0,47, banking & flex kertas mengikuti kecepatan sudut |
| 5,70–6,95 | **Rekonsiliasi**: TOTAL Rp 721.500 di resi dan baris "TRF KE TOKO SUMBER MAKMUR 721.500" di rekening ditandai, lalu benang kuning menyambungkan keduanya | Cerita "AI mencocokkan data" disampaikan oleh objeknya sendiri, tanpa simbol + / = |
| 6,70–7,78 | Kedua dokumen dilipat Z menjadi paket, lalu meluncur jadi satu tumpukan | Lipat dan geser overlap → satu gestur yang kontinu |
| 7,50–8,26 | Tumpukan berputar 180°. Tepat saat edge-on, tumpukan diganti laporan terlipat yang tebal dan ukurannya sama, tertutup motion blur | Tidak ada objek yang hilang atau teleport |
| 8,0 | Cover navy **LAPORAN KEUANGAN** (sisi belakang panel atas letter-fold, laminasi glossy) | Momen "kemasan premium" |
| 8,22–9,3 | Letter-fold terbuka (panel atas lalu bawah, spring) | Bahasa "membuka dokumen" yang sama dengan Video 2 |
| 9,05–10,1 | Marker judul, kolom chart tumbuh berurutan, marker **Laba bersih** | Puncak emosional: data tersusun |
| 9,2–11,0 | Push-in pelan ke hero, float meredam, hold mulai 10,25 | Akhir yang tenang dan mudah diedit |

## Identitas brand dan batasannya (penting)

- **Website `masterpajak.ai` tidak bisa diakses** dari mesin render: domain tidak diizinkan network policy session ini. Semua identitas brand diambil dari **screenshot yang diberikan**, bukan dari website. Tidak ada aset yang diklaim berasal dari website.
- **Warna** disampling langsung dari screenshot: navy `#212C5F`, ink `#161D3A`, kuning `#FED111`, surface `#EDEFF5`.
- **Logo "M"** adalah *redraw vektor* hasil tracing dari screenshot (`04_ASSETS/brand/masterpajak-mark.svg`), **bukan file master resmi**. Sebelum publikasi, ganti dengan SVG resmi dari klien. Logo hanya dipakai di `src/docs/draw.js → mark()`, jadi cukup diganti di satu tempat lalu render ulang.
- **Font**: Rubik dipilih karena cocok secara visual dengan headline dan wordmark di screenshot. Font asli website tidak bisa diverifikasi. Struk memakai JetBrains Mono, karena printer thermal memang mono.
- **Data**: semua angka, nama usaha, nomor rekening, dan nomor resi **fiktif**. Setiap dokumen diberi label "Data ilustrasi". Tidak ada logo bank asli. Angka di laporan konsisten secara internal: pendapatan 248,6 jt − beban 163,2 jt = 85,4 jt; PPh Final 0,5% = 1.243.000; laba bersih 84.157.000. Total di rekening juga cocok dengan saldo berjalan.
- **Referensi** hanya dipakai sebagai patokan kualitas. Tidak ada frame, elemen, produk, layout, atau koreografi yang disalin. Lihat `REFERENCE_ANALYSIS.md`.
