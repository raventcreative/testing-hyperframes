# ASSET INVENTORY — AIpreneur 20 Effects (3D mascot remake)

Project: `projects/aipreneur-20-effects-mascot/` (new, isolated; no other project or file touched).
Renderer: HyperFrames CLI 0.8.186 (local Chrome + FFmpeg). Output: 1080×1920, 30 fps, H.264/AAC.

| Asset | Path (project) | Source | Verified | Status / notes |
|---|---|---|---|---|
| 3D mascot (hero) | `assets/mascot3d/mascot_rigged_v4.glb` | the existing AIpreneur mascot already used in our Hypit / X-RAY projects (copied, unchanged) | 7.6 MB GLB, 85,654 verts / 133,682 tris, 1 PBR material (basecolor + normal + metallicRoughness 2K, no AO) | Identity, colours, proportions untouched. Rendered live with Three.js (`vendor/mascot3d.js`) in one WebGL canvas. |
| Rig | (in GLB) | — | 19 joints: hips, spine, chest, neck, head, shoulder/upperarm/forearm/hand L+R, thigh/shin/foot L+R. **0 morph targets, 0 animations** | Body acting = keyed poses + damped springs on these joints. Legs exist (used only for subtle weight shifts). |
| Lip sync | `vendor/vo_words.js` (VO_WORDS / VO_PHONES / VO_ENV) | `tools/vo_align.py` | CTC forced alignment (MMS-300m ONNX) × VO energy, zero-phase low-pass | **Limit:** no mouth morph targets/jaw bone → the mouth is a shader-drawn mouth on the face texture driven by the VO phones (open/round/closed). Not a geometric jaw. |
| Eyes / blinks | — | — | GLB has no eyelid geometry | **Limit:** no blinks (every faked eyelid produced artefacts in earlier tests). Eye life comes from head turns/gaze via head bone. Hands are mitten-shaped (no finger bones). |
| Voice-over | `assets/audio/vo_20effects_elevenlabs.mp3` | user (ElevenLabs) | mp3 mono 44.1 kHz, **50.991 s**; 150 words aligned (`production/word_timing.json`, `phoneme_timing.json`); whisper cross-check: one word differs by 0.28 s ("Kita"), alignment kept | Used untouched (no stretch/pitch). Video duration = VO + 0.41 s quiet brand hold = **51.4 s**. |
| Background | `assets/brand/background_navy.png` (original) → `assets/brand/bg_navy_1080x1920.png` | user | original 1080×1350 RGBA | Derivative keeps the original pixels 1:1 in the middle; 285 px mirrored extension top and bottom (`tools/prep_brand.py`). No stretch, no recolour. |
| Logo | `assets/brand/aipreneur_logo_original.png` (original) → `assets/brand/logo_trim.png` | user | 1485×1485, alpha bbox (139,652)-(1326,759) | Derivative = crop to alpha bbox + 4 px (pixels untouched), shown at x 64, y 72, width 265. Sheen = a white-cyan band masked by the logo alpha. |
| Fonts | `assets/fonts/poppins-latin-{400,700}-normal.woff2` + OFL | Google Fonts (OFL) | — | Poppins Regular + Bold only. |
| SFX | `assets/sfx/*.mp3` + `CREDITS.md` | HyperFrames bundled library (Pixabay licence) | — | click-soft, key-press, ping, pop, sparkle, typing, whoosh-short. High-passed VO-safe copies in `assets/sfx/vo_safe/`. **No BGM.** |
| Grain | `assets/brand/grain_256.png` | ours | — | subtle film grain, stepped (deterministic). |
| Reference video | `…/scratchpad/pack20/…/reference_20_effects.mp4` (NOT in project) | user pack | 720×1280, 30 fps, 59.65 s | **Motion reference only.** Not copied into the project, not used in the output (no human, room, creator UI, logo, audio or text). |
| Self-shots | `assets/elements/selfshots/*.png` | rendered from THIS composition | — | Stills of our own finished scenes, used where the story needs several copies of the result at once (cold-open preview, B-roll tiles, frame-break shards, montage). |

## Missing inputs
None blocking. No licensed music needed (brief says NO BGM).
