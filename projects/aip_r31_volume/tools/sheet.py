"""python3 tools/sheet.py <dir> <out.jpg> [cols] [w] — contact sheet of the frames in <dir> (sorted), labelled with the time."""
import sys, glob, subprocess, os
d, out = sys.argv[1], sys.argv[2]; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6; w = int(sys.argv[4]) if len(sys.argv) > 4 else 270
fs = sorted(glob.glob(d + "/f_*.jpg"))
from PIL import Image, ImageDraw
ims = [Image.open(f).convert("RGB").resize((w, int(w * 1920 / 1080))) for f in fs]
h = ims[0].height; rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (cols * w, rows * h), "black")
for i, (im, f) in enumerate(zip(ims, fs)):
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, 64, 18], fill="black"); dr.text((3, 3), os.path.basename(f)[2:-4], fill="yellow")
    S.paste(im, ((i % cols) * w, (i // cols) * h))
S.save(out, quality=85); print(out, len(ims))
