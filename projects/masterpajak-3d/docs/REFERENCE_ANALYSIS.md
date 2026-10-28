# Analisis Referensi → Prinsip untuk MasterPajak AI

Referensi: video 720×540, 60 fps, 14,57 dtk. Isinya landing page produk sepatu lari dengan carousel kartu berderet dan modal detail yang pop-up. Analisis dilakukan frame-by-frame lewat contact sheet 2 fps (overview) dan 10 fps (momen transisi).

## Yang membuat referensi terasa premium

| Teknik di referensi | Pengamatan | Diterjemahkan jadi (orisinal) |
|---|---|---|
| **Shared-element continuity** | Kartu yang diklik *tumbuh dari posisinya sendiri* jadi modal. Tidak ada objek yang muncul dari nol | Resi + rekening dilipat, ditumpuk, lalu flip. Laporan menggantikan tumpukan tepat saat edge-on, dengan tebal dan ukuran yang sama, jadi tidak ada teleport |
| **Blur → tajam saat masuk** | Kartu dan headline masuk dengan blur + opacity, lalu settle | Motion blur fisik (akumulasi sub-frame, shutter 180°) yang proporsional dengan kecepatan nyata di layar |
| **Expo-out dengan ekor panjang** | Gerakan cepat di awal, lalu sangat pelan saat mendarat | Kurva cubic-out + spring teredam. Grafik kecepatan diverifikasi bebas lonjakan (lihat `QC_MOTION_VELOCITY_PLOTS.png`) |
| **Panel melebar horizontal untuk reveal detail** | Modal membuka panel kanan sambil teks muncul berurutan | Laporan *membuka lipatan*, lalu data muncul berurutan (judul → kolom chart → laba) |
| **Rack focus / dim background** | Background di-dim dan di-blur saat modal aktif | Dihindari, karena green screen wajib bersih. Hierarki dibangun lewat skala, kedalaman, dan push-in kamera |
| **Kecepatan carousel konstan dan tenang** | Drift horizontal tidak pernah tergesa | Orbit memakai profil kecepatan: akselerasi → cruise stabil → deselerasi, puncak ±0,35 putaran/dtk |
| **Stagger dari pusat ke luar** | Kartu tengah muncul duluan | Stagger antar lipatan (0,18 dtk), antar baris highlight (0,42 dtk), dan antar kolom chart (0,13 dtk) |
| **Palet terbatas** | Hampir monokrom + satu aksen | Navy + kuning MasterPajak saja. Kuning hanya untuk informasi yang penting |

## Yang sengaja TIDAK diambil
Tidak ada sepatu, kartu produk, layout website, lanskap rumput, carousel horizontal, atau koreografi modal. Tidak ada frame atau elemen referensi yang dipakai sebagai footage, overlay, atau background. Konsep, objek, dan koreografi ketiga video dibuat khusus untuk dokumen keuangan MasterPajak AI.
