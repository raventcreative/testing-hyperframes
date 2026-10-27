# SPEC — Indonesia Map Journey

GOAL:    The viewer follows one continuous camera journey across a geographically correct Indonesia and recognises three real landmarks per destination; the film ends on a still national map with eight visited markers.
OUTPUT:  HyperFrames, 1920 × 1080 landscape (composed for 16:9, not letterboxed), 30 fps, MP4 H.264 + AAC (sound design, no music/VO).
TIME:    82 s × 30 = 2460 frames. No music (none supplied), no voice-over.
SOUND:   bed_air (synthesised from the camera path: altitude air + speed-driven rush panned with travel + cloud-layer gusts),
         whoosh on long travels, click + soft low thump on each marker landing, pen-trace under each boundary draw-on,
         tick per connector line, paper swish per photo frame (3 takes rotated), reverse swish on retract, chime + low swell at the end.

LOOK:    (revision 2 — user asked for a realistic, non-white map, clouds, city boundaries, more sound)
         national & travel = shaded relief from real elevation (AWS Terrain Tiles): hypsometric land tint
         (lowland #688F56 → highland #A08C6E → peaks #ECECEC) x hillshade (sun NW 45°, exaggeration 14x at z5 → 3x at z10);
         ocean = bathymetric tint (shelf #7EC8D6 → abyss #122E5C) x faint seafloor shade. Lakes from Natural Earth.
         city close-ups = cloud-free Sentinel-2 true-colour mosaics (SCL cloud mask, median of 6 dry-season passes,
         shared dates across tiles, feathered seams) crossfading in from 0.55x to 0.85x of the hold zoom.
         official boundary at arrival: fill #ACC6E7 @ 26 %, outline 2.6 px #FBFCFE over a 6.5 px rgba(14,30,54,.55) under-stroke,
         drawn on over 1.1 s from the marker landing; Jakarta shows its five kota as thin inner lines.
         clouds = 10 seeded cumulus sprites (volume-lit from NW) in 46 cloud systems at altitude, perspective parallax,
         ground shadows at mid altitude, fly-through banks over each destination during its descent, none at holds.
         altitude haze rgba(200,220,242) up to 10 %; edge vignette rgba(10,22,40) 0 → 30 %; static grain 35 %.
         white UI on the dark map: route = dashed #FBFCFE 1.7 px over a 4 px dark under-stroke; labels 700 26 px white with
         dark halo; destination titles 700 44 px white with dark shadow; marker = navy dot + white ring, white contact pulse.
         Montserrat 700/600/400. Photographs keep natural colour, white 10 px mat, 6 px radius.
OBJECTS: the archipelago (Natural Earth 10m), city markers (navy dot 9.5 px + white 3 px ring, contact pulse once),
         Bali = regional island highlight + dashed halo ellipse (no point pin), visited markers 6.5 px (Bali = hollow ring),
         sequence trail (dashed navy 1.6 px) whose leading point is the next locator ring, photo frames with label + credit.
MOTION:  camera = van Wijk–Nuij smooth zoom-pan (altitude rises with distance; rho 1.05 for Java hops → 1.65 Medan→Bali),
         travel ease = smootherstep(t^0.82) (quick lift, long deceleration); no motion blur (canvas blur too slow in software render, and every frame stays sharp).
         camera dead still from marker landing to departure (connectors stay attached).
         title per letter 0.32 s, 0.035 s stagger, blur 5 → 0 px, no translate. connector draw 0.30 s power2.out.
         frame unfold 0.70 s expo.out from the connector endpoint (scale 0.06 → 1, rotateY ±14° → 0), stagger 0.20 s.
         photo push 1.000 → 1.035 sine.inOut over the hold. retract 0.36 s power3.in (stagger 0.06 s), lines pull back 0.28 s.
SHOTS:   see STORYBOARD.md (11 shots) and CAMERA.md (exact camera states per segment).
BANNED:  flat white map, dark void, glow/bloom, globes, compass props, aircraft, control rooms, glass cards, neon, purple gradients,
         invented landmark GPS, street networks, municipal borders, fake terrain, monochrome-tinted photos,
         one-photo-at-a-time slideshows, page-turn/glitch transitions, fade to black, CTA, statistics, travel times.
QA:      0 s (map visible), 5.9 s (Surabaya lands), 9 / 18 / 27 / 36 / 45 / 59 / 67 / 75 s (three photos each),
         51.5 s (five markers), 81.9 s (eight markers, still), every travel seam (no jump), seek-order determinism.
