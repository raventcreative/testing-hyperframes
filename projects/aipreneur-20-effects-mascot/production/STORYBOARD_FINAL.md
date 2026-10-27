# STORYBOARD FINAL — 1 klip → 20 transformasi → cara bikin → hasil → KOMEN EDIT

Locked to the real VO (`assets/audio/vo_20effects_elevenlabs.mp3`, 50.991 s). Duration 51.4 s (VO + 0.41 s brand hold). 30 fps, 1080×1920.
Every cut sits ~0.08 s before the first word of its scene (frame-snapped). Times in seconds.

Framing presets (`tools/scenes/kit.py`): MED = medium hero (feet 1800, figure 1470 px, face ≈ y 922); WIDE = full body (feet 1720, figure 1150); CU / ECU = camera re-framed closer (real 3D re-render, not CSS scale).
Fixed screen: logo top-left (x 64, y 72, w 265); effect header (badge + label + 20-dot progress) at y 128–206; captions lower third y 1404–1540 (max 2 lines, cyan keywords Bold); Reels UI safe zone respected.

## S00 · Cold open — proof before explanation  (0.00–3.40, 3.40 s) · ACT 0
- **VO:** “Satu klip polos. Dua puluh efek. Lihat hasilnya.”
- **Visual:** 0.00–0.60: three hard-cut micro previews of OUR results (01 Orbit, 11 Paper Cutout, 17 Frame Break self-shots) on a punch-in, click on each. 'polos': they fold into ONE plain clip panel (smoked-glass frame, mascot medium inside, tiny REC). 'Dua puluh efek': 20 numbered cyan-acrylic chips burst out in a ring around the panel + big `20 EFEK` (20 in cyan). 'Lihat hasilnya': chips orbit and collapse into the panel, camera pushes into the panel.
- **Mascot framing:** MED inside panel clip; push-in
- **Hand-off:** → S01: panel grows to the plain source frame

## S01 · The boring source  (3.40–4.97, 1.57 s) · ACT 0
- **VO:** “Karakter ini awalnya cuma diam.”
- **Visual:** Single plain video panel (thin white border, flat lighter-navy cyc, small timecode). Deliberately effect-free. Mascot medium, a small head turn on 'diam' (never frozen > 0.6 s). Last 0.35 s: the panel's corner radius grows and it shrinks into a tilted ellipse ring around the head.
- **Mascot framing:** MED, lock-off
- **Hand-off:** → S02: panel border becomes the orbit ring

## S02 · 01 ORBIT  (4.97–6.87, 1.90 s) · ACT I
- **VO:** “Lalu ikon mengorbit kepalanya.”
- **Visual:** Tilted orbit ring (thin white + cyan glint) round the head; 4 smoked-glass icon chips (audio wave, 'Aa' caption, image, cursor) orbit 1.25 turns: on the far half they are in the BACK layer (hidden by the head), on the near half in the FRONT layer. Contact glints. Camera to a 3/4 (yaw −14). Head follows the icons.
- **Mascot framing:** MED → 3/4
- **Hand-off:** → S03: the round caption chip flies forward = chat avatar

## S03 · 02 CHAT TAKEOVER  (6.87–8.20, 1.33 s) · ACT I
- **VO:** “Chat mengambil alih layar.”
- **Visual:** Smoked-glass chat window grows out of the avatar circle and takes the frame. Messages (VO words): user bubble 'Satu klip polos.' → reply bubble that contains a small LIVE preview of the mascot (clipped, mascot small) + 'Dua puluh efek.'; a cursor clicks the preview.
- **Mascot framing:** mascot clipped into the preview bubble (h≈520)
- **Hand-off:** → S04: the preview bubble border becomes a physical frame

## S04 · 03 FRAME ESCAPE  (8.20–9.23, 1.03 s) · ACT I
- **VO:** “Dia keluar dari frame,”
- **Visual:** Navy-porcelain picture frame (thickness, bevel, contact shadow) holds the clipped mascot; on 'keluar' the frame tilts back/recedes while the clip releases from the top: the mascot comes forward out of the frame (camera + frame move, no fake leg walk).
- **Mascot framing:** clip → none, h 900 → 1470
- **Hand-off:** → S05: frame corners become the viewfinder corners

## S05 · 04 SNAP ZOOM  (9.23–11.43, 2.20 s) · ACT I
- **VO:** “dan kamera langsung menghantam close-up.”
- **Visual:** Viewfinder corners + centre reticle. 'menghantam': anticipation pull-back 0.15 s, 0.28 s push to a real close-up (re-framed camera, not bitmap scale), 0.16 s settle with tiny overshoot. HERO APEX #1 on the snap. Hold the close-up through 'close-up.' (reaction: head tilt).
- **Mascot framing:** MED → CU (face fills)
- **Hand-off:** → S06: reticle circle round the eye becomes the first check circle

## S06 · 05 CHECKLIST POP  (11.43–13.17, 1.73 s) · ACT I
- **VO:** “Checklist muncul satu per satu.”
- **Visual:** Mascot 3/4 left; 4 enamel pills with cyan acrylic check discs pop in his eye line on the right with 80 ms stagger: 01 Orbit, 02 Chat Takeover, 03 Frame Escape, 04 Snap Zoom (the effects we just saw). Check strokes draw, rim glint, shadows.
- **Mascot framing:** 3/4, fx 400
- **Hand-off:** → S07: last pill stretches into a headline strip

## S07 · 06 HEADLINE STORM  (13.17–14.13, 0.97 s) · ACT II
- **VO:** “Judul berhamburan.”
- **Visual:** Headline strips (Poppins Bold, VO words only: JUDUL BERHAMBURAN, DUA PULUH EFEK, SATU KLIP POLOS, CLOSE-UP, CHAT) cross in perspective at different depths, some behind the mascot, some in front (never over the face). The centre strip slows and locks.
- **Mascot framing:** MED, slight dutch
- **Hand-off:** → S08: centre strip curls into a ring

## S08 · 07 ZOOM PORTAL  (14.13–15.23, 1.10 s) · ACT II
- **VO:** “Kamera masuk ke portal,”
- **Visual:** Satin-metal ring with cyan acrylic inner rim in front of the chest; inside it (mask) the graph world (grid + rising curve). 'portal': camera flies through — ring grows past the lens. HERO APEX #2 on the pass.
- **Mascot framing:** MED → push
- **Hand-off:** → S09: we exit inside the graph world

## S09 · 08 GROWTH CURVE  (15.23–17.43, 2.20 s) · ACT II
- **VO:** “lalu keluar lewat grafik yang sedang naik.”
- **Visual:** Matte grid floor in perspective; an SVG curve draws from lower-left to upper-right behind the mascot, nodes light segment by segment (no numbers/axes values). Camera follows the curve up. Mascot full body.
- **Mascot framing:** WIDE
- **Hand-off:** → S10: the curve's end becomes a studio light cable

## S10 · 09 STUDIO REVEAL  (17.43–20.07, 2.63 s) · ACT II
- **VO:** “Sekarang lihat perubahan gayanya. Studio menyala.”
- **Visual:** Dim stage (mascot dimmed). The cable runs to two satin-metal light stands; their arms open on 'perubahan gayanya'; on 'Studio menyala' softboxes switch on, beams + floor pool, mascot lit (brightness up), small `STUDIO` signage in cyan.
- **Mascot framing:** WIDE → MED 3/4
- **Hand-off:** → S11: the key beam rectangle opens the editor monitor

## S11 · 10 B-ROLL OVERLAY  (20.07–23.43, 3.37 s) · ACT II
- **VO:** “B-roll menumpuk di atas video, lalu timeline editornya terbuka.”
- **Visual:** The mascot clip plays in a monitor (clipped). 'B-roll menumpuk': 3–4 B-roll tiles (self-shots of our earlier effects) stack over the video with slight rotation. 'timeline editornya terbuka': timeline panel opens (V1/V2/A1 tracks, playhead), the tiles drop into V2, cursor drags one. Camera tilts over the timeline.
- **Mascot framing:** mascot clipped in the monitor
- **Hand-off:** → S12: a paper-textured tile lifts off = the paper set

## S12 · 11 PAPER CUTOUT  (23.43–24.73, 1.30 s) · ACT III
- **VO:** “Karakter berubah jadi potongan”
- **Visual:** BUILT (prototype). See tools/scenes/s12.py.
- **Mascot framing:** WIDE
- **Hand-off:** → S13: floor paper edge stretches = rail

## S13 · 12 DOLLY ZOOM  (24.73–25.57, 0.83 s) · ACT III
- **VO:** “kertas, masuk”
- **Visual:** BUILT (prototype). See tools/scenes/s13.py.
- **Mascot framing:** WIDE (constant size)
- **Hand-off:** → S14: viewfinder rect = cover border

## S14 · 13 MAGAZINE COVER  (25.57–26.47, 0.90 s) · ACT III
- **VO:** “ke sampul majalah,”
- **Visual:** BUILT (prototype). See tools/scenes/s14.py.
- **Mascot framing:** cover portrait (clipped)
- **Hand-off:** → S15: cover gloss band = glass highlight

## S15 · 14 LIQUID GLASS  (26.47–28.30, 1.83 s) · ACT III
- **VO:** “lalu melewati kaca yang melengkung.”
- **Visual:** A tall curved glass slab (rounded, thick bevel, edge highlights, chromatic fringe lines) sweeps across the mascot; inside it a simulated refraction (backdrop blur/saturation band + bent highlight). Honest simulation — no full-screen cheap blur. The slab slows over the face on 'melengkung'.
- **Mascot framing:** MED
- **Hand-off:** → S16: the slab curls into a round lens aperture

## S16 · 15 ZOOM THROUGH CUT  (28.30–29.70, 1.40 s) · ACT III
- **VO:** “Kita zoom menembus satu frame,”
- **Visual:** Satin-metal iris aperture centred on the face opens; the camera pushes through a thin frame and into the eye (ECU) with a speed ramp; the pupil's dark becomes the opening of the next world.
- **Mascot framing:** MED → ECU
- **Hand-off:** → S17: the aperture opening already holds the skyline

## S17 · 16 GREEN SCREEN  (29.70–30.80, 1.10 s) · ACT IV
- **VO:** “pindah ke latar kota,”
- **Visual:** Mascot on a green cyc (soft floor) for a beat; 'latar kota': a cyan key line wipes the green away to an original navy city skyline (layered towers, lit windows, parallax), rim light matches.
- **Mascot framing:** MED/WIDE
- **Hand-off:** → S18: vertical building lines become the crack lines

## S18 · 17 FRAME BREAK  (30.80–31.40, 0.60 s) · ACT IV
- **VO:** “pecahkan layar,”
- **Visual:** 'pecahkan': cracks run from the face; the frame splits into ~14 shards (polygon copies of OUR S17 frame) that tilt and fall away in one consistent direction, revealing the HUD scene. HERO APEX #3.
- **Mascot framing:** —
- **Hand-off:** → S19: edge shards settle as HUD corner guides

## S19 · 18 DIGITAL ZOOM  (31.40–32.07, 0.67 s) · ACT IV
- **VO:** “dan masuk”
- **Visual:** Camera HUD: four corner guides, REC (cyan dot), zoom read-out 1.0× → 1.5× → 2.0× in steps, mascot face punched in each step (re-framed, sharp).
- **Mascot framing:** MED → CU steps
- **Hand-off:** → S20: the guides close into the phone bezel

## S20 · 19 PHONE MOCKUP  (32.07–33.30, 1.23 s) · ACT IV
- **VO:** “ke tampilan HP.”
- **Visual:** Navy-porcelain phone (bezel, side buttons, camera island, glass reflection, contact shadow) forms from the HUD guides; its screen plays our own result (live mascot clipped to the screen + mini header). Phone turns on 'HP.'
- **Mascot framing:** mascot clipped to the screen
- **Hand-off:** → S21: phone back = checklist board

## S21 · 20 CHECKLIST  (33.30–35.73, 2.43 s) · ACT IV
- **VO:** “Yang bikin ini terasa mahal bukan efeknya satu-satu.”
- **Visual:** Two-column board of all 20 effect names (Poppins ≥ 28 px), checks chain 01→20, a cyan focus slides; macro on the last two names; then a cyan line links the items ('bukan efeknya satu-satu'). Mascot small at the side pointing.
- **Mascot framing:** small, side
- **Hand-off:** → S22: the linking line becomes the paper edge

## S22 · The secret is continuity  (35.73–39.93, 4.20 s) · ACT V
- **VO:** “Tepi kertas berubah jadi rel kamera. Rel itu membawa kita ke scene berikutnya.”
- **Visual:** Mascot left, pointing. Three cards (self-shots of 11 Paper Cutout, 12 Dolly Zoom, 13 Magazine Cover). 'Tepi kertas' lights the paper edge; 'rel kamera' it morphs into the rail; 'Rel itu membawa kita ke scene berikutnya' a mini dolly rides the rail into the cover card, which grows.
- **Mascot framing:** MED left
- **Hand-off:** → S23: the card becomes the code panel

## S23 · Claude Code workflow  (39.93–43.30, 3.37 s) · ACT V
- **VO:** “Semua bisa kita rancang di Claude Code lewat animasi berbasis kode.”
- **Visual:** Four chained props FOOTAGE → BRIEF → CODED SCENES → PREVIEW (smoked-glass cards, cyan connectors). A conceptual code panel (not an official UI) types a few lines; 'Claude Code' label in text only. Mascot hands the brief card over.
- **Mascot framing:** MED right
- **Hand-off:** → S24: the preview card widens into the montage

## S24 · Human direction + checks  (43.30–46.27, 2.97 s) · ACT V
- **VO:** “Tetap perlu arahan visual, timing, dan pengecekan hasil.”
- **Visual:** Montage grid of 6 self-shots (our results). Three human checks pop on their words: `Arahan visual`, `Timing`, `Pengecekan hasil` (checks draw). Honest framing: AI builds, a human directs and reviews.
- **Mascot framing:** MED
- **Hand-off:** → S25: grid folds into the CTA plate

## S25 · CTA — KOMEN EDIT  (46.27–51.40, 5.13 s) · ACT V
- **VO:** “Mau daftar dua puluh efek, breakdown scene, dan prompt yang bisa lo pakai? Komen EDIT. Gue kirim.”
- **Visual:** Mascot centre, pointing at the viewer. Three deliverable chips on their words: `Daftar 20 efek`, `Breakdown scene`, `Prompt`. 'Komen EDIT': comment card with EDIT in cyan Bold — HERO APEX #4; logo final sheen; last 0.4 s is a calm, complete brand frame (no fade to black).
- **Mascot framing:** MED
- **Hand-off:** end frame

## Hero apexes (only these get the brightest bursts)
S05 snap (≈10.2 s) · S08 portal pass (≈14.9 s) · S12 paper flip (≈23.9 s, soft) · S18 frame break (≈30.9 s) · S25 EDIT (≈50.0 s).
