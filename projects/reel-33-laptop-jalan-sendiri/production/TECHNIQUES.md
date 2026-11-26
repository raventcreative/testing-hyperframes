# reel-33 — "laptop jalan sendiri"

White theme (base `light`). **Composition 53.9 s, VO 53.36 s** (last word ends 52.94 s).
Built from reel-31's white template (reel-26b is the blue one) with reel-30's `tools/layout_audit.cjs`
carried in, plus two audits written for this reel: `tools/robot_audit.py` and `tools/beat_audit.py`.

## Voiceover

Real VO, ElevenLabs voice Dakocan, model `eleven_v4` (accepted first try — no model fallback needed),
one call with the whole script so the per-sentence tags stay in one take: `production/vo_text_sent.txt`.
Word timings from the local `align_whisper.py` (faster-whisper `small`, Indonesian): **136/139 tokens
matched**, the rest interpolated. Largest gap between caption phrases is **0.457 s**, so no pause padding
was needed and `tools/pad_pauses.py` (reel-31's, with hard-coded timestamps) was removed from here.

Getting there took three credential states, recorded because the error texts are easy to misread:

1. **HTTP 401 "Invalid API key"** — nothing was being injected; the literal `proxy-injected` placeholder
   was forwarded.
2. **HTTP 400 `authentication_error` / `api_key_id_used_as_api_key`** — a secret *was* injected, but it
   was the key's **ID**, not the key. A 400 here is still an authentication failure, not a payload problem;
   reproduced with a 3-word payload and with the full script, different request ids, identical error.
3. Working, once a value starting with `sk_` (shown only at key creation/rotation) was saved.

No audio was ever faked while this was blocked.

To regenerate, in order — `el_tts.py` and `voice_config.json` live at the repo root, not in this project:

```bash
python3 -I ../../tools/el_tts.py "$(cat production/vo_text_sent.txt)" assets/audio/vo.mp3
```

```bash
ffmpeg -y -i assets/audio/vo.mp3 -ac 1 -ar 44100 assets/audio/vo.wav
```

```bash
python3 -I tools/align_whisper.py . && python3 -I tools/vo_env.py .
```

```bash
python3 -I tools/build.py . && python3 -I ../../tools/add_robot3d.py .
```

```bash
npm run check && python3 -I tools/robot_audit.py && python3 -I tools/beat_audit.py
```

`align_whisper.py` carries this reel's 32 caption phrases hard-coded in its `PHRASES` block (reel-31's
were inherited and had to be replaced — it will otherwise align the audio against the wrong script and
produce timings that look plausible and are wrong).

## What the real timings changed

The provisional estimate was 58.93 s; the real VO is 53.36 s. The speaking rate was close, but the
**gaps between lines are far tighter than estimated** (0.14–0.46 s instead of 0.30 s flat), and that is
what broke things — not the overall length. Fixed after the swap:

- **`FX.iris` / `FX.doors` / `FX.shutter` are ~1.1 s long**, longer than any gap in this VO. What has to
  land on the beat is the wipe's **mid** (where the scene swaps), not its full open. `beat_audit.py`
  measures mid for wipes and full settle for camera moves; all ten transitions are now inside tolerance.
- The **S4 → S5 camera slide** (0.86 s) could not fit a 0.42 s gap and was still moving 0.22 s into
  "Bagian dua". Compressed to 0.50 s and started on the previous line's last word.
- The **window swing** was still turning 0.2 s into "Pas topiknya abis"; it now leads by 0.55 s.
- The **CTA wave** (1.9 s) overran the "link" point, so `runGestures` silently dropped that point — the
  kind of thing only the audit catches. Wave moved onto the question, point onto the word.
- **Elements that the shorter lines left no room for:** the "Kelar" plate landed 0.1 s before the shutter
  (dropped; the chain's fourth node is the payoff, and the nodes were scaled up to fill the panel), the
  verdict bar had 0.58 s (moved onto its line), the run chips had 0.48 s (moved into the previous line),
  the schedule footer had 0.52 s, and the third gate tick had 0.2 s (each tick is now stamped just
  *before* its word, and the gates clear later).
- **Containers that were briefly empty** because their content was keyed to a line that had moved: the
  hook's phone, the four-lane panel, the week table. All now arrive with their content.
- The CTA held 7 s frozen; the dead tail was trimmed and the closing line given its own beat.
- `tools/build.py` SFX were re-keyed to the new anchors (and spread over 8 tracks, which cleared the
  overlapping-audio warnings).

## Scene shapes — no shape used twice

| # | beat | shape |
|---|------|-------|
| 1 | hook | full-bleed laptop + phone, **outside the app window** — a render finishing by itself, a phone asking for an OK, the OK tapped |
| 2 | jadwal | round clock dial (the only circle in the reel) + schedule card |
| 3 | empat bagian | one long prompt block that **splits into four numbered lanes** |
| 4 | panduan | a sheet of paper with a file tab, checkboxes ticking, an edit caret |
| 5 | topik | seven-row week table with status pills belum → proses → selesai |
| 6 | gaya | three vertical episode cards sharing one fingerprint, joined by a verdict bar |
| 7 | suara | script line → arrow → dark waveform strip drawing left to right |
| 8 | ide | **phone pop-out outside the window**, researching, then five ideas and a "Bales 2" |
| 9 | alur | four-node chain with a travelling dot, then a Kelar plate |
| 10 | gerbang | three gate cards stamped ✓, a struck-through grey "posting otomatis" bar (no red) |
| 11 | keputusan | everything clears; one plate carries the closing line, robot risen beside it |
| — | CTA | fixed AIpreneur Automation card |

## Transitions — ten, none repeated

zoom punch-through the laptop screen → tab click + camera slide → **FX.iris** → camera slide →
**FX.doors** → zoom punch-in → 3D swing + pop-out → zoom-out reveal → **FX.shutter** → zoom-through to CTA.

Four zoom transitions (brief asked for ≥2), plus iris and doors as specified.
`FX.sweep` was tried for the ninth and replaced: in the white theme it is a solid white band over a
white background, so mid-wipe frames read as an empty screen. `shutter` keeps visible banding.
`dots` stays banned.

## Robot

`tools/robot_audit.py` replays the pose track against the gesture queue and asserts the result —
it does not eyeball it. Current state: **14 gestures, 0 skipped by `runGestures`, hands alternate
strictly LEFT/RIGHT/LEFT/…, 14 pose moves, 3 side rises** (upR 14.1 s with the document on the left,
upL 36.5 s with the phone on the right, upR 49.3 s with the plate on the left). Never centred over the
element being explained, never zoomed or cropped, whole and centred-bottom at the CTA.

The mechanism, for whoever edits this next: `point` uses the arm **away** from the robot's side
(`R ? lh : rh`), so alternating hands means alternating the robot's side between point beats. `go()`
registers its new pose at `at + dur/2`, and `runGestures` silently drops any gesture starting less
than 0.05 s after the previous one ends — points need ≥1.75 s of separation.

## Checks that found real defects here

- **`tools/layout_audit.cjs`** (160 samples, now 160/160 clean) caught: text past its own box edge on
  the laptop's `100%` readout, on `16.00` and on the schedule footer; the long prompt card overlapping
  the lanes it becomes; the voice-scene card sitting behind the phone pop-out; flow nodes touching on
  their pulse; and the decision plate landing on top of the gate cards.
  Poppins' ascent exceeds its em box, so large type needs `line-height ≥ 1.5` to stay inside its own box.
- **Contact-sheet reading** (the way the client reads it) caught five near-empty frames that no
  automated check flags: an emptied phone after the OK, a table/panel/waveform/phone appearing before
  its contents, and a white gap between the pop-out leaving and the next scene arriving. Every
  container now arrives with its content, or with a working state of its own
  (the phone shows "lagi riset tren sendiri" before the ideas land).
- The **no-cut-text guard** hides any text unit sliced by the camera frame. A full-width centred box
  (`left:0; right:0`) is *always* counted as sliced at scale 1, so centred labels need a bounded
  width — that is why `#dialNum` / `#dialSub` are `left:70px; width:340px`.
