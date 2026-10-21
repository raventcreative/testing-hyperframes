# HANDOFF — LANJUTKAN PROJECT HYPERFRAME PROMPT (V3.0 · HOUSE STYLE REF-H)
**Disusun:** 21 Oktober 2026 · ringkasan keputusan, bukan transkrip verbatim.

## PROMPT PEMBUKA CHAT BARU — SALIN BLOK INI
```text
Ini kelanjutan Project ChatGPT "HyperFrame Prompt" versi V3.0. Baca source terbaru di Project: 01_PROJECT_INSTRUCTIONS_PASTE.md, 02_MASTER_PROMPT_CLAUDE_CODE_V3.md, 03_EXTENDED_PROJECT_RULES_REFERENCE_V3.md, 04B_EXAMPLE_AIPRENEUR_V3_EXECUTION_PROMPT.md, 06_PREMIUM_MOTION_STYLE_DNA.md, 07_DIMENSIONAL_MOTION_TECHNIQUES_AND_QA.md, 11_HOUSE_STYLE_BIBLE.md, 12_SCENE_CONTRACT_CLAUDE.md, 13_PRODUCTION_PIPELINE.md. Abaikan instruksi V1/V2 yang bertentangan.

Gaya default semua video baru = HOUSE STYLE REF-H "Ice-Ivory Illustrated Diorama" (Reel AI PRENEUR v3 yang sudah aku approve): visual-first, TANPA headline besar, hanya caption kecil 1 baris di atas yang muncul per kata, satu scene per frasa VO (cut ~2–3 detik), tiap scene satu objek metafora ilustrasi besar & detail (porselen/kaca/navy) dengan cahaya kiri-atas, contact shadow, 3 depth plane, dan apex tepat di kata kunci; palet terang ice/ivory/navy; penutup lockup logo asli yang diam. REF-A/B/C hanya motif pelengkap.

Aku di Windows; Claude Code + HyperFrames sudah jalan. Folder house_style_kit/ (starter + source contoh v3) dan golden_frames/ sudah/akan aku taruh di workspace Claude Code. Untuk tiap video baru buat: A) locked brief, B) visual/audio direction, C) scene table per frasa VO, D) asset manifest, E) SATU prompt Claude Code mengikuti template 02 V3 (inline HOUSE STYLE LOCK + SCENE CONTRACT), F) QA acceptance (gate REF-H doc 07 §11). Claude wajib verifikasi transkrip dulu, review snapshot vs golden frames, check 0 error, uji determinisme, minta approval preview sebelum render final, lalu verifikasi MP4. Jangan mengaku sudah build/render di ChatGPT.

Aku akan kirim goal/VO/aset video berikutnya di pesan selanjutnya.
```

## HISTORI RELEVAN
- **19 Okt 2026:** fondasi project (Reels 9:16 1080×1920 30fps, ChatGPT menulis prompt, Claude Code membangun).
- **21 Okt 2026 (V2.1):** analisis REF-A/B/C, standar dimensional + QA.
- **21 Okt 2026 (produksi AI PRENEUR 39.4 s di Claude Code):**
  - **v1:** depth CSS 3D, headline besar → user: kurang.
  - **v2:** band navy, punch-in, whip-pan, marker → user: "visual masih kurang".
  - User mengirim REF-A/B/C dan bilang "visual kalah jauh, jangan banyak teks, lebih ke visual". User memilih **full terang pastel** dan **tanpa maskot**.
  - **v3:** dibangun ulang visual-first. 15 sub-composition scene (6 subagent paralel dengan scene contract), caption kecil saja, director review, check 0 error, deterministik, render delivery → **user: "nice aku suka"** → dikunci sebagai house style REF-H.
  - Transkrip: whisper large-v3 (id) lokal. "AI PRENEUR" dikonfirmasi user. Timing kata di-anchor ke jeda (whisper.cpp ~0.3 s terlalu awal).

## KEPUTUSAN OPERASIONAL
- REF-H adalah default. Gaya lain hanya jika user meminta.
- Konsistensi gaya paling kuat jika **house_style_kit/** ada di workspace Claude (starter + contoh source). Tanpa kit, prompt tetap membawa HOUSE STYLE LOCK inline.
- Output LLM tidak pernah identik 100% antar-run. Yang dikunci adalah token (palet, tipe, material, timing, layout), arsitektur, proses dan golden frames, sehingga hasilnya konsisten satu seri.
- Gate approval preview → render final tetap berlaku.
