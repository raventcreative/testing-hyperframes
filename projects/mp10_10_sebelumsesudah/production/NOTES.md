# Video 10 · Sebelum vs Sesudah — production notes

**Format:** 1080×1920, 32.0 s (`TM.total` = `data-duration` = 32.0), title "MasterPajak AI · Video 10 — Sebelum vs Sesudah".
**Status:** composition, robot choreography, SFX and cover are done. Full render and commit are left to the lead (per brief).

## Concept
Each comparison is a **3D before/after slider**: two worlds share one frame. **SEBELUM** is a light paper desk (perspective floor grid, floating objects at different depths, depth-of-field blur). **SESUDAH** is the navy brand world (perspective grid, glow, white UI cards in 3D). A yellow divider with a knob clips the SESUDAH world (`--dx` CSS var → `clip-path`). The **robot host grabs the knob and drags it**. The knob is placed in the robot's hand on every frame, sampled from the robot's filtered motion (`window.ROBOT_POS`). The robot lets go at the side-by-side moment, then the divider snaps open.
Directions alternate (R→L, L→R, R→L), so the robot ends each comparison on the other side of the frame. Comparisons are joined by horizontal whip pans: an SVG horizontal motion blur plus a pan of both worlds. The film ends with the series end card (beam → iris, tagline, CTA pill, "Link di bio", robot waves and points, logo hologram left).

## TM keys ↔ VO (VO_SCRIPTS.md §10)
| key | t (s) | VO line / beat |
|---|---|---|
| `l1` | 0.30 | **Ini cara lama: rekap manual, tiga file, angka nggak pernah cocok.** |
| `rk` | 1.45 | ↳ "rekap manual" (headline line 1, total typed by hand) |
| `tf` | 2.50 | ↳ "tiga file" (camera pulls back, badges 1-2-3, robot rises) |
| `nc` | 3.35 | ↳ "angka nggak pernah cocok" (stabilo on 3 totals, badges flip to ≠, files jitter, x-eyes) |
| `l2` | 5.90 | **Ini cara sekarang: catatan jualan, pembukuan, dan laporan dalam satu alur.** (drag 1 → SESUDAH, chest hologram) |
| `cj` | 7.20 | ↳ "catatan jualan" (step 1 lights) |
| `pb` | 8.20 | ↳ "pembukuan" (step 2) |
| `lp` | 9.00 | ↳ "laporan" (step 3) |
| `sa` | 9.60 | ↳ "dalam satu alur" (pulse runs the flow, "satu alur." in yellow) |
| `l3` | 11.40 | **Sebelum: nebak-nebak untung.** (whip at l3−0.3) |
| `l3b` | 13.50 | **Sesudah: laporan laba rugi yang jelas.** (drag 2) |
| `jl` | 14.90 | ↳ "jelas" (stabilo on Laba + headline) |
| `l4` | 16.40 | **Sebelum: bingung pajaknya berapa.** (whip at l4−0.3) |
| `l4b` | 18.60 | **Sesudah: ada estimasi pajak, plus tim ahli kalau perlu.** (drag 3, estimasi counts up) |
| `ta` | 20.30 | ↳ "plus tim ahli" (Tim ahli card, stabilo "sesuai layanan") |
| `l5` | 22.60 | **Jualan jalan terus, pajaknya AI yang urus.** (beam/iris at l5−0.5, end card) |
| `cta` | 26.10 | **Coba kalkulator pajak gratisnya.** (CTA pill "Coba kalkulator gratis") |
| `bio` | 28.00 | **Link di bio.** |
| `total` | 32.00 | end |

Planned for ~2.4 words/s plus short pauses. To re-time to the real ElevenLabs VO, edit only `window.TM`. Everything else follows: the drag windows in `window.RIG` (reach −0.75, grab −0.4, drag −0.05…+0.75, release/snap +0.95…+1.3 around `l2`/`l3b`/`l4b`), the robot keys, the knob path and `tools/sfx.py`.

## Scenes
1. **C1 SEBELUM (0–5.9)**: tag "SEBELUM · cara lama". The camera opens close on `rekap_manual_FINAL_v3.xlsx` while its total is typed by hand; the other two files are out of focus. It pulls back to three spreadsheet windows cascading in depth (pesanan_toko.csv, mutasi_bank.pdf). Totals Rp47.180.000 / Rp48.250.000 / Rp44.730.000 get stabilo, count badges flip to "≠", the windows jitter. The robot rises with the pull-back, points at the stack, shows x-eyes and shakes its head. The divider slides in at the right edge from frame 1. Label "Ilustrasi data".
2. **C1 SESUDAH (5.9–11.1)**: the robot drags the divider; side-by-side moment; snap. **Brand moment**: robot bottom-left, chest "M" hologram (MasterPajak AI panel, x 540–960, y ≈1384–1496, on screen ≈4.25 s; the pointing hand stays clear of it). Flow cards in 3D: 1 Catatan jualan → 2 Pembukuan (rapi, bisa ditelusuri) → 3 Laporan (laba rugi siap dibaca). They light up on cue and the robot points at each. Headline "Dari catatan jualan / sampai laporan, / satu alur." Label "Simulasi alur".
3. **C2 (11.1–16.1)**: SEBELUM is a notebook page in perspective (Omzet 48 jt − modal ? − ongkir ? − iklan ??, Untung ≈ ~~5 jt?~~ ~~8 jt?~~ (3 jt??)), with strike-throughs and a scribbled circle drawn live, a pencil, and floating "?" in depth. The robot scratches its head, then drags L→R. SESUDAH is a 3D "Laporan Laba Rugi" card at the same spot (Penjualan Rp48.250.000, Biaya produk −Rp21.400.000, Ongkir & biaya platform −Rp9.870.000, Iklan −Rp6.120.000, Laba Rp10.860.000; the arithmetic is consistent). Stabilo on Laba and "jelas". Labels "Ilustrasi data · Simulasi alur".
4. **C3 (16.1–22.1)**: SEBELUM is a 3D calculator flickering "Rp ???" / "Err" with three sticky notes (pajaknya berapa? / hitungnya gimana? / pakai data yang mana?). The robot shrugs, then drags R→L. SESUDAH is an "Estimasi pajak · dari data usahamu" card counting up to Rp1.215.000 (no rate, labelled "Ilustrasi data · Simulasi alur"), plus a "Tim ahli Muamalah Pajak · sesuai layanan" card with a "kalau perlu" tab.
5. **END (22.1–32.0)**: series end card, the same as Video 1: beam + iris, "Jualan jalan terus, / pajaknya AI yang urus.", CTA pill "Coba kalkulator gratis", "Link di bio". The robot rises bottom-right, the logo hologram is left (on screen ≈8.9 s), it waves, points at the CTA and waves again.

## Files
- `index.html`: composition. All beats are in `window.TM`. The slider rig is `window.RIG` (head). Headline lines are auto-fitted to their column in `buildReady["rig"]`, and the knob path is built there too.
- `robot_perf.js`: choreography. Adds `window.ROBOT_POS` (filtered x/y/h, used by the rig). Hand offset measured from renders: ≈0.50·h beside the body at shoulder height for pose `arm(115, −20, 5)` with body yaw ∓20.
- `tools/sfx.py` → `assets/audio/sfx.wav` (32.0 s, 48 kHz mono). Typing ticks, slider grab / friction slide / snap, whips, markers, scribbles, pops, hologram fx, beam boom, chime.
- `thumbnail/cover.html` → `thumbnail/COVER_MP10_SEBELUM_SESUDAH.png`: split SEBELUM | SESUDAH frame with the "VS" divider; the robot holds the knob. Everything important is inside the 4:5 crop.

## QA done
- Snapshots at every scene, every transition midpoint (tease, pull-back, drag, side-by-side, snap, whips, beam, iris) and the end card.
- Flat-layout text audit (transforms neutralised): every text node sits inside its card or pill and no text runs under another element. Found and fixed: "Tim ahli Muamalah Pajak" ran under the "kalau perlu" chip, and the estimasi value touched its mini bars.
- Headline lines are fitted to their column (850 px on the SEBELUM side, so they never reach the divider).
- All "from" states are applied up front, so a cold seek to any frame is correct.
- No console errors (only the expected 404 for `lipsync.js`).
- Frame-edge text check over 0–32 s in 0.1 s steps: the only hits are mid-whip frames (content leaving the frame by design). Also the close-up at 0–2.2 s, where the second file is a heavy depth-of-field blur (11 px, unreadable) partly behind the SESUDAH sliver. Decorative "?" glyphs were moved inside the frame for every camera position.
- The end card keeps Video 1's choreography. Its wave/point arm (`armL`) sits mostly off-frame on the right; a visible `armR` gesture was tested but its hand lands on the logo hologram, so the series pattern was kept.

## Not done / notes for the lead
- No dashboard screen recording exists, so all UI is a generic simulation labelled "Simulasi alur". Swap it in if a recording arrives.
- `lipsync.js` is not generated yet (VO not recorded). The robot mouth is driven once the ElevenLabs VO exists (`tools/lipsync.py`).
- No full render was made (per brief).
