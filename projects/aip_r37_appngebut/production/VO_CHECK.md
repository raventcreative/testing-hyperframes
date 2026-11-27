# R37 · VO check on the FINAL MP4 (out/AIP_R37_APP_NGEBUT.mp4)

- VO: ONE untouched ElevenLabs take (Dakocan, eleven_v4, auto tags), 84.61 s, delayed 0.3 s — not cut, padded, spliced or stretched.
- whisper **medium** on the final MP4, word diff vs production/vo_lines.txt (tools/vo_check.py): 14 diffs, all spelling /
  number-format / word-joining only:
  Claude→Cloud (×2, known since R11), pelangganku→"pelanggan ku", dua puluh empat→24, divirtualisasi→"di virtualisasi",
  file-nya→"file -nya", per halaman→perhalaman (×2), Script→Skrip, dobel→double, ke layanan→kelayanan, ke antrean→keantrean,
  satu→1 (in "N plus satu"), prompt-nya→"prompt -nya". No dropped words, no chopped onsets.
- Loudness (ebur128 on the final MP4):  I −14.3 LUFS, LRA 1.5 LU true peak −3.9 dBFS; −14 LUFS ±1 (two-pass loudnorm, tools/remix_audio.sh).
- SFX: 220 cues from the composition (tools/sfx_events.cjs → tools/sfx.py), fixed level (p90 window peaks ≈ 9 dB under the VO
  p90), none within 70 ms of a word onset (95 cues nudged), no sidechain on SFX; synthesised music bed ducked under the VO.
