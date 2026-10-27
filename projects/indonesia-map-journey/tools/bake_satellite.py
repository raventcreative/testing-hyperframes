"""Cloud-free Sentinel-2 true-colour mosaics for each destination's close-up.

Source: Sentinel-2 L2A COGs on AWS Open Data (s3://sentinel-cogs, Element 84), Copernicus Sentinel data, free & open.
For each destination:
  AOI   = union of everything the camera sees while it is near the destination at >= 0.42x the hold zoom
  scenes= per MGRS tile, the 6 scenes with the lowest cloud + no-data score (selected months 2019-2024)
  pixel = median of the scenes whose SCL class is clear (cloud, cirrus, shadow, no-data masked)
  grid  = Web Mercator, aligned to the film's world coordinates, 1 px = 1 screen px at the hold zoom
Writes assets/sat/<id>.jpg and data/sat.js (world bounds per image).
Usage: python3 -I tools/bake_satellite.py [city ...]
"""
import concurrent.futures as cf, json, math, os, re, sys, urllib.request
import numpy as np
import mgrs, rasterio
from rasterio.warp import reproject, Resampling
from rasterio.transform import Affine
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUCKET = "https://sentinel-cogs.s3.us-west-2.amazonaws.com"
S, LON0, LAT0, W, H, R = 40.0, 88.0, 12.0, 1920, 1080, 6378137.0
M0 = math.log(math.tan(math.pi / 4 + math.radians(LAT0) / 2))
YEARS = range(2020, 2025)
MONTHS = {"medan": [1, 2, 3, 7], "makassar": [7, 8, 9, 10], "default": [7, 8, 9, 10]}
os.environ.setdefault("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")
os.environ.setdefault("CPL_VSIL_CURL_ALLOWED_EXTENSIONS", ".tif")


def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(url, timeout=60).read()
        except Exception:
            if i == 3:
                raise


def w2ll(X, Y):
    return X / S + LON0, math.degrees(2 * math.atan(math.exp(M0 - Y / (S * 180 / math.pi))) - math.pi / 2)


def world_to_merc(X, Y):  # world (base px) -> EPSG:3857 metres
    lon = X / S + LON0
    m = M0 - Y / (S * 180 / math.pi)
    return R * math.radians(lon), R * m


def list_prefixes(prefix):
    xml = get(f"{BUCKET}/?list-type=2&prefix={prefix}&delimiter=/").decode()
    return re.findall(r"<Prefix>([^<]+/)</Prefix>", xml)[1:]


def scene_meta(prefix):
    name = prefix.rstrip("/").split("/")[-1]
    try:
        d = json.loads(get(f"{BUCKET}/{prefix}{name}.json"))
    except Exception:
        return None
    p = d["properties"]
    score = p.get("eo:cloud_cover", 100) + 0.6 * p.get("s2:nodata_pixel_percentage", 0)
    return dict(prefix=prefix, name=name, score=score, cloud=p.get("eo:cloud_cover"), date=p["datetime"][:10])


def best_scenes(tile, months, n=40):
    zone, band, sq = tile[:2], tile[2], tile[3:]
    prefixes = [f"sentinel-s2-l2a-cogs/{int(zone)}/{band}/{sq}/{y}/{m}/" for y in YEARS for m in months]
    with cf.ThreadPoolExecutor(24) as ex:
        scenes = [s for lst in ex.map(list_prefixes, prefixes) for s in lst]
        metas = [m for m in ex.map(scene_meta, scenes) if m]
    metas.sort(key=lambda m: m["score"])
    out, dates = [], set()
    for m in metas:  # one scene per date (_0/_1 reprocessings are the same pass)
        if m["date"] not in dates:
            out.append(m); dates.add(m["date"])
    return out[:n]


def read_into(url, dst_shape, dst_transform, resampling, src_res_target=None):
    """Windowed, overview-aware read straight into the destination Web Mercator grid."""
    from rasterio.vrt import WarpedVRT
    from rasterio.windows import from_bounds
    hpx, wpx = dst_shape
    left, top = dst_transform.c, dst_transform.f
    right, bottom = left + dst_transform.a * wpx, top + dst_transform.e * hpx
    with rasterio.open("/vsicurl/" + url) as src:
        with WarpedVRT(src, crs="EPSG:3857", transform=dst_transform, width=wpx, height=hpx,
                       resampling=resampling, src_nodata=0, nodata=0) as vrt:
            return vrt.read()


def bake(city, frames, plan):
    c = next(x for x in plan["cities"] if x["id"] == city)
    kh = W / (c["span"] * S)
    # AOI from camera frames near this destination
    xs, ys = [], []
    for f, (ux, uy, w) in enumerate(frames):
        t = f / 30
        k = W / w
        cx = (c["lon"] - LON0) * S
        cy = (M0 - math.log(math.tan(math.pi / 4 + math.radians(c["lat"]) / 2))) * S * 180 / math.pi
        near = math.hypot(ux - cx, uy - cy) < 1.6 * c["span"] * S
        if k < 0.52 * kh or not near or not (c["start"] - 2.5 <= t <= c["start"] + c["dur"] + 2.5):
            continue
        xs += [ux - w / 2, ux + w / 2]; ys += [uy - H / 2 / k, uy + H / 2 / k]
    X0, X1, Y0, Y1 = min(xs), max(xs), min(ys), max(ys)
    mx = (X1 - X0) * 0.03; my = (Y1 - Y0) * 0.03
    X0, X1, Y0, Y1 = X0 - mx, X1 + mx, Y0 - my, Y1 + my
    wpx, hpx = int((X1 - X0) * kh), int((Y1 - Y0) * kh)
    scale = min(1.0, 5200 / max(wpx, hpx))  # cap the texture size
    wpx, hpx = int(wpx * scale), int(hpx * scale)
    mx0, my1 = world_to_merc(X0, Y0); mx1, my0 = world_to_merc(X1, Y1)
    tr = Affine((mx1 - mx0) / wpx, 0, mx0, 0, -(my1 - my0) / hpx, my1)
    mpp = (mx1 - mx0) / wpx
    lo0, la1 = w2ll(X0, Y0); lo1, la0 = w2ll(X1, Y1)
    tiles = set()
    m = mgrs.MGRS()
    for lo in np.linspace(lo0, lo1, 14):
        for la in np.linspace(la0, la1, 10):
            tiles.add(m.toMGRS(la, lo, MGRSPrecision=0))
    print(city, f"AOI lon {lo0:.3f}..{lo1:.3f} lat {la0:.3f}..{la1:.3f}", f"{wpx}x{hpx}px", f"{mpp:.1f} m/px", sorted(tiles), flush=True)
    out = np.zeros((hpx, wpx, 3), np.float32); have = np.zeros((hpx, wpx), bool)
    used = []
    months = MONTHS.get(city, MONTHS["default"])
    with cf.ThreadPoolExecutor(6) as ex:
        pools = dict(zip(sorted(tiles), ex.map(lambda tl: best_scenes(tl, months), sorted(tiles))))
    from collections import Counter
    freq = Counter(m["date"] for p in pools.values() for m in p if m["cloud"] < 20)
    bests = {}
    for tl, p in pools.items():
        bests[tl] = sorted(p, key=lambda m: m["score"] - 6.0 * (freq[m["date"]] - 1))[:6]

    def composite(tile):
        best = bests[tile]
        scls, keep = [], []
        for sc in best:
            try:
                scl = read_into(f"{BUCKET}/{sc['prefix']}SCL.tif", (hpx, wpx), tr, Resampling.nearest)[0]
            except Exception as e:
                print("  skip", sc["name"], e, flush=True); continue
            if scl.any():
                scls.append(scl); keep.append(sc)
        if not scls:
            return None
        anyd = np.any(np.stack([x > 0 for x in scls]), 0)
        ys, xs = np.nonzero(anyd)
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        sub_tr = tr * Affine.translation(x0, y0)
        stack, valid, info = [], [], []
        for sc, scl in zip(keep, scls):
            try:
                tci = read_into(f"{BUCKET}/{sc['prefix']}TCI.tif", (y1 - y0, x1 - x0), sub_tr, Resampling.bilinear)
            except Exception as e:
                print("  skip", sc["name"], e, flush=True); continue
            data = tci.transpose(1, 2, 0)
            stack.append(data); valid.append(np.isin(scl[y0:y1, x0:x1], [2, 4, 5, 6, 11]) & (data.sum(-1) > 0))
            info.append(dict(tile=tile, scene=sc["name"], date=sc["date"], cloud=round(sc["cloud"], 1)))
        del scls
        st = np.stack(stack).astype(np.float32); va = np.stack(valid)
        cov = (st.sum(-1) > 0).any(0)
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            med = np.nanmedian(np.where(va[..., None], st, np.nan), axis=0)
        fallback = st[0]
        for i in range(1, len(st)):
            fallback = np.where((fallback.sum(-1) > 0)[..., None], fallback, st[i])
        img = np.where(np.isnan(med), fallback, med).astype(np.float32)
        del st, va, med
        full = np.zeros((hpx, wpx), bool); full[y0:y1, x0:x1] = cov
        print("  tile", tile, "scenes", [x["date"] for x in info], "window", (int(y1 - y0), int(x1 - x0)), flush=True)
        return (int(y0), int(y1), int(x0), int(x1)), full, img, info

    with cf.ThreadPoolExecutor(2) as ex:
        results = [r for r in ex.map(composite, sorted(tiles)) if r is not None]
    # place the tile nearest the destination first, then colour-match each next tile to what is already placed
    cxp = (c["lon"] - lo0) / (lo1 - lo0) * wpx; cyp = (la1 - c["lat"]) / (la1 - la0) * hpx
    def dist(r):
        ys, xs = np.nonzero(r[0][::8, ::8]); return np.hypot(xs.mean() * 8 - cxp, ys.mean() * 8 - cyp) if len(xs) else 1e9
    results.sort(key=lambda r: dist((r[1],)))
    for (y0, y1, x0, x1), cov, tile_img, info in results:
        covc = cov[y0:y1, x0:x1]; havec = have[y0:y1, x0:x1]; outc = out[y0:y1, x0:x1]
        ov = covc & havec
        if ov.sum() > 2000:
            a = tile_img[ov]; b = outc[ov]
            ma, sa = a.mean(0), a.std(0) + 1e-3; mb, sb = b.mean(0), b.std(0) + 1e-3
            g = np.clip(sb / sa, 0.7, 1.4)
            tile_img = np.clip((tile_img - ma) * g + mb, 0, 255)
        from scipy.ndimage import distance_transform_edt
        wgt = np.clip(distance_transform_edt(covc) / 70.0, 0, 1)[..., None]
        blend = covc & havec
        outc[blend] = (outc * (1 - wgt) + tile_img * wgt)[blend]
        put = covc & ~havec
        outc[put] = tile_img[put]; havec |= put
        used += info
    # fill swath-edge holes from other passes in each tile's candidate pool (colour-matched on a ring around the hole)
    from scipy.ndimage import binary_dilation
    for tl in sorted(tiles):
        if have.all():
            break
        for sc in [x for x in pools.get(tl, []) if x not in bests[tl]]:
            holes = ~have
            if holes.sum() < 200:
                break
            try:
                scl = read_into(f"{BUCKET}/{sc['prefix']}SCL.tif", (hpx, wpx), tr, Resampling.nearest)[0]
            except Exception:
                continue
            m = holes & np.isin(scl, [2, 4, 5, 6, 11])
            if m.sum() < 200:
                continue
            ys, xs = np.nonzero(m)
            y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
            tci = read_into(f"{BUCKET}/{sc['prefix']}TCI.tif", (y1 - y0, x1 - x0), tr * Affine.translation(x0, y0), Resampling.bilinear)
            img = tci.transpose(1, 2, 0).astype(np.float32)
            mc = m[y0:y1, x0:x1] & (img.sum(-1) > 0)
            ring = binary_dilation(mc, iterations=25) & have[y0:y1, x0:x1] & (img.sum(-1) > 0)
            if ring.sum() > 500:
                a = img[ring]; b = out[y0:y1, x0:x1][ring]
                img = np.clip((img - a.mean(0)) * np.clip((b.std(0) + 1e-3) / (a.std(0) + 1e-3), 0.7, 1.4) + b.mean(0), 0, 255)
            out[y0:y1, x0:x1][mc] = img[mc]; have[y0:y1, x0:x1] |= mc
            used.append(dict(tile=tl, scene=sc["name"], date=sc["date"], cloud=round(sc["cloud"], 1), role="hole-fill"))
            print("  hole-fill", tl, sc["date"], int(mc.sum()), "px", flush=True)
    # gentle grade: percentile stretch + slight gamma lift (tropical haze)
    px = out[have]
    lo, hi = np.percentile(px, 0.5, axis=0), np.percentile(px, 99.7, axis=0)
    g = np.clip((out - lo) / (hi - lo), 0, 1) ** 0.88
    lum = g.mean(-1, keepdims=True)
    g = np.clip(lum + (g - lum) * 1.12, 0, 1)
    img = (g * 255).astype(np.uint8)
    # alpha: holes stay transparent (relief shows through), feathered over ~6 px
    from PIL import ImageFilter
    alpha = Image.fromarray((have * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(3))
    os.makedirs(os.path.join(ROOT, "assets", "sat"), exist_ok=True)
    rgba = Image.fromarray(img).convert("RGBA"); rgba.putalpha(alpha)
    rgba.save(os.path.join(ROOT, "assets", "sat", f"{city}.webp"), "WEBP", quality=86, method=4)
    return dict(id=city, file=f"assets/sat/{city}.webp", world=[X0, Y0, X1, Y1], px=[wpx, hpx], kHold=kh,
                coverage=round(float(have.mean()), 4), scenes=used)


if __name__ == "__main__":
    plan = json.load(open(os.path.join(ROOT, "data", "plan.json")))
    frames = json.load(open(os.path.join(ROOT, "data", "camera_frames.json")))
    ids = sys.argv[1:] or [c["id"] for c in plan["cities"]]
    man_fn = os.path.join(ROOT, "data", "sat.json")
    man = json.load(open(man_fn)) if os.path.exists(man_fn) else {}
    for cid in ids:
        man[cid] = bake(cid, frames, plan)
        print(cid, "coverage", man[cid]["coverage"], flush=True)
        json.dump(man, open(man_fn, "w"), indent=1)
    with open(os.path.join(ROOT, "data", "sat.js"), "w") as fh:
        fh.write("/* generated by tools/bake_satellite.py */\nwindow.__SAT=" + json.dumps({k: {kk: v[kk] for kk in ("file", "world", "px", "kHold")} for k, v in man.items()}) + ";\n")
