# Video 11 · Mitos vs Fakta Pembukuan — production notes

1080×1920, 35.0 s (`TM.total` = `data-duration`). Title: "MasterPajak AI · Video 11 — Mitos vs Fakta Pembukuan".
The tech skeleton is the same as Video 1: one `index.html`, a paused GSAP `tl` in `window.__timelines["main"]`, `F/show/hide`, the backward-seek patch,
the `ROBOT_APPLY` onUpdate line and the end marker. It uses `robot_perf.js` (same engine, new choreography), and `lipsync.js` is loaded with `onerror`.

## Concept
Three myth cards in one 3D paper room (back wall + perspective floor grid, contact shadows, out-of-focus receipts near the lens, a lens
depth-of-field band). Each card is a real 3D board (780×1000, 16 px thick, cream paper front / navy back, visible edges). Camera rig:
`.stage` (perspective 1400) › `.cam` (dolly + orbit) › `.pan` (world focus); whip pans with directional motion blur between the cards.

1. **Hook** — the three cards stand stacked, then fan out like a hand ("tiga"). Each card shows a faint "?" in its window. Caption "3 mitos / pembukuan (stabilo) / yang sering dipercaya seller.".
   The robot judge pops up bottom-right and points. The camera swings in while cards 2 and 3 are dealt out to their stations.
2. **Myth 1** — a top bar appears: "MITOS vs FAKTA · 1 2 3". A red rubber stamp **MITOS** (ink texture, crooked) slams onto card #1
   ("“Pembukuan cuma buat usaha gede.”"). In the card window a giant tower rises with a "PEMBUKUAN" sign on its roof; a tiny shop pops up at its foot with a "?" (the scale gag).
   The robot shows x-eyes and shakes its head. **Flip** (hop + turn) → navy **FAKTA** side: "Toko kecil juga perlu tahu *untungnya berapa.*" (stabilo).
   The scale is now reversed: the shop "TOKO KECIL" is the hero, the tower is small in the back, and a card "UNTUNG BULAN INI Rp3.250.000" shows bars and a check (Ilustrasi data).
3. **Myth 2** — whip → card #2 "“Catat omzet aja udah cukup.”". A receipt "CATATAN BULAN INI": the omzet column types in, the BIAYA column stays empty
   (dashed boxes blink), and LABA gets a red "?". The robot tilts its head and shrugs. **Flip** (1.5-turn spin) → FAKTA: "Tanpa *catat biaya,* kamu nggak tahu labanya."
   The biaya column types in (−420.000 … −365.000), then LABA = **Rp3.250.000** (stabilo). The numbers add up: 5.225.000 − 1.975.000.
4. **Myth 3** — whip → card #3 "“Nanti aja, akhir tahun sekalian.”". Twelve month folders (JAN…DES) pile into a leaning tower, wobble and crash into a heap.
   The robot flinches with x-eyes and hands up. **Flip** → FAKTA: "Dicicil tiap bulan *jauh lebih ringan.*" Twelve small monthly steps (J F M … D) rise one by one,
   with a check on each and a yellow line climbing them ("SEDIKIT-SEDIKIT, TIAP BULAN").
5. **Brand** — the series band sweep with the marquee → navy. The robot rises half-body bottom-left with the chest hologram "MasterPajak AI".
   The three FAKTA cards fly in from three directions and stack into one deck, which squares up. The top card flips into a white card:
   **Pembukuan** (03/11 Pesanan #1041 +Rp186.500 · Ongkir −Rp24.000 · Iklan −Rp50.000, each ✓) + **LAPORAN LABA RUGI** (Penjualan / Biaya / **Laba Rp3.250.000**, stabilo).
   Chip "SIMULASI ALUR", footer "ILUSTRASI DATA". Whisper "bantu menata catatan jualanmu".
6. **End card** — the series template, unchanged: beam + iris, "Jualan jalan terus, / pajaknya **AI** yang urus.", CTA pill "Coba kalkulator gratis", "Link di bio".
   The robot waves, shows the logo hologram on the left, points at the CTA and waves again.

## TM keys ↔ VO (`VO_SCRIPTS.md` § 11, pace ≈ 2.4 words/s + short pauses — re-time to the real VO by editing `window.TM` only)
| key | t (s) | VO line |
|---|---|---|
| `hook` | 0.25 | Tiga mitos pembukuan yang sering dipercaya seller. |
| `m1` | 3.3 | Mitos satu: pembukuan cuma buat usaha gede. |
| `f1` | 6.5 | Faktanya, toko kecil juga perlu tahu untungnya berapa. |
| `m2` | 9.9 | Mitos dua: catat omzet aja udah cukup. |
| `f2` | 12.9 | Faktanya, tanpa catat biaya, kamu nggak tahu labanya. |
| `m3` | 16.3 | Mitos tiga: nanti aja, akhir tahun sekalian. |
| `f3` | 19.4 | Faktanya, dicicil tiap bulan jauh lebih ringan. |
| `sol` | 22.5 | MasterPajak AI bantu menata catatan jualanmu jadi pembukuan dan laporan laba rugi. |
| `end` | 27.9 | Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 31.1 | Coba kalkulator pajak gratisnya. |
| `bio` | 33.0 | Link di bio. |
| `total` | 35.0 | (end) |

Every beat is an offset from these keys:
- the stamp lands at `m` + 0.58;
- each flip starts at `f` − 0.36 and lands at about `f` + 0.45;
- the whip to the next card starts at `m` − 0.32.

The animations, the robot and `tools/sfx.py` all read TM, so a re-time moves everything together. Re-run `python3 tools/sfx.py` after any change.

## Robot / hologram
- **Hook and myths:** host from `hook` + 0.35 s, head and shoulders bottom-right (`x` 872, `y` 1840, `h` 760, paper lighting). It stays clear of every card and text block.
  - Myth 1: x-eyes and a head shake.
  - Myth 2: head tilt and shrug.
  - Myth 3: x-eyes and hands up at the crash.
  - On each flip: eyes follow the card, then it is happy and points at the FAKTA side.
  - It leans into the swing and the whips, and ducks before the bands.
- **Brand:** half-body bottom-left. The chest hologram is on screen from `sol` + 0.72 to `end` − 0.38 (≈ 4.3 s; `hx` 720, `hy` 1520, `hw` 420, the same as the series).
- **End card:** hologram from `end` + 0.75 to the end (≈ 6.3 s, `hx` 360). Both hologram positions are inside x 60–1020 and y ≤ 1600.
- `CUTS` = [`sol` − 0.05, `end` − 0.01].

## Brand / claims
- No DJP / government marks, no marketplace or bank brands. No tax rates, deadlines, penalties or guarantees.
- Features named: pembukuan, laporan laba rugi. The CTA names the kalkulator gratis.
- Demo numbers carry "ILUSTRASI DATA":
  - on the profit card and the FAKTA receipt;
  - as a screen chip from `f1` + 0.4 until the bands;
  - on the brand report card, which also carries "SIMULASI ALUR".
- The red of the MITOS stamp (#C8442F) is the one colour outside the base palette, as the batch-2 brief asks ("red-ish stamp").
- The spelling is MasterPajak AI. Tagline and CTA are exactly as briefed.

## Renderer notes (important for anyone editing this file)
- The final renderer (chrome-headless-shell 152, BeginFrame, SwiftShader) did NOT depth-sort nested 3D layers. I first built pop-up dioramas inside the card faces
  (preserve-3d faces with translateZ children). In the real `hyperframes snapshot`, the back cards' text came through the front card, and diorama pieces were drawn in the wrong order.
  It looked fine in the Playwright quick tool. The fix: **card faces are flat planes** (only the card rig, `.flp`, is preserve-3d), as in Video 4's flip card.
  The tower's side and roof are 2D oblique faces.
- Planes must not touch or intersect. The cards stand 4 px above the floor, the contact shadows lie 1 px above the floor, and the floor ends 15 px short of the wall.
  Before this, a whip frame showed the wall drawn over a card.
- All initial states are pinned on the timeline at 0, including the inline-hidden layers `#ilu`, `#bands`, `#beamwrap` and `#tbar`. Without this, `#ilu` showed at 0 s in the real runtime (autoAlpha revert).
  Frame 0 is primed with one forced `tl.render(0)` at build. Scale tweens use `scaleX/scaleY` (`XS()`).

## Files
- `index.html`, `robot_perf.js`
- `tools/sfx.py` → `assets/audio/sfx.wav` (48 kHz mono, 35.0 s, synthesised). Sounds:
  - hook and myths: card flicks for the fan and the deal, rubber-stamp thumps, the tower rise rumble, pops, "?" boings, typed-number ticks, folder drops, the pile crash (rumble, boom, paper flicks);
  - flips: flip whooshes with landing knocks;
  - stabilo strokes, monthly-step pops, small chimes;
  - brand and end: the bands, hologram fx, the deck fly-ins, the report flip, the row pops, beam/iris, CTA pops, the end chime.
- `thumbnail/cover.html` → `thumbnail/COVER_MP11_MITOS_FAKTA.png`. It is a light paper room with the two faces of a myth card in 3D:
  - the paper card has the red MITOS stamp, "“Pembukuan cuma buat usaha gede.”" and the tower + tiny shop;
  - the navy FAKTA card has "Toko kecil juga perlu tahu untungnya." and the profit card with ILUSTRASI DATA.
  - The headline is the stamp "MITOS" vs "FAKTA" (stabilo), "3 mitos pembukuan seller", and a pill "Cek 3 faktanya →".
  - The live robot judge waves. Everything sits inside the 4:5 crop (y 285–1635).

## QA done
- Real runtime (`npx hyperframes@0.8.186 snapshot --no-end`): every scene, every transition midpoint (swing, 2 whips, 3 flips, bands, deck flip, beam, iris) and the end card.
  Contact sheets are in the scratchpad (`m11/QA_A/contact-sheet-1.jpg`, `-2.jpg`, `m11/QA_B/contact-sheet-1.jpg`, `-2.jpg`).
- `hyperframes validate`: the only errors are the expected `lipsync.js` 404s. The contrast warnings come from the hidden back faces of the 3D cards and the deliberately muted inactive chip.
- Text-in-box check with transforms neutralised: all 131 text runs sit inside their card, window, chip, sign or row. The fitted quotes and facts are within their height budget (2 and 2–3 lines).
- Frame-edge check over 0–35 s: the only hits are mid-whip or mid-fly-in frames, hidden back faces, and the series marquee band. No held text is cut by the frame.

## Not done / open
- No VO yet. TM is estimated from the word count (77 words in about 32 s of speech). After the ElevenLabs VO, re-time `TM`, generate `lipsync.js` with `tools/lipsync.py`, and re-run `tools/sfx.py`.
- The tightest beats depend on the real VO pace. If "Mitos satu…" or "Mitos tiga…" runs long, push `f1` / `f3`: the myth-3 crash must finish before the flip, so keep `f3` − `m3` ≥ 3.0 s.
- I did not run the full render and did not commit (per the brief).
