# 12 — SCENE CONTRACT (for Claude Code scene builders / subagents)
**Version:** V3.0. Paste this whole document (or point to it in the workspace) for every agent that builds a scene.
It is the generalized form of the contract that produced REF-H (`house_style_kit/example_aipreneur_v3/production/SCENE_CONTRACT.md`).

## Context
The host `index.html` (from `house_style_kit/starter/`) already provides the pastel background (plate + paper grid + haze + motes + grain), the small word-synced caption at the top (y 232–380) and the voice-over. **A scene builder only writes `compositions/sNN.html`** for the scenes assigned to it. Overwrite the placeholder completely.

Style authority: `11_HOUSE_STYLE_BIBLE.md` + `golden_frames/` + `style_references/ref_H_house_style_aipreneur_v3.mp4`. Secondary (craft inspiration only, never copy imagery): REF-B light scenes (~12 s, 22–28 s, 34–38 s, 56–62 s), REF-C, REF-A.

## What "good" looks like (match REF-H)
1. ONE hero object, big (60–75 % of the visual zone), instantly readable as the metaphor for the spoken words.
2. 20–60 detailed elements: bevels, rims, screws, pins, ticks, sticky notes, stitched edges, tiny abstract UI lines, reflections.
3. Soft key light from the upper left, white inner top highlights, contact shadows down/right, a spotlight cone or glow only on the key moment.
4. Three depth planes (blurred far discs/props, the hero, near particles) + push-in + parallax.
5. Frame 0 already shows the hero in motion. Nothing static for more than 0.6 s.
6. The key action and apex land exactly on the given word times.

## Palette & type
Ink `#202B3B`, navy `#294B77`, navy-2 `#3A6299`, deep `#1C3354`, ice `#ACC6E7 #CBDBF4 #E8F0FB #FBFCFE`, graphite `#2E2E2E`, paper `#FFFEFB`. Small accents: mint `#9FD8C4`, amber `#F2C46D`. No red, no neon, no full-screen dark/opaque background (the host BG must stay visible).
Fonts: Montserrat 400/700/900, Inter 400/700, IBM Plex Mono 400/700 only.
Host kit classes you may use: `.kit-card .kit-paper .kit-glass .kit-navy .kit-contact .kit-mono .kit-line` and CSS vars `--ink --navy --navy-2 --navy-deep --ice1..4 --graphite --paper --shadow-lg/md/sm`.

## Text rules (strict)
- The caption already shows the spoken words, so scenes are almost text-free.
- Any readable word drawn in a scene must be a word from the verified transcript and fit the meaning. Otherwise use abstract lines/bars/icons.
- Never draw brand names, numbers/stats, URLs, "follow/save", fake UI copy or lorem ipsum.
- A logo may appear only in scenes told to use it: `<img src="assets/brand/<logo>.png">`, setting only `width`. Never redraw, recolour, crop or stretch it.

## Layout
Visual zone x 50–1030, y 400–1520, hero centre y ≈ 900–1000. Keep y < 380 clear (caption) and y > 1560 empty-ish (Reels UI).

## File template
Start from `house_style_kit/starter/compositions/_scene_template.html`. Replace `sXX` with the id everywhere. It contains the skeleton: key light, far discs, spotlight cone, hero placeholder, contact shadow, apex kit (glow, shockwave, sparkles, mint check), seeded PRNG and push-in.
```html
<template>
  <style> #root { position:absolute; inset:0; overflow:hidden; }  /* every other selector prefixed sNN- */ </style>
  <div id="root" data-composition-id="sNN" data-width="1080" data-height="1920"> … </div>
  <script>
    (function () {
      const R = document.querySelector('[data-composition-id="sNN"]');
      const q = (s) => R.querySelector(s), qa = (s) => R.querySelectorAll(s);
      const tl = gsap.timeline({ paused: true });
      // build… times are SCENE-LOCAL seconds
      window.__timelines["sNN"] = tl;   // register LAST
    })();
  </script>
</template>
```

## Hard technical rules
- Use an IIFE (scripts share one global scope). Query only inside `R`. Prefix every class, id and SVG gradient id with `sNN-`.
- One paused timeline, registered last. Never call `play()`.
- Use `tl.set(..., 0)` for initial states FIRST, then tweens; for apex `fromTo` use `immediateRender: false`. Never use `gsap.from`.
- Never combine a CSS `transform` with GSAP transform tweens on the same element (lint `gsap_css_transform_conflict`).
- Tween transforms/opacity/filter/clipPath/strokeDashoffset/colours only. Never left/top/width/height (lint `gsap_non_transform_motion`).
- Deterministic only: no `Math.random` (use a seeded PRNG), no clocks, timers, rAF, network, `repeat:-1` (use finite repeats).
- No `<br>`, `crossorigin`, `<video>` or `<audio>` in scenes.
- CSS 3D: `perspective` on a parent + `transform-style: preserve-3d`. `opacity<1`, `filter` and `overflow:hidden` on a preserve-3d node flatten it, so fade the leaf faces.
- Intentional overlaps (extruded type layers, double labels, engraved text, typed characters) get `data-layout-allow-overlap` on that element, so the `check` layout audit passes honestly.

## Self-verification (required; iterate at least 2 passes)
1. `npx hyperframes lint` → fix every error naming your file.
2. `npx hyperframes snapshot . --at <global times> --no-end -o .hyperframes/work-sNN` (just after the cut, each key word, end −0.1). Open the PNGs and judge them honestly against the golden frames: is the hero big, detailed, lit and readable? Any clipping, empty frames, caption-zone intrusion or artifacts? Fix and re-snapshot.
3. Ignore problems in files that aren't yours. Never edit `index.html` or other scenes.

## Report back (short)
Per scene: file path, the metaphor in one line, key beats with local times, the snapshot folders you inspected, and anything not achieved.
