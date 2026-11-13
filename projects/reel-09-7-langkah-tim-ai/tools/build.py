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
tSim = ph("Gue tunjukin")["start"]; t2 = ph("Dua, instruksi")["start"]; t3 = ph("Tiga, otak")["start"]; t4 = ph("Empat, sambungin")["start"]
t5 = ph("Lima, SOP")["start"]; t6 = ph("Enam, sambungin")["start"]; t7b = ph("Tujuh, pasang")["start"]; tCta = ph("Mau sistem")["start"]
WIPES = [tSim - 0.55, t2 - 0.45, t3 - 0.6, t4 - 0.55, t5 - 0.6, t6 - 0.6, t7b - 0.6, tCta - 0.5]   # dots shutter slats doors dots shutter slats doors
ev = [("pop", 0.15), ("pop", wt("Semua orang", "punya") - 0.1), ("pop", wt("Semua orang", "agent") - 0.05), ("pop", wt("Semua orang", "agent") + 0.15),
      ("pop", ph("tapi nggak")["start"] + 0.1), ("click", wt("tapi nggak", "nunjukin") - 0.25), ("ping", ph("Tujuh langkah")["start"])]
ev += [("whoosh", w) for w in WIPES]
for s0, dt in [("Satu, berhenti", 0), ("Dua, instruksi", 0.15), ("Tiga, otak", 0.1), ("Empat, sambungin", 0.1), ("Lima, SOP", 0.1), ("Enam, sambungin", 0.1), ("Tujuh, pasang", 0.1)]:
    ev.append(("click", ph(s0)["start"] + dt - 0.02))
ev += [("click", wt("Mulai mikir", "workflow") - 0.12), ("pop", wt("riset, bikin", "riset") - 0.12), ("pop", wt("riset, bikin", "bikin") - 0.12),
       ("pop", wt("riset, bikin", "review") - 0.12), ("whoosh", wt("riset, bikin", "bikin") + 0.05), ("pop", ph("Ini yang bikin")["start"] - 0.1),
       ("pop", wt("brand guide", "brand") - 0.15), ("pop", wt("brand guide", "kompetitor") - 0.15), ("pop", wt("iklan lama", "iklan") - 0.15),
       ("pop", wt("iklan lama", "dokumen") - 0.15), ("click", wt("Empat, sambungin", "tools") - 0.22), ("whoosh", wt("terus jalanin", "cloud") - 0.55),
       ("pop", ph("Laptop ditutup")["start"] - 0.2), ("ping", wt("agent tetap", "24") - 0.2), ("pop", wt("yang boleh", "boleh") - 0.1), ("pop", wt("yang boleh", "nggak") - 0.05),
       ("ping", wt("sama cara ngecek", "ngecek") + 0.1), ("click", wt("Tiap minggu", "feedback")), ("pop", ph("kualitasnya naik")["start"] - 0.25),
       ("ping", wt("kualitasnya naik", "naik") - 0.2), ("ping", wt("satu bot yang", "ngatur") + 0.35), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
