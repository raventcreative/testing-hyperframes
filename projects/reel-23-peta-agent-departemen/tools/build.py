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
phn = lambda s, n: [p for p in PH if p["text"].startswith(s)][n]
def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.8}
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.035}
tSim = ph("Ini simulasinya")["start"]; tStas = ph("tiap stasiun")["start"]; tClick = tStas + 0.95
tOps = ph("Jalur operasional")["start"]; tKeu = ph("Jalur keuangan")["start"]; tPagi = ph("Tiap pagi")["start"]
tAg = ph("Tiap agent")["start"]; tCta = ph("Mau sistem")["start"]
tCall = ph("satu lagi jadwalin")["start"]; tInv = ph("Invoice keluar")["start"]
tZ5 = ph("dan pembukuan")["end"] - 0.12
ev = [("whoosh", t) for t in (tSim - 0.85 + 0.1, tClick + 0.05, tCall + 0.4, tOps - 0.95, tKeu - 0.95, tInv + 0.85, ph("yang telat")["start"] - 0.15,
                              tZ5, tPagi - 0.35, tAg - 0.4, tCta - 0.85)]
ev += [("pop", 0.1), ("pop", ph("berapa agent")["start"]), ("sparkle", ph("Gue petain")["start"] + 0.5), ("pop", ph("di satu halaman")["start"] + 0.1), ("click", ph("di satu halaman")["start"] + 0.2),
       ("pop", ph("Kayak peta")["start"] + 0.1), ("ping", ph("tiap jalur")["start"] + 0.2), ("pop", ph("tiap stasiun")["start"] + 0.1), ("pop", ph("tiap stasiun")["start"] + 0.4),
       ("pop", ph("tiap stasiun")["start"] + 0.7), ("ping", ph("tiap stasiun")["start"] + 0.9), ("click", tClick),
       ("ping", wt("Satu agent kasih", "skor") + 0.9), ("pop", ph("satu nulis")["start"] + 1.35), ("pop", tCall + 0.6), ("ping", tCall + 1.9),
       ("pop", ph("Klien baru")["start"] + 0.2), ("pop", ph("Klien baru")["start"] + 0.6), ("pop", ph("Klien baru")["start"] + 1.0), ("ping", ph("dan update")["start"] + 1.0),
       ("pop", ph("sebelum ada")["start"] + 0.05), ("pop", ph("Invoice keluar")["start"] + 0.5), ("click", wt("Invoice keluar", "tepat")), ("ping", tInv + 1.9),
       ("pop", ph("yang telat")["start"]), ("pop", ph("yang telat")["start"] + 0.7), ("ping", ph("dan pembukuan")["start"] + 1.2),
       ("pop", ph("Dia baca")["start"] + 0.4), ("pop", ph("Dia baca")["start"] + 0.65), ("pop", phn("apa yang macet", 0)["start"] + 0.1), ("ping", ph("terus balikin")["start"] + 0.3),
       ("pop", ph("Apa yang closing")["start"]), ("pop", phn("apa yang macet", 1)["start"]), ("pop", ph("dan tiga hal")["start"]), ("click", ph("dan tiga hal")["start"] + 0.35),
       ("pop", tAg + 0.3), ("pop", tAg + 0.9), ("pop", tAg + 1.5), ("ping", ph("jadi lu bisa")["start"] + 0.1),
       ("pop", ph("apa yang dia")["start"]), ("click", ph("apa yang dia")["start"] + 0.8), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 14}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
