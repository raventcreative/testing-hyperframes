"""Stitch the scrolling screen recording into one tall page image.
Only the page area is used (browser chrome with private tabs is cut away): x 360-1560, y 152-1032 (below the site's fixed navbar);
the navbar is taken once from the first frame. Scroll offset between samples = best vertical shift (coarse at 1/4, refined at full res).
Run: python3 -I tools/stitch_page.py <project>  -> assets/web/page_full.png (+ page_meta.json)"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image
P = Path(sys.argv[1]).resolve(); SRC = P / "assets/web/aipreneur_screenrec.mp4"
X0, X1, Y0, Y1, NAV0 = 360, 1560, 152, 1032, 88
W, H = X1 - X0, Y1 - Y0
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(SRC), "-vf", f"fps=12,crop={W}:{(Y1 - NAV0)}:{X0}:{NAV0}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
FH = Y1 - NAV0
fr = np.frombuffer(raw, np.uint8).reshape(-1, FH, W, 3)
nav = fr[0, :Y0 - NAV0].copy(); body = fr[:, Y0 - NAV0:]
g = body.mean(axis=3)
def shift(a, b, lo, hi, step=1):
    best, bs, hh = 1e18, 0, a.shape[0]
    for s in range(lo, hi + 1, step):
        if s >= hh - hh // 6: break
        d = np.abs(a[s:, :] - b[:hh - s, :]).mean()
        if d < best: best, bs = d, s
    return bs, best
offs = [0]; tot = 0
for i in range(1, len(g)):
    a = g[i - 1][::4, ::4]; b = g[i][::4, ::4]
    s4, _ = shift(a, b, 0, 180)
    s, err = shift(g[i - 1], g[i], max(0, s4 * 4 - 6), s4 * 4 + 6)
    tot += s; offs.append(tot)
total_h = tot + H
canvas = np.zeros((total_h, W, 3), np.uint8)
for i in range(len(body)):
    y = offs[i]
    if i == 0: canvas[0:H] = body[0]; continue
    new = offs[i] - offs[i - 1]
    if new <= 0: continue
    canvas[y + H - new: y + H] = body[i][H - new:]
page = np.concatenate([nav, canvas], axis=0)
Image.fromarray(page).save(P / "assets/web/page_full.png")
(P / "assets/web/page_meta.json").write_text(json.dumps({"width": W, "height": int(page.shape[0]), "nav_h": int(Y0 - NAV0), "frames": len(body)}))
print("page", page.shape, "frames", len(body))
