#!/usr/bin/env python3
"""Plot per-document screen speed (px/frame) and camera distance from a *_motion.json probe.
Flags velocity discontinuities (|dv| > threshold between consecutive frames)."""
import json, sys, math
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src)); rows = d['rows']; fps = d['fps']
names = sorted({k for r in rows for k in r if k != 'cam'})
cols = {'receipt': (254, 209, 17), 'statement': (120, 160, 255), 'statementP2': (180, 180, 200), 'report': (255, 120, 120)}
W, H, P = 1400, 520, 50
im = Image.new('RGB', (W, H), (20, 24, 44)); g = ImageDraw.Draw(im)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
n = len(rows); vmax = 1
speeds = {}
for nm in names:
    sp = [None] * n
    for i in range(1, n):
        a, b = rows[i - 1].get(nm), rows[i].get(nm)
        if a and b: sp[i] = math.hypot(b[0] - a[0], b[1] - a[1])
    speeds[nm] = sp
    vmax = max(vmax, max([v for v in sp if v is not None] or [0]))
vmax = min(vmax, 80)
X = lambda i: P + (W - 2 * P) * i / (n - 1)
Y = lambda v: H - P - (H - 2 * P) * min(v, vmax) / vmax
for s in range(0, int(n / fps) + 1):
    g.line([(X(s * fps), P), (X(s * fps), H - P)], fill=(45, 50, 80)); g.text((X(s * fps) - 4, H - P + 6), f'{s}s', fill=(200, 200, 220), font=font)
for v in range(0, int(vmax) + 1, 10):
    g.line([(P, Y(v)), (W - P, Y(v))], fill=(40, 44, 70)); g.text((8, Y(v) - 7), f'{v}', fill=(160, 160, 190), font=font)
report = []
for nm in names:
    sp = speeds[nm]; c = cols.get(nm, (255, 255, 255)); prev = None
    for i in range(1, n):
        if sp[i] is None: prev = None; continue
        if prev is not None: g.line([(X(i - 1), Y(prev)), (X(i), Y(sp[i]))], fill=c, width=2)
        if prev is not None and abs(sp[i] - prev) > 3.0: report.append(f'{nm} jump {prev:.1f}->{sp[i]:.1f} px/f at {i / fps:.2f}s')
        prev = sp[i]
    g.text((W - 260, 14 + 16 * names.index(nm)), f'— {nm}', fill=c, font=font)
cam = [math.dist(r['cam'], [0, 0, 0]) for r in rows]
lo, hi = min(cam), max(cam)
for i in range(1, n):
    g.line([(X(i - 1), H - P - 60 * (cam[i - 1] - lo) / max(1e-6, hi - lo) - 10), (X(i), H - P - 60 * (cam[i] - lo) / max(1e-6, hi - lo) - 10)], fill=(90, 255, 160), width=1)
g.text((W - 260, 14 + 16 * len(names)), f'— camera dist {lo:.2f}..{hi:.2f}', fill=(90, 255, 160), font=font)
g.text((P, 12), f'{src.split("/")[-1]}  screen speed px/frame (max {vmax:.0f})', fill=(255, 255, 255), font=font)
im.save(out)
print('\n'.join(report) if report else 'no velocity discontinuities > 3 px/frame')
