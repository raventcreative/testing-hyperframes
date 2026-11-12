"""VO word timing without network ASR (model hosts are blocked in this environment).
Speech groups come from ffmpeg silencedetect (-34 dB, >= 70 ms) on assets/audio/vo.mp3 and are mapped by hand to the
script below. Inside a group, words get syllable-weighted durations; every boundary is snapped to the lowest-energy
10 ms frame within +-80 ms. Output: vendor/vo_words.js (VO_WORDS = [[word, start, end, phraseIndex]], VO_PHR)
Run: python3 -I tools/align.py <project>"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
AUDIO = P / "assets/audio/vo.mp3"

# (start, end, [phrases]) - a group may hold several phrases when no clear pause separates them
GROUPS = [
    (0.07, 3.47, ["Gimana rasanya kalau", "satu perusahaan"]),
    (3.59, 5.24, ["dijalanin sama 137 AI agent?"]),
    (5.76, 6.94, ["Gue tunjukin simulasinya."]),
    (7.46, 8.82, ["Hai gue Freddie Kashawan,"]),
    (8.95, 13.17, ["udah bisnis 10 tahun", "dan 2 tahun terakhir", "pake AI di bisnis gue sendiri."]),
    (13.64, 14.15, ["Pertama,"]),
    (14.27, 16.63, ["sambungin dulu tools", "yang udah lu pakai tiap hari."]),
    (17.09, 19.13, ["Email, CRM, kalender,"]),
    (19.26, 20.65, ["chat, sampai pembukuan."]),
    (20.98, 21.94, ["Begitu tersambung,"]),
    (22.01, 25.42, ["137 agent langsung kebagi", "ke 7 divisi."]),
    (25.84, 26.41, ["Sales,"]), (26.58, 27.12, ["deals,"]), (27.24, 27.87, ["marketing,"]),
    (28.04, 28.63, ["customer,"]), (28.86, 29.57, ["operations,"]),
    (29.64, 31.25, ["intelligence,", "dan back office."]),
    (31.53, 33.38, ["Sekarang gue klik", "divisi sales."]),
    (33.74, 35.36, ["Ada 22 agent di sini."]),
    (35.68, 36.38, ["Gue buka satu:"]),
    (36.76, 37.90, ["Cold Email Drafting."]),
    (38.23, 39.63, ["Dia nggak kerja asal-asalan."]),
    (39.96, 41.59, ["Tugasnya dipecah jadi tiga:"]),
    (41.99, 42.81, ["nulis sequence,"]),
    (42.93, 43.90, ["bikin subject line,"]),
    (44.02, 45.12, ["bikin kalimat pembuka."]),
    (45.47, 49.63, ["Datanya diambil dari", "target customer", "dan riset tiap prospek."]),
    (50.01, 50.63, ["Klik run."]),
    (50.99, 52.00, ["Dalam hitungan detik,"]),
    (52.40, 56.00, ["sequence-nya jadi.", "Satu agent ini aja", "udah gantiin output inti satu SDR."]),
    (56.37, 57.75, ["Tapi nggak langsung dikirim."]),
    (58.03, 60.29, ["Masuk dulu ke HP lu,", "nunggu approval."]),
    (60.60, 62.12, ["Lu approve,", "baru jalan."]),
    (62.41, 63.68, ["Dan tiap pagi jam tujuh,"]),
    (63.77, 65.47, ["lu dapet satu halaman laporan."]),
    (65.83, 68.57, ["Apa yang udah dikerjain,", "apa yang nunggu keputusan lu."]),
    (68.98, 69.99, ["AI-nya yang kerja."]),
    (70.36, 72.00, ["Keputusan tetap di tangan lu."]),
    (72.45, 75.88, ["Ok follow gua", "Freddie Kashawan", "kalo lu mau update", "seputar AI."]),
]
PRON = {"22": "duapuluhdua", "crm": "siarem", "run": "ran", "sequence-nya": "sikuensnya", "approval": "eprufal", "hp": "hape", "ai-nya": "einya", "simulasinya": "simulasinya", "tools": "tuls", "chat": "cet", "137": "seratustigapuluhtujuh", "10": "sepuluh", "2": "dua", "7": "tujuh", "60": "enampuluh", "80": "delapanpuluh",
        "ai": "ei", "full": "ful", "freddie": "fredi", "kashawan": "kasawan", "marketing": "marketing", "sales": "seils",
        "deals": "dils", "customer": "kastomer", "operations": "operesyens", "intelligence": "intelijens", "back": "bek",
        "office": "ofis", "job": "job", "cold": "kold", "email": "imel", "drafting": "drafting", "sequence": "sikuens",
        "subject": "sabjek", "line": "lain", "output": "autput", "sdr": "esdiar", "human-led": "hiumenled",
        "human-assisted": "hiumenasisted", "fully": "fuli", "autonomous": "otonomus", "approve": "eprup",
        "follow": "folou", "update": "apdet", "ok": "okei", "target": "target", "plus": "plas"}


def syl(w):
    k = re.sub(r"[^\w-]", "", w.lower())
    k = PRON.get(k, k)
    return max(1, len(re.findall(r"[aiueo]+", k)))


raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(AUDIO), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
fr = 160
env = np.array([np.sqrt(np.mean(x[i:i + fr] ** 2) + 1e-12) for i in range(0, len(x) - fr, fr)])


def snap(t, lo, hi):
    a, b = max(lo, t - 0.08), min(hi, t + 0.08)
    ia, ib = int(a * 100), int(b * 100)
    if ib <= ia:
        return t
    return (ia + int(np.argmin(env[ia:ib]))) / 100


words, phr = [], []
for g0, g1, phrases in GROUPS:
    toks = [(w, pi) for pi, p in enumerate(phrases) for w in p.split()]
    wts = [syl(w) for w, _ in toks]
    tot = sum(wts)
    t, bounds = g0, [g0]
    for wgt in wts[:-1]:
        t += (g1 - g0) * wgt / tot
        bounds.append(t)
    bounds.append(g1)
    for i in range(1, len(bounds) - 1):
        bounds[i] = snap(bounds[i], bounds[i - 1] + 0.06, bounds[i + 1] - 0.06)
    base = len(phr)
    for pi, p in enumerate(phrases):
        phr.append({"text": p})
    for i, (w, pi) in enumerate(toks):
        words.append([w, round(bounds[i], 3), round(bounds[i + 1], 3), base + pi])
for k, p in enumerate(phr):
    ws = [w for w in words if w[3] == k]
    p["start"], p["end"] = ws[0][1], ws[-1][2]

out = P / "vendor/vo_words.js"
out.write_text("// generated by tools/align.py\nwindow.VO_WORDS = " + json.dumps(words, ensure_ascii=False) +
               ";\nwindow.VO_PHR = " + json.dumps(phr, ensure_ascii=False) + ";\n")
(P / "production/word_timing.json").write_text(json.dumps({"words": words, "phrases": phr}, ensure_ascii=False, indent=1))
for p in phr:
    print(f"{p['start']:6.2f}-{p['end']:6.2f}  {p['text']}")
