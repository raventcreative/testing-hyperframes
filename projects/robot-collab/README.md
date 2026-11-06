# AI PRENEUR robot (client's Tripo model) — rig + baked logo + screen face

Source: client's Tripo GLB (1.3 M verts, Draco, no rig). Pipeline (scratch work in the session scratchpad, scripts kept here):
1. `mascot-bizman/tools/prep.mjs <src.glb> robot_rt.glb 0.045` — weld + meshopt simplify to 87 k tris, textures 2048 webp.
2. `tools/dump_robot.mjs` — raw arrays; `tools/texmap.py` — texel → 3D position/normal maps.
3. Baked eyes removed from base / roughness / normal maps (3D-fitted visor colour, feathered by eye radius), UV-rim fix + gutter padding (`tools/gutter.py`).
4. `tools/bake_logo.py 0.27 0.385 0.0` — AI PRENEUR wordmark printed into the 4096 base colour on the collar front with a cylindrical
   projection (constant letter width on the curved shell), satin roughness under the ink, normal map flattened under the print.
5. Emissive mask for the blue lights; `tools/rig_robot.mjs` — bones rig_root > body > head (soft blend over the collar seam), hand_L /
   hand_R (rigid floating hands) + `_FACE` visor coordinates (eyes at s = ±1).
6. Runtime `src/robot.js` (bundled to `vendor/robot3d.js` in the reel projects): screen-face shader (blink, gaze, happy, squint, talk
   bars), light pulse, deterministic `setView` / `setState`.
Result: `work/robot_final.glb` (= `github_gratis_collab_2026/assets/robot3d/robot_aipreneur.glb`).
