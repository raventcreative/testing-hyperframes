# COPY THE ENTIRE PROMPT BELOW INTO CLAUDE CODE

You are the **AI PRENEUR senior creative director + technical animation director + 3D character artist + HyperFrames lead engineer + final QA lead**. Build a polished, original Indonesian Instagram Reel titled **THE INVISIBLE LAYER**, inspired by the *logic and topic* of the uploaded 51.5-second reference, not by copying its original footage/characters/memes/graphic style.

## Expected outcome

Create an **editable, complete, running** 1080×1920, 30fps video project containing 12 premium 3D motion scenes, narrator VO sync, physically motivated transitions, beautiful but highly legible typography and a repaired **existing mascot**. Generate contact sheets and a **draft assembled preview**; audit it. Ask for user's approval before full-quality final render. If the recorded VO isn't available, create the scene structure and high-quality still/short lookdev tests; **do not fabricate a final narration or pretend lip sync is done**.

### Materials to locate relative to this prompt file

- `assets/background_ice.png` — user's pale-white/ice-blue background, 1080×1350.
- `assets/logo_aipreneur_dark.png` — actual dark AIpreneur logo PNG, 1485×1485 with alpha canvas.
- `reference/original_hidden_ai_marks.mp4` — source reference, analyze-only, NO video/audio assets reused in new render.
- `reference/source_contact_sheet.jpg` — visual research reference.
- `02_NASKAH_VO_FINAL.txt` — authoritative Indonesian words.
- `03_STORYBOARD_SCENE_BY_SCENE.md` — exact 12-shot concept and motivation.
- `05_CHARACTER_SUIT_RIG_REPAIR_QA.md` — **strict mascot quality contract**.
- `06_CHECKLIST_JEJAK_LEAD_MAGNET.md` — actual resource for promised CTA.

Find an **actual user-provided 3D mascot** already in the Claude Code workspace. Search relevant assets/components for `.glb`, `.gltf`, `.fbx`, `.blend`, material maps, animation clips, skeleton controllers, Blender scripts, model loader hooks. Keep original identity: face, silhouette, clothes, color, proportions, accessories. Do NOT create a new mascot. If source mesh/rig cannot be found, stop for exact path, don't replace with an image gen.

### Crucial: character repair precedes video animation

This isn't just an editing task. User reports the mascot looks **stiff, its suit/jacket is messy, and 3D render bugs persist**. Before creating scenes, inspect the actual mesh at front/side/back and action poses; fix *the causes*, not just visual coverups.

**Rig quality pass**: validate model scale/origin and hierarchy, duplicate/skinned components, skinning matrices, bone transforms and bind/rest pose, missing keyframe clips, shoulder/elbow/wrist weights, neck/head look target, leg/foot IK, hand grasp, and facial controls if they exist. Test 4 poses: neutral idle, reach file, scanner press, camera-facing wrap-up. Fix intersecting sleeves/forearms, shoulder collapse, overly linear body movement, foot sliding and bad hand-object contact. If there is no real arm rig, DO NOT fake independent arm motions by rotating the entire model; use only legitimately supported motion and flag unfixable requirements.

**Suit tailoring pass**: inspect jacket mesh for collar float, broken lapels, left/right asymmetry, shoulder silhouette, collar-to-neck overlap, armhole puckering, sleeve/cuff intersection, tie/shirt clipping, button misalignment, front flap and hem geometry, holes, flipped normals, UV/material seams, z-fighting, incorrect transparency and texture stretching. Align lapels and buttons without changing costume identity. Repair normals/weights, add appropriate smooth shading and physical thickness while keeping silhouette consistent. Use local Blender tools if installed; otherwise in-place GPU mesh/material fixes only when they actually resolve the pixels. Work on **a copy** of the 3D source; never destructively overwrite the only original file. If substantial remeshing is required, report the blocker and ask for approval.

**Acting animation pass**: create restrained performer-level acting with natural 3-stage gestures (anticipation → action → settle), eased arcs, shoulder-elbow-wrist cascade, believable pelvis mass shift, head subtly leading torso by 2–4 frames, eyes leading object target if supported, seeded blinking, slow breathing, and planted feet. Avoid manic expressions, procedural jitter, constant floating arms, over-stretch, robotic T-pose, fake lip sync or perpetual bobbing. The 3D mascot is a physically present **digital investigator**, not a dancing cutout.

Test all repaired actions from two 3D angles, under production lighting, with 3–5 representative frames including peak deformation. No scene build until `CHARACTER_QA_PREVIEW` shows jacket clean and natural gestures. If it cannot pass, clearly report failures and possible fixes rather than claiming perfect.

## AI PRENEUR BRAND LOCK — USER OVERRIDES ANY OLD PROJECT DEFAULT

- Format: **1080×1920 9:16 vertical**, **30fps**, voice-driven final duration ~55–70 s as measured from recorded VO (not a rigid target).
- Background: use `background_ice.png` on all scenes. Keep its actual light white-blue gradient. Source aspect is 1080×1350, so **preserve its proportions**, derive generous edge-extension or color-matched gradient at top/bottom to make 1080×1920. Never stretch the photo. Add subtle optically coherent ground plane and object shadows; do not cover it with full dark background.
- Font: **Poppins Bold 700 and Poppins Regular 400 ONLY**. Do not substitute Montserrat, Inter, generic futuristic display fonts, or monospace for visible narration. User font choice explicitly wins over any template or old house style.
- Regular headline/caption: **ink gradient `#0A0D2C → #294B77`**, applied to Poppins. Deep enough contrast on white background, crisp rasterized letters, no double drop-shadows.
- **Important highlighted word treatment**: text itself pure **WHITE `#FFFFFF`**, encapsulated by a **solid navy gradient pill/rounded rectangle** (`linear-gradient(108deg,#0A0D2C 0%,#294B77 100%)`, radius ~15–22px). Add refined **blue glow to the highlight BOX ONLY**: a soft 10–18px blurred navy/ice-light rim at 0.18–0.30 opacity, brief 0.25–0.40s power3.out bloom timed ON the corresponding spoken keyword, settle to subtle low-glow. Add one tiny specular glint to selected high-impact keyword boxes only. NEVER create illegible white text on pale background, blurry blue letter glyphs, permanent neon or full-screen blooming lines. Screen shot both in active glow state and resting state.
- Persistent genuine AIpreneur logo at **top-left**, displayed logo letters at an actual legible width ~170–215px; the source has much transparent padding, so **trim transparent padding only**, leaving every nontransparent artwork pixel unchanged. Correct source proportions and premultiplied alpha fringes. Start with a **small 8°? no**: tiny 2–3° counter-tilt easing into straight line + 12px slide in first 0.45s. Then keep stable. Every **7–9 seconds**, send a **single 0.6–0.9s alpha-masked light leak sweep** along the inside of the wordmark: narrow white-to-ice streak, luminance 0.18–0.28, no alpha blowout, not a glow halo around image bounds. A tiny bright exit glint on final letter allowed, 0.15s. No exaggerated movement, no flicker, no constant breathing/scale. Logo persists in the root, not restarted scene-by-scene; no text or mascot behind it.
- Materials: tactile porcelain / ivory, glass plaque, satin navy enamel, brushed graphite, physical printed paper, microfasteners, tiny chamfers, accurate contact shadow; avoid glossy AI-plastic, random bubble geometry, heavy bokeh, bright teal HUD overlays, default 3D spheres, oversaturation, and pseudo-holographic noise.
- Key light upper-left, reflections obey viewing angle, consistent direction in every shot; max 2 gentle environment lights + specific hardware mini-lights.
- VO is the one user-supplied file. **No BGM**. SFX only from clearly licensed/user-supplied sources; if unavailable, leave SFX silent. The original MP4 audio must never enter the final edit.

## Creative world: THE INVISIBLE LAYER

One original 3D stage: elegant **digital forensics laboratory** in an ice-white studio. The same source file/card (a physical file-shaped translucent glass tile) stays in the viewer's mental model throughout: first unopened, then its outer metadata layer removed, its internal watermark shown conceptually, two official check stations, then checklist. The mascot inspects and manipulates real 3D objects; it does NOT repeatedly point at screen text with stiff arm swings.

**Story truth:** Some supported AI outputs may carry provenance signals. There is a difference between (1) signed metadata like C2PA and (2) an embedded watermark/text model signal. Unicode hidden characters are not proof of universal AI watermarking. Removing metadata does not imply removing an in-content mark. “No signal detected” does not prove the content was authored by a human. Specific capabilities/format support vary by product. Never promise automatic removal or fooling detection; the video teaches inspection and accuracy.

Use sources `07_OFFICIAL_SOURCES.md`: Anthropic official watermark & Content Credentials, Claude Content Checker (checks supported file marks, **not text watermark**) and OpenAI Verify (supports images/audio, not publicly text). Don't fabricate a successful checker scan or mock an official verified status. If you need website UI, request/capture genuine allowed browser recording locally; otherwise build clearly illustrated *concept* stations with authentic names, not fake screenshot pixels.

## Storyboard: implement 12 distinct physical scenes

Use `03_STORYBOARD_SCENE_BY_SCENE.md` as primary shot instructions. The following is the sound-to-visual execution intent:

1. **Cold open — belief reversal**: on spoken “Hapus metadata belum tentu menghilangkan jejak AI”, an exterior ID badge peels away from a glass file, BUT an internal signal pattern remains. Mascot performs the peel with a correctly animated hand/contact. Camera near macro 50–85mm. Visible frame 0, no empty fade. Highlight phrase `BELUM TENTU HILANG` glows once.
2. **One file, two layers**: camera tracks through the same glass file, zooming to nested real depth planes. Character manipulates a separation ring. UI labels `METADATA` and `WATERMARK` are separately anchored to layer surfaces.
3. **Metadata = ID card**: outer provenance badge materializes as a small, precise ID card with `C2PA`. Show the mechanics of how a label attaches to a supported file. No counterfeit signature graphics.
4. **Embedded watermark**: camera penetrates the outer layer into canvas fabric/pixel substrate; a subtle in-content pattern exists as an **illustrative metaphor only**. Mark `WATERMARK DI KONTEN`, not cartoon binary rain.
5. **Hidden Unicode caveat**: minuscule invisible text marks in a clean editor are revealed by a UV scan, then a physical stamp `BUKAN BUKTI OTOMATIS`; must not imply the detected symbols are Anthropic's proprietary watermark algorithm.
6. **Different products, different supports**: two precise bays with `CLAUDE` / `OPENAI`; separate model text/file mark and supported image/audio provenance contexts, no invented universal coverage.
7. **Removal limitation**: microscope sees the exterior metadata label lifted; internal signal layer remains indeterminate; no triumphant 100% “clean” checkmark. Highlight `GAK OTOMATIS HILANG` with controlled bloom.
8. **Inspect original file**: mascot places the original in a mechanical inspector with visible input slot and file-type selector. The camera follows its corner through the scanner.
9. **Checker**: two physically built verification stations labeled `CLAUDE CONTENT CHECKER` and `OPENAI VERIFY`; show eligibility/type differentiation; do NOT fabricate actual site UI/results.
10. **Result interpretation**: three drawers `TERDETEKSI`, `TIDAK TERDETEKSI`, `TIDAK DIDUKUNG`. Focus `TIDAK TERDETEKSI ≠ MANUSIA` as a clear disclaimer, not malicious scary graphic.
11. **CTA checklist**: one drawer opens into genuine **JEJAK** checklist present in the package. Mascot calmly presents it with believable grip/eye gaze, no plastic freeze-face.
12. **End lockup**: slow dolly-out shows entire lab and both file layers. `KENALI ASAL FILE` then short CTA only if exact spoken. Logo glint crosses once near final beat, finish on 0.3s still frame. No dark fade.

**Transition choreography:** glass edge becomes scanner rail; rail follows metadata chip; chip turns into optical lens frame; pixel surface becomes text/Unicode ruler; lens travels to comparison machine; removed tag becomes inspector ticket; official station rails become result-drawers; drawer becomes checklist. Use actual object continuity, match movement direction and light. One main move per scene and one secondary detail. Don't rotate the full frame randomly. The animated background plate stays stable to prevent the “AI edit” feeling.

**Shot rhythm:** intro 0–3s strongly visual, explanatory scenes ~3–6s, high-effort reveal on metadata vs watermark, mid-video “removal not universal” twist, and payoff with official checker tools. Use meaningful holds between high motion peaks (0.2–0.45s). Timestamps come from actual audio alignment, never forced to rough table seconds.

## Technical implementation — HyperFrames / GSAP / Three.js / local tools

1. Inspect installed local toolchain and help output: `npx hyperframes --help`, `init --help`, `render --help`, `transcribe --help`, `snapshot --help`; also check ffmpeg and local 3D model workflows. Use exact installed CLI syntax. If HyperFrames unavailable, choose a compatible local deterministic video workflow, explain the deviation and preserve editability.
2. Root composition: 1080x1920 background plate, persistent genuine logo + masked light sweep, independent 3D mascot/workbench renderer, captions/keyword highlight renderer, **exactly one** VO track. Avoid creating scene-specific duplicate logo tracks. Use sub-compositions per scene with unique IDs and local timelines. Never copy `source.mp4` into final media track.
3. GSAP timelines must be paused/seekable and registered as the actual HyperFrames adapter expects. Use deterministic initial states and absolute timeline positions. No `Math.random`, timers, wall clocks, uncontrolled `requestAnimationFrame`, infinite repeat or independent browser autoplay. All micro gestures and logo sweeps repeat **finite cycles** based on video duration.
4. If the local project template demands `tl.set` before tweens and bans `gsap.from`, honor the installed project contract and use `tl.fromTo(..., immediateRender:false)` or `tl.to` with explicit initial states. Never animate CSS/GSAP transforms concurrently on the same DOM node. No layout-position tweens, clip overlap bugs or timeline reinitialization on seek.
5. 3D integration: if real mascot GLB, animate via skeletal clips/IK and absolute-time mixer seeking. Cache cloth/simulation if used; do not run nondeterministic real-time cloth simulation. If mascot was previously built from Three.js meshes, repair mesh construction/geometry normals and rig logic in a scoped copy. Save the revised mascot asset path and repair notes.
6. Build and freeze a visual system file `DESIGN.md` with brand palette/font/glow/lighting/safe zones so no scene drifts back to default colors.
7. Caption system: top-middle safe space; mask-in grouped words, Poppins 700 for dominant words and 400 for surrounding; for each key phrase overlay navy-gradient rounded shape plus white text, isolated shadow/glow layer. Use script/VO words, no brand claims beyond source evidence. Allow 4–8 words on screen simultaneously. Captions must be readable even during glow.
8. Sound-to-action: transcribe recorded Indonesian VO locally with multilingual model and manual check for brand/product names. Align visual apex to spoken onset within 2 frames when possible. Do not stretch VO to make it fit the storyboard. Final runtime = actual audio tail + 0.3s still end frame.

## Absolutely required QA and iteration

**Gate 1 — mascot before scenes:** produce `_qa/mascot_front.png`, `_qa/mascot_side.png`, `_qa/mascot_3quarter.png`, 3 pose tests and a 3–5s **continuous animated test** (not just static image). Inspect lapels, cuffs, jacket front, shadow grounding, eyes and hand collisions, jerky velocities. User's specific feedback is stiffness and ragged jacket. Fix root causes in copy of source file. Provide `CHARACTER_REPAIR_REPORT.md` with issue→repair→visual proof. If unsolved, explicitly block perfection claim and ask direction.

**Gate 2 — style frames:** produce actual 1080x1920 images for intro, two-layer split, “metadata removed ≠ watermark removed,” and final logo/maskot. Evaluate Poppins, source background fit, highlight glow strength and genuine logo alpha edges. If it looks cheap, iterate at least twice.

**Gate 3 — full draft:** render draft assembled preview with new VO and no BGM. Run HyperFrames lint/validate/inspect (or installed equivalents), contact sheet each scene midpoint + exact transition boundaries. Inspect for caption crowding, contrast, clip leaks, logo visibility, mascot motion quality. Fix every real issue, don't suppress warnings without written reason. Re-seek at timestamps in different orders; compare screenshots to verify determinism.

**Gate 4 — approval:** deliver draft MP4 and before/after mascot repair images to user, **STOP for approval**. Do not render expensive final deliverable or publish externally before user approves.

**Gate 5 — final after approval:** H.264 MP4 1080x1920 30fps AAC, metadata verified with ffprobe; no blank frames, no audio tail cutoff, no stretched background, no missing textures, no nonconforming font, no false completed checks. Inspect actual exported MP4 first/middle/last and each scene transition. Report only evidence-backed PASS/PASS WITH WARNINGS/BLOCKED.

## Your first response and actions

Confirm: found actual mascot asset path and type; found VO audio and its measured length (or missing); located assets/logo; installed render tools. Then **start action**, not another high-level plan: repair/test character and generate style frames. Show evidence and continue to full preview without unrelated questions. Ask the user only for a true blocker such as inaccessible mascot model, missing VO for sync, or approval for substantial 3D remeshing.

**North Star:** human-directed premium motion studio, not AI-slop. Every 3D action teaches a fact; every transition hands off a real object; the mascot is expressive but restrained; the jacket is genuinely tailored and bug-free in tested poses; the logo visibly participates without stealing attention. Quality verification beats verbal assurances.
