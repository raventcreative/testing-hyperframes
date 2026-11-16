# testing-hyperframes

Video remakes for AIpreneur / AIpreneur Automation, built with HyperFrames (HTML + GSAP → MP4) under projects/.

**For any new reel / remake request, read REELS_PIPELINE.md first and follow it end to end** (format, alternating
blue/white theme from reels_log.json, robot presenter, ElevenLabs VO via tools/el_tts.py, open-source assets only,
check frames before delivering, commit + push to `main`).

**Logos (client rule, 2026-11-16):** any brand logo (Claude, GitHub, Instagram, WhatsApp, Meta, TikTok, …) must be sourced from the web
from an open-source set — Simple Icons (CC0, npm `simple-icons`) by default — never hand-drawn or copied from a reference. Then build it
as a real 3D object (SVG path → Three.js SVGLoader + ExtrudeGeometry with a small bevel, brand colour) so it can be animated (spin, pop,
orbit). Record source + licence in the project's production/asset_credits.json.
