"""Builds production/vo_words_raw.json (faster-whisper format) from the ElevenLabs character alignment written by
tools/el_tts_ts.py (production/vo_el.json): split on whitespace, drop the audio-tag tokens ("[playful]", "[excited]").
Each line becomes one segment. Run: python3 -I tools/el_to_words.py ."""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
d = json.loads((P / "production/vo_el.json").read_text())
a = d["align"]; ch, st, en = a["chars"], a["start"], a["end"]
segs, cur, tok = [], [], None
def flush_tok():
    global tok
    if tok is None: return
    w = "".join(ch[i] for i in tok)
    if not re.fullmatch(r"\[[^\]]*\]", w):
        cur.append({"w": w, "s": round(st[tok[0]], 3), "e": round(en[tok[-1]], 3), "p": 1.0})
    tok = None
def flush_seg():
    global cur
    if cur:
        segs.append({"start": cur[0]["s"], "end": cur[-1]["e"], "text": " ".join(x["w"] for x in cur), "words": cur})
    cur = []
for i, c in enumerate(ch):
    if c == "\n": flush_tok(); flush_seg(); continue
    if c.isspace(): flush_tok(); continue
    if tok is None: tok = []
    tok.append(i)
flush_tok(); flush_seg()
(P / "production/vo_words_raw.json").write_text(json.dumps({"language": "id", "duration": d["duration"], "segments": segs}, ensure_ascii=False, indent=1))
n = 0
for s in segs:
    print(f"[{s['start']:6.2f}-{s['end']:6.2f}] " + " ".join(f"{n + k}:{w['w']}" for k, w in enumerate(s["words"]))); n += len(s["words"])
