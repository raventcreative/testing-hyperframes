"""Estimate word timings inside each VO segment.
Method: 10ms RMS envelope -> speech onset/offset + internal pauses; words distributed over
voiced time proportional to syllable weight; comma/period boundaries snapped to the nearest
detected pause. usage: python align_words.py <asr_json> <project_dir> <out_json>
"""
import json, sys, re, subprocess, os, numpy as np

asr, proj, out = sys.argv[1:4]
d = json.load(open(asr))
# reviewed display text (spelling normalised; spoken words unchanged)
REVIEWED = {
 "VO01": "Banyak orang bilang hasil AI itu masih biasa aja.",
 "VO02": "Padahal masalahnya sering bukan di AI-nya.",
 "VO03": "Masalahnya ada di arahan yang diberikan.",
 "VO04": "AI itu cepat, tapi hasilnya mengikuti seberapa jelas brief-nya.",
 "VO05": "Jadi bukan cuma bilang bikin yang keren,",
 "VO06": "tapi menjelaskan style, ritme, komposisi, transisi, dan hierarki.",
 "VO07": "Karena prompt yang tepat bisa mengubah output secara drastis.",
 "VO08": "Dari teks biasa, menjadi motion yang terlihat mahal.",
 "VO09": "Dan inilah cara AI PRENEUR mengarahkan AI.",
 "VO10": "Lebih cepat, lebih terarah, dan hasilnya jauh lebih premium.",
 "VO11": "AI bisa membuat motion selevel ini, asal prompt-nya tepat.",
}
SPECIAL = {"ai": 2, "ai-nya": 3, "style": 1, "brief-nya": 2, "prompt": 1, "prompt-nya": 2,
           "motion": 2, "output": 2, "preneur": 2, "premium": 3, "hierarki": 4}

def syl(w):
    k = re.sub(r"[^a-z\-]", "", w.lower())
    if k in SPECIAL: return SPECIAL[k]
    return max(1, len(re.findall(r"(ai|au|oi|[aiueo])", k)))

wav = os.path.join(proj, "assets/audio/vo_master_39s.wav")
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", wav, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(pcm, dtype=np.float32)
HOP = 160
rms = np.sqrt(np.convolve(x**2, np.ones(400)/400, "same")[::HOP] + 1e-12)
db = 20*np.log10(rms)

segs = []
for s in d["segments"]:
    a, b = int(s["start"]*100), int(s["end"]*100)
    e = db[a:b]
    thr = max(np.percentile(e, 95) - 30, -52)
    voiced = e > thr
    idx = np.where(voiced)[0]
    on, off = idx[0], idx[-1]+1
    # internal pauses >= 70ms
    pauses, i = [], on
    while i < off:
        if not voiced[i]:
            j = i
            while j < off and not voiced[j]: j += 1
            if j - i >= 7: pauses.append(((i+j)/2, i, j))
            i = j
        else: i += 1
    text = REVIEWED[s["id"]]
    words = text.split()
    w = np.array([syl(t) + 0.35 for t in words], float)
    cumw = np.concatenate([[0], np.cumsum(w)])
    tot = cumw[-1]
    # voiced-time share at each pause centre
    def vshare(f):
        before = (f-on) - sum(min(j, f)-i for _, i, j in pauses if i < f)
        return before / ((off-on) - sum(j-i for _, i, j in pauses))
    # ASR-probe verified anchors: pause start (s) -> number of words spoken before it.
    # None = intra-word gap (ignored); "end" = sentence already finished (speech offset).
    PROBE = {"VO04": {9.26: 3}, "VO05": {13.11: 4}, "VO06": {16.05: 3, 16.78: 4, 17.8: 5},
             "VO07": {20.53: 1, 22.66: None, 23.06: 8}, "VO08": {24.59: 1, 25.46: 3, 27.88: "end"},
             "VO09": {30.92: "end"}, "VO10": {31.83: 2, 32.81: 4, 34.69: 8}, "VO11": {37.88: 6}}
    anchors = []
    for c, i, j in pauses:
        key = round((a+i)/100, 2)
        v = PROBE.get(s["id"], {}).get(key, "missing")
        if v == "missing": raise SystemExit(f"unprobed pause {s['id']} {key}")
        if v is None: continue
        if v == "end": off = i; continue
        anchors.append((v, i, j))
    anchors.sort()
    # chunks between anchors, distribute proportionally inside each
    bounds = [None]*(len(words)+1); ends = {}
    edges = [(0, on)] + [(k, j) for k, i, j in anchors]
    stops = [(k, i) for k, i, j in anchors] + [(len(words), off)]
    for (k0, f0), (k1, f1) in zip(edges, stops):
        for k in range(k0, k1+1):
            bounds[k] = f0 + (f1-f0)*(cumw[k]-cumw[k0])/max(1e-9, cumw[k1]-cumw[k0])
        ends[k1-1] = f1
    for k, i, j in anchors: bounds[k] = j
    ws = []
    for k, t in enumerate(words):
        st = (a + bounds[k]) / 100; en = (a + ends.get(k, bounds[k+1])) / 100
        ws.append(dict(text=t, start=round(st, 3), end=round(max(en, st+0.08), 3)))
    segs.append(dict(id=s["id"], start=s["start"], end=s["end"], speech_on=round((a+on)/100, 3),
                     speech_off=round((a+off)/100, 3), text_machine=s["text_master"],
                     text_reviewed=text, pauses=[[round((a+i)/100, 3), round((a+j)/100, 3)] for _, i, j in pauses],
                     words=ws))
    print(s["id"], " ".join(f'{q["text"]}@{q["start"]:.2f}' for q in ws))
json.dump(dict(method="energy-pause anchors + syllable-proportional distribution (estimated, ±0.12s)",
               segments=segs), open(out, "w"), ensure_ascii=False, indent=1)
