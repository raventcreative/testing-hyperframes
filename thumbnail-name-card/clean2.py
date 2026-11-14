# Crop photo from a screenshot and inpaint white burned-in captions inside given boxes.
# usage: clean2.py src out x0,y0,x1,y1(crop) bx0,by0,bx1,by1 [more boxes...]   (boxes in source coords)
import cv2, numpy as np, sys
src, out, crop = sys.argv[1], sys.argv[2], [int(v) for v in sys.argv[3].split(',')]
im = cv2.imread(src); hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
white = ((hsv[..., 2] > 190) & (hsv[..., 1] < 70)).astype(np.uint8)
mask = np.zeros(im.shape[:2], np.uint8)
for b in sys.argv[4:]:
    x0, y0, x1, y1 = [int(v) for v in b.split(',')]
    mask[y0:y1, x0:x1] = white[y0:y1, x0:x1] * 255
mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), 2)
clean = cv2.inpaint(im, mask, 7, cv2.INPAINT_TELEA)
x0, y0, x1, y1 = crop
cv2.imwrite(out, clean[y0:y1, x0:x1]); print('masked', int(mask.sum() / 255))
