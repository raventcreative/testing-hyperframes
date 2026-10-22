# F. QA ACCEPTANCE CRITERIA / PASS-FAIL

1. **Story:** Viewers understand interviewer question → AI suggestion → mechanism → training value → ethics → recruiter debate. Failure: only isolated headline cards with no cause-and-effect.
2. **Timing:** 8 major chapters, all VO spoken through natural end, 95.00-second video at 30fps target; scene cuts synced to actual recorded phrases. Silence-detection scene boundaries are only a baseline. No clipped VO or audio stretching.
3. **Exact copy:** Every quoted headline in the 25-beat storyboard appears spelled/punctuated as documented and when relevant. Accessibility subtitles, if used, must match audio (not just a script file).
4. **Identity:** Use latest AI PRENEUR original logo correctly, no retyping or distortion; opaque-white source only on pale card, transparent derived version visually checked.
5. **Typography:** Poppins Bold 700 and Regular 400 verified by computed/loaded font and snapshots. Font names in CSS are insufficient if files fail to load; don't package proprietary font files.
6. **Color:** Hero gradient #00c9ff → #294b77 consistent; contrast maintained on navy by composition/backing and variable prominence of cyan. Background is recognizably the user-provided texture.
7. **Cinematic depth:** at hero B13 glass, B20 balance scale, B23 decision selector: visible perspective/thickness + occlusion + grounded shadow and coherent light. Visual FAIL even if lint passes when scene remains flat, card-only, or repeatedly fade-rise.
8. **Motion:** Every beat has entry/anticipation, main action, apex linked to VO, settle/legible hold, and purposeful exit/handoff. Verify intermediate frames, not only perfect hero poses. No stutter, jump, shadow mismatch, z-fighting, text pop-in, or awkward holds.
9. **Responsible representation:** UI is illustrated concept, not an authenticated product demo. Do not promote concealment/bypassing recruiter detection or present imaginary application capabilities as verified.
10. **Mobile safe zone heuristic:** Key copy/logo stays approximately x 90–900 / y 220–1540 on 1080×1920, then actually review phone-sized layout with Reels overlay risk; do not pretend heuristic is official policy.
11. **Render contract:** official local HyperFrames version wins. `npx hyperframes lint`, `npx hyperframes check --snapshots` (when supported), midpoints and transitions, non-sequential seek check, complete preview and **mandatory official approval before final render**.
12. **Real exported MP4:** After approval, verify nonempty physical file with media inspector, portrait 1080×1920, 30fps, duration 95s within container frame tolerance, audio AAC stream, no black tail, no missing frames, correct VO.
13. **Truthful report:** PASS/BLOCKED with checked evidence, final absolute output path only if it exists; no unverified aesthetic PASS or fake output claim.
