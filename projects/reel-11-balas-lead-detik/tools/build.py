"""Assemble index.html from production/index.src.txt + static SFX <audio> tags timed from production/word_timing.json.
(3D robot: shipped separately by ../../tools/add_robot3d.py; no 2D rig injection.)  Run: python3 -I tools/build.py <project>"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
def wt(s, w):
    k = PH.index(ph(s))
    return next(x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower()))
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.0}
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.04}
tNih = ph("Nih gue")["start"]; W1 = tNih - 1.12; tSimW = wt("Nih gue", "simulasinya")
t3 = ph("Tiga, AI")["start"]; tZ = t3 - 1.0; t4 = ph("Empat, AI")["start"]; W3 = t4 - 1.02
t5 = ph("Lima, balasan")["start"]; tKir = wt("Lima, balasan", "kekirim"); tCall = wt("dan lead panas", "call")
t6 = ph("Semua jalan")["start"]; tZ3 = max(tCall + 0.3, t6 - 0.55); tCta = ph("Mau sistem")["start"]; W5 = tCta - 1.13
tJalan = wt("trigger langsung", "jalan"); tYang = ph("Yang ini")["start"]; tNama = ph("namanya siapa")["start"]; tData = wt("Tiga, AI", "data")
# one quiet whoosh per transition / big camera move
ev = [("whoosh", W1), ("whoosh", tSimW + 0.35), ("whoosh", tJalan + 0.2), ("whoosh", tYang - 0.42), ("whoosh", tZ + 0.3),
      ("whoosh", tNama - 0.38), ("whoosh", W3), ("whoosh", tKir + 0.32), ("whoosh", tZ3 + 0.3), ("whoosh", tZ3 + 0.85), ("whoosh", W5)]
ev += [("pop", wt("Lead lu nanya", "sebelas") - 0.15), ("pop", ph("baru dibales")["start"] - 0.2), ("pop", wt("baru dibales", "siang") - 0.2),
       ("pop", wt("Pas dibales", "udah") - 0.2), ("click", wt("Pas dibales", "kompetitor") - 0.02), ("pop", wt("Pas dibales", "kompetitor")),
       ("pop", wt("Satu, ada", "komen") - 0.12), ("pop", wt("Satu, ada", "DM") - 0.12), ("ping", tJalan + 0.05), ("ping", wt("cuma nanya", "siap") + 0.35),
       ("pop", tYang - 0.25), ("sparkle", wt("Yang ini", "enam")), ("pop", ph("lead panas")["start"] - 0.1),
       ("click", t3 + 0.35), ("pop", max(t3 + 1.05, tData - 0.05)), ("pop", tNama - 0.45), ("ping", wt("namanya siapa", "order")),
       ("pop", wt("Empat, AI", "personal") - 0.1), ("click", wt("bukan template", "kaku") - 0.3), ("pop", wt("bukan template", "kaku") - 0.05),
       ("click", tKir - 0.45), ("ping", tKir - 0.3), ("pop", tKir + 0.45), ("pop", tKir + 0.7), ("pop", ph("dan lead panas")["start"] + 0.75),
       ("ping", wt("dan lead panas", "dijadwalin") - 0.15), ("pop", wt("Semua jalan", "sendiri") - 0.1), ("pop", wt("Semua jalan", "jam") - 0.05),
       ("pop", ph("Nggak ada lagi")["start"] - 0.1), ("sparkle", wt("Nggak ada lagi", "nunggu")), ("click", wt("Klik link", "link") - 0.05)]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
