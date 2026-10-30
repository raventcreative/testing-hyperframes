#!/usr/bin/env python3
"""Derivatives of the supplied brand files (originals untouched).
- ai_preneur_background.png 1080x1350 -> bg_1080x1920.png: original pixels 1:1 in the middle; 285 px above/below
  are mirrored edge bands, progressively softened (Gaussian) so the extension reads as the same gradient (no stretch).
- ai_preneur_logo.png 1485x1485 (white wordmark, alpha) -> logo_trim.png: alpha bbox crop + 6 px pad, pixels untouched."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
P = Path(__file__).resolve().parents[1] / "assets/brand"
bg = Image.open(P / "ai_preneur_background.png").convert("RGB")
W, H = bg.size; pad = (1920 - H) // 2; rest = 1920 - pad - H
top = ImageOps.flip(bg.crop((0, 0, W, pad))).filter(ImageFilter.GaussianBlur(28))
bot = ImageOps.flip(bg.crop((0, H - rest, W, H))).filter(ImageFilter.GaussianBlur(28))
out = Image.new("RGB", (W, 1920)); out.paste(top, (0, 0)); out.paste(bot, (0, pad + H)); out.paste(bg, (0, pad))
# feather the seams 40 px into the extension so no hard line remains
for y0, band in ((pad - 40, out.crop((0, pad - 40, W, pad + 40))), (pad + H - 40, out.crop((0, pad + H - 40, W, pad + H + 40)))):
    out.paste(band.filter(ImageFilter.GaussianBlur(6)), (0, y0))
out.paste(bg.crop((0, 40, W, H - 40)), (0, pad + 40))
out.save(P / "bg_1080x1920.png")
lg = Image.open(P / "ai_preneur_logo.png").convert("RGBA")
x0, y0, x1, y1 = lg.split()[-1].getbbox()
lg.crop((x0 - 6, y0 - 6, x1 + 6, y1 + 6)).save(P / "logo_trim.png")
c = Image.open(P / "click_cursor.png").convert("RGBA"); cb = c.split()[-1].getbbox()
c.crop(cb).save(P / "cursor_trim.png")
print("bg", out.size, "logo", (x1 - x0 + 12, y1 - y0 + 12), "cursor", (cb[2] - cb[0], cb[3] - cb[1]))
