# CLAUDE CODE — PREMIUM 3D REEL REMAKE

Paket handoff untuk remake video tutorial Claude Code yang dikirim Freddie.

## Isi paket

1. `01_CLAUDE_CODE_EXECUTE.md` — **PROMPT UTAMA**. Ini yang disalin ke Claude Code.
2. `02_REFERENCE_SCENE_BREAKDOWN.md` — bedah video asli 61,48 detik, dengan timecode, transisi, dan motion yang tampak.
3. `03_PREMIUM_STORYBOARD.md` — rancangan remake baru (18 scene; timing awal akan dikunci oleh VO).
4. `04_VOICE_OVER_INDONESIA.md` — naskah dan arahan rekaman VO; `04_VOICE_OVER_PLAIN.txt` khusus teks bersih siap copy-paste.
5. `05_CHARACTER_LOGO_QA.md` — instruksi memperbaiki maskot 3D, jas, gestur, lighting, logo.
6. `06_RENDER_QA_CHECKLIST.md` — pemeriksaan visual, animasi, audio, dan export.
7. `07_BONUS_PROMPT_CTA.md` — template prompt/checklist yang dijanjikan pada CTA `ANIMASI`.
8. `assets/brand/background_original.png` — **background asli dari user**, tidak diubah.
9. `assets/reference/reference_original.mp4` — video referensi 61,48 detik, untuk analisis **saja**.
10. `assets/reference/contact_01.jpg`, `contact_02.jpg` — contact sheet visual untuk memudahkan Claude membandingkan source.
11. `DESIGN.md` — style lock spesifik dark-blue/cyan/Poppins (menggantikan house style lama hanya untuk remake ini).

## Cara pakai di Claude Code

1. Ekstrak ZIP ini ke dalam **folder project Claude Code yang sudah berisi maskot 3D dan logo asli**. Boleh sebagai subfolder `remake_brief/`; jangan menimpa file existing.
2. Buka sesi Claude Code di root project itu. Salin **semua isi** `01_CLAUDE_CODE_EXECUTE.md`, lalu jalankan.
3. Claude harus lebih dulu menemukan dan memverifikasi file **maskot 3D asli** serta **logo asli** di project yang sudah ada; paket ini memang **tidak** membawa/menebak path keduanya.
4. Rekam naskah `04_VOICE_OVER_INDONESIA.md` dalam satu berkas WAV/MP3, lalu berikan file tersebut ke Claude Code. Timing di storyboard hanya estimasi sebelum VO final tersedia.
5. Minta preview lengkap dan review frame demi frame sebelum render final. Semua aktivitas yang memerlukan API berbayar, kredensial, atau perubahan besar di project lama memerlukan approval.

## Kunci brief Freddie

| Elemen | Keputusan |
|---|---|
| Media | Instagram/TikTok **9:16**, 1080×1920, 30 fps; sesuai rasio video referensi 720×1280. |
| Durasi | Kira-kira 65–75 detik; **VO final adalah patokan**, bukan angka storyboard. |
| Background | Pakai PNG biru user; jangan digambar ulang, ditarik/stretch, atau diubah hue. |
| Tipografi | **Poppins Bold 700** untuk headline/kata penting; **Poppins Regular 400** untuk deskripsi. |
| Warna teks | Putih `#FFFFFF` dan cyan `#00D0FE`. |
| Highlight | `#00D0FE` dengan glow **selektif**, hanya pada kata kunci/impact. |
| Kotak teks | Glass/enamel biru gelap: gradient `#0A0D2C → #294B77`, border cyan tipis, ada inner highlight. |
| Maskot | Gunakan karakter 3D asli user di Claude Code. Perbaiki kaku, pose, penetration/clipping dan jas. |
| Logo | Logo asli existing di **kiri atas** dengan moving sheen/glow periodik yang tidak mengubah desain. |
| Presentasi | Visual edit kreatif, camera parallax nyata, prop depth, motivated match-cuts, ritme VO. Bukan AI slideshow. |

## Yang sengaja TIDAK dilakukan

- Tidak membuat ulang logo atau maskot dari AI generatif.
- Tidak menyalin identitas kreator/mascot asli video referensi.
- Tidak menyertakan musik atau SFX berhak cipta tanpa izin.
- Tidak mengklaim bisa memperbaiki rig/suit sebelum inspeksi aset sumber.
- Tidak mengarang path `logo.png`, `mascot.glb`, dependensi, atau hasil render.

## Fakta sumber produk

Panduan resmi Anthropic yang relevan: https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code

Claude Desktop memiliki tab Code; saat membuka project, sesi dapat menggunakan folder kerja lokal. UI dapat berubah, jadi screenshot pada video referensi adalah ilustrasi visual historis—verifikasi implementasi sesuai antarmuka aktual, jangan menyalin label UI usang.
