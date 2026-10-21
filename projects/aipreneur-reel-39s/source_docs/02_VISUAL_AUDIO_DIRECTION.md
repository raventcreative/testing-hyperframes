# B. VISUAL & AUDIO DIRECTION

## Art direction: ice-ivory dimensional editorial

**Style router:** REF-B / Cinematic-Object-Depth sebagai DNA utama; REF-A / Editorial-Kinetic sebagai pendukung. **Depth:** medium hampir sepanjang video, satu/dua hero-3D shot pada klausa paling penting yang teridentifikasi dari audio. Jangan memaksakan sculpture/3D untuk kata-kata abstrak yang lebih efektif dengan tipografi.

**Palet, diambil dari aset asli:** blue-grey `#ACC6E7` di kiri atas, powder `#CBDBF4`, soft-cloud `#E8F0FB`, near-white `#FBFCFE`, graphite logo sekitar `#2E2E2E`; teks `#202B3B` untuk body/header, accent navy-ice `#294B77` jika kontrastif. **Brand lock:** bentuk logo dan warnanya dipertahankan. Jangan mengasumsikan user meminta gradient khusus untuk copy; warna pendukung adalah keputusan artistik.

**Background:** jangan hanya `object-fit:cover` source 980×1225 lalu crop secara destruktif. Gunakan foto aslinya sebagai arah tekstur dan warna, perpanjang dengan gradient cream/ice-blue yang mulus ke 1080×1920, difusi cahaya besar di kiri-atas dan kanan-bawah. Morphing: lokasi/lintasan blue haze halus antar-beat (sebagai layer seekable mengikuti detik timeline), bukan mengganti ke latar gelap acak atau disco glow. Full bleed valid; konten penting tetap di safe-zone.

**Typography:** sans-slab? NO. Pilih sans-serif geometrik bersih yang **benar-benar tersedia di Windows/browser renderer** (contoh Segoe UI/Arial; local Inter jika ada dan lisensinya jelas), 2 weights dominan (semibold/bold). Headline sangat kontras dan editorial, 1 focal message per scene, 2–5 kata per headline bila didukung isi audio, caption otomatis 1–2 baris max setelah hasil transcript. Tidak perlu teks kecil berjajar panjang.

**Z-planes:**
- BG (-600): extended ice-ivory environment, atmospheric blue haze, textured subtle geometry grid optional semantik.
- MG (-160): stage/floor matte ivory yang terkena cahaya, existing orbit path, architectural volume/cutouts yang relevan dengan klausa.
- HERO (+60 to +260): card/paper mechanism/glass window/dial/hardware motif hanya jika menjelaskan VO, edge bevel sungguhan/simulated, material matte porcelain + graphite rim + selectively tinted glass.
- FG (+340): occlusion wipe/masked moving mechanism dan dedicated high-contrast readable text plane; logo asli tidak perspective-distort secara tidak perlu.

**Light/material:** broad soft key upper-left (+ satu cool fill upper-right), tint tipis biru-kaca yang menyatu dengan background; contact shadow benar-benar anchored to stage. Elevation bertambah → cast shadow meluas dan melembut. Rim highlight putih-biru tipis; tidak semua objek metal/glass. Glass butuh tinted plate, double edge highlight, background separation dan soft credible shadow; jika CSS `backdrop-filter` tidak survive headless snapshot, jatuhkan ke composited simulated translucent plate yang jujur.

**Camera:** gunakan satu staging camera dengan dolly subtil (sekitar x/y 20–65 px di ruang 1080 frame; rotation sekitar 3°–7° sesuai konteks), differential parallax foreground > midground > background. Title utama tetap camera-facing, jangan dibuat miring sulit dibaca. Macro movement 0.7–1.4s, objek mekanik 0.5–1.0s, micro selection 0.2–0.45s dengan settle singkat. Camera movement **tidak konstan**; hentikan sejenak saat inti VO dibaca.

**Motif yang boleh diterjemahkan jadi konten AI PRENEUR, tergantung VO:**
- REF-B **7.5–11.5s:** stack folder/paper yang bertumpuk, pola keberlanjutan scene dan parallax. Cocok untuk mengorganisasikan ide/data; jangan gunakan bila narration bukan tentang proses/informasi.
- REF-B **40.9–43.2s:** UI/elemen berubah menjadi control circular mechanical dial dengan titik state-change berlampu. Cocok untuk keputusan/pergantian mode yang benar disebut VO.
- REF-B **48.2–50.0s:** kotak fisik membuka lalu reveal konten, timing causality dengan spotlight. Cocok untuk informasi hasil, output, atau unlock; jangan copy bentuk asli.
- REF-A **7.2–9.2s:** focused selected-row tracking; hanya untuk poin daftar/tutorial yang memang dipresentasikan dalam narasi.

**Per-beat choreography:** anticipation → purposeful entry/reveal → hero action tepat pada kata relevan → settle (power3.out), hold ~0.6–1.3s → cinematic handoff/match-cut. Match geometry between acts; jangan endless fade-in, slide-up, scale-only zoom berulang. Satu editorial hard cut cukup kalau memang mengganti konsep.

**Negative visual:** dark neon wallpaper, rainbow glow, semu '3D' padahal cuma rounded cards shadow, generic template 11 slide, fakery data/brand/logo, scrolling bullet tanpa sebab, morph logo jadi simbol lain, ice surface yang terlalu transparan membuat teks hilang, micro typography, wajah/karakter otomatis dibuat tanpa aset asli.

## Audio

- Single authoritative VO: **`assets/audio/vo_master_39s.wav`**, sample-accurate, mono 44.1kHz, 39.381361s.
- Scene choreography harus diarahkan ke **kata/frasa yang transkripnya diverifikasi**, bukan tebakan berdasarkan nama file.
- **BGM: tidak ada secara default** agar VO tetap jadi focus; hanya tambahkan jika user menyetujui/sumber audio original/berlisensi terbukti dan intelligibility aman.
- **SFX:** maksimal 3–6 micro-events (select, tap mekanik, paper unfolding, restrained whoosh) sesuai object action; hanya dari sound lokal original/rights-clear, beri duck di bawah VO dan mix tanpa clipping; tanpa SFX pun sah.
- **Captions:** jika ASR berhasil, verbatim + timestamp dari master. Jangan menempatkan subtitle menumpuk heading di area y>1540; tinggikan pada scene UI padat; tipografi subtle charcoal-on-ivory backing.
- **Ending:** durasi visual 39.40s; audio selesai 39.381s, sisa 0.019s saja; jangan fade-to-black 1s atau menambah tagline tidak diucapkan.
