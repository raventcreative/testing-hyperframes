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
tSib = ph("lu lagi sibuk")["start"]; tNgk = ph("nggak ada")["start"]; tPad = ph("Padahal")["start"]; tBk = ph("yang mau booking")["start"]; tCek = ph("Cek sim")["start"]
tNgang = wt("Resepsionis", "ngangkat"); tNyapa = ph("nyapa")["start"]; tNawar = wt("nyapa", "nawarin"); tKosong = ph("jam yang")["start"]
tSeb = wt("Selasa jam", "sebelas"); tNama = wt("AI langsung", "nama"); tNomor = ph("nomor")["start"]; tLayS = ph("sama layanannya")["start"]
tUlang = ph("Terus dia")["start"]; tSem = wt("Terus dia", "semuanya"); tKonf = ph("buat konfirmasi")["start"]; tBiar = ph("biar nggak")["start"]; tBiarE = ph("biar nggak")["end"]
tIni = ph("ini AI")["start"]; tJujur = ph("Dia jawab")["start"]; tSamb = ph("dan nawarin")["start"]; tOrang = ph("ke orang")["start"]; tOrE = ph("ke orang")["end"]
tJad = ph("jadwal masuk")["start"]; tKal = wt("jadwal masuk", "kalender"); tKonf2 = ph("dan konfirmasi")["start"]; tWA = ph("ke WhatsApp")["start"]; tWAE = ph("ke WhatsApp")["end"]
tBukan = ph("Bukan lagi")["start"]; tTapi = ph("Tapi satu")["start"]; tYang = ph("yang jaga")["start"]; tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.05), ("ping", 0.3), ("pop", tSib - 0.05), ("pop", tNgk - 0.1), ("pop", tPad - 0.1), ("whoosh", tBk + 0.02),
      ("whoosh", tCek + 0.04),                                   # zoom-through 1
      ("ping", tNgang), ("pop", tNyapa), ("pop", tNyapa + 0.6), ("pop", tNawar), ("pop", tKosong),
      ("click", tSeb + 0.05), ("whoosh", tSeb + 0.3),            # zoom punch-in 2
      ("click", tNama), ("click", tNomor + 0.05), ("click", tLayS + 0.1),
      ("whoosh", tUlang - 0.18),                                 # pop-out
      ("ping", tSem), ("pop", tKonf), ("sparkle", tBiar + 0.3),
      ("whoosh", tBiarE + 0.1),                                  # 3D tilt
      ("pop", tIni - 0.15), ("pop", tJujur), ("pop", tSamb + 0.05), ("ping", tOrang),
      ("whoosh", tOrE),                                          # doors
      ("pop", tJad + 0.05), ("sparkle", tKal - 0.05),
      ("whoosh", tKonf2 - 0.3),                                  # WhatsApp pop-out
      ("pop", tKonf2 + 0.15), ("ping", tWA),
      ("whoosh", tWAE + 0.04),                                   # stripes
      ("pop", tBukan - 0.2), ("pop", tTapi - 0.12), ("pop", tYang - 0.1),
      ("whoosh", tCta - 0.5), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
