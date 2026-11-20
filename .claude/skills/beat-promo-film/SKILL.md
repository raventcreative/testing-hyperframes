---
name: beat-promo-film
description: 20-second high-end minimal product promo (1920×1080, 60 fps) cut to 10 bars at 120 BPM — hook word-by-word on beats, hook word morphs into the product UI, cursor types/clicks, circle opens from the button into a dark scene at the drop, then one move per bar with REAL vertical clips (scan-line wall with 3 winners, big-type output, 3D carousel with floor reflections + whip, hero clip in a phone + flipping results panel, push-cut stats, 3-word ticker, logo reveal, fade to black). Beat grid from numpy analysis, every cut on a downbeat, 3-subframe motion blur. Use for "/beat-promo-film", "promo produk ikut beat musik", "video launch minimalis pakai klip asli".
---
# /beat-promo-film

Verbatim client brief: `references/brief.md`.

## Start protocol
1. Ask for: product name + one-line promise, 3–5 UI moments, ONE accent colour, 10–20 real vertical clips the user
   owns, a royalty-free song with a clear drop (Mixkit etc., commercial use allowed). Never substitute placeholder cards
   for missing footage — ask again (for AIpreneur/SKINKU, clips can come from their own content).
2. Analyse the song first, then show a **storyboard with every timing on the calibrated beat grid** (10 bars × 2 s at
   120 BPM: bar 1 hook, bar 2 UI morph + cursor, drop = circle opens into dark scene, then one move per bar). Wait for
   approval before writing any code.

## Direction
High-end minimal: one idea per shot, lots of empty space, one accent colour, one clean sans (Geist or Inter) with tight
tracking, masked type reveals, match cuts, one smooth camera language, real footage only, **no full stops in on-screen text**.
Banned: shockwave rings, particle bursts, RGB split, camera shake, lens flares, neon glows, grid floors, flashing
backgrounds, bouncy easing. (Note: these bans override our voxel-reel habits — no shockwave/flash here.)

## Build
1. One HTML file 1920×1080; every style from time inside `window.seek(t)` (no CSS animations, timers or state between frames).
2. Clips → 30 fps JPEG sequences (`ffmpeg -i clip.mp4 -vf fps=30,scale=-2:1080 -q:v 3 clip_%04d.jpg`); swap `<img>` src
   per frame; `seek` awaits `img.decode()` for every visible frame.
3. Song analysis with numpy (librosa if available): onset envelope → tempo, beat grid, energy per bar, the drop
   (largest energy rise); calibrate the grid to real kick hits (low-band onset peaks). Cuts on downbeats, UI hits on beats.
4. Render with Playwright: 3 subframes per frame at t − 1/240, t, t + 1/240 s, blend with ffmpeg `tmix=frames=3`, 60 fps H.264.
5. SFX placed by measured peak (not file start), quiet under the music, final loudnorm −14 LUFS; commercial-use licences
   only, credited in production/asset_credits.json.
6. Probe ≥20 frames before the full render; fix clutter, overlap, unreadable text.

## Gotchas
- Never set opacity/filter on a `preserve-3d` element (it flattens, both faces show) — fade its wrapper.
- Measure element positions at runtime (getBoundingClientRect inside seek) for match cuts.
- Carousel reflections: a flipped copy below with a gradient mask on the wrapper, not on the 3D element.
