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
html-demo (MengTo, MIT — live HTML app demos for web pages), product-launch-film (15 s 2D launch film, landscape), landing-flythrough-3d (3D fly-through of a website), beat-promo-film (20 s minimal promo on a beat grid with real clips), design-taste-frontend (Taste Skill: professional websites / landing pages), business-explainer-30s (30 s 5-scene business explainer), throughline-explainer (30 s explainer with one transforming through-line object), feed-carousel (static IG feed/carousel 1080×1350, navy/white, Poppins Bold + Inter). Keep both copies in sync when a skill changes.
**Technique bank:** external skills/briefs the client shares are other people's products — keep only the technique and
apply it to the client's own videos (skills/aipreneur-reels-studio/references/technique_bank.md). Read it for every new video.
**Real screen recordings (client rule, 2026-11-20):** when a video talks about a website or social media (Instagram,
TikTok, WhatsApp, a web page…), ask the client to screen-record HIS OWN account / HIS OWN website and use that footage
(in a phone/browser frame, cropped and zoomed) instead of rebuilt or mock UI. Ask at the start of the job (say exactly what
to record: which screens, how long, vertical 9:16), and keep building the rest meanwhile.

**Stored recordings = use them automatically (client, 2026-11-21):** the client's recordings live in `brand/rec/` (local only, gitignored; see brand/rec/README.md). Whenever a reel's topic matches one (his IG, his website, Claude/Claude Code…), USE IT in that reel without asking and put it in the agent brief — never fall back to mock UI when a matching recording exists. Only ask him to record something new when no stored recording fits.
