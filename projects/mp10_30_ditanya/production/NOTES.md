# MasterPajak AI · Video 30 — "Usahamu Untung Berapa?"

1080×1920 · **34.6 s** (`TM.total` = `data-duration` = 34.6) · HyperFrames 0.8.186 · built VO-first (batch-3 workflow).
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept: an interview in a paper-diorama meeting room, then a split screen
One **light CSS-3D meeting room**. The people are illustrated cut-outs (flat SVG planes) sitting behind a real 3D table:
- a **wood table** (top, apron, legs) with a name tent on it;
- an office chair behind each person;
- a back wall with a window and a plant (hook), or a bookshelf and a plant (sellers);
- a grid floor, a coffee cup, and the partner's notebook.

Each world uses three camera-twin rigs (room + person | table | items), so the table always covers the person's lower half and
the papers / tablet always ride on top. This avoids depth-sorting trouble in the software compositor.

The people are fictional and generic: the **mitra bisnis** (a generic business partner: glasses, bun, slate blazer, pen at the chin), **Penjual A** (coral
tee, messy hair) and **Penjual B** (teal hijab). No bank, no lender, no real people, no brands.

The film runs in five parts:
1. **Hook.** Across the table, the mitra bisnis asks "Usahamu untung berapa sebulan?" in a big speech bubble. The two sellers
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
- **Take 5 is used.** Takes 1–4 are kept in the scratch dir (`mp30/VO_MP30_take*.mp3`):
  - **Take 1** ran 33.6 s spoken, over the limit; the script was trimmed.
  - **Take 2** (first delivery) had "Calon mitra nanya: …". Both whisper models misheard the hook as "Calon Nitra / Ngitra", and
    `small` heard "untuk". The lead asked for a clean, generic hook.
  - **Take 3**, "Ada mitra bisnis nanya: usahamu untung berapa sebulan?": "mitra" was fine, but `small` dropped "untung" and
    `medium` heard "untuk".
  - **Take 4** added a comma, "…usahamu, untung berapa sebulan?". Both models heard "mitra" and "untung", but it ran
    33.00 s spoken, with no margin.
  - **Take 5** keeps the comma and drops "kamu" from the brand line ("biar bisa jawab pakai data"). It passes both checks.
- **Length.** `VO_MP30.mp3` is 32.96 s. Speech runs 0.32 → 33.00 on the timeline (energy envelope), so it is **32.7 s
  spoken** (≤ 33 s), 70 words.
- **Audio.** `assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP30.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.
  Film times below include the +0.30 s.

| # | film time | tags the tool used | line |
|---|---|---|---|
| L1 | 0.32 – 4.30 | [playful] [excited] [curious] | Ada mitra bisnis nanya: usahamu, untung berapa sebulan? |
| L2 | 5.06 – 11.58 | [playful] [excited] [sighs] | Yang satu bingung, bongkar nota, chat, catatan kececer. Jawabnya: kira-kira. |
| L3 | 11.74 – 17.14 | [playful] [excited] | Yang satu lagi tenang, buka laporan laba rugi: penjualan, biaya, labanya jelas. |
| L4 | 17.22 – 21.37 | [playful] [excited] | Bedanya bukan gede kecilnya usaha, tapi ada datanya atau nggak. |
| L5 | 21.32 – 27.75 | [playful] [excited] | MasterPajak AI bantu nyusun catatan jualan dan biayamu jadi laporan laba rugi, biar bisa jawab pakai data. |
| L6 | 27.74 – 30.94 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L7 | 30.94 – 33.00 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

- **The sigh.** The `[sighs]` tag on L2 produces an audible sigh at 4.40–5.0, before "Yang satu". The film uses it: Penjual A's
  shoulders drop as the split panels arrive.
- **Line 1 check.** faster-whisper on the first 4.3 s (numpy input, `tools/fw_transcribe.py`, language id):
  - `small`: "Ada mitra bisnis nanya, usahamu? Untung berapa sebulan?" — mitra p 0.62, Untung p 0.89.
  - `medium`: "Ada mitra bisnis nanya, usahamu untung berapa sebulan?" — mitra p 0.78, untung p 0.83.

  Both models hear "mitra" and "untung" correctly.
- **Full listen check** (`small`). Every line is heard, and no tag is read aloud:
  > Ada mitra bisnis nanya, usahamu? Untung berapa sebulan? / Yang satu bingung, bongkarnota, cat, catatan kececer. / Jawabnya
  > kira-kira. / Yang satu lagi tenang, buka laporan labarugi. / Penjualan biaya labanya jelas. / Bedanya bukan gede kecilnya usaha,
  > tapi ada datanya atau nggak. / Master Pajak AI bantu nyusun catatan jualan dan biayamu jadi laporan labarugi / biar bisa jawab
  > pakai data. / Jualan jalan terus. Pajaknya AI yang urus. / Coba kalkulator gratis. Link di bio.

  `small` writes "chat" as "cat". Re-checked with `medium` on L2: "Yang satu bingung, bongkar nota, **chat**, catatan
  kececer." "labarugi" and "bongkarnota" are only whisper's spelling.

## TM (every key is a real word time: JSON character alignment + 0.30)
The alignment puts the first word of each line 0.1–0.3 s **late**, because the tag characters compress it. Line-start keys
(`hook`, `a`, `b`, `beda`, `sol`, `end`, `cta`) therefore use the audio onset of that word, measured from the 20 ms energy
envelope of `vo.wav`; `sigh` is the onset of the breath. All other keys are alignment + 0.30.

| key | t | word | key | t | word | key | t | word |
|---|---|---|---|---|---|---|---|---|
| hook | 0.32 | Ada | b | 11.74 | Yang (satu lagi) | sol | 21.32 | MasterPajak |
| mitra / bisnis | 0.66 / 0.86 | mitra bisnis | tenang | 12.46 | tenang | ai | 21.98 | AI |
| nanya | 1.26 | nanya | buka | 13.18 | buka | nyusun | 22.74 | nyusun |
| usaha | 2.14 | usahamu | lap | 13.50 | laporan | cat | 23.02 | catatan |
| untung | 3.02 | untung | rugi | 14.06 | rugi | jual | 23.62 | jualan |
| berapa | 3.46 | berapa | pj | 14.70 | penjualan | biaya | 24.14 | biayamu |
| sebulan | 3.74 | sebulan | by | 15.50 | biaya | lr | 24.86 | laporan (laba rugi) |
| sigh | 4.40 | (sigh, audio) | laba | 16.14 | labanya | biar | 26.06 | biar |
| a | 5.06 | Yang (satu) | jelas | 16.54 | jelas | jwb | 26.54 | jawab |
| bingung | 5.66 | bingung | beda | 17.22 | Bedanya | pakai | 26.94 | pakai |
| bongkar | 6.54 | bongkar | bukan | 17.82 | bukan | dat | 27.10 | data |
| nota | 7.14 | nota | gede | 18.06 | gede | end | 27.74 | Jualan |
| chat | 7.66 | chat | usaha2 | 18.62 | usaha | urus | 29.26 | pajaknya |
| catatan | 8.14 | catatan | tapi | 19.42 | tapi | cta | 30.94 | Coba |
| kececer | 8.62 | kececer | ada | 19.74 | ada | bio | 32.49 | Link |
| jawab | 9.82 | Jawabnya | data | 20.06 | datanya | total | 34.60 | last speech 33.00 + 1.6 |
| kira | 10.70 | kira-kira | atau / nggak | 20.54 / 20.78 | atau / nggak | | | |

**Cuts derived from TM keys.** The cuts are now computed from TM keys (identical in `index.html`, `robot_perf.js` and
`tools/sfx.py`), so a re-time moves them too:
- split doors `tS = max(sebulan + 0.45, a − 0.98)` = 4.19;
- divider → A at `a − 0.13`;
- divider → B at `b − 0.2`;
- divider → middle `tS4 = beda − 0.3` = 16.92.

**Series gaps.**
- `end − sol` = 6.42 s. The brand chest hologram is on screen from 21.82 to 27.44 (5.6 s), with full alpha from 22.04 to
  27.19 (5.15 s ≥ 4 s).
- `total − end` = 6.86 s. The end-card hologram runs from 28.5 to the end.

## Scenes (timeline seconds)
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 4.61 | Hook: meeting room | The camera pushes in over the two sellers' shoulders toward the mitra bisnis (name tent "MITRA BISNIS"). "Ilustrasi cerita" fades in at 0.6. The italic line "ada mitra bisnis nanya:" rises at 0.14. The speech bubble pops at 1.84: "Usahamu" 2.04, "untung" 2.92, "berapa" 3.36, "sebulan?" 3.64, with stabilo on untung (3.41) and berapa (3.79). The partner raises the pen to the chin on "nanya" (1.06), tilts the head on "berapa" and blinks. The robot rises between the sellers (0.15–0.85), looks up, lifts a hand and tilts its head ("hmm?"). |
| T | 4.19 – 4.79 | Split doors | Panel A slides in from the left and panel B from the right (4.19–4.61), and the divider draws (4.49–4.79). The room is hidden at 4.69. The sigh (4.40) drops A's shoulders. |
| S2 | 4.61 – 11.54 | Penjual A (focus) | The divider moves 540 → 760 (4.93–5.53) and B dims. Caption "yang satu" 4.96, "bingung." 5.54. On "bingung" A puts a hand on the head, three "?" pop (5.72–5.98), and a sweat drop runs (6.01). On "bongkar" (6.56) both arms go up and nine papers burst up from the pile. Heroes: the **nota** at 6.96 (left), the **chat** screenshot at 7.48 (right), the **catatan** page at 7.96 (centre). Caption "nota, chat," / "catatan kececer." word by word. On "kececer" (8.62) everything falls scattered onto the table, two papers fly out of frame, and stabilo lands at 8.97. "jawabnya:" at 9.77, the bubble at 10.17, "Kira-kira…" at 10.58, and the wobbling "Rp ???" pill at 11.0. A shrugs at 10.65 and sweats again. The robot squints, flinches, shakes its head and shrugs with A. |
| T | 11.54 – 12.14 | Divider → B | 760 → 320. A's captions fade first; A dims. The robot walks with the divider. |
| S3 | 12.14 – 16.92 | Penjual B (focus) | Caption "yang satu lagi" 11.69, "tenang." 12.36 (stabilo 12.76). B closes the eyes happily, with sparkles (12.46). "buka laporan laba rugi:" 13.13. The tablet lifts from the table into B's hands (13.06–13.56) and pushes toward us (13.45–14.05). Rows fill on their words: Penjualan 14.65, Modal barang 15.42, Biaya 15.62, Laba bersih 16.09 (pulse). The "✓ jelas" chip lands at 16.49. The robot points at the tablet, nods on each row and raises both arms on "jelas". |
| T | 16.92 – 17.52 | Divider → middle | 320 → 540. A's panel undims, and the tablet steps back so both faces show. |
| S4 | 16.92 – 21.32 | Both | Caption "bedanya bukan" 17.12 / "gede kecilnya usaha," 17.94, then "tapi" 19.37 / "ada datanya" 19.64 / "atau nggak." 20.42, with stabilo on "ada datanya" at 20.36. Badges: B "✓ Ada datanya" at 19.74, A "✕ Nggak ada data" at 20.73. "Ilustrasi cerita" shows at 17.22. The robot looks left and right on "gede kecilnya", points at B on "ada datanya", shakes its head at A on "nggak", then ducks out. |
| T | 20.84 – 21.40 | Band sweep | Series bands with the MasterPajak AI marquee. |
| S5 | 21.32 – 27.74 | Brand (navy) | The robot rises half-body bottom-left with the chest hologram (x 510–930, y ≈ 1450–1600). The MasterPajak AI tablet swings up (21.36–22.31) showing skeleton rows. Captions: "MasterPajak AI bantu nyusun" 21.42, "catatan jualan & biayamu" 22.90 (underline 24.49). Notes fly in: CATATAN JUALAN 22.77, a chat bubble 23.47, NOTA BIAYA 23.89 and a sticky "modal ± ?" 24.19. They dive into the tablet at 24.31–24.99. The report rows build at 24.91–25.30, the laba value pops and a chime plays. "biar bisa jawab" 25.98, the question bubble "Untung berapa sebulan?" 26.01, the laba row pulses on "jawab" (26.54), the "✓ jawab pakai data" chip lands at 26.89, and "pakai data." at 26.84 (underline 27.15). The far arm points at the notes, the report and the answer. |
| T | 27.22 – 28.24 | Beam + iris | Series. |
| S6 | 27.74 – 34.6 | End card | Series template: "Jualan jalan terus," 27.84, "pajaknya AI yang urus." 29.04, CTA "Coba kalkulator gratis" 30.84 (pulse 31.84), "Link di bio" 32.44. The robot waves, points at the CTA and waves again, with the logo hologram on the left (x 150–570). |

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
  - **"Ilustrasi cerita"**: in the hook (0.6–4.7) and the comparison (17.2–21.3), because the people and the story are
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

  Two targeted passes followed the polish edits: `mp30/rtB0.jpg` (13 frames) and `mp30/rtC0.jpg` (5 frames). The real runtime
  matched the playwright preview in every frame; no renderer-only bugs were found. Fixes made from these passes:
  - the yellow flash over the navy laba rows (it read olive) became a pulse;
  - the wall clock behind A's caption was removed;
  - the brand tablet now starts at `sol + 0.04`, so the first brand frame is not empty;
  - the number-free brand notes and the "Simulasi alur" chip on B's tablet were added.
- **`hyperframes validate`**: 0 errors.
  - The 4 warnings are GL "GPU stall due to ReadPixels" driver messages.
  - There are 8 contrast notes, all on hidden or edge-on elements: the band marquee, the tent behind the tablet, and the chat
    header of a paper lying flat. The tiny tablet chips were darkened afterwards.
- **After the VO change** (take 5, new TM): one targeted real-runtime pass of 22 frames covered the hook, every moved cut
  (doors, all three divider slides, bands, iris) and the first and last frames: `mp30/rtD0.jpg` and `mp30/rtD1.jpg`.
- **Lip-sync**: `tools/lipsync.py` writes `lipsync.js` (1991 frames at 60 fps, talking fraction 0.82).
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
- **Spoken length.** 32.7 s spoken, just under the 33 s limit. The film is 34.6 s with the end-card hold.

## Files
- `index.html`: the composition, with `TM` at the top.
- `robot_perf.js`: the choreography. CUTS are at `sol − 0.05` and `end − 0.01`. The split host is at y 1650, h 460, with x
  following the divider 540 → 760 → 320 → 540. Brand and end follow the series.
- `lipsync.js`, `assets/audio/vo.wav`, `assets/audio/sfx.wav`.
- `production/vo/`: `lines.txt`, `VO_MP30.mp3`, `VO_MP30.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP30_UNTUNG_BERAPA.png`:
  - The headline reads "USAHAMU / UNTUNG BERAPA?" (stabilo) with "kalau ditanya mitra bisnis…", renamed with the film.
  - Two tilted split panels show Penjual A (papers, "?", "✕ Kira-kira…") and Penjual B (tablet with the laporan laba rugi row
    names ✓, "✓ Pakai data"). They use the same SVG people as the film.
  - The live robot points at B.
  - There are no numbers, and everything sits inside the 4:5 crop.
- `.gitignore`: `out/`, `.hyperframes/`.
