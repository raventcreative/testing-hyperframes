# R35 VO + mix check (final out/AIP_R35_GITHUB_7_TOOLS.mp4, 87.0 s, 1080×1920, 30 fps)
- VO = one untouched ElevenLabs take (assets/audio/vo.mp3, 85.36 s, voice Dakocan, eleven_v4) at +0.3 s; no cuts, pads, splices or
  time-stretch. The PICTURE follows the voice: scenes were blocked on an earlier take; after two lines were reworded (ATM overlap
  "Ada versi Windows, Mac dan Linux"; "Asisten" misheard as "Assistant") the whole take was regenerated and the scene timeline is
  re-mapped onto the new word times (tools/warp.py → vendor/warp.js, 196 word anchors; captions/lip sync use the final take directly).
- whisper MEDIUM on the final MP4 vs production/vo_lines.txt: 19 diffs, all spelling/number format — numbers as digits (Tujuh/Satu/Dua/
  Tiga/Empat/Lima/Enam/ketujuh → 7/1/2/3/4/5/6/"ke 7", dua → 2), open-source → "open source", ChatGPT → "chat GPT", AI-nya/link-nya →
  "AI -nya"/"link -nya", Upscayl → "Upscale" (the app's own pronunciation), transkrip → "transkript", ComfyUI → "Comfy UI",
  node → "note", Komen → "Comment" (same sound; Indonesian "komen" = comment). No missing/extra/chopped words; first word intact.
- Listen-check history: take 1 "ngedit" heard as "edit" by small+medium → reworded "mengolah"; take 3 "Asisten" heard as "Assistant" by
  both → reworded "Buat meeting"; take 4 = final.
- SFX (tools/sfx.py): whoosh on every transition (23), riser + soft impact on reveals, pops/clicks on titles, tags, objects, a soft tick on
  each of the 78 caption chunks, typing ticks on scripted windows. Hits ≈ −10…−14 dBFS (peak −5.7) vs VO sample peak ≈ −1 dBFS → about
  8–10 dB under VO peaks; every hit moved ≥70 ms off word onsets (159 moved). SFX at fixed level (no sidechain); music bed ducked under VO.
- Loudness (two-pass loudnorm, tools/remix_audio.sh): integrated −14.4 LUFS, LRA 1.9 LU, true peak −4.1 dBFS.
- Render: hyperframes 0.8.186, 0 page errors; `npx hyperframes check .` 0 errors.
