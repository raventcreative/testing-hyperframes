import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
UV = np.fromfile('uv.f32', np.float32).reshape(-1, 2); I = np.fromfile('idx.u32', np.uint32).reshape(-1, 3)
def coverage(S):
    im = Image.new('L', (S, S), 0); d = ImageDraw.Draw(im)
    uv = UV * (S - 1)
    for t in I: d.polygon([tuple(uv[t[0]]), tuple(uv[t[1]]), tuple(uv[t[2]])], fill=255)
    return np.asarray(im) > 0
def dilate(img, cov, radius=6):
    """copy the nearest covered texel into uncovered texels within `radius` (standard UV gutter padding)"""
    dist, (iy, ix) = ndimage.distance_transform_edt(~cov, return_indices=True)
    m = (~cov) & (dist <= radius)
    out = img.copy(); out[m] = img[iy[m], ix[m]]
    return out
