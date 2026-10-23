# REVIEW — Hypit × ElevenLabs × 3D Mascot (v2 preview, NOT final)

Status: **v2 assembled preview built and QA'd; waiting for Freddie's approval before the final delivery render.**

## What changed in v2 (Freddie's revision)
- **3D mascot from Freddie's GLB**, rigged here (source had no rig): 19-bone skin, surface-following facial controls (blink, happy eyes, gaze, brows, visemes), CTA lip sync. One overlay track `compositions/mascot.html` drives 7 appearances: Hypit intro peek→hold edge→curious tilt→step out→wave (s02), coding-agent "ooh" (s04), editing workflow tracking + lean + brows + point at the trim handle (s06–s08), swap tracking + surprise + open-hands present (s11), approving nod (s14), brief nod (s16), CTA hop-in + point + lip sync + wave + calm closed-mouth final (s19). Details: `production/mascot_rig_qa.md`.
- **Designed transitions at all 18 cuts**: zoom-through / zoom-from, whip left/right, push-up, match + pop, each scene wrapper matched by a root light-streak/flash overlay (`compositions/fx.html`), and the mascot overlay follows the same moves.
- **Word highlights**: karaoke pill travels word-to-word; keyword boxes pop with overshoot, white text jumps in, light sheen sweeps the box.
- **Pop-ups & living detail** in every scene (icon chips, sparkles, sheens, LED chases, rotating mechanisms), stronger camera pushes/punches on apex words.
- **Freddie's 5 reference elements** cut out locally and used: hopper machine (s05 hero), edit desk (s07), glass film (s03, s12), isometric app UI (s04), phone + player (s09 hero). Assumed to be Freddie's own/licensed images.

## Measured
- `lint`: 0 errors; 1 warning kept (mascot.html line count).
- `check` (run per time range because the software-WebGL mascot makes a single full pass exceed the 120 s deadline): runtime 0 errors, layout 0 errors, contrast 0, craft 0. Warnings kept: WebGL "GPU stall due to ReadPixels" (software renderer perf notice), `rotation_pivot_drift` on the s17 needle (intended: it rotates about its hub).
- Seek determinism: 20 timestamps incl. mascot frames, forward vs reverse order → **0 changed pixels**.
- On-screen text audit: only VO words + the verified install command.

## Not checked by anyone
- Nobody has heard the audio (two VO pronunciation flags remain, see `production/transcript_review.md`).
- Lip-sync interior viseme timing is estimated (±~0.1 s).

## Weakest spots
1. s06–s08 deck is smaller (to make room for the mascot) → below the 60–75% hero target.
2. Some whip-in first frames are mostly blur by design (s13, s17).
3. Mascot hands are single bones (no finger poses); eyelids/mouth are shader overlays (best from front/¾ view).
4. Final "HYPIT" still holds ~1.8 s because the film length is locked to the VO end; optional +0.4 s silent hold.

## Regeneration
- `tools/gen_root.py` → index.html, captions.html, fx.html.
- `tools/mascot3d/{prep,rig,facejac}.mjs` → optimized/rigged GLB + face config; `npx esbuild tools/mascot3d/src/mascot.js --bundle --format=iife --minify --outfile=vendor/mascot3d.js`.
- Scene HTML in `compositions/` is the source of truth.
