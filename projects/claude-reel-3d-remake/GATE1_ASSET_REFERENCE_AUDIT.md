# Gate 1 — Asset & reference audit (verified, 2026-10-31)

## Assets (real paths, nothing invented)
| Item | Path | Verified facts |
|---|---|---|
| Video engine | HyperFrames 0.8.186 (npx, pinned) + GSAP + Three.js mascot runtime | Same stack as opus55-reel / hidden-marks-2026. Deterministic seek: every scene is a paused GSAP timeline; WebGL drawn in `hf-seek` from time t only. |
| Mascot 3D | `projects/opus55-reel/assets/mascot3d/mascot_jas3_rigged.glb` (identical md5 9f87ea01 in 6 projects) | **Skinned 3D**, 19 joints, 1 mesh / 1 primitive / 1 material (Tripo AI generated, baked 2048² basecolor+RM+normal webp). No finger bones, no morph targets, jacket is NOT a separate mesh (fused with body). |
| Mascot runtime | `projects/hypit-remake-elevenlabs-mascot-v2/tools/mascot3d/src/` → `vendor/mascot3d.js` | Acting director (`direct.js`), spring performance, VO lip sync, face/lid shader fixes. |
| Logo (AIpreneur, genuine) | `projects/opus55-reel/assets/brand/ai_preneur_logo.png` 1485×1485 RGBA; trimmed `logo_trim.png` 1199×119 RGBA (alpha 0–255, aspect 10.08:1) | Used as image only, mask-clipped sheen. Copied to `assets/brand/`. |
| Background | `brief/.../assets/brand/background_original.png` 1080×1350 RGB | Extended to `assets/brand/bg_1080x1920.png`: native-scale centre plate + mirrored, softened 285 px bands. No stretch, no recolor. |
| Poppins 400 / 700 | `assets/fonts/poppins-latin-{400,700}-normal.woff2` | Local files (copied from aipreneur-six-worlds-remake). |
| VO | — | **MISSING** (to be recorded from 04_VOICE_OVER_INDONESIA.md). |
| Claude product logo | — | No official Claude/Anthropic mark in the repo; UI is shown as a schematic with the word "Code". |

## Reference (assets/reference/reference_original.mp4)
720×1280, 30 fps, 61.48 s, H.264 + AAC. Scene-change detection (threshold 0.12) cuts at:
3.53 · 4.47 · 4.83 · 8.20 · 9.03–9.40 · 13.53 · 17.20 · 20.00 · 20.50 · 26.30 · 30.73 · 33.67–34.03 · 46.40 · 47.47 · 48.40 · 51.80–52.30 · 53.93 · 57.13 · 58.73 · 59.93
Corrections to 02_REFERENCE_SCENE_BREAKDOWN: corkboard hook runs 0–4.5 (not 0–3); envelope "HOW?" 4.5–8.2; 6-STEPS grid + "like this" phone 8.2–9.0; step 1 9.0–13.5; folder 13.5–17.2; AI Video Editor folder 17.2–20.5; new chat/local/folder 20.5–26.3; tools 26.3–33.7; fun part + typing 33.7–40.5; script/VO/animate/captions in phone 40.5–46.4; "If something / 6" 46.4–51.8; recap 51.8–53.9; personal system/files 53.9–58.7; comment CTA 58.7–61.48.

## Mascot / jacket lookdev (out/gate2_suit_motion_test.mp4, qa_suit_zoom.jpg)
- Clean: collar and lapels stay symmetric at 0° / ±35°; no neck or chin intersection; feet planted; buttons stay on the surface.
- **Defects found**: dark "frayed fibre" fringes along the jacket hem, pocket flaps and front edge, and white fringe at the cuffs; slight fringe at the outer sleeve when the arm is raised sideways. Root cause: the Tripo-generated texture/mesh (single fused mesh, baked texture with noisy seam bleed). It is not cloth clipping from the rig.
- Fixable here: texture-level cleanup (seam/fringe repair in the basecolor atlas) + keep gestures in the forward range.
- **Not fixable without a new source**: true separate jacket layer, cloth physics, finger pointing (no finger bones). Needs a re-modelled/re-rigged GLB (Blender) — BLOCKED unless provided.
