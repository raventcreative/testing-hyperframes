# SCENE CONTRACT — Interview Dibantu AI v1 (read fully before building a scene)

Project: `projects/interview-ai-v1/` (HyperFrames 0.8.185). Root `index.html` mounts `compositions/s01..s08.html` + `captions.html`
and loads `vendor/gsap/gsap.min.js`, `vendor/three/three.min.js` (r159, global `THREE`) and `assets/kit.css` (shared classes, apply inside scenes).
Reference implementation of the house look: **`compositions/s01.html`** — read it first and match its craft level.

## Format rules (HyperFrames)
- File = `<template>` with `<style>`, `<div id="root" data-composition-id="sNN" data-width="1080" data-height="1920">`, `<script>`.
  Style the root as `#root { position:absolute; inset:0; overflow:hidden; }`. Prefix every id/class with `sN-` (e.g. `s4-`).
- One paused GSAP timeline, absolute scene-local seconds, registered last: `window.__timelines["sNN"] = tl;`.
  Scene-local t = global t − scene start (see STORYBOARD.md).
- `fromTo` (not `from`). Never put a CSS `transform` on an element GSAP transforms — wrap it (static outer with CSS transform, animated inner).
- No `Date.now`, `Math.random`, timers, rAF, CSS animations/transitions, `repeat:-1`. Everything is a function of timeline time.
- Elements you build with JS at init are fine (static markup); visibility/motion only via the timeline.
- Avoid two tweens on the same property of the same element overlapping in time (lint `overlapping_gsap_tweens`).
- Assets root-relative (`assets/...`). No network.

## Look (locked)
- Background: the user's navy plate is the root layer — scenes are transparent; never paint a full-frame opaque background.
- Light: one soft key from the **upper-left**, cool cyan (#00c9ff) edge light from the right, subtle right fill. **Shadows fall down-right**.
  Every object that sits on or floats over something has a shadow: a tight dark *contact* patch (`.k-contact`) + a broad soft *cast* (`.k-cast`).
  Lifted objects: cast shadow moves further down-right, grows, softens and fades as height increases; contact patch shrinks/fades.
- Four planes: plate → stage/workstation (CSS 3D with `perspective` + `preserve-3d`) → tangible objects (paper, panels, rails, dials with
  visible thickness: stacked edge faces or real side faces) → camera-facing text plane (never rotated in 3D).
- Materials from `assets/kit.css`: `.k-paper` (ivory card with edge thickness), `.k-panel` (dark bezel), `.k-screen`, `.k-glass` (frosted —
  do NOT use inside a preserve-3d tree; backdrop-filter breaks there), `.k-signal` (cyan bead — the only glowing thing), `.k-metal`, `.k-pool` (light pool).
- Cyan is a *signal* colour (bead, waveform, active node, selector pointer). No blanket glow, no neon borders everywhere, no red, no gold.
- Camera: differential parallax by moving a world container in z / rotationX / rotationY inside a `perspective` parent (see `#s1-cam/#s1-world`).
  Never scale the whole frame flat. Moves ease both ways (`power2.inOut`), 3–8° orbits, 4–6% dollies.

## Typography (locked)
- Poppins only, 700 for hero copy, 400 for support/labels (bundled + `@font-face` in kit.css).
- Hero headline: `<div class="k-field">` block at left 90, top ≈214, width 900, lines as `<span class="sN-line"><span class="k-hl">…</span></span>`
  (block spans with `overflow:hidden` for masked reveals). `.k-field` makes one gradient field #00c9ff → #294b77 across the 900px block.
  Size 88–104px, 1–3 lines, must end above the stage (≈ y 560). Small counter `0N / 08` at left 90, top 186 (Poppins 400 22px, #8fb0d6).
- Copy is LOCKED exactly as in STORYBOARD.md (caps, punctuation, ellipsis “…”). No extra headline copy. Small object labels
  (e.g. “DRAFT”, “JAWABAN KAMU”) may use Poppins 700 20–30px letter-spaced, pale or #12284f on paper.
- Entrances: vary them (masked line rise `yPercent 105→0 expo.out 0.55–0.75s`, per-word blur 6px→0 in 0.13s 0.07s apart, whole-line blur-in).
  A landed title is dead still. Exit: blur 8px + fade 0.2s `power2.in`. Readable hold ≥ 0.5 s + 0.3 s/word.

## Layout / safe zones (1080×1920)
- Nothing in y < 168. Headline zone y 186–560. Stage/hero objects y 560–1330. Captions live at y ≈ 1418–1500 (root track) — keep
  that band free of important objects; decoration/shadow only below 1330. Key content within x 90–990.

## Motion grammar per beat
entry/anticipation → causal main action → apex on the VO word (time from STORYBOARD/vo_alignment) → settle + readable hold → handoff into the next beat.
Objects *do* things (hinge, fold, extrude, dock, click, slide on a rail). Arrivals `expo.out`/`power4.out`, camera `power2.inOut`, exits `power3.in`
and 40–50 % shorter than entries. Springs: closed-form or `back.out(1.2)` max on position only. Forbidden: idle breathing/pulsing loops,
everything fading+sliding up, titles that keep moving after landing, arbitrary spins, camera shake, click rings, permanent glow.

## Content rules
- UI is an illustrated concept, not a real product: no brand names, logos, app screenshots, fake data, numbers or scores.
- Never show how to hide AI from an interviewer or bypass detection.

## Check your work (from the project dir)
- `npx hyperframes lint` → 0 errors (fix warnings you caused).
- `npx hyperframes snapshot --at <global seconds,…> -o .hyperframes/<sceneid>` then Read the PNGs. Look at entry, apex, hold and exit frames,
  not only hero poses. Iterate at least twice. Fix: text overlapping objects, objects cut by the frame, flat cards with no thickness/shadow,
  dim unreadable text, empty frames.
