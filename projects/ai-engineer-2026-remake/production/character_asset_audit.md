# Character asset audit — the user's suit mascot

- **Source asset (user-supplied, this session):** `cute_chibi_boy_3d_model-compressed.glb` (Tripo export, Draco + WebP, 1 mesh,
  0 skins / 0 animations, 988k verts). Kept untouched in `projects/aipreneur-maskot-jas-test/mascot3d_v2/original_tripo.glb`.
- **Runtime copy used here:** `assets/mascot3d/mascot_jas2_rigged.glb` — built non-destructively by
  `projects/aipreneur-maskot-jas-test/tools/m3d/` (simplify to 87,972 verts -> `rig_jas2.mjs` 19-joint skin measured from the
  mesh cross-sections, arm/torso seam cut so the sleeve separates cleanly, flattened baked-smile groove; texture clean-up
  `clean_tex2.py`: baked smile painted out, hands one skin tone, jacket bake specks + cuff edge cleaned, UV seam padding).
  Geometry, face, hair, clothes and colours are the user's model; nothing was regenerated.
- **Rig:** hips, spine, chest, neck, head, shoulder/upperarm/forearm/hand L+R, thigh/shin/foot L+R. Mitten hands (no finger
  bones) -> gestures are arm/hand-level only. Wide sideways arm abduction exposes the armpit seam -> not used in this video.
- **Face:** no morph targets. Mouth = procedural shader viseme layer driven by the CTC phones + VO energy (closes in silence);
  blinks = shader eyelids painted after lighting (skin lid + lash line), seeded deterministic schedule.
- **Logo on the jacket:** the misprint-free AI PRENEUR wordmark (user PNG) as a curved surface decal on the right chest,
  parented to the chest bone (`tools/decals.json`).
- **Render path:** one persistent WebGL canvas (Three.js via `vendor/mascot3d.js`, bundled from
  `projects/hypit-remake-elevenlabs-mascot-v2/tools/mascot3d/src`), seeked by frame time inside the HyperFrames seek handler;
  springs pre-simulated over the whole timeline -> deterministic and order-independent.
