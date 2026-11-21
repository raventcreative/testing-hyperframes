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
S = lambda s: ph(s)["start"]
tZ1 = S("Gue tunjukin") - 0.15
tSplit = S("Nah, di situ") - 0.55
tW1 = S("Setelah tau") - 1.2
tZ2 = S("Terus kasih") - 0.85
tSplit2 = S("Copy kayak") - 0.05
tW5 = S("Berikutnya") - 1.2
tW6 = S("Dan yang ngatur") - 1.15
tSplit3 = S("dan satu penawaran") + 1.0
tZ7 = S("Mau sistem") - 0.75
# one quiet whoosh per transition / 3D swing / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.1, tSplit, tW1, tZ2 + 0.04, tSplit2, tW5, tW6, S("Tiap Senin") - 0.5, tSplit3, tZ7)]
# hook
ev += [("pop", wt("Salah baca", "mahal") - 0.25), ("pop", S("satu departemen") + 0.2), ("sparkle", S("isinya tiga") + 0.4), ("ping", S("isinya tiga") + 1.4),
       ("pop", wt("Mereka tau", "pelanggan") - 0.2), ("pop", S("apa yang kompetitor")), ("pop", S("dan di mana")), ("click", wt("Jadi lu berhenti", "nebak") + 0.12),
       ("pop", S("dan mulai jualan") + 0.4), ("ping", S("yang emang") + 0.3)]
# competitor intel
ev += [("pop", S("Pertama, intel") + 0.2), ("pop", S("Pertama, intel") + 0.4), ("pop", S("Pertama, intel") + 0.6), ("pop", S("penawaran mereka")), ("pop", wt("penawaran mereka", "harga")),
       ("pop", S("review mereka")), ("pop", S("Layanan yang")), ("pop", S("Keluhan yang")), ("ping", S("Nah, di situ") + 0.3)]
# customer voice
ev += [("pop", S("yang nentuin") + 0.1), ("pop", S("yang nentuin") + 0.5), ("pop", S("yang nentuin") + 0.9), ("ping", S("Dia baca ratusan") + 0.4),
       ("pop", S("dalam bahasa") + 0.1), ("pop", S("dalam bahasa") + 0.4), ("pop", S("dalam bahasa") + 0.7), ("click", tZ2),
       ("pop", S("Terus kasih") - 0.2), ("pop", S("Terus kasih") + 0.1), ("pop", S("Terus kasih") + 0.4), ("ping", wt("yang dipakai orang", "siap")), ("pop", S("Copy kayak") + 0.8), ("ping", S("Copy kayak") + 1.3)]
# radar
ev += [("ping", S("Berikutnya") + 0.3)] + [("pop", S("yang bilang kapan") + 0.1 + k * 0.22) for k in range(5)] + [("pop", S("Dia nunjukin") + 0.1 + k * 0.14) for k in range(5)]
ev += [("ping", S("dan nandain") + 0.4), ("pop", S("Jadi lu launching") - 0.2), ("sparkle", wt("Jadi lu launching", "launching")), ("pop", wt("bukan dua bulan", "bulan")), ("pop", S("bukan dua bulan") + 0.9)]
# research brain
ev += [("pop", S("Dan yang ngatur") + 0.1), ("pop", S("Dan yang ngatur") + 0.32), ("pop", S("Dan yang ngatur") + 0.54), ("sparkle", S("otak risetnya")), ("pop", S("Tiap Senin") + 0.05),
       ("pop", S("Apa yang berubah")), ("pop", S("apa yang lagi ditanyain")), ("pop", S("dan satu penawaran") - 0.1), ("ping", S("dan satu penawaran") + 0.9),
       ("pop", tSplit3 + 0.55), ("pop", tSplit3 + 0.83), ("pop", tSplit3 + 1.11)]
# stats + CTA
ev += [("pop", S("Kompetitor lu nebak") - 0.05), ("pop", S("Kompetitor lu nebak") + 0.55), ("pop", S("Lu tau.") - 0.15), ("click", S("Lu tau.") + 0.25),
       ("pop", S("Mau sistem") - 0.1), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
