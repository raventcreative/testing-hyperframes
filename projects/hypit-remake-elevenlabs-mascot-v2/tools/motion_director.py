"""SMART MOTION DIRECTOR — auto-direction pass.

Reads the measured VO timing + script, detects the narrative intent of every phrase, and writes a
scene-by-scene motion plan that picks effects from vendor/motion-director.js with restraint:

  1. narrative analysis      -> intent per phrase (lexicon + caption keywords + punctuation)
  2. emphasis points         -> caption keywords / stressed words (VO timing)
  3. effect choice           -> intent -> effect families (see INTENT_FX)
  4. restraint rules         -> max one MAJOR effect at a time, >= MIN_GAP s between majors,
                                no identical effect twice in a row, at most MAX_PER_SCENE majors per
                                scene, scenes already carrying a dense hero ("busy") get none,
                                presenter windows keep their own pop-ups (director only adds what they lack)
  5. sync                    -> every effect anchored to a VO word start
  6. mascot acting hints     -> what the host does on the beat (consumed by hand in tools/mascot_src.html)

Output: production/motion_plan.json (human-readable, with the reason for every choice).
tools/gen_director.py turns the plan into compositions/director.html + camera moves in index.html.
Re-run on any new script/VO: python3 tools/motion_director.py .
"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
wt = json.loads((P / "production/word_timing.json").read_text())
words = wt["words"]
scenes = json.loads((P / "production/scenes.json").read_text())["scenes"]
keys = {i for g in wt["caption_groups"] for i in g["highlight"]}

# ---------------------------------------------------------------- 1. narrative lexicon (Indonesian + tech)
LEX = {
    "reveal": ["namanya", "hypit", "jangan", "hasilnya", "komen", "efek"],
    "workflow": ["agent", "coding", "workflow", "skill", "pasang", "proses", "teknis", "kode", "framework"],
    "conversation": ["kasih", "referensi", "brief", "komen", "caranya"],
    "product": ["video", "jualan", "produk", "presenter", "footage", "b-roll", "caption"],
    "data": ["puluhan", "ribu", "stars", "beberapa", "versi"],
    "list": ["footage", "caption", "b-roll", "efek", "musik", "aset"],
    "premium": ["open", "source", "model", "layanan", "github", "repo"],
    "contrast": ["bukan", "tapi", "tanpa", "sementara"],
    "emotion": ["jangan", "bukan", "ganti"],
    "focus": ["dipertahankan", "struktur"],
}
INTENT_FX = {  # ordered preferences
    "conversation": ["chatTakeover"],
    "list": ["checklistPop"],
    "data": ["growthCurve"],
    "premium": ["orbitReveal", "liquidGlass"],
    "reveal": ["snapZoom", "frameEscape"],
    "emotion": ["dollyZoom", "snapZoom"],
    "workflow": ["liquidGlass", "zoomPortal"],
    "product": ["phoneMockup", "bRollOverlay"],
    "contrast": ["digitalZoom"],
    "focus": ["digitalZoom"],
}
# how long each effect owns the screen (s); "scene" = until the scene ends
HOLD = {"chatTakeover": "scene", "checklistPop": "scene", "growthCurve": "scene", "orbitReveal": 1.2, "snapZoom": 0.6,
        "dollyZoom": 0.9, "frameEscape": "scene", "zoomPortal": 0.6, "phoneMockup": 2.0, "bRollOverlay": 2.5, "studioReveal": 1.2}
FIRST_WORD_ANCHOR = {"growthCurve", "chatTakeover", "checklistPop"}   # these start on the first word of their beat
MINOR_GAP = 10.0
MAJOR = {"chatTakeover", "checklistPop", "growthCurve", "orbitReveal", "snapZoom", "dollyZoom", "frameEscape", "zoomPortal", "phoneMockup", "bRollOverlay", "magazineCover", "studioReveal"}
MIN_GAP, MAX_PER_SCENE = 1.4, 2
# scene notes from the storyboard: busy = dense hero already fills the frame; free = zone for overlays;
# allow = effects that fit the scene's layout (presenter windows keep their own pop-ups and only get what they lack)
SCENE_ALLOW = {
    "s01": ["studioReveal", "snapZoom"], "s02": ["orbitReveal", "growthCurve"], "s03": ["chatTakeover"],
    "s06": ["checklistPop"], "s10": ["digitalZoom"], "s13": ["dollyZoom"], "s14": [], "s18": ["orbitReveal"], "s19": ["frameEscape"],
}
SCENE_NOTES = {
    "s01": {"busy": False, "presenter": True, "free": "top"}, "s02": {"busy": False, "free": "top-left"},
    "s03": {"busy": False, "presenter": True, "free": "top"}, "s04": {"busy": True}, "s05": {"busy": True},
    "s06": {"busy": False, "free": "top-right"}, "s07": {"busy": True}, "s08": {"busy": True}, "s09": {"busy": True},
    "s10": {"busy": False, "free": "camera"}, "s11": {"busy": True}, "s12": {"busy": True},
    "s13": {"busy": False, "presenter": True, "free": "camera"}, "s14": {"busy": False, "presenter": True},
    "s15": {"busy": True}, "s16": {"busy": True}, "s17": {"busy": True},
    "s18": {"busy": False, "presenter": True, "free": "card-corner"}, "s19": {"busy": False, "free": "mascot-frame"},
}

def norm(t):
    return re.sub(r"[^a-z\-]", "", t.lower())

# phrases = runs of words between punctuation
phrases, cur = [], []
for i, w in enumerate(words):
    cur.append(i)
    if re.search(r"[.,:?!]$", w["text"]):
        phrases.append(cur); cur = []
if cur:
    phrases.append(cur)

def scene_of(t):
    for s in scenes:
        if s["start"] - 1e-6 <= t < s["end"]:
            return s["id"]
    return scenes[-1]["id"]

plan, per_scene = [], {}
state = {"busy_until": -9.0, "last_fx": None, "last_minor": -99.0}
def scene_end(sid):
    return next(x["end"] for x in scenes if x["id"] == sid)
def push(e):
    plan.append(e)
    fx = e["effect"]
    if fx in MAJOR:
        h = HOLD.get(fx, 1.0)
        state["busy_until"] = scene_end(e["scene"]) if h == "scene" else e["at"] + h
        state["last_fx"] = fx
        per_scene[e["scene"]] = per_scene.get(e["scene"], 0) + 1
    else:
        state["last_minor"] = e["at"]

push({"scene": "s01", "at": 0.0, "effect": "studioReveal", "preset": "HIGH", "word": None, "intent": "establish",
      "reason": "establishing shot: light sweep over the glass-arch set while the host walks in"})

ORDER = ["conversation", "list", "premium", "data", "emotion", "reveal", "focus", "contrast", "workflow", "product"]
for ph in phrases:
    toks = [norm(words[i]["text"]) for i in ph]
    intents = sorted([k for k, lst in LEX.items() if any(t in lst for t in toks)], key=ORDER.index)
    sid = scene_of(words[ph[0]]["start"])
    allow = SCENE_ALLOW.get(sid, [])
    for it in intents:
        for fx in INTENT_FX[it]:
            if fx not in allow or fx == state["last_fx"]:
                continue
            anchors = [i for i in ph if norm(words[i]["text"]) in LEX[it]]
            ak = anchors if fx in FIRST_WORD_ANCHOR else ([i for i in anchors if i in keys] or anchors)
            at = round(words[ak[0]]["start"], 3)
            if fx in MAJOR:
                if at < state["busy_until"] + 0.05 or at - (plan[-1]["at"] if plan else -9) < MIN_GAP or per_scene.get(sid, 0) >= MAX_PER_SCENE:
                    continue
            elif at - state["last_minor"] < MINOR_GAP:
                continue
            push({"scene": sid, "at": at, "effect": fx, "intent": it, "word": words[ak[0]]["text"], "words": ak, "phrase_words": ph,
                  "phrase": " ".join(words[i]["text"] for i in ph),
                  "preset": "HIGH" if it == "emotion" else "SUBTLE" if fx == "digitalZoom" else "STANDARD",
                  "reason": f"{it} beat on '{words[ak[0]]['text']}' -> {fx} (allowed in {sid}, screen free)"})
            break

# compositing + camera polish that run under everything (not "major")
plan.append({"scene": "*", "at": 0, "effect": "greenScreen", "preset": "STANDARD", "reason": "integrate the 3D host into every plate: light wrap + contact shadow"})
plan.append({"scene": "*", "at": 0, "effect": "cinematicOrbit", "preset": "SUBTLE", "reason": "slow orbit on the 3D host during presenter shots + per-scene stage orbit"})
plan.sort(key=lambda e: e["at"])
out = {"generated_by": "tools/motion_director.py", "rules": {"min_gap_s": MIN_GAP, "max_major_per_scene": MAX_PER_SCENE, "no_repeat": True},
       "effects": plan}
(P / "production/motion_plan.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
for e in plan:
    print(f'{e["at"]:6.2f}  {e["scene"]:4} {e["effect"]:15} {e.get("preset",""):9} {e.get("word") or "":14} {e["reason"]}')
