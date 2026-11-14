"""Turn a folder of HyperFrames snapshot PNGs into one labelled JPG contact sheet, then delete the PNGs.
Usage: python3 -I tools/sheet.py <png_dir> <out.jpg> [cols] [thumb_width]"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

src, out = Path(sys.argv[1]), Path(sys.argv[2])
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 360
pngs = sorted(src.glob("*.png"), key=lambda p: float(re.search(r"at-([\d.]+)s", p.name).group(1)) if re.search(r"at-([\d.]+)s", p.name) else 0)
if not pngs:
    raise SystemExit("no pngs in " + str(src))
th = round(tw * 1350 / 1080)
rows = (len(pngs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw + (cols + 1) * 8, rows * (th + 26) + (rows + 1) * 8), (40, 44, 60))
d = ImageDraw.Draw(sheet)
for i, p in enumerate(pngs):
    im = Image.open(p).convert("RGB").resize((tw, th), Image.LANCZOS)
    x = 8 + (i % cols) * (tw + 8)
    y = 8 + (i // cols) * (th + 34)
    sheet.paste(im, (x, y + 26))
    m = re.search(r"at-([\d.]+)s", p.name)
    d.text((x + 4, y + 6), (m.group(1) + " s") if m else p.stem, fill=(255, 255, 255))
sheet.save(out, quality=86)
for p in pngs:
    p.unlink()
for j in src.glob("contact-sheet*.jpg"):
    j.unlink()
print("sheet", out, len(pngs))
