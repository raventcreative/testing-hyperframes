# 07 — DIMENSIONAL MOTION TECHNIQUES & VISUAL QA V3.0

> V3.0: §11 adds the REF-H gates (default). The techniques in §1–10 remain valid; the default style choice is REF-H (doc 11), not a free A/B/C pick.
## Practical playbook to prevent flat, generic HyperFrames motion

**Applies to:** new motion-design/explainer/Reels where the user wants a high-end 2.5D/3D, glass, volumetric, physically staged or premium aesthetic. This is a **look-development and testing specification**, not proof that these methods were used in the three source videos.

**Provenance:** the visual motifs come from the three user-supplied MP4s described in `06_PREMIUM_MOTION_STYLE_DNA.md`. Engineering approaches here are informed by the public HyperFrames documentation and must be checked against actual **installed** skills and CLI before implementation. No guarantee that a requested 3D/shader feature is supported by the user's renderer until tested.

## 1. STYLE SELECTION: one hero visual language, not an effect soup

| Choice | Visual priority | Use when | Avoid |
|---|---|---|---|
| `A / editorial-kinetic` | clear hierarchy; impactful titles + staged UI + selection highlights | short tutorials, fast digital explanations, energetic hooks | static word wallpaper, endless fade-and-rise headlines |
| `B / cinematic-object-depth` | tactile object / metaphor, contact shadow, angled surfaces, spotlight, controlled physical action | premium product/storytelling, persuasion, invisible concepts needing a visual object | decorative gold on everything, arbitrarily floating meshes |
| `C / clean-3D-explainer` | volumetric mascot + clean UI/feature-card arrangement; generous white/negative space | product explainers, comparisons, educational software and brand characters | oversized mascot blocking copy, excessive card bounce |

For a mixed video, choose one primary and up to one secondary. Pick **specific observed motifs** from `06` with source timecodes. Do not copy a creator's original artwork, palette/brand, layout verbatim, text, logos, voices or scenes. A new brand brief may override the palette entirely.

## 2. SCENE LOOKDEV CARD (MANDATORY FOR EVERY HERO SHOT)

Before writing code, fill this per important shot:

```text
scene_id / absolute in-out:
role and meaning:
selected DNA and source motif/timecodes:
visual subject and single focal action:
background / midground / foreground / text planes:
hero object geometry or image-source type:
material family and edge behavior:
light direction, softness, motivated source:
contact/cast shadow: where attached and how it moves:
camera viewpoint / movement / parallax logic:
entry / anticipation / action apex / settle / hold / exit timings:
VO/SFX cue that drives the hero action:
visibility and occlusion handoff:
mobile-safe copy placement:
technique and render fallback:
evidence frames to inspect:
```

An empty `material`, `shadow`, `depth`, `camera` or `handoff` field is a **planning defect** for a hero 3D shot. These parameters can be 'not used intentionally' with an explanation; they must not be left to generic defaults.

## 3. DEPTH: MAKE THE PIXELS PROVE IT

A card with rounded corners and one drop shadow is still largely 2D. For any scene declared **hero 3D / dimensional**, design at least **three complementary visible cues**, chosen according to story:

1. **Perspective/geometry:** visible side/bevel/thickness, receding edges, credible rotation in X/Y or a true modeled object. Keep text close to camera-facing planes for legibility.
2. **Occlusion/order:** a foreground object crosses in front of a midground object; depth order changes cleanly during motion.
3. **Anchoring:** cast/contact shadow maps the hero to a plane, or a credible hanging/floating rationale exists. Shadow must correspond to object's location, scale and lamp direction.
4. **Light/material:** highlights follow the implied shape; consistent key/fill/rim. Metal vs matte vs glass look distinct.
5. **Parallax:** near object travels more across screen than distant environment during a dolly/orbit; do not simply move entire composition together.
6. **Depth-scaled transition:** a staged object rises toward camera, rotates into position or reveals nested elements through an aperture/hinge instead of appearing by opacity alone.

Do not add depth cues that contradict each other (shadow below right, rim indicating light below left, perspective that reverses during the same fixed-camera shot).

### Implementation choice

- **HTML/CSS + GSAP (2.5D):** interface panels, browser mockups, cards, layered typography, simulated bevels, CSS `perspective`, `rotateX/Y`, `translateZ`, shadows and camera-group transforms. Confirm actual behavior of nested `transform-style`, clipping, filters, alpha and font rasterization in captured frames. CSS 3D is not the same as physically lit 3D.
- **SVG + GSAP:** schematic diagrams, reveal masks, line tracking, simple mechanical dials, chart paths and controlled vector layering. Can provide excellent depth *illustration* with gradients and shadows without true meshes.
- **Three.js/WebGL:** true geometric props, physically staged surfaces, 3D cameras, lights, occluding meshes and material properties. Read the installed `hyperframes-animation` Three.js adapter. Use HyperFrames `hf-seek`/published time as the single render-time clock; explicit composition duration. Preload assets before critical seeking.
- **TypeGPU/WebGPU/shader:** specialized liquid-glass, particles, volumetric-looking lighting only if genuinely needed and tested with current capture/runtime. Provide a graceful fallback; do not claim native shader support just because it runs in a personal browser.
- **Pre-rendered assets:** permitted where sourced/created legally and honestly documented. Can look high-end but may not support independent movement or camera changes; use limited parallax to avoid a cardboard cutout appearance.

Always inspect current official local docs for syntax and seek contract. Don't import React/Remotion by default.

## 4. GLASS / FROSTED INTERFACE MATERIAL

**Target outcome:** a panel appears made of a translucent, luminous material with readable content and actual background separation, not a low-opacity white rectangle.

Useful ingredients (select, do not pile all on):
- **Tint/transmission illusion:** controlled translucent fill that slightly reveals or modulates the background. On a bright background, a dark or colored frosted plate may read better than plain white.
- **Edge/rim:** a thin brighter top/side highlight, restrained specular stroke, and optional second darker edge that suggests thickness. Highlights obey the implied light direction.
- **Separation:** soft medium-width cast shadow and a small near-contact shadow, not a giant gray aura or uniformly glowing border.
- **Background response:** `backdrop-filter` frost/blur only if validated in render; a precomposed backdrop/material texture is acceptable if browser blur behaves inconsistently.
- **Controlled movement:** a slight camera-relative tilt or changing glint can make the glass feel tangible. Tiny elements and main copy must not undergo severe perspective distortion.
- **Text contrast:** readable dark/bright labels with quiet backing; no translucent paragraph over busy moving imagery.

**Naming honesty:** CSS blur/tint/gradient is simulated glass, not physically accurate refraction. Do not promise true lensing unless a working shader/refraction path is implemented and reviewed.

**Glass QA:** capture at entry midpoint, hero frame, tilt apex and exit. Panel must remain recognizable; edges do not vanish; no z-fighting/aliasing; text is legible; no hard rectangular backdrop-filter cutoff; color/light matches environment; blur doesn't swallow the reference content.

## 5. LIGHTING AND SHADOWS

For each dimensional scene, choose a motivated light source. On a dark world, use restrained key with soft falloff and one accent rim/spot when appropriate. On a white product stage, use a broad soft key and subtle ambient bounce rather than hard black shadows.

**Shadow ladder:**
- contact shadow at closest approach, darker/tighter,
- cast shadow softens with distance from the support plane,
- ambient occlusion in creases and intersections when achievable,
- avoid identical shadows for objects at different heights.

As a card rises along Z, its cast shadow should normally become broader/softer and its contact relation change. A dial/box actually resting on a stage should not cast a detached shadow. Shadow direction must agree with highlights and the camera world. Transparent material shadows are more subtle than opaque metal/clay. Keep the background stage uncluttered so the lighting reads.

## 6. MOTION CHOREOGRAPHY: ACTION, NOT PRESET TRANSITIONS

A premium action has a readable causal chain:

`prepare/anticipation → meaningful change → peak/contact → settle → readable hold → intentional handoff`

**Suggested rhythmic heuristics (not rigid requirements):**
- micro-selection/highlight: around 0.2–0.5 s; align the selected term with VO,
- meaningful UI/card entry: around 0.35–0.8 s with spatial origin and braking,
- mechanical reveal/object transformation: often 0.5–1.2 s plus a hold,
- camera dolly/orbit: slower than small UI tweens; preserve subject readability,
- text should hold sufficiently for actual reading, not merely appear for 2 frames.

Use varied eases, e.g. `power2.out` or `power3.out` for focused entrances; `power2.inOut` for deliberate camera moves. Physical overshoot/elastic settle is selective, low-amplitude and motivated by mass; don't bounce every title and card. This is creative guidance, not a claim about the original video easing curves.

### Example choreography — a glass integration card (illustration, NOT locked video copy)

For a hypothetical 3-second beat (scene-local times), a UI card might start behind a foreground object and then come into focus:

| Local time | Motion stage | Visible depth evidence |
|---|---|---|
| 0.00–0.35 | Back plane and stage appear; edge light establishes camera angle | clear three-plane space |
| 0.35–0.90 | glass card comes forward along Z, slight Y rotation, decelerates; shadow responds | scale/perspective + cast shadow + edge highlight |
| 0.90–1.35 | callout becomes readable; selection moves to one field | causality tied to narration |
| 1.35–2.45 | hold; restrained specular/secondary action or still intentional hero moment | preserve readability; no purposeless floating |
| 2.45–3.00 | hero frame transforms into next shot's background via matching edge/anchor | clean continuity; no hard pop |

Never copy that template into every scene. A minimalist hard cut often communicates better than another morph.

## 7. CHARACTER AND PRODUCT AUTHENTICITY

- **One flat PNG:** may be translated, scaled, rotated, layered as a whole. Do **not** claim its elbows/eyes/legs are independently rigged. Extra pose assets require permission and consistency verification.
- **Layered art / sprites / rig:** analyze what is actually separable; animate believable pivot hierarchy; align gestures to scene objects and narration. Follow `05_CHARACTER_MOTION_REFERENCE.md` for per-pose planning.
- **Real object/brand:** never replace logos, product shape or faces to make an effect easier; don't hide mandatory printed details behind highlights or perspective distortions.
- **Reference creator's mascot:** inspiration for volumetric shading/scene staging only, not a source character to reuse.

## 8. HYPERFRAMES BUILD CONTRACT (PROMPT MUST INCLUDE)

1. Inspect available router (`/hyperframes:hyperframes` or `/hyperframes`) and installed HyperFrames version. Read `hyperframes-core`, `hyperframes-animation`, relevant adapters, `hyperframes-cli`, media-use, and schema. Use `npx hyperframes --help` / command `--help` for real flags.
2. Create a **new** Windows-compatible folder; verify real assets and rights; choose composition structure. Search local catalog/registry for useful primitives before reimplementing, but adapt them to original brief.
3. Implement seek-safe animation: root composition ID/width/height/duration, timed clips, exact text, correct layering and stacking context. Register one fully constructed finite paused GSAP timeline to exact composition ID as required by installed contract.
4. For Three.js, drive object transforms, camera and renderer deterministically from HyperFrames time (`hf-seek` and installed adapter contract). Avoid wall-clock, independent RAF loop, unseeded random, arbitrary `setTimeout`, manual video playback changes, or network fetch at seek time.
5. Use **`npx hyperframes lint` during iteration**. Before final preview use **`npx hyperframes check --snapshots`**, and suitable `*.motion.json` sidecar with supported assertions. If CLI supports `--at` or `--at-transitions`, check meaningful scene midpoints, not only one beginning/end screenshot.
6. Inspect actual snapshots including 3D tilt midpoints and transitions; check whether glass/lighting/shadows are visible as designed. Review full preview at mobile size.
7. Respect the official **final preview → user render approval checkpoint**; do not treat already approved storyboard as approval of the completed video. Only then render as CLI/skill permits.
8. Verify actual exported MP4: file present/nonempty, 1080×1920, ~30fps, expected runtime, correct audio tracks, representative critical frames (incl. in-between) and complete VO/CTA. If failure: repair → recheck → re-render → reinspect.

Public documentation snapshot checked on 21 October 2026: HyperFrames official repo `https://github.com/heygen-com/hyperframes`, `skills/hyperframes-core/`, `skills/hyperframes-animation/adapters/gsap.md`, `skills/hyperframes-animation/adapters/three.md`, `skills/hyperframes-cli/`. **Installed version overrides this document.**

## 9. VISUAL QUALITY GATES: WHAT COUNTS AS PREMIUM

Automated lint/check PASS is necessary but **not enough**. Judge the exported frames by the user's reference intent:

| Gate | PASS evidence | FAIL / rework signal |
|---|---|---|
| Reference-inspired art direction | clear selected A/B/C motifs/timecodes transformed to user's story | arbitrary 'premium' adjective with no motif |
| Focal depth | in hero 3D shot, ≥3 complementary depth cues are visible | only a 2D card plus shadow called '3D' |
| Materials | glass/metal/clay visibly distinct where chosen, highlights and edge finishes convincing | flat gradients claimed as photorealistic glass |
| Lighting | motivated key/fill/rim or intentional flat editorial lighting | mixed contradictory shadow directions |
| Anchoring | plausible contact/cast shadow tracks movement | cards/objects float without stage logic |
| Camera + parallax | viewpoint makes sense; depth planes behave consistently | everything moves at same rate while named 'dolly' |
| Motion polish | meaningful anticipation, apex, settle, hold and handoff | repetitive fade-rise/zoom on every beat |
| Mid-tween integrity | no z-flips, pops, clipping, missing surfaces at intermediate times | final still looks good but movement is broken |
| Mobile clarity | hero/copy readable at small size throughout scene; IG UI-safe | glass blur obscures headline or text crosses rail |
| Honesty | report verified file, steps, known limitations | self-awarded PASS without watching/export checks |

**Rework trigger:** if the user specifically requested 3D/material-rich premium motion and the core hero shots still look like a generic flat text slideshow, consider **a visual-direction failure** even if command-line checks are green. Selective aesthetic review is needed: compare corresponding *motifs*, not exact third-party screenshots.

## 10. CLAUDE EXECUTION INSERT (COPY INTO EACH FINAL VIDEO PROMPT)

Do not assume Claude Code sees this ChatGPT file. Insert the following instruction as needed **alongside complete per-beat details**:

> **PREMIUM DIMENSIONAL LOOKDEV LOCK:** Choose one primary reference DNA (A editorial / B cinematic physical / C clean volumetric) and at most one supporting DNA, based on the locked brief. For each 3D hero beat specify BG/MG/FG/text planes, lighting direction, hero material/edge finish, credible contact/cast shadow, perspective/occlusion and camera-parallax mechanism. Implement using supported HyperFrames-native techniques, picking GSAP+CSS/SVG for 2.5D interfaces and Three.js/hf-seek for true modeled geometry when needed. Never substitute generic fade+rise text and single-shadow flat cards for an explicitly dimensional scene. Glass must show controlled tint, believable edge highlight and separable background, not opacity alone. Storyboard entry/anticipation/action apex/settle/hold/exit and overlap at precise times. Produce lookdev snapshots at critical in-between frames, check deterministic seeking with documented motion assertions, review actual output and mark the visual gate FAIL if it still looks flat, cheap, repetitive, clipped or visually incoherent. Follow the official preview approval gate before final rendering, and report only verified outcomes.


## 11. REF-H HOUSE STYLE GATES (V3.0 — mandatory for the default look)

| Gate | PASS | FAIL / rework |
|---|---|---|
| Text economy | only the top caption (46 px) + spoken words drawn inside objects | headlines, text cards, bottom subtitle boxes |
| Scene rhythm | one scene per spoken phrase, 0.8–5.5 s, hard cuts | long static scenes, slideshow fades |
| Hero | one big metaphor object, 60–75 % of the visual zone, readable at phone size | small icons, several equal-weight objects |
| Detail density | 20–60 crafted elements (bevels, screws, ticks, notes, UI lines) | flat shapes + one drop shadow |
| Light & shadow | upper-left key, inner top highlights, contact shadow under every object | floating objects, contradictory shadows |
| Depth | far blurred plane + hero + near particles, push-in + parallax | everything on one plane moving together |
| Sync | the key action/apex lands on the word (±0.05 s) | effects drifting from the VO |
| Frame 0 | the hero already visible and moving on the cut | empty first frames |
| Palette | ice/ivory/navy (+ small mint/amber) | red, neon, dark full screens |
| Ending | still brand lockup with the genuine logo, no fade | fade to black, cropped/recoloured logo |
| Consistency | contact sheet reads like the same series as `golden_frames/` | a mix of unrelated looks |
| Engineering | lint 0 errors · check 0 errors · seek determinism 0 px · MP4 verified | self-declared PASS without evidence |

**Execution insert (REF-H):** paste the HOUSE STYLE LOCK + SCENE CONTRACT blocks from `02_MASTER_PROMPT_CLAUDE_CODE_V3.md` into every Claude prompt.
