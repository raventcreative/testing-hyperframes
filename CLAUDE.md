# HyperFrames workspace — Freddie Kashawan

Repo ini dipakai untuk bikin video dengan skill HyperFrames (`.claude/skills/`, dari `heygen-com/hyperframes`).
Jangan edit file skill-nya langsung; aturan lokal ada di sini.

## Environment (wajib diikuti setiap kali skill hyperframes dipakai)

- Chrome render disiapkan otomatis oleh SessionStart hook (`scripts/hf-session-setup.sh`, log di `$TMPDIR/hf-session-setup.log`).
  Sebelum render pertama, pastikan siap dengan `npx hyperframes browser ensure` (idempotent, cepat kalau sudah ada).
- Network cloud bisa memblokir `cdn.jsdelivr.net` / `unpkg.com`. Setelah `hyperframes init` atau `hyperframes add`,
  dan sebelum `preview`/`render`, SELALU jalankan:
  `bash scripts/hf-vendor-libs.sh <project-dir>` — mengganti URL CDN di HTML dengan file lokal dari npm.
  Kalau render gagal dengan `sub_timeline_script_failure` atau `connect_rejected`, jalankan script ini dulu, lalu render ulang.
- Saat `init` di sini, set `HYPERFRAMES_SKIP_SKILLS=1` (skill sudah terpasang di repo) dan pakai `--non-interactive`.
- Project video taruh di `projects/<nama-project>/`. Output MP4 final taruh di `projects/<nama-project>/out/`.

## Kebijakan credit HeyGen (WAJIB)

Prinsip: **lokal & gratis dulu, HeyGen hanya kalau memang tidak bisa diganti dan sudah disetujui user.**

GRATIS — jalankan tanpa tanya:
- Authoring komposisi (HTML/GSAP), `catalog`/`add` registry (pencarian lokal), `lint`/`check`/`snapshot`/`preview`.
- Render lokal: `npx hyperframes render` (Chrome + FFmpeg di container). JANGAN pernah pakai `cloud render` sebagai default.
- Logo (theSVG/favicon), color grade/LUT, SFX dari library bawaan, transkripsi lokal (whisper), Kokoro TTS / mflux / LTX lokal kalau terpasang.
- MCP HyperFrames by HeyGen: hanya tool baca (`list_projects`, `get_project`, `get_project_status`, `get_render_status`).

BERBAYAR / pakai kuota HeyGen — WAJIB minta izin dulu:
- `npx hyperframes cloud render` / `cloudrun` / `lambda` (per credit; 4K = 1.5×).
- MCP `compose` dan `render_video` (bikin project & render di cloud HeyGen).
- `media-use resolve --type video` (avatar video HeyGen) — paling mahal.
- TTS voiceover HeyGen, BGM/image/icon dari katalog HeyGen. Via OAuth = kuota gratis bulanan (tetap terbatas);
  via API key = langsung potong API credits. Login HeyGen CLI selalu pakai `--oauth`, bukan API key.

Format minta izin (satu pesan, singkat): fitur apa, kenapa butuh HeyGen, alternatif gratisnya apa
(dan kekurangannya), perkiraan pemakaian (durasi/jumlah). Tanpa "ya" eksplisit → pakai alternatif gratis.

Default otomatis:
- Pakai `resolve --local-only` kecuali user sudah setuju pakai HeyGen untuk project itu.
- Musik/voice: tanya dulu apakah user punya file sendiri (rekaman suara Freddie / musik lisensi) sebelum generate.
- Sebelum & sesudah aksi berbayar, cek `npx hyperframes auth status` / `usage --json` dan laporkan sisa kuota.
- Render draft (`--quality draft`) untuk review, render final sekali saja setelah approve.

## Default kreatif (kalau user tidak menyebut lain)

- Format: 9:16 portrait 1080x1920 (`--resolution portrait`) — untuk Reels / TikTok / Shorts.
- Bahasa teks on-screen: Bahasa Indonesia, gaya Freddie: tajam, cepat, Gen Z tapi profesional.
- Struktur short-form: hook kuat di 1–2 detik pertama, isi padat, CTA jelas di akhir.
- Brand: AIpreneur (default), SKINKU, Rave Tailor, Raveloux — sesuaikan tone per brand (lihat preferensi user).
- Caption/teks harus terbaca di safe zone (hindari area UI Reels/TikTok di bawah & kanan).
- Pertanyaan intent interview dari skill tetap boleh, tapi ringkas; jangan tanya hal yang sudah dijawab default di atas.
