# Prompt-Motion technique catalogue

Distilled from the community gallery at prompt-motion.com (scraped 2026-11-20: 237 entries, 234 with prompt text, 3
empty pages). Every prompt there belongs to its creator; the site lets people use them, but our client wants the
**techniques**, not the prompts. Everything below is a paraphrase in our own words. Credit = the entry link. Never paste
an entry's prompt into a project, and never reuse another creator's product, brand, characters or likeness.

How to read the fit tags:
- **REEL**: works in an AIpreneur reel (1080×1920, Indonesian VO by Dakocan, 3D mascot host, navy/white brand, per-word
  captions). Brand rules in `brand.md` / `client_rules.md` / `voxel_reel.md` always win.
- **LAND**: belongs to landscape launch/promo films (1920×1080 or square), e.g. for SKINKU, Rave Tailor, Raveloux,
  MasterPajak AI, AIpreneur Automation, or the client's site heroes.
- **BOTH**: works in either.

Several of our existing skills already started from entries in this gallery: `/product-launch-film` ([ultimaxbt-2ddf1e](https://prompt-motion.com/ultimaxbt-2ddf1e)),
`/beat-promo-film` ([twoclipping-6dd14e](https://prompt-motion.com/twoclipping-6dd14e)), `/landing-flythrough-3d` ([twoclipping-d89be5](https://prompt-motion.com/twoclipping-d89be5)) and `/business-explainer-30s`
([alex-prompter-1ea044](https://prompt-motion.com/alex-prompter-1ea044)). Use those skills when the brief matches them; use this catalogue to vary and extend them.

## Category counts (each entry counted once, by its main purpose)

| category | entries | what is there |
|---|---|---|
| Product launch films / promos | 86 | SaaS/app launch films, teasers, promos, mostly 15–40 s landscape |
| Showreels (abstract "show me what you can do") | 57 | the viral one-liner and its variants; type, shapes, particles |
| Explainers / diagrams | 25 | business explainers, how-it-works, history, recipes, whiteboard, maths |
| Characters / 3D | 21 | story shorts, mascots, Three.js scenes, pixel art, dance |
| Charts / data | 10 | stock/finance apps, news recaps, timelines, milestones |
| Social / vertical reels | 10 | 9:16 pieces, hype edits, talking-head cut-downs, portrait variants |
| Typography | 8 | spoken-word type films, bumpers, lyric videos |
| UI animation | 7 | morphing-component loops, single-object guided UI films, badge unlock |
| Other | 6 | music machines, viral physics, mood scenes, long stories |
| Logo reveals / brand stings | 4 | logo assemble, anniversary sting, brand reels (plus many end-card logo moves inside launch films) |

A full index of every entry, by category, is at the end of this file.

---

## 1. Product launch films / promos (86)

**What the strong ones do.** 12–30 s, 1920×1080 (some 1080×1080 / 1440×1440 square), 60 fps. One continuous take with
a single camera over one "world" layout; scenes are built out of the previous scene (a button becomes the page, a colour
flood carries the words, a chart point becomes the corner of the next card). The story is an emotional arc, not a feature
list: problem/chaos → control → clarity → brand, with only 3–5 visual ideas and the first product moment inside the first
2 s. UI is rebuilt from the real product (design tokens, real copy, real logo traced to SVG), cut into layers so each
region can move, never a scaled screenshot. Sound is beat-locked music (≈120–130 BPM, drop on the key reveal) with one
quiet SFX per event, placed by its measured peak, mastered to −14 LUFS. Build is one HTML page whose frames are computed from
the clock alone (`seek(t)`), rendered with Playwright + ffmpeg (or Remotion / HyperFrames), with sub-frame motion blur.
QA is a hard gate: stills at fixed timestamps, contact sheets, frame-difference scans, then a fix pass.

Techniques:
- **Stage inside the frame**: a dark rounded "stage" (~80% width) on an atmospheric brand-colour background; every
  oversized move is clipped to the stage, so zooms feel contained and premium. [brainextends-e19ac3](https://prompt-motion.com/brainextends-e19ac3) — BOTH (navy stage on
  the navy plate works for MasterPajak/Automation demos).
- **Persistent anchor element**: one small bar (a player, a progress pill) stays on screen across shots and stitches them
  together; it must stay visually secondary. [brainextends-e19ac3](https://prompt-motion.com/brainextends-e19ac3) — BOTH (for us: a caption bar or "chapter" chip).
- **Hero asset keeps its identity**: the same artwork/object travels search → detail → tile → zoom → logo; position
  relationships are preserved through every hand-off. [brainextends-e19ac3](https://prompt-motion.com/brainextends-e19ac3) — BOTH.
- **Arc in four words**: chaos → control → clarity → brand; ~4 visual ideas in 15 s; "3 extraordinary moments beat 10
  mediocre ones". [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — BOTH (great for MasterPajak: messy receipts → organised books).
- **Object-driven transitions list**: chart line → document edge, number → amount in the next card, gold pill → button,
  camera pushes through a UI element; crossfades/random wipes/spins/glitch banned. [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — BOTH.
- **Self-review checklist at fixed timestamps** (0, 1, 2.5, 4.5 … 14.8 s), then inspect decoded frames from the final
  MP4, not browser screenshots; reject anything that looks like a template. [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — BOTH.
- **No safe audio? Deliver a cue sheet** instead of pulling copyrighted music. [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — BOTH.
- **Shots enter already moving**: exponential ease-out (a fixed fraction of the remaining distance per frame) on entry, an
  accelerating move or a blur ramp on exit, so no cut happens on a still frame. [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — BOTH.
- **Hard cuts two frames before the beat** so the eye lands on the beat. [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — BOTH.
- **Keyframe tables per frame** (`kf(frame, [[f,v]...], ease)`), continuous in frame number so a 60 fps master can be
  rendered from a 30 fps plan; seeded hashes instead of `Math.random`. [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — BOTH.
- **Directional blur by velocity** (separate x/y blur), zoom-smear end card from 20–30 scaled faded copies of the word.
  [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — BOTH.
- **Frosted-glass titles**: giant letters filled with a blurred, lightened copy of the image behind, clipped by the card
  edge. [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — LAND (on reels only for one hero word, brand colours).
- **Cursor with personality**: turns to face where it travels, grows on hover, shrinks on press. [notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a) — BOTH.
- **Composer with iridescent glow → send button becomes the next object** (a wok tossing ingredients), colour flood from
  the object carries the message text, button expands into the page, a route pin becomes the brand mark.
  [ultimaxbt-2ddf1e](https://prompt-motion.com/ultimaxbt-2ddf1e) — LAND (built as `/product-launch-film`).
- **Iris-blade shutter, wordmark squeezed into its own full stop, goo blob → glass toolbar, phone bezel growing out of
  the screen edge, black shape that keeps morphing through order states**. [twoclipping-221cab](https://prompt-motion.com/twoclipping-221cab) — LAND (Raveloux/Rave
  Tailor product films).
- **Real-clip wall + scan line picking 3 winners, 3D carousel with floor reflections, stats on push cuts.**
  [twoclipping-6dd14e](https://prompt-motion.com/twoclipping-6dd14e) — LAND (built as `/beat-promo-film`).
- **Landing page lying on a studio floor, one camera glide with per-pixel depth of field, pieces lifting toward the
  lens.** [twoclipping-d89be5](https://prompt-motion.com/twoclipping-d89be5) — LAND (built as `/landing-flythrough-3d`).
- **VO pipeline with takes**: generate several full takes, regenerate a weak line several times and splice the best,
  shorten long pauses (>~0.28 s → 0.2 s), level phrases toward the median, and align word timings by transcribing each
  pause-split segment separately (one Whisper pass can be up to 0.5 s late). [rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7) — REEL (directly
  improves our Dakocan VO + per-word captions).
- **Captions typed at the exact spoken time; music drop on the "verb" line; images switch on 16th notes with a click
  each; 3-band sidechain ducking so the voice sits ~9 dB over the music in the speech band.** [rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7) — REEL.
- **Liquid glass needs something behind it**: on plain white add a slow pastel aura or a blurred wash of the photo.
  [rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7) — BOTH (white theme: use the bg-light plate + brand-blue aura).
- **Burst of 100+ images that converge into the logo.** [rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7) — BOTH.
- **Build the promo from the site itself**: scrape real tiles/clips, lay the gallery out once in world coordinates, corner
  radius → 0 as a tile reaches full-bleed so pull-backs and whips are exact match cuts, find cut-free loop windows with
  scene detection, stagger loop phases, cursor homes on the live button, reversed whooshes into hits, then a fresh critic
  reviews the render. [antonio-kodheli-490109](https://prompt-motion.com/antonio-kodheli-490109) — BOTH (AIpreneur site/community promos).
- **Slow, polished one-camera desktop**: moves of 1.5–3 s, "half the speed you'd default to", film grain, oversized
  cursor, lowercase copy; a fast-spinning list of ~30 pains (not meant to be read) lands slowly on the one that matters,
  then a "?" pops. [jake11moran-f60e35](https://prompt-motion.com/jake11moran-f60e35) — BOTH (hook: spinning list of AI pains → "…dan kamu masih manual?").
- **Four-to-five-scene story** (why it matters / why it hurts / how it's fixed / what you get), one short title per scene,
  one soft SFX per appearing element and silence otherwise, logo traced to SVG, render → check frames → fix.
  [aschapmann-131210](https://prompt-motion.com/aschapmann-131210) — BOTH.
- **Paper-light canvas with handwritten marker notes** (stroke-dashoffset), abrupt switches between light and dark
  grounds, fresh idea roughly each 1.5–2 s, no animator jargon or timeline chrome on screen, no invented numbers; the prompt is a template with
  `{{PRODUCT}}`-style slots. [ik-builds-b8bdcf](https://prompt-motion.com/ik-builds-b8bdcf) — BOTH (white-theme reels: marker notes in #294b77).
- **Break screenshots into components and icons** so each piece can animate; motion must match music.
  [ho-ba-f3f0e9](https://prompt-motion.com/ho-ba-f3f0e9) — BOTH.
- **Score retimed until every cut/hit lands on a beat or the drop; hook in the first second.** [jhylee95-e1152f](https://prompt-motion.com/jhylee95-e1152f) — BOTH.
- **Only facts on the site**, pacing that accelerates and relaxes as the story needs, product inside browser and phone
  frames. [wani-shola-16ca7a](https://prompt-motion.com/wani-shola-16ca7a) — BOTH.
- **"Research it first" one-liners** (read the landing page/codebase/components, then make the film) consistently
  produce more specific films than generic ones. [fractadev-149adc](https://prompt-motion.com/fractadev-149adc) [ajith-io-c52e09](https://prompt-motion.com/ajith-io-c52e09) — BOTH.

## 2. UI animation (7)

**What they do.** Short (7–15 s) seamless loops, square or 16:9, Dribbble-grade. One object never cuts: a shape morphs
through a sequence of UI states, or a single ball/dot guides the eye from component to component. A scripted cursor makes
every change (real clicks, drags, long-presses). Light warm-grey or near-black canvas, one font, one accent, springs with
tiny overshoot, camera zooms so each state fills the frame, last frame = first frame. 120 BPM, something on every beat.

Techniques:
- **One shape, many states** (button → loader → check → island → player → slider → toggle → tabs → chart → command
  palette → toast → button); content swaps with a short blur inside the morphing container. [demonugc-4c5753](https://prompt-motion.com/demonugc-4c5753)
  [twoclipping-5cba86](https://prompt-motion.com/twoclipping-5cba86) — BOTH (reel idea: "1 tombol, 10 tools AI").
- **Sum-of-springs**: when a value gets retargeted repeatedly, add one closed-form spring per retarget; the result is
  still computable from t alone. Same entries — BOTH (engine rule).
- **Two edges on two springs**: a tab indicator's leading edge outruns the trailing edge so it stretches like liquid.
  Same entries — BOTH.
- **Direct-manipulation drags**: while held, the value follows the cursor; on release it springs back from where it was.
  Same entries — BOTH.
- **Loop seam includes cursor position AND speed**, or the loop stutters. Same entries + [rossaxbt-94583b](https://prompt-motion.com/rossaxbt-94583b) — BOTH.
- **A guide object carries every hand-off** (a ball springs out of a toggle, rides a slider whose value is computed from
  its x, triggers notifications, taps the keys that type the reply). Never teleport; the keys pressed must match the
  text. [rossaxbt-94583b](https://prompt-motion.com/rossaxbt-94583b) — REEL (our mascot/robot can be the "ball").
- **Through-line dot**: one accent dot starts in the UI, becomes the dot on an "i", draws a spring graph (graph and dot
  use the same function), grows into a frame-filling shape, opens into a halftone field and returns to the start.
  [ultimaxbt-bbebf5](https://prompt-motion.com/ultimaxbt-bbebf5) — BOTH (cyan #01ccf7 dot on navy).
- **Badge as a physical 3D object** that tilts toward the cursor, celebratory gold burst, fast and not bouncy; match the
  design file exactly and add only motion. [bthreeagency-b9b8d9](https://prompt-motion.com/bthreeagency-b9b8d9) — REEL (certificate/"lulus kelas" moment; particles in
  brand cyan, not gold).
- **Powers-of-ten zoom**: one dot on black → many windows → zoom out until the desktop is a point in space → zoom back in
  to a phone. [dale-vaz-cc612a](https://prompt-motion.com/dale-vaz-cc612a) — BOTH.

## 3. Explainers / diagrams (25)

**What they do.** 30–90 s; a clear story spine (problem → what it does → how in steps → proof → name), often with
synthesized narration and subtitles. Styles chosen to suit the subject: whiteboard hand-drawing, stop-motion paper,
Manim maths, 3D tours, pixel art. Best ones target a named audience ("someone with zero background", "a first-time
visitor") and pick one concrete example.

Techniques:
- **5-scene business explainer** (problem, what we do, 3 steps, one proof, name). [alex-prompter-1ea044](https://prompt-motion.com/alex-prompter-1ea044) — BOTH (already
  `/business-explainer-30s`).
- **Process-fill visual**: show a process from empty to complete with each ingredient/measurement entering as a labelled
  layer (empty glass → finished cocktail). [ror-fly-9950f1](https://prompt-motion.com/ror-fly-9950f1) [sarut0bisasuke-cefa43](https://prompt-motion.com/sarut0bisasuke-cefa43) — REEL (e.g. "resep prompt": each
  prompt component pours into a glass/jar the mascot holds).
- **One genre per explanation**: each pass at the concept is told in a radically different visual style; self-referential
  and fast. [emollick-8661a8](https://prompt-motion.com/emollick-8661a8) — REEL (e.g. "AI agent dijelaskan 5 gaya").
- **Product explains itself in first person**, hand-drawn stop-motion. [nikolajankovic-ce4ff4](https://prompt-motion.com/nikolajankovic-ce4ff4) — REEL (mascot speaks as
  the tool).
- **Two-pass whiteboard**: first a quick hand-drawn whiteboard animation, then the MP4 with narration added.
  [tak3sh8-be5012](https://prompt-motion.com/tak3sh8-be5012) [lemomo-ai-0d9cff](https://prompt-motion.com/lemomo-ai-0d9cff) — BOTH.
- **User-journey chain**: one example user goes through each step in order (create campaign → connect metrics →
  attribution → voice agent → follow-up → human in the loop → analytics). [charlesmendez-73b6e4](https://prompt-motion.com/charlesmendez-73b6e4) — BOTH (AIpreneur
  Automation demos).
- **Maths/concepts with Manim + free TTS, with a worked example and a question that makes the viewer think.**
  [linearuncle-5d2bae](https://prompt-motion.com/linearuncle-5d2bae) — BOTH.
- **Zero-background audience**: explain what each common command means, in the viewer's language, with sound.
  [yunn260414-60d996](https://prompt-motion.com/yunn260414-60d996) — REEL (Indonesian basics series).
- **Plain canvas, zero dependencies, frames derived from t only**, so any external renderer can capture it.
  [parkerrex-1a54fe](https://prompt-motion.com/parkerrex-1a54fe) — BOTH (engine rule).
- **"Show me what goes on inside X"** as a 3D walk-through of a place. [mdaman010-e7226a](https://prompt-motion.com/mdaman010-e7226a) — BOTH (inside an AI agent / a
  data centre for an AI basics reel).
- **History as a timeline or a pixel-art boomerang** that speeds up to the present and then goes wild.
  [kloss-xyz-fe0c31](https://prompt-motion.com/kloss-xyz-fe0c31) [pluginplay-3d4006](https://prompt-motion.com/pluginplay-3d4006) — REEL.
- **Article → educational video** and **1-minute educational video with synthesized narration from a URL**.
  [henkvaness-0e06af](https://prompt-motion.com/henkvaness-0e06af) [1stnoel-c20a89](https://prompt-motion.com/1stnoel-c20a89) — REEL (turn Freddie's blog/WA-channel posts into reels).

## 4. Charts / data (10)

**What they do.** Numbers are the hero: a hero figure resolves crisply, the chart draws itself, supporting metrics settle
a beat later; data is either real (from the site) or clearly demo-safe. Mono font for figures. Timelines and news recaps
use a list structure with one highlight per item.

Techniques:
- **Hero number resolves, chart draws, secondary metrics settle slightly later** (subtle stagger), mono figures, accent
  only on the active state, green only for a truly positive state, demo-safe values. [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — BOTH.
- **Graph and moving object share one function**: the dot that bounces is literally drawing the spring curve, with a
  "+N%" call-out at the settle. [ultimaxbt-bbebf5](https://prompt-motion.com/ultimaxbt-bbebf5) — BOTH.
- **Chart that draws itself with a hover tooltip**, inside a morph loop. [demonugc-4c5753](https://prompt-motion.com/demonugc-4c5753) — BOTH.
- **Milestone film** (N visitors after N months) — counters + growth line as the story. [viktoroddy-98c1d8](https://prompt-motion.com/viktoroddy-98c1d8) — REEL
  (AIpreneur alumni/member milestones, only with real numbers).
- **News recap from the viewer's point of view**: each item gets the one reason it's interesting, ~60 s.
  [gigabit-million-16b3a0](https://prompt-motion.com/gigabit-million-16b3a0) — REEL ("5 tools AI rilis minggu ini").
- **Long timeline compressed** (decades of history in one film). [triglyceee-bd5b08](https://prompt-motion.com/triglyceee-bd5b08) — REEL.
- **Two deliverables from one edit**: landscape and portrait versions with fast royalty-free music.
  [palashbagchi11-0a4b6b](https://prompt-motion.com/palashbagchi11-0a4b6b) — BOTH.
- **Maths showreel**: equations, curves and geometry as the motion material. [math-files-39c9d0](https://prompt-motion.com/math-files-39c9d0) — LAND.
- Rule from many entries: **no invented %, multipliers, customer names or figures** ([ik-builds-b8bdcf](https://prompt-motion.com/ik-builds-b8bdcf),
  [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4)) — matches our "no invented results for Freddie" rule.

## 5. Showreels (57)

**What they do.** Mostly the viral one-liner ("a dynamic 15-second motion graphics showreel … go all out") or a
translation of it, sometimes pointed at a brand. Typical results: kinetic type, geometric shapes, particles, camera
moves, colour shifts, cut to a self-composed track, 10–20 s, 16:9. The variants that add one or two constraints get
noticeably better results than the bare line.

Techniques (the useful constraints people add):
- **Spell out the energy**: something moves every second, big type, bold colour, real camera moves, no slow fades;
  format/fps given; a single seekable HTML file, Playwright frames + ffmpeg; "don't ask, just build".
  [aichrislee-a6cb42](https://prompt-motion.com/aichrislee-a6cb42) — BOTH.
- **Ban the AI giveaways**: no frames and no text pinned in the corners. [1littlecoder-9fef89](https://prompt-motion.com/1littlecoder-9fef89) [souravbhar871-61f424](https://prompt-motion.com/souravbhar871-61f424) —
  REEL (keep our logo/chip system, but no extra corner HUD text).
- **Structure for a reel**: striking hook in the first second → a run of distinct techniques (type, shape play, camera,
  colour shifts) → one clean memorable final frame; cut as if to music. [reflex-cloud-72ffe5](https://prompt-motion.com/reflex-cloud-72ffe5) — REEL.
- **Name the technique palette** (kinetic type, 2D/3D, abstract geometry, fluids, particles, distortion, masking,
  lighting, depth, seamless camera) but demand it feels art-directed, not a random effects pile. [lukasersil-0ed38e](https://prompt-motion.com/lukasersil-0ed38e) —
  BOTH.
- **Self-critique loop**: look up current motion/sound trends, question the plan, start over if it doesn't feel pro.
  [heyiammallik-e72d17](https://prompt-motion.com/heyiammallik-e72d17) — BOTH.
- **A concept instead of a product** ("overthinking", life cycle that loops, hypnotic), or a print style keyword
  (risograph, oscilloscope). [gizakdag-cf4ae6](https://prompt-motion.com/gizakdag-cf4ae6) [loicrambo-ad6830](https://prompt-motion.com/loicrambo-ad6830) [monokern-ade5b6](https://prompt-motion.com/monokern-ade5b6) [rneayan-474bcf](https://prompt-motion.com/rneayan-474bcf)
  [rneayan-ea6129](https://prompt-motion.com/rneayan-ea6129) — REEL (a style keyword per series gives each AIpreneur series its own look inside brand colours).
- **Music "inspired by" a famous theme but composed from scratch**. [ajith-io-4c248f](https://prompt-motion.com/ajith-io-4c248f) — BOTH (never use the original).
- **All graphics from scratch as a niche agency would**. [jacksonfall-54b2ac](https://prompt-motion.com/jacksonfall-54b2ac) — LAND.
- **Anti-reference**: a deliberately terrible showreel, useful as a checklist of what not to do. [henkpoley-3d3407](https://prompt-motion.com/henkpoley-3d3407).

## 6. Characters / 3D (21)

**What they do.** Story-first pieces: invent a short story, then animate it in Three.js/JS with a named quality bar
("Pixar-level", "80s–90s cartoon"), often with code-made sound. Characters perform in place (a kata, a dance), assemble
(vehicles combining into a robot), or bring hand-drawn input to life.

Techniques:
- **Story that only subtly promotes** the product (or doesn't show it at all, but matches its values) — better for social
  reach. [anilraok-eff262](https://prompt-motion.com/anilraok-eff262) — REEL (mascot mini-stories).
- **Imagine the story first, then build it** in Three.js with a named era/style. [ryzoft-4f85bd](https://prompt-motion.com/ryzoft-4f85bd) — REEL.
- **Assembly sequence**: separate parts transform and lock together into a robot. [allforbigfire-86ff3c](https://prompt-motion.com/allforbigfire-86ff3c) — REEL (robot
  co-host assembling from AI tool logos).
- **Character performs on one spot** through a run of impressive poses (with fire/energy effects). [chrisjdimarco-f068db](https://prompt-motion.com/chrisjdimarco-f068db)
  — REEL (mascot "kata" for a hook).
- **Hand-drawn inputs come alive**, sounds matched to the frames. [abderrahmen-g-9e8ed0](https://prompt-motion.com/abderrahmen-g-9e8ed0) — REEL (Freddie's sketches /
  student drawings).
- **Mascot carries a programme promo** (referral, shop chatbot). [paulo-kombucha-96431c](https://prompt-motion.com/paulo-kombucha-96431c) [anas0ra-e57aea](https://prompt-motion.com/anas0ra-e57aea) — REEL
  (referral/affiliate reels with our mascot).
- **Silent short where sound tells half the story**. [kamstudiolabs-0b0824](https://prompt-motion.com/kamstudiolabs-0b0824) — BOTH.
- **Personified concept** (a stubborn software bug as the hero). [kamstudiolabs-c9bb28](https://prompt-motion.com/kamstudiolabs-c9bb28) — REEL ("prompt yang gak mau
  dibaca AI").
- **Beat-lit 3D scene**: a ball falls and bounces through objects that light up on the beat, with gags.
  [gorden-sun-041f56](https://prompt-motion.com/gorden-sun-041f56) — REEL (voxel world objects lighting on VO stresses).
- **Cultural-moment pixel scene researched from real elements** (Chuseok). [hoyoyoda-3a5c08](https://prompt-motion.com/hoyoyoda-3a5c08) — REEL (Lebaran, 17
  Agustus, Harbolnas).
- **Life-cycle loop** (same person, childhood → old age → loop). [loicrambo-ad6830](https://prompt-motion.com/loicrambo-ad6830) — REEL.
- **"Take all the time you need" for one intricate subject**. [axtonliu-0b861d](https://prompt-motion.com/axtonliu-0b861d) — LAND.
- Do NOT copy: anime characters, celebrity references or other people's IP from entries like [topi-003-b0e12c](https://prompt-motion.com/topi-003-b0e12c),
  [davidshulmanfl-371638](https://prompt-motion.com/davidshulmanfl-371638) — the client's own mascot/robot replace them.

## 7. Typography (8)

**What they do.** Type is the set and the actor. The best entries lock the exact copy and order, give each word a role,
and cue on phrases and pauses rather than a dance beat.

Techniques:
- **Words as architecture**: each key word gets a structural role (beam, load, support, opening, platform) built from
  its own letterforms; the final line literally stands on what earlier words built; allow at least one ~400 ms stillness;
  loop by resetting hidden elements under full occlusion. [gdgtify-287ddf](https://prompt-motion.com/gdgtify-287ddf) — REEL (a motivational line for Freddie
  where "AI" becomes the floor).
- **Kinetic bumper system**: locked message order, three-font system (display / grotesque / mono crumbs), strict
  palette, per-glyph springs staggered at a 16th note, print misregistration only on accent frames, next word revealed
  through a mask made of the outgoing word, a strikethrough that turns into the underline of the next line, seeded
  letter scramble, a tiny "breath" on the hold, loopable. [techhalla-90b8ec](https://prompt-motion.com/techhalla-90b8ec) — REEL (adapt to brand: navy + white +
  #01ccf7 only, Poppins).
- **Lyrics/VO-synced type** that hits the vocals and the beat. [samaote-5e2fc2](https://prompt-motion.com/samaote-5e2fc2) — REEL (our per-word captions as hero
  type in the hook).
- **Trivial question, epic answer** ("what day is it?" as a 30 s cinematic). [tankazunori0914-0fc886](https://prompt-motion.com/tankazunori0914-0fc886) — REEL (hooks).
- **Poster breaks out of its own frame**. [pankajkumar-dev-0bee87](https://prompt-motion.com/pankajkumar-dev-0bee87) — REEL (title card breaking the reel frame).

## 8. Logo reveals / brand stings (4 + end cards across the gallery)

Techniques:
- **Slow assemble-then-reveal**: pieces gather over the whole duration and only at the end read as the logo.
  [tdinh-me-815acb](https://prompt-motion.com/tdinh-me-815acb) — BOTH.
- **Anniversary sting** (10 s) from a brand image. [deebeeeff-50fcd0](https://prompt-motion.com/deebeeeff-50fcd0) — BOTH (AIpreneur batch/anniversary).
- **Fast ad painted over images, morphing text, ends on the logo**; study a reference's timing and shot lengths but
  change the design completely. [lexnlin-038035](https://prompt-motion.com/lexnlin-038035) — BOTH (this is our ATM rule in motion form).
- **End-card logo moves inside launch films**: covers converge and fold around the icon, which emerges from the same
  centre and slides beside the wordmark ([brainextends-e19ac3](https://prompt-motion.com/brainextends-e19ac3)); a route pin becomes the mark ([ultimaxbt-2ddf1e](https://prompt-motion.com/ultimaxbt-2ddf1e));
  100+ images converge into the logo ([rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7)); wordmark squeezes into its own period ([twoclipping-221cab](https://prompt-motion.com/twoclipping-221cab));
  a gold glint reveals a fragment of the mark ([daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4)); end mid-collapse instead of a static hold
  ([notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a)). For AIpreneur: the 3D logo built from Simple Icons / the client's own logo file, never redrawn.

## 9. Social / vertical reels (10)

Techniques:
- **Recompose, don't crop**: the vertical/social version is a deliberately recomposed edit, not a crop of the 16:9
  master. [daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4) — REEL.
- **Talking-head → punchy edit** with subtitles, graphics and music. [sab8a-364a5a](https://prompt-motion.com/sab8a-364a5a) — REEL (Freddie's own clips; see
  `anthropic-skills:business-short-form-reels`).
- **9:16 with a strong POV/personality voice**, chaotic pacing, rendered from Python + ffmpeg. [kloss-xyz-15182a](https://prompt-motion.com/kloss-xyz-15182a) — REEL
  (use sparingly; brand tone is "sharp, practical, not hype").
- **9:16 paper cut-out shadow theatre** with gentle code-made audio for a reflective topic. [x4b47x-9cc84f](https://prompt-motion.com/x4b47x-9cc84f) — REEL
  (story-style AIpreneur episode, navy/white silhouettes).
- **Portrait showreel** — same brief, portrait mode. [ndhabarde11-f155b4](https://prompt-motion.com/ndhabarde11-f155b4) — REEL.
- **10-second ad-style reel from a plain info list** (lineup/schedule). [gonzalomacagno-2de1a9](https://prompt-motion.com/gonzalomacagno-2de1a9) — REEL (class schedule
  / webinar announcement).
- **Thank-you film for the first N users** — community milestone. [sudiyasa-f48ac9](https://prompt-motion.com/sudiyasa-f48ac9) — REEL.
- **"Edit that goes hard"** hype cut (beat-locked type + flashes). [maxalexweber-67688b](https://prompt-motion.com/maxalexweber-67688b) — REEL (avoid the anime IP
  crossover in [micheleharmonic-77628e](https://prompt-motion.com/micheleharmonic-77628e)).

## 10. Other (6)

- **Every note from a visible collision** (audio-visual causality). [kamstudiolabs-447565](https://prompt-motion.com/kamstudiolabs-447565) — BOTH (VO stresses = mascot
  taps).
- **Satisfying physics loop "that could go viral"** (ball escaping rings). [kantamk-61f410](https://prompt-motion.com/kantamk-61f410) — REEL (hook background).
- **One-line mood scene with a film-director style reference.** [itsolelehmann-e47532](https://prompt-motion.com/itsolelehmann-e47532) — LAND.
- **Video + interactive HTML** from one build. [demitiyageekzen-7770ad](https://prompt-motion.com/demitiyageekzen-7770ad) — LAND.
- **Long story with audio + subtitles, clean the workspace after**. [rebutonepress-810f78](https://prompt-motion.com/rebutonepress-810f78).
- **Track-first visuals** (genre track + ASCII visuals). [rames-jusso-589f80](https://prompt-motion.com/rames-jusso-589f80).

---

## Fit summary for AIpreneur reels vs. landscape films

Take into **AIpreneur reels** (1080×1920, mascot host, Dakocan VO, navy/white):
VO takes + per-segment word alignment ([rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7)), captions typed at spoken time, guide object carrying every
hand-off ([rossaxbt-94583b](https://prompt-motion.com/rossaxbt-94583b) — the mascot is the guide), through-line accent dot ([ultimaxbt-bbebf5](https://prompt-motion.com/ultimaxbt-bbebf5)), process-fill
explainer ([ror-fly-9950f1](https://prompt-motion.com/ror-fly-9950f1)), one-genre-per-explanation ([emollick-8661a8](https://prompt-motion.com/emollick-8661a8)), spinning-pain-list hook
([jake11moran-f60e35](https://prompt-motion.com/jake11moran-f60e35)), hook → distinct techniques → clean final frame ([reflex-cloud-72ffe5](https://prompt-motion.com/reflex-cloud-72ffe5)), words-as-architecture
and kinetic bumper type systems in brand colours ([gdgtify-287ddf](https://prompt-motion.com/gdgtify-287ddf), [techhalla-90b8ec](https://prompt-motion.com/techhalla-90b8ec)), assembly sequence for the
robot ([allforbigfire-86ff3c](https://prompt-motion.com/allforbigfire-86ff3c)), beat-lit objects ([gorden-sun-041f56](https://prompt-motion.com/gorden-sun-041f56)), recompose-not-crop ([daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4)),
no corner giveaways ([1littlecoder-9fef89](https://prompt-motion.com/1littlecoder-9fef89)), no invented numbers.

Keep for **landscape launch films** (client products/sites): stage-in-frame, persistent player, frosted-glass titles,
iris/wordmark-squeeze, landing flythrough, real-clip carousel, site-built gallery promo, slow polished desktop camera.

---

## Prompt patterns that work

The long, structured entries (21 of them are over 1,000 characters; 12 use an `<inputs>` block) share a shape. Use the
same shape when writing a brief for ourselves or for a sub-agent:

1. **Role + stakes in one line.** "Senior motion designer + product designer + engineer for <brand>"; the bar is named
   ("premium product film", "Dribbble-level"), and so is what it must NOT feel like (template, PowerPoint, screen
   recording). ([daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4), [techhalla-90b8ec](https://prompt-motion.com/techhalla-90b8ec))
2. **Inputs with defaults.** List what to ask for (name, logo, one-line pitch, screenshots, photos, music with a drop,
   voice ID) and a default for each, so the job runs even when the client skips something. ([notdwd-7de38a](https://prompt-motion.com/notdwd-7de38a),
   [rossaxbt-3085b7](https://prompt-motion.com/rossaxbt-3085b7), [ultimaxbt-2ddf1e](https://prompt-motion.com/ultimaxbt-2ddf1e))
3. **Direction block**: format (size, fps, duration), palette as hex roles, fonts with weights, camera language in one
   sentence, the one accent and where it may appear, and a **banned list** (crossfades, bouncy easing, particles, glows,
   holds > 1 s, invented features/numbers, template look). Bans are as important as wishes.
4. **Beat structure**: the timeline written in beats or seconds (often "120 BPM, N beats; bN–bM: …"), each scene's
   transition named as an object hand-off, the drop assigned to the key reveal, a loop rule if any.
5. **Numbered build steps**: one HTML / Remotion composition, every value from `seek(t)`; springs closed-form; one camera
   transform with log-space zoom; real media as decoded frame sequences; beat grid from analysis; SFX by measured peak;
   −14 LUFS; sub-frame motion blur; QA stills and frame-diff scans before the full render.
6. **Gotchas**: the specific traps the author already hit (flood must pass all corners in ~0.3 s; preserve-3d + opacity
   flattens; will-change blurs scaled text; white shapes vanish on white without a hairline; text swapping inside a
   morphing shape needs its own timing; measure text after fonts load; loop seam must match cursor speed).
7. **Start protocol**: "ask for the inputs → show the beat map / storyboard → show 4–8 stills → only then render".
   For our client (who wants finished files) we skip the approval stops unless asked, but still make the stills for
   our own QA.
8. **Copy rules**: exact locked lines in a fixed order, short (1–4 words per hit), no full stops on screen, no animator
   jargon, every word speaks to the buyer, only facts that exist. ([techhalla-90b8ec](https://prompt-motion.com/techhalla-90b8ec), [ik-builds-b8bdcf](https://prompt-motion.com/ik-builds-b8bdcf))
9. **Real-product-only gate**: inspect the repo/site first, don't invent screens or metrics, use demo-safe values,
   rebuild UI as layers from the design system. ([daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4), [wani-shola-16ca7a](https://prompt-motion.com/wani-shola-16ca7a))
10. **Deliverables list**: storyboard, source, master MP4, poster frame, contact sheet, exact runtime, assets used,
    compromises, reproduce commands. ([daniel-haida-8691d4](https://prompt-motion.com/daniel-haida-8691d4), [brainextends-e19ac3](https://prompt-motion.com/brainextends-e19ac3))

## Short one-shot prompts

About 190 entries are under 300 characters; the "dynamic 15-second motion graphics … showreel … go all out" line (and
translations) alone accounts for ~80. What they achieve: with no constraints the model picks its own story, palette and
music and usually delivers an energetic 10–20 s abstract reel — kinetic type, geometric shapes, particles, camera
pushes, self-composed track. Strengths: speed, surprise, a good "what's possible" probe, fresh ideas for transitions.
Weaknesses: generic subject matter, invented copy/numbers, off-brand colours, corner HUD text, landscape by default, no
VO, nothing tied to a real product.

Adding just one or two specifics changes the outcome a lot: a product URL to research ([ajith-io-c52e09](https://prompt-motion.com/ajith-io-c52e09)), "use the
real components" ([fractadev-149adc](https://prompt-motion.com/fractadev-149adc)), "portrait" ([ndhabarde11-f155b4](https://prompt-motion.com/ndhabarde11-f155b4)), "no corner text"
([1littlecoder-9fef89](https://prompt-motion.com/1littlecoder-9fef89)), "something moves every second, no slow fades" ([aichrislee-a6cb42](https://prompt-motion.com/aichrislee-a6cb42)), "sound synced to the
cuts" with brand colours as slots ([polydao-7a572b](https://prompt-motion.com/polydao-7a572b)).

When to use the one-shot style for this client:
- As an **idea probe**: generate 2–3 quick 10 s sketches to find a transition or hook, then rebuild the winner inside
  the brand system. Never deliver a one-shot result as-is.
- For **brand-free B-roll** inside a reel (an abstract "AI thinking" moment, a hook background), recoloured to
  navy/white + #01ccf7.
- Never for anything that carries claims, numbers, logos or the mascot — those need the structured brief (brand.md,
  client_rules.md, ATM rules, open-source logo rule, QA).

---

## Full index by category


### Product launch films / promos (86)

- [AIsa API key promo](https://prompt-motion.com/0xfemyn-e114d3) — Product UI
- [Paper-style product launch film](https://prompt-motion.com/ik-builds-b8bdcf) — Charts, Diagrams, Music · HyperFrames + GSAP
- [Fitters Bible app promo](https://prompt-motion.com/adamdesgns-478d6d) — Product UI, Phone, Diagrams
- [Trezio app motion reel](https://prompt-motion.com/agonaliu-466a8f) — Product UI, Kinetic type
- [FigPad product promo](https://prompt-motion.com/ai-baymax-0ef9dd) — Product UI
- [Distilbook promo showreel](https://prompt-motion.com/ajith-io-4c248f) — Particles
- [Distilbook product video](https://prompt-motion.com/ajith-io-c52e09) — Product UI
- [Distilbook motion showreel](https://prompt-motion.com/ajith-io-ea7f2d) — Shapes, Particles
- [Commotion app showreel](https://prompt-motion.com/amol909s-27533e) — Product UI, Phone, Code
- [Studio website showreel](https://prompt-motion.com/andginja-333d32) — Product UI, Photos
- [Prompt Motion site promo](https://prompt-motion.com/antonio-kodheli-490109) — Product UI, Music
- [Pixelup Labs studio showreel](https://prompt-motion.com/arjunsh1607-93005d) — Product UI, Photos
- [SaaS launch video](https://prompt-motion.com/aschapmann-131210) — Product UI, Music · Remotion
- [Bento.surf product video](https://prompt-motion.com/bizibeast-10f264) — Product UI, Phone
- [Product intro synced to music](https://prompt-motion.com/bogdandragomir-35e024) — Product UI, Particles, Music
- [Spotify product film](https://prompt-motion.com/brainextends-e19ac3) — Product UI, Music
- [Lidlezz app promo](https://prompt-motion.com/cansincengiz-me-cf68dd) — Product UI
- [Amazon wholesale pitch video](https://prompt-motion.com/ceowinkz-7c776b) — Product UI, Kinetic type
- [Taxtello bookkeeping app film](https://prompt-motion.com/daniel-haida-8691d4) — Product UI, Charts · Remotion
- [Motion designer showreel](https://prompt-motion.com/danilowm-d3720d) — Product UI, Kinetic type, Charts · HyperFrames
- [Lism CSS 1.0 release video](https://prompt-motion.com/ddryo-loos-300829) — Product UI, Code
- [Tennis game launch video](https://prompt-motion.com/deifosv-04e4d3) — Product UI, Phone
- [Dubz Up motion showreel](https://prompt-motion.com/devius-maximus-beab45) — Product UI, Phone, Kinetic type, Characters
- [Muse connector tracker promo](https://prompt-motion.com/elliot-garreffa-f334bc) — Product UI · Remotion
- [Website analyzer product promo](https://prompt-motion.com/en-ra-81c6dd) — Product UI
- [AI Arena product promo](https://prompt-motion.com/ezshine-c90d73) — Product UI, Code
- [Voice agent SaaS launch](https://prompt-motion.com/fractadev-149adc) — Product UI, Charts
- [Parenting app hype video](https://prompt-motion.com/francoxavier33-d2dfd2) — Product UI, Phone, Kinetic type · Remotion
- [Enxovaly baby app promo](https://prompt-motion.com/gabrielbuzziv-4ff0c6) — Product UI, Phone · HyperFrames
- [Matra caption app promo](https://prompt-motion.com/gautam-mer1-2ae354) — Product UI, Phone, Photos · Remotion, React
- [Portfolio motion reel](https://prompt-motion.com/heyiammallik-e72d17) — Product UI, Kinetic type, Particles
- [mdfor.dev product intro video](https://prompt-motion.com/ho-ba-f3f0e9) — Product UI, Code
- [Browser automation skill launch](https://prompt-motion.com/hqmank-7c61f1) — Product UI, Music, Code
- [Database client launch video](https://prompt-motion.com/iammxfschr-d68f90) — Product UI, Code
- [Personal skills showreel](https://prompt-motion.com/ibrahimwasim240-809370) — Product UI, Particles, Characters
- [Distilbook motion showreel](https://prompt-motion.com/itisrazak-3ad902) — Product UI, Kinetic type, Particles, Music
- [NotchBrowser product teaser](https://prompt-motion.com/jake11moran-f60e35) — Product UI, Kinetic type · HyperFrames
- [AgentHud project motion video](https://prompt-motion.com/jazzen-chen-4542ae) — Product UI, Code
- [Ondefica app motion reel](https://prompt-motion.com/jesscaroline7-1ff7cb) — Product UI, Phone, Kinetic type, Charts · HyperFrames
- [Supademo launch video](https://prompt-motion.com/jhylee95-e1152f) — Product UI, Kinetic type, Music
- [Tented image gen product video](https://prompt-motion.com/justincooperman-e7bbc4) — Product UI, Photos · Blender
- [Motion designer showreel](https://prompt-motion.com/kangaroohere-b10f8d) — Product UI, Phone, Kinetic type, Charts
- [Design portfolio video reel](https://prompt-motion.com/kikelopezdesign-7cc9e8) — Product UI, Phone
- [Email verification tool promo](https://prompt-motion.com/kmasiff-cc72cb) — Product UI
- [org2html product showreel](https://prompt-motion.com/kyonax-on-tech-aabc1d) — Product UI, Code
- [PicTwin AI app ad](https://prompt-motion.com/l3d1c-0e35a3) — Product UI, Photos
- [CloudJoi search showcase](https://prompt-motion.com/lester-tyy-f897f7) — Product UI, Photos · Remotion
- [GenVizu product launch](https://prompt-motion.com/listudio-820c7b) — Product UI, Photos
- [Ren app launch video](https://prompt-motion.com/macrohou-33959d) — Product UI, Phone, Charts
- [Gene Spectra promo](https://prompt-motion.com/madebyjmayala-b9204d) — Product UI
- [Brieform product presentation](https://prompt-motion.com/majorbaguette-fb11d7) — Product UI · Remotion
- [Step race app promo](https://prompt-motion.com/marklaunches-3b9492) — Product UI
- [Crux motion design showreel](https://prompt-motion.com/marouanegazouzi-6071d5) — Product UI, Kinetic type, Charts, Music
- [ocrX app launch video](https://prompt-motion.com/mehul4795-4a7007) — Product UI
- [Email tool promo reel](https://prompt-motion.com/melvynx-6cde6c) — Product UI, Kinetic type
- [Quetzal social app reel](https://prompt-motion.com/miskinho-443898) — Product UI, Photos
- [Frame by Frame launch video](https://prompt-motion.com/notdwd-7de38a) — Product UI, Music
- [Launch video remake comparison](https://prompt-motion.com/notdwd-c2037d) — Product UI, Photos, Music
- [Photo retouch app promo](https://prompt-motion.com/oliahmed205-3e31c4) — Product UI, Photos
- [Jev engineering showreel](https://prompt-motion.com/polydao-7a572b) — Product UI, Kinetic type, Music
- [Alan agent platform promo](https://prompt-motion.com/prasad-pilla-2c0cba) — Product UI, Diagrams
- [QuickDesign brand promo](https://prompt-motion.com/quickdesignio-dd93d0) — Product UI, Kinetic type, Music
- [founder.page launch video](https://prompt-motion.com/ratheejaisal-1f4538) — Product UI, Charts
- [Chunku product promo](https://prompt-motion.com/reyzostyle-b55864) — Product UI, Kinetic type · HyperFrames
- [SuperX feature release teaser](https://prompt-motion.com/robj3d3-b18fad) — Product UI
- [Ora 2 image model launch film](https://prompt-motion.com/rossaxbt-3085b7) — Product UI, Photos, Music · HTML canvas + Playwright + ffmpeg
- [Hoplite cloud handoff launch](https://prompt-motion.com/ryan-morr-ccc796) — Product UI, Phone, Kinetic type
- [Norilu product launch video](https://prompt-motion.com/sachaarbonel-8f14f4) — Product UI
- [ViralGrow product promo](https://prompt-motion.com/samuel-yostt-891f87) — Product UI, Phone, Photos
- [Claude self-promo spot](https://prompt-motion.com/slvdev-64c45a) — Product UI, Phone, Kinetic type
- [Dub promo video](https://prompt-motion.com/steventey-0d20e4) — Product UI, Charts
- [Visual guides library launch](https://prompt-motion.com/techyoutbe-945b56) — Product UI, Diagrams, Code
- [AjustaCV Pro pricing promo](https://prompt-motion.com/thayto-dev-44b911) — Product UI · HyperFrames
- [Second brain service promo](https://prompt-motion.com/theviableedge-9065be) — Product UI, Code · Remotion
- [sweetRegret app update reel](https://prompt-motion.com/thilina-a-891c09) — Product UI, Phone, Characters
- [Travel visa service promo](https://prompt-motion.com/thismacapital-dfba20) — Product UI, Kinetic type, Photos
- [YouTube transcript product ad](https://prompt-motion.com/tstfully-0aa6b4) — Product UI, Kinetic type
- [Photo print app launch film](https://prompt-motion.com/twoclipping-221cab) — Product UI, Phone, Photos, Music · HTML + Playwright
- [UGC ad generator promo](https://prompt-motion.com/twoclipping-6dd14e) — Product UI, Phone, Photos, Music · HTML + Playwright
- [Landing page 3D scroll](https://prompt-motion.com/twoclipping-d89be5) — Product UI, Kinetic type · WebGL2 + Playwright
- [Food craving launch film](https://prompt-motion.com/ultimaxbt-2ddf1e) — Product UI, Kinetic type, Photos, Music · HTML
- [Bold Pilot SEO promo](https://prompt-motion.com/utopyaszx-1b2f94) — Product UI, Kinetic type, Charts
- [Tally product demo](https://prompt-motion.com/visheshbaghell-3aba37) — Product UI, Kinetic type
- [Developer portfolio site showreel](https://prompt-motion.com/wani-shola-16ca7a) — Product UI, Music · Remotion
- [Supasito launch video](https://prompt-motion.com/wozu-co-242285) — Product UI
- [SaaS product launch video](https://prompt-motion.com/xelandre-363f00) — Product UI · HTML/JS, Playwright, ffmpeg

### UI animation (7)

- [Badge unlock screen animation](https://prompt-motion.com/bthreeagency-b9b8d9) — Product UI, Phone, Particles
- [Sahi trading terminal reveal](https://prompt-motion.com/dale-vaz-cc612a) — Product UI, Phone, Particles, Charts · JavaScript
- [Morphing UI states loop](https://prompt-motion.com/demonugc-4c5753) — Product UI, Music · HTML, Playwright
- [Five scroll-based sections](https://prompt-motion.com/ercankeskinx-ec2568) — Product UI, Photos
- [White ball UI motion loop](https://prompt-motion.com/rossaxbt-94583b) — Product UI, Music · HTML
- [Shape morphing through UI states](https://prompt-motion.com/twoclipping-5cba86) — Product UI, Charts, Music · HTML + Playwright
- [Orange dot motion system](https://prompt-motion.com/ultimaxbt-bbebf5) — Kinetic type, Shapes, Music · HTML

### Explainers / diagrams (25)

- [Celld job ownership explainer](https://prompt-motion.com/0xnfrith-5be616) — Diagrams
- [Sotto reading app explainer](https://prompt-motion.com/1stnoel-c20a89) — Product UI, Phone
- [Animated business explainer](https://prompt-motion.com/alex-prompter-1ea044) — Diagrams · HTML
- [Handwoven textiles brand explainer](https://prompt-motion.com/amitsingha89-150378) — Kinetic type, Photos
- [First & 10 yellow line explainer](https://prompt-motion.com/blueoctopusai-dd17bd) — Diagrams
- [Indian civilisation history film](https://prompt-motion.com/buildfastwithai-53234e) — Diagrams
- [Datagran ChatGPT ads explainer](https://prompt-motion.com/charlesmendez-73b6e4) — Product UI, Phone, Charts
- [Recursion explained in genres](https://prompt-motion.com/emollick-8661a8) — Characters, Code
- [Prompting mistakes video tutorial](https://prompt-motion.com/henkvaness-0e06af) — Diagrams
- [Sherwood agentic hedge fund explainer](https://prompt-motion.com/imthatcarlos-e04bfe) — Product UI, Kinetic type, Photos · Remotion
- [FundMyCompute platform overview](https://prompt-motion.com/jayscambler-3f8889) — Product UI, Diagrams
- [History of AI timeline](https://prompt-motion.com/kloss-xyz-fe0c31) — Kinetic type, Particles, Diagrams
- [Whiteboard skill tutorial](https://prompt-motion.com/lemomo-ai-0d9cff) — Product UI, Diagrams
- [AI data centre 3D film](https://prompt-motion.com/mdaman010-e7226a) — Diagrams · HTML
- [DeFi Saver stop-motion explainer](https://prompt-motion.com/nikolajankovic-ce4ff4) — Charts, Diagrams
- [Token bucket rate limiter](https://prompt-motion.com/parkerrex-1a54fe) — Charts, Diagrams · Canvas
- [Pixel art LLM history](https://prompt-motion.com/pluginplay-3d4006) — Diagrams, Characters · HTML
- [Negroni recipe animation](https://prompt-motion.com/ror-fly-9950f1) — Diagrams · HTML
- [White Russian recipe animation](https://prompt-motion.com/sarut0bisasuke-cefa43) — Diagrams
- [AI data centre 3D tour](https://prompt-motion.com/sayan-shanky-f850d8) — Diagrams · HTML
- [DistilBook product explainer](https://prompt-motion.com/sudo-kiran-4f8b59) — Product UI
- [DistilBook product explainer](https://prompt-motion.com/sudo-kiran-6609ed) — Product UI, Diagrams
- [DistilBook motion explainer](https://prompt-motion.com/sudo-kiran-b055de) — Product UI, Diagrams
- [Replica symmetry breaking whiteboard](https://prompt-motion.com/tak3sh8-be5012) — Diagrams
- [What is Git explainer](https://prompt-motion.com/yunn260414-60d996) — Diagrams, Code · JavaScript

### Charts / data (10)

- [Stock analysis app promo](https://prompt-motion.com/aistocksavvy-3fb9f5) — Product UI, Charts
- [Steam new releases news recap](https://prompt-motion.com/gigabit-million-16b3a0) — Charts
- [Drone Emprit showreel](https://prompt-motion.com/ismailfahmi-557268) — Particles, Charts
- [Derivative concept explainer](https://prompt-motion.com/linearuncle-5d2bae) — Charts, Diagrams · Manim, edge-tts
- [Mathematics motion showreel](https://prompt-motion.com/math-files-39c9d0) — Charts, Diagrams
- [Backlink audit data promo](https://prompt-motion.com/palashbagchi11-0a4b6b) — Kinetic type, Charts
- [AllInvestView product promo](https://prompt-motion.com/rammanq-f5a90f) — Product UI, Phone, Charts
- [Flexprice motion showreel](https://prompt-motion.com/sudeepsd-1a3485) — Particles, Charts
- [Moroccan political history timeline](https://prompt-motion.com/triglyceee-bd5b08) — Kinetic type, Charts
- [MotionSites one million visitors](https://prompt-motion.com/viktoroddy-98c1d8) — Product UI, Charts, Code

### Showreels (57)

- [Claude self-intro motion graphic](https://prompt-motion.com/1littlecoder-9fef89) — Kinetic type, Shapes
- [Risograph studio intro](https://prompt-motion.com/rneayan-474bcf) — Kinetic type, Diagrams
- [Oscilloscope-style studio motion graphic](https://prompt-motion.com/rneayan-ea6129) — Kinetic type, Charts
- [Claude motion designer showreel](https://prompt-motion.com/3xtihor-0f6911) — Kinetic type, Shapes, Charts, Music
- [Motion designer showreel](https://prompt-motion.com/aichrislee-a6cb42) — Kinetic type, Shapes, Music
- [Abstract motion design reel](https://prompt-motion.com/ajith-io-b5626e) — Kinetic type, Shapes, Music
- [Photon journey from the Sun](https://prompt-motion.com/apoorvjain25-d24184) — Kinetic type, Particles
- [Studio1 intro showreel](https://prompt-motion.com/astrodevil-3f2054) — Kinetic type, Charts
- [Claude motion design showreel](https://prompt-motion.com/ayushunleashed-ece3e3) — Kinetic type, Shapes, Particles, Music
- [Particle sphere motion reel](https://prompt-motion.com/blue-clarity-ef56d0) — Kinetic type, Particles
- [Recruiter self-intro reel](https://prompt-motion.com/blushpetal795-0c85c2) — Kinetic type, Particles, Charts
- [Motion principles showreel](https://prompt-motion.com/chatgptastra-0d95c7) — Kinetic type, Particles, Diagrams
- [Claude motion reel](https://prompt-motion.com/codestackr-c071bf) — Kinetic type, Shapes
- [Claude motion designer showreel](https://prompt-motion.com/crazyalphaaa-bc7e75) — Kinetic type, Particles
- [Motion designer showreel](https://prompt-motion.com/eyishazyer-af035b) — Kinetic type, Shapes, Charts, Music
- [Blue editorial motion showreel](https://prompt-motion.com/fionntobin-97b7af) — Kinetic type, Shapes, Music
- [Claude motion design reel](https://prompt-motion.com/ghinaiya-nirmal-5d8fec) — Kinetic type, Shapes, Music
- [Keyframe motion design reel](https://prompt-motion.com/grace-sunnyy-29bc61) — Kinetic type, Particles, Music
- [Motion designer showreel](https://prompt-motion.com/hanifproduktif-54bdee) — Kinetic type, Particles
- [Full Stop figure sequence](https://prompt-motion.com/hbcoop-de365c) — Shapes, Particles
- [Deliberately terrible motion showreel](https://prompt-motion.com/henkpoley-3d3407) — Characters · HTML
- [Motion designer showreel](https://prompt-motion.com/himanshutwtxs-5f4b43) — Kinetic type, Particles, Diagrams
- [fal motion design showreel](https://prompt-motion.com/influencer-seo-ce8c33) — Kinetic type, Photos
- [Kinetic type showreel](https://prompt-motion.com/itsuki-dev-10942d) — Kinetic type, Shapes, Music
- [Branding agency showreel](https://prompt-motion.com/jacksonfall-54b2ac) — Kinetic type, Photos
- [Claude motion reel](https://prompt-motion.com/jasonzhou1993-8595e0) — Kinetic type, Particles, Charts
- [Code-only motion design reel](https://prompt-motion.com/johnsavage-ai-b091c0) — Kinetic type, Shapes
- [Lead Notifi product ad](https://prompt-motion.com/leadnotifi-e83f94) — Kinetic type, Shapes, Diagrams
- [Geometric motion designer showreel](https://prompt-motion.com/leonkohli-6dc01b) — Kinetic type, Shapes
- [Swiss-style motion showreel](https://prompt-motion.com/levabashidze-2d713a) — Kinetic type, Shapes
- [Motion techniques showreel](https://prompt-motion.com/lukasersil-0ed38e) — Kinetic type, Shapes, Particles
- [Kinetic type and particle showreel](https://prompt-motion.com/m1n9-k7-ff9ab9) — Kinetic type, Particles, Music
- [Personal research intro reel](https://prompt-motion.com/madhav-xo-f97f20) — Kinetic type, Particles, Code
- [Flowdrive motion showreel](https://prompt-motion.com/manuelogomigo-f33ca9) — Shapes, Particles
- [LiteLLM promo reel](https://prompt-motion.com/misbahsy-80eaec) — Diagrams, Music, Code
- [Psychedelic hypnotic eye showreel](https://prompt-motion.com/monokern-ade5b6) — Shapes
- [Bold typographic motion showreel](https://prompt-motion.com/motiondsgnr-9dcfa6) — Kinetic type, Shapes, Charts
- [What happens in one second](https://prompt-motion.com/nolkeeg-bf062e) — Kinetic type, Particles
- [Motion designer résumé reel](https://prompt-motion.com/raphaelaubryy-4b137e) — Shapes, Particles
- [Claude motion design showreel](https://prompt-motion.com/rendesr-86be44) — Kinetic type, Shapes
- [Nohandslabs brand promo](https://prompt-motion.com/robvjourney-ce3e1a) — Kinetic type, Particles, Code
- [Easing and morphing showreel](https://prompt-motion.com/roundtablespace-d3a1be) — Kinetic type, Shapes, Music
- [Motion design showreel](https://prompt-motion.com/safarkhanshuvo-ffd52d) — Kinetic type, Shapes, Particles
- [3D motion design showreel](https://prompt-motion.com/sahildesigner23-ee3155) — Kinetic type, Shapes, Music
- [Motion design showreel](https://prompt-motion.com/samuel-spitz-974923) — Kinetic type, Shapes
- [Kinetic shapes showreel](https://prompt-motion.com/shinskinakamoto-20190b) — Kinetic type, Shapes, Particles
- [Bold kinetic type showreel](https://prompt-motion.com/shneural-2abdfa) — Kinetic type, Shapes, Particles
- [Claude motion designer showreel](https://prompt-motion.com/stephanlivera-df17a2) — Kinetic type, Shapes, Music
- [Claude motion design showreel](https://prompt-motion.com/sudo-kiran-49176d) — Kinetic type, Shapes, Particles
- [Claude motion design reel](https://prompt-motion.com/tequilafunks-97f6c9) — Kinetic type, Shapes, Particles, Music · Remotion
- [Motion designer showreel](https://prompt-motion.com/teslachartz-c58b32) — Kinetic type, Shapes, Diagrams
- [Motion design principles reel](https://prompt-motion.com/tolgayhickiran-e90799) — Kinetic type, Shapes, Particles, Music
- [Kinetic type motion showreel](https://prompt-motion.com/topi-003-9ca6b5) — Kinetic type, Particles
- [Motion designer showreel](https://prompt-motion.com/vanshwtfff-db0466) — Kinetic type, Shapes, Particles
- [Type, form, space showreel](https://prompt-motion.com/web3wesley-7bb108) — Kinetic type, Shapes
- [Motion designer showreel](https://prompt-motion.com/zaqailo-212ad3) — Kinetic type, Shapes, Particles, Music
- [Kinetic type showreel](https://prompt-motion.com/zheke-38deff) — Kinetic type, Shapes

### Characters / 3D (21)

- [Pixel wizard crypto animation](https://prompt-motion.com/0xevinho-3777d8) — Characters
- [Sketchbook animals come alive](https://prompt-motion.com/abderrahmen-g-9e8ed0) — Characters · JavaScript
- [Pixel art card battle game](https://prompt-motion.com/aisongman-71ffac) — Characters
- [Anime robot combining sequence](https://prompt-motion.com/allforbigfire-86ff3c) — Characters · Python
- [Shop chatbot mascot promo](https://prompt-motion.com/anas0ra-e57aea) — Characters
- [Scrabble tile character story](https://prompt-motion.com/anilraok-eff262) — Characters · Three.js
- [Pelican riding a bicycle](https://prompt-motion.com/axtonliu-0b861d) — Characters
- [Three.js Skyraider aircraft model](https://prompt-motion.com/buildfastwithai-ed9447) — Product UI · Three.js
- [Fiery samurai kata](https://prompt-motion.com/chrisjdimarco-f068db) — Particles, Characters · JavaScript
- [Clay-style music video](https://prompt-motion.com/davidshulmanfl-371638) — Characters, Music
- [The Last Light animated short](https://prompt-motion.com/faroukzy-9ff23e) — Characters
- [Beat-synced bouncing 3D ball](https://prompt-motion.com/gorden-sun-041f56) — Music · Three.js
- [Chuseok pixel night scene](https://prompt-motion.com/hoyoyoda-3a5c08) — Characters
- [Lighthouse keeper silent short](https://prompt-motion.com/kamstudiolabs-0b0824) — Characters
- [Animated short about a bug](https://prompt-motion.com/kamstudiolabs-c9bb28) — Characters, Code
- [Cycle of life animation](https://prompt-motion.com/loicrambo-ad6830) — Characters
- [Starry Night cat-spotting game](https://prompt-motion.com/mandelduck-95fd08) — Characters
- [Porco Rosso sunset dogfight](https://prompt-motion.com/nft-chen-5f8bb0) · Three.js
- [Mascot referral program promo](https://prompt-motion.com/paulo-kombucha-96431c) — Product UI, Characters
- [Animated space cartoon episode](https://prompt-motion.com/ryzoft-4f85bd) — Characters · Three.js
- [Anime maid dance showreel](https://prompt-motion.com/topi-003-b0e12c) — Kinetic type, Characters, Music

### Typography (8)

- [Speech built as architecture](https://prompt-motion.com/gdgtify-287ddf) — Kinetic type · SVG/Canvas
- [Overthinking motion study](https://prompt-motion.com/gizakdag-cf4ae6) — Kinetic type
- [Poster breaking its frame](https://prompt-motion.com/pankajkumar-dev-0bee87) — Kinetic type, Shapes, Music
- [Synced lyrics motion video](https://prompt-motion.com/samaote-5e2fc2) — Kinetic type, Music
- [Kinetic type self-portrait](https://prompt-motion.com/souravbhar871-61f424) — Kinetic type
- [What day is it](https://prompt-motion.com/tankazunori0914-0fc886) — Kinetic type, Music · HyperFrames
- [TechHalla kinetic type bumper](https://prompt-motion.com/techhalla-90b8ec) — Kinetic type
- [Shin Majin-shiki promo](https://prompt-motion.com/majin-appsheet-2d3c1a) — Kinetic type · HyperFrames

### Logo reveals / brand stings (4)

- [Recipe brand 20th anniversary](https://prompt-motion.com/deebeeeff-50fcd0) — Particles
- [Engraving-style Claude ad](https://prompt-motion.com/lexnlin-038035) — Kinetic type, Photos
- [Reflex brand motion reel](https://prompt-motion.com/reflex-cloud-72ffe5) — Kinetic type, Music
- [TypingMind logo reveal](https://prompt-motion.com/tdinh-me-815acb) — Shapes

### Social / vertical reels (10)

- [Lightspark social promo video](https://prompt-motion.com/davidmarcus-a28a60) — Kinetic type, Code
- [Festival lineup promo reel](https://prompt-motion.com/gonzalomacagno-2de1a9) — Kinetic type
- [Chaotic Claude POV video](https://prompt-motion.com/kloss-xyz-15182a) — Kinetic type, Code · Python + ffmpeg
- [ODATANO Cardano hype edit](https://prompt-motion.com/maxalexweber-67688b) — Kinetic type, Particles
- [GravityDEX anime hype edit](https://prompt-motion.com/micheleharmonic-77628e) — Kinetic type
- [Motion designer portrait showreel](https://prompt-motion.com/ndhabarde11-f155b4) — Kinetic type, Shapes, Particles
- [Talking-head clip edit](https://prompt-motion.com/sab8a-364a5a) — Photos · OpenEdit
- [Chain.wtf pitch video](https://prompt-motion.com/spearwtf-3c1fd1) — Kinetic type
- [EyezOn 100 users thank-you](https://prompt-motion.com/sudiyasa-f48ac9) — Kinetic type, Shapes, Music
- [Shadow theatre home story](https://prompt-motion.com/x4b47x-9cc84f) — Characters · JavaScript

### Other (6)

- [Tengwang Pavilion moonlit river](https://prompt-motion.com/demitiyageekzen-7770ad) · WebGL2 + Canvas 2D + Web Audio
- [Four seasons train window](https://prompt-motion.com/itsolelehmann-e47532)
- [Collision-driven music machine](https://prompt-motion.com/kamstudiolabs-447565) — Particles, Music · HTML
- [Ball escaping twelve rings](https://prompt-motion.com/kantamk-61f410) — Shapes, Music
- [UK dubstep track with ASCII visuals](https://prompt-motion.com/rames-jusso-589f80) — Music, Code · HyperFrames
- [Black hole time story](https://prompt-motion.com/rebutonepress-810f78)
