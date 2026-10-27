"""Keep satellite pixels only over land + a coastal band; open sea falls back to the relief bathymetry.
Uses Natural Earth 10m land rings (assets/maps/geo.js), dilated by --coast px, feathered.
Usage: python3 -I tools/mask_sea.py <city> [--coast 10]
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
coast = 10
only = None
if "--only" in args:  # rasterise this destination's official boundary instead of all land
    i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
if "--coast" in args:
    i = args.index("--coast"); coast = int(args[i + 1]); del args[i:i + 2]
src = open(os.path.join(ROOT, "assets", "maps", "geo.js")).read()
G = json.loads(src[src.index("=") + 1:src.rindex(";")])
man = json.load(open(os.path.join(ROOT, "data", "sat.json")))
for city in args:
    e = man[city]
    im = Image.open(os.path.join(ROOT, e["file"])).convert("RGBA")
    w, h = im.size
    X0, Y0, X1, Y1 = e["world"]
    m = Image.new("L", (w, h), 0); d = ImageDraw.Draw(m)
    rings = G["idn"] + G["other"]
    if only:
        bs = open(os.path.join(ROOT, "assets", "maps", "bounds.js")).read()
        rings = json.loads(bs[bs.index("=") + 1:bs.rindex(";")])[only]["outer"]
    for ring in rings:
        pts = [((ring[i] / G["Q"] - X0) / (X1 - X0) * w, (ring[i + 1] / G["Q"] - Y0) / (Y1 - Y0) * h) for i in range(0, len(ring), 2)]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if max(xs) < 0 or min(xs) > w or max(ys) < 0 or min(ys) > h:
            continue
        d.polygon(pts, fill=255)
    m = m.filter(ImageFilter.MaxFilter(2 * coast + 1)).filter(ImageFilter.GaussianBlur(coast * 0.8))
    a = np.minimum(np.asarray(im)[..., 3], np.asarray(m))
    im.putalpha(Image.fromarray(a.astype(np.uint8)))
    im.save(os.path.join(ROOT, e["file"]), "WEBP", quality=86, method=4)
    print(city, "land+coast alpha", round(float((a > 128).mean()), 3))
