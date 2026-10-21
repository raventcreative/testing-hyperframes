# AI PRENEUR — HyperFrames Reels Production Pack

**Status:** source media siap dipakai di Claude Code; prompt dan blueprint sudah disiapkan. **Belum ada video MP4 hasil render.**

## Cara pakai (Windows)

1. Download dan **extract seluruh ZIP**. Pastikan folder `assets`, `production`, `references`, dan file `PROMPT_CLAUDE_CODE_COPAS.txt` tetap berada dalam satu folder; jangan upload ZIP saja ke Claude Code tanpa diekstrak.
2. Buka Claude Code di folder yang memiliki akses ke folder hasil extract ini (paling mudah, buka terminal di dalam folder hasil extract lalu jalankan Claude Code).
3. Buka `PROMPT_CLAUDE_CODE_COPAS.txt`, **Ctrl+A → Ctrl+C**, tempel sebagai satu pesan ke Claude Code.
4. Claude Code akan mengecek versi HyperFrames lokal, membaca **WAV master** dan **11 sumber audio**, melakukan **transkripsi** dan koreksi on-screen copy, mendesain serta mengecek motion, kemudian memberikan preview lengkap.
5. Periksa preview. Ketika Claude Code meminta approval render final sesuai workflow HyperFrames yang terpasang, berikan approval hanya setelah hasil preview sesuai keinginan. Sesudah itu Claude Code merender dan mengaudit MP4.

## Yang sudah benar-benar diverifikasi di sini

- **11 file audio asli ada**, dikumpulkan menjadi `assets/audio/original_parts/vo_01.mpeg` hingga `vo_11.mpeg`.
- **Asumsi urutan** memakai urutan nama file WhatsApp: `5.32.04 PM` tanpa angka, lalu `(1)`…`(5)`, lanjut `5.32.05 PM` tanpa angka, lalu `(1)`…`(4)`. Pembuktian **alur kalimat secara semantik masih menunggu transkripsi**; pastikan ucapan awal hingga akhir mengalir sebelum final export.
- Durasi **WAV master yang benar dari audio hasil decode:** 39.381361 detik; spesifikasi komposisi **39.40 detik = 1182 frame @30fps**, menyisakan sekitar 0.019s video sesudah audio. Angka metadata gabungan MP3 bisa lebih panjang karena padding encoder.
- Audio master `assets/audio/vo_master_39s.wav` = PCM 16-bit mono 44.1kHz, segmen digabung tanpa inter-clip silence, batas segmen diberi micro-fade 2ms, volume global -1.5dB untuk headroom. Audio original tidak diubah.
- Logo transparan: `assets/brand/ai_preneur_logo_original.png` (**1485×1485**), versi crop-alpha non-destructive `ai_preneur_logo_trimmed.png` agar placement tidak kosong. Background asli `assets/brand/pastel_background_original.jpeg` (**980×1225**).
- Gaya motion dikembangkan dari **REF-B (utama, dimensional physical/metaphor)** dan **REF-A (pendukung, editorial typography/selection)**; bukan menyalin footage/referensi.

## Batasan dan gate terpenting

**Isi 11 audio BELUM ditranskripsi/verifikasi verbatim di paket ini.** Jangan menganggap kalimat, klaim, nama platform, CTA, dan subtitle sudah diketahui. Claude Code wajib mencoba `npx hyperframes transcribe --help` dan transkrip **model multilingual** yang mendukung bahasa Indonesia, dengan audio sebagai sumber tunggal kebenaran. Model `*.en` adalah *English-only*, jadi jangan dipakai untuk VO bahasa Indonesia. Jika tidak ada ASR lokal/multilingual yang cocok, Claude wajib berhenti pada gate teks dan meminta **transkrip/naskah audio**—jangan mengarang. Perintah HyperFrames dan ketersediaan model mengikuti instalasi aktual pada Windows user; model mungkin perlu download dan perlu keputusan user.

**Paket ini bukan source project HyperFrames yang sudah dibuild.** Claude Code-lah yang menghasilkan HTML/CSS/JS komposisi, melaksanakan lint/check, preview, dan render sesuai approval resmi.

## File penting

- `PROMPT_CLAUDE_CODE_COPAS.txt` — **SATU prompt utama**, siap-tempel.
- `01_LOCKED_CREATIVE_BRIEF.md` — locks, asumsi, objective.
- `02_VISUAL_AUDIO_DIRECTION.md` — detail material, kamera, lighting, palette, audio.
- `03_TIMECODED_STORYBOARD.md` — durasi 11 audio cue plus motion-stage story structure.
- `04_ASSET_MANIFEST.md` — sumber, nama path yang benar, status.
- `05_QA_ACCEPTANCE.md` — kriteria lulus/gagal.
- `production/audio_timeline.json` dan `production/audio_cues.csv` — source of truth timing.
- `production/transcript_verified.txt` — status transkripsi.
- `references/STYLE_DNA_SELECTED.md` — aturan style yang disalin mandiri dari referensi, tanpa footage pihak ketiga.
