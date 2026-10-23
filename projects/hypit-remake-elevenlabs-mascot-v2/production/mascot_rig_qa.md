# 3D Mascot — rigging, facial & lip-sync QA notes

## Source inspection (measured)
- File: `assets/mascot3d/mascot_source_tripo.glb` (Freddie's upload, untouched). Generator: glTF-Transform; Tripo AI mesh.
- 1 mesh, 993,200 vertices / 1,909,784 triangles, Draco-compressed, 3 WebP textures 2048² (base colour, normal, roughness/metal).
- **No skeleton, no skin weights, no morph targets/blendshapes, no animations.** Eyes, brows and mouth are baked into the texture; the mouth is also a sculpted cavity and the eyes are slightly domed geometry.
- The original was **not rigged** — everything below was built on a copy.

## What was built (non-destructive copies)
| File | What |
|---|---|
| `assets/mascot3d/mascot_rt.glb` | optimised copy: welded + meshoptimizer-simplified to 133,682 triangles, textures kept 2048² WebP (`tools/mascot3d/prep.mjs`) |
| `assets/mascot3d/mascot_rigged.glb` | skinned copy: 19-bone armature + JOINTS_0/WEIGHTS_0 + `_FACEMASK` attribute (`tools/mascot3d/rig.mjs`) |
| `assets/mascot3d/face_config.json` | measured facial landmarks + local UV Jacobians for gaze/brow shifts (`tools/mascot3d/facejac.mjs`) |
| `vendor/mascot3d.js` | runtime (three.js r170 + skinning + facial shader + acting/lip-sync helpers), bundled locally from `tools/mascot3d/src` |

### Armature (19 bones)
hips → spine → chest → neck → head; chest → shoulder/upperarm/forearm/hand ×2; hips → thigh/shin/foot ×2. Joint positions measured from orthographic silhouettes of the model.

### Skin weights
Inverse-distance (power 6) to bone segments, gated by body region (hair never follows the arms, hands never follow thighs), 6 Laplacian smoothing passes that respect the gates, coincident UV-seam vertices unified (prevents seam cracks), top-4 influences.

### Facial controls (surface-following, no stickers)
Implemented in the material shader using the vertex's **rest-pose position**, so every control rides on the actual face surface and follows head rotation/skinning:
- Blink (upper lid per eye), lower lid / happy "^ ^" eyes, gaze (iris re-sampled inside the eye opening via the local UV Jacobian), brow raise/tilt (texture shift on the brow region), mouth visemes (baked mouth covered with skin, procedural mouth drawn in place).
- Under covered regions the normal is replaced by a smooth head-sphere normal (follows the head bone) so lids/closed mouth shade like skin instead of showing the domed eye/cavity geometry.

## Verified (rendered stills, `npx hyperframes snapshot`)
- Poses: wave, point, open-hands present, lean/think, surprise recoil, walk step, nod, head turns — no tearing, no seam cracks after fixes (earlier versions showed shirt-hem drag and white seam cracks; both fixed and re-checked).
- Face: blink closed, happy eyes, gaze L/R, brow raise, visemes AA / E / I / O / U / MBP / rest.
- In-film: CTA close-ups at 59.0–61.05 s show distinct mouth shapes on Komen / HYPIT / Nanti / gue / bagiin and a closed smiling mouth at rest.

## Lip sync (v3: narrator)
- The **whole VO** is lip-synced whenever the mascot is visible (≈41 s of 61 s): `vendor/vo_words.js` (145 words, generated from `production/word_timing.json` by `tools/gen_vo_words.py`) → `buildSpeech()` / `lipAt()` in `tools/mascot3d/src/acting.js`.
- Indonesian grapheme→viseme mapping (a→AA, e→E, i→I, o→O, u/w→U, m/b/p→MBP, f/v→FV, others→C, "ng" merged); HYPIT/Hypit spoken as "hai-pit", Claude as "klod", AI as "ei-ai". Coarticulated with sine blends; the mouth closes only in real gaps (>70 ms) and rests in a closed smile in silences.
- Talking body language from the same timings (`talk()`): alternating hand gestures per phrase, a beat per word (stronger on caption keywords), keyword nods, head bob, body sway. Not amplitude-driven; no extra dialogue.

## Known limitations (honest)
1. **Hands are single bones** (mitten-style chibi hands): wrists rotate, fingers do not curl — pointing is done with arm/wrist direction, not an index finger.
2. **Brows**: the left brow (screen-left) is mostly hidden under the bangs; brow motion is subtle by design (texture shift, not geometry).
3. **Eyelids / mouth are shader overlays**, not new geometry: they read correctly from front and three-quarter views; at strong side angles the domed eye/mouth cavity silhouette is unchanged.
4. Interior word timings are estimates (±~0.1 s) → visemes inside words can be up to ~3 frames early/late; word onsets after pauses are tighter.
5. Back of the polo has unreadable texture text from the Tripo source ("NMCE\"); camera angles avoid showing it.
6. Rendering is software WebGL (SwiftShader) in this container; deterministic but slower to render.

If Freddie later provides a professionally rigged GLB/FBX with finger bones and facial blendshapes (ARKit/visemes), the acting track in `compositions/mascot.html` can drive those directly for richer hands and mouths.
