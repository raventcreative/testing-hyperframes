"""Fill remaining transparent holes in a baked Sentinel-2 mosaic using scenes from any month (2019-2024).
Usage: python3 -I tools/patch_holes.py <city> [<city> ...]
"""
import json, math, os, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bake_satellite as B
from rasterio.transform import Affine
from rasterio.warp import Resampling
from scipy.ndimage import binary_dilation
import concurrent.futures as cf
import mgrs

ROOT = B.ROOT
man = json.load(open(os.path.join(ROOT, "data", "sat.json")))
args = sys.argv[1:]
WIN = None
if "--window" in args:  # lon0,lat0,lon1,lat1: only patch holes inside this box
    i = args.index("--window"); WIN = [float(v) for v in args[i + 1].split(",")]; del args[i:i + 2]
for city in args:
    e = man[city]
    im = Image.open(os.path.join(ROOT, e["file"])).convert("RGBA")
    arr = np.asarray(im).copy()
    rgb = arr[..., :3].astype(np.float32); alpha = arr[..., 3]
    hpx, wpx = alpha.shape
    X0, Y0, X1, Y1 = e["world"]
    mx0, my1 = B.world_to_merc(X0, Y0); mx1, my0 = B.world_to_merc(X1, Y1)
    tr = Affine((mx1 - mx0) / wpx, 0, mx0, 0, -(my1 - my0) / hpx, my1)
    holes = alpha < 250
    if WIN:
        wx0 = int((B.world_to_merc(*[(WIN[0] - B.LON0) * B.S, 0])[0] - mx0) / tr.a); wx1 = int((B.world_to_merc(*[(WIN[2] - B.LON0) * B.S, 0])[0] - mx0) / tr.a)
        M = lambda la: math.log(math.tan(math.pi / 4 + math.radians(la) / 2))
        wy0 = int((my1 - B.R * M(WIN[3])) / -tr.e); wy1 = int((my1 - B.R * M(WIN[1])) / -tr.e)
        keep = np.zeros_like(holes); keep[max(0, wy0):max(0, wy1), max(0, wx0):max(0, wx1)] = True
        outside = holes & ~keep
        holes = holes & keep
    else:
        outside = np.zeros_like(holes)
    ys, xs = np.nonzero(holes)
    if not len(xs):
        print(city, "no holes"); continue
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    lo0, la1 = B.w2ll(X0 + (X1 - X0) * x0 / wpx, Y0 + (Y1 - Y0) * y0 / hpx)
    lo1, la0 = B.w2ll(X0 + (X1 - X0) * x1 / wpx, Y0 + (Y1 - Y0) * y1 / hpx)
    m = mgrs.MGRS()
    tiles = {m.toMGRS(la, lo, MGRSPrecision=0) for lo in np.linspace(lo0, lo1, 6) for la in np.linspace(la0, la1, 6)}
    print(city, "hole px", int(holes.sum()), "tiles", sorted(tiles), flush=True)
    B.YEARS = range(2019, 2025)
    cands = []
    for t in sorted(tiles):
        cands += B.best_scenes(t, list(range(1, 13)), n=200)
    cands.sort(key=lambda c: c["cloud"])
    sub_tr = tr * Affine.translation(x0, y0)
    hsub = holes[y0:y1, x0:x1]
    for sc in cands:
        if hsub.sum() < 50:
            break
        try:
            scl = B.read_into(f"{B.BUCKET}/{sc['prefix']}SCL.tif", (y1 - y0, x1 - x0), sub_tr, Resampling.nearest)[0]
        except Exception:
            continue
        mk = hsub & np.isin(scl, [2, 4, 5, 6, 11])
        if mk.sum() < 50:
            continue
        tci = B.read_into(f"{B.BUCKET}/{sc['prefix']}TCI.tif", (y1 - y0, x1 - x0), sub_tr, Resampling.bilinear).transpose(1, 2, 0).astype(np.float32)
        mk &= tci.sum(-1) > 0
        ring = binary_dilation(mk, iterations=30) & ~hsub & (tci.sum(-1) > 0)
        sub = rgb[y0:y1, x0:x1]
        if ring.sum() > 300:  # match the grade of the finished mosaic around the patch
            a = tci[ring]; b = sub[ring]
            tci = np.clip((tci - a.mean(0)) * np.clip((b.std(0) + 1e-3) / (a.std(0) + 1e-3), 0.6, 1.6) + b.mean(0), 0, 255)
        sub[mk] = tci[mk]; hsub[mk] = False
        print("  filled", sc["date"], sc["name"], int(mk.sum()), "left", int(hsub.sum()), flush=True)
        e.setdefault("scenes", []).append(dict(scene=sc["name"], date=sc["date"], cloud=round(sc["cloud"], 1), role="hole-patch"))
    holes[y0:y1, x0:x1] = hsub
    holes |= outside
    a = Image.fromarray((~holes * 255).astype(np.uint8))
    from PIL import ImageFilter
    a = a.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(3))
    out = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA"); out.putalpha(a)
    out.save(os.path.join(ROOT, e["file"]), "WEBP", quality=86, method=4)
    e["coverage"] = round(float(1 - holes.mean()), 4)
    print(city, "coverage", e["coverage"], flush=True)
json.dump(man, open(os.path.join(ROOT, "data", "sat.json"), "w"), indent=1)
