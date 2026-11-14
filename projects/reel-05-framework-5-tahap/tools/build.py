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
ev = [("whoosh", 0.05), ("click", wt("bikin AI agent", "agent") - 0.1), ("pop", ph("Padahal")["start"] - 0.1), ("pop", wt("Padahal", "itu")),
      ("whoosh", wt("datang paling", "terakhir") - 0.45), ("pop", wt("Gue tunjukin", "simulasinya")), ("ping", ph("Lima tahap")["start"])]
for s0 in ["Tahap satu", "Tahap dua", "Tahap tiga", "Tahap empat", "Tahap lima"]:
    ev += [("click", ph(s0)["start"] - 0.05)]
ev += [("whoosh", ph("Tahap satu")["start"] - 1.12), ("whoosh", ph("Tahap dua")["start"] - 1.2), ("whoosh", ph("Tahap tiga")["start"] - 1.12),
       ("whoosh", ph("Tahap empat")["start"] + 0.1), ("whoosh", ph("Tahap lima")["start"] + 0.1), ("whoosh", ph("Terakhir")["start"] - 1.15)]
ev += [("pop", ph("Stop dulu")["start"]), ("pop", ph("Dokumentasi")["start"]), ("pop", ph("Hapus")["start"]), ("pop", ph("Sederhanakan")["start"]),
       ("ping", ph("masuk ke satu")["start"] + 0.2), ("click", wt("mereka yang", "jalan") - 0.35), ("ping", wt("mereka yang", "jalan") - 0.2),
       ("pop", wt("Ada booking", "booking") + 0.25), ("pop", wt("penjualan baru", "penjualan") + 0.25), ("pop", wt("penjualan baru", "email") + 0.25),
       ("ping", wt("Hasilnya numpuk", "numpuk")), ("whoosh", ph("Mau sistem")["start"] - 0.2), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
