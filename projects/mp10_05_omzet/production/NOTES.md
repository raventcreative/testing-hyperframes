# Video 5 · Omzet vs Untung — production notes

1080×1920, 33.5 s, HyperFrames 0.8.186 (same tech skeleton as Video 1). Title: "MasterPajak AI · Video 5 — Omzet vs Untung".
Served for QA at `http://127.0.0.1:8805/index.html`. Not rendered and not committed here (the lead renders and commits).

## Concept
A paper "studio" with a real CSS-3D camera rig (`.stage > .cam (anchor, dolly z, tilt X) > .yaw (orbit Y) > .pan (−focus)`).
The **omzet** is a tall 3D money column (navy, stacked-bill texture, gold-rimmed top) that shoots up while an **odometer** counts to
Rp50.000.000. Each cost is **sliced off by a yellow laser**, turns grey, gets its tag, then **peels off and falls past the camera**
(biaya produk → ongkir + biaya platform as two pieces → iklan) while the odometer rolls down. A dashed **ghost** of each lost chunk stays,
so what is left (yellow block, **LABA**, stabilo on the kicker) is read against the full omzet height.
Then a **rack-focus** scene: sellers look at the OMZET card (sharp), the camera dollies past it onto the LABA card (focus pull), and three
business decisions branch off it. Brand: series band sweep → robot rises + chest hologram → one **Laporan laba rugi** card whose three
rows (penjualan / biaya / laba) are dealt apart in 3D ("pisahkan") → series end card.

Depth tools used: perspective camera with crane/orbit/dolly moves, low-angle macro open, backdrop-filter depth of field (`#dof1a/b`,
`#dof3`), CSS filter rack focus, far bokeh layers for parallax, floor grid in perspective, contact shadows, horizontal SVG motion blur on
the whip pan, vertical SVG motion blur on the odometer roll.

## Scenes ↔ TM keys ↔ VO (one key per VO line, plus sub-beats)
| key | time (s) | VO line | picture |
|---|---|---|---|
| `hook` | 0.35 | Omzet bulan ini kelihatan gede. | low-angle macro, column rises, odometer counts up to Rp50.000.000, robot rises bottom-right and looks up |
| `ask` | 2.75 | Tapi untungnya berapa? | camera pulls back to the 3/4 studio view; "tapi untungnya / berapa?"; robot shrugs |
| `c1` | 4.85 | Kurangi biaya produk. | laser slice, chunk turns grey + "Biaya produk", tag −Rp23.500.000, chunk falls; kicker → SISANYA |
| `c2` | 6.60 | Kurangi ongkir dan biaya platform. | two pieces (Ongkir, Biaya platform) fall one after the other; tag −Rp9.000.000 |
| `c3` | 9.15 | Kurangi iklan. | Iklan chunk falls; tag −Rp6.500.000; odometer lands on Rp11.000.000 |
| `laba` | 10.75 | Nah... sisanya ini yang beneran laba. | tags clear, camera cranes down/pushes in, the rest turns yellow; robot points |
| `labaW` | 13.10 | (word "laba") | "LABA" on the block + shine, kicker rolls to LABA with stabilo |
| `seller` | 14.50 | Banyak seller cuma lihat omzet, | whip pan (`seller − 0.36`); OMZET card sharp, LABA card blurred behind |
| `dec` | 16.85 | padahal keputusan bisnis harusnya dari laba. | dolly past OMZET + rack focus onto LABA; decision chips (restok, budget iklan, harga jual); stabilo on "laba" |
| `sol` | 19.70 | MasterPajak AI bantu pisahkan penjualan, biaya, dan laba dalam satu laporan sederhana. | bands (`sol − 0.48`) → robot + chest hologram (sol+0.55…end−0.3, ≈5.3 s); report card rows spread at sol+1.3, filled at +1.75 / +2.4 / +3.1; "satu laporan sederhana." at +3.9 |
| `end` | 25.60 | Jualan jalan terus, pajaknya AI yang urus. | beam + iris → series end card, robot waves, logo hologram left (end+0.75 → total, ≈7.2 s) |
| `cta` | 28.75 | Coba kalkulator pajak gratisnya. | CTA pill "Coba kalkulator gratis"; robot points |
| `bio` | 30.90 | Link di bio. | "Link di bio"; robot waves |
| `total` | 33.50 | — | `data-duration` = 33.5 |

Timing is planned for ~2.4 words/s with short pauses; re-time by editing `window.TM` only (robot, SFX and all tweens read it).

## Brand-rule checklist
- All demo numbers carry **"Ilustrasi data"**: odometer chip (S1–S2, covers the tags), both cards in S3, report card header, cover.
- No tax rates, deadlines, penalties or guarantees anywhere. Features named only as "laporan laba rugi" (+ kalkulator gratis in the CTA).
- No DJP/government branding. Spelling MasterPajak AI; tagline and CTA exactly as the series end card.
- Hologram: brand moment (x 720, y 1520, w 420) and end card (x 360, y 1500, w 420) — inside the safe zone, ≥ 4 s each.
- Robot hosts the whole film: small full-body host bottom-right in the light scenes (never over text), ducks out before the bands,
  half-body + hologram for brand, series end-card choreography.

## Files
- `index.html` — composition; `robot_perf.js` — robot choreography (CUTS at `sol − 0.05`, `end − 0.01`).
- `tools/sfx.py` → `assets/audio/sfx.wav` (33.5 s, synthesised, cues from TM).
- `thumbnail/cover.html` → `thumbnail/COVER_MP05_OMZET_UNTUNG.png` (key content inside the 4:5 crop y 285–1635).

## QA done
- Snapshots of every scene and transition midpoint; containment check (every text leaf inside its tag/card/row/face, no auto-shrink needed).
- `edgecheck.cjs`: only transitional hits remain — the whip pan at `seller − 0.36…+0.06` (motion-blurred, masked split chars) and the
  series marquee in the band sweep (same as Video 1). Falling chunk labels fade before reaching the frame edge; card A fades before it leaves.
- Odometer digits are drawn once to a canvas (after fonts load) and rolled as a repeat-y background, so no hidden text strips.
- Console: only the expected `lipsync.js` 404 (loaded with `onerror`, VO not recorded yet).

## Not done / open
- Full render not run (lead). VO not recorded: robot lip-sync is driven later by `lipsync.js`; TM should be re-timed to the real VO.
- The odometer roll and whip use SVG `url(#…)` filters (verified in Chromium snapshots); if a renderer build ever drops them the scene
  still works, only without the motion blur.
