# CLAUDE CODE — EXECUTION PROMPT: THE SCREENSHOT COMES ALIVE

## Your mission

Act as an elite motion design director, creative editor, 2.5D compositing artist, and code-based animation engineer. Implement a real, polished **40.0-second, 9:16, 1080x1920, 30 fps Indonesian Instagram Reel** inside the **existing Claude Code project**. The creative premise: a real static Claude Code screenshot transforms into a premium multi-layer motion graphic. The viewer must immediately see proof of the visual transformation, then discover **how** layering, cursor-driven transitions, parallax, and VO timing work.

This is a **production task**, not a mood board or a text-only tutorial. Create a 0–6 s playable proof first, perform a serious visual review, then implement and render the full video after the first 6 s look is approved. Use only the supplied genuine real-world UI assets, the user's existing real 3D mascot, and code-driven motion graphics. **Do not generate synthetic AI imagery, counterfeit Claude interfaces, fake commands, invented before/after results, or unrelated stock imagery.**

No generic template-based animation. No repetitive card-flip sequences, no constant zooms, no gratuitous particles or glitch effects. Every transition must visually cause the next action. Keep the design costly, legible, cinematic, modern, and unmistakably hand-directed.

## Work safely in the existing repo

1. Inspect the current repo, animation engine, build scripts, brand/style variables, mascot files or rig, font files, backgrounds, motion references, and export workflow **before editing anything**. The creator has already installed/designed some of these. Never overwrite existing project material, delete unrelated files, or rebuild the entire project from scratch.
2. Prefer the repository's current **HyperFrames + GSAP** production pipeline if present. Adapt to the actually installed engine rather than introducing another stack. All project-specific scene contract and deterministic-timeline rules take precedence over generic animation conventions. If the project uses the provided `12_SCENE_CONTRACT_CLAUDE.md` conventions: use `tl.set` for initial states, paused timelines with deterministic seeking, no `gsap.from`, no `repeat:-1`, no uncontrolled `requestAnimationFrame`, no global selectors, and never mix CSS and GSAP transforms on one node.
3. Read the supplied guidance in `claude_motion_pack/reference_style/` (house style, scene contract, production pipeline, and reference video). Preserve the existing creator's brand palette/fonts as the primary authority. Their genuine orange Claude logo and dark UI screenshots are permitted subject matter even if a reference palette is pale blue. Do not invent a new brand color or typeface; ask only if neither the repo nor references establish one.
4. Implement in a dedicated composition or feature directory. Do not replace previous Reels, do not modify unrelated scenes, and report output locations.

## Real input assets: only use genuine materials

All paths below are relative to `claude_motion_pack/`:

| File | Authentic role | Best usage |
| --- | --- | --- |
| `assets/vo/master_vo.mp3` | **Master audio, 39.549375 s** | Primary narration throughout; never re-generate its words |
| `assets/recording/claude_navigation_raw.mp4` | Original ~35.28 s 1920x1032 screen capture | Real Google → Claude/UI movement, source for genuine live interaction inserts |
| `assets/ui/01_claude_code_session.png` | Real dark Claude Code new-session screenshot | Static “before”, actual UI hero, transforms and reveals |
| `assets/ui/02_claude_logo_3d.png` | Genuine supplied orange 3D Claude logo | Floating centered hero with subtle rotation and physically plausible contact shadow |
| `assets/ui/03_claude_code_sidebar.png` | Genuine Claude Code sidebar cutout | Panel extraction/depth rig |
| `assets/ui/04_claude_chat_home.png` | Genuine Claude web/chat landing screenshot | Secondary interface context; do not confuse with Claude Code |
| `assets/ui/05_claude_chat_sidebar.png` | Genuine Claude/chat sidebar cutout | Optional split between Claude and Claude Code |
| `assets/ui/06_google_claude_result.png` | Genuine Google search result | Discovery/search opening |
| `assets/ui/07_google_claude_code_query.png` | Genuine Google query screenshot | Search-to-product match cut |
| `assets/ui/08_google_search_bar.png` | Genuine search bar fragment | Cursor/search bar visual bridge |
| `assets/ui/09_cursor_pointer.png` | Genuine hand cursor graphic | Core edit transition object; high-speed match cuts |

**Mascot:** the user's real 3D mascot, logo, background, and brand fonts already exist in the project, so find and reuse those local files rather than making a replacement. If the mascot is a flat PNG, animate the whole cutout in 2.5D; do **not** pretend individual limbs can be rigged. Keep its cameo brief (two intentional beats maximum). The Claude 3D icon may contain red/yellow stray pixels near its transparent boundary: inspect the asset at 100%; remove stray edge artifacts with non-destructive alpha matting/masking only. Preserve the original shape, material, logo, and orange color.

Never print passwords, cookies, tokens, account metadata, or sensitive project strings in the output or screenshots. If any are visible in source, mask just those areas consistently; do not recreate a fake UI.

## Audio-led timeline is mandatory

- First verify the MP3 duration with `ffprobe`; do not assume the previous draft is verbatim.
- Convert a **copy** to mono WAV at 16 kHz if needed, then use available local transcription/alignment tooling (the project's HyperFrames CLI may provide `npx hyperframes transcribe ... --model large-v3 --language id --json`). Review Indonesian words against `VOICEOVER_TRANSCRIPT_REFERENCE.md` and the source recording. **The MP3 is the single source of truth.** Never claim word-accurate timings from a plain silencedetect log.
- Pause anchors from the actual uploaded audio are supplied in `VOICEOVER_TRANSCRIPT_REFERENCE.md`. They are approximate markers to inspect, not definitive cuts.
- Build a word-synced `transcript_review.md` and an SRT or equivalent caption source before animation. If reliable transcription is unavailable, use the draft as a manually reviewed guide and verify each phrase against the audio in a waveform playback; clearly report any unresolved words.
- Do not speed up, slow down, trim off the last syllable, revoice, or repeat the VO. Extend the finished hold to an even **40.000 s = 1200 frames** at 30 fps, leaving about 0.45 s after the recorded narration.
- Keep captions short, selective and timed with actual words. Avoid a redundant giant subtitle covering the motion. Maintain caption-safe top/center zones and UI button-safe bottom margins.

## The aesthetic / motion direction

**World:** premium editorial 2.5D. Real screenshots become tangible textured interface planes. A cursor acts like a physical editing tool that cuts through layers, causing panels to extrude, arc and realign. Familiar on-screen graphics are treated like live photographed objects: perspective, contact shadow, glossy edge highlights, controlled light falloff, subtle film grain, and believable camera movement. Let the user recognize genuine Claude Code before transforming it. Use clean mask reveals, object continuity, track-matte portals, Y-axis spatial folding, selective motion blur only on very fast movement, and deliberate depth-of-field on background planes (never on readable UI). Use no more than one hero visual per beat.

**Hierarchy:** 1 hero object at a time; 2-3 depth planes behind/around it; small truthful annotation typography, only where needed. All typography crisp and readable on a phone, no thin 8-pixel UI screenshots as the main text. Use the established background/font/colors from the existing project. Orange Claude icon is a meaningful subject accent, not a replacement for the brand palette.

**Motion grammar:** every 0.5–0.9 s a purposeful micro-action; at least every 2–3 s a change in visual idea, scale, shot grammar, or camera axis. Limit one visual spectacle per spoken idea. Make the first 0.3 s visually arresting while preserving the authentic UI. Favor strong cuts and object match cuts; do not fade to black. Each scene must present meaningful motion from its very first frame and maintain frame continuity into the next scene.

**Audio:** prominent, clear spoken voice; music very low (if license-cleared music exists in the repo), light SFX only at meaningful transitions: 1 search/click, 1 split/shatter-by-layer, 1 cursor slice, 1 depth push, 1 reveal, 1 CTA tap. Do not mask consonants with a loud whoosh; no artificial narration or loud intro stinger.

## Detailed shot-by-shot director's storyboard

The timestamps below are **initial scene-boundary estimates** derived from listening/pause inspection, not word-verified. After transcription, adjust boundaries to naturally fall between spoken phrases, while retaining the complete 40 s arc. Cut on the beat or a verified silence; never split a word.

### S01 — 00:00–00:03.40 — THE PAYOFF FIRST / THUMB-STOP

- **VO target:** “Screenshot Claude Code bisa jadi video sekeren ini?”
- **On screen:** Start on a tight, high-quality depth-filled *finished* Claude Code screenshot composition (built from the same assets, not a fictitious result). The 3D Claude icon feels like a physical badge. A huge sharp cursor interrupts the depth stack, and the layers snap into a clean real UI screenshot for an instant, telling viewers this elaborate scene originated as a screenshot. The actual screenshot's recognizability must appear within the first second.
- **Animation sequence:** first 0.3 s establish an impossible-looking 3D stack; 0.3–1.3 s camera rapidly dolly-pulls to reveal source UI; 1.3–2.4 s cursor sweeps the composition, generating three actual separable interface planes; 2.4–3.4 s hold enough to read the promise and match-cut into the original screenshot.
- **Graphics:** restrained top typography: “CUMA SCREENSHOT?” or verified VO words; high-contrast UI and natural shadows. No huge decorative elements.
- **Transition:** cursor movement match-cuts to a cursor resting on the actual unedited screenshot in S02.

### S02 — 00:03.40–00:05.63 — THE UNEDITED BEFORE

- **VO:** “Awalnya, ini cuma tampilan biasa.”
- **On screen:** `01_claude_code_session.png` at high fidelity in a calm, framed vertical layout, with a small “BEFORE” label outside the actual UI. Use a controlled camera float rather than pretending it is recorded footage.
- **Animation:** single understated push; the 3D treatment vanishes for contrast. A thin orange cursor outline taps a real visible element.
- **Transition:** the panel boundary at that tap becomes the live geometric separation line for S03.

### S03 — 00:05.63–00:08.00 — FIRST REAL EXTRACTION

- **VO target:** “Tapi coba lihat ketika logo ...”
- **On screen:** Genuine Claude icon rises from the screenshot into its authentic user-supplied `02_claude_logo_3d.png` physical form. Preserve real photo/source transparency and edge fidelity. One genuine mascot cameo can react to the layer lift for less than 0.9 s if the rig supports it.
- **Animation:** realistic scale, rotation no more than ~12°, layered shadows and rear-plate parallax, not a generic bouncing logo.
- **Transition:** logo rotates 90° around its vertical axis, becoming an interface divider in S04.

### S04 — 00:08.00–00:10.87 — LOGO / PANEL / CURSOR = DEPTH PLANES

- **VO target:** “... panel, dan cursor kita pisahkan jadi beberapa layer.”
- **On screen:** An exploded-view composition: 3D logo front plane, the `03_claude_code_sidebar.png` at middle depth, screenshot back plate, and `09_cursor_pointer.png` physically positioned in front. All use exact user assets, not retyped UI.
- **Animation:** move between plane positions with synchronized three-point perspective motion; 0.5 s quiet lock at apex so the visual is understood.
- **Transition:** the foreground cursor pierces an outline around the middle panel to launch S05.

### S05 — 00:10.87–00:14.70 — CLAUDE CODE AS THE MOTION WORKSPACE

- **VO:** “Di Claude Code, setiap elemen bisa kita atur gerakannya.”
- **On screen:** Back to *real* Claude Code screen recording or the supplied genuine new-session screenshot. Frame the entire real interface as a tilted glass screen; bring three narrow real overlay snippets out from it labeled with VO-aligned motion concepts (e.g. “CURSOR”, “PANEL”, “TIMING”). Only the overlay labels may be newly drawn; do not pretend overlays are native Claude Code controls.
- **Animation:** animate small transform gizmos around extracted planes, move the real assets with exact scripted keyframes, and show the believable result in a second viewport.
- **Transition:** the actual cursor accelerates across the frame, executing the next cut.

### S06 — 00:14.70–00:16.43 — CURSOR CAUSES THE CUT

- **VO target:** “Cursor memicu transisi ...”
- **On screen:** Hero is the authentic pixel-style `09_cursor_pointer.png`, zoomed for impact but with nearest-neighbor or crisp pixel-safe resampling. One genuine real UI boundary is cut by the pointer and cleanly peeled back as a track-matte portal.
- **Animation:** rapid cursor acceleration, crisp one-frame contact, then physically coherent masked pull; no arbitrary flash/strobe.
- **Transition:** the cut edge turns into the leading edge of a perspective panel moving in S07.

### S07 — 00:16.43–00:19.00 — CAMERA DRIVES PANEL PARALLAX

- **VO target:** “... panel bergerak mengikuti kamera ...”
- **On screen:** Genuine screenshot planes orbit subtly in 3D, one foreground sidebar and one back screenshot. Camera passes along the edge, revealing realistic thickness/shadow; the readable content remains in focus.
- **Animation:** shoulder-height dolly-through, controlled rotation; small light sweep across card edges. No infinite floating.
- **Transition:** camera lands on a large typographic baseline which continues in S08.

### S08 — 00:19.00–00:21.13 — TYPE SYNCS TO WORDS

- **VO target:** “... dan teks muncul tepat mengikuti suara.”
- **On screen:** 3–5 *actual verified words from the spoken recording* animate one at a time in an editorial kinetic type treatment over a real Claude Code screenshot crop. Each word hits when its word begins; the camera follows the text, then centers the whole expression.
- **Animation:** tight character reveals, modest scale response, exact audio onset. Not random typewriter simulation.
- **Transition:** lines of type compress into a horizontal ruler / timeline track in S09.

### S09 — 00:21.13–00:23.70 — WHY IT FEELS EXPENSIVE

- **VO:** “Nah, ini yang bikin motion terlihat lebih mahal.”
- **On screen:** A clear side-by-side composition of the *same* supplied genuine screenshot: left flat and right staged with real depth. Use a precise camera axis and shadow to emphasize the difference, rather than adding gratuitous elements.
- **Animation:** split divider tracks across the screen, revealing the meaningful effect. End on the polished half.
- **Transition:** the divider deconstructs into three clean connected timelines in S10.

### S10 — 00:23.70–00:26.30 — MORE EFFECTS IS NOT THE SOLUTION

- **VO target:** “Bukan efek yang ditumpuk sebanyak mungkin ...”
- **On screen:** Briefly illustrate three cluttering graphic fragments crowding the **same** screenshot, then have them rapidly collapse, leaving one beautiful and legible intentional action. This is a quick controlled contrast (under 0.8 s of clutter), not a long intentionally ugly scene.
- **Animation:** fragments slide on meaningful axes; remove them via a crisp reverse mask and leave a refined three-part interface rig.
- **Transition:** remaining three parts become the TIMING / DEPTH / TRANSITION connections.

### S11 — 00:26.30–00:29.70 — TIMING × DEPTH × TRANSITIONS

- **VO target:** “... tapi timing, kedalaman, dan transisi yang saling terhubung.”
- **On screen:** A physically arranged triptych: a small timeline ruler (timing), layered real screenshot planes (depth), and the real pointer connecting them (transition). Active elements respond sequentially to the exact verified words. Use only VO-supported labels.
- **Animation:** three stages link as one cause-and-effect motion; visual apex is a clean portal opening to the final comparison.
- **Transition:** match the portal aperture to a vertical before/after divider.

### S12 — 00:29.70–00:31.80 — AUDIENCE GETS A COMPARISON PROMISE

- **VO:** “Sekarang coba bandingkan hasilnya.”
- **On screen:** Two equal authentic windows on an elegant neutral plate: left pristine original; right the actual completed motion treatment from earlier scenes. Focus on readability and continuity; no unsubstantiated claims.
- **Animation:** pause for visual anticipation, then a crisp slider drag driven by the actual pointer.
- **Transition:** motion follows the slider exactly into S13.

### S13 — 00:31.80–00:35.47 — THE TRUE BEFORE / AFTER PAYOFF

- **VO:** “Dari layar yang tadinya diam, jadi animasi yang jauh lebih hidup.”
- **On screen:** The strongest genuine before/after in the entire film. Left must remain the exact authentic `01_claude_code_session.png`, and right must be an actual instance of this same editor-composed motion design. Show the actual layered panels and 3D logo, not a generated hero image. A subtle mascot cameo may guide attention to the moving side, if available.
- **Animation:** pointer drags slider smoothly over ~1.5 s, then the camera pushes into the animated side, culminating in the hero image from S01. Make this loop feel intentional.
- **Transition:** right-side camera movement resolves as a single graphical speech bubble/comment-card shape for S14.

### S14 — 00:35.47–00:40.00 — EARNED CTA AND LOGO LOCKUP

- **VO:** “Kalau lo mau prompt dan breakdown cara bikinnya, komen MOTION.”
- **On screen:** Brand-consistent refined end card over a very subtle real interface echo. One strong line: “KOMEN MOTION” (only if the recording says those words), plus a small one-line resource promise. Use the creator's real logo / mascot found in the existing project, not an invented logo. Avoid counterfeit Instagram comment UI or misleading fake engagement numbers.
- **Animation:** cursor taps the speech bubble once; “MOTION” locks with a precise physical settle; final logo frame remains completely still for the last ~0.45 seconds after narration ends. SFX should never mask “MOTION”.

## Practical production workflow — execute these gates

**Gate A: source audit / truthfulness.** List all files, show which assets actually exist, inspect the recording for a clean Google→Claude excerpt, extract a representative frame sheet, confirm the native image dimensions/alpha, document the project mascot/background/fonts, and check for sensitive UI strings. The landscape recording may be placed as a **crisp framed wide screen within a vertical composition**; do not upscale a 16:9 UI crop until letters become pixelated. Prefer strategic enlarged callout crops and genuine screenshots at native detail.

**Gate B: audio lock.** Measure the VO, make a reviewed transcript, map word starts, and create an exact 40.0 s/1200-frame composition. Source screenshots stay unaltered as content even though their plates can be cut, masked, tilted and composited. Audio drives cuts, not the other way around.

**Gate C: actual 0–6 s proof.** Render a **playable high-quality 0–6 s MP4** showing S01, S02, and the start of S03. Do not stop at a storyboard. Inspect at least frames 0, 8, 20, 45, 75, 100, 130, 170 and the last preview frame. Ask the creator to approve the look before committing to final assembly.

**Gate D: full build and active art direction.** Implement and connect all 14 shots using existing project code practices. Cross-check the real uploaded `reference_style/ref_H_house_style_aipreneur_v3.mp4` for design finish and hierarchy, but **do not copy its visuals**. Do at least two visual QA passes: check image crop and alpha artifacts at 100%, typography readability at actual phone size, safe areas, visual continuity, and whether the motion feels motivated and non-repetitive. Explicitly inspect transitions and the final 10 s.

**Gate E: technical validation.** Where HyperFrames is available, run `npx hyperframes lint` and `npx hyperframes check`, inspect snapshots at every scene start/midpoint/exit, correct real warnings/errors and test deterministic seeks. Use the project's working render command (likely `npx hyperframes render --quality delivery --fps 30 -o out/claude_code_motion_reel_01_final.mp4`). Ensure the **rendered output**, not only the editor preview, is inspected. Verify output with `ffprobe`: **1080x1920**, **30 fps**, **1200 frames or exact 40 s**, **H.264 + AAC**, VO present through the last spoken word. Use `blackdetect` to catch missing frames. Make sure no cut or caption covers any visible sensitive detail.

**Quality bar:** Genuine text and logo sharpness on mobile; no blurry upscaled UI, halos, corrupted alpha edges, black gaps, random flashes, clipping/warping of real brand interfaces, phantom cursor, drifting subtitles, unnatural easing, or generic template motion. At least 3 standout transitions (cursor-to-panel mask, depth-layer orbit, true before/after slider) should be visibly distinctive and confidently art-directed. Do **not** invent measurable views or promise 10K views.

## Deliverables and reporting

1. `preview_00_06.mp4`: playable 6 s proof for user approval.
2. `claude_code_motion_reel_01_final.mp4`: full high-quality vertical video after look approval.
3. `storyboard_final.md`: corrected shot boundaries and actual quoted/verified VO phrase per scene.
4. `transcript_review.md` and timed caption/SRT source.
5. `contact_sheet_review.png` showing first frame, hook apex, each scene midpoint, comparison, CTA and last frame.
6. Brief QA report with actual frame count, resolution, codec, audio sync, and any unresolved issue.

**First action now:** Inspect my existing project, identify the authentic imported files, read the reference style, transcribe/alignment-check the VO, then build and render the 0–6-second visual proof. Return the proof and what you changed. Do not claim the full 40-second video is done until the final MP4 is genuinely rendered and inspected.
