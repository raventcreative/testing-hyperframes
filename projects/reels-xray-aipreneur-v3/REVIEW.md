# REVIEW — REELS X-RAY (AIpreneur V3) — v2 draft preview, NOT final

## v2 (26 Oct) — user elements + REF-H upgrade
- User elements dissected and animated part by part: mechanical phone (S01–S02: body, 5 rotating gear sprites,
  rebuilt 3D glass plane posed with matrix3d), camera rail (S04: rail rebuilt under the cart, dolly glides on the rail
  vector), navy dial (S08: needle/hub/gears re-animated inside the dial's affine), Google logo + user's Claude Code
  screen (S06: REF-M search-bar morph -> line match -> screen unfolds, typing, send). Private "Blocked" session
  names were removed from the screenshot.
- REF-H global layers (pastel plate, 54 px grid, haze, motes, grain) and the bible's caption word-rise.
- Genuine AI PRENEUR logo lockup on a porcelain plate in the final still frame.
- VO-safe SFX: high-passed variants, peak on apex, ducked against the measured VO, typing as one clip per span.
- Docs: production/REFERENCE_MOTION_ATLAS.md, production/MOTION_BLUEPRINT.md.
- QA v2: lint 0 errors; check 4 ranges 0 errors, contrast 54/54; 0 overlapping same-property tweens.

---

Status: assembled preview built and QA'd; **waiting for Freddie's approval before the final delivery render.**
Preview: `out/PREVIEW_reels-xray-aipreneur-v3_draft.mp4` (draft quality).

## What it is
54.6 s, 1080×1920, 30 fps. 18 dioramas in the Ice-Ivory illustrated style (STORYBOARD.md), the user's 3D chibi mascot
as host (bottom-left, real rig), captions word-by-word in the top band, ElevenLabs VO untouched, 42 subtle SFX, no music.

## Measured
- VO timing: MMS CTC forced alignment on the real audio (120 words, 677 phones), cross-checked against a local
  faster-whisper medium transcript and the energy envelope (onsets land on the consonant bursts).
- Lip sync (numeric): mouth vs VO energy cross-correlation lag = 0 frames; mouth closed in every pause and after
  the last word; mouth peaks (183) fewer than vowel phones (282) -> never flaps faster than the syllables.
- `lint`: 0 errors (1 warning: captions.html is long).
- `check` in 4 ranges × 6 samples: 0 errors; layout 0, contrast 10/10 passed; runtime warnings = WebGL ReadPixels notices.
- Determinism: 0 overlapping same-property tweens in all 18 scenes (tools/tween_overlaps.py); forward vs reverse seek
  over 13 timestamps: 11 identical, 2 differ only in 1-px anti-aliasing on edges of 3D-transformed layers (Chrome raster
  cache depends on the previous frame; element positions are identical).

## Smart Motion Director
Library `vendor/motion-director.js` (20 effects, SUBTLE/STANDARD/HIGH). Auto-direction `tools/motion_director.py`:
snap zooms on kebuka / kode / MP4 / baru (HIGH) / EDITOR, one restrained digital zoom on "kredit" in the calm
cost stretch, orbit reveal of the 3D GitHub mark on "repo", host compositing (light wrap + contact shadow) and
a slow camera orbit around the host. Scene mechanics (hinges, rails, presses) carry the rest.

## Not checked / limits
- Nobody has listened to the full mix by ear here.
- The mascot has no eyelids/blendshapes: mouth drawn on the face surface, no blinks, mitten hands.
- White light bursts read softly on the ivory ground; navy rings/edges carry most apex contrast.
- Scene notes from the build: s13's family shot holds ~0.5 s; s17's lid->bubble is a quick crossfade.

## Regenerate
`<venv>/bin/python -I tools/vo_align.py . && python3 tools/build_scenes.py && python3 tools/motion_director.py &&
python3 tools/gen_sfx.py && python3 tools/gen_root.py && python3 tools/gen_mascot.py`
