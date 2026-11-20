---
name: video-carousel
description: Remake of a video carousel for IG (e.g. "15 Animasi Landing Page") — N slides 1080×1350, silent 6 s seamless loops (cover 8 s), one config file drives all slides, DM prompt pack + caption. Use for "/video-carousel", "remake carousel", carousel tanpa VO.
---
# /video-carousel
Reference: `projects/aip_carousel1/` — `carousel.json` (all copy), `effects/<id>/` (one effect per slide), `vendor/` shared
kit, `tools/build.py` (generates slides + manifest + DM), `tools/render.sh <n>` (one slide at a time, ffprobe check),
`tools/stills.sh`, `tools/loopcheck.sh`. Outputs `out/CAROUSEL_AIP_<TOPIC>_SLIDE_01..NN.mp4` + `out/stills/*.png`.
Rules: background as the client asks (white for that one), Indonesian copy, no VO (client: "cuman remake carousel"),
ATM (own slide copy), never claim untested things (changed "Prompt teruji" → "Prompt siap pakai").
Deliver a zip: `video/` (all MP4s in order) + `preview_png/` + `DM_<KEYWORD>.md` + `CAPTION.md`.
