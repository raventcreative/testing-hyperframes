# AI PRENEUR — Interview Dibantu AI (Claude Code HyperFrames)

## BUKA INI DULU

**Ini proyek Interview Dibantu AI yang BARU.** Jangan gunakan ZIP lama `konten ai preneur.zip` yang berisi 11 audio / cerita lain.

**Status paket:** siap diekstrak sebagai ASSET + PROMPT pack. Belum ada implementasi, preview, atau video MP4 final; Claude Code-lah yang akan build/render.

## Tiga langkah di Windows

1. Extract ZIP menjadi folder biasa, misalnya `D:\Projects\konten ai preneur - interview ai`. Pastikan folder memiliki `assets`, `references`, `docs`.
2. Buka terminal PowerShell **di folder hasil extract**, jalankan `claude` atau buka project tersebut di Claude Code yang sudah kamu pakai. Tidak perlu instal ulang HyperFrames.
3. Buka `docs\01_PROMPT_CLAUDE_CODE.md`, **copy seluruh isi**, paste sebagai satu pesan di Claude Code, tekan Enter. Claude akan membaca file berdasarkan path relatif di folder ini. Kalau direktori Claude berbeda, buka folder hasil extract dahulu.

Claude Code akan cek skill/CLI versi lokal, menganalisis aset+audio, membuat motion, preview dan pemeriksaan. Jika HyperFrames meminta persetujuan setelah preview FINAL, setujui setelah melihat kualitasnya agar render MP4 dimulai.

## Asset saat ini
- `assets/audio/voiceover_final.mp3` = **SATU VO GABUNGAN** 93.153 detik (bukan 8 file terpisah).
- `assets/background/background_original.png` = background asli navy user (1080x1350).
- `assets/background/background_1080x1920_extended.png` = adaptasi vertikal tanpa stretch; perlu diperiksa bila pola mirror terlalu kentara.
- `assets/branding/logo_aipreneur_original.png` = logo TERBARU dari user (aslinya berlatar putih).
- `assets/branding/logo_aipreneur_transparent_derived.png` = turunan dari logo TERBARU; latar putih dilepas, bentuk logo dipertahankan.
- `references/reference_interview_ai.mp4` = referensi gaya 2m56s, **tidak** boleh ditempel ke film final sebagai footage.

## Kunci brand
Font Poppins Bold 700 + Regular 400. Gradient teks #00c9ff ke #294b77. Background navy user. Film 9:16 1080x1920, 30fps, target **95.00 detik**. Logo asli AI PRENEUR. Tidak ada font .ttf/.woff yang dikemas; renderer harus memverifikasi font tersedia.

## Dokumen lain
- `docs/02_NASKAH_VOICEOVER.txt`: naskah 8 segmen dari percakapan; file audio hasil ElevenLabs tetap otoritatif.
- `docs/03_LOCKED_CREATIVE_BRIEF.md`: tujuan, audiens, pesan, batasan.
- `docs/04_STORYBOARD_25_BEATS.md`: 8 scene, 25 microbeat, timecode, aksi kamera/object, exact copy, audio, handoff.
- `docs/05_ASSET_MANIFEST.md`: file dan hak pakai.
- `docs/06_QA_ACCEPTANCE.md`: pemeriksaan mutu visual, audio, dan render.
- `metadata/audio_timing.json`: metadata durasi dan baseline 8 scene dari jeda audio (perkiraan yang wajib divalidasi dengan VO).

## Source tambahan
Tidak ada source WAJIB lagi agar bisa mulai produksi konsep original. Kalau punya screenshot aplikasi yang ASLI, footage interview berizin, rig karakter, atau SFX legal, boleh tambahkan kemudian, tetapi jangan biarkan Claude membuat product UI palsu yang disajikan sebagai demo nyata.
