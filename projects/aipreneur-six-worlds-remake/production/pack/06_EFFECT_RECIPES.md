# SIX EFFECT RECIPES — original implementation logic

## 01 — Kallaway Split / Editorial Perspective

- UI build: split stage 40/60; grid thin dark navy opacity <10%, hard baseline and title anchor; each bar is a real 3D-extruded slab or CSS 3D with visible depth; show 6 symbolically labelled editorial cells, **no invented views**.
- Animation: first baseline traces in 0,32s. Bars launch non-uniform stagger 60–90ms, no 1s uniform bounces; maskot acts on chart. Camera travels through bar #03.
- Handoff: match bar rectangular contour to screen bezel. Maintain travel direction and apparent scale over bridge.
- Avoid: bar sequence with no reason, fake upward analytics numbers, generic stock infographic.

## 02 — Over-the-Shoulder / True Parallax

- Create one Three.js camera move: front three-quarter → curved track around right shoulder → focus plane behind shoulder. Body occludes near edge of monitor, foreground moves faster.
- On-screen working editor is original UI built from code with timeline/6 slots (no screenshot of Claude or other user's account).
- Bring focal length from 50mm to 35mm only if camera matches; do not animate wildly changing FOV.
- Handoff: monitor bezel / lit edge transforms into first extruded letter outline.
- Avoid: blurry fake portrait, mere 2D cutout moved sideways and called camera orbit.

## 03 — Backdrop Word / Solid Typography

- Model letters `CLAUDE` as matte navy dimensional signage (or extruded text geometry); physical thickness visible 4–8cm relative to mascot scale.
- Key light creates grounded shadows; camera 10–15° side arc exposes bevel, maskot stands in front.
- Put aesthetic overlay name `03 — WORD STAGE` in Poppins; **giant word is a prop, not an on-screen subtitle**.
- Handoff: letter C and next slab form controlled doorway with continuous camera move.
- Avoid: rubber letters, spinning giant glyphs at unreadable speed, words clipping eyes, jumping perspective.

## 04 — Glass Widgets / Actual Depth

- Material: restrained transmission, faint navy tint (~7–12%), brighter hairline top edge, thicker bevel below, soft AO, physically motivated reflection; background pale still visible through it.
- Text UI remains on legible front-facing plane in gradient navy; avoid auto-rotating its contents.
- Place three surfaces on depth rails (z differences) and animate gentle near/far parallax, not three identical pop-ins.
- Handoff: top-edge light glint races across card, extends into cone of spotlight.
- Avoid: generic white card with opacity 0.7, giant bloom, unreadable gray text.

## 05 — Spotlight / Lighting as Story

- A one-source light motivation: glint from glass becomes tracked stage beam. Local stage vignette only; background identity remains visible at edges.
- Key cool-neutral 5000–6000K; stage contact shadow shifts coherently. Ambient halo subtle.
- Maskot reacts with head turn and posture change. At light apex, hold 0.7s. Dim grade only temporarily.
- Handoff: projected circular gobo narrows into real grading-filter aperture.
- Avoid: unrelated strobe, all-black room with random neon fog, overblown whites.

## 06 — Color Grade / Controlled Comparison

- Build single matched shot with two grades of *the same render*: before = flat low contrast neutral; after = balanced navy shadows, pale highlights, skin/character color preserved.
- Gesture rotates one visible optical dial/split-screen control; divider has thickness and reflection.
- Color transition must not recolor company logo or invert avatar skin/material in unnatural way.
- Show before/after 0.7s each so user can actually compare; transition follows dialogue.
- Handoff: split circular slider becomes timeline carousel arc used in closing recap.
- Avoid: Instagram LUT orange/teal extreme, sudden aesthetic change with no visual cause, fake film scratches.

## Top-left logo motif

Use the supplied PNG as alpha-trimmed wordmark. At start, it gets a tiny 0.25s slide of 6–9px and settles; every roughly 8–10s, a **controlled very faint diagonal specular sweep passes across existing glyph alpha** for ~0.45s. During large spotlights, slight local illumination is okay; never rotate the entire logo, zoom it in/out randomly, or obscure it. Respect its original dark glyph color on light BG.

## Sound design

No BGM by default. Use 6–9 very quiet, non-generic sounds: tactile card slide, monitor bezel pass, subtle mechanical letter shift, soft glass tick, focused light click, dial detent, final paper/card settle. Effects never compete with VO; keep audio peak safe. Do not simulate explosive cinematic trailer impacts.
