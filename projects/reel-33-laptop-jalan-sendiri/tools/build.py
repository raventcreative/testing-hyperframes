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

tLap = S("Laptop gue ngerjain")
tMall = S("gue lagi makan")
tOke = S("tinggal bales oke")
tCek = S("Cek simulasinya.")
tNyala = S("Sistemnya nyala sendiri")
tSore = wt("Sistemnya nyala sendiri", "sore")
tBukan = S("Ini bukan satu prompt")
tEmpat = S("tapi empat bagian.")
tB1 = S("Bagian satu:")
tJadwal = wt("Bagian satu:", "jadwal")
tGanti = S("Mau ganti alurnya?")
tEdit = S("Edit file itu aja.")
tB2 = S("Bagian dua:")
tStatus = wt("Bagian dua:", "statusnya")
tB3 = S("Bagian tiga:")
tBiar = S("Biar gaya videonya")
tB4 = S("Bagian empat:")
tSekali = S("sekali jalan.")
tAbis = S("Pas topiknya abis,")
tRiset = S("dia riset sendiri,")
tLima = S("terus kirim lima ide")
tBales = S("Tinggal bales nomornya,")
tMana = S("dari mana aja.")
tAlur = S("Alurnya simpel: dia kerja,")
tKabar = S("kirim kabar,")
tCekN = S("gue cek,")
tOkeN = S("gue bilang oke.")
tNggak = S("Nggak ada yang ke-posting")
tGerbang = S("Ada tiga gerbang: topik,")
tNaskah = S("naskah,")
tPreview = S("preview.")
tKeputusan = S("Keputusan akhir tetep")
tCta = S("Mau sistem kayak gini")

# transition timings mirrored from production/index.src.txt
tZ1 = tCek - 0.72          # zoom punch-through the laptop screen into the app
tT2 = tBukan - 0.55        # tab click -> "isi sistemnya"
tW1 = tB1 - 0.62           # iris -> guide file
tT3 = tB2 - 0.6            # camera slide -> week table
tW2 = tB3 - 0.62           # doors -> style cards
tZ2 = tB4 - 0.68           # zoom punch-in -> waveform
tSw = tAbis - 0.4          # 3D swing + phone pop-out
tZ3 = tAlur - 0.6          # zoom-out reveal -> flow chain
tW3 = tNggak - 0.6         # sweep -> approval gates
tZ4 = tCta - 0.72          # zoom through into the CTA

# one quiet whoosh per transition / swing / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.1, tT2 - 0.05, tW1, tT3, tW2, tZ2 + 0.04, tSw, tZ3, tW3, tZ4)]
# S1 hook: render finishing on the laptop, the phone asking, the OK tapped
ev += [("pop", tLap + 0.12), ("ping", tLap + 1.05), ("sparkle", 3.3)]
ev += [("pop", tMall + 0.05), ("pop", tMall + 0.6)]
ev += [("click", tOke + 0.6), ("ping", tOke + 1.05)]
# S2 schedule dial
ev += [("pop", tNyala + 0.1)] + [("pop", tNyala + 0.5 + k * 0.24) for k in range(3)]
ev += [("pop", tNyala + 0.25), ("click", tSore - 0.05)]
# S3 one prompt -> four lanes
ev += [("click", tT2 - 0.05), ("pop", tT2 + 0.12)]
ev += [("pop", tEmpat - 0.28 + k * 0.17) for k in range(4)]
# S4 guide file
ev += [("pop", tB1 + 0.16)] + [("pop", tJadwal - 0.2 + k * 0.18) for k in range(3)]
ev += [("pop", tGanti + 0.1), ("click", tEdit + 0.1)]
# S5 week table
ev += [("pop", tT3 + 0.42), ("pop", tB2 + 0.5)]
ev += [("pop", tStatus - 0.5 + k * 0.16) for k in range(3)] + [("ping", tStatus)]
# S6 style cards
ev += [("pop", tB3 + 0.12), ("pop", tB3 + 0.34)]
ev += [("pop", tB3 + 0.75 + k * 0.16) for k in range(3)] + [("sparkle", tBiar + 0.55)]
# S7 script -> waveform
ev += [("pop", tB4 + 0.5), ("sparkle", tB4 + 0.95), ("pop", tSekali - 0.2), ("pop", tSekali + 0.1)]
# S8 ideas on the phone
ev += [("pop", tRiset - 0.1)] + [("pop", tLima + 0.05 + k * 0.17) for k in range(5)]
ev += [("click", tBales + 0.25), ("ping", tBales + 0.35)]
# S9 flow chain
ev += [("pop", t) for t in (tAlur + 0.15, tKabar, tCekN, tOkeN)] + [("sparkle", tOkeN + 0.5)]
# S10 gates
ev += [("pop", tNggak + 0.1), ("click", tNggak + 0.75)]
ev += [("pop", t) for t in (tGerbang + 0.1, tNaskah, tPreview)]
ev += [("ping", t + 0.18) for t in (tGerbang + 0.1, tNaskah, tPreview)]
ev += [("pop", tKeputusan - 0.3)]
# CTA
ev += [("pop", tZ4 + 0.34), ("click", wt("Klik link di bio,", "link"))]

ev = [(k, t) for k, t in ev if t >= 0]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
