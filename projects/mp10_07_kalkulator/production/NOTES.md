# MasterPajak AI · Video 7 — Kalkulator Gratis 3 Langkah

1080×1920 · 33.0 s (`TM.total` = `data-duration` = 33) · HyperFrames 0.8.186 (tech skeleton from Video 1, unchanged).
Not rendered here. The lead renders and commits.

## Concept
A guided tour of the free calculator inside a **3D navy world**. A tilted 3D phone (bezel thickness layers, soft shadow, glare
sweep) runs a **generic calculator UI** (label **"Simulasi alur"**, no real recording yet). Each step is introduced by a
**giant extruded 3D numeral** that flies in from the lens and settles behind the phone (parallax), plus camera swings and
push-ins on the active UI. The step‑2 amount card and the step‑3 result card **lift off the glass in 3D**. In the result
beat the camera pulls back, the phone recedes **out of focus (depth of field)** and the floating "Estimasi pajak" card is the
hero. The robot hosts the whole film: it peeks in during the hook, rises with the **chest hologram** at the brand line, guides
each step, and ends on the series end card.

- Hook (paper, light): floating seller objects at several depths with foreground and background blur, a slow camera dolly,
  and a whip into the band sweep. Headline "penasaran / estimasi pajak (stabilo) / usahamu?" + a 3D card "ESTIMASI PAJAK
  USAHAMU · Rp ?".
- Brand → steps → result (navy): HUD top-left (small label + big title), "● SIMULASI ALUR" chip top-right (on screen whenever the UI is).
- End: series template (beam + iris → tagline in two lines, CTA pill "Coba kalkulator gratis", chips "Gratis" +
  "Cuma beberapa menit", "Link di bio ↓", robot waves and points, logo hologram left). The VO has no tagline line, but the
  tagline is still shown, as briefed.

## TM keys ↔ VO (VO_SCRIPTS.md §7). One key per VO line, plus 3 sub-beats
| key | t (s) | VO |
|---|---|---|
| `hook` | 0.3 | **L1a** Penasaran estimasi pajak usahamu? |
| `brand` | 3.0 | **L1b** Coba kalkulator gratis MasterPajak AI. *(2nd sentence of line 1, brand moment)* |
| `s1` | 8.0 | **L2** Satu: isi data usahamu. |
| `s2` | 12.0 | **L3** Dua: masukkan omzetmu. |
| `s3` | 15.9 | **L4** Tiga: lihat estimasi pajaknya. |
| `res` | 20.2 | **L5** Hasilnya estimasi, jadi kamu punya gambaran … |
| `kon` | 23.1 | *(sub-beat of L5)* … sebelum ngobrol sama tim atau konsultan. |
| `end` | 26.4 | **L6** Gratis, cuma butuh beberapa menit. |
| `bio` | 28.5 | *(sub-beat of L6)* Link ada di bio. |
| `total` | 33.0 | end |

Timing was planned for ~2.4 words/s with short pauses. The VO is not recorded yet. `lipsync.js` is loaded with `onerror`,
so the 404 for it is expected. When re-timing to the real VO, keep these gaps:
- `s1 − brand ≥ 4.95 s`: the brand hologram is at full alpha from `brand+0.72` to `s1−0.2`, which must stay ≥ 4 s. It is 4.08 s now.
- `total − end ≥ 4.8 s`: the end-card hologram runs from `end+0.75` to the end. It is 5.85 s now.
- Each step needs about 3.9 s for its UI action (typing, keypad, count-up). Step‑internal beats are offsets from `s1/s2/s3`.

## Scenes
| # | time | scene | what happens |
|---|---|---|---|
| S0 | 0 – 3.0 | Hook (paper, 3D) | dolly through floating objects (blurred near/far), headline kinetic + stabilo, "Rp ?" card flies in, robot peeks bottom-right with a curious head tilt |
| T | 2.55 – 3.75 | band sweep | Video 1 bands + "MasterPajak AI" marquee, then the bands slide out |
| S1 | 3.0 – 7.5 | Brand | phone flies in from depth (start screen: Kalkulator Pajak · GRATIS · 3 langkah · cuma beberapa menit), HUD "coba / Kalkulator gratis", robot rises bottom-left + **chest hologram** (x 740, y 1500), tap on "Mulai hitung" |
| S2 | 7.5 – 11.5 | Langkah 1 · Isi data usaha | numeral 1, push-in on the form: name typed, "Fashion & aksesoris" selected, chips Marketplace + Media sosial, "Lanjut" |
| S3 | 11.5 – 15.4 | Langkah 2 · Masukkan omzet | numeral 2, amount card lifts off the glass, 8 keypad presses → Rp28.450.000 (**Ilustrasi data**), "Hitung estimasi" |
| S4 | 15.4 – 19.65 | Langkah 3 · Lihat estimasi | numeral 3, loader, navy result card **"ESTIMASI PAJAK · Rp96.500 · Ilustrasi data · Hasil berupa estimasi"** counts up, ringkasan rows, the card lifts off |
| S5 | 19.65 – 25.9 | Hasilnya estimasi | camera pull-back, phone recedes + defocus, result card hero, "jadi kamu punya gambaran", consult card "sebelum ngobrol sama **tim atau konsultan**" + "PENDAMPINGAN SESUAI LAYANAN", robot glides right and points |
| T | 25.9 – 26.9 | beam + iris | Video 1 pattern |
| S6 | 26.4 – 33.0 | End card | tagline, CTA, Gratis · Cuma beberapa menit, Link di bio, robot wave/point/wave, logo hologram left (x 360, y 1500) |

## Brand-rule checks
- No tax rate, deadline, penalty or guarantee anywhere. The result shows an illustrative amount only. Omzet Rp28.450.000 and
  estimate Rp96.500 were chosen so their ratio does **not** match any real rate. Both carry "Ilustrasi data". The ringkasan
  header reads "RINGKASAN · ILUSTRASI DATA".
- "Simulasi alur" is on screen for the whole UI part (brand → result).
- Features are named only as allowed: kalkulator gratis, estimasi pajak. The expert line reads "tim atau konsultan" (VO wording)
  with "pendampingan sesuai layanan".
- No DJP or government marks. The spelling "MasterPajak AI" is used everywhere.
- Text containment: an automated text-vs-box sweep every 0.5 s over the whole film found no overflow. The only hits were the
  band marquee, which is intentionally clipped by its band as in Video 1. The frame-edge check is clean (the hook coins
  carry no text).
- Safe zone: the HUD sits at y ≥ 228, x 70–1020. The holograms are at x 530–950 (brand) and 150–570 (end), y ≈ 1450–1600.

## Swapping in the real calculator recording
In `index.html` look for **`SWAP POINT`** inside `#ui`. Replace the four `.scr` screens with a `<video>` (468×1008, screen
size) and re-time `TM.s1/s2/s3` to the recording. The twins `#amtT` and `#resT` are clones of the simulated cards and fly
in 3D. Remove them, or rebuild them from frames of the recording, along with their tweens (step‑2 lift block, step‑3 lift,
and the result flight in `buildReady["kalk3d"]`). The step labels in the HUD and the numerals stay. If the real flow has
different steps, change the HUD titles `#hB1–#hB3` and the start-screen list.

## Files
- `index.html`: composition. `robot_perf.js`: robot choreography (CUTS at `brand−0.05` and `end−0.01`).
- `tools/sfx.py` writes `assets/audio/sfx.wav` (33.0 s, synthesised: dolly air, marker, bands, phone fly-in, holo fx,
  numeral fly-bys + thuds, typing/keypad/taps, loader shimmer, result chime + count ticks, lifts, beam/iris, end pops).
- `thumbnail/cover.html` renders to `thumbnail/COVER_MP07_KALKULATOR.png`. Everything is inside the 4:5 crop (y 285–1635).

## Known issues / notes for the lead
- The UI is a generic simulation (no recording yet). The step wording follows the brief (isi data usaha → masukkan omzet → lihat estimasi).
- The numerals have no DOF blur. Blurring their 8 extrusion layers made frames about 5× slower to composite under
  SwiftShader. Depth comes from parallax and extrusion. DOF is used in the hook (blurred objects) and the result scene
  (defocused phone).
- The machine was heavily loaded during QA (load avg 30–39). Snapshots took 3–35 s per frame, and the step section is the
  heaviest part to render.
- In the hook, the robot's "hand to chin" gesture sits mostly below frame. Only the curious head tilt reads.
- The consult card has a small bubble "Udah ada gambarannya." that is not in the VO. Delete `#kbub` if strict VO-only copy is wanted.
