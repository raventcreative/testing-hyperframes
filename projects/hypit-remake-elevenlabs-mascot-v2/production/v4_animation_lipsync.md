# V4 — pro mascot animation, audio-driven lip sync, reference-grade motion

Freddie's 4th revision: mascot still stiff / not smooth, brown circles on the face, walk-in should be
half-body with pointing, smoother wave, hands never dead; study the 3 reference videos; new assets
(GitHub page + mark, halftone film strip / clapper / camera); text gradient #0a0d2c → #294b77.

## 1. Reference analysis (what was taken, what was not)
| Ref | Techniques observed | Applied here |
|---|---|---|
| A (8.9 s, Claude chat promo) | light streak → icon spin-in, UI materialising out of blur (depth of field), push-in while a cursor clicks, text dissolving in blur | rack-focus entrances (blur 16 px → 0), cursor clicks on cards, blur-through exits |
| B (36 s, edit-agency promo) | 3D cards tilted in perspective, fast whips with motion blur, kinetic type, halftone collage cut-outs (clapper, camera), word walls | 3D hinge entrances (rotateY ±72° → rest angle), 3D whip swing of the whole stage at every whip cut, halftone film/clapper/camera cut-outs |
| C (18 s, "editing is a skill") | small context word + big bold keyword snapping in with blur, 3D objects with thickness turning, objects exiting with blur | keyword caption box flips up in 3D (rotateX −85° → 0) and its text snaps from 175 % with blur, slow 3D orbit on every scene |

Not copied: no logos, footage, wording, colours or layouts of the reference creators.

## 2. Lip sync — driven by the real audio
- **Forced alignment**: MMS-300m CTC aligner (ONNX, local CPU, `tools/phoneme_align.py`) on
  `assets/vo_elevenlabs_final.mp3`, character level on the spoken form (Indonesian orthography ≈ phonemes;
  English words spelled as heard: Claude→klod, HYPIT→haipit, code→kod, agent→ejen, …) →
  `production/phoneme_timing.json` (766 phones, 20 ms grid). Every word onset verified on speech energy (> −38 dB).
- **Finding**: the v3 word timing (Whisper + estimates) was off by 0.13 s on average and up to 0.55 s
  (e.g. "lo kasih satu video" started ~0.5 s later than estimated). That is why the mouth looked faster than the VO.
  v4 makes the measured timing the master clock for lip sync, captions, SFX and the visual hits in every scene
  (`vendor/timewarp.js` re-maps each scene timeline through old→new word starts; transitions stay pinned).
- **Mouth** (`buildLipTrack` in `tools/mascot3d/src/perform.js`): shape = Gaussian-weighted blend of the aligned
  vowels (≈55 ms coarticulation); openness = vowel opening × measured VO energy (100 Hz envelope), so the jaw
  cannot move ahead of or faster than the audio; m/b/p press the lips shut while they sound; silence = closed smile;
  zero-phase low-pass (≈5–10 Hz) removes jitter without adding lag.
- Validated frame-by-frame on the diagnostic render (closed at 9.97–10.23 s gap, opens on "lo kasih …").

## 3. Body animation — layered and physically settled
- Layer 1: key poses per body track (left arm, right arm, torso, head, root) placed on the measured word times,
  held between beats (stillness), with an automatic 10 % anticipation on big arm moves.
- Layer 2: every bone channel chases its target through its own damped spring (shoulder fast, forearm slower,
  hand slowest & least damped) → overlapping action, follow-through and natural settle; no linear or sine moves.
- Layer 3: dialogue accents — small head nods on stressed syllables measured from the VO energy.
- Layer 4: lip sync (above). Layer 5: breathing + slow value-noise weight shift, short blinks (≤1 closed frame).
- Framing is half-body only: waist-up presenter (intro walks forward from the glass arches straight into a
  waist-up shot waving "hai"), chest-up host rising from the bottom corner in the other scenes. Legs never shown.

## 4. Face clean-up (non-destructive: `assets/mascot3d/mascot_rigged_v4.glb`)
- The "brown/pink circles" were flat highlight blobs painted into the Tripo hair texture: 29 detected
  (`tools/face_texture_clean.py`) and inpainted from the surrounding hair.
- The baked open mouth (lips, teeth, tongue, cavity) painted out to skin; the sculpted cavity filled by projecting it
  onto a surface fitted to the surrounding skin (`tools/mascot3d/facepatch.mjs`); normal map flattened there.
- New procedural mouth (soft smile line closed; cavity, upper teeth and tongue when open) drawn on clean skin.
- Eyelids sample the real skin colour around the eye; closed eyes become a curved lash line. Gaze and brow
  texture shifts are no longer used (they caused the ring/duplicate-brow artifacts).

## 5. Honest limits
- The GLB has no facial blendshapes or jaw bone: mouth and lids are shader-drawn on the face surface; best from
  front / ¾ (the camera stays there). Hands are single bones (no finger poses).
- Phone timing is on the acoustic model's 20 ms grid; interior consonant timing can be ±1 frame.
- Brow acting is not available any more (texture shift looked broken); emotion comes from head, body and mouth.
- "Hai" is a wave gesture only — the VO has no "hai".
