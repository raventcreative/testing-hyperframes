# Video 3 · Foto Nota → Pembukuan — production notes

**Format:** 1080×1920, 33.5 s (`TM.total` = `data-duration` = 33.5), HyperFrames 0.8.186, same tech skeleton as Video 1
(GSAP `tl` in `window.__timelines.main`, `F/show/hide`, backward-seek patch, `ROBOT_APPLY` onUpdate, end marker).
**Title:** MasterPajak AI · Video 3 — Foto Nota ke Pembukuan.

## Concept
The problem is a light, physical scene; the fix is one continuous navy 3D world.

1. **Hook (light):** a navy drawer (a real CSS 3D box: floor, inner walls, rims, a front panel with a yellow handle) stuffed with
   folded thermal receipts. The folds are 3D segments, the drawer sits on a perspective grid desk, and depth of field plus haze soften the far edge.
   Three more receipts drop in from the start, and the camera drifts and orbits. A phone snaps one nota (shutter + flash), then the photo
   disappears into a scrolling gallery. A "?" pops up, the robot appears at bottom-left and shrugs, and the phone drifts away out of focus.
2. **Brand (navy):** the series band sweep with the MasterPajak AI marquee, then the robot rises half-body at bottom-left with the chest
   hologram (on screen 5.9–10.5 s ≈ 4.6 s). A 3D phone (sliced body, so it has a real edge) flies in with a generic app UI ("Unggah
   nota"). It photographs the nota and uploads it. A "SIMULASI ALUR · ILUSTRASI DATA" chip sits under it.
3. **Read:** the camera pushes into the phone, the photo fills the screen, a scan beam sweeps it and three fields get boxed.
   A ledger card ("Pembukuan", Tanggal / Kategori / Nominal) rises from below. On each VO word, the field lifts off the paper and flies in an
   arc into its cell. All of this is one shared 3D space; start poses are solved with DOMMatrix, so the chip leaves exactly from the paper.
4. **One photo, one row:** the phone steps back behind the ledger (layered, slightly defocused). Every new nota slides onto the
   screen, flashes, and turns into a row card that flies into the next slot (5 rows), while the counter counts. Captions: "1 foto = 1 baris
   rapi", then "~~ketik ulang~~ / dari nol? nggak perlu." The robot nods, then shakes its head.
5. **Complete:** the camera pulls back and the ledger tilts into a 12-row page. The rows cascade in, the badge turns "✓ Lengkap", and a
   "Laporan laba rugi" card rises in front (no numbers; bars only) with "✓ Siap dipakai buat laporan".
6. **Series ending:** beam + iris → end card (tagline in two lines, "Coba kalkulator gratis" pill, "Link di bio", robot at bottom-right
   waving and pointing, logo hologram at left, ≈ 7.6 s on screen).

## TM keys ↔ VO (pace ≈ 2.4 words/s + short pauses)
| key | t (s) | VO |
|---|---|---|
| `hook` | 0.4 | **L1** "Nota belanja numpuk di laci? Difoto doang, terus lupa?" |
| `numpuk` | 1.35 | sub-beat: stabilo on "numpuk" |
| `lupa` | 2.85 | sub-beat: "Difoto doang, terus lupa?" (shutter at +0.3, robot cameo +0.7…+2.06) |
| `brand` | 5.2 | **L2** "Di MasterPajak AI, foto nota bisa diunggah lewat aplikasi." |
| `up` | 7.0 | sub-beat: "foto nota bisa diunggah…" (phone flies in) |
| `snap` | 8.1 | sub-beat: shutter + upload |
| `read` | 9.95 | **L3** "Isinya dibaca, terus disusun jadi baris pembukuan: tanggal, kategori, nominal." |
| `susun` | 11.1 | sub-beat: "terus disusun jadi baris pembukuan" (ledger rises) |
| `tgl` / `kat` / `nom` | 13.1 / 13.75 / 14.4 | the words "tanggal" / "kategori" / "nominal" (each field flies on its word) |
| `row` | 15.6 | **L4** "Satu foto, satu baris rapi. Nggak perlu ketik ulang dari nol." |
| `ketik` | 18.0 | sub-beat: "Nggak perlu ketik ulang dari nol." |
| `ledger` | 21.0 | **L5** "Pembukuanmu jadi lengkap, dan siap dipakai buat laporan." |
| `lap` | 22.6 | sub-beat: "dan siap dipakai buat laporan" (report card) |
| `end` | 25.2 | **L6** "Jualan jalan terus, pajaknya AI yang urus. Coba kalkulator pajak gratisnya. Link di bio." |
| `cta` | 28.6 | sub-beat: "Coba kalkulator pajak gratisnya" (CTA pill, robot points) |
| `bio` | 30.6 | sub-beat: "Link di bio" |
| `total` | 33.5 | end (≈ 1.8 s hold after the VO) |

All animation times (timeline, `robot_perf.js`, `tools/sfx.py`) are offsets from these keys. To re-time to the real VO, edit only `window.TM`, then re-run
`python3 tools/sfx.py .` (and `tools/lipsync.py` for the mouth).

## Brand / claims
- Spelling "MasterPajak AI", official tagline and CTA on the end card; no DJP / government marks; no rates, deadlines or guarantees.
- Shop names on the receipts are generic and invented. Every number (receipt lines, ledger rows) is illustration data. The navy part carries
  "SIMULASI ALUR · ILUSTRASI DATA" whenever the app UI or numbers are on screen; it hides only while it changes position. The hook
  receipts carry no readable numbers.
- Features named: unggah foto nota via aplikasi (Simulasi alur), pembukuan, laporan laba rugi, kalkulator gratis.

## Tech notes
- Each 3D world uses one `preserve-3d` chain; no opacity or overflow on the containers while chips fly, so nothing flattens. `#rows` is
  `preserve-3d` for the same reason.
- The flying chips and rows are children of their ledger cells. In `buildReady["nota3d"]`, `relPose()` seeks the timeline to the take-off time and
  composes offsets + computed transforms up to `#cam` (DOMMatrix). It then solves the pose that puts the cell over the paper field and decomposes it to
  GSAP x/y/z/rotation/rotationY/rotationX/scale (GSAP order translate → rotate → rotateY → rotateX → scale). The flight tweens back to identity,
  so the landing is exact.
- **GSAP quirk (affects the series):** with the backward-seek patch, once the timeline has been seeked backward, a `scale` alias in
  `fromTo` from-vars loses `scaleY`. Here it made the end-card CTA pill collapse to scaleY 0. The `F()` helper here expands `scale` into
  `scaleX/scaleY`. Any video that seeks backward (buildReady seeks, or out-of-order frame capture) and tweens `scale` can hit this.
- Performance: no `filter: blur` on the many 3D layers. Receipt shadows are box-shadows and the bokeh are soft gradients; the only filters are
  the defocus of the receiving phone (L4, one element) and the hook phone fade-out. Three backdrop-filter DOF overlays in total (two in the hook,
  one at the bottom of the complete page).

## QA done (no full render)
- Snapshots at every scene and transition midpoint (≈ 70 frames, contact sheets in the scratchpad `mp03/` folder). Fixed during QA:
  the hook camera was too close; the hook phone intersected the receipt pile (it now has its own overlay stage); the ledger/report and app phone
  peeked in before their entrances (perspective); exiting italic captions left descender fragments (words now hide on exit); the end-card tagline
  lost its spaces (NBSP in `split()`); the GSAP `scale` quirk above.
- `edgecheck` 0–33.45 s: no text crosses the frame edge, apart from the series band marquee (same as Video 1). The receipts falling in from above
  carry print bars only, and the phone fades as it leaves frame.
- Containment check (own script): every visible text run sits inside its card, pill or receipt (ledger rows inside the ledger card, report, upload
  sheet, labels). The only hits are row cards mid-flight, which have their own card background.
- Console: only the expected `lipsync.js` 404 (onerror fallback). Robot never covers text: it hosts bottom-left in the brand scene and
  bottom-right (head below y ≈ 1540) during the ledger beats; hologram 5.9–10.5 s and 25.95–33.5 s, inside the side margins.
- The label chip dissolves twice while it changes place: about 0.5 s while the ledger rises past its spot (≈ 11.5–12.1 s) and about 1 s while the ledger
  tilts (21.0–22.0 s).

## Files
- `index.html`, `robot_perf.js` (cameo shrug, brand + hologram, duck & swap to the right, eyes follow the fields, nod, head shake, point at the report,
  series end), `tools/sfx.py` → `assets/audio/sfx.wav` (33.5 s), `thumbnail/cover.html` → `thumbnail/COVER_MP03_FOTO_NOTA.png`.

## Not done / open
- No real screen recording of the app exists, so the phone UI is a generic simulation (labelled). Swap in a recording when one is available.
- VO not recorded yet: `lipsync.js` is absent (the robot's mouth stays closed), and the beat times are estimates at 2.4 words/s.
- Full render not run (the lead renders).
