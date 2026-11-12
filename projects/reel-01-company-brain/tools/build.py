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
ev = [("whoosh", 0.05), ("pop", wt("Ini simulasinya", "simulasinya")), ("click", ph("Semua agent baca")["start"] - 0.05), ("whoosh", ph("Semua agent baca")["start"] + 0.1),
      ("pop", wt("Email,", "Email")), ("pop", wt("Email,", "call")), ("ping", wt("sampai ribuan", "ribuan")), ("click", ph("Coba cari")["start"]),
      ("pop", ph("Langsung ketemu")["start"]), ("click", ph("Pindah ke control")["start"] - 0.05), ("whoosh", ph("Pindah ke control")["start"] + 0.1),
      ("click", ph("Tanya agentnya")["start"]), ("pop", ph("Dia jawab")["start"]), ("click", ph("Agent yang ini")["start"] - 0.05), ("whoosh", ph("Agent yang ini")["start"] + 0.1),
      ("whoosh", ph("Lagi di luar")["start"] - 0.15), ("pop", wt("Chat aja", "HP")), ("whoosh", ph("Dan bagian")["start"] + 0.4), ("click", wt("lu bisa pilih", "pilih") - 0.1),
      ("click", ph("Kalau keputusannya")["start"] - 0.05), ("pop", wt("suruh mereka", "debat")), ("ping", wt("satu yang", "keputusan") - 0.3),
      ("whoosh", ph("Mau sistem")["start"] - 0.2), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
