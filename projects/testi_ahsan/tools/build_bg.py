"""Ahsan testimonial (matte from u2net_human_seg, tools/matte.py) background (white theme, same look as testi_thumb): the client's photo (source/foto.webp) with the client's
cut-out (source/cutout.webp) as matte -> subject sharp, room blurred and lifted toward white (high-key), placed on 1080x1920 with the
head below the headline. Writes assets/bg.jpg + assets/gridmask.png (grid only behind the subject, fading toward the bottom)."""
import cv2, numpy as np
im = cv2.imread("source/foto.webp").astype(np.float32)
H0, W0 = im.shape[:2]
a = cv2.imread("source/matte.png", 0).astype(np.float32) / 255
S = 1.2; HEAD = 610                                     # zoom; canvas y of the head top (photo y ~215)
k = 1080 / W0 * S; ox = 540 - (W0 * 0.5) * k; oy = HEAD - 215 * k
A = np.array([[k, 0, ox], [0, k, oy]], np.float32)
img = cv2.warpAffine(im, A, (1080, 1920), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
al = cv2.warpAffine(a, A, (1080, 1920), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
ab = cv2.GaussianBlur(al, (0, 0), 1.5)[..., None]
subj = np.clip(img + 0.25 * (img - cv2.GaussianBlur(img, (0, 0), 1.4)), 0, 255)
bgd = cv2.GaussianBlur(img, (0, 0), 3.0) * 0.7 + 255 * 0.3
cv2.imwrite("assets/bg.jpg", np.clip(subj * ab + bgd * (1 - ab), 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
amk = cv2.dilate(cv2.GaussianBlur(al, (0, 0), 2.0), np.ones((7, 7), np.uint8))
g = (1 - amk) * np.clip((1650 - np.arange(1920)) / 500, 0, 1)[:, None]
cv2.imwrite("assets/gridmask.png", np.dstack([np.full((1920, 1080, 3), 255, np.uint8), (np.clip(g, 0, 1) * 255).astype(np.uint8)]))
print("ok k=%.3f" % k)
