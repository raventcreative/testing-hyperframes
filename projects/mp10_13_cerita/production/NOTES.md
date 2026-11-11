# Video 13 · Laris Tapi Saldo Tipis — production notes

1080×1920, 34.6 s (`TM.total` = `data-duration`). Title: "MasterPajak AI · Video 13 — Laris Tapi Saldo Tipis".
The tech skeleton is the same as Video 1: one `index.html`, a paused GSAP `tl` registered in `window.__timelines["main"]`, the `F/show/hide` helpers, the backward-seek patch, the `ROBOT_APPLY` onUpdate line, the end marker, `robot_perf.js` (same engine with new choreography) and `lipsync.js` loaded with `onerror`.
Every 3D world is real CSS 3D: `.stage` (perspective) › `.cam` (dolly z + orbit) › `.pan` (world point on the lens axis), as in Video 9. There is one font-metrics build step, `buildReady["fit"]`. It shrinks any `[data-fit]` text to its box and collapses the width of the odometer's vanishing leading digit.

## Concept
A short story about a fictional seller, **Rina**. She is a stylised paper cut-out (flat avatar in a hijab, with a white die-cut edge and no realistic features). A permanent chip, "ILUSTRASI CERITA", sits bottom-left from 0.15 s until the brand bands. The robot host narrates the story.

1. **Shop diorama** (`rina`, `laris`): Rina's shop is a layered 3D paper diorama: shelves wall (DOF blur), Rina, a striped awning with the sign "Toko Rina", and a 3D counter. "Ini Rina." brings in a paper name tag ("Rina · penjual online"). The robot rises bottom-right and presents her with an open palm. On "laris", ten 3D parcel cubes pop onto the counter, and eight "Pesanan baru +Rp…" bubbles burst out of her phone in depth. A floating card "PESANAN HARI INI" rolls an odometer from 18 to 96 (labelled ILUSTRASI DATA).
2. **Balance slab** (`tipis`, `sal`): a whip-pan with motion blur lands on her balance card, "Saldo rekening toko · AKHIR BULAN". The card sits on top of a thick 3D stack of 18 yellow layers. The number rolls down from Rp18.450.000 to **Rp2.380.000**. As it rolls, the layers peel away until the slab is thin, a dashed "ghost" outline shows the lost thickness, and the bar against "Penjualan bulan ini" shrinks. Captions: "Tapi tiap akhir bulan, / saldonya kok / **tipis?**" (stabilo). The robot's mouth drops open, it tilts its head and shrugs, then it ducks.
3. **X-ray month** (`ternyata` … `potongan`): a vertical whip down to her month: a tilted board of 30 day tiles that show only sales ("YANG TERCATAT: PENJUALAN"). A glowing scan line sweeps left to right. Everything it passes shows an X-ray copy of the same world (same camera, revealed by clip-path), with glowing cost tokens on every day and the header "BIAYA YANG NGGAK KECATAT". The captions are duplicated, so the text is X-rayed too (navy turns white/yellow). The month then dims, and four 3D coins rise one per word: **Ongkir, Kemasan, Iklan, Potongan platform**. The matching tiny tokens pulse with each coin.
4. **Where the money went** (`rapi`, `pergi`): "the light comes back on". The scan line runs again and pulls the X-ray copy off, which reveals a light money-flow board. The four coins fly onto their cost cards. The source bar "Penjualan bulan ini Rp18.450.000" fills, and ribbons sized by amount flow into six cards: Modal barang · tercatat (grey), Ongkir, Kemasan, Iklan, Potongan platform (yellow), and **Sisa ke saldo Rp2.380.000** (navy, ringed). The thin ribbon ends in the thin balance. Captions: "Pas dirapikan, baru kelihatan / ke mana aja / **uangnya pergi.**"
5. **Brand** (`sol`, `lap`, `baca`): the series band sweep with the marquee. The robot rises half-body bottom-left with the chest hologram, and the whisper "dengan MasterPajak AI," appears. A "Laporan laba rugi · Toko Rina · bulan ini" card (SIMULASI ALUR, ILUSTRASI DATA) flies in from depth. Its rows build, and the four coins fly in from the sides and dock into the cost rows. "Laba Rp2.380.000" gets a stabilo stroke under the headline "Laporan laba rugi / **yang gampang dibaca.**" The robot points at the rows, then nods.
6. **End card**: the series template, unchanged. Beam and iris, "Jualan jalan terus, / pajaknya **AI** yang urus.", the CTA pill "Coba kalkulator gratis", and "Link di bio". The robot waves, shows the logo hologram on the left, points at the CTA and waves again.

## TM keys ↔ VO (`VO_SCRIPTS.md` § 13, ≈ 2.4 words/s plus pauses; re-time by editing `window.TM` only)
| key | t (s) | VO line |
|---|---|---|
| `rina` | 0.3 | Ini Rina. |
| `laris` | 1.4 | Jualannya laris, pesanan tiap hari penuh. |
| `tipis` | 4.5 | Tapi tiap akhir bulan, |
| `sal` | 6.4 | saldonya kok tipis? |
| `ternyata` | 8.1 | Ternyata biaya kecil-kecil nggak pernah kecatat: |
| `ongkir` | 11.3 | ongkir, |
| `kemasan` | 11.9 | kemasan, |
| `iklan` | 12.6 | iklan, |
| `potongan` | 13.1 | potongan platform. |
| `rapi` | 14.4 | Pas dirapikan, |
| `pergi` | 15.45 | baru kelihatan ke mana aja uangnya pergi. |
| `sol` | 18.9 | Dengan MasterPajak AI, |
| `lap` | 20.7 | catatan jualan dan biaya ditata |
| `baca` | 22.9 | jadi laporan laba rugi yang gampang dibaca. |
| `end` | 26.3 | Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 29.8 | Coba kalkulator pajak gratisnya. |
| `bio` | 31.8 | Link di bio. |
| `total` | 34.6 | (end) |

Every animation, the robot choreography and `tools/sfx.py` read these keys, so a re-time moves everything together. The balance roll starts at `sal − 0.55`, so it lands as "tipis?" is spoken.

## Robot / hologram
- The robot hosts from `rina` (rises 0.4–1.1 s) to `ternyata − 0.2`, bottom-right, below all text. It is hidden during the X-ray month and the flow board (those scenes use the full frame), then returns for the brand scene and the end card.
- Chest hologram on screen at the brand moment from about 19.6 to 25.9 s (≈ 6.3 s; `hx` 720 / `hy` 1520 / `hw` 420, as in Videos 1 and 9). On the end card from about 27.0 s to the end (≈ 7.5 s; `hx` 360). Both stay inside the 120 px side margins.
- `CUTS` = [`sol` − 0.05, `end` − 0.01]. The paper scenes use default lighting and the navy scenes use `NAVY`.

## Brand / claims
- Rina, "Toko Rina" and every amount are fictional. The "ILUSTRASI CERITA" chip runs through the whole story part, and every card with numbers carries "ILUSTRASI DATA". The report carries "SIMULASI ALUR".
- No marketplace, bank or government branding. Generic UI text only: "Pesanan baru", "Saldo rekening toko", "potongan platform".
- No rates, deadlines, penalties or guarantees. Features named: pembukuan / laporan laba rugi (from catatan jualan + biaya) and kalkulator gratis (CTA).
- Numbers are consistent across scenes: Penjualan 18.450.000 − modal barang 9.200.000 − ongkir 1.860.000 − kemasan 740.000 − iklan 2.350.000 − potongan platform 1.920.000 = 2.380.000 (the thin balance = "Laba" in the report).

## Files
- `index.html`, `robot_perf.js`
- `tools/sfx.py` → `assets/audio/sfx.wav` (48 kHz mono, 34.6 s, all synthesised): paper pops, parcel thuds, generic order pings, odometer ticks, whips, a deflating roll-down, marker strokes, scanner hum with token sparkles, four coin rings, a "light on" switch, ribbon swishes, card pops, ring ping, bands, hologram fx, row pops and coin docks, beam/iris, CTA pops, chime.
- `thumbnail/cover.html` → `thumbnail/COVER_MP13_LARIS_SALDO_TIPIS.png`: navy; Rina at her counter with parcels, the thin "Saldo akhir bulan Rp2.380.000" card with its dashed ghost, four cost coins with "ongkir · kemasan · iklan · potongan", the headline "Laris, / tapi saldonya / **TIPIS?**", the pill "Ini biang keroknya →", "ILUSTRASI CERITA", and the robot shrugging. Everything sits inside the 4:5 crop.

## QA done
- Final check in the real runtime: `npx hyperframes@0.8.186 snapshot` at every scene, every transition midpoint (whip 4.25 s, vertical whip 7.94 s, scan 10.2 s, wipe 14.5 s, bands 18.65 s, beam 26.1 s, iris 26.45 s), the first frame and the end card. Contact sheets: scratchpad `m13/final/`.
- The real runtime caught one bug that `snap.cjs` did not. Overlays hidden only by `visibility` (scan line, bands, beam, chip) came back visible after the renderer's back-seeks, because `autoAlpha` records opacity 1 as its start value. Fix: every initial state is pinned on the timeline at 0 (the `pin()` helper), with `autoAlpha: 0` for these overlays.
- `hyperframes validate`: the only errors are the expected `lipsync.js` 404s. The contrast warnings come from the series' muted label style (ILUSTRASI DATA and similar).
- Frame-edge check (`edgecheck.cjs`, 0–34.5 s, step 0.25): no sharp text is cut by the frame. The only hits are the band marquee, layers during the two whips, and odometer digit strips that their masks hide (false positives). The X-ray board was re-framed (scale 0.88, gentler push) so its footer stays inside x ≤ 1000.
- Text-in-card check (transforms neutralised): every text run sits inside its card. The only hits are the report rows' amounts, which sit flush right in their layout row, 44 px inside the card.

## Not done / open
- No VO yet. TM is estimated from the word count. After the ElevenLabs VO, re-time `TM` and generate `lipsync.js` with `tools/lipsync.py`.
- Full render not run (the lead renders). Heavy frames are the whips (SVG motion blur) and the blurred X-ray month during the coins.
- Creative choices to confirm with the client:
  - Rina is drawn wearing a hijab. The SVG colours and shapes are easy to change.
  - The money flow and the report include a "Modal barang · tercatat" line that the VO does not mention. It is there so the illustrative numbers add up honestly.
  - The ending balance equals "Laba" in the report, as a simplification for the story.
- The tile amounts on the month board are small on screen (≈ 18–20 px). They are texture; the key messages are in the captions and coins.
