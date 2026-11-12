# MasterPajak AI · Video 20 — Diskon Gede, Untung Ikut Gede?

1080×1920 · **37.5 s** (`TM.total` = `data-duration` = 37.5) · HyperFrames 0.8.186 · VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes music and commits.

## Concept: a quiz show
One **CSS-3D light quiz studio** filmed by one moving camera (crane-in, dolly, orbit, whip pan). The set has:
- a navy **quiz board** with chasing bulbs, a lamp truss with five studio lamps and two legs;
- two **answer podiums A / B**, each with a buzzer dome;
- spot cones and floor pools, a stage disc with a yellow rim, and a grid floor.

The problem part is in the light studio. The brand and end parts are navy, as in the rest of the series.

1. **Hook.** The lamps clunk on and the bulbs chase. The headline reads "Kuis cepat! / Diskon 30%, / untungnya ikut gede?".
   A yellow **shop price tag** swings in, reading "DISKON 30% · promo toko". This makes it clear the 30 % is a store discount.
2. **Choices.** Quiz lozenges slide in: the question, then **A · Pasti naik ↑** and **B · Belum tentu**. Each podium's buzzer
   lights as its letter is spoken, and a countdown ring drains around the "?".
3. **Calculation.** The camera pushes into the board, which becomes a calculation screen for one product, "Kaos polos". The
   promo tag flies onto the product tile as a sticker. Rows appear on the spoken words:
   - harga normal
   - diskon toko 30 %
   - harga jual
   - modal barang
   - ongkir yang kamu tanggung

   The **UNTUNG PER BARANG** box shows "???" during a drum-roll, then an odometer rolls to **Rp10.000**. The robot reacts
   with X-eyes and a "wah-wah" sting.
4. **"Padahal tadinya…".** A bar card flies in front of the board, comparing Rp40.000 (harga normal) with Rp10.000 (diskon
   30 %). The navy bar is exactly 4× the yellow one, and dashed lines split it into four.
5. **"Jawabannya B".** A whip pan returns to the podiums.
   - B lights: the lozenge turns yellow with a ✓ and the buzzer and lamps flash.
   - A greys out with a ✕ on both the lozenge and the podium.
   - Confetti falls.

   On "Biar untungnya sama…" the studio blurs and an **equation card** rises: 1 × Rp40.000 = Rp40.000 against
   4 × Rp10.000 = Rp40.000, with four parcels popping. A **"jual 4× lipat"** stamp lands on "empat".
6. **Brand (navy).** The series band sweep plays. The robot rises half-body bottom-left with the **chest hologram**, and a
   **MasterPajak AI "Laporan laba rugi"** card swings up. The card shows "bulan lalu, 100 barang", using the same unit
   numbers as the quiz:
   - Penjualan, Modal barang and Ongkir ditanggung rows
   - **Laba Rp4.000.000**, with stabilo
   - a chip reading **"Rp40.000 per barang"**

   Captions: "Cek dulu / laporan laba rugi." then "biar tahu untung aslinya / sebelum promo.". On "sebelum promo" the
   DISKON 30 % tag swings onto the card's corner.
7. **End card.** This is the series template, unchanged in style: beam and iris, the tagline in two lines, the CTA pill
   "Coba kalkulator gratis" and "Link di bio". The robot waves and points, with the logo hologram on the left.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP20.mp3`
(no `--tags`). The model is eleven_v4 and the voice settings come from `tools/voice_config.json`. Speech runs 0.07–35.60 s
in the mp3, so **35.5 s spoken**. Times below are on the timeline: mp3 time + 0.30 s, since vo.wav has a 300 ms adelay.

| # | timeline | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.38–4.18 | [playful] [excited] [curious] | Kuis cepat! Diskon tiga puluh persen, untungnya ikut gede? |
| 2 | 4.65–8.15 | [playful] [excited] | Pilihan A: pasti naik. Pilihan B: belum tentu. |
| 3 | 8.21–12.71 | [playful] [excited] | Kita hitung satu barang. Harga seratus ribu, diskon jadi tujuh puluh ribu. |
| 4 | 12.84–16.95 | [playful] [excited] | Kurangi modal lima puluh ribu, plus ongkir yang kamu tanggung sepuluh ribu. |
| 5 | 17.17–20.79 | [playful] [excited] [surprised] | Untungnya tinggal sepuluh ribu. Padahal tadinya empat puluh ribu! |
| 6 | 20.85–25.35 | [playful] [excited] | Jawabannya B. Biar untungnya sama, kamu harus jual empat kali lipat. |
| 7 | 25.41–30.47 | [playful] [excited] | Cek dulu laporan laba rugi di MasterPajak AI, biar tahu untung aslinya sebelum promo. |
| 8 | 30.53–33.50 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 9 | 33.58–35.90 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Listen check.** I ran faster-whisper `small` on numpy input, language id (`tools/fw_transcribe.py`). Every word was
  transcribed and no tag was read aloud. It reads numbers as digits ("diskon 30%", "100 ribu", "4x lipat"), which is
  expected.
- **Take 1** is kept in `production/vo/take1/` and was rejected. It had a longer line 2 and a 3.8 s brand line. That would
  have left the brand hologram on screen for under 4 s and made the film 37.5 s anyway. I shortened line 2 and lengthened
  the brand line, so the brand moment is 5.1 s.
- `assets/audio/vo.wav` was made with
  `ffmpeg -i production/vo/VO_MP20.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  `lipsync.js` comes from `tools/lipsync.py` (2150 frames at 60 fps). `assets/audio/sfx.wav` comes from `tools/sfx.py`, all
  synthesised, 37.5 s.

## TM keys (all real word times from the JSON character alignment + 0.30 s)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.375 | Kuis | laba | 17.167 | Untungnya |
| disk | 1.34 | Diskon | l10 | 17.74 | sepuluh |
| per | 2.06 | persen | tadi | 18.94 | Padahal |
| unt | 2.78 | untungnya | l40 | 19.62 | empat (puluh) |
| gede | 3.74 | gede? | jwb | 20.854 | Jawabannya |
| optA | 4.647 | Pilihan (A) | jB | 21.42 | B. |
| aA | 4.86 | A: | biar | 22.033 | Biar |
| optB | 6.54 | Pilihan (B) | kamu | 23.233 | kamu |
| bB | 6.78 | B: | x4 | 24.14 | empat (kali lipat) |
| hit | 8.214 | Kita (hitung) | sol | 25.414 | Cek (brand) |
| harga | 9.66 | Harga | lr | 25.82 | laporan |
| disk2 | 10.94 | diskon | mpai | 27.06 | MasterPajak |
| j70 | 11.66 | tujuh | asli | 28.167 | biar (tahu untung aslinya) |
| modal | 12.837 | Kurangi | promo | 29.42 | sebelum |
| m50 | 13.42 | lima | end | 30.534 | Jualan |
| ongkir | 14.46 | plus (ongkir) | urus | 31.82 | pajaknya |
| o10 | 15.98 | sepuluh | cta | 33.58 | Coba |
| | | | bio | 35.127 | Link |

`total` = 37.5, which is the last word end (35.90) + 1.6 s. The gaps the series template needs are met:
- `end − sol` = 5.12 s, which is at least 5.0. The brand hologram is visible for about 4.3 s: alpha starts at `sol+0.5`,
  is full from `sol+0.72` to `end−0.55`, and fades out by `end−0.3`.
- `total − end` = 6.97 s. The end-card hologram runs from `end+0.75` to the end.

## Scenes
| # | time (s) | scene | notes |
|---|---|---|---|
| S1 | 0 – 4.6 | Hook, light studio | The crane-in starts high and wide. Lamps switch on at 0.4 and the bulbs chase. The promo tag swings in on "Diskon" (1.3) and the "?" pops on "untungnya". Stabilo on "ikut gede?". The robot rises bottom-right, makes a host flourish, then points at the tag. |
| S2 | 4.6 – 8.2 | Choices | Question lozenge, then A (4.65) and B (6.54). Each buzzer lights on its letter and the countdown ring drains. The lozenges slide out on "Kita hitung". |
| S3 | 8.2 – 17.2 | Calculation board | The camera pushes in, the board switches to calculation and the podium labels fade. The sticker lands at 11.2. Rows: harga 9.6, diskon 11.0, harga jual 11.6, modal 12.9 (value 13.4), ongkir 14.8 (value 16.0). A drum-roll leads into the odometer. |
| S4 | 17.2 – 20.85 | Reveal and compare | UNTUNG PER BARANG rolls to Rp10.000, landing on "sepuluh" (17.8), and the robot shows X-eyes. At 18.8 the bar card flies in over the emptied board; the 40k bar grows on "empat puluh". |
| T | 20.85 – 21.4 | Whip pan | Directional motion blur (Video 9 pattern). |
| S5 | 20.85 – 25.4 | Answer B | Lozenges return, B flashes yellow with ✓, A greys with ✕ (podium too). Lamps flash, confetti falls, the robot hops and points at B. The equation card rises over the blurred studio at 22.0, four parcels pop at 23.3 and the 4× stamp lands at 24.1. |
| T | 24.93 – 25.5 | Band sweep | Series bands with the "MasterPajak AI" marquee. |
| S6 | 25.4 – 30.5 | Brand, laporan laba rugi | The robot rises half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). The card swings up and its rows fill (26.3–27.3). Captions: "Cek dulu / laporan laba rugi." with an underline at 26.9, then "biar tahu untung aslinya / sebelum promo.". Laba stabilo and the "Rp40.000 per barang" chip appear at 28.7–28.8, and the promo tag lands on the card at 29.3. |
| T | 30.0 – 31.1 | Beam and iris | Series. |
| S7 | 30.5 – 37.5 | End card | Tagline, CTA at 33.58 (pulses at 34.6), "Link di bio" at 35.13. The robot waves, points and waves again, with the logo hologram on the left (x 150–570). |

## Quiz arithmetic (all on screen, all "Ilustrasi data")
One product, Kaos polos:

| | Harga normal | Diskon toko 30 % |
|---|---|---|
| Harga | Rp100.000 | Rp100.000 − Rp30.000 = **Rp70.000** (30 % of 100.000 = 30.000) |
| − Modal barang | − Rp50.000 | − Rp50.000 |
| − Ongkir yang kamu tanggung | − Rp10.000 | − Rp10.000 |
| **Untung per barang** | 100.000 − 50.000 − 10.000 = **Rp40.000** | 70.000 − 50.000 − 10.000 = **Rp10.000** |

- On the board: 100.000 − 30.000 − 50.000 − 10.000 = **10.000** ✓.
- Bar card: 40.000 : 10.000 = **4 : 1**. The bars are 320 px and 80 px tall, and the label reads "4× lebih kecil" ✓.
- Equation: 1 × 40.000 = **40.000**, and 4 × 10.000 = **40.000**, so selling 4× as many items gives the same profit ✓. That
  is why the answer is "B · Belum tentu": profit only stays level if sales quadruple.
- Laporan laba rugi, 100 barang:
  - penjualan 100 × 100.000 = 10.000.000
  - modal 100 × 50.000 = 5.000.000
  - ongkir 100 × 10.000 = 1.000.000
  - laba 10.000.000 − 5.000.000 − 1.000.000 = **4.000.000**
  - per barang 4.000.000 / 100 = **40.000** ✓, the same number as the quiz's harga normal case.

## Labels and brand rules
- **"Ilustrasi data"** appears on the quiz board in both modes, the bar card, the equation card and the laporan card. The
  laporan card also carries **"Simulasi alur"**.
- **The 30 % is a shop discount.** It always appears as a yellow price tag reading "DISKON 30% · promo toko", as "Diskon toko
  30%" on the board, and as "setelah diskon 30%" on the result.
- **No forbidden content.** There is no tax rate, deadline, penalty, guarantee or invented statistic. There are no
  marketplace, bank, e-wallet or government marks. The quiz UI is generic.
- **Features and copy.** The only feature named is "laporan laba rugi", plus the kalkulator gratis on the end card. The
  tagline and CTA match the brief exactly.
- **Text containment.** I ran a check with transforms and clip-paths disabled, comparing every text run against its nearest
  painted box (`scratchpad/mp20/contain.cjs`). The only hits are the two bar-chart axis labels, which sit below the axis line
  by design and inside the card. The edge sweep every 0.2 s (`ml/edgecheck.cjs`) only flags single frames of elements in
  motion: the tag swinging in, lozenges sliding, flying cards, the series marquee, and podium B during the whip.
- **Robot.** It never stands over text:
  - Board pointing uses the far arm.
  - The podium letters and labels fade while the camera pushes past the robot (8.2 s) and return during the whip (21 s).
  - During the brand scene the laporan card ends above the robot's antenna.
- **Holograms** stay inside x 150–930, y ≤ 1600.

## QA done (final build, real runtime `npx hyperframes@0.8.186 snapshot`)
- 30 frames covering every scene, every cut midpoint and the end card. Contact sheets:
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp20/QA_final_F1/contact-sheet.jpg`
  … `QA_final_F4/contact-sheet.jpg`. Earlier rounds are in `rtA`–`rtD`.
- `hyperframes validate`: **0 errors**, since `lipsync.js` exists so there is no 404. There are 3 contrast warnings, all
  transitional: the series marquee measured while hidden, and one board row caught mid yellow flash at 11.25 s.

## Known issues / notes for the lead
- **Length.** The film is 37.5 s, a bit over the earlier 30–36 s guideline. Spoken length is 35.5 s, inside the batch-3
  28–36 s. This voice reads at about 2.5 words/s, and both takes came out at 35.6 s.
- **Single in-motion edge hits.** The promo tag enters from off-screen right at 1.3 s and flies onto the board at 10.9 s. Both
  are motion frames only.
- **Robot gestures.** The CTA point on the end card uses the far arm, as in the series, so it is subtle.
- **Contrast.** The "Diskon toko 30%" row has low contrast for about 0.3 s while its yellow highlight flash fades (11.0–11.3).

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. CUTS are at `sol−0.05` and `end−0.01`. Light studio host is x 925, y 1595, h 520;
  brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP20.mp3`, `VO_MP20.json`, and `take1/` (the rejected take).
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP20_DISKON.png`. The cover shows "DISKON / GEDE," (stabilo), "untung ikut
  gede?", the hanging DISKON 30% · promo toko tag, the A / B lozenges tilted in 3D, a glowing buzzer, the pill "Jawab dulu: A
  atau B?" and the live robot. Everything sits inside the 4:5 crop and no answer is given away.
