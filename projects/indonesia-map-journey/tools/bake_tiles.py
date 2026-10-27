"""Bake a shaded-relief basemap pyramid along the camera path.

Source: AWS Terrain Tiles (Terrarium encoding; SRTM, GMTED2010, ETOPO1 ...), s3://elevation-tiles-prod.
For every frame of data/camera_frames.json the visible Web Mercator tiles at the frame's level
(+1 tile margin) are baked to assets/tiles/{z}/{x}/{y}.webp:
  land  = hypsometric tint x hillshade (sun from the north-west), exaggeration falls with zoom
  ocean = bathymetric tint x faint seafloor shade
Hillshade is computed on a 3x3 neighbourhood mosaic, so tiles join without seams.
Usage: python3 -I tools/bake_tiles.py [--force]
"""
import concurrent.futures as cf, io, json, math, os, sys, threading, urllib.request
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "terrarium")
OUT = os.path.join(ROOT, "assets", "tiles")
URL = "https://elevation-tiles-prod.s3.amazonaws.com/terrarium/{z}/{x}/{y}.png"
S, LON0, LAT0, W, H = 40.0, 88.0, 12.0, 1920, 1080
M0 = math.log(math.tan(math.pi / 4 + math.radians(LAT0) / 2))
FORCE = "--force" in sys.argv

LAND = [(0, (104, 146, 86)), (60, (118, 156, 92)), (250, (140, 166, 100)), (600, (166, 172, 112)),
        (1100, (176, 162, 116)), (1800, (162, 140, 110)), (2700, (150, 134, 122)), (3800, (205, 200, 196)), (5000, (236, 236, 236))]
SEA = [(0, (126, 200, 214)), (-25, (100, 182, 208)), (-120, (74, 152, 196)), (-400, (54, 120, 176)),
       (-1500, (40, 94, 154)), (-4000, (27, 66, 120)), (-7000, (18, 46, 92))]
EXAG = {5: 14, 6: 11, 7: 8, 8: 6, 9: 4.2, 10: 3.0, 11: 2.2}


def level_for(k):
    ppd = S * k
    return max(4, min(10, round(math.log2(ppd * 360 / 256))))


def w2ll(X, Y):
    lon = X / S + LON0
    m = M0 - Y / (S * 180 / math.pi)
    return lon, math.degrees(2 * math.atan(math.exp(m)) - math.pi / 2)


def ll2t(lon, lat, z):
    n = 2 ** z
    return (lon + 180) / 360 * n, (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n


def needed():
    cams = json.load(open(os.path.join(ROOT, "data", "camera_frames.json")))
    need = set()
    for ux, uy, w in cams:
        k = W / w
        z = level_for(k)
        l0, a1 = w2ll(ux - w / 2, uy - (H / 2) / k)
        l1, a0 = w2ll(ux + w / 2, uy + (H / 2) / k)
        x0, y0 = ll2t(l0, a1, z); x1, y1 = ll2t(l1, a0, z)
        for tx in range(int(x0) - 1, int(x1) + 2):
            for ty in range(int(y0) - 1, int(y1) + 2):
                if 0 <= ty < 2 ** z:
                    need.add((z, tx % (2 ** z), ty))
    return sorted(need)


def fetch(z, x, y):
    n = 2 ** z
    x %= n
    if y < 0 or y >= n:
        return None
    fn = os.path.join(CACHE, str(z), str(x), f"{y}.png")
    if os.path.exists(fn):
        try:
            Image.open(fn).verify()
        except Exception:
            os.remove(fn)
    if not os.path.exists(fn):
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        for attempt in range(4):
            try:
                data = urllib.request.urlopen(URL.format(z=z, x=x, y=y), timeout=60).read()
                break
            except Exception:
                if attempt == 3:
                    raise
        tmp = f"{fn}.{os.getpid()}.{threading.get_ident()}.tmp"
        open(tmp, "wb").write(data)
        os.replace(tmp, fn)  # atomic: concurrent workers never read a half-written tile
    return fn


def elev(fn):
    a = np.asarray(Image.open(fn).convert("RGB")).astype(np.float32)
    return a[..., 0] * 256 + a[..., 1] + a[..., 2] / 256 - 32768


def ramp(e, stops):
    xs = [s[0] for s in stops]
    rev = xs[0] > xs[-1]
    if rev:
        stops = stops[::-1]; xs = xs[::-1]
    out = np.zeros(e.shape + (3,), np.float32)
    for c in range(3):
        out[..., c] = np.interp(e, xs, [s[1][c] for s in stops])
    return out


def bake(z, x, y):
    out = os.path.join(OUT, str(z), str(x), f"{y}.webp")
    if os.path.exists(out) and not FORCE:
        return out
    mos = np.zeros((768, 768), np.float32)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            fn = fetch(z, x + dx, y + dy)
            if fn:
                mos[(dy + 1) * 256:(dy + 2) * 256, (dx + 1) * 256:(dx + 2) * 256] = elev(fn)
            else:  # beyond the poles: replicate the centre tile
                mos[(dy + 1) * 256:(dy + 2) * 256, (dx + 1) * 256:(dx + 2) * 256] = elev(fetch(z, x, y))
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * (y + 0.5) / 2 ** z))))
    mpp = 156543.03 * math.cos(math.radians(lat)) / 2 ** z
    ex = EXAG.get(z, 3)
    gy, gx = np.gradient(mos * ex, mpp)
    # sun from the north-west, 45 deg altitude; Lambert, normalised so flat ground = 1
    az, alt = math.radians(315), math.radians(45)
    lx, ly, lz = math.cos(alt) * math.sin(az), math.cos(alt) * math.cos(az), math.sin(alt)
    nz = 1 / np.sqrt(gx * gx + gy * gy + 1)
    shade = (-gx * nz * lx + gy * nz * ly + nz * lz) / lz  # image y grows southward
    e = mos[256:512, 256:512]; sh = shade[256:512, 256:512]
    land = ramp(np.clip(e, 0, 6000), LAND) * np.clip(0.42 + 0.58 * sh, 0.25, 1.35)[..., None]
    sea = ramp(np.clip(e, -9000, 0), SEA) * np.clip(0.80 + 0.20 * sh, 0.6, 1.15)[..., None]
    a = np.clip((e - 0.0) / 3.0 + 0.5, 0, 1)[..., None]  # ~1 px soft shoreline
    rgb = np.clip(sea * (1 - a) + land * a, 0, 255).astype(np.uint8)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    Image.fromarray(rgb).save(out, "WEBP", quality=84, method=4)
    return out


if __name__ == "__main__":
    tiles = needed()
    print("tiles", len(tiles), {z: sum(1 for t in tiles if t[0] == z) for z in sorted({t[0] for t in tiles})})
    with cf.ThreadPoolExecutor(16) as ex:
        fut = {ex.submit(bake, *t): t for t in tiles}
        for i, f in enumerate(cf.as_completed(fut)):
            f.result()
            if i % 200 == 0:
                print("baked", i, flush=True)
    keys = [f"{z}/{x}/{y}" for z, x, y in tiles]
    with open(os.path.join(ROOT, "data", "tiles.js"), "w") as fh:
        fh.write("/* generated by tools/bake_tiles.py */\nwindow.__TILES=" + json.dumps(keys, separators=(",", ":")) + ";\n")
    total = sum(os.path.getsize(os.path.join(OUT, k + ".webp")) for k in keys)
    print("done", len(keys), "tiles", round(total / 1e6, 1), "MB")
