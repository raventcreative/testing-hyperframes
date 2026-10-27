"""Scene specs -> production/STORYBOARD_FINAL.md (times + words pulled from the measured VO)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
SPEC = {
 "s00": ("ACT 0", "Cold open — proof before explanation",
   "0.00–0.60: three hard-cut micro previews of OUR results (01 Orbit, 11 Paper Cutout, 17 Frame Break self-shots) on a punch-in, click on each. "
   "'polos': they fold into ONE plain clip panel (smoked-glass frame, mascot medium inside, tiny REC). 'Dua puluh efek': 20 numbered cyan-acrylic chips burst out in a ring around the panel + big `20 EFEK` (20 in cyan). "
   "'Lihat hasilnya': chips orbit and collapse into the panel, camera pushes into the panel.",
   "MED inside panel clip; push-in", "→ S01: panel grows to the plain source frame"),
 "s01": ("ACT 0", "The boring source",
   "Single plain video panel (thin white border, flat lighter-navy cyc, small timecode). Deliberately effect-free. Mascot medium, a small head turn on 'diam' (never frozen > 0.6 s). "
   "Last 0.35 s: the panel's corner radius grows and it shrinks into a tilted ellipse ring around the head.",
   "MED, lock-off", "→ S02: panel border becomes the orbit ring"),
 "s02": ("ACT I", "01 ORBIT",
   "Tilted orbit ring (thin white + cyan glint) round the head; 4 smoked-glass icon chips (audio wave, 'Aa' caption, image, cursor) orbit 1.25 turns: on the far half they are in the BACK layer (hidden by the head), on the near half in the FRONT layer. Contact glints. Camera to a 3/4 (yaw −14). Head follows the icons.",
   "MED → 3/4", "→ S03: the round caption chip flies forward = chat avatar"),
 "s03": ("ACT I", "02 CHAT TAKEOVER",
   "Smoked-glass chat window grows out of the avatar circle and takes the frame. Messages (VO words): user bubble 'Satu klip polos.' → reply bubble that contains a small LIVE preview of the mascot (clipped, mascot small) + 'Dua puluh efek.'; a cursor clicks the preview.",
   "mascot clipped into the preview bubble (h≈520)", "→ S04: the preview bubble border becomes a physical frame"),
 "s04": ("ACT I", "03 FRAME ESCAPE",
   "Navy-porcelain picture frame (thickness, bevel, contact shadow) holds the clipped mascot; on 'keluar' the frame tilts back/recedes while the clip releases from the top: the mascot comes forward out of the frame (camera + frame move, no fake leg walk).",
   "clip → none, h 900 → 1470", "→ S05: frame corners become the viewfinder corners"),
 "s05": ("ACT I", "04 SNAP ZOOM",
   "Viewfinder corners + centre reticle. 'menghantam': anticipation pull-back 0.15 s, 0.28 s push to a real close-up (re-framed camera, not bitmap scale), 0.16 s settle with tiny overshoot. HERO APEX #1 on the snap. Hold the close-up through 'close-up.' (reaction: head tilt).",
   "MED → CU (face fills)", "→ S06: reticle circle round the eye becomes the first check circle"),
 "s06": ("ACT I", "05 CHECKLIST POP",
   "Mascot 3/4 left; 4 enamel pills with cyan acrylic check discs pop in his eye line on the right with 80 ms stagger: 01 Orbit, 02 Chat Takeover, 03 Frame Escape, 04 Snap Zoom (the effects we just saw). Check strokes draw, rim glint, shadows.",
   "3/4, fx 400", "→ S07: last pill stretches into a headline strip"),
 "s07": ("ACT II", "06 HEADLINE STORM",
   "Headline strips (Poppins Bold, VO words only: JUDUL BERHAMBURAN, DUA PULUH EFEK, SATU KLIP POLOS, CLOSE-UP, CHAT) cross in perspective at different depths, some behind the mascot, some in front (never over the face). The centre strip slows and locks.",
   "MED, slight dutch", "→ S08: centre strip curls into a ring"),
 "s08": ("ACT II", "07 ZOOM PORTAL",
   "Satin-metal ring with cyan acrylic inner rim in front of the chest; inside it (mask) the graph world (grid + rising curve). 'portal': camera flies through — ring grows past the lens. HERO APEX #2 on the pass.",
   "MED → push", "→ S09: we exit inside the graph world"),
 "s09": ("ACT II", "08 GROWTH CURVE",
   "Matte grid floor in perspective; an SVG curve draws from lower-left to upper-right behind the mascot, nodes light segment by segment (no numbers/axes values). Camera follows the curve up. Mascot full body.",
   "WIDE", "→ S10: the curve's end becomes a studio light cable"),
 "s10": ("ACT II", "09 STUDIO REVEAL",
   "Dim stage (mascot dimmed). The cable runs to two satin-metal light stands; their arms open on 'perubahan gayanya'; on 'Studio menyala' softboxes switch on, beams + floor pool, mascot lit (brightness up), small `STUDIO` signage in cyan.",
   "WIDE → MED 3/4", "→ S11: the key beam rectangle opens the editor monitor"),
 "s11": ("ACT II", "10 B-ROLL OVERLAY",
   "The mascot clip plays in a monitor (clipped). 'B-roll menumpuk': 3–4 B-roll tiles (self-shots of our earlier effects) stack over the video with slight rotation. 'timeline editornya terbuka': timeline panel opens (V1/V2/A1 tracks, playhead), the tiles drop into V2, cursor drags one. Camera tilts over the timeline.",
   "mascot clipped in the monitor", "→ S12: a paper-textured tile lifts off = the paper set"),
 "s12": ("ACT III", "11 PAPER CUTOUT", "BUILT (prototype). See tools/scenes/s12.py.", "WIDE", "→ S13: floor paper edge stretches = rail"),
 "s13": ("ACT III", "12 DOLLY ZOOM", "BUILT (prototype). See tools/scenes/s13.py.", "WIDE (constant size)", "→ S14: viewfinder rect = cover border"),
 "s14": ("ACT III", "13 MAGAZINE COVER", "BUILT (prototype). See tools/scenes/s14.py.", "cover portrait (clipped)", "→ S15: cover gloss band = glass highlight"),
 "s15": ("ACT III", "14 LIQUID GLASS",
   "A tall curved glass slab (rounded, thick bevel, edge highlights, chromatic fringe lines) sweeps across the mascot; inside it a simulated refraction (backdrop blur/saturation band + bent highlight). Honest simulation — no full-screen cheap blur. The slab slows over the face on 'melengkung'.",
   "MED", "→ S16: the slab curls into a round lens aperture"),
 "s16": ("ACT III", "15 ZOOM THROUGH CUT",
   "Satin-metal iris aperture centred on the face opens; the camera pushes through a thin frame and into the eye (ECU) with a speed ramp; the pupil's dark becomes the opening of the next world.",
   "MED → ECU", "→ S17: the aperture opening already holds the skyline"),
 "s17": ("ACT IV", "16 GREEN SCREEN",
   "Mascot on a green cyc (soft floor) for a beat; 'latar kota': a cyan key line wipes the green away to an original navy city skyline (layered towers, lit windows, parallax), rim light matches.",
   "MED/WIDE", "→ S18: vertical building lines become the crack lines"),
 "s18": ("ACT IV", "17 FRAME BREAK",
   "'pecahkan': cracks run from the face; the frame splits into ~14 shards (polygon copies of OUR S17 frame) that tilt and fall away in one consistent direction, revealing the HUD scene. HERO APEX #3.",
   "—", "→ S19: edge shards settle as HUD corner guides"),
 "s19": ("ACT IV", "18 DIGITAL ZOOM",
   "Camera HUD: four corner guides, REC (cyan dot), zoom read-out 1.0× → 1.5× → 2.0× in steps, mascot face punched in each step (re-framed, sharp).",
   "MED → CU steps", "→ S20: the guides close into the phone bezel"),
 "s20": ("ACT IV", "19 PHONE MOCKUP",
   "Navy-porcelain phone (bezel, side buttons, camera island, glass reflection, contact shadow) forms from the HUD guides; its screen plays our own result (live mascot clipped to the screen + mini header). Phone turns on 'HP.'",
   "mascot clipped to the screen", "→ S21: phone back = checklist board"),
 "s21": ("ACT IV", "20 CHECKLIST",
   "Two-column board of all 20 effect names (Poppins ≥ 28 px), checks chain 01→20, a cyan focus slides; macro on the last two names; then a cyan line links the items ('bukan efeknya satu-satu'). Mascot small at the side pointing.",
   "small, side", "→ S22: the linking line becomes the paper edge"),
 "s22": ("ACT V", "The secret is continuity",
   "Mascot left, pointing. Three cards (self-shots of 11 Paper Cutout, 12 Dolly Zoom, 13 Magazine Cover). 'Tepi kertas' lights the paper edge; 'rel kamera' it morphs into the rail; 'Rel itu membawa kita ke scene berikutnya' a mini dolly rides the rail into the cover card, which grows.",
   "MED left", "→ S23: the card becomes the code panel"),
 "s23": ("ACT V", "Claude Code workflow",
   "Four chained props FOOTAGE → BRIEF → CODED SCENES → PREVIEW (smoked-glass cards, cyan connectors). A conceptual code panel (not an official UI) types a few lines; 'Claude Code' label in text only. Mascot hands the brief card over.",
   "MED right", "→ S24: the preview card widens into the montage"),
 "s24": ("ACT V", "Human direction + checks",
   "Montage grid of 6 self-shots (our results). Three human checks pop on their words: `Arahan visual`, `Timing`, `Pengecekan hasil` (checks draw). Honest framing: AI builds, a human directs and reviews.",
   "MED", "→ S25: grid folds into the CTA plate"),
 "s25": ("ACT V", "CTA — KOMEN EDIT",
   "Mascot centre, pointing at the viewer. Three deliverable chips on their words: `Daftar 20 efek`, `Breakdown scene`, `Prompt`. 'Komen EDIT': comment card with EDIT in cyan Bold — HERO APEX #4; logo final sheen; last 0.4 s is a calm, complete brand frame (no fade to black).",
   "MED", "end frame"),
}
wt = json.loads((P / "production/word_timing.json").read_text())
sc = json.loads((P / "production/scenes.json").read_text())
W = wt["words"]
out = ["# STORYBOARD FINAL — 1 klip → 20 transformasi → cara bikin → hasil → KOMEN EDIT", "",
       f"Locked to the real VO (`assets/audio/vo_20effects_elevenlabs.mp3`, {wt['audio_duration']} s). Duration {sc['duration']} s (VO + 0.41 s brand hold). 30 fps, 1080×1920.",
       "Every cut sits ~0.08 s before the first word of its scene (frame-snapped). Times in seconds.", "",
       "Framing presets (`tools/scenes/kit.py`): MED = medium hero (feet 1800, figure 1470 px, face ≈ y 922); WIDE = full body (feet 1720, figure 1150); CU / ECU = camera re-framed closer (real 3D re-render, not CSS scale).",
       "Fixed screen: logo top-left (x 64, y 72, w 265); effect header (badge + label + 20-dot progress) at y 128–206; captions lower third y 1404–1540 (max 2 lines, cyan keywords Bold); Reels UI safe zone respected.", ""]
for s in sc["scenes"]:
    act, title, body, frame, hand = SPEC[s["id"]]
    words = " ".join(w["text"] for w in W if s["start"] - 0.02 <= w["start"] < s["end"] - 0.02)
    out += [f"## {s['id'].upper()} · {title}  ({s['start']:.2f}–{s['end']:.2f}, {s['dur']:.2f} s) · {act}",
            f"- **VO:** “{words}”", f"- **Visual:** {body}", f"- **Mascot framing:** {frame}", f"- **Hand-off:** {hand}", ""]
out += ["## Hero apexes (only these get the brightest bursts)", "S05 snap (≈10.2 s) · S08 portal pass (≈14.9 s) · S12 paper flip (≈23.9 s, soft) · S18 frame break (≈30.9 s) · S25 EDIT (≈50.0 s).", ""]
(P / "production/STORYBOARD_FINAL.md").write_text("\n".join(out))
print("ok")
