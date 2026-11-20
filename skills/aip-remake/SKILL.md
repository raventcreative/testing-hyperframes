---
name: aip-remake
description: AIpreneur IG remake (R-series R1–R26 style) of a reference reel — HTML/GSAP motion-graphic scenes with the client's 3D chibi mascot as host (+ AIpreneur robot co-host), ElevenLabs VO (Dakocan), ATM rules, alternating navy/white, CTA "Komen <KEYWORD>, aku kirim lewat DM", DM file + caption + cover. Use for "/aip-remake", "remake video ini buat AIpreneur", batches of reference reels.
---
# /aip-remake
- Read `references/BRIEF_batch3..6.md` (copied from the repo) in order: house style, pipeline, QA lessons, ATM rules,
  overlap checks with earlier reels. Kits: navy → copy `projects/aip_r19_jarvis/` (or r15/r25), white → copy
  `projects/aip_r20_freellm/` (or r12/r24). Never copy `out/`.
- Mascot: `compositions/mascot.html` with glances disabled (`const glance = (t) => 0;` — a glance made the eyes read as
  blank white discs). Robot co-host `compositions/robot.html`.
- VO: `tools/el_tts_ts.py lines.txt vo.mp3` (auto tags), timing `tools/timing.py`, scenes `tools/build_index.py`.
  Spoken length 35–56 s. Whisper small+medium listen-check.
- Render: `aipreneur-reels-studio/scripts/render/render_aip.sh <dir> AIP_R<n>_<TOPIC>.mp4` (adds ducked music bed, −14 LUFS).
- Theme alternates per delivered video; brand per `aipreneur-reels-studio/references/brand.md`.
- If the client wants it more creative / with a 3D world → use `/voxel-reels` instead.
- Batches: zip with `<name>/` + `<name>/thumbnail/COVER_*.png` (zip -0).

## Upgrade techniques (always apply)
Read `aipreneur-reels-studio/references/mascot_robot_recipes.md` and pick 3–5 recipes for this reel (guide object,
robot-screen portal, button → page, accent-dot journey, spinning pain list, process fill, beat-locked changes, camera
push, spring motion, ducking). Note the chosen recipes + credits in production/VO_SCRIPT.md.
