# SCENE BRIEF v2 — the 12 animation ROUNDS (r2–r12) · "Bank animasi bikinan Claude" (AI PRENEUR reel)

Project root: `projects/bankanim_2026/` · 1080×1920 · 30 fps · **59.6 s** · HyperFrames 0.8.186. Read `production/SCENE_BRIEF.md`
first for the general rules (style lock, code conventions, checks); this file adds the v2 round system. The client asked that EVERY
animation of the bank is explained and demonstrated: the VO now goes "Satu, centang. Buat tanda tugas beres atau pesanan sukses. Dua,
loading. …" — one ROUND per animation (r1–r12), after the hook (s01, s02) and before s05 (copy → Claude Code), s06 (live edit), s08 (CTA).

## The round system (already built — read these files fully)
- `vendor/rounds.js` → `window.ROUNDS[k]` = { k, id, type, start, dur, tNum, tName, tUse, speechEnd, words: [[text, t], …] } (GLOBAL s).
- `compositions/strip.html` (persistent): the 12 cards as mini chips at **y 300–366** (MicroAnim.STRIP). During round k chip k is
  HIDDEN (a dashed slot shows) from `start` to `start + dur − 0.08`, then it comes back with a green ✓. In the last 0.5 s of r12 the
  12 chips grow back into the GRID (s05 starts on the GRID). Counter "k / 12" at the top right (y 262–292).
- **`compositions/r1.html` = THE ROUND KIT** (Centang). Copy its kit exactly (CSS + markup + builder code; rename the `r1-` prefix,
  set `K`): the big 300 px card LIFTS OUT of its strip chip at the round start and lands on the name (`tName`) at x 80, y 512; the
  number badge pops on the number (`tNum`); the name rises on the name; "animasi k dari 12"; the EXAMPLE PANEL ("CONTOH PEMAKAIAN",
  x 410–1000, y 500–910) swings in on the name and acts out the use the VO describes; EXIT in the last 0.42 s (panel folds away, title
  drops, the big card flies back INTO its chip — it must be exactly at the chip when the strip shows it again at `start + dur − 0.08`).
  **r12 only**: the big card must be back in its chip by `start + dur − 0.5` (the strip starts growing into the GRID then).
- Replace ONLY the example content (the "r1 CENTANG" block) with yours. Keep layout, entrance, exit, timing helpers (`W(word)` =
  local time of a word of this round), and the hf-seek `drawBig` (the big card's animation starts on the name).
- Hero zone for your example: inside the panel (590×410). Nothing below y 935 (captions at y ≈ 966; mascot + robot below).

## Your rounds — the example must SHOW the spoken use (generic, clean UI; no real brands, no people, no invented quotes/claims)
- **r2 Loading** — "biar penonton tahu ada yang lagi diproses": a video export window: thumbnail with skeleton shimmer, "Memproses
  video…" + a small spinner + % bar crawling; on "diproses." it completes (✓ "Selesai").
- **r3 Angka naik** — "pas buat pamer hasil atau pencapaian": a results card: big number counting up (per-value tl.set, e.g. 0 → 10.000
  "pengikut"), a small up-trend sparkline, and on "pencapaian." a trophy/milestone badge (lucide trophy) pops. Label it clearly as an
  example ("contoh"), no real account.
- **r4 Notifikasi** — "bikin penonton ngerasa ada yang baru": a phone-style screen/app header: notification banners drop in one after
  another ("Konten baru tayang", "3 komentar baru", "Pesan baru"), the bell shakes, the badge count increments on "baru.".
- **r5 Grafik** — "data jadi gampang dibaca": a raw table of numbers (4 rows) on "data" morphs into a clean bar chart on "gampang
  dibaca." (bars grow from the numbers' positions; the highest bar highlighted).
- **r6 Toggle** — "buat nunjukin fitur nyala atau mati": a settings panel with 3 rows ("Mode gelap", "Notifikasi", "Auto-posting");
  on "nyala" one switches ON (and its row reacts, e.g. the panel goes dark for Mode gelap), on "mati." another switches OFF.
- **r7 Like** — "ngajak penonton kasih reaksi": a generic social post card (image placeholder, AI PRENEUR logo as avatar): double-tap
  → big heart burst + floating hearts, the like count +1, a reaction row lights up on "reaksi.".
- **r8 Progres** — "nunjukin seberapa dekat ke target": a goal tracker "Target 30 konten bulan ini": a progress bar/ring fills to 24/30
  with milestone ticks; on "target." a chip "6 lagi!" pops.
- **r9 Mengetik** — "kesannya lagi dibalas langsung": a chat window: an incoming bubble ("Kak, masih bisa order?"), then the typing
  dots, then on "langsung." the reply bubble lands ("Bisa kak, langsung aja ya") with a ✓✓ read tick.
- **r10 Upload** — "buat momen kirim file": a file card (e.g. "video_final.mp4") flies into a dropzone, upload progress, on "file." →
  "Terkirim ✓".
- **r11 Cari** — "pas buat momen nyari solusi": a search bar types "cara bikin konten cepat" (per-letter tl.set), results slide in, the
  top result highlights on "solusi.".
- **r12 Rating** — "buat testimoni dan ulasan": a review card: stars fill 1→5 with pops, "5,0", generic avatar icon + skeleton text
  lines (no invented quote), on "ulasan." a second review card stacks behind. Remember the earlier exit (−0.5 s).

## Checks (mandatory)
`node tools/check_scene.cjs <ids>` (preview server :3015 is running) · lint 0 errors in your files · snapshots: the round start (the
card leaving its chip), the name, every example beat, the exit, the last frame (big card exactly in its chip, panel gone). LOOK at them.
Edit only your round files (+ new assets under `assets/fx/`). Do not commit. Report briefly (beats, risks).

## VERIFIED TIMING (global s)
- **r1** check: start 7.6333 dur 4.1334 (end 11.7667) · Satu,@7.88  Centang,@8.63  buat@9.32  tanda@9.64  tugas@9.88  beres@10.12  atau@10.48  pesanan@10.70  sukses.@11.10
- **r2** loading: start 11.7667 dur 3.7 (end 15.4667) · Dua,@11.95  Loading,@12.59  biar@13.31  penonton@13.62  tahu@13.90  ada@14.14  yang@14.48  lagi@14.61  diproses.@14.73
- **r3** counter: start 15.4667 dur 3.7666 (end 19.2333) · Tiga,@15.74  Angka@16.33  naik,@16.66  pas@17.22  buat@17.46  pamer@17.66  hasil@17.88  atau@18.32  pencapaian.@18.46
- **r4** bell: start 19.2333 dur 3.6334 (end 22.8667) · Empat,@19.43  Notifikasi,@20.00  bikin@21.06  penonton@21.49  ngerasa@21.80  ada@22.12  yang@22.24  baru.@22.34
- **r5** chart: start 22.8667 dur 3.0333 (end 25.9) · Lima,@23.10  Grafik,@23.60  data@24.37  jadi@24.68  gampang@24.95  dibaca.@25.36
- **r6** toggle: start 25.9 dur 3.5333 (end 29.4333) · Enam,@26.15  Toggle,@26.76  buat@27.41  nunjukin@27.75  fitur@28.14  nyala@28.41  atau@28.73  mati.@28.91
- **r7** heart: start 29.4333 dur 2.8667 (end 32.3) · Tujuh,@29.60  Like,@30.13  ngajak@30.76  penonton@31.17  kasih@31.51  reaksi.@31.69
- **r8** ring: start 32.3 dur 3.3667 (end 35.6667) · Delapan,@32.54  Progres,@33.19  nunjukin@33.93  seberapa@34.46  dekat@34.80  ke@35.15  target.@35.27
- **r9** typing: start 35.6667 dur 3.1 (end 38.7667) · Sembilan,@35.85  Mengetik,@36.24  kesannya@37.21  lagi@37.64  dibalas@37.90  langsung.@38.19
- **r10** upload: start 38.7667 dur 2.7333 (end 41.5) · Sepuluh,@38.95  Upload,@39.64  buat@40.26  momen@40.57  kirim@40.91  file.@41.16
- **r11** search: start 41.5 dur 2.9667 (end 44.4667) · Sebelas,@41.72  Cari,@42.44  pas@42.94  buat@43.23  momen@43.45  nyari@43.78  solusi.@43.92
- **r12** stars: start 44.4667 dur 3.2 (end 47.6667) · Dua belas,@44.68  Rating,@45.22  buat@46.02  testimoni@46.34  dan@46.88  ulasan.@47.06
