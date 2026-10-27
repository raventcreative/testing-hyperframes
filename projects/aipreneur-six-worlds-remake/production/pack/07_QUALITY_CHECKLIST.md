# REVIEW CHECKLIST — ask Claude Code to tick using visual evidence

## Preflight

- [ ] Source MP4 observed, ~22.94s, 720x1280; NEVER reused as target footage.
- [ ] `background_original.png` inspected and scaled into 1080x1920 without stretch/seam.
- [ ] `aipreneur_logo_original.png` alpha bounds inspected; shape unchanged, aligned top-left.
- [ ] Mascot asset real path logged, render preview from front/side/3-quarter.
- [ ] Rig hierarchy, bones, morph targets, clips and fallback plan documented.
- [ ] VO final file found and probed; **or** work clearly marked provisional silent animatic.

## Visual system

- [ ] Background visibly user's pale-blue/white gradient throughout; spotlight only dims locally.
- [ ] Main font Poppins Bold and supporting Poppins Regular loaded correctly.
- [ ] Normal headline text gradient exactly #0A0D2C→#294B77.
- [ ] Highlight white text only inside suitably dark/navy gradient box; safe legibility.
- [ ] Logo upper-left throughout, restrained repeat specular sweep (not constant pulse).
- [ ] No original speaker, stats, watermark, social comment, or original UI screenshot appears in target footage.

## Scene craft

- [ ] S01 hook hero visible at frame 0, mascot 3D recognizable.
- [ ] S02 editorial split has 3D chart depth and valid no-fake-data semantics.
- [ ] S03 genuine over-the-shoulder parallax and no cutout card effect.
- [ ] S04 giant type has bevel/contact shadow with visible occlusion.
- [ ] S05 glass panels read as volumetric, text remains legible.
- [ ] S06 beam path, light direction, pose and cast shadow agree.
- [ ] S07 grading compares the SAME frame; brand/maskot color still accurate.
- [ ] S08 recaps connected objects visibly; narrational payoff appears before CTA.
- [ ] S09 production view includes VO/timing quality caveat, no fake software proof.
- [ ] S10 actually shows 6 original looks and valid CLAUDE resource promise.
- [ ] All transitions have matching contour/optical path, no accidental half-second blank.
- [ ] Camera motion varies meaningfully; no identical tween/ease, no infinite timeline, no head/limb clipping.

## Engineering proof

- [ ] Native portrait 1080x1920 30fps.
- [ ] Deterministic seeking: compare same timestamp rendered twice, no unexpected differences.
- [ ] Lint/validation and scene bounding-box review passed for installed toolchain.
- [ ] Snapshot at 0%, 25%, 50%, 75%, 100% and every material transition midpoint.
- [ ] Test at phone-size width ~360px for legibility and social top/bottom safe zones.
- [ ] Face/head/morph identity consistency manually checked every camera cut.
- [ ] Final VO audible to last word with no clipping; SFX do not drown it; no BGM default.
- [ ] Show draft preview to user and get approval BEFORE delivery-quality render.
- [ ] After approved final render: MP4 verified by ffprobe and manual spot inspection.

## Realism audit / devil's advocate

**More transitions ≠ more premium.** A continuous camera portal only works when spatial orientation and object edges match; if scene depth is fake, a restrained editorial transition looks better. A true 3D avatar may lack hand/facial rig; in that case design around credible torso/eye-line/prop movement. Never trade identity for exaggerated facial acting.

If these gates fail, flag exact timestamp + defect + repair approach. Do not self-award “10/10” based only on the code compiling.
