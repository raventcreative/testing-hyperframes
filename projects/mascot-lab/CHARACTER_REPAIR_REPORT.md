# AI PRENEUR Mascot — Repair & Natural Motion Report (v7)

Asset: `assets/mascot3d/mascot_jas3_rigged.glb` (rig 19 joints, no morph targets, no finger bones).
Original user GLB untouched: `projects/aipreneur-maskot-jas-test/mascot3d_v2/original_tripo.glb`.
Shared runtime: `projects/hypit-remake-elevenlabs-mascot-v2/tools/mascot3d/src/` → bundled to each project's `vendor/mascot3d.js`.

## 1. Issues found → verified root cause → repair

| Issue (user feedback) | Root cause (measured) | Repair |
| --- | --- | --- |
| Stiff, robotic, "two hands up" in every scene | `kit.py` `GESTURES` only contained both-hands-raised poses; the pose changed every 2 words; the head turned left/right on every word | New director `direct.js`: one gesture per **phrase**, mostly one hand, never the same action twice in a row, deliberate still phrases |
| Hands always look like waving (palm to camera) | Axis test (`qa/axes`, `qa/axes2`): bending the elbow alone swings the forearm **sideways in the camera plane** | Poses rebuilt with upper-arm twist (`upperarm y` +1.2…+1.5) so the forearm comes **forward** in front of the body, palm turned up (`hand y` < 0) |
| Gesture without body follow | Arm keys had no head/eye/torso coordination | Eyes lead (−0.22 s) → head (−0.14 s) → chest rotates toward the gesture → arm via spring chain (shoulder leads, forearm lags, hand settles); weight shift between lines |
| Constant motion | Every word triggered a beat | After each phrase: settle to 60%, then rest if the next idea is >1 s away; ~30% of plain lines stay hands-down |
| Mouth too high / not symmetric (earlier) | Old model offset +1.35 cm | Mouth centred (`mouthDy 0`) |
| Chin / face bumpy | Noisy normals on the simplified mesh | Welded Laplacian face normals + higher-res mesh |
| Eyelid patch during blink | Eye relief geometry + flat lid colour | Lid lit with fitted smooth normals, rim colour/roughness sampled from surrounding skin |
| Jacket tear at the armpit when the arm rises | Seam between jacket and sleeve skin clusters | Seam hem smoothing + tuck; the gesture library keeps the arm forward (no wide abduction) |

## 2. Gesture library (reusable)
`idle, explain, present, point, pointFwd, thinking, emphasize, compare, question, reveal, confident, welcome, cta`
Poses: `rest, restIn, explain, explain2, open, present, presentLow, point, pointFwd, think, beat, heart, shrug, welcome, hold`.

Usage in any HyperFrames project (Python scene kit):
```python
S.intent(S.W(12), "present", "left")   # screen side; left = his right arm
S.intent(S.W(30), "question")          # both palms up, head tilt
```
Without intents, the director reads the Indonesian line (jangan/bukan → emphasize + small head shake,
kenapa/? → question, pertama/kedua → compare, komen/follow → cta …) and rotates through the rest.
JS: `const DIR = Mascot3D.direct(VO_WORDS, D, { intents, seed, quiet })` → `buildPerformance(DIR.tracks)`,
`DIR.gaze(t)` → eye shader, `DIR.blinks` → blink schedule, `Mascot3D.micro(t)` → breathing / weight shift.

## 3. Tests
| Test | How | Result |
| --- | --- | --- |
| Pose sheet (12 poses) + joint axes (front/side) | `qa/poses1`, `qa/axes`, `qa/axes2`, `qa/p2` stills | Done: axis conventions found, forward poses chosen |
| A idle · B explain · C point L/R · D both hands (reveal) · E compare/torso · F close-up think/question · G/H welcome-confident-CTA full body | `tools/spec.json` (31 s sequence), stills `qa/t1` | Stills checked: varied gestures, head + eyes turn to the pointed side, jacket clean in all tested poses |
| Same in production context | `hidden-marks-2026` draft (60 s, real VO, lip sync) | See draft video |

## 4. Remaining limitations (honest)
- No finger bones in the GLB → a "point" reads as an open directing hand; real index-finger pointing needs a re-rig.
- No cloth simulation: the jacket follows skin weights. Clean for the tested forward gestures; a very wide sideways
  raise (> ~70°) can still crease the armpit, so the library avoids it.
- No hand-object contact solver: props are staged where the gesture points, not physically gripped.
