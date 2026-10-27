# MOTION BLUEPRINT — REELS X-RAY v2

Timing comes from `production/word_timing.json` (CTC alignment on the real VO). Cuts are hard cuts on phrase boundaries.

Four motifs repeat across the film:
- **SHAPE MATCH** — the circle family: gear → dial → drum, lens → spool, magnifier → iris.
- **LINE MATCH** — rail / line / composer.
- **OBJECT HANDOFF**
- **MECHANICAL TRANSITION**

| # | Time | Hero | Motif (reference) | Apex (word @ s) | Camera | Hand-off |
|---|---|---|---|---|---|---|
| 01 | 0.00–3.24 | User's mechanical phone, screen on | Mechanical transition (REF-B), apex recipe (REF-H) | dibongkar 1.88 | push-in → into the seam | Same phone, closer |
| 02 | 3.24–5.18 | Glass swings open over the gears | Mechanical hinge (REF-B) | kebuka 4.38 | dolly + ¾ turn | Glass flies square-on → type plate |
| 03 | 5.18–7.22 | Dimensional type, cards, ribbon | Staged entrances (REF-A) | Teks 5.28 / kartu 5.84 / transisi 6.44 | slow orbit | Ribbon → rail (LINE MATCH) |
| 04 | 7.22–10.42 | User's camera on rail + suspended planes | Camera track + parallax (REF-B) | masing-masing 9.24 | tracks the dolly | Lens circle → spool (SHAPE MATCH) |
| 05 | 10.42–13.78 | Blueprint machine | Mechanical | kode 12.98 | push | Cartridge → navy cube |
| 06 | 13.78–16.72 | Search bar → user's Claude Code screen | REF-M morph, REF-D panel unfold, LINE MATCH, SCALE MORPH | Claude 15.82 (send) | follows the caret | Screen tips onto the round stage |
| 07 | 16.72–18.32 | Round production stage | Object assembly | scene 17.76 | push | Drive gear → dial (SHAPE MATCH) |
| 08 | 18.32–20.22 | User's navy dial | Rotating dial (REF-B) | geraknya 19.44 (needle stops) | push | Dial → sprocket drum |
| 09 | 20.22–22.82 | Render press | Mechanical | MP4 21.76 | pull-back | Reel drops to a drawer |
| 10 | 22.82–25.58 | Porcelain cabinet | Opening box (REF-B) | modular 24.76 | push | Ring on the product module |
| 11 | 25.58–28.54 | Editing console | Guided selection (REF-A) | produk / kalimat / timing | follows each edit | Parts lift |
| 12 | 28.54–32.48 | Reassembly + before/after | Comparison (REF-C) | baru 29.56 / dipakai 31.64 | snap zoom HIGH | Twin reels → template |
| 13 | 32.48–37.88 | Template → 3 dioramas | Camera track | edukasi / promo / iklan | track | Meter dial |
| 14 | 37.88–41.60 | Credit meter vs local render | Dial (REF-B) | kredit 39.74 | digital zoom | Tray → scale pan |
| 15 | 41.60–45.20 | Balance scale | Mechanical | berbiaya 44.30 (amber) | calm push | Pivot → magnifier |
| 16 | 45.20–50.26 | QC studio | Guided selection | visual / transisi / sinkron | follows the lens | Iris (MASK REVEAL) |
| 17 | 50.26–52.26 | Glass repo case + 3D GitHub mark | Opening case (REF-B), orbit reveal | repo 50.52 / prompt 51.30 | push | Lid → bubble |
| 18 | 52.26–54.60 | EDITOR bubble + logo lockup | REF-H lockup | EDITOR 52.64 | snap SUBTLE → still | Still final frame |

## Sound

VO-safe SFX are documented in `tools/gen_sfx.py`. The rules:
- Every SFX is high-passed.
- Each sound's peak lands on its apex.
- Levels duck against the measured VO.
- Typing is a single clip per typed span.
- At most 2 cues per 0.45 s.
- No music.
