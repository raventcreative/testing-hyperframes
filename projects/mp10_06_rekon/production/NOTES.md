# Video 6 · Bulanan ≠ Tahunan — production notes

MasterPajak AI · 10-video series · 1080×1920 · 35.0 s · `index.html` (HyperFrames 0.8.186, same tech skeleton as Video 1).
Title: "MasterPajak AI · Video 6 — Bulanan vs Tahunan". Served for QA at `http://127.0.0.1:8806/index.html`.

## Concept
The monthly total and the annual recap of a seller don't match. Problem on paper (light), solution on navy (series look).

- **P · paper world (one 3D desk, one continuous camera).** Two lifted cards: BULANAN `Rp612,4 jt` vs TAHUNAN `Rp618,9 jt`;
  a yellow ≠ drops from above the camera and slams (shake). The monthly card bursts into 12 month tiles that fly at the camera,
  then are counted back into the card one by one (odometer). ≠ again + "SELISIH Rp6,5 jt". The camera dives into March's
  spreadsheet: row 7 is a copy of row 6 (lifts off, "dicatat 2×"), the rows part for a missing transaction (dashed slot,
  ghost row "12 Mar · Pencairan toko · 6.745.000", "kelewat"). Pull back: a magnifier (its glass is a 1.6× clone of the sheet)
  hunts row by row, a clock spins faster and faster, the light turns to late afternoon: "Bisa seharian."
  (The numbers are consistent: 612,4 = 618,9 − 6,745 + 0,245.)
- **T · band sweep** with the "MasterPajak AI" marquee (Video 1 pattern).
- **N · navy world.** Robot rises bottom-left with the chest hologram (brand moment, hologram on screen 17.9–23.3 s = 5.4 s).
  The 12 months fly in from the mess and snap into a grid under "Rekonsiliasi bulanan & tahunan"; a scan beam checks every
  month (✓) and flags MAR and AGU yellow; summary "Bulanan vs tahunan · 10 cocok · 2 perlu dicek". March opens into its
  reconciliation list: ✓ rows and two yellow "perlu dicek" rows ("muncul 2×", "belum tercatat"). On "mulai periksa dari mana"
  the checked rows step aside, the flagged rows rise to the top, the card shrinks, "↑ Mulai periksa dari sini", robot points.
- **End card** (series template, unchanged copy): beam + iris, "Jualan jalan terus, / pajaknya AI yang urus.",
  "Coba kalkulator gratis", "Link di bio", robot waves and points, logo hologram left (on screen 28.4–35.0 s).

Depth: CSS 3D camera rig per world (`.stage` perspective 1500 > `.shk` shake > `.cam` tilt/pan/roll > `.dolly` world offset + push),
cards/tiles/rows at different z with their own desk shadows, real parallax on every camera move, depth-of-field bands
(backdrop-filter, `#dofP1/#dofP2/#dofN1`) and per-element blur on the layers that fall out of focus, film grain.

## TM keys ↔ VO (VO_SCRIPTS.md §6) — one key per VO line, plus sub-beats
| key | t (s) | VO line / beat |
|---|---|---|
| `hook` | 0.3 | 1 · "Angka bulanan sama tahunan kok beda?" (cards lift on "bulanan" +0.42 / "tahunan" +1.2) |
| `ne` | 2.3 | sub · "beda?" — ≠ slams |
| `sum` | 3.4 | 2 · "Dua belas bulan dijumlah, hasilnya nggak sama dengan rekap setahun." — months burst out |
| `add` | 4.6 | sub · "dijumlah" — months counted back in (odometer) |
| `tot` | 5.4 | sub · "hasilnya nggak sama" — ≠ again + SELISIH chip |
| `why` | 8.3 | 3 · "Biasanya ada transaksi yang kecatat dua kali, atau malah kelewat." — dive into the sheet |
| `dup` | 9.9 | sub · "kecatat dua kali" — duplicate row lifts, "dicatat 2×" |
| `miss` | 11.6 | sub · "atau malah kelewat" — rows part, ghost row, "kelewat" |
| `hunt` | 13.2 | 4 · "Nyarinya satu-satu di spreadsheet? Bisa seharian." — magnifier + clock, "satu-satu…" |
| `day` | 15.6 | sub · "Bisa seharian." — clock speeds up, warm light |
| `sol` | 17.2 | 5 · "MasterPajak AI bantu cocokkan angka bulanan dan tahunan, terus tandai baris yang perlu dicek." — brand moment |
| `cek` | 18.5 | sub · "cocokkan" — scan, ✓ / yellow months, summary |
| `flag` | 20.8 | sub · "terus tandai baris yang perlu dicek" — March list, yellow "perlu dicek" rows |
| `know` | 23.7 | 6 · "Jadi kamu tahu harus mulai periksa dari mana." — flagged rows to the top, "Mulai periksa dari sini" |
| `end` | 27.6 | 7 · "Jualan jalan terus, pajaknya AI yang urus." — end card |
| `cta` | 31.1 | sub · "Coba kalkulator pajak gratisnya." — CTA pill |
| `bio` | 33.1 | sub · "Link di bio." |
| `total` | 35.0 | = `data-duration` |

Planned at ~2.4 words/s with short pauses. When the ElevenLabs VO exists: set each key to the word stamp, keep `total` =
`data-duration`, re-run `python3 tools/sfx.py` (it parses TM) and generate `lipsync.js`; everything (camera, robot, SFX) follows TM.

## Scenes
| # | time | world | what happens |
|---|---|---|---|
| 1 | 0–3.4 | paper | hook: BULANAN vs TAHUNAN cards in 3D, "kok beda?", ≠ slam; robot rises bottom-right, scratches head, flinches |
| 2 | 3.4–8.3 | paper | months burst at the camera, counted back in; ≠ + "SELISIH Rp6,5 jt"; robot counts, shakes head |
| 3 | 8.3–13.2 | paper | camera dive to the March sheet; duplicate row ("dicatat 2×"); missing row (slot + ghost, "kelewat"); robot points, shrugs |
| 4 | 13.2–16.7 | paper | wide sheet, magnifier hunting row by row, clock, "satu-satu…" → "Bisa seharian.", warm light; robot tired, ducks out |
| T | 16.7–17.3 | — | band sweep + marquee |
| 5 | 17.2–20.8 | navy | robot + chest hologram; months snap; scan ✓ / MAR + AGU yellow; summary 10 cocok · 2 perlu dicek |
| 6 | 20.8–23.7 | navy | March list: ✓ rows + 2 yellow "perlu dicek" rows |
| 7 | 23.7–27.1 | navy | flagged rows to the top, list shrinks, "Mulai periksa dari sini", robot points |
| T | 27.1–28.2 | — | beam + iris |
| 8 | 27.6–35.0 | deep navy | end card (series template) |

## Brand rules check
- Spelling "MasterPajak AI", official tagline + CTA "Coba kalkulator gratis" + "Link di bio" on the end card.
- "ILUSTRASI DATA" chip on screen for the whole paper part; "ILUSTRASI DATA · SIMULASI ALUR" for the whole navy part (app UI
  flow is simulated). Cover carries "ILUSTRASI DATA".
- No tax rates, deadlines, penalties or guarantees; no DJP/government marks. Feature named only as "Rekonsiliasi bulanan &
  tahunan" + "perlu dicek". Transaction dates in the sheet are ordinary sale dates (no obligation dates).
- Every text line is auto-fitted to its box after the fonts load (`buildReady["fit"]`), so nothing can bleed out of a card.

## Files
- `index.html`, `robot_perf.js` (robot hosts the problem part bottom-right, brand moment bottom-left, end card bottom-right;
  `CUTS` at `sol − 0.05` and `end − 0.01`), `tools/sfx.py` → `assets/audio/sfx.wav` (35.0 s, 48 kHz mono),
  `thumbnail/cover.html` → `thumbnail/COVER_MP06_BULANAN_TAHUNAN.png`.

## Not done / notes for the lead
- Full HyperFrames render not run (lead renders). `lipsync.js` absent until the VO is recorded (loads with `onerror`, 404 in the
  console is expected).
- The robot ducks out before the band sweep (the bands sit under the robot canvas) and re-enters on navy.
