# R37 · "App hasil vibe coding biar ngebut" — VO script (NAVY, CTA APP)

Reference: `projects/aip_remake_batch9/refs/ref2.mp4` (86.0 s, EN, a vibe-coder asking Claude for 31 app-performance fixes,
CTA "Comment APP"). Client asked for the ref2 *format* (clean 2D motion graphics, one idea per beat, big spoken headline with
one emphasised word, one illustrative UI card, small host in the corner, beat counter, pill CTA) — technique only, never its
pixel creature or branding. **No voxel world.**
Target 80–88 s → final **86.4 s** (VO 84.61 s, ONE untouched ElevenLabs take, offset 0.3 s, ~1.5 s tail on the CTA).

## VO lines (`production/vo_lines.txt`, voice Dakocan, eleven_v4, auto tags) — 24 tips
1. Claude, aplikasi buatanku harus ngebut, pelangganku nggak sabar nunggu.
2. Kerjakan dua puluh empat perbaikan ini.
3. Pasang skeleton loading, biar layar nggak pernah kosong.
4. Tampilan berubah duluan, server menyusul kemudian.
5. Jawaban AI muncul kata demi kata, nggak nunggu selesai.
6. Daftar panjang divirtualisasi, cuma yang kelihatan yang digambar.
7. Gambar pakai WebP atau AVIF, file-nya lebih kecil.
8. Gambar di bawah layar dimuat belakangan.
9. JavaScript dipecah per halaman, yang dimuat cuma yang perlu.
10. Script pihak ketiga dimuat setelah halaman siap.
11. Buang library yang nggak dipakai.
12. Taruh file di CDN, dikirim dari lokasi terdekat.
13. Aktifkan kompresi Gzip, kiriman jadi lebih ringan.
14. Pakai cache browser, kunjungan berikutnya nggak unduh ulang.
15. Pencarian pakai debounce, cari setelah orang berhenti ngetik.
16. Cegah request dobel waktu tombol diklik dua kali.
17. Request yang nggak saling tunggu, jalankan bareng.
18. Kasih batas waktu ke layanan luar, biar nggak ikut macet.
19. Tugas berat lempar ke antrean di belakang layar.
20. Data yang sering dibuka, simpan sementara di Redis.
21. Tambah index di database, pencarian nggak periksa semua baris.
22. Benahi query N plus satu, ambil datanya sekaligus.
23. Ambil kolom yang perlu aja, bukan semuanya.
24. Hasil yang banyak dibagi per halaman, pakai pagination.
25. Pakai connection pooling, koneksi database dipakai ulang.
26. Terakhir, tes di HP murah dan sinyal lemah.
27. Komen APP, aku kirim semua prompt-nya buat Claude lewat DM.

## ATM — what we changed (Amati, Tiru, Modifikasi)
- **Language & voice:** Indonesian, "kamu", Freddie's practical tone; every tip carries ONE short "why" clause a non-programmer
  understands ("biar layar nggak pernah kosong", "kunjungan berikutnya nggak unduh ulang", "biar nggak ikut macet").
- **Own hook:** "Claude, aplikasi buatanku harus ngebut, pelangganku nggak sabar nunggu" — the business angle (customers who
  won't wait) instead of the reference's "lose users"; then "Kerjakan 24 perbaikan ini" (spinning-list hook).
- **Own selection & order (24, not 31):** grouped by where the slowness lives — what the user sees (skeleton, optimistic UI,
  streaming, virtualised lists) → what the browser downloads (WebP/AVIF, lazy-load, code splitting, 3rd-party scripts, unused
  libraries, CDN, compression, browser cache) → requests (debounce, duplicate guard, parallel, timeouts, background queue) →
  database (cache/Redis, index, N+1, select columns, pagination, pooling) → test on cheap phones / weak signal.
  Dropped from the reference: OpenTelemetry tracing, server-near-database, load balancing, font self-hosting, re-render
  prevention, RUM monitoring (the last three are listed as bonus notes in the DM). No sentence uses >3 consecutive words of
  the reference (different language; ordering and examples are ours).
- **Technically correct only:** standard, widely documented performance practices; no invented numbers or speed-up claims
  (bars in the cards are relative, unlabelled; the CTA card says "24 perbaikan", which is exactly what the DM lists).
- **Own visuals:** every card is our own scripted illustration on the client's navy plate (Lucide icons, Poppins, brand
  colours only). The hook uses the **client's own screen recording** (`brand/rec/claude_code_chrome_2026-10-30.mp4`, rule
  2026-11-21: Claude topic → use it): claude.ai home "What's on today, FREDDIE KASHAWAN?" (rec 16.3–17.1 s) then the Claude
  Code input (rec 24.0–26.9 s), crops reused from R34's `assets/rec/` (page content only, no browser chrome, no sidebar /
  session titles). The typed text on the real input is an example and is labelled "contoh prompt".
- **Host:** the client's 3D chibi mascot (whole body, bottom-left corner, lip-synced, a different reaction on every beat,
  CTA pose on "Komen") replaces the reference's pixel creature. No robot, no voxel world.
- **CTA:** "Komen APP" pill + toolkit card listing the 24 fixes; DM = `production/DM_APP.md` (24 fixes + a ready-to-paste
  prompt each + how to use).

## Techniques applied (skills — technique only)
1. **ref2 format** (client request): spoken headline = the VO line, revealed word by word on the voice's own word times
   (blur-rise), ONE emphasised word/phrase in Poppins Bold *italic* + cyan gradient; one card per beat; beat counter
   "07 / 24" with a progress ring and rolling digits; pill CTA; subtle particles + grain.
2. **html-demo** — every card is a pure function of the beat clock (View(t)): scripted cursor that arrives early, presses
   0.15–0.2 s and glides; typed text (~10 chars/s); working state → result → hold (skeleton → content, spinner → loaded,
   "Memproses…", timers, toasts).
3. **product-launch-film** — closed-form step-response springs for every enter/pop/settle; shared elements: the hook's
   spinning list lands on row "01 Skeleton loading" and dives into the first card; the **database cylinder is ONE element
   that glides (arc + spring) through all six database tips** (Redis → index → N+1 → columns → pagination → pooling).
4. **beat-promo-film / technique bank** — every card change lands on the first word of its VO line (cards enter 0.24 s
   before the word), never the same transition twice in a row (26 transitions from 10 enter × 7 exit moves); motion blur on
   fast moves. NOTE: implemented as velocity-proportional blur computed from the same pure functions (t vs t−1/30 s), not as
   3 rendered subframes — a 3× frame render would triple the shared-lock render time.
5. **mascot_robot_recipes** — guide object carries the hand-offs (DB cylinder), spinning pain list hook, mascot reacts on every
   beat (present / explain / point / emphasize / reveal cycle, hop on each beat), CTA point.

## Timing
Beats = first word of each line (composition time, VO offset 0.3 s): 0.52, 4.91, 7.08, 10.05, 13.26, 17.09, 21.02, 24.54,
27.02, 30.54, 33.34, 35.10, 38.36, 41.56, 44.91, 48.36, 51.32, 53.73, 56.99, 59.66, 62.46, 66.09, 69.26, 71.90, 75.17,
78.29, 81.10 (CTA). Pipeline: `tools/words.py` → `tools/vo_data.py` (vendor/vo_words.js: words, phones, envelope, beats) →
`tools/build.py` (index.html) → `tools/sfx_events.cjs` + `tools/sfx.py` (SFX cues come from the composition itself) →
render (shared lock) → `tools/remix_audio.sh` (two-pass −14 LUFS).

## VO QA (listen-check on the take, before building)
- Take 1 (89.2 s, too long): whisper small + medium BOTH misheard "statis"→"status", "Brotli"→"Broadly", "cache (seperti
  Redis)"→"charge" → reworded ("Taruh file di CDN", Brotli dropped, "simpan sementara di Redis") and shortened 4 lines;
  the WHOLE take regenerated.
- Take 2 (84.61 s) kept untouched. Medium: only spelling/number-format differences ("Claude"→"Cloud" as in R11–R35,
  "dua puluh empat"→"24", "N plus satu"→"N plus 1", "nggak"→"gak", "dobel"→"double", "Script"→"Skrip", "per halaman"→
  "perhalaman"). Small additionally heard "ngebut"→"ngeboot" and "pihak ketiga"→"PH3" (medium correct → not both → kept).
- Final check on the final MP4: see `production/VO_CHECK.md`.
