# NOTES — R6 · Tes ide bisnis ke 100 "pembeli AI" sebelum keluar modal (LIGHT) · `projects/aip_r6_founder/`

1080×1920 · 30 fps · **49.70 s** (1491 frames) · VO 48.4 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r4_remote` (LIGHT).
Serve: `python3 -m http.server 8826 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed. No music (lead adds the bed).

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`
   (saved voice; every line tagged) → `assets/audio/vo.mp3` + `vo.json` (line times + character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js`. Numbers are spoken as words but captioned as
   digits (MERGE/FIXI: 100, 11, Rp25.000, 18). Two alignment onsets were corrected by hand against the energy + whisper
   (`raw[14]` "pun." → 4.86 s, `raw[80]` "belum." → 32.21 s; both had landed in a pause).
4. `python3 -I tools/rounds.py .` → `vendor/rounds.js` (TOTAL, SCN, the 3 featured skills) · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −29.4 LUFS vs VO −18.5 LUFS).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_FOUNDER_1080x1920.png` (static server on :8826).

## Shared kit — `vendor/r6kit.js` (window.R6, loaded in <head>)
Lucide icons (`R6.svg`), the 3 featured skills `R6.SK` (board violet #7c5cff · CFO blue #3a6fe0 · panel navy #294b77), the 11 commands
`R6.CMDS` (README order), **the PANEL** `R6.crowd(prefix, x, y)` = 100 avatars 20 × 5 (pitch 44.4, size 36; ids `p-a0…p-a99`; never
give another element an id of that form), `R6.BUY` = the 18 example buyers, `R6.EX` = the example numbers, `R6.PEOPLE` = 3 fictional
personas. Semantic colours: green = mau beli / angkanya masuk / aman, coral = belum / keberatan, gold = paling seru / ide pemenang,
amber = TAHAN DULU. Avatars use no green tone (green is reserved for "buys").

## Scenes
| id | start–end (s) | VO | visual |
|---|---|---|---|
| s01 | 0.00–5.87 | Ide bisnis kamu bisa dites ke 100 pembeli AI dulu, sebelum keluar modal sepeser pun. | "Ide bisnis kamu" card (frame 0) · "Dites" chip + scan · connector · the PANEL pops in as a wave, counter 0→100 · "Modal yang keluar" card, **Rp0** slams, AMAN badge |
| s02 | 5.87–9.70 | Namanya Founder: 11 skill Claude, gratis dan open source. | pack card "Founder" (github.com/Jakeschincariol/founder-skill) · "11" badge slams · 11 `/founder-…` chips fly out (README order) · GRATIS + "MIT · open source" · board/consumer/cfo ringed |
| s03 | 9.70–14.60 | Satu jadi dewan direksi, pakai kerangka berpikir Hormozi, Thiel, dan Steve Jobs. | `/founder-board` · "Dewan Direksi" · 3 seats (OFFERS / MONOPOLI / PRODUK, book source) light on each name · chips skor · risiko · vote · "kerangka dari buku, bukan orangnya" |
| s04 | 14.60–18.10 | Satu lagi jadi CFO, yang ngitung margin asli kamu. | CFO card (CONTOH): 25.000 − 11.000 − 2.000 − 3.000 → sisa Rp9.000 · ring 0→36 % "Margin asli" · "Kelihatannya untung Rp25.000" struck, "bukan segini" |
| s05 | 18.10–25.47 | Tapi yang paling seru: panel konsumen. 100 pembeli AI, masing-masing punya penghasilan, kebiasaan, dan keraguan sendiri. | `/founder-consumer` + PALING SERU · "Panel Konsumen" slam · PANEL wave · 3 avatars ring → fanned persona cards (Rina front; Dimas, Sari behind) · penghasilan / kebiasaan / keraguan rows land on their words (CONTOH SIMULASI) |
| s06 | 25.47–29.37 | Contohnya, ide katering makan siang kantor, Rp25.000 per porsi. | PITCH card (CONTOH SIMULASI): title writes in, Rp25.000 slams, chips "Antar sebelum jam 12" / "Menu ganti tiap hari" · "dikirim ke 100 pembeli AI" · ripple through the PANEL |
| s07 | 29.37–33.37 | CFO-nya bilang: angkanya masuk. Tapi panelnya bilang: belum. | two verdict cards: CFO (sisa Rp9.000 · balik modal 20 porsi/hari · arithmetic note) → green ANGKANYA MASUK · Panel lights, 0→18/100, bar 18 % → coral **BELUM** stamp |
| s08 | 33.37–38.67 | Cuma 18 dari 100 yang mau beli. Ada yang bawa bekal, ada yang bilang warteg lebih murah. | big green 18 "dari 100 pembeli AI yang mau beli" · 18 avatars ring green, 82 dim · objection rows with coral-ringed avatars: bawa bekal 34 · warteg lebih murah 29 · takut telat 19 (= 82) |
| s09 | 38.67–42.13 | Mending dengar ini sekarang, daripada setelah beli peralatan dapur. | SEKARANG card (ketahuan dari panel AI, "Modal masih utuh") vs NANTI card (cart: kompor, rice cooker, wadah, freezer — no prices) · "Bayar sekarang" → amber **TAHAN DULU** stamp |
| s10 | 42.13–46.67 | Ingat, panelnya simulasi. Jadi ide yang menang, tes lagi ke pembeli beneran. | PANEL in a dashed violet box, **SIMULASI** stamp, "angka beli = batas atas, bukan ramalan" · ↓ "Ide yang menang" · ↓ "Tes ke pembeli beneran — /founder-launch mulai dari tes kecil di dunia nyata", 4 solid buyers + checks |
| s11 | 46.67–49.70 | Komen FOUNDER, aku kirim lewat DM. | package "Founder · 11 skill" · comment sheet, FOUNDER types, heart, send → plane · DM bubble "Founder · link + urutan pakainya / 11 skill Claude · gratis · MIT", terkirim ✓✓ · end logo + glint |

Robot (co-host, right): flies in on "pembeli AI", waves, cheers "Founder", nods at each board name, TYPES on the holo keyboard while
the CFO counts, scans the panel, thinks on "keraguan", claps on "masuk", shakes on "belum"/"bekal"/"murah", startled on "18", presents
the cart, thinks on "simulasi", cheers the CTA. Mascot (host, left): present/explain/emphasize intents on the key words of each line,
glances at the robot when it flies in and on "FOUNDER".

## Sources (checked 2026-11-12) — details + quotes in production/VO_SCRIPT.md
- Official README: https://github.com/Jakeschincariol/founder-skill (raw README fetched 2026-11-12): name, 11 skills, free, MIT, no
  signup/API key, the 11 commands + order, board = 3 sub-agents on published frameworks ($100M Offers / Zero to One / Isaacson's Jobs),
  CFO = real profit margin + break-even, consumer panel = 100 buyer agents by default with own income/habits/objection, fine print
  (simulated, buy rate = upper bound, confirm with real people; /founder-launch starts with a cheap real-world test), install routes.
- Secondary (cross-check only): skills-hub.ai/sources/founder-skill, explainx.ai review "claims vs README".

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot` + `validate`)
- Final pass, 70 frames (every scene 3–7×, each cut at ±0.03 s, first frame 0 and last frame 49.66): full-frame sheets
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r6/qa_final/contact-sheet-1…8.jpg`, hero-zone crops with timestamps `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r6/qa_final/sheet_00…07.jpg`.
  After that pass s03/s04/s05/s07 were polished (seats + empty panel seats visible from the scene start, CFO rows earlier, persona
  fields as dim placeholders, CFO card dims to 75 %) and re-checked (13 frames): `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r6/qa_fix/sheet_00…01.jpg` (+ contact-sheet-1…2.jpg).
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit). `validate`: 0 errors, 0 contrast warnings
  (SIMULASI tag darkened to #6141e8 after the first run flagged 4.35:1); kit warning "multiple instances of Three.js" (robot + mascot).
- Every initial state is pinned at 0 (`I()` = gsap.set + tl.set at 0); counters use seekable `innerText` tweens with snap (no
  onUpdate); hosts are pure functions of global time; captions never covered (hero content ends ≤ y 928, captions at y 966+).
- Bug caught by the real runtime and fixed: s10's arrow ids (`s10-a0/1`) collided with the panel avatar ids → renamed `s10-ar0/1`.
- VO checked with faster-whisper `small`: all words spoken, tags not read. Two alignment onsets corrected (see Pipeline step 3).

## Known issues / notes for the lead
- Scenes hand over with a short exit/entrance (no shared object between scenes): around each cut there are ~0.1–0.2 s with only the
  background, hosts and caption (visible on the ±0.03 s frames). Persistent object = the 100-avatar PANEL design, re-staged per scene.
- All business numbers, personas (Rina/Dimas/Sari), objection counts and the kitchen-gear list are ILLUSTRATIVE and labelled CONTOH /
  CONTOH SIMULASI on screen; arithmetic is consistent (see VO_SCRIPT.md). The per-seat questions in s03 are our paraphrases of the three
  frameworks, not quotes; no likeness of Hormozi/Thiel/Jobs is shown.
- The repo was not installed/run here (no Claude Code session against it); everything said about it comes from its README (2026-11-12).
  The DM content ("link + urutan pakainya") = the README's install routes + the run order board → … → plan.
- Tiny 1–2 px dots occasionally visible in the caption band on single frames while a caption word is mid-rise (same caption system as
  the kit); not seen on held frames.
- The lead adds the music bed + loudness normalisation; SFX bed is −29.4 LUFS (VO −18.5 LUFS) before the 0.9 track volume.
