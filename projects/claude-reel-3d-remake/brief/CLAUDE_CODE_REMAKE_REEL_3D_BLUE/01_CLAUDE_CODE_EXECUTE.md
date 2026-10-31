# COPY ALL TEXT BELOW INTO CLAUDE CODE

You are my **senior motion design director, technical animator, 3D character TD, creative editor, and final QA engineer**. Produce a working video remake using the files in this extracted brief folder. The goal is a highly polished, editorially creative and cinematic vertical tutorial. **Do not merely generate a new prompt; inspect this repository, implement the video in its existing supported video stack, and show an assembled preview.** Do not render/export the final MP4 until I approve the full preview.

## Priority and integrity

1. This instruction is the user's **current explicit brief**. If any older project style document mandates light-ivory backgrounds, Montserrat, forbids mascots, or forbids cyan, the **current user instructions override that older house style** for this video only.
2. Preserve the **actual existing 3D mascot and actual existing logo in my Claude Code project**. They are ALREADY there. Find their real paths; do not invent names/paths, generate lookalikes, or use the 2D human mascot from the reference video.
3. Reference MP4: locate `assets/reference/reference_original.mp4` inside this extracted folder. Reference background: `assets/brand/background_original.png`. Resolve absolute paths via search from current repository root; do not assume this document is at the repository root.
4. The video reference is for **scene analysis and editorial timing only**, not a source to insert unmodified or a license to copy another creator's identity. New video must use original rendered scenes, our 3D mascot and branding.
5. Do **not** overwrite unrelated user code, mascot rig, logos, past video renders, or settings. Create a unique new project/output subfolder. Do not delete or reset files.
6. No external paid API, paid renderer, unauthorized publication, credential extraction, forced package upgrades, or automatic API key use. Ask first. No fake status `PASS` without verifying the output.

## Mandatory reconnaissance before creation

Read these documents entirely, in this order:

1. `START_HERE.md`
2. `DESIGN.md`
3. `02_REFERENCE_SCENE_BREAKDOWN.md`
4. `04_VOICE_OVER_INDONESIA.md`
5. `03_PREMIUM_STORYBOARD.md`
6. `05_CHARACTER_LOGO_QA.md`
7. `06_RENDER_QA_CHECKLIST.md`

Then do the following, and give a concise evidence-backed status report:

- Inspect repository `package.json`, `CLAUDE.md`, video-related config, and available renderer. Determine whether this is HyperFrames, Remotion, Three.js with custom export, or another pipeline. **Use and respect the existing working stack**; do not start an unrelated project from scratch. If HyperFrames is installed, use its current official skills, CLI help and deterministic GSAP/Three.js contracts. If Remotion is installed instead, follow its installed version and correct frame-based architecture. Do not blindly mix both engines.
- Use `ffprobe` on the reference (known ≈61.48 s, 720×1280, 30 fps), and inspect frames at roughly 1–2 second intervals and key transitions. Read the supplied contact sheets as an overview. Verify the source analysis time windows; report any corrections.
- Inventory original mascot assets and animation data. Prove whether it is skinned/rigged 3D, procedural 3D, layered illustration, or a simple rendered still. Inventory the suit meshes/materials and identify exactly where the present jacket clipping/deformation bugs come from.
- Inventory the genuine logo's file. Report aspect and alpha handling. Do not redraw or replace its lettering.
- Confirm availability of Poppins Regular (400) and Bold (700), voiceover asset (likely absent until I record it), and any official brand assets.
- Check how to make export deterministic at **arbitrary time seeking**. Never depend on non-deterministic animation wall-clock loops, uncontrolled `requestAnimationFrame`, `Math.random()` without seed, arbitrary timers or negative frame ranges.
- Show a specific list of missing assets/capabilities before claiming success. If the 3D rig source is missing or cannot be fixed, ask for it; offer an honest fallback preview but don't fake corrected jacket motion.

## Project objective

Remake the attached English tutorial about producing animated Reels via Claude Code into a better **Bahasa Indonesia** video with clear story progression:

**spectacular finished animation hook → show 6-step workflow → reveal practical setup → one-line idea becomes storyboard → show camera/VO/transitions → emphasize the overlooked final revision → visible quality improvement → final result + CTA.**

Target audience: Indonesian AI creators, content editors, people curious about Claude Code. The subject is how the workflow **can help** create animated reels—not a promise that every install automatically renders a finished video with no setup.

VO: Use `04_VOICE_OVER_INDONESIA.md` exactly as spoken content. I will record it separately. Place the user's genuine VO track once, beginning at 0, with no duplication or artificial TTS. Until the VO exists, build a marked **timing-preview draft** based on ~72 seconds, then replace its approximate boundaries using actual audio transcription/alignment. **Final scene times and word-highlight beats must align to verified VO**, not the source English audio.

CTA keyword: `ANIMASI`. The audience fulfillment template is in `07_BONUS_PROMPT_CTA.md`.

## Output format and design lock

- Portrait **1080×1920 (9:16)**, **30fps**, original reference is portrait, deliver H.264 video + AAC clean VO upon final approval. Aim ~65–75 seconds, adjusted to actual spoken VO.
- Background **must use the supplied actual PNG** `background_original.png` (1080×1350, 4:5). Preserve its original gradient, hue, saturation, design and proportions. Fit to 9:16 by native-scale centre plate plus **mirror-extended softly blended upper/lower margins** or seamless extension. **Never stretch it to 1080×1920**. Do not replace with generated gradient art. Maintain readable contrast while keeping visible recognizable gradient.
- Font **Poppins Bold 700** for key words/section headings, **Poppins Regular 400** for supportive copy. No generic fallback visually, no Montserrat or Inter unless a local asset is missing and this is explicitly flagged, and no accidental font substitution on render.
- Main on-screen text **white `#FFFFFF`**; key words/active outline/CTA emphasis **cyan `#00D0FE`**. Use just 1–3 emphasized words per phrase, not entire sentences in cyan.
- Place text in physically layered **dark navy gradient plates**, not raw text directly over bright blue gradient. Suggested `linear-gradient(135deg,rgba(10,13,44,.95),rgba(41,75,119,.92))`; rounded rectangle 16–28px, 1.5px faint cyan rim, upper-left white inner bevel, softly grounded shadow. All labels crisp in 1080×1920.
- Cyan word glow only at impact: max `0 0 14px rgba(0,208,254,.35)` on text and a short travelling underline/sheen. **No constant glow, excessive lens flares, big bloom halos, random sparks, glitch spam, blue RGB streak wall, or cartoonish bounce**.
- Genuine logo always upper-left, away from top caption and Instagram UI. Keep exact geometry and colors, aspect ratio and original image. Animate with recurring restrained light sweep clipped to its actual shape, plus rare subtle scale pulse; glow behind rather than repainting logo. See exact contract in `05_CHARACTER_LOGO_QA.md`.
- Existing mascot 3D: realistic shading within stylized brand aesthetic; smooth shoulders/neck/arm motion, breathing, grounded feet, eye-line, intentional gestures, fabric/body secondary animation. **Jacket must be clean**: aligned lapels, collar, cuffs, sleeves, buttons; no penetration, flicker, UV stretch or unweighted meshes, especially during motion. See `05_CHARACTER_LOGO_QA.md`.
- Main reading zone: logo x 60–240, y 95–190; hero heading begins around y 245–385, central visual y 400–1480; keep bottom 250px clear of critical content because social UI overlays. Reflow intelligently as scene composition demands.
- Do not just keep a near-static mascot stuck at the bottom throughout: use it for **narrative actions** in approximately half the scenes; in other scenes let strong dimensional prop/UI visuals lead.

## Required scene plan

Use **ALL 18 shot blocks** from `03_PREMIUM_STORYBOARD.md` as the *director's starting blueprint*. Each has scene intention, provisional time, corresponding VO phrase, visible hero, layout, camera, character action, animated keyword and exact transition handoff. The plan exists to improve reference fidelity and guide implementation; adjust scene borders only with a logged VO-alignment justification.

Implement a **time-driven motion grammar**:

1. **Anticipation**: 0.08–0.18 s before meaningful action (only where physical).
2. **Action**: object transforms, prop opens, camera turns with parallax, UI state changes, body gesture happens.
3. **Word-synced apex**: key effect lands on the spoken trigger (target ±0.08 s after actual VO alignment).
4. **Follow-through/settle**: no sliding feet, no robot freeze, no badly eased puppet motion.
5. **Readable hold**: allow titles/UI 0.6–1.2 seconds of genuine reading time as appropriate.
6. **Physical handoff transition**: a meaningful existing line, folder tab, cursor, playhead, card edge, camera arc or filmstrip **becomes** the next scene element. Each major cut must have a reason.

### Transition requirements

- Follow the **17 transitions** in the chart of `03_PREMIUM_STORYBOARD.md`; target handoffs 0.25–0.45 s, with some sharp rhythmic editorial cuts when supported by meaningful edge movement. Do not use a single generic preset between every scene.
- The source video is mostly UI card entrances/cuts/selection highlights; your remake should achieve a more expensive sense of continuity via object-origin matching, real perspective change, occlusion, motion-vector continuity, motivated light and contact shadows.
- Transition must preserve live content until it is truly covered/replaced. No black gap, frozen intermediate frame, offscreen pop, white flash on dark background, or duplicated/ghost limbs across clips.
- Avoid 360° spins, random optical-flow warping, unreadable 3D type rotation, cheap particle storms, 100% blur, and constant zooming.
- Reuse the same camera/lighting world across transitions when the prop represents the same object, so the story feels continuous.

### Logo motion spec

An upper-left permanent identity cue: actual logo, clipping mask over its alpha, white-to-cyan narrow sheen traversing left-right at irregular but **deterministic** moments every approximately 4–7s, ~0.5s per pass; low-opacity bloom behind. At `SATU KALIMAT`, `06`, and `ANIMASI`, allow one 3% scale pulse. Never obscure logo, change its shape or set it spinning. End with a fully visible, settled logo (0.8–1s lockup).

### Mascot movement and jacket debug gate

Before assembling the 18 shots, make a 4–6 second **character lookdev preview** containing the three hardest movements: look/point to interface, folder tap, CTA palm-open gesture, plus a 3/4 jacket turn. Inspect 0/25/50/75/100% frames of each move. Fix clipping and rig/source-level defects before integrating all scenes. If missing proper rig, stop and present the actual blocker instead of fake success.

Per-character performance must have eyes/head lead the gesture, torso/shoulder follow, hand contact on objects, wrist follow-through, feet grounded, natural small breathing and restrained facial emotion. Suit weights must be consistent through whole movement and camera angles. Avoid waving every few seconds, blink-on-a-loop, random head bob or rubber limbs.

## Sound design

User's VO is the sole narrative anchor. Use only rights-clear SFX if available: short UI button ticks, paper fold, physical folder click, restrained whoosh on travel, quiet bass contact, a mild `DONE` check sound. Level SFX enough to feel tactile but never mask words. If royalty-free audio is not provided, create no unauthorized music or copyrighted sound. Original English reference track must **never** appear in final. Do not overcompress VO; avoid long silences or clipping. Optional licensed BGM can be mixed later only after user supplies/approves it.

## Implementation gates — DO NOT SKIP

**Gate 1: asset audit**: show paths and screenshots of real mascot+logo, report what supports animation and what doesn't. No guesswork.

**Gate 2: lookdev**: create 3 approved styleframes: (A) hook with brand, (B) mid-tutorial UI/mascot, (C) CTA ending. Plus 4–6s test of suit motion. Compare with user background and exact typography. If they look cheap/flat/unreadable or the suit still clips, revise before all scenes.

**Gate 3: complete build**: implement all 18 shots in the installed video framework. Use exact target specs, editable source project, voice-ready timing, scene graph + camera and deterministic animation. No unrenderable placeholders on final composition.

**Gate 4: structured QA**: read `06_RENDER_QA_CHECKLIST.md`. Render/inspect snapshots of scene apex, every transition midpoint, suit angles and important in-between frames; compare with reference motifs but do not copy third-party branding. Run installed official lint/check/inspect commands (discover current syntax first). Capture the exact results and resolve failures.

**Gate 5: assembled preview for Freddie**: provide a browser-playable preview or a watermarked, clearly labeled draft. If no VO was supplied, say `VO BELUM ADA — TIMING BELUM FINAL`. **STOP and ask for visual approval**. Do not claim final-ready based on 3 nice still images.

**Gate 6: final export only after approval and real VO**: render MP4, verify via ffprobe dimensions/fps/duration, verify audio head and tail, manually inspect sampled exported frames including suit and last CTA, and report exact file location, build status, test evidence, limitations. No invented 10/10 label.

## Expected report from you

Respond with:

1. **ASSET AUDIT:** exact verified file paths for mascot, logo, video engine, VO, background; missing dependencies.
2. **REFERENCE AUDIT:** what you observed in the 61.48s source and which transition/motion features you used. If actual observations differ from provided scene table, state corrected timecodes.
3. **DIRECTOR'S PLAN:** 18-shot breakdown with adjusted timings if voice exists; 3 styleframes and 1 suit movement preview.
4. **BUILT PREVIEW:** concrete preview path/link, not just text descriptions.
5. **QA:** clipping, animation in-between, typography, logo, timing, render status and honest blockers.
6. **APPROVAL ASK:** ask for approval to export only once assembled preview is ready.

START NOW with non-destructive asset inspection and analysis of the actual reference. Do not invent or replace existing user assets. Be ambitious in editorial choreography, realistic in technical claims, and brutally honest in QA.
