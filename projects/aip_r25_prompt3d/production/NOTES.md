# NOTES — R25 · Website 3D dari 1 prompt: bedah promptnya (AI PRENEUR · NAVY) · `projects/aip_r25_prompt3d/`

- **Duration** 45.90 s (1377 frames @30) · VO 44.48 s starting at 0.30 s (spoken ≈44.5 s, 100 words) · CTA keyword **SITUS** ·
  reference `aip_remake_batch6/refs/ref5.mp4` (49.7 s, English; same video as R8's reference). Not rendered (the lead renders), not
  committed. Serve: `python3 -m http.server 8955 --bind 127.0.0.1` in this folder.
- **Kit**: copied from `projects/aip_r19_jarvis` (NAVY; without `out/`, its VO/QA/cover PNG, scenes, music bed). Mascot glance disabled
  from the start (`const glance = (t) => 0;`). `.gitignore` = `out/`.
- **Angle** (see `production/VO_SCRIPT.md`): NOT R8's library-and-sell story. We dissect ONE prompt into 5 labelled parts (objek utama ·
  suasana · gerakan · isi halaman · teknis), show what each part adds to a 3D landing page, combine → Claude → revise in plain words,
  then honest pricing in rupiah (method, no numbers, no earning promise), free empty template via DM (`production/DM_SITUS.md`).

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
   (NO --tags = client's AUTO tags; one call, one take, 44.56 s) → copied to `assets/audio/vo.mp3`; `production/vo_el.json` = line
   times, tags used, character alignment.
2. `python3 -I tools/el_to_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the ElevenLabs alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (one merge: "Three"+"JS" → "Three.js" on screen;
   "situs," shown as "SITUS,"; PRON map for lip sync; scene cuts + caption chunks).
4. `python3 -I tools/build_index.py .` → `index.html` (4 scene slots, captions, logo, audio `vo.mp3` @0.3 s + `sfx.wav`, no music).
5. `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples; master −35.2 dB RMS = same level as
   R19's bed).
6. Cover: `python3 -m http.server 8955 --bind 127.0.0.1` at the project root, then
   `PORT=8955 node thumbnail/render_cover.cjs thumbnail/COVER_SITUS_1080x1920.png`.
7. Listen check: `python3 -I tools/fw_transcribe.py production/vo_el.mp3 <out.json> small id` (and `medium`).

## Shared components — `vendor/r25kit.js` (window.R25K) + `vendor/r25icons.js` (Lucide 1.70.0, ISC, generated from lucide-static)
- Boilerplate as the R19 kit: every initial state pinned in a nested timeline that is the first child at 0 (`I()`), `ft` fromTo with
  `immediateRender:false`, scene-local word times `wt()`, per-letter typing without onUpdate, `finish()` = end marker + backward-seek
  patch + `tl.render(0, true, true)`. Positions clamped ≥ 0. No Math.random / Date / rAF.
- **Prompt card** (x 60, y 330, 600×600): "prompt-website-3d.txt" (CONTOH), five rows (disc number / active cyan / done green check,
  label, one-line preview with ellipsis, typed text, s01 paragraph). Accordion geometry `K.rowTops(k)`: collapsed 64 px, active 216 px.
- **Phone** (x 700, y 330, 320×600): our own example landing page (toko parfum lokal, fictional, CONTOH): blank page → amber glass bottle
  (own SVG, front label hides during the scaleX "360°" spin) → teal gradient wipe, warm light beam, glass highlight, shadow → scrollbar +
  swipe hand, spin, zoom closer → headline, 3 product cards, testimonial ("Rina, Bandung · contoh"), sticky "Pesan via WhatsApp" →
  tech sheet (index.html · cukup 1 file ✓, Three.js · objek 3D-nya ✓, Ringan di HP meter ✓) → green glow. Tags on the phone name each
  layer (melayang, warna latar, cahaya, bayangan, 360°, mendekat, judul diperbesar).
- s01 → s02 hand-over at identical state (`K.cardCollapsed` + `K.phoneSet(..., "blank")`).

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–5.90 | Prompt website 3D yang keren itu bukan sihir. Kalau dibedah, isinya cuma lima bagian. | Frame 0: prompt card as one wall of text (5 paragraphs) + phone with the finished parfum page (bottle floating). "Prompt": card glows; "3D": bottle spins 360°, phone breathes; "keren itu": 4 sparkles + "sihir?" chip; "bukan": chip struck through, then drops; "Kalau dibedah": cyan laser + scissors sweep down the card, four cut lines between the parts; "isinya": strips separate (slight tilt) and cross-fade into 5 labelled rows; "cuma lima": discs 1–5 pop; "bagian": footer "5 bagian · kita isi satu per satu"; last 0.6 s: scan line rewinds the phone to an empty page |
| s02 | 5.90–31.60 | Satu … melayang. / Dua … bayangan. / Tiga … mendekat. / Empat … WhatsApp. / Lima … HP. / Gabungin … sehari-hari. | Per part: its row opens (accordion), its prompt line types in (CONTOH), the phone gains the layer (see Phone above); done rows get a green check + preview. **1 Objek** 5.92–9.6 (bottle drops on "botol", "melayang" tag) · **2 Suasana** 9.69–13.8 (bg wipe on "warna", beam + light on "arah cahaya", shadow on "bayangan") · **3 Gerakan** 13.92–17.6 (swipes on "di-scroll", spin on "muter", zoom on "mendekat") · **4 Isi halaman** 17.66–21.8 (headline on "judul", scroll + 3 cards on "produk", testimonial, WhatsApp button) · **5 Teknis** 21.92–27.4 (scroll back, sheet: index.html ✓ on "HTML", Three.js ✓, spin on "3D-nya", meter on "ringan", ✓ + green glow on "HP") · **Gabung** 27.54–31.6 (rows stack into a deck → one message "Prompt website 3D · 1–5 · 5 bagian, lengkap" in "Chat dengan Claude"; send; typing dots; "Siap! Halamannya jadi: index.html" + phone rescan; "judulnya gedein dikit, ya" typed + sent; headline grows + "judul diperbesar"); last 0.28 s fade |
| s03 | 31.60–39.73 | Soal harga, lupakan patokan dolar. Hitung jam kerjamu, jatah revisi, domain dan hosting, lalu bandingkan dengan harga jasa di kotamu. | Header "Harga jasa · hitung dalam rupiah · tanpa janji cuan · JUJUR"; "$" coin + amber "patokan dolar"; "lupakan": strike + dim + wobble; "dolar.": coin flips to "Rp" + green "pakai rupiah"; "Hitung": coin parks; blocks drop + stack with "+" joints (Jam kerjamu · Jatah revisi · Domain + hosting) — group centred; "hosting": result bar "= harga kamu · kamu yang hitung, dalam rupiah" (no number); "lalu": stack slides left, card "Di kotamu · cek 3–5 jasa web serupa" with a cheaper→pricier ruler, 5 grey dots (no numbers), "kisaran wajar" band, cyan "kamu" marker slides in on "kotamu", amber note "tanpa angka: bukan janji penghasilan"; last 0.28 s fade |
| s04 | 39.73–45.90 | Template kosongnya aku siapin gratis, tinggal isi. Komen SITUS, aku kirim lewat DM. | Empty template card "Template prompt website 3D" (5 labelled rows, dashed blanks), blanks glow on "kosongnya", green GRATIS stamp on "gratis", pencil fills "botol parfum amber" on "tinggal isi"; "Komen": template folds into the file card "Template prompt website 3D · 5 bagian · gratis, tinggal isi"; comment bar, SITUS typed per letter + caret, heart; DM panel (AI PRENEUR) "Ini template 5 bagiannya, gratis ya", paper plane, card lands as attachment, "terkirim"; end logo (corner logo fades at 44.52) |

Hosts: mascot bottom-left (welcome, present per part, emphasize on "bukan"/"cahaya"/"WhatsApp"/"ringan"/"lupakan"/"domain"/"kotamu",
question on "Soal", compare on "bandingkan", reveal on "lima"/"Gabungin"/"gratis", cta on "Komen", point on "DM."); robot bottom-right
(types the prompt lines on the holo keyboard in every part, scans the page, "no" on "bukan"/"lupakan", claps on "Gabungin", cheers
"lima"/"muter"/"ringan"/"gratis"/"Komen", hops at every part change and scene cut).

## Sources (checked 13 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- Three.js: github.com/mrdoob/three.js (sparse clone acf77e4: README "JavaScript 3D library", package.json 0.187.0 MIT, LICENSE;
  manual pages installation.html (CDN import map, local server, `npx serve .`) and loading-3d-models.html (glTF/.GLB, GLTFLoader)).
  threejs.org itself is DNS-blocked in this sandbox.
- GSAP: github.com/greensock/GSAP (sparse clone 5e6c35f: README "100% FREE … even for commercial use", ScrollTrigger; "Standard 'no
  charge' license").
- Claude artifacts: support.claude.com/en/articles/9487310 ("single-page websites", Free plan included).
- MDN prefers-reduced-motion (github.com/mdn/content 92395f8; developer.mozilla.org DNS-blocked).

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R19 kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors, 0 contrast warnings; remaining warnings = "multiple Three.js instances"
  (robot + mascot bundles, as in the kit) + SwiftShader ReadPixels notices. (A first run flagged 18 contrast notes: preview/placeholder
  grey, WhatsApp green, CONTOH tag, and off-screen sections measured through the phone clip → all fixed, see below.)
- All four scene timelines + robot + mascot register in the preview (checked with a Playwright script on :8955, then stopped; the
  preview's stamped `data-hf-id` attributes were stripped again). Layout check in the same run: no text outside its box (only the
  intentional ellipsis previews), the five typed prompt lines fit the open row (≤ 108 px of 152), the s01 paragraphs fit (58 of 94 px).
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): one full pass of 71 frames (first frame, every beat of every scene, both sides
  of each cut 5.90 / 31.60 / 39.73, the end 45.86) + two targeted fix passes (6 + 6 frames). Contact sheets (JPG):
  `production/qa/runtime_full_1..3.jpg` (full frames), `production/qa/runtime_hero_1..3.jpg` (hero zone + captions, larger),
  `production/qa/runtime_hosts_1..2.jpg` (mascot + robot, eye check), `production/qa/runtime_fix.jpg` (after the fixes). PNG dumps deleted.
- Mascot eyes: pupils in every frame of the full pass (closed lids at 15.5 / 31.1 / 45.5 s = blinks); glance disabled from the start.
- Captions: never covered (hero content ends at y 930, captions at y≈960–1030, hosts below).
- Fixed during QA: (1) s04 "tinggal isi" fill text rendered as stacked letters — a generic `.bl span` rule also hit the per-letter typing
  spans → scoped to `.bl > span`; (2) s01 "isinya": the card read almost empty for ~0.2 s while the strips moved → paragraph text now
  cross-fades into the row labels; (3) contrast: previews/placeholders #8a99b3 → #5d6f8f, WhatsApp button #2da44e → #1f7f3a (18 px),
  CONTOH tag darker, product/testimonial sections hidden whenever they sit below the screen clip; (4) s03: the cost stack now stays
  centred until "lalu" and slides left when the comparison card arrives (the right half was empty for 3 s).

## Known issues / notes for the lead
- Frame 0 shows the prompt card + finished phone page only: the mascot pops up from below over 0.5 s and the robot flies in over
  0.75 s (kit behaviour, same as R19). The cover is separate.
- The "3D" in the phone is our own SVG bottle with a scaleX spin + zoom (no WebGL in the composition): it reads as a 3D product page
  illustration, labelled CONTOH. The example prompt text and page are ours, not a tested output of a real prompt run.
- `production/DM_SITUS.md` (the hand-out) was written for this reel; the template was not run end-to-end through Claude here — results
  vary per AI (said in the DM). Pricing is a method only (no amounts), on screen and in the DM.
- Mid-spin frames (e.g. 1.3 s, 16.5 s, 25.6 s) show the bottle as a thin sliver for 1–2 frames — that's the edge-on moment of the spin.
- Caption chunks can show an empty chip for 1–2 frames while the first word rises (house caption behaviour).
- `hyperframes preview/snapshot` wrote `.hyperframes/` into the folder (harmless, as in R19); preview-stamped `data-hf-id`
  attributes were stripped again.
