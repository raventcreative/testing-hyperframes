"""SMART MOTION DIRECTOR — auto-direction pass for REELS X-RAY (reuses vendor/motion-director.js).

1. Narrative analysis: phrases (punctuation) -> intent from an Indonesian/tech lexicon.
2. Emphasis points: caption keywords on measured VO word starts.
3. Effect choice: intent -> effect family. In this film the scenes already carry the in-world mechanics
   (hinges, rails, presses), so the director only adds GLOBAL camera emphasis on #world and documents the
   in-scene effects the scenes use (orbitReveal, liquidGlass, checklist, frameBreak, greenScreen, orbit).
4. Restraint: >= 6 s between camera punches, never in the calm cost/QA stretch (37.9–50.3 s) except one
   restrained digital zoom, never on top of a scene's own camera push (only on hold beats).
Outputs production/motion_plan.json + production/director_camera.json (consumed by tools/gen_root.py).
Run: python3 tools/motion_director.py
"""
import json, re
from pathlib import Path

P = Path(__file__).resolve().parents[1]
wt = json.loads((P / "production/word_timing.json").read_text())
words = wt["words"]
keys = {i for g in wt["caption_groups"] for i in g["highlight"]}
LEX = {
    "reveal": ["dibongkar", "kebuka", "kode", "baru", "editor"],
    "payoff": ["mp4", "baru", "dipakai"],
    "focus": ["kredit", "berbiaya", "dicek"],
    "emotion": ["gila", "lihat"],
}
INTENT_FX = {"reveal": "snapZoom", "payoff": "snapZoom", "focus": "digitalZoom", "emotion": None}
CALM = (37.88, 50.26)
MIN_GAP = 6.0
norm = lambda t: re.sub(r"[^a-z0-9]", "", t.lower())

plan, last = [], -99.0
for i, w in enumerate(words):
    k = norm(w["text"])
    intent = next((n for n, lst in LEX.items() if k in lst), None)
    if not intent or i not in keys and intent != "focus":
        continue
    fx = INTENT_FX[intent]
    t = w["start"]
    if fx is None:
        continue
    in_calm = CALM[0] <= t < CALM[1]
    if fx == "snapZoom" and (in_calm or t - last < MIN_GAP):
        continue
    if fx == "digitalZoom" and (not in_calm or any(p["effect"] == "digitalZoom" for p in plan)):
        continue
    preset = "HIGH" if k in ("baru",) else "SUBTLE" if fx == "digitalZoom" or k == "editor" else "STANDARD"
    plan.append({"at": round(t, 3), "word": w["text"], "intent": intent, "effect": fx, "preset": preset,
                 "reason": f"{intent} beat on '{w['text']}' -> {fx}"})
    last = t

# in-scene effects (implemented inside the scene modules; listed for the record)
plan += [
    {"at": 0, "effect": "greenScreen", "where": "mascot", "reason": "ivory light wrap + contact shadow integrate the 3D host"},
    {"at": 0, "effect": "cinematicOrbit", "where": "mascot camera + scene cameras", "reason": "slow orbit keeps every shot alive"},
    {"at": round(words[110]["start"], 3), "effect": "orbitReveal", "where": "s17", "reason": "3D GitHub mark revealed on 'repo'"},
    {"at": round(words[117]["start"], 3), "effect": "frameBreak/dynamic letters", "where": "s18", "reason": "EDITOR lands in the comment bubble"},
]
plan.sort(key=lambda e: e["at"])
cam = []
for e in plan:
    if e["effect"] == "snapZoom":
        cam.append({"fx": "snapZoom", "opts": {"target": "#world", "at": round(e["at"] - 0.02, 3), "amount": 0.06, "preset": e["preset"], "hold": 0.28, "release": 0.5}})
    elif e["effect"] == "digitalZoom":
        end = next(s["end"] for s in json.loads((P / "production/scenes.json").read_text())["scenes"] if s["start"] <= e["at"] < s["end"])
        cam.append({"fx": "digitalZoom", "opts": {"target": "#world", "at": round(e["at"] - 0.1, 3), "amount": 0.05, "dy": -18, "dur": 0.6, "preset": "SUBTLE", "releaseAt": round(end - 0.62, 3)}})
(P / "production/motion_plan.json").write_text(json.dumps({"generated_by": "tools/motion_director.py", "effects": plan}, indent=1, ensure_ascii=False))
(P / "production/director_camera.json").write_text(json.dumps(cam, indent=1))
for e in plan:
    print(f'{e["at"]:6.2f}  {e["effect"]:24} {e.get("preset", ""):9} {e.get("word", e.get("where", ""))}')
