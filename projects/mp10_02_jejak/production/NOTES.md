# Video 2 · Jejak 1 Transaksi — production notes

Format 1080×1920, 35.6 s (`TM.total` = `data-duration`). Tech skeleton = Video 1 (GSAP timeline `tl`, `F`/`show`/`hide`,
backward-seek patch, `ROBOT_APPLY` onUpdate, end marker). No full render, no commit (lead).

## Concept
One order card (**Rp100.000 · Ilustrasi data**) travels a real 3D road on a paper floor (CSS 3D camera rig:
`.foc` anchor/z-dolly/pitch/roll → `.yaw` heading → `.pan` focus → floor). Tollgates bite the amount (biaya layanan, ongkir,
retur "kadang"): the gate light flashes, the card jolts, a yellow chip with the deduction flies out and lands flat beside the road,
and a rolling-digit odometer ticks the amount down (100.000 → 93.500 → 84.500 → 74.500). Then PENCAIRAN TOKO (card becomes
"SALDO TOKO") and REKENING BANK (card becomes "MASUK REKENING", check badge). The camera cranes up to show the whole route
("sepanjang ini"), the card multiplies, tangled routes draw across the floor and a swarm of small cards rides them
("gimana yang ribuan?", counter 1 → 2.847, Ilustrasi data). Series band sweep → navy brand world: the robot rises with the chest
hologram, the tangles straighten into trace lines (orders → rows), a ledger "Pembukuan · bisa ditelusuri" forms, the camera pulls
back to show Pesanan → Pembukuan → Laporan with pulses along the traces, then pushes into the ledger: rows get a check (cocok) or a
yellow flag ("perlu dicek"). Series beam + iris end card.

## TM keys ↔ VO lines (VO pace planned at ~2.4 words/s)
| key | time | VO |
|---|---|---|
| l1 | 0.3 | Satu pesanan ini... |
| q1 | 1.8 | ...uangnya lari ke mana aja? |
| l2 | 3.5 | Pesanan seratus ribu. |
| fee | 5.1 | Kepotong biaya layanan, (bite 1 at fee+0.7) |
| ong | 6.4 | ongkir, (bite 2 at ong+0.29) |
| ret | 7.1 | kadang retur. (bite 3 at ret+0.44) |
| l3 | 8.3 | Masuk ke pencairan toko. (arrival l3+0.55) |
| bank | 10.1 | Baru nyampe ke rekening bank. (arrival bank+0.8) |
| l4 | 12.4 | Kalau satu transaksi aja jalannya sepanjang ini, (crane-up) |
| l4b | 13.9 | ...jalannya sepanjang ini (caption line 2) |
| ribu | 15.4 | gimana yang ribuan? |
| l5 | 17.0 | MasterPajak AI bantu menata jejak itu (brand + hologram) |
| l5b | 19.6 | jadi pembukuan yang bisa ditelusuri, |
| l5c | 21.7 | dari pesanan sampai laporan. |
| l6 | 23.6 | Jadi kamu tahu angka mana yang cocok, |
| l6b | 26.5 | dan mana yang perlu dicek. |
| l7 | 28.7 | Jualan jalan terus, pajaknya AI yang urus. (end card) |
| cta | 31.9 | Coba kalkulator pajak gratisnya. |
| bio | 33.7 | Link di bio. |
| total | 35.6 | |

All beats (camera segments, bites, robot choreography, SFX) are derived from these keys, so re-timing to the real VO = editing
`window.TM` only, then `python3 tools/sfx.py .`.

## Scenes
1. 0–3.5 Hook (light): close-up on the order card standing on the paper floor, camera orbits; "Satu pesanan ini… / uangnya lari /
   ke mana aja?" on the sky; pull back + rise reveals the road and gates. Robot bottom-right presents the card, shrugs.
2. 3.5–12.3 Journey (light): stabilo on Rp100.000; 5 road segments with camera tracking (yaw follows the heading, lag, roll), three
   bites, pencairan, bank. Depth of field (backdrop blur bands), fog at the horizon. Robot rides along in the corner, flinches.
3. 12.4–17.0 Overview + swarm (light): crane-up (pitch 62°→36°, dolly out), all gates back, caption "1 transaksi aja, / jalannya
   sepanjang ini." → "gimana yang ribuan?" with odometer 1 → 2.847; clones burst, 26 tangled routes, 130 riding cards
   (offset-path), static field of ~1500. Robot: arms up, X eyes.
4. 16.55–17.0 Series band sweep with "MasterPajak AI" marquee.
5. 17.0–23.4 Brand (navy, 3D plane): robot half-body bottom-left, chest hologram reveal (on 17.7 → 23.05, ≈5.4 s, x 510–930,
   y ≈1465–1575). Tangles straighten, ledger forms, stabilo "bisa ditelusuri", pull back to Pesanan → Pembukuan → Laporan.
6. 23.4–28.3 Checks (navy): push into the ledger, scan bar, ✓ on 3 rows + legend "cocok", yellow flags on 2 rows + pills
   "perlu dicek" + legend. Robot moves bottom-right and points.
7. 28.2–35.6 Series end: beam + iris, tagline in two lines, CTA pill "Coba kalkulator gratis", "Link di bio"; robot waves/points,
   logo hologram left (on ≈29.4 → 35.6).

## Brand-rule checklist
- Numbers on screen: card amount, bite chips, ledger rows, counter — "Ilustrasi data" on the card, a fixed chip during the journey,
  next to the counter, in the ledger footer. Ledger + report = product UI simulation → "SIMULASI ALUR" chips.
- No tax rates, deadlines, penalties, guarantees; no DJP / government / marketplace branding; generic icons only.
- Features named: pembukuan yang bisa ditelusuri, laporan laba rugi, kalkulator gratis (CTA). Tagline + CTA exact.

## Robot / hologram
- Robot visible in every section: hook host (bottom-right, presents the card, shrugs), rides along in the corner during the
  journey (flinches at bites, small celebration at the bank), overview (looks up, then arms up + X eyes on "ribuan"), ducks out
  under the bands (CUT at l5−0.05), brand half-body bottom-left, checks half-body bottom-right, end card (series choreography).
- Chest hologram (logo panel): brand 17.5 → 23.05 s (≈5.4 s, centre 720/1520, w 420 → x 510–930, y ≈1465–1575); end card
  29.2 → 35.6 s (≈6.2 s, centre 360/1500). Both inside the safe zone, never touching frame edges.
- Light journey scenes use default robot lighting; NAVY lighting (rim 2.0, shadow 0.5) on the brand/end scenes.

## Illustrative numbers (all labelled "Ilustrasi data")
Rp100.000 − Rp6.500 (biaya layanan) − Rp9.000 (ongkir) − Rp10.000 (retur, kadang) = Rp74.500 (pencairan → rekening bank).
Counter 1 → 2.847 transaksi. Ledger rows #0417–#0421 (two flagged "perlu dicek").

## QA done (snapshots, no full render)
- Contact sheets of every scene + transition midpoints (see the lead report for paths); text-edge check over 0–35.5 s.
- Edge check: no flat-scene hits. Remaining hits are 3D-camera motion (gate labels / bite chips / far report card entering or
  leaving the frame while the camera moves) and the odometer digit strips (hidden digits clipped by their columns — false positives).
- Text fits: the card amount auto-shrinks to its card, bite chips and captions are fitted in the build step (`buildReady["jejak"]`).

## Known issues / not done
- `lipsync.js` not present yet (VO not recorded) — loaded with `onerror`; the 404 in the console is expected.
- Beat times are planned at ~2.4 words/s; after the ElevenLabs VO exists, re-time `window.TM` (one key per VO line + sub-beats).
- Heavy page (CSS 3D floor 4000×7400 + backdrop-filter DOF + WebGL robot): expect slower render than Video 1.

## Files
- `index.html`, `robot_perf.js`, `tools/sfx.py` → `assets/audio/sfx.wav`, `thumbnail/cover.html` →
  `thumbnail/COVER_MP02_JEJAK_TRANSAKSI.png`.
- `lipsync.js` not present yet (VO not recorded) — loaded with `onerror`, the 404 in the console is expected.
