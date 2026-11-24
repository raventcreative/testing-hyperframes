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

tA = [S(x) for x in ["Nomor satu", "Nomor dua", "Nomor tiga", "Nomor empat", "Nomor lima",
                     "Nomor enam", "Nomor tujuh", "Nomor delapan, agent", "Nomor sembilan", "Dan nomor sepuluh"]]
tSim, tSepAg, tFav1 = S("Ini simulasinya"), S("Sepuluh agent AI"), S("Dan nomor delapan favorit")
tSep, tBales = S("Sepuluh kerjaan, satu"), S("Bales chat")
tFav, tKar, tInv, tDp = S("Nomor delapan favorit gue,"), S("karena dia"), S("Invoice kekirim"), S("DP diingetin")
tJalan, tJam, tTanpa, tCta = S("Sepuluh kerjaan ini jalan"), S("dua puluh empat jam"), S("Tanpa lu nambah"), S("Mau sistem")
tZ1, tW1, tBL, tW2 = tSim - 0.85, 14.295, 20.5, 24.82
tZ2, tZ3, tZ4 = tFav - 0.8, tJalan - 0.62, tCta - 0.75

# one quiet whoosh per transition / pop-out / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.1, tW1 + 0.2, tBL + 0.2, tW2 + 0.2, tA[5] - 0.15, tA[6] - 0.3, tZ2 + 0.05, tZ3, tZ4)]
# hook: the ten jobs drop into the queue, then the queue stalls
ev += [("pop", tBales + 0.12 + k * 0.33) for k in range(10)]
ev += [("ping", tSep - 0.3), ("pop", tSep - 0.1), ("click", tSep + 0.75)]
# roster: ten tiles light up, number eight gets the star
ev += [("pop", tSepAg + 0.18 + k * 0.2) for k in range(10)]
ev += [("sparkle", tFav1 + 0.35), ("ping", tFav1 + 0.4)]
# 01 chat
ev += [("pop", tA[0] + 0.18), ("pop", tA[0] + 0.62), ("ping", tA[0] + 1.02)]
# 02 follow up
ev += [("pop", tA[1] + 0.18 + k * 0.26) for k in range(3)]
# 03 booking
ev += [("pop", tA[2] + 0.42), ("click", tA[2] + 0.56), ("ping", tA[2] + 1.04)]
# 04 itinerary
ev += [("pop", tA[3] + 0.16 + k * 0.2) for k in range(4)]
# 05 vendor
ev += [("pop", tA[4] + 0.14 + k * 0.2) for k in range(3)] + [("ping", tA[4] + 0.72)]
# 06 konten pop-out
ev += [("pop", tA[5] + 0.26 + k * 0.26) for k in range(3)]
# 07 harga
ev += [("pop", tA[6] + 0.12), ("pop", tA[6] + 0.34), ("ping", tA[6] + 0.62)]
# 08 invoice teaser, 09 review, 10 laporan
ev += [("pop", tA[7] + 0.12), ("pop", tA[8] + 0.12), ("sparkle", tA[8] + 0.3), ("pop", tA[9] + 0.12), ("click", tA[9] + 0.78)]
# the favourite: invoice, DP reminders, lunas
ev += [("pop", tKar + 0.3), ("pop", tInv + 0.1), ("pop", tDp + 0.1), ("sparkle", tDp + 0.5), ("ping", tDp + 1.1)]
# 24/7 + CTA
ev += [("pop", tJalan + 0.08), ("sparkle", tJam - 0.1), ("pop", tTanpa - 0.1)]
ev += [("pop", tTanpa + 0.2 + k * 0.05) for k in range(10)]
ev += [("ping", tTanpa + 0.42), ("pop", tCta - 0.1), ("click", wt("Klik link", "link"))]

tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
