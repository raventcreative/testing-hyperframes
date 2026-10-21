---
workflow: general-video
flow: automation
storyboard: no
message: "Motion AI premium itu mungkin — asal arahan/prompt-nya jelas, bukan cuma 'bikin yang keren'."
destination: reels
aspect: 1080x1920
language: id
audience: company leaders, business owners, enterprise/creative professionals
length: 48s
---

## Intent

Showreel korporat AI PRENEUR yang sekaligus MENGATAKAN dan MENDEMONSTRASIKAN manfaat prompt yang presisi:
dari prompt kabur → lima parameter arahan → hasil motion premium → wordmark AI PRENEUR asli.
Brief, VO, copy, timing dan typography dikunci oleh paket user (`docs_source/`).

## Assets

- assets/background/background_portrait_1080x1920.png — background full-frame semua scene (statis, tidak diganti).
- assets/logo/ai_preneur_wordmark_trimmed.png — wordmark asli (S01 kecil, S09 reveal, S10→S11 lockup). Pixel tidak diubah.
- assets/voice/voice_master_48s.m4a — VO master tunggal 48.000s (11 VO asli sudah ditempatkan). Satu-satunya audio.
- assets/fonts/poppins-latin-{400,700}-normal.woff2 — Poppins Regular/Bold resmi (OFL-1.1, via @fontsource/poppins 5.2.7).

## Customizations

- Typeface terkunci: Poppins 400 + 700 saja, `font-synthesis: none`. Gradient `linear-gradient(120deg,#0a0d2c 15%,#294b77 100%)` di Bold hero.
- Tanpa BGM, tanpa SFX (tidak ada SFX berlisensi terverifikasi lokal).

## Notes

- Timing frame-akurat dari `docs_source/05_AUDIO_TIMING.csv` (11 beat, 1440 frame @30fps).
- Tidak ada label UI tambahan, angka, URL, atau klaim di luar copy terkunci.
- `reference_motion_original.mp4` hanya referensi pace — tidak dipakai di output.
