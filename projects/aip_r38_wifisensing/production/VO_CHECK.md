# R38 VO + mix check (final out/AIP_R38_WIFI_SENSING.mp4, 47,6 s, 1080×1920, 30 fps, h264 + aac)
- VO = one untouched ElevenLabs take (assets/audio/vo.mp3, 45,87 s, Dakocan, eleven_v4, auto tags) at +0,3 s; no cuts, pads, splices
  or time-stretch. The picture follows the voice (beats = word times from the take's character alignment).
- Listen-check before build (whisper small + medium on the bare take): take 1 "ngubah" (small "ngebah", medium "mengubah") → reworded
  "mengubah"; take 2 "ngerasain gerakan" (medium "ngerasa imgerakan") → "mendeteksi"; take 3 "ESP32" (small AND medium "ASP32") →
  removed from the VO ("Sensor kecil"; ESP32-S3 shown on screen). Take 4 = final.
- whisper MEDIUM on the FINAL MP4 vs production/vo_lines.txt: 13 diffs, all spelling / number format / proper names — "Wi-Fi"→"Wi -Fi" (×3),
  "di balik"→"dibalik", "seratus"→"100", "sembilan"→"9", "napas"→"nafas" (×2), "AI-nya"→"AI -nya", "repo-nya"→"Repo -nya",
  "nggak"→"enggak", "RuView"→"Ruvio" (the project name, not in whisper's vocabulary), "Claude"→"Cloud" (as in R20/R34/R36, pronounced
  correctly). No missing / extra / chopped words; first word "Sinyal" intact; no low-probability words.
- SFX (tools/sfx.py, 101 events from vendor/r38.js): whoosh-in when the mascot comes forward + soft pop when it leaves, whoosh on every
  card, pops/clicks on chips/rows/logos, typing ticks, impacts on stamps, riser + impact + click on the CTA pill. Fixed level, no sidechain;
  every hit ≥70 ms off word onsets (81 moved); SFX peak −10,2 dBFS vs VO peak ≈ −1 dBFS. Music bed (tools/music_bed.py) ducked under VO.
- Loudness (two-pass loudnorm, tools/remix_audio.sh): integrated **−14,2 LUFS**, LRA 2,0 LU, true peak −4,3 dBFS.
- Render: hyperframes 0.8.186 via the shared-lock script, 0 page errors; `check` 0 errors (11 read-time warnings on fast sub-labels).
