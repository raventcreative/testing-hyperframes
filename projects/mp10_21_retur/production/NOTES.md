# MasterPajak AI · Video 21 — Retur Juga Harus Dicatat

1080×1920 · **34.1 s** (`TM.total` = `data-duration` = 34.1) · HyperFrames 0.8.186 · VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes music and commits.

## Concept: a boomerang delivery yard
One **CSS-3D paper delivery yard** filmed by one moving camera. A U-shaped track lies on the grid floor:
- the navy **KIRIM** lane runs from the shop's mat ("toko", near-left, a pallet of 10 kraft parcels) away from camera
  to three generic buyer houses with a **"Pembeli"** sign;
- the yellow **RETUR** lane curves back round the far end like a boomerang and returns to a dashed **retur mat** (near-right).

The problem part is light (yard). Brand and end are navy, as in the rest of the series. The robot hosts the yard
(small, full-body, bottom-right), then the series half-body brand pose and the series end card.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP21.mp3`
(no `--tags`; model eleven_v4, settings from `tools/voice_config.json`). Take 1 kept. Speech runs 0.07–32.16 s in the
mp3, so **32.2 s spoken** (76 words). Times below are on the timeline (mp3 + 0.30 s; vo.wav has a 300 ms adelay).

| # | timeline | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.38–3.54 | [playful] [excited] [curious] | Paketnya diretur, tapi penjualannya masih kamu hitung? |
| 2 | 3.96–7.91 | [playful] [excited] | Misalnya kamu jual sepuluh paket. Semuanya tercatat jadi penjualan. |
| 3 | 7.98–12.31 | [playful] [excited] | Terus dua paket diretur. Barangnya balik, uangnya juga balik ke pembeli. |
| 4 | 12.45–16.47 | [playful] [excited] | Kalau returnya nggak dicatat, penjualanmu kelihatan lebih gede dari aslinya. |
| 5 | 16.69–19.19 | [playful] [excited] [surprised] | Padahal uang yang beneran masuk nggak segitu. |
| 6 | 19.33–24.23 | [playful] [excited] | Di MasterPajak AI, rekonsiliasi bulanan nyocokin catatan jualan sama uang yang masuk. |
| 7 | 24.30–27.19 | [playful] [excited] | Jadi retur yang kelewat ketahuan dari selisihnya. |
| 8 | 27.26–30.22 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 9 | 30.30–32.46 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Listen check.** faster-whisper `small` on numpy input (`tools/fw_transcribe.py`): every word transcribed, no tag read
  aloud (numbers come back as digits: "10 paket", "2 paket"). The two doubtful words were re-checked on excerpts with
  `medium`: "nyocokin" is clear; "returnya" is spoken quickly ("re-tur-nya", whisper writes "riternya"/"return yang").
- `assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP21.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  `lipsync.js` from `tools/lipsync.py` (1943 frames at 60 fps). `assets/audio/sfx.wav` from `tools/sfx.py` (all synthesised, 34.1 s).

## TM keys (all real word times from the JSON character alignment + 0.30 s)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.375 | Paketnya | pjm | 13.90 | penjualanmu |
| ret0 | 1.02 | diretur, | klh | 14.54 | kelihatan |
| pj0 | 2.06 | penjualannya | gede | 15.30 | gede |
| masih | 2.62 | masih | asli | 15.74 | aslinya |
| hit0 | 3.06 | hitung? | pad | 16.687 | Padahal |
| mis | 3.958 | Misalnya | uyb | 17.02 | uang (yang beneran) |
| jual | 4.74 | jual | umsk | 17.78 | masuk |
| p10 | 4.94 | sepuluh | ngk | 18.02 | nggak (segitu) |
| semua | 6.06 | Semuanya | sol | 19.328 | Di (brand) |
| tc | 6.54 | tercatat | mpai | 19.50 | MasterPajak |
| pjl | 7.18 | penjualan. | rek | 20.647 | rekonsiliasi |
| trs | 7.98 | Terus | cocok | 21.70 | nyocokin |
| dua | 8.42 | dua | cat | 22.22 | catatan (jualan) |
| dir | 9.02 | diretur. | um | 23.42 | uang (yang masuk) |
| brg | 9.74 | Barangnya | jadi | 24.30 | Jadi |
| uang | 10.70 | uangnya | retur | 24.70 | retur |
| pmb | 11.62 | pembeli. | kel | 25.10 | kelewat |
| kal | 12.448 | Kalau | tah | 25.58 | ketahuan |
| ndc | 12.98 | nggak (dicatat) | dari / sel | 26.19 / 26.38 | dari / selisihnya |
| | | | end | 27.26 | Jualan |
| | | | urus | 28.593 | pajaknya |
| | | | cta / bio | 30.296 / 31.66 | Coba / Link |

`total` = 34.1 = last word end (32.46) + 1.64 s. Series gaps: `end − sol` = 7.93 s (brand hologram at full alpha
20.05 → 26.71, ≈ 6.7 s); `total − end` = 6.84 s (end-card hologram from `end + 0.75` to the end).

## Scenes
| # | time (s) | scene | notes |
|---|---|---|---|
| S1 | 0 – 3.96 | Hook, the yard | The KIRIM arrow draws in. A big parcel boomerangs out (0.3): up KIRIM, round the far end on "diretur" (0.92–1.32, the yellow RETUR arrow draws behind it), back down RETUR, lands on the retur mat (1.92, squash) and gets RETUR stickers. Sale chip "PENJUALAN +Rp150.000 · ✓ tercatat" swings in at 0.58 (the sale was counted when it left), flashes on "penjualannya", "?" badge pops on "hitung?" (3.08). Titles "Paketnya diretur," (stabilo 1.32) / "tapi penjualannya" / "masih kamu hitung?" (underline 3.36). Robot rises 0.15–0.9, eyes follow the parcel, shrugs on "hitung?". |
| S2 | 3.96 – 7.98 | Ten parcels ship | "misalnya kamu / jual 10 paket. / semua tercatat." The hook parcel pops away; 10 parcels drop onto the shop pallet; the ledger card swings in bottom-left. From 4.82 every 0.215 s a parcel hops onto KIRIM, slides to the far end and drops into a house (bump). As each leaves, the ledger ticks a pip, the counter rolls 1→10 paket and Penjualan Rp150.000 → Rp1.500.000. TERCATAT stamp on "tercatat" (6.64), Penjualan row flash on "penjualan" (7.23). Robot points at the pallet, nods at the ledger. |
| S3 | 7.98 – 12.45 | Two come back | "terus / 2 paket diretur." then "barangnya balik, / uangnya juga balik / ke pembeli." Two parcels pop out of the left and right houses (8.62 / 8.80, RETUR stickers), boomerang round the far end and down RETUR (9.0 / 9.22) and land on the retur mat (10.16 / 10.38); white dashes flow along the RETUR arrow. On "uangnya" two money notes ("Rp" tokens, no amounts) arc from the shop back to those two houses (land 11.62 / 11.80). The ledger stays at 10 paket · Rp1.500.000. Robot reaches after the money. |
| T | 12.4 – 13.2 | Blur | The yard blurs (filter 8 px) under a light veil; the ledger flies forward to the centre (×1.18). |
| S4 | 12.45 – 16.69 | Ledger, "kelihatan lebih gede" | "kalau returnya nggak dicatat," → ghost row "Retur 2 paket · belum dicatat · —" (dashed) and "?" rings on the two returned pips (13.0–13.4). "penjualan kelihatan / lebih gede." → the Penjualan number puffs up (13.95) with a "kelihatan" pill; bars **Kelihatan Rp1.500.000** (14.74) vs **Aslinya Rp1.200.000** (15.74, exactly 80 %). Robot shakes its head, spreads its arms on "gede", points at the yellow bar. |
| S5 | 16.69 – 19.33 | ≠ rekening | "padahal uang yang beneran masuk / nggak segitu." Bars collapse; the ledger slides left; a generic **Mutasi rekening · rekening usaha** card flies in (pencairan toko +Rp750.000, transfer pembeli +Rp450.000, **Uang masuk Rp1.200.000**, flash on "masuk"); a yellow **≠** badge pops between the two totals on "nggak segitu" (18.07). Robot startles, points up at the rekening card, shakes its head. |
| T | 18.85 – 19.41 | Band sweep | Series bands with the "MasterPajak AI" marquee. |
| S6 | 19.33 – 27.26 | Brand, rekonsiliasi bulanan | Robot half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). MasterPajak AI card **"Rekonsiliasi bulanan"** swings up (19.63). "di MasterPajak AI, / rekonsiliasi bulanan" (underline 21.25). On "nyocokin" a scan sweeps both columns and the link icon spins; **Catatan jualan Rp1.500.000** pops on "catatan jualan" (22.17), **Uang masuk Rp1.200.000** on "uang yang masuk" (23.37); the link icon turns into ≠ (24.12). "Jadi": the **Selisih Rp300.000** row slides in; chip "2 retur belum dicatat" on "kelewat" (25.10); captions "retur yang kelewat ketahuan / dari selisihnya."; flash + stabilo on Rp300.000 at "selisihnya" (26.36), underline 26.93. Robot points at the card (rekonsiliasi) and at the selisih row. |
| T | 26.74 – 27.76 | Beam and iris | Series. |
| S7 | 27.26 – 34.1 | End card | Series template: "Jualan jalan terus," / "pajaknya AI yang urus." (28.49), CTA "Coba kalkulator gratis" at 30.30 (pulse 31.3), "Link di bio" at 31.66. Robot waves, points at the CTA, waves; logo hologram left (x 150–570). |

## Numbers (all on screen, all "Ilustrasi data")
- One parcel = Rp150.000 (hook chip "+Rp150.000").
- Sold: 10 × Rp150.000 = **Rp1.500.000** (ledger, rolls in 150.000 steps).
- Retur: 2 × Rp150.000 = Rp300.000. Aslinya: 8 × Rp150.000 = **Rp1.200.000** (bar = 1.2 / 1.5 = 80 % of the Kelihatan bar).
- Rekening: pencairan toko Rp750.000 + transfer pembeli Rp450.000 = **Rp1.200.000** = uang masuk.
- Selisih: Rp1.500.000 − Rp1.200.000 = **Rp300.000** = the 2 unrecorded returns.

## Labels and brand rules
- **"Ilustrasi data"** on the hook chip, the ledger card, the rekening card and the brand card; the brand card also carries
  **"Simulasi alur"**. The money notes carry only "Rp" (no amount).
- **No forbidden content.** No tax rate, deadline, penalty, guarantee or invented statistic. No marketplace, bank,
  e-wallet, courier or government names/marks: buyers are generic houses, the statement is "Mutasi rekening · rekening
  usaha". The only feature named is **rekonsiliasi bulanan** (+ kalkulator gratis on the end card); tagline and CTA exact.
- **Text containment.** Transform-free check (`scratchpad/mp21/contain.cjs`, at 3.3 / 15.6 / 18.7 / 26.7 / 33.5 s): the
  only hits are the masked odometer / counter strips and the collapsed bars wrapper (all `overflow: hidden`, by design).
  Edge sweep every 0.25 s (`edgecheck.cjs`): only single motion frames (ledger flying in ≈ 4.25 s, rekening card flying in
  ≈ 17.0 s, series marquee 19.0–19.25 s) plus the masked odometer values. Title lines go through a fit-to-940 px pass.
- **Robot** never stands over text: yard host bottom-right (x ≈ 780–1040, y ≥ 1325); ledger bottom-left / centre-left;
  in S5 the cards end at y ≈ 1080. Holograms inside x 150–930, y ≤ 1600.

## QA done (final build, real runtime `npx hyperframes@0.8.186 snapshot`)
- 32 frames covering every scene, every transition and the end card:
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp21/FINAL_A_sheet.jpg` (0–15.9 s)
  and `…/mp21/FINAL_B_sheet.jpg` (17.2–34.05 s). Earlier rounds: `rt1–rt3`, `fin1–fin3` sheets in the same folder.
- `hyperframes validate`: **0 errors**; 4 warnings (software-GL "ReadPixels" driver messages); contrast warnings only
  for mid-animation glyphs, the series marquee measured while hidden, the collapsed "Aslinya" row, the muted "—"
  placeholder in the ghost row, the rekening header subline mid fly-in, and the painted RETUR floor word (decorative).

## Known issues / notes for the lead
- **Length** 34.1 s (spoken 32.2 s), inside the batch-3 window.
- **Frame 0** shows the yard with the parcel only; the first title letters rise from 0.18 s and the robot rises 0.15–0.9 s
  (it is still entering while the first word is spoken).
- **Counter rolls** in S2 move every 0.215 s, so a few frames catch the Penjualan strip between two values (odometer motion).
- GSAP in this kit has no `scaleZ`; parcels shrink in x/y only when they enter a house (≈ 0.3 s, far away).
- SFX are normalised to −1 dBFS peak like the other videos; the lead sets the bed/VO balance.

## Files
- `index.html`: the composition (TM at the top). `robot_perf.js`: choreography (yard host x 912 / y 1590 / h 520; CUTS
  at `sol−0.05` and `end−0.01`; brand and end follow the series).
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP21.mp3`, `VO_MP21.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP21_RETUR.png`: lockup, "RETUR" + stabilo "juga dicatat?", "paket balik,
  uangnya juga balik", the 3D U-track (KIRIM / RETUR) with a RETUR parcel whirling round the far end and one landed on
  the retur mat, pill "Biar penjualan nggak kegedean", live robot pointing up. All inside the 4:5 crop, no numbers.
