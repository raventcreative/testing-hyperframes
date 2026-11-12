# MasterPajak AI · Video 23 — Utang ke Supplier Jangan Cuma di Kepala

1080×1920 · **33.66 s** (`TM.total` = `data-duration` = 33.66) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow) from the
Video 14 kit. Not rendered and not committed here: the lead renders, mixes the music and commits.

## Concept: a head full of sticky notes
One **CSS-3D light paper studio** (grid floor, bokeh, depth of field) filmed by one moving camera, then the series navy brand and end.

- **The seller's head.** A cartoon seller (our own flat drawing, no real person: hoodie, short hair, a white sticker outline)
  floats in the studio as a cut-out. Five sticky notes **orbit the crown like dizzy cartoon stars**. The orbit is pure nested
  transforms (tilt > spin > place > billboard counter-spin with the same ease), so every frame is a plain timeline state and the
  notes stay depth-sorted against the head (back notes pass behind it).
  - The three utang notes: "Supplier kain · belum lunas · Rp1.200.000", "Supplier kemasan · baru bayar separuh · sisa
    Rp450.000", "Tukang sablon · belum dibayar · Rp350.000".
  - Two extra notes: "Supplier benang · eh, udah lunas?", "Ongkos jahit · nanti dulu…".
  - Each utang note swings to the front as it is named. The face follows: eyes look at the note, the brows worry, a wavy mouth.
- **"Lama-lama ada yang lupa."** The orbit accelerates, the eyes turn into spinning spirals, the head wobbles, a sweat drop
  slides. On "lupa" the sablon note hands over to a free twin and flutters down out of frame, while the benang note drifts back
  into the blur.
- **Whip pan to the shop counter** (same world, horizontal motion blur): a 3D counter (navy front, yellow strip), a cash box with
  a drawer, a back wall with shelves of parcels and folded shirts, the same seller behind the counter.
  - "Pas ditagih": a **TAGIHAN** from the tukang sablon flies in (Rp350.000).
  - The **lost sablon note** lands on the bill's corner.
  - "Kamu kaget": shock eyes, an "O" mouth, a "!" pop.
  - "Uangnya udah kepakai": the cash drawer slides open **empty**, with a dust puff, a sweat drop and a wavy mouth.
- **"Untungmu kelihatan lebih gede dari aslinya."** The counter blurs and an "UNTUNG BULAN INI" card swings up.
  - A dashed row reads "Utang supplier · kain · kemasan · sablon · Rp2.000.000", and a **BELUM DICATAT** stamp lands on
    "dicatat".
  - A navy bar grows to **Untung kelihatan Rp6.000.000**. Its top third turns hatched yellow ("utang supplier
    −Rp2.000.000").
  - On "dari aslinya" that chunk peels off toward the utang row. The label is struck through and **Untung asli Rp4.000.000**
    appears (stabilo).
- **Brand (navy).** The series band sweep, then the robot rises half-body bottom-left with the chest hologram.
  - A small **avatar of the same seller's head** pops in top-right, worried. On "pindahin dari kepala" the three notes fly out
    of it, under the captions, and land as the rows of a MasterPajak AI **"Utang supplier"** pembukuan card. The avatar then
    smiles.
  - On "ke siapa / berapa / sisanya berapa" the three columns light up in turn: stabilo on the sisa cells, and the total
    **Rp2.000.000** turns yellow.
  - On "semua kecatat" a check pops on every row.
  - On "bisa ditelusuri" a dashed trace runs from the kemasan row to a **Riwayat** popover: ambil kemasan Rp900.000, bayar
    separuh −Rp450.000, sisa utang Rp450.000.
- **End card.** The series template, unchanged.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP23.mp3` (no `--tags`).
The tool used the voice in `tools/voice_config.json` (eleven_v4, stability 0.41, similarity 0.75). Generated once and accepted.
Speech runs 0.08–31.76 s in the mp3, so **31.7 s spoken**. Timeline = mp3 + 0.30 s
(`assets/audio/vo.wav` = `adelay=300|300`, 48 kHz mono). Per-word times are in `production/vo/words_MP23.json`.

| # | timeline (s) | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.38–3.14 | [playful] [excited] [curious] | Utang ke supplier, masih kamu simpan di kepala? |
| 2 | 3.41–7.82 | [playful] [excited] | Kain belum lunas, kemasan baru bayar separuh, sablon belum dibayar. |
| 3 | 8.67–10.58 | [playful] [excited] [sighs] | Lama-lama ada yang lupa. |
| 4 | 10.78–13.78 | [playful] [excited] [surprised] | Pas ditagih, kamu kaget, uangnya udah kepakai. |
| 5 | 13.98–17.78 | [playful] [excited] | Utangnya nggak dicatat, untungmu kelihatan lebih gede dari aslinya. |
| 6 | 18.19–21.91 | [playful] [excited] | Tenang, pindahin dari kepala ke pembukuan MasterPajak AI. |
| 7 | 21.97–26.63 | [playful] [excited] | Ke siapa, berapa, sisanya berapa, semua kecatat dan bisa ditelusuri. |
| 8 | 26.69–29.74 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 9 | 29.82–32.06 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

**Listen check** (faster-whisper `small`, numpy input, `tools/fw_transcribe.py`): every word was transcribed and no tag was read
aloud. The `[sighs]` tag is performed as an audible "haa" just before line 3 (≈7.9–8.6 s on the timeline), which suits "lama-lama
ada yang lupa". Whisper's spellings "kepake", "dicatet", "gak", "kecatet" and "Kesiapa" are the colloquial pronunciation, not
missing words.

## TM keys (every key = real word start from the alignment + 0.30 s)
- L1: `hook` 0.38 (Utang) · `sup` 0.78 · `masih` 1.66 · `kepala` 2.46
- L2: `kain` 3.413 · `lunas` 3.90 · `kemas` 4.70 · `separuh` 5.50 · `sablon` 6.30 · `dibayar` 6.94
- L3: `lama` 8.673 · `ada` 9.50 · `lupa` 9.86
- L4: `pas` 10.78 · `tagih` 10.94 · `kamu` 11.66 · `kaget` 11.90 · `uang` 12.62 · `pakai` 13.10
- L5: `utang2` 13.98 · `catat` 14.62 · `untung` 15.42 · `lihat` 15.98 · `gede` 16.62 · `dari` 16.94 · `asli` 17.18
- L6: `sol` 18.191 (Tenang) · `pindah` 18.753 · `kepala2` 19.34 · `pemb` 19.98 · `mpai` 20.54
- L7: `ke` 21.974 · `siapa` 22.06 · `berapa` 22.993 · `sisa` 23.26 · `sisab` 23.90 · `semua` 24.30 · `catat2` 24.70 · `bisa` 25.46
  · `telusur` 25.74
- L8–9: `end` 26.694 (Jualan) · `urus` 28.14 · `cta` 29.816 · `bio` 31.26
- `total` 33.66 = last word end 32.06 + 1.6 s hold.

`end − sol` = 8.5 s and `total − end` = 6.97 s. The brand hologram is at full alpha from 18.91 to 26.14 s (7.2 s). The end-card
hologram runs from 27.44 s to the end (6.2 s). Both stay inside x 120–960, y ≤ 1620.

## Scenes
| # | time (s) | VO | what happens |
|---|---|---|---|
| S1 | 0 – 3.4 | L1 | **Hook (light 3D).** The camera dollies in on the floating head while the notes orbit and settle. The eyes follow the notes and the head tilts on "kepala?". The robot rises bottom-right and looks up, curious. Text: "Utang ke supplier," / "masih kamu simpan" / "di kepala?" (stabilo). |
| S2 | 3.4 – 7.8 | L2 | The camera pushes in toward the halo. The kain (3.3), kemasan (4.6) and sablon (6.2) notes each swing to the front as hero (×1.14, forward), and the orbit turns 72° between them. Brows worry on "lunas"/"dibayar". The robot points at kain and sablon and nods at kemasan. |
| S3 | 7.8 – 10.6 | L3 | The orbit accelerates (from 7.69 s). Spiral eyes, head wobble, the robot sighs. On "lupa" (9.86) the sablon note slips off and falls out of frame (free twin), the benang note drifts away, a sweat drop slides. Text: "lama-lama," / "ada yang lupa." (stabilo). |
| T | 10.62 – 11.14 | — | **Whip pan** to the counter (horizontal motion blur, the robot hops). |
| S4 | 11.1 – 14.0 | L4 | **Shop counter.** The TAGIHAN flies in on "ditagih" (10.89) and the lost note lands on it (11.5–12.0). "kaget" (11.9): shock face, "!" pop, the robot jumps. "uangnya" (12.62): the drawer slides open empty with dust; "kepakai": sweat, wavy mouth, the robot shakes its head. Text: "pas ditagih," / "kamu kaget," / "uangnya udah kepakai." (stabilo). |
| S5 | 14.0 – 18.0 | L5 | **Bar card** over the blurred counter. Dashed utang row (14.4), BELUM DICATAT stamp (14.57), the bar grows (15.42), the chunk turns hatched (16.43), the chunk peels (16.9), strike + "Untung asli Rp4.000.000" (17.0–17.2). Text: "utangnya nggak dicatat," / "untungmu kelihatan" / "lebih gede." (stabilo). The robot points at the card. |
| T | 17.84 – 18.4 | — | Series band sweep with the "MasterPajak AI" marquee. |
| S6 | 18.2 – 26.7 | L6–L7 | **Brand (navy).** The robot rises with the hologram and the ledger card swings up (18.4). The seller avatar pops in (18.5). The notes fly out of it into rows 1–3 (18.95–20.5) and the avatar smiles (20.43). Column flashes on siapa / berapa / sisa (22.0–24.25), stabilo on the sisa cells, the total turns yellow (23.9). Checks pop (24.6–24.84). The riwayat popover and trace appear on "bisa ditelusuri" (25.3). Captions: "Tenang, pindahin dari kepala" / "ke pembukuan." (underline), then "ke siapa, berapa, sisanya berapa," / "semua kecatat," / "bisa ditelusuri." (underline). |
| T | 26.17 – 27.25 | — | Series beam flood and iris. |
| S7 | 26.7 – 33.66 | L8–L9 | **Series end card**: the tagline in two lines, the CTA pill "Coba kalkulator gratis" on `cta`, "Link di bio" on `bio`. The robot waves and points, with the logo hologram on the left. |

## Numbers (all on screen, all "Ilustrasi data")
| supplier | total | dibayar | sisa |
|---|---|---|---|
| Supplier kain | Rp1.200.000 | 0 | Rp1.200.000 ("belum lunas") |
| Supplier kemasan | Rp900.000 | Rp450.000 (separuh) | Rp450.000 |
| Tukang sablon | Rp350.000 | 0 | Rp350.000 ("belum dibayar") |
| **Total sisa utang** | | | **Rp2.000.000** (1.200.000 + 450.000 + 350.000 ✓) |

- **Note amounts.** The orbit notes show the same amounts: kain Rp1.200.000, kemasan "sisa Rp450.000", sablon Rp350.000.
  The TAGIHAN is Rp350.000 for "Sablon 100 kaos".
- **Bar card.**
  - Untung kelihatan Rp6.000.000 − unrecorded utang supplier Rp2.000.000 = **Untung asli Rp4.000.000** ✓.
  - Bar heights are 360 px and 240 px, and the chunk is 120 px (6 : 4 : 2 ✓).
- **Riwayat.** Rp900.000 − Rp450.000 = Rp450.000 ✓.

## Labels and brand rules
- **"Ilustrasi data"** appears on:
  - the light-studio pill (bottom-left) while the notes with amounts are on screen, 0–10.6 s
  - the TAGIHAN
  - the bar card
  - the ledger card
- **"Simulasi alur"** appears on the ledger card (the only app UI).
- **Nothing forbidden.**
  - No tax rate, deadline, penalty, guarantee or invented statistic.
  - No due dates on the supplier debts: no "jatuh tempo", no dates.
  - No logos or brand colours of a marketplace, bank, e-wallet or government.
  - Suppliers are generic: "Supplier kain", "Supplier kemasan", "Tukang sablon", "Supplier benang", "Ongkos jahit". The bill
    is generic too ("TAGIHAN · No. 0217").
  - The seller and the avatar are our own flat drawing.
- **Features named:** "pembukuan" (the ledger reads "Pembukuan · MasterPajak AI", plus "bisa ditelusuri" with the riwayat)
  and "kalkulator gratis" on the end card. The tagline and CTA are exact, and "MasterPajak AI" is spelled as required.
- **Robot.** It appears in every scene and never stands over text.
  - In the light scenes it is the bottom-right host.
  - During the brand scene it is half-body bottom-left, and the far arm points so the near arm never crosses the hologram.
  - The riwayat popover sits right of its head and above the hologram.

## QA done (final build)
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`). It covered every scene, the whip midpoints (10.75 / 10.86 s), the
  band-sweep and beam/iris midpoints, and the end card. Contact sheets are in the scratchpad `mp23/`:
  - `QA_final_1/QA1_sheet.jpg` (0–11.0 s)
  - `QA_final_2/QA2_sheet.jpg` (11.5–18.2 s)
  - `QA_final_3b/QA3b_sheet.jpg` (18.6–26.8 s; re-shot after the fit-pass fix below)
  - `QA_final_4/QA4_sheet.jpg` (27.4–33.6 s)
  - `QA_final_3c/` (the trace start at 25.9 / 26.2 s)

  Earlier rounds are `rtA`–`rtC` and `QA_final_3` (superseded). Frame 0 is clean: only the head and its orbit show, the robot rises later, and nothing
  leaks. Every initial state is pinned on the timeline at 0 through `init()` (`gsap.set` + `tl.set(…, 0)`).
- **`hyperframes validate`:** 0 errors and 0 contrast warnings. The 4 warnings are the software-GL "GPU stall" driver messages.
  `lipsync.js` exists, so there are no 404s.
- **Text containment** (`scratchpad/mp23/contain.cjs`, transforms disabled): no text sticks out of its box.
  - The fit pass uses layout widths (scrollWidth / offsetWidth), because the notes and cards sit inside scaled 3D transforms.
  - `fonts.cjs` lists what the fit pass shrank. Only real overflows were shrunk: the "baru bayar separuh" note line (86 %), the
    hatched "−Rp2.000.000" (86 %), "masih kamu simpan" (94 %) and the two Rp1.200.000 cells (94 %).
  - A first version over-shrank the ledger title and amounts. The real-runtime pass caught it (`QA_final_3`) and it is fixed
    (`QA_final_3b`).
- **Frame-edge sweep** every 0.2 s (`edgecheck.cjs`). The only hits are single motion frames:
  - the whip at 10.8 s
  - the bill flying in at 11.0 s
  - the series marquee at 18.0–18.4 s
- **Audio.** `tools/sfx.py` writes `assets/audio/sfx.wav` (33.66 s, synthesised, keyed to TM; mean −24.6 dB, the same level as
  Videos 17 and 20). `tools/lipsync.py` writes `lipsync.js` (1919 frames at 60 fps).

## Known issues / notes for the lead
- **Entering objects.** Each of these is cropped by the frame edge for a few frames while it enters:
  - the returning sablon note enters from the top-right corner (≈11.5 s)
  - the TAGIHAN flies in from the left (≈11.0 s)
- **The empty drawer** is small, at the left end of the counter. The "uangnya udah kepakai" beat is carried by the caption,
  the drawer, the dust puff and the seller's face together.
- **The slipping note's hand-over** (9.86 s) resets its paper wobble angle (≤ 5°) during fast motion. It is not visible at speed.
- **Flying notes.** In the brand scene the flying notes pass over the ledger header for about 0.3 s each on their way to the
  rows. This is intentional and they never cross the captions.
- **CLI state folder.** `.hyperframes/` in the folder was created by the CLI snapshot runs (its state file), as in the other
  projects.
- **Machine load.** The machine was heavily loaded (load ≈ 25–29), so I used snapshots with longer timeouts.

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the kit engine with Video 23 choreography. The light host is x 905, y 1585, h 520; brand and end follow the
  series. CUTS are at `sol−0.05` and `end−0.01`.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP23.mp3`, `VO_MP23.json`, `words_MP23.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP23_UTANG_SUPPLIER.png`.
  - Text: "UTANG / SUPPLIER" (stabilo) and "jangan cuma di kepala".
  - Art: the worried seller with sticky notes orbiting the crown (back notes soft, front notes sharp), the kemasan note slipping
    away, and the pill "Udah dicatat?".
  - The live robot points. There are no numbers, and everything sits inside the 4:5 crop (y 285–1635).
