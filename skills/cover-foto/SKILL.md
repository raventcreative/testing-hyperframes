---
name: cover-foto
description: Navy cover from a photo/frame of Freddie (or a speaker) — full-bleed photo, navy gradients, grid behind subject, logo + eyebrow + 2-line headline + tagline, HD upscale + face restore when small. Use for "/cover-foto", "thumbnail dari foto ini".
---
# /cover-foto
Examples: `projects/adopsi5_thumb` (5 Level Adopsi AI: frame cleanup, hand rebuild, HD pass) and
`projects/struktur_thumb` ("1 Orang Bisa Mimpin 100 AI Agent?"). Pipeline `tools/build_photo.py`: Real-ESRGAN ×2 →
GFPGAN on the face (5 landmarks measured from a gridded zoom crop) → u2net matte → navy split-tone → canvas with the head
at y≈765 → `assets/bg.jpg` + `assets/gridmask.png`; `thumbnail/cover.html` + `render_cover.cjs` (HTTP server for the CSS mask).
Use the client's exact headline text; navy brand colours only (white text, cyan accent).
