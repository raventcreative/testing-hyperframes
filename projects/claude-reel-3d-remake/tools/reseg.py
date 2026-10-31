#!/usr/bin/env python3
"""Carry finished render segments from an old plan dir to the new one (only when the edit cannot touch those frames).
Run: python3 tools/reseg.py <old_hash_dir_name> <new_hash_dir_name>"""
import json, shutil, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1] / "renders/.hf-segments"
old, new = R / sys.argv[1], R / sys.argv[2]
m = json.load(open(old / "segments.json"))
comp = []
for c in m["completed"]:
    src = Path(c["path"]); dst = new / src.name
    shutil.copy2(src, dst); comp.append(dict(c, path=str(dst)))
json.dump(dict(m, planHash=sys.argv[2], completed=comp), open(new / "segments.json", "w"))
print(sorted(c["index"] for c in comp))
