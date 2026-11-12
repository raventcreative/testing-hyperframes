# NOTES — R10 · Edit video yang sudah ada pakai AI (Runway Aleph) (LIGHT) · `projects/aip_r10_aleph/`

1080×1920 · 30 fps · **35.8333 s** (1075 frames) · VO 34.32 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r4_remote` (LIGHT).
Serve: `python3 -m http.server 8830 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed.
No footage: every before/after "video" is our own animated illustration (HTML/CSS/SVG + GSAP), labelled **ILUSTRASI** in the player.

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`
   (saved voice; every line tagged) → `assets/audio/vo.mp3` + `vo.json` (line times + character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles).
4. `python3 -I tools/rounds.py .` → `vendor/rounds.js` (TOTAL, SCN, DEMOS) · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −31.5 LUFS vs VO −19.1 LUFS).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_ALEPH_1080x1920.png` (server on :8830).

## The illustration kit — `vendor/r10kit.js` (window.R10)
- `R10.park(p, look)` — park clip in 5 looks with identical geometry: `day`, `night` (moon, twinkling stars, lit windows, fireflies,
  lamp glow + light cone + ground pool), `sakura` (pink crown + blossom dots, petals falling, petals on the grass), `snow` (white
  crown, snow caps on bench/lamp, overcast sky, snowfall), `dusk` (low sun glow, purple/orange sky, warm grade). Layers: sky ·
  celestial · clouds · hills+city · treeline · ground (path, tree, bench, lamp) · lamp light · person · particles · foreground bushes ·
  grade. `R10.street(p, car)` — Indonesian ruko row + pavement + kerb + road, a walking person; `car=true` adds a parked car.
  `R10.shelf(p, products)` — room with window light, pendant lamp, two wall shelves (plant, books, vase stay in every copy);
  `products=true` adds a fictitious "PRODUKMU" line (3 bottles, box, 2 jars, glints).
- `R10.footage(api, prefixes, t0, dur, opts)` gives EVERY copy of a clip the identical "footage" motion (slow push-in + layered
  parallax, cloud drift, star twinkle, person sway/wave/walk, particles, lamp flicker), so before/after copies stay pixel-aligned
  and the wipe reads as the same shot edited. SVG parts animate with `attr: {transform}` around fixed pivots; no negative timeline
  positions (GSAP shifts children when a tween is inserted before 0 — that bug was found and fixed).
- `R10.player / prompt / wipe / type` — the shared before/after player (frame left 60 top 318, 960×548; viewport 940×528), divider
  with handle, labels **VIDEO ASLI** / **HASIL EDIT AI** (+ sub-chips Siang/Malam, Musim panas/sakura/salju, …), **ILUSTRASI** tag,
  and the prompt pill (y 842–918) with per-character typing + send.
- Demo clips s01→s05 hand over as a CAROUSEL: each clip's stage also carries the next clip's first frame (pinned with the next
  scene's own footage options) and slides one clip width in its last 0.33 s, so the last frame of a clip == the first frame of the
  next (verified at every cut ±1 frame).

## Scenes
| id | start–end (s) | VO | visual |
|---|---|---|---|
| s01 | 0.00–4.80 | Video yang udah kamu rekam, sekarang bisa kamu ubah cuma pakai satu kalimat. | player already on screen (park, REC timecode, person waves on "rekam") · prompt rises + types "Change the season to winter" · "ubah": divider sweeps → snow · split asli/hasil · "1 kalimat" badge |
| s02 | 4.80–7.33 | Mau siang jadi malam? Tinggal ketik. | closer park shot · "Make it night" · sweep → night (moon, stars, lit windows, fireflies), lamp flickers on · split siang/malam |
| s03 | 7.33–11.67 | Mau ganti musim? Dari musim panas, jadi sakura, atau salju. | shot on the big tree · "Musim panas" · "Make it cherry blossom season" → sakura (falling petals) · "Change the season to winter" → snow (snowfall) |
| s04 | 11.67–14.43 | Pinggir jalan yang kosong, bisa ditambahin mobil. | ruko street, walker · marquee "area kosong" on the kerb · "Add a car parked by the curb" → parked car (walker passes behind it), settle + sparkle |
| s05 | 14.43–17.20 | Rak yang polos, bisa diisi produk kamu. | plain shelf, dust in the lamp light · marquees "rak kosong" · "Put my product on this shelf" → PRODUKMU line (plant/books/vase unchanged) · glint; player sinks |
| s06 | 17.20–23.87 | Namanya Runway Aleph. Kamu kasih videonya, tulis mau diubah apa, bagian lainnya dibiarin kayak aslinya. | name card "Runway Aleph" (text only) + "versi terbaru: Aleph 2.0" · 3 step cards (skeletons, then lit on their beats): upload clip · prompt "Make it night" · result (mini wipe → night) · dashed outlines on the person · chips Orangnya / Gerakannya / Sudut kameranya sama |
| s07 | 23.87–29.17 | Cocok banget buat konten dan marketing: satu video, banyak versi, tanpa syuting ulang. | source clip tile (ILUSTRASI) · pills Konten / Marketing · "1 video asli" · four playing portrait versions fan out (Malam · Sakura · Salju · Senja) · card "Tanpa syuting ulang" with struck clapperboard |
| s08 | 29.17–32.43 | Catatan: fitur ini ada di paket berbayar Runway. | note card: "Aleph 2.0 tersedia di semua paket berbayar Runway." + marker · stamp PAKET BERBAYAR · rows: pakai kredit per detik video · dicek 12 Nov 2026, harga & kuota bisa berubah · cek situs resmi Runway |
| s09 | 32.43–35.83 | Komen AI, aku kirim cara pakainya. | package "Cara pakai Runway Aleph" · comment field types AI, heart, send → plane → DM bubble "terkirim" · end logo |

Robot: flies in on "rekam", TYPES every prompt on its holo keyboard (s01–s05 + step 2), cheers/claps the reveals, presents "Runway
Aleph", shakes its head on "tanpa syuting ulang", thinks on "Catatan", cheers the CTA. Mascot (host): presents the player, reacts to
each reveal, explains the steps, CTA.

## Sources (checked 2026-11-12) — details in production/VO_SCRIPT.md
runway.com / runwayml.com / help.runwayml.com are DNS-blocked from this sandbox: facts were verified from search results restricted
to those official domains (titles + page excerpts) and Runway's Replicate listing:
- https://runway.com/product/aleph-2 — Aleph 2.0: describe a change, the model alters only that.
- https://runway.com/research/introducing-runway-aleph — Aleph: add/remove/transform objects, new angles, style + lighting.
- https://runway.com/news/introducing-aleph-2-and-edit-studio — Aleph 2.0 + Edit Studio (21 May 2026): time of day/relight, season
  ("Change the season to winter"), remove objects, product variants, background; "available now on all paid Runway plans".
- https://help.runwayml.com/hc/en-us/articles/51683104370451-Creating-with-Edit-Studio — credits per second (28/s, 56 min), 2–30 s input.
- https://help.runwayml.com/hc/en-us/articles/52150503729171-Aleph-2-0-Prompting-Guide — verb (add/remove/change/replace/re-light) + result.
- https://runway.com/pricing · https://replicate.com/runwayml/aleph-2

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot`)
- Final pass, 64 frames (every scene, each cut ±1 frame, first + last frame): contact sheets in
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r10/qa_final/`
  (`hero_sheet_A.jpg` 0–16.5 s, `hero_sheet_B.jpg` 17–35.8 s = hero + caption band; `contact-sheet-1..8.jpg` = full frames;
  `s08_marker_check.jpg` after the last s08 change). PNG dumps deleted.
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit). `validate`: 0 errors; kit warning "multiple
  instances of Three.js" (robot + mascot bundles); 1 WCAG note ("KOPI" sign at 10.75 s) is measured on the next clip's street copy
  that waits off-screen (clipped) for the carousel — not visible.
- Every initial state is pinned at 0 (labels, prompt characters via display, clip-path wipes, SVG attr transforms, particles).

## Known issues / notes for the lead
- Runway's official pages could not be opened directly (DNS block); facts come from search excerpts of runway.com /
  help.runwayml.com. Worth a 1-minute human check of the pricing/plan line before posting (VO says only "paket berbayar").
- On-screen prompts are in English on purpose (Runway's prompt guide pattern); we make no claim about Indonesian prompts.
- The DM hand-out ("Cara pakai Runway Aleph · langkah + contoh prompt") is promised by the CTA but not written here.
- s06/s07/s08/s09 start from an empty hero for ~2–8 frames while their first card rises (scene breath after the previous exit).
- The s04 walker scale is small (0.74) by design (it walks behind the parked car to show depth).
- The HTTP server started for this session is stopped at the end; restart with the command above.
