# FINAL VIDEO QA — PASS / FAIL CHECKLIST

This list is for **the Claude Code renderer/technical editor**. It is a gate, not a self-congratulatory score. Attach actual screenshots/diagnostics to each pass.

## Asset/authenticity

- [ ] Found the mascot's actual source and described its rig type. No lookalike generated.
- [ ] Found existing real logo. No redrawing/retyping/ratio change.
- [ ] User-supplied blue PNG visible throughout, with clean vertical seam extension (not stretched, no banding).
- [ ] No original reference human/mascot, video clips, source creator logo, reused music or `221 FILES` claim appears in output.
- [ ] Poppins 400 and 700 actually embedded/loaded and visible in sample export.

## Suit/rig (lookdev must pass before full assembly)

- [ ] Jacket lapels stay symmetric through 3/4 turn and pointing.
- [ ] Neck/collar, sleeve/wrist, buttons, shirt and torso **do not intersect**.
- [ ] No jagged polygon silhouette, stretched UV, shiny texture seams, flickering normals or z-fighting.
- [ ] Feet are planted, accurate ground/contact shadows move with character.
- [ ] Eyes lead gesture; torso follows, arms don't stretch, animation has anticipation + settle.
- [ ] Full-body test observed at 0/25/50/75/100% plus 6 angles. Screenshots saved.

## Composition and editorial

- [ ] Source reference inspected. Story retains the six-step educational meaning in original Indonesian VO; new scenes are genuinely redesigned.
- [ ] All **18 storyboard scenes** have a specific hero, one clear focal action, motivated camera, shadow, motion handoff and on-VO phrase text.
- [ ] 17 transition boundaries inspected at **outgoing, midpoint, incoming** frames. No black flashes/gaps, clipping or hidden characters teleporting.
- [ ] At least **5 distinct** transition mechanics present (cable, folder hinge, filmstrip, cursor, playhead, slider, etc.); no one repeated canned wipe dominating.
- [ ] Near/mid/far layers show true differential parallax where used. Shadows react correctly when lifted.
- [ ] Glow is selective, cyan highlights really use `#00D0FE`; no unreadable bloom or strobing.
- [ ] Text is **Poppins Bold + Regular**, white/cyan only, gradient backing consistent; all emphasis is script-relevant.
- [ ] Logo at upper-left in every scene, moving sheen/pulse visible at least 3 distinct moments, exact original artwork intact.
- [ ] Mobile 25%-size screenshot: headings, number steps, CTA still readable. No text under UI safe zones.
- [ ] End frame fully resolved with genuine logo and `KOMEN ANIMASI`, hold at least 0.5s. No fade to black.

## VO, sound, typography sync

- [ ] Actual user-recorded VO imported once, source English audio excluded.
- [ ] Every numbered step and key motion apex syncs to actual detected phrase/word, target max ±0.08s shift.
- [ ] No cut through spoken word or jump in VO; no repeated words, timing overflow, or chopped CTA tail.
- [ ] Voice dialogue clear, peaks safe, no clipping; music/SFX rights-cleared and genuinely lower than VO.
- [ ] Titles on screen are truthful and accurately reflect speech. No invented technical claim or credential information.

## Technical verification

- [ ] Final file is non-empty H.264/AAC MP4, 1080×1920, 30 fps, duration matching VO end + logo tail.
- [ ] Rendered 0th, middle, key animation midpoints, scene-boundary, penultimate and last frames inspected **from exported MP4**.
- [ ] Rendering/seek determinism confirmed; same timeline timestamp yields identical frame in different seek orders. No random, wall-clock, async animation drift.
- [ ] Lint/check/inspect commands verified from installed version; real exit codes reported. All meaningful warnings resolved or explicitly disclosed.
- [ ] User approved assembled preview **before** final render.

## Mandatory failure conditions

If any of the following persists, status must be **FAIL / FIX BEFORE EXPORT**, even if other checks pass:

1. Jacket collar/lapel intersects character or mesh flickers in motion.
2. Mascot is a fixed illustration falsely labeled fully rigged 3D.
3. Logo missing, distorted, redrawn, or animation overlaps subtitle.
4. Source footage, source English VO or unrelated third-party branding appears in final.
5. Any black gap or obvious frozen broken transition.
6. Text illegible at phone size, font substituted, cyan glow masking speech-critical words.
7. VO absent but result is claimed final.
8. Render unverified / fake success.
