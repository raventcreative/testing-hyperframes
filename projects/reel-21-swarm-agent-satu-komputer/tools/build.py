"""Assemble index.html from production/index.src.txt: static SFX <audio> tags timed from production/word_timing.json.
The 3D presenter robot ships separately: python3 -I ../../tools/add_robot3d.py .
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
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.035}
tZ1 = ph("Gue tunjukin")["start"] - 0.15; tKlik = ph("Klik tim")["start"]; tPo = ph("terus tracking")["start"] - 0.1
tW3 = ph("Pindah ke")["start"] - 0.4; tPo2 = ph("nyari apa")["start"] - 0.18; tW4 = ph("Dan semua")["start"] - 0.33
tZ5 = ph("kesimpen")["end"] - 0.25; tK0 = ph("dan inget")["end"]; tW7 = ph("Mau sistem")["start"] - 0.95
ev = [("whoosh", t) for t in (tZ1 + 0.1, tKlik + 0.1, tPo, tW3, tPo2, tW4, tZ5, tK0, tW7)]
ev += [("pop", 0.08), ("pop", wt("Bayangin", "lima") - 0.08), ("pop", ph("masing-masing")["start"] + 0.12), ("sparkle", ph("dan nggak ada")["start"] + 0.3),
       ("pop", wt("yang manusia", "manusia") - 0.1), ("click", wt("yang manusia", "manusia") + 0.15), ("ping", ph("Satu otak")["start"] + 0.05),
       ("click", tKlik), ("pop", ph("Mereka follow")["start"] + 0.15), ("pop", ph("kualifikasi")["start"]), ("ping", wt("terus tracking", "closing")),
       ("pop", ph("Semua di satu")["start"] - 0.1), ("pop", ph("Mereka mantau")["start"] + 0.2), ("pop", ph("sampai update")["start"] - 0.3),
       ("ping", wt("masuk ke", "otak")), ("pop", wt("Tiap chat", "chat") - 0.2), ("pop", wt("Tiap chat", "lead") - 0.2), ("pop", wt("Tiap chat", "catatan") - 0.2),
       ("ping", ph("kesimpen")["start"]), ("pop", wt("Jadi bukan", "sepuluh") - 0.25), ("click", ph("yang nggak saling")["start"] + 0.1),
       ("ping", ph("Tapi satu")["start"] + 0.1), ("pop", ph("yang jalanin")["start"] - 0.08), ("pop", ph("dan inget")["start"] - 0.08),
       ("pop", ph("Kalau tim")["start"] - 0.05), ("pop", ph("hal yang sama")["start"] - 0.1), ("pop", ph("ini jawabannya")["start"] - 0.2),
       ("click", ph("ini jawabannya")["start"] + 0.1), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
