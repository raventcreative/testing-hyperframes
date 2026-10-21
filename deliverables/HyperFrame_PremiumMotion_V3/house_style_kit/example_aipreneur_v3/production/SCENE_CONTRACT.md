# Scene contract — AI PRENEUR Reel v3 (read fully before writing a scene)

Project: `/home/user/testing-hyperframes/projects/aipreneur-reel-39s` (HyperFrames CLI 0.8.x, `npx hyperframes …`).
Canvas 1080×1920, 30 fps, total 39.40 s. The host `index.html` already provides: the pastel background
(ivory → ice-blue plate + faint paper grid + haze + motes), a small word-synced caption at the top
(y 232–350), and the voice-over. **You only build the visual scene(s) assigned to you**, each as a
sub-composition file `compositions/sNN.html` (a placeholder exists — overwrite it completely).

## Why this rebuild exists
The client said the previous version had too much text and weak visuals compared to their references.
The new direction: **visual-first, REF-B density on a LIGHT pastel palette.** Every scene is a rich,
detailed, well-lit illustrated metaphor that explains the spoken words — not text on cards.

References (style only — never copy their imagery, brands, people, or text):
- Contact sheets: `/tmp/claude-0/-home-user-testing-hyperframes/83a864b1-6d12-50af-8cc9-33ebe35808fc/scratchpad/refs/ref_B_cinematic_dimensional_sheet.jpg` (PRIMARY),
  `.../refs/ref_C_clean_character_3d_sheet.jpg`, `.../refs/ref_A_editorial_kinetic_sheet.jpg`. View them with the Read tool.
- Full videos (extract frames with ffmpeg into your own scratch dir if you need a closer look):
  `/root/.claude/uploads/83a864b1-6d12-50af-8cc9-33ebe35808fc/1e46d161-ref_B_cinematic_dimensional.mp4` (REF-B light scenes at ~12 s, 22–28 s, 34–38 s, 56–62 s are the closest match to our palette),
  `.../9a7a6813-ref_C_clean_character_3d.mp4`, `.../4106e491-ref_A_editorial_kinetic.mp4`.

What makes REF-B look expensive (match this level):
1. ONE strong hero object per moment, big (fills ~60–75 % of the visual zone), instantly readable as a metaphor.
2. Micro-detail everywhere: bevels, inner highlights, rims, screws/pins, stitched edges, tick marks, tiny UI lines,
   stamps, sticky notes, labels-as-shapes, reflections. 20–60 visual elements per scene, not 5.
3. Real lighting: soft key light from upper-left, rim highlights on top/left edges, soft contact shadows on the
   ground (shadows fall down-right), occasional spotlight cone / glow on the key moment.
4. Depth: 3 planes (far props blurred/smaller, hero mid, a foreground element or particles), parallax drift.
5. Constant purposeful motion: things assemble, snap, rotate, slide, light up. Nothing sits static > 0.6 s
   (at minimum a slow push-in/drift + one ambient loop). Key actions land EXACTLY on the spoken word times given.
6. Quick, confident timing: entrances 0.25–0.5 s (power3/power4.out, back.out(1.4) for small pops), stagger 0.03–0.06.

## Palette & type (light / pastel only — client decision)
- Ink `#202B3B`, navy `#294B77` (primary accent), navy-2 `#3A6299`, deep navy `#1C3354`, ice `#ACC6E7`, `#CBDBF4`,
  `#E8F0FB`, near-white `#FBFCFE`, graphite `#2E2E2E`, warm paper `#FFFEFB`. Tiny accents allowed: soft mint `#9FD8C4`
  for "OK/checks", soft amber `#F2C46D` for light/warmth — sparingly. NO red, NO neon, NO dark full-screen backgrounds.
- Do NOT paint a full-screen opaque background — the host background must stay visible. Local panels/desks/
  surfaces are fine.
- Fonts (bundled, render offline): Montserrat 400/700/900, Inter 400/700, IBM Plex Mono 400/700. Nothing else.
- Shared CSS from the host you may use: `.kit-card`, `.kit-paper`, `.kit-glass`, `.kit-navy`, `.kit-contact`
  (contact shadow ellipse), `.kit-mono`, `.kit-line`, CSS vars `--ink --navy --navy-2 --navy-deep --ice1..4 --graphite
  --paper --shadow-lg --shadow-md --shadow-sm`.

## Text rules (strict)
- The caption already shows the spoken words. Your scene should be **almost text-free**.
- Any readable word you draw MUST be a word from the transcript (production/transcript_review.md) and fit the
  meaning. Otherwise use abstract lines/bars/icons. No brand names, no product names, no numbers/stats, no
  URLs, no "follow/save", no fake UI copy, no lorem ipsum.
- Logo: only `assets/brand/ai_preneur_logo_trimmed.png` (1214×168 incl. 32 px transparent padding). Never
  redraw, recolor, crop or stretch it; set only `width` (height auto). Only scenes that are told to use it.

## Layout / safe zones
- Visual zone: x 50–1030, y 400–1520. Keep the hero centered around y ≈ 900–1000.
- Keep y < 380 clear (caption). Keep y > 1560 empty-ish (Reels UI covers it) — soft floor shadow/reflection ok.

## File template (copy exactly; replace sNN everywhere)
```html
<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        #root { position: absolute; inset: 0; overflow: hidden; }
        /* every other selector MUST be prefixed with the scene id: .sNN-xxx  #sNN-xxx */
      </style>
      <div id="root" data-composition-id="sNN" data-width="1080" data-height="1920">
        <!-- markup: every class/id prefixed sNN- -->
      </div>
      <script>
        (function () {
          const R = document.querySelector('[data-composition-id="sNN"]');
          const q = (s) => R.querySelector(s), qa = (s) => R.querySelectorAll(s);
          const tl = gsap.timeline({ paused: true });
          // ... build everything, times are SCENE-LOCAL seconds (0 = scene start) ...
          window.__timelines["sNN"] = tl;   // register LAST, after the build
        })();
      </script>
    </template>
  </body>
</html>
```

## Hard technical rules (lint/render will break otherwise)
- Wrap the script in an IIFE (scripts share one global scope; `const tl` at top level collides across scenes).
- Query only inside your root `R`. Prefix every class/id with `sNN-` (all scenes share one DOM).
- One paused timeline, registered at the end as `window.__timelines["sNN"]`. Never call play().
- Use `tl.fromTo(...)` / `tl.set(...)` (not `gsap.from`). No `gsap.set` outside the timeline for animated props;
  static positioning via CSS is fine.
- Never give an element a CSS `transform` AND tween transforms on it with GSAP (lint `gsap_css_transform_conflict`).
  Put initial transforms in `tl.set(el, {...}, 0)` or the `fromTo` from-vars. Center with left/top/flex, or GSAP xPercent/yPercent.
- Animate transforms/opacity (x, y, scale, rotation, rotationX/Y, opacity, xPercent). Do NOT tween left/top/width/height
  (lint `gsap_non_transform_motion`). `filter`, `clipPath`, `strokeDashoffset`, colors, `borderRadius` are fine.
- Deterministic: no Math.random (use a seeded PRNG if needed), no Date/performance.now, no timers, no rAF,
  no network, no `repeat: -1` (compute finite repeats: `Math.max(0, Math.floor(dur / cycle) - 1)`).
- No `<br>` in text; no `crossorigin`; no `<video>`/`<audio>`.
- CSS 3D: use `perspective` on a parent + `transform-style: preserve-3d` for real depth. Note: `opacity < 1`, `filter`,
  `overflow:hidden` on a preserve-3d element flatten it — fade the leaf faces instead.
- SVG is encouraged for detailed illustration (gradients via `<linearGradient>`, strokes, `stroke-dasharray` draws).
  Give SVG gradient ids the scene prefix too (`sNN-g1`), they are document-global.
- The scene's last frame holds until the slot ends; the cut to the next scene is a hard cut. Make frame 0 of your
  scene already show something (hero partially in / moving) — never an empty first frame.

## Verify your own work (required, iterate until it's good)
1. `cd /home/user/testing-hyperframes/projects/aipreneur-reel-39s && npx hyperframes lint 2>&1 | grep -E "sNN|✗|◇"` — fix every error that names your file.
2. Snapshot at GLOBAL times (scene start + local): `npx hyperframes snapshot . --at <t1>,<t2>,... --no-end -o .hyperframes/work-sNN`
   (take ~5 per scene: just after start, each key word, end-0.1). Open the PNGs/contact sheet with Read and judge them
   honestly against REF-B: is the hero big, detailed, lit, readable as the metaphor? Any clipping, empty frames,
   overlapping the caption zone, ugly artifacts? Fix and re-snapshot (at least 2 improvement passes).
3. Other workers edit other scene files at the same time — ignore lint/snapshot issues in files that aren't yours,
   and never edit index.html or other scenes.

## Report back (short)
Per scene: file path, the visual metaphor in one line, key beats with local times, snapshot paths you inspected,
anything you could not achieve.
