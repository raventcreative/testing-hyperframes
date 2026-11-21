# R33 notes

## Build
- Kit: white voxel (aip_voxel_uji look) on the R26 engine (vendor/vx.js + vxlib.js) + mascot host (vendor/mascot_host.js) + AIpreneur robot
  co-host ported from R29 (vendor/robot_host.js + robot3d.js, assets/robot3d). Big static assets are hard links to R26/R29/R27 files (disk).
- Pipeline: `python3 tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` → `python3 tools/words.py` → `python3 tools/vo_data.py`
  → `python3 tools/sfx.py` → `python3 tools/build.py` → `npx --yes hyperframes@0.8.186 check .` → render (render_aip.sh) →
  `bash tools/remix_audio.sh` (two-pass loudnorm, VO untouched) → whisper medium diff (`tools/fw_transcribe.py` + `tools/vo_diff.py`).
- Every time in vx.js / UI / mascot / robot / SFX is looked up from the VO alignment (wt(word, after)), so a re-take re-times everything.
- Cover: `python3 -m http.server 8833` in the project root, then `node thumbnail/render_cover.cjs <out.png> [dsf]`.

## Screen recording to ask Freddie for (client rule 2026-11-20) — the reel uses SIMULATED chat UI until then
Vertical 9:16, phone screen recording (or the WhatsApp Desktop/Claude Desktop window), 10–20 s each, no private chats on screen
(use a test chat or blur later):
1. WhatsApp on his phone: scrolling the chat list fast (≈10 s) — replaces the hook phone screen.
2. WhatsApp → Settings → Linked Devices → "Link a device" QR scanner (≈10 s) — replaces the QR-scan moment.
3. Claude Desktop with the WhatsApp integration enabled, asking one question about his own business chat and the answer streaming
   (≈15–20 s) — replaces the "Tanya pakai bahasa biasa" window.
4. Optional: the terminal running `go run main.go` showing the QR (≈10 s).
