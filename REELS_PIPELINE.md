# AIpreneur Automation — reels pipeline (software-demo remakes)

Client workflow: the client sends a reference video and goes to sleep. Claude does everything end to end without
asking in between, then sends the finished MP4. Quality bar is high: check frames before delivering.
**Do not send the script or intermediate drafts for approval — deliver only the finished video** (plus a short note).
The ElevenLabs API is already connected (key saved on the testing-hyperframes environment); the client does nothing.

## Fixed format
- 1080×1920, 30 fps, IG Reels. Safe zone: ≥80 px side margins; logo top-left at (84, 150), 300 px wide.
- **No intro** (no "Hai gue Freddie…"). Start with the hook.
- **CTA (always):** "Mau sistem kayak gini dipasang/dipetain di bisnis lu? Klik link di bio, ngobrol langsung sama tim AIpreneur Automation." + CTA card "AIpreneur Automation" with a "Link di bio" button pressed on the word "link".
- Style: **software demo / simulation** (app window, cursor clicks, panels, toggles, counters), built in HTML/GSAP
  (HyperFrames). Label everything "SIMULASI"; numbers are illustrative ("angka ilustrasi"). Never copy the reference
  product's name, logo or UI; never claim the client personally achieved the reference creator's results.
- **Robot presenter** (brand/robot, rig in robot_rig2.js): bottom-left, 600 px wide, base slightly cropped by the frame.
  Head stays still. Left hand waves (first beat + CTA), right hand points at the demo on every click, alternating hand
  beats on key words, eye blinks every 3–4 s, chest/base light follows VO loudness. Reuse the rig code from
  projects/blueprint-demo (tools/build.py injects it).
- **Robot v3 (current, client-approved):** front-facing AIpreneur robot with an animated, lip-synced mouth (glowing
  D-shaped smile that opens/closes with the VO loudness) + blinking eyes + hand gestures. After `tools/build.py`, always
  run `python3 -I tools/add_mouth.py projects/<name>` (copies brand/robot/r3_head.png + cleaned parts + robot_rig3.js and
  injects the mouth). Source art: brand/robot/robot3_src.webp.
- Layout: app window ≈ x 80–1000, y 250–1270; captions y 1282–1400 (2 lines max); robot y ≥ 1408. Nothing overlaps.
- Captions: phrase chunks, smooth fade in/out, words brighten in sync (no pop/bounce). Poppins Bold for key words,
  Poppins Regular for the rest.

## Demo variety (no monotone single-window demos) — reference: projects/reel-08-admin-wa-ramah
Client feedback: one static window with tiny push-ins feels monotonous. Change the "shot" every ~2–4 s, mixing:
- **Kinetic hook (no window):** big cards in the stage area (chat bubble, huge counter, stamp slam + shake), then a
  zoom-through transition (hook scales up + fades, app window scales in).
- **Screen-recording camera:** wrap all window content in `#wcam` (transform-origin 0 0) inside the fixed frame;
  `cState(x, y, s)` clamped so no empty edge shows. Use macro close-ups (s 1.8–2.0) on what gets clicked, medium
  shots (≈1.26) on the main panel, and **whip pans** (0.42 s, expo.inOut) between two close-ups.
- **Pop-out cards:** the key UI element flies out of the window as a big floating card (window dims + scales 0.95),
  then flies back.
- **3D split:** window swings back (rotationY ≈20°, origin left) while a detail card (receipt, report…) floats in front.
- **Kinetic stat stack** before the CTA: window recedes (scale 0.84, opacity 0.16), 2–3 big stat rows stack in.
- Small life everywhere: slow 3D drift on the window, printed-reveal (clip-path) for tickets, mini bar charts,
  background dot drift. A whoosh SFX on each big transition (keep it quiet).
All of it stays inside the stage (x 80–1000, y 290–1240); captions untouched.

## Motion style v3 (client reference: explainer with a living robot) — kit: brand/fx/reel_fx.js
`tools/add_mouth.py` copies the kit to `vendor/reel_fx.js` (+ bg-blue/bg-light/both logos). In the page: wrap the robot
as `<div id="rmove"><!--ROBOT_HTML--></div>` (CSS `transform: translateY(700px)` so it starts hidden), add `#bgD`,
`#logoD`/`#logoL`, dark caption CSS (`#main[data-sc="dark"]`), put `/*ROBOT_SETUP*/` before the scenes, then
`const FX = REEL_FX({ tl, ft, st, $, $$, D, rob, lh, rh, headIn, RG }); FX.theme("light"|"dark", 0);` and end with
`FX.runGestures()`. In tools/build.py replace the rig's slide-in with `st(rob, { opacity: 1 }, 0)`.
- **Robot is a co-star, never static:** `FX.enter(pose, t)`, `FX.go(pose, t)` (hop + lean while moving),
  `FX.dip(pose, t)` (sinks out during a wipe, pops up somewhere else), `FX.hop`, `FX.shiver`; poses home / center /
  right / close (CTA close-up, head ≥ y 1420 so captions stay clear). Expressions `FX.face("happy"|"x"|"wide"|"excited"|"flat", t, dur)`
  on story beats (bad news = x/wide, AI works = excited/happy). Gestures `FX.point/wave/beat` are side-aware.
- **ONE background per reel — never mix white and blue** (client rule). Pass `base: "light"` (white reel) or
  `base: "dark"` (blue reel) to REEL_FX; wipes `FX.stripes`, `FX.blocks`, `FX.sweep` then use only shades of that
  theme (+ a thin accent: #294b77 on white, #01ccf7 on blue). Use a wipe between scenes every ~5–8 s.
- **Kinetic text:** `FX.drop(el, t)` (letters fall in, add `data-letter="gt"` for gradient letters), `FX.sticker`
  (small rotated tags around the hook cards), `FX.marker` (cyan highlight sweep).
- Reference build: projects/reel-08-admin-wa-ramah (v3).

## 3D presenter robot (current, client-approved direction) — brand/robot3d
Client's own GLB (decimated, Draco) with an AI PRENEUR chest logo, skinned arms, glass-smooth visor and a procedural face
(blink, happy/x/wide/excited/flat cross-fades, mouth low-passed from VO_ENV). Ship it with `python3 -I tools/add_robot3d.py
projects/<name>` (instead of add_mouth.py) and wire it like projects/reel-08-admin-wa-ramah: importmap + robot3d_state.js +
module robot3d.js, `<canvas id="robo3d" width="820" height="700">` at left -92, top 1362 inside #rmove, and
`REEL_FX({ ..., r3d: window.R3D, base })`. Size: R3D.pxPerUnit 650 (head top y 1402, chest logo visible).
**Never zoom/crop the robot (no "close" pose) — the client wants it big but whole, also at the CTA.** All motion eased
(sine/power3, no back-overshoot pops). Render ≈ 20–25 min per 35 s reel (WebGL per frame).

## Client rules added 2026-11-13 (batch 2 re-send)
- **No cut text in the demo, ever.** Every text element visible in a frame must be fully readable. When the screen-recording
  camera (#wcam) zooms, any panel the frame edge would slice fades out for that shot (or the shot frames whole panels).
  Check pop-outs, chips, receipts for overflow/clipped words. Snapshot every camera shot before rendering.
- **Robot must travel:** besides bottom home/center/right, use peekL/peekR/low and 2-3 "up"/"upL"/"upR" moments where it
  stands full-body in the middle of the screen (lay those scenes out around it). CTA: robot whole, never zoomed.
- **Transitions differ per reel** (sets from: stripes, blocks, sweep, iris, shutter, doors, slats, dots).
- Run heavy local tools under `flock /tmp/claude-0/cpu.lock`, renders under `flock /tmp/claude-0/render.lock`.

## Alternating themes (one per video, see reels_log.json → `next_theme`)
| theme | background | text | accents | logo |
|---|---|---|---|---|
| **blue** | brand/bg-blue.png | white | #01ccf7 | brand/logo-aipreneur-white.png |
| **white** | brand/bg-light.png | gradient #0a0d2c → #294b77 | #294b77 (+ UI blue/orange only inside the app) | brand/logo-aipreneur-dark.png |
After each delivered video, append it to reels_log.json and flip `next_theme`.

## Assets (open source only — never AI-looking stock)
Poppins (OFL), Lucide icons (ISC, npm lucide-static), Simple Icons brand marks (CC0, npm simple-icons), SFX from
projects/visual-codes-remake vo_safe set. Record sources in each project's production/asset_credits.json.
The robot is the client's own mascot.

## Steps
1. **Analyse the reference:** ffprobe + 1 fps contact sheets; transcribe with local faster-whisper (`small.en` for
   English, `small` + language="id" for Indonesian; pass audio as a numpy array — the bundled `av` decoder is broken).
2. **Script (Indonesian, Freddie voice: sharp, practical, casual "lu/gue"):** hook → 3–6 demo beats that each map to
   an on-screen action ("klik…", "pindah ke…", "cari…") → CTA above. 55–75 s. No overclaiming; say "simulasi".
3. **VO via ElevenLabs API** (key is injected by the environment proxy; client voice in tools/voice_config.json):
   `python3 tools/el_tts.py "[playful] <script>" assets/audio/vo.mp3`, then convert to vo.wav (44.1 kHz mono).
   If the API fails, report it — do not fake audio.
4. **Word timing:** tools like projects/blueprint-demo/tools/align_whisper.py (Whisper word timestamps aligned to the
   exact script phrases). Then tools/vo_env.py for the voice envelope.
5. **Composition:** copy projects/blueprint-demo (white) or projects/agent-demo-137 (blue) as the starting point;
   rewrite the demo screens for the new topic; keep robot, captions, CTA, safe zones. `npm run check` (0 errors),
   snapshot the key beats and look at them, fix overlaps.
6. **Render:** `npx hyperframes@0.8.186 render . -o out/<name>_1080x1920.mp4 -q delivery` (~10–12 min, run in
   background). Verify duration/audio, sample frames, then SendUserFile and commit + push to `main`.
