#!/usr/bin/env python3
"""Self-shots: stills of OUR OWN composition (no header/captions/logo/grain) used where the story needs copies of
the result (S00 previews, S11 B-roll tiles, S18 shards, S22/S24 montage, S20 phone screen).
Run: python3 tools/selfshots.py [name ...]  -> assets/elements/selfshots/<name>.jpg (540x960) + <name>_full.jpg (1080x1920)"""
import os, subprocess, sys, shutil
from pathlib import Path
from PIL import Image
P = Path(__file__).resolve().parents[1]
SHOTS = {"orbit": 6.2, "chat": 7.95, "escape": 9.05, "snap": 10.9, "checks": 12.95, "headline": 13.9, "portal": 14.75,
         "growth": 17.1, "studio": 19.8, "broll": 22.9, "paper": 24.45, "dolly": 25.4, "cover": 26.3, "glass": 27.9,
         "zoomthru": 29.1, "city": 30.6, "city_end": 30.78, "break": 31.15, "dzoom": 31.95, "phone": 33.0, "check20": 35.4}
names = sys.argv[1:] or list(SHOTS)
out = P / "assets/elements/selfshots"; out.mkdir(parents=True, exist_ok=True)
tmp = Path(os.environ.get("SELFSHOT_TMP", "/tmp/claude-0/selfshots")); shutil.rmtree(tmp, ignore_errors=True)
idx = P / "index.html"
orig = idx.read_text()
clean = orig
for tag in ('<div id="hud"', '<div id="captions"', '<div id="logo"', '<div id="grain"'):
    a = clean.index(tag); b = clean.index("\n", a)
    clean = clean[:a] + "<!-- selfshot: removed -->" + clean[b:]
try:
    idx.write_text(clean)
    shutil.rmtree(P / ".hyperframes", ignore_errors=True)
    times = ",".join(str(SHOTS[n]) for n in names)
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "snapshot", "--at", times, "--no-end", "-o", str(tmp)], cwd=P, check=True, capture_output=True)
finally:
    idx.write_text(orig)
    shutil.rmtree(P / ".hyperframes", ignore_errors=True)
files = sorted(tmp.glob("frame-*-at-*.png"))
for n, f in zip(names, files):
    im = Image.open(f).convert("RGB")
    im.save(out / f"{n}_full.jpg", quality=90)
    im.resize((540, 960), Image.LANCZOS).save(out / f"{n}.jpg", quality=88)
    print(n, SHOTS[n], f.name)
