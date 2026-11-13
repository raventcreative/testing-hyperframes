"""Assemble index.html from production/index.src.txt: robot presenter rig (CSS/markup/JS setup reused from agent-demo-137)
and static SFX <audio> tags timed from production/word_timing.json. Afterwards run tools/add_mouth.py (repo root).
Run: python3 -I tools/build.py <project>"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
ref = (P.parent / "agent-demo-137/index.html").read_text()
lines = ref.split("\n")
c0 = next(i for i, l in enumerate(lines) if l.strip().startswith("#robot { position: absolute;"))
c1 = next(i for i, l in enumerate(lines) if l.strip().startswith("#logo {"))
css = "\n".join(lines[c0:c1])
h0 = ref.index('<div id="robot">'); h1 = ref.index("</div></div></div></div>", h0) + len("</div></div></div></div>")
html = ref[h0:h1]
j0 = ref.index("        /* robot presenter rig v2"); j1 = ref.index("        // gestures:", j0)
js = ref[j0:j1]

T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32}
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045}
ev = [("whoosh", 0.05), ("pop", wt("Gue tunjukin", "simulasinya")), ("pop", wt("Ini mesin", "AC") - 0.1), ("pop", wt("radius 5", "5") - 0.1),
      ("ping", wt("modul mana", "modul")), ("pop", wt("Bukan dari", "kalender")),
      ("click", wt("Pertama, radar", "radar") - 0.05), ("whoosh", wt("Pertama, radar", "radar") + 0.15), ("pop", ph("Kamis bakal")["start"]),
      ("pop", ph("Pencarian service")["start"]), ("pop", ph("Rating kompetitor")["start"]), ("whoosh", wt("Budget iklan", "dipindah") - 0.1),
      ("click", ph("Terus semua kanal")["start"]), ("whoosh", ph("Terus semua kanal")["start"] + 0.2),
      ("pop", wt("profil Maps", "Maps") - 0.1), ("pop", wt("profil Maps", "iklan") - 0.1), ("pop", wt("halaman area", "halaman") - 0.1),
      ("pop", wt("halaman area", "video") - 0.1), ("pop", wt("sampai grup", "grup") - 0.1), ("ping", wt("Semua dari", "otak") - 0.2),
      ("click", ph("Dan ini yang")["start"] + 0.15), ("whoosh", ph("Dan ini yang")["start"] + 0.3), ("pop", wt("Jam 9", "chat") - 0.1),
      ("pop", ph("Dibales dalam")["start"] + 0.25), ("ping", wt("jadwal teknisi", "ke-booking") - 0.1),
      ("whoosh", ph("Mau sistem")["start"] - 0.2), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
