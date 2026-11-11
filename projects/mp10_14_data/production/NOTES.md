# MasterPajak AI · Video 14 — Siapin 4 Data Ini

1080×1920 · 33.5 s (`TM.total` = `data-duration` = 33.5) · HyperFrames 0.8.186 (tech skeleton and series ending from Video 1).
Not rendered here, not committed. The lead renders and commits.

## Concept
A checklist film set in one **CSS-3D paper studio**: a navy archive box labelled **"DATA USAHA"** sits on a grid floor, and a
moving camera (dolly, orbit, tilt) films it. The box has outer and inner walls, lit rims, a hinged lid and a label with four
checkboxes.
- **Hook:** a ghost card reading "ESTIMASI PAJAK · Rp ???" floats over the closed box.
- **"Siapin 4 data ini dulu":** the ghost card recedes into depth, the lid swings open, and a progress HUD drops in
  (DATA SIAP 0/4, four bars).
- **The four items:** each data item is a tangible 3D object. It flies in from off-camera, hovers as the hero (tilted, big
  numbered title), gets a yellow **tick stamp** (HUD bar fills, counter rolls to k/4), then drops into the box as a file.
  A checkbox on the box label ticks when it lands.
- **"Udah kekumpul?":** the files sink in, the lid closes with a thump, a big tick stamp lands on the label, and the HUD shows
  "LENGKAP ✓".
- **Brand (navy, series band sweep):** the robot rises with the chest hologram. The box drops in, its lid pops off, and it tips
  and **pours four file chips into a MasterPajak AI "Pembukuan" card**, filling the rows (penjualan, biaya, mutasi rekening,
  nota & bukti transfer). On "estimasi pajaknya" the pembukuan card recedes out of focus and the **"Estimasi pajak" card lifts
  out of it**. An odometer rolls to **Rp127.400**, labelled "Ilustrasi data", "Hasil berupa estimasi" and "Simulasi alur".
  No rate is shown.
- **End:** series end card (beam + iris, the tagline in two lines, CTA pill "Coba kalkulator gratis", "Link di bio"). The robot
  waves and points, and the logo hologram sits on the left.

The four items:
1. **Catatan penjualan**: an order sheet (stacked pages) with 6 orders and a total.
2. **Catatan biaya**: a thermal receipt. On "termasuk ongkir dan iklan", two tags pop out (Ongkir / Iklan) and are stabilo-marked
   on the receipt and in the sub-line.
3. **Mutasi rekening usaha**: a generic statement ("Rekening usaha · •••• 4821"). No bank name and no logo.
4. **Nota & bukti transfer**: a handwritten nota stamped LUNAS, plus a generic "Transfer berhasil" phone card.

## TM keys ↔ VO (VO_SCRIPTS.md §14). One key per VO line, plus sub-beats
| key | t (s) | VO |
|---|---|---|
| `hook` | 0.3 | **L1a** Mau tahu gambaran pajak usahamu? |
| `siap` | 2.7 | **L1b** Siapin empat data ini dulu. *(2nd sentence of line 1)* |
| `d1` | 5.4 | **L2** Satu: catatan penjualan. |
| `d2` | 8.0 | **L3** Dua: catatan biaya, … |
| `d2b` | 9.6 | *(sub-beat of L3)* … termasuk ongkir dan iklan. |
| `d3` | 11.7 | **L4** Tiga: mutasi rekening usaha. |
| `d4` | 14.3 | **L5** Empat: nota dan bukti transfer. |
| `kum` | 17.1 | **L6a** Udah kekumpul? |
| `sol` | 18.4 | **L6b** MasterPajak AI bantu menata semuanya jadi pembukuan, … *(band sweep at sol−0.48, brand moment)* |
| `est` | 21.8 | **L6c** … terus bantu hitung estimasi pajaknya. |
| `end` | 25.6 | **L7a** Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 28.6 | **L7b** Coba kalkulator pajak gratisnya. |
| `bio` | 30.7 | **L7c** Link di bio. |
| `total` | 33.5 | end |

The timing was planned for about 2.4 words/s with short pauses. The VO is not recorded yet. `lipsync.js` is loaded with
`onerror`, so its 404 is expected. Every other beat is an offset from these keys, so re-timing means editing `window.TM`, then
running `python3 tools/sfx.py` again.

Keep these gaps when you re-time:
- `end − sol ≥ 5.0 s`: the brand hologram is at full alpha from `sol+0.72` to `end−0.3` (6.2 s now, must stay ≥ 4 s).
- `total − end ≥ 4.8 s`: the end-card hologram runs from `end+0.75` to the end (7.15 s now).
- Item beats need `d(k+1) − d(k) ≥ 2.5 s`. Within that, the fly-in takes 0.82 s, the tick lands at `+1.05` (item 2:
  `d2b+0.8`), and the drop starts at `next−0.88`.
- `d2b − d2 ≥ 1.2 s`, `d3 − d2b ≥ 1.9 s`, `sol − kum ≥ 1.3 s` (the files sink and the lid closes before the bands).
- `est − sol ≥ 3.0 s`: the pour and row fill run from `sol+1.0` to `sol+2.3`, and "pembukuan." sits at `sol+2.25`.

## Scenes
| # | time | scene | what happens |
|---|---|---|---|
| S1 | 0 – 2.7 | Hook (paper studio, 3D) | Wide camera push-in on the closed box. The ghost card "ESTIMASI PAJAK · Rp ???" floats and its "?" marks wobble. Text: "Mau tahu / gambaran pajak (stabilo) / usahamu?". The robot rises bottom-right with a curious head tilt. |
| S2 | 2.7 – 5.4 | Siapin 4 data | The ghost card recedes behind the opening lid, and the lid swings open (box jiggle). Text: "siapin / 4 data (stabilo) ini dulu." The HUD drops in at 0/4. The robot points at the box. |
| S3.1 | 5.4 – 8.0 | ① Catatan penjualan | The order sheet flies in from the left and hovers, tick, HUD 1/4, then it drops into the box and checkbox 1 ticks. |
| S3.2 | 8.0 – 11.7 | ② Catatan biaya | The receipt flies in from the right. On `d2b` the Ongkir and Iklan tags pop out with stabilo (sub-line "termasuk ongkir & iklan"). Tick, 2/4, drop. The robot points at the tags. |
| S3.3 | 11.7 – 14.3 | ③ Mutasi rekening usaha | The statement flies in from low-left, tick, 3/4, drop. |
| S3.4 | 14.3 – 17.1 | ④ Nota & bukti transfer | The nota and phone card fly in from the right, tick, 4/4, drop. |
| S3b | 17.1 – 18.4 | Udah kekumpul? | The files sink, the lid closes (thump), the stamp lands on the label, and the HUD shows "LENGKAP ✓". The robot cheers with both arms. |
| T | 17.9 – 18.5 | Band sweep | Video 1 bands with the "MasterPajak AI" marquee. |
| S4 | 18.4 – 21.8 | Brand · pembukuan | The robot rises half-body bottom-left with the **chest hologram** (x 510–930, y ≈ 1450–1600). The box drops in, its lid pops off, and it tips and pours 4 chips into the "Pembukuan · MasterPajak AI" card ("Ilustrasi data", "Simulasi alur"). Rows fill with a flash. Captions "bantu menata semuanya jadi / pembukuan." with an underline sweep. |
| S4b | 21.8 – 25.6 | Estimasi pajak | The pembukuan card recedes and blurs. The "Estimasi pajak" card lifts out, the odometer rolls 000.000 → 127.400, and a shine sweeps across. Captions "terus bantu hitung / estimasi pajak." The robot looks at the card and smiles. |
| T | 25.1 – 26.1 | Beam + iris | Video 1 pattern. |
| S5 | 25.6 – 33.5 | End card | The tagline in two lines, the CTA pill and its pulse, "Link di bio". The robot waves, points and waves again. The logo hologram is on the left (x 150–570, y ≈ 1450–1560). |

## Brand-rule checks
- **Numbers:** no tax rate, deadline, penalty or guarantee anywhere. The estimate is an illustrative amount, Rp127.400, labelled
  "Ilustrasi data", "Hasil berupa estimasi" and "Simulasi alur". The pembukuan shows Penjualan Rp38.640.000, and
  127.400 / 38.640.000 ≈ 0,33 % matches no real rate.
- **"Ilustrasi data":** every object with demo numbers carries this chip. That covers all four items (both papers of item 4), the
  pembukuan card and the estimate card. The pembukuan and estimate UI also carry "Simulasi alur".
- **Generic documents:** the statement and the transfer card are generic, with no bank names or logos. There are no
  DJP/government marks. The spelling "MasterPajak AI" is used throughout. Features are named only as pembukuan and estimasi
  pajak, plus the kalkulator gratis on the end card. The tagline and CTA match the brief exactly.
- **Text containment:** an automated check with every transform disabled found every text run inside its card, chip or box. The
  only hits are intended: the HUD counter's off-window digits (masked strip) and the series band marquee. The frame-edge sweep
  every 0.2 s found no text cut on held frames. The only hits were single frames of items entering from off-screen, plus the
  marquee.
- **Safe zone:** the HUD and titles sit at x 70–1010, y 230–570. The holograms stay inside x 120–960, y ≤ 1600.
- **Robot:** it never covers text. On the light scenes it is a small full-body figure bottom-right, next to the box. On navy it
  is half-body bottom-left, below the cards, which end at y ≤ 1180.

## Real-runtime findings (fixed, and worth knowing for the render)
These were found with `npx hyperframes@0.8.186 snapshot`. They did not show in `snap.cjs`, because that tool runs with GPU
compositing, while the HyperFrames runtime probes to software compositing.
1. **The ghost card was invisible for the whole hook.** This is batch-1 lesson 3. All initial visibilities and transforms are
   now pinned with `tl.set(…, 0)`.
2. **Fractional opacity on a `preserve-3d` group gets clipped.** The software compositor flattens the group and keeps only its
   +x/+y quadrant, and the clipped part stops moving. Opacity is now tweened only on flat children. For example, the ghost card
   fades `#ghost .gh`, not `#ghost`.
3. **Thin parallel planes get mis-sorted.** Inside the box's 16 px wall slab, a back page showed through as a vertical sliver
   in front of the page. The fix:
   - The flying and hovering items now live in an **overlay rig**, `#w1b`, an exact twin of the studio camera (the `cam()`
     helper drives both rigs). They are never depth-sorted against the box.
   - At the start of each descent, the item hands over to a **flattened single-plane twin**, `#itNb`, in the studio world. Its
     pose is identical and it is already in its final state: tick on, tags tucked, stabilo on.
   - The stacked back pages are now box-shadows in the paper's own plane.

## QA done (final build)
- `hyperframes validate`: the only errors are the two `lipsync.js` 404s. The contrast warnings come from the marquee and from
  blurred or transitional frames, the same kind as the approved videos.
- Real-runtime snapshots of every scene, every transition midpoint and the end card, 37 frames (scratchpad
  `mp14/QA_final_A/contact-sheet-1..3.jpg` and `mp14/QA_final_B/contact-sheet-1..2.jpg`). The final estimate card is in
  `mp14/QA_final_est/`.

## Files
- `index.html`: the composition, with `TM` at the top. `robot_perf.js` holds the robot choreography; its CUTS are at `sol−0.05`
  and `end−0.01`.
- `tools/sfx.py` writes `assets/audio/sfx.wav` (33.5 s, synthesised). It contains:
  - studio air, the stabilo marker, the lid swing and cardboard knocks
  - per-item fly-in whooshes, tick pops with rising dings, HUD fill and counter clicks, paper drops into the box, checkbox
    ticks
  - the lid-close thump with the stamp chime
  - the bands, the hologram fx, the pour flutter with landing pops, odometer ticks with the result chime, the shine shimmer
  - the beam/iris boom and the end pops with a chime
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP14_4_DATA.png`: "SIAPIN / 4 DATA (stabilo) / sebelum cek gambaran
  pajakmu", with the open DATA USAHA box and a 4-item checklist card rising out of it. It has no numbers. The pill reads "Udah
  lengkap? ✓" and the live robot points. Everything sits inside the 4:5 crop (y 285–1635).

## Known issues / notes for the lead
- `hyperframes check` hit its 120 s deadline in the overlap pass because the machine was heavily loaded (load avg ≈ 21). It
  reported no composition errors. `validate` completes cleanly.
- While the box pours (≈ 19.0–20.6 s), the tipped box covers the M logo tile of the pembukuan card. The "Pembukuan" title stays
  readable, and the box leaves before "pembukuan." is spoken.
- On navy the robot points with the far arm, as in Videos 1 and 5, so the gesture is subtle. A near-arm point would put the hand
  over the hologram.
- The odometer shows rolling intermediate digits for about 1.3 s, by design. The stacked-page shadows on items 1 and 3 are subtle
  on the light background.
- `index.html` is about 75 KB, because the item papers are real HTML.
