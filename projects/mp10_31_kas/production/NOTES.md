# MasterPajak AI · Video 31 — "Untung Tapi Uang Kok Nggak Ada?"

1080×1920 · **28.9 s** (`TM.total` = `data-duration` = 28.9) · HyperFrames 0.8.186 · built VO-first (batch-3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept: the laba is water in a plumbing wall
One **light CSS-3D plumbing wall** (light tiles, glass pipes, yellow valve wheels) filmed by one moving camera. It holds:
- a big glass **LABA tank** (plate "LABA BULAN INI · Rp8.000.000") at the top left;
- a glass main pipe that runs down the wall, with three branches, each behind a yellow **valve wheel**;
- three glass tanks on wall shelves, each with its own contents drawn on the back panel and seen through the water:
  - **STOK BELUM LAKU**: cardboard boxes that go under water;
  - **DANA BELUM CAIR**: a clock whose hands race, plus a padlock on the glass that snaps shut;
  - **BELANJA STOK LAGI**: a shopping basket, and a new box drops in;
- at the bottom, a faucet over the steel **KAS cash box** ("KAS · UANG DI TANGAN") on a counter.

The film:
1. **Hook.** A laporan laba rugi card says *Laba bersih Rp8.000.000* and gets an **UNTUNG** stamp. The camera tilts down to
   the cash box: the lid pops open, it is almost empty (two coins, one note), dust puffs and a moth flies out.
2. **"Bayangin, labanya itu air."** The laba amount lifts off the card as a chip, flies up to the LABA tank, turns into a
   drop and splashes in. The tank fills with water.
3. **Three valves, one per line.** Each valve turns open, water runs through the glass pipe (moving flow dashes, an inflow
   jet inside the tank), the tank fills, the LABA tank drains, and the amount chip pops.
4. **"Yang sampai ke kas, tinggal sedikit."** The rest runs down the main pipe. The tap turns, and only four drips fall
   into the cash box: ripples and a thin water line ("KAS Rp700.000").
5. **"Untung sama uang di tangan itu beda."** Wide shot of the whole wall (the LABA tank now empty, the three tanks full,
   the cash box nearly dry) under two number cards: "Untung (laba) Rp8.000.000" ≠ "Uang di tangan (kas) Rp700.000".
6. **Brand (navy).** A MasterPajak AI *Pembukuan* card: the laba row, then a yellow trunk that branches into four rows
   (stok belum laku, dana belum cair, belanja stok lagi, kas), each with a water bar sized to its share. The first three
   get "NYANGKUT" tags and the kas row gets "UANG DI TANGAN". The robot rises with the chest hologram. Series end card.

Point: laba ≠ uang di tangan. Untung and kas are different, and tidy books show where the money is sitting.
Not used in videos 1–30: no conveyor, river, quiz show, kitchen, filing cabinet, relay race, orbiting notes, order storm,
archery, day-sky timeline or split interview. Water moves only in pipes and tanks, never as a river.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP31.mp3` (no `--tags`).
**One take** (no regeneration).
- `VO_MP31.mp3` is 27.04 s. Speech runs 0.36 → 27.25 on the film timeline (energy envelope): **26.9 s spoken** (≤ 33 s), 67 words.
  This is a little under the 28 s the batch-3 brief suggests; the voice read fast. Not regenerated (limited credit; every word is clean).
- `assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP31.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.36 – 3.42 | [playful] [excited] [curious] | Laporannya untung, tapi kok uangnya nggak ada? |
| L2 | 3.70 – 6.10 | [playful] [excited] | Bayangin, labanya itu air. |
| L3 | 6.32 – 8.10 | [playful] [excited] | Sebagian jadi stok yang belum laku. |
| L4 | 8.28 – 10.66 | [playful] [excited] | Sebagian masih dana penjualan yang belum cair. |
| L5 | 10.84 – 12.78 | [playful] [excited] | Sebagian kepakai belanja stok lagi. |
| L6 | 13.00 – 14.90 | [playful] [excited] | Yang sampai ke kas, tinggal sedikit. |
| L7 | 15.24 – 17.46 | [playful] [excited] | Untung sama uang di tangan itu beda. |
| L8 | 17.70 – 21.82 | [playful] [excited] | Pembukuan MasterPajak AI yang rapi bantu kamu lihat uangmu nyangkut di mana. |
| L9 | 22.08 – 24.84 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L10 | 25.02 – 27.25 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Line 1 check** (first 3.65 s, numpy input, `tools/fw_transcribe.py`, language id):
  - `small`: "Laporannya untung, tapi kok uangnya nggak ada?" (untung p 0.92)
  - `medium`: "Laporannya untung, tapi kok uangnya nggak ada?" (untung p 0.99)
- **Full listen check** (`small`): every word is heard and no tag is read aloud:
  > Laporannya untung, tapi kok uangnya nggak ada? / Bayangin, labanya itu air. / Sebagian jadi stock yang belum laku. /
  > Sebagian masih dana penjualan yang belum cair. / Sebagian kepake belanja stock lagi. / Yang sampai kekas, tinggal sedikit. /
  > Untung sama uang di tangan itu beda. / Pembukuan Master Pajak AI yang rapi bantu kamu lihat uangmu nyangkut di mana. /
  > Jualan jalan terus, pajaknya AI yang urus. / Coba kalkulator gratis, link di bio.

  "stock", "kepake" and "kekas" are only whisper's spelling of stok / kepakai / ke kas.

## TM (every key is a real word time: JSON character alignment + 0.30)
The alignment puts some line-start words late (e.g. "Bayangin" by 0.33 s), so the line-start keys (`hook`, `bay`, `s1`, `s2`,
`s3`, `yang`, `u2`, `sol`, `end`, `cta`) use the audio onset of that word from the 20 ms energy envelope of `vo.wav`.
All other keys are alignment + 0.30.

| key | t | word | key | t | word | key | t | word |
|---|---|---|---|---|---|---|---|---|
| hook | 0.36 | Laporannya | s2 | 8.28 | Sebagian (2) | u2 | 15.24 | Untung (L7) |
| untung | 1.10 | untung | masih | 8.94 | masih | uang2 | 15.98 | uang (L7) |
| tapi | 1.90 | tapi | dana | 9.18 | dana | tangan | 16.26 | tangan |
| kok | 2.26 | kok | pj | 9.42 | penjualan | itu2 | 16.54 | itu (L7) |
| uang | 2.46 | uangnya | blm2 | 10.06 | belum (L4) | beda | 17.02 | beda |
| nggak | 2.78 | nggak | cair | 10.22 | cair | sol | 17.70 | Pembukuan |
| ada | 3.10 | ada | s3 | 10.84 | Sebagian (3) | mp / ai | 18.30 / 18.78 | MasterPajak / AI |
| bay | 3.70 | Bayangin | pakai | 11.50 | kepakai | rapi | 19.18 | rapi |
| laba | 4.89 | labanya | belanja | 11.82 | belanja | bantu / kamu | 19.70 / 20.06 | bantu / kamu |
| itu | 5.34 | itu | stok2 | 12.14 | stok (L5) | lihat | 20.34 | lihat |
| air | 5.66 | air | lagi | 12.38 | lagi | uangmu | 20.62 | uangmu |
| s1 | 6.32 | Sebagian (1) | yang | 13.00 | Yang | nyangkut | 20.98 | nyangkut |
| stok | 7.10 | stok | sampai | 13.26 | sampai | mana | 21.58 | mana |
| belum | 7.50 | belum (L3) | kas | 13.74 | kas | end | 22.08 | Jualan |
| laku | 7.66 | laku | tinggal | 14.14 | tinggal | pajak / urus | 23.47 / 24.46 | pajaknya / urus |
| | | | sedikit | 14.46 | sedikit | cta / gratis | 25.00 / 26.10 | Coba / gratis |
| | | | | | | bio | 26.57 | Link |
| | | | | | | total | 28.90 | last word end 27.34 + 1.56 |

**Brand hologram ≥ 4 s.** The voice runs fast, so `end − sol` is only 4.38 s. The band sweep therefore starts on "beda" at
`sol − 0.8` (16.90), the navy brand scene is up at `sol − 0.35` (17.35), and the robot CUT is at `sol − 0.45`
(`robot_perf.js`, `index.html` and `tools/sfx.py` use the same offsets). The chest hologram is on screen 17.45 → 21.88 (4.4 s),
at full alpha 17.65 → 21.70 (4.05 s).

## Scenes (timeline seconds)
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 3.70 | Hook: report card + cash box | The card swings in (0.02–0.57). Caption "laporannya" 0.18, "untung," 0.98 (stabilo 1.40). The UNTUNG stamp slams at 1.14. On "tapi" (1.90) the card steps up and back while the camera tilts down to the cash box; caption "tapi kok" / "uangnya nggak ada?" (stabilo 3.08). The lid pops at 2.44–3.06, dust at 2.78, the moth flies out 2.83–4.4. A light fog hides the stations behind the card until "bayangin". The robot rises (0.1–0.8), points at the card, nods on "untung", looks into the box and shrugs on "nggak ada". |
| T | 3.75 – 4.75 | Tilt up | The card falls away; the camera tilts up the wall to the LABA tank. |
| S2 | 3.70 – 6.32 | "Bayangin, labanya itu air." | The laba chip flies up (3.74–4.70), turns into a drop and dives into the tank; splash at 4.86; the tank fills 4.88–5.73; the plate lights up. "Ilustrasi data" chip from 5.06. Caption "bayangin," / "labanya itu air." (stabilo on "air." 5.78). The camera pulls out to frame the tank and the first station (5.95–6.75). |
| S3 | 6.32 – 8.28 | Stok belum laku | Valve 1 opens 6.44, water in the pipe 6.59–7.05, the tank fills 7.04–7.86 over the boxes, the LABA tank drains to 5/8, chip "Rp3.000.000" at 7.74. Caption "sebagian jadi" / "stok yang belum laku." Valve closes 8.08. |
| S4 | 8.28 – 10.84 | Dana belum cair | Camera down (8.28–9.0). Valve 2 opens 8.43, the tank fills 9.13–10.42, the clock races 9.18–10.72, the padlock snaps shut 10.08, the LABA tank drains to 2.5/8, chip "Rp2.500.000" at 10.34. Caption "sebagian masih" / "dana penjualan" / "yang belum cair." |
| S5 | 10.84 – 13.00 | Belanja stok lagi | Camera down (10.84–11.56). Valve 3 opens 10.99, the tank fills 11.71–12.60, a new box drops into the basket 12.09, the LABA tank drains to 0.7/8, chip "Rp1.800.000" at 12.48. Caption "sebagian kepakai" / "belanja stok lagi." |
| S6 | 13.00 – 15.24 | Kas | The camera follows the water down to the cash box (13.0–13.8). The tap turns at 13.74; drips land at 14.40, 14.74, 15.10, 15.32 (ripples, the water line rises to 21 px). The LABA tank runs empty by 15.16. Chip "KAS Rp700.000" at 14.52. Caption "yang sampai ke kas," / "tinggal sedikit." (stabilo 14.76). The robot squints and shakes its head. |
| S7 | 15.24 – 16.90 | Untung ≠ uang di tangan | The camera pulls back to the whole wall (15.24–16.09). Number cards: "Untung (laba) Rp8.000.000" 15.26 (full bar), "Uang di tangan (kas) Rp700.000" 15.88 (8.75 % bar), the ≠ stamp at 16.52 with a shake, caption "itu beda." 16.48. The robot ducks out from 16.54. |
| T | 16.90 – 17.35 | Band sweep | Series bands with the MasterPajak AI marquee (on "beda"). |
| S8 | 17.35 – 22.08 | Brand (navy) | The robot rises half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). The Pembukuan card swings up (17.38–18.33). Caption "pembukuan MasterPajak AI yang rapi" 17.66, "bantu kamu lihat" 19.60, "uangmu nyangkut di mana." 20.50 (underline 21.10). Laba row 17.75; the yellow trunk draws on "MasterPajak" (18.2); the four rows and their water bars fill on "rapi" (19.18–19.95); "NYANGKUT" tags on "nyangkut" (21.00, 21.13, 21.26), "UANG DI TANGAN" at 21.40 (right after the three tags, before the beam); the card pulses on "lihat". The far arm points at the rows and at the tags. |
| T | 21.56 – 22.58 | Beam + iris | Series. |
| S9 | 22.08 – 28.90 | End card | Series template: "Jualan jalan terus," 22.18, "pajaknya AI yang urus." 23.33, CTA "Coba kalkulator gratis" 24.90 (pulse 25.90), "Link di bio" 26.52. The robot waves, points at the CTA and waves again, with the logo hologram on the left (x 150–570). |

## Numbers (all "Ilustrasi data"; arithmetic exact)
**Laporan laba rugi (hook card):** Penjualan Rp24.500.000 − Modal barang Rp12.300.000 − Biaya Rp4.200.000 = **Laba bersih
Rp8.000.000**. Check: 24.500.000 − 12.300.000 = 12.200.000; 12.200.000 − 4.200.000 = 8.000.000 ✓.

**Where the laba sits (tanks, number cards, brand card):**

| where | amount | share of the laba (water bar) |
|---|---|---|
| Stok belum laku | Rp3.000.000 | 37.5 % |
| Dana belum cair | Rp2.500.000 | 31.25 % |
| Belanja stok lagi | Rp1.800.000 | 22.5 % |
| Kas (uang di tangan) | Rp700.000 | 8.75 % |
| **Total** | **Rp8.000.000** | **100 %** |

Check: 3.000.000 + 2.500.000 + 1.800.000 + 700.000 = 8.000.000 ✓. The LABA tank drains in the same steps (8 → 5 → 2.5 → 0.7 → 0
juta of water), and the kas bar on the number card is 8.75 % of the laba bar. The model is simplified on purpose (it treats
the month's laba as the only money flowing): stock bought and not yet sold, sales recorded but not yet paid out, and restock
spending all hold laba that is not cash in hand.

## Labels and brand rules
- **"Ilustrasi data"**: on the report card (hook); a screen chip (top right) from 5.06 to the band sweep, while the tanks,
  amount chips and number cards are on screen; on the Pembukuan card.
- **"Simulasi alur"**: on the Pembukuan card (the only app UI).
- No tax rate, deadline, penalty, guarantee or invented statistic. No marketplace, bank, e-wallet or app names, logos or
  colours: "dana penjualan yang belum cair" stays generic.
- Features named: only pembukuan (+ laporan laba rugi as the hook card) and the kalkulator gratis on the end card.
  "MasterPajak AI" is spelled that way everywhere. Tagline and CTA match the brief.
- The robot appears in every part. On the light wall it is a small full-body host in the bottom-left corner, below all
  captions, tanks and the cash box. Both holograms stay inside the safe zone.

## QA done
Scratch dir: `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp31/`.
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`), one full pass of 40 frames: every scene, every camera move and
  transition midpoint, the band sweep, the beam/iris and the end card. JPG contact sheets:
  - `mp31/rtA0.jpg`: hook → tank fill → first two valves (0 – 8.6)
  - `mp31/rtA1.jpg`: dana / belanja / kas → untung ≠ kas → bands (9.6 – 17.4)
  - `mp31/rtA2.jpg`: brand → beam → end card (17.8 – 28.85)

  The real runtime matched the playwright preview in every frame; no renderer-only bugs were found.
- **Fixes from that pass**, checked in one targeted pass of 8 frames (`mp31/rtB0.jpg`: 4.2, 6.6, 13.6, 16.8, 18.0, 19.8,
  21.5, 21.7):
  - the two number cards were narrowed so the right card ends at x 1020 (it reached 1034);
  - the brand card moved up 30 px so the robot's antenna no longer touches its bottom-left corner;
  - the "UANG DI TANGAN" tag pops at 21.40 instead of 21.56, so it is not hidden by the beam at once.
- Earlier preview fixes: a light fog hides the three stations behind the report card in the hook; the cash station moved
  down (counter at y 1110) and the hook camera looks down at 34° so the two coins and the note are visible; a bigger moth
  (it read as a grey blob); more transparent water so the tank contents show; a thin water line inside the cash box.
- **`hyperframes validate`**: 0 errors. 4 warnings are GL "GPU stall due to ReadPixels" driver messages; 6 contrast notes are
  all on the band marquee while it is hidden.
- **Text containment** (`contain.cjs`, transforms off): no text sticks out of its box. Captions, plates and number values
  are also shrunk to their boxes at build time (`buildReady["fit"]`).
- **Lip-sync**: `tools/lipsync.py` writes `lipsync.js` (1636 frames at 60 fps, talking fraction 0.85).
- **SFX**: `tools/sfx.py` writes `assets/audio/sfx.wav`, 28.9 s, fully synthesised, −24.3 dB RMS (a little louder than
  Video 30's −27.1 because the running water is a continuous layer; the lead's mix may want it ~2 dB lower). It contains:
  - room air, the card swing + UNTUNG stamp, camera whooshes, the steel lid clank, dust, the moth flutter;
  - the chip flying up, a bubble, the splash and the LABA tank filling (rising resonance + bubbles);
  - per station: valve squeak, water running in the pipe, the tank filling, the amount-chip pop + ding, the valve closing;
  - the racing clock ticks and the padlock click, the new box dropping into the basket;
  - the tap squeak and four drips (drop + "plink"), the number-card pops and the ≠ stamp;
  - bands, hologram fx, pembukuan row ticks + small fills, tag pops, the underline marker, beam/iris boom, end pops + chime.
- The cover was rendered with `scratchpad/ml/cover.cjs` (preview: `mp31/cover_final_s.jpg`).
- PNG dumps were deleted; only JPG sheets are kept. The preview `http.server` on 8941 was stopped.

## Renderer notes (applied from the start)
- Initial states live in a nested `tl0`, the first child of `tl` at 0 (the `PIN` map of earliest from-values). They are also
  applied with `gsap.set` at build, and `tl.render(0, true, true)` runs at the end of the build.
- Three camera-twin rigs (A wall + pipes + valves, B tanks + cash box + faucet, C chips + drips + splash + moth), so the
  software compositor never has to depth-sort the pipe plane against the tanks.
- The pipe SVG animates only attributes (`stroke-dashoffset`, `opacity`); valve wheels, the tap lever and the clock hands
  are HTML children that rotate inside their planes. No CSS filter on any 3D plane (the wall is 3600 × 4200).
- Water levels are `height` tweens on HTML children of the glass planes (front and both sides) plus a surface plane on a
  wrapper that moves in y; the surface plane only switches `visibility`.
- Every label of a 3D plane is inside that plane's own box (plates, padlock, chips).
- Elements that fade in by opacity get `visibility` sets, not `autoAlpha`, so a set never overrides the fade.

## Known issues / notes for the lead
- **Spoken length.** 26.9 s spoken (0.36 → 27.25), under the 28 s the batch-3 brief suggests, because the voice read fast;
  one take was kept to save credit (every word is clean in whisper). The film is 28.9 s with the end-card hold.
- **Hologram margin.** With the fast voice, `end − sol` is 4.38 s. The brand cut is pulled 0.35 s ahead of "Pembukuan"
  (bands on "beda") so the chest hologram is at full alpha for 4.05 s. "beda." is heard during the band sweep.
- **Frame 0.** The report card swings in over 0.02–0.57 and the robot rises 0.1–0.8, so the very first frame shows only the
  closed cash box under the fog.
- **Wide shot.** In S7 the whole wall is shown at about half scale (station labels ≈ 11 px); the number cards above carry
  the two key numbers.
- **Robot.** In S5 (11–13 s) the robot's raised arm overlaps the front-left corner of the cash box a little (no text there).
  As in the series, the navy pointing uses the far arm, so the gesture is subtle.
- **Tank labels in close-ups.** When the camera moves down, the LABA plate and the upper chips slide under the caption
  scrim (faded by design, never under readable caption text).

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. CUTS at `sol − 0.45` and `end − 0.01`. Light-wall host at x 150, y 1660, h 440.
- `lipsync.js` (1636 frames at 60 fps, talking fraction 0.85), `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP31.mp3`, `VO_MP31.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP31_UNTUNG_TAPI_UANG_NGGAK_ADA.png`.
- `.gitignore`: `out/`, `.hyperframes/`.
