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
