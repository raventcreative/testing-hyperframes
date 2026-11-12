# MasterPajak AI · Video 25 — Kategori Biaya Biar Nggak Campur Aduk

1080×1920 · **31.6 s** (`TM.total` = `data-duration` = 31.6) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits. Preview port 8925.

## Concept: a filing cabinet for receipts
One **CSS-3D paper office** filmed by one moving camera (push-in, rise, crane + orbit). A heap of mixed, generic receipts lies on
the grid floor: struk, handwritten nota, "Tagihan iklan", "Resi kirim". There are no shop, marketplace, courier, bank or e-wallet
names. A navy **5-drawer filing cabinet** stands behind the heap. Each drawer has a cream label holder, a yellow handle and a tray
that shows when it is pulled out.

- **Problem (light).** Receipts rain onto the heap. A "Total biaya bulan ini" card rises with a grey stacked bar whose five parts
  are all "?". The cabinet drops in, and each drawer gets its label on the spoken word. Matching receipts in the heap get a
  yellow category tag.
- **Brand (navy).** A phone (Simulasi alur) photographs the receipts one by one, reading tanggal, kategori and nominal. Each
  photo flies into its own drawer. Every drawer then shows its monthly total, and the phone shows the same stacked bar, now
  coloured. The biggest drawer (bahan baku) slides out with a yellow ring.

It does not reuse the formats of videos 16–24: no conveyor, rivers, quiz show, recipe card, chat phone, gallery or shelf.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP25.mp3`
(no `--tags`; model eleven_v4, settings from `tools/voice_config.json`). Take 1 kept. Speech runs 0.16–29.68 s in the mp3,
so **29.5 s spoken** (72 words). Times below are on the timeline: mp3 + 0.30 s, since vo.wav has a 300 ms adelay.

| # | timeline | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.46–3.14 | [playful] [excited] [curious] | Nota biaya usahamu masih campur aduk kayak gini? |
| 2 | 3.49–7.26 | [playful] [excited] | Ujung-ujungnya, kamu nggak tahu uangnya paling banyak habis buat apa. |
| 3 | 7.49–13.46 | [playful] [excited] | Biar jelas, pisahin per kategori: bahan baku, ongkir, iklan, kemasan, sama operasional. |
| 4 | 13.73–17.30 | [playful] [excited] | Di MasterPajak AI, cukup unggah foto notanya lewat aplikasi. |
| 5 | 17.26–21.83 | [playful] [excited] | Tanggal, kategori, sama nominalnya kecatat, terus masuk ke lacinya masing-masing. |
| 6 | 21.89–24.47 | [playful] [excited] | Jadi kelihatan, biaya mana yang paling gede. |
| 7 | 24.54–27.66 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 8 | 27.74–29.98 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Listen check.** I ran faster-whisper `small` on numpy input (`tools/fw_transcribe.py`). Every word was transcribed and no
  tag was read aloud. Whisper's transcript: "Nota biaya usahamu masih campur aduk kayak gini. / Ujung-ujungnya, kamu nggak tahu
  uangnya paling banyak habis buat apa. / Biar jelas, pisahin per kategori. Bahan baku, ongkir, iklan, kemasan sama
  operasional. / Dimaster pajak AI, cukup unggah foto notanya lewat aplikasi. / Tanggal, kategori sama nominalnya kecatet,
  terus masuk ke lacinya masing-masing. / Jadi kelihatan, biaya mana yang paling gede? / Jualan jalan terus, pajaknya AI yang
  urus. / Coba kalkulator gratis, link di bio." ("Dimaster pajak" and "kecatet" are whisper spellings.)
- `assets/audio/vo.wav` was made with
  `ffmpeg -i production/vo/VO_MP25.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  `lipsync.js` comes from `tools/lipsync.py` (1795 frames at 60 fps). `assets/audio/sfx.wav` comes from `tools/sfx.py`, all
  synthesised, 31.6 s.

## TM keys (real word times from the JSON character alignment + 0.30 s)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.46 | Nota | sol | 13.733 | Di (brand) |
| campur / aduk | 1.90 / 2.14 | campur aduk | mpai | 13.90 | MasterPajak |
| kayak / gini | 2.327 / 2.58 | kayak gini? | cukup | 14.913 | cukup |
| ujung | 3.485 | Ujung-ujungnya | unggah / foto / nota | 15.26 / 15.50 / 15.74 | unggah foto notanya |
| kamu | 4.46 | kamu | apl | 16.42 | aplikasi |
| uang | 5.34 | uangnya | tgl | **17.26** | Tanggal (see note) |
| paling | 5.74 | paling | kat2 | 17.90 | kategori |
| habis / apa | 6.22 / 6.70 | habis … apa | nom | 18.78 | nominalnya |
| biar | 7.493 | Biar | catat | 19.26 | kecatat |
| pisah | 8.30 | pisahin | masuk / laci / msg | 20.22 / 20.62 / 21.02 | masuk … lacinya masing-masing |
| kat | 8.86 | kategori | jadi / lihat | 21.894 / 22.14 | Jadi kelihatan |
| c1 | 9.66 | bahan (baku) | biaya / mana | 22.833 / 23.18 | biaya mana |
| c2 | 10.54 | ongkir | plg / gede | 23.66 / 23.94 | paling gede |
| c3 | 11.18 | iklan | end | 24.54 | Jualan |
| c4 | 11.94 | kemasan | jalan / urus | 24.94 / 25.873 | jalan / pajaknya |
| c5 | 12.70 | operasional | cta / bio | 27.736 / 29.207 | Coba / Link |

- **Note on `tgl`.** For line 5 the alignment puts "Tanggal" at 17.78 s, which is 0.5 s late because the tags compress the
  start of that line. The real onset in the audio is 17.26 s: the energy gap ends there, and whisper also has it at 17.20.
  `tgl` uses the audio onset.
- **Total.** `total` = 31.6, which is the last word end (29.98) + 1.62 s.
- **Derived offsets** (index.html, robot_perf.js and sfx.py all use the same ones):
  - `SB = sol + 0.12` = 13.85 is when the brand scene appears under the closed bands.
  - `EA = end + 0.26` = 24.80 is when the iris opens. "Paling gede" can hold until the beam, and the tagline rises on
    "jalan".
  - Robot CUTS are at `SB − 0.05` and `EA − 0.01`.
- **Series gaps.**
  - The brand hologram is at full alpha from 14.57 to 24.25, about 9.7 s.
  - The end-card hologram runs from 25.55 to 31.6, about 6 s.

## Scenes
| # | time (s) | scene | notes |
|---|---|---|---|
| S1 | 0 – 3.49 | Hook, the heap | Slow push-in over the receipt heap. The cabinet is hidden here, so the frame is clean. Three receipts flutter down and land at 0.85, 1.2 and 1.6. Titles: "Nota biaya usahamu masih" / "campur aduk" (stabilo 2.26) / "kayak gini?". The heap shuffles on "campur aduk". The robot rises bottom-right, shakes its head and points at the heap on "gini". |
| S2 | 3.49 – 7.49 | "Habis buat apa?" | The camera rises. A **Total biaya bulan ini · Rp5.500.000** card ("Ilustrasi data") lifts out of the heap. Its stacked bar has five grey parts, each a "?" (pop from 4.61). The amount accents on "uangnya", the biggest grey part lifts on "paling" and the "?" marks wobble on "habis buat apa". Titles: "ujung-ujungnya, kamu nggak tahu" / "uangnya paling banyak" / "habis buat apa?" (stabilo 6.8). The robot looks up and shrugs. |
| T | 7.49 – 8.85 | Crane + cabinet drop | The card flies away. The camera cranes and orbits to the cabinet, which **drops into the office** at 7.79 and lands with a thud at 8.21. Focus pull: the heap in the foreground goes soft (blur 2.6 px). |
| S3 | 7.49 – 13.85 | "Pisahin per kategori" | Titles: "biar jelas," / "pisahin per kategori" (stabilo 9.22). On each spoken category (9.66 / 10.54 / 11.18 / 11.94 / 12.70) the matching drawer acts: its label appears (bahan baku, ongkir, iklan, kemasan, operasional), the label flashes yellow, the drawer pulls out with its tray showing and clunks back, and that category's receipts in the heap get a yellow icon tag. The robot points at each drawer as it is named. |
| T | 13.37 – 13.93 | Band sweep | Series bands with the "MasterPajak AI" marquee. |
| S4 | 13.85 – 24.80 | Brand: unggah foto nota | The robot rises half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). The phone ("Unggah nota · MasterPajak AI", chips "Simulasi alur" and "Ilustrasi data") swings in at the left; the cabinet with its "Biaya per kategori" sign stands at the right. Beats: <br>• The tagihan-iklan receipt slides into the viewfinder on "unggah". <br>• Brackets lock and a scan line runs on "foto". <br>• Flash and shutter on "notanya". <br>• The upload bar fills on "aplikasi". <br>• The **result sheet** slides up: Tanggal **4 Nov** (17.26), Kategori **Iklan** chip (17.90), Nominal **Rp350.000** (18.78), then **✓ Tercatat** (19.22). <br>• On "masuk" the photo flies into the IKLAN drawer, which opens, receives it and closes. <br>• On "masing-masing" four more receipts are shot one by one, and each photo flies into its drawer (bahan baku, ongkir, kemasan, operasional) between 20.6 and 21.84. <br>• On "jadi kelihatan" the phone switches to the summary: total Rp5.500.000, the same stacked bar coloured, and a legend. Every drawer label shows its total, and the labels flash in sequence on "biaya mana". <br>• On "paling gede" the bahan baku drawer slides out with a yellow ring and stabilo on Rp2.400.000, and its legend row flashes. <br>Captions: "di MasterPajak AI, cukup unggah / foto notanya." → "tanggal, kategori, nominal kecatat, / masuk lacinya." → "jadi kelihatan, biaya mana / yang paling gede." |
| T | 24.30 – 25.35 | Beam + iris | Series. |
| S5 | 24.80 – 31.6 | End card | Series template: "Jualan jalan terus," / "pajaknya AI yang urus." (25.77), CTA "Coba kalkulator gratis" at 27.74 (pulse 28.7), "Link di bio" at 29.21. The robot waves, points and waves again, with the logo hologram on the left. |

## Numbers (all "Ilustrasi data"; every total is computed in code from its own lines)
- **Monthly drawer totals.**

  | Bahan baku | Ongkir | Iklan | Kemasan | Operasional | Sum |
  |---|---|---|---|---|---|
  | 2.400.000 | 850.000 | 1.200.000 | 450.000 | 600.000 | **5.500.000** |

  2.400.000 + 850.000 = 3.250.000; + 1.200.000 = 4.450.000; + 450.000 = 4.900.000; + 600.000 = **5.500.000**. This equals the
  hook card's "Total biaya bulan ini Rp5.500.000" and the phone summary total ✓.
- **Stacked bar.** The hook card's grey bar and the phone's coloured bar use the same widths, each amount / 5.500.000: 43.6 %,
  15.5 %, 21.8 %, 8.2 % and 10.9 %. Bahan baku is the biggest, which is the drawer flagged "paling gede" ✓.
- **Receipts** (each total = the sum of its own lines):

  | Category | Receipts |
  |---|---|
  | Bahan baku | kain katun 640.000 + benang 45.000 = **685.000**; kancing 50.000 + resleting 25.000 = **75.000**; kain linen **410.000** |
  | Ongkir | 6 paket **96.000**; 3 paket **54.000**; 2 paket **32.000** |
  | Iklan | iklan produk 200.000 + iklan toko 150.000 = **350.000**; promosi **90.000** |
  | Kemasan | kardus 60.000 + lakban 25.000 = **85.000**; plastik mailer **45.000**; bubble wrap **40.000** |
  | Operasional | listrik 220.000 + internet 100.000 = **320.000**; fotokopi & ATK **35.000** |

- **Result sheet.** The photographed tagihan iklan reads "Iklan toko · 7 hari · 4 Nov", and the sheet shows Tanggal 4 Nov,
  Kategori Iklan and Nominal Rp350.000, which equals that receipt's total ✓.
- **Monthly totals vs. visible receipts.** The visible receipts are examples inside the month. The film never claims they sum
  to the drawer totals.

## Labels and brand rules
- **Labels.**
  - "Ilustrasi data" appears on the heap (screen chip, bottom-left, S1–S3), the total card, the phone (both the result
    sheet and the screen chips) and the cabinet sign.
  - "Simulasi alur" appears on the phone and on the cabinet sign.
- **No forbidden content.** There is no tax rate, deadline, penalty, guarantee or invented statistic. The receipt dates are
  purchase dates (2–9 Nov), not obligations. There are no marketplace, bank, e-wallet, courier or government names or marks.
- **Features named.** The only feature is unggah foto nota lewat aplikasi, showing tanggal, kategori and nominal. The kalkulator
  gratis appears on the end card. The tagline and CTA match the brief exactly.
- **Text containment.** `scratchpad/mp25/contain.cjs` measures scrollWidth/Height for every receipt row, label, sign, sheet row
  and summary row.
  - All of them fit. The summary total was shrunk to 34 px after the first check.
  - The only flags are the sheet rows before they appear: their values wait at opacity 0 with a +24 px slide offset.
  - Every title goes through a fit-to-940 px pass.
- **Robot.** It never stands over text.
  - In the light scenes it is a small full-body host at the bottom-right, at y ≥ 1325. The cabinet ends at y ≈ 1260.
  - In the brand scene it is half-body bottom-left, under the phone (which ends at y ≈ 1150).
  - The holograms stay inside x 150–930, y ≤ 1600.
- **Batch 3 lessons applied.**
  - All initial states are pinned in a nested timeline `tl0`, the first child of `tl` at 0. The earliest from-value of every
    tween is recorded automatically.
  - `tl.render(0, true, true)` is called at the end of the build.
  - Screen text is drawn above the 3D stages.
  - Opacity is only tweened on flat leaves, never on preserve-3d groups.
  - Falling receipts, leaning receipts and the card live in an overlay twin rig, so they are never depth-sorted against the
    floor heap.

## QA done (real runtime `npx hyperframes@0.8.186 snapshot`)
All paths are in `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp25/`.
- **Full pass, 38 frames.** Every scene, every cut, the beam/iris and the end card. My sheets are `rtA_part1.jpg` … `rtA_part4.jpg`;
  the tool's own sheets are `rtA/contact-sheet-1..5.jpg`.
- **Fix passes.**
  - `rtB_sheet.jpg`: cabinet drop, label scan flash, the "paling gede" ring.
  - `rtC_sheet.jpg`: frame 0 and S3 reframed, with the heap focus pull.
- **`hyperframes validate`: 0 errors.**
  - The 4 warnings are software-GL "ReadPixels" driver messages.
  - The contrast warnings come from small receipt text in the 3D heap: receipts lying under other receipts, perspective, the
    navy invoice header measured against the paper. The rest are caption glyphs measured while still hidden below their mask.

## Known issues / notes for the lead
- **Length.** 31.6 s, with 29.5 s spoken.
- **S3 framing.** The heap is a foreground object partly out of frame on the left (8.5–13.4 s). Some receipt lines are cut by
  the frame edge, but they are out of focus (focus pull), and no title or label is cut. The other edge hits are single motion
  frames:
  - the card's "Ilustrasi data" chip flying away at 8.0 s
  - the phone entering at 14.0 s
  - the series marquee
- **Tags behind the robot.** In S3 a few heap tags sit behind the robot host. Most stay visible.
- **Cabinet drop.** The cabinet is hidden during the hook and S2. It is too close to frame there (a cut slab at the right edge)
  and would cover the titles. It drops in on "biar jelas" instead.
- **Robot gestures.** On navy the robot points with the far arm, as in the series, so the gesture is subtle.

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. The light host is at x 912 / y 1590 / h 520; brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP25.mp3`, `VO_MP25.json`.
- `tools/sfx.py` contains:
  - office air, receipt flutters and paper slaps, the heap rustle, marker strokes and text pops
  - the card rise, "?" ticks, crane whooshes and the cabinet thud
  - drawer rail slides with clunks, label dings and tag pops
  - the bands and hologram fx
  - phone swing, bracket ticks, scan beep, camera shutter, upload rise with a done ding, sheet rows and the "Tercatat" chime
  - photo whooshes into the drawers, summary ticks, the "paling gede" drawer with a chime
  - the beam/iris boom and the end pops with a chime

  Also in `tools/`: `lipsync.py` and `fw_transcribe.py`.
- `.gitignore`: `.hyperframes/`, `out/`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP25_KATEGORI_BIAYA.png`, with everything inside the 4:5 crop and no numbers.
  It shows:
  - the lockup, "BIAYA" / "CAMPUR ADUK?" (stabilo) / "pisahin per kategori, biar jelas"
  - the navy 5-drawer cabinet, labelled, with the OPERASIONAL drawer pulled out
  - two tagged receipts flying in
  - a pill reading "Habis buat apa?"
  - the live robot, pointing
