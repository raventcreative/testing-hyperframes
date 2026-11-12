# MasterPajak AI · Video 26 — Reseller & Dropship: Uang Lewat vs Untung

1080×1920 · **32.6 s** (`TM.total` = `data-duration` = 32.6) · HyperFrames 0.8.186 · VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes music and commits.

## Concept: a relay race
One **CSS-3D paper stadium** filmed by one moving camera:
- a blue running track (oval, four white lanes, start line with lane numbers, checkered finish);
- two yellow changeover zones in lane 2;
- a navy scoreboard in the infield.

The runners are flat **pictogram standees** (sports-pictogram style, limbs as nested divs with a real run cycle):
- **PEMBELI** is grey-blue.
- **KAMU** is the fictional reseller/dropshipper, in navy with a yellow headband and bib.
- **SUPPLIER** is slate.

The customer's payment is the **baton**: a gold capsule that reads "Rp100.000". On "delapan puluh ribunya", its front 80 % turns navy (Rp80.000) and gets passed on to the supplier. Only the cut yellow 20 % stub (Rp20.000) stays in Kamu's hand.

The scoreboard then shows what happens when only *uang masuk* is recorded: the omzet reads like untung. The brand scene (navy) is a MasterPajak AI **laporan laba rugi** that records both sides. This is not a conveyor, river, quiz show, recipe card or filing cabinet.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP26.mp3` (no `--tags`;
model eleven_v4, settings from `tools/voice_config.json`). Take 1 kept. The mp3 runs 0.08–30.80 s, so **30.7 s spoken** (77 words). Times below are on the timeline (mp3 + 0.30 s, because vo.wav has a 300 ms adelay).

| # | timeline | tags used (auto) | line |
|---|---|---|---|
| 1 | 0.38–5.51 | [playful] [excited] | Reseller atau dropship itu kayak lari estafet: kebanyakan uangnya cuma numpang lewat. |
| 2 | 5.57–8.23 | [playful] [excited] | Pembeli bayar seratus ribu, itu omzetmu. |
| 3 | 8.37–11.11 | [playful] [excited] | Delapan puluh ribunya langsung kamu oper ke supplier. |
| 4 | 11.18–14.71 | [playful] [excited] | Yang tinggal di tanganmu cuma dua puluh ribu. Itu untungnya. |
| 5 | 14.85–18.47 | [playful] [excited] | Kalau cuma uang masuk yang dicatat, omzet kelihatan kayak untung. |
| 6 | 18.61–23.03 | [playful] [excited] | Di MasterPajak AI, catat dua sisinya: dari pembeli dan ke supplier. |
| 7 | 23.09–25.91 | [playful] [excited] | Jadi laporan laba rugi nunjukin untung aslimu. |
| 8 | 25.98–28.94 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| 9 | 29.02–31.10 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **Listen check.** I ran faster-whisper `small` on numpy input (`tools/fw_transcribe.py`). Every word was transcribed and no tag was read aloud. Whisper writes the numbers as digits ("100 ribu", "80 ribunya", "20 ribu"). It also spells a few words its own way ("omsetmu", "dicatet", "labar rugi"); these are whisper spellings of the spoken words.
- `assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP26.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
- `lipsync.js` comes from `tools/lipsync.py` (1867 frames at 60 fps).
- `assets/audio/sfx.wav` comes from `tools/sfx.py`, all synthesised, 32.6 s. The sounds are:
  - starter whistles and footfalls (same stride maths as the run cycles);
  - baton clacks at both changeovers, and a zipper on the 80/20 reveal;
  - a coin chime on OMZET;
  - a scoreboard clunk, lamp ticks and LED blips;
  - an "eh-eh" on "nggak dicatat";
  - plus the series band, hologram, beam and end-card sounds.

## TM keys (real word times from the JSON character alignment + 0.30 s)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.38 | Reseller | kal | 14.848 | Kalau |
| drop | 1.18 | dropship | msk | 15.26 | uang (masuk) |
| est | 2.06 | lari (estafet) | dct | 15.98 | dicatat |
| keb | 3.22 | kebanyakan | omz2 | 16.78 | omzet |
| uang0 | 3.74 | uangnya | klh | 17.06 | kelihatan |
| nump / lewat | 4.433 / 4.70 | numpang / lewat | unt2 | 17.82 | untung |
| pmb | 5.574 | Pembeli | sol | 18.608 | Di (brand) |
| byr / r100 | 5.98 / 6.22 | bayar / seratus | mpai | 18.78 | MasterPajak |
| itu1 | 7.18 | itu | catat / dua2 | 19.82 / 20.22 | catat / dua (sisinya) |
| omz | 7.50 | omzetmu = **changeover 1** | dari / pmb2 | 21.153 / 21.393 | dari / pembeli |
| d80 | 8.368 | Delapan | keS / sup2 | 22.18 / 22.62 | ke / supplier |
| lgs | 9.50 | langsung | jadi | 23.094 | Jadi |
| oper | 10.10 | oper = **changeover 2** | lap | 23.42 | laporan |
| sup | 10.70 | supplier | nunj | 24.34 | nunjukin |
| ting / tgn | 11.18 / 11.74 | Yang (tinggal) / tanganmu | asli | 24.86 | untung (aslimu) |
| cuma / r20 | 12.22 / 12.42 | cuma / dua (puluh ribu) | end | 25.98 | Jualan |
| itu2 / unt | 13.42 / 13.86 | Itu / untungnya | urus / cta / bio | 27.313 / 29.016 / 30.38 | pajaknya / Coba / Link |

`total` = 32.6, which is the last word end (30.94) + 1.66 s. The series gaps:
- `end − sol` = 7.37 s. The brand hologram is at full alpha from 19.33 to 25.43, about **6.1 s**.
- `total − end` = 6.62 s. The end-card hologram runs from `end + 0.75` to the end.

## Scenes
| # | time (s) | scene | notes |
|---|---|---|---|
| S1 | 0 – 5.57 | Hook, the stadium | Close on KAMU standing in changeover zone 1; the "KAMU · reseller / dropship" tag pops on "Reseller". On "lari estafet" the camera cranes back into a depth shot down the straight: Pembeli (tag pops) holds the gold baton (glint), Kamu waits, all get set. Titles "Reseller atau dropship?" / "Kayak lari estafet." then "kebanyakan uangnya cuma" / "numpang lewat." (stabilo on "lewat"). On "numpang lewat" a stream of Rp coins + a gold streak runs down lane 2 straight past every runner. Robot rises bottom-right, pumps its arms on "estafet", sweeps an arm after the coins. |
| T | 5.1 – 6.45 | Swing | The camera orbits from the depth shot to a side-on tracking shot; the pan follows Pembeli's own acceleration curve (no speed kink). |
| S2 | 5.57 – 8.37 | First leg | Pembeli runs (run cycle, bob), tag "Rp100.000" pops on "seratus" (Ilustrasi data pill appears bottom-left). Kamu sets off and reaches back; **changeover on "omzetmu" (7.50)**: the hands meet at one world point (solved with forward kinematics) and the baton changes owner; OMZET badge pops on it. Titles "pembeli bayar Rp100.000," / "itu omzetmu." (stabilo). |
| S3 | 8.37 – 11.18 | Second leg | On "Delapan" the front 80 % of the baton sweeps navy and the tag becomes "Rp80.000 · KE SUPPLIER". Supplier (tag pops on "langsung") sets off and reaches back; **changeover on "oper" (10.10)**: the navy part goes to the supplier, the cut yellow stub stays with Kamu. The supplier runs off over the finish (its tags fold away before it leaves frame). Titles "Rp80.000-nya langsung" / "kamu oper ke supplier.". |
| S4 | 11.18 – 14.85 | What stays in the hand | Kamu stops and raises the stub; the camera pushes in. "Rp20.000" tag pops on "dua puluh ribu" (glint), "UNTUNG" badge on "untungnya". Titles "yang tinggal di tanganmu" / "cuma Rp20.000." (stabilo) + pill "= itu untungnya". Robot looks up, points at the stub. |
| S5 | 14.85 – 18.61 | Scoreboard | The scoreboard rises in the infield, the camera cranes up to it, lamps switch on. "CATATAN KAMU": Uang masuk Rp100.000 "✓ dicatat" (on "dicatat"); Ke supplier Rp80.000 dashed/dim "✕ nggak dicatat"; UNTUNG LED flips to Rp100.000 on "omzet", "kelihatan" chip + wobbling "?" on "kelihatan"; on "untung" the number is struck through and a chip "aslinya Rp20.000" pops. Titles "kalau cuma uang masuk yang dicatat," / "omzet kelihatan" / "kayak untung." (stabilo). Robot shakes its head, points. |
| T | 18.13 – 18.69 | Band sweep | Series bands with the "MasterPajak AI" marquee. |
| S6 | 18.61 – 25.98 | Brand: laporan laba rugi | Robot half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). Card "Laporan laba rugi · MasterPajak AI · bulan ini" swings up. The three baton pieces fly into their rows: whole baton → **Dari pembeli** Rp5.000.000 (on "dari pembeli"), navy part → **Ke supplier** −Rp4.000.000 (on "ke supplier"), yellow stub → **Laba kotor** Rp1.000.000 (on "untung aslimu", stabilo). Captions "di MasterPajak AI," / "catat dua sisinya." (underline), then "jadi laporan laba rugi" / "nunjukin untung aslimu." (underline). Robot points up at the rows with the far arm. |
| T | 25.46 – 26.53 | Beam and iris | Series. |
| S7 | 25.98 – 32.6 | End card | Series template: "Jualan jalan terus," / "pajaknya AI yang urus.", CTA "Coba kalkulator gratis" at 29.02 (pulse 30.0), "Link di bio" at 30.38. Robot waves, points at the CTA, waves; logo hologram left. |

## Arithmetic (all on screen, all "Ilustrasi data")
- **Per order.** Pembeli bayar **Rp100.000**, and that is the omzet.
  - Ke supplier: **Rp80.000** (80 %).
  - Stays with Kamu: Rp100.000 − Rp80.000 = **Rp20.000** (20 %), which is the untung / margin.
  - The baton is 180 px long: the navy part is 144 px (80 %) and the yellow stub is 36 px (20 %).
- **Scoreboard (only uang masuk recorded).** Uang masuk Rp100.000 is recorded and ke supplier Rp80.000 is not. So "untung kelihatan" = **Rp100.000**, which is the omzet. Aslinya it is 100.000 − 80.000 = **Rp20.000**.
- **Laporan laba rugi, bulan ini, 50 pesanan.**
  - Penjualan: 50 × 100.000 = **5.000.000**.
  - Harga pokok (ke supplier): 50 × 80.000 = **4.000.000**.
  - **Laba kotor**: 5.000.000 − 4.000.000 = **1.000.000** = 50 × 20.000 ✓.
  - The card says "laba kotor · margin" (before other costs). It does not claim to be the final net profit.

## Labels and brand rules
- **"Ilustrasi data" and "Simulasi alur".**
  - "Ilustrasi data" is a screen pill bottom-left from the first number (6.22 s) to the brand cut. It is also in the scoreboard header and on the brand card.
  - The brand card also carries "Simulasi alur".
- **No forbidden content.**
  - No tax rate, deadline, penalty, guarantee or invented statistic.
  - No marketplace, bank, e-wallet, courier or government names or marks. The runners are generic pictograms and the "R" bib means reseller.
  - The only feature named is **laporan laba rugi** (plus the kalkulator gratis on the end card). The tagline and CTA are exact.
- **Text containment.**
  - I used the transform-free check (`scratchpad/mp21/contain.cjs`) at 2.5 / 7.4 / 10.1 / 13.9 / 17.9 / 24.0 / 25.4 / 30.0 s. No text sticks out of its box.
  - The edge sweep (`ml/edgecheck.cjs`, 0.25 s steps over the film plus 0.125 s and 0.0625 s re-sweeps of 2.5–11.5 s) found only two kinds of hit:
    - lane numbers **painted on the track floor** that leave the frame as the camera moves (world decoration, like the painted RETUR word in Video 21);
    - the series marquee in the band sweep.
  - Two moving-text hits were fixed. Kamu's tag steps aside while the camera swings past it, and the supplier's tags fold away before it runs out of frame.
  - Title lines go through a fit-to-940 px pass.
- **Robot.**
  - It never stands over text. On the stadium it is the host bottom-right (x ≈ 780–1040, y ≥ 1330), and the action is framed centre-left.
  - The brand and end placements follow the series.
  - Holograms stay inside x 150–930 and y ≤ 1600.

## QA done (real runtime `npx hyperframes@0.8.186 snapshot`)
- **Full pass.** It was split into parts A, B and C, covering every scene, every cut and transition midpoint, and the end card. Targeted fix passes D and E followed. Contact sheets (JPG; the PNG dumps were deleted):
  - `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp26/rtE_sheet.jpg`: **final**, S1–S5, 16 frames from 0.3 to 18.3 s.
  - `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp26/rtC_sheet.jpg`: **final**, brand + end, 15 frames from 18.9 to 32.5 s. Nothing in this range changed after it.
  - `rtA_sheet.jpg`, `rtB_sheet.jpg` and `rtD_sheet.jpg` in the same folder are earlier rounds. `rtA` shows the name-tag clipping bug that was then fixed.
- **Real-renderer lesson (new).** The real runtime clips a 3D standee plane to its own box: anything a flat plane draws outside its CSS box disappears. The runner plane was enlarged to 660 × 510 so the tags and the raised stub are inside it. Builders using standee figures with labels should do the same.
- **Lessons from videos 16–20 are applied.**
  - Every initial state is pinned in a nested timeline that is the first child of `tl` at 0 (earliest from-values plus INIT).
  - `tl.render(0, true, true)` runs at the end of the build.
  - On-screen text sits above the 3D stage, behind a soft "sky" fade.
- **`hyperframes validate`: 0 errors**, with 4 warnings (the software-GL "ReadPixels" driver messages). There are no contrast warnings after the ghosted "Rp80.000" row was lifted above 3:1.

## Known issues / notes for the lead
- **Frame 0** shows Kamu alone on the track. The first title letters rise from 0.18 s and the robot rises 0.15–0.9 s, as in Video 21.
- **Edge sweep hits.** The painted lane numbers (floor) leave the frame edge during the hook/swing camera moves, and the series marquee crosses the edges in the band sweep. Both are expected.
- **Kamu's name tag** pops out at 5.37 and back in at 6.72 so the swinging camera never cuts it.
- **Batons and tags are flat** (pictogram style), so they read as paper cut-outs when the camera is at an angle, which is intentional.
- **SFX levels.** They are normalised to −1 dBFS peak like the other videos; the lead sets the bed/VO balance.

## Files
- `index.html` is the composition, with `TM` at the top. Race plan:
  - Pembeli runs at 440 px/s and Kamu at 440 px/s.
  - The changeover points come from forward kinematics of the PASS and RECV arm poses.
  - Camera channels are keyed separately.
- `robot_perf.js`: the choreography. The stadium host is at x 912, y 1590, h 520, with CUTS at `sol−0.05` and `end−0.01`. Brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP26.mp3`, `VO_MP26.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP26_DROPSHIP.png`. The cover has:
  - the lockup, "RESELLER & DROPSHIP", "OMZET" / "≠ UNTUNG" (stabilo) and "uangnya cuma numpang lewat";
  - a white pictogram runner on the blue track holding up the glowing yellow stub (chip "UNTUNGMU") while the big navy baton part flies off (chip "ke supplier →");
  - the pill "Catat dua sisinya" and the live robot pointing up.

  Everything sits inside the 4:5 crop and there are no numbers.
- `.gitignore` ignores `out/`.
