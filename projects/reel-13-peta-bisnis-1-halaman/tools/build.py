"""Assemble index.html from production/index.src.txt: static SFX <audio> tags timed from production/word_timing.json
(times mirror the composition script). The 3D robot is added afterwards by tools/add_robot3d.py.
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
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.0}
VOL = {"whoosh": 0.055, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.04}
tBer = wt("Bisnis lu", "berantakan"); tItu = ph("Itu karena")["start"]; tNy = wt("Itu karena", "nyangkut")
tCoba = ph("Coba lihat")["start"]; tKlik = wt("Sekali klik", "klik"); tHal = wt("di satu", "halaman")
tPal = ph("Paling atas")["start"]; tKeb = wt("kebaca", "kebaca"); tGes = ph("Geser dikit")["start"]
tTech = wt("Geser dikit", "tech"); tAtur = wt("aset, sampai", "aturan"); tTiap = ph("Tiap divisi")["start"]
DN = [wt("marketing", "marketing"), wt("marketing", "sales"), wt("customer", "customer"), wt("customer", "keuangan"), wt("sampai otomasi", "otomasi")]
tKF = ph("Klik funnel")["start"]; tAs = ph("dari orang")["start"]; tPem = wt("sampai jadi", "pembeli"); tAng = wt("lengkap", "angkanya")
tTer = ph("Terus AI")["start"]; tKas = ph("dan kasih")["start"]; tTiga = wt("tiga prioritas", "tiga")
tSatu = ph("Satu halaman")["start"]; tSem = ph("semua divisi")["start"]; tNgg = ph("nggak ada")["start"]
tCta = ph("Mau sistem")["start"]; tF = wt("Klik link", "link")
tS1 = tCoba - 1.35; tS2 = tTiap - 1.15; tP = tKF + 0.18
ev = [("pop", 0.03), ("pop", 0.33), ("pop", 0.53), ("click", tBer - 0.02), ("whoosh", tItu + 0.3), ("pop", tItu + 0.85), ("pop", tNy - 0.1),
      ("whoosh", tS1), ("click", tKlik), ("whoosh", tKlik + 0.3), ("ping", tHal - 0.1),
      ("click", tPal + 0.1), ("whoosh", tPal + 0.35), ("sparkle", tKeb - 0.1), ("whoosh", tGes - 0.42),
      ("whoosh", tGes), ("pop", tTech - 0.15), ("whoosh", tAtur - 0.42), ("pop", tAtur + 0.05),
      ("whoosh", tS2)] + [("pop", t - 0.12) for t in DN] + [
      ("click", tKF), ("whoosh", tP), ("pop", tP + 0.75), ("ping", tPem - 0.05), ("pop", tAng - 0.25),
      ("whoosh", tTer - 0.05), ("pop", wt("Terus AI", "baca") - 0.1), ("ping", tTiga - 0.1), ("pop", tTiga + 0.25),
      ("whoosh", tSatu - 0.62), ("pop", tSatu - 0.15), ("pop", tSem - 0.15), ("pop", tNgg - 0.15),
      ("whoosh", tCta - 0.6), ("pop", tCta + 0.55), ("click", tF)]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
