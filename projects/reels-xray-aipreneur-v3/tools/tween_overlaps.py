"""Find tweens on the same element + property that overlap in time (a source of seek-order dependence)."""
import glob, json, re, sys
from collections import defaultdict
pat = re.compile(r'tl\.fromTo\(("[^"]+"),\s*(\{.*?\}),\s*(\{.*?\}),\s*([\d.]+)\);')
bad = 0
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "compositions/*.html")):
    seen = defaultdict(list)
    for m in pat.finditer(open(f).read()):
        sel = json.loads(m.group(1))
        try:
            to = json.loads(m.group(3))
        except Exception:
            continue
        t0 = float(m.group(4)); t1 = t0 + float(to.get("duration", 0))
        for k in to:
            if k in ("duration", "ease", "immediateRender", "transformOrigin", "transformPerspective"):
                continue
            for (a, b) in seen[(sel, k)]:
                if t0 < b - 1e-4 and a < t1 - 1e-4:
                    bad += 1
                    print(f.split("/")[-1], sel, k, f"[{a:.3f},{b:.3f}] vs [{t0:.3f},{t1:.3f}]")
            seen[(sel, k)].append((t0, t1))
print("overlaps:", bad)
