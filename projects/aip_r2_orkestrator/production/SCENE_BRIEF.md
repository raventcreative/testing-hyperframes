# SCENE BUILD BRIEF — "Bikin alat penyusun prompt sendiri, gratis" (AI PRENEUR reel remake) · LIGHT background

Project root: `projects/promptbuilder_2026/` · 1080×1920 · 30 fps · 45.2333 s · HyperFrames 0.8.186.
VO (client's voice): "Stop beli prompt mahal-mahal. Bikin alat penyusun prompt sendiri, gratis. Prompt yang bagus punya 6 bagian: peran,
konteks, tugas, format, contoh, dan batasan. Masalahnya, nulis 6 bagian itu tiap hari, capek. Jadi, kita suruh Claude bikinin alatnya.
Cuma 5 langkah. Satu, buka Claude. Dua, tempel prompt pembuat alat yang aku kasih. Tiga, Claude langsung bikinin aplikasi kecilnya di
dalam chat. Empat, ketik ide singkat. Misalnya, rencana konten seminggu buat kedai kopi. Lima, alatnya nyusun jadi master prompt lengkap.
Tinggal salin. Nggak perlu kelas mahal, nggak perlu beli prompt. Mau prompt pembuat alatnya? Komen MASTER, aku kirim lewat DM."
A REMAKE of a reference reel (a talking head showing Gemini Canvas, 8 steps) — ours is faceless, uses Claude, 5 steps, and our own
6-part prompt anatomy. Client rules: premium motion, a different creative transition every scene, nothing AI-looking, never boring.

## Host layers (read; do not edit): index.html, robot.html, mascot.html, vendor/rounds.js
Paint order: light background (white → soft blue) with an ANIMATED grid top-right · **scenes (yours)** · robot · mascot · dark logo
(top-left y 262–300) · captions (navy gradient, Poppins, centred at **y ≈ 966–1030**, one line).
- Mascot (host) half body bottom-left, head top ≈ y 1140. Robot (co-host) bottom-right ≈ x 700–960, y 1340–1680; it TYPES on a holo
  keyboard during "ketik ide singkat … kedai kopi" (28.3–32.6 s), shakes its head on "capek" and "Nggak … beli".
- → **Hero zone y 290–935, x 60–1020** (x > 340 for y < 305: the logo). Nothing in y > 945.
- `window.ROUNDS` (vendor/rounds.js) = the 5 STEPS r1–r5 { k, start, dur, tNum, tName, tUse, words } (global s).

## THE VISUAL SYSTEM (shared by all scenes — keep it consistent)
- **The 6 prompt blocks** (our anatomy, used in s02, s03, r5): rounded "puzzle" chips, each with a lucide icon + label and its own colour:
  PERAN (user-round, navy #294b77), KONTEKS (map-pin, blue #3a6fe0), TUGAS (list-checks, green #2da44e), FORMAT (layout-template,
  violet #7c5cff), CONTOH (lightbulb, gold #f4b400), BATASAN (shield, coral #e5484d). White text on the colour, radius 18, soft shadow.
  Copy the same CSS block into every scene that shows them.
- **The chat window** (r1–r5): a generic, clean chat app window (white, radius 30, title row with the Claude mark
  `assets/icons/lobe-claude-color.svg` + "Claude"), a message list and an input bar. Generic UI — never a pixel copy of a real product.
- **The tool** (r3–r5): a small app card inside the chat: "Penyusun Master Prompt" — an input "Ide singkat kamu", a button
  "Susun master prompt", an output area that fills with the 6 blocks, a "Salin" button.

## YOUR SCENES (ideas; make them better; every beat lands on its spoken word — see the timing table)
- **s01 HOOK** (0–5.03) "Stop beli prompt mahal-mahal. Bikin alat penyusun prompt sendiri, gratis." — frame 0 must already show
  content: a rack of generic "prompt pack" cards with price tags ("Rp 499.000", "Rp 1,2 jt" — generic examples) and a "Kelas Prompt"
  ticket; on "Stop" a big navy STOP stamp slams + the tags get struck; on "Bikin alat" the 6 blocks fly in and snap into a little
  machine/tool; on "gratis." a "Rp 0 · GRATIS" stamp (green) lands.
- **s02** (5.03–11.80) "Prompt yang bagus punya 6 bagian. Peran, konteks, tugas, format, contoh, dan batasan." — a big empty "prompt"
  document; on each spoken name its block drops into its slot (stacking into a complete prompt).
- **s03** (11.80–15.87) "Masalahnya, nulis 6 bagian itu tiap hari, capek." — the 6 blocks have to be rebuilt again and again: a day
  calendar flips (Sen, Sel, Rab…) and the blocks pile up/tilt; a "capek" beat (the pile wobbles and collapses, a sweat-drop/clock icon).
- **s04** (15.87–19.40) "Jadi, kita suruh Claude bikinin alatnya. Cuma 5 langkah." — the Claude chip (mark + "Claude") arrives and the
  pile turns into the tool; on "5 langkah" a 5-step rail appears (5 numbered dots) at the top of the hero zone — **the step rail stays
  visible in r1–r5** (each r-scene draws it in the same place: x 140–940, y 300–360, the current step active, done steps checked).
- **RAIL SPEC (exact, shared by s04 and r1–r5 so the cut is invisible)**: 4 px line from x 166 to 914 at y 330 (colour #d5e0f0; the
  part up to the active step navy gradient). 5 dots, 52 px circles, centres x = 166 + i·187 (166, 353, 540, 727, 914), y 330.
  Upcoming: white fill, 2 px border #c9d6ea, number Poppins 700 22 px #294b77. Active: fill linear-gradient(135deg,#0a0d2c,#294b77),
  white number, a soft 8 px ring rgba(41,75,119,.18). Done: fill #2da44e with a white lucide check (24 px). In s04 the rail ends with
  all 5 upcoming; each r-scene k starts with steps < k done, step k becomes active on its number word (tNum), and ends with step k done.
- **r1** (19.40–21.10) "Satu, buka Claude." — the chat window opens (scale/clip reveal) under the rail.
- **r2** (21.10–24.13) "Dua, tempel prompt pembuat alat yang aku kasih." — a clipboard chip "Prompt pembuat alat" flies in and pastes
  into the input as a long message bubble (fast scrolling text lines), sent.
- **r3** (24.13–28.00) "Tiga, Claude langsung bikinin aplikasi kecilnya di dalam chat." — a reply builds the tool card inside the chat
  (skeleton → real UI, with a little "membuat…" progress).
- **r4** (28.00–33.20) "Empat, ketik ide singkat. Misalnya, rencana konten seminggu buat kedai kopi." — the tool's input types
  "rencana konten seminggu buat kedai kopi" (per-letter tl.set, synced with the robot typing), then the button presses.
- **r5** (33.20–37.17) "Lima, alatnya nyusun jadi master prompt lengkap. Tinggal salin." — the output fills with the 6 blocks, each
  with a short filled line (e.g. PERAN: "Kamu content strategist kedai kopi…"), on "salin" the Salin button → "Tersalin ✓".
- **s10** (37.17–39.93) "Nggak perlu kelas mahal, nggak perlu beli prompt." — the s01 class ticket and a prompt pack return and get
  crossed out / torn; the tool card stays proud in the middle.
- **s11 CTA** (39.93–45.23) "Mau prompt pembuat alatnya? Komen MASTER, aku kirim lewat DM." — a comment row, "MASTER" types itself big
  (navy gradient) on "MASTER,", a heart pops; a paper plane carries a "Prompt pembuat alat" card into a DM card ("terkirim ✓") on "DM.";
  calm end beat with the dark logo `assets/brand/logo_dark_trim.png` (the small corner logo fades out at 44.0 s).

## STYLE LOCK (client rules)
- Text **Poppins 700/400 only**; headings in the navy gradient `linear-gradient(172deg,#0a0d2c 8%,#294b77 92%)` (background-clip text),
  small text #0a0d2c / #294b77 / #5d6f8f. White cards `linear-gradient(180deg,#fff,#f6f8fd)`, radius 24–34, soft navy shadows.
- Icons: `assets/icons/lucide-*.svg` (ISC) — copy any you need from
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/` into
  `assets/icons/lucide-<name>.svg`. Brand: only the Claude mark and our AI PRENEUR logo. No people photos, nothing AI-generated.

## Code conventions (deviations break the render)
- `<template>` + `<style>` + ONE root `<div id="root" data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>` IIFE;
  the runtime strips the root id → `document.getElementById` on unique PREFIXED ids (`r3-…`); prefix classes and SVG ids.
- Timeline boilerplate exactly as `/home/user/testing-hyperframes/projects/bankanim_2026/compositions/s01.html` (`_sc` patch, `ft`, `I`,
  `tl.set({}, {}, D - 0.01)`, seek-order patch, `window.__timelines["ID"] = tl`). D = scene dur. Beats via `wt(word, after)` on
  `window.VO_WORDS` (words: [text, start, end, …], global s; local = global − scene start).
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (per-value tl.set).
  Give every fromTo COMPLETE from-values. One attr/clip-path tween per property; no svgOrigin in CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen blur per frame; ≤ ~250 animated elements per scene.
- **Hand-overs**: scenes that share an element (the 6 blocks s02→s03→s04, the chat window r1→r5, the rail r1→r5) must end/start in
  EXACTLY the same state (same positions/sizes) so the cut is invisible. Write down each scene's end state in a comment at its top.

## Checks (mandatory)
1. `node tools/check_scene.cjs <ids>` → `ok <dur>` (shared preview server on :3017).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`… snapshot . -o <scratch> --at <≤8 times> --no-end --describe false --timeout 90000`): first frame, every beat, last
   frame, and the frames either side of each cut. LOOK at them: legible on a phone, in the hero zone, nothing over captions/characters.
4. Report briefly. Do not commit. Edit only your scene files (+ assets you add).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 5.0333 (end 5.0333): Stop@0.33  beli@0.53  prompt@0.90  mahal-mahal.@1.06  Bikin@2.38  alat@2.80  penyusun@2.97  prompt@3.26  sendiri,@3.35  gratis.@4.08
- **s02** start 5.0333 dur 6.7667 (end 11.8): Prompt@5.35  yang@5.78  bagus@5.89  punya@6.15  6@6.42  bagian.@6.69  Peran,@7.53  konteks,@8.16  tugas,@8.96  format,@9.60  contoh,@10.34  dan@10.89  batasan.@11.11
- **s03** start 11.8 dur 4.0667 (end 15.8667): Masalahnya,@12.12  nulis@12.76  6@13.26  bagian@13.42  itu@13.84  tiap@14.00  hari,@14.28  capek.@15.12
- **s04** start 15.8667 dur 3.5333 (end 19.4): Jadi,@16.08  kita@16.67  suruh@16.90  Claude@17.20  bikinin@17.38  alatnya.@17.72  Cuma@18.53  5@18.76  langkah.@18.89
- **r1** start 19.4 dur 1.7 (end 21.1): Satu,@19.70  buka@20.40  Claude.@20.73
- **r2** start 21.1 dur 3.0333 (end 24.1333): Dua,@21.36  tempel@22.09  prompt@22.62  pembuat@22.80  alat@23.10  yang@23.37  aku@23.45  kasih.@23.60
- **r3** start 24.1333 dur 3.8667 (end 28.0): Tiga,@24.46  Claude@25.22  langsung@25.65  bikinin@26.12  aplikasi@26.37  kecilnya@26.79  di@27.18  dalam@27.29  chat.@27.48
- **r4** start 28.0 dur 5.2 (end 33.2): Empat,@28.30  ketik@28.95  ide@29.54  singkat.@29.65  Misalnya,@30.12  rencana@30.97  konten@31.59  seminggu@31.91  buat@32.32  kedai@32.49  kopi.@32.71
- **r5** start 33.2 dur 3.9667 (end 37.1667): Lima,@33.46  alatnya@33.95  nyusun@34.56  jadi@35.04  master@35.15  prompt@35.46  lengkap.@35.69  Tinggal@36.46  salin.@36.77
- **s10** start 37.1667 dur 2.7666 (end 39.9333): Nggak@37.33  perlu@37.78  kelas@37.94  mahal,@38.21  nggak@38.66  perlu@39.08  beli@39.36  prompt.@39.56
- **s11** start 39.9333 dur 5.3 (end 45.2333): Mau@40.22  prompt@40.56  pembuat@40.79  alatnya?@41.05  Komen@41.87  MASTER,@42.15  aku@42.90  kirim@43.15  lewat@43.44  DM.@43.61
