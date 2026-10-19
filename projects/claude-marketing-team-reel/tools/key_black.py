"""Key out the pure-black background of the HeyGen character video.
Background = near-black pixels (r+g+b <= SEED) connected to the frame border; enclosed dark pixels
(hair crevices, suit shadows) stay opaque. 1-2px soft edge with black-fringe removal."""
import numpy as np
from scipy import ndimage
SEED = 6
def key(rgb):
    lum = rgb.astype(np.int32).sum(2)
    lab, n = ndimage.label(lum <= SEED)
    border = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    bg = np.isin(lab, border[border > 0])
    near = ndimage.binary_dilation(bg, iterations=2) & ~bg
    a = np.ones(lum.shape, np.float32); a[bg] = 0
    a[near] = np.clip((lum[near] - SEED) / 45.0, 0, 1)
    out = rgb.astype(np.float32)
    m = near & (a > 0.05)
    out[m] = np.clip(out[m] / a[m, None], 0, 255)  # un-premultiply the black fringe
    return np.dstack([out, a * 255]).astype(np.uint8)
