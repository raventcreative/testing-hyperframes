# 3D mascot version — conversion brief (project: projects/efek-17-carousel-3d)

The illustrated presenter is replaced by the user's 3D AIpreneur mascot (chibi, brown hair, black "AI PRENEUR" polo, cream trousers, white sneakers).
It is a pre-rendered transparent talking loop (mouth moves, hand gestures, head acting), exactly 4.0 s, seamless loop (frame 0 == frame 4):
- `assets/mascot/mascot_talk_loop_1x.webm`  1080x1350, VP9 alpha — use this by default
- `assets/mascot/mascot_talk_loop_2x.webm`  2160x2700, same motion — use ONLY where the mascot is scaled > 1.2x (close-ups, punch-ins), displayed at width:1080px height:1350px so it stays sharp

## How to place it (see compositions/e01.html — already converted, the reference)
Static markup inside your figure layer (videos must be in the HTML, not injected by JS):
```html
<div id="eN-figwrap" class="eN-layer"><video id="eN-mascot" class="clip" data-start="0" data-duration="4"
  src="assets/mascot/mascot_talk_loop_1x.webm" muted playsinline style="position:absolute;left:0;top:0;width:1080px;height:1350px"></video></div>
```
Default framing (set once in JS on the wrapper): `transform: translate(0px,-44px) scale(0.78); transform-origin: 540px 1204px` → feet stand on y 1160.
Animate framing changes on the WRAPPER (never on the <video> itself). Remove every `HFP.mount` / `HFP.animate` / figure-SVG use; keep `HFP.backdropHTML` and `HFP.chromeHTML`.

## Landmarks in the 1080x1350 frame with the DEFAULT framing
- hair top y≈377 · head (with hair) x 289–777, widest at y 565–630 · eyes y≈704 · chin/neck y≈785–800
- torso (polo) y 815–1000, hands swing within x 355–730 · trousers 1000–1130 · feet y≈1160 (soft contact shadow is baked in)
- body centre x≈540 · chest centre ≈ (540, 880)
- keep clear (face): x 330–750, y 470–800
- free space: above head y 130–370 · left of head x 60–285 · right of head x 780–1020 · below feet y 1170–1300 (`.k-cap` caption at y 1196 sits on the floor under the feet — fine)
Unscaled plate (scale 1, no translate): hair top 200, head x 218–844, eyes ≈620, chin ≈730, feet 1204. Mapping default: x' = 540 + (x−540)·0.78, y' = 1160 + (y−1204)·0.78.
You may choose a different framing per effect (bigger, smaller, moved) if the effect reads better — the mascot is chibi (big head, small body), so re-think layouts that relied on the old tall bust; just keep the face clear.

## Silhouette effects (no HFP.SIL any more — the mascot shape is the video's alpha)
- White paper-cut border: SVG filter on the wrapper, e.g.
  `<filter id="eN-cut"><feMorphology in="SourceAlpha" operator="dilate" radius="14" result="d"/><feFlood flood-color="#fff"/><feComposite in2="d" operator="in" result="w"/><feMerge><feMergeNode in="w"/><feMergeNode in="SourceGraphic"/></feMerge></filter>`
  (radius is in the wrapper's local px, so divide by the wrapper scale). Add a drop-shadow after it for the paper lift.
- Boiling doodle outline: dilate(R) minus dilate(R−7) ring from SourceAlpha → white, then feTurbulence + feDisplacementMap; switch between 3 fixed `seed` values every 0.1 s (deterministic: pick the filter id by Math.floor(t/0.1)%3).
- Behind/in-front layering works automatically: elements in layers before the figure layer are hidden by the mascot's body.

## Rules unchanged
Everything in production/BRIEF.md still applies (4.0 s, loop-friendly, chrome on top, deterministic, Indonesian copy, Poppins, ids eN-, lint 0 errors, snapshot and LOOK at your frames, no check/render/commit, don't touch shared files or other effects).
