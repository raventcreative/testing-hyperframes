"""ElevenLabs character alignment (production/vo_take*/vo.json from el_tts_ts.py) -> production/vo_words_raw.json in the
faster-whisper format the kit's timing.py reads: {"segments":[{"start","end","text","words":[{"w","s","e","p"}]}]}.
Audio tags ("[playful] [excited]") are skipped; words are split on whitespace; one segment per VO line.
Run: python3 -I tools/align_words.py . production/vo_take1/vo.json"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1]).resolve()
A = json.loads((P / sys.argv[2]).read_text())
al = A["align"]; ch, st, en = al["chars"], al["start"], al["end"]
segs, words, cur, inb = [], [], None, False
def flush():
    global cur
    if cur and cur["w"].strip():
        words.append({"w": cur["w"], "s": round(cur["s"], 3), "e": round(cur["e"], 3), "p": 1.0})
    cur = None
def endseg():
    flush()
    if words:
        segs.append({"start": words[0]["s"], "end": words[-1]["e"], "text": " ".join(w["w"] for w in words), "words": list(words)})
        words.clear()
for i, c in enumerate(ch):
    if c == "[": inb = True; flush(); continue
    if inb:
        if c == "]": inb = False
        continue
    if c == "\n": endseg(); continue
    if c.isspace(): flush(); continue
    # a word ends on its last letter/digit: trailing punctuation can carry the following pause in the alignment
    if cur is None: cur = {"w": c, "s": st[i], "e": en[i]}
    else:
        cur["w"] += c
        if c.isalnum(): cur["e"] = en[i]
endseg()
(P / "production/vo_words_raw.json").write_text(json.dumps({"language": "id", "duration": A["duration"], "segments": segs}, ensure_ascii=False, indent=1))
n = sum(len(s["words"]) for s in segs)
print("segments", len(segs), "words", n)
k = 0
for s in segs:
    print(" ".join(f"{k + i}:{w['w']}@{w['s']:.2f}" for i, w in enumerate(s["words"]))); k += len(s["words"])
