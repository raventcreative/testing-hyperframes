# MasterPajak AI · Video 28 — Target Bulan Depan dari Data, Bukan Feeling

1080×1920 · **31.75 s** (`TM.total` = `data-duration` = 31.75) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept: an archery range
One **CSS-3D light archery range** under a moving camera:
- a straw **target boss** at the far end of the lane (navy / royal / white rings, gold centre) on a navy stand, with a
  **"TARGET BULAN DEPAN"** sign above it;
- a lane with dashed distance lines and a yellow shooting line, a **recurve bow on a tripod stand** with a rack (bow, stand and rack
  are one plane; the string is an SVG path tweened as a plain string);
- two arrows, drawn side-on in their own vertical plane:
  - the **feeling arrow** has a grey shaft, coral "?" fletching and a paper flag "FEELING · Rp50 jt?";
  - the **data arrow** has a navy shaft, a yellow head and a "DATA" pill. Its fletching starts as four empty slots.

Last month's **laporan laba rugi** floats above the bow. Its figures peel off the rows and become the data arrow's fletching. The
feeling arrow misses the board (it wobbles off and sticks in the turf beside it). The data arrow lands in the inner rings, and a
result tag pops up beside the board. The point: set next month's target from what really sold and what it really cost, not from
gut feeling. Nothing promises that the target will be reached. The on-screen word is "masuk akal" (reasonable).

Different from videos 16–27: there is no conveyor, river, quiz show, kitchen, filing cabinet, relay race, orbiting notes or order
storm.

## VO (ElevenLabs, client voice, eleven_v4, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP28.mp3` (no `--tags`).
- **Takes.** Take 3 is used. In takes 1 and 2, whisper heard line 2's "meleset" as "maeset" / "mau eset" (p 0.43–0.64), and
  `medium` agreed. So "sering meleset jauh" became "sering nggak kena sasaran". Take 2 also lengthened the brand line ("bidik
  **target** pakai data") so that the chest hologram is on screen for more than 4 s.
- **Length.** `VO_MP28.mp3` is 29.81 s. Speech runs 0.08–29.84 in the mp3, so it is **29.8 s spoken** (74 words, limit 33 s).
- **Timeline offset.** `assets/audio/vo.wav` =
  `ffmpeg -i production/vo/VO_MP28.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`. Film times below
  include that +0.30 s.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.40 – 4.06 | [playful] [excited] [curious] | Target bulan depan kamu, dari data atau dari feeling? |
| L2 | 4.23 – 7.26 | [playful] [excited] | Kalau cuma pakai feeling, sering nggak kena sasaran. |
| L3 | 7.37 – 9.27 | [playful] [excited] | Bidik pakai data bulan lalu. |
| L4 | 9.25 – 15.51 | [playful] [excited] | Lihat laporan laba rugi: apa yang benar-benar laku, berapa modal dan biayanya, dan berapa labanya. |
| L5 | 15.48 – 18.97 | [playful] [excited] | Dari situ, target bulan depan jadi lebih masuk akal. |
| L6 | 18.93 – 24.55 | [playful] [excited] | MasterPajak AI bantu nyusun laporan laba rugi tiap bulan, biar kamu bidik target pakai data. |
| L7 | 24.53 – 27.82 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L8 | 27.81 – 30.14 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

Line starts are audio onsets from the `vo.wav` energy envelope. The alignment puts each line's first word 0.1–0.3 s late.

**Listen check (take 3).** faster-whisper `small`, numpy input, `tools/fw_transcribe.py`. Every word is heard and no tag is read
aloud:

```
Target bulan depan kamu? Dari data atau dari feeling? / Kalau cuma pakai feeling, sering gak kena sasaran. / Bidik pakai data
bulan lalu. / Lihat laporan labarugi. Apa yang benar-benar laku, berapa modal dan biayanya, dan berapa labanya. / Dari situ,
target bulan depan jadi lebih masuk akal. / Master pajak AI bantu nyusun laporan labarugi tiap bulan, biar kamu bidik target
pakai data. / Jualan jalan terus. Pajaknya AI yang urus. / Coba kalkulator gratis. Link di bio.
```

"gak" and "labarugi" are only whisper's spelling. The takes and transcripts are in the scratchpad `mp28/` (`VO_MP28_take1/2.*`,
`fw_take1-3.json`).

## TM (every key is a real word time: JSON character alignment + 0.30; line starts and post-pause words use the audio onset)
| key | t | word | key | t | word |
|---|---|---|---|---|---|
| hook | 0.395 | Target (L1) | brp | 12.355 | berapa (onset) |
| kamu | 1.42 | kamu | modal | 12.78 | modal |
| data | 2.22 | data | biaya | 13.34 | biayanya |
| atau | 2.86 | atau | dbrp | 14.00 | dan (berapa, onset) |
| feel | 3.50 | feeling? | laba | 14.70 | labanya |
| kal | 4.225 | Kalau (L2) | dari | 15.475 | Dari (L5) |
| feel2 | 5.06 | feeling | situ | 15.78 | situ |
| sering | 5.74 | sering | target | 16.593 | target |
| ngk | 6.10 | nggak | jadi | 17.34 | jadi |
| kena | 6.30 | kena | lebih | 17.66 | lebih |
| sas | 6.46 | sasaran | masuk | 18.06 | masuk |
| bidik | 7.365 | Bidik (L3) | akal | 18.30 | akal |
| data2 | 8.22 | data | sol | 18.925 | MasterPajak (L6) |
| blnl | 8.50 | bulan lalu | bantu | 20.10 | bantu |
| lihat | 9.245 | Lihat (L4) | lrb | 20.78 | laporan (laba rugi) |
| lap | 9.58 | laporan | tiap | 21.62 | tiap (bulan) |
| apa | 10.67 | apa (onset) | biar | 22.34 | biar (onset) |
| benar | 11.34 | benar-benar | bidik2 | 23.02 | bidik |
| laku | 11.78 | laku | tgt2 | 23.42 | target |
| data3 | 24.22 | data | end | 24.53 | Jualan (L7) |
| urus | 26.033 | pajaknya | cta | 27.81 | Coba (L8) |
| bio | 29.30 | Link (onset) | total | 31.75 | last word end 30.14 + 1.61 |

**Gaps that hold.**
- `end − sol` = 5.6 s. The brand chest hologram is at full alpha from `sol+0.72` to `end−0.55` (4.3 s) and on screen from `sol+0.5`
  to `end−0.3` (4.8 s).
- `total − end` = 7.2 s. The end-card hologram runs from `end+0.75` to the end.

**Derived beats (in index.html and robot_perf.js).**
- Feeling arrow: released at `sering+0.02`, lands at `sas−0.04`.
- Data arrow: released at `target−0.5`, hits on `target`.
- Figure peels: `benar−0.02`, `modal+0.08`, `biaya+0.1`, `laba+0.08`, each taking 0.62 s to fly into the fletching.

## Scenes
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 4.23 | Hook | **Opening.** Close on the board and its "TARGET BULAN DEPAN" sign (frame 0 has no text yet). **Captions.** "Target bulan depan kamu," / "dari **data**" (stabilo) / "atau dari *feeling?*" (coral, wiggles). **Camera.** At 2.0 it starts a long pull-back down the right side of the lane, arriving at the bow by 4.1. The feeling arrow (flag "Rp50 jt?") is nocked; the DATA arrow waits on the rack. "Ilustrasi data" chip from 3.0. **Robot.** Rises bottom-right, points at the board on "data", shrugs with a head tilt on "feeling?". |
| S2 | 4.23 – 7.37 | Feeling shot | **Captions.** "Kalau cuma pakai feeling," / "sering **nggak kena**" / "sasaran." **Shot.** A creaky, wobbly draw (5.0–5.6). Release on "sering" (5.76); the arrow fishtails in a high arc, the camera follows, and it veers right of the board. It sticks in the turf beside the board on "sasaran" (6.42): head hidden as if embedded, quiver, dust ring, coral ✕ stamp. **Robot.** X-eyes, hands to head, recoil. |
| S3 | 7.37 – 15.48 | Data arrow + laporan | **Whip.** At 7.32 a whip-pan with motion blur back to the bow. The DATA arrow hops from the rack onto the bow; captions "Bidik pakai" / "**data bulan lalu.**" **Card.** At 9.15 "LAPORAN LABA RUGI · Bulan lalu" swings in above the bow; caption "Lihat laporan laba rugi:". **Figures.** The second caption line swaps as each phrase is spoken. Each row flashes, its figure peels out toward the camera and drops into the fletching, then the row value dims: "apa yang benar-benar **laku,**" (TERJUAL 200 pcs), "berapa **modal & biayanya,**" (MODAL Rp11 jt, BIAYA Rp4 jt), "dan berapa **labanya.**" (LABA Rp5 jt). **Robot.** Points at the arrow, then the card, nodding on each figure. |
| S4 | 15.48 – 18.93 | The data shot | **Draw.** The card fades in place. A steady draw with a dashed yellow aim line to the board; caption "Dari situ,". **Arrow cam.** Release at 16.09; the camera rides with the arrow tip down the lane and the board rushes in. **Hit.** It lands in the inner rings on "target" (16.59): ripple rings, quiver. **Result tag.** "DARI DATA BULAN LALU · **220 pcs** · Rp22.000.000 penjualan · Ilustrasi data" pops beside the board, and the **"masuk akal ✓"** badge lands on "masuk" (18.11). The feeling arrow is still stuck in the turf at the lower right. **Captions.** "target bulan depan" / "jadi lebih **masuk akal.**" **Robot.** Hops with both arms up, then points at the tag. |
| T | 18.45 – 19.0 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S5 | 18.93 – 24.53 | Brand (navy) | **Robot.** Half-body bottom-left with the **chest hologram**. **Card.** "Laporan laba rugi · MasterPajak AI · bulan lalu" flies in, rows slide in and glow on "laporan laba rugi". **Chips.** "tiap bulan ↻" pops on "tiap". On "biar" a mini target slides in; on "target" (23.42) a mini DATA arrow lands in it; then the "dari data ✓" chip. **Captions.** "MasterPajak AI bantu nyusun / **laporan laba rugi.**", then "biar kamu bidik / **target pakai data.**" (underlines). |
| T | 24.0 – 25.1 | Beam + iris | Series. |
| S6 | 24.53 – 31.75 | End card | Series template: tagline in two lines, the "Coba kalkulator gratis" CTA pill (with pulse) and "Link di bio". The robot waves, points at the CTA and waves again, with the logo hologram on the left. |

## Numbers (all "Ilustrasi data"; illustrative only)
**Last month's laporan laba rugi** (the floating card, the fletching and the brand card):

| row | value |
|---|---|
| Penjualan, 200 pcs terjual | Rp20.000.000 (200 × Rp100.000) |
| Modal barang | −Rp11.000.000 |
| Biaya (ongkir, iklan, kemasan) | −Rp4.000.000 |
| **Laba** | **Rp5.000.000** |

- Check: 20.000.000 − 11.000.000 − 4.000.000 = **5.000.000** ✓
- The fletching carries the same figures: TERJUAL 200 pcs, MODAL Rp11 jt, BIAYA Rp4 jt, LABA Rp5 jt.

**Next month's target** on the result tag: **220 pcs**, Rp22.000.000 penjualan.
- 220 × Rp100.000 = **Rp22.000.000** ✓
- Rp100.000 per pcs = Rp20.000.000 ÷ 200 pcs ✓
- 220 pcs is a modest step up from the 200 pcs that really sold (an example, +20 pcs). It is shown as "masuk akal", never as a
  promise.

**The feeling arrow's flag** reads "Rp50 jt?". It is an unfounded guess, shown on the arrow that misses.

## Brand-rule checks
- **Labels.**
  - "Ilustrasi data" is a screen chip bottom-left for the whole range part (3.0–18.4), which covers the flag, card, fletching and
    tag. It also appears on the laporan card, the result tag and the brand card.
  - "Simulasi alur" is on the brand card, the only app UI in the film. The range is a metaphor, not an app flow.
- **No forbidden content.**
  - No tax rate, deadline, penalty, guarantee or invented statistic. "Sering nggak kena sasaran" is a figure of speech about
    feeling-based targets.
  - No promise of reaching a target. The words are "lebih masuk akal" and "masuk akal".
- **Names and features.**
  - "MasterPajak AI" is spelled that way everywhere.
  - The only feature named is laporan laba rugi, plus the kalkulator gratis on the end card.
  - The tagline and CTA match the brief exactly.
  - No marketplace, bank, e-wallet or government marks.
- **Robot.**
  - It appears in every scene. On the range it is a small full-body host bottom-right (x 925, y 1595, h 520), and every caption,
    the card and the tag sit left of it or above y 1335.
  - In the brand scene the card ends above its antenna.
  - The holograms stay inside the safe zone (brand x ≈ 510–930, end x ≈ 150–570, y ≤ 1600).
- **Text containment.** `contain.cjs` (scratchpad `mp28/`, transforms disabled) reports "no text sticks out of its box". A
  `buildReady["fit"]` step shrinks screen captions if a font renders wider than 940 px.

## QA done (final build)
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`): one full pass plus two targeted fix passes, 61 frames in all. Labelled JPG
  sheets in the scratchpad `mp28/`:
  - `rtA_sheet.jpg`: hook → whip, 15 frames
  - `rtB_sheet.jpg`: fletching → shot → hit → bands, 15 frames
  - `rtC_sheet.jpg`: brand → end card, 15 frames
  - `rtD_sheet.jpg` and `rtE_sheet.jpg`: the fix passes (caption swaps, highlights, brand mini arrow)
  - also `rtC_runtime_contact-1/2.jpg` and `rtE_runtime_contact.jpg`

  PNG dumps were deleted.
- **`hyperframes validate`**: 0 errors.
  - The 4 warnings are GL "GPU stall due to ReadPixels" driver messages.
  - The contrast warnings are hidden split-caption glyphs and the series marquee. The coral "feeling?" text was darkened to
    #C9472C and the flag label to #B23F27 after the check.
- **Frame-edge sweep** (`edgecheck.cjs`, every 0.2 s over 0–31.6). No held frame cuts text. The hits are all motion:
  - the sign during the pull-back (3.0–3.2), the whip (7.6) and the arrow cam (16.0–16.6);
  - a "?" fin during the whip;
  - the laporan card flying in (9.2);
  - the series marquee;
  - the flag / DATA pill while they are behind the camera in the hook, where they are not drawn.
- **Lip-sync.** `tools/lipsync.py` turned `vo.wav` into `lipsync.js` (1804 frames at 60 fps, talking fraction 0.85).
- **SFX.** `tools/sfx.py` writes `assets/audio/sfx.wav`: 31.75 s, fully synthesised, about −25.4 dB RMS (Video 14 is −25.2). It
  contains:
  - range air, title pops, stabilo markers, a "feeling?" wobble, the pull-back whoosh;
  - a creaky draw, twang, fluttering whistle, turf thud and ✕ for the feeling arrow;
  - the whip, the nock click, the card swing, and a tick + whoosh + snap for each figure;
  - a steady draw, the aim-line tone, twang, a clean whistle, the THWACK into the boss, the tag pop and the "masuk akal" ding;
  - bands, hologram fx, brand pops, the mini-arrow thwack, beam/iris boom, end pops and chime.

## Renderer notes (applied from the batch-3 lessons)
- **Overlay twin rig.** Arrows, chips, the laporan card, the ✕ stamp, the aim line and the result tag live in an overlay twin rig
  (`#w1b`, same camera keys), so they are never depth-sorted against the boss or bow planes.
  - When an arrow lands, its head is hidden so the tip reads as embedded.
  - Each fletching chip hands over to an identical fin inside the arrow plane at the same pose.
- **Pins.** Initial states are pinned in the nested `tl0` (the first child of `tl`). `tl.render(0, true, true)` runs at the end of
  the build.
- **SVG.** Animated SVG parts (bow string `d`, ripple `r`/`opacity`) tween attributes as plain strings, with no transform cache.
- **Filters.** No CSS filter on any large 3D plane. The whip blur is an SVG filter on the `#kit` wrapper only during the whip, as
  in Video 24.
- **Layout.** The layout was solved with a projection model of the rig (scratchpad `mp28/proj.py`, which also checks the camera
  eye path so the pull-back never crosses the near plane).
  - The feeling arrow veers right because, from this camera side, it is then seen side-on.
  - Arrows are side-view planes facing +x; all cameras use negative yaw.
- **Caption swaps.**
  - The outgoing caption line also fades, because descender slivers showed in its last sink frames.
  - Highlight-in tweens end before the swap's highlight-out. An overlap left a stabilo ghost.

## Known issues / notes for the lead
- **Robot timing.** The robot rises in over 0.15–0.85 s, so it is not on frame 0 (same as the series).
- **Overlaps with the robot.**
  - In the miss and hit views, the stuck feeling arrow sits next to the robot and is partly behind it. Its "?" fins stay
    visible.
  - In the hook/S2 bow shots, the rack arrow's tip reaches toward the robot's side.
- **Small text.** The fletching labels are about 25–29 px on screen in the S3 close-up and small in the hit view. The figures
  are also on the card rows and the brand card.
- **Hit-moment framing.** At the hit moment (16.6) the camera is still settling, so the sign briefly touches the right frame
  edge for ~0.3 s (motion).
- **Sheet cleanup.** The real-runtime contact sheets of runs A/B/D were overwritten when I collected them into one folder. The
  labelled sheets `rtA–rtE_sheet.jpg` were built from the same real-runtime frames and are complete.

## Files
- `index.html` (TM at the top), `robot_perf.js` (choreography; CUTS at `sol−0.05` and `end−0.01`), `lipsync.js`.
- `assets/audio/vo.wav` and `sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP28.mp3`, `VO_MP28.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP28_TARGET.png`:
  - the headline is "TARGET / **DARI DATA**" (stabilo), with "bukan dari ~~feeling~~";
  - the boss is tilted in 3D, with the DATA arrow (fletching labelled TERJUAL / LABA / MODAL / BIAYA, no numbers) in the inner
    rings;
  - the coral "?" arrow sails over the board with a ✕;
  - the pill reads "bidik pakai laporan laba rugi", and the live robot points;
  - everything sits inside the 4:5 crop (y 285–1635).
- `.gitignore` holds `out/`.
