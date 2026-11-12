"""Builds production/vo_words_raw.json from a faster-whisper word transcript (tools/fw_transcribe.py, model small) but with OUR
script's words as display text (production/vo_lines.txt). Used because the ElevenLabs character alignment of this take drifts late at
phrase ends (e.g. "manager." aligned 18.36–18.80 s while the voice stops at 18.40 s); whisper's word times + timing.py's
silence snap match the waveform. Whisper tokens split by hyphens ("sendiri -sendiri,") or clitics ("workflow nya?") are merged.
Run: python3 -I tools/fw_to_words.py <fw.json> production/vo_lines.txt <out.json>"""
import json, re, sys
fw, lines, out = sys.argv[1], sys.argv[2], sys.argv[3]
DISPLAY = {"tujuh": "7", "Lima": "5"}
ours = [DISPLAY.get(w, w) for l in open(lines).read().splitlines() if l.strip() for w in l.split()]
toks = [dict(w) for s in json.load(open(fw))["segments"] for w in s["words"]]
merged = []
for t in toks:
    if merged and (t["w"].startswith("-") or t["w"].lower().startswith("nya")):
        merged[-1]["w"] += t["w"]; merged[-1]["e"] = t["e"]
    else: merged.append(t)
assert len(merged) == len(ours), (len(merged), len(ours))
k = re.compile(r"[^a-z0-9]")
for m, o in zip(merged, ours):
    a, b = k.sub("", m["w"].lower()), k.sub("", o.lower())
    if a[:1] != b[:1] and not (b in ("7", "5", "claude", "claude.", "komen", "nggak", "nggak?")): print("CHECK", m["w"], "->", o)
    m["w"] = o
res = {"language": "id", "source": "faster-whisper small + script text", "segments": [{"start": merged[0]["s"], "end": merged[-1]["e"],
       "text": " ".join(o for o in ours), "words": [{"w": m["w"], "s": m["s"], "e": m["e"], "p": m.get("p", 1)} for m in merged]}]}
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print("ok", len(merged), "words")
