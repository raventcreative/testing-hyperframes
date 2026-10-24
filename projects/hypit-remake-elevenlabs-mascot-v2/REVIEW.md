# REVIEW — Hypit × ElevenLabs × 3D Mascot (v4 preview, NOT final)

Status: **v4 assembled preview built and QA'd; waiting for Freddie's approval before the final delivery render.**
Preview: `out/PREVIEW_v4_hypit-pro-mascot_draft.mp4` (draft quality). Diagnostic: `out/DIAG_v4_mascot_0-17s.mp4`.
The final render runs only after an explicit "ya". Details: `production/v4_animation_lipsync.md`.

## What changed in v4 (Freddie's 4th revision)
- **Mouth follows the real audio.** Phone-level forced alignment of the VO (local MMS CTC aligner) showed the old
  word timing was up to 0.55 s off — the reason the mouth looked faster than the voice. The measured timing now
  drives lip sync, captions, SFX and every visual hit in the scenes. Mouth opening follows the VO energy; silence = closed.
- **Clean face.** The brown/pink circles were highlight blobs painted in the model's hair texture (29 removed);
  the baked open mouth and its cavity were replaced by clean skin + a new drawn mouth; eyelids use the real skin
  tone; gaze/brow shifts that caused rings were dropped. New cleaned model copy: `assets/mascot3d/mascot_rigged_v4.glb`.
- **Smooth, intentional acting.** Key poses on the spoken words, every bone settled by its own spring
  (anticipation, overlap, follow-through), moments of stillness, nods on stressed syllables, breathing/idle.
- **Half-body only.** Intro: walks forward from the glass arches straight into a waist-up shot waving "hai",
  points at the video card, opens hands on "efek". Other scenes: chest-up host rising from the corner.
- **Reference-grade motion**: 3D hinge card entrances with rack focus, blur fly-outs, 3D whip swings + motion
  blur at whip cuts, slow 3D orbit on every scene, keyword boxes flip up and snap in, halftone film/clapper/camera
  collage, GitHub mark flip (s02) and a 3D GitHub page card on "link repo".
- Text/box gradient changed to **#0a0d2c → #294b77** everywhere.

## Measured (v4)
- `lint`: 0 errors, 0 warnings.
- `check` per range (8 ranges × 6 samples): 0 errors. Warnings: WebGL "GPU stall due to ReadPixels"
  (software renderer notice), caption sheen passing outside its box mid-sweep (intended, clipped).
- Seek determinism (forward vs reverse order, 18 timestamps incl. every mascot and presenter window): 0 changed pixels.
- On-screen text: VO words + the verified install command. Pop-ups are Freddie's images/icons.

## Not checked by anyone
- Nobody has listened to the full mix by ear here (pronunciation flags in `production/transcript_review.md`).

## Known limits
1. No blendshapes/jaw in the GLB → mouth and lids are drawn on the face surface; best from front / ¾.
2. Mitten hands (single bone), no finger poses; brows no longer animate.
3. "Hai" is a gesture only (not in the VO).
4. The GitHub mark and GitHub home-page screenshot are Freddie's supplied assets (third-party trademark,
   used editorially for "repo GitHub" / "link repo").

## Regeneration
`<venv>/bin/python tools/phoneme_align.py . && python3 tools/retime_v4.py . && python3 tools/apply_warp.py . &&
python3 tools/gen_presenter.py . && python3 tools/gen_mascot.py . && python3 tools/gen_root.py .`
Face: `node tools/mascot3d/facepatch.mjs mask|apply …` + `tools/face_texture_clean.py`.
Bundle: from `tools/mascot3d`: `npx esbuild src/mascot.js --bundle --format=iife --minify --outfile=../../vendor/mascot3d.js`.
