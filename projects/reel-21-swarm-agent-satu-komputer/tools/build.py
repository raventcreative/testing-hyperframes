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
# measured silent gaps of the padded VO (same constants as in the composition)
G2, G3, G5 = 11.28, 28.84, 39.90
tZ1 = 5.95; tW2 = G2 + 0.02; tMecah = ph("mecah satu")["start"]; tPar = ph("Terus semuanya")["start"]; tPoA = tPar + 0.95
tDes = ph("ada yang nulis")["start"]; tStuck = ph("Kalau ada yang")["start"]; tHand = ph("oper tugasnya")["start"]; tW3 = G3 - 0.02
tPoB = ph("halaman produk")["start"] - 0.1; tCek = ph("Tinggal lu cek")["start"]; tRec = tCek + 0.62; tW5 = G5 - 0.04
tCap = ph("ada yang bikin")["start"]; tLu = ph("Lu tinggal")["start"]; tAp = wt("Lu tinggal", "approve")
ev = [("whoosh", t) for t in (tZ1 + 0.1, tW2, tMecah - 0.3, tPoA, tDes - 0.04, tCap - 0.3, tStuck - 0.3, tHand, tW3, tPoB, tRec, tW5)]
ev += [("pop", 0.1), ("pop", 0.45), ("sparkle", ph("dua puluh empat agent AI")["start"] + 0.2), ("pop", ph("semuanya kerja")["start"] + 0.05), ("click", ph("di detik")["start"] + 0.3),
       ("pop", ph("di detik")["start"] + 0.02), ("ping", ph("Gue tunjukin")["start"] + 0.3), ("click", ph("Tugasnya")["start"] + 0.3), ("ping", ph("Pertama")["start"] + 0.5),
       ("pop", tMecah + 0.3), ("pop", tMecah + 0.7), ("pop", ph("jadi dua puluh empat tugas")["start"] + 0.2), ("sparkle", tPar + 0.05),
       ("pop", wt("Ada yang riset", "harga")), ("pop", wt("Ada yang riset", "harga") + 0.3), ("ping", wt("Ada yang riset", "kompetitor") + 0.1),
       ("pop", ph("ada yang nulis")["start"] + 0.3), ("pop", tCap + 0.2), ("pop", ph("ada yang nyiapin")["start"] + 0.2),
       ("click", tStuck + 0.05), ("pop", tStuck + 0.1), ("ping", tHand + 1.15), ("sparkle", ph("Hasilnya digabung")["start"] + 0.5),
       ("pop", wt("halaman produk", "halaman") + 0.3), ("pop", wt("halaman produk", "caption") + 0.3), ("pop", ph("sama jadwal")["start"] + 0.3), ("ping", tCek),
       ("pop", ph("Satu tugas gede")["start"] - 0.05), ("pop", ph("dua puluh empat agent,")["start"] - 0.05), ("pop", ph("satu komputer.")["start"] - 0.05),
       ("click", tAp + 0.1), ("ping", tAp + 0.2), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
