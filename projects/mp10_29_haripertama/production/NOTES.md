# MasterPajak AI · Video 29 — Hari Pertama Pakai MasterPajak AI

1080×1920 · **32.8 s** (`TM.total` = `data-duration` = 32.8) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits. Preview port 8929.

## Concept: one day as a sky/sun timeline
One fictional seller's first day with the app ("Toko Mentari", invented) in one continuous shot, from dawn to night.

- **The sky** is screen space behind the 3D stage. It has five gradient layers (dawn, pagi, siang, sore, malam) that crossfade,
  plus a white top haze for caption legibility (off at night), drifting clouds, stars and a moon.
- **The sun** travels a big arc: it rises at the left in the hook, is high at siang, low and orange at sore, and sets at malam.
- **The diorama** is a small CSS-3D shop-room on a navy plinth (a cutaway room). It has:
  - a window with its **own little sky, sun and moon**, synced with the big sky, and a TUTUP → BUKA sign;
  - a **wall clock** whose hands spin through every time-lapse;
  - shelves with goods and a counter reading "TOKO MENTARI";
  - a phone on a stand, a desk lamp and a plant;
  - parcels that drop in at siang;
  - a **sunlight patch** that moves across the floor.

  Every wall, floor and counter plane has one tint overlay: dawn blue, then morning warm, clear, sunset orange and night navy.
  At night the lamp switches on (glow on the counter, the wall and the floor).
- **The HUD** at the top is the day track PAGI · SIANG · SORE · MALAM. The track fills, the active stop lights and done stops
  get a tick. A rolling clock shows 06.00 → 07.30 → 13.30 → 16.30 → 20.00.
- **The app card** has its own perspective stage above the diorama. At "Pagi" it flies out of the phone. At every time word it
  flips in 3D to the next screen: **Unggah foto nota → Catatan jualan → Laporan laba rugi → Asisten AI**.
- **Each time word starts a ~1 s time-lapse.** Sky, sun, tint, floor patch, wall clock, HUD clock and track all move together,
  and the camera orbits a step (yaw −22° → −4° over the day).
- **Brand (navy).** The day's four steps line up in one MasterPajak AI **Pembukuan** card, and a yellow trace line joins their
  four time icons ("semuanya nyambung"). Then the series end card plays.

It does not look like videos 16–28: there is no conveyor, river, quiz, kitchen, cabinet, relay, orbit, storm or archery.

## VO (ElevenLabs, client voice, eleven_v4, default AUTO tags)
The command was `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP29.mp3`
(no `--tags`). There was one take. `VO_MP29.mp3` is 31.04 s, and speech runs 0.35–31.15 on the timeline, so it is **≈30.8 s
spoken**, 71 words (limit 33 s).

`assets/audio/vo.wav` was made with
`ffmpeg -i production/vo/VO_MP29.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.35 – 3.90 | [playful] [excited] [curious] | Hari pertama pakai MasterPajak AI, ngapain aja sih? |
| L2 | 4.16 – 7.62 | [playful] [excited] | Pagi, kamu foto nota belanja, terus unggah lewat aplikasi. |
| L3 | 7.77 – 11.18 | [playful] [excited] | Siang, pesanan masuk, catatan jualannya jadi rapi. |
| L4 | 11.17 – 15.75 | [playful] [excited] | Sore, buka laporan: penjualan, biaya, sampai labanya kelihatan. |
| L5 | 15.70 – 20.63 | [playful] [excited] | Malam, masih ada yang belum jelas? Tanya asisten AI, jawabannya dari datamu sendiri. |
| L6 | 20.59 – 25.91 | [playful] [excited] | Dari foto nota sampai laporan laba rugi, semuanya nyambung di pembukuan MasterPajak AI. |
| L7 | 25.86 – 29.10 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L8 | 29.09 – 31.34 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

**Listen check.** I ran faster-whisper `small` (numpy input, `tools/fw_transcribe.py`) on the whole take. It heard every line,
and no tag was read aloud. Three spots needed a closer look:
- **"ngapain A aja"** is small's artifact. `medium` on the clip hears "ngapain aja sih?".
- **"datangmu"** is small's spelling. `medium` hears "datamu".
- **"sampai laporannya kelihatan"** came from small on the full take. Re-checking line 4 on its own, small hears
  "sampai **labanya** kelihatan". `medium` segments the same syllables as "sampailah banyak lihatan". The word spoken is "labanya".

## TM (real word times on the film timeline)
Keys are the JSON character alignment + 0.30 s. The alignment puts the first word of a line late, because the tag characters
compress it, so the line-start keys (hook, pagi, siang, sore, malam, sol, end, cta) and ngap / bio use the audio onset measured
from the energy envelope of `vo.wav`.

| key | t | word | key | t | word | key | t | word |
|---|---|---|---|---|---|---|---|---|
| hook | 0.35 | Hari | pes | 8.39 | pesanan | masih | 16.26 | masih |
| pert | 0.74 | pertama | msk | 8.78 | masuk | jelas | 16.94 | jelas? |
| mpai | 1.34 | MasterPajak | cat | 9.33 | catatan | tanya | 17.61 | Tanya |
| ngap | 2.62 | ngapain | jdr | 10.26 | jadi | asis | 17.90 | asisten |
| pagi | 4.16 | Pagi (L2) | rapi | 10.42 | rapi | jwb | 18.78 | jawabannya |
| kamu | 4.73 | kamu | sore | 11.17 | Sore (L4) | data | 19.58 | datamu |
| foto | 5.06 | foto | buka | 11.82 | buka | sol | 20.59 | Dari (L6) |
| nota | 5.26 | nota | lap | 12.10 | laporan | fn | 20.98 | foto nota |
| blj | 5.42 | belanja | pj | 12.73 | penjualan | lr | 21.98 | laporan laba rugi |
| ungg | 6.38 | unggah | by | 13.50 | biaya | smua | 23.207 | semuanya |
| apl | 6.94 | aplikasi | laba | 14.54 | labanya | nyb | 23.58 | nyambung |
| siang | 7.77 | Siang (L3) | kel | 14.90 | kelihatan | pmb | 24.193 | pembukuan |
| malam | 15.70 | Malam (L5) | end | 25.86 | Jualan (L7) | mpai2 | 24.78 | MasterPajak |
| urus | 27.28 | pajaknya | cta | 29.09 | Coba (L8) | bio | 30.51 | Link |

- **Total.** `total` = 32.8, which is the last word end (≈31.2) + 1.6 s.
- **Brand gap.** `end − sol` = 5.27 s. The brand chest hologram is on screen from `sol+0.5` to `end−0.3` (**4.47 s**) and at full
  alpha for 4.0 s.
- **End gap.** `total − end` = 6.94 s. The end-card hologram runs from `end+0.75` to the end.

## Scenes (film seconds)
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 4.16 | Hook, dawn | The camera starts close on the dim shop at dawn (lavender sky, blue room tint) and pulls back to the wide diorama by 4.4. The sun rises at the left edge and birds chirp. The HUD drops in at 0.9 with clock 06.00. Captions: "Hari pertama pakai / MasterPajak AI, / ngapain aja sih?", with stabilo on "ngapain aja". The sign flips TUTUP → BUKA at 2.42. The robot rises at 0.15–0.85 and does a morning stretch (both arms up), then a head tilt with a hand to the chin on "ngapain". |
| T | 3.36 – 4.76 | Dawn → pagi | The sky crossfades, the haze comes in, the sun reaches the morning spot, the room tint warms, the floor patch appears and the wall clock spins to 07.30. The HUD stop PAGI lights at 4.14. |
| S2 | 4.16 – 7.77 | Pagi | Caption "Pagi, / unggah foto nota." with stabilo. The card **flies out of the phone** at 4.06–4.86. "Unggah foto nota" has a camera viewfinder with the nota photo; the shutter flashes on "foto" (5.04), and the nota on the counter flashes too. On "unggah" the upload bar fills and a scan line passes. On "aplikasi" the fields fill: Tanggal "Hari ini · 07.40", Kategori "Kemasan", Nominal "Rp60.000". "Tersimpan ✓" appears at 7.39. The robot points at the card, nods, then pumps an arm. |
| T | 7.47 – 8.47 | Pagi → siang | Time-lapse: the sun rises to the top, the clock moves to 13.30 and the camera orbits a step. The card flips P → S at 7.57–8.29. |
| S3 | 7.77 – 11.17 | Siang | Caption "Siang, / pesanan masuk," then "catatan jadi rapi." with stabilo on "rapi". Four orders pop in as **tilted notification toasts** (8.33–8.90) while three parcels drop onto the floor. On "catatan jualannya" they fly into tidy table rows (9.39–9.81). On "rapi" the total row "4 PESANAN · TOTAL Rp650.000" and a yellow **"✓ Rapi"** stamp appear. The robot hops, then pumps an arm. |
| T | 10.87 – 11.87 | Siang → sore | Time-lapse: the sky turns golden, the sun goes low at the right and turns orange, the clock moves to 16.30, and the floor patch stretches to the left. The card flips S → O at 10.97–11.69. |
| S4 | 11.17 – 15.70 | Sore | Caption "Sore, / buka laporan." then "labanya kelihatan.", each with stabilo. The "Laporan laba rugi" card fills on the words: Penjualan Rp650.000 (12.69), Modal barang −Rp390.000 (13.44), Biaya kemasan −Rp60.000 (13.70). The bars grow. **LABA Rp200.000** pops at 14.48 and pulses on "kelihatan". The robot points, nods, then raises both arms up on "labanya". |
| T | 15.40 – 16.40 | Sore → malam | The sun sets and fades out, the sky turns navy, stars and the moon come up at the left, and the room goes dark. The **lamp switches on** at 16.05. The clock shows 20.00, and the HUD switches to its night colours. The card flips O → M at 15.50–16.22. |
| S5 | 15.70 – 20.59 | Malam | Caption "Malam, / masih belum jelas?" then "tanya asisten AI." with a yellow underline. On the "Asisten AI" chat card the question "Laba hari ini dari mana?" pops (16.31), typing dots run on "Tanya asisten AI", and the answer arrives line by line from "jawabannya" (18.73): "Dari datamu hari ini: penjualan Rp650.000, dikurangi modal barang Rp390.000 dan kemasan Rp60.000. Jadi labanya **Rp200.000**." Rp200.000 gets stabilo on "datamu". Crickets play. The robot (night lighting) looks up at the moon, tilts its head, points at the chat and nods. It ducks out at 19.84–20.31. |
| T | 20.11 – 20.67 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S6 | 20.59 – 25.86 | Brand | The robot rises half-body bottom-left with the **chest hologram** (x 510–930, y ≈ 1450–1600). The "Pembukuan · MasterPajak AI · hari pertama" card swings up. Four day rows slide in on "foto nota" … "laporan laba rugi": PAGI · FOTO NOTA Kemasan −Rp60.000; SIANG · CATATAN JUALAN 4 pesanan Rp650.000; SORE · LAPORAN LABA RUGI Laba hari ini Rp200.000; MALAM · ASISTEN AI Pertanyaan terjawab ✓ dari datamu. On "nyambung" the yellow **trace line** draws down through the four time icons, which light one by one. The header pulses on "pembukuan", the logo on "MasterPajak". Captions: "dari foto nota sampai / laporan laba rugi," then "semuanya nyambung di / pembukuan MasterPajak AI.", each with an underline. |
| T | 25.34 – 26.41 | Beam + iris | Series. |
| S7 | 25.86 – 32.8 | End card | Series template: the tagline in two lines, the CTA pill "Coba kalkulator gratis" (pulse at 29.99) and "Link di bio". The robot waves, points and waves again, with the logo hologram on the left (x 150–570). |

## Numbers (every number on screen is "Ilustrasi data"; the arithmetic is exact)
**Pagi · nota** (photo in the viewfinder):
- Plastik 40.000 + Lakban 20.000 = **Rp60.000**
- It is read into the fields as Kategori **Kemasan**, Nominal **Rp60.000**.

**Siang · catatan jualan** (4 pesanan):

| time | order | amount |
|---|---|---|
| 09.15 | Kaos polos ×2 | Rp150.000 |
| 10.40 | Tote bag | Rp95.000 |
| 11.55 | Kemeja linen | Rp225.000 |
| 13.05 | Hoodie | Rp180.000 |

150.000 + 95.000 + 225.000 + 180.000 = **Rp650.000** ✓

**Sore · laporan laba rugi (hari ini):**
- Penjualan **Rp650.000** (the siang total)
- − Modal barang **Rp390.000** (an illustrative cost of the four items sold, 60 % of penjualan)
- − Biaya kemasan **Rp60.000** (the pagi nota)
- = **LABA Rp200.000**

650.000 − 390.000 − 60.000 = **200.000** ✓

The bar widths are proportional to penjualan: 100 %, 60.00 % (390/650) and 9.23 % (60/650).

**Malam · asisten AI** repeats exactly the same numbers (650.000, 390.000, 60.000 → 200.000).

**Brand pembukuan** repeats −Rp60.000, Rp650.000 (4 pesanan) and Rp200.000.

Clock times (06.00 → 07.30 → 13.30 → 16.30 → 20.00, the nota at 07.40, the orders 09.15–13.05) are times of day, not deadlines.

## Labels and brand rules
- **Labels.**
  - Every app card (P, S, O, M) carries both **"Ilustrasi data"** and **"Simulasi alur"** in its header.
  - The brand Pembukuan card carries both too.
  - A **"Simulasi alur"** chip sits bottom-left (x 60, y 1548) for the whole day part (0.9 → 20.04).
- **No forbidden content.**
  - No tax rate, deadline, penalty, guarantee, result promise or invented statistic.
  - "jadi rapi" and "kelihatan" describe the simulated flow, not a business result.
- **Names and features.**
  - "MasterPajak AI" is spelled that way everywhere.
  - The features named are unggah foto nota (via aplikasi), catatan jualan → pembukuan, laporan laba rugi and asisten AI, plus
    the kalkulator gratis on the end card.
  - The tagline and CTA match the brief exactly.
- **No real brands.** There are no marketplace, bank, e-wallet, chat-app or government names, logos or colours. "Toko Mentari"
  is an invented shop, and the sales and chat UIs are generic.
- **Robot and hologram.**
  - The robot appears in every scene. In the day part it is a small full-body host bottom-right (x 925, y 1600, h 500), below
    and to the right of every card, caption and the "Rapi" stamp. It never covers text.
  - In the brand scene the card ends above its antenna.
  - The holograms stay inside x 150–930 and y ≤ 1600.
- **Text containment.** `contain.cjs` (transforms off) reports "no text sticks out of its box". It found one case, the NOTA
  heading's line box in the viewfinder, which is fixed. A `buildReady["fit"]` step shrinks screen captions to 940 px if a font
  renders wider. It shrinks "pembukuan MasterPajak AI." on the brand scene.

## QA done (final build)
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`). The full pass rtA has 32 frames covering every scene, every flip /
  time-lapse midpoint, the band cut, the beam/iris and the end card. The fix pass rtB has 8 frames: the HUD contrast at dawn,
  the nota photo, two flips, the night switch, the brand cut, the brand rows and the end card. Contact sheets (JPG only, PNG
  dumps deleted):
  - `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp29/rtA_1.jpg`: 0–13.8 s
  - `…/mp29/rtA_2.jpg`: 15.2–32.6 s
  - `…/mp29/rtB.jpg`: the fix pass
  - Half-resolution detail strips: `…/mp29/det1.jpg` (pagi / siang / sore cards) and `…/mp29/det2.jpg` (malam, brand, pagi).
- **`hyperframes validate`**: 0 errors. The 4 warnings are GL "GPU stall due to ReadPixels". The contrast warnings are of the
  usual kinds: hidden split-caption glyphs and the series marquee. The HUD labels and the brand-row small caps were darkened
  after the first run.
- **Frame-edge sweep** (`edgecheck.cjs`, every 0.25 s over 0–32.6): no visible text crosses a frame edge. The only hits are the
  series marquee (clipped by its band) and the hidden top digit of the HUD clock strip (clipped by its box).
- **Lip-sync**: `tools/lipsync.py` turned `vo.wav` into `lipsync.js` (1876 frames at 60 fps, talking fraction 0.86).
- **SFX**: `tools/sfx.py` writes `assets/audio/sfx.wav`, 32.8 s, fully synthesised, −25.2 dB RMS (Video 14 is −25.2). It
  contains:
  - dawn air and bird chirps, the sign flip
  - four time-lapses (swell + the clock ratchet), HUD stop pops and dings
  - the card fly-out, shutter, upload ticks, field pops, the "Tersimpan" ding
  - notification blips, parcel knocks, row snaps, the "Rapi" chime
  - report row pops and bar whooshes, the LABA ding
  - the lamp click, crickets, send / typing / reply blips
  - bands, hologram fx, the pembukuan row pops and trace-line shimmer, beam/iris, end pops and chime

## Renderer notes (batch-3 lessons applied from the start)
- **Pins.** Initial states are pinned in a nested `tl0`, the first child of `tl` at 0. Every `fromTo` records its earliest
  from-value, and `pinAll` both `gsap.set`s it at build and pins it in `tl0`. `tl.render(0, true, true)` runs at the end of the
  build, so frame 0 is the pinned state.
- **No CSS filter anywhere in the 3D world.** The 3600 px ground and the walls only get a tint child whose `backgroundColor`
  tweens. The only blur is the series bottom DOF (`backdrop-filter`, screen space).
- **SVG transforms as plain strings.** The wall-clock hands tween their `transform` attribute as `rotate(a 60 60)` strings, with
  no GSAP SVG transform cache.
- **The cards have their own perspective stage (`#w3`)**, drawn over the diorama, so they are never depth-sorted against room
  planes. The sun, moon and clouds are screen space behind the stage. The sun's arc is a chain of linear x/y segments on a
  cosine time curve, with no onUpdate.
- **Layout.** It was placed with a projection model of the rig (`scratchpad/mp29/proj.cjs`). It keeps the room below the cards,
  the window visible under the card, and the robot corner free of anything that matters.

## Known issues / notes for the lead
- **Robot timing.** As in the series, the robot rises in at 0.15–0.85 s, so frame 0 shows only the dawn shop with no caption.
  The HUD arrives at 0.9 s.
- **Small text in the photo.** The nota photo inside the viewfinder (Plastik 40.000, Lakban 20.000) is about 13–15 px. It is a
  photo; the extracted fields beside it carry the spoken values at 29 px.
- **Flips are intentional cuts.** The card flips (0.72 s each) hide the card content for about 0.3 s at each time word. During
  that time the day changes behind them (time-lapse).
- **Modal barang has no on-screen source.** Rp390.000 appears first in the sore report and has no earlier on-screen source in the
  film. It is labelled Ilustrasi data like every other number.
- **The day is simplified.** The report covers one day, and the morning kemasan purchase is expensed on the same day. This is an
  illustrative simplification.
- **Pointing gesture.** As in the series, the brand-scene pointing uses the far arm, so the gesture is subtle.

## Files
- `index.html` (TM at the top), `robot_perf.js` (choreography; CUTS at `sol−0.05` and `end−0.01`), `lipsync.js`.
- `assets/audio/vo.wav` and `sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP29.mp3`, `VO_MP29.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `.gitignore` holds `out/`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP29_HARI_PERTAMA.png`:
  - The headline reads "HARI / PERTAMA" (stabilo) with "dari pagi sampai malam".
  - A day dome runs from a morning sky to a night sky. A dashed yellow arc carries four stops: PAGI "foto nota", SIANG "catatan
    rapi", SORE "laporan" and MALAM "tanya AI".
  - The film's Toko Mentari diorama sits under it, and the live robot points up.
  - There are no numbers, and everything sits inside the 4:5 crop (y 285–1635).
