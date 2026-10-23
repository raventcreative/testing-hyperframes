# REVIEW — Hypit × ElevenLabs × 3D Mascot (v3 preview, NOT final)

Status: **v3 assembled preview built and QA'd; waiting for Freddie's approval before the final delivery render.**
Preview: `out/PREVIEW_v3_hypit-narrator_draft.mp4` (draft quality). Final render runs only after an explicit "ya".

## What changed in v3 (Freddie's 3rd revision) — details: `production/v3_narrator_presenter.md`
- **Mascot is the narrator**: mouth lip-syncs the whole VO whenever he is on screen; talking hands alternate per phrase with a beat on every word, nods on keywords, head bob and body sway (smooth curves, no pops).
- **Opening "hai"**: walks toward camera out of the glass-arch podium while waving, then explains in front of the blurred scene.
- **Presenter scenes** (big mascot in front, background blurred, elements popping around him): 0–4.2, 9.05–13.8, 40.6–46.87, 56.6–58.73 — pixel cursor clicks the video player, the reference video flies into the agent workspace, "jangan" stop-hand + no-sign on someone else's content, footage/music/image chips drop into the folder + shield on "jelas", link / folder / guide pop-ups on the CTA question.
- **Bug fixed**: the intro vault mask no longer slices through his body when he steps out.
- **Stronger transitions**: global stage camera punch + roll at every cut on top of the zoom/whip/push wrappers; 4.2–16.87 is one continuous mascot take (peek → presenter → corner cameo).
- 12 extra subtle SFX for the new pop-ups and clicks.

## Measured (v3)
- `lint`: 0 errors; 1 warning kept (mascot.html line count).
- `check` per range (0–8 … 56–61.05, 6 samples each): 0 errors. Warnings: WebGL "GPU stall due to ReadPixels" (software renderer notice); 4 transient caption contrast samples at ~20.6 s while the keyword boxes are mid-pop.
- Seek determinism (forward vs reverse order, 16 timestamps incl. every presenter window): **0 changed pixels**.
- On-screen text: VO words + the verified install command only. Pop-ups are images/icons, no new text.

## Not checked by anyone
- Nobody has heard the audio (VO pronunciation flags in `production/transcript_review.md`).
- Lip-sync interior viseme timing is estimated (±~0.1 s).

## Known limits
1. Mouth/eyes are shader overlays (the GLB has no blendshapes or jaw); best from front / ¾.
2. Mitten hands (single bone): no finger poses.
3. "Hai" is a gesture — the VO has no "hai" word.
4. The walk toward camera is staged (orthographic scale + floor line).

## Regeneration
`python3 tools/gen_vo_words.py . && python3 tools/gen_presenter.py . && python3 tools/gen_mascot.py . && python3 tools/gen_root.py .`
Bundle: from `tools/mascot3d`: `npx esbuild src/mascot.js --bundle --format=iife --minify --outfile=../../vendor/mascot3d.js`.
