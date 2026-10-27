#!/usr/bin/env python3
"""Derivatives of the supplied brand files (originals untouched).
- background_original.png 1080x1350 -> bg_1080x1920.png: original pixels kept 1:1 in the middle, 285 px mirrored
  extension above and below (no stretch, no recolour).
- aipreneur_logo_original.png -> logo_trim.png: crop to the alpha bounding box + 4 px pad (pixels untouched)."""
from pathlib import Path
from PIL import Image, ImageOps
P = Path(__file__).resolve().parents[1] / "assets/brand"
bg = Image.open(P / "background_original.png").convert("RGB")
W, H = bg.size
pad = (1920 - H) // 2
out = Image.new("RGB", (W, 1920))
out.paste(bg, (0, pad))
out.paste(ImageOps.flip(bg.crop((0, 0, W, pad))), (0, 0))
rest = 1920 - pad - H
out.paste(ImageOps.flip(bg.crop((0, H - rest, W, H))), (0, pad + H))
out.save(P / "bg_1080x1920.png")
lg = Image.open(P / "aipreneur_logo_original.png")
x0, y0, x1, y1 = lg.split()[-1].getbbox()
lg.crop((x0 - 4, y0 - 4, x1 + 4, y1 + 4)).save(P / "logo_trim.png")
print("bg", out.size, "pad", pad, "logo", (x1 - x0 + 8, y1 - y0 + 8))
