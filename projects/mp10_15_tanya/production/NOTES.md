# Video 15 · Tanya Cepat ke Robot (FAQ) — production notes

Format 1080×1920, 34.0 s (`TM.total` = `data-duration` = 34.0). Title: "MasterPajak AI · Video 15 — Tanya Cepat ke Robot".
The tech skeleton is unchanged from Video 1: GSAP `tl` paused in `window.__timelines.main`, `F/show/hide` (+ the `XS()` scale→scaleX/scaleY
guard), the backward-seek patch, the robot `onUpdate` line, the end marker, `buildReady["layout"]` + `buildReady["robot"]`, and `lipsync.js`
loaded with `onerror`. Every initial state is also pinned on the timeline at 0 (`S0()` = `gsap.set` + `tl.set(…, 0)`, batch-1 lesson 3).
The build step never seeks and does not use `robot_perf.js`. No full render was done; the lead renders.

## Concept
FAQ show, and **the robot is the star**: the host is big (head and shoulders, `h` 1000–1050) and on screen from frame 0. It reacts to
every question (reads, thinks, types) and answers each one with a gesture, a crisp white answer card and a camera push. A counter pill
shows "PERTANYAAN 1/3 → 2/3 → 3/3" with a digit roller and yellow progress segments.

1. **Hook (paper):** seller questions float as chat bubbles in a 3D field: an arc of bubbles at several depths, depth-of-field blur and a
   perspective floor grid. The robot's antenna peeks at frame 0, then it pops up and waves. Kicker "TANYA CEPAT KE ROBOT", a yellow 3D tile
   "**3** pertanyaan", and "yang **paling sering** ditanya seller" with a stabilo stroke. Three bubbles get numbered badges 1/2/3, and the
   robot counts them with head tilts.
2. **Dive → Q1:** the camera flies through the bubble field (blur), and Q1 arrives from depth as a chat message ("Usahaku masih kecil,
   perlu pembukuan?", seller avatar, "PERTANYAAN SELLER · SIMULASI ALUR"). The robot reads it, tilts its head to think, and a typing bubble
   appears. Answer card "JAWABAN ROBOT · **Perlu.**" with a yellow check stamp, "biar kamu tahu **untungnya beneran berapa**." (stabilo),
   and mini bars omzet / untung where the untung bar goes from a dashed "?" to filled yellow ("ILUSTRASI DATA"). The camera pushes in and
   the question goes slightly soft (DOF). The robot nods, presents the card, then speaks to the viewer.
3. **Chat scroll → Q2:** a vertical whip (motion blur and streaks), the counter rolls to 2, and the robot hops to the left. "Harus ngerti
   akuntansi dulu?" A heavy 3D book "BUKU AKUNTANSI · edisi super lengkap" (CSS cuboid with page edges) drops in with a thud and a camera
   shake, and the robot leans back sceptically. **"Nggak harus."** The robot shakes its head and flicks the book out of frame, and the
   answer card arrives with "✕ ~~ngerti akuntansi dulu~~" (a strike line is drawn through it).
4. **Brand moment (navy):** band sweep with the MasterPajak AI marquee. The robot rises half-body bottom-left with the **chest hologram
   logo** (13.96–18.62 s, 4.66 s). "MasterPajak AI bantu menata catatanmu," while messy notes swirl in 3D (nota, chat pesanan, sticky
   "ongkir??", mutasi rekening). On "jadi laporan yang **gampang dibaca.**" the notes fly into one white **Laporan laba rugi** card
   (Penjualan / Biaya / Laba, rows flash as the notes dock, stabilo on laba, "ILUSTRASI DATA"). The robot points at the report.
5. **Whip pan → Q3:** the counter rolls to 3 and the robot glides to the bottom-right. "Kalau bingung, tanya siapa?" The robot tilts
   its head, typing appears, then a "ta-da" with both arms open and the **chest screen glows**: the asisten AI is the robot itself. Cards
   **Asisten AI** ("bantu jelasin angka usahamu") and **Tim ahli** ("**sesuai layanan**" with stabilo, avatars, "MUAMALAH PAJAK"), each
   flying in from depth with a camera push, while the robot points at each in turn.
6. **End card:** the series template, unchanged: beam + iris, "Jualan jalan terus, / pajaknya **AI** yang urus.", CTA pill "Coba
   kalkulator gratis", "Link di bio". The robot rises bottom-right, waves, shows the logo hologram on the left (8 s), points at the CTA
   and waves again.

## TM keys ↔ VO lines (`VO_SCRIPTS.md` §15, planned at ~2.4 words/s + short pauses)
| key | t (s) | VO |
|---|---|---|
| `hook` | 0.3 | Tiga pertanyaan yang paling sering ditanya seller. |
| `q1` | 3.6 | "Usahaku masih kecil, perlu pembukuan?" |
| `a1` | 6.25 | Perlu, biar kamu tahu untungnya beneran berapa. |
| `q2` | 9.85 | "Harus ngerti akuntansi dulu?" |
| `a2` | 12.0 | Nggak harus. |
| `sol` | 13.4 | MasterPajak AI bantu menata catatanmu |
| `lap` | 15.9 | jadi laporan yang gampang dibaca. *(sub-beat)* |
| `q3` | 19.0 | "Kalau bingung, tanya siapa?" |
| `a3` | 21.25 | Ada asisten AI, |
| `tim` | 22.8 | dan tim ahli sesuai layanan. *(sub-beat)* |
| `end` | 25.4 | Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 29.0 | Coba kalkulator pajak gratisnya. |
| `bio` | 31.4 | Link di bio. |
| `total` | 34.0 | — |

To re-time to the real VO, put the ElevenLabs word stamps into `window.TM` (keep `key: number` pairs), set `data-duration` = `TM.total`,
and re-run `python3 tools/sfx.py .`. Scenes, robot and SFX all follow the keys. Keep `q3 ≥ sol + 5.3` so the brand hologram stays ≥ 4 s,
and keep `a2 → sol ≥ 1.3 s` so "Nggak harus." is readable before the bands.

## Scenes
| scene | TM span | bg | depth / camera |
|---|---|---|---|
| S0 hook — bubble field | 0 → q1 | paper | bubbles at z −1000…+300 with DOF blur and an arc (rotationY), floor grid, slow orbit, dive through the field |
| S1 Q1 — "Perlu." | q1 → q2 | paper | Q layer arrives from depth; bubble/card tilted opposite ways; far numeral "1" and bokeh for parallax; push on the answer |
| S2 Q2 — "Nggak harus." | q2 → sol | paper | vertical chat-scroll whip in; 3D book cuboid drop + camera shake; push on the answer |
| S3 brand — laporan | sol → q3 | navy | band sweep in; notes swirling at depth (blur by z) dock into the 3D report card; orbit; chest hologram |
| S4 Q3 — asisten AI + tim ahli | q3 → end | navy | horizontal whip + light streaks; cards fly in from depth; push |
| S5 end card | end → total | deep | beam + iris (series template) |

Robot (`robot_perf.js`, same engine): bottom centre `h` 1050 (hook) → glides right `x` 770 / `h` 1000 (Q1) → hops left `x` 310 (Q2) → ducks
under the bands (cut) → half-body bottom-left, hologram right at (720, 1480, w 420) (brand) → glides right `x` 820 (Q3) → ducks under the
beam (cut) → end card as Video 1 (hologram 360, 1500). CUTS = `sol − 0.05`, `end − 0.01`. In the question scenes the antenna never goes
above y ≈ 1165 and all question/answer text sits above ≈ 1120, so the robot never covers text. The mouth channel `mo` stays 0 on VO lines
and the face stays camera-readable, so `lipsync.js` can drive it later.

## Labels / rules check
- Chat UI (all three question bubbles): "SIMULASI ALUR" chip. Numbers / bars: "ILUSTRASI DATA" (mini chart, laporan laba rugi).
- Tim ahli always "sesuai layanan" (stabilo); the asisten AI only "bantu jelasin angka usahamu" (explains, no advice claim).
- No rates, deadlines, penalties, guarantees, DJP/government marks. Features named only as allowed (pembukuan, laporan laba rugi,
  asisten AI, tim ahli sesuai layanan, kalkulator gratis). Tagline + CTA "Coba kalkulator gratis" + "Link di bio" on the end card.
- Hologram on screen: brand 13.96 → 18.62 s (4.66 s), end 25.98 → 34.0 s (8.0 s), both inside x 120–960 / y ≤ 1600.

## QA done
- Final check in the real runtime: `npx --yes hyperframes@0.8.186 snapshot . --at …(28 times: every scene, every transition midpoint,
  end card) --no-end --timeout 60000`. All frames are correct, with no pops and no leaked build state.
- `npx --yes hyperframes@0.8.186 validate .`: the only errors are the expected `lipsync.js` 404s. The remaining WCAG warnings are for
  the decorative background numerals, the hidden marquee and the small series labels.
- A text-in-box and frame-edge sweep (0–34 s, 0.1 s steps) found no text leaving its card. The only hits are letters still hidden
  inside their rising masks, the deliberate badge numbers on the hook bubbles, and frame-edge crossings during camera transitions only
  (dive 3.4–3.6, chat scroll 9.7, book drop-in 11.2, band marquee 13.0–13.4, whip 18.8–19.0).

## Files
`index.html`, `robot_perf.js`, `tools/sfx.py` → `assets/audio/sfx.wav` (34.0 s, 48 kHz mono), `thumbnail/cover.html` →
`thumbnail/COVER_MP15_TANYA_ROBOT.png`, `.gitignore` (same as Video 1: `.hyperframes/`, `out/parts/`).

## Not done / open
- No full render (by brief). Timing is planned, not measured against the real VO.
- The robot's arms cannot reach above its shoulders at this size, so "pointing at the cards" is a sideways reach toward them, plus
  head turns and gaze.
- The robot is cut by the left or right frame edge when it stands to the side in Q1–Q3 (intentional "star" framing; its face stays
  in frame).
