# Production task plan & non-negotiable QA

## Phase 0 — Inspect existing Claude Code project

- [ ] Identify existing main project root; read available instructions rather than setting up an unrelated new project.
- [ ] Locate actual **mascot 3D/rig/component** files. Record exact paths and how they are rendered/animated.
- [ ] Locate existing **user VO**. Read audio duration, detect phrase boundaries and confirm no new narration is required.
- [ ] Confirm assets/ai_preneur_logo.png, ai_preneur_background.png, click_cursor.png load correctly.
- [ ] Confirm Poppins Regular 400 and Bold 700 are available or added legally.
- [ ] Use a safe new composition/output location without overwriting unrelated working videos.

**Exit criterion:** mascot and VO are both found and load in a minimal test preview. If not found, report missing path and stop; don't create generic stand-ins.

## Phase 1 — Scene timing and art direction

- [ ] Turn the VO into time-coded phrases, preserve natural pauses.
- [ ] Align seven beats from STORYBOARD_30S.md to words and existing audio length.
- [ ] Keep final duration approximately 30 seconds unless real VO length requires a transparent adjustment.
- [ ] Block compositions for room/laptop, Google UI, Claude logo, safe Claude Code, 3D result, half-body mascot/dual-video, and brand finale.
- [ ] Verify safe margins at 1080×1920. No text over a face or sharp upper preview.

**Exit criterion:** annotated storyboard and low-fidelity playblast show coherent room-to-laptop-to-result geography.

## Phase 2 — Visual assets and movement

- [ ] Build room and physical laptop with layered lighting matching the supplied navy background.
- [ ] Use the **existing mascot**, animate slight walk/advance, purposeful hands, torso/head follow, final step back.
- [ ] Reconstruct privacy-safe Google → Claude → Claude Code UI with editable motion, rather than using unsanitized personal screenshots.
- [ ] Implement cursor asset click wave using 2–3 rings, restrained impact-shake and tactile click SFX.
- [ ] Show short believable Code prompt typing and response-progress state; no 5-second loading dead air.
- [ ] Build and render new astronaut/cube/miniature world with stable geometry, believable shadowing and cinematic orbital camera.
- [ ] In mascot explanation scene, derive blurred background and sharp floating 3D video from **the same source render with synchronized source time**.
- [ ] Use true Poppins 400/700 and white/blue accents; white rectangle + blue Bold for selected words.
- [ ] Preserve AIpreneur logo image and background pixel identity, without distortion.

**Exit criterion:** rendered frame and motion previews show correct asset identity, dimension, layout, coherent transitions and no fake AI-like distortion.

## Phase 3 — Audio, render & review

- [ ] Attach original VO only; no TTS replacement or re-scripting.
- [ ] Time captions/emphasis and mascot gestures to actual spoken words.
- [ ] Add SFX at appropriate levels (keyboard, click/rings, logo reveal, code completion, world unfold), ducked under voice.
- [ ] Render draft MP4 and inspect **every scene midpoint and all transition boundaries**.
- [ ] Check no UI-private text or names in frame 0, in center Recent cards, in masked transitions, reflected surfaces, thumbnail previews, or final export.
- [ ] Check logo aspect ratio and highlight readability on 360px-wide phone preview.
- [ ] Verify no static dead-air segments, awkward animation loops, cut-off words, missing VO tails, clipping, black frames, or placeholder geometry.
- [ ] Present draft and request approval before final delivery render.
- [ ] Export final **H.264/AAC MP4, 1080×1920, 30fps** plus editable project. Verify using ffprobe.
- [ ] Return exact final paths and what was genuinely built versus reenacted UI. Do not claim to have captured a live end-to-end generation if UI scenes were recreated.

**Exit criterion:** checked output + approved preview, no remaining blocker, privacy audit passes.

## Fail conditions

- Personal Claude Recent, Projects, artifact cards, prompts, name, browser suggestions, or other sensitive content is visible for even one frame.
- Mascot is a newly invented character instead of the existing one.
- Existing user VO is silently replaced.
- Red/green neon text or non-Poppins caption fonts appear against the user-approved blue/white spec.
- Weak full-rectangle blur is used to conceal sensitive text while it remains faintly legible.
- Result animation copies the previous reference video or contains random AI wobbling/warping.
- Blurred background and sharp floating preview show different animation time positions.
- The final is landscape, portrait with stretched background, or not 1080×1920.

## Output names suggested

- Draft: **out/ai_preneur_claude_opus55_mascot_reel_draft.mp4**
- Final: **out/ai_preneur_claude_opus55_mascot_reel_1080x1920.mp4**
- Preview snapshots: **out/review_frames/** (only privacy-safe final output)
- Source: use the existing project's native editing/rendering composition format
