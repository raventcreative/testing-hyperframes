#!/usr/bin/env bash
# One representative 1080x1350 PNG per slide (time = "still" in slides/manifest.json) -> out/stills/<name>.png,
# plus a JPG overview sheet of all of them in <scratch dir>. Usage: tools/stills.sh <scratch dir>
set -euo pipefail
cd "$(dirname "$0")/.."
SCR="$1"; mkdir -p out/stills "$SCR"
python3 -I - "$SCR" <<'PY'
import json, shutil, subprocess, sys
from pathlib import Path
from PIL import Image
scr = Path(sys.argv[1]); tmp = scr / "stills_tmp"; tmp.mkdir(exist_ok=True)
thumbs = []
for s in json.loads(Path("slides/manifest.json").read_text()):
    for p in tmp.glob("*"): p.unlink()
    t = s["still"]
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "snapshot", s["dir"], "--at", str(t), "--no-end", "--keep", "--timeout", "60000", "-o", str(tmp)], check=True, capture_output=True)
    png = next(tmp.glob("at-*.png"))
    im = Image.open(png)
    assert im.size == (1080, 1350), im.size
    dst = Path("out/stills") / (s["out"] + ".png")
    shutil.move(str(png), dst)
    thumbs.append(Image.open(dst).convert("RGB").resize((270, 338), Image.LANCZOS))
    print("still", dst, t)
for p in tmp.glob("*"): p.unlink()
tmp.rmdir()
cols = 6; rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * 278 + 8, rows * 346 + 8), (40, 44, 60))
for i, im in enumerate(thumbs):
    sheet.paste(im, (8 + (i % cols) * 278, 8 + (i // cols) * 346))
sheet.save(scr / "stills_overview.jpg", quality=85)
print("overview", scr / "stills_overview.jpg")
PY
