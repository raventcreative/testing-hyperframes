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
tNung = ph("tapi harus nunggu")["start"]; tSehari = wt("tapi harus nunggu", "seharian"); tAna = ph("Analis data")["start"]; tWf = wt("Analis data", "workflow"); tOrg = ph("bukan orang")["start"]
tCek = ph("Cek sim")["start"]; tChat = ph("Lu cukup chat")["start"]; tOm = ph("omzet Maret")["start"]; tBaca = ph("AI baca")["start"]; tBuka = ph("terus buka")["start"]; tBukaE = ph("terus buka")["end"]
tFil = ph("Dia filter")["start"]; tDari = ph("dari Maret")["start"]; tRef = ph("Yang refund")["start"]; tCuma = ph("Cuma yang")["start"]; tCumaE = ph("Cuma yang")["end"]
tSum = ph("Terus semuanya")["start"]; tKirim = ph("dan jawabannya")["start"]; tWaLu = ph("ke WhatsApp lu")["start"]; tWaLuE = ph("ke WhatsApp lu")["end"]
tBon = ph("Bonusnya")["start"]; tTik = ph("penjualan TikTok")["start"]; tRefP = ph("tapi refund")["start"]; tSatu = ph("dari satu produk")["start"]; tSatuE = ph("dari satu produk")["end"]
tLap = ph("Nggak perlu buka")["start"]; tRum = ph("nggak perlu rumus")["start"]; tNya = ph("Tinggal nanya")["start"]; tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.1), ("pop", tNung), ("pop", tSehari - 0.05), ("whoosh", tAna - 0.1), ("pop", tWf), ("pop", tOrg - 0.05),
      ("whoosh", tCek + 0.04),                                   # zoom-through 1
      ("pop", tOm - 0.1), ("click", tOm + 0.05), ("pop", tBaca + 0.15), ("pop", tBaca + 0.43), ("pop", tBaca + 0.71), ("ping", tBaca + 1.0),
      ("pop", tBuka + 0.05),
      ("whoosh", tBukaE - 0.8),                                  # zoom punch-in 2
      ("pop", tDari + 0.1), ("whoosh", tRef - 0.17),             # whip to status
      ("pop", tRef + 0.35), ("pop", tRef + 0.63), ("pop", tRef + 0.91), ("pop", tRef + 1.19), ("ping", tCuma + 0.45),
      ("whoosh", tCumaE - 0.2),                                  # slats
      ("ping", tSum + 1.6), ("pop", tSum + 0.3),
      ("whoosh", tKirim - 0.45), ("pop", tKirim + 0.6), ("sparkle", tWaLu + 0.1),
      ("whoosh", tWaLuE - 0.2),                                  # blocks
      ("pop", tTik + 0.1), ("ping", tTik + 1.1),
      ("whoosh", tRefP - 0.75), ("pop", tRefP + 0.1), ("ping", tSatu),
      ("whoosh", tSatuE - 0.24),                                 # zoom-out reveal
      ("pop", tLap), ("pop", tRum - 0.1), ("pop", tNya - 0.1),
      ("whoosh", tCta - 0.5), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
