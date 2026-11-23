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

tMateri = S("Materi udah jadi,")
tIklan = S("iklan udah jalan,")
tSepi = S("terus sepi.")
tCek = S("Cek simulasinya.")
tUji = S("Ide lu diuji")
tSeblm = S("sebelum duitnya")
tPer = S("Pertama, tiga penasihat")
tHarga = S("harga, janji,")
tBedaD = S("sama bedanya di mana.")
tBikin = S("Terus dibikin seratus")
tBedaK = S("Beda kerjaan, beda dompet,")
tTanya = S("Satu-satu ditanya,")
tMau = S("Yang mau tiga puluh enam,")
tNggak = S("yang nggak enam puluh empat.")
tAlasan = S("Alasannya pakai bahasa")
tKmhl = S("Kemahalan.")
tKbyg = S("Nggak kebayang hasilnya.")
tDari = S("Dari situ ketahuan,")
tApaB = S("apa yang bikin yang nolak")
tAngka = S("Baru angkanya dicek:")
tUntung = S("untung per peserta,")
tBalik = S("balik modal di berapa orang,")
tMargin = S("marginnya berapa.")
tHasil = S("Hasil akhirnya cuma dua:")
tLayak = S("layak, atau belum layak.")
tOrang = S("Orang biasanya baru tau")
tAbis = S("setelah duitnya abis.")
tIniTau = S("Ini tau sebelum keluar sepeser.")
tInget = S("Tapi inget, pembelinya simulasi.")
tKalau = S("Kalau lolos,")
tUjiL = S("uji lagi ke orang beneran.")
tCta = S("Mau sistem kayak gini")

# transition timings mirrored from production/index.src.txt
tZ1 = tCek - 0.78          # zoom punch-through into the app
tT3 = tPer - 0.62          # tab click -> advisor table
tW1 = tBikin - 0.62        # stripes -> 100-buyer panel
tSplit = tMau - 0.52       # panel splits into MAU / NGGAK
tQ = tAlasan - 0.22        # 3D swing -> quote card
tW2 = tDari - 0.6          # shutter -> levers
tZ3 = tAngka - 0.72        # punch into the margin -> money view
tPm = tUntung + 0.1        # profit card out (robot rises right)
tFlip = tHasil - 0.5       # card flip -> verdict
tSlide = tOrang - 0.52     # slide -> comparison strips
tZ4 = tInget - 0.6         # window recedes -> SIMULASI caveat
tPr = tKalau - 0.2         # next-step card (robot rises left)
tZ5 = tCta - 0.72          # zoom through into the CTA

# one quiet whoosh per transition / swing / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.1, tT3 - 0.05, tW1, tSplit, tQ + 0.05, tW2, tZ3 + 0.04, tFlip, tSlide, tZ4, tZ5)]
# hook: launch click, check chips, empty board, burning ad spend
ev += [("click", tMateri - 0.25), ("ping", tMateri - 0.05)]
ev += [("pop", tMateri + 0.1 + k * 0.26) for k in range(3)]
ev += [("pop", tIklan + 0.35)] + [("pop", tSepi - 0.35 + k * 0.2) for k in range(3)]
# flow strip
ev += [("pop", tUji + 0.3 + k * 0.17) for k in range(5)] + [("ping", tSeblm + 0.1)]
# advisor table
ev += [("pop", tPer + 0.1 + k * 0.22) for k in range(3)]
ev += [("pop", tHarga + 0.05), ("pop", tHarga + 0.95), ("pop", tBedaD + 0.35)]
# 100-buyer panel
ev += [("sparkle", tBikin + 0.2), ("ping", tBikin + 2.3)] + [("pop", tBedaK + 0.05 + k * 0.42) for k in range(3)]
# ask + split
ev += [("ping", tTanya - 0.1), ("pop", tMau + 0.1), ("pop", tNggak + 0.1)]
# quotes
ev += [("pop", tKmhl - 0.2), ("pop", tKbyg - 0.2)]
# levers
ev += [("pop", tDari + 0.2), ("pop", tDari + 0.7), ("ping", tApaB + 0.15), ("ping", tApaB + 0.7)]
# money
ev += [("pop", tUntung - 0.15), ("pop", tBalik - 0.15), ("pop", tMargin - 0.3), ("pop", tPm + 0.1), ("click", tAngka + 0.1)]
# verdict + comparison
ev += [("pop", tHasil + 0.1), ("pop", tHasil + 0.3), ("sparkle", tLayak + 0.1)]
ev += [("pop", tOrang + 0.05), ("pop", tIniTau - 0.3), ("ping", tIniTau + 0.3)]
# caveat + next step + CTA
ev += [("pop", tInget + 0.15)] + [("pop", tUjiL - 0.1 + k * 0.3) for k in range(3)]
ev += [("pop", tCta - 0.1), ("click", wt("Klik link di bio,", "link"))]

ev = [(k, t) for k, t in ev if t >= 0]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
