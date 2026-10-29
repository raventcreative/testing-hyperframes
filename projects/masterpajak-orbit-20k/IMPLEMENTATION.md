# MasterPajak — 20K EFEK orbital mascot (10 s)

**Output:** `out/masterpajak_20K_EFEK_orbit_1080x1920.mp4`: 1080×1920, 30 fps, 300 frames, exactly 10.000 s, H.264 High, yuv420p, no audio.
**QA:** `out/qa/` holds a contact sheet (every 0.5 s), the key beats, the hero frame, the exit sequence and a logo zoom.
Rendered locally (HyperFrames CLI 0.8.214, Chrome + FFmpeg). No HeyGen credits used.

## Character: an honest scope note
- No 3D model of MasterPajak exists in the repo. The only 3D GLB is the AIpreneur mascot, which has its own face, so it was not used.
- That makes this a **2.5D image puppet, not a 3D rig**. `tools/build_rig.py` cuts the supplied PNG into 4 layers (body, character's right arm, character's left arm, head). It only masks the original pixels. The logo is never redrawn.
- Reassembled at rest, the 4 layers match the original image exactly. The only exceptions are a few hundred anti-aliased edge pixels inside the arm creases.
- `vendor/mp-puppet.js` renders the puppet in one WebGL2 canvas:
  - **Body:** the upper body rotates and breathes around the hips. The legs have weight 0, so the feet stay planted.
  - **Arms:** smooth mesh skinning from the shoulder seam, which stays glued to the torso, down to the hand. A soft bend runs along the arm, so there is no visible joint. Gestures are capped at ±50° because the mesh starts to thin beyond that.
  - **Head:** tilt is a rigid rotation around the neck. Yaw and pitch are a spherical re-projection of the original head pixels, so the logo foreshortens like a sphere turning, and the head outline does not move.
- "Right arm" means the **character's** right arm, which is on the **left** of the screen.

## Reusable parts (all values are host `data-variable-values` in `index.html`)
| Component | File | Settings you can change |
|---|---|---|
| Orbit ring | `compositions/orbit.html` | count, labels, cx/cy, rx/ry, turns, speedKeys (speed profile), buildStart/End, exitStart, capsule size, font, depth, colours |
| Mascot | `compositions/mascot.html` | preset (`orbit-host`, `idle`, or add a new one to `PRESETS` as pose keys), heightPx, centerX, feetY, shadow |
| Headline | `compositions/headline.html` | accent / main text, colours, Y position, size, revealAt, exitAt |

- Capsules are only translated along the ellipse, never rotated, so the numbers stay upright by construction.
- Capsules are spaced evenly by arc length and move clockwise.
- Rotation is the integral of the speed profile. The default totals exactly 1 turn, so capsule 01 is back at 12 o'clock for the hero frame.

## Timeline
| Time | What happens |
|---|---|
| 0–1.2 s | Mascot reveal plus a camera push-in (0.94→1). Head tilts and the right arm starts to rise. |
| 1.2–3.0 s | Capsules 01→20 appear clockwise from 12 o'clock while the right-arm presentation gesture plays. The track ring draws itself in. |
| 3.0–5.5 s | Rotation ramps up. The head follows the direction of travel and the arm lowers. |
| 5.5–7.0 s | The "20K EFEK" headline is revealed with a masked rise. The mascot gives an asymmetric two-arm welcome: the right arm leads, the left is smaller. |
| 7.0–9.0 s | The orbit decelerates and stops at about 8.5 s with 01 at the top. The mascot faces forward. Hero hold. |
| 9.0–10 s | Capsules retract in a stagger, the mascot nods, and the headline fades by about 9.8 s. The last frame is the mascot alone on the background, ready for the next scene. |

## QA results
- The logo in the hero frame correlates 0.979 with the original.
- All 20 capsules are readable, and none overlaps the head or the headline.
- No stutter or jump frames were found in a frame-to-frame diff scan.
- `hyperframes check`: 0 errors. The `dead_stretch` warning (1.6–5.5 s) is a false positive: the checker cannot see motion on a canvas or on inline styles, and the frames show the orbit building and rotating.
