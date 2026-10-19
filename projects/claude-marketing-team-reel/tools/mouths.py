"""Builds lip-sync mouth variants for every expression used in the video.
Open mouth = the real open mouth from the TALK tile of 2.png (only the mouth pixels, no box),
scaled to the target face and placed on the target's own closed mouth (which is painted over with
that face's skin tone). Half = the same mouth squashed to ~55% height. Nothing else is touched.
Outputs assets/lips/<name>-0.png (closed, original), -1.png (half), -2.png (open)."""
import numpy as np
from PIL import Image
import os

os.makedirs("assets/lips", exist_ok=True)
SRC = np.array(Image.open("assets/expr/talk.png").convert("RGBA")).astype(int)

def skin_of(img, box):
    x0, y0, x1, y1 = box
    reg = img[y0:y1, x0:x1, :3].reshape(-1, 3)
    return np.median(reg, axis=0)

def mouth_mask(img, box, thr):
    """pixels in box that are clearly not skin (mouth line / opening)."""
    x0, y0, x1, y1 = box
    reg = img[y0:y1, x0:x1, :3]
    sk = skin_of(img, box)
    d = np.abs(reg - sk).sum(2)
    m = (d > thr) & (img[y0:y1, x0:x1, 3] > 200)
    return m, sk

# open mouth of TALK tile (mouth region found by inspection: cols 130-186, rows 222-262)
TB = (130, 222, 186, 262)
tm, tsk = mouth_mask(SRC, TB, 70)
# keep only the mouth opening: the contiguous row band around the widest row (drops nose shadow / chin edge)
rc = tm.sum(1); bands = []; r = 0
while r < len(rc):
    if rc[r] > 0:
        q = r
        while q + 1 < len(rc) and rc[q + 1] > 0: q += 1
        bands.append((int(rc[r:q + 1].sum()), r, q)); r = q + 1
    else: r += 1
_, lo, hi = max(bands)
tm[:lo] = False; tm[hi + 1:] = False
ys, xs = np.nonzero(tm)
T = SRC[TB[1] + ys.min(): TB[1] + ys.max() + 1, TB[0] + xs.min(): TB[0] + xs.max() + 1].copy()
TM = tm[ys.min(): ys.max() + 1, xs.min(): xs.max() + 1]
QUIET_W = 33.0  # closed-mouth width on the 2.png tiles

def build(name, path, box, thr=45, out_prefix=None, scale=None):
    img = np.array(Image.open(path).convert("RGBA")).astype(int)
    m, sk = mouth_mask(img, box, thr)
    # keep the largest horizontal run cluster around the box centre (the mouth line)
    ys, xs = np.nonzero(m)
    if len(xs) == 0:
        raise SystemExit(f"no mouth found for {name}")
    x0, y0 = box[0] + xs.min(), box[1] + ys.min()
    x1, y1 = box[0] + xs.max(), box[1] + ys.max()
    w = x1 - x0 + 1
    cx = (x0 + x1) / 2
    s = scale if scale else w / QUIET_W
    out = out_prefix or name
    Image.fromarray(img.astype(np.uint8)).save(f"assets/lips/{out}-0.png")
    for lvl, vs in ((1, 0.55), (2, 1.0)):
        o = img.copy()
        # paint the closed mouth with skin (1px dilation)
        pad = max(1, int(round(s)))
        o[y0 - pad:y1 + 3 * pad + 1, x0 - pad:x1 + pad + 1, :3] = sk.astype(int)
        th, tw = TM.shape
        nw, nh = max(2, int(round(tw * s))), max(2, int(round(th * s * vs)))
        patch = Image.fromarray(T.astype(np.uint8)).resize((nw, nh), Image.NEAREST)
        pm = Image.fromarray((TM * 255).astype(np.uint8)).resize((nw, nh), Image.NEAREST)
        P = np.array(patch).astype(int); PM = np.array(pm) > 127
        px = int(round(cx - nw / 2)); py = int(round(y0 - s * 1.5))
        reg = o[py:py + nh, px:px + nw]
        reg[PM] = P[PM]
        o[py:py + nh, px:px + nw] = reg
        Image.fromarray(o.astype(np.uint8)).save(f"assets/lips/{out}-{lvl}.png")
    return (x0, y0, x1, y1, round(s, 2))

# search boxes around each expression's closed mouth (tile coords; 1.png coords for seated)
JOBS = {  # name: (file, mouth search box, fixed scale or None)
    "quiet": ("assets/expr/quiet.png", (128, 222, 190, 246), 1.0),
    "smile": ("assets/expr/smile.png", (124, 210, 194, 240), 1.0),
    "smile2": ("assets/expr/smile2.png", (125, 205, 190, 232), 1.0),
    "confident": ("assets/expr/confident.png", (135, 190, 195, 212), 1.0),
    "seated": ("assets/char-seated.png", (440, 560, 640, 630), None),
    "seated-head": ("assets/expr/seated-head.png", (225, 470, 425, 540), None),
}
for n, (p, b, sc) in JOBS.items():
    print(n, build(n, p, b, scale=sc))
