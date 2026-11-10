"""Crops the close-up robot shots (tools/shoot_thumbs.cjs) to 144×144 strip chips: assets/thumbs/<style>.png.
Run: python3 -I tools/thumbs.py <raw dir> ."""
import sys
from pathlib import Path
from PIL import Image
RAW, P = Path(sys.argv[1]), Path(sys.argv[2] if len(sys.argv) > 2 else ".").resolve()
(P / "assets/thumbs").mkdir(parents=True, exist_ok=True)
for f in sorted(RAW.glob("*.png")):
    im = Image.open(f).convert("RGB")
    cx, cy, s = 410, 470, 780
    im.crop((cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2)).resize((144, 144), Image.LANCZOS if f.stem != "pixel" else Image.BOX).save(P / "assets/thumbs" / f.name, optimize=True)
    print(f.name)
