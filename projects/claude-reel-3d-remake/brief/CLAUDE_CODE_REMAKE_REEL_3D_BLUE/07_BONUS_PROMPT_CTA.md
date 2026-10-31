# BONUS UNTUK KOMENTAR `ANIMASI`

Isi ini bisa diberikan ke audiens yang komentar `ANIMASI`. Templatenya umum; ini **bukan** klaim semua fitur akan otomatis tersedia di akun mereka. Tidak memerlukan 221 files, API key yang dibagikan, atau software berbayar tertentu.

## Template prompt untuk Claude Code

```text
Kamu adalah creative director, motion designer, dan editor video profesional.

Tugasmu adalah membuat storyboard dan membangun video animasi berdurasi [30/45/60] detik dengan rasio 9:16, output 1080×1920, 30fps.

TOPIK:
[TULIS TOPIK VIDEO DI SINI]

TARGET AUDIENS:
[SIAPA YANG AKAN MENONTON]

GAYA VISUAL:
[MISAL: 3D clean dengan warna brand / motion graphic editorial / diorama cinematic]

ASET YANG SUDAH ADA:
[MASUKKAN PATH LOGO, KARAKTER, BACKGROUND, VO DARI PROJECT ASLI; JANGAN INVENT PATH]

TAHAP WAJIB:
1. Periksa dulu file proyek, asset yang tersedia, rig karakter, dan library rendering yang sudah terpasang. Laporkan apa yang tidak ada.
2. Bedah maksud naskah saya per kalimat, lalu buat scene breakdown yang mengikuti VO.
3. Buat storyboard visual. Untuk setiap scene jelaskan: hero visual, animasi, motion kamera, depth/parallax, pencahayaan, transisi masuk/keluar dan key word highlight.
4. Buat 3 styleframe + satu gerakan karakter pendek untuk validasi sebelum semua scene.
5. Bangun video pada video stack yang sudah dipakai project saya. Jangan merombak project lain.
6. Review setiap scene dan setiap transisi pada frame yang relevan. Perbaiki clipping, text overflow, gerakan yang kaku dan pose yang aneh.
7. Gunakan file VO saya sebagai sumber waktu. Jangan mengganti suara saya secara otomatis.
8. Beri preview lengkap untuk saya approve. Render final baru setelah approved.

LARANGAN:
- Tidak membuat data, screenshot software, klaim, atau logo palsu.
- Tidak pakai zoom/fade berulang di seluruh video.
- Tidak mengubah identitas maskot atau font brand.
- Tidak memaksa memakai API berbayar tanpa persetujuan.
- Tidak mengklaim render selesai jika belum dicek.

Berikan ringkasan proyek, apa saja yang dibuat, bukti screenshot review, kendala yang masih ada, dan link/path preview.
```

## Checklist pemula sebelum mulai

1. [ ] Instal dan login Claude Desktop atau Claude Code lewat metode yang mendukung akunmu.
2. [ ] Pastikan sudah punya folder proyek lokal.
3. [ ] Tentukan video vertikal 9:16, durasi, dan topik.
4. [ ] Siapkan logo, visual referensi, dan aset karakter sendiri bila perlu.
5. [ ] Rekam VO yang bersih agar animasi mudah sinkron.
6. [ ] Tanyakan ke Claude Code video renderer apa yang tersedia—jangan berasumsi semuanya sudah terpasang.
7. [ ] Cek satu adegan dulu, baru bangun semua scene.
8. [ ] Tonton preview penuh, cek salah ketik dan gerakan patah.
9. [ ] Render setelah preview disetujui, lalu cek file finalnya.

Panduan resmi Anthropic untuk alur awal: https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code
