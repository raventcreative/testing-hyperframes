# 13 — PRODUCTION PIPELINE THAT PRODUCED REF-H (repeat this exactly)
**Version:** V3.0. This is the process Claude Code followed to build the approved v3 Reel. The style (doc 11) only comes out consistently when this process is followed, especially the **scene split + one-hero-per-phrase + visual review loop**.

## Phase 0 — Inputs & transcript gate (no visuals before the words are known)
1. Inventory: VO audio (one master track), logo (transparent PNG, ideally alpha-trimmed), optional BG plate. Verify durations with `ffprobe`.
2. Transcribe locally (free): `npx hyperframes transcribe <vo.wav> --model large-v3 --language id --json` (multilingual model; never `*.en` for Indonesian). Save `production/transcript_machine.json` + `production/transcript_review.md` (status: machine → reviewed).
3. Review brand names and spellings (e.g. "AI-preneur" → **AI PRENEUR**) and ask the user to confirm only the doubtful ones.
4. Word timing: whisper.cpp word starts can run ~0.3 s early (measured on REF-H). Anchor them: detect pauses with `ffmpeg -af silencedetect=noise=-38dB:d=0.12`, then check which words come before each pause (optional helper scripts in `house_style_kit/tools/`). Caption and apex timing use these anchored starts.
5. Derive: one core takeaway, the hook (first phrase), any spoken CTA. If no CTA is spoken, none is shown.

## Phase 1 — Scene split (the backbone of the style)
- Split the transcript into **spoken phrases**; each phrase = one scene (0.8–5.5 s; ~2.6 s average). Cut at the gap before the phrase's first word.
- For each scene pick ONE physical metaphor from the catalog (doc 11 §9) or a new one in the same spirit. Write a one-line visual plus the key word(s) where the apex lands.
- Record the plan in `STORYBOARD.md` as a table: `Scene | Global start–end | VO phrase | Visual metaphor | Apex word(s)`.
- The final scene = closing/recap + genuine logo lockup, ending on a still brand frame.

## Phase 2 — Scaffold
```bash
npx hyperframes init <project> --example blank --resolution portrait --non-interactive --skip-transcribe
# copy house_style_kit/starter/* into the project (index.html, compositions/_scene_template.html, assets/brand/*, vendor/gsap)
```
Fill in `index.html`: title, total duration (= VO end rounded up to a whole frame), VO file + duration, the `W` word list (display text + anchored start), `CAPS` (one caption per scene with key words), and one `<div id="sNN" data-composition-src="compositions/sNN.html" …>` per scene with global start/duration (alternate track-index 2/3/4). Create a placeholder for each scene from the template. Run `npx hyperframes lint` and a snapshot to prove the mounting works.

## Phase 3 — Build the scenes (parallel)
- **Up to ~6 scenes:** build inline, one after another.
- **More than 6:** use subagents. Give each worker **2–3 scenes**, spawn them all in **one wave**, and pass each of them:
  1. doc 12 (scene contract) — complete,
  2. a one-line summary of every scene in the video (continuity),
  3. for each assigned scene: file path, duration, global start, the VO phrase with **scene-local word times**, the metaphor, required micro-details, the beat list (what happens on which word), and special rules (e.g. logo usage, "deliberately flat").
- **Worker brief template (per scene):**
```
### sNN — compositions/sNN.html, duration D s (global A–B). VO: "<phrase>" — word1 t1, word2 t2, …
Metaphor: <concept> → <hero object>. Hero details: <materials, parts, micro-details>.
Beats: frame 0 <already moving…>; <word> tX: <action>; <key word> tY: APEX <what happens>; end: <hold/ambient>.
Special: <logo rules / text allowed / continuity with sNN-1 and sNN+1>.
```
- Workers lint and snapshot their own scenes and iterate at least twice before reporting.

## Phase 4 — Director review (the lead agent, not the workers)
1. Snapshot every scene midpoint + key words: `npx hyperframes snapshot . --at <list> --no-end -o .hyperframes/review`.
2. Compare the contact sheets against `golden_frames/`: hero size, detail density, light direction, shadow, palette, caption clearance. Fix weak scenes (empty frames, small heroes, flat objects, text crowding).
3. Check continuity at the cuts (object/colour handoff where it makes sense).

## Phase 5 — Gates
1. `npx hyperframes check` → 0 errors. Mark intentional overlaps with `data-layout-allow-overlap` (extruded type layers, engraved text, double labels, typed characters). Fix real ones (tween tails, contrast).
2. Determinism: snapshot the same 6–7 times in two different orders; the pixel difference must be 0.
3. Review the full assembled timeline (draft render `--quality draft` or Studio preview) and get the **user's approval** before the final render (official HyperFrames gate).

## Phase 6 — Final render & MP4 QA
```bash
npx hyperframes render --quality delivery --fps 30 -o out/<slug>_final.mp4
```
Verify with ffprobe: 1080×1920, 30/1, nb_frames = duration × 30, H.264 + AAC. Check loudness (ebur128), VO audible through the last word, no black segments (`blackdetect`). Extract and view frames from the **exported MP4** at every scene midpoint plus the last frame (it must be the still brand lockup). Report only verified facts.

## Measured reference numbers (REF-H)
- 15 scenes / 39.4 s · lint 0 errors · check 0 errors, 31/31 text contrast checks pass · deterministic (0 px diff) · render ≈ 7 min (software GPU, 4 cores) · 40.9 MB at delivery quality.
