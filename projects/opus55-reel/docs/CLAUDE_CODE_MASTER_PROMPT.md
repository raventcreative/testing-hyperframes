# MASTER EXECUTION PROMPT — CLAUDE CODE

## Your role / mission

You are the **Lead Creative Director, Senior Motion Designer, 3D Animator, Privacy-Safe Video Editor, and Render QA Engineer**. Produce an exceptionally polished, original, **30-second, vertical (1080×1920, 30fps) AIpreneur reel**, combining an existing **3D mascot** and **existing recorded VO** with an accurate, privacy-safe animated journey: **Google → Claude → Claude Code → 3D animated result → mascot explains result → AIpreneur brand ending**.

**Read every relevant file in this ZIP before coding**, particularly `STORYBOARD_30S.md`, `BRAND_AND_MOTION_GUIDE.md`, `SCREEN_RECORDING_ANALYSIS_AND_PRIVACY.md`, and `BUILD_AND_QA_CHECKLIST.md`. Read existing project docs and inspect its render stack; integrate into the current project instead of blindly scaffolding a duplicate. The user-approved brief in this kit takes precedence over generic house-style prohibitions on characters/mascots, text colors, or fonts.

## Project discovery — mandatory, first

1. Search current project files for the **already-implemented mascot** and its **existing 3D rig/components/animation controls**. Identify the authoritative asset(s), mesh, animation system, and way to animate arm/head/torso and camera. Reuse exactly: **no new substitute mascot**, no changes to face, material, proportions, branding or overall silhouette.
2. Search for **existing user VO audio** (MP3/WAV/M4A/OGG), inspect its duration and words without altering the original. Do not generate a replacement voice, impersonation, or TTS. Sync text, mascot performance, cuts, and impact effects to actual phrases. If VO length differs materially from 30s, prefer matching VO length and note the deviation in preview report, or ask for a cut decision. No speed-changing speech to fit an arbitrary runtime.
3. Use the assets from `Claude_Opus55_Reel_Kit/assets/`, preserving actual pixels/branding. Inspect formats and alpha. Import exact fonts **Poppins Regular 400** and **Poppins Bold 700**; bundle or use appropriate local assets, subject to license.
4. Inspect existing dependencies. Build using the project’s working rendering approach (e.g., Remotion/React/Three.js, HyperFrames/GSAP, or existing WebGL scene code). **Avoid adding a second incompatible rendering stack**. Create a separate video-specific composition/output, preserving unrelated project files.
5. Before implementing all scenes, provide a short asset discovery note containing the maskot component path, VO path/duration, chosen video framework, proposed scene cut timing, and any truly blocking missing item.

## Story & exact scene hierarchy

Story goal: demonstrate believable progression from an idea entered in Claude Code to an original, sophisticated motion graphic; never imply a production screen capture shows a generation that was not captured. The browser/programming interaction is a clean reconstructed demonstration inspired by the user's real recording.

**S1 [0–3s] — Room & hook.** In a well-designed 3D room built to match the provided blue/navy background, place the *existing* mascot in front of a physical desk with credible laptop/monitor. Start with camera already moving, subtle parallax/depth/light, not a static slide. Mascot walks/pushes toward camera or slightly leans into shot and performs a purposeful hand gesture on the first hook phrase. Existing VO only.

**S2 [3–6s] — Laptop to Google.** A single coherent physical camera push travels past mascot shoulder to laptop display. Screen aligns with viewport and transitions seamlessly into a clean recreated dark-mode Google UI. Zoom into search field; typing animation creates exact word **Claude** with blink caret, appropriate key SFX. Cursor asset enters and heads to the relevant search result. Do **not** use actual browser autocomplete / browsing history.

**S3 [6–8s] — Click ripple & Claude logo.** Cursor asset `click_cursor.png` depresses in ~100–130ms, produces 2–3 concentric blue #00C9FF shockwave rings expanding rapidly and fading, plus 2–3px equivalent subtle camera impact (120–160ms), clean click sound. Transition through the click position. Official Claude logo/mark does an elegant 0.3s emergence/soft light reaction, then shrinks to reveal **sanitized** Claude home UI; no user real name, account avatar, private Recent, Projects, or artifacts. Do not redraw/alter a supplied brand logo.

**S4 [8–12s] — Claude to Claude Code; code prompt.** Transition from the safe Claude home UI into a safe, minimal Claude Code workspace. Use plausible terminal/editor UI without fake personal repository content. Cursor types a short prompt (text may be shortened for readability): **“Build a cinematic 3D pocket universe: an astronaut discovers a glowing cube that unfolds into a living miniature world.”** Use real-looking monospace code UI for the editor, while video captions remain Poppins. Enter action → brief status line indicating work underway (not an extended spinner). Make this a cinematic dramatization of a workflow, not a fake recording of a real generation.

**S5 [12–17s] — Original 3D result.** Transition from a luminous pixel/window aperture on the code screen **into a full-screen original 3D animation**: small astronaut character in a bright yet dimensional futuristic environment discovers a detailed glowing cube. The cube's layered panels articulate mechanically and reveal a breathtaking miniature landscape: terrain, skyline, trees, moving clouds, tiny light points/roads. Smooth partial orbit/dolly on the reveal; at least three depth planes, coherent shadows, controlled glow, surface detail, real perspective, imperfect handcrafted micro-motion. **Absolutely no apocalyptic fire, pasted paper character, or reused visuals from previous reference video.** This is a new creative concept, distinct from the old footage.

**S6 [17–25s] — Mascot + sharp video above, matching blurred video background.** The same generated animation (not a mismatched copy) becomes a live blurred background while the already-existing 3D mascot advances into crisp half-body framing at lower/central foreground. At the top of the frame, float a premium dimensional frame showing **the same animation in sharp focus**, synchronized with the blurred background. The video frame sits *above the mascot's head* with sufficient separation; the mascot never occludes important imagery or captions. Small label above frame: **CLAUDE OPUS 5.5**. Mascot points or gestures toward the crisp preview. Avoid unnatural mouth flapping: use authored body/head/hand performance; only add lip-sync if existing rig actually supports trustworthy mouth motion and audio alignment.

**S7 [25–30s] — Finish.** Last beat of miniature universe, panel shrinks back into the monitor along a coherent camera path. Mascot steps back; 3D room returns. AIpreneur wordmark from `assets/ai_preneur_logo.png` resolves beautifully (do not redraw or retype the brand logo). A short CTA supported by the existing VO can appear using Poppins. End with at least 0.4s of clean complete brand lockup, no dark blank ending.

**Caveat:** Scene timings are target beats, not a license to cut through words. Re-time to the **real existing VO** using phrase boundaries; deliver an updated time-coded storyboard with actual VO timings.

## Visual design locked by user

- Video: **1080 × 1920, 9:16 portrait, 30fps, ~30s**, export H.264 MP4 + AAC audio.
- Existing background: `assets/ai_preneur_background.png` is **1080×1350**. Extend to full 1080×1920 using matching blue/navy gradients and softened edge extension; **never stretch it vertically** or use ugly letterboxes.
- Typography: **Poppins Regular 400** for narrative / connective words; **Poppins Bold 700** for impact words. Core colors **#FFFFFF** and **#00C9FF**. For highlighted words, use a compact **solid #FFFFFF rectangle with #00C9FF Poppins Bold text**, padded and rounded subtly. No noisy continuous lower thirds, no giant paragraph overlays, no random fonts.
- Caption placement: maintain readable title-safe zone; caption not collide with top sharp floating video frame, mascot face, or logos. Highlight on actual keyword accent, with rhythm aligned to VO.
- Click cursor: use **actual user-supplied** `assets/click_cursor.png`, not a generic substitute. Add short scale compression + wave shock rings + restrained impact shake.
- Use provided AIpreneur wordmark **as image**, preserve aspect, transparency, wordmark design.
- Design quality: premium human art direction; realistic camera language and lighting, controlled rather than excessive particle noise; purposeful cinematic transitions, optical depth-of-field, parallax, physical light response, temporal coherence, careful easing; no AI-looking wobbly geometry or melting objects.

## Privacy-first, non-negotiable

**The original 35.276s 1920×1032 screen capture was analyzed but NOT supplied in this kit**, because it displays private Claude Recent/Projects and recent-artifact cards, plus possibly browsing-history suggestions. Reconstruct only the public/neutral interface portions, using `SCREEN_RECORDING_ANALYSIS_AND_PRIVACY.md` as the timing reference. Never invent or expose actual project names. If an original recording is later added to the project, use privacy redaction **before scaling/zooming**, cover full sensitive regions with opaque replacements (do not rely on weak blur), inspect frames at every transition, and ensure names cannot be reconstructed. Do not output private screenshots, original raw capture or any privacy-unsafe intermediate in deliverables.

## Sound, VO & motion

- Existing VO is the master timeline and never replaced. Time the mascot gesture to meaningful words; only include words on screen that are in voiceover or exact product/interface labels approved above.
- SFX restrained but satisfying: keys, UI click, shock ripple, tiny logo reveal shimmer, computer confirm, cube unfolding mechanisms, world reveal. Duck SFX under VO; never obscure spoken words.
- Keep continuous music only if existing project has licensed track or make a safe original/simple soundtrack; do not use unauthorized copyrighted music.
- No frame frozen >0.7s except intentional final brand lockup. Avoid long fake loading. Anchor impactful motions on narration emphasis, not arbitrary random cuts.

## Build process and gates

1. **Discover and confirm existing mascot and VO**; inspect existing project dependencies and assets. Surface any blockers honestly.
2. Draft precise storyboard based on detected VO phrase timings. Write out shot compositions, keyframe plan, UI-safe assets, and compositing layer order.
3. Build **a 5–7s look-development preview** covering Google click → Claude logo → Code, and one 5s sample for astronaut cube → miniature world (may be reviewed separately). Check that the palette, logo, cursor, and highlight treatment are correct before full render.
4. Complete the ~30s project with correct reusable scene components and meaningful animated performance. Compose the sharp preview video and blurred background from the **same source render and playback clock**.
5. Produce **draft MP4**. Review scene boundaries, privacy, text edges, camera collisions, mascot continuity, audio mix, and legibility on mobile; iterate until visibly premium.
6. **Request approval of draft before delivery render.** Then render final `out/ai_preneur_claude_opus55_mascot_reel_1080x1920.mp4` and preserve editable source.
7. Run `ffprobe` validation (1080×1920, 30fps, target length, H.264 + AAC), screenshot midpoints + first/last frames, detect blank frames, audit private content and all readable text.

## Required handoff report

Provide: discovered mascot path, VO path and duration, framework chosen, deliverable preview path, final video path once approved, list of source files added/changed, asset provenance, privacy audit result, and any constraints or compromises. Do **not** falsely claim real API generation if the Code scene is a reconstructed demonstration. **Do not stop at writing plans only; implement and preview.**
