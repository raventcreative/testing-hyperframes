---
name: cover-testimoni
description: White-theme testimonial cover "TESTIMONI PESERTA — Kata Mereka Setelah Belajar AI" with the participant's photo (high-key room, sharp subject, grid behind), name in navy + role pill. Use for "/cover-testimoni", "thumbnail testi <nama>".
---
# /cover-testimoni
Template `aipreneur-reels-studio/templates/thumbnail/cover_testimoni_white.html` (set `#nm` = name, `#rl` = role · city).
Background: `scripts/thumb/testi_build_bg.py` (photo + the client's cut-out as matte) or
`scripts/thumb/testi_build_from_screenshot.py` (small screenshot: LaMa removes captions/watermark → Real-ESRGAN ×4 →
GFPGAN face → u2net matte). Models: lama_fp32.onnx, real_esrgan_x2.onnx, gfpgan_1.4.onnx, u2net_human_seg.onnx.
Name tag: navy #0B1B4D, name ≤ 820 px wide, left 150 px, top ≈1360 (above the Reels UI). Examples: `projects/testi_thumb`
(Ibu Eka), `projects/testi_debi` (Debi Kurniawan). Render via `thumbnail/render_cover.cjs` with HTTP=<port>, plus DSF=2 HD.
