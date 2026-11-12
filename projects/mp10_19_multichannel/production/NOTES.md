# MasterPajak AI · Video 19 — Jualan di Banyak Tempat, Catatannya Satu

1080×1920 · **33.7 s** (`TM.total` = `data-duration` = 33.7) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept
One CSS-3D **paper map** under a moving camera. Three generic places are drawn as **rivers**:
**Toko online A** (royal), **Toko online B** (periwinkle) and **Media sosial** (yellow). The colours come from the brand palette
only. There are no marketplace or social-media names, logos or colours, and the icons are a generic storefront and a chat
bubble with a heart. Each river carries the same three kinds of things in **its own shape**:

| | pesanan | potongan biaya | pencairan |
|---|---|---|---|
| A · square tiles | PESANAN #A-1021 | POTONGAN −Rp9.800 | PENCAIRAN Rp1.250.000 |
| B · pills | ORD-88213 | Admin −Rp6.500 | Cair Rp780.000 |
| C · chat bubbles | "Kak, pesan 2 ya" Rp150.000 | "Ongkirnya berapa?" Rp18.000 | "Udah transfer ya" Rp168.000 (= 150.000 + 18.000) |

Each river ends in its **own pool** with its own scattered note: a sheet "Rekap toko A", a handwritten "Catatan toko B" and a chat
screenshot "Chat pesanan".

On the brand cut (navy), the three glowing rivers flow into **one lake**. The lake stands up as **one pembukuan**, with every row
tagged by its source so it can be traced. Then the **rekonsiliasi bulanan** card checks each place's recorded total against the
money that came in.

## VO (ElevenLabs, client voice `plgKUYgnlZ1DCNh54DwJ`, eleven_v4, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP19.mp3` (no `--tags`).
Output: `VO_MP19.mp3` and `VO_MP19.json`, 31.76 s. `assets/audio/vo.wav` holds the VO delayed by 0.30 s (48 kHz mono). Film times
below include that +0.30 s.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.38 – 3.82 | [playful] [excited] [curious] | Jualan di banyak tempat, catatannya kepencar ke mana-mana? |
| L2 | 4.05 – 7.42 | [playful] [excited] | Toko online A, toko online B, sama media sosial. |
| L3 | 7.71 – 12.23 | [playful] [excited] | Bentuknya beda-beda: ada pesanan, potongan biaya, sampai pencairan. |
| L4 | 12.98 – 16.41 | [playful] [excited] [sighs] | Kalau dicatat terpisah-pisah, ngitung untungnya jadi ribet. |
| L5 | 16.68 – 21.35 | [playful] [excited] | MasterPajak AI bantu satukan semuanya jadi satu pembukuan yang bisa ditelusuri. |
| L6 | 21.49 – 26.47 | [playful] [excited] | Terus rekonsiliasi bulanan bantu cek, angka tiap tempat udah cocok sama uang yang masuk. |
| L7 | 26.54 – 29.74 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L8 | 29.82 – 32.06 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

**Listen check.** faster-whisper `small` (numpy input) heard every word, and no tag was read aloud. Its transcript:

```
Jualan di banyak tempat, catatannya kepencara kemana-mana. / Toko online A, Toko online B, sama media sosial. /
Bentuknya beda-beda, ada pesanan, potongan biaya, sampai pencairan. / Haaa, kalau di catat terpisah-pisah, ngitung untungnya jadi ribet. /
Master Pajak AI bantu satukan semuanya jadi satu pembukuan yang bisa ditelusuri. / Terus, rekonciliasi bulanan bantu cek, angka tiap tempat
sudah cocok sama uang yang masuk. / Jualan jalan terus, pajaknya AI yang urus. / Coba kalkulator gratis. Link di bio.
```

- "Haaa" is the `[sighs]` tag performed as a sigh before L4, as intended.
- "kepencara", "rekonciliasi" and "sudah" are whisper spellings of the spoken words.

## TM (every key is a real word time from the JSON alignment + 0.30)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.38 | Jualan (L1) | pisah | 12.98 | Kalau (L4) |
| hookB | 1.98 | catatannya | ter | 13.50 | terpisah-pisah |
| kep | 2.54 | kepencar | untung | 14.98 | untungnya |
| chA | 4.053 | Toko (L2) | ribet | 15.58 | ribet |
| chB | 5.18 | toko (B) | sol | 16.675 | MasterPajak (L5) |
| chC | 6.46 | media | satu | 17.82 | satukan |
| bent | 7.713 | Bentuknya (L3) | pemb | 19.34 | pembukuan |
| pes | 9.14 | pesanan | telus | 20.46 | ditelusuri |
| pot | 9.82 | potongan | rek | 21.488 | Terus (L6) |
| cair | 11.34 | pencairan | cek | 23.50 | cek |
| end | 26.54 | Jualan (L7) | cocok | 24.94 | cocok |
| cta | 29.816 | Coba (L8) | masuk | 25.94 | masuk |
| bio | 31.26 | Link | total | 33.70 | last word end 32.06 + 1.64 |

Gaps that hold:
- The brand hologram is at full alpha from `sol+0.72` to `end−0.3`, which is 9.2 s.
- The end-card hologram runs from `end+0.75` to the end, which is 6.4 s.

## Scenes
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 4.05 | Hook (paper map) | The rivers are already partly drawn on frame 0 and finish drawing. Three pools bloop in. On "kepencar" the three notes pop up at the three pools and drift apart. Text: "Jualan di banyak tempat, / catatannya / kepencar?", with stabilo on "kepencar?". The robot rises bottom-right with a puzzled tilt and a small shrug. |
| T | 3.9 – 4.95 | Fly-over | The camera flies forward over the map to the springs, and the notes fold away. |
| S2 | 4.05 – 7.71 | Three places | A sign rises out of each spring as it is named: "Toko online A" at 4.05, "Toko online B" at 5.18, "Media sosial" at 6.46. That river then starts carrying its three tokens. The robot points at each sign. An "Ilustrasi data" chip sits bottom-left from 4.35. |
| T | 7.66 – 8.8 | Crane | The camera cranes back over the mid-river. |
| S3 | 7.71 – 12.45 | "Bentuknya beda-beda:" | Three chips appear on their words: pesanan at 9.14, potongan biaya at 9.82, pencairan at 11.34. At the same moment the three tokens of that kind pulse with a yellow ring. The robot gives a beat on each. |
| T | 12.45 – 13.5 | Downstream | The camera travels downstream to the pools. It leaves right after "pencairan." so the notes pop up in a settled frame. |
| S4 | 12.98 – 16.2 | "Kalau dicatat terpisah-pisah, ngitung untungnya jadi ribet." | The notes pop back, and each token jumps into the note of **its own** place (13.08 – 14.2). On "untungnya" a navy "UNTUNG BULAN INI · Rp ???" card pops in, and tangled dashed lines draw from the three notes into it. On "ribet." the word gets stabilo, the notes jitter, and the robot sighs and shrugs. |
| T | 16.2 – 16.75 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S5 | 16.675 – 21.49 | Brand: one pembukuan | On navy, three glowing rivers flow down under standing labels Toko online A / Toko online B / Media sosial. The robot is half-body bottom-left with the **chest hologram** (x 510–930, y ≈ 1450–1600). On "satukan" the rivers fill **one lake** with ripples, and the tokens plop in. On "pembukuan" the lake lifts up as the **"Pembukuan · MasterPajak AI · semua tempat"** card, whose rows carry a source chip: Pesanan #A-1021 (A), Biaya admin (B), Transfer masuk (Media sosial), Pencairan (A). On "ditelusuri" the Pencairan row lights up and the strip "Telusuri: Pencairan → Toko online A → Pesanan #A-1021" unrolls. Captions: "bantu satukan semuanya jadi / satu pembukuan.", with an underline. |
| S6 | 21.49 – 26.54 | Rekonsiliasi bulanan | The pembukuan recedes and blurs, and the **"REKONSILIASI BULANAN · Tercatat vs uang masuk, per tempat"** card lifts out of it. Its rows go from "menunggu" to "✓ Cocok" for Toko online A (23.6) and Toko online B (24.25). Media sosial gets "⚑ Perlu dicek" at 25.14, with stabilo on its "Masuk Rp1.300.000" against tercatat Rp1.375.000. The summary "2 cocok · 1 perlu dicek" appears at 25.84. Captions: "terus rekonsiliasi bulanan cek, / udah cocok?". The robot points with the far arm. |
| T | 26.0 – 27.1 | Beam + iris | Series transition. |
| S7 | 26.54 – 33.7 | End card | Series template: the tagline in two lines, the CTA pill "Coba kalkulator gratis" with a pulse, "Link di bio". The robot waves, points and waves again, with the logo hologram on the left (x 150–570). |

## Brand-rule checks
- **Labels**
  - "Ilustrasi data" appears on:
    - the map scenes, as a screen chip, whenever tokens with amounts are on screen
    - every note
    - the pembukuan card
    - the rekonsiliasi card
  - "Simulasi alur" appears on the pembukuan and rekonsiliasi cards.
- **Numbers**: there are no tax rates, deadlines, penalties or guarantees anywhere. The demo amounts are consistent with each
  other:
  - The chat transfer is Rp168.000, made up of the Rp150.000 order plus Rp18.000 ongkir. The pembukuan "Transfer masuk" row shows
    the same Rp168.000.
  - The pembukuan rows reuse the token amounts.
  - Toko online B: the rekonsiliasi shows Rp2.180.000, which matches note B ("2.180rb").
  - Media sosial shows a Rp75.000 gap and is flagged "Perlu dicek". There is no promise that every place matches.
- **Names**: "MasterPajak AI" is spelled that way throughout. The places are generic ("Toko online A/B", "Media sosial"), and so is
  the chat UI. No bank, e-wallet, marketplace, chat app or government marks appear.
- **Features named**: pembukuan yang bisa ditelusuri, rekonsiliasi bulanan, and the kalkulator gratis on the end card.
- **Robot and hologram**: the robot is in every scene and never covers text. On the map it is a small full-body figure
  bottom-right. Every token, note and card stays above y 1325 or left of x 775. The holograms are inside the safe zone.

## QA done
- **Text containment**: a check with every transform disabled (scratchpad `mp19/tools/contain.cjs`) found every text run inside
  its card, chip, note or box. A `buildReady["fit"]` step also shrinks screen captions if a font renders wider than planned.
- **Frame edges**: a sweep every 0.2 s over 0 – 33.6 found no text cut by the frame edge. The only hits are the series band
  marquee (intended) and, before the S3→S4 re-time, the notes during the camera move. That re-time fixed them (a 0.1 s sweep of
  12.2 – 14.4 is clean).
- **`hyperframes validate`**: 0 errors. There are no 404s, because `lipsync.js` exists. The contrast warnings come from the
  marquee and from transitional frames, which is the same kind as the approved videos.
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`): every scene, every cut and the end card. Contact sheets:
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp19/QA_final/contact-sheet-*.jpg`.
- **Robot lip-sync**: `tools/lipsync.py` turned `vo.wav` into `lipsync.js` (1919 frames at 60 fps, talking fraction 0.84).
- **SFX**: `tools/sfx.py` writes `assets/audio/sfx.wav`, 33.7 s, fully synthesised. Its overall level is about −26 dB RMS, the
  same as Video 14's.

## Engineering notes (worth knowing for the render)
- **Initial states.** Every `fromTo` records its from-state. The earliest from-value of each element/property is pinned at t = 0
  in a nested timeline `tl0`, which is the **first** child of `tl`. Pins added last would overwrite tweens that start at exactly
  0 on a worker's first render pass. Seeking to the current time renders nothing, so `tl.render(0, true, true)` runs once at the
  end of the build so that frame 0 shows the pinned state.
- **Two light rigs.** As in Video 14, the floor (the map plane with the river SVG) is in rig `#w1`. Everything standing on it
  (signs, tokens, notes, the untung card) is in an identical twin rig, `#w1b`, so nothing is ever depth-sorted against the floor.
  Token shadows are SVG ellipses inside the floor SVG.
- **Navy map stage.** The navy map has its own stage, `#w2m`, behind the card stage. In a shared stage the tilted plane's near
  half rendered in front of the cards. The standing river labels live inside the map (`#map2` is `preserve-3d`). Opacity is faded
  only on its flat children, never on the 3D group.
- **Tangle lines.** The S4 tangle lines are drawn in screen space (`#tng`), with anchors projected from the near-static S4 camera
  hold (drift under 4 px).

## Files
- `index.html` is the composition; `window.TM` is at the top.
- `robot_perf.js` holds the choreography. Its CUTS are at `sol−0.05` and `end−0.01`.
- `lipsync.js` is the robot's mouth track.
- `tools/sfx.py` and `tools/lipsync.py` are the generators.
- `production/vo/` holds `lines.txt`, `VO_MP19.mp3` and `VO_MP19.json`.
- `assets/audio/` holds `vo.wav` and `sfx.wav`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP19_SATU_CATATAN.png`:
  - The headline reads "jualan di banyak tempat, / CATATANNYA / SATU", with "SATU" in stabilo.
  - Three labelled rivers on a tilted navy map flow into one lake, where a "Pembukuan · semua tempat jualan" card stands with three
    ticked source rows.
  - The pill reads "Rekonsiliasi tiap bulan ✓", and the live robot points.
  - There are no numbers, and everything sits inside the 4:5 crop (y 285–1635).

## Known issues / notes for the lead
- **S5→S6 crossfade.** For about 0.5 s (21.6 – 22.1) the receding pembukuan and the rising rekonsiliasi card overlap
  half-transparent. This is the same est-card pattern as Video 14.
- **Early camera motion.** During the first fly-over (4.0 – 4.6) the large near river and the folding notes pass under the camera.
  It is a moving shot with no held text cut.
- **Token text size.** The token texts are small on the map (about 15–20 px on screen at the mid-river camera). They read as
  "different formats" texture. The chips at the top carry the spoken words.
- **Pointing gesture.** As in Videos 1, 5 and 14, the navy pointing uses the far arm, so the gesture is subtle.
- **Antenna.** In S6 the robot's antenna tip reaches the rekonsiliasi card's empty bottom-left corner, which has no text. The card
  was raised 34 px to keep it clear of the rows.
- **Lead's ElevenLabs notice.** The key outage did not affect this video. The single `el_tts_ts.py` call succeeded, and the take
  was Whisper-checked.
