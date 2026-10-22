# REVIEW — AI PRENEUR · Interview Dibantu AI v2 (client revision of v1)

Status: **v2 draft review stage — waiting for user approval before the final render.**

## v2 changes (client feedback)
- Keyboard now in front: interview set rebuilt around the user's laptop icon on a 2.5D desk (no CSS-3D desk plane, so no
  edge-on flicker) + an applicant seen from behind (over-the-shoulder, ref5), navy blazer, idle breathing, head drops on "kepala".
- S01 opening uses the user's icons: white box tumbles in and lands (ref3), widens into a "MULAI INTERVIEW" button, the user's
  cursor arcs in and clicks (1.60 s, click SFX), the button grows into the call screen and the camera pulls back to reveal the laptop.
- Headlines: blue gradient field + key word(s) in white (`k-white`).
- Kinetic VO text: every word appears on its spoken time (word times in production/word_times.json), current word white.
- Global camera (#gcam): punch-ins on apex words + drift, plate follows at 30 % for parallax.
- S02 rebuilt on the new set (ghost keyboard lifts off = "tanpa mengetik"; strips land on the SFX ticks).
- S03 B07 like ref4: prompt box morphs open around the caret, prompt types, cursor clicks send (23.95 s, click SFX), paths draw.
- S03–S05: 6 stiff moments replaced (board no longer starts edge-on, mic/outline card/tiles/second window arrive physically).
- S08 B24: IZINKAN / LARANG buttons split out of the decision line; cursor hovers IZINKAN on "mengizinkan", LARANG on
  "melarangnya", then hesitates — no click (the dilemma stays open).
- Box icon: the supplied PNG has a white background with JPEG noise, so the box is rebuilt in CSS with the same shape/shadow.

## Creative calls
- Locked storyboard executed as given (8 scenes / 25 beats, locked copy). No alternative storylines were built — the brief locked the film.
- Look: user's navy plate + CSS-3D miniature stage (desk, monitor, paper with edge thickness, contact + cast shadows down-right), cyan used only as signal.
- Real 3D (Three.js r159, vendored, driven only from timeline time): B20/B21 balance scale (S07), B23 two-state selector dial and B25 sculptural question mark (S08).
- B13 frosted window is 2.5D (`backdrop-filter` outside any preserve-3d tree).
- Headline gradient: one #00c9ff→#294b77 field across the 900 px text block (`.k-field`), so short lines stay readable on navy; key ivory plates (answer card, DRAFT card, logo plate) give the light editorial plate moments.
- Phrase-level VO subtitles added (y≈1418–1500, Poppins 400). Toggle with the root variable `show-captions`.
- Sound: VO unchanged + 7 sparse SFX from the bundled HyperFrames library (Pixabay Content License): bead ping, 3 strip ticks, lever click, two dial contacts. No BGM (per brief).
- Background: the supplied mirror extension doubled the lower-right glow (visible seam ≈ y 1635), so `background_1080x1920_v1_reworked.png` was made: original uniformly scaled (3 px edge artefacts trimmed), centred, top/bottom continued from the blurred colour field with the original's own grain. The original file is untouched.

## Timing changes vs provisional (full list in STORYBOARD.md)
S04 starts 32.90 (VO4 "Cara kerjanya…" begins 33.15, not 34.93). Internal beats moved to the anchored words; VO never retimed; output stays 95.00 s.

## Measured
- `npx hyperframes check`: ok — lint 0 errors, runtime 0 errors, layout 0 errors (intentional overlaps opted out: extruded "?" layers, typed characters, stacked strips, flip-tag faces), motion assertions (`index.motion.json`) 0 errors, contrast 0 errors.
- Non-monotonic seek test (`tools/seek_determinism.sh`, 68.4→12→87→43… in two orders): 0 differing pixels at 8 instants.
- Poppins 400/700: `document.fonts` reports both faces `loaded` from `assets/fonts/*.woff2` (OFL); no system Poppins present.
- Seams: 5-frame strips around every cut checked; handoff objects match on both sides.
- Phone sheet (360 px): headlines and subtitles legible.

## Draft render (out/interview-ai-v1_DRAFT_review.mp4, --quality draft, local)
ffprobe: 1080×1920, H.264, 30/1, 2850 frames, 95.000 s; AAC 48 kHz stereo. blackdetect: 0 black segments.
`hyperframes audio`: -14.8 LUFS integrated, true peak -1.0 dBTP, no clipping, speech ends 92.97 s. Frames extracted from the MP4
at 12 instants incl. 3D mid-action (68.4, 71.9, 83.4, 94.95) match the snapshots; last frame = logo lockup.

## Looked at only
Motion feel between sampled frames, ease quality, overall pacing. Sound is measured, not heard.

## Warnings kept on purpose
- craft `text_below_floor`: chapter counters (22 px) and small object labels (PEWAWANCARA, POIN 1–3, PROMPT, CATATAN) are texture, not reading text.
- craft `line_unread`: the typed question is counted per character; chapter counters swap at seams.
- runtime: Three.js r159 UMD deprecation notice and a WebGL ReadPixels performance note (no effect on frames).
- lint `composition_file_too_large` on s08 (B22–B25 share one Three.js scene).

## Weakest shots / with more time
- B11 semantic tiles and B14 window stack read a little small on a phone.
- B05/B06 strips + assistant ring could carry more material detail.
- S06 → S07 passes through a ~0.3 s near-empty dark frame (intentional dip, but could carry the light pool more strongly).

## v2 draft render (out/interview-ai-v2_DRAFT_review.mp4, --quality draft, local)
ffprobe: 1080×1920, H.264, 30/1, 2850 frames, 95.000 s; AAC 48 kHz stereo. blackdetect: 0. `hyperframes audio`: -14.8 LUFS,
true peak -1.0 dBTP, no clipping, speech ends 92.97 s. 14 frames extracted from the MP4 (incl. box drop, click, laptop reveal,
prompt click, 3D scale/dial, decision cursor, final logo) match the snapshots. `check` passed; seek test 0 px diff.
