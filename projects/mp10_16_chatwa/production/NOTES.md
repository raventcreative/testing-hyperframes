# MasterPajak AI · Video 16 — Dari Chat ke Catatan Rapi

1080×1920 · **31.7 s** (`TM.total` = `data-duration` = 31.7) · HyperFrames 0.8.186, built on the `mp10_14_data` kit.
Built VO-first: the voice was generated first and every `window.TM` key is a real word time from the alignment, plus 0.30 s.
Not rendered here, not committed. The lead renders, mixes the music and commits.

## Concept
One light **CSS-3D paper studio** with a back-wall grid, bokeh, a moving camera and depth-of-field bands.

- **Hook:** a tilted 3D phone shows a **generic chat UI**: "Chat pembeli · Toko Benang Biru", a yellow unread badge, and
  navy/white bubbles. It has no app name, logo or brand colour. Buyer bubbles flood in, the badge climbs 3 → 99+, and short
  bubbles spill out of the phone edges in depth.
- **Line 2:** the three bubbles the VO reads lift off the screen into the top of the frame, closer to the lens each time:
  "Mau 2 ya, kak" (Kaos polos), "Jadi transfer ya" (Tote bag) and "Ongkirnya berapa?" (Topi rajut).
- **Line 3:** on the sigh they drop back onto the screen, and more bubbles pile on top (**numpuk**). The top order bubble
  (Wulan · Kemeja linen) teeters, slides off the edge and falls out of shot, blurring (**kelewat**).
- **Lines 4–5:** the phone sinks to the bottom-left and a **"Catatan jualan"** sheet flies in with columns TANGGAL · PESANAN ·
  NOMINAL. Each order bubble peels off the phone, flies and **lands as one row**. Row 1 fills cell by cell on "tanggal,
  pesanan, nominal", in step with the header stabilo. The lost bubble flies back in as row 4. On "rapi" the total row slides
  in (Rp696.000 = 178+65+49+189+215 rb). On "dicek" five ticks pop.
- **Brand (navy, series band sweep):** the robot rises half-body with the chest hologram. The filled sheet flies in, then
  **flips into a MasterPajak AI "Pembukuan" card** on "pembukuan". On "bisa ditelusuri" row 1 lights up, its link icon turns
  yellow, and a trace line draws out to a source chip: "Asal: catatan jualan · 3 Mei".
- **End:** the series end card: beam + iris, the tagline in two lines, the CTA pill "Coba kalkulator gratis", and
  "Link di bio". The robot waves and points, and the logo hologram sits on the left.

## Script (`production/vo/lines.txt`) and the tags the tool used (ElevenLabs, client voice, default auto tags)
| # | tags used | line | spoken (s, raw → film +0.30) |
|---|---|---|---|
| 1 | [playful] [excited] [curious] | Orderan masuk lewat chat terus. Tapi, dicatat di mana? | 0.08–3.86 → 0.38–4.16 |
| 2 | [playful] [excited] [curious] | Mau dua ya, kak. Jadi transfer ya. Ongkirnya berapa? | 4.16–7.53 → 4.46–7.83 |
| 3 | [playful] [excited] [sighs] | Kalau cuma numpuk di chat, pesanan gampang kelewat. | 8.27–11.46 → 8.57–11.76 (audible sigh 7.9–8.5) |
| 4 | [playful] [excited] | Biasain catat tiap pesanan jadi satu baris: tanggal, pesanan, nominal. | 11.73–16.17 → 12.03–16.47 |
| 5 | [playful] [excited] | Satu pesanan, satu baris. Rapi, dan gampang dicek. | 16.31–19.70 → 16.61–20.00 |
| 6 | [playful] [excited] | MasterPajak AI bantu menata catatan jualanmu jadi pembukuan yang bisa ditelusuri. | 19.98–24.65 → 20.28–24.95 |
| 7 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. | 24.71–27.76 → 25.01–28.06 |
| 8 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. | 27.84–30.00 → 28.14–30.06 |

- Files: `production/vo/VO_MP16.mp3` (29.96 s) and `VO_MP16.json` (per-line times and character alignment). The film audio is
  `assets/audio/vo.wav`, 48 kHz mono, with speech starting at 0.30 s.
- `lipsync.js` comes from `tools/lipsync.py`.
- **Listen check** (faster-whisper `small`, numpy input): every word is spoken and no tag is read aloud. The only extra sound
  is the [sighs] tag, performed as a sigh ("Haaa") before line 3. That is intended by the auto tag, and the film plays it as
  the slump/drop beat. Whisper hears "pesenan" / "catet", the colloquial pronunciation of pesanan / catat.
- **Claims:** no rates, deadlines, penalties, guarantees or statistics. The only feature named is "pembukuan yang bisa
  ditelusuri", plus "kalkulator gratis" in the CTA. Recording each order is shown as the seller's own habit; the film never
  claims the app reads chats.

## TM keys (word time + 0.30 s) ↔ VO
`hook 0.38` Orderan · `chatw 1.42` chat · `tapi 2.54` Tapi · `dicatat 3.18` · `mana 3.9` · `b1 4.46` Mau dua ya kak ·
`b2 5.58` Jadi transfer ya · `b3 6.7` Ongkirnya berapa · `sigh 7.9` (sigh audio) · `numpuk 8.567` Kalau · `numpukw 8.98` numpuk ·
`lost 10.087` pesanan · `lostw 10.78` kelewat · `catat 12.035` Biasain · `baris 13.5` satu baris · `tgl 14.38` · `psn 15.02` ·
`nom 15.66` · `satu 16.608` Satu pesanan · `satu2 17.34` satu baris · `rapi 18.22` · `gampang 18.98` · `cek 19.34` dicek ·
`sol 20.275` MasterPajak AI · `catj 21.74` catatan jualanmu · `pemb 22.993` pembukuan · `bisa 23.5` yang bisa ·
`telusur 24.06` ditelusuri · `end 25.014` Jualan · `urus 26.353` pajaknya AI yang urus · `cta 28.136` Coba · `bio 29.5` Link ·
`total 31.7`. The last word ends at 30.06; the end card holds about 1.6 s after it.

To re-time, edit `window.TM`, then run `python3 tools/sfx.py` again. Every beat, robot key and SFX is an offset from these keys.

## Scenes
| # | time (s) | scene | on screen |
|---|---|---|---|
| S1 | 0 – 4.4 | Hook: chat flood (light, 3D) | The phone tilts in and six bubbles arrive with scroll. Eight spill bubbles fly out in depth, and the badge climbs to 99+. Titles: "orderan masuk lewat / **chat** terus." → "tapi, dicatat / **di mana?**". The robot rises bottom-right, eyes on the phone, and shrugs on "di mana?". |
| S2 | 4.4 – 7.9 | The three read-outs | On each VO phrase one bubble lifts off the screen (yellow ring, scaled 1.4, z toward the lens) into the top of the frame. Its slot in the chat stays as a faint ghost. The robot follows each one with its eyes. |
| S3 | 7.9 – 12.0 | Numpuk · kelewat | Sigh: the three drop back and six more bubbles pile on the screen. "kalau cuma / **numpuk** di chat," (robot: x-eyes) → "pesanan gampang / **kelewat.**": the top order bubble slides off and falls out of shot. The robot reaches for it, too late. |
| T | 12.0 – 13.0 | Phone → sheet | The camera reframes, the phone sinks to the bottom-left and the "Catatan jualan" sheet flies in from top-right. |
| S4 | 12.0 – 16.6 | Biasain catat | "biasain catat tiap pesanan / jadi **satu baris.**" The first order bubble peels off and lands as row 1 (13.45–14.1). The cells fill on tanggal / pesanan / nominal, with the matching header stabilo. The robot points and nods. |
| S5 | 16.6 – 20.0 | Satu pesanan, satu baris | Rows 2–5 land in rhythm. The lost bubble flies back in from below as row 4. "satu pesanan, / **satu baris.**" → "rapi, dan / **gampang dicek.**". The chatter sinks into the phone, the total row slides in, five ticks pop on "dicek" and the robot does an arm pump. |
| T | 19.8 – 20.4 | Band sweep | Series bands with the "MasterPajak AI" marquee. |
| S6 | 20.3 – 25.0 | Brand: pembukuan yang bisa ditelusuri (navy) | The robot rises half-body bottom-left with the chest hologram at x 510–930, y ≈ 1450–1600. The hologram is at full alpha 20.6–24.7 (> 4 s). The sheet flies in and flips (22.4–23.0) into "Pembukuan · MasterPajak AI", labelled "Ilustrasi data" and "Simulasi alur". Captions: "bantu menata catatan jualanmu jadi / **pembukuan** / yang bisa **ditelusuri.**". On "bisa ditelusuri", row 1 lights up, the trace draws, and the source chip "Asal: catatan jualan · 3 Mei" pops. |
| T | 24.7 – 25.7 | Beam + iris | Series pattern, run 0.15 s later than the default so the trace beat can land. |
| S7 | 25.0 – 31.7 | End card | "Jualan jalan terus, / pajaknya **AI** yang urus.", then the "Coba kalkulator gratis" pill and its pulse at 28.1, then "Link di bio" at 29.5. The robot waves, points and waves again. The logo hologram is on the left at x 150–570, from 25.9 to the end (5.8 s). |

## Labels and brand rules
- **"Ilustrasi data"** appears under the chat phone (S1–S3: the quoted prices), on the "Catatan jualan" sheet (S4–S5), on
  the brand sheet's front, and on the Pembukuan card.
- **"Simulasi alur"** appears on the Pembukuan card, the product UI.
- The chat UI is fully generic: no app or marketplace name, logo or brand green. The tick colour is yellow, and there is no
  notification-sound imitation (the SFX blips are synthesised two-tone). Buyers and the shop ("Toko Benang Biru") are
  fictional, and there are no banks or e-wallets.
- No rates, deadlines, guarantees or invented statistics on screen. Dates such as "3 Mei" are order dates in the
  illustrative table.
- The hologram stays inside the safe zone (side margins ≥ 120 px). Key text sits inside x 60–1020, y 220–1600.
- Every text line sits inside its box. A build-time self-check logs `OVERFLOW` console errors for bubbles, cells, headers and
  chips, and logged none. Titles shrink to 940 px if a font renders wider.

## Audio
- `assets/audio/vo.wav`: the VO, delayed to 0.30 s, 48 kHz mono, 30.22 s.
- `assets/audio/sfx.wav`: from `tools/sfx.py`, synthesised, 31.7 s, peak 0.89. It holds: chat blips, spill pops, badge
  ticks, stabilo strokes, lift/drop air, pile landings, the lost bubble's teeter and long fall, the sheet fly-in, peel and
  land pops up the scale, cell ticks, five check pops, the band sweep, hologram fx, the flip, the trace zip and chip chime,
  and the beam boom and end pops.
- No music: the lead mixes the bed.

## QA done
- **Real runtime:** `npx hyperframes@0.8.186 snapshot` covered every scene, the transition midpoints (8.3, 12.5, 20.0,
  20.25, 22.6, 25.0, 25.3) and the end card. Labelled contact sheets are in the scratch dir `mp16/`: `rt1.jpg` (0–12.5),
  `rt2.jpg` (13.2–22.6), `rt3.jpg` (23.3–31.6) and `rt4.jpg` (final pass 0–31.68, after the last edits).
- **`hyperframes validate`:** 0 errors. There are 84 WCAG contrast warnings, all for small decorative chat text (timestamps,
  placeholder, ghost slots) and the band marquee, the same class as earlier videos.
- **Initial states:** pinned both at build time and on the timeline at 0 (`PIN()`), so the t = 0 frame shows no leaked
  sheet or card. `edgecheck` at 0 is clean.

## Known issues
- In S4–S5 the receding chat phone at the bottom-left is cropped by the bottom frame edge, inside the bottom DOF blur band.
  Some of its small chat text ("Tulis pesan…", "Ongkirnya berapa?") is cut there. It is out-of-focus background in a 3D
  scene, not key text.
- During the sheet's fly-in (about 12.2 s, under 0.1 s) its right edge crosses the frame edge. This is transitional.
- The [sighs] auto tag adds an audible sigh of about 0.6 s before line 3. It is kept, because the client asked for the auto
  tags and the film uses it as a beat.
- The beam/iris runs 0.15 s later than the series template. The end card's first line still rises with "Jualan".
