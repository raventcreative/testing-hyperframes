# SCENE BUILD BRIEF — "Motivasi, disiplin, obsesi" · AI PRENEUR reel remake · LIGHT background

Project root: `projects/tigamental_2026/` · 1080×1920 · 30 fps · 26.3 s · HyperFrames 0.8.186.
VO (client's voice): "Tiga orang, target yang sama. Posting konten 100 hari. Motivasi semangat banget di awal. Hari ke-14, berhenti.
Disiplin jalan terus, pelan tapi pasti. Hari ke-100, target tercapai. Obsesi? Sampai 100, dia malah pasang target baru. 1.000.
Disiplin nyelesaiin target. Obsesi nyari gunung yang lebih tinggi. Kamu yang mana? Tulis di komen."
A REMAKE of `production/reference_sheet.png` (dark cinematic: 3 stick figures hammer a wall, counters 14 / 100 / 1,000; no VO). DO NOT
copy it — no stick figures, no wall, no hammers, no dark palette. Our metaphor is the client's world: **a 100-DAY POSTING STREAK**. Three
people = three lanes, each a **100-cell streak board** (like a contribution heatmap: 20 columns × 5 rows) that fills day by day.
Client rules: premium motion, a different creative transition every scene, nothing AI-looking, real/open-source assets only, never boring.

## Host layers (read; do not edit): index.html, compositions/robot.html, compositions/mascot.html
Paint order: light background (white → soft blue) with an ANIMATED grid top-right · **scenes (yours)** · robot · mascot · dark logo
(top-left y 262–300, fades out at the end) · captions (navy gradient, Poppins 50 px, centred at **y ≈ 966–1030**, one line).
- Mascot (host) half body bottom-left (in frame from 0), head top ≈ y 1140. Robot (co-host) bottom-right ≈ x 700–960, y 1340–1680,
  flies in on "orang," (~0.2 s): cheers on "semangat", shakes its head on "berhenti.", nods on "jalan"/"pasti.", claps on "tercapai.",
  thinks on "Obsesi?", shock on "1.000.", points up on "tinggi.", looks at the mascot on "mana?", cheers on "komen.".
- → **Hero zone y 290–935, x 60–1020** (x > 340 for y < 305: the logo). Nothing in y > 945.

## THE SYSTEM (keep it consistent across scenes)
- **The three people** (never photos/figures — badge avatars): a 76 px circle with a lucide icon + a name pill, each with its colour:
  MOTIVASI amber `#f4b400`→`#e8790c` (lucide flame), DISIPLIN blue `#3a6fe0`→`#294b77` (calendar-check), OBSESI violet `#7c5cff`→`#4b2fd6`
  (infinity). Before s02 they are "Orang 1/2/3" with neutral grey badges; each gets its name + colour in its scene.
- **The lane**: label column x 60–300 (badge, name, a big day counter "Hari 14" Poppins 700), board x 316–1020: 100 cells (20 × 5) of
  30 px with 5.5 px gaps, radius 7; empty cell #e6ecf6, filled cell = the person's colour (slight gradient), "today" cell glows.
  Right end: a small goal flag "100" (lucide flag). Three lanes stacked in the hero zone (≈ 190 px each).
- Counters/fills are per-value tl.set windows (no onUpdate). A deterministic seeded PRNG for any scatter.

## YOUR SCENES (ideas; make them better; every beat lands on its spoken word — see the timing table)
- **s01 HOOK** (0–4.53) "Tiga orang, target yang sama. Posting konten 100 hari." — frame 0 already striking (the 3 badges + a huge
  "100 HARI" target already on screen, not an empty frame); on "Tiga orang," the three badges pop into their lanes; on "target yang sama."
  one goal flag "100" splits into three, one per lane; on "Posting konten 100 hari." the 3 empty boards draw in (cells cascade) with a
  tiny "posting" icon tick.
- **s02 MOTIVASI** (4.53–8.60) — lane 1 gets its name/colour and comes forward (the others dim/recede); "semangat banget di awal." =
  cells fill FAST in bursts with a flame flare, counter races; on "Hari ke-14," it hits 14 and stutters; on "berhenti." the flame goes out
  (a smoke puff), the lane desaturates, a "BERHENTI · hari 14" stamp lands; the other 86 cells stay empty.
- **s03 DISIPLIN** (8.60–14.33) — lane 2 forward; a steady metronome rhythm: one cell per tick ("pelan tapi pasti"), then a time-lapse
  fill (the counter rolls) reaching 100 exactly on "ke-100,"; on "tercapai." the flag becomes a green ✓ "TARGET TERCAPAI" with a crisp
  deterministic confetti burst.
- **s04 OBSESI** (14.33–18.60) — lane 3 forward; "Sampai 100," = fast-forward to a full board; "dia malah pasang target baru." = the flag
  is pulled out and replanted further away; on "1.000." the camera ZOOMS OUT: the 100-board becomes a small tile inside a huge 1.000-cell
  board (40 × 25) with a new flag "1.000", the counter ticks 100 → 101.
- **s05 COMPARE** (18.60–22.67) "Disiplin nyelesaiin target. Obsesi nyari gunung yang lebih tinggi." — a clean flat-vector mountain
  scene (SVG layers, our colours, no stock art): on "Disiplin" the blue badge stands on a summit flag "100 ✓"; on "Obsesi" a second, much
  taller violet peak rises behind it; on "lebih tinggi." the view tilts/pans up to its summit marked "1.000".
- **s06 CTA** (22.67–26.30) "Kamu yang mana? Tulis di komen." — the three badges return as three poll cards (Motivasi / Disiplin /
  Obsesi); on "mana?" they bob in turn; on "Tulis di komen." a comment row slides up (avatar circle with lucide user-round, input) and types
  "Aku tim Disiplin" (per-letter tl.set), send → a heart pops; calm end beat with the dark logo `assets/brand/logo_dark_trim.png` (the
  corner logo fades out at 25.1 s).

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
- **Hand-overs**: scenes that share an element (the 3 lanes s01→s04, the mountains in s05) must end/start in
  EXACTLY the same state (same positions/sizes) so the cut is invisible. Write down each scene's end state in a comment at its top.

## Checks (mandatory)
1. `node tools/check_scene.cjs <ids>` → `ok <dur>` (shared preview server on :3019).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`… snapshot . -o <scratch> --at <≤8 times> --no-end --describe false --timeout 90000`): first frame, every beat, last
   frame, and the frames either side of each cut. LOOK at them: legible on a phone, in the hero zone, nothing over captions/characters.
4. Report briefly. Do not commit. Edit only your scene files (+ assets you add).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 4.5333 (end 4.5333): Tiga@0.33  orang,@0.42  target@1.29  yang@1.62  sama.@1.84  Posting@2.63  konten@3.11  100@3.58  hari.@3.75
- **s02** start 4.5333 dur 4.0667 (end 8.6): Motivasi@4.78  semangat@5.44  banget@5.82  di@6.03  awal.@6.28  Hari@6.93  ke-14,@7.17  berhenti.@7.95
- **s03** start 8.6 dur 5.7333 (end 14.3333): Disiplin@8.93  jalan@9.42  terus,@9.63  pelan@10.40  tapi@10.87  pasti.@10.95  Hari@12.02  ke-100,@12.26  target@13.08  tercapai.@13.42
- **s04** start 14.3333 dur 4.2667 (end 18.6): Obsesi?@14.56  Sampai@15.38  100,@15.82  dia@16.34  malah@16.52  pasang@16.80  target@17.04  baru.@17.20  1.000.@17.99
- **s05** start 18.6 dur 4.0667 (end 22.6667): Disiplin@19.11  nyelesaiin@19.64  target.@19.95  Obsesi@20.71  nyari@21.29  gunung@21.59  yang@21.88  lebih@21.95  tinggi.@22.09
- **s06** start 22.6667 dur 3.6333 (end 26.3): Kamu@22.85  yang@23.23  mana?@23.27  Tulis@23.92  di@24.19  komen.@24.23
