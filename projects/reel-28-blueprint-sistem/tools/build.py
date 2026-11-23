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

tMimpi, tKantor, tIsinya, tLampu = S("Itu bukan"), S("Itu kantor"), S("Isinya agent"), S("lampunya")
tProp, tJadi, tSet7 = S("proposal buat"), S("udah jadi"), S("Jam setengah")
tDulu, tTiga = S("Dulu gue"), S("Tiga peran")
tOrang, tNol = wt("Tiga peran", "satu"), wt("Tiga peran", "nol")
tK1, tBrief, tUbah, tTamu = S("Karyawan pertama"), S("Tiap brief"), S("dia ubah"), S("jumlah tamu")
tMenu, tHarga = wt("jumlah tamu", "menu"), wt("jumlah tamu", "harga")
tK2, tAcc, tPecah, tBelanja = S("Karyawan kedua"), S("Proposal yang"), S("dia pecah"), S("belanja, sama")
tCrew = wt("belanja, sama", "crew")
tK3, tAnalis, tEvent, tSaring, tUntung = S("Karyawan ketiga"), S("agent analis"), S("Tiap event"), S("dia nyaring"), S("yang beneran")
tLolos, tKirim, tPutaran, tTajam = S("Paket yang"), S("dikirim balik"), S("Jadi tiap"), S("penawarannya")
t247, tSuruh = S("Semua ini"), S("tanpa gue")
tLega, tBukan, tArah, tNgerjain, tNgatur = S("Yang bikin"), S("bukan jumlah"), S("Tapi gue"), S("Gue nggak"), S("Gue ngatur")
tCta, tF = S("Mau sistem"), wt("Klik link", "link")

# one quiet whoosh per transition (zoom 1, doors, zoom 2, card flip, stripes, zoom-out, rotate-morph, sweep, zoom-through)
ev = [("whoosh", t) for t in (tMimpi + 0.35, tDulu - 0.86, tK1 - 0.72, tK2 - 0.62, tK3 - 0.9, tLolos - 0.66, t247 - 0.58, tLega - 0.82, tCta - 0.78)]
# hook: the night rail, the finished proposal
ev += [("pop", tSet7 - 0.1), ("pop", tProp - 0.1), ("ping", tJadi + 0.05)]
# office: floors, lights, chip
ev += [("pop", tKantor - 0.15 + k * 0.14) for k in range(3)]
ev += [("pop", tIsinya + 0.1 + k * 0.22) for k in range(3)] + [("sparkle", tLampu), ("pop", tLampu + 0.45)]
# the one-person pain
ev += [("pop", tDulu + 0.25 + k * 0.26) for k in range(3)] + [("pop", t - 0.08) for t in (tTiga, tOrang, tNol)]
# agent proposal
ev += [("pop", tBrief - 0.5 + k * 0.18) for k in range(3)] + [("click", tBrief + 0.6), ("pop", tUbah - 0.05)]
ev += [("pop", t - 0.06) for t in (tTamu, tMenu, tHarga)] + [("ping", tHarga + 0.62)]
# agent produksi
ev += [("pop", tAcc + 0.05)] + [("pop", tPecah + 0.05 + k * 0.16) for k in range(4)]
ev += [("pop", tBelanja + 0.12 + k * 0.16) for k in range(3)] + [("pop", tCrew - 0.05 + k * 0.14) for k in range(3)]
# agent analis
ev += [("pop", tAnalis - 0.1)] + [("pop", tEvent - 0.15 + k * 0.13) for k in range(5)] + [("ping", tUntung - 0.05)]
# the loop
ev += [("pop", tLolos + 0.05), ("pop", tKirim + 1.6), ("pop", tPutaran + 0.05)] + [("pop", tTajam - 0.1 + k * 0.17) for k in range(3)]
# 24/7 ring
ev += [("ping", t247 + 0.1)] + [("pop", t247 + 0.15 + k * 0.14) for k in range(3)] + [("pop", tSuruh - 0.05)]
# payoff + CTA
ev += [("pop", tLega - 0.05), ("pop", tArah - 0.1)] + [("pop", tArah + 0.55 + k * 0.16) for k in range(3)]
ev += [("pop", tNgerjain - 0.08), ("pop", tNgatur - 0.05), ("pop", tCta - 0.1), ("click", tF)]

tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
