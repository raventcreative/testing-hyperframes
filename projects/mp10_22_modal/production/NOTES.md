# MasterPajak AI · Video 22 — Modal Masuk Bukan Penjualan

1080×1920 · **32.3 s** (`TM.total` = `data-duration` = 32.3) · HyperFrames 0.8.186 · VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes music and commits.

## Concept: a money sorting line
One **CSS-3D light studio** filmed by one moving camera. It holds:
- a **conveyor belt** ("UANG MASUK · REKENING USAHA") that carries money tokens. Every token starts as a white
  **"Rp · Uang masuk"** chip;
- four **floor lanes** with running chevrons, from the belt back to four boards:
  - **PENJUALAN**, a yellow board with the **OMZET gauge** (0–30 jt), the value, and a "Terjual … pcs" row;
  - **PINJAMAN**, **TAMBAHAN MODAL** and **UANG PRIBADI**, three navy boards that each show a counter;
- a yellow **SCAN gate** that slides along the belt.

The point, kept simple: money coming in from a loan, extra capital or personal money is not a sale. If it is counted as
omzet, the gauge jumps even though nothing more was sold.

1. **Hook.** A close-up on a "Uang masuk" chip riding the belt. The camera pulls back to the lone omzet gauge.
2. **"Eh, tunggu".** The belt makes an emergency stop and the chips jolt. The camera swings out to the frontal wide.
   Three more lanes draw back, and the PENJUALAN header drops on the gauge board.
3. **Scan.** The gate drops in and tracks along the belt. Each chip flips (3D) to its real kind as it is spoken, and the
   matching board rises from the floor.
4. **Sort.** Each chip jumps off the belt into its lane on its words, glides back and is counted on its board. Then come
   "Bukan hasil jualan" stamps on the three side boards.
5. **Wrong lane.** The three non-sales chips jump out of their boards onto the penjualan board. The gauge leaps
   12 → 20 → 25 → 27 jt (coral, needle overshoot, board shake, NAIK flag) while **Terjual stays 240 pcs (TETAP)**.
6. **Brand (navy).** A MasterPajak AI **Pembukuan** card tags every uang masuk by kind. Omzet stays **Rp12.000.000**, and
   Rp27.000.000 is struck through.
7. **End card.** The series template.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP22.mp3` (no `--tags`).
Model eleven_v4; voice settings from `tools/voice_config.json`. Speech runs 0.08–30.40 s in the mp3, so **30.4 s spoken**
(73 words). Times below are on the timeline: mp3 time + 0.30 s, because vo.wav has a 300 ms adelay.

| # | timeline | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.38–4.02 | [playful] [excited] [curious] | Ada uang masuk ke rekening usaha, langsung kamu catat jadi omzet? |
| 2 | 4.22–7.52 | [playful] [excited] | Eh, tunggu. Nggak semua uang masuk itu penjualan. |
| 3 | 7.72–11.03 | [playful] [excited] | Ada pinjaman, tambahan modal, sampai uang pribadi. |
| 4 | 11.17–15.67 | [playful] [excited] | Pinjaman itu utang, tambahan modal itu setoran. Bukan hasil jualan. |
| 5 | 15.81–19.78 | [playful] [excited] [surprised] | Kalau ikut dihitung omzet, angkanya naik, padahal jualanmu nggak nambah. |
| 6 | 19.89–25.27 | [playful] [excited] | Di pembukuan MasterPajak AI, uang masuk dicatat sesuai jenisnya, biar omzetmu tetap asli. |
| 7 | 25.34–28.38 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 8 | 28.46–30.70 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Listen check.** I ran faster-whisper `small` (numpy input, `tools/fw_transcribe.py`, language id) on the whole take.
  Every line was transcribed and no tag was read aloud. Small heard "ke rekening" as "kerekenai" (p 0.57), so I re-checked
  line 1 with `medium`, which gives "Ada uang masuk ke rekening usaha, langsung kamu catet jadi …". The words are spoken. Only
  one take was made.
- **Brand line.** It runs 5.45 s (`end − sol`), so the brand hologram holds full alpha for 4.2 s.
- **Audio files.**
  - `assets/audio/vo.wav` was made with `ffmpeg -i production/vo/VO_MP22.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  - `lipsync.js` comes from `tools/lipsync.py` (1838 frames at 60 fps).
  - `assets/audio/sfx.wav` comes from `tools/sfx.py`: synthesised, 32.3 s, with an RMS level that matches videos 14 and 20.

## TM keys (all real word times from the JSON character alignment + 0.30 s)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.38 | Ada | kalau | 15.812 | Kalau |
| rek | 1.14 | rekening | hit | 16.14 | dihitung |
| lang | 2.38 | langsung | omz2 | 16.54 | omzet |
| omz | 3.50 | omzet? | angka | 17.10 | angkanya |
| eh | 4.22 | Eh, | naik | 17.62 | naik |
| tung | 4.54 | tunggu | pdh | 18.167 | padahal |
| ngk | 5.313 | Nggak | jmu | 18.46 | jualanmu |
| jual | 6.54 | penjualan | ngk2 | 18.86 | nggak (nambah) |
| ada2 | 7.722 | Ada (L3) | sol | 19.893 | Di (brand) |
| pinj | 7.82 | pinjaman | mpai | 20.54 | MasterPajak |
| tmod | 8.593 | tambahan (modal) | umsk | 21.58 | uang (masuk) |
| prib | 10.06 | uang (pribadi) | jenis | 22.62 | sesuai (jenisnya) |
| pin2 | 11.168 | Pinjaman (L4) | biar | 23.633 | biar |
| utang | 11.82 | utang | omu | 23.82 | omzetmu |
| tm2 | 12.593 | tambahan (modal) | asli | 24.62 | asli |
| setor | 13.50 | setoran | end | 25.34 | Jualan |
| bukan | 14.353 | Bukan | urus | 26.70 | pajaknya |
| hasil | 14.70 | hasil | cta | 28.456 | Coba |
| | | | bio | 29.90 | Link |

- **Total.** `total` = 32.3, which is the last word end (30.70) + 1.6 s.
- **Series gaps.**
  - `end − sol` = 5.45 s.
  - `total − end` = 6.96 s. The end-card hologram runs from `end + 0.75` to the end.
- **Beats without their own TM key.** These are tied to TM keys or fixed in the script:
  - The scan flips are at `ada2 − 0.32` (penjualan, right after "…itu penjualan."), `pinj`, `tmod` and `prib`.
  - The sorter jumps are at 11.05, `pin2 + 0.1`, `tm2 − 0.02` and 13.3, each counted on its board 1.13 s later.
  - The wrong-lane jumps are at `hit − 0.12`, `hit + 0.12` and `hit + 0.36`.

## Scenes (timeline seconds)
| # | time | scene | notes |
|---|---|---|---|
| S1 | 0 – 4.22 | Hook | The opening is a close-up on a "Uang masuk" chip, then a tracking pull-back to the omzet gauge (Rp0). Captions: "Uang masuk ke rekening usaha," (0.2) / "langsung jadi" (2.33) / "omzet?" (3.38), with stabilo at 3.75. The gauge needle flicks at 3.45. The robot rises bottom-right (0.15–0.9), points at the gauge and tilts its head. |
| S2 | 4.22 – 7.4 | "Eh, tunggu" | Emergency stop at 4.24 (chips jolt). The camera swings to the frontal wide by 5.8, and all four chips are in frame. Lanes for pinjaman, tambahan modal and uang pribadi start drawing back at 5.51–5.75, and the junction marks light. The PENJUALAN header drops at 6.64. Captions "Eh, tunggu." / "Nggak semua uang masuk" / "itu penjualan." with stabilo at 7.09. The robot raises a stop palm and shakes its head. |
| S3 | 6.8 – 10.9 | Scan | The SCAN gate drops at 6.78 and the camera tracks right with it. Flips: Penjualan 7.40, Pinjaman 7.82, Tambahan modal 8.59, Uang pribadi 10.06. Each side board rises with its chip. The gate leaves at 10.5–11.2. |
| S4 | 10.9 – 15.8 | Sort | The camera stays wide, then drifts toward the boards (13.6–15.8). Jumps and counts: Penjualan → **Rp12 jt · 240 pcs** at 12.18; Pinjaman → Rp8 jt at 12.40; Tambahan modal → Rp5 jt at 13.70; Uang pribadi → Rp2 jt at 14.43. Captions "Pinjaman = utang" (11.12, stabilo 12.12), "Tambahan modal = setoran" (12.54, stabilo 13.90), then "Bukan hasil jualan." (14.45, stabilo 15.05). Three "BUKAN HASIL JUALAN" stamps land at 14.50–14.76, while the robot shakes its head with its arms out. |
| S5 | 15.8 – 19.9 | Wrong lane | All four boards are in frame. The three chips pop out of their boards (their counters return to Rp0) and land on the penjualan board: 20 jt at 16.84, 25 jt at 17.14, 27 jt at 17.44. On "naik" (17.62) the needle overshoots, the board shakes, the NAIK flag shows and the robot gets X-eyes. Captions "kalau ikut dihitung omzet," / "angkanya naik ↑", then "padahal" / "jualanmu nggak nambah." with stabilo at 19.11. The camera pushes onto the omzet board on "padahal". The Terjual row flashes at 18.56 and the **TETAP** chip lands at 18.91. The robot shrugs. |
| T | 19.41 – 19.97 | Band sweep | The series bands, with the MasterPajak AI marquee. |
| S6 | 19.89 – 25.34 | Brand | The robot is half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600), at full alpha from 20.61 to 24.79. The Pembukuan card swings up at 20.19. Four token chips fly into its rows (21.23–22.38), and the kind chips pop on "sesuai jenisnya" (22.72–23.14). The footer reads "Omzet bulan ini ~~Rp27.000.000~~ **Rp12.000.000**", with stabilo at 24.67. Captions: "di pembukuan MasterPajak AI," / "uang masuk dicatat" / "sesuai jenisnya." (underline), then "biar" / "omzetmu tetap asli." (underline at 24.72). |
| T | 24.82 – 25.89 | Beam and iris | Series. |
| S7 | 25.34 – 32.3 | End card | Series template: tagline (25.44 / 26.64), CTA 28.46 (pulse 29.46), Link di bio 29.90. The robot waves, points at the CTA and waves again, with the logo hologram on the left (x 150–570). |

## Numbers (all on screen, all "Ilustrasi data")
| uang masuk | amount | kind on the brand card |
|---|---|---|
| Penjualan | Rp12 jt (240 pcs) | OMZET |
| Pinjaman | Rp8 jt | UTANG · bukan omzet |
| Tambahan modal | Rp5 jt | SETORAN · bukan omzet |
| Uang pribadi | Rp2 jt | PRIBADI · bukan omzet |

- **Wrong count.** 12 + 8 = 20, 20 + 5 = 25, 25 + 2 = **27 jt** ✓. The gauge steps 12 → 20 → 25 → 27 on a 0–30 jt
  dial at 6° per jt.
- **Terjual.** It stays 240 pcs, so omzet rises with no extra sales.
- **Brand card.**
  - Rp12.000.000 + 8.000.000 + 5.000.000 + 2.000.000 = 27.000.000 (struck through).
  - Omzet bulan ini = Rp12.000.000 ✓.
- **Chips.** The chips carry no numbers.

## Labels and brand rules
- **Labels.**
  - "Ilustrasi data" is on all four boards.
  - The brand card carries "Ilustrasi data" and "Simulasi alur".
- **No forbidden content.**
  - No tax rate, deadline, penalty, guarantee or invented statistic.
  - No bank, lender, marketplace, e-wallet or government names, logos or colours.
  - "Rekening usaha" is generic.
- **Features and copy.**
  - Features are named only as "pembukuan" (on the card, "Pembukuan · MasterPajak AI"), plus the kalkulator gratis on the
    end card.
  - The tagline and CTA match the brief exactly.
- **Correctness.**
  - Pinjaman = utang (to be paid back).
  - Tambahan modal = setoran.
  - Neither, nor uang pribadi, is hasil jualan, so none of them is omzet.
- **Robot.**
  - In the light studio it is a small host at the bottom-right, below the belt. It never covers a caption, a board or a
    chip label.
  - During the brand scene the card ends above its antenna.
- **Holograms.** They stay inside x 150–930 and y ≤ 1600.

## QA done (final build, real runtime `npx hyperframes@0.8.186 snapshot`)
- **Contact sheets.** 38 frames over every scene, every cut and the end card:
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp22/QA_final_F1/contact-sheet.jpg`
  … `QA_final_F5/contact-sheet.jpg`. Earlier rounds are in `rtA`–`rtH`.
- **`hyperframes validate`.** 0 errors.
  - The 4 warnings are GL "GPU stall due to ReadPixels" driver messages.
  - There are 14 contrast warnings. They are all measurements of hidden faces: the back face of each flipping chip and the
    hidden band marquee.
- **Text containment** (`scratchpad/mp22/contain.cjs`, transforms off): no text sticks out of its box.
- **Edge sweep every 0.2 s** (`edgecheck.cjs`). It only flags motion frames:
  - chips entering from the right in the hook;
  - the gauge board sliding in during the pull-back (1.8–2.2);
  - chips at the edge while the camera tracks the scan (7.8–9.4);
  - the boards during the S5 push (18.4–18.8);
  - the band marquee (clipped by its band);
  - invisible chip back faces.

  No static shot cuts any text.

## Renderer notes (worth knowing for the series)
- **The belt has its own camera-twin rig (`#w1c`).** It sits between the world rig (floor, lanes, boards) and the token
  overlay rig. In HyperFrames' software compositor the belt planes were mis-sorted or clipped against the floor, so whole
  belt segments vanished in the real runtime only. The belt is also built from 480 px segments, because one 2,880 px plane
  was clipped in close shots.
- **The gauge needle is an HTML element with a CSS pivot.** GSAP `svgOrigin` on an SVG `<g>` drifted off its pivot after
  backward seeks in the real runtime.
- **Time-0 states are pinned twice.** Each one is applied with `gsap.set` at build and also pinned with `tl.set(…, 0)`
  (the `PIN` helper). A fresh paused timeline seeked to 0 renders nothing, so without this the chips would sit at the world
  origin on frame 0.
- **3D labels are fitted from markup.** Labels inside the 3D rigs are measured with canvas from their markup.
  `innerText` is empty for still-hidden boards, which is why "TAMBAHAN MODAL" clipped before this fix.

## Known issues / notes for the lead
- **Robot timing.** The robot rises in over 0.15–0.9 s, so it is not on the very first frame.
- **Small text in wide shots.** Chip labels are about 20 px in the S2/S4 wide shots. Each kind is shown large in the S3
  scan tracking shot, in the captions and on the boards.
- **In-motion edge frames.** These are the hits listed above. They are not static cuts.
- **Spoken length.** 30.4 s (73 words), inside the ≤ 33 s target. The film is 32.3 s with the end-card hold.

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. CUTS are at `sol − 0.05` and `end − 0.01`. The light-studio host is at x 935, y 1665,
  h 470; brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP22.mp3`, `VO_MP22.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP22_MODAL.png`. The cover reads "MODAL MASUK / ≠ PENJUALAN" (stabilo) and
  "jangan ikut dicatat jadi omzet". It shows:
  - the PENJUALAN · OMZET gauge board reading "Rp???";
  - a short conveyor with the yellow Penjualan chip (✓);
  - the Pinjaman, Tambahan modal and Uang pribadi chips kicked off the belt (coral ✕);
  - the live robot pointing.

  There are no numbers on the cover, and everything sits inside the 4:5 crop.
