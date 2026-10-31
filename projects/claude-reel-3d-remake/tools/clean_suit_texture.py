#!/usr/bin/env python3
"""Repair the 'frayed fibre' fringe on the mascot's jacket/shirt (texture-level, non-destructive).
The Tripo atlas packs UV charts edge to edge; the bake left foreign (hair/skin) texels in a thin band along every
chart border, which shows as dark fibres on the jacket hem, pocket flaps and cuffs.
For every UV chart that is jacket (dark, desaturated) or shirt/cuff (bright, desaturated), the outer EDGE px band of
the chart is replaced by colour propagated inward-out from the chart's own interior. Skin, hair, eyes untouched.
In:  projects/opus55-reel/assets/mascot3d/mascot_jas3_rigged.glb (never modified)
Out: assets/mascot3d/mascot_jas3_clean.glb  +  qa/suit_texture_before_after.jpg"""
import json, struct, io
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

P = Path(__file__).resolve().parents[1]
SRC = P.parents[0] / "opus55-reel/assets/mascot3d/mascot_jas3_rigged.glb"
OUT = P / "assets/mascot3d/mascot_jas3_clean.glb"
EDGE = 5

raw = SRC.read_bytes()
jlen = struct.unpack_from("<I", raw, 12)[0]
J = json.loads(raw[20:20 + jlen])
blen = struct.unpack_from("<I", raw, 20 + jlen)[0]
BIN = bytearray(raw[28 + jlen:28 + jlen + blen])

def acc(i):
    a = J["accessors"][i]; bv = J["bufferViews"][a["bufferView"]]
    off = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
    dt = {5125: np.uint32, 5126: np.float32, 5123: np.uint16}[a["componentType"]]
    n = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4}[a["type"]]
    return np.frombuffer(BIN, dt, a["count"] * n, off).reshape(a["count"], n) if n > 1 else np.frombuffer(BIN, dt, a["count"], off)

prim = J["meshes"][0]["primitives"][0]
idx = acc(prim["indices"]).reshape(-1, 3).astype(np.int64)
uv = acc(prim["attributes"]["TEXCOORD_0"]).astype(np.float64)
img_i = J["textures"][J["materials"][0]["pbrMetallicRoughness"]["baseColorTexture"]["index"]].get("extensions", {}).get("EXT_texture_webp", {}).get("source")
if img_i is None:
    img_i = J["textures"][J["materials"][0]["pbrMetallicRoughness"]["baseColorTexture"]["index"]]["source"]
im = J["images"][img_i]; bv = J["bufferViews"][im["bufferView"]]
base = Image.open(io.BytesIO(bytes(BIN[bv.get("byteOffset", 0):bv.get("byteOffset", 0) + bv["byteLength"]]))).convert("RGB")
W, H = base.size

# charts: union-find over triangles sharing a vertex index (UV seams split vertices)
parent = np.arange(len(uv))
def find(x):
    r = x
    while parent[r] != r: r = parent[r]
    while parent[x] != r: parent[x], x = r, parent[x]
    return r
for a, b, c in idx:
    ra, rb, rc = find(a), find(b), find(c)
    parent[rb] = ra; parent[find(rc)] = ra
roots = np.array([find(v) for v in range(len(uv))])
tri_chart = roots[idx[:, 0]]
_, tri_label = np.unique(tri_chart, return_inverse=True)
tri_label = tri_label + 1                              # 0 = empty
lab = Image.new("I", (W, H), 0); dr = ImageDraw.Draw(lab)
px = (uv % 1.0) * [W, H]                              # sampler wraps (REPEAT); UVs span -1..1
span = np.ptp(np.stack([px[idx[:, 0]], px[idx[:, 1]], px[idx[:, 2]]], 1), axis=1).max(1)
for t, (a, b, c) in enumerate(idx):
    if span[t] > W / 2: continue                      # triangle straddles the wrap seam
    dr.polygon([tuple(px[a]), tuple(px[b]), tuple(px[c])], fill=int(tri_label[t]))
print('coverage', round(float((np.array(lab) > 0).mean()), 3))
L = np.array(lab, dtype=np.int64)
A = np.asarray(base).astype(np.float64)

# classify charts by mean colour: jacket = dark + desaturated, shirt/cuff = bright + desaturated
nlab = L.max() + 1
cnt = np.bincount(L.ravel(), minlength=nlab).astype(float)
mean = np.stack([np.bincount(L.ravel(), A[..., k].ravel(), minlength=nlab) for k in range(3)], 1) / np.maximum(cnt, 1)[:, None]
lum = mean.mean(1) / 255; sat = (mean.max(1) - mean.min(1)) / 255
target = ((lum < 0.32) & (sat < 0.09)) | ((lum > 0.78) & (sat < 0.08))
target[0] = False
T = target[L]

# edge band: texels whose (2*EDGE+1) neighbourhood touches another label
def shift(a, dy, dx, fill):
    o = np.full_like(a, fill); h, w = a.shape[:2]
    o[max(dy, 0):h + min(dy, 0), max(dx, 0):w + min(dx, 0)] = a[max(-dy, 0):h + min(-dy, 0), max(-dx, 0):w + min(-dx, 0)]
    return o
edge = np.zeros_like(T)
for dy in range(-EDGE, EDGE + 1):
    for dx in range(-EDGE, EDGE + 1):
        if dy * dy + dx * dx <= EDGE * EDGE:
            edge |= shift(L, dy, dx, -1) != L
fix = T & edge
known = T & ~edge
out = A.copy()
# grow inward-out: each pass fills fix texels from known 8-neighbours of the SAME chart (mean of those)
for _ in range(EDGE * 3):
    if not fix.any(): break
    s = np.zeros_like(A); n = np.zeros(L.shape)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0: continue
            k = shift(known, dy, dx, False) & (shift(L, dy, dx, -1) == L)
            s += shift(out, dy, dx, 0) * k[..., None]; n += k
    can = fix & (n > 0)
    out[can] = s[can] / n[can][:, None]
    known = known | can; fix = fix & ~can
print(f"charts {nlab - 1}, target charts {int(target.sum())}, texels repaired {int((T & edge).sum())}, unfilled {int(fix.sum())}")
# 2) in-chart fibre strands on the jacket cloth: replace texels that deviate strongly from a 7x7 median (dark
#    jacket charts only, so buttons/lapel lines of the shirt and all skin/hair/eyes stay as authored)
from PIL import ImageFilter
cur = Image.fromarray(out.clip(0, 255).astype(np.uint8))
med = np.asarray(cur.filter(ImageFilter.MedianFilter(7))).astype(np.float64)
jacket = (((lum < 0.32) & (sat < 0.09)) & target)[L]
dev = np.abs(out - med).mean(2)
strand = jacket & (dev > 18)
out[strand] = med[strand] * 0.85 + out[strand] * 0.15
print('fibre texels smoothed', int(strand.sum()))
new = Image.fromarray(out.clip(0, 255).astype(np.uint8))

# before/after crop for QA (jacket-heavy region of the atlas)
(P / "qa").mkdir(exist_ok=True)
bb = (500, 900, 1300, 1500)
qa = Image.new("RGB", (1600, 600)); qa.paste(base.crop(bb), (0, 0)); qa.paste(new.crop(bb), (800, 0))
qa.save(P / "qa/suit_texture_before_after.jpg", quality=88)

# write the new GLB: swap the image bytes, rebuild bufferView offsets (all views are slices of buffer 0)
buf = io.BytesIO(); new.save(buf, "WEBP", quality=94, method=6); nb = buf.getvalue()
views = J["bufferViews"]; order = sorted(range(len(views)), key=lambda i: views[i].get("byteOffset", 0))
outbin = bytearray()
for i in order:
    v = views[i]; o = v.get("byteOffset", 0)
    data = nb if i == im["bufferView"] else bytes(BIN[o:o + v["byteLength"]])
    while len(outbin) % 4: outbin += b"\0"
    v["byteOffset"] = len(outbin); v["byteLength"] = len(data); outbin += data
while len(outbin) % 4: outbin += b"\0"
J["buffers"][0]["byteLength"] = len(outbin)
js = json.dumps(J, separators=(",", ":")).encode()
js += b" " * ((4 - len(js) % 4) % 4)
OUT.parent.mkdir(parents=True, exist_ok=True)
glb = struct.pack("<III", 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(outbin)) + struct.pack("<II", len(js), 0x4E4F534A) + js + struct.pack("<II", len(outbin), 0x004E4942) + outbin
OUT.write_bytes(glb)
print("wrote", OUT, len(glb))
