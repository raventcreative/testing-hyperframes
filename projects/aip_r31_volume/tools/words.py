"""Word timings from the ElevenLabs character alignment (assets/audio/vo.json) -> production/words.json [[word, start, end], ...].
Audio tags like [playful] are skipped."""
import json, re
d = json.load(open("assets/audio/vo.json"))
ch, st, en = d["align"]["chars"], d["align"]["start"], d["align"]["end"]
out, i, n = [], 0, len(ch)
while i < n:
    if ch[i] == "[":
        while i < n and ch[i] != "]": i += 1
        i += 1; continue
    if ch[i].isspace(): i += 1; continue
    j = i
    while j < n and not ch[j].isspace() and ch[j] != "[": j += 1
    w = "".join(ch[i:j])
    if re.search(r"\w", w): out.append([w, round(st[i], 3), round(en[j - 1], 3)])
    i = j
json.dump(out, open("production/words.json", "w"), ensure_ascii=False)
print(len(out)); print(" ".join(f"{w}@{s:.2f}" for w, s, e in out))
