# V2 ADDENDUM — user revision (read after production/SCENE_CONTRACT.md; this file wins where they differ)

Project: `projects/interview-ai-v2/` (v1 is frozen in `projects/interview-ai-v1/`, do not touch it).

## What the user asked for
1. Keyboard must be in FRONT (v1 had it behind the monitor). The interview set is now: user's laptop icon
   (`assets/icons/laptop.png`, 620×494 on screen) on a 2.5D desk + an applicant seen from behind (over-the-shoulder,
   like reference ref5: a person at a desk facing screens). See `compositions/s01.html` (rebuilt; it is the new reference).
2. Headline = blue gradient field (#00c9ff→#294b77, `.k-field .k-hl`), the KEY WORD(S) in WHITE: add class `k-white` to
   that `.k-hl` (already applied to S02–S08 keywords). Never use other colours for headlines.
3. Kinetic VO text follows the voice word by word (root `compositions/captions.html`, y 1408–1518, centred). Keep
   important objects out of that band; dark objects behind it are fine.
4. User icons: cursor (`assets/icons/cursor.png`, hotspot = fingertip ≈ 7,6 at 112×114), laptop (above), and a small
   white rounded box (rebuilt in CSS, see `#s1-btn` in s01). Use the cursor for real "click" moments with a proper
   arc path, hover, press (scale .86 for 0.07 s, release), release, then exit. Placement must look intentional.
5. No stiff pop-ins: nothing appears in one frame. Everything arrives through motion (tumble/drop/morph/extrude/unfold),
   with anticipation and settle. No CSS 3D plane that starts edge-on (it flickers/"pata-pata").
6. A root-level camera (`#gcam` in index.html) adds drift and punch-ins on top of each scene; do not fight it.

## Reference techniques to apply (analysed from references/v2/ref1–ref5)
- ref3 (search bar): a small square TUMBLES in with rotation and a growing contact shadow, lands with a small squash,
  then MORPHS by widening into a bar; icons pop in; a cursor clicks; the bar collapses into a line → line shrinks away.
  (Transform one object into the next instead of fading between objects.)
- ref4 (chat prompt): a glowing mark forms, the chat box opens around it, the prompt types letter by letter, the cursor
  clicks send, the answer fills in; camera zoom-through between states; subtle blur on fast moves.
- ref1 (kinetic editorial): words appear in sequence with the voice, the key word large/bold; 3D objects (cards, frames,
  clock, target) enter tilted in perspective and settle; quick whip transitions with motion blur between ideas.
- ref2: physical objects with real light/shadow, UI cards that slide on a list, word walls; cuts land on motion.
- ref5: over-the-shoulder applicant at a desk (acting = small idle movements, not loops on UI).

## Rules
- Motion blur on fast moves: `filter: blur()` peaking mid-move (6–12 px text-sized, horizontal for horizontal moves).
- Arrivals expo.out/power4.out; camera power2.inOut; exits power3.in, 40–50 % shorter.
- Keep every scene seam state exactly as documented unless the lead changes it.
