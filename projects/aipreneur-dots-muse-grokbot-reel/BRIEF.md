---
workflow: general-video
flow: automation
storyboard: no
message: "Dots, Muse dan Grok Bot sama-sama AI yang bisa dikasih tugas, tapi cocok untuk pekerjaan yang beda — mulai dari satu tugas berulang."
destination: instagram-reels
aspect: 1080x1920
language: id
audience: "Kreator, profesional dan owner bisnis Indonesia yang mau pakai AI agent secara praktis"
length: 72s
angle: voice-led premium motion-graphics explainer
---

## Intent

Reel AIpreneur 72 detik (2160 frame @30fps), dipandu narasi MiniMax "Olish" milik user. Visual icon-led, navy/icy-blue/near-white,
motion grammar terinspirasi referensi AI Shift (stagger identity card, header stabil, panel demo yang isinya berganti, warna per seksi,
recap bertahap) — tanpa memakai aset, maskot, audio, atau trade dress referensi.

## Assets

- assets/voiceover_original.mp3 — narasi asli (71.758s, mono 44.1k). Otoritas timing. Dipakai utuh, tidak diedit.
- assets/aipreneur_logo_original.png — logo 1485x215, header persisten + signature di CTA. Tidak di-recolor.
- assets/brand_reference.jpg — referensi palet/whitespace/tipografi (Poppins, mix regular+bold uppercase). Tidak ditampilkan.
- assets/script_reference.txt — transkrip reel referensi AI Shift; TERNYATA BUKAN isi MP3. Tidak dipakai untuk copy.
- vo_segments_asr.txt — transkrip per-segmen MP3 (whisper-small lokal via sherpa-onnx) + batas jeda dari silencedetect.

## Customizations

- User memilih (2026-10-19): beat & copy on-screen disusun ulang mengikuti narasi MP3 yang sebenarnya, bukan 12 beat brief lama.
- User memilih CTA: audio dibiarkan utuh ("…dan follow buat cara pakai AI di bisnis" — nama brand tidak terucap di MP3);
  brand ditampilkan on-screen "FOLLOW AIPRENEUR" + logo, sinkron ke kata "follow" (~69.22s). Tidak ada TTS/sambungan audio.
- Tanpa BGM, tanpa SFX (speech-first).

## Notes

- Brief paket (EXECUTION_PROMPT.md) mengunci copy dari script AI Shift; tidak cocok dengan MP3 → diganti dengan beat map di STORYBOARD.md.
- Jangan tampilkan "AI Shift", handle @, harga/angka/benchmark yang tidak diucapkan, logo resmi OpenAI/Meta/xAI, atau UI aplikasi palsu.
- Safe zone teks kritis: x 100–900 (panel s/d 970), y 200–1500.
