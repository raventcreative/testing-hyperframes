# MasterPajak AI · Video 30 — "Usahamu Untung Berapa?"

1080×1920 · **34.6 s** (`TM.total` = `data-duration` = 34.6) · HyperFrames 0.8.186 · built VO-first (batch-3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept: an interview in a paper-diorama meeting room, then a split screen
One **light CSS-3D meeting room**. The people are illustrated cut-outs (flat SVG planes) sitting behind a real 3D table:
- a **wood table** (top, apron, legs) with a name tent on it;
- an office chair behind each person;
- a back wall with a window and a plant (hook), or a clock and a bookshelf (sellers);
- a grid floor, a coffee cup, and the partner's notebook.

Each world uses three camera-twin rigs (room + person | table | items), so the table always covers the person's lower half and
the papers / tablet always ride on top. This avoids depth-sorting trouble in the software compositor.

The people are fictional and generic: the **calon mitra** (glasses, bun, slate blazer, pen at the chin), **Penjual A** (coral
tee, messy hair) and **Penjual B** (teal hijab). No bank, no lender, no real people, no brands.

The film runs in five parts:
1. **Hook.** Across the table, the calon mitra asks "Usahamu untung berapa sebulan?" in a big speech bubble. The two sellers
   sit in the foreground with their backs to us, and the robot peeks up between them.
2. **Split screen.** Two panels slide in over the room like sliding doors: the reverse shot of each seller. A white divider
   slides to give the speaking side the focus (760 / 320 px), and the other side dims. The robot host stands on the divider
   and follows it, like a referee.
3. **Penjual A** fumbles. A messy pile on the table bursts up ("bongkar"). A nota, a chat screenshot and a catatan page hover
   in front of A one by one, then everything falls scattered ("kececer"). Question marks, sweat drops and a shrug follow:
   "Kira-kira… Rp ???".
4. **Penjual B** stays calm. B lifts a tablet with a clear laporan laba rugi, and its rows fill on the spoken words. Then both
   panels sit side by side with "Ada datanya ✓" and "Nggak ada data ✕" badges.
5. **Brand (navy).** Notes like A's fly into a MasterPajak AI tablet, which builds the same laporan. The question bubble
   returns, and the laba row answers it ("jawab pakai data"). The series end card follows.

The point is being able to answer with data. Nothing promises approval, funding, credit or any outcome from the partner.
The partner never reacts with a yes or no.

It looks different from videos 16–29: no conveyor, river, quiz show, kitchen, filing cabinet, relay, orbiting notes, order
storm, archery or day-timeline sky. The papers burst up and fall; they do not orbit.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP30.mp3` (no `--tags`).
- **Take 2 is used.** Take 1 had line 1 as "Calon mitra nanya ke dua penjual: …" and L2 ending "…catatan yang kececer. Jawabnya
  cuma, kira-kira." It ran 33.6 s, over the 33 s limit, so the script was trimmed.
- **Length.** `VO_MP30.mp3` is 32.80 s. Speech runs 0.32 → 32.80 on the timeline (energy envelope), so it is **32.5 s
  spoken** (≤ 33 s), 69 words.
- **Audio.** `assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP30.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  Film times below include the +0.30 s.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.32 – 3.66 | [playful] [excited] [curious] | Calon mitra nanya: usahamu untung berapa sebulan? |
| L2 | 4.68 – 10.94 | [playful] [excited] [sighs] | Yang satu bingung, bongkar nota, chat, catatan kececer. Jawabnya: kira-kira. |
| L3 | 11.18 – 16.64 | [playful] [excited] | Yang satu lagi tenang, buka laporan laba rugi: penjualan, biaya, labanya jelas. |
| L4 | 16.80 – 20.96 | [playful] [excited] | Bedanya bukan gede kecilnya usaha, tapi ada datanya atau nggak. |
| L5 | 20.95 – 27.91 | [playful] [excited] | MasterPajak AI bantu nyusun catatan jualan dan biayamu jadi laporan laba rugi, biar kamu bisa jawab pakai data. |
| L6 | 27.85 – 30.86 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L7 | 30.86 – 32.80 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **The sigh.** The `[sighs]` tag on L2 produces an audible sigh at 3.86–4.5, before "Yang satu". The film uses it: Penjual A's
  shoulders drop as the split panels arrive.
- **Listen check.** faster-whisper `small` (numpy input, `tools/fw_transcribe.py`, language id) heard every line. No tag was read
  aloud:
  > Calon Nitra nanya, usahamu untuk berapa sebulan? / Yang satu bingung, bongkarnota, chat, catatan kececer / Jawabnya kira-kira /
  > Yang satu lagi tenang, buka laporan labarugi / Penjualan biaya labanya jelas / Bedanya bukan gede kecilnya usaha, tapi ada
  > datanya atau nggak? / Master pajak AI bantu nyusun catatan jualan dan biayamu jadi laporan labarugi / biar kamu bisa jawab
  > pakai data / Jualan jalan terus, pajaknya AI yang urus. / Coba kalkulator gratis, link di bio.
- **Line 1 re-check with `medium`.** It gives "Calon Ngitra nanya, usahamu **untung** (p 0.73) berapa sebulan?", so "untung" is
  spoken. The "N/Ngitra" is the n–m join in "calon mitra" (both models hear a nasal onset); the word is said.

## TM (every key is a real word time: JSON character alignment + 0.30)
The alignment puts the first word of each line 0.1–0.3 s **late**, because the tag characters compress it. Line-start keys
(`hook`, `a`, `b`, `beda`, `sol`, `end`, `cta`) therefore use the audio onset of that word, measured from the 20 ms energy
envelope of `vo.wav`. All other keys are alignment + 0.30.

| key | t | word | key | t | word | key | t | word |
|---|---|---|---|---|---|---|---|---|
| hook | 0.32 | Calon | b | 11.18 | Yang (satu lagi) | sol | 20.95 | MasterPajak |
| mitra | 0.74 | mitra | tenang | 11.98 | tenang | ai | 21.74 | AI |
| nanya | 1.02 | nanya | buka | 12.70 | buka | nyusun | 22.46 | nyusun |
| usaha | 1.90 | usahamu | lap | 13.02 | laporan | cat | 22.78 | catatan |
| untung | 2.46 | untung | rugi | 13.58 | rugi | jual | 23.34 | jualan |
| berapa | 2.82 | berapa | pj | 14.22 | penjualan | biaya | 23.82 | biayamu |
| sebulan | 3.10 | sebulan | by | 15.02 | biaya | lr | 24.54 | laporan (laba rugi) |
| sigh | 3.86 | (sigh, audio) | laba | 15.66 | labanya | biar | 25.85 | biar |
| a | 4.68 | Yang (satu) | jelas | 16.06 | jelas | jwb | 26.74 | jawab |
| bingung | 5.26 | bingung | beda | 16.80 | Bedanya | pakai | 27.02 | pakai |
| bongkar | 6.14 | bongkar | bukan | 17.34 | bukan | dat | 27.54 | data |
| nota | 6.74 | nota | gede | 17.58 | gede | end | 27.85 | Jualan |
| chat | 7.26 | chat | usaha2 | 18.22 | usaha | urus | 29.18 | pajaknya |
| catatan | 7.74 | catatan | tapi | 19.02 | tapi | cta | 30.86 | Coba |
| kececer | 8.14 | kececer | ada | 19.34 | ada | bio | 32.22 | Link |
| jawab | 9.26 | Jawabnya | data | 19.66 | datanya | total | 34.60 | last word end (33.10 alignment) + 1.5 |
| kira | 10.14 | kira-kira | atau / nggak | 20.14 / 20.30 | atau / nggak | | | |

Series gaps:
- `end − sol` = 6.9 s. The brand chest hologram is on screen from 21.45 to 27.55 (6.1 s), with full alpha from 21.67 to
  27.30 (5.6 s ≥ 4 s).
- `total − end` = 6.75 s. The end-card hologram runs from 28.6 to the end.

## Scenes (timeline seconds)
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 4.12 | Hook: meeting room | The camera pushes in over the two sellers' shoulders toward the calon mitra (name tent "CALON MITRA"). "Ilustrasi cerita" fades in at 0.6. The italic line "calon mitra nanya:" rises at 0.14. The speech bubble pops at 1.60: "Usahamu" 1.80, "untung" 2.36, "berapa" 2.72, "sebulan?" 3.00, with stabilo on untung (2.77) and berapa (3.15). The partner raises the pen to the chin on "nanya" (0.82), tilts the head on "berapa" and blinks. The robot rises between the sellers (0.15–0.85), looks up, lifts a hand and tilts its head ("hmm?"). |
| T | 3.70 – 4.30 | Split doors | Panel A slides in from the left and panel B from the right (3.70–4.12), and the divider draws (4.0–4.3). The room is hidden at 4.2. The sigh (3.86) drops A's shoulders. |
| S2 | 4.12 – 10.98 | Penjual A (focus) | The divider moves 540 → 760 (4.55–5.15) and B dims. Caption "yang satu" 4.58, "bingung." 5.14. On "bingung" A puts a hand on the head, three "?" pop (5.32–5.58), and a sweat drop runs (5.61). On "bongkar" (6.16) both arms go up and nine papers burst up from the pile. Heroes: the **nota** at 6.56 (left), the **chat** screenshot at 7.08 (right), the **catatan** page at 7.56 (centre). Caption "nota, chat," / "catatan kececer." word by word. On "kececer" (8.14) everything falls scattered onto the table, two papers fly out of frame, and stabilo lands at 8.49. "jawabnya:" at 9.21, the bubble at 9.61, "Kira-kira…" at 10.02, and the wobbling "Rp ???" pill at 10.44. A shrugs at 10.09 and sweats again. The robot squints, flinches, shakes its head and shrugs with A. |
| T | 10.98 – 11.58 | Divider → B | 760 → 320. A's captions fade first; A dims. The robot walks with the divider. |
| S3 | 11.58 – 16.50 | Penjual B (focus) | Caption "yang satu lagi" 11.13, "tenang." 11.88 (stabilo 12.28). B closes the eyes happily, with sparkles (11.98). "buka laporan laba rugi:" 12.65. The tablet lifts from the table into B's hands (12.58–13.08) and pushes toward us (12.97–13.57). Rows fill on their words: Penjualan 14.17, Modal barang 14.94, Biaya 15.14, Laba bersih 15.61 (pulse). The "✓ jelas" chip lands at 16.01. The robot points at the tablet, nods on each row and raises both arms on "jelas". |
| T | 16.50 – 17.10 | Divider → middle | 320 → 540. A's panel undims, and the tablet steps back so both faces show. |
| S4 | 16.5 – 20.95 | Both | Caption "bedanya bukan" 16.70 / "gede kecilnya usaha," 17.46, then "tapi" 18.97 / "ada datanya" 19.24 / "atau nggak." 20.02, with stabilo on "ada datanya" at 19.96. Badges: B "✓ Ada datanya" at 19.34, A "✕ Nggak ada data" at 20.25. "Ilustrasi cerita" shows at 16.8. The robot looks left and right on "gede kecilnya", points at B on "ada datanya", shakes its head at A on "nggak", then ducks out. |
| T | 20.47 – 21.03 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S5 | 20.95 – 27.85 | Brand (navy) | The robot rises half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). The MasterPajak AI tablet swings up (20.99–21.94) showing skeleton rows. Captions: "MasterPajak AI bantu nyusun" 21.05, "catatan jualan & biayamu" 22.66 (underline 24.17). Notes fly in: CATATAN JUALAN 22.53, a chat bubble 23.19, NOTA BIAYA 23.57 and a sticky "modal ± ?" 23.87. They dive into the tablet at 23.99–24.67. The report rows build at 24.59–24.98, the laba value pops and a chime plays. "biar kamu bisa jawab" 25.77, the question bubble "Untung berapa sebulan?" 25.80, the laba row glows on "jawab" (26.74), the "✓ jawab pakai data" chip lands at 26.97, and "pakai data." at 26.92 (underline 27.59). The far arm points at the notes, the report and the answer. |
| T | 27.33 – 28.35 | Beam + iris | Series. |
| S6 | 27.85 – 34.6 | End card | Series template: "Jualan jalan terus," 27.95, "pajaknya AI yang urus." 29.15, CTA "Coba kalkulator gratis" 30.76 (pulse 31.76), "Link di bio" 32.17. The robot waves, points at the CTA and waves again, with the logo hologram on the left (x 150–570). |

## Numbers (all "Ilustrasi data"; arithmetic exact)
**Laporan laba rugi** (Penjual B's tablet and the MasterPajak AI brand tablet show the same rows):

| row | value |
|---|---|
| Penjualan | Rp24.000.000 |
| Modal barang | −Rp13.200.000 |
| Biaya (ongkir, iklan, kemasan, dll.) | −Rp6.300.000 |
| **Laba bersih (bulan ini)** | **Rp4.500.000** |

- **Check.** 24.000.000 − 13.200.000 = 10.800.000, and 10.800.000 − 6.300.000 = **4.500.000** ✓.
- **Biaya.** Only the total is on screen. A breakdown that matches it, if the lead needs one: ongkir 1.800.000 + iklan 2.700.000
  + kemasan 600.000 + lain-lain 1.200.000 = 6.300.000 ✓.

**Penjual A's papers:**
- Nota No. 0458: Kain katun 640.000 + Kancing 85.000 = **Jumlah Rp725.000** ✓.
- Chat: "Total Rp178.000 kak". It is a single quoted figure with nothing to add up.
- Catatan: "Senin: 12 pcs", "modal ± ?", "ongkir ??", "iklan … lupa".
- The sticky notes, slips and brand notes carry no numbers. The brand notes show only ✓ marks.

**"Rp ???"** is A's non-answer, not a number. The cover shows no numbers.

## Labels and brand rules
- **Labels.**
  - **"Ilustrasi data"**: on the nota, the chat screenshot, the catatan page, Penjual B's tablet and the MasterPajak AI tablet.
  - **"Simulasi alur"**: on both tablets (the only app-like UI).
  - **"Ilustrasi cerita"**: in the hook (0.6–4.2) and the comparison (16.8–20.95), because the people and the story are
    fictional.
- **No forbidden content.**
  - No tax rate, deadline, penalty, guarantee or invented statistic.
  - No bank, lender, investor, marketplace, e-wallet or chat-app names, logos or colours. The chat UI is generic (grey/white
    and pale-blue bubbles, "Pembeli").
  - Nothing says or implies that the partner approves, funds or lends.
- **Names and features.**
  - "MasterPajak AI" is spelled that way everywhere.
  - The only feature named is the laporan laba rugi, plus the kalkulator gratis on the end card.
  - The tagline and CTA match the brief exactly.
- **Robot and hologram.**
  - The robot appears in every part. In the split it stands on the divider at the bottom (head from y ≈ 1420), below all
    captions, badges and tablets.
  - Both holograms stay inside the safe zone.
- **Text containment.** `contain.cjs` (scratch `mp30/`, transforms off) lists only one item: a 5 px Playfair ascent above the
  double-underlined "Rp725.000" on the receipt. That is inside the paper, with no box edge visible. The panel captions measure
  wider than the default 540 px panel there, but they are only on screen while their panel is 760 px wide (≤ 690 px of text,
  fitted by `buildReady["fit"]`).

## QA done
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`). One full pass of 39 frames covered every scene, every cut and
  transition midpoint, and the end card. Contact sheets (scratch dir):
  - `mp30/rtA0.jpg`: hook → A's papers
  - `mp30/rtA1.jpg`: kira-kira → B → comparison
  - `mp30/rtA2.jpg`: bands → brand → end card

  A targeted pass after the last edits is `mp30/rtB0.jpg`. The real runtime matched the playwright preview in every frame;
  no renderer-only bugs were found.
- **`hyperframes validate`**: see the result in the final report (log `mp30/validate.log`).
- **Lip-sync**: `tools/lipsync.py` writes `lipsync.js` (1982 frames at 60 fps, talking fraction 0.83).
- **SFX**: `tools/sfx.py` writes `assets/audio/sfx.wav`, 34.6 s, fully synthesised, −27.1 dB RMS (Video 24 is −25.7). It
  contains:
  - room air, caption pops, the bubble, stabilo strokes
  - the door whooshes and clack, divider slides
  - "?" boings and sweat drips, the paper burst, flutter, slaps and paper rain
  - the "Rp ???" wobble, a calm sparkle and chime
  - the tablet lift, tap and push, row ticks, the "jelas" ding, badge ding / soft "nope"
  - bands, hologram fx, the notes flying into the tablet, the report build and chime, the answer ding
  - the beam/iris boom, end pops and a chime

## Renderer notes (applied from the start)
- Initial states live in a nested `tl0`, the first child of `tl` at 0. They are also applied with `gsap.set` at build, and
  `tl.render(0, true, true)` runs at the end of the build.
- SVG parts animate only through attribute strings: eye blinks as `matrix(1 0 0 s 0 oy·(1−s))`, the pen arm as `translate`.
  Arm poses swap by opacity on SVG groups.
- No CSS filter is used on any 3D plane. Depth of field comes from the dimmed panels and the vignette only.
- Each world uses three camera-twin rigs (room/person | table | items). Flat papers rest 3 px above the table in the items rig,
  and nothing intersects the name tent.
- The split panels are plain `overflow:hidden` boxes whose width/left tween. The 1080 px world inside is centred with
  `left:50%`, so each camera stays centred on its seller while the divider moves.

## Known issues / notes for the lead
- **Inactive panel cropping.** The inactive panel crops its contents (B's tablet lying on the table, A's scattered papers). It
  is a dimmed, narrow camera view by design. The panel captions are only shown in the focused, 760 px panel.
- **Paper chaos.** During the burst (6.2–6.6) and the fall (8.1–8.9), papers spin edge-on across A's face for a few frames.
  This is intentional chaos.
- **Divider robot.** The robot follows the divider with its spring filter, so it lands about 0.1 s after the divider stops.
- **Spoken length.** 32.5 s spoken, just under the 33 s limit. The film is 34.6 s with the end-card hold.

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. CUTS are at `sol − 0.05` and `end − 0.01`. The split host is at y 1650, h 460, with x
  following the divider 540 → 760 → 320 → 540. Brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP30.mp3`, `VO_MP30.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP30_UNTUNG_BERAPA.png`:
  - The headline reads "USAHAMU / UNTUNG BERAPA?" (stabilo) with "kalau ditanya calon mitra…".
  - Two tilted split panels show Penjual A (papers, "?", "✕ Kira-kira…") and Penjual B (tablet with the laporan laba rugi row
    names ✓, "✓ Pakai data"). They use the same SVG people as the film.
  - The live robot points at B.
  - There are no numbers, and everything sits inside the 4:5 crop.
- `.gitignore`: `out/`, `.hyperframes/`.
