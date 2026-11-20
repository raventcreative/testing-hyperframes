# Technique bank — what to borrow from the external skills/briefs the client gave (apply to the client's own videos)

The client's rule: external briefs are other people's products — take the TECHNIQUE, apply it to Freddie's brands.
Client format rules (brand.md, client_rules.md, voxel_reel.md) always win when they conflict.

Timing & structure
- Beat grid: pick/compose music, analyse tempo + downbeats + drop (numpy/librosa), calibrate to real kicks; cuts on
  downbeats, UI hits on beats; something changes on every beat; no hold > 0.5–1 s. (beat-promo-film, product-launch-film)
- Storyboard beat-by-beat with exact times BEFORE building; show 4–7 key stills for approval when the brief asks.
- Hook = the problem in 3–5 big words in the first bar.

Transitions (no cuts/crossfades)
- Through-line object: one element that transforms scene to scene and ends as the logo. (throughline-explainer)
- Shared elements: the button carries its label into the page; a colour flood carries the words it covers; a hook word
  morphs into the UI. Measure positions at runtime (getBoundingClientRect) for match cuts.
- Floods/circles must scale past all four corners in ≈0.35 s (else it reads as a flash).
- Buttons expand into pages; text rises from a mask line; outgoing/incoming text on separate timing.

Camera
- One camera transform on a container, keyed [time, zoom, x, y], eased, zoom interpolated in log space.
- One eased move per scene, never zoom in then out consecutively, never reverse direction; slow push 1.0 → 1.04 so it
  never sits still; each scene starts at the previous scene's end zoom. Screen-studio zooms so each UI moment fills frame.

Motion feel
- Closed-form springs (small overshoot) and exponential easing as pure functions of t; nothing appears from nothing.
- Motion blur from subframes: 3 (t ± 1/240 s) for UI films, 8–16 for fast/3D moves, blended with ffmpeg tmix.
  Directional blur proportional to speed.
- Cursor like a person: arrives 0.3–0.6 s early, press 0.15–0.2 s, glide 0.5–0.9 s cubic-bezier(0.55,0,0.25,1),
  typing ~50 chars/s, hold ≥1 s on results; results show a working state → reveal → settle. (html-demo)

Look
- One typeface, one accent used only on the key object/word, lots of empty space, real footage/photos/UI only.
- Minimal-film bans (when the brief is "high-end minimal"): particles, glows, flares, shake, RGB split, grid floors,
  flashing backgrounds, bouncy easing. (Our voxel reels may keep their approved glow/shockwave moments.)

Sound
- SFX placed by measured peak, not file start; quiet under music; −14 LUFS. Music can be composed in code
  (OfflineAudioContext: kick per beat, hit per scene change) when no licensed track is given. Commercial-use licences only.

Engineering
- One HTML, everything from `seek(t)`, no timers/state; declare variables before the first seek; z-index every layer;
  no opacity/filter on preserve-3d elements (fade the wrapper); no will-change on camera-scaled nodes; lock page layout
  before capturing websites; preload/decode images in seek; probe 20+ frames (or one per beat) before the full render.
