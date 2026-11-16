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
S = lambda s: ph(s)["start"]
tJalan = S("jalan sendiri"); tYang = S("Yang mikirin"); tSampai = S("sampai bales"); tCek = S("Cek sim"); tAtur = S("Aturannya"); tNggak = S("nggak ada"); tSebelumEnd = ph("sebelum lu")["end"]
tM1 = S("Modul satu"); tDeng = S("Dia dengerin"); tScan = S("terus scan"); tBukan = S("Bukan yang"); tTapi = S("tapi yang paling"); tKalau = S("kalau postingannya")
tSepuluh = wt("Tiap minggu, lu", "sepuluh"); tDariEnd = ph("dari apa")["end"]
tM2 = S("Modul dua"); tTulis = S("Tiap minggu dia"); tNaskah = S("sama tiga"); tAIv = S("AI video"); tDes = S("dan desain"); tTinggal = S("Lu tinggal"); tSetuju = wt("Lu tinggal", "setujuin")
tTayang = S("terus semuanya"); tMuncul = S("Jadi lu muncul"); tHari = wt("Jadi lu muncul", "hari"); tTanpaEnd = ph("tanpa ngabisin")["end"]
tM3 = S("Modul tiga"); tBacaS = S("Dia baca"); tNanya = S("Pas ada yang"); tAtau = S("atau, bisa"); tTandain = S("dia tandain"); tVN = S("Terus dia kirim"); tPlus = S("plus link"); tCall = S("Callnya"); tCallEnd = ph("Callnya")["end"]
tKeb = S("Kebanyakan"); tPasItu = S("Pas itu"); tPasEnd = ph("Pas itu")["end"]
tBrain = S("Yang ngatur"); tNP = wt("Dia nyambungin", "postingan"); tNK = wt("Dia nyambungin", "komentar"); tNC = wt("Dia nyambungin", "call"); tJadiLu = S("jadi lu tau"); tBen = wt("jadi lu tau", "beneran")
tSenin = S("Tiap Senin"); tBukanC = S("Bukan cuma"); tTapiL = S("Tapi lebih"); tCta = S("Mau sistem")
tZ1 = tCek - 0.85; tW2 = tSebelumEnd - 0.12; tZ3 = tDariEnd - 0.35; tW4 = tTanpaEnd - 0.15; tWb = tCallEnd - 0.05; tW6 = tPasEnd - 0.05; tZ6 = tSenin - 0.4
pop = lambda *ts: [("pop", t) for t in ts]
ev = pop(0.25, 0.43, 0.61, 0.79, 0.97) + [("pop", tJalan + 0.1), ("ping", tJalan + 0.3), ("click", tYang + 0.1), ("click", tSampai + 0.1),
      ("whoosh", tZ1 + 0.15),                                    # zoom-through 1 (roster -> app)
      ("pop", tCek + 0.3), ("click", tNggak - 0.05), ("ping", tNggak + 0.2), ("pop", tSebelumEnd - 0.5),
      ("whoosh", tW2),                                           # iris
      ("pop", tM1 + 0.15), ("pop", tDeng + 0.45), ("pop", tDeng + 0.85), ("pop", tScan + 0.1), ("pop", tScan + 0.22), ("pop", tScan + 0.34), ("ping", tTapi + 0.9),
      ("pop", tKalau + 0.1), ("pop", tKalau + 0.38), ("pop", tKalau + 0.66), ("pop", tKalau + 0.94),
      ("whoosh", tSepuluh + 0.1), ("ping", tSepuluh + 0.5),       # pop-out + robot side-rise 1
      ("whoosh", tZ3),                                           # zoom punch-in
      ("pop", tTulis + 0.2), ("pop", tTulis + 0.4), ("pop", tTulis + 0.6), ("pop", tNaskah + 0.2), ("pop", tNaskah + 0.4), ("pop", tNaskah + 0.6),
      ("ping", tAIv + 0.35), ("ping", tAIv + 0.8), ("ping", tAIv + 1.25),
      ("pop", tDes + 0.2), ("pop", tDes + 0.4), ("pop", tDes + 0.6),
      ("click", tSetuju), ("ping", tSetuju + 0.2),
      ("whoosh", tTayang - 0.05), ("pop", tTayang + 0.4), ("pop", tTayang + 0.56), ("pop", tTayang + 0.72), ("pop", tHari - 0.25),   # pop-out + robot side-rise 2
      ("whoosh", tW4),                                           # sweep
      ("pop", tM3 + 0.2), ("pop", tM3 + 0.4), ("pop", tM3 + 0.6), ("ping", tBacaS + 1.4),
      ("sparkle", tTandain + 0.15), ("sparkle", tTandain + 0.45),
      ("whoosh", tVN - 0.15), ("pop", tVN + 0.4), ("pop", tPlus + 0.1), ("ping", tCall + 0.2),   # pop-out + robot side-rise 3
      ("whoosh", tWb),                                           # blocks
      ("pop", tKeb + 0.1), ("pop", tPasItu + 0.2), ("sparkle", tPasItu + 1.5),
      ("whoosh", tW6),                                           # stripes
      ("pop", tNP - 0.05), ("pop", tNK - 0.05), ("pop", tNC - 0.05), ("pop", tJadiLu + 0.1), ("pop", tJadiLu + 0.26), ("pop", tJadiLu + 0.42), ("sparkle", tBen + 0.3),
      ("whoosh", tZ6),                                           # zoom-out reveal
      ("pop", tSenin + 0.1), ("pop", tBukanC + 0.2), ("click", tBukanC + 0.85), ("pop", tTapiL + 0.1),
      ("whoosh", tCta - 0.45), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
