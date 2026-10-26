# Scene contract — REELS X-RAY (every scene module follows this)

Build: `python3 tools/build_scenes.py sNN` -> compositions/sNN.html. Look: `npx --yes hyperframes@0.8.186 snapshot --at <global s,...>`.
Module: `tools/scenes/sNN.py` with `build(S)` (see tools/xk.py docstring). Times are GLOBAL seconds (S.W(i) = measured word start).
Optional module attribute `SFX = [(t_global, "click"|"key"|"pop"|"sparkle"|"whoosh", vol 0.05-0.15)]`, max 2 per scene, on the apex.

Layout
- Caption band y 232–380 is sacred: hero top stays >= 430 (except the last ~0.25 s of a hand-off push).
- Host mascot = bottom-left, x 0–420, y 1320–1920 (drawn over the scene). Keep key hero content out of that box.
- Hero zone x 50–1030, y 430–1520, centre ~(590, 930); hero fills 60–75 % of it. Set `S.persp_origin = (590, heroTop+100)`
  so camera z-pushes grow downward.
- Three planes: far (backdrop/arch/rails in a wrapper `transform:translateZ(-520px) scale(1.26)`), mid (hero + contact
  shadows), near (1–2 out-of-focus foreground pieces in `translateZ(260px) scale(.87)`, blur <= 5 px).

Look (Ice-Ivory diorama)
- Porcelain (.por) + glass (.glass) + navy sidewalls/masses for contrast: every hero has at least one clear navy mass.
- Key light upper-left; contact shadow under every object (xk.shadow); 20–60 micro-details (screws, rivets, pins, ticks,
  hinges, rails) — but keep radial-gradient/blur/clip-path elements < ~30 per scene (screw/rivet/led/bloom count).
- Mint = confirmation only, amber = caveat only (s15). No red, purple, neon, dark full-frame backgrounds.
- Readable words = VO words only (+ spoken product names "Claude Code", "HyperFrames", "GSAP", "FFmpeg", "MP4", "EDITOR").
  Code/text lines are abstract bars. IBM Plex Mono only for non-word micro marks.

Motion
- Frame zero of the scene is fully populated. One apex (xk.apex) on the apex word; primary action lands on the word.
- Hand-off: end state anticipates the next scene's opening shape/position (STORYBOARD.md column).
- All tweens via S.ft / S.keys (fromTo, immediateRender false). No transforms in inline style on GSAP-tweened elements
  (put static transforms on a wrapper). No back/elastic eases on filter properties. Vary eases and durations.
- Continuous purposeful micro-motion (gears turn, pointers tick, cards drift) — never a dead frame.
