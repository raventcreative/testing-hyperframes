# Scene Builder Contract — Hypit Remake (ElevenLabs × Mascot)

Copied to every scene builder. Applies to every `compositions/sNN.html`.

## Ownership
- You own ONLY your assigned `compositions/sNN.html` files. Never edit `index.html`, `compositions/captions.html`, assets, or other scenes.
- The root (`index.html`) already provides: the supplied background plate (`assets/background_asli.png`, object-fit cover) under every scene, a top caption band (y≈220–385, word-synced, owned by `captions.html`), and the ONE ElevenLabs `<audio>`. **Never add `<audio>`/`<video>` or captions in a scene.** Never paint a full-screen opaque fill (the background must stay visible).

## File skeleton (verified against installed HyperFrames v0.8.186)
```html
<template>
  <style>
    #root { position:absolute; inset:0; overflow:hidden; pointer-events:none; font-family:"Poppins",sans-serif; }
    /* every other selector prefixed .sNN- / #sNN- */
  </style>
  <div id="root" data-composition-id="sNN" data-width="1080" data-height="1920">
    ... markup, all ids/classes/svg defs prefixed sNN- ...
  </div>
  <script>
    (function () {
      const R = document.querySelector('[data-composition-id="sNN"]');
      const q = (s) => R.querySelector(s);
      const qa = (s) => R.querySelectorAll(s);
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      // tl.set(...) explicit initial states at 0
      // tl.fromTo(..., {..., immediateRender:false}, t)
      window.__timelines["sNN"] = tl;   // registered LAST
    })();
  </script>
</template>
```
- Scene-local seconds (0 = scene host start). The scene duration is given to you; keep every tween inside `[0, duration - 0.04]`.
- GSAP is global (`gsap`). No other libraries, no network, no `Math.random`, `Date`, timers, rAF, `repeat:-1`, `play()`. Use `fromTo` (never bare `from`). Animate transforms/opacity/filter/clip-path only — never left/top/width/height. No CSS `transform` property on an element GSAP also transforms (put static transforms on a parent wrapper).
- Fonts: Poppins 400/700/800 is declared at root via `@font-face`; just use `font-family:"Poppins"`. Monospace for a terminal line: `"JetBrains Mono", monospace` (bundled).
- SVG `<defs>` ids must be prefixed (`sNN-grad1`) — the page is shared by 19 scenes.

## Canvas, zones
- 1080×1920. Caption band y 220–385 belongs to captions — NOTHING of yours above y≈400 except soft far-plane bokeh/haze (low opacity).
- Hero stage: x 50–1030, y 415–1520. Hero occupies 60–75% of that stage. Below y 1570: only low-density floor/shadow/texture.
- First frame of the scene must already show the hero (hard/match cuts; no blank intro, no fade from nothing on the whole scene).

## Palette lock (Freddie custom — beats any reference palette)
- Navy gradient (enamel, plates, controls, highlight backing): `linear-gradient(105deg,#121532 0%,#274976 100%)`.
- Ink `#121532`, blue `#274976`, white `#FFFFFF`, ice-white `#F7FAFF`, rim `#DCE8F6`, graphite `#26354E`. Local tints between these are fine (e.g. `#3a5d8f`, `#8ea9cc`, `#b8cbe4`) for bevel/shadows.
- Materials: porcelain / frosted glass bodies (ice-white → `#DCE8F6` → soft blue-grey shading) with navy enamel inlays, chrome-ish rims (`#DCE8F6`→`#8ea9cc`), soft glass highlights. Key light from upper-left: highlights top-left edges, shadows fall down-right. Every grounded object has a soft contact shadow (`radial-gradient` ellipse in rgba(18,21,50,.18–.32)).
- FORBIDDEN: red, orange, pink, yellow, neon/violet, full-screen navy, black backgrounds, third-party logos (no GitHub octocat, no Anthropic/Claude logo, no sponsor), fake metrics/numbers (no star counts, no prices, no Rp, no %), fake screenshots.

## Text rules
- Only words that are literally spoken in YOUR scene's VO phrase (or the verified command `npx skills add hypit-ai/hypit -g` in s15). Max 1–3 tiny labels per scene, 24–34px, Poppins.
- Dark text = navy `#121532` on light surfaces. **Any WHITE text must sit inside a visible padded rounded box with the navy gradient (radius 10–14px, padding ≥ 6px 16px)**, box appears BEFORE the glyphs (box scaleX 0→1, then text 1–2 frames later).
- No headlines; captions are handled globally.

## Craft bar (benchmark = REF-H depth/density, NOT its palette/fonts)
- ONE big hero object/metaphor per scene; 20–60 purposeful micro-parts (screws, ticks, bevels, apertures, ridges, trim rails, LEDs, hinge knuckles, engraved rulers, perforations, cable nodes…). Build with layered divs + inline SVG; use gradients, inset shadows, border highlights for bevels.
- Three planes: far (soft blurred bokeh/glass discs/ghost panels, low opacity, slow parallax), mid (hero + contact shadow), near (a small out-of-focus foreground prop or glass chip, blurred 2–6px, moves more in parallax).
- Camera: a wrapper `.sNN-cam` with a gentle push (scale ≤1.06 over the scene) or slight drift; vary per scene (some push, some lateral drift, some still-then-punch).
- Beats: entrance (≤0.5s, `expo.out`/`power4.out`, can start already mostly in place for match cuts) → anticipation (small counter-move 0.1–0.2s before apex) → ACTION hits the apex word time exactly (±0.05s): micro scale punch (1.0→1.04→1.0), a brief shockwave ring (scale 0.6→1.8, opacity .8→0 in ~0.5s), 3–6 sparkle glints → settle → handoff pose at scene end that matches the next scene's opening silhouette when specified.
- No idle bobbing/breathing loops, no infinite pulsing, no every-element-slides-up. Landed things hold still; motion moves to the next element or the camera.
- Mascot (only in scenes that list it): `<img src="assets/mascot/mascot_front.png|mascot_side.png|mascot_back.png">` (transparent PNG cutouts: front 544×886, side 452×889 (faces LEFT), back 496×885). Display height 380–560px, width ≤ 25–40% of stage width, standing on a ground line with its own soft contact shadow ellipse under the shoes. Motion = WHOLE SPRITE only: translate, rotation ≤4°, scale 0.95–1.05, lean, peek, small step with shadow following, tilt-nod. No limb/head/mouth animation, no constant bounce, no flipping that mirrors the polo text (do NOT scaleX(-1) the front view; mirroring the side view is allowed ONLY if no text is visible — the side view shows "NEUR" text, so avoid mirroring it too). Never cover the hero's key part or the caption band.

## Determinism & QA
- Initial states: use `gsap.set(el, {...})` (immediate, OUTSIDE the timeline) for every animated element's starting state — a `tl.set(..., 0)` does NOT render while the playhead sits exactly at 0 (lint rule `gsap_timeline_set_initial_hide`). `tl.set` is fine at t>0 for instant flips; `fromTo` with `immediateRender:false` for later tweens on the same property; never two tweens fighting over one property at the same time.
- Seeking to any t in any order must give identical pixels.
- Before finishing, run from the project dir:
  `npx hyperframes lint .` and
  `npx hyperframes snapshot . --composition sNN --frames 5 -o .hyperframes/artifacts/sNN` and LOOK at the PNGs. If the hero is small, flat, empty, or text-led → rebuild. Fix every lint error that names your file.
