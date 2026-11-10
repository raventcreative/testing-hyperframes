# SCENE BUILD BRIEF — "Bank animasi bikinan Claude" (AI PRENEUR reel, remake)

Project root: `projects/bankanim_2026/` · 1080×1920 · 30 fps · 29.2 s · HyperFrames 0.8.186 (`npx --yes hyperframes@0.8.186 …`).
Story (VO, Indonesian): "This video wasn't edited in After Effects, it was all made with Claude. Including this animation bank:
check, loading, counter, notification, chart. All smooth, like a motion designer made it. Easy: copy one command, paste it into
Claude Code, the animation is done. Just change the text and the data, fits your own content. No app to install, no editing skills.
Want the guide and the bank? Comment EDIT, I'll DM it." It is a REMAKE of a Spanish reel (talking head + screen recording of an
animation bank); ours is faceless, everything on screen is coded, and it must not look like the reference.
The client wants top-designer motion, a different creative transition every scene, nothing AI-looking, never boring.

## Already built (read them; do not edit them)
- `index.html` (host): light background (white → soft blue) with an ANIMATED grid top-right, dark AI PRENEUR logo top-left (y 262–300),
  word-synced captions (navy gradient, Poppins) centred at **y ≈ 966–1030** (one line), the mascot (host, half body, bottom-left,
  head top ≈ y 1140, x 120–650) and the robot (co-host, bottom-right, x ≈ 700–960, y ≈ 1340–1680; it TYPES on a holo keyboard
  during "Copy … jadi." and "ganti teks", shakes its head on "install" / "jago").
  → Your **hero zone is y 290–935, x 60–1020** (keep x > 340 for y < 305 because of the logo). Nothing in y > 945.
- `vendor/microanim.js` = **the animation bank** (`window.MicroAnim`): 12 hand-coded UI micro-animations (check, loading, counter, bell,
  chart, toggle, heart, ring, typing, upload, search, stars), labels in Indonesian. `MicroAnim.mount(parent, type, {size, label, id})`
  → handle `{ el, draw(t) }`; **draw from GLOBAL time** in an `hf-seek` listener (see s02). `MicroAnim.grid(parent, prefix)` builds
  all 12 cards at `MicroAnim.GRID` (4×3 cards of 190 px, x 127…, y 300 / 512 / 724). Look at `tools/kit_test.html`.
  You may build bigger cards with `mount(..., {size: 380})`; you may add NEW micro-animation types inside your own scene file if a beat
  needs one (same style: white card, navy ink, blue #3a6fe0, green #2da44e, coral #e5484d, gold #f4b400).
- `compositions/s01.html` (hook: an editing-app timeline whose clips fall off → a dark code window types → Claude chip) and
  `compositions/s02.html` (the code window compiles into a flash and the 12 cards burst out onto the GRID). Copy their boilerplate.

## HAND-OVER CONTRACT (this is what makes the scene changes seamless)
- **Every scene starts on the GRID** (12 cards built with `MicroAnim.grid`, at rest, opacity 1) **and ends on the GRID** — except s08,
  which may end on its own CTA end card. Because every card is drawn from global time, the cards look identical across the cut.
- What happens between start and end is yours: zoom, lift, fly, fold, re-arrange, cover them with UI — but by the scene's last frame
  the 12 cards are back exactly at GRID (x/y/scale/rotation reset, opacity 1) and every extra element of yours is gone.
- Every scene must open with a fresh, distinct transition idea (no two scenes alike), timed to the VO words below.

## YOUR SCENES (ideas; make them better, stay true to the words)
- **s03** "Centang, loading, angka naik, notifikasi, grafik." — a SPOTLIGHT run: on each spoken word, that card (check / loading /
  counter / bell / chart) lifts out of the grid and enlarges (≈ 2×) to the hero centre while the others dim and recede; the next word
  swaps it (the previous one flies back home). ~0.65 s per word. Back to GRID by the end.
- **s04** "Semuanya gerak halus, kayak bikinan motion designer." — "gerak halus": the whole grid does one silky wave (stagger by
  distance); "motion designer": a sleek EASING-CURVE editor panel (bezier curve with two handles, a dot travelling the curve, a
  "ease-in-out" label, a mini timeline with keyframes) glides in over the grid and drives one card's motion; it leaves at the end.
- **s05** "Caranya gampang. Copy satu perintah, tempel ke Claude Code, animasinya langsung jadi." — the grid parks (shrinks to a band
  or slides up); a PROMPT card with a Copy button: a cursor clicks Copy on "Copy" (ripple, "Tersalin ✓"); on "tempel ke Claude Code"
  a generic dark terminal window titled with the Claude mark (`assets/icons/lobe-claude-color.svg`) + "Claude Code" receives the
  pasted prompt (fast typing, per-value tl.set); on "langsung jadi" Enter → a progress line → a NEW card pops out of the terminal and
  lands in its grid slot. Never imitate a real product UI pixel-for-pixel; generic and clean.
- **s06** "Tinggal ganti teks sama datanya, cocok buat konten kamu sendiri." — LIVE EDIT: one card (counter or chart) enlarges next to
  a small inspector panel (fields "Teks", "Data", "Warna"); on "teks" the text field changes (e.g. "98%" → "Rp 25 jt") and the card
  updates; on "datanya" chart bars re-shape; on "konten kamu sendiri" the edited card drops into a phone frame (a generic social post
  frame with the AI PRENEUR logo as avatar, no people) — then everything returns to the GRID.
- **s07** "Nggak perlu install aplikasi, nggak perlu jago editing." — two quick "nope" beats: (1) a generic "Install aplikasi · 2,4 GB"
  download dialog with a progress bar gets stamped "GAK PERLU" (coral) and flicked away on "install"; (2) a crowded keyframe/graph-editor
  panel (many keyframes, curves) gets stamped/crossed on "jago editing" and folds away. Cards stay visible behind (dimmed) and settle.
- **s08 CTA** "Mau panduan sama bank animasinya? Komen EDIT, aku kirim lewat DM." — on "panduan … bank animasinya" the 12 cards fly into
  a "Panduan + Bank Animasi" bundle card (a neat folder/pack with the 12 mini icons, "12 animasi" badge); on "Komen" a comment row slides
  up (avatar circle with lucide user icon, input field), "EDIT" types itself big (per-letter tl.set) on "EDIT,", heart pops; on "kirim"
  a paper plane (`assets/icons/lucide-send.svg`, CSS mask) carries the bundle into a DM card ("Panduan & bank animasi — terkirim ✓",
  lucide message-circle / check) on "DM."; last ~1 s: a calm end beat (soft glow, the dark logo `assets/brand/logo_dark_trim.png`).

## STYLE LOCK (client rules)
- Text: **Poppins 700/400 only**; headings = navy gradient `linear-gradient(172deg,#0a0d2c 8%,#294b77 92%)` (background-clip text);
  small text solid #0a0d2c / #294b77 / #5d6f8f. Light, premium UI: white cards `linear-gradient(180deg,#fff,#f6f8fd)`, radius 24–34,
  soft navy shadows; dark panels allowed for code/terminal (#0a0d2c → #0f1638). Accents: blue #3a6fe0, green #2da44e, coral #e5484d.
- Icons: `assets/icons/lucide-*.svg` (ISC; CSS mask or inline paths) — need another? copy it from
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/`.
  Brand: only the Claude mark above and our AI PRENEUR logo. No Adobe/other logos, no people photos, nothing AI-generated.

## Code conventions (deviations break the render)
- File = `<template>` + `<style>` + ONE root `<div id="root" data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>`
  IIFE. The runtime strips the root id → use `document.getElementById` on unique PREFIXED ids (`s05-…`); prefix classes and SVG ids.
- Timeline boilerplate exactly as `compositions/s02.html` (`_sc` patch, `ft`, `I`, `tl.set({}, {}, D - 0.01)`, seek-order patch,
  `window.__timelines["ID"] = tl`). D = the scene's dur (table below). Timeline length ≤ D.
- Micro-animation cards: draw them in an `hf-seek` listener with GLOBAL time `e.detail.time + (window.__T0 || 0)` (as s02).
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (per-value tl.set
  windows for counters/typing). **Give every fromTo COMPLETE from-values** (a partial from starts the other props from the t=0 state).
  One attr/clip-path tween per property; no svgOrigin inside CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen blur per frame; ≤ ~250 animated elements per scene.

## Mandatory checks
1. `node tools/check_scene.cjs <ids…>` → `ok <duration>` (shared preview server on :3015 is running; don't start another).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`npx --yes hyperframes@0.8.186 snapshot . -o <your scratch dir> --at <≤8 times> --no-end --describe false --timeout 60000`):
   the FIRST frame (must equal the GRID), every beat (several frames), the LAST frame (must equal the GRID). LOOK at them. Legible at
   phone size (≥ 20 px text), inside the hero zone, nothing over the captions/mascot/robot, no blank frames.
4. Report briefly what you built + beat timings + risks. Do not commit. Edit only your own scene files (+ new assets under `assets/fx/`).

## VERIFIED TIMING (global s; local = global − start)
- **s01** start 0.0 dur 4.2667 (end 4.2667): Video@0.42  ini@0.66  nggak@0.94  diedit@1.09  di@1.54  After Effects,@1.60  semuanya@2.70  dibikin@3.23  pake@3.57  Claude.@3.75
- **s02** start 4.2667 dur 1.7 (end 5.9667): Termasuk@4.51  bank@5.03  animasi@5.12  ini.@5.50
- **s03** start 5.9667 dur 3.8 (end 9.7667): Centang,@6.25  loading,@6.94  angka@7.64  naik,@7.93  notifikasi,@8.41  grafik.@9.08
- **s04** start 9.7667 dur 2.9333 (end 12.7): Semuanya@9.90  gerak@10.47  halus,@10.79  kayak@11.30  bikinan@11.49  motion@11.87  designer.@12.04
- **s05** start 12.7 dur 5.0333 (end 17.7333): Caranya@13.04  gampang.@13.39  Copy@14.29  satu@14.69  perintah,@14.78  tempel@15.40  ke@15.77  Claude Code,@15.81  animasinya@16.50  langsung@16.95  jadi.@17.25
- **s06** start 17.7333 dur 3.4 (end 21.1333): Tinggal@18.02  ganti@18.36  teks@18.63  sama@18.86  datanya,@18.94  cocok@19.72  buat@20.18  konten@20.28  kamu@20.55  sendiri.@20.64
- **s07** start 21.1333 dur 2.9334 (end 24.0667): Nggak@21.40  perlu@21.63  install@21.79  aplikasi,@22.00  nggak@22.74  perlu@22.94  jago@23.24  editing.@23.56
- **s08** start 24.0667 dur 5.1333 (end 29.2): Mau@24.40  panduan@24.62  sama@24.98  bank@25.08  animasinya?@25.23  Komen@26.19  EDIT,@26.43  aku@26.96  kirim@27.13  lewat@27.46  DM.@27.63
