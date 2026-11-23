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

# ---- transition anchors (mirror production/index.src.txt) ----
tZ1 = S("Cek simulasinya") - 0.78          # zoom through the hook
tZ2 = S("Agent pertama") - 0.72            # zoom into the agent node
tW1 = S("Terus dia baca") - 0.82           # slats
tW2 = S("Pas deal") - 0.80                 # iris
tSw = S("Tapi ada agent") - 0.36           # 3D swing + pop-out
tW3 = S("Baru disebar") - 0.80             # blocks
tW4 = S("Pembeli bales") - 0.46            # whip
tW5 = S("Habis closing") - 0.78            # sweep
tZ3 = S("Setahun kemudian") - 0.62         # pull back to the flywheel
tZ4 = S("Mau sistem") - 0.72               # zoom through to the CTA
ev = [("whoosh", t) for t in (tZ1 + 0.08, tZ2, tW1, tW2, tSw, tW3, tW4, tW5, tZ3 + 0.28, tZ4)]

# hook — midnight message, nobody awake, lead walks
ev += [("pop", S("ada yang nanya") - 0.3), ("pop", S("Lu lagi tidur") - 0.25), ("click", S("Besok siang") - 0.2),
       ("pop", S("dia udah ngobrol") + 0.15), ("ping", S("dia udah ngobrol") + 0.5)]
# agent ring
ev += [("pop", S("Sepuluh agent") - 0.2 + k * 0.088) for k in range(10)]
ev += [("ping", S("jalan dua puluh") - 0.12)]
# valuation
ev += [("pop", S("Agent pertama") - 0.1), ("pop", S("Agent pertama") + 0.02), ("ping", S("dalam hitungan") - 0.35)]
ev += [("pop", S("lengkap sama tiga") + 0.02 + k * 0.2) for k in range(3)]
# three paths
ev += [("pop", S("Terus dia baca") - 0.05)] + [("pop", S("Terus dia baca") + 0.52 + k * 0.14) for k in range(3)]
ev += [("pop", S("Mau jual sekarang") - 0.2), ("ping", S("jadwal ketemu") - 0.05),
       ("pop", S("Belum siap") - 0.18), ("pop", S("harganya dikirim") + 0.5),
       ("pop", S("Ngilang") - 0.18), ("click", S("hari kedua") - 0.1), ("click", S("hari kedua") + 0.32), ("pop", S("hari kedua") + 0.75)]
# listing photos -> description
ev += [("pop", S("Pas deal") + 0.05 + k * 0.072) for k in range(6)]
ev += [("pop", S("deskripsinya ditulis") - 0.26), ("sparkle", S("deskripsinya ditulis") - 0.15), ("pop", S("deskripsinya ditulis") + 0.72)]
# rule check
ev += [("pop", S("Tapi ada agent") + 0.18 + k * 0.26) for k in range(3)]
ev += [("pop", S("Kalimat yang") + 0.42), ("click", S("ditandain") - 0.12), ("pop", S("ditandain") + 0.3), ("ping", S("ditandain") + 0.62)]
# fan-out
ev += [("pop", S("Baru disebar") - 0.05), ("pop", S("Baru disebar") + 0.36), ("pop", S("portal listing") - 0.2), ("pop", S("sama pembeli") - 0.22), ("sparkle", S("sama pembeli") + 0.1)]
# buyer, showing, sold
ev += [("pop", S("Pembeli bales") - 0.1 + k * 0.42) for k in range(3)]
ev += [("ping", S("jadwal survei") - 0.12), ("pop", S("alamat kekirim") - 0.12), ("sparkle", wt("alamat kekirim", "Rumah") - 0.2)]
# after closing + flywheel
ev += [("pop", S("Habis closing") - 0.05)] + [("pop", S("Habis closing") + 0.42 + k * 0.1) for k in range(5)]
ev += [("pop", S("terus kirim update") - 0.18)]
ev += [("pop", S("Setahun kemudian") - 0.05 + k * 0.17) for k in range(5)]
ev += [("ping", S("Temennya jadi lead") - 0.14)] + [("pop", S("muter lagi") + 0.02 + k * 0.13) for k in range(3)]
# CTA
ev += [("pop", S("Mau sistem") - 0.1), ("click", wt("Klik link di bio", "link"))]

# spread across enough tracks that no two overlapping clips share one (the longest clip is 1.8 s)
ev = sorted(ev, key=lambda e: e[1])
free, tags = {}, []
for i, (k, t) in enumerate(ev):
    t = max(0.0, t)
    lane = next((n for n in range(10, 30) if free.get(n, -1) <= t + 1e-6), 10)
    free[lane] = t + DUR[k]
    tags.append(f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{lane}" data-volume="{VOL[k]}"></audio>')
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
