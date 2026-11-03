"""Assemble index.html for one example clip (scenes/_base.html + scenes/<id>.html) and optionally render it
to ../assets/clips/<id>_aipreneur.mp4. Sections: @@META (dur=), @@CSS, @@HTML, @@JS.
Run: python3 -I tools/build.py e02 [--render]"""
import re, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sid = sys.argv[1]
sec, cur = {}, None
for line in (P / f"scenes/{sid}.html").read_text().splitlines():
    m = re.match(r"^@@(\w+)\s*$", line)
    if m:
        cur = m.group(1); sec[cur] = []; continue
    if cur:
        sec[cur].append(line)
sec = {k: "\n".join(v) for k, v in sec.items()}
meta = dict(l.split("=", 1) for l in sec.get("META", "").splitlines() if "=" in l)
html = (P / "scenes/_base.html").read_text()
for k, v in {"ID": sid, "DUR": meta.get("dur", "5"), "CSS": sec.get("CSS", ""), "HTML": sec.get("HTML", ""), "JS": sec.get("JS", "")}.items():
    html = html.replace("{{" + k + "}}", v)
(P / "index.html").write_text(html)
print("index.html <-", sid)
if "--render" in sys.argv:
    out = P.parent / f"assets/clips/{sid}_aipreneur.mp4"
    r = subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "render", "-o", str(out), "-q", "delivery", "-f", "30"], cwd=P, capture_output=True, text=True)
    print("rendered", out.name if r.returncode == 0 else r.stderr[-1500:])
