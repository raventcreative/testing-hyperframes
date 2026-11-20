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

From prompt-motion.com (paraphrased; full list + links in prompt_motion_catalogue.md, skill /prompt-motion-techniques)
- VO takes + alignment: several full takes, redo weak lines and splice, trim pauses >0.28 s to 0.2 s, level phrases, get
  word times by transcribing each pause-split segment separately (one pass can drift ~0.5 s). (prompt-motion.com/rossaxbt-3085b7)
- Duck music under VO so speech sits ~9 dB above it in 300 Hz–4 kHz; drop lands on the key "verb" line. (rossaxbt-3085b7)
- Guide object carries every hand-off (never teleports): use the mascot/robot as the "ball" that triggers each beat.
  (rossaxbt-94583b)
- Through-line accent dot (#01ccf7) that becomes a letter dot, draws the graph, floods, returns at the end; graph and dot
  share one function. (ultimaxbt-bbebf5)
- Shots enter already moving and leave accelerating or on a blur ramp; hard cuts ~2 frames before the beat. (notdwd-7de38a)
- Arc chaos → control → clarity → brand with ~4 visual ideas; object-driven transitions (number → next card's amount,
  chart line → document edge). (daniel-haida-8691d4)
- Hook: a fast-spinning list of pains (unreadable on purpose) that lands slowly on the one that matters. (jake11moran-f60e35)
- Reel shape: hook in the first second → distinct techniques per beat → one clean memorable final frame. (reflex-cloud-72ffe5)
- Process-fill explainer: each ingredient/step pours into a container with its label until it is complete. (ror-fly-9950f1)
- One explanation per visual genre for the same concept, fast and self-referential. (emollick-8661a8)
- Type system for bumpers: locked copy order, display + grotesque + mono, per-glyph springs at 1/16 note, next word
  revealed through a mask of the outgoing word, strikethrough becomes the next underline (brand colours only). (techhalla-90b8ec)
- Words as architecture: key words get structural roles; last line stands on what earlier words built; one ~400 ms
  stillness. (gdgtify-287ddf)
- Morphing-component loops: one shape through many UI states; sum of springs per retarget; two edges on two springs for
  stretchy indicators; loop seam matches cursor position AND speed. (demonugc-4c5753, twoclipping-5cba86)
- Recompose the vertical version; never crop the 16:9 master. (daniel-haida-8691d4)
- Ban AI giveaways: no decorative corner frames/HUD text; no invented %, multipliers or customer names. (1littlecoder-9fef89, ik-builds-b8bdcf)
- QA: stills at fixed timestamps, inspect decoded frames of the final MP4, scan frame differences for single-frame pops,
  then a fresh reviewer who didn't build it. (daniel-haida-8691d4, antonio-kodheli-490109)
