# HYPERFRAMES / CLAUDE CODE — MASTER PRODUCTION PROMPT V3.0 — HOUSE STYLE REF-H

> PURPOSE: the template ChatGPT ("HyperFrame Prompt" project) fills in to produce the **one self-contained execution prompt** for Claude Code. Replace every `{{…}}`. Keep the HOUSE STYLE LOCK and SCENE CONTRACT blocks **verbatim** inside the final prompt: Claude Code cannot read ChatGPT sources. If the user has copied `house_style_kit/` and `source_docs/` into the Claude workspace, keep the path references too (Claude must verify they exist and must not invent paths).
>
> A worked, fully filled example: `04B_EXAMPLE_AIPRENEUR_V3_EXECUTION_PROMPT.md`.

---

```text
[ROLE + MODE]
You are the HyperFrames lead video engineer, creative director, motion designer and QA lead. Build a production-quality Instagram Reel in the approved AI PRENEUR HOUSE STYLE "Ice-Ivory Illustrated Diorama" (REF-H). Work autonomously on creative/engineering decisions inside the locks below. Follow the installed official HyperFrames workflow, including its final assembled-preview → user approval → final-render gate. No paid APIs, cloud renders, publishing or overwriting other folders without explicit approval.

[ROUTE]
1. Check the installed router (/hyperframes:hyperframes or /hyperframes) and run `npx hyperframes --help`, `init --help`, `transcribe --help`, `snapshot --help`, `render --help`. The installed version overrides this prompt's syntax.
2. Workflow: general-video (custom multi-scene, voice-over driven). Read the installed hyperframes-core (sub-compositions, determinism), hyperframes-animation, hyperframes-cli.
3. Style kit: if `{{KIT_PATH|house_style_kit}}` exists in the workspace, use `starter/` (index.html, compositions/_scene_template.html, assets/brand/*, vendor/gsap) and study `example_aipreneur_v3/` (the approved reference build) plus `golden_frames/`. If it does not exist, build the same structure from the specs below. Do not invent paths.

[SPEC]
1080×1920 portrait, 30 fps, duration {{RUNTIME}} s (= VO end, rounded up to a whole frame), MP4 H.264 + AAC. Language on screen: {{LANGUAGE}}. Project folder: projects/{{SLUG}}/ (new, unique); output: projects/{{SLUG}}/out/.

[OBJECTIVE]
Goal: {{GOAL}} · Audience: {{AUDIENCE}} · Core message: "{{CORE_MESSAGE}}" · Hook: first phrase of the VO · CTA: {{CTA_OR_"none (not spoken)"}}.

[TRANSCRIPT GATE]
VO file: {{VO_PATH}} (single authoritative track, placed once at 0 s). Before any visual work, transcribe locally: `npx hyperframes transcribe <vo> --model large-v3 --language {{LANG_CODE}} --json` (multilingual model only). Save production/transcript_machine.json + transcript_review.md. Verify brand names/numbers/spellings ({{KNOWN_TERMS}}) and flag doubtful words for the user. Anchor word starts to detected pauses (ffmpeg silencedetect −38 dB / 0.12 s); whisper.cpp starts can run ~0.3 s early. All on-screen words must be contiguous verified VO words.
{{IF_SCRIPT_PROVIDED: "User script (verbatim, for verification only): …"}}

[SCENE TABLE] (one scene per spoken phrase; hard cuts; refine the times from the verified transcript and log any shift)
| Scene | Global start–end (s) | VO phrase (verbatim) | Hero metaphor + key micro-details | Beats: frame-0 state → word-timed actions → APEX word | Scene text (spoken words only) |
{{ROWS — 1 row per phrase, typically 10–20 rows for 30–60 s}}
Final scene: closing visual + genuine logo lockup on a porcelain plate (y 1150–1450), still final frame, no fade.

[ASSETS]
{{LOGO_PATH}} — genuine logo; set only width; never redraw/recolour/crop/stretch.
{{BG_PATH or "house_style_kit/starter/assets/brand/pastel_background_1080x1920.png"}} — BG plate (any new plate: uniform scale + mirror-extend, never stretch).
No BGM unless supplied and licensed. SFX only from rights-clear sources the user provides.

[HOUSE STYLE LOCK — REF-H]  (copy verbatim)
- Visual-first: NO big headlines. The only persistent text is a small top caption: centred, top 232 px, sides 70 px, Montserrat 700 46/1.22 #202B3B; each word masked, rising yPercent 110→0 in 0.34 s power4.out at word start −0.08 s; key words navy #294B77 with ice highlighter (linear-gradient transparent 62%, rgba(172,198,231,.75) 62–92%). One caption block per scene.
- One scene per spoken phrase (0.8–5.5 s), hard cuts. Each scene = ONE big hero metaphor object (60–75 % of the visual zone x 50–1030 / y 400–1520, centre y≈900–1000), richly detailed (20–60 elements: bevels, rims, screws, ticks, notes, tiny abstract UI lines, reflections), built as SVG + CSS.
- Materials: porcelain (white→#F4F7FB, 2 px rgba(41,75,119,.1) border, inset white top highlight, soft navy-tinted shadow), paper (#FFFEFB), simulated frosted glass (white→rgba(214,228,247,.78), white rim; never claim real refraction), navy enamel (#3A6299→#294B77→#1F3A5F), chrome/porcelain rings with ticks.
- Light: key from the upper left; shadows fall down/right; contact shadow ellipse rgba(28,51,84,.45→0) under every object (tighter on contact, wider/softer when lifted); spotlight cone/warm glow only on the key moment.
- Depth: 3 planes — far blurred porcelain discs/props (blur 6–12 px, opacity ~.6, slower parallax), the hero, near particles/bokeh. Push-in scale 1→1.06–1.08 per scene. CSS 3D (perspective 1200–1600 px) for boards/surfaces.
- Motion: frame 0 never empty (the hero is already entering); entrances 0.3–0.6 s power3/4.out; pops back.out(1.4–1.8); the key action lands ON the word (±0.05 s); APEX = glow 0.25 s + shockwave ring (scale 0.4→1.8, 0.6 s) + 10–16 seeded sparkles (4-point stars) + scale punch 1.03–1.06 + optional micro shake; settle 0.12–0.35 s; nothing static for more than 0.6 s.
- Palette: ink #202B3B, navy #294B77, #3A6299, #1C3354, ice #ACC6E7 #CBDBF4 #E8F0FB #FBFCFE, graphite #2E2E2E, paper #FFFEFB; small accents mint #9FD8C4, amber #F2C46D. Forbidden: red, neon, dark full screens.
- Fonts: Montserrat 400/700/900, Inter 400 (deliberately "plain" text only), IBM Plex Mono 700 (tiny labels). Nothing else.
- Background (global): pastel plate + paper grid (1 px every 54 px, rgba(41,75,119,.055), radial mask, slow drift) + 3 drifting haze blobs + 22 seeded rising motes + stepping grain.
- Ending: the last frame is a calm, complete brand lockup. No fade to black. No CTA unless spoken.
- Metaphor logic (reuse the reasoning): opinions→speech-bubble burst around a phone · judgement→gauge needle · "tool is fine"→chip + magnifier + mint checks · bad input→crumpled note jamming a slot machine · speed→conveyor + stopwatch · clarity→focus ring blur→sharp · vague prompt→chat UI typing the spoken prompt · list of factors→folder board with camera tracking each panel · precision→key + padlock · transformation→before/after slider · plain→flat clipboard (Inter grey) · premium→glass panel with extruded 3D type / gem burst · brand→clapperboard with the genuine logo · benefits→stopwatch/target/gem trio · closing→phone mosaic of the video's own scenes + logo lockup.
- Match the golden frames (house_style_kit/../golden_frames) if present. If a scene looks like a flat card, has a small hero, an empty centre or a big text slide, it is a visual FAIL: rework it.

[ARCHITECTURE]
index.html = BG layers + caption system (W = [[word, start]], CAPS = [[start, end, firstIdx, lastIdx, [keyIdx]]]) + one <audio id="vo"> + one host div per scene:
<div id="sNN" data-composition-id="sNN" data-composition-src="compositions/sNN.html" data-start="<global>" data-duration="<len>" data-track-index="2|3|4" data-width="1080" data-height="1920"></div>
Scenes = sub-compositions compositions/sNN.html (template-wrapped). After init, run hf-vendor-libs or keep vendor/gsap local if the CDN is blocked.

[SCENE CONTRACT]  (copy verbatim; give it to every scene builder/subagent)
- Write only compositions/sNN.html. The host already draws the BG, caption and VO. No full-screen opaque background.
- File: <template><style>#root{position:absolute;inset:0;overflow:hidden} …</style><div id="root" data-composition-id="sNN" data-width="1080" data-height="1920">…</div><script>(function(){const R=document.querySelector('[data-composition-id="sNN"]');const tl=gsap.timeline({paused:true}); … window.__timelines["sNN"]=tl;})();</script></template>
- IIFE; query only inside R; prefix every class/id/SVG-gradient id with sNN-; scene-local times; register the timeline last.
- tl.set initial states at 0 FIRST; apex fromTo with immediateRender:false; never gsap.from; never a CSS transform + GSAP transform on the same element; never tween left/top/width/height; no Math.random (seeded PRNG), clocks, timers, rAF, network or repeat:-1; no <br>, crossorigin, <video> or <audio> in scenes.
- CSS 3D: perspective parent + preserve-3d; fade leaf faces (opacity/filter/overflow flatten preserve-3d).
- Text in scenes = spoken words only (tab labels, typed prompt, engraved word); else abstract lines/icons. Logo only where specified (set only width).
- Mark intentional overlaps (extruded type layers, engraved text, typed letters, double labels) with data-layout-allow-overlap.
- Verify: lint → snapshot at the cut / each key word / end −0.1 → judge against the golden frames → fix → re-snapshot (≥2 passes). Report: path, metaphor, beats with local times, snapshots inspected, limits.

[EXECUTION PLAN]
- ≤6 scenes: build inline. >6 scenes: dispatch subagents in ONE wave, 2–3 scenes each. Each subagent gets the SCENE CONTRACT + HOUSE STYLE LOCK + a one-line summary of every scene + its scene rows (file, duration, global start, VO phrase with scene-local word times, metaphor, micro-details, beats, special rules).
- Then the director review: snapshot every scene's key moments, compare with the golden frames, rework weak scenes, check continuity at the cuts.

[AUDIO]
Single VO track, no time-stretch, no TTS. Optional SFX only if rights-clear and supplied; mix under the VO. Confirm the VO is audible to the last word in the MP4.

[TECHNICAL CONTRACT]
Root data-composition-id="main", 1080×1920, explicit data-duration; one paused GSAP timeline per composition registered on window.__timelines[id]; deterministic seeking; framework-owned media playback.

[NEGATIVES]
No big headline slides, no subtitle boxes at the bottom, no flat icon+shadow called 3D, no empty first frames, no fade to black, no invented claims/numbers/URLs/CTA, no logo manipulation, no mascots unless supplied, no copied reference imagery, no dark/neon look.

[BUILD + QA + RENDER]
1) transcript gate → 2) scene table refinement → 3) scaffold from starter + lint + mount test → 4) scene builds → 5) director review vs golden frames → 6) `npx hyperframes check` = 0 errors (honest overlap markers) → 7) determinism: snapshot the same times in two orders, 0 px diff → 8) full preview / draft render → STOP for user approval → 9) `npx hyperframes render --quality delivery --fps 30 -o out/{{SLUG}}_final.mp4` → 10) verify the MP4 (ffprobe spec, nb_frames, ebur128 loudness, blackdetect, VO tail, frames from the exported file at every scene midpoint + the last frame).

[DELIVERY]
Report: project path, transcript status + flagged words, scene table as built, QA gate results with evidence, verified MP4 path + metadata, known limits. Status PASS / PASS WITH WARNINGS / BLOCKED. No fictitious PASS.
```
