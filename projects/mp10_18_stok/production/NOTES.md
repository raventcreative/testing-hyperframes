# MasterPajak AI · Video 18 — Stok Itu Uang yang Lagi Diam

1080×1920 · **34.06 s** (`TM.total` = `data-duration` = 34.06) · HyperFrames 0.8.186. Built VO-first (batch 3 brief).
Not rendered and not committed here. The lead renders, mixes the music and commits.

## Concept
The whole problem half plays in one **CSS-3D warehouse studio**: a navy steel shelf (rak) with a pegboard back holds
**12 cardboard boxes (kardus)** on three tiers. Every box is a real cube, and its back face shows the money it cost (a
banknote bundle priced "Rp400.000"). A moving camera films it: dolly, orbit, a close-up and one depth-of-field shot.
- **Hook:** the shelf is full. A "Saldo usaha Rp850.000" card turns almost edge-on on "tipis", so it literally goes thin.
  The robot shrugs.
- **Coba balik kardusnya:** one box hops and flips. On "uang", the other 11 flip in a domino wave and the whole shelf becomes
  money. On "diam", a big pause badge pops up and the boxes shiver still.
- **Bukan uang hangus / bukan untung:** that box floats out toward the camera and the shelf blurs behind it. Stickers
  "UANG HANGUS?" and "UNTUNG?" slap onto it, get a red X and fall away. The robot shakes its head.
- **Itu modal yang nyangkut:** the box goes back into its slot, and a yellow **MODAL** tag hooks onto the shelf lip under it
  ("nyangkut").
- **Baru jadi biaya pas barangnya laku:** a BIAYA card arrives. Two boxes get a **LAKU** stamp and turn back to plain goods.
  Their money chips fly into BIAYA (Rp0 → Rp800.000), and the boxes leave the shelf (sold).
- **Kalau semuanya langsung dianggap biaya:** chips from all 10 remaining boxes fly into BIAYA (→ Rp4.800.000, "semua belanja
  stok"), and the MODAL tag drops off. On "jeblok", the LABA card falls from Rp500.000 to **−Rp3.500.000**, and the robot gets
  X-eyes.
- **Padahal barangnya masih ada:** the cards clear and the camera returns to the shelf. The 10 boxes hop and glow, and a card
  reads "MASIH DI RAK · 10 kardus · belum laku · Rp4.000.000".
- **Brand (navy, series band sweep):** the robot rises with the chest hologram. Three chips (Belanja stok / Stok laku / Sisa
  stok) arc into a MasterPajak AI **Pembukuan** card. Then the **Laporan laba rugi** card lifts out of it, the laba gets a
  stabilo and a ✓ stamp lands on "kebaca bener".
- **End:** the series end card: beam + iris, the tagline in two lines, the CTA pill, "Link di bio", the robot waving and
  pointing, and the logo hologram on the left.

**Accounting point (kept simple, no tax treatment):** belanja stok is modal that sits on the shelf. It is not lost money and
it is not profit. It becomes a cost (modal barang terjual) when the goods sell. If all of it is counted as cost straight away,
the month's laba looks like it crashed while the goods are still there.

## VO (ElevenLabs, client voice, default AUTO tags), `production/vo/`
`lines.txt` → `VO_MP18.mp3` + `VO_MP18.json` (per-line start/end + character alignment). `vo.wav` = the mp3 delayed 0.30 s
(48 kHz mono). Times below are film times (+0.30).

| # | tags the tool used | line | film time |
|---|---|---|---|
| 1 | `[playful] [excited] [sighs]` | Stok numpuk di rak, tapi saldo kok tipis? | 1.02–3.98 (a short sigh from ~0.4) |
| 2 | `[playful] [excited]` | Coba balik kardusnya. Isinya? Uang kamu yang lagi diam. | 4.21–8.02 |
| 3 | `[playful] [excited]` | Belanja stok itu bukan uang hangus, tapi juga bukan untung. | 8.21–11.66 |
| 4 | `[playful] [excited]` | Itu modal yang nyangkut, dan baru jadi biaya pas barangnya laku. | 12.04–15.98 |
| 5 | `[playful] [excited] [surprised]` | Kalau semuanya langsung dianggap biaya, labamu kelihatan jeblok. Padahal barangnya masih ada. | 16.06–21.43 |
| 6 | `[playful] [excited]` | MasterPajak AI bantu catat belanja stok di pembukuan, biar laporan laba rugimu kebaca bener. | 21.50–27.03 |
| 7 | `[playful] [excited]` | Jualan jalan terus, pajaknya AI yang urus. | 27.09–30.07 |
| 8 | `[playful] [excited] [confident]` | Coba kalkulator gratis. Link di bio. | 30.14–32.46 |

Spoken length is 32.2 s (0.3 → 32.46). `TM.total` = last word end + 1.6 s.

**Listen-check (faster-whisper `small`, numpy input):** every word is present and no tag is read aloud.
`VO_MP18_whisper_small.json` holds the transcript of the chosen take.
- **Line 2 was reworded.** With the first wording ("Isinya uang kamu, yang lagi diam."), four takes all came back from whisper
  as "lagi **biyem**/biam". A control line from the same voice ("Uangnya lagi diam di rak.") came back correctly, so I
  re-voiced. The reworded take E is heard as "lagi **diem**", the normal colloquial pronunciation.
- **Whisper quirks that appeared in every take:** "saldo kok" → "saudok kok", "laba rugimu" → "labar rugimu" (liaison), and a
  low confidence on the final "bio". All look like whisper-small artefacts. The lead may still want a quick listen to those
  three spots.

## TM keys (all are real word times, from the JSON alignment + 0.30)
`hook 1.02` (Stok) · `saldo 2.70` · `tipis 3.26` · `balik 4.21` (Coba) · `isi 5.66` · `uang 6.38` · `diam 7.38` · `bel 8.21`
(Belanja) · `hangus 9.58` · `untung 11.10` · `modal 12.04` (Itu) · `nyangkut 12.62` · `biaya 13.42` (dan) · `laku 14.70` (pas) ·
`kalau 16.06` · `semua 16.94` (dianggap) · `jeblok 18.14` (labamu) · `padahal 19.69` · `sol 21.50` (MasterPajak) · `catat 22.94` ·
`pemb 23.82` · `lr 24.62` (biar) · `bener 25.94` (kebaca) · `end 27.09` (Jualan) · `cta 30.14` · `bio 31.66` · `total 34.06`.
Every animation and robot beat is an offset from these keys. `tools/sfx.py` reads them from `index.html`.

## Scenes
| # | time (s) | VO | what happens |
|---|---|---|---|
| S1 | 0 – 4.21 | L1 | Hook in the warehouse. The camera pushes in slowly on the full shelf, and the robot rises bottom-right. Text: "Stok numpuk di rak, / tapi saldo / kok **tipis?**". The saldo card (Rp850.000, Ilustrasi data) swings in at 2.4 and turns edge-on at 3.4. The robot shrugs. |
| S2 | 4.21 – 8.21 | L2 | Text: "coba / **balik** kardusnya." The camera moves closer, and the hero box (middle tier) hops and flips at 4.63, so its money face shows. Text: "isinya?". At 6.38 the domino wave flips the other 11 boxes and the camera pulls back. Text: "uang kamu / yang lagi **diam.**", the pause badge appears and the boxes settle. The shelf's "Ilustrasi data" chip appears. |
| S3 | 8.21 – 12.04 | L3 | The hero box floats out toward the camera (overlay rig) while the shelf blurs (`#dofM` backdrop blur) behind a light veil. The "UANG HANGUS?" sticker slaps on with a red X at 9.7 and falls. The "UNTUNG?" sticker does the same at 11.2. The robot shakes its head twice. |
| S4 | 12.04 – 16.06 | L4 | The box goes back into its slot and the camera pulls back (shelf left, cards right). The MODAL tag hooks on and swings; "nyangkut" appears at 12.67. The BIAYA card ("modal barang terjual", Rp0) arrives at 13.37. At 14.75 / 14.97 two boxes flip back to cardboard, get the LAKU stamp, send their Rp400.000 chips to BIAYA (→ Rp800.000) and drop out. |
| S5 | 16.06 – 21.50 | L5 | "kalau semuanya langsung / dianggap biaya,". Ten chips stream into BIAYA (→ Rp4.800.000, "semua belanja stok" in red), the boxes turn plain, the MODAL tag drops and BIAYA shakes. "labamu kelihatan / **jeblok.**": the LABA card (Rp500.000) arrives, then rolls to −Rp3.500.000 and drops at 18.86. The robot gets X-eyes. "padahal / barangnya / masih **ada.**": the cards swish out, the camera returns to the shelf, the 10 boxes hop and glow, and the MASIH DI RAK card appears. The robot points. |
| T | 21.02 – 21.58 | – | Series band sweep with the "MasterPajak AI" marquee. |
| S6 | 21.50 – 27.09 | L6 | Brand (navy). The robot rises half-body bottom-left and the chest hologram is at full alpha from 22.22 to 26.79 (4.6 s, x 510–930). The Pembukuan card rises, and three chips arc in and fill the rows: Belanja stok Rp4.800.000 · Stok laku Rp800.000 · Sisa stok Rp4.000.000. Captions: "bantu catat belanja stok di / **pembukuan.**". At 24.80 the Laporan laba rugi card lifts out (the pembukuan card recedes and blurs). Captions: "biar laporan laba rugimu / **kebaca bener.**", stabilo on Laba Rp500.000, the ✓ stamp and a shine. |
| T | 26.57 – 27.6 | – | Series beam + iris. |
| S7 | 27.09 – 34.06 | L7–L8 | End card: "Jualan jalan terus," / "pajaknya AI yang urus." at 28.39, the CTA pill "Coba kalkulator gratis" at 30.14, "Link di bio" at 31.66. The robot waves, then points at the CTA. The logo hologram is on the left (x 150–570) from 27.84 to the end (6.2 s). |

## Numbers (all illustrative, all add up)
- **Stock:** 12 kardus × Rp400.000 = **Rp4.800.000** belanja stok. 2 laku = modal barang terjual **Rp800.000**. 10 left =
  **Rp4.000.000**. Check: 800.000 + 4.000.000 = 4.800.000.
- **Laporan laba rugi:** Penjualan Rp1.500.000 − Modal barang terjual Rp800.000 − Ongkir & iklan Rp200.000 = **Laba
  Rp500.000**.
- **Wrong treatment (S5):** all of the belanja stok counted as biaya gives 1.500.000 − 4.800.000 − 200.000 =
  **−Rp3.500.000**. That equals 500.000 − 4.000.000, the stock that is still on the shelf.
- **Saldo usaha:** Rp850.000, a standalone illustration.
- No tax rate, deadline, penalty, guarantee or tax-treatment advice anywhere. The features named are only pembukuan, laporan
  laba rugi and the kalkulator gratis (end card).

## Labels
- **"Ilustrasi data":** the saldo card; the shelf's money faces (a screen chip bottom-left from 6.9 s to the end of the studio
  scenes); the BIAYA, LABA and MASIH DI RAK cards; the Pembukuan card; the Laporan laba rugi card; the cover.
- **"Simulasi alur":** the Pembukuan card and the Laporan laba rugi card.
- No logos, marketplaces, banks, e-wallets or government marks. The boxes say only "STOK". The money is a generic illustrated
  bundle, not real Rupiah artwork.

## Files
- `index.html`: the composition, with `TM` at the top.
  - The studio world (shelf + 12 kardus cubes) is built in the script. An overlay twin rig (`#w1b`) holds everything that sits
    in front of the shelf: the floating box, stickers, pause badge, MODAL tag and the two sold boxes, so none of it is
    depth-sorted against the shelf.
  - The money chips are screen-space. Their start points are the measured money-face centres (`FACE`, camera KM1). The brand
    mini-chip targets (`ROWX`/`ROWY`) were measured the same way. Re-measure both if a camera or card moves.
- `robot_perf.js`: the robot choreography. CUTS are at `sol−0.05` and `end−0.01`. Light scenes: small full-body host
  bottom-right (x 920, h 500). Brand and end follow the series template.
- `lipsync.js` comes from `tools/lipsync.py assets/audio/vo.wav lipsync.js`, so the robot's mouth follows the real VO.
- `tools/sfx.py` writes `assets/audio/sfx.wav` (34.06 s, synthesised). It covers:
  - warehouse air, marker strokes, the saldo swing, the box hop / flip / knock and the 11-box domino
  - a soft till "ching", the pause badge, the depth swell, sticker slaps with red-X buzzes and falls
  - the MODAL clink, card whooshes, LAKU stamps, chip whooshes with landing ticks and counter clicks
  - the "jeblok" drop, the padahal hops with a shimmer, the bands, the hologram fx, the pembukuan chips, the laba rugi card,
    the stamp chime and the shine
  - the beam/iris boom and the end pops with a chime
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP18_STOK.png`.
  - Copy: "STOK ITU / UANG DIAM" (stabilo) / "modal yang nyangkut di rak", plus the pill "Modal, bukan untung ✓".
  - Picture: a turned-round money kardus (Rp400.000) in front of two plain boxes on a navy shelf board, with the MODAL tag
    hanging off it. Labelled "Ilustrasi data". The live robot points at it.
  - All of it sits inside the 4:5 crop (y 285–1635).

## QA done
- **`hyperframes validate`:** 0 errors (`lipsync.js` exists, so there are no 404s). The 6 contrast warnings are all the
  hidden series marquee, the same as in the approved videos.
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`): 40 frames covering every scene, every cut and transition midpoint,
  and the end card. The contact sheets are in the scratchpad: `mp18/QA_final_A … QA_final_E/contact-sheet.jpg`.
- **Text containment check** (every visible text run against its card, chip, sticker, tag or face box at 13 times): the only
  hits are the off-window values of the masked BIAYA/LABA odometer strips, which is by design.
- **Frame-edge sweep** (0–34 s, step 0.25–0.5): the only hits are single frames of cards flying in or out (the saldo card at
  4.5, the BIAYA/LABA/MASIH cards at 20.0–20.5) and the series marquee. Nothing is cut on a held frame.
- **Safe zone:** text and cards stay inside x 60–1020, y 220–1600. Both holograms stay inside the 120 px side margins.

## Known issues / notes for the lead
- Line 1 opens with an audible sigh (the auto `[sighs]` tag), so the first word lands at 1.02 s. The visuals (shelf, rising
  text, robot) start at 0.
- In S3, `#dofM` animates a `backdrop-filter` blur (8.2–12.6 s). It renders correctly in the real-runtime snapshots, but it is
  the heaviest layer if the render is slow.
- On some held light-scene frames the robot's hand or arm brushes the corner of the bottom-right box. The box's "STOK" label
  stays readable, and no overlay text is ever covered.
- The saldo card's "tipis" gag deliberately leaves it as a thin sliver for about 0.9 s before it flies off.
- The git status shows the folder was already picked up by a commit while I worked. I did not commit anything.
