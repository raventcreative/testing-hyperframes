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

tJam, tKal, tTujuh = S("Jam dua belas"), S("kalender konten"), S("tujuh hari")
tSek, tTiga, tGue = S("Sekarang yang ngerjain"), S("tapi tiga belas"), S("Gue tunjukin")
tTelat, tLibur, tGaji = S("Timnya nggak pernah"), S("nggak pernah libur"), S("nggak pernah minta")
tNaskah, tRumus, tLemah, tGanti = S("Satu nulis naskah"), S("pakai rumus hook"), S("Pembuka yang lemah"), S("terus diganti")
tAudit, tKrit, tBio = S("Satu lagi ngaudit"), S("pakai dua belas"), S("terus nulis ulang")
tJadwal, tDraf = S("Ada yang nyusun"), S("sampai draf caption")
tGila, tTren, tUrut, tKelip = S("Tapi yang paling"), S("si riset tren"), S("Dia ngurutin ide"), S("tapi dari kelipatan")
tNaik, tBukan = S("Jadi yang naik"), S("bukan akun yang")
tCara, tTerm, tApl, tDev = S("Masangnya ada dua"), S("Lewat terminal"), S("Atau tinggal buka"), S("di laptop, di web")
tDown, tAppr, tCta = S("Download sekali"), S("Dan semua hasilnya"), S("Mau sistem kayak")
tF = wt("Klik link", "link")

tZ1 = tGue - 0.2
tV2, tV3, tV4 = tNaskah - 0.55, tAudit - 0.5, tJadwal - 0.5
tW1, tW2 = tGila - 1.12, tCara - 1.16
tFlip, tZ2, tZ3 = tApl - 0.5, tAppr - 0.62, tCta - 0.72

# one quiet whoosh per scene transition / swing / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.08, tV2, tV3, tBio - 0.25, tV4, tW1, tW2, tFlip, tZ2, tZ3)]
# hook: clock, week cards, empty note, composer
ev += [("pop", 0.2), ("pop", 0.6), ("pop", 0.95), ("pop", tKal - 0.1), ("pop", tTujuh)]
# hook: 13 skills arrive, week fills
ev += [("ping", tSek + 0.1)] + [("pop", tSek + 0.35 + k * 0.3) for k in range(4)]
ev += [("pop", tTiga + 0.1 + k * 0.24) for k in range(4)] + [("sparkle", tTiga + 0.6)]
# team roster + traits
ev += [("pop", tZ1 + 1.0 + k * 0.18) for k in range(4)]
ev += [("click", tTelat), ("click", tLibur), ("click", tGaji), ("ping", tGaji + 0.35)]
# writer
ev += [("pop", tNaskah + 0.1), ("pop", tNaskah + 0.25), ("pop", tNaskah + 0.4), ("pop", tRumus + 0.15)]
ev += [("pop", tLemah + 0.18), ("click", tGanti + 0.1), ("ping", tGanti + 0.45)]
# auditor
ev += [("pop", tAudit + 0.1), ("sparkle", tAudit + 0.35)] + [("pop", tKrit + 0.1 + k * 0.22) for k in range(4)]
ev += [("pop", tBio + 0.2), ("ping", tBio + 0.65)]
# planner
ev += [("pop", tJadwal + 0.1 + k * 0.18) for k in range(4)] + [("pop", tDraf + 0.1 + k * 0.2) for k in range(4)]
# trend research
ev += [("pop", tGila + 0.15), ("pop", tGila + 0.32), ("pop", tGila + 0.5), ("ping", tTren + 0.15)]
ev += [("pop", tKelip + 0.15), ("pop", tKelip + 0.45), ("sparkle", tNaik + 0.2), ("ping", tNaik + 0.85), ("pop", tBukan + 0.1)]
# install: two ways, terminal, devices, download, toggles
ev += [("pop", tCara + 0.15), ("pop", tCara + 0.38), ("click", tTerm + 0.05), ("pop", tTerm + 0.35), ("pop", tTerm + 0.66), ("ping", tTerm + 1.05), ("sparkle", tTerm + 1.3)]
ev += [("pop", tDev + 0.12), ("pop", tDev + 0.74), ("pop", tDev + 1.36)]
ev += [("click", tDown + 0.6), ("pop", tDown + 1.0)] + [("click", tDown + 1.3 + k * 0.33) for k in range(3)]
# approve + CTA
ev += [("pop", tAppr + 0.1), ("click", tAppr + 1.35), ("ping", tAppr + 1.65), ("pop", tCta - 0.1), ("click", tF)]

tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{max(0.0, t):.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
