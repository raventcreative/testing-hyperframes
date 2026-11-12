# NOTES — R3 · 5 tool gratis bikin Claude jadi desainer (AI PRENEUR · NAVY)

- **Duration** 47.533 s (1426 frames @30) · VO 45.92 s starting at 0.30 s · CTA keyword **DESAIN**.
- **Kit**: copied from `projects/igagent_2026` (without `out/`); index built by `tools/build_index.py`; shared scene kit
  `vendor/r3kit.js` (header, tool tiles, mock pages, timeline helpers). Scene details: `production/SCENE_BRIEF.md`.
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"`
  (saved voice, every line tagged) → `assets/audio/vo.mp3`; `tools/el_to_words.py` turns the character alignment into
  `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js` (one merge: "image to three JS" →
  caption word **img2threejs.**). Pronunciation checked with faster-whisper large-v3.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, no samples).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_DESAINER_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_DESAINER_1080x1920.png`,
  static server on :8823).

## Scenes (global s)
s01 0.00–6.23 hook · t1 6.23–12.73 Taste Skill · t2 12.73–19.23 Impeccable · t3 19.23–26.17 Playwright CLI ·
t4 26.17–33.80 Awesome DESIGN.md · t5 33.80–41.27 img2threejs · s07 41.27–44.17 recap/gratis · s08 44.17–47.53 CTA.

## Sources (checked 12 Nov 2026, official READMEs on GitHub)
- Taste Skill — github.com/Leonxlnx/taste-skill (tasteskill.dev), MIT.
- Impeccable — github.com/pbakaus/impeccable (impeccable.style), Apache-2.0.
- Playwright CLI — github.com/microsoft/playwright-cli, Apache-2.0.
- Awesome DESIGN.md — github.com/VoltAgent/awesome-design-md, MIT (84 DESIGN.md per badge).
- img2threejs — github.com/img2threejs/img2threejs (formerly hoainho/img2threejs; demos img2threejs.io), Apache-2.0.
Details of what each claim rests on: `production/VO_SCRIPT.md`.

## QA (real runtime, hyperframes 0.8.186)
- `node tools/check_scene.cjs …` → all 8 scenes + robot + mascot register (durations ≤ slot).
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the
  kit), SwiftShader ReadPixels notices, and contrast notes on decorative/hidden text (off-screen digits of the header number roll,
  tiny URL text inside the mock browser pages).
- Snapshots (`snapshot . --at … --no-end`): `production/qa/runtime_A/full_sheet_A.jpg` (0–19.2 s), `runtime_B/full_sheet_B.jpg`
  (19.27–41.25 s), `runtime_C/full_sheet_C.jpg` (41.3–47.5 s); every scene start/mid, both sides of every cut, first and last frame.
  The full-resolution PNGs were moved out of the project (scratch) to keep the folder small.

## Known issues / notes for the lead
- The bike in t5 is drawn by a deterministic software projection updated in the scene's `hf-seek` listener (same mechanism as the
  robot/mascot hosts, `detail.time + __T0`). It renders correctly in `snapshot`; if a chunked render ever shows a static bike, that
  listener is the place to look.
- Short "header only" beats while a tool's name is being said: 26.17–26.4 (t4) and 33.80–34.2 (t5) — intentional breathing room.
- t3 shows a deliberately cut phone headline ("teks kepotong" flag) for ~0.4 s before it is fixed — an illustrated bug, not a layout error.
- Mock pages ("NovaAI", "Kedai Sangrai") are fictional; DESIGN.md token values are generic UI examples; site names in the list are text only.
- `hyperframes preview` (used for `tools/check_scene.cjs`) stamps `data-hf-id` attributes into the composition files; harmless.
