"""Assemble index.html for one carousel slide from scenes/_base.html + scenes/<id>.html, optionally render it.
Scene files are split into sections by lines '@@NAME' (META, CSS, HEAD, STAGE, USE, JS); META holds key=value lines.
Run: python3 -I tools/build.py <slide-id> [--render]"""
import re, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sid = sys.argv[1]
src = (P / f"scenes/{sid}.html").read_text()
sec, cur = {}, None
for line in src.splitlines():
    m = re.match(r"^@@(\w+)\s*$", line)
    if m: cur = m.group(1); sec[cur] = []; continue
    if cur: sec[cur].append(line)
sec = {k: "\n".join(v) for k, v in sec.items()}
meta = dict(l.split("=", 1) for l in sec.get("META", "").splitlines() if "=" in l)
html = (P / "scenes/_base.html").read_text()
fill = {"ID": sid, "DUR": meta.get("dur", "7"), "CHIP": meta.get("chip", ""), "LOCKLB": meta.get("lock", ""), "FOOTR": meta.get("footr", "Geser"),
        "CSS": sec.get("CSS", ""), "HEAD": sec.get("HEAD", ""), "STAGE": sec.get("STAGE", ""), "USE": sec.get("USE", ""), "JS": sec.get("JS", "")}
for k, v in fill.items(): html = html.replace("{{" + k + "}}", v)
(P / "index.html").write_text(html)
print("index.html <-", sid)
if "--render" in sys.argv:
    out = P / f"out/motion_pack_{sid}_1080x1350.mp4"
    r = subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "render", "-o", str(out), "-q", "delivery", "-f", "30"], cwd=P, capture_output=True, text=True)
    print(r.stdout[-400:] if r.returncode == 0 else r.stderr[-2000:])
