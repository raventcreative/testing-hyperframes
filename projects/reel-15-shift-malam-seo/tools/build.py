"""Assemble index.html from production/index.src.txt + static SFX <audio> tags timed from production/word_timing.json.
Run: python3 -I tools/build.py <project>"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.8}
VOL = {"whoosh": 0.055, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.035}
tCek = ph("Cek sim")["start"]; tWebw = wt("website, review", "website"); tMapsE = ph("sampai listing")["end"]
tStr = ph("Agent strategi")["start"]; tMilE = ph("terus milih")["end"]; tGayaE = ph("dan gaya")["end"]; tBalik = ph("dibalikin")["start"]
tLolos = wt("Direvisi", "lolos"); tLolE = ph("Direvisi")["end"]; tFreshE = ph("biar tetep")["end"]; tBiar = ph("Biar pas")["start"]
tMalam = ph("Malam ini")["start"]; tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.05), ("pop", ph("lu lagi tidur")["start"] - 0.05), ("pop", wt("Tapi lima", "lima") - 0.05), ("pop", wt("lagi kerja", "website") - 0.3),
      ("whoosh", tCek + 0.04),                                   # zoom-through 1
      ("pop", ph("semua kompetitor")["start"] - 0.2), ("whoosh", tWebw - 0.5),
      ("pop", tWebw), ("pop", wt("website, review", "review")), ("pop", wt("sampai listing", "maps")),
      ("whoosh", tMapsE + 0.03),                                 # sweep
      ("ping", wt("Ketemu enam", "enam") - 0.1),
      ("whoosh", tStr - 0.35), ("pop", wt("terus milih", "potensial") - 0.1),
      ("whoosh", tMilE + 0.06),                                  # zoom punch-in 2
      ("click", wt("pakai info", "asli") - 0.1), ("click", wt("dan gaya", "brand") - 0.15),
      ("whoosh", tGayaE - 0.02),                                 # shutter
      ("pop", ph("Ada dua")["start"] + 0.15), ("whoosh", tBalik - 0.15), ("ping", tLolos - 0.1),
      ("whoosh", tLolE - 0.16),                                  # slats
      ("ping", ph("ke website")["start"] - 0.05), ("sparkle", wt("biar tetep", "fresh") - 0.15),
      ("whoosh", tFreshE + 0.05),                                # zoom-out reveal 3
      ("ping", ph("semua beres")["start"] + 0.05), ("whoosh", tBiar - 0.25), ("pop", ph("bisnis lu yang")["start"] - 0.05),
      ("whoosh", tMalam - 0.4), ("pop", tMalam - 0.05), ("pop", tMalam + 0.3), ("pop", wt("Malam ini", "jalan") - 0.1),
      ("whoosh", tCta - 0.5), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
