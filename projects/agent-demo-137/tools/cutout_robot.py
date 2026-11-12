"""Cut the client-supplied robot out of its grey studio background (no network model needed).
Background = smooth gradient fitted on the border band; pixels close to it (dist < 32) OR bluish, unsaturated
mid-grey shadow pixels below the shoulders are grown from the image border into a background mask. Edge alpha is a
ramp on the distance; floor shadow/glow under the robot is cropped away.
Run: python3 -I tools/cutout_robot.py assets/robot/robot_src.webp assets/robot/robot.png"""
import sys
from collections import deque
import numpy as np
from PIL import Image, ImageFilter

src, out = sys.argv[1], sys.argv[2]
orig = np.asarray(Image.open(src).convert("RGB").crop((0, 0, 1312, 1062)))
a = orig.astype(np.float32); H, W, _ = a.shape
yy, xx = np.mgrid[0:H, 0:W]
band = np.zeros((H, W), bool); b = 24; band[:b, :] = band[-b:, :] = band[:, :b] = band[:, -b:] = True
X = np.stack([np.ones(H * W), xx.ravel() / W, yy.ravel() / H, (xx * yy).ravel() / (W * H), (xx.ravel() / W) ** 2, (yy.ravel() / H) ** 2], 1)
bg = np.zeros_like(a)
for c in range(3):
    coef, *_ = np.linalg.lstsq(X[band.ravel()], a[..., c].ravel()[band.ravel()], rcond=None)
    bg[..., c] = (X @ coef).reshape(H, W)
dist = np.sqrt(((a - bg) ** 2).sum(-1))
luma = 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]
sat = a.max(-1) - a.min(-1); tint = a[..., 2] - a[..., 0]
shadow = ((yy > 600) | ((xx > 1000) & (yy > 250))) & (luma > 110) & (luma < 232) & (sat < 40) & (tint >= 8)
cand = (dist < 32) | shadow
seen = np.zeros((H, W), bool); q = deque()
for x in range(W):
    for y in (0, H - 1):
        if cand[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
for y in range(H):
    for x in (0, W - 1):
        if cand[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if 0 <= ny < H and 0 <= nx < W and cand[ny, nx] and not seen[ny, nx]:
            seen[ny, nx] = True; q.append((ny, nx))
alpha = np.ones((H, W), np.float32)
ramp = np.clip((dist - 16) / 16, 0, 1)
alpha[seen] = np.where(shadow[seen], 0, ramp[seen])
m = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.0))
al = np.asarray(m).copy()
# keep only real parts (body + two hands): drop small disconnected specks
solid = al > 60; lab = np.zeros(al.shape, np.int32); n = 0; sizes = {}
for sy, sx in zip(*np.nonzero(solid)):
    if lab[sy, sx]: continue
    n += 1; lab[sy, sx] = n; dq = deque([(sy, sx)]); c = 0
    while dq:
        y, x = dq.popleft(); c += 1
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < H and 0 <= nx < W and solid[ny, nx] and not lab[ny, nx]: lab[ny, nx] = n; dq.append((ny, nx))
    sizes[n] = c
keep = np.isin(lab, [k for k, v in sizes.items() if v > 4000])
near = np.asarray(Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))) > 0
al[~near] = 0
res = Image.fromarray(np.dstack([orig, al]), "RGBA")
res = res.crop(res.split()[3].getbbox())
res.save(out)
print(res.size)
