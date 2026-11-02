# 11 — HOUSE STYLE BIBLE: "ICE-IVORY ILLUSTRATED DIORAMA" (REF-H)
**Version:** V3.0 · 21 Oktober 2026
**Source of truth:** the approved AI PRENEUR Reel v3 (`style_references/ref_H_house_style_aipreneur_v3.mp4`, 39.4 s, 1080×1920, 30 fps). Its complete working source is in `house_style_kit/example_aipreneur_v3/`. The client (Freddie) approved this look: *"aku suka banget"*.
**Rule:** for every new Reel, **REF-H is the default look**. REF-A/B/C (doc 06) are only secondary motif libraries. If anything below conflicts with older docs (01–08 V2.1), this bible wins, unless the user explicitly asks for another style.

---

## 1. THE LOOK IN ONE PARAGRAPH
A light, airy ivory → ice-blue world with a faint paper grid. The video tells the story through **one big, richly detailed, softly lit illustrated object per spoken phrase**, like a porcelain-and-glass diorama (REF-B craft on a light palette). It cuts every ~2–3 s on the voice-over. Text is minimal: **one small caption line at the top**, revealed word by word, with the key words in navy and an ice-blue highlighter. Every scene has a hero object that fills the frame, micro-detail, a key light from the upper left, soft contact shadows, three depth planes, and a payoff "apex" (flash + shockwave + sparkles + scale punch) landing exactly on the key spoken word. The video ends on a calm, static brand lockup (logo on a porcelain plate). No dark screens, no neon, no big headlines, no mascots.

## 2. WHAT IS MANDATORY (the 12 locks)
1. **Visual-first.** Big headlines are forbidden. The only persistent text is the top caption (§5). Visual copy inside a scene uses only spoken words (tab labels, a typed prompt, a word engraved on a key, "Aa" glyphs).
2. **One scene per spoken phrase.** Cut on phrase boundaries in the verified transcript. Scene length 0.8–5.5 s (v3 averages 2.6 s across 15 scenes in 39.4 s). A sentence spanning two audio clips stays one scene.
3. **One hero metaphor per scene**, filling ~60–75 % of the visual zone (hero centre y ≈ 900–1000).
4. **Micro-detail:** 20–60 drawn elements per scene (bevels, screws, rivets, pins, ticks, sticky notes, stitched edges, tiny abstract UI lines, reflections). Never 5 flat shapes.
5. **Light:** soft key light from the upper left, a white top/left inner highlight, and shadows that fall down-right/below. Spotlight cones and warm glow appear only on the key moment.
6. **Grounding:** every object has a contact shadow (an ellipse that tightens when touching and widens/softens when lifted).
7. **Depth:** three planes. Far: blurred porcelain discs/props (blur 6–12 px, opacity ~0.6) moving slower. Mid: the hero. Near: particles/bokeh/foreground prop. Plus a slow push-in (scale 1 → 1.06–1.08 over the scene). Use CSS 3D (perspective 1200–1600 px, board tilts rotateX 30–40°) where an object is a surface or board.
8. **Frame 0 is never empty:** the hero is already mid-entrance on the cut.
9. **Key action lands on the word** (±0.05 s), using the word-start times from the verified transcript.
10. **Constant purposeful motion:** nothing static for more than 0.6 s (at least push-in + one ambient loop).
11. **Hard cuts between scenes** (REF-B rhythm). Never fade to black. The last scene's final frame is a still, complete brand composition.
12. **Light palette only** (§3). Mint and amber are small accents.

## 3. PALETTE (exact)
| Token | Hex | Use |
|---|---|---|
| ink | `#202B3B` | caption text, dark type |
| navy | `#294B77` | primary accent: key words, enamel parts, selection frames, needles |
| navy-2 | `#3A6299` | gradient partner, secondary bars |
| navy-deep | `#1C3354` | shadow colour base `rgba(28,51,84,a)`, deep gradient end |
| ice1 | `#ACC6E7` | haze, rings, secondary fills |
| ice2 | `#CBDBF4` | panels, glass tint |
| ice3 | `#E8F0FB` | surfaces, BG fallback |
| ice4 | `#FBFCFE` | near-white highlights |
| graphite | `#2E2E2E` | logo colour, dark details (sparingly) |
| paper | `#FFFEFB` | paper/notes |
| muted | `#5B6676` | secondary text |
| mint (accent) | `#9FD8C4` → `#BFE9DA` | OK / check badges / "healthy" states |
| amber (accent) | `#F2C46D` | warm glow, a single star, warning lamp |
**Forbidden:** red, neon, purple/cyan gradients, full-screen dark backgrounds, pure `#000`.

## 4. TYPOGRAPHY
- **Montserrat** 700 (caption, labels), 900 (hero type inside a scene, e.g. 3D extruded words). Geometric, matches the AI PRENEUR wordmark.
- **Inter** 400 only for intentionally "plain/boring" text (e.g. a "before" state).
- **IBM Plex Mono** 700 for tiny engraved/UI labels (letter-spacing 0.06–0.2 em).
- All three are bundled in the HyperFrames renderer. Do not use other fonts.
- Minimum in-scene label size: 26 px. The caption is 46 px.

## 5. GLOBAL LAYERS (index.html — use `house_style_kit/starter/index.html`)
1. **BG plate** — `assets/brand/pastel_background_1080x1920.png`: the original 980×1225 pastel JPEG, uniformly scaled to a width of 1080 and mirror-extended top/bottom with blurred seams (never stretched).
2. **Paper grid** — 1 px lines every 54 px, `rgba(41,75,119,0.055)`, radial mask (75 % × 60 %), drifting 27 px over the video.
3. **Haze** — three radial blobs (ice1 upper-left 900 px, ice2 lower-right 1000 px, white centre 800 px) drifting with sine yoyo.
4. **Motes** — 22 seeded glass dots, 4–13 px, rising 120–360 px over the whole video.
5. **Grain** — 256 px tiling noise PNG at opacity 0.5, stepping position (`steps(N)`).
6. **Scenes** — sub-compositions `compositions/sNN.html`, one per phrase, hard-cut.
7. **Caption** — top 232 px, sides 70 px, centred, Montserrat 700 46/1.22, ink. Each word sits in an overflow mask and rises `yPercent 110 → 0` in 0.34 s `power4.out` at word start −0.08 s. Key words: navy + highlighter `linear-gradient(transparent 62%, rgba(172,198,231,0.75) 62% 92%, transparent 92%)`. One caption block per scene (1–2 lines).
8. **Audio** — one VO `<audio>` placed once. No BGM unless supplied and licensed.

## 6. SAFE ZONES / LAYOUT
- Caption zone: y 232–380, keep it clear of scene objects.
- **Visual zone: x 50–1030, y 400–1520**, with the hero centred at y ≈ 900–1000.
- y > 1560: keep empty-ish (Reels UI). Soft shadows/bokeh are allowed.
- The logo lockup plate sits between y 1150 and 1450 in the final scene.

## 7. MATERIAL & FX RECIPES (CSS, copy exactly)
```css
/* porcelain card (default surface) */
background: linear-gradient(175deg,#ffffff,#f4f7fb); border:2px solid rgba(41,75,119,.10); border-radius:26px;
box-shadow: 0 2px 0 rgba(255,255,255,.9) inset, 0 40px 70px -24px rgba(28,51,84,.38), 0 10px 22px rgba(28,51,84,.12);
/* paper */
background: linear-gradient(178deg,#fffefb,#f6f4ee); border:1px solid rgba(46,46,46,.08);
/* simulated frosted glass (honest: no real refraction) */
background: linear-gradient(140deg,rgba(255,255,255,.92),rgba(214,228,247,.78)); border:2px solid rgba(255,255,255,.95);
box-shadow: inset 0 0 40px rgba(255,255,255,.8), 0 30px 60px -20px rgba(28,51,84,.35);
/* navy enamel */
background: linear-gradient(135deg,#3a6299,#294b77 55%,#1f3a5f); color:#fbfcfe;
/* contact shadow (ellipse under the object, slightly right) */
background: radial-gradient(ellipse, rgba(28,51,84,.45), rgba(28,51,84,.14) 45%, rgba(28,51,84,0) 72%);
/* far-plane bokeh disc */
filter: blur(7px); opacity:.65; background: radial-gradient(circle at 35% 30%,#fff,#e8f0fb 45%,#acc6e7 100%);
/* spotlight cone */
clip-path: polygon(41% 0,59% 0,100% 100%,0 100%); filter: blur(8px);
background: linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.6) 55%,rgba(255,255,255,.85));
/* light-ray burst (payoff) */
background: repeating-conic-gradient(from 0deg, rgba(172,198,231,0) 0 6deg, rgba(172,198,231,.7) 6deg 8deg, rgba(255,255,255,.95) 8deg 10deg, rgba(172,198,231,0) 10deg 15deg);
mask-image: radial-gradient(circle,#000 0 14%,rgba(0,0,0,.7) 30%,transparent 62%);
/* warm payoff glow */
background: radial-gradient(circle,#fff,rgba(255,247,226,.75) 30%,rgba(242,196,109,.18) 52%,rgba(242,196,109,0) 70%);
/* shockwave ring */
border:5px solid rgba(255,255,255,.95); box-shadow:0 0 30px rgba(172,198,231,.9), inset 0 0 24px rgba(172,198,231,.7);
/* mint check badge */
background: linear-gradient(160deg,#bfe9da,#9fd8c4); border:3px solid #fff; box-shadow:0 10px 18px -6px rgba(28,51,84,.4);
/* porcelain pill label */
height:50px; padding:0 22px; border-radius:25px; font:700 30px/1 Montserrat; color:#294b77;
background: linear-gradient(175deg,#fff,#eef3fa); border:2px solid rgba(41,75,119,.12);
/* navy selection frame: 4 corner brackets, 5–6 px navy strokes, snaps around the focused element */
```
**Sparkle:** 4-point star SVG `M20 2 C21 14 26 19 38 20 C26 21 21 26 20 38 C19 26 14 21 2 20 C14 19 19 14 20 2Z`, white fill + ice stroke, scattered with a **seeded PRNG**.
**Illustration method:** heroes are hand-built SVG (gradients via `<linearGradient>`, strokes, `stroke-dasharray` draws) + CSS boxes. Bevel = a lighter top/left stroke + a darker bottom/right edge. Metal ring = concentric circles with alternating light/dark gradients + tick marks.

## 8. MOTION GRAMMAR
| Moment | Timing | Ease |
|---|---|---|
| Hero entrance on the cut (already in motion at frame 0) | 0.3–0.6 s | `power3.out` / `power4.out` |
| Small pops (badges, chips, bubbles) | 0.25–0.4 s, stagger 0.03–0.06 | `back.out(1.4–1.8)` |
| Key action → apex **on the word** | lands at word start ±0.05 | `power4.in` into contact, then `power3.out` |
| Apex FX | glow 0.25 s; shockwave 0.6 s (scale 0.4 → 1.8, fade); 10–16 sparkles 0.7 s; scale punch 1.03–1.06 yoyo 0.12 s; optional micro camera shake | — |
| Settle | 0.12–0.35 s, low amplitude | `power2.out` / rare `elastic.out(1.1,0.45)` |
| Ambient loop | push-in 1 → 1.07 over the scene + far-plane parallax + one object loop (needle wobble, belt, pulses) | `none` / `sine.inOut` |
| Typing | per character 0.04–0.05 s, starting on each word's time | steps |
| Blur→sharp (clarity) | `filter: blur(14px) → 0` over 0.5 s, crisp on the word | `power2.inOut` |
| Exit | hard cut (no exit animation needed) | — |

## 9. SCENE METAPHOR CATALOG (proven in REF-H — reuse the logic, not necessarily the same object)
| Concept in the VO | Hero object (v3 scene) | Apex on the word |
|---|---|---|
| "many people say / opinions" | phone feed card + burst of 15–22 speech/comment bubbles in 3 depth layers (s01) | waves of pops on each word |
| quality judgement "biasa aja / meh" | AI-generator window with bland beige results + porcelain reaction gauge, needle droops to the middle (s02) | needle settles on the judgement word |
| "the tool itself is fine" | 3D-tilted circuit board, chip embossed "AI", magnifier scan, status rows with mint checks (s03) | navy check badge stamps on the chip |
| "problem is the input/instruction" | braided cable from chip → porcelain input-slot machine, crumpled note circled in navy, jams, lamp turns amber (s04) | hand-drawn circle around the note |
| speed | diagonal conveyor with flying cards + chrome stopwatch hand whip (s05) | hand clicks to 12 |
| clarity / dependency | camera focus ring between a brief clipboard and an output poster; both go blur→sharp together (s06) | crisp + lens glint |
| vague prompt | original chat tablet; cursor types the spoken prompt; generic template reply with 3/5 stars (s07) | send press → bland reply |
| list of factors | navy folder opens to a brief board; the camera tracks 5 illustrated panels with a navy selection frame (s08) | each panel acts on its word |
| precision | "prompt" key + porcelain padlock (s09) | shackle pops, mint check |
| transformation | before/after monitor with a slider handle (s10) | slider snaps across + flash |
| plain / ordinary | flat clipboard with grey typed text (Inter, no glow) (s11) | typing only (deliberately flat) |
| premium / expensive | paper shatters into glass shards → glass panel with 6-layer extruded 3D type + editor timeline (s12) | sparkle burst + sheen |
| brand / "this is how WE do it" | porcelain clapperboard with the **genuine logo** on the slate; then a directed card grid (s13) | clapper snaps shut on the brand name |
| benefits trio | stopwatch → archery target (arrow hits) → faceted gem on a pedestal (s14) | each lands on its word; gem bursts on the last |
| closing / "this level" | phone with a mosaic of this video's own scenes + logo plate lockup (s15) | logo sheen; still final frame |
**Extending the catalog:** pick a physical, instantly readable object for the concept (dial = choice, scale = comparison, box opening = reveal, bridge = connection, funnel = filtering, rocket = growth, shield = safety, puzzle = fit). Always light, porcelain/glass/navy material, with one apex on the word.

## 10. GOLDEN FRAMES (match these)
`golden_frames/H01…H19` are stills from REF-H at hero moments (filename = timestamp). New work must look like it belongs in the same series: same palette, light direction, detail density, caption size/position and shadow style. `reference_contact_sheets/ref_H_house_style_overview.jpg` shows them all at once.

## 11. DON'T
- Big headline text, subtitles in a bottom box, or text-on-card slides.
- Flat icons with one drop shadow called "3D".
- Empty first frames, fades to black, dead holds > 0.6 s.
- Copying REF-A/B/C imagery, characters, brands or layouts.
- Inventing claims, numbers, URLs, CTAs or product names. If no CTA is spoken, none is shown.
- Redrawing, recolouring, cropping or stretching a logo. Set only its width.
- Mascots or characters unless the user supplies a rig/asset and asks for them.
- `Math.random`, wall clocks, infinite repeats, or tweening layout properties (left/top/width/height).
