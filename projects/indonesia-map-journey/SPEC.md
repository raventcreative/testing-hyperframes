# SPEC — Indonesia Map Journey

GOAL:    The viewer follows one continuous camera journey across a geographically correct Indonesia and recognises three real landmarks per destination; the film ends on a still national map with eight visited markers.
OUTPUT:  HyperFrames, 1920 × 1080 landscape (composed for 16:9, not letterboxed), 30 fps, MP4 H.264 + AAC (SFX only).
TIME:    82 s × 30 = 2460 frames. No music (none supplied), no voice-over.

LOOK:    ground = rebuilt cartography, never screenshots.
         ocean #E4EDF9 → bathymetry >200 m #DBE6F6, >1000 m #D3E0F3, >3000 m #CAD9EF (Natural Earth depth polygons = the real "depth" layer).
         Indonesia land #FBFCFE, coast stroke #294B77 @ 58 %, 1.05 px; neighbours #EDF1F6, stroke #3A6299 @ 30 %.
         land contact shadow = two offset fills (2.2 px @ 8 %, 4.5 px @ 6 %); surf rim 7 px #FBFCFE @ 55 %.
         haze = radial edge veil #FBFCFE 0 → 42 %; paper grain = static 1920 px PNG (seed 7), alpha ≤ 22/255 at 50 %.
         ink #202B3B, navy #294B77 (markers, connectors, routes), secondary #3A6299 (credits), ice #ACC6E7.
         Montserrat 700 44 px +0.16 em for destination names; 600 26 px (min 22) landmark labels; 400 13 px credits.
         Photographs keep natural colour, white 10 px mat, 6 px radius, shadow 0 18 38 −10 rgba(32,43,59,.30).
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
BANNED:  dark void, glow/bloom, globes, compass props, aircraft, control rooms, glass cards, neon, purple gradients,
         invented landmark GPS, street networks, municipal borders, fake terrain, monochrome-tinted photos,
         one-photo-at-a-time slideshows, page-turn/glitch transitions, fade to black, CTA, statistics, travel times.
QA:      0 s (map visible), 5.9 s (Surabaya lands), 9 / 18 / 27 / 36 / 45 / 59 / 67 / 75 s (three photos each),
         51.5 s (five markers), 81.9 s (eight markers, still), every travel seam (no jump), seek-order determinism.
