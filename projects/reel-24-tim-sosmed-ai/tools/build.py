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
tIsi = ph("isinya")["start"]; tYang = ph("Yang mikirin")["start"]; tSampai = ph("sampai bales")["start"]; tCek = ph("Cek sim")["start"]
tAtur = ph("Aturannya")["start"]; tNggak = ph("nggak ada")["start"]; tSebelumEnd = ph("sebelum lu")["end"]
tPert = ph("Pertama")["start"]; tBaca = ph("baca komentar di")["start"]; tBuat = ph("buat nyari")["start"]; tTiap = ph("Tiap minggu")["start"]
tKedua = ph("Kedua")["start"]; tCap = ph("caption dan")["start"]; tDes = ph("agent desain")["start"]; tSemua = ph("Semuanya")["start"]
tTinggal = ph("Lu tinggal")["start"]; tSetuju = wt("Lu tinggal", "setujui"); tJadwal = ph("dan jadwalnya")["start"]
tKetiga = ph("Ketiga")["start"]; tBacaS = ph("baca semua")["start"]; tNanya = ph("Yang nanya")["start"]; tDit = ph("ditandain")["start"]
tDibales = ph("Dibales")["start"]; tLengkap = ph("lengkap sama")["start"]
tTerakhir = ph("Terakhir")["start"]; tPost = wt("postingan, komentar", "postingan"); tKom = wt("postingan, komentar", "komentar"); tBook = wt("postingan, komentar", "booking")
tJadi = ph("Jadi lu tau")["start"]; tYangB = ph("yang beneran")["start"]; tTiapS = ph("Tiap Senin")["start"]; tSatuH = ph("satu halaman")["start"]
tCta = ph("Mau sistem")["start"]
tZ1 = tCek - 0.85; tW2 = tSebelumEnd - 0.05; tZ3 = tTiap + 1.45; tW4 = tJadwal + 2.0; tW5 = tLengkap + 1.0; tZ6 = tTiapS - 0.4
ev = [("pop", 0.25), ("pop", 0.43), ("pop", 0.61), ("pop", 0.79), ("pop", 0.97), ("pop", tIsi + 0.1), ("ping", tIsi + 0.3),
      ("click", tYang + 0.15), ("click", tSampai + 0.1),
      ("whoosh", tZ1 + 0.15),                                    # zoom-through 1 (roster -> app)
      ("pop", tCek + 0.3), ("click", tNggak - 0.05), ("ping", tNggak + 0.2), ("pop", tSebelumEnd - 0.5),
      ("whoosh", tW2),                                           # iris
      ("pop", tPert + 0.1), ("pop", tPert + 0.3), ("pop", tPert + 0.5), ("ping", tBaca + 0.9),
      ("pop", tBuat + 0.1), ("pop", tBuat + 0.4), ("pop", tBuat + 0.7), ("pop", tBuat + 1.0),
      ("whoosh", tTiap - 0.45), ("ping", tTiap + 0.3),            # pop-out + robot side-rise 1
      ("whoosh", tZ3),                                           # zoom punch-in
      ("pop", tKedua + 0.2), ("pop", tKedua + 0.4), ("pop", tKedua + 0.6), ("pop", tCap + 0.2), ("pop", tCap + 0.4), ("pop", tCap + 0.6),
      ("pop", tDes + 0.2), ("pop", tDes + 0.4), ("pop", tDes + 0.6),
      ("click", tSetuju), ("ping", tSetuju + 0.2),
      ("whoosh", tJadwal - 0.1), ("pop", tJadwal + 0.4), ("pop", tJadwal + 0.56), ("pop", tJadwal + 0.72),   # pop-out + robot side-rise 2
      ("whoosh", tW4),                                           # sweep
      ("pop", tKetiga + 0.2), ("pop", tKetiga + 0.4), ("pop", tKetiga + 0.6), ("ping", tBacaS + 1.4),
      ("sparkle", tDit + 0.15), ("whoosh", tDibales - 0.2), ("pop", tLengkap + 0.1), # pop-out + robot side-rise 3
      ("whoosh", tW5),                                           # stripes
      ("pop", tTerakhir + 0.2), ("pop", tPost + 0.05), ("pop", tBook - 0.05), ("pop", tJadi + 0.1), ("pop", tJadi + 0.26), ("pop", tJadi + 0.42), ("sparkle", tYangB + 0.3),
      ("whoosh", tZ6),                                           # zoom-out reveal
      ("pop", tTiapS + 0.1), ("pop", tSatuH + 0.2), ("pop", tCta - 0.95),
      ("whoosh", tCta - 0.45), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
