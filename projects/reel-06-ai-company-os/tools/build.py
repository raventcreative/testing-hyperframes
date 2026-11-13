"""Assemble index.html from index.src.html: robot presenter rig (CSS/markup/JS setup reused from agent-demo-137)
and static SFX <audio> tags timed from production/word_timing.json.
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
tSim = ph("Gue tunjukin")["start"]; tRun = wt("Klik jalankan", "jalankan"); NT = [ph(s)["start"] for s in ("Agent riset", "CMO langsung", "Sales ngecek", "Analis mantau", "developer benerin", "Terus CEO")]
tKunci = ph("Tapi kunci")["start"]; tMem = wt("memori bersama", "memori"); tZ = ph("Satu agent")["start"] - 0.55; tMak = ph("Makin lama")["start"]; tCta = ph("Mau sistem")["start"]
tEnam = wt("dijalanin", "enam")
ev = [("pop", 0.1), ("pop", tEnam - 0.1)] + [("pop", tEnam + 0.35 + i * 0.24) for i in range(3)]
ev += [("whoosh", tSim - 0.55)]                                            # iris
ev += [("pop", wt("Ada CEO", w)) for w in ("CEO", "riset")] + [("pop", wt("sales,", w)) for w in ("sales", "analis")]
ev += [("whoosh", ph("Masing-masing")["start"] + 0.05)]                      # CMO card pops out
ev += [("whoosh", ph("Klik jalankan")["start"] - 0.62), ("click", tRun - 0.05)]   # shutter, click
ev += [("pop", NT[0]), ("pop", NT[1]), ("whoosh", NT[2] - 0.55), ("pop", NT[3]), ("pop", NT[4]), ("pop", NT[5])]   # doors
ev += [("ping", wt("mana yang", "dikerjain"))]
ev += [("whoosh", tKunci - 0.5), ("pop", tKunci + 0.15), ("pop", tMem - 0.15), ("whoosh", tZ)]   # iris, kinetic, zoom-through
ev += [("pop", wt("Satu agent", "belajar")), ("ping", ph("semua agent")["start"] + 0.2), ("pop", wt("Nggak mulai", "nol"))]
ev += [("whoosh", tMak - 0.1), ("ping", wt("sistemnya", "pintar")), ("whoosh", tCta - 0.62), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
