# SCENE BUILD BRIEF — "Claude jadi tim konten Instagram" (Instagram Agent Skill) · AI PRENEUR reel remake · NAVY

Project root: `projects/igagent_2026/` · 1080×1920 · 30 fps · 57.8 s · HyperFrames 0.8.186.
VO (client's voice): "Claude sekarang bisa jadi tim konten Instagram kamu. Gratis, open source. Namanya Instagram Agent Skill. Isinya 13
skill, masing-masing punya tugas sendiri. Yang pertama bikin kaget: dia bedah reel yang lagi naik di niche kamu, terus urutin dari yang
paling melonjak. Lalu, satu ide kamu dijadiin naskah reel. Tiga hook dari 26 rumus, langsung dikasih skor. Profil kamu diaudit pakai 12
kriteria, skornya dari 100. Bagian paling lemah dibenerin duluan. Jadwal seminggu juga disusun. Posting apa, formatnya apa, jam berapa,
plus 10 akun buat kamu ajak interaksi. Sisanya? Caption, carousel, story, balas komentar, DM, sampai bersihin tulisan dari gaya khas AI.
Pasangnya gampang. Tempel link repo-nya ke Claude, suruh install. Selesai. Tenang, nggak ada yang keposting sendiri. Semuanya draf, kamu
yang posting. Mau link-nya? Komen TIM, aku kirim lewat DM."
A REMAKE of `production/reference_sheet.png` (small light UI cards, semicircle score gauges, a hub-and-spoke "team", a bar chart, a phone
"stop scroll", an "Rp0" tag). DO NOT copy any of it: no semicircle gauges, no hub-and-spoke, no bar chart, no Rp0 tag, no light cards on a
light top. Our story: **Claude hires a content TEAM — 13 employee ID badges**, each skill is a team member with a role and a command;
each round opens that member's desk and shows its work. Client rules: premium motion, a different creative transition every scene,
nothing AI-looking, real or open-source assets only, never boring.

## Facts (verified 10 Nov 2026 from the official README of `Jakeschincariol/instagram-agent-skill`, MIT — show only these)
- 13 skills (exact commands): /ig-viral, /ig-reel, /ig-profile, /ig-plan, /ig-caption, /ig-carousel, /ig-story, /ig-human, /ig-comment,
  /ig-reply, /ig-dm, /ig-repurpose, /ig-audit. Free, open source (MIT).
- /ig-viral: finds high-performing reels in your niche and ranks them against each account's own median (outliers) → show an
  "× dari median" multiplier chip (UI example values like ×6,4 are fine; never claim real accounts).
- /ig-reel: one idea → a reel script; 3 hooks chosen from 26 scored hook formulas.
- /ig-profile: scores the profile out of 100 against a 12-part rubric, then rewrites weak areas fix-first.
- /ig-plan: plans the week — what to post, format, timing, plus 10 accounts to engage with.
- /ig-human removes stock/AI-sounding phrasing; /ig-caption, /ig-carousel, /ig-story, /ig-comment, /ig-reply, /ig-dm, /ig-repurpose,
  /ig-audit do the rest.
- Install (easiest): paste the repo URL into Claude and ask it to install. It never posts by itself: everything is a draft, you post.
- No Instagram/GitHub logos (TEXT only: "Instagram", "github.com/Jakeschincariol/instagram-agent-skill"); the Claude mark
  `assets/icons/lobe-claude-color.svg` may be used. Never a pixel copy of the Instagram app (generic social UI only).

## Host layers (read; do not edit): index.html, compositions/robot.html, compositions/mascot.html
Paint order: navy background · **scenes (yours)** · robot · mascot · white logo (top-left y 262–300; fades out at 56.4 s) · captions.
- Captions: words on navy chips, white + cyan #01CCF7, centred at **y ≈ 960–1030** (one line).
- Mascot (host) half body bottom-left, head top ≈ y 1150, x 140–650 (pops up at 0 s). Robot (the team at work) bottom-right
  ≈ x 700–960, y 1340–1680: waves at 0.3 s, shocks on "kaget:", scans on "bedah"/"diaudit"/"bersihin", types on "urutin"/"dijadiin"/
  "Jadwal"/"Caption,"/"Tempel", "no" on "lemah"/"nggak", looks at the mascot on "kamu yang posting".
- → **Your hero zone is y 290–935, x 60–1020** (keep x > 340 for y < 305 because of the logo). Nothing in y > 945.

## THE SYSTEM — the 13 ID BADGES (keep identical in every scene that shows them)
- **Badge** (wall size 150×204, radius 20): white card `linear-gradient(180deg,#fff,#eef3fb)`; a 54 px coloured header band with a
  lanyard clip slot (a 34×8 rounded hole) at top centre; a 56 px circle with the lucide icon (white on the colour) overlapping the band;
  role (Poppins 700 19 px #0a0d2c, 2 lines max) and the command (Poppins 400 17 px #294b77). Lanyard: a 6 px strap going up off-card.
- Members (k: command · role · icon · colour):
  1 /ig-viral · Pemburu Tren · trending-up · #ff5c8a · 2 /ig-reel · Penulis Naskah · clapperboard · #01ccf7 · 3 /ig-profile · Auditor
  Profil · scan-face · #9d8cff · 4 /ig-plan · Perencana Jadwal · calendar-days · #ffb35c · 5 /ig-caption · Caption · type · #3ddc97 ·
  6 /ig-carousel · Carousel · gallery-horizontal · #6adfff · 7 /ig-story · Story · circle-dashed · #ff8f6b · 8 /ig-human · Penghalus
  Tulisan · eraser · #c7a6ff · 9 /ig-comment · Komentar · message-circle · #5ec8ff · 10 /ig-reply · Balas Komentar · reply · #7ee2b8 ·
  11 /ig-dm · DM · send · #ffd66b · 12 /ig-repurpose · Daur Ulang · repeat · #ff9ec0 · 13 /ig-audit · Audit Postingan · chart-column ·
  #8fb6ff.
- **TEAM WALL** (s02 end state): 13 badges in rows 5 / 4 / 4, row centres y 400, 625, 850 (badge 150×204 scaled 0.92), centred in x,
  gap 26; a title plate "Instagram Agent Skill" above is NOT needed (the caption says it) — use a small "TIM KONTEN · 13 skill" label.
- **ROUND HEADER** (r1–r4, and s07 for the rest): the member's badge flies from its wall slot (or arrives with a lanyard swing) to the
  header spot **x 60–210, y 300–504 at scale 1**, its role in large type beside it (Poppins 700 52 px white) and the command in cyan
  (Poppins 700 30 px #01ccf7), y 320–470, x 236–1020. The workspace below is **y 520–935**.

## YOUR SCENES (ideas; make them better; every beat lands on its spoken word — see the timing table)
- **s01 HOOK** (0–4.50) — frame 0 striking: the Claude mark glowing in the centre with a generic "Instagram" profile card behind; on
  "tim konten" a cascade of ID badges drops in on their lanyards from above (deterministic swing, staggered); on "Gratis," a stamp
  "GRATIS" + an "open source · MIT" seal lands.
- **s02** (4.50–10.20) — "Namanya Instagram Agent Skill." = the name types as a big title on a lanyard-style ribbon; "Isinya 13 skill," =
  a counter 1→13 while the badges snap into the TEAM WALL; "masing-masing punya tugas sendiri." = each badge flips quickly to show its role.
  End state = the TEAM WALL exactly as specified.
- **r1 /ig-viral** (10.20–16.53) — badge 1 leaves the wall (the others slide away); "bikin kaget:" = a sharp flash; "bedah reel yang lagi
  naik di niche kamu" = 6 abstract reel tiles (gradient thumbnails with a play icon, view counts as UI examples) get scanned (a
  magnifier/x-ray line); "urutin dari yang paling melonjak." = a LEADERBOARD sort animation (tiles swap positions to rank 1–6), the top one
  gets a "×6,4 dari median" chip and a crown/flame.
- **r2 /ig-reel** (16.53–22.90) — badge 2 header; "satu ide kamu" = a sticky note "ide: kopi susu gula aren" becomes a script page
  (scene lines write in); "Tiga hook dari 26 rumus," = a 3-reel SLOT MACHINE spinning hook-formula names (generic: "Pertanyaan
  nyelekit", "Angka mengejutkan", "Mitos vs fakta"…) and landing on 3 ("26 rumus" counter); "langsung dikasih skor." = score stamps
  (e.g. 9,1 · 8,4 · 7,8 — UI examples) slam onto each.
- **r3 /ig-profile** (22.90–29.13) — badge 3 header; a generic profile card (avatar circle with lucide user-round, name lines, bio
  lines, highlight circles) under a scanning sweep; "12 kriteria," = a 12-segment RING (like a clock face, NOT a semicircle gauge) that
  fills segment by segment; "skornya dari 100." = the centre counts to e.g. 64/100; "Bagian paling lemah" = 2 segments flash coral and
  the matching profile part (bio) highlights; "dibenerin duluan." = the bio rewrites, those segments turn green, score climbs (e.g. 86).
- **r4 /ig-plan** (29.13–36.57) — badge 4 header; "Jadwal seminggu juga disusun." = a 7-column week board (Sen…Min) drops in; "Posting
  apa," = topic cards, "formatnya apa," = format icons (reel/carousel/story), "jam berapa," = time chips (e.g. 19.00); "plus 10 akun buat
  kamu ajak interaksi." = 10 abstract avatar circles (initials only, no photos) line up and get dotted lines + heart/comment icons.
- **s07 SISANYA** (36.57–44.00) — the 9 remaining badges are dealt like a fan of cards on each spoken word (Caption, carousel, story,
  balas komentar, DM — the matching badges light up on their words); "sampai bersihin tulisan dari gaya khas AI." = badge 8 (Penghalus
  Tulisan) wipes a text card: generic stock phrases ("Di era digital ini…", "Tak bisa dipungkiri…") get erased and replaced by plain
  human lines.
- **s08 PASANG** (44.00–48.80) — a generic Claude chat window (Claude mark + "Claude", input bar); "Tempel link repo-nya" = a link chip
  "github.com/Jakeschincariol/instagram-agent-skill" pastes into the input; "suruh install." = the message "install skill ini" sends, a
  progress line; "Selesai." = "13 skill terpasang ✓" with the 13 badges snapping into a folder.
- **s09 AMAN** (48.80–53.37) — "Tenang, nggak ada yang keposting sendiri." = an "auto-posting" switch shown OFF with a lock; "Semuanya
  draf," = 3 post cards stamped "DRAF"; "kamu yang posting." = a big "Posting" button that only a cursor labelled "kamu" presses (the
  robot looks at the mascot).
- **s10 CTA** (53.37–57.80) — a comment row slides up (avatar circle with lucide user-round, input); "TIM" types itself big in cyan on
  "TIM," (per-letter tl.set); a heart pops; on "kirim … DM." a paper plane carries a "Link Instagram Agent Skill" card into a DM card
  ("terkirim ✓"); last ~1 s calm end beat with `assets/brand/logo_white_trim.png` (the corner logo fades out at 56.4 s).

## STYLE LOCK
- Text **Poppins 700/400 only**: white `#ffffff`, cool `#e3edfa`, cyan `#01ccf7` / `#6adfff`; navy glass panels `rgba(12,22,64,.82)` with
  `inset 0 0 0 1.5px rgba(255,255,255,.10)` borders, radius 24–34; white cards for the badges/UI with navy text. Accents: green #2da44e/
  #3ddc97 (ok), coral #e5484d (weak/fail, sparingly), the badge colours above.
- Icons: `assets/icons/lucide-*.svg` (ISC) — trending-up, clapperboard, scan-face, calendar-days, type, gallery-horizontal, circle-dashed,
  eraser, message-circle, reply, send, repeat, chart-column, user-round, check, heart, lock, folder-open, link, sparkles, file-pen,
  badge-check, shield-check, play, flame. Inline the SVG markup (stroke currentColor). More:
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/`.
- No brand logos except the Claude mark, no people photos, nothing AI-generated, no invented facts (UI example values are fine).

## Code conventions (deviations break the render)
- `<template>` + `<style>` + ONE root `<div id="root" data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>` IIFE;
  the runtime strips the root id → `document.getElementById` on unique PREFIXED ids (`r2-…`); prefix classes and SVG ids.
- Timeline boilerplate exactly as `compositions/s01.html` of the sister project `../lamarankerja_2026/compositions/s01.html` (`_sc`
  patch, `ft`, `I`, `tl.set({}, {}, D - 0.01)`, seek-order patch, `window.__timelines["ID"] = tl`). D = the scene dur below; timeline
  length ≤ D. Use `wt(word, after)` on `window.VO_WORDS` for beats.
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (per-value tl.set windows
  for counters/typing). Give every fromTo COMPLETE from-values. One attr/clip-path tween per property; no svgOrigin in CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen blur per frame; ≤ ~250 animated elements per scene.

## Checks (mandatory)
1. `node tools/check_scene.cjs <ids>` → `ok <dur>` (shared preview server on :3020 is running).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`npx --yes hyperframes@0.8.186 snapshot . -o <your scratch dir> --at <≤8 times> --no-end --describe false --timeout 90000`)
   of the first frame, every beat and the last frame. LOOK at them: legible on a phone (≥ 20 px), inside
   the hero zone, nothing over captions/mascot/robot, transitions between scenes seamless (check the frame before and after each cut).
4. Report briefly. Do not commit. Edit only your scene files (+ new assets under `assets/fx/`).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 4.5 (end 4.5): Claude@0.32  sekarang@0.52  bisa@0.74  jadi@1.05  tim@1.31  konten@1.59  Instagram@1.97  kamu.@2.18  Gratis,@3.18  open@3.96  source.@4.16
- **s02** start 4.5 dur 5.7 (end 10.2): Namanya@4.66  Instagram@5.56  Agent@6.00  Skill.@6.44  Isinya@7.06  13@7.55  skill,@7.96  masing-masing@8.52  punya@9.16  tugas@9.61  sendiri.@9.87
- **r1** start 10.2 dur 6.3333 (end 16.5333): Yang@10.45  pertama@10.73  bikin@11.16  kaget:@11.50  dia@12.26  bedah@12.63  reel@12.90  yang@13.10  lagi@13.29  naik@13.45  di@13.75  niche@13.86  kamu,@14.02  terus@14.42  urutin@14.74  dari@15.26  yang@15.38  paling@15.76  melonjak.@16.01
- **r2** start 16.5333 dur 6.3667 (end 22.9): Lalu,@16.71  satu@17.26  ide@17.53  kamu@17.72  dijadiin@17.92  naskah@18.50  reel.@18.78  Tiga@19.60  hook@20.10  dari@20.29  26@20.47  rumus,@20.97  langsung@21.53  dikasih@22.06  skor.@22.37
- **r3** start 22.9 dur 6.2333 (end 29.1333): Profil@23.21  kamu@23.74  diaudit@23.90  pakai@24.40  12@24.56  kriteria,@24.88  skornya@25.76  dari@26.19  100.@26.34  Bagian@27.14  paling@27.61  lemah@27.78  dibenerin@28.21  duluan.@28.64
- **r4** start 29.1333 dur 7.4334 (end 36.5667): Jadwal@29.38  seminggu@30.11  juga@30.51  disusun.@30.61  Posting@31.36  apa,@31.68  formatnya@32.02  apa,@32.62  jam@33.10  berapa,@33.32  plus@33.80  10@34.26  akun@34.56  buat@35.16  kamu@35.32  ajak@35.58  interaksi.@35.88
- **s07** start 36.5667 dur 7.4333 (end 44.0): Sisanya?@36.85  Caption,@37.74  carousel,@38.40  story,@38.96  balas@39.56  komentar,@39.94  DM,@40.58  sampai@40.84  bersihin@41.78  tulisan@42.12  dari@42.52  gaya@42.76  khas@43.16  AI.@43.44
- **s08** start 44.0 dur 4.8 (end 48.8): Pasangnya@44.40  gampang.@45.34  Tempel@45.88  link@46.49  repo-nya@46.62  ke@46.95  Claude,@47.10  suruh@47.34  install.@47.88  Selesai.@48.14
- **s09** start 48.8 dur 4.5667 (end 53.3667): Tenang,@49.12  nggak@50.04  ada@50.22  yang@50.44  keposting@50.56  sendiri.@50.90  Semuanya@51.28  draf,@52.06  kamu@52.38  yang@52.92  posting.@52.98
- **s10** start 53.3667 dur 4.4333 (end 57.8): Mau@53.67  link-nya?@53.93  Komen@54.59  TIM,@55.04  aku@55.28  kirim@55.71  lewat@56.03  DM.@56.19
