# RIG, SUIT, 3D CHARACTER AND BRAND LOGO — NON-NEGOTIABLE QA

## 1. Asset verification BEFORE any animation

1. Inspect the existing project and find the user's mascot source: `.blend`, `.fbx`, `.glb/.gltf`, rig script, layered sprites, or rendered images. Report **actual verified paths and rig capabilities**. Do not call a flat PNG a jointed 3D rig.
2. Locate the user's existing genuine logo and inspect dimensions, alpha channel and aspect ratio. Reference the original file directly. **Never invent or remake** brand icon, letter shapes, spelling, textures or colors.
3. If the user supplied only a still image but asks for convincing full-body 3D, stop and report the limitation, request a rig/layered source, and provide a safe camera/prop-driven fallback preview. Do not hallucinate fingers, knees or cloth simulation.
4. Protect existing assets. Work in a **new scene/remake branch**; avoid overwriting old character files or global suit materials without a backup/diff and explicit review.

## 2. Suit (jas) defect-specific fixes

| Defect to inspect | Required correction | Proof |
|---|---|---|
| Lapel jagged / asymmetric | Contour geometry/smoothing, both sides symmetric under rotation, consistent lapel width and roll | 3/4 close-up left/right, 0°, 45°, 90° turntable frames |
| Collar intersects neck/head | Rework neck clearance, skin weight, depth order, pose-driven deformation | front + profile, idle + head turn |
| Jacket clips chest or arm | Correct topology/weights/mesh depth; sleeve angle follows shoulder without volume disappearing | arm raised/lowered at 0%, 50%, 100% movement |
| Sleeve cuffs glitch | Sleeve length, cuffs and hand intersections; no sudden popping | wrist roll and pointing gesture sampled every 3–5 frames |
| Buttons/tie / undershirt float | Anchor to cloth surface with correct Z offsets and skinning | full-body turntable at 6 angles |
| Flicker/z-fighting | Remove coplanar overlapping faces, adjust depth precision/material normals | slow orbit, identical frames stable |
| Texture stretch | UV maps, color, normal roughness consistency during pose | close-up under key/fill/rim lights |
| Shadow detached | Contact ellipse / actual cast shadow from feet to ground | standing, stepping, stopping |

If there are **no editable 3D geometry/rig assets**, do not claim these problems are fixed. Instead mark `BLOCKED — source rig required`, isolate the affected shot, and offer a crop/pose fallback with honesty.

## 3. Life-like 3D motion, no mannequin stiffness

- Pose system: **gaze leads → head turns → torso follows → arm gestures → wrist/fingers follow-through → settle**. No all-joints-at-once moves.
- Anticipation 4–8 frames, clear action 12–24 frames, follow-through 6–10 frames, settle 8–14 frames at 30 fps (adjust for gesture type).
- Idle: subtle respiration amplitude under 1% torso scale or believable rib/spine deformation, micro weight shifts every few seconds—not sine-wave bouncing of the entire character.
- Feet plant: when speaking/pointing, one weight-bearing foot stays planted. Hip movement matches stance. Avoid moonwalk / foot sliding.
- Face: purposeful blink when shifting attention (not on a fixed 2s loop), eye tracking toward labels, smile/mouth movement only if supported by actual rig. Lip sync should follow the user's VO only if rig supports it and has been visually verified.
- Gesture diversity: pointing once, palm-up explanation, comparing with both hands, touching a UI, thoughtful inspect, nod, relaxed CTA. Do **not** keep a hand permanently raised.
- Character proportions: original scale and identity lock, all scenes; no hand enlargement or limb regeneration by a generative pass.
- Cloth: gravity and material cues. Suit should lag shoulder turns slightly and settle quickly; not viscous wobble. If cloth simulation is unstable at seek/render time, use deterministic keyed deformation instead.
- Camera: 3/4 body shots at 35–50mm equivalent, subtle 4–8° orbit, practical key/fill/rim. Avoid fisheye faces and impossible movement.
- Every dramatic action has **anticipation, contact, recover**, not generic “wiggle/jump/ease out”.

## 4. Three hero actions to inspect extra carefully

1. **S05 folder tap:** fingertip lands on actual folder tab, wrist follows, tab moves with touch; no hand penetration.
2. **S15 before/after slider:** pointer/finger grasps slider exactly; match camera geometry; the improved jacket still works in the middle of the gesture.
3. **S18 CTA:** eye-line to the CTA, delayed open-palm presentation then natural settle; no frozen smile or over-animated jaw.

## 5. Logo animation — animated but tasteful

- Original logo locked top-left, visible throughout. Keep a constant bounding box and original aspect ratio.
- At initial arrival: opacity 0→1 with 4–7px upward travel or subtle scale 0.96→1.00, over 0.36–0.48s. Never stretch.
- Recurring effect (once every approx. 4–7 seconds, **staggered from other bright highlights**): a narrow *moving light sweep* clipped to actual logo alpha, 0.45–0.65s. Add a low-opacity cyan/back-white halo **behind** the logo; never recolor its pixels.
- Light sweep travels left→right and terminates completely. On selected scene apex, pulse scale 1→1.035→1.00 over ~0.32s, but do not obstruct text.
- Last 1 sec: final sheen, calm fully visible lockup. No flickering or glowing continuously. Logo remains readable at 25% video playback scale.

## 6. Visual inspection minimum

Screenshots: first frame, each scene apex, each transition midpoint, six angles of the outfit, critical motion in-between at 0/25/50/75/100%, the penultimate frame and final frame. Check that no mesh folds through another, text never sits over logo, no checkerboard halo, no contrast fail, no one-frame limb pop, and no black transition gaps.
