# testing-hyperframes

Video remakes for AIpreneur / AIpreneur Automation, built with HyperFrames (HTML + GSAP → MP4) under projects/.

**For any new reel / remake request, read REELS_PIPELINE.md first and follow it end to end** (format, alternating
blue/white theme from reels_log.json, robot presenter, ElevenLabs VO via tools/el_tts.py, open-source assets only,
check frames before delivering, commit + push to `main`).

**Logos (client rule, 2026-11-16):** any brand logo (Claude, GitHub, Instagram, WhatsApp, Meta, TikTok, …) must be sourced from the web
from an open-source set — Simple Icons (CC0, npm `simple-icons`) by default — never hand-drawn or copied from a reference. Then build it
as a real 3D object (SVG path → Three.js SVGLoader + ExtrudeGeometry with a small bevel, brand colour) so it can be animated (spin, pop,
orbit). Record source + licence in the project's production/asset_credits.json.

**Thumbnails / covers (client rules, 2026-11-16):** follow the brand theme table in REELS_PIPELINE.md exactly — navy = the client's navy
background plate (e.g. projects/aip_r25_prompt3d/assets/brand/bg_1080x1920.png), white text, accent #01ccf7 only, white logo; white =
brand/bg-light.png, text gradient #0a0d2c → #294b77, accent #294b77, dark logo. No other colours (no red badges, no yellow headlines).
Minimal layout with negative space: logo, one chip, 2-line headline, short tagline, the 3D mascot, and ONE topic logo in 3D (open-source,
see Logos rule) floating above the mascot's head — e.g. TikTok topic → TikTok logo; "3 AI" topic → those three AI logos. Free/value hooks
("GRATIS") are fine only when the DM really delivers that exact thing.

**Skills (2026-11-20):** project skills live in `.claude/skills/` (auto-loaded) and a portable copy in `skills/`
(index: skills/aipreneur-reels-studio/INDEX.md). Pick the matching one even when the client doesn't name it:
voxel-reels, aip-remake, masterpajak-video, automation-demo, video-carousel, cover-topik, cover-testimoni, cover-foto,
html-demo (MengTo, MIT — live HTML app demos for web pages), product-launch-film (15 s 2D launch film, landscape), landing-flythrough-3d (3D fly-through of a website). Keep both copies in sync when a skill changes.
