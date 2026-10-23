# V3 ADDENDUM — second client revision (wins over SCENE_CONTRACT.md and V2_ADDENDUM.md where they differ)

Project: `projects/interview-ai-v3/` (v1, v2 frozen — never edit them).

## Client feedback being addressed
- The set looked empty and the laptop floated. The interview now happens in a ROOM: shared module `assets/room.js`
  (window icon on the wall, wooden desk icon, laptop icon resting ON the desk top, desk lamp with warm light,
  plant, books, mug, wall shelf, floor/rug, window light shafts, rim-lit applicant seen from behind).
  Load it in a scene with `<script src="assets/room.js"></script>` inside `<template>` and call
  `const R = window.HFRoom.build(hostEl, "sNr")`. API: `HFRoom.cam(R, scale, x, y, frontExtraY)` (differential parallax
  around the laptop screen centre 650,843), `HFRoom.light(R, lamp0to1, windowShaft0to1)`, `HFRoom.act(R, globalTime, settle0to1)`
  (breathing only — the client disliked bigger body animation). `R.scr` = laptop screen div (world rect x477.5 y747 w345 h192.5),
  `R.L0/L1/L2` = wall / set / applicant layers. See `compositions/s01.html` for full usage (it is the reference).
- Motion must feel less stiff and transitions must VARY. Planned seams: S02→S03 zoom THROUGH the laptop screen;
  S06→S07 zoom THROUGH the window. Use motion blur on fast moves, anticipation and settle.
- Glow must be elegant: small, soft, never thick neon halos. Subtitles are handled by the root (do not touch).
- Light and shadow are part of the design: lamp warm pool, window shafts, contact + cast shadows on every object.

## v3c (client: logo top-left with slow motion, lamp light aligned, more life)
- Brand mark: user's white AI PRENEUR wordmark (`assets/branding/logo_aipreneur_white_user_crop.png`, cropped to alpha bbox) at left 64 / top 104, 320 px wide, outside `#gcam` so it never zooms.
  Motion (pure function of root time): 0.9 s soft entrance, float ±4 px (6.4 s), drift ±2 px (9.7 s), breathing scale ±1.2 % (5.3 s), tilt ±0.5° (8.1 s), cyan sheen sweep every 7 s. Fades out 91.9–92.4 before the end logo plate (no double logo).
- Lamp fix: head was rotated +32° (shade pointed left, off the desk) while cone/pool were drawn to the right. Head now −20° → bulb ≈ (348,866), axis hits desk ≈ (420,1068).
  Cone redrawn as a blurred SVG beam from the shade mouth to the pool; pool re-centred under the axis; warm halo at the bulb; slow ±4 % warmth breathing (no flicker).
- Ambient (room.js `ambient()`, called from `act()`): plant sway, two mug steam wisps, 14 dust motes drifting down the window shaft (behind the desk/laptop).
