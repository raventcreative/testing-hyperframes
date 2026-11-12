# NOTES — R17 · Repo GitHub buat belajar bikin teknologi dari nol: build-your-own-x (AI PRENEUR · NAVY)

- **Duration** 42.00 s (1260 frames @30) · VO 40.40 s starting at 0.30 s · CTA keyword **RAKIT**.
- **Kit**: copied from `projects/aip_r9_youtube` (navy; without `out/`, its VO/SFX/bed audio, QA or cover PNG), with the R13 builders
  (`tools/build_index.py`, `tools/timing.py`, `tools/sfx.py`, CTA scene pattern) adapted; new shared scene kit `vendor/r17kit.js`
  (header with icon roll / title / one-line job / chip / 3 progress segments, lucide icons, Claude mark, timeline boilerplate).
  **Initial states** are pinned in a NESTED timeline that is the FIRST child of every scene timeline at 0 (`K.scene` → `pin`, `I()`),
  the same in `index.html` (captions + logo), and every build ends with `tl.render(0, true, true)`; tween positions are clamped to
  ≥ 0.005 s. Audio setup as batch 3/4/5: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` + `<audio id="sfx" src="assets/audio/sfx.wav">`
  (no music; the lead adds the ducked bed + loudness pass). `out/` is git-ignored (`.gitignore` in this folder).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = the client's auto tags: `[playful] [excited]` on every line + `[confident]` on the CTA) → `assets/audio/vo.mp3`;
  `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js`.
  Take 2 is final (take 1's line 7 "kodenya" was heard as "kodonya" by faster-whisper twice → the line was rewritten, see VO_SCRIPT.md).
  Timing overrides (OVR in timing.py) for "Git," / "Docker," (line 3) and "Code:" (line 7): the onset snap had pushed them into the
  next voiced run; values checked against the energy segments + a faster-whisper small pass. No caption merges.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples), cued to this reel.
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_RAKIT_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_RAKIT_1080x1920.png`,
  static server on :8937 at the project root). NAVY: chip "REPO GITHUB · GRATIS · 360 TUTORIAL", "Bosen bikin to-do app? / RAKIT /
  Git, Docker & database versi kamu sendiri", the four blueprint cards from t1 (Git lit), mascot + typing robot. No star number / rank
  on the cover (those live in the reel with their check date).
- **Lead fix applied**: the mascot's "glance at the robot" (`glance` in `compositions/mascot.html`) is disabled
  (`const glance = (t) => 0;`, the old function kept as `glance_unused`) — it rendered blank white-disc eyes in the real render (R13).

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
(filled in below)
