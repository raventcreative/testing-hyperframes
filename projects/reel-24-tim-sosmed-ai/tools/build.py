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
tTidur = ph("terus lu tidur")["start"]; tBangun = ph("Pas bangun")["start"]; tCek = ph("Cek sim")["start"]
tCeo = ph("Di atas")["start"]; tMalem = ph("Tiap malem")["start"]; tBagi = ph("terus bagi")["start"]
tWeb = ph("Agent web")["start"]; tNama = wt("Agent web", "nama"); tLogo = wt("Agent web", "logo"); tHal = ph("sama halaman")["start"]
tDua = ph("dua puluh tujuh klinik")["start"]; tLay = ph("yang layak")["start"]; tEm = ph("dua puluh tujuh email")["start"]; tSesuai = ph("sesuai tiap")["start"]
tAda = ph("Ada satu")["start"]; tSalah = wt("Ada satu", "salah"); tCoret = wt("nyebut nama", "coret"); tTombol = ph("Tombol kirim")["start"]; tTangan = wt("Tombol kirim", "tangan")
tKlik = wt("tinggal klik", "klik"); tSatuK = ph("Satu kalimat, satu")["start"]; tTim = wt("Satu kalimat, satu", "tim"); tAkhir = ph("dan lu yang")["start"]
tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.05), ("click", tTidur), ("pop", tTidur + 0.35),
      ("pop", tBangun + 0.3), ("pop", tBangun + 0.7), ("pop", tBangun + 1.1), ("pop", tBangun + 1.5),
      ("whoosh", tCek + 0.18),                                   # zoom-through 1
      ("ping", tCeo + 0.1), ("click", tMalem + 0.25), ("whoosh", tBagi - 0.4), ("pop", tBagi + 0.2), ("pop", tBagi + 0.5), ("pop", tBagi + 0.8), ("ping", tBagi + 1.4),
      ("whoosh", tWeb - 0.6),                                    # pop-out + robot side-rise 1
      ("click", tNama + 0.1), ("pop", tLogo), ("sparkle", tHal + 0.9),
      ("whoosh", 16.66),                                         # sweep
      ("pop", tDua), ("ping", tDua + 1.3), ("pop", tLay + 0.1), ("whoosh", tLay + 0.3),   # top-3 pop-out + side-rise 2
      ("whoosh", 21.2),                                          # zoom punch-in 2
      ("click", tEm), ("ping", tEm + 2.0), ("pop", tSesuai + 0.05), ("pop", tSesuai + 0.45),
      ("whoosh", 26.36),                                         # doors
      ("pop", 27.9), ("pop", 28.35), ("pop", 28.8),
      ("whoosh", tAda + 0.35), ("ping", tSalah - 0.1), ("click", tCoret - 0.15),   # 3D split + side-rise 3
      ("whoosh", tTombol + 0.1), ("sparkle", tTangan), ("click", tKlik), ("ping", tKlik + 0.15),
      ("whoosh", 37.02),                                         # zoom-out reveal
      ("pop", tSatuK), ("pop", tTim - 0.4), ("pop", tAkhir - 0.1),
      ("whoosh", tCta - 0.45), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
