"""Real footage stills (documentary evidence) for the scenes: one frame of the user's own screen recording, cropped
to the readable focal area, lightly denoised + sharpened (no AI upscaling: UI text is never re-invented).
The Stitch and Pomelli recordings carry a 'clideo.com' watermark (from the compression website) at a fixed spot in
the lower right; every crop from those two files is asserted to stay clear of it, so the mark never reaches the video.
Writes assets/footage/<name>.jpg + production/footage_provenance.json.  Run: python3 -I tools/footage.py ."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
WM = (1370, 870, 1880, 985)          # watermark box (x0, y0, x1, y1) in the 1920x1032 source, with margin
# name: (source, time s, crop x, y, w, h, output width)
SHOTS = {
    "pom_title":     ("pomelli", 1.0, 440, 160, 1040, 700, 1560),
    "pom_campaign":  ("pomelli", 131, 300, 236, 1060, 624, 1590),
    "pom_brief":     ("pomelli", 131, 16, 240, 282, 396, 564),
    "pom_card1":     ("pomelli", 131, 509, 387, 290, 474, 580),
    "pom_card2":     ("pomelli", 134, 810, 387, 290, 474, 580),
    "pom_card3":     ("pomelli", 131, 1111, 387, 290, 474, 580),
    "stitch_prompt": ("stitch", 12.5, 420, 300, 946, 620, 1419),
    "stitch_screens": ("stitch", 98, 400, 140, 1460, 728, 1460),
    "stitch_s1":     ("stitch", 98, 417, 185, 319, 684, 638),
    "stitch_s2":     ("stitch", 98, 785, 185, 321, 684, 642),
    "stitch_s3":     ("stitch", 98, 1155, 185, 319, 684, 638),
    "stitch_live":   ("stitch", 182, 790, 170, 350, 770, 700),
    "web_hero":      ("aipreneur_website", 2.0, 300, 95, 1320, 935, 1320),
    "anti_hero":     ("antigravity", 0.5, 200, 120, 1520, 720, 1520),
    "anti_wordmark": ("antigravity", 15.7, 0, 420, 1920, 612, 1920),
}
out = P / "assets/footage"; out.mkdir(parents=True, exist_ok=True)
tmp = P / "production/raw"; tmp.mkdir(parents=True, exist_ok=True)
prov = {}
for name, (src, t, x, y, w, h, ow) in SHOTS.items():
    if src in ("stitch", "pomelli"):
        overlap = not (x + w <= WM[0] or x >= WM[2] or y + h <= WM[1] or y >= WM[3])
        assert not overlap, f"{name}: crop touches the watermark area"
    f = tmp / f"{src}_{t}.png"
    if not f.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(P / f"assets/src/{src}.mp4"), "-frames:v", "1", str(f)], check=True)
    im = Image.open(f).convert("RGB").crop((x, y, x + w, y + h))
    im = im.filter(ImageFilter.MedianFilter(3)) if src in ("stitch", "pomelli") else im   # soften block noise of the compressed files
    oh = round(h * ow / w)
    im = im.resize((ow, oh), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    im.save(out / f"{name}.jpg", quality=93)
    prov[name] = {"source": f"assets/src/{src}.mp4", "time_s": t, "crop_xywh": [x, y, w, h], "size": [ow, oh]}
    print(name, ow, oh)
(P / "production/footage_provenance.json").write_text(json.dumps(prov, indent=1))
