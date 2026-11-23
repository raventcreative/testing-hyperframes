"""Word timing: local Whisper (faster-whisper, 'small', Indonesian) word timestamps aligned to the exact script text.
Script tokens are matched to recognised words with difflib; unmatched tokens are interpolated between neighbours.
Output: production/word_timing.json, vendor/vo_words.js (VO_WORDS [word,start,end,phraseIdx], VO_PHR)
Run: python3 tools/align_whisper.py <project>"""
import difflib, json, re, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
# caption phrases (short on-screen chunks), in spoken order
PHRASES = """Jam dua pagi, lu tidur.
Jam setengah tujuh,
proposal buat klien besok
udah jadi.
Itu bukan mimpi.
Itu kantor katering gue.
Isinya agent AI semua,
lampunya nggak pernah mati.
Dulu gue ngerjain semuanya sendiri.
Tiga peran, satu orang, nol tidur.
Karyawan pertama, agent proposal.
Tiap brief masuk,
dia ubah jadi penawaran lengkap:
jumlah tamu, menu, harga.
Karyawan kedua, agent produksi.
Proposal yang lu setujui,
dia pecah jadi rundown,
belanja, sama jadwal crew.
Karyawan ketiga, yang paling penting:
agent analis.
Tiap event kelar,
dia nyaring paket mana
yang beneran untung.
Paket yang lolos,
dikirim balik ke agent proposal.
Jadi tiap putaran,
penawarannya makin tajam.
Semua ini jalan dua puluh empat jam,
tanpa gue suruh.
Yang bikin gue lega
bukan jumlah eventnya.
Tapi gue punya waktu mikirin arah.
Gue nggak lagi ngerjain event.
Gue ngatur kantornya.
Mau sistem kayak gini
dipasang di bisnis lu?
Klik link di bio,
ngobrol langsung sama tim AIpreneur Automation.""".strip().split("\n")
NUM = {"masing-masing": "masing masing", "AIpreneur": "ai prender"}
ALIAS = {"nggak": "gak", "5": "lima", "1": "satu", "10": "sepuluh", "7": "tujuh", "3": "tiga", "2": "dua", "20": "puluh", "manager": "manajer", "reset": "riset", "lo": "lu", "gua": "gue", "audience": "audiens", "point": "poin", "tetap": "tetep", "senin": "senin", "35": "lima", "tiga": "tiga", "puluh": "puluh"}
norm = lambda w: ALIAS.get(re.sub(r"[^a-z0-9]", "", w.lower()), re.sub(r"[^a-z0-9]", "", w.lower()))

w = wave.open(str(P / "assets/audio/vo.wav")); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
if sr != 16000:
    idx = np.arange(0, len(x), sr / 16000); x = np.interp(idx, np.arange(len(x)), x).astype(np.float32)
cache = P / "production/whisper_words.json"
if cache.exists():
    raw = json.loads(cache.read_text())
else:
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(x, language="id", word_timestamps=True)
    raw = [[wd.word, wd.start, wd.end] for s in segs for wd in s.words]
    cache.write_text(json.dumps(raw, ensure_ascii=False))
# Whisper word starts drift early after a pause: clamp each recognised word to the real speech (ffmpeg silencedetect)
import subprocess
_sil = subprocess.run(["ffmpeg", "-nostats", "-i", str(P / "assets/audio/vo.wav"), "-af", "silencedetect=noise=-38dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True).stderr
_a = [float(v) for v in re.findall(r"silence_start: ([0-9.]+)", _sil)]; _b = [float(v) for v in re.findall(r"silence_end: ([0-9.]+)", _sil)]
SIL = list(zip(_a, _b))
def _clamp(s0, s1):
    for a, b in SIL:
        if a < s0 < b and b < s1 - 0.05: s0 = b
        if a > s0 + 0.05 and a < s1 < b: s1 = a
    return s0, s1
raw = [[w0, *_clamp(s0, s1)] for w0, s0, s1 in raw]
rec = [(norm(w0), s0, s1) for w0, s0, s1 in raw if norm(w0)]
# script tokens (numbers expanded so they can match spoken words; each expansion maps back to its token)
toks, sub = [], []
for pi, ph in enumerate(PHRASES):
    for t in ph.split():
        parts = NUM.get(t.strip(",.?:"), t).split() if t.strip(",.?:") in NUM else [t]
        for k, p in enumerate(parts):
            sub.append((len(toks), norm(p)))
        toks.append([t, None, None, pi])
sm = difflib.SequenceMatcher(a=[s[1] for s in sub], b=[r[0] for r in rec], autojunk=False)
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        ti = sub[blk.a + k][0]; _, s0, s1 = rec[blk.b + k]
        toks[ti][1] = s0 if toks[ti][1] is None else min(toks[ti][1], s0)
        toks[ti][2] = s1 if toks[ti][2] is None else max(toks[ti][2], s1)
# interpolate gaps
known = [i for i, t in enumerate(toks) if t[1] is not None]
for i, t in enumerate(toks):
    if t[1] is not None: continue
    lo = max([k for k in known if k < i], default=None); hi = min([k for k in known if k > i], default=None)
    a0 = toks[lo][2] if lo is not None else 0.0; b0 = toks[hi][1] if hi is not None else len(x) / 16000
    n0 = (lo if lo is not None else -1); n1 = (hi if hi is not None else len(toks))
    f0 = (i - n0) / (n1 - n0); f1 = (i + 1 - n0) / (n1 - n0)
    t[1] = a0 + (b0 - a0) * f0; t[2] = a0 + (b0 - a0) * f1
words = [[t[0], round(t[1], 3), round(t[2], 3), t[3]] for t in toks]
phr = []
for pi, ph in enumerate(PHRASES):
    ws = [wd for wd in words if wd[3] == pi]
    phr.append({"text": ph, "start": ws[0][1], "end": ws[-1][2]})
matched = len(known)
(P / "vendor/vo_words.js").write_text("// generated by tools/align_whisper.py\nwindow.VO_WORDS = " + json.dumps(words, ensure_ascii=False) +
                                      ";\nwindow.VO_PHR = " + json.dumps(phr, ensure_ascii=False) + ";\n")
(P / "production/word_timing.json").write_text(json.dumps({"words": words, "phrases": phr}, ensure_ascii=False, indent=1))
print(f"matched {matched}/{len(toks)} tokens")
for p in phr: print(f"{p['start']:6.2f}-{p['end']:6.2f}  {p['text']}")
