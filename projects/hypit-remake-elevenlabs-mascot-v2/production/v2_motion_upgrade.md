# V2 motion upgrade — Freddie's revision notes (binding for every scene builder)

Freddie's feedback on the first preview: **visuals feel stiff, transitions are basic, motion is ordinary — wants zoom in / zoom out, things popping up, word highlights; a real 3D animated mascot instead of the static PNG.** Everything in `production/scene_builder_contract.md` still applies (palette, white-text-in-navy-box, determinism, gsap.set initial states, no Math.random, etc.).

## 1. Remove the PNG mascot from your scenes
The PNG cutouts (`assets/mascot/mascot_*.png`) are retired. A rigged **3D mascot** is rendered by a separate root overlay (`compositions/mascot.html`, z-index above scenes). Delete every `<img src="assets/mascot/...">`, its shadow ellipse and its tweens. **Keep the mascot zone below free of key hero parts** (soft background/far-plane is fine there):

| Scene | Global window | Mascot zone to keep clear (px, 1080×1920) | What the mascot does |
|---|---|---|---|
| s02 | 4.200–9.167 | x 700–1050, y 860–1540 | hides BEHIND the vault's right edge, peeks out, holds the edge, steps out right, waves. **The vault's right edge must be a straight vertical edge at exactly x = 700 from y 860 to the floor (≥ y 1500) for the whole scene** (the mascot is masked at x < 700 while hiding). Vault body x ≈ 60–700. |
| s04 | 13.800–16.867 | x 770–1050, y 960–1520 | side-view cameo watching the core, "ooh" at 'kode'. |
| s06–s08 | 20.467–27.967 | x 760–1060, y 940–1560 | stands right of the deck: head tracks each module click, leans in, raises brows, at 'edit' (27.010) points LEFT toward the trim handle. Shift/shrink the deck to x ≈ 40–770 so the trim handle / modules stay visible. |
| s11 | 31.867–35.933 | x 20–330, y 980–1560 | tracks each swap left→right, surprised on 'presenter', then opens both hands to present the result. |
| s14 | 42.867–46.867 | x 770–1050, y 1000–1520 | follows the media entering, approving nod on 'jelas'. |
| s16 | 49.867–51.767 | x 770–1050, y 1000–1500 | side cameo watching the ports, nods on 'brief'. |
| s19 | 58.733–61.100 | x 700–1060, y 820–1540 | hops in from the right, faces camera, lip-syncs "Komen HYPIT. Nanti gue bagiin.", points LEFT at the bubble on 'HYPIT' (59.271), small wave, calm final pose. Keep the bubble x ≈ 40–690. |

The floor line under the mascot is y ≈ 1500–1540; keep your contact-shadow floor consistent there.

## 2. Scene-to-scene transitions (every cut gets a designed transition)
Wrap EVERYTHING inside your `#root` in one new outermost wrapper `<div id="sNN-xf">` (position:absolute; inset:0; transform-origin set per transition). Animate ONLY `#sNN-xf` for the in/out transition (transform + filter blur + opacity is NOT allowed to go to 0 on the whole scene except for the whip's motion-blur moment). Never fade to blank: the first and last frame must still show your hero (blurred/zoomed is fine).

Durations: OUT = last 0.24–0.30 s of your scene (ease `power3.in`, accelerate into the cut). IN = first 0.35–0.50 s (ease `expo.out`, decelerate). Speeds must match across the seam.

| Cut (global s) | Out (end of left scene) | In (start of right scene) |
|---|---|---|
| s01→s02 4.200 | ZOOM-THROUGH into the rising chip (origin ≈ 540,460): scale 1→2.6, blur 0→10px | ZOOM-FROM the vault slot: scale 1.5→1, blur 10→0 (origin = slot) |
| s02→s03 9.167 | WHIP-LEFT: x 0→−620, blur 0→16 | WHIP-IN from right: x 620→0, blur 16→0 |
| s03→s04 13.800 | ZOOM-THROUGH portal centre: scale 1→2.4 | ZOOM-FROM lens centre: 1.45→1 |
| s04→s05 16.867 | PUSH-UP: y 0→−520, blur 0→12 | PUSH-UP in: y 520→0, blur 12→0 |
| s05→s06 20.467 | ZOOM-THROUGH the structure cube (s05 hero) | ZOOM-FROM deck centre 1.4→1 |
| s06→s07 23.267 | ZOOM-THROUGH the 'efek' module | ZOOM-FROM paper sheet 1.5→1 |
| s07→s08 25.133 | WHIP-LEFT (paper already flying left) | WHIP-IN from right |
| s08→s09 27.967 | ZOOM-THROUGH preview monitor | ZOOM-FROM phone/player 1.5→1 |
| s09→s10 30.100 | MATCH (brackets) + punch 1→1.06 | MATCH + settle 1.06→1 |
| s10→s11 31.867 | ZOOM-OUT: scale 1→0.82 | settle 1.12→1 |
| s11→s12 35.933 | frame shrinks (existing) + scale 1→0.9 | ZOOM-FROM 1.25→1 |
| s12→s13 40.700 | WHIP-RIGHT: x 0→+620 (following the flying card) | WHIP-IN from left |
| s13→s14 42.867 | MATCH (shield→vault) + punch | POP-IN: scale 0.88→1 back.out(1.6) |
| s14→s15 46.867 | ZOOM-THROUGH the vault door | ZOOM-FROM terminal screen 1.5→1 |
| s15→s16 49.867 | ZOOM-OUT 1→0.85 | settle 1.1→1 |
| s16→s17 51.767 | WHIP-LEFT | WHIP-IN from right |
| s17→s18 56.700 | PUSH-UP | PUSH-UP in |
| s18→s19 58.733 | ZOOM-THROUGH the booklet page | POP-IN bubble: scale 0.7→1, elastic-ish back.out(1.7) |

The root adds a matching light-streak / flash overlay at each cut; you only do the wrapper moves.

## 3. "Kaku" fixes inside every scene
- **Camera**: stronger, purposeful moves on `#sNN-cam`: push-in 1.00→1.10 across the phrase, or a slow 1–2° dutch tilt, or a lateral drift 30–60 px with parallax (far plane moves 0.4×, near plane 1.6×). Punch-in 1.00→1.06→1.03 on the apex word.
- **Pop-ups**: 2–4 small pop-up elements per scene at relevant words: glass chips / icon badges / sparkle bursts / mini cards (no new text unless it is a spoken VO word). Pop = scale 0→1.15→1 with `back.out(2)` 0.35 s + slight rotation settle; exit with scale 1→0 `power2.in` 0.2 s or stay.
- **Living machine detail**: gears/reels rotate continuously (linear, finite), light sheens sweep across glass/enamel (a skewed white gradient bar translating, opacity 0.35), LEDs chase, particles drift (seeded).
- **Apex**: every apex word = anticipation (0.1–0.15 s counter-move) → hit (scale punch + shockwave ring + 4–6 sparkles + glow) → overshoot settle (`back.out` / `elastic.out(1,0.6)` on the hero part).
- Never idle-bob everything; motion must have a cause.

## 4. Freddie's reference elements (cutouts with alpha, in `assets/elements/`)
Use as real `<img>` elements inside your scene (they are Freddie's own elements), with contact shadows and motion (float-in, pop, parallax, sheen). Keep the palette: they are already navy/blue/white.
- `ref1_hopper_machine.png` (1407×1080, transparent): isometric machine — film pieces go in the hopper, a glass "structure cube" sits on a conveyor. → **s05 hero** ("agent menyusun struktur produksinya": film tiles drop into the hopper, the cube lights up / rotates in on 'struktur').
- `ref2_edit_desk.png` (850×933 after crop; file 1024×1024): isometric editing desk with monitors, reel, film strip, clapper. → **s07**: the paper script peels away to reveal this desk ("workflow"), pop-up highlights on its monitors.
- `ref3_glass_film.png` (1999×1500, translucent glass film reel + strip). → **s03** reference video travelling into the capsule (glass film unrolling), and as a sweeping element in **s12** (variants ribbon).
- `ref4_app_ui.png` (1268×791 after crop; file 1400×791): isometric app UI cards. → **s04**: the agent's workspace materialises behind/around the core on 'proses teknis' (pop-up stagger of the UI).
- `ref5_player_phone.png` (830×618): phone with a video-player card. → **s09 hero** ("video jualan"): phone + player card pops up, the generic product appears ON the player, play button pulses on 'jualan'.

## 5. Verify (same as before)
lint clean for your files; `snapshot --composition sNN` + apex shots + first/last frame; seek-order determinism 0 px; check the mascot zone is clear. Do not touch index.html, captions.html, mascot.html, other scenes.
