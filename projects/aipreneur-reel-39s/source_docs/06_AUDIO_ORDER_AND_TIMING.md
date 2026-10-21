# AUDIO MASTER AND SEGMENT ORDER

**Use only `assets/audio/vo_master_39s.wav` for final VO.** Original clips are for forensic review and word-by-word transcription QA. The user says audio files are already ordered; this pack assumes chronological naming + duplicate suffix order. **Check actual sentence flow with the transcript**; don't assert semantic order was verified here.

| Cue | Start (s) | End (s) | Durasi (s) | File di paket | Copy yang diketahui |
|---|---:|---:|---:|---|---|
| VO01 | 0.000 | 3.379 | 3.379 | `assets/audio/original_parts/vo_01.mpeg` | **Menunggu transkripsi audio** |
| VO02 | 3.379 | 6.026 | 2.647 | `assets/audio/original_parts/vo_02.mpeg` | **Menunggu transkripsi audio** |
| VO03 | 6.026 | 8.336 | 2.310 | `assets/audio/original_parts/vo_03.mpeg` | **Menunggu transkripsi audio** |
| VO04 | 8.336 | 11.935 | 3.599 | `assets/audio/original_parts/vo_04.mpeg` | **Menunggu transkripsi audio** |
| VO05 | 11.935 | 14.582 | 2.647 | `assets/audio/original_parts/vo_05.mpeg` | **Menunggu transkripsi audio** |
| VO06 | 14.582 | 19.888 | 5.306 | `assets/audio/original_parts/vo_06.mpeg` | **Menunggu transkripsi audio** |
| VO07 | 19.888 | 24.265 | 4.377 | `assets/audio/original_parts/vo_07.mpeg` | **Menunggu transkripsi audio** |
| VO08 | 24.265 | 28.073 | 3.808 | `assets/audio/original_parts/vo_08.mpeg` | **Menunggu transkripsi audio** |
| VO09 | 28.073 | 31.161 | 3.088 | `assets/audio/original_parts/vo_09.mpeg` | **Menunggu transkripsi audio** |
| VO10 | 31.161 | 35.701 | 4.540 | `assets/audio/original_parts/vo_10.mpeg` | **Menunggu transkripsi audio** |
| VO11 | 35.701 | 39.381 | 3.680 | `assets/audio/original_parts/vo_11.mpeg` | **Menunggu transkripsi audio** |

WAV audio sample count: **1736718** @ 44,100 samples/sec = **39.381361 seconds**. Video output at 30fps is **39.40s** = **1182 frames** (ceil to next frame), not 39.83s padded original media duration.

Peak after global -1.5dB attenuation ≈ -1.04 dBFS, and joins have 2ms boundary ramps. MP3 source files remain unchanged. No automatic speed-up, noise suppression, new TTS or pause insertion. Master audio should not be trimmed or silence-padded to 39.40s beyond the tiny natural last-frame gap unless HyperFrames requires exact duration alignment. If extra music is added, mix carefully with narration and verify output peak/ducking.
