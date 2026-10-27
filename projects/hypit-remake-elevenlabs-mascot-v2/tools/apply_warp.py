"""Inserts the v4 time-warp call into every scene timeline (idempotent). See vendor/timewarp.js."""
import json, re, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
sc = json.loads((P / "production/scenes.json").read_text())["scenes"]
for s in sc:
    f = P / f"compositions/{s['id']}.html"
    t = f.read_text()
    t = re.sub(r"\n\s*window\.__warpTL && window\.__warpTL\(tl, [\d.]+, [\d.]+\);[^\n]*", "", t)
    line = "      const tl = gsap.timeline({ paused: true });"
    assert t.count(line) == 1, f
    t = t.replace(line, line + f"\n      window.__warpTL && window.__warpTL(tl, {s['start']}, {s['end']}); // v4: hits follow the measured VO timing")
    f.write_text(t)
print("warp inserted in", len(sc), "scenes")
