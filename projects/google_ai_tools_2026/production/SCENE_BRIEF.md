# SCENE BUILD BRIEF — Google AI Tools 2026 (REF-H Ice-Ivory Illustrated Diorama)

Project root: `projects/google_ai_tools_2026/` (1080x1920, 30 fps, total 49.5667 s = 1487 frames). The host `index.html` already renders the background plate, the word-synced top caption (top 232 px, ~1-2 lines, ends around y 350) and the voice-over. Each scene is ONE sub-composition `compositions/sNN.html` mounted at the global start below. The current scene files are untouched copies of the house template (placeholder card) — replace the hero with the real illustration.

## Reference material (read before building)
- House style bible: `deliverables/HyperFrame_PremiumMotion_V3/source_docs/11_HOUSE_STYLE_BIBLE.md`
- Approved example build (study the scene code for technique, lighting, materials, FX): `deliverables/HyperFrame_PremiumMotion_V3/house_style_kit/example_aipreneur_v3/compositions/s01.html … s15.html`
- Golden frames = the quality bar: `deliverables/HyperFrame_PremiumMotion_V3/golden_frames/*.jpg` (look at several)
- Scene template (already copied into every sNN.html): `deliverables/HyperFrame_PremiumMotion_V3/house_style_kit/starter/compositions/_scene_template.html`

## Mascot: NOT used in this video (user decision). Background music: none.

## Fonts available
Montserrat 400/700/900 (loaded by the host via @font-face). Inter is installed system-wide. IBM Plex Mono is NOT available: use Montserrat 700 with letter-spacing for tiny technical labels.

## Real footage stills (documentary evidence — the ONLY product UI allowed on screen)
All in `assets/footage/` (reference them from a scene as `assets/footage/<file>` — paths are relative to the project root). They are single frames of the user's own screen recordings, cropped and lightly sharpened; provenance in `production/footage_provenance.json`. Never draw fake UI to imitate them; never add a watermark or browser chrome.
| file | size px | content |
|---|---|---|
| `pom_title.jpg` | 1560x1050 | Pomelli landing: big 'Pomelli' wordmark on dark olive, 'Easily generate on-brand content for your business', decorative product props |
| `pom_campaign.jpg` | 1590x936 | Pomelli campaign page: 'Campaign' heading + 3 real Raveloux creatives (Tailored To Your Moment / Sculpted To Every Curve / Crafted For Special Evenings) + 1 loading card |
| `pom_brief.jpg` | 564x792 | Pomelli campaign brief panel: 'Bespoke Elegance Tailored to Your Story' + description + 3 image thumbnails |
| `pom_card1.jpg` | 580x948 | Raveloux creative: 'Tailored To Your Moment' (atelier, mannequin, red fabric) |
| `pom_card2.jpg` | 580x948 | Raveloux creative: 'SCULPTED TO EVERY CURVE' (woman in ivory satin gown) |
| `pom_card3.jpg` | 580x948 | Raveloux creative: 'Crafted For Special Evenings' (three women in blush feather gowns) |
| `stitch_prompt.jpg` | 1419x930 | Stitch landing: 'Design at the speed of AI' + prompt box with the real typed prompt (recipe/cocktail app, moody speakeasy aesthetic) |
| `stitch_screens.jpg` | 1460x728 | Stitch canvas: 4 generated mobile screens of 'The Velvet Cask' (The Cellar, The Parlour, The Matchmaker, The Alchemist) with their titles |
| `stitch_s1.jpg` | 638x1368 | single generated screen: The Cellar – Bar Cart Inventory |
| `stitch_s2.jpg` | 642x1368 | single generated screen: The Parlour – Matched Discovery |
| `stitch_s3.jpg` | 638x1368 | single generated screen: The Matchmaker – Bottle Combiner |
| `stitch_live.jpg` | 700x1540 | single generated screen: The Alchemist Ritual – Live Mixing Mode (interactive step timer UI) |
| `web_hero.jpg` | 1320x935 | AIpreneur website (marketing.aipreneur.co.id) hero: nav, headline 'Bangun Sistem Konten Berbasis AI…', video thumbnail 'AI MARKETING FOR BUSINESS' — an ILLUSTRATIVE business website |
| `anti_hero.jpg` | 1520x720 | Google Antigravity landing hero (white): 'Experience liftoff with the next-gen agent platform', Download button, particle field |
| `anti_wordmark.jpg` | 1920x612 | Google Antigravity landing footer: giant 'Antigravity' wordmark on white |

## Scene timing (VERIFIED from the VO — use these, not the provisional times in the table further down)
Local time 0 = the scene's own start. APEX = the key action, which must land on the given word (±0.05 s). `DUR` in the scene script must equal the slot duration.

- **s01** global start 0.0 s, DUR 2.6 s — "Google punya lima AI tools viral."
  - word starts (local s): Google 0.08, punya 0.52, lima 0.92, AI 1.31, tools 1.65, viral. 1.94
- **s02** global start 2.6 s, DUR 1.9667 s — "Tapi dua sedang dipensiunkan."
  - word starts (local s): Tapi 0.17, dua 0.61, sedang 0.81, dipensiunkan. 1.15
- **s03** global start 4.5667 s, DUR 2.6333 s — "Yang masih layak kamu coba sekarang ada tiga."
  - word starts (local s): Yang 0.05, masih 0.21, layak 0.50, kamu 0.82, coba 1.04, sekarang 1.35, ada 1.74, tiga. 2.04
- **s04** global start 7.2 s, DUR 1.5667 s — "Pertama, Pomelli."
  - word starts (local s): Pertama, 0.21, Pomelli. 0.79
- **s05** global start 8.7667 s, DUR 3.7333 s — "Tempel website bisnismu, dia bisa membaca identitas brand kamu."
  - word starts (local s): Tempel 0.19, website 0.50, bisnismu, 0.84, dia 1.59, bisa 1.76, membaca 2.01, identitas 2.43, brand 3.00, kamu. 3.27
- **s06** global start 12.5 s, DUR 3.9 s — "Lalu membantu bikin materi promosi dengan tampilan yang konsisten."
  - word starts (local s): Lalu 0.11, membantu 0.50, bikin 0.95, materi 1.14, promosi 1.61, dengan 2.20, tampilan 2.41, yang 3.02, konsisten. 3.19
- **s07** global start 16.4 s, DUR 1.4667 s — "Kedua, Stitch."
  - word starts (local s): Kedua, 0.19, Stitch. 0.69
- **s08** global start 17.8667 s, DUR 3.3666 s — "Tulis ide aplikasi, desain layarnya langsung disusun."
  - word starts (local s): Tulis 0.21, ide 0.47, aplikasi, 0.88, desain 1.44, layarnya 1.96, langsung 2.44, disusun. 2.67
- **s09** global start 21.2333 s, DUR 2.8667 s — "Bahkan bisa dijadikan prototipe yang bisa diklik."
  - word starts (local s): Bahkan 0.07, bisa 0.45, dijadikan 0.72, prototipe 1.17, yang 1.82, bisa 2.03, diklik. 2.25
- **s10** global start 24.1 s, DUR 1.9667 s — "Ketiga, Antigravity."
  - word starts (local s): Ketiga, 0.26, Antigravity. 0.86
- **s11** global start 26.0667 s, DUR 4.5 s — "AI agent bisa bantu coding lewat editor, terminal, sampai browser."
  - word starts (local s): AI 0.22, agent 0.50, bisa 0.88, bantu 1.11, coding 1.50, lewat 1.99, editor, 2.22, terminal, 2.80, sampai 3.53, browser. 3.94
- **s12** global start 30.5667 s, DUR 3.1666 s — "Nah, ini bagian yang sering orang lewatkan."
  - word starts (local s): Nah, 0.14, ini 0.57, bagian 0.99, yang 1.35, sering 1.59, orang 1.91, lewatkan. 2.43
- **s13** global start 33.7333 s, DUR 4.1 s — "Mixboard sudah ditutup sejak 28 September 2026."
  - word starts (local s): Mixboard 0.06, sudah 0.31, ditutup 0.64, sejak 1.14, 28 1.52, September 2.20, 2026. 2.78
- **s14** global start 37.8333 s, DUR 4.3667 s — "Opal juga dijadwalkan berhenti tanggal 17 November 2026."
  - word starts (local s): Opal 0.20, juga 0.57, dijadwalkan 0.89, berhenti 1.41, tanggal 1.85, 17 2.17, November 2.65, 2026. 3.20
- **s15** global start 42.2 s, DUR 3.2667 s — "Jadi, jangan asal simpan daftar AI yang sudah lama."
  - word starts (local s): Jadi, 0.11, jangan 0.62, asal 0.90, simpan 1.17, daftar 1.59, AI 1.88, yang 2.17, sudah 2.41, lama. 2.67
- **s16** global start 45.4667 s, DUR 3.0333 s — "Mau link tiga tools yang masih aktif, plus contoh promptnya?"
  - word starts (local s): Mau 0.13, link 0.39, tiga 0.55, tools 0.82, yang 0.97, masih 1.24, aktif, 1.52, plus 1.86, contoh 2.10, promptnya? 2.42
- **s17** global start 48.5 s, DUR 1.0667 s — "Komen GOOGLE."
  - word starts (local s): Komen 0.19, GOOGLE. 0.47

## Narrative continuity (17 scenes, one hero metaphor per spoken phrase)
S01 five AI cartridges orbit a hub → S02 two are ejected/retired (graphite, never red) → S03 three remain on a turntable → S04 Pomelli scanner lens → S05 website console scanned for brand identity → S06 real Raveloux campaign on an easel → S07 Stitch needle/drafting desk → S08 design machine with the 4 real generated screens → S09 one screen on a porcelain phone, clicked → S10 Antigravity portal → S11 conceptual workstation (editor/terminal/browser) → S12 archive vault reveals two forgotten tiles → S13 Mixboard drawer CLOSED (past) → S14 Opal calendar SCHEDULED (future, not yet closed) → S15 binder: old list slides away, 3 keeper chips stay → S16 resource box with 3 tool plaques + prompt sheet → S17 comment bubble settles into the genuine AI PRENEUR logo on a porcelain plate.

## Original scene table from the client brief (visual intent; times provisional)
[SCENE TABLE — PROVISIONAL TIMES, RE-ALIGN FROM ACTUAL VO TRANSCRIPT]
The times below are illustrative edit points, NOT fabricated transcript verification. Start/end MUST be corrected to word boundaries by the transcription gate. Duration coverage target = 49.5667s, no gaps. Every scene begins visually populated. Every caption is one short phrase of ACTUAL spoken words only. APEX lands exactly on the indicated spoken anchor within ±0.05 s. The time of the apex is the WORD timestamp obtained by Claude, not a made-up absolute number.

S01 | 0.00–2.71 | "Google punya lima AI tools viral." | Hero: 5 dense porcelain/nickel AI cartridges orbit a large illuminated Google-inspired neutral five-slot hub (avoid unauthorized Google logo reconstruction), 55 tiny circuit etchings, engraved grooves, micro-LEDs, shadowed slots. | Kinetic reveal 5 by 5; camera dives through ring, APEX on "lima"; match-cut into S02. | Top words: "Google punya lima AI tools viral."

S02 | 2.71–4.45 | "Tapi dua sedang dipensiunkan." | Same five cartridges; exactly 2 lift out of sockets, swap to matte pale graphite inactive seals (NO forbidden bright red), while 3 stay polished navy. Tiny mechanical springs, eligibility tags, rolling indicator. | Snap + small shockwave on "dua"; 2 motion trails spiral offscreen, carry three chips to S03. | "Tapi dua sedang dipensiunkan."

S03 | 4.45–7.24 | "Yang masih layak kamu coba sekarang ada tiga." | Three oversized tiered display columns emerge from a single porcelain turntable; each is sculptural (not flat cards), with detailed bolts, optical highlights, inset glass. Each receives Pomelli/Stitch/Antigravity abstract accent symbol. | 5-to-3 transformation, depth shift, APEX on "tiga"; whip/zoom through left column for S04. | Phrase word-synced.

S04 | 7.24–8.69 | "Pertama, Pomelli." | Giant porcelain/ice magnifying scanner, inner navy ring, restrained PROMINENT authentic UI snippet from real Pomelli recording behind glass; 25+ micro-ticks and refracted-edge simulations. | Scanner locks onto real title 'Pomelli'; APEX on "Pomelli"; lens fills screen into S05. | "Pertama, Pomelli."

S05 | 8.69–12.45 | "Tempel website bisnismu, dia bisa membaca identitas brand kamu." | Main hero: HUGE inclined porcelain laptop/website console carrying cropped SHARP 1920x1032 AIpreneur website footage from supplied recording. 3D layers of abstract extracted design tokens orbit scanner (navy/mint tone chips, type samples represented as non-legible shapes). | True footage plane behind glass, UI footage is NOT reconstructed. A URL strip concept enters on "website", scanning bar moves on "membaca", APEX on "identitas". | Spoken top caption only. IMPORTANT: this is illustrative website footage, not evidence of producing the Raveloux Pomelli output in S06.

S06 | 12.45–16.60 | "Lalu membantu bikin materi promosi dengan tampilan yang konsisten." | Main hero: large premium porcelain campaign easel holding ACTUAL Raveloux custom-dress campaign visible inside supplied Pomelli screen recording; editorial layered paper/material slices and 3 coordinated image windows, at least 40 bevel/reflection/micro-layout details. | Transform from design-token scanner to branded campaign editorial plates, center real Raveloux Pomelli recording, APEX on "konsisten"; do not claim this was derived from the AIpreneur URL. | Verbatim caption only; avoid spelling additional fake ad copy.

S07 | 16.60–17.84 | "Kedua, Stitch." | Oversized luminous mechanical needle/blueprint sculptural glyph above navy-enamel drafting desk. Actual Stitch footage is revealed through angled frosted glass; no fake product UI. 30 mini guide marks and rivets. | Needle pierces page on "Stitch" + ripple, aperture transition to S08. | "Kedua, Stitch."

S08 | 17.84–20.93 | "Tulis ide aplikasi, desain layarnya langsung disusun." | A big layered design machine (porcelain drafting plotter + four mechanical glass screen slots) demonstrates ACTUAL supplied Stitch recording for the "Speakeasy Bar Cart Studio" UI; four authentic generated screen compositions are visible as clear real footage crops. | Typed-concept rhythm (caption only must match VO), panels unfold synchronously on "desain layarnya", APEX on "disusun". Do not invent feature demos that are absent from footage. | Verbatim spoken top caption only.

S09 | 20.93–24.36 | "Bahkan bisa dijadikan prototipe yang bisa diklik." | One huge 3D porcelain phone over the existing authentic Stitch design screenshot, distinct physically sculpted cursor/hand pointer. An honest conceptual click ripple highlights one of the REAL screenshot areas; do not imply real site was clicked unless footage shows it. Strong contact shadow and layered foreground arc. | Finger/cursor taps on "diklik" + visual tactile shockwave; scroll into S10. | Spoken words only.

S10 | 24.36–26.00 | "Ketiga, Antigravity." | Huge cinematic white enamel coding portal, giant framing hoop and browser-like glass plane containing ACTUAL Antigravity LANDING PAGE recording. Detailed engraved orbit axes/camera tracking, no dark theme. | Portal aligns at "Antigravity" with flash and crystal highlights; swing through portal to S11. | "Ketiga, Antigravity."

S11 | 26.00–30.72 | "AI agent bisa bantu coding lewat editor, terminal, sampai browser." | One coherent monumental 3D engineering workstation with THREE connected sculptural tools (editor glass plane, terminal ivory command block, browser porcelain viewport); 35–60 micro-details, thin conduits, command tokens represented abstractly rather than legible fake output. Antigravity landing page used as product identity ONLY. | Three optical target rings light up on spoken "editor", "terminal", "browser"; apex on "browser". Crucial honesty: these three panes are conceptual motion illustrations, NOT claimed screenshots of actual agent running. | Top VO words only.

S12 | 30.72–33.78 | "Nah, ini bagian yang sering orang lewatkan." | Massive hinged porcelain checklist vault suddenly cracks open behind camera: three polished tools at front, two dusted/forgotten archival tiles behind. 40 delicate paper folds, rivets, seal marks. | Reveal hidden rear plane on "lewatkan"; visual tempo drops for suspense, then smash cut. | Phrase only.

S13 | 33.78–37.78 | "Mixboard sudah ditutup sejak 28 September 2026." | Large pale-ivory archive drawer with sculpted label "MIXBOARD" (spoken word), a paper date wheel visibly showing "28 SEPTEMBER 2026" (all words/numbers spoken by VO), bronze/grey seals and frosted glass shutting over an icon. | Drawer closes physically on "ditutup" then a clean date stamp lands on "28 September 2026"; cool grey archived, not angry red. | Top caption from exact VO; date only if already spoken.

S14 | 37.78–42.31 | "Opal juga dijadwalkan berhenti tanggal 17 November 2026." | Separate larger porcelain countdown/calendar station with sculpted engraving "OPAL" and flipping tiles "17 NOVEMBER 2026". Two planes: current hand reaching toward calendar and future archive gate (not yet closed). | Set future marker on "dijadwalkan" and "17 November 2026"; distinguish S13 ALREADY CLOSED vs S14 SCHEDULED, not yet shut on production date (04 Nov 2026). APEX on "17 November". | Exact spoken words only.

S15 | 42.31–45.60 | "Jadi, jangan asal simpan daftar AI yang sudah lama." | Huge physical porcelain flip-file binder; outdated paper list sheets mechanically slide away, replaced by three premium dimensional chips. Crisp 3D paper tabs, holes, pins, realistic corner shadows; not a flat text slide. | Old list retracts at "sudah lama"; short synchronized punch on "jangan" or "lama" depending true transcript. | Top spoken caption.

S16 | 45.60–48.35 | "Mau link tiga tools yang masih aktif, plus contoh promptnya?" | Hero: massive pearlescent resource box opens, 3 individual genuine tool identifiers as embossed mini plaques and one abstract folded prompt sheet. 3 raised sections, thin grid ornament, translucent details. Avoid legible invented URLs or prompts. | Three chips fall into resource box; sparkle apex on "contoh promptnya". | Spoken caption only.

S17 | 48.35–49.5667 | "Komen GOOGLE." | Final huge premium 3D phone/comment bubble quickly settles to refined **genuine AI PRENEUR logo lockup** on white porcelain plate (real logo only, original ratio/colors), on soft ice-ivory background. | Short, strong comment bubble punch exactly on "GOOGLE"; then settle fully before end. Last decoded frame must be a calm still full brand lockup, not mid-transition, no fade/black. | "Komen GOOGLE." (only spoken CTA).

Transition continuity: S01 hub→S02 2 ejections→S03 3 remaining; S03 left aperture→S04 Pomelli; S04 lens→S05 website; S05 extraction token swipes→S06 real Raveloux example; S06 clipped editorial edge→S07 Stitch; S07 needle slot→S08 four screens; S08 one screen→S09 clickable concept; S09 click portal→S10 Antigravity; S10 portal expands→S11 workstation; S11 three connection lines→S12 hidden archive; S12 archive drawers→S13 closed Mixboard→S14 upcoming Opal; S14 date flip→S15 outdated binder; S15 three keeper chips→S16 resource; S16 porcelain box→S17 logo.

[FACT & FOOTAGE INTEGRITY]
- Official Google product status as of 2026-11-04: Mixboard closure stated for 2026-09-28 in Google Labs Help (https://support.google.com/labs/answer/16689296?hl=en); Opal discontinuation scheduled for 2026-11-17 in Google for Developers Opal FAQ (https://developers.google.com/opal/faq). Check current status if network permitted; preserve the user's actual narrated phrases even if you need to flag updates for user approval. Never replace "dijadwalkan" with "sudah tutup" in OPAL illustration.
- The recorded AIpreneur homepage is NOT the site used to generate the recorded Raveloux Pomelli campaign. Indicate their relationship only as illustrative: "paste your website" example followed by a **separate real Raveloux campaign** example.
- The recorded Stitch interface and four generated "Speakeasy Bar Cart Studio" UI screens are legitimate footage; use actual crops. Do not alter app screenshots into made-up different app screens.
- The Antigravity recording contains the official LANDING PAGE ONLY. The editor/terminal/browser visuals in S11 must be explicitly conceptual visualization, without fake real log output, fake recorded activity, or misleading UI labels.
- Avoid claims such as guaranteed growth, marketing performance or app functionality that the screen recording does not show.

[HOUSE STYLE LOCK — REF-H, NON-NEGOTIABLE]
- Visual-first: NO big headlines. The only persistent text is a small top caption: centred, top ~232 px, sides >=70 px, Montserrat 700 46px / line-height ~1.22, #202B3B; each word masked and rises yPercent 110→0 over 0.34 s with power4.out at actual word start −0.08 s; keyword navy #294B77 with an ice highlighter. One caption block per scene; prioritize ONE LINE and short, timed chunks of real VO if phrase is long.
- One scene per spoken phrase, hard cuts; each scene = ONE big hero metaphor object (60–75% of visual zone x50–1030 / y400–1520, center y≈900–1000), richly detailed with 20–60 visible micro-elements. It may incorporate actual website footage while remaining a dimensional object. Avoid isolated icon or a small card floating in empty space.
- Materials: glossy porcelain (#FFFEFB→#F4F7FB, subtle navy border, white rim highlight), ivory paper, frosted ice glass (simulated translucency; no fake real refraction), navy enamel (#3A6299→#294B77→#1F3A5F), silver ceramic/chrome rim ticks. Refined high-end illustrated diorama, not photoreal humanoid or generic neon AI glow.
- Lighting: strong soft key from top left, rim highlights upper left, contact shadows down/right (tight dark contact + wide soft shadow when lifted), tasteful local glow only at key beat; clear 3D volume and perspective.
- Depth: at least 3 distinct planes: far blurred ceramic discs/props, hero, near motes/bokeh. Slower background parallax and subtle 1→1.06–1.08 push-in within the scene; CSS perspective around 1200–1600px, preserve-3d where valid.
- Motion: frame 0 visibly contains entering hero; 0.3–0.6s energized entries power3/4.out, tactile back.out(1.4–1.8) pops. On key spoken word ±0.05s run coordinated (a) 0.25s luminous flicker, (b) shockwave 0.4→1.8 scale ~0.6s, (c) 10–16 seeded four-point sparkles, (d) 1.03–1.06 hero scale punch, and (e) settle 0.12–0.35s. Keep meaningful micro-motion continuous, but do not create noise or uncontrolled looping.
- Colors: ink #202B3B, navy #294B77, deeper navy #1C3354, blue #3A6299, ice #ACC6E7/#CBDBF4/#E8F0FB/#FBFCFE, graphite #2E2E2E, warm paper #FFFEFB. Very sparing mint #9FD8C4 and amber #F2C46D. NO red, no neon green, no dark fullscreen, no dark gradients.
- Fonts: Montserrat 400/700/900, Inter 400 for unstyled utility text only, IBM Plex Mono 700 for tiny labels. Do not use random decorative fonts.
- Global BG: approved light pastel plate with a 54px paper grid (1px rgba(41,75,119,.055) radial masked, slow drift), 3 drifting haze blobs, 22 SEED-BASED motes, subtle procedural but deterministic stepping grain. Extend wallpaper with uniform scaling and mirror extension; never stretch it.
- All transitions visible and thematic. Hard cuts between scenes; match shape/camera/prop when possible rather than generic wipe. No full white flash lasting multiple frames. No more than ~0.6s of inactivity except the desired final still brand lockup.
- Last frame: crisp authentic AIpreneur logo, porcelain display plate, visually complete, no fade-to-black or abrupt cut to empty. CTA ONLY because "Komen GOOGLE" is spoken.
- Existing approved REF-H golden frames are the bar. If a scene is flat, has tiny hero, has huge headline, lacks lighting/contact shadow, uses generic floating cards or a dark UI theme, mark VISUAL QA FAIL and rework it regardless of CLI result.

[SCENE CONTRACT — GIVE THIS BLOCK TO EACH BUILDER]
- Write ONLY the assigned `compositions/sNN.html`. Host already renders BG + captions + authoritative voice; no separate background, VO or looping video player inside a scene.
- Structural contract: `<template><style>#root{position:absolute;inset:0;overflow:hidden} ...</style><div id="root" data-composition-id="sNN" data-width="1080" data-height="1920"> ... </div><script>(function(){const R=document.querySelector('[data-composition-id="sNN"]');const tl=gsap.timeline({paused:true}); /* all deterministic animations */ window.__timelines['sNN']=tl;})();</script></template>`. Follow exact installed project template if it differs.
- Namespaced CSS classes, SVG gradient IDs, selectors (prefix `sNN-`). Query DOM inside this scene root only. Timeline starts at 0 local. Register timeline last. Track a summary of the overall 17-scene narrative for continuity.
- Set initial states with `tl.set(..., ..., 0)` FIRST, followed by `tl.to` or `tl.fromTo({immediateRender:false})`. NO `gsap.from`, NO CSS transform and GSAP transform fighting on same target, NO `left/top/width/height` tweens; transform and opacity/filter where feasible.
- No Math.random, clock time, Date.now, timers, rAF, network calls, repeat:-1, auto-play loops, manual `tl.play()`. Use seeded reproducible coordinates. Ensure both forward and backward timeline seeks return identical pixels.
- Perspective on parent and preserve-3d on relevant spatial planes, not on opacity/filter flattened leaf faces. Shadows/contact highlights remain visible through the whole animation.
- No legible text in scene beyond exact spoken VO words, authentic product-identifying labels from actual footage, or dates spoken by VO. Tiny abstract technical UI lines are preferred over invented command messages. The top caption is already drawn globally; don't duplicate as a huge scene title.
- Real cropped MP4/video is handled by installed framework's approved deterministic media layer; do not include uncontrolled `<video>` or `<audio>` inside scene sub-compositions. Place source clips through framework-recognized media clips/host tracks with synchronized local trim and deterministic time; if unsupported, use quality-preserving extracted, time-indexed actual footage frames with explicit provenance. Never add fake screenshot UI.
- Intentional overlaps mark `data-layout-allow-overlap` only where justified. Do not blanket-suppress check warnings.
- Before handoff: inspect snapshots at entering frame, apex, and exit; compare to the approved golden frames. Rework poor lookdev; report scene path, object hierarchy, local apex word/time, any honest limitations.

## Project-specific technical rules (override anything above that conflicts)
- Footage is used as `<img>` stills (deterministic, sharp) inside your 3D objects — no `<video>`/`<audio>` in scenes. Animate them with transform (pan/zoom/scroll inside a masked screen) to feel alive.
- Hero zone: x 50–1030, y 400–1520 (caption above, keep y < 380 clear except the far background). Hero 60–75 % of that zone.
- Genuine logo (S17 only): `assets/brand/ai_preneur_logo_trimmed.png` (1214x168, graphite #2E2E2E on transparent). Set width only (height auto). Never redraw/recolour.
- No Google logo reconstruction (no 4-colour G). The word 'Google' only appears in the global caption.
- Tool names may appear as engraved labels ONLY where the VO says them in that scene or as the genuine footage itself (S16 plaques may reuse small crops of the real footage as identifiers).
- Check your work: from the project root run `npx --yes hyperframes@0.8.186 snapshot --at <global seconds,comma separated>` and LOOK at the PNGs it writes (entry ~0.1 s after scene start, apex, exit ~0.1 s before scene end). Also `npx --yes hyperframes@0.8.186 lint` (the `nested_structure_needs_subcomposition [bg]` warning is expected). Rework until it matches the golden frames' richness.
- Do NOT edit `index.html`, other scenes, timing or assets. Do NOT render, commit or push.