#!/usr/bin/env python3
"""Self-shots: stills of OUR OWN composition (no header/captions/logo/grain) used where the story needs copies of
the result (S00 previews, S11 B-roll tiles, S18 shards, S22/S24 montage, S20 phone screen).
Run: python3 tools/selfshots.py [name ...]  -> assets/elements/selfshots/<name>.jpg (540x960) + <name>_full.jpg (1080x1920)"""
import os, subprocess, sys, shutil
from pathlib import Path
from PIL import Image
P = Path(__file__).resolve().parents[1]
SHOTS = {"editorial": 6.6, "ots": 10.9, "word": 15.2, "glass": 18.3, "spot": 20.15, "grade": 23.1}
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
