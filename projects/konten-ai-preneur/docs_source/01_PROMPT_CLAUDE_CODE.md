YOU ARE CLAUDE CODE running in the extracted local Windows folder `konten ai preneur` containing the supplied assets and docs. Act as HyperFrames Creative Motion Director, motion engineer, audio sync editor and QA operator. Deliver a REAL verified portrait MP4; do not merely describe one. Do not ask for another creative brief; brief/VO/motion design are locked. Always honor any final-render approval requirement enforced by the installed official HyperFrames workflow.

[ROUTE]
Use the OFFICIAL locally installed HyperFrames skill router if available: `/hyperframes:hyperframes` (plugin install) or `/hyperframes` (standalone install), but DISCOVER which is actually installed; never invent a slash command. Prefer a current official `motion-graphics` or `general-video` route based on the installed router's documented selection. Read any local `CLAUDE.md`/`AGENTS.md`, installed HyperFrames skills, CLI schema, and relevant official docs. Source-of-truth: https://github.com/heygen-com/hyperframes and the actual installed CLI. Inspect `npx hyperframes --help`, `render --help`, `check --help`, `lint --help`, and init options as needed. Do NOT reinstall an already working setup or use guessed deprecated flags.

[FORMAT / SPEC]
PROJECT: AI PRENEUR — Premium Motion from Prompt
PROJECT OUTPUT FOLDER: create a NEW subfolder `production/` or another uniquely named fresh project INSIDE this extracted folder; preserve original assets/docs. Never overwrite unrelated projects.
FORMAT: native vertical 9:16, 1080x1920, 30fps, actual MP4 high quality; H.264 video and AAC audio if locally supported.
TOTAL: EXACTLY 48.000s = 1440 frames at 30fps (end-exclusive). The previous 50-second estimate is superseded by measured VO durations.
AUDIENCE: company leaders, business owners, enterprise/creative professionals.
LANGUAGE: Bahasa Indonesia for all visible and spoken copy.
CORE MESSAGE: Premium AI-assisted motion is possible with explicit, well-directed prompting—not with vague requests alone.
DO NOT generate new VO. The eleven recorded files and a correctly assembled aligned VO master already exist.

[OBJECTIVE]
Make an aesthetically exquisite corporate showreel that simultaneously TELLS and DEMONSTRATES the benefit of precise prompting by presenting real polished motion on screen. This must feel like a custom-built professional motion film, not cards + fades or a static PowerPoint. A strong visual argument travels from a vague prompt through five direction parameters to a dynamic sophisticated result, then lands on the user's authentic AI PRENEUR wordmark. A test viewer should understand the claim without needing an external talking-head presenter or fake statistics.

[AUTHORITATIVE LOCAL ASSETS]
Root of all relative paths = the extracted folder in which this prompt file resides. Check each file actually exists before implementing. Quotes below denote names, not shell syntax.
- `assets/background/background_portrait_1080x1920.png`: PRIMARY FULL-FRAME BACKGROUND for ALL scenes, user-provided original color palette preserved. Original available `assets/background/background_user_original.png`.
- `assets/logo/ai_preneur_wordmark_trimmed.png`: PREFERRED original AI PRENEUR wordmark with transparent padding cropped away; no glyph/color modification. The untouched original is `assets/logo/ai_preneur_logo_original.png`.
- `assets/voice/VOICE_MASTER_48s.m4a`: USE THIS SINGLE 48.0s ALIGNED AUDIO TRACK for Indonesian speech. Isolated source VO `assets/voice/VOICE KE 1.mp3` ... `assets/voice/VOICE KE 11.mp3` are also included for per-scene checking. NEVER include master and eleven originals simultaneously in playback (double VO).
- `reference/reference_motion_original.mp4`: 52.607s original user-provided style benchmark for pace and visual energy ONLY. Must NEVER be copied into the final film or have its audio lifted.
- `docs/05_AUDIO_TIMING.csv`: authoritative scene-to-clip mapping and absolute voice start times.
- `docs/07_SCENE_DATA.json`: precise frame ranges, full motion mechanics, visuals, text and handoffs. Use it to verify the detailed instructions below.
- `docs/06_VO_SCRIPT_REFERENSI.md`: textual VO DRAFT only. The supplied recorded audio is authoritative for spoken delivery; do not fabricate transcriptions or overwrite real clips. Inspect the actual supplied audio and manually verify legible copy against it; if a substantive mismatch is genuinely unresolvable, flag it without inventing changed speech.

[VISUAL / MOTION SYSTEM]
BRAND GRADIENT: `linear-gradient(120deg,#0a0d2c 15%,#294b77 100%)`. Apply to BIG headline lettering using actual CSS/SVG gradient with browser-render parity; supporting text solid #0a0d2c. No cyan, neon, bronze, lime or red substitute. Light airy supplied background must remain recognizable. Use sparse thin blue-gray rules, refined framing and occasional intentionally subdued white panel layers. Do not recreate the background with a generic unrelated CSS gradient unless the user asset is genuinely broken (and report blocker).
TYPEFACE — HARD LOCK (USER REVISION): Use **Poppins** exclusively for ALL newly authored on-screen text, in exactly TWO genuine styles: **Poppins Regular (font-weight: 400)** + **Poppins Bold (font-weight: 700)**. Art-direct a CUSTOM WEIGHT-MIXED editorial composition, rather than setting whole paragraphs to Bold or mixing different font families. Treat both face and weights as required, not a mere suggestion. This overrides any old Manrope / Plus Jakarta Sans / Segoe UI defaults. Poppins Regular = quiet setup lines, context, secondary copy, smaller interface labels. Poppins Bold = punchline, key benefit, central claim and close. The supplied AI PRENEUR logo remains the untouched IMAGE asset, NOT typed as Poppins.
FONT IMPLEMENTATION: First verify whether both genuine Poppins Regular and Poppins Bold are available on this Windows machine/local project. If missing, use an authentic properly licensed source for both exact weights only if local policy/permission/network allows; verify usage rights, inspect font metadata, import local project assets and ensure they load in HyperFrames render/browser. Do not fake Bold using CSS synthetic font-weight, use wrong substitute without informing the user, or download dubious font bundles. No font binaries are included in this ZIP. If the authentic fonts cannot be obtained, report a blocking font dependency rather than silently switching to another family. With @font-face use separate face declarations for weights 400 and 700; set `font-family: 'Poppins', sans-serif` and `font-synthesis: none` (verify renderer supports these). Never use 500/600/800/900 as substitute weights.
TYPE HIERARCHY & GRADIENT: The Bold hero/punchline spans use the LOCKED navy–steel gradient `linear-gradient(120deg,#0a0d2c 15%,#294b77 100%)`; Regular setup copy uses solid #0a0d2c (or the restrained gradient only where still readable). Preserve exactly ALL quoted words, punctuation and case. Favor optical left-alignment, distinct size + weight contrast, considered line breaks and breathing space. Poppins's broad letterforms may require recalculating text widths, masks, scene spacing and render measurements. Reduce font size, adjust tracking/line breaks, or rebalance layout if necessary; never let text clip; never solve by substituting fonts. Weights may appear simultaneously on separate lines or within a headline using multiple inline spans—do not animate each word pointlessly.
PER-SCENE WEIGHT CHOREOGRAPHY (copy itself unchanged): S01 first line 400, second line 700. S02 first line 400, second 700. S03 first 400, second 700. S04 first 700, middle 400, final 700. S05 first 400, quoted phrase 700. S06 intro 400, selected/main category 700 with inactive category labels 400; on reveal each category temporarily becomes 700 without displaying duplicate words. S07 first 400, second 700. S08 first 400, second 700. S09 first 400, brand claim 700 (real logo stays its original artwork). S10 'LEBIH CEPAT.' 400, 'LEBIH TERARAH.' 400, 'LEBIH PREMIUM.' 700 at final tableau; change focus via timing if desired but not via unsupported weights. S11 first 400, second 700, third 700. Timing, audio, brand, background and exact copy are UNCHANGED by this font revision.
See also `docs/08_POPPINS_TYPOGRAPHY_SPEC.md` for typography QA and per-scene hierarchy. (Filename intentionally shown below in accurate spelling.)
LAYOUT: Mobile-first frame; conservative approx critical-copy x=90–900, y=220–1540 on 1080x1920, a design heuristic and NOT an Instagram UI guarantee. Larger room for decorative lines only. One primary focal element per moment. Design typography with 2–3 levels, consistent baseline rhythm, calculated visual spacing and proper contrast. No tiny fake code in the scene.
MOTION PHILOSOPHY: Precise, cinematic, distinct. Prefer true MASKED reveal, shared-element spatial continuity, clip-boundary geometry, nested frames, subtle parallax (<3% drift), grid alignment, selective stagger, eased settling and visual cause/effect. Mechanisms must differ meaningfully across scenes. Avoid fake always-moving backgrounds, endless spin, bouncing labels, repeated generic bottom-up text, gratuitous glow/shaders, tacky glass, extreme zoom, fake 3D holograms. For genuine UI demonstrations implement ORIGINAL abstract components; never fabricate brand dashboards or product features.
BRAND: Do NOT recreate logo text from a font or morph arbitrary characters into the logo. Reveal the untouched trimmed image by mask/fade/position while preserving aspect ratio and actual pixel identity.
TRANSITIONS: all geometry and opacity must be authored with deterministic time-based seekable animations. Scene transitions may visually share geometry across beat boundaries via properly timed layers; total runtime and VO timings stay locked.

[AUDIO]
Use ONLY the supplied `VOICE_MASTER_48s.m4a` track as VO; no auto TTS. Every VO original is mapped to its own beat (VOICE KE N = SNN). Audio alignment already includes 6 frames (0.2s) of scene pre-roll and ~0.5s trailing breathing space per scene, with longer endcard hold. Do not time-stretch original VO to force previous storyboard durations. NO background music. Subtle SFX ONLY if verified locally accessible, licensed, and will not overpower speech; otherwise omit all SFX. Check no clipping, doubled VO, silence dropouts beyond intended holds, or final hard cut.

[LOCKED BEATS — TIMECODES ARE FRAME-ACCURATE]
Each beat uses END-EXCLUSIVE frame indices. Use actual seconds = frame/30 without cumulative floating-rounding. All EXACT ON-SCREEN COPY written in double quotes below is LOCKED. Do not add additional legible interface labels, made-up performance numbers, fake URLs, misleading studies, or branding.

S01 | FRAMES 0..123 | 0.000000s → 4.133333s | duration 124 frames
ROLE: Hook / challenge assumption
EXACT COPY:
    "BANYAK ORANG BILANG"
    "AI HASILNYA MASIH BIASA AJA."
VISUAL / LAYOUT: Use the real pale blue-white supplied background edge-to-edge. A small ORIGINAL AI PRENEUR wordmark sits in the upper safe area. A 2-line typographic monolith occupies center-left, with hairline crop marks and an intentionally empty right side. Negative space is generous.
INTERNAL MOTION / TRANSITION: 0.00–0.20s: live background and one thin line; 0.20–0.65s: mask-reveal first line via shallow diagonal clipping; 0.62–1.40s: second line exposes in two precisely offset word groups; 1.40–3.65s: a restrained shift of typographic depth and traveling hairline, not idle bounce; last 0.38s: second-line mask becomes the next scene split. Cubic-out for entry; smoothstep for settle.
AUDIO: VOICE KE 1.mp3 begins at global 0.200000s, approx ends 3.622041s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: One subtle low soft accent at main thesis reveal; only if source license is verified.
EXIT / HANDOFF: First headline partitions into left/right comparison rails; image background never cuts to black.
ASSETS: background_portrait, logo_trimmed, VOICE KE 1.

S02 | FRAMES 124..225 | 4.133333s → 7.533333s | duration 102 frames
ROLE: Problem reframing / visual contrast
EXACT COPY:
    "PADAHAL MASALAHNYA"
    "SERING BUKAN DI AI-NYA."
VISUAL / LAYOUT: Create a split BEFORE/AFTER concept using the SAME neutral typographic sample, not invented product claims: left = flat static type and broken spacing; right = a refined, aligned motion grid. Floating narrow navy dividers give direction. Headline is anchored top-left of the main content zone.
INTERNAL MOTION / TRANSITION: First 0.45s the existing rails hinge apart; next 0.45s two sides resolve with masked vertical windows. Within following 1.5s an example on right animates cleanly from wireframe to composed grid while left holds flat. No abrupt camera spins. Last 0.35s the right rail becomes the keynote underline in S03.
AUDIO: VOICE KE 2.mp3 begins at global 4.333333s, approx ends 7.023945s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Tiny pane lock/click at the clean-right reveal.
EXIT / HANDOFF: Right-side refined rule line extends into the S03 headline baseline.
ASSETS: background_portrait, abstract CSS/SVG typography only, VOICE KE 2.

S03 | FRAMES 226..317 | 7.533333s → 10.600000s | duration 92 frames
ROLE: Central thesis / precision
EXACT COPY:
    "MASALAHNYA ADA DI"
    "ARAHAN YANG DIBERIKAN."
VISUAL / LAYOUT: Show one giant headline left-biased. Under it, a long thin guide line with 3 moving control nodes implies explicit creative direction. Restrained perspective layers reinforce clarity.
INTERNAL MOTION / TRANSITION: At start a line inherited from S02 draws across an invisible baseline (0.35s). Headline emerges using independent word masks with 0.07s stagger, NOT flying from the bottom. Control nodes move to fixed grid anchors, then stop. Last 0.35s guide line folds neatly into the structural frame of S04.
AUDIO: VOICE KE 3.mp3 begins at global 7.733333s, approx ends 10.084353s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Single soft interface-confirmation tick when guide nodes align.
EXIT / HANDOFF: Guide line becomes the three precision tiers/steps, no full-frame flash.
ASSETS: background_portrait, generated SVG rules/nodes, VOICE KE 3.

S04 | FRAMES 318..447 | 10.600000s → 14.933333s | duration 130 frames
ROLE: Reason / brief clarity
EXACT COPY:
    "AI ITU CEPAT."
    "TAPI HASILNYA MENGIKUTI"
    "SEBERAPA JELAS BRIEF-NYA."
VISUAL / LAYOUT: A vertical precision ladder: three increasingly refined abstract modules, WITHOUT extra unreadable labels. Graphic 1 = one vague bar; graphic 2 = aligned instructions; graphic 3 = finished visual arrangement. Supporting copy is prominent and positioned away from modules.
INTERNAL MOTION / TRANSITION: Unfold three modules successively from a single shared center pivot over 0.95s, then sweep a slim focus indicator sequentially. The final module assembles into a crisp composition using a 0.55s constrained morph of rectangles (not fake content). Hold while VO lands. The final module opens into the prompt editor for S05.
AUDIO: VOICE KE 4.mp3 begins at global 10.800000s, approx ends 14.431020s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Very light focus snaps at the three meaningful completion points.
EXIT / HANDOFF: Third module frame stretches smoothly into one large prompt field.
ASSETS: background_portrait, HTML/CSS geometry, VOICE KE 4.

S05 | FRAMES 448..549 | 14.933333s → 18.333333s | duration 102 frames
ROLE: Weak prompt / clear negative example
EXACT COPY:
    "BUKAN CUMA SURUH"
    "‘BIKIN YANG KEREN’"
VISUAL / LAYOUT: One bespoke prompt-input canvas with large readable generic instruction. One empty detail column communicates a missing brief via whitespace and structural placeholders—not fake textual errors or faux software brand. Only quoted words are legible.
INTERNAL MOTION / TRANSITION: Prompt canvas grows out of S04 module at start; cursor/typing effect is restrained and finishes within ~0.65s. Brief moment of near-stillness to communicate vagueness. Detail rows remain unfilled, and the quoted instruction scales down to dock at upper-left before S06.
AUDIO: VOICE KE 5.mp3 begins at global 15.133333s, approx ends 17.823945s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: One understated keyboard note, not exaggerated typing.
EXIT / HANDOFF: The raw prompt remains as small anchor while structured direction enters, proving an upgrade.
ASSETS: background_portrait, generated clean prompt panel, VOICE KE 5.

S06 | FRAMES 550..731 | 18.333333s → 24.400000s | duration 182 frames
ROLE: What good prompting specifies
EXACT COPY:
    "TAPI MENJELASKAN"
    "STYLE"
    "RITME"
    "KOMPOSISI"
    "TRANSISI"
    "HIERARKI"
VISUAL / LAYOUT: Prompt architecture forms an exquisite system diagram: five typographic labels following a left-aligned spine. Each label controls a nearby live miniature graphic: font treatment, rhythmic motion bars, responsive grid, connective transitioning shape, and reading-order emphasis. Never stack five generic identical cards.
INTERNAL MOTION / TRANSITION: 0.0–0.35s thesis repositions; each named category starts after its spoken cue (approximate at scene-local 0.7, 1.65, 2.6, 3.55, 4.5s; verify against actual VO), initially appears via mask and activates its own meaningful graphic. Animate a line traveling between modules, not five separate fly-ins. At local 5.2–5.8s all five align into a unified prompt schematic. Last 0.3s the graphic compresses to become S07 transformation input.
AUDIO: VOICE KE 6.mp3 begins at global 18.533333s, approx ends 23.888435s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Only 2–3 deliberate ticks at meaningful reveals; no whoosh per keyword.
EXIT / HANDOFF: Unified system sends a guided blue line directly to the BEFORE/AFTER axis.
ASSETS: background_portrait, SVG/CSS micro-illustrations, VOICE KE 6.

S07 | FRAMES 732..885 | 24.400000s → 29.533333s | duration 154 frames
ROLE: Cause / effect demonstration
EXACT COPY:
    "PROMPT YANG TEPAT"
    "MENGUBAH OUTPUT"
VISUAL / LAYOUT: A continuous comparative object demonstration of the same 2D composition evolving from a cramped text block to a polished cinematic typographic layout. A slender cause-to-effect line travels LEFT TO RIGHT. The right side is an actual animated result, not a screenshot/fake product demo.
INTERNAL MOTION / TRANSITION: First 0.45s central prompt token enters and settles. From 0.6–2.4s a controlled sweep progresses across the comparison boundary; rectangle spacing, typography masks and line density mutate deterministically. At 2.4–4.0s the premium side performs 2 complementary motions—a staggered reveal and a masked object pivot—to prove visual capability. Last 0.4s camera shifts subtly into the now-dominant premium side.
AUDIO: VOICE KE 7.mp3 begins at global 24.600000s, approx ends 29.014694s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: One precision transformation soft impact, no stock explosive riser.
EXIT / HANDOFF: The AFTER side scales into the full canvas without changing the supplied background.
ASSETS: background_portrait, custom graphics, VOICE KE 7.

S08 | FRAMES 886..1022 | 29.533333s → 34.100000s | duration 137 frames
ROLE: Premium hero motion / payoff
EXACT COPY:
    "DARI TEKS BIASA"
    "JADI MOTION YANG TERLIHAT MAHAL."
VISUAL / LAYOUT: This is the showcase beat. One central typographic hero, moving orchestrated borders, intentional depth, component-level parallax, numerical-free diagrams and edge-aligned micro-panels. Do not invent dashboards, brands, statistics or labels. Gradient headline is exceptionally clean and spacious.
INTERNAL MOTION / TRANSITION: Entry as inherited BEFORE/AFTER sample expands (0.4s); mask cuts reveal the top headline; hero second headline emerges through shared boundary geometry (0.55–1.25s). During 1.2–3.6s execute a designed 4-part movement: hairline follows a spline-like rectilinear path, nested frame resolves, iconless blocks travel in stagger, and camera drifts <3% to reinforce space. Movement finishes at VO payoff. At exit, all components move outward to expose centered logo.
AUDIO: VOICE KE 8.mp3 begins at global 29.733333s, approx ends 33.573333s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Restrained cinematic accent on final result lock.
EXIT / HANDOFF: Graphic elements clear a brand-safe zone; never pretend shapes generate the true logo.
ASSETS: background_portrait, generated abstract motion graphics, VOICE KE 8.

S09 | FRAMES 1023..1138 | 34.100000s → 37.966667s | duration 116 frames
ROLE: Brand provenance / reveal
EXACT COPY:
    "INILAH CARA"
    "AI PRENEUR MENGARAHKAN AI."
VISUAL / LAYOUT: Center-left brand wordmark appears from the actual transparent logo asset with exact proportions. A single thin brand-line tracks underneath. Copy remains highly legible; no random glyphs morph into the logo. White–blue background remains consistent.
INTERNAL MOTION / TRANSITION: 0–0.4s previous shapes leave via precise paths; 0.35–0.85s logo fades/reveals under one clean mask in its actual image geometry; at 0.85–1.55s copy resolves in two steps. Last 1.0s line draws rightward and plants three future nodes for S10.
AUDIO: VOICE KE 9.mp3 begins at global 34.300000s, approx ends 37.434694s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Brand reveal has a single low understated accent if rights verified.
EXIT / HANDOFF: Underline branches to three benefit modules while original logo stays preserved and unclipped.
ASSETS: background_portrait, ORIGINAL logo trimmed, VOICE KE 9.

S10 | FRAMES 1139..1297 | 37.966667s → 43.266667s | duration 159 frames
ROLE: Value summary / three proof-by-motion examples
EXACT COPY:
    "LEBIH CEPAT."
    "LEBIH TERARAH."
    "LEBIH PREMIUM."
VISUAL / LAYOUT: Three statements arranged sequentially as an architectural vertical editorial layout. EACH claim shows a distinct graphic cue rather than generic cards: CEPAT = one line resolves in a swift controlled path; TERARAH = nodes snap into deliberate grid order; PREMIUM = final meticulous alignment with quiet border highlights. They are design claims, not quantified business performance promises.
INTERNAL MOTION / TRANSITION: First concept becomes focal in 0–1.2s, second takes priority in 1.2–2.6s, third completes from 2.6–4.4s; keep earlier statements visible at reduced emphasis. Link all movements through a single continuous line from S09. Last ~0.4s reduce visual clutter so close can breathe.
AUDIO: VOICE KE 10.mp3 begins at global 38.166667s, approx ends 42.738096s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: One gentle snap per concept completion (maximum three).
EXIT / HANDOFF: Three graphic motifs contract towards one horizontal brand baseline; no collision.
ASSETS: background_portrait, brand logo small if composition allows, VOICE KE 10.

S11 | FRAMES 1298..1439 | 43.266667s → 48.000000s | duration 142 frames
ROLE: Memorable brand endcard / CTA
EXACT COPY:
    "AI BISA MEMBUAT"
    "MOTION SELEVEL INI."
    "ASAL PROMPT-NYA TEPAT."
VISUAL / LAYOUT: Clean spacious endcard using the REAL AI PRENEUR wordmark at top of central safe area. Three lines of closing statement occupy central-left/center alignment with strong hierarchy. Deep navy–steel blue gradient only on hero phrase; body solid navy. No website/handle or extra claims unless provided.
INTERNAL MOTION / TRANSITION: 0–0.45s carry three graphic motifs into one thin underline. 0.4–1.45s headline reveals via tiered masks; 1.25–2.1s last line draws in with a rare restrained letter-group stagger. Brand lockup holds genuinely still for at least the final 0.82s after the voice ends (~47.18 to 48.0). Do NOT fade to black or abruptly remove the logo.
AUDIO: VOICE KE 11.mp3 begins at global 43.466667s, approx ends 47.176055s; already encoded into supplied master. Do not replay isolated clip on top. Optional SFX idea: Optional soft resolve around last line, then silence for readable branded end.
EXIT / HANDOFF: Final frame at 48.0s contains clean stable branded composition.
ASSETS: background_portrait, ORIGINAL logo trimmed, VOICE KE 11.

[EXACT COPY / SPEECH AUTHORITY]
Above double-quoted strings constitute the entire approved visible narrative. You may reflow line breaks for accessibility but never change words, punctuation, capitalization or add claims. Use recorded Indonesian VO verbatim. The prior text script in `docs/06_VO_SCRIPT_REFERENSI.md` is a convenience/reference, NOT certified transcription. Review video with audio to ensure the graphic sequence matches spoken phrases; if audio differs in a material way, keep audio untouched, record mismatch, and ask ONLY if essential. Do not assert words were transcribed unless actually verified. No subtitle track is required because the principal message exists as full-size visual typography; if subtitles materially improve accessibility and do not obscure the graphics, use exact words and real timing, not guessed captions.

[ASSETS / PROVENANCE]
- Verified provided: user gradient background, authentic company wordmark, 11 recorded MP3 voices, user-reference MP4.
- Verified derived in package: portrait background (crop+resize only), cropped transparent original wordmark, 48s audio master (original VO plus placed silence; no regenerated speech).
- Self-create only abstract UI/components/lines/tokens with native HTML/CSS/SVG/GSAP as compatible with local HyperFrames. The user has not provided a real website UI or staff photographs; do not invent those as factual proof.
- No need to call external media generation services. Do not purchase assets, trigger paid API use, publish to the web, or send private company materials to public sites without express permission.
- Keep all artifacts and modifications inside the fresh project output subfolder while reading original inputs from supplied assets folder. If HyperFrames init needs copied assets inside project, copy exactly and verify imported relative paths.

[TECHNICAL CONTRACT]
Read installed official skills/schema first. Author TRUE HyperFrames-supported HTML/CSS/JS composition(s), not React/Remotion by habit. Establish a unique root composition ID, native 1080x1920, 48s total duration, and timed scene clips with supported `data-start`/`data-duration`/track properties per installed version. Clip visibility and z-index are different concepts—use the local engine's correct conventions. For GSAP, if used, create synchronous, finite, PAUSED timeline(s) registered at `window.__timelines[EXACT_COMPOSITION_ID]` per installed contract; do not let separate runtimes drift. Ensure timeline seeking to arbitrary frames is deterministic. No `setTimeout`, independent real clock, unseeded Math.random, live external fetches, or manual audio/video `.play()`/`.currentTime` synchronization. Media transport/mixing is HyperFrames-owned. Use actual metadata/voice clips; DO NOT invent source paths or engine flags. HTML elements must remain visible only in their intended scene spans. No unknown opacity hangovers or z-index collisions.

[NEGATIVES]
Never use slideshow-style repeated enter-from-bottom captions; generic identical 11 cards; mass-produced AI glow; crushed type at mobile size; screen-wide shake; logo redraw/recolor/geometry alteration; any source-reference frame/audio as final content; synthetic people or faces; hallucinated dashboard/brand; fake ROI/performance/metric evidence; manual footage seek controls; black frames/tails; missing VO; or unsupported/unverified software commands.

[BUILD + QA + RENDER]
1) PREFLIGHT: Confirm local working directory contains expected files; inspect MP3 durations, background dimensions, transparent logo bbox/cropping and 48.000s master. Inspect installed official router and CLI help. Run the current installed official workflow. Open reference for style insight only; do not re-use its copyrighted visuals/audio.
2) AUTHOR: Create a fresh project under `production/`. Write root composition, scene parts and timed clips with exact per-scene frames/times and ORIGINAL visual choreography as described. Implement master voice as ONE source on the audio track. Create supplementary project notes if workflow demands.
3) ITERATE: Run `npx hyperframes lint` (if supported, otherwise verified local equivalent). Fix errors; do not ignore missing audio warnings.
4) BROWSER GATE: Run `npx hyperframes check --snapshots` (or installed documented equivalent). Review screenshots at at least 0.6, 2.2, 4.8, 8.7, 11.8, 16.0, 21.0, 26.4, 31.0, 35.9, 40.1, 44.7 and 47.6 seconds; additionally scene boundary ±0.1s and actual motion in-between times. Adapt snapshot flags after `--help`. Ensure no missing background, altered logo, inaccurate text, clipped headlines or flashes during handoff. Probe nonsequential seeks to catch timeline bugs.
5) VISUAL / AUDIO REVIEW: Preview FULL 48s assembled timeline at a phone-size viewport and full resolution. Listen to original VO and master with visual sync, watching every beat and exact copy; verify volume and readability. Fix overly static or stock effects and rerun checks. Do NOT represent a procedural check as a human-viewed inspection when it wasn't done.
6) MANDATORY FINAL-RENDER APPROVAL: Follow the official installed skill's checkpoint if required. Otherwise render autonomously as user has already authorized.
7) EXPORT: Check `npx hyperframes render --help` and use valid installed options. Example ONLY if supported: `npx hyperframes render --output renders\konten-ai-preneur-final.mp4 --fps 30 --quality high`. Confirm real exported file is nonempty.
8) MP4 QA: Inspect EXPORTED media with available tools such as ffprobe/ffmpeg: actual 1080x1920, portrait, 30fps, total duration near exactly 48.0s, audio stream present, 1 normal Indonesian VO (not doubled). Review full output at intro, all scene centers, transitions, and final logo/CTA; catch black frames, render glitches, clip jumps, missing gradients, text raster artifacts, cropped logo and silence/out-of-sync VO. Repair / rerender as needed. Do NOT claim successful render based on code or preview alone.

[DELIVERY]
Send a concise truthful report containing: PASS/PASS WITH WARNINGS/BLOCKED; VERIFIED final MP4 path; verified project root/composition source path; actual video/audio metadata; asset integrity and VO clip counts; lint/check/snapshot/seek and exported MP4 inspection status with evidence; material repairs; outstanding issues. Do not guess an output path, and never report PASS without checking the actual artifact.
