"""Write static SFX <audio> tags into index.html (between <!--SFX--> markers) from production/word_timing.json.
Run: python3 -I tools/sfx.py <project>"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]


def ph(s):
    return next(p for p in PH if p["text"].startswith(s))


def wt(s, w):
    k = PH.index(ph(s))
    for x in W:
        if x[3] == k and x[0].lower().startswith(w.lower()):
            return x[1]
    return ph(s)["start"]


DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32}
VOL = {"whoosh": 0.07, "pop": 0.05, "click": 0.09, "ping": 0.05}
ev = [("whoosh", 0.05), ("pop", ph("Gue tunjukin")["start"]), ("whoosh", 7.2), ("whoosh", 13.3),
      ("click", wt("sambungin", "sambungin") + 0.05)]
for t in [wt("Email,", "Email"), wt("Email,", "CRM"), wt("Email,", "kalender"), wt("chat,", "chat"), wt("chat,", "pembukuan")]:
    ev.append(("pop", t))
tb = ph("Begitu")["start"] + 0.05
ev += [("click", tb), ("whoosh", tb + 0.25), ("click", wt("divisi sales", "sales") - 0.15), ("whoosh", wt("divisi sales", "sales") + 0.05),
       ("click", ph("Cold Email")["start"]), ("whoosh", ph("Cold Email")["start"] + 0.3),
       ("pop", ph("nulis sequence")["start"]), ("pop", ph("bikin subject")["start"]), ("pop", ph("bikin kalimat")["start"]),
       ("click", wt("Klik run", "run")), ("ping", ph("sequence-nya")["start"]), ("whoosh", ph("Masuk dulu")["start"] - 0.15),
       ("click", wt("Lu approve", "approve")), ("ping", wt("Dan tiap", "tujuh")), ("whoosh", ph("lu dapet")["start"] - 0.2),
       ("whoosh", ph("Mau sistem")["start"] - 0.3), ("click", wt("Klik link", "link"))]
tags = []
for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1])):
    tags.append(f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" '
                f'data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>')
html = (P / "index.html").read_text()
block = "<!--SFX-->\n      " + "\n      ".join(tags) + "\n      <!--/SFX-->"
html = re.sub(r"<!--SFX-->.*?<!--/SFX-->", block, html, flags=re.S) if "<!--/SFX-->" in html else html.replace("<!--SFX-->", block)
(P / "index.html").write_text(html)
print(len(tags), "sfx")
