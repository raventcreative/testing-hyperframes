# Word-level times: whisper words re-mapped into the audio-anchored phrase windows (production/vo_alignment.json).
import json, re
W = json.load(open('production/transcript_words_machine.json'))
W = W if isinstance(W, list) else W.get('words', W)
P = json.load(open('production/vo_alignment.json'))['phrases']
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
# letter stream of whisper words with per-letter word index
stream = []; owner = []
for i, w in enumerate(W):
    n = norm(w['text']); stream.append(n); owner += [i] * len(n)
letters = ''.join(stream)
pos = 0; out = []
for p in P:
    toks = p['t'].split()
    plen = sum(len(norm(t)) for t in toks)
    a, b = pos, pos + plen
    wi0, wi1 = owner[a], owner[min(b, len(owner)) - 1]
    ws0, we1 = W[wi0]['start'], W[wi1]['end']
    span = max(0.2, we1 - ws0)
    k = a; words = []
    for t in toks:
        ln = len(norm(t)); wi = owner[min(k, len(owner) - 1)]
        # fraction inside the whisper word for split tokens ("apa pun")
        wstart = W[wi]['start']; wlen = max(1, len(stream[wi])); first = owner.index(wi)
        frac = (k - first) / wlen
        tw = wstart + frac * (W[wi]['end'] - W[wi]['start'])
        ts = p['s'] + (tw - ws0) / span * (p['e'] - p['s'])
        words.append({'w': t, 't': round(max(p['s'], min(p['e'] - 0.05, ts)), 3)})
        k += ln
    out.append({'s': p['s'], 'e': p['e'], 'words': words})
    pos = b
json.dump(out, open('production/word_times.json', 'w'), ensure_ascii=False, indent=1)
for ph in out: print(f"{ph['s']:6.2f}", ' '.join(f"{w['w']}@{w['t']:.2f}" for w in ph['words']))
