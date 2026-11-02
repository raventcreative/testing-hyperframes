#!/usr/bin/env python3
"""Non-destructive prep of the genuine UI assets (originals in assets/ui stay untouched):
 - 01_claude_code_session_safe.png : private strings masked (2 session titles, repo name) with neutral bars in the
   same row colour; the rest of the real UI unchanged.
 - 02_claude_logo_3d_clean.png     : stray red/yellow edge pixels removed by edge colour decontamination (semi-transparent
   rim pixels take the colour of their nearest opaque neighbour) + 1 px alpha tidy. Shape/material/orange untouched.
 - 09_cursor_trim.png              : alpha-trimmed cursor (pixel art, scaled later with nearest-neighbour)."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
P = Path(__file__).resolve().parents[1]
U = P / "assets/ui"

im = Image.open(U / "01_claude_code_session.png").convert("RGBA")
a = np.asarray(im).copy()
def mask(x0, y0, x1, y1, bars):
    bg = np.median(a[y0 - 3:y0, x0:x1, :3].reshape(-1, 3), axis=0)
    a[y0:y1, x0:x1, :3] = bg
    for (bx0, by, bx1) in bars:
        a[by - 3:by + 3, bx0:bx1, :3] = (74, 74, 74)
mask(738, 482, 932, 498, [(742, 490, 905)])          # session title 1 (keep the orange 'Waiting')
mask(738, 513, 932, 529, [(742, 521, 880)])          # session title 2
mask(583, 907, 786, 928, [(588, 917, 760)])           # repo name in the composer bar
Image.fromarray(a).save(U / "01_claude_code_session_safe.png")

lg = np.asarray(Image.open(U / "02_claude_logo_3d.png").convert("RGBA")).astype(np.float64)
al = lg[..., 3]
opaque = al >= 250
rgb = lg[..., :3].copy(); known = opaque.copy()
for _ in range(6):                                     # propagate opaque colours outward into the soft rim
    s = np.zeros_like(rgb); n = np.zeros(al.shape)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            k = np.roll(np.roll(known, dy, 0), dx, 1)
            s += np.roll(np.roll(rgb, dy, 0), dx, 1) * k[..., None]; n += k
    grow = (~known) & (n > 0) & (al > 0)
    rgb[grow] = s[grow] / n[grow][:, None]; known |= grow
al2 = np.where(al < 24, 0, al)                         # drop near-invisible stray specks
out = np.dstack([rgb, al2]).clip(0, 255).astype(np.uint8)
Image.fromarray(out).save(U / "02_claude_logo_3d_clean.png")

cur = Image.open(U / "09_cursor_pointer.png").convert("RGBA")
cur.crop(cur.getchannel("A").getbbox()).save(U / "09_cursor_trim.png")
lb = Image.open(U / "02_claude_logo_3d_clean.png").getchannel("A").getbbox()
print("safe screenshot + clean logo (alpha bbox", lb, ") + cursor", Image.open(U / "09_cursor_trim.png").size)
