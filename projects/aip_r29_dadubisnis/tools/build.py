"""tools/index.src.html -> index.html (fills the total/VO durations from production/timing.json and the inline icons).
Run: python3 -I tools/build.py ."""
import json, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
LOOP = '<svg viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11a8 8 0 0 0-14.3-4.9L4 8"/><path d="M4 3v5h5"/><path d="M4 13a8 8 0 0 0 14.3 4.9L20 16"/><path d="M20 21v-5h-5"/></svg>'
s = (P / "tools/index.src.html").read_text()
s = s.replace("{{TOTAL}}", str(T["total_sec"])).replace("{{VOSEC}}", str(round(T["vo_sec"], 3))).replace("{{CHECK}}", CHECK).replace("{{LOOP}}", LOOP)
s = s.replace("/*UIJS*/", (P / "vendor/ui.js").read_text())
(P / "index.html").write_text(s)
print("index.html", T["total_sec"], "s")
