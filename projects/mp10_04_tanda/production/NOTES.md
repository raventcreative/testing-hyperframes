# Video 4 · 3 Tanda Pembukuanmu Berantakan — production notes

MasterPajak AI · 10-video series · 1080×1920 · 35.5 s · Indonesian VO (ElevenLabs, recorded later).
Built on the Video 1 skeleton (GSAP timeline `main`, `window.TM`, `robot_perf.js`, `lipsync.js` with `onerror`, grain, series ending).

## Concept
A listicle in one continuous 3D **paper room**: a back wall and a perspective floor grid, one camera rig (`#cam`: orbit +
dolly, CSS perspective 1400 px) and **whip pans** (camera swing + 16 px motion blur on `#lens`) between the signs.
Each sign has a giant **extruded 3D numeral** (18 stacked glyph layers: navy face / gold sides; the "3" is inverted, yellow
face / navy sides, and carries a "PALING SERING" stamp). Depth of field: backdrop-blur bands (`#dofA/#dofB`), far papers
blurred, near foreground papers blurred. A **hook counter** chip (TANDA ① ② ③, top-right) pulses the 3 on "nomor tiga
paling sering" and fills as the list advances. The robot hosts from the bottom-right corner the whole time (head and
shoulders only, under every text block) and reacts to each sign; it ducks under the brand bands and rises half-body with
the chest hologram for the brand beat and the end card (series template).

## Scenes · TM keys ↔ VO lines
| TM key | time (s) | VO line | on screen |
|---|---|---|---|
| `hook` | 0.25 | Tiga tanda pembukuan toko kamu udah berantakan. | Camera pushes into the room; hero 3D "3" swings in, "tanda / pembukuanmu / berantakan" (messy letters pop in askew, stabilo at +2.45). Robot rises (+0.6), points at the 3. |
| `h3` | 3.35 | Nomor tiga paling sering. | Counter dot ③ pulses yellow (+0.2); "PALING SERING" stamp slams on the 3 (+0.68, camera shake), robot points + happy. |
| `s1` | 5.40 | Satu: angka pesanan sama uang masuk nggak pernah cocok. | Whip → numeral "1". "Angka pesanan ≠ uang masuk". Card TOTAL PESANAN (odometer rolls to Rp48.750.000), card UANG MASUK (Rp41.230.500). They try to meet (+2.3), a 3D ≠ disc slams between them (+2.72), both bounce apart, robot x-eyes + head shake. "nggak pernah cocok." |
| `s2` | 9.95 | Dua: nota dan bukti transfer kesebar di mana-mana. | Whip → numeral "2". 16 papers (notas, bukti transfer, chat screenshots) burst into the room in depth and drift; blurred foreground sheets pass the lens; location tags pop on "kesebar di mana-mana" (+2.0: laci, galeri HP, chat, email); stabilo on "mana-mana". Robot looks around, sweeping point. |
| `s3` | 13.95 | Tiga: omzet kelihatan, … | Whip → yellow numeral "3" + stamp (callback). "Omzet kelihatan," Dashboard card: omzet odometer Rp120.500.000 + 12 rising bars, crisp. |
| `s3u` | 15.80 | … tapi untungnya berapa, nggak tahu. | "untungnya berapa?" — UNTUNG BERSIH value stays blurred and flickers; a 3D "?" pops out (+0.75) and wobbles; "nggak tahu." (+1.5) + robot shrug. |
| `kal` | 18.60 | Kalau ada satu aja, saatnya dirapikan. | Whip → the three numerals askew among scattered papers; each hops in turn (+0.75); on "dirapikan" (+1.6) they snap upright into one line and the papers fly into one neat stack; stabilo on "dirapikan." |
| `sol` | 21.60 | MasterPajak AI bantu menata catatan jualan jadi pembukuan dan laporan laba rugi yang gampang dibaca. | Series band sweep with "MasterPajak AI" marquee → navy. Robot rises half-body bottom-left, chest hologram logo right (+0.55…). Flow pills "catatan jualan → pembukuan → laporan laba rugi" light up on the words (+1.6 / +2.85 / +3.7). Chips Pesanan / Pencairan / Nota fly in and dive into a 3D "Pembukuan" ledger card (+2.2…), which flips in 3D into "Laporan laba rugi" (+3.55): Penjualan / Biaya / Laba (stabilo on Laba +4.9). "jadi gampang dibaca." (+4.95, stabilo +5.4). |
| `end` | 28.60 | Jualan jalan terus, pajaknya AI yang urus. Coba kalkulator pajak gratisnya. Link di bio. | Series end card (beam + iris, same as Video 1): tagline line 1 (+0.1), line 2 (+1.4), CTA pill "Coba kalkulator gratis" (+3.35, pulse +4.3), "Link di bio" (+5.2). Robot waves, points at the CTA, waves again; logo hologram left. |
| `total` | 35.50 | — | `data-duration="35.5"` |

All other beat times are offsets from these keys, so re-timing to the real VO = editing `window.TM` only (then re-run
`python3 tools/sfx.py`). Pace assumed: ~2.4 words/s plus short pauses.

## Brand / claim checks
- "Ilustrasi data" chip on every scene with demo numbers (signs 1–3 and the "kalau ada satu aja" papers); "ILUSTRASI DATA"
  + "SIMULASI ALUR" on both faces of the pembukuan / laporan laba rugi card (UI flow without a screen recording).
- No tax rates, deadlines, penalties or guarantees; features named only as pembukuan + laporan laba rugi; no DJP/government
  marks. Spelling "MasterPajak AI"; tagline + CTA exactly as the brief.
- Hologram: brand beat sol+0.72 → end−0.3 (≈6.0 s, panel centre 720/1495, width 420); end card end+0.75 → 35.5 (≈6.1 s,
  centre 360/1490). Both inside x 60–1020 / y ≤ 1600, clear of the frame edges.

## QA done
- Snapshots of every scene and every transition midpoint (46 frames, contact sheets in the scratchpad
  `mp04/MP04_contact_A.jpg` and `mp04/MP04_contact_B.jpg`).
- Text-in-box check with all transforms disabled (45 containers / 846 text runs, cards, papers, tags, stamps, chips, pills,
  CTA): every glyph inside its box. Frame-edge check over the whole film: no text cut on held frames; the only hits are
  inside the motion-blurred whip pans and the series band marquee (same as Video 1).
- 3D numerals keep ≥ 40 px from the frame edge and a clear gutter to the text column at the deepest camera push.
- Robot never over text (head ≥ y 1420 at x > 640 while hosting; sol caption ends above its antenna).
- Console: only the expected 404 for `lipsync.js` (VO not recorded yet, loaded with `onerror`, same as Video 1).

## Files
- `index.html` — composition (`TM` at the top), `robot_perf.js` — robot choreography + hologram.
- `tools/sfx.py` → `assets/audio/sfx.wav` (35.5 s, synthesised: whips, odometer ticks, ≠ slam, paper flutters, tag pops,
  "?" boing, tidy clicks, bands, hologram fx, flip, beam/iris, end chime). Re-run after any TM change.
- `thumbnail/cover.html` → `thumbnail/COVER_MP04_3_TANDA.png` (paper room, extruded "3" + PALING SERING stamp,
  "tanda / pembukuanmu / berantakan", "Nomor 3 paling sering" pill, live robot with x-eyes + shrug; all inside y 285–1635).

## Not done / for the lead
- No full HyperFrames render and no commit (per brief).
- VO not recorded: `lipsync.js` absent (robot mouth idle), timings are planned at ~2.4 words/s; re-time `TM` to the
  ElevenLabs word stamps, then run `tools/lipsync.py` and `tools/sfx.py`.
- The robot's raised "satu" arm on "kalau ada satu aja" is mostly off the right frame edge (reads as a shoulder move);
  the visible beats there are the numeral hops and the tidy sweep.
