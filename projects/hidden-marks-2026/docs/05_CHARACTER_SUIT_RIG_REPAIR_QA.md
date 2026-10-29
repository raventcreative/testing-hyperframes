# MASKOT 3D — repair contract + QA details

User complaint: **gerakan maskot kaku, jas kurang rapi, ada bug render/animasi**. Tidak mungkin menyatakan masalah selesai hanya dengan prompt—harus inspect model real di Claude Code, repair, render test dan dibandingkan.

## Audit sumber (sebelum scene)

1. Temukan asset asli (GLB/GLTF/FBX/Blender/custom Three.js); catat nama file, ukuran, mesh count, material/texture count, bone/clip names dan render stack.
2. Backup secara **non-destruktif** ke folder proyek baru, jangan overwrite file maskot tunggal user.
3. Render front, side, back dan 3/4 pada pencahayaan brand; identifikasi clipping di **rest**, **arm-up**, **hand-forward**, **torso-turn**.
4. Inspect normals, tangents, UV seams, textured shoulder/jacket fabric, lapel depth, single-sided polygons, z-fighting, skin weights, bind pose, bone axes, arm IK, shadow catcher.

## Perbaikan jas sesuai masalah pengguna

| Area | Gejala | Fix / Acceptance |
| --- | --- | --- |
| Lapel kiri/kanan | Beda ukuran, zig-zag, tembus shirt | Align topology, mirror as appropriate, enforce clean seam, thickness, no z-fighting, no face clipping |
| Collar / kerah | Mengambang di tengkuk/menembus leher | Correct base geometry, normals, bind weights and contact placement, keep wearer proportions |
| Bahu | Siluet terpotong atau pecah saat lengan naik | Fix skin weight gradients around clavicle/upper-arm, adjust armhole geometry; test 45°/90° arm raise |
| Sleeve/cuff | Lengan jas menembus tangan/shirt | Collision-safe silhouette across 4 critical poses; align cuff with wrist rig |
| Kancing / tie | Mengambang, geometry off-axis | Align physical attachment to jacket/shirt, check all-angle visibility |
| Front hem | Melintir/tembus kaki saat bergerak | Weighted or shape-corrected hems, no frame-to-frame popping; avoid runtime nondeterministic cloth |
| Fabric | Terlalu glossy, terlihat mainan | Satin suit fabric with restrained roughness/normal variation, no artificial neon shine |

## Perbaikan gerakan

- **Idle:** breathing almost imperceptible, shoulder movement minimal, blink deterministic 3–6 sec apart, no permanent rocking/sway.
- **Anticipation:** head/eyes track prop first, shoulder reacts 2–4 frames later, elbow/wrist follow; character weight shifts into action with planted feet.
- **Grip:** hand/object are kinematically linked at contact, no sliding fingers or prop teleport.
- **Gesture:** arc path rather than linear tween. A quick reach is 0.35–0.65s, smooth acceleration/deceleration, 0.15–0.25s settle and micro follow-through. Actual timing aligned with VO.
- **Walking/turn:** consistent center of gravity, contact foot sole stays planted, hips turn 2–4 frames before upper torso when appropriate; no drifting.
- **Expression:** understated micro smile/brow/head tilt if actual rig allows; do not invent facial rig. No automated mouth movement for VO narrator unless separately requested and supported.
- **Continuous motion proof:** at least 3–5 seconds of repaired animation from several angles. Static good-looking frame is insufficient evidence.

## Must not do

- No masking out suit defects by blurry foreground, fake lens bloom, cropping lower body, hiding in shadow, redrawing a new character or regenerating its face.
- No applying cloth physics that changes when seeking random frames. Cache or bake if needed.
- No 3D asset remeshing that changes facial identity or garment design without user approval.
- No claiming 100% bug free until checked full preview and actual MP4 frames.

## Acceptance evidence

- Three **before** screenshots (if available) and three **after** using identical camera and light; include closeup lapels, shoulder with arm extended, and back of suit.
- Test scene with prop pickup and scanner action, no foot-slide/body stiffness, no interpenetration across at least sampled frames around motion peak.
- Character model hierarchy and repaired file path logged.
- Render quality comparable across ALL 12 scenes, not just one beauty shot.

**Fallback:** If the model has low-quality baked geometry and no editable topology/rig, the proper fix may require a new 3D repair pass in Blender. Report exact issue and required input/approval. A prompt cannot create missing rig information with certainty.
