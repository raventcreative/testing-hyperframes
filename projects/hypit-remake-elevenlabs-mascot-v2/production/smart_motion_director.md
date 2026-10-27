# Smart Motion Director — AI PRENEUR effect library + auto-direction

Reusable for every new script/VO in this workspace. Built on GSAP + HyperFrames only (no new runtime
dependencies), deterministic (seek-safe, frame-accurate), tested with forward/reverse seek renders.

## Pieces
| File | Role |
|---|---|
| `vendor/motion-director.js` | effect library, `window.MD.fx.<effect>(ctx, opts)` |
| `tools/motion_director.py` | auto-direction: narrative intents → restrained motion plan (`production/motion_plan.json`) |
| `tools/gen_director.py` | plan → `compositions/director.html` (overlay effects) + `production/director_camera.json` (camera) |
| `tools/gen_root.py` | mounts the director layer inside `#world`; camera moves on `#world` / `#stage-dir` |
| `projects/motion-director-demo/` | 10.6 s demo with the mascot (`out/DEMO_smart-motion-director.mp4`) |

## Effect library (all 20)
Common options: `at`, `dur`, `preset` (SUBTLE / STANDARD / HIGH), `intensity`, `ease`, `dir` (L/R/U/D),
`until` (exit time), `theme` ({ink, ink2, glass, accent}), `sfx` (cue name; the root places the audio).

| Effect | Use it for | Notes |
|---|---|---|
| liquidGlass | premium tech cards | translucent body, rim, specular sweep, 3D hinge + rack focus entrance |
| frameEscape | important reveal | element lifts out of a framed card past its border (synced twin copies) |
| snapZoom | key statement | fast punch on a camera wrapper, short hold, eased release |
| zoomThroughCut | strong transition | camera accelerates through a foreground object into the next shot |
| chatTakeover | conversational beat | glass thread, messages on VO words, thread expands into the main visual |
| bRollOverlay | product / context | layered cards with depth parallax |
| cinematicOrbit | 3D object / host | controlled perspective sweep (+ the mascot camera yaw orbit) |
| dynamicHeadline | impact statement | VO words only, navy box + white text, snap with focus pull |
| growthCurve | data / growth | progressive line + area + marker, no invented numbers |
| paperCutout | collage objects | paper edge, lift shadow, hand-placed wobble |
| checklistPop | lists | rows land and tick on their VO words |
| studioReveal | openings | light sweep + vignette lifting + camera settle |
| zoomPortal | spatial transition | circular window opens on a point, ring through the cut |
| magazineCover | editorial moment | big image, masthead (VO word), rules, folio marks |
| dollyZoom | rare emphasis | background scale changes while the host keeps his size |
| phoneMockup | app demos | CSS device, real screen content, glass reflection, 3D tilt |
| frameBreak | dimensional break | frame edge shatters as the subject pushes through |
| digitalZoom | restrained reframe | slow scale + offset, auto release |
| greenScreen | compositing | light wrap + contact shadow + tiny colour match for cut-outs / the host |
| orbitReveal | logos / objects | half orbit into view, glint, settle |

## Auto-direction rules (tools/motion_director.py)
1. Phrases = VO words between punctuation; intent from an Indonesian/tech lexicon
   (reveal, workflow, conversation, product, data, list, premium, contrast, emotion, focus).
2. Intent → effect family (e.g. conversation → chatTakeover, list → checklistPop, data → growthCurve,
   emotion → dollyZoom, reveal → snapZoom / frameEscape, focus → digitalZoom).
3. Restraint: one major effect on screen at a time (occupancy), ≥ 1.4 s between majors, no identical effect twice
   in a row, ≤ 2 majors per scene, minor effects ≥ 10 s apart, busy scenes get nothing, per-scene allow-lists.
4. Every effect is anchored to a measured VO word start (CTC alignment).

## This film's plan (production/motion_plan.json)
0.00 studioReveal · 3.18 snapZoom "efek" · 6.12 orbitReveal 3D GitHub mark "GitHub" · 7.78 growthCurve
"puluhan ribu stars" · 9.36 chatTakeover "kasih … video referensi … coding agent … Claude Code" · 20.66 checklistPop
"footage, caption, B-roll, efek" · 30.98 digitalZoom "dipertahankan" · 41.26 dollyZoom "jangan" · 57.26 orbitReveal
GitHub mark "repo" · 59.34 frameBreak/escape "HYPIT" — plus greenScreen compositing and a slow cinematic orbit on the
host in every presenter shot.

## Limits
- Liquid glass is simulated with layered gradients (no real refraction: backdrop-filter is unreliable inside
  HyperFrames sub-compositions).
- "Green screen" here = compositing polish for already-cut-out layers; no chroma keying of footage is needed in this film.
- Eye-follow of moving elements is done with head direction (the GLB has no eye bones; texture gaze caused artifacts).
