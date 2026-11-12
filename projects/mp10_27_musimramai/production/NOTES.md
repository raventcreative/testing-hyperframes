# MasterPajak AI · Video 27 — Musim Ramai, Catatan Jangan Ikut Kacau

1080×1920 · **33.42 s** (`TM.total` = `data-duration` = 33.42) · HyperFrames 0.8.186 · built VO-first (batch 3 workflow) from the
Video 14 kit, with the Video 24 pin pattern (`tl0` first child + `pinAll()` + `tl.render(0, true, true)`).
Not rendered and not committed here: the lead renders, mixes the music and commits. `out/` is git-ignored (`.gitignore`).

## Concept: a storm of orders over a small packing room
One **CSS-3D light packing room** (a cut-away diorama on the series grid floor) filmed by one moving camera:
- back wall with a **window** (2D storm painted inside it: navy sky, rain, mini order cards falling, a hanging **BUKA / TUTUP**
  sign), a **wall clock**, a pegboard side wall (tape, scissors, label sheet), a navy **packing table** with a desk **lamp** and a
  **notebook "Catatan jualan"** on a stand (cover hinged at the spine, opens in 3D);
- above the room a screen-space **storm cloud** (volumetric lumps), rain streaks, a lightning bolt + flash, and a dense layer of
  falling **order cards** at three depths; the cards that land in the room become **parcel boxes** (yellow kraft, navy tape) that
  pile up in 4 levels and sway.

Story: the storm pours orders in → parcels pile up, a receipt slips under a box, sticky notes postpone the notebook → the storm
passes, the parcels ship out, the notebook opens on an empty page ("?") → the habit: dusk, the lamp clicks on, the storm is back
**outside the window** while inside one row is written per day (week strip Sen..Min ticks), the clock fills a 5-minute sector and
the sign flips to TUTUP → brand (navy): a MasterPajak AI **Pembukuan** keeps up with the storm (order chips rain into the
Penjualan column, nota photos fly into the Modal & biaya column), then the **asisten AI** answers "Untungnya berapa?" from those
records → series end card.

Different from 16–26: no conveyor, river, quiz show, recipe/kitchen, filing cabinet, relay race or orbiting head.

## VO (ElevenLabs, client voice, default AUTO tags)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MP27.mp3` (no `--tags`), one
take, accepted. Voice/settings from `tools/voice_config.json` (eleven_v4, stability 0.41, similarity 0.75). `VO_MP27.mp3` is
31.76 s; on the timeline speech runs 0.38 – 31.82 s, so **≈31.4 s spoken** (limit 33 s).
`assets/audio/vo.wav` = `ffmpeg -i production/vo/VO_MP27.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono"`.

| # | film time (s) | tags the tool used | line |
|---|---|---|---|
| L1 | 0.38 – 3.95 | [playful] [excited] | Musim ramai belanja, pesanan datang kayak badai. |
| L2 | 4.97 – 8.78 | [playful] [excited] [sighs] | Paket numpuk, nota nyelip, catatannya ditunda terus. |
| L3 | 9.07 – 12.14 | [playful] [excited] [curious] | Begitu sepi, baru kepikiran: untungnya berapa? |
| L4 | 12.43 – 15.50 | [playful] [excited] | Kuncinya: catat tiap hari, sebentar aja. |
| L5 | 15.49 – 17.42 | [playful] [excited] | Lima menit, sebelum tutup toko. |
| L6 | 17.40 – 22.54 | [playful] [excited] | MasterPajak AI bantu ngejar ramainya: unggah foto nota, jadi pembukuan yang rapi. |
| L7 | 22.54 – 26.62 | [playful] [excited] | Untungnya berapa? Tanya asisten AI, jawabannya dari catatanmu. |
| L8 | 26.57 – 29.74 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. |
| L9 | 29.73 – 31.82 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. |

**Listen check.** faster-whisper `small` (numpy input, `tools/fw_transcribe.py`) heard every line; no tag was read aloud. The
`[sighs]` tag is performed as an audible "hah" before L2 (≈4.2–4.9 s on the timeline). `small` wrote "notanya lip" and
"grafis"; a `medium` re-check of those two clips heard **"nota nyelip"** and **"gratis"** exactly. "5 menit" is whisper's
spelling of "lima menit".

## TM (every key is a real word time + 0.30 s)
Line-start keys use the audio onset of the first word (energy envelope of `vo.wav`), because the alignment puts line starts up to
0.3 s late (the tag characters compress them; Video 24 found the same). All other keys are the JSON character alignment + 0.30.
Per-word times are in `production/vo/words_MP27.json`.

- L1: `hook` 0.38 (Musim) · `ramai` 0.78 · `bel` 1.10 · `pes` 2.06 · `datang` 2.62 · `badai` 3.26
- L2: `paket` 4.97 · `numpuk` 5.34 · `nota` 6.14 · `nyelip` 6.46 · `catat` 7.18 · `tunda` 7.78 · `terus` 8.30
- L3: `sepi` 9.07 (Begitu) · `sepiW` 9.50 · `pikir` 10.38 · `untung` 11.21 · `berapa` 11.86
- L4: `kunci` 12.43 · `catat2` 13.34 · `tiap` 13.66 · `hari` 14.10 · `bentar` 14.38 · `aja` 14.94
- L5: `lima` 15.49 · `menit` 15.74 · `sebelum` 16.273 · `tutup` 16.50 · `toko` 16.78
- L6: `sol` 17.40 (MasterPajak) · `bantu` 18.54 · `kejar` 18.94 · `ramainya` 19.26 · `unggah` 19.95 · `foto` 20.22 · `nota2` 20.74
  · `jadi` 21.10 · `pemb` 21.30 · `rapi` 21.94
- L7: `q` 22.54 (Untungnya) · `qb` 22.94 · `tanya` 23.64 · `asis` 23.98 · `jawab` 24.967 · `dari` 25.54 · `catmu` 25.74
- L8–9: `end` 26.57 (Jualan) · `urus` 28.033 (pajaknya) · `cta` 29.73 (Coba) · `bio` 31.287 (Link)
- `total` 33.42 = last word end 31.82 + 1.6 s.

Derived time: the brand scene switches at `CUTB = TM.sol + 0.15` (17.55; the band sweep runs 17.07–17.6), so the L5 caption
"sebelum tutup toko." gets ~0.85 s before the bands. The robot's CUTS are `CUTB − 0.05` and `end − 0.01`.
- `end − CUTB` = 9.0 s. The brand chest hologram is at full alpha from `CUTB + 0.72` (18.27) to `end − 0.55` (26.02): **7.75 s**.
- `total − end` = 6.85 s. The end-card hologram runs from `end + 0.75` (27.32) to the end: **6.1 s**.

## Scenes
| # | time (s) | VO | what happens |
|---|---|---|---|
| S1 | 0 – 4.7 | L1 | **Hook, wide (light).** The storm cloud hangs over the packing room; order cards fall at three depths, the window shows the storm, parcels A/B/D stand. Cards landing on the pile become parcels (1.0, 1.75, 2.35, 2.85, 3.38 s); others scatter on the floor. On "badai" lightning: bolt, white flash, window flash, thunder. The robot rises bottom-right, looks up, raises its arms on "pesanan datang", ducks with arms over its head on the lightning. Text (white on the cloud): "Musim ramai belanja," / "pesanan datang" / "kayak badai." (stabilo). |
| S2 | 4.7 – 9.0 | L2 | Camera pushes to the pile. "Paket numpuk": three more parcels drop (5.0, 5.4, 5.8) and the pile sways. "Nota nyelip": a receipt flutters down and slides under the front parcel; only its end sticks out, a dashed yellow ring marks it. Camera to the notebook (6.9): "catatannya ditunda terus": sticky notes slap on the cover — "nanti aja", "besok deh", "abis ramai…". The robot points at the pile, the receipt, and shakes its head. |
| S3 | 9.0 – 12.3 | L3 | "Begitu sepi": the cloud lifts away, rain and storm cards stop, the window sky clears, the parcels ship out to the right, cards stay on the floor. Camera mid → close on the notebook; the cover swings open (10.7–11.4) onto an empty page and a big "?" is drawn on "berapa". Text (dark): "begitu sepi, baru kepikiran:" / "untungnya" / "berapa?" (stabilo). Robot: curious head tilt, shrug. |
| S4 | 12.3 – 17.55 | L4–L5 | **The habit.** Dusk falls, the lamp clicks on (warm pool on the table and wall), the floor mess fades, the storm is back **outside** the window. Week strip "CATAT TIAP HARI" (Sen..Min). On "tiap hari" one row per day is written in the notebook (Sen Rp2.400.000 … Min Rp5.700.000) while each day pill fills yellow with a tick (13.6–15.3); "± 5 menit / hari". "Lima menit": the wall clock's minute hand sweeps 55→60 and fills a yellow 5-minute sector; pill "5 menit". "Tutup": the window sign flips BUKA → TUTUP. Text: "kuncinya:" / "catat tiap hari," (stabilo) / "sebentar aja." then "lima menit," (stabilo) / "sebelum tutup toko." The robot points, nods per row, points up at the clock, waves. |
| T | 17.07 – 17.6 | — | Series band sweep with the MasterPajak AI marquee. |
| S5 | 17.55 – 26.57 | L6–L7 | **Brand (navy).** Robot half-body bottom-left with the chest hologram. The **Pembukuan · Musim ramai · 7 hari** card swings up (Ilustrasi data + Simulasi alur). "Bantu ngejar ramainya": seven "Pesanan" chips rain into the Penjualan cells (row flashes). "Unggah foto nota": seven nota photos (camera badge) fly up from the robot's side into the Modal & biaya cells. "Pembukuan yang rapi": the TOTAL row lights (Rp31.000.000 / −Rp22.000.000) and shines. "Untungnya berapa?": the ledger recedes up-left, the **Asisten AI** chat swings in; question bubble, typing dots on "tanya asisten AI", the answer "Laba 7 hari ini **Rp9.000.000**" (Penjualan Rp31.000.000 / Modal & biaya −Rp22.000.000); on "dari catatanmu" the chip "dari 7 catatan harian ✓" and the seven ledger rows flash in turn. Captions above the stage: "MasterPajak AI bantu" / "ngejar ramainya." → "unggah foto nota, jadi" / "pembukuan yang rapi." → "untungnya berapa?" / "tanya asisten AI." (underlines). |
| T | 26.05 – 27.07 | — | Series beam flood + iris. |
| S6 | 26.57 – 33.42 | L8–L9 | **Series end card**: tagline in two lines, CTA pill "Coba kalkulator gratis" on `cta`, "Link di bio" on `bio`; the robot waves and points, logo hologram left. |

## Numbers (all "Ilustrasi data")
| hari | Penjualan | Modal & biaya |
|---|---|---|
| Sen | Rp2.400.000 | −Rp1.700.000 |
| Sel | Rp3.100.000 | −Rp2.200.000 |
| Rab | Rp3.800.000 | −Rp2.700.000 |
| Kam | Rp4.500.000 | −Rp3.200.000 |
| Jum | Rp5.200.000 | −Rp3.700.000 |
| Sab | Rp6.300.000 | −Rp4.500.000 |
| Min | Rp5.700.000 | −Rp4.000.000 |
| **TOTAL** | **Rp31.000.000** (2.4+3.1+3.8+4.5+5.2+6.3+5.7 = 31.0 ✓) | **−Rp22.000.000** (1.7+2.2+2.7+3.2+3.7+4.5+4.0 = 22.0 ✓) |

- Asisten AI: Laba 7 hari ini **Rp9.000.000** = Rp31.000.000 − Rp22.000.000 ✓ ("dari 7 catatan harian").
- The notebook's daily rows in S4 are the same Penjualan values as the ledger.
- Order cards show single-item prices (Rp55.000–Rp250.000); the slipped receipt shows Rp185.000. They are not summed anywhere.

## Labels and brand rules
- **"Ilustrasi data"**: a screen pill bottom-left for the whole light part (order cards, receipt and notebook amounts), on the
  Pembukuan card and on the Asisten AI chat. **"Simulasi alur"**: on the Pembukuan card and the chat (the only app UI).
- No tax rate, deadline, penalty, guarantee or invented statistic. No event dates and no marketplace/bank/e-wallet/government
  names, logos or colours ("musim ramai belanja" only; day names Sen..Min are a week strip, not dates). "± 5 menit / hari" and
  "lima menit" are the habit tip, not a product promise.
- Features named: pembukuan (+ unggah foto nota), asisten AI, kalkulator gratis (end card). Tagline and CTA exact; spelling
  "MasterPajak AI".
- Robot in every scene: light scenes small full-body bottom-right (x 905, foot line ≈1845), keeping left of / above it free;
  brand half-body bottom-left with the far arm pointing (near arm low, never over the hologram); end card series template.

## QA done (final build)
Scratch dir: `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp27/`
- **Real runtime** (`npx hyperframes@0.8.186 snapshot`), JPG sheets only (PNG dumps deleted):
  - `rtA/RT_A1.jpg`, `rtA/RT_A2.jpg`: one full pass over the light part (0–16.85 s, 18 frames: hook, flash, pile, receipt,
    stickies, storm exit, cover opening, "?", habit, clock, TUTUP).
  - `rtB/RT_B1.jpg`, `rtB/RT_B2.jpg`: band sweep, brand, chat, beam/iris and the end card (17.3–33.3 s, 17 frames).
  - Fix passes: `rtC/RT_C.jpg` (camera dip for "nota nyelip"), `rtD/RT_D.jpg` (receipt + flat floor cards after the
    rotation-order fix), `rtE/RT_E.jpg` (final check: frame 0, receipt, stickies, dusk HUD label).
  - Frame 0 is clean (storm, room, parcels A/B/D, cards mid-air; no caption, robot below frame). All initial states are pinned in
    the nested `tl0` (first child of `tl`) by `pinAll()`, and `tl.render(0, true, true)` runs at the end of the build.
- **`hyperframes validate`**: 0 errors. 4 warnings = the software-GL "GPU stall due to ReadPixels" messages (same as Videos 23/24).
  `lipsync.js` exists, so no 404s. Contrast warnings sit at 4 sample instants only: the lightning flash (3.34 s, 0.1 s white
  flash), a camera move over white order cards (10.0 s), the dusk habit shot (16.7 s; the HUD label and notebook labels were
  darkened after this), and the receded ledger partly covered by the chat panel (23.4 s, by design).
- **Text containment** (`scratchpad/mp27/contain.cjs`, transforms disabled): "no text sticks out of its box". It caught and I
  fixed two cases (the "abis ramai…" sticky and the enlarged receipt total). A `buildReady["fit"]` step shrinks screen captions,
  order-card names, the ledger title, the answer value and the question bubble if a font renders wider than planned.
- **Frame-edge sweep** (`edgecheck.cjs`, every 0.25 s): no screen caption is ever cut. The hits are 3D props only: order cards
  falling or lying on the floor at the frame edges during S1–S3 camera moves (and falling cards behind the cloud at the top),
  the window edge during the floor dip (6.5–7.0 s), the band marquee (17.25–17.5 s) and the chat panel flying in (22.5 s).
- **Audio**: `tools/sfx.py` → `assets/audio/sfx.wav` (33.42 s, −25.2 dB RMS, peak 0.89); `tools/lipsync.py` → `lipsync.js`
  (1919 frames at 60 fps, talking fraction 0.81).

## Real-renderer / build findings (fixed; worth knowing)
1. **GSAP applies `rotationZ` after `rotationX`** (CSS order `rotateZ() rotateY() rotateX()`), so a plane laid flat with
   `rotationX: 90` and spun with `rotationZ` tilts sideways and half of it sinks under the floor. The floor receipt and the
   scattered order cards now spin with `rotationY` (around the vertical axis). Before the fix only "000" of the receipt showed.
2. **Duplicate ids**: an SVG gradient `id="lB"` shadowed the caption `#lB`, so the caption was never split and showed from frame 0.
   The gradients are now `cgL*`; a static-id duplicate check is clean.
3. **Captions above the stage in the brand scene** (batch-3 lesson): the `#sol` captions come after `#w2` in the DOM, and the
   order chips start just above the card (never in the caption band).
4. The page is heavier than earlier videos (16 screen-space storm cards + a 3D room). A `drop-shadow` filter on the big cloud SVG
   made `snap.cjs` time out under load and was removed; the scratch copies of `snap.cjs`/`cover.cjs` use 150–240 s timeouts.

## Known issues / notes for the lead
- **Props at the frame edges.** Scattered order cards on the floor are cut by the frame edge in some S1–S3 shots (foreground
  clutter during camera moves); the window is cut by the left edge for ~0.5 s in the floor dip. No caption is affected.
- **Parcels shipping out (9.4–10.4 s)** happens while the camera moves to the mid shot, so only the last boxes are seen leaving;
  "begitu sepi" is carried by the cloud lifting away, the clear window, the quiet and the empty floor.
- **Hand-over pop.** At 6.53 s the flying receipt hands over to the floor piece; the part that goes under the parcel disappears
  in one frame (the flying twin lives in the overlay rig and is never depth-sorted against the box).
- **Third sticky note** ("abis ramai…") slaps on at 8.42 s, just before the storm lifts; it is on screen for ~0.6 s in the close-up.
- The bands start at `CUTB − 0.48` (17.07 s), so "sebelum tutup toko." is readable for ~0.85 s before the sweep.
- **Commits.** I made no commits. The lead's batch commits (`c06559a`, `1dc38c7`) already picked up this folder in progress;
  `production/NOTES.md` changed after them. `.hyperframes/` is the CLI's snapshot state folder (as in the other projects).

## Files
- `index.html` (TM at the top), `robot_perf.js` (kit engine + Video 27 choreography), `lipsync.js` (from `vo.wav`).
- `assets/audio/vo.wav`, `assets/audio/sfx.wav` (`python3 tools/sfx.py`, 33.42 s, synthesised, −25.2 dB RMS like Video 14).
- `production/vo/`: `lines.txt`, `VO_MP27.mp3`, `VO_MP27.json` (per-line times + character alignment), `words_MP27.json`.
- `tools/sfx.py`, `tools/lipsync.py`, `tools/fw_transcribe.py`.
- `thumbnail/cover.html` → `thumbnail/COVER_MP27_MUSIM_RAMAI.png`.
