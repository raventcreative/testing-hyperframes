# AIpreneur Automation — reels pipeline (software-demo remakes)

Client workflow: the client sends a reference video and goes to sleep. Claude does everything end to end without
asking in between, then sends the finished MP4. Quality bar is high: check frames before delivering.

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
- Layout: app window ≈ x 80–1000, y 250–1270; captions y 1282–1400 (2 lines max); robot y ≥ 1408. Nothing overlaps.
- Captions: phrase chunks, smooth fade in/out, words brighten in sync (no pop/bounce). Poppins Bold for key words,
  Poppins Regular for the rest.

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
