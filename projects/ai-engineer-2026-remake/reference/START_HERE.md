# AI PRENEUR — AI ENGINEER ROADMAP 2026
## Premium Remake / Claude Code Production Package

**Konsep:** *Build the Machine* — maskot AIpreneur merakit sebuah mesin AI dari 10 komponen, dari fondasi hingga sistem yang benar-benar siap dipakai.

**Status:** Paket **pra-produksi**, bukan video final. Paket ini menyediakan pembacaan referensi, naskah untuk direkam, storyboard, aset asli dari Freddie, dan satu prompt eksekusi yang bisa langsung diberikan ke Claude Code. Model 3D maskot tidak termasuk karena Freddie menyimpannya di proyek Claude Code.

## Mulai dalam 5 langkah

1. Ekstrak ZIP ini ke folder proyek baru atau folder kerja Claude Code di komputer yang sama dengan maskot 3D.
2. Buka `02_VOICE_OVER_FINAL.txt`; buat VO Bahasa Indonesia dari teks itu melalui ElevenLabs atau rekam sendiri. Simpan sebagai `assets/voiceover_final.wav` atau `.mp3` **tanpa musik**.
3. Pastikan model 3D maskot yang sudah ada di workspace Claude Code masih dapat dibaca. Bila tidak ditemukan, Claude Code harus **bertanya lokasi file**, bukan membuat karakter baru.
4. Buka `04_PASTE_INTO_CLAUDE_CODE.md`, salin **seluruh isi** ke Claude Code. Prompt itu menginstruksikan Claude memeriksa aset, menghitung durasi VO, membangun preview visual, dan mengaudit hasil.
5. Setujui preview sebelum render kualitas akhir. Setelah disetujui, Claude Code boleh mengekspor MP4.

## Isi paket

| File | Untuk apa |
| --- | --- |
| `01_BEDAH_VIDEO_REFERENSI.md` | Observasi video sumber 3:00, bagian per bagian, plus peluang peningkatan |
| `02_VOICE_OVER_FINAL.txt` | Teks VO utuh, siap ditempel ke tool suara |
| `03_STORYBOARD_PREMIUM.md` | Adegan, sudut kamera, material, gerakan maskot, teks, dan transisi |
| `04_PASTE_INTO_CLAUDE_CODE.md` | **Satu prompt lengkap** untuk eksekusi di Claude Code |
| `05_QA_AND_BRAND_LOCK.md` | Standar kualitas, font/warna/logo, cek teknis, cek narasi |
| `06_OFFICIAL_LEARNING_SOURCES.md` | Referensi resmi terkait isi roadmap |
| `assets/background_pale_ice.png` | Background foto/warna dari user, 1080×1350; harus di-fit, jangan distretch |
| `assets/aipreneur_logo_dark.png` | Logo asli dari user dengan alpha PNG |
| `reference/source_ai_engineer_180s.mp4` | Video sumber untuk referensi observasi saja; **bukan untuk final output** |

## Konsep visual yang dikunci

- Format **9:16 / 1080×1920 / 30 fps**.
- Background user: putih es lembut dengan titik biru halus. Pertahankan gambar sumber sebagai plate; bila perlu 9:16, perluas pinggirnya secara proporsional dengan turunan warna, **jangan diregangkan**.
- Teks biasa: **Poppins Regular/Bold** dengan gradient tinta `#0A0D2C → #294B77`. Contoh CSS: `linear-gradient(105deg,#0A0D2C 0%,#294B77 100%)`.
- Kata penting: **putih** di atas **kotak gradient** `#0A0D2C → #294B77`, radius halus, bukan neon.
- Logo asli AI PRENEUR **selalu di kiri atas**; animasi masked light sweep kecil tiap 7–9 detik + micro-tilt masuk awal. Logo wajib terbaca dan tidak kedip/glow berlebihan.
- Maskot dari aset 3D user, bukan avatar generatif baru. Geraknya fungsional: mengangkat, menyambung, memutar, mengecek.
- No BGM. Efek suara hanya yang berlisensi jelas atau diberikan user.
- Gaya: motion studio premium, perpindahan kamera yang punya sebab, diorama 3D berbobot, typography editorial, *no AI slop*.

## Alur besar

**Masalah** → **blueprint** → **rakit 10 komponen** → **tes & produksi** → **pilih jalur** → **sistem menyala utuh**.

Catatan durasi: target editorial sekitar **100–115 detik**, tetapi waktu final wajib mengikuti **durasi audio VO yang benar-benar direkam**. Timing di storyboard hanya perkiraan kreatif, bukan timestamp transkripsi presisi.
