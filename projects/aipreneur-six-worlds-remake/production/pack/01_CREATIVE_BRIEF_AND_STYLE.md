# CREATIVE BRIEF — “Satu video, enam dunia visual”

## Intent

Buat Reels 9:16 dengan satu maskot 3D milik AIpreneur. Kamera membawa penonton melewati enam gaya motion design yang menyatu menjadi satu cerita. Harus terasa seperti karya senior human motion designer dan 3D animator: art-directed, purposeful, rhythmic, clear on mobile; **bukan kumpulan preset otomatis**.

## Audience response

- 0–3 s: “Lah, kok bisa objek ini berubah jadi scene berikutnya?”
- Tengah: penonton merasakan kamera melintasi ruang nyata, tidak hanya slide.
- Akhir: memahami bahwa *keterhubungan* visual, bukan efek berlebihan, adalah sumber kualitas.
- CTA: “Komen CLAUDE” untuk **6 prompt + storyboard + guide** yang benar-benar ada dalam paket.

## User-directed look LOCK

| Properti | Spesifikasi |
|---|---|
| Canvas | 1080×1920 9:16, 30 fps, H.264/AAC final |
| Background | **Gunakan `assets/background_original.png`**, pale-blue/cool-white dari user. Extend proporsional; jangan diganti dark background |
| Title & normal text | **Linear gradient #0A0D2C → #294B77**, pastikan kontras pada putih muda |
| Highlight word/phrase | **White #FFFFFF** di **badge kotak berisi gradient #0A0D2C → #294B77**; radius 10–16 px, padding cukup, bukan pill murahan |
| Fonts | **Poppins Bold** untuk anchor 700; **Poppins Regular** untuk teks pendukung 400. Jangan substitusi secara diam-diam |
| Logo | Logo asli transparan di top-left; ukur agar terbaca, trim margin alpha; sweep kilau kecil pada huruf setiap 8–10 s, bukan glow terus menerus |
| Brand palette | Hindari warna cyan lama, neon ungu, oranye berlebihan, color noise; silver/charcoal hanya untuk material 3D pendukung |
| Sound | VO user satu-satunya audio naratif; sound effects pendek seperlunya, NO BGM kecuali user secara eksplisit memintanya |
| Mascot | **Gunakan file 3D existing**, identity lock. Jangan generate figur wajah baru dan jangan memakai footage orang di source |

## Camera & 3D grounding

- Gerak kamera: lens language 35–50mm untuk medium shot, 65–85mm untuk detail; dolly/arc nyata, bukan hanya scaling layer.
- Hierarki scene: satu hero object, 2–3 supporting props, typography singkat. 3–5 level kedalaman yang benar-benar terlihat.
- Staging maskot: eye-line tertuju pada objek aktif, tangan memberi sebab-akibat, body weight shift, subtle breathing; jangan semua scene hand waving.
- Lighting: satu key area soft dari kiri atas, bounce lembut; spotlight hanya ketika narasi butuh. Bayangan contact sesuai posisi, tidak melayang tanpa alasan.
- Material: huruf matte-extruded, kaca dengan edge/reflection/refraction halus, frame monitor anodized, floor/contact shadow. Jangan semuanya jadi glossy plastic.
- Jangan gunakan generic spinning rings, particle explosions, overshoot berulang, glow neon sepanjang video, speed ramp setiap 0,5 detik, jitter/warping wajah, atau random UI meaningless.

## Transisi signature (maksimal 2 keluarga besar)

1. **Object-as-portal / edge match-cut** (utama). Satu objek di scene sebelumnya membesar/berputar dan benar-benar menjadi tepi/objek scene berikutnya: bar → monitor, monitor → huruf, huruf → kaca, kaca → berkas cahaya, cahaya → panel grade.
2. **Physical camera handoff** (pendukung). Kamera menelusuri objek, kamera/lighting melanjutkan gerak konsisten. Tidak bergantung pada flash putih berulang.

Jangan sampai kreativitas motion mengalahkan keterbacaan. Hero pose/typography harus memiliki hold setidaknya ~0,55–0,9 s setiap beat utama.

## Penggunaan referensi

`assets/reference_video.mp4` adalah analisis struktur/demo efek, **tidak untuk cropping, restyling, face replacement atau reuse frame**. UI, angka view, dan creator asli bukan asset kampanye baru. Ganti semua elemen menjadi original AIpreneur dengan asset yang sah.

## Batasan teknis

Claude Code harus memeriksa rig GLB sebelum menjanjikan lip-sync atau gerak wajah. Jika tidak memiliki morph target/jaw controls, gunakan eye direction, head rotation, bahu/tangan/pose sebagai ekspresi; jangan merusak mesh untuk membuka mulut.

Jangan mengaku 'photoreal' untuk objek yang jelas stylized. Targetnya **premium stylized realism** dengan cahaya/material logis dan anti-AI-slop.
