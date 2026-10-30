# Locked identity and motion guide

## Assets

- **assets/ai_preneur_logo.png**: exact user-provided transparent AIpreneur white wordmark. No traced/retyped/redrawn substitutes.
- **assets/ai_preneur_background.png**: exact user-provided navy/blue gradient, original 1080×1350. Generate matching additional vertical gradient content for 1080×1920 instead of stretching.
- **assets/click_cursor.png**: exact user-provided white pixel-hand pointer. Keep the recognizable outline and shape. Alpha is included; preserve it.
- Maskot/VO: **already exist outside this ZIP** in the current Claude Code project. Search, inspect, and reuse.

## Typography

| Role | Family / weight | Fill | Treatment |
| --- | --- | --- | --- |
| Normal narration | Poppins Regular / 400 | #FFFFFF | Clear, restrained entrance, readable on mobile |
| Emphasized narration | Poppins Bold / 700 | #00C9FF | Word-synced kinetic emphasis and purposeful scale |
| Selected highlight word | Poppins Bold / 700 | #00C9FF | **White #FFFFFF solid rounded rectangle** with neat padding, no glow behind box |
| App/product label | Poppins Bold / 700 | White or blue as contrast permits | Small label, no oversized hero headline |

- **Never mix font families** inside authored captions. Native code/terminal mockup can use a conventional monospace to remain authentic; all editorial typography is Poppins.
- No rainbow palettes, neon green, red alert effects, or gratuitous giant 3D typography.
- Design mobile-first at 1080×1920; respect top/bottom UI safe areas.
- A highlight should always follow a meaningful spoken word; captions do not need to repeat every word if exact subtitles already exist in the user's project.

## Click cursor: shockwave ripple spec

1. Cursor travels with a polished non-linear Bézier arc and settles precisely on a clickable area.
2. Press: 100–130ms at scale 1 → 0.88 → 1.0; small down/up position shift.
3. Ring A: 0.05–0.55s, radius 6 → 70px at 1080 portrait project scale, alpha 0.6 → 0, line 3px, color #00C9FF.
4. Ring B: 0.14–0.67s, radius 8 → 95px, alpha 0.42 → 0, line 2px.
5. Optional Ring C: 0.25–0.75s, radius 8 → 125px, alpha 0.28 → 0, line 1.5px.
6. Camera impulse: small screen-space ±2–3 px over 0.12–0.16s, decaying, **never heavy jitter** or fake earthquake distortion.
7. Sound: compact tactile click with short low impact, tail <0.45s; VO remains intelligible.

## Overall look

- Dark/deep navy base from provided gradient, cyan #00C9FF as accent, white typography. Claude app scenes keep recognizable brand identity within safe neutral UI.
- Spatially motivated transitions; camera movement driven by viewer focus, not arbitrary preset effects.
- Believable contact shadows, stable texture scale, coherent directional light and reflective highlights.
- Use optical-depth feeling: foreground layer, hero subject, distant environment; background blur used purposefully.
- A mascot's torso/hand/head performance is preferred to invented facial deformation. Only lip-sync when rig supports natural mouth articulation.
- Avoid excessive glows/particles, unnatural wobbling, generic AI zoom loops, low-detail flat icon pretending to be 3D, and lengthy loading sequences.

## Logo behavior

The *Claude* logo reveal at ~6–8s is a separate brand moment, using correct mark when available. The *AIpreneur* wordmark appears as the supplied image at closing. Never swap brands or recolor the AIpreneur source.
