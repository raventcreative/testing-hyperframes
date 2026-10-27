# MOTION TRANSITION MAP — every cut hands one object to the next

Geometry contracts live in `tools/scenes/kit.py` (screen px, 1080×1920). "A end" = last frame of scene A, "B start" = first frame of B: they show the same object at the same place/size, so a pause on either side of the cut reads as one continuous move. Easing: entries `power3.out`/`back.out` (settle), exits `power2.in`/`power3.in` (commit), camera pushes `power2.inOut`, snaps = anticipation + `power4.out` + overshoot settle.

| Cut (s) | A end state | B start state | Matching geometry | Lens / camera path | Purpose |
|---|---|---|---|---|---|
| S00→S01 3.40 | chips collapsed into the plain clip panel, camera pushing in | the same panel, flat, effect-free | `PANEL` (90,300,900×1180, r36), mascot MED clipped inside | push-in continues, settles to lock-off | "this is the boring source" |
| S01→S02 4.97 | panel border rounds and shrinks into a tilted ellipse around the head | orbit ring | `ORBIT` centre (540,760), Ø1000, scaleY .28, −8° | lock-off → slow orbit to 3/4 (yaw −14) | frame comes alive |
| S02→S03 6.87 | the round 'Aa' icon flies forward, grows | chat avatar circle | `AVATAR` (166,436) Ø96 | camera holds, UI scales from the avatar | icon becomes a conversation |
| S03→S04 8.20 | preview bubble with the live mascot inside | picture frame opening, same mascot framing | `PREVIEW` (250,640,560×700, r28) + `PREVIEW_VIEW` | frame tilts back (rotX 18°) and recedes, mascot un-clips forward | the frame becomes physical, he escapes it |
| S04→S05 9.23 | receded frame corners | viewfinder corners | `VF` (150,360,780×1040) | anticipation pull-back → 0.28 s snap push → settle | the frame becomes the lens |
| S05→S06 11.43 | reticle circle shrinks to beside the eye | first check disc | `CHECK0` (700,578) Ø64 | CU → 3/4 medium (re-frame) | target becomes a tick |
| S06→S07 13.17 | last pill stretches into a full-width strip | headline strip | `STRIP` (−40,1000,1160×96) | slight dutch, lateral drift | list turns into headlines |
| S07→S08 14.13 | centre strip curls into a ring | portal ring | `RING` (540,1050) Ø560 | push through the ring, ring passes the lens | headline becomes a door |
| S08→S09 15.23 | inside of the ring = graph world fills the frame | graph world (`graph_world()` identical markup) | full frame | continue forward, then tilt up following the curve | exit through the graph |
| S09→S10 17.43 | curve tip glowing at the top-right | glowing studio cable start | `CABLE0` (1040,420) | follow the cable down to the stands | data line powers the studio |
| S10→S11 20.07 | key-light beam narrows to a lit rectangle | editor monitor | `MONITOR` (110,300,860×640, r24) | tilt down over the timeline | light opens the edit |
| S11→S12 23.43 | last (paper) clip lifts out of the timeline and lands as the floor strip | paper floor strip | floor strip (−40,1712,1160×70) | wide, static | the edit becomes a material |
| S12→S13 24.73 | paper set, floor strip scaleX 1.18, cut-out mascot | identical set and mascot | `diorama()` + floor strip | dolly in + zoom out (set recedes by depth, mascot constant) | paper edge → rail |
| S13→S14 25.57 | viewfinder locked on the cover rect, world dimmed | cover page swings in on its spine inside the same rect | `COVER` (160,300,760×990) | page turn rotY −84°→0 around the spine, then slow push | camera frame → cover |
| S14→S15 26.47 | gloss band sweeping off the cover | the same cover, the band re-enters as the glass slab's front edge | `COVER` + band at 18° | lateral sweep | gloss → glass |
| S15→S16 28.30 | slab curls into a round lens over the face | iris aperture | `LENS` (540,922) Ø520 | push through frame → ECU → pupil | glass → aperture |
| S16→S17 29.70 | dark pupil / aperture | aperture opening reveals the green cyc | circle from the centre | open-out | lens → new set |
| S17→S18 30.80 | city skyline frame | the same frame as shards (self-shot `city_end`) | full frame | static, shards fall toward camera-left | city → break |
| S18→S19 31.40 | edge shards settle at the corners | HUD corner guides | `HUD` (90,290,900×1220) | stepped digital zoom 1.0→1.5→2.0× | shards → camera HUD |
| S19→S20 32.07 | HUD guides close in | phone bezel | `PHONE` (295,300,490×1010, r70) | phone rises, turns on 'HP.' | HUD → device |
| S20→S21 33.30 | phone turned showing its back | checklist board | `BOARD` (80,290,920×1080, r40) | macro on the last two names | device → recap |
| S21→S22 35.73 | cyan line linking the 20 items | the paper edge in the continuity diagram | horizontal line | lateral | list → the secret |
| S22→S23 39.93 | cover card grows | code panel | card rect → panel | push | trick → method |
| S23→S24 43.30 | preview card widens | montage grid | card → grid | pull-back | method → results |
| S24→S25 46.27 | grid folds | CTA plate | centre | settle | results → action |

## Hero apexes (brightest bursts only here)
S05 snap 10.16 · S08 portal pass ≈14.95 · S12 paper flip 23.92 (soft) · S18 frame break 30.9 · S25 EDIT 50.0.

## Seek safety
All motion = `tl.set` init + `fromTo(..., immediateRender:false)` on paused registered timelines; mascot framing on a private timeline seeked inside the `hf-seek` handler; no `gsap.from`, no left/top/width/height tweens, no random, no timers, finite repeats.
