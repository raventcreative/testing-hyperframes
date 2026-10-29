import sys, glob
from PIL import Image
d, crop, cols = sys.argv[1], tuple(map(int, sys.argv[2].split(','))), int(sys.argv[3])
fs = sorted(glob.glob(d + '/frame-*.png'))
w = int(sys.argv[4]) if len(sys.argv) > 4 else 360
ims = [Image.open(f).convert('RGB').crop(crop) for f in fs]
h = int(w * ims[0].height / ims[0].width)
rows = (len(ims) + cols - 1) // cols
c = Image.new('RGB', (w * cols, h * rows), 'white')
for i, im in enumerate(ims): c.paste(im.resize((w, h)), ((i % cols) * w, (i // cols) * h))
c.save(d + '/grid.jpg', quality=88); print(c.size)
