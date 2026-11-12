# MasterPajak AI · Video 24 — Laporan Laba Rugi dalam 30 Detik

1080×1920 · **32.4 s** (`TM.total` = `data-duration` = 32.4) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept: a cooking show
One **CSS-3D light kitchen** under a moving camera:
- a **recipe card** "RESEP · Laporan Laba Rugi" standing on the counter (back right), with Bahan, Langkah and "Porsi: 1 bulan";
- a **digital kitchen scale** with a mixing bowl on top; its navy **LCD** shows a label and a rolling odometer;
- four **measuring cups** on a wall **shelf** behind the scale: Modal barang (navy) and the three Biaya cups Ongkir / Iklan /
  Kemasan (yellow), each labelled with its portion;
- a **jar of PENJUALAN coins** that flies in from off-frame only for the pour;
- a subway-tile backsplash, bokeh, depth of field top and bottom.

The recipe structure drives the film. Bahan = penjualan, modal barang, biaya. Langkah = take the portions out of the bowl one by
one. Hasil = what stays in the bowl is the laba. A four-step HUD (Bahan · Langkah 1 · Langkah 2 · Hasil) and a kitchen timer
that drains until the result track progress. On the brand cut (navy) the recipe card flips into a MasterPajak AI
**"Laporan laba rugi"** with the same numbers, then the series end card plays.

## VO (ElevenLabs, client voice, eleven_v4, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP24.mp3` (no `--tags`), one
take. `VO_MP24.mp3` is 30.72 s; speech runs 0.36–30.74 on the timeline, so it is **≈30.4 s spoken** (limit 33 s).
`assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP24.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
Film times below include that +0.30 s.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.36 – 3.65 | [playful] [excited] | Resep laporan laba rugi, tiga puluh detik. Yuk, masak! |
| L2 | 3.88 – 7.31 | [playful] [excited] | Bahannya tiga: penjualan, modal barang, sama biaya. |
| L3 | 7.57 – 11.46 | [playful] [excited] | Langkah satu: penjualan dikurangi modal barang, jadi laba kotor. |
| L4 | 11.72 – 15.99 | [playful] [excited] | Langkah dua: kurangi biayanya satu-satu. Ongkir, iklan, kemasan. |
| L5 | 16.23 – 19.61 | [playful] [excited] | Hasilnya: laba. Itu untung kamu yang sebenarnya. |
| L6 | 19.89 – 25.11 | [playful] [excited] | MasterPajak AI bantu nyusun laporan laba rugi dari catatan jualan dan biayamu, tiap bulan. |
| L7 | 25.33 – 28.36 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L8 | 28.56 – 30.74 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

**Listen check.** faster-whisper `small` (numpy input, `tools/fw_transcribe.py`) heard every word, and no tag was read aloud:

```
Resep laporan labarugi, 30 detik! / Yuk, masak! / Bahannya tiga, penjualan, modal barang, sama biaya. /
Langkah satu, penjualan di kurangi modal barang, jadi labakotor. / Langkah dua, kurangi biayanya satu-satu, ongkir, iklan, kemasan. /
Hasilnya, laba! Itu untung kamu yang sebenarnya. / Master Pajak AI bantu nyusun laporan labarugi dari catatan jualan dan biayamu,
tiap bulan. / Jualan jalan terus, pajaknya AI yang urus. / coba kalkulator gratis, link di bio.
```
"labarugi", "di kurangi" and "labakotor" are only whisper's spelling. The voice reads "tiga puluh detik" as words.

## TM (every key is a real word time: JSON character alignment + 0.30)
The alignment puts the first word of each line 0.1–0.3 s **late**, because the tag characters compress it. Line-start keys
therefore use the audio onset of that word, measured from the energy envelope of `vo.wav`. All other keys are alignment + 0.30.

| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.36 | Resep (L1) | krg2 | 12.727 | kurangi |
| lap | 0.78 | laporan | satu | 13.50 | satu-satu |
| dtk | 1.90 | tiga (puluh detik) | ong | 14.38 | Ongkir |
| yuk | 2.94 | Yuk | ikl | 15.02 | iklan |
| masak | 3.34 | masak | kem | 15.50 | kemasan |
| bahan | 3.88 | Bahannya (L2) | has | 16.23 | Hasilnya (L5) |
| pj | 5.02 | penjualan | laba | 17.073 | laba |
| mb | 5.82 | modal | unt | 18.22 | untung |
| by | 6.86 | biaya | sbn | 18.98 | sebenarnya |
| l1 | 7.57 | Langkah (satu, L3) | sol | 19.89 | MasterPajak (L6) |
| pj2 | 8.54 | penjualan | lr | 21.50 | laporan |
| krg | 9.14 | dikurangi | cat | 22.70 | catatan |
| mb2 | 9.62 | modal barang | bia | 23.70 | biayamu |
| lk | 10.78 | laba kotor | bln | 24.487 | tiap bulan |
| l2 | 11.72 | Langkah (dua, L4) | end | 25.33 | Jualan (L7) |
| urus | 26.753 | pajaknya | cta | 28.56 | Coba (L8) |
| bio | 30.14 | Link | total | 32.40 | last word end 30.78 + 1.62 |

Gaps that hold:
- `end − sol` = 5.44 s. The brand chest hologram is at full alpha from `sol+0.72` to `end−0.55` (4.2 s) and on screen from
  `sol+0.5` to `end−0.3` (4.6 s).
- `total − end` = 7.07 s. The end-card hologram runs from `end+0.75` to the end (6.3 s).

## Scenes
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 3.88 | Hook, kitchen wide | The camera drifts in on the set: scale + bowl left, shelf with the four cups, recipe card back right. Text: "Resep / laporan laba rugi, / 30 detik." with stabilo on "30 detik." and a kitchen timer that pops and winds on "tiga puluh detik". On "Yuk, masak!" a navy sticker pops. The robot rises bottom-right with a host flourish, points up at the timer, then hops with both arms up. |
| T | 3.63 – 4.63 | Push to the card | The hook text sinks first, then the camera pushes in on the recipe card. |
| S2 | 3.88 – 7.57 | Bahan | The HUD drops in with "Bahan" active, and the timer starts draining. Caption "Bahannya tiga:" with stabilo on "tiga". Recipe rows write in with a yellow flash on their words: Penjualan Rp10.000.000 at 5.0, Modal barang Rp5.500.000 at 5.8, Biaya Rp2.300.000 at 6.8. The sub-rows Ongkir / Iklan / Kemasan follow (7.06–7.30). The robot points at each row and nods. |
| T | 7.42 – 8.27 | Whip pan | A directional motion-blur whip (Video 9/20 pattern) to the scale station. "Bahan ✓" turns yellow and "Langkah 1" becomes active. |
| S3 | 7.57 – 11.72 | Langkah 1 | The jar flies in from top-left, tips over the bowl and pours (8.4–9.3). The coin mound rises, and the LCD reads PENJUALAN and rolls 0 → Rp10.000.000. On "dikurangi modal barang" a chip "−Rp5.500.000" rises out of the bowl and lands in the Modal barang cup, which fills, ticks and hops. The mound sinks, and the LCD reads "− MODAL BARANG" and rolls to Rp4.500.000. On "laba kotor" the LCD label becomes **LABA KOTOR** with a flash. Caption: "penjualan − modal barang / = laba kotor" (stabilo). |
| S4 | 11.72 – 16.23 | Langkah 2 | Caption "kurangi biayanya satu-satu." On "satu-satu" the three biaya cups hop in turn. On each word a chip leaves the bowl for its cup, a caption chip pops, and the LCD steps down: ongkir −Rp800.000 → Rp3.700.000, iklan −Rp1.200.000 → Rp2.500.000, kemasan −Rp300.000 → Rp2.200.000. The robot points and follows each chip. |
| S5 | 16.23 – 19.89 | Hasil | The timer rings (ding) and the HUD shows "Hasil". The camera pushes in on the scale, and the shelf and cups go soft behind the captions. On "laba" the LCD reads **LABA ✓ Rp2.200.000** with a flash and sparkles, and the robot cheers. Captions: "Hasilnya: / laba." then "untung kamu yang sebenarnya." with stabilo on "sebenarnya." |
| T | 19.41 – 19.97 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S6 | 19.89 – 25.33 | Brand: laporan laba rugi | The robot rises half-body bottom-left with the **chest hologram** (x 510–930, y ≈ 1450–1600). The recipe card flies in, then **flips** at 21.15 into the "Laporan laba rugi · MasterPajak AI · bulan ini" card. Its seven rows slide in, and the LABA value pops. On "catatan jualan" the Penjualan row lights. On "biayamu" the Modal barang / Ongkir / Iklan / Kemasan rows light. On "tiap bulan" last month's reports fan out behind. Captions: "MasterPajak AI bantu nyusun / laporan laba rugi." then "dari catatan jualan & biayamu, / tiap bulan.", each with an underline. |
| T | 24.81 – 25.88 | Beam + iris | Series. |
| S7 | 25.33 – 32.4 | End card | Series template: the tagline in two lines, the CTA pill "Coba kalkulator gratis" (with pulse) and "Link di bio". The robot waves, points and waves again, with the logo hologram on the left (x 150–570). |

## The recipe arithmetic (every number on screen, all "Ilustrasi data")
Bahan (recipe card):
- Penjualan **Rp10.000.000**
- Modal barang **Rp5.500.000**
- Biaya **Rp2.300.000**, made up of:
  - Ongkir **Rp800.000**
  - Iklan **Rp1.200.000**
  - Kemasan **Rp300.000**

Check: 800.000 + 1.200.000 + 300.000 = **2.300.000** ✓

Langkah, as the scale LCD shows them in order:

| step | LCD label | calculation | LCD shows |
|---|---|---|---|
| pour | PENJUALAN | 0 + 10.000.000 | **10.000.000** |
| 1 | − MODAL BARANG → LABA KOTOR | 10.000.000 − 5.500.000 | **4.500.000** |
| 2a | − ONGKIR | 4.500.000 − 800.000 | **3.700.000** |
| 2b | − IKLAN | 3.700.000 − 1.200.000 | **2.500.000** |
| 2c | − KEMASAN | 2.500.000 − 300.000 | **2.200.000** |
| Hasil | LABA ✓ | | **2.200.000** |

Cross-check in one line: 10.000.000 − 5.500.000 − 2.300.000 = **2.200.000** ✓

The brand "Laporan laba rugi" repeats exactly these rows:
- Penjualan Rp10.000.000
- −Rp5.500.000 Modal barang
- **Laba kotor Rp4.500.000**
- −Rp800.000 Ongkir
- −Rp1.200.000 Iklan
- −Rp300.000 Kemasan
- **LABA Rp2.200.000**

The four portion chips that fly into the cups carry the same values: −Rp5.500.000, −Rp800.000, −Rp1.200.000, −Rp300.000. The
coin mound height follows the bowl's contents (1 → 0.5 → 0.43 → 0.3 → 0.27).

## Brand-rule checks
- **Labels.**
  - "Ilustrasi data" appears on the recipe card (front and brand copy), on the scale body under the LCD, and as a screen chip
    bottom-left for the whole kitchen part from 4.2 s, which covers the jar, chips and cups. It also appears on the laporan card.
  - "Simulasi alur" appears on the MasterPajak AI laporan card, the only app UI in the film.
  - The kitchen is a metaphor, not an app flow.
- **No tax rates, deadlines, penalties, guarantees or invented statistics.** "tiap bulan" describes the report period only.
  "30 detik" is the video's recipe-format title and refers to the explanation, not a product promise.
- **Names and features.**
  - "MasterPajak AI" is spelled that way everywhere.
  - The only feature named is laporan laba rugi, plus the kalkulator gratis on the end card.
  - The tagline and CTA match the brief exactly.
  - No marketplace, bank, e-wallet or government marks appear.
- **Robot and hologram.**
  - The robot appears in every scene and never stands over text: small full-body bottom-right in the kitchen, with every card,
    cup and caption left of x 800 or above y 1330.
  - The holograms stay inside the safe zone.
  - In the brand scene the card ends above the antenna.
- **Text containment.** `contain.cjs` (scratchpad `mp24/`, transforms disabled) reports "no text sticks out of its box". It found
  and fixed one case, the jar label "Rp10.000.000". A `buildReady["fit"]` step shrinks screen captions if a font renders wider
  than planned.

## QA done (final build)
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`): 36 frames covering every scene, every cut midpoint and the end card.
  Contact sheets:
  - `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp24/QA_final_A/contact-sheet-1.jpg`
    and `contact-sheet-2.jpg`: hook → Langkah 1
  - `…/mp24/QA_final_B/contact-sheet-1.jpg` and `contact-sheet-2.jpg`: Langkah 2 → brand start
  - `…/mp24/QA_final_C/contact-sheet-1.jpg` and `contact-sheet-2.jpg`: caption hand-overs, report, end
- **`hyperframes validate`**: 0 errors, and no 404s because `lipsync.js` exists. The contrast warnings are all of one kind:
  hidden split-caption glyphs, the series marquee, the cups while blurred, and 3D-measured labels. The approved videos have the
  same kind.
- **Frame-edge sweep** (`ml/edgecheck.cjs`, every 0.2 s over 0–32.3): no held frame cuts text. The only hits are:
  - 4.0–4.2: during the push from the hook to the card, the shelf cups pass the left edge;
  - 7.8: during the whip pan, which is blurred;
  - the series marquee.
- **Lip-sync**: `tools/lipsync.py` turned `vo.wav` into `lipsync.js` (1857 frames at 60 fps, talking fraction 0.83).
- **SFX**: `tools/sfx.py` writes `assets/audio/sfx.wav`, 32.4 s, fully synthesised, about −25.7 dB RMS (Video 14 is −25.2). It
  contains:
  - room tone, title pops, a timer ratchet, a "Yuk, masak!" sizzle
  - recipe-row scribbles, soft timer ticks while the recipe runs
  - the whip, a coin cascade for the pour, odometer ticks, portion whooshes with clinks into the cups, cup knocks
  - the kitchen-timer bell on "Hasilnya", sparkles
  - bands, hologram fx, the card flip, row pops, the beam/iris boom, end pops and a chime

## Real-renderer findings (fixed; worth knowing)
1. **Multi-tween SVG scales drift away under the runtime's seek.** The bowl's coin mound was tweened with GSAP
   `scaleY` + `svgOrigin` across five tweens. It was **invisible in the real renderer** but fine in `snap.cjs`, because the
   runtime seeks with `totalTime(t ± ε)` and then `totalTime(t)`, and GSAP's smoothOrigin offsets accumulate. All SVG parts
   (mound, cup fills, timer hands) now tween their **`transform` attribute as a plain string** (`matrix(1 0 0 s 0 oy·(1−s))`,
   `rotate(a cx cy)`), with no transform cache.
2. **A filter on a very wide 3D plane disappears under software compositing.** The focus-pull `filter` was pinned at 0 on the
   5200 px backsplash, and it vanished in the real renderer. Now:
   - the wall is 4000 px wide and never filtered;
   - the cups and shelf get their filter only from the focus pull at 16.28 (a raw `fromTo`, not pinned).

   `scratchpad/mp24/snapR.cjs` reproduces the renderer's software compositing (`--disable-gpu-compositing`) for quick checks.
3. **Pins come from the earliest from-value.** The cup "hop" tween started from `y: 0`, so the pin stood the cups on the counter
   instead of the shelf. It now uses `y: CUPY`.
4. **The layout was solved numerically.** `scratchpad/mp24/proj.py` is a projection model of this camera rig, and it matches the
   renderer within a few px. It placed the station, the card and the shelf so that:
   - the card is out of frame in the scale shots;
   - the shelf is out of frame in the card shot;
   - nothing sits in the robot's corner.
5. As in Videos 14 and 19, the jar, coins and chips fly in an **overlay twin rig** (`#w1b`), so they are never depth-sorted
   against the bowl or scale planes. Initial states are pinned in the nested `tl0` (the first child of `tl`), and
   `tl.render(0, true, true)` runs at the end of the build.

## Files
- `index.html` (TM at the top), `robot_perf.js` (choreography; CUTS at `sol−0.05` and `end−0.01`), `lipsync.js`.
- `assets/audio/vo.wav` and `sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP24.mp3`, `VO_MP24.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP24_LABA_RUGI.png`:
  - The headline reads "RESEP / LABA RUGI" (stabilo) with "dalam 30 detik" and a timer.
  - The film's recipe card is tilted in 3D, showing bahan, langkah ✓ and "HASIL · LABA ✓".
  - The bowl of coins sits on the scale, whose LCD reads only "LABA ✓".
  - The pill reads "penjualan − modal − biaya = laba", and the live robot points.
  - There are no numbers, and everything sits inside the 4:5 crop (y 285–1635).

## Known issues / notes for the lead
- **Odometer motion.** For about 0.5–0.8 s per step the LCD shows rolling intermediate digits (odometer by design).
- **Jar entry.** The jar enters from the top-left edge (≈8.0–8.3 s), and its label is briefly cut by the frame while it flies in.
- **Small cup labels.** The cup labels are small on the wide shots (about 17–20 px on screen). The flying chips and the caption
  chips carry the spoken amounts and names.
- **Caption gap.** Between "Langkah dua:" (11.72) and "kurangi" (12.73) only the HUD pill "Langkah 2" is lit, with no caption.
  This is intentional: it gives a short breath before the second step.
- **Pointing gesture.** As in the series, the navy pointing uses the far arm, so the gesture is subtle.
- **Slow machine.** The machine was heavily loaded (load ≈ 21), so `snap.cjs` needed a 90 s timeout (the local copy is
  `scratchpad/mp24/snap.cjs`).
