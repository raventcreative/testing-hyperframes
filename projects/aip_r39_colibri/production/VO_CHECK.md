# R39 · VO check on the FINAL MP4 (out/AIP_R39_COLIBRI.mp4)

- VO: ONE untouched ElevenLabs take (take 4; Dakocan, eleven_v4, auto tags), 63.40 s, delayed 0.3 s; not cut, padded, spliced or
  stretched. Takes 1–3 were regenerated in full after rewording words BOTH whisper small and medium misheard (see VO_SCRIPT.md).
- whisper **medium** on the final MP4, word diff vs production/vo_lines.txt (tools/vo_check.py): 13 diffs, all spelling /
  number-format / word-joining only:
  delapan giga→8GB (×2), enam belas giga→16 GB, tiga puluh dua giga→32 GB, giga→GB, Colibri/COLIBRI→Kolibri (×2, same sound;
  "kolibri" is the Indonesian word), cepat→cepet, DeepSeek→DeepSec (brand-name spelling; every wording tested gave a variant),
  Qwen→Quen, chat-nya→"chat -nya", link-nya→"link -nya", per ukuran→perukuran.
  No dropped words, no chopped onsets ("Model", "Kimi K3", "Posisinya" all heard intact).
- Loudness (ebur128 on the final MP4): I −14.4 LUFS, LRA 1.5 LU, true peak −4.3 dBFS: −14 LUFS ±1 (two-pass loudnorm,
  tools/remix_audio.sh: VO + SFX at a fixed level + synthesised bed ducked under the VO; video stream copied).
- SFX: 116 cues from the composition (tools/sfx_events.cjs → tools/sfx.py): whoosh per card in/out, pops/clicks/keys/pings on UI
  actions, a soft whoosh-in when the mascot comes forward and a pop-out when it leaves, riser + impact on the CTA. Fixed level, p90
  window peaks ≈ 9 dB under the VO p90 (SFX +2 dB in the remix), none within 70 ms of a word onset (50 cues nudged), no sidechain on SFX.
