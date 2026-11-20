---
name: product-launch-film
description: 15-second 2D product launch film (1920x1080, 60 fps) in one continuous take — composer with an Apple-Intelligence iridescent glow, typed request, send → shared-element transformations (button → wok → colour flood → cards → chat → page → brand mark), beat-locked to a ~130 BPM Mixkit song with a drop, closed-form springs, log-space camera, 8-subframe motion blur. Use for "/product-launch-film", "launch video produk", "film peluncuran app", "video promo aplikasi gaya Apple", or any short app/product launch film in landscape.
---
# /product-launch-film

Full reference brief (the food-ordering example, keep as the quality bar): `references/brief_food_ordering.md`.

## Start protocol (always, before building)
1. **Ask for the inputs**: the product (name + what it does), the exact request a user types into it, 6–8 photos for
   the result cards, a royalty-free song ≈130 BPM with a clear drop (Mixkit, free for commercial use), the brand mark
   for the end card. Anything skipped → defaults: food-ordering story, Pexels food photos (fire noodles, birria tacos,
   hot chicken, buffalo wings, smash burger, spicy ramen), Mixkit "Cat Walk".
2. **Show the beat map** (32 beats @130 BPM = 14.8 s, song starts 12 beats before its drop; beats 0–6 ask, 6 send,
   6–12 think, 12 drop, 16–21 chat, 21–32 outro — adapt the story beats to the product) **and 4 stills** (ask, drop,
   chat, outro) rendered with `seek(t)` + Playwright. Wait for approval, then write the full film.

## Direction (non-negotiable)
- 2D only, ONE continuous take: no cuts, fades, crossfades, blur-ins, 3D, particles, template feel, holds > 1 s.
  Every scene grows from the last (text rises from a mask line, buttons expand into pages, colour floods from one object
  and shrinks into another).
- Camera: one eased move per scene, never zoom in then out consecutively, never reverse direction.
- Look: canvas #f5f5f2, UI black #0e0e10, lime #cdf24f, orange #ff6a2a, send blue #2f6bff; iridescent glow = blurred
  conic gradient rotating pink → orange → lime → cyan → violet around the input; real photos on dark cards; Geist for UI,
  a serif for the product name on the end card. (For AIpreneur/SKINKU products swap the palette to that brand.)

## Build rules
1. One HTML file, 1920×1080. Every style computed from time inside `seek(t)`; no CSS transitions, timers or state carried
   between frames. Declare every variable before the first `seek()` call.
2. One camera transform on a container, keyed by `[time, zoom, x, y]`, eased segments, zoom interpolated in log space.
3. Closed-form step-response springs for every pop/settle (pure functions of t).
4. Every handoff is a shared element (the flood carries a copy of the bubble's words; the button carries its label into the page).
5. z-index on every layer (cards never above the flood). Typed request on fixed lines (camera never follows a wrapping cursor).
6. Flood reaches the farthest corner in ≈0.35 s (else it reads as a flash).
7. Sound: a downloaded Mixkit SFX per event (typing, send pop, each toss, drop impact, card swoosh, click, success tone,
   page-fill whoosh, mark sparkle), placed by its measured peak, mix loudnorm −14 LUFS. Record each source URL + licence
   in `production/asset_credits.json`. (If mixkit.co is blocked by the network, ask the user to allow it or to upload the files.)
8. Render: Playwright at 60 fps, 8 subframes per frame blended with ffmpeg `tmix` (4 leaves ghosts — slow the move instead).
   Review every fast moment frame by frame and scan the whole video for single-frame pops. HyperFrames can also render it
   (its seek is time-pure) when subframe blur isn't needed.

## Deliver
MP4 1920×1080 60 fps + the 4 approval stills + a short beat map. Commit the HTML/tools (not the MP4) and push.
