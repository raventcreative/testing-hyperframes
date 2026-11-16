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
tZ1 = ph("Gue tunjukin")["start"] - 0.15
tW1 = ph("Agent riset")["start"] - 1.22
tZ2 = ph("Habis itu")["start"] - 0.85
tW3 = ph("Tapi draft")["start"] - 0.65
tW4 = ph("Di sini")["start"] - 0.30
tPoles = ph("terus poles")["start"] - 0.05
tZ5 = ph("Terakhir")["start"] - 0.82
tW6 = ph("AI nulis")["start"] - 0.2
tZ7 = ph("Mau sistem")["start"] - 0.75
# one quiet whoosh per transition / 3D swing
ev = [("whoosh", t) for t in (tZ1 + 0.1, tW1, tZ2 + 0.04, tW3, tW4 + 0.1, tPoles, tZ5, tW6, ph("Tujuh konten")["start"] - 0.5, tZ7)]
# hook
ev += [("pop", 0.1), ("pop", 0.6), ("pop", 1.1), ("sparkle", wt("bisa kelar", "menit")), ("pop", wt("bisa kelar", "bisa") - 0.15),
       ("pop", ph("dua agent AI")["start"]), ("click", ph("dua agent AI")["start"] + 0.45), ("pop", ph("dua agent AI")["start"] + 0.55),
       ("ping", wt("dua agent AI", "bagi")), ("pop", wt("dua agent AI", "bagi") + 0.25)]
# brand voice file
ev += [("ping", ph("file brand")["start"]), ("pop", ph("niche")["start"]), ("pop", wt("niche", "audiens")), ("pop", ph("gaya ngomong")["start"]),
       ("pop", wt("sama tiga", "postingan")), ("pop", wt("sama tiga", "postingan") + 0.18), ("pop", wt("sama tiga", "postingan") + 0.36), ("ping", wt("sama tiga", "terbaik") + 0.1)]
# research
ev += [("pop", ph("banyak sumber")["start"] + 0.05 + k * 0.18 + 0.3) for k in range(0, 6, 2)]
ev += [("ping", ph("cari sepuluh")["start"] + 0.3), ("pop", ph("terus pilih")["start"] + 0.05), ("pop", ph("terus pilih")["start"] + 0.5), ("pop", ph("terus pilih")["start"] + 0.9),
       ("ping", wt("terus pilih", "terkuat")), ("click", tZ2)]
# table
ev += [("pop", ph("Habis itu")["start"] + 0.55), ("pop", ph("Senin sampai")["start"] - 0.05), ("pop", ph("Hook")["start"] + 0.05), ("pop", wt("Hook", "poin")),
       ("pop", ph("caption")["start"]), ("pop", wt("caption", "hashtag")), ("ping", ph("semuanya satu")["start"] + 0.1), ("click", ph("semuanya satu")["start"] + 1.0)]
# warning + editor
ev += [("pop", ph("Tapi draft")["start"] + 0.2), ("pop", ph("Tapi draft")["start"] + 0.52), ("pop", ph("Tapi draft")["start"] + 0.84), ("click", wt("gampang", "ketahuan") - 0.08),
       ("pop", ph("Di sini")["start"] + 1.1), ("pop", ph("Di sini")["start"] + 1.3), ("pop", ph("Di sini")["start"] + 1.5),
       ("sparkle", ph("Dia belajar")["start"] + 0.9), ("ping", ph("terus poles")["start"] + 0.6), ("pop", ph("terus poles")["start"] + 0.8),
       ("pop", ph("Fakta")["start"] - 0.05), ("pop", wt("Fakta", "angka") - 0.05), ("pop", ph("sumber nggak")["start"] - 0.05)]
# review + decision
ev += [("pop", ph("buka sumbernya")["start"]), ("ping", ph("buka sumbernya")["start"] + 0.5), ("pop", ph("cocokin")["start"]), ("ping", ph("cocokin")["start"] + 0.5),
       ("pop", ph("buang")["start"]), ("click", ph("buang")["start"] + 0.35), ("pop", ph("AI nulis")["start"] + 0.2), ("pop", ph("AI nulis")["start"] + 0.35), ("pop", ph("AI nulis")["start"] + 0.5),
       ("ping", ph("keputusan")["start"] + 0.2)]
# stats + CTA
ev += [("pop", ph("Tujuh konten")["start"] - 0.1), ("pop", wt("Tujuh konten", "dua") - 0.1), ("pop", ph("dua puluh menit")["start"] - 0.1), ("click", ph("dua puluh menit")["start"] + 0.3),
       ("pop", ph("Mau sistem")["start"] - 0.1), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
