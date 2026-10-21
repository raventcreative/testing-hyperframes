# house_style_kit — REF-H "Ice-Ivory Illustrated Diorama"

## starter/ (copy into every new HyperFrames project)
```bash
npx hyperframes init <project> --example blank --resolution portrait --non-interactive --skip-transcribe
# copy everything from house_style_kit/starter/ into <project>/ (overwrite index.html)
```
Fill the `{{…}}` placeholders in `index.html`:
| Placeholder | Value |
|---|---|
| `{{TITLE}}` | working title |
| `{{TOTAL_SEC}}` | video duration (VO end rounded up to a whole frame, e.g. 39.4) |
| `{{TOTAL_SEC_HALF}}` | half of that (haze drift yoyo) |
| `{{TOTAL_SEC_X10}}` | duration × 10, integer (grain steps) |
| `{{VO_FILE}}`, `{{VO_SEC}}` | VO file in assets/audio/ and its exact duration |
| `W` | verified words `[text, start]` |
| `CAPS` | one caption per scene `[start, end, firstIdx, lastIdx, [keyIdx]]` |
| scene slots | one `<div id="sNN" … data-composition-src="compositions/sNN.html">` per phrase |

For every scene, copy `compositions/_scene_template.html` → `compositions/sNN.html` and replace `sXX` → `sNN`. The template already contains the house FX kit (key light, far discs, spotlight cone, contact shadow, apex glow/shockwave/sparkles/mint check, seeded PRNG, push-in). Replace the placeholder hero with the illustrated metaphor (see source_docs/11 §9 and the example scenes).

Tested on 21 Oct 2026 with HyperFrames CLI 0.8.18x: fresh init + starter + one scene → lint 0 errors, snapshot correct.

## example_aipreneur_v3/ (the approved reference build)
The complete source of the 39.4 s AI PRENEUR Reel v3: `index.html`, `compositions/s01–s15.html`, `production/` (transcripts, scene contract), `assets/` (VO, logo, plate), `STORYBOARD.md`, `BRIEF.md`. Re-render with:
```bash
cd example_aipreneur_v3
npx hyperframes lint
npx hyperframes render --quality delivery --fps 30 -o out/check.mp4
```
Study the scenes to see how the hero illustrations, apex FX and timing are built. Reuse techniques, not literal objects, unless the metaphor fits.

## tools/ (optional, for precise word timing)
- `asr_segments.py` — Whisper large-v3 (sherpa-onnx) per audio segment.
- `probe_pauses.py` — finds which words come before each detected pause.
- `align_words.py` — distributes word starts between verified pause anchors. Its `REVIEWED`/`PROBE` tables are project-specific: edit them per project.
Requires Python 3 + `pip install sherpa-onnx numpy` + a downloaded sherpa-onnx Whisper model. The simpler default is `npx hyperframes transcribe … --model large-v3 --language id`, then checking the timings against `ffmpeg silencedetect`.
