# R27 SFX events (exec'd by tools/sfx.py: uses its helpers put/whoosh/pop/tick/chime/typing/card/chip/okck/rise/boom/...,
# word lookups wt()/ws() on production/timing.json, scene starts st()). Synthesised, deterministic. A hit on every scene change.
for sid in ("s02", "s04", "s05", "s06", "s07", "s08", "s09", "s10"):
    out_(sid)
# --- s01 hook: the spend list spins (ticks slowing down), lands twice, receipt rows drop, card flips, the idea is thrown, residents pop
for k in range(16):
    t = 0.05 + 0.7 * (1 - (1 - k / 16) ** 2)
    put(t, tick(0.018, 3600), 0.07)
tS = wt("stok"); put(tS + 0.05, pop(500, 900, 0.08), 0.12); chip(tS + 0.1)
tB = wt("bayar")
for k in range(9):
    put(tB - 0.2 + 0.5 * (1 - (1 - k / 9) ** 2), tick(0.018, 3800), 0.06)
tI = wt("iklan,"); put(tI + 0.1, pop(500, 900, 0.08), 0.12); chip(tI + 0.14); put(tI + 0.3, boom(0.3, 160, 70), 0.08)
tL = wt("lempar"); put(tL - 0.15, whoosh(0.3, 1800, 500, 1.3, 0.35), W * 0.5); card(tL + 0.02, 0.8)
tD = wt("idemu"); put(tD - 0.05, whoosh(0.5, 400, 2600, 1.1, 0.4), W * 0.7)
tW = wt("warga"); put(tW, boom(0.5, 120, 50), 0.12)
for k in range(10):
    put(tW + 0.05 + k * 0.035, pop(700 + 40 * k, 1100 + 40 * k, 0.05), 0.04)
for k in range(3):
    put(wt("AI.") + 0.06 + k * 0.12, pop(900, 1400, 0.06), 0.06)
# --- s02 name: letters, swarm, chips, the counter rolls, stars, GitHub logo spins in
s2 = st("s02"); card(s2 + 0.0, 0.9)
tN = wt("MiroFish,")
for k in range(8):
    put(tN - 0.22 + k * 0.045, tick(0.02, 3000 + 120 * k), 0.08)
put(tN + 0.1, whoosh(0.6, 600, 2200, 1.2, 0.4), W * 0.4)
chip(wt("open") - 0.06); chip(wt("source,") - 0.04)
tP = wt("puluhan"); put(tP - 0.05, rise(0.85, 400, 1600), 0.05)
for k in range(12):
    put(tP - 0.05 + k * 0.07, tick(0.015, 4400), 0.05)
tBi = wt("bintang"); put(tBi + 0.2, chime((1568, 2093, 2637), 0.9), 0.06)
for k in range(4):
    put(tBi - 0.1 + k * 0.07, pop(1100, 1700, 0.05), 0.05)
tG = wt("GitHub."); put(tG - 0.35, whoosh(0.9, 300, 1800, 1.0, 0.5), W * 0.6); put(tG + 0.1, pop(400, 700, 0.1), 0.1)
# --- s03 portal from the robot's face, upload, skyline, residents
s3 = st("s03"); put(s3 - 0.05, whoosh(0.5, 200, 3000, 0.9, 0.7), W * 0.9); put(s3 + 0.38, boom(0.6, 110, 45), 0.12)
tDk = wt("dokumen"); put(tDk - 0.2, whoosh(0.35, 1500, 500, 1.3, 0.4), W * 0.4); put(tDk + 0.15, pop(380, 620, 0.09), 0.1)
typing(tDk + 0.1, wt("idemu,") + 0.4, 0.04, 22)
okck(wt("idemu,") + 0.5)
tBg = wt("bangun")
for k in range(11):
    put(tBg - 0.05 + k * 0.065, pop(260 + 25 * k, 520 + 25 * k, 0.09), 0.06)
tBr = wt("berisi")
for k in range(16):
    put(tBr + k * 0.04, pop(900 + 30 * k, 1500 + 30 * k, 0.04), 0.035)
chip(wt("ribuan") - 0.05)
# --- s04 persona fan -> profile, attribute rows
s4 = st("s04")
for k in range(3):
    put(max(s4 + 0.02, wt("Tiap") - 0.15) + k * 0.08, whoosh(0.3, 600, 1800, 1.2, 0.4), W * 0.3)
tPy = wt("punya"); put(tPy - 0.1, whoosh(0.4, 400, 2000, 1.1, 0.45), W * 0.6); put(tPy + 0.25, pop(420, 760, 0.09), 0.1)
for w in ("kepribadian,", "ingatan,", "bersikap"):
    t = wt(w, s4); put(t - 0.12, pop(600, 1000, 0.07), 0.09); put(t - 0.04, tick(0.02, 2600), 0.05)
# --- s05 chaos: posts, round counter ticks, debate slam, replies, chip
s5 = st("s05"); card(s5, 0.8)
for k in range(30):
    put(wt("posting,") - 0.2 + (st("s06") - wt("posting,")) * (k / 30) ** 0.7, tick(0.012, 3000 + 40 * k), 0.035)
tDb = wt("debat,"); put(tDb - 0.12, whoosh(0.25, 2400, 600, 1.4, 0.4), W * 0.6); put(tDb + 0.08, boom(0.4, 150, 60), 0.15); put(tDb + 0.1, pop(300, 160, 0.1), 0.1)
for w in ("saling", "balas"):
    t = wt(w, s5)
    for k in range(2):
        put(t - 0.1 + k * 0.16, pop(800, 1250, 0.06), 0.07)
chip(wt("media", s5) - 0.08)
# --- s06 product, price, comments, likes
s6 = st("s06"); card(s6, 0.8); put(s6 + 0.14, rise(0.4, 300, 800), 0.04)
tR = wt("Rp55 ribu."); put(tR - 0.08, pop(500, 1000, 0.1), 0.14); put(tR + 0.02, chime((1318.5, 1760), 0.5), 0.04)
tK = wt("kemahalan,"); put(tK - 0.12, whoosh(0.3, 1600, 500, 1.3, 0.4), W * 0.5); put(tK + 0.1, pop(380, 200, 0.1), 0.1)
for k in range(8):
    put(tK + 0.3 + k * 0.1, tick(0.012, 4000), 0.03)
tT = wt("tanya", s6); put(tT - 0.15, whoosh(0.3, 1600, 500, 1.3, 0.4), W * 0.45); put(tT + 0.1, pop(500, 300, 0.08), 0.08)
# --- s07 report bars, chat typing, answer
s7 = st("s07"); card(s7, 0.9)
for k in range(3):
    put(wt("laporan,") - 0.05 + k * 0.16, rise(0.45, 300 + 80 * k, 900 + 120 * k), 0.035)
typing(wt("ngobrol") - 0.12, wt("langsung") + 0.15, 0.08, 16)
put(wt("warganya.") - 0.2, pop(700, 1200, 0.07), 0.1); put(wt("warganya.") - 0.15, chime((1568, 2093), 0.5), 0.04)
# --- s08 Claude Code request, logo spin, steps, keys
s8 = st("s08"); card(s8, 0.8)
typing(max(s8 + 0.15, wt("Pasangnya") - 0.05), wt("Claude Code,") - 0.05, 0.08, 18)
tC = wt("Claude Code,"); put(tC - 0.2, whoosh(0.9, 300, 1800, 1.0, 0.5), W * 0.6)
for k in range(4):
    put(tC + 0.18 + k * 0.24, pop(900, 1400, 0.05), 0.06)
put(wt("tinggal") - 0.1, whoosh(0.4, 900, 300, 1.2, 0.4), W * 0.3)
typing(wt("isi", s8) - 0.02, wt("API key.") + 0.75, 0.06, 14)
# --- s09 kinetic type: words thump, strike scratch, underline slide
s9 = st("s09"); card(s9, 0.7)
for w in ("ini", "simulasi,", "bukan", "ramalan."):
    put(wt(w, s9) - 0.1, pop(300, 180, 0.09), 0.1)
tRm = wt("ramalan."); put(tRm + 0.1, rip(0.25), 0.05); put(tRm + 0.3, whoosh(0.3, 1200, 400, 1.3, 0.4), W * 0.4)
# --- s10 CTA: package, comment IDE typing, heart, send, plane, DM chime, end
s10 = st("s10")
put(s10 + 0.0, pop(500, 900, 0.09), 0.12); put(s10 + 0.02, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tId = wt("IDE,"); ta = max(s10 + 0.2, tId - 0.06)
for k in range(3):
    put(ta + k * 0.14, tick(0.022, 4200), 0.16)
put(ta + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt("aku", s10) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", s10) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
