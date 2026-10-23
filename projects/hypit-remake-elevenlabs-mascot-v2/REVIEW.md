# REVIEW — Hypit × ElevenLabs × Mascot (preview stage, NOT final)

Status: **assembled preview built and QA'd; waiting for Freddie's approval before the final delivery render.**

## What was built
- HyperFrames v0.8.186 project, 1080×1920, 30 fps, 61.100 s (1833 frames).
- Root `index.html`: supplied `background_asli.png` (uniform cover, no stretch) under every frame, ONE ElevenLabs `<audio id="vo">`, one caption sub-composition, 19 scene hosts, 27 low-volume SFX (bundled Pixabay-licence library).
- `compositions/s01…s19.html`: one hero object per VO phrase, built in SVG/CSS + one paused GSAP timeline each.
- Mascot: 3 transparent cutouts made locally from the supplied sheet (labels/white removed, identity untouched), whole-sprite motion only, in s02/s04/s08/s11/s14/s16/s19.

## Measured (not just looked at)
- `npx hyperframes lint .` → 0 errors, 0 warnings (21 files).
- `npx hyperframes check . --json` → ok. runtime 0, layout 0 errors (7 info: camera wrappers intentionally larger than frame), contrast 13/13 pass, craft 1 warning kept (see below). Report: `production/qa_check.json`.
- Seek determinism: 14 timestamps snapshotted in forward and reverse order → **0 changed pixels** at every timestamp.
- Each scene builder also ran per-scene determinism tests (all 0 px).
- Review sheets: `.hyperframes/artifacts/review/` (beats, seams across all 18 cuts, phone-width).

## Looked at, not measured
- Hero size/detail/planes per scene vs REF-H craft (contact sheets per scene).
- Mascot edges on the light background (no white halo seen at 3× zoom).

## Not checked by anyone
- Nobody has *heard* the audio. Two VO items are flagged in `production/transcript_review.md` ("per katanya" possibly spoken as "perkataannya"; "Claude" pronounced like "Cloud").
- SFX levels are set by volume (0.08–0.25 under the VO); measured after render only by loudness, not by ear.

## Warnings kept on purpose
- `line_unread` on the final "HYPIT" letters: on screen 1.80 s vs the 2.0 s guideline. Cause: video length is locked to the VO end (61.1 s) per brief. Fix option: add a ~0.4 s silent hold at the end (VO untouched).

## Weakest shots / what I'd improve with more time
1. s11 last ~0.3 s: stage is briefly sparse while tray/mascot leave and the frame shrinks into s12's card.
2. s12: variant cards are small (≈210 px), so their inner detail is tiny on a phone.
3. s05–s08 share one deck silhouette (deliberate match-cut chapter) — less variety than four different heroes.
4. Interior word timings are estimates (±~0.1 s); apex actions on words right after pauses are tighter (≈±0.03 s).

## Generators (re-running overwrites hand edits)
- `tools/gen_root.py` → index.html + compositions/captions.html (from production/word_timing.json, production/scenes.json, tools/sfx_plan.json).
- Scene builders used scratch generators for s05–s08 and s09–s12; the HTML in `compositions/` is the source of truth now.
