# Crop the photo out of the screenshot and inpaint away the burned-in texts.
import cv2, numpy as np, sys
src, out = sys.argv[1], sys.argv[2]
im = cv2.imread(src)[12:744, 46:456]                     # photo area only (drop black bars)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
white = ((hsv[..., 2] > 185) & (hsv[..., 1] < 70)).astype(np.uint8)
blue = ((hsv[..., 0] > 95) & (hsv[..., 0] < 125) & (hsv[..., 1] > 120) & (hsv[..., 2] > 140)).astype(np.uint8)
mask = np.zeros(im.shape[:2], np.uint8)
for (x0, y0, x1, y1), extra in [((140, 30, 270, 62), blue), ((140, 520, 270, 552), None)]:   # logo, caption
    m = white[y0:y1, x0:x1].copy()
    if extra is not None: m |= extra[y0:y1, x0:x1]
    mask[y0:y1, x0:x1] = m * 255
mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), 2)
cv2.imwrite(out.replace('.png', '_mask.png'), mask)
clean = cv2.inpaint(im, mask, 6, cv2.INPAINT_TELEA)
cv2.imwrite(out, clean)
print(im.shape, int(mask.sum() / 255), 'px masked')
