# R34 VO + mix check (final out/AIP_R34_MOTION_STUDIO.mp4, 42.0 s — brand-plate version with the client's Claude Code recording)
- VO = one untouched ElevenLabs take (assets/audio/vo.mp3, 40.99 s) at +0.3 s; no cuts, pads, splices or time-stretch (unchanged since v1).
- whisper MEDIUM on the final MP4 vs production/vo_lines.txt: 10 diffs, spelling/number format only — Claude→"Cloud"/"cloth" (whisper's
  spelling of Claude, as in R11–R30), "delapan puluh tujuh"→"87", GreenSock→"Green Sock", open-source→"open source", Empat→"4.",
  diedit→"di-edit", repo-nya→"riponnya". No missing/extra/chopped words; first word "Video" intact; onsets match the alignment.
- SFX (client: "kasih sound effect biar gak suara VO aja"): tools/sfx.py rebuilt — whoosh on all 17 transitions, riser + soft impact on the 4
  reveals (zoom-out, portal, lens dive, CTA), UI pops/clicks (title tabs, tags, logos, crates, cards, click highlights, CTA send/DM), a soft
  tick on each of the 36 caption chunks, typing ticks (index.html, star counter, prompt, STUDIO). Hits ≈ −10…−12 dBFS (loudest −6.8) vs VO
  sample peak −1 dBFS → ~8–10 dB under the VO peaks; every hit kept ≥70 ms off word onsets (energy-onset scan: 0 transients within 50 ms).
  SFX at a fixed level in the mix (volume 1.0, no sidechain on SFX); music bed ducked under the VO only.
- Loudness (two-pass loudnorm, tools/remix_audio.sh): integrated −14.5 LUFS, LRA 2.1 LU, true peak −4.3 dBFS.
