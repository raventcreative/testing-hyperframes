# reel-33 — "laptop jalan sendiri"

White theme (base `light`), 59.6 s composition, VO 58.6 s. Built from reel-31's white template
(reel-26b is the blue one) with reel-30's `tools/layout_audit.cjs` carried in.

## Blocker: no voiceover yet

`tools/el_tts.py` fails with **HTTP 401 "Invalid API key"** — the proxy is not injecting a key for
`api.elevenlabs.io` (it forwards the literal `proxy-injected` placeholder, and the request reaches
ElevenLabs and is rejected). Checked twice with different request ids, and `curl $HTTPS_PROXY/__agentproxy/status`
shows no ElevenLabs relay failure, so the credential itself is the problem. **No audio was faked.**

Until the credential is restored:

- `production/word_timing.json` and `vendor/vo_words.js` hold **provisional** timings from
  `tools/provisional_timing.py` (3.05 words/s, 0.14 s clause gap, 0.30 s line gap). The phrase
  *texts* match what `align_whisper.py` produces for the same script, so every `ph("…")` anchor in
  `production/index.src.txt` survives the swap untouched.
- `assets/audio/vo.wav` is **deliberately absent**, so a render fails loudly instead of shipping silent.

To finish, in order:

```bash
python3 -I ../../tools/el_tts.py "$(sed 's/^[[:space:]]*$//' production/vo_script.txt)" assets/audio/vo.mp3
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
npm run check && python3 -I tools/robot_audit.py && node tools/layout_audit.cjs index.html "$(python3 -c "print(','.join(f'{x*0.37:.2f}' for x in range(1,161)))")"
```

`el_tts.py` and `voice_config.json` live at the repo root, not in this project. Reel-31's
`tools/pad_pauses.py` was removed from here: its pad timestamps are hard-coded for that reel and the
current rule keeps clause gaps ≤ 0.45 s anyway, so plain ffmpeg is the right conversion.

Real timings will shift every anchor slightly; re-read the contact sheet after the swap.

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
