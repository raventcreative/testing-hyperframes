# COPY ALL TEXT BELOW INTO CLAUDE CODE

You are the creative director, 3D integration engineer, senior motion designer, HyperFrames/GSAP composition engineer, technical storyteller, and QA lead for **AI PRENEUR — AI Engineer Roadmap 2026**.

## 0. Mission

**Build a project and a reviewable video preview, not just a written concept.** Remake the supplied 3-minute English video as an **original Indonesian 9:16 premium cinematic motion graphics explainer**. Use the **user's existing 3D mascot in this Claude Code workspace** in place of the illustrated person from the reference video. Visual quality must resemble a meticulous human motion design studio: tangible 3D objects, logically connected transitions, creative art direction and unusually good scene continuity.

Working title: **THE AI ENGINEER BLUEPRINT — BUILD THE MACHINE**.

Core narrative: People jump to flashy agents before building fundamentals; the 10 skills are physically assembled into one working AI system. Your video is **a continuous build journey**, not 10 disconnected slides.

Constraints: no paid API, cloud rendering, external publishing, deleting/replacing unrelated folders, or invented mascot. Work locally with available tools/dependencies. New scoped project folder only. The ZIP is a preparation pack, not a licensed source footage library.

## 1. Mandatory discovery (do this before coding)

1. Identify the folder containing this prompt. Locate these files relative to it:
   - `assets/background_pale_ice.png` (original image from the user, 1080×1350).
   - `assets/aipreneur_logo_dark.png` (genuine user PNG, 1485×1485 canvas with transparency).
   - `reference/source_ai_engineer_180s.mp4` (source analysis ONLY).
   - `02_VOICE_OVER_FINAL.txt` (authoritative spoken wording).
   - `03_STORYBOARD_PREMIUM.md` (scene blueprint and camera/transition direction).
   - `05_QA_AND_BRAND_LOCK.md` (acceptance criteria).
   Do not invent paths. If the input pack is somewhere else, ask for its path.
2. **Locate the 3D mascot already in the Claude Code project**. Inspect files in typical project asset paths for `.glb`, `.gltf`, `.fbx`, `.blend`, character components, texture maps, rigging and existing render routines. Reuse the original asset, identity, geometry, clothes, color and style. DO NOT generate a new character or change its face/body without approval. If no usable character source is found, STOP and request its exact location.
3. Find the recorded user VO in `assets/voiceover_final.wav` or `assets/voiceover_final.mp3`, or a user-designated path. If missing, create an asset map and still-frame lookdev/test composition only; **do not claim final sync is complete**. Tell the user to generate the exact script from `02_VOICE_OVER_FINAL.txt` and provide the audio. Do not substitute synthetic audio without approval.
4. Inspect versions for `npx hyperframes --help`, `npx hyperframes init --help`, `npx hyperframes transcribe --help`, `npx hyperframes snapshot --help`, `npx hyperframes render --help`. Follow installed syntax, not guessed arguments. Detect available Three.js, GSAP, Blender, FFmpeg and safe local mascot render solution. Prefer the established HyperFrames workflow if installed.
5. Watch the actual source file and inspect sample frames/timecodes; use `01_BEDAH_VIDEO_REFERENSI.md` as observation notes, not gospel. Do NOT copy its character, original audio/music, logos, video frames, layout, or trade dress into the remake.

## 2. Non-negotiable style lock — USER OVERRIDES OLD DEFAULTS

Output: **1080×1920, 9:16 portrait, 30 fps, H.264 MP4 + AAC**. Target story ~100–115 seconds only as an editorial goal; **actual length must follow the recorded VO, not the time estimate**. Every cut, motion apex, and word caption must be retimed to the final audio.

Background: always feature the provided `background_pale_ice.png` as the underlying ice-white/pale-blue plate. It's only 1080×1350. Fit proportionally with edge continuation/colour-matched gradient outside the bounds. NEVER vertically stretch or distort the source. A very subtle fine navy drafting grid, 0.04–0.06 opacity, may be overlaid near the machine. No full black or dark-blue background replaces the user's plate.

Main typography: **Poppins Regular 400 + Poppins Bold 700 exclusively**. NO Montserrat. Main type fill uses real **navy gradient `#0A0D2C → #294B77`**; inline words may be solid navy for readability. Highlighted words use **pure white `#FFFFFF` text on a filled gradient rounded rectangle `linear-gradient(105deg,#0A0D2C 0%,#294B77 100%)`**. Correct contrast on each actual rendered frame; no blue text on a blue card, no gradient inside already-highlighting white text. Avoid full-word masks or clipping that crop descenders.

Caption grammar: 1–2 short lines only, 4–8 words visible at a time depending on phrasing, aligned to actual VO. Prefer editorial top/mid-headline at roughly y=245–420. The mascot and hero prop inhabit the middle/lower vertical zone. Labels on hardware (e.g. `PYTHON`, `RAG`) permitted when spoken in the script and used as a small marker, not duplicate massive headline. Keep 9:16 social UI safe area: critical brand and type avoid top 60 px and bottom 300 px.

Logo: **genuine uploaded AI PRENEUR dark PNG**, top-left in every scene, x=62–75, baseline y=70–140; visually crop **only transparent empty padding** if necessary while preserving every actual logo pixel and original proportions. Target legible displayed width ~175–235 px. Animate entry with 0.25s precision slide/tilt; then a very restrained masked soft-blue diagonal light sweep crossing the letterforms every 7–9s, never dazzling, never flickering. Logo remains completely visible, stationary between sweeps. Do NOT redesign/redraw it; no glow halo on the whole image. Reuse one persistent layer from root, never restart it every cut.

Mascot: **the existing 3D character**, authentic volumetric geometry and physically convincing textures. No new AI-generated face. No comically floppy IK or overblown rubber limbs. Use an actual 3D solution compatible with rendering, e.g. Three.js loaded GLB with timeline-controlled transforms/animation mixer, or a locally pre-rendered transparent animation sequence from its exact source model if better. If arm rig is missing, do not simulate fake limb gestures: use plausible whole-body pose/camera moves and the environment as the action, document the limitation. Character acts as a master engineer and moves only at storytelling beats. Never fake lip sync; voice is narration, not character dialogue.

Materials: frosted engineered glass, satin navy enamel, brushed aluminum details, porcelain white, soft ice-polymer housings, natural graphite/rubber joints, real beveled edges and minute gasket seams. Crisp physically motivated shadows (tight under contact, diffuse when raised), plausible occlusion, top-left key light + subtle blue rim, no fake shallow depth everywhere. No heavy bokeh, iridescent plastic, oversaturated neon, endless particle fog, rainbow lights or cheap HUD rings.

No BGM. Use narration master only. Optional user-provided/right-cleared SFX in reserved transient gaps, mixed lower than speech. No unsourced music, copyright footage or creator identity elements.

## 3. Production concept: the evolving Workbench

One giant, meticulously designed **AI CORE WORKSTATION** on a grounded architectural workbench. At opening, an impressive AI agent module is precariously stacked without a base, and it fails. The mascot unveils a *blueprint with 10 sockets*. Every new skill becomes a **functional part with a unique cause-and-effect action** attached to the SAME central machine. Screens/UI are supporting instruments, not floating card clutter. By scene 12 the machine can operate. The conclusion zooms back to its whole modular construction, with the mascot proudly doing the final inspection.

Use this camera geography to preserve continuity:

- LEFT = input/data racks and code assembly.
- CENTER = AI core and network/calculation stages.
- RIGHT = application/tool output and test/deployment bay.
- FOREGROUND = mascot working zone and physical levers.
- BACK = ice-white blueprint grid and broad rigging, always visually subordinate.

Maintain a scene continuity ledger: incoming foreground object, outgoing object, camera motion direction, last frame, first frame of next scene, shared light direction, logo persistence, location of the central core.

## 4. Storyboard: create 15 sub-compositions with motivated transitions

The time windows here are **rough estimates**, NOT locks. Phrase timing is controlled by verified VO.

**SC01 / HOOK** (VO: “Bikin AI agent doang… ambruk.”): begin on frame 0 with a gloriously engineered floating AI core, but one thin pedestal wobbles under weight; a component slips; mascot physically catches it; no destructive crash or random digital glitch. Highlight `AI AGENT` then `FONDASI`. Camera macro push-in, micro-tilt as joint fails. A fallen connector becomes a blueprint line.

**SC02 / BLUEPRINT** (“sepuluh komponen”): camera follows the connector line to top-down giant blueprint; paper crease expands into a softly extruded porcelain workbench with 10 metallic sockets in perspective. Mascot taps socket #1, precision snap. Hero readable instantly. On-screen highlighted `10 KOMPONEN`.

**SC03 / PYTHON** (“Python… debugging… program kecil”): macro Poppins/code-shaped engravings become actual paths. Function brackets close like 2 hinged calipers; 3 data blocks slide into sockets, API pin clicks and an error bolt is unscrewed by the mascot. On `benar-benar jalan`, a tiny device finally operates. **Match transition:** engraved code strip extrudes into cable pointing toward software bay. Caption `01 PYTHON`.

**SC04 / SOFTWARE ENGINEERING** (“Git, database, backend…”): camera flies gently *along that cable*, never through an unmotivated white flash. Git version rails fork/rejoin, cylinders of database rise with contact shadow, backend chassis receives authentication gate and interface port. This is architecture, not 4 random logos. Caption `02 SOFTWARE ENGINEERING` and one quick highlighted `FONDASI`. Next: database pin drops as a data bead into ML tray.

**SC05 / MACHINE LEARNING** (“data melatih… menguji… salah”): data beads move into a transparent test plane; a sensible simple fitting line appears; one outlier triggers inspection; the model is tested against a separate set. Maskot rotates a calibrated dial. Don't show invented hard numbers. The trend line extrudes into a neuronal conductive path. Caption `03 MACHINE LEARNING`.

**SC06 / DEEP LEARNING** (“neural network, tensor, PyTorch”): 3–4 glass layers of neurons with believable spacing, occasional energy pulse crossing weighted connectors, a small tensor slab snaps in. Top left soft key. Camera pushes **through** physically ordered nodes. Caption `04 DEEP LEARNING`. Last neural edge becomes a text-token track.

**SC07 / LLM** (“token, konteks, embedding…”): typed phrase becomes chunky letter tiles; tiles split into token segments, proceed to context roller and attention matrix; subtle selected lines illuminate causal relationships. No nonsensical AI brain glow. Camera racks from tile macro to precise relational panel. Caption `05 LLM`. One token sequence leaves via output rail.

**SC08 / AI APPLICATION** (“API… output… fitur”): output rail plugs into standardized API connector on one real UI apparatus. Miniature response payload forms structured rows and appears on a phone/app console (not fake logos). Tool action shown as bounded interface call. Caption `06 AI APPLICATION`. UI paper edges fold into the spine of a real document archive cabinet.

**SC09 / RAG — premium showpiece** (“mencari bagian dokumen… relevan… data”): camera flies along archive grooves. A real drawer opens with a measured spring; pages slide into exact chunks, become indexed shelves; a highlighted user question sends a track through the index; **only relevant chunks** detach and return toward model unit; answer assembly occurs at end with 2 tiny connected source tabs. Distinguish retrieval from model generation visually. Cinematic subtle glass reflections and shadows; no vector-space confetti. Caption `07 RAG`, highlight `DOKUMEN RELEVAN`. Its output sheet becomes agent instruction card.

**SC10 / AGENT — premium showpiece** (“alat dan batasan… memilih… memeriksa”): sheet docks in a small task robot. Four stations around finite physical loop: Understand → Choose Tool → Act → Check. Use visual indicators rather than tiny illegible English. Crucially, mascot opens an approval gate before tool action, making user control legible. A device queries database, updates a sample display, verifies return. No infinite self-driving claim. Loop turning wheel becomes evaluation gauge. Caption `08 AI AGENT`.

**SC11 / EVALUATION** (“tes sulit… gagal… tes lagi”): physical test bench: one case fails; clear red/muted warm coral ERROR accent is allowed **inside the tiny instrument only** (the user palette still dominates), mascot swaps defective part, re-runs, pass lamp; no fake percentage uplift. Camera tight tracking to passing needle; pass sticker physically joins machine. Caption `09 EVALUATION`.

**SC12 / PRODUCTION** (“deploy, biaya… keamanan…”): unit enters quality-finished casing. A real hinged enclosure closes; monitoring dials fill at normal, load/latency/cost/log charts become restrained instrument inserts; blue security gate engages. It operates with reliable rhythmic parts and a visible app output. Hero-light beauty reveal with crane-up. Caption `10 PRODUCTION`; highlight `SIAP DIPAKAI`.

**SC13 / PATH CHOICE** (“produk AI atau… training”): master selector lever branches the same platform into two routes. Left: application production bay, API/RAG/agent/eval. Right: deeper model workshop, training/fine-tuning/optimization. A single central core visually anchors both; this is a **choice**, not a requirement to do both. Caption `PILIH JALURMU` and clear short labels.

**SC14 / BUILD IN STAGES** (“proyek kecil… sedikit demi sedikit”): three quick stage models: small ML project → practical LLM app/RAG → reliable deployable assistant. They remain connected by the exact same cable; no teleport. Camera pulls back to reveal the long build journey as workbench layers engage. Caption `SATU PROYEK DULU`.

**SC15 / ENDING** (“bisa membangun sistem… simpan…”): the machine's 10 components align, begin actually working, and show readable miniature end-to-end input→retrieval→tool→result→test monitoring. Mascot stands left within the physical stage with natural body mechanics, does a **small satisfied final check**; no giant wave. Logo upper-left glint is the last subtle motion. Large recap text `SISTEM AI YANG BEKERJA`; final `SIMPAN ROADMAP INI` only where spoken. End on a **calm, fully composed still** for ≥0.25s, no black fade.

**Negative examples for every scene:** generic zoom-pop/rotating card, unrelated spinning chrome object, text wall, noise particles, unanchored hover, five SFX at once, neon bloom, text clipped by phone UI, giant rubber hands, new invented mascot, AI-generated extra fingers, fake lens smear, jitter, random stock clips, unlicensed audio.

## 5. Narrative / voice alignment

The **entire exact Indonesian narration** lives in `02_VOICE_OVER_FINAL.txt`. Do not paraphrase after audio is recorded. If there is no audio yet, scaffold the project and lookdev; ask for the audio before final timing. Once the voice file is supplied:

1. Inspect with ffprobe. Use the installed local offline multilingual transcribe/align route in HyperFrames (e.g. `transcribe --model large-v3 --language id` if available). Save original audio, machine transcript, reviewable anchored word timestamps. Flag recognition ambiguities: `AI Engineer`, `machine learning`, `deep learning`, `PyTorch`, `LLM`, `API`, `RAG`, `agent`, `evaluation`, `production`.
2. Compare every transcript phrase to the user's script for wording. Detect spoken pauses and adjust word-onset alignment; whisper timestamps may be offset. The recorded audio itself is authoritative for absolute pacing, while the written script resolves transcription spelling.
3. Scene start = phrase boundary; action apex must hit the corresponding spoken word to within ~2 frames (≈67 ms). Caption word group remains visible long enough to read; no rapid wipes mid-word.
4. Do not speed-up/time-stretch voice to match estimated storyboard. Video runtime = VO duration plus 0.25–0.4 s clean last-frame hold, rounded to 1/30 s.
5. No unspoken claims, numbers, CTA, app names or fake tech capabilities rendered as new persuasive copy.

## 6. Technical architecture and coding rules

Use the installed HyperFrames version if available and compatible; base structure:

```
project_ai_engineer_remake/
  index.html
  assets/brand/background_pale_ice.png
  assets/brand/aipreneur_logo_dark.png
  assets/audio/voiceover_final.wav|mp3
  assets/mascot/<existing mascot asset reference or copied approved file>
  compositions/s01.html ... s15.html
  production/transcript_machine.json
  production/transcript_review.md
  production/scene_map.json
  production/continuity_ledger.md
  out/
```

Root owns one background plate, one logo layer, one VO player, one main caption player; **scene compositions never create duplicate logo/VO**. Integrate mascot in a persistent root THREE canvas or in per-scene comps with verified continuity and original model/rig; prefer persistent scene graph if possible to avoid lighting/pop/cut changes. Ensure logo and mask share GPU compositing without alpha fringes.

Each composition uses a deterministic, paused GSAP timeline. Use explicit initial `tl.set` for all moveable elements. Use `tl.fromTo(...,{...},{...,immediateRender:false})` or `tl.to`; do not use `gsap.from` if the installed house kit forbids it. Keep local times relative to each scene. No `Math.random`, wallclock, requestAnimationFrame-driven continuous simulation, network textures, infinite loops or unseeded particle states. Every frame must be seekable/reproducible. If using THREE animation mixer, advance via absolute video time (`mixer.setTime`) rather than elapsed wallclock. Never mix CSS transforms and GSAP transform properties on the same DOM element. Do not tween layout geometry (left/top/width/height) during compositing; animate transform, masks and opacity. Prefix per-scene IDs to avoid style collisions.

3D contact and lighting: use a grounded worktop, cast shadow maps or baked contact shadow under the mascot, plausible arm joints, shadows consistent with original background. Use one canonical camera and light rig; derive animated shots from a coherent rig. Background is fixed while workbench/camera moves—do not wobble the entire background plate like a phone camera. Shallow DOF only on 2–3 cinematic macro beats, keep educational diagrams crisp.

Responsive brand clipping test: inspect Poppins on gradient at every major scale; logo actually visible at 1080 width; caption never touches top-left logo, hero part never enters bottom social UI overlay. No UI text smaller than 28px for explanatory labels; major caption preferably 48–62px, with balanced lines.

Do not try to create high-end 3D from only low-detail rounded CSS boxes. Use THREE/Blender local model render where needed, and CSS/SVG/GSAP for clear typography and annotated indicators. Use procedural geometric parts only for fictional machine pieces. The user’s mascot must stay the true visual asset; if fidelity is weak, iterate lighting/textures/camera, don't replace it with an AI picture.

Sub-composition script wrapper (if supported by installed HyperFrames):

```html
<template>
  <style>/* per-scene prefixed classes */</style>
  <div id="root" data-composition-id="s01" data-width="1080" data-height="1920">...</div>
  <script>
    (() => {
      const R = document.querySelector('[data-composition-id="s01"]');
      const tl = gsap.timeline({ paused: true });
      tl.set(R.querySelector('.s01-hero'), {autoAlpha: 1}, 0);
      // Deterministic, VO-aligned transforms, always scene-local time.
      window.__timelines['s01'] = tl;
    })();
  </script>
</template>
```

Always use **installed API schema** and actual `npx hyperframes --help` outputs over the illustration above. Do not fake support for missing tools. If any command unavailable, report and choose the narrowest safe local fallback while preserving specs.

## 7. Quality workflow — must execute and show evidence

Phase A: assets + mascot rig audit; audio sync gate; contact-sheet review of original + design sketches of three hero shots (SC01, SC09, SC12).

Phase B: **style calibration**. Build still frames for SC01, SC09 and SC12 at 1080×1920 using the real mascot model, real logo and pale ice backdrop. Compare scale, shadow, typography, colors, depth. If any looks like a low-effort AI template, revise before building the remaining scenes.

Phase C: complete all 15 compositions. Construct objects with actual 3D relationships and purposeful transitions. Preserve continuity ledger. Export review snapshots at first frame, every hero action, cut handoff, peak, and end.

Phase D: inspect and iterate. If HyperFrames available: lint, check and snapshot commands in the installed version; correct all legitimate errors. Repeat screenshots in shuffled request order and diff pixels for seek determinism. Check overlapping caption/logo, frames 0–15, scene boundaries, mascot model quality, prop contacts and transitions.

Phase E: build **draft full assembled preview** with final VO (no music). **STOP and ask user to approve this preview before high-quality final render**, per established production gate.

Phase F: after approval only, render `ai_engineer_2026_aipreneur_final.mp4` H.264 1080×1920 30fps AAC, verify ffprobe duration/audio streams, no all-black frames, no 9:16 stretch, no dropped mascot textures, voice audible through last syllable, logo crisp at 100% and final frame still. Inspect representative frames from the **exported MP4** not just source HTML. Report verified render path and warnings honestly.

## 8. Deliverables and your initial response

From Claude Code, create:

- Editable project and scene files.
- `production/character_asset_audit.md` with *actual* mascot path/rig findings.
- `production/transcript_review.md` with verified timing and uncertain words.
- `production/scene_map.json` 15 scenes with actual starts/ends/apex timestamps.
- `production/continuity_ledger.md` for physical object/camera continuity.
- Lookdev PNGs, preview MP4, QA report and final MP4 only **after approval**.

When you start, confirm (a) input asset paths, (b) whether the existing mascot was found and its format, (c) whether final VO audio was found, (d) installed render tools, (e) intended output folder. Then execute production gates. Do not stop after restating this brief or merely writing suggestions.

**Creative North Star:** A world-class motion design studio teaching AI Engineering through one surprisingly satisfying, handmade-looking 3D machine build. The viewer should understand a technical concept at each visual action. Restraint + mechanical causality + coherent camera travel are what make this feel expensive.
