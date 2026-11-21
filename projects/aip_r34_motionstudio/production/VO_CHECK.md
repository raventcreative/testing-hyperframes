# R34 VO check (final MP4 out/AIP_R34_MOTION_STUDIO.mp4, 42.0 s)
- VO = one untouched ElevenLabs take (assets/audio/vo.mp3, 40.99 s), placed at +0.3 s; no cuts, pads, splices or time-stretch.
- whisper MEDIUM on the final MP4, word diff vs production/vo_lines.txt: 10 diffs, all spelling/number format only:
  open-source→"open source", Claude→"Cloud"/"Clot" (whisper's usual spelling of Claude, same as R11–R30), "delapan puluh tujuh ribu"→"87.000",
  GreenSock→"Green Sock", Empat→"4.", diedit→"di-edit", repo-nya→"riponnya". No missing, extra or chopped words (first word "Video" intact,
  every line present in order, word onsets match the alignment within ~0.05 s).
- Pre-check on the raw take: whisper small + medium; no word misheard by both apart from the Claude spelling → take kept.
- Mix: SFX at a fixed level (volume 0.6, no sidechain on SFX; every SFX hit moved off VO word onsets ±70 ms, tools/sfx.py), music bed ducked
  under the VO (sidechain on the bed only), two-pass loudnorm (tools/remix_audio.sh).
- Loudness: integrated -14.5 LUFS, LRA 2.1 LU, true peak -4.4 dBFS.
