# 05 — CHARACTER MOTION REFERENCE

> Project: **HyperFrame Prompt**  
> Purpose: reusable motion-direction source for future HyperFrames Instagram Reels featuring animated characters.  
> Reference ID: `CHAR-MOTION-001`  
> Reference URL: https://www.instagram.com/reel/DeRPpHaCMV1/  
> Creator/account: `@classai_id` (confirmed from the Instagram page text)  
> Source verification status (19 October 2026): **LINK AND POST TEXT VERIFIED; VIDEO FRAMES / CHARACTER MOTION NOT YET VISUALLY VERIFIED.**  
> Important: None of the specific motion-design recommendations below should be misrepresented as a frame-by-frame observation of the Instagram Reel. The original video or a screen recording is needed to lock that precise animation style.

## 1. Where this reference applies

- Use this reference as a **preferred direction for character movement and performance** in character-based explainers, AI/technology Reels, illustrations and mixed-media videos **when the user does not provide a more specific motion reference**.
- This is a **motion-only** reference. Do not automatically copy the source creator's character identity, art style, colors, typography, logos, storyline, music, voice, composition or assets.
- Do not force character animation into a project that should instead use product footage, interface demos, documentary footage, typographic motion or another explicit style.
- A newer, video-specific user reference or locked storyboard takes precedence. The user's actual character asset and identity preservation rules always take precedence.

## 2. Reference-inspection gate (mandatory before claiming a style match)

The exact animation from `CHAR-MOTION-001` is **pending visual analysis**. Before a production prompt claims to match the reference:

1. Inspect the playable source video, ideally a user-provided MP4 or screen recording. A caption, static thumbnail or the Instagram URL alone is **not evidence of motion**.
2. Review several time-separated frames and continuous passages, including the beginning, middle and end of character actions.
3. Extract a motion profile with concrete evidence: actual pose changes, silhouette, gestures, pivot points, ease-in/out behavior, hold durations, looping/idle behavior, scene interaction, movement intensity, entrances/exits, camera coupling and possible mouth/eye expressions.
4. Record observed versus inferred properties separately. If something is not clearly visible, label it `unverified` rather than guessing.
5. Update **Section 3** with verified observations and timecodes. Until then, use **Section 4** only as a provisional quality baseline, **not** as a source-accurate style recipe.
6. If Claude Code cannot access the Instagram media locally, supply this analysis as prose and provide only legitimately obtainable/user-provided media; never assume an external link will become an importable video asset.

## 3. Verified reference motion profile — TO BE COMPLETED AFTER VIDEO REVIEW

| Criterion | Reference observation | Evidence/timecode |
|---|---|---|
| Character type / illustration treatment | Unverified | MP4 needed |
| Actual character gestures/actions | Unverified | MP4 needed |
| Full-body / upper-body / facial movement | Unverified | MP4 needed |
| Motion cadence and gesture frequency | Unverified | MP4 needed |
| Easing and settling / secondary motion | Unverified | MP4 needed |
| Character–text or character–object interaction | Unverified | MP4 needed |
| Idle holds and transitions | Unverified | MP4 needed |
| Camera movement relative to the character | Unverified | MP4 needed |
| Limits or distinguishing traits | Unverified | MP4 needed |

**Locking rule:** Replace `Unverified` with concise, witnessed descriptions and exact or approximate source timecodes only after reviewing the moving images. This profile becomes authoritative for the *motion language*, subject to current brief and asset feasibility.

## 4. PROVISIONAL character-motion quality baseline (creative guidance, not observed reference data)

Use these as sensible interim choices for a premium Reels explainer featuring a character:

- **Character performs, not just floats.** Tie each action to a verb or narrative cue: looks, notices, points, reacts, presents, compares, enters, exits, or acknowledges. Do not endlessly move an illustration up/down/scale in place as a substitute for acting.
- **Clear pose-to-pose storytelling.** Design a readable starting pose, anticipated action, main gesture, brief settle, and stable readable end pose. Keep the silhouette understandable on a phone.
- **A living hold, not restless motion.** On longer holds, use restrained natural secondary motion *if the supplied asset supports it*. A deliberate still pose is preferable to arbitrary perpetual bobbing.
- **Gestures support emphasis.** Sync the main gesture peak to the corresponding spoken phrase, visual reveal, or reaction. Let the key graphic/text be readable during the action.
- **Hierarchy of movement.** When the source asset is legitimately riggable, primary action may involve body/arm/head changes, with smaller delayed secondary response. Avoid independent limb movement that violates anatomy or a stylized character's design.
- **Spacing and anticipation.** Use controlled acceleration, deceleration, overshoot/settle only when appropriate; avoid mechanical linear motion throughout or repeated excessive bounce, squash, spin or rubbery movement.
- **Shot-to-shot continuity.** Preserve the character's identity, scale and pose logic across adjacent beats; use purposeful repositioning rather than teleporting unintentionally.
- **Avoid stock-template repetition.** Vary meaningful actions with story context rather than repeating the same wave, zoom, entrance and exit every scene.
- **Narrative-first.** If a scene needs a clear product/demo shot, reduce character motion or move the character out of focus without obscuring evidence or exact copy.
- **Mobile framing.** Keep faces, pointing hands and core on-screen copy clear of Instagram UI-risk zones throughout tween motion, not only in final keyframes.

### Motion planning fields required for each character beat

Include in storyboard / execution prompt:

- **Narrative intention:** what the character communicates in this beat.
- **Start pose & screen location:** silhouette, eye/face direction, left/middle/right screen zone.
- **Primary action:** exact movement and pivot/anchor, plus what event triggers it.
- **Timing:** absolute beat start/end; animation entry, anticipation, action peak, settle, hold and exit; any overlap with captions.
- **Secondary action:** only if visually justified and supported by assets.
- **Interaction:** relationship with a visible text callout, card, icon, UI or object.
- **Exit/handoff pose:** precisely where/how the character is at the handoff.
- **Required rig/layers:** which independently moving character pieces or pose variants actually exist.

## 5. Asset feasibility (do not pretend a flattened PNG is a rig)

- If the user provides **one flat JPG/PNG** of a character, the implementation can reliably move the whole image (position/scale/rotation) and apply limited justified effects, but it **cannot produce truthful independent elbow/knee/hand articulation** without usable separate layers, additional poses, a proper rig or explicitly authorized generative editing.
- If the user provides **layered PSD/PNG/SVG parts, rigged model, spritesheet, pose variants or animation footage**, inspect the actual contents and build within their supported degrees of freedom.
- Do not redraw/reimagine the user's face, mascot, clothing details, logos or signature appearance merely to achieve an impossible motion. If additional assets are essential, request the missing source or explicitly mark the limitation.
- If visual poses can be created with permission, require character consistency and verify each resulting pose before animation. Don't hallucinate file paths or claim media is already created.
- Use HyperFrames-compliant HTML/CSS/JS and seek-safe, deterministic GSAP or other supported local approach. Clip timing and media seeking belong to the framework.

## 6. Prompt insertion rule for ChatGPT → Claude Code

For a future character-based Reel, insert a specific paragraph under `[VISUAL/MOTION]`:

> Character motion reference: `CHAR-MOTION-001` (https://www.instagram.com/reel/DeRPpHaCMV1/). It is a preferred reference for **character performance and motion only**, not for copying the creator's art/branding. If the verified motion profile in `05_CHARACTER_MOTION_REFERENCE.md` is available, implement that profile within the locked scene brief and the provided rig/assets. If motion details remain unverified or the source video is inaccessible, use the clearly labeled provisional baseline and do not claim exact style-matching. For each beat, specify start pose, action cue, joint/whole-layer mechanism, gesture apex, settling, hold, end pose and transition. Never fake independent limb articulation from a single flattened image.

Also include relevant pose/motion tests in `[BUILD + QA + RENDER]` and F. QA.

## 7. Character-animation QA checklist

A character-motion implementation **fails QA** if any blocking issue occurs:

1. Wrong user-supplied character identity or modified brand/face without approval.
2. Unintended stiff cutout motion when the story requires character acting and the needed assets were available.
3. Broken elbow/knee pivots, detached components, impossible gestures or clipping/cropping mid-tween.
4. Gesture/action happens after or before the point it should illustrate, harming comprehension.
5. Pop/jump/discontinuity at scene boundaries that was not deliberately storyboarded.
6. Repetitive auto-bounce/float applied to the character for the entire video without narrative reason.
7. Scene/keyframe seeks produce inconsistent poses, positions or visibility.
8. Character obscures required exact copy, product proof or Instagram-safe reading area.
9. Claims of exact resemblance to `CHAR-MOTION-001` without inspecting actual motion footage.

## 8. Project precedence and future updating

- This file is a **Project source/reference**, not a required design template for every Reel.
- It complements `02_MASTER_PROMPT_CLAUDE_CODE_V3.md` (motion contract and QA), `03_EXTENDED_PROJECT_RULES_REFERENCE_V3.md` (creative system), and `04_EXAMPLE_REELS_EXECUTION_PROMPT.md` (example only).
- When a user supplies a new video or requests a revised character-motion style, adapt it for that video; do not silently overwrite this library's reference interpretation.
- After the original source clip has been visually reviewed, update Section 3 and optionally add a short verified motion grammar, observed timecodes and source-frame contact sheet. Keep explicit provenance; do not embed or redistribute the original Reel without rights.
