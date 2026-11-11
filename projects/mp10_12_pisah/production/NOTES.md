# Video 12 · Uang Pribadi vs Uang Usaha — production notes

1080×1920, 34.8 s (`TM.total` = `data-duration`). Title: "MasterPajak AI · Video 12 — Uang Pribadi vs Uang Usaha".
Served for QA at `http://127.0.0.1:8812/index.html`. Not rendered and not committed here (the lead renders and commits).
Tech skeleton as Video 1: one `index.html`, paused GSAP `tl` in `window.__timelines["main"]`, `F/show/hide` (+ the `XS()` scale helper from
Video 3), backward-seek patch, `ROBOT_APPLY` onUpdate line, end marker, `robot_perf.js` (same engine, new choreography), `lipsync.js` with `onerror`.

## Concept
One hero object: a **glass coin jar** ("UANG JUALAN") in a paper studio, built in real CSS 3D (20-strip glass cylinder with Fresnel
edges and highlights, ribbed navy lid with a coin slot, gold fill that rises/falls, a hanging paper tag that rolls the balance).
Camera rig `.stage > .cam (anchor, dolly, tilt) > .yaw (orbit) > .pan (−focus)`, floor grid in perspective, contact shadows, far bokeh,
backdrop-filter depth of field, SVG motion blur on whip pans.

1. **Uang jualan masuk…** — three "Jualan masuk +Rp…" chips drop in; each shrinks into two coins that fall edge-first through the slot.
   The tag rolls Rp0 → Rp1.250.000 → Rp2.480.000 → Rp3.600.000, the fill rises, an **UNTUNG** gauge (off to the left) climbs.
2. **eh, kepake buat jajan, bayar cicilan, kirim ke keluarga** — an expense tile pops on each phrase (cup / calendar / house-with-heart icons,
   no brands); two coins leap out of the slot to each tile; the tag rolls down to Rp1.250.000, the fill drops. Caption swaps word by word.
3. **Pas dicek, untungnya ke mana?** — whip pan to the UNTUNG gauge: the needle hunts, collapses to the bottom, the arc empties, a yellow
   **"?"** badge pops. The robot shrugs.
4. **uang pribadi + usaha campur** — whip back: the lid blows off, yellow *usaha* coins erupt, grey *pribadi* coins rush in, and both swirl
   into one tornado around the jar (comet-tail wind rings, camera orbits). Legend chips "uang usaha / uang pribadi". The tag rolls to
   "Rp?.???.???". Robot gets dizzy X-eyes on "campur".
5. **angka usahamu jadi nggak kebaca** — a "Catatan usaha" card swings down in front of the (blurred) swirl; Pemasukan / Pengeluaran /
   Untung digits scramble and smear until they read "Rp?.???.???" / "???". Robot squints and scratches its head.
6. **Pisahin dulu catatannya** — the robot walks to centre and karate-chops: a light blade cuts the frame, the jar splits in two halves that
   slide apart, the coins sort themselves: yellow to the left, grey to the right. The camera cranes up onto **two lanes** with a glowing
   divider (chevrons flow into depth). Signs flip down: **PEMASUKAN usaha** (lane1) and **PENGELUARAN pribadi** (lane2); the income chips
   ride the left lane, the expense tiles the right lane. The robot referees, one arm per lane.
7. **Brand** — series band sweep → robot half-body + chest hologram. A **"Pembukuan usaha"** ledger (subtitle "Bulan ini · uang pribadi
   dipisah", chip SIMULASI ALUR, footer ILUSTRASI DATA) swings up; yellow usaha coins (+ one receipt for "Biaya kemasan") fly in and become
   rows. On "bisa ditelusuri": row 1 gets the stabilo, its link icon pulses and a yellow trace line runs to the source card
   "SUMBER · MINGGU 1 / Rekap pesanan / 38 pesanan · Rp1.250.000".
8. **End card** — series template unchanged (beam + iris, tagline two lines, CTA "Coba kalkulator gratis", "Link di bio", robot waves,
   points at the CTA, logo hologram left). Beam/disc origin mirrored bottom-right as in Video 5 (brand robot stands bottom-left).

## TM keys ↔ VO (`VO_SCRIPTS.md` § 12, ≈ 2.4 words/s + pauses; re-time by editing `window.TM` only — tweens, robot and SFX all read it)
| key | t (s) | VO phrase | picture |
|---|---|---|---|
| `masuk` | 0.35 | Uang jualan masuk... | chips → coins through the slot, tag rolls up, gauge climbs |
| `eh` | 2.30 | eh, kepake buat jajan, | surprised robot; "jajan," tile + coins out at `eh + 0.8` |
| `cicil` | 4.20 | bayar cicilan, | "Bayar cicilan" tile + coins out |
| `kirim` | 5.25 | kirim ke keluarga. | "Kirim ke keluarga" tile + coins out (tag Rp1.250.000) |
| `cek` | 7.05 | Pas dicek, | whip to the gauge (`cek − 0.35`), needle hunts |
| `mana` | 8.15 | untungnya ke mana? | needle collapses, "?" badge, shrug |
| `campur` | 9.90 | Kalau uang pribadi dan uang usaha campur, | whip back, lid off, coin tornado, legend, "campur." at +2.2 |
| `kebaca` | 13.05 | angka usahamu jadi nggak kebaca. | scrambling "Catatan usaha" card |
| `pisah` | 15.60 | Pisahin dulu catatannya: | chop + blade at `pisah + 0.4`, jar splits, camera onto the lanes |
| `lane1` | 17.25 | mana pemasukan usaha, | sign PEMASUKAN usaha, income chips on the left lane |
| `lane2` | 18.80 | mana pengeluaran pribadi. | sign PENGELUARAN pribadi, expense tiles on the right lane |
| `sol` | 20.70 | MasterPajak AI bantu menata catatan usahamu | bands (`sol − 0.48`), robot + hologram, ledger rows fill |
| `telusur` | 23.80 | jadi pembukuan yang bisa ditelusuri. | headline, row stabilo, trace line → source card |
| `end` | 26.10 | Jualan jalan terus, pajaknya AI yang urus. | beam + iris → end card |
| `cta` | 29.65 | Coba kalkulator pajak gratisnya. | CTA pill, robot points |
| `bio` | 31.90 | Link di bio. | "Link di bio", robot waves |
| `total` | 34.80 | — | `data-duration` = 34.8 |

## Robot / hologram
- Light scenes: small full-body host bottom-left (x 168, h 500) — cheers, surprised hands, follows the coins, shrug, dizzy X-eyes,
  head-scratch; walks to centre before the chop (no cut), referees the lanes, ducks out before the bands. Never over text (checked).
- Brand: half-body bottom-left, chest hologram `hx 720 / hy 1520 / hw 420` from `sol + 0.72` to `end − 0.3` (≈ 4.4 s).
  End card: `hx 360 / hy 1500 / hw 420` from `end + 0.75` to the end (≈ 7.9 s). Both inside the 120 px side margins.
- `CUTS` = [`sol − 0.05`, `end − 0.01`]. LIGHT lighting on paper scenes, NAVY on navy scenes. Arms: `aR` = screen-left arm, `aL` = screen-right.

## Brand / claims checklist
- Spelling MasterPajak AI; tagline + CTA + "Link di bio" exactly as the series end card.
- Every amount carries "Ilustrasi data": the jar tag (own pill), screen chip ILUSTRASI DATA bottom-right through all light scenes (chips,
  tiles, lanes), the "Catatan usaha" card, the ledger footer; the ledger UI also carries SIMULASI ALUR. Cover has no numbers.
- No tax rates, deadlines, penalties or guarantees. The ledger dates (03/11 …) are transaction dates. Feature named: "pembukuan yang bisa
  ditelusuri" (+ kalkulator gratis in the CTA). No DJP / government marks. Expense icons are generic (cup, calendar, house + heart);
  no bank, e-wallet, lender or marketplace names or logos.

## Files
- `index.html` (composition), `robot_perf.js` (choreography).
- `tools/sfx.py` → `assets/audio/sfx.wav` (48 kHz mono, 34.8 s, synthesised: coin clinks with inharmonic partials, slot drops, tag ticks,
  needle ratchet, "?" pop, whip whooshes, cork pop, tornado wind with scattered jingles, scramble blips, blade zing + impact, sign pops,
  series band whooshes, hologram fx, docking pops, stabilo/trace marker, beam boom, CTA pops, chime). Cues read from `window.TM`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP12_PISAH_UANG.png` (navy; "Uang pribadi / vs uang usaha / jangan dicampur." + pill
  "Pisahin dulu catatannya →"; the jar split by the light blade — usaha coins left, pribadi coins right — and the robot mid-chop; all key
  content inside the 4:5 crop y 285–1635). The jar is one inline SVG (an HTML/clip version rasterised with black holes in software GL).

## QA done
- Final QA with the real runtime: `npx hyperframes@0.8.186 snapshot . --at … --no-end` at every scene, every transition midpoint (whips,
  blade, bands, beam, iris) and the end card — 34 frames (contact sheets in the scratchpad, see the report).
- `hyperframes validate .`: only the expected `lipsync.js` 404s. `hyperframes check .` timed out on its own 120 s sample deadline
  (shared CPU), lint clean apart from the file-size note.
- `edgecheck.cjs` 0–34.8 s: no text crosses the frame edges except the motion-blurred whip pans (6.9 s, 9.8 s) and the series marquee.
- Containment check (layout-based): every text run sits inside its card/tile/tag/sign/ledger; the tag value and the ledger date column
  were tightened to fit with margin.
- Found only in the real runtime and fixed: cards that shared one 3D sorting context with the jar's cylinder strips lost polygon pieces
  (HyperFrames' software compositor drops pieces split against the strips). The world is now two stacked 3D contexts driven by the same
  camera tweens: **A** = floor, jar, gauge, lane floors/divider; **B** = tag, chips, tiles, all coins, wind rings, lane cards.
  Coins dropping "into" the slot now fade at the slot instead of passing behind the lid.
- No build-time state leaks: no `tl.seek()` during build; every initial state is pinned on the timeline at 0 (`pin()`); scale tweens go
  through `XS()` (scaleX/scaleY). The only buildReady step (`fit`) does not touch `robot_perf.js`.

## Not done / open
- Full render not run (lead). VO not recorded: re-time `TM` to the ElevenLabs VO, then generate `lipsync.js` with `tools/lipsync.py`.
- The world uses many 3D planes plus per-frame backdrop-filter DOF; frames render slower than Video 1.
- Coins orbiting behind the jar draw over the glass (context B sits above context A). It reads fine because the glass is transparent and the
  fill is empty during the swirl, but it is a deliberate trade-off for the compositor bug above.
