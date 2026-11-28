# R36 VO + mix check (final out/AIP_R36_PETA_AI_AGENT.mp4, 55,5 s, 1080×1920, 30 fps, h264 + aac)
- VO = one untouched ElevenLabs take (assets/audio/vo.mp3, 54,2 s, Dakocan, eleven_v4, auto tags) at +0,3 s; no cuts, pads, splices
  or time-stretch. The picture follows the voice (beats = word times from the take's character alignment).
- Listen-check before build: take 1 → "aku kasih" ("apukasi") and "Riset" ("Reset") misheard by small AND medium → both lines
  reworded, whole take regenerated (take 2 = final).
- whisper MEDIUM on the FINAL MP4 vs production/vo_lines.txt: 5 diffs, spelling/number format only — "Tiga puluh"→"30",
  "tujuh"→"7", "follow-up"→"follow up", "agent"→"agen" (Indonesian spelling, same sound), "Claude"→"Klot" (the proper name; on the
  bare VO medium writes "Cloud", as in R20/R34 — pronounced correctly). No missing/extra/chopped words; first word "Ini" intact.
  (The SFX whoosh/pop before "Claude" were moved earlier and softened before the final mix.)
- SFX (tools/sfx.py, 161 events from vendor/r36.js): whoosh on every card/scene change, tick on each beat-counter change, pops/clicks on
  chips/rows/tiles/logos, typing ticks, impacts on stamps, riser + impact on the CTA pill. Fixed level, no sidechain; every hit ≥70 ms off
  word onsets (83 moved); peak −7,5 dBFS vs VO peak ≈ −1 dBFS. Music bed (tools/music_bed.py) ducked under the VO.
- Loudness (two-pass loudnorm, tools/remix_audio.sh): integrated **−14,4 LUFS**, LRA 2,1 LU, true peak −4,2 dBFS.
- Render: hyperframes 0.8.186 via the shared-lock script, 0 page errors; `check` 0 errors.
