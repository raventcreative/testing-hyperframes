# ASSET AUDIT — AIpreneur SIX WORLDS (Phase A)

Project: `projects/aipreneur-six-worlds-remake/` (new; no older project or file overwritten).
Toolchain (verified, already working in this repo): HyperFrames CLI 0.8.186 (Chrome + FFmpeg, local render), GSAP (vendored),
Three.js mascot runtime `vendor/mascot3d.js` (same runtime used in our Hypit / X-RAY / 20-Effects videos).

| Asset | Path | Verified facts | Use / limits |
|---|---|---|---|
| Voice-over (final) | `assets/audio/voiceover_final.mp3` | ElevenLabs, mp3 mono 44.1 kHz, **39.967 s**; whisper transcript matches the script (only "Tapi"→"Hapi", "Komen CLAUDE"→"Comment cloud" mishearings) | Used untouched (no stretch). 89 words force-aligned (MMS-300m CTC) → `production/word_timing.json`, phones → lip sync. Video = 40.4 s (VO + 0.43 s still brand hold). |
| Background | `assets/brand/background_original.png` → `bg_1080x1920.png` | 1080×1350 RGBA, pale cool-blue → off-white | Original pixels 1:1 in the middle, 285 px mirrored extension top & bottom (`tools/prep_brand.py`); no stretch, no hue change, no seam (mirror). |
| Logo | `assets/brand/aipreneur_logo_original.png` → `logo_trim.png` | 1485×1485, dark glyphs, alpha bbox (158,655)–(1308,759) | Crop to alpha bbox + 4 px only (1158×112), shown top-left x 70, y 128, width 330. Settle 0.28 s at start + glyph-clipped light sweep ~every 9 s. Never recoloured/rotated. |
| Mascot (hero) | `assets/mascot3d/mascot_rigged_v4.glb` | the user's existing AIpreneur mascot (from our earlier projects), 85,654 verts / 133,682 tris, 1 PBR material (basecolor + normal + metal-rough 2K) | Identity locked; rendered live in Three.js (real 3D: any camera yaw/pitch incl. over-the-shoulder from behind). |
| Rig | (in GLB) | 19 joints: hips, spine, chest, neck, head, shoulder/upperarm/forearm/hand L+R, thigh/shin/foot L+R. **0 morph targets, 0 animation clips** | Acting = keyed poses + damped springs (anticipation, overlap, settle) on real joints. |
| Lip sync | `vendor/vo_words.js` | CTC phones × VO energy, zero-phase low-pass | **Limit:** no jaw bone / mouth morphs → mouth is drawn by the face shader (open/round/closed) from the VO; no mesh warping. |
| Eyes / hands | — | no eyelid geometry; mitten hands (no finger bones) | **Limit:** no blinks; gestures are whole-hand. |
| Fonts | `assets/fonts/poppins-latin-{400,700}-normal.woff2` + OFL | Poppins Regular/Bold | the only fonts used. |
| SFX | `assets/sfx/*.mp3` + `CREDITS.md` | HyperFrames bundled library (Pixabay licence) | high-passed VO-safe copies, under the VO. **No BGM.** |
| Reference videos | pack `assets/reference_video.mp4` (22.94 s, 720×1280) + ref_A/B/C | **not copied into the project** | motion study only — no person, numbers, UI, audio, watermark in the output. |

Missing inputs: none.
