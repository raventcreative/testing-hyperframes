"""Builds production/vo_words_raw.json (faster-whisper format) from the ElevenLabs character alignment written by
tools/el_tts_ts.py (<take>.json): audio tags ("[playful] [excited]") are skipped, words are split on whitespace, one segment per VO line.
Display fixes (spoken number words -> digits for the captions) are applied here.   Run: python3 -I tools/el_to_words.py <take.json> <out.json>"""
import json, re, sys
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src)); a = d["align"]; ch, st, en = a["chars"], a["start"], a["end"]
DISPLAY = {"tujuh": "7", "Lima": "5"}
segs, cur, words, i, n = [], None, [], 0, len(ch)
def flush_word(w):
    if w is None: return
    txt = "".join(ch[k] for k in w)
    words.append({"w": DISPLAY.get(txt, txt), "s": round(st[w[0]], 3), "e": round(en[w[-1]], 3), "p": 1.0})
line_words = []; wbuf = None
while i < n:
    c = ch[i]
    if c == "[":                                  # skip an audio tag
        j = ch.index("]", i) if "]" in ch[i:] else i
        i = j + 1; continue
    if c == "\n":
        flush_word(wbuf); wbuf = None
        if words: segs.append(words); words = []
        i += 1; continue
    if c.isspace():
        flush_word(wbuf); wbuf = None; i += 1; continue
    wbuf = (wbuf or []) + [i]; i += 1
flush_word(wbuf)
if words: segs.append(words)
res = {"language": "id", "source": "elevenlabs-alignment", "segments": [
    {"start": s[0]["s"], "end": s[-1]["e"], "text": " ".join(w["w"] for w in s), "words": s} for s in segs]}
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
k = 0
for s in segs:
    print(" ".join(f"{k + q}:{w['w']}@{w['s']:.2f}" for q, w in enumerate(s))); k += len(s)
