# SCENE BUILD BRIEF — "10 gaya animasi Claude" (AI PRENEUR reel, remake) — overlay scenes

Project root: `projects/anim10_2026/` · 1080×1920 · 30 fps · 46.5667 s · HyperFrames 0.8.186.
Story: the AI PRENEUR robot is re-rendered into 10 animation genres (one ROUND each, r1–r10), after a hook (s01) and before a CTA
"Komen PROMPT" (s12). The client wants top-designer motion, nothing AI-looking, never boring, and NOT a copy of the reference reel
(the reference = an office worker walking in 10 styles with a numbered list on the left; we use our robot, a stage, a strip).

## What already exists (do NOT edit these — they are shared host layers)
Paint order (DOM order = paint order): navy background · **stage** · **scene slots s01, r1–r10, s12 (YOUR files)** · **title** · **strip** ·
mascot · logo + grain · captions.
- `compositions/stage.html` — the STAGE: an 820×980 screen at **x 130–950, y 450–1430** (radius 34) where StyleBot renders the robot in a
  small office set (desk + monitor with bar chart at the left, standing chart board at the right, plant bottom-right, window, wall clock
  top-right). It already does: the hook flicker through all 10 styles, the cyan "re-render" SWEEP into each round's style right on the
  spoken style name (`ROUNDS[i].sweep = [s0, s1]` global), camera moves, and the robot's acting per genre (see `ACT` in stage.html:
  lego = hop + wave, glow = rise + present, comic = punch + point at "panel", chalk = nod + point at the board on "kapur", pixel = two jumps
  (on the sweep end and on "game"), line = slow turn + soft wave, explainer = present + nod, ps2 = turntable spin, flat = glide in from the
  left + wave, cgi = ascend + cheer). `window.__STAGE.styleAt(t)` tells which style is on screen. At the CTA the stage shrinks to scale 0.6
  and moves up 258 px (new box ≈ **x 294–786, y 388–976**) and keeps cycling through the 10 styles.
- `compositions/title.html` — ROUND TITLE chip (cyan number badge + navy pill "Lego Style") straddling the stage top edge at
  **x 152–~620, y 414–498**, during every round. Keep that area clear.
- `compositions/strip.html` — 10 style chips (thumbnails `assets/thumbs/<style>.png`, 144 px) at **y 316–388, x 135–945** + progress line
  y 404; chips drop in on "Tahan" (hook) and flip open at each sweep; hidden from the CTA start (s12 takes over).
- Mascot (host) bottom-left: head top ≈ y 1440, x 20–330. Captions (word chips) centred at **y 1328–1400** (one line, on the stage floor).
  Logo top-left y 262–300.
- `vendor/rounds.js` (loaded globally): `window.ROUNDS` [{k, id, style, name, a, b, start, dur, tNum, tName, sweep:[s0,s1], tDesc,
  speechEnd}], `window.HOOK`, `window.CTA`, `window.TOTAL`. All GLOBAL seconds. Your scene's local time = global − start.
  `window.VO_WORDS` = [text, start, end, isCyan, spoken] for every word.
- SFX already exist for: number slam (tNum), sweep scan, a genre stinger at sweep[1] (lego brick clicks, glow neon shimmer, comic POW,
  chalk scratch, pixel 8-bit arpeggio, line pen stroke, explainer marimba, ps2 synth pad, flat UI pops, cgi braaam), chip flip, a pop on
  tDesc. Sync your accents to these moments.

Look at it rendered first: `npx --yes hyperframes@0.8.186 snapshot . -o <your scratch dir> --at <times> --no-end --describe false --timeout 60000`
(≤ 8 `--at` per run; each run takes ~1 min because the stage WebGL engine warms up). Read the PNGs.

## YOUR JOB: the overlay scenes (they paint ABOVE the stage, BELOW the title/strip/captions)
Each round overlay adds GENRE EMBELLISHMENTS that make the style feel authentic and fun, timed to the VO words of its round. They must
stay **inside the stage box** (clip to it: wrap everything in a div at left 130, top 450, 820×980, `overflow:hidden; border-radius:34px`),
avoid the robot (centre of the stage, roughly stage-local x 250–600, y 330–800 — check the snapshots, the camera moves), avoid the title
(stage-local top-left 0–500 × 0–60) and the caption band (stage-local y 870–960). Good zones: stage-local top-right (x 520–800, y 60–330),
the left wall (x 20–230, y 80–520), around the robot's edges. Max 2–3 embellishment beats per round; elegant, not cluttered.
Embellishments appear AFTER the sweep lands (`sweep[1]`), and leave by the round end (`start + dur`) with a quick exit (the next sweep
starts ~0.35 s after the next round starts — be gone by `start + dur`).

### Per-round ideas (make them great; you may improve them, but stay in genre)
- **r1 Lego** ("Kayak mainan yang hidup"): toy bricks (2×4 / 2×2 with studs, drawn in SVG/CSS, glossy ABS red/yellow/blue/green) drop in
  and SNAP-stack in the stage's top-right on the brick-click SFX (sweep[1]); on "hidup" a little "klik!" burst. Stop-motion feel: animate
  in steps (12 fps — use `steps()`-like per-value `tl.set` or quantised times).
- **r2 Glow Sketch** ("Garis neon nyala di ruang gelap"): a glowing gold/cyan pen line draws itself (SVG stroke-dashoffset) around the
  robot as a sketchy orbit/underline on "garis", tiny sparkles; on "nyala" the line flares (glow pulse).
- **r3 Comic** ("lengkap sama panel dan balon kata"): on "panel" two black gutter lines slice the stage into comic panels for a beat
  (white gutters, slight offset, then they slide out); on "balon kata" a white speech bubble (black 4px ink outline, tail toward the robot's
  head) pops with "Halo! Aku robot AI PRENEUR!" (Poppins 700, black). A small yellow caption box top-left under the title is OK.
- **r4 Chalkboard** ("Gambar kapur, pas buat konten edukasi"): chalk-drawn annotations (white/pastel strokes with a rough, grainy edge:
  SVG with feTurbulence-free tricks, e.g. dashed jittered paths or a chalk texture via a repeating noise PNG you generate offline with
  Python into `assets/fx/`): an arrow to the robot with a label "ini robot", a circled "A+" on "edukasi", an underline scribble.
- **r5 Pixel Art** ("Retro, kayak game jadul"): pixel-art coins (SVG rects, crisp, `shape-rendering: crispEdges`) pop "+100" above the
  robot on each of its two jumps (sweep[1] and "game"), with a pixel sparkle; a small pixel "LEVEL 5" or "1UP" banner. Steps at 10 fps.
- **r6 Minimal Line** ("Cuma satu garis, tapi elegan"): ONE thin white continuous line draws across the dark stage (dashoffset, ~1.4 s)
  — e.g. it enters left, loops once gracefully around the robot and exits right — with a tiny dot pen-tip; on "elegan" it settles into a
  hairline underline. Nothing else. Very minimal.
- **r7 Explainer 3D** ("Lembut, cocok buat jelasin produk"): product-explainer callouts: 2–3 soft rounded label chips (pastel, white text
  on soft navy or navy text on white) with thin leader lines + dots pointing to robot parts: "Layar wajah", "Logo AI PRENEUR", "Tangan
  melayang" — they appear on "jelasin produk". Soft springy easing.
- **r8 PS2** ("Kotak-kotak khas game tahun 2000-an"): a 2000s console-game CHARACTER-SELECT frame: ◄ ► arrows at the stage sides
  (bobbing), a bottom-left plate "ROBOT • AI PRENEUR" and 3 chunky stat bars (KECEPATAN / KEKUATAN / GAYA) filling up; a subtle scanline
  overlay; generic, NO PlayStation logos/fonts/sounds.
- **r9 Flat Vector** ("Rapi, aman buat brand"): clean flat geometric confetti (circles, plus signs, squiggles, half-circles) pops around
  the robot on the sweep, then on "brand" a neat 4-swatch "brand kit" palette row (navy, cyan, white, coral) slides in at the top-right.
- **r10 CGI Motion** ("Sinematik, kayak cuplikan film"): cinematic letterbox bars slide in (inside the stage) on "sinematik", a soft
  anamorphic lens-flare streak (horizontal cyan) crosses on the sweep, a small film slate/timecode label "SCENE 10 · TAKE 1" in the
  letterbox. This is the finale: premium and restrained.

### s01 HOOK (0 → 5.9667 s) — "Robot ini aku ubah jadi 10 gaya animasi, semuanya pakai Claude. Tahan sampai nomor 10."
The stage pops in at 0 and flickers through the 10 styles from HOOK.tRobot+0.15 (0.53) to HOOK.tAnimasi (2.457). Free zone: **y 300–440**
(above the stage, until the strip drops at HOOK.tTahan = 4.87; vacate it by 4.85) + the stage itself for small accents.
- Kinetic headline above the stage: on "10" (1.681) a big cyan "10" slams, "GAYA ANIMASI" (white, Poppins 700) rises in word by word on
  "gaya" (2.09) / "animasi." (2.457). While the stage flickers, a small style-name chip under/over the stage bottom edge flicks through
  the names in sync with the flicker (window.__STAGE.styleAt is available, or recompute: flicker step k from 0.53 every
  (2.457−0.53)/10 s, order = ROUNDS[k].name).
- On "Claude." (4.057) a Claude chip pops: the Claude mark `assets/icons/lobe-claude-color.svg` (MIT, lobehub) + "Claude" in white
  bold — next to/under the headline. (Never redraw the logo.)
- On "Tahan" (4.87) the headline + Claude chip lift away (the strip drops into that space); on "nomor 10." (5.559) add a small cyan
  pointer/arrow above chip 10 of the strip (chip 10 centre x = 135 + 9·82 + 36 = 909, y 352) that bounces until 5.95.

### s12 CTA (41.6 → 46.5667) — "Mau prompt kesepuluh gaya ini? Komen PROMPT, aku kirim lewat DM."
At 41.6 the strip hides and the stage shrinks to the box x 294–786, y 388–976 over 0.6 s (and keeps cycling styles). Free zone:
**y 990–1300** (+ around the shrunk stage, x 60–280 and 800–1020, y 300–980). Captions at y 1328.
- The ten thumbnails take over from the strip at 41.6 exactly (same positions: chip i at x 135+82·i, y 316, 72 px, radius 18,
  `assets/thumbs/<style>.png`, small number badge bottom-left) and fly into two vertical columns of 5 flanking the shrunk stage
  (left column x ≈ 120–210, right x ≈ 870–960, y 400–960), lightly tilted, on "kesepuluh gaya ini" (42.43).
- A comment row slides up at y ≈ 1040–1140 on "Komen" (43.54): avatar circle, input field; "PROMPT" types itself in big cyan Poppins 700
  on "PROMPT," (43.786) (per-letter `tl.set` windows), a heart pops. On "kirim" (44.44) a paper plane (`assets/icons/lucide-send.svg`,
  CSS mask) flies from the comment row to a DM card that slides in (y ≈ 1160–1290): "📩 DM · Prompt 10 gaya animasi — terkirim ✓"
  (no emoji in the render: use lucide-message-circle / lucide-check icons) on "DM." (44.94).
- Last ~1.2 s: a soft end beat (e.g. the DM card glows, a small "AI PRENEUR" white wordmark `assets/brand/logo_white_trim.png` under it).

## STYLE LOCK (client rules)
- Text: **Poppins 700/400 only** (fonts already loaded by the host), colours: white `#ffffff`, cool `#e3edfa`, cyan `#01ccf7` / `#6adfff`,
  navy chips `rgba(8,14,46,.85)`. Genre-specific colours are allowed INSIDE the stage (comic yellow, lego bricks, chalk white, pixel palette).
- Icons: `assets/icons/lucide-*.svg` (ISC; available: lock, lock-open, sparkles, message-circle, send, heart, wand-sparkles, play, check,
  mouse-pointer-click, arrow-down, corner-down-right, film, clapperboard). Need another? It is in
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/` — copy it in.
- No people photos, no brand logos except the Claude mark above and our own AI PRENEUR logo. Nothing AI-generated.

## Code conventions (deviations break the render)
- File = `<template>` + `<style>` + ONE root `<div data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>` IIFE.
  The runtime STRIPS the root's id → use `document.getElementById` on unique PREFIXED ids (`r3-…`); prefix classes and SVG ids too.
- Timeline: `const tl = gsap.timeline({ paused: true })`, the `_sc` scale patch, `ft` = fromTo with `immediateRender:false`, `I(el, vars)` =
  `gsap.set` + `tl.set(…, 0)`, end with `tl.set({}, {}, DUR - 0.01)`, the seek-order render patch, `window.__timelines["ID"] = tl`.
  Copy the boilerplate from `/home/user/testing-hyperframes/projects/repo9_2026/compositions/s01.html` (lines 33–43 and 73–76).
  DUR = the scene's `dur` (r-k: ROUNDS[k-1].dur; s01 5.9667; s12 4.9667). Timeline length must be ≤ DUR.
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (use per-value `tl.set`
  windows for counters/typing/stepped motion). One `attr`/clip-path tween per property; no `svgOrigin` inside CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen CSS filters/blur per frame (small `filter: drop-shadow` on small elements is OK);
  ≤ ~200 animated elements per scene.

## Mandatory checks
1. `node tools/check_scene.cjs <ids…>` → `ok <duration>` (shared preview server on :3014 is running; don't start another).
2. `npx --yes hyperframes@0.8.186 lint .` → no errors in your files.
3. Snapshots of every beat (several frames), the first and last frame of your scene. LOOK at them: legible at phone size, inside the
   stage, not covering the robot/title/captions, no blank frames.
4. Report briefly what you built and any risk. Do not commit. Do not edit any file but your own scenes (+ new assets you create under
   `assets/fx/`).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 5.9667: Robot@0.38  ini@0.57  aku@0.89  ubah@1.16  jadi@1.56  10@1.68  gaya@2.09  animasi.@2.46  Semuanya@3.30  pakai@3.81  Claude.@4.06  Tahan@4.87  sampai@5.24  nomor@5.36  10.@5.56
- **r1** start 5.9667 dur 3.1: Satu,@6.28  gaya@6.92  Lego,@7.24  kayak@7.96  mainan@8.18  yang@8.55  hidup.@8.63
- **r2** start 9.0667 dur 3.5: Dua,@9.23  Glow@9.78  Sketch,@10.09  garis@10.77  neon@11.16  nyala@11.34  di@11.79  ruang@11.95  gelap.@12.13
- **r3** start 12.5667 dur 3.2: Tiga,@12.74  Comic,@13.29  lengkap@13.89  sama@14.37  panel@14.47  dan@14.83  balon@15.02  kata.@15.29
- **r4** start 15.7667 dur 3.8333: Empat,@16.01  Chalkboard,@16.55  gambar@17.34  kapur@17.76  pas@18.29  buat@18.51  konten@18.75  edukasi.@19.01
- **r5** start 19.6 dur 3.1333: Lima,@19.80  Pixel@20.36  Art,@20.60  retro,@21.13  kayak@21.54  game@21.80  jadul.@22.06
- **r6** start 22.7333 dur 3.5334: Enam,@22.96  Minimal@23.48  Line,@23.82  cuma@24.40  satu@24.60  garis@24.80  tapi@25.31  elegan.@25.64
- **r7** start 26.2667 dur 3.9333: Tujuh,@26.49  Explainer@27.00  3D,@27.55  lembut,@28.30  cocok@28.96  buat@29.40  jelasin@29.52  produk.@29.81
- **r8** start 30.2 dur 4.2: Delapan,@30.46  gaya@30.92  PS2,@31.52  kotak-kotak@32.35  khas@33.03  game@33.33  tahun@33.46  2000-an.@33.65
- **r9** start 34.4 dur 3.3667: Sembilan,@34.53  Flat@35.08  Vector,@35.38  rapi,@36.21  aman@36.92  buat@37.20  brand.@37.39
- **r10** start 37.7667 dur 3.8333: Sepuluh,@37.98  CGI@38.49  Motion,@38.89  sinematik,@39.76  kayak@40.59  cuplikan@40.80  film.@41.15
- **s12** start 41.6 dur 4.9667: Mau@41.91  prompt@42.18  kesepuluh@42.43  gaya@42.75  ini?@42.91  Komen@43.54  PROMPT,@43.79  aku@44.27  kirim@44.44  lewat@44.77  DM.@44.94

  - r1 lego: tNum 6.28 · tName 7.235 · sweep [6.795, 7.295] · tDesc 7.96 · end 9.0667
  - r2 glow: tNum 9.23 · tName 9.78 · sweep [9.34, 9.84] · tDesc 10.77 · end 12.5667
  - r3 comic: tNum 12.74 · tName 13.29 · sweep [12.85, 13.35] · tDesc 13.89 · end 15.7667
  - r4 chalk: tNum 16.01 · tName 16.55 · sweep [16.11, 16.61] · tDesc 17.34 · end 19.6
  - r5 pixel: tNum 19.8 · tName 20.36 · sweep [19.92, 20.42] · tDesc 21.13 · end 22.7333
  - r6 line: tNum 22.96 · tName 23.48 · sweep [23.04, 23.54] · tDesc 24.4 · end 26.2667
  - r7 explainer: tNum 26.49 · tName 27.0 · sweep [26.56, 27.06] · tDesc 28.3 · end 30.2
  - r8 ps2: tNum 30.46 · tName 31.52 · sweep [31.08, 31.58] · tDesc 32.35 · end 34.4
  - r9 flat: tNum 34.53 · tName 35.08 · sweep [34.64, 35.14] · tDesc 36.21 · end 37.7667
  - r10 cgi: tNum 37.98 · tName 38.492 · sweep [38.052, 38.552] · tDesc 39.76 · end 41.6
