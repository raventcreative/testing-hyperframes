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
tCek = ph("Cek sim")["start"]; tAIE = ph("layanan, hari")["end"]; tPel = ph("Pelanggan bilang")["start"]; tAI = ph("AI langsung")["start"]
tTaw = ph("jadi dia tawarin")["start"]; tTigaE = ph("jam empat tiga puluh.")["end"]; tSet = ph("Pelanggan setuju")["start"]
tBookW = wt("dan slotnya", "kebooking"); tBookE = ph("dan slotnya")["end"]; tBarisE = ph("satu baris")["end"]; tSS = wt("satu baris", "spreadsheet")
tTer = ph("Terakhir")["start"]; tSatu = ph("Satu telepon")["start"]; tTig3 = ph("tiga sistem")["start"]; tNgetik = ph("ngetik manual")["start"]; tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.05), ("pop", ph("pas lu udah")["start"] - 0.05), ("pop", ph("langsung cari")["start"] - 0.15), ("pop", ph("Sekarang")["start"] - 0.05),
      ("pop", wt("yang ngangkat", "ngangkat") - 0.2), ("pop", wt("yang ngangkat", "ngatur") - 0.2), ("pop", wt("dan nyatet", "nyatet") - 0.2),
      ("whoosh", tCek + 0.04),                                   # zoom-through 1
      ("ping", ph("Pelanggan bilang")["start"] + 0.1),
      ("whoosh", tAI - 0.5), ("pop", wt("layanan, hari", "layanan")), ("pop", wt("layanan, hari", "hari")), ("pop", wt("layanan, hari", "jamnya") - 0.1),
      ("whoosh", tAIE + 0.03),                                   # iris
      ("pop", wt("Jam empat udah", "penuh") - 0.1),
      ("whoosh", tTaw - 0.5), ("pop", ph("jam empat tiga puluh.")["start"] - 0.1),
      ("whoosh", tTigaE - 0.12),                                 # zoom punch-in 2
      ("click", tSet + 0.35), ("ping", tSet + 0.45), ("ping", tBookW - 0.1),
      ("whoosh", tBookE + 0.03),                                 # shutter
      ("pop", ph("nama, nomor")["start"]), ("pop", wt("nama, nomor", "nomor")), ("pop", ph("dan layanannya")["start"]), ("sparkle", tSS - 0.15),
      ("whoosh", tBarisE + 0.03),                                # zoom-out reveal 3
      ("ping", tTer + 0.1), ("whoosh", tTer - 0.5), ("pop", ph("jadwal Kakak")["start"]), ("ping", ph("jam empat tiga puluh, ya")["start"] + 0.1),
      ("whoosh", tSatu - 0.5), ("pop", tSatu - 0.05), ("pop", tTig3 - 0.05), ("pop", tNgetik),
      ("whoosh", tCta - 0.5), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
