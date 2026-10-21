# D. ASSET MANIFEST (relative paths rooted at extracted package)

| ID | Relative path | Role | Verified facts | Status | Rules / fallback |
|---|---|---|---|---|---|
| LOGO_RAW | `assets/brand/ai_preneur_logo_original.png` | Original identity | PNG RGBA, 1485×1485, bbox konten (158,655)-(1308,759) | **PROVIDED + VERIFIED** | Jangan recolor/warp/ubah teks; boleh crop transparent outer margin |
| LOGO_TRIM | `assets/brand/ai_preneur_logo_trimmed.png` | Logo placement | Derived from original by cropping transparent margins ±32px; no changed pixels in visible area | **DERIVED + VERIFIED** | Gunakan untuk scale/layout lebih praktis, original tetap bukti |
| BG_RAW | `assets/brand/pastel_background_original.jpeg` | Visual base/background | JPEG RGB 980×1225; pale ivory/ice-blue | **PROVIDED + VERIFIED** | Extension procedural untuk 9:16 boleh, jangan stretch/crop sehingga warna/komposisi tampak rusak |
| VO_MASTER | `assets/audio/vo_master_39s.wav` | Authoritative video VO | 44.1kHz mono PCM16, 39.381361s | **DERIVED + VERIFIED** | Tempatkan sekali di timeline, jangan juga play tiap audio part |
| VO_PREVIEW | `assets/audio/vo_master_preview.m4a` | Listening only | AAC 192k, preview | **DERIVED + VERIFIED** | Bukan audio tambahan di video; jangan tambahkan bersamaan dengan WAV |
| VO_PARTS | `assets/audio/original_parts/vo_01.mpeg` … `vo_11.mpeg` | Audit order/wording | 11 MP3 mono sumber asli yang tidak diubah | **PROVIDED + VERIFIED** | Dipakai untuk cek segment ambigu; BUKAN multi-track audio pada cut final |
| AUDIO_CUES | `production/audio_timeline.json` | Absolute timing authority | PCM sample boundaries, source hashes, ceil video frames | **DERIVED + VERIFIED** | Sumber utama precision; jangan pakai MP3 encoder padded duration untuk menggeser cut |
| WORD_TRANSCRIPT | *Belum ada* | Exact copy/word times | ASR tidak dapat diverifikasi dalam environment ini | **MISSING-ESSENTIAL BEFORE NARRATIVE LOCK** | Claude Code gunakan tool lokal/HyperFrames `transcribe` dengan multilingual support, cek manual proper nouns; jika gagal, minta script user |
| EXTRA_UI/PROPS | **Belum dibuat** | 2.5D/3D visual storytelling | CSS/SVG/Three berdasarkan VO, bukan external source | **CREATE WITH USER'S PRODUCTION PERMISSION** | Generate sendiri dari code untuk makna VO, tanpa fake screenshots/data |
| MUSIC | *Tidak ada* | Optional | No licensed track provided | **NOT PROVIDED / OMIT** | Silence except VO and rights-clear local SFX |
| REF_A / REF_B / REF_C | Tidak dicopy sebagai footage ke paket | Style design inspiration | Analisis timecode ada dalam `references/STYLE_DNA_SELECTED.md` | **REFERENCE ONLY** | Jangan masukkan video/frames/creator artwork ke final output |

**Checksum ringkas untuk aset inti:**

- Logo original: `8d43b339433be9c1b54f13c749974daccdafaa79e16f5fda86c2ab6feee2783d`
- Logo trimmed: `1d4ac13d17210063124116b3109749fc5ce01bf739b78b08d30c3c9f7fdfe709`
- Background original: `cd0c9c5df379d6e389ee7772b4bef3926ee76aa23fdbeee749e0d82650610ce7`
- VO master: `e4ee97fd37dd1267c6f4c1c503b2c693d9bc63bebd2a5f03dcdcfc50b58a6919`

**Scope path:** Semua nama di atas adalah **relative path di dalam ZIP**, bukan lokasi pasti setelah extract ke Windows. Claude Code harus memverifikasi lokasi aktual sebelum import. Tidak ada klaim bahwa file hasil render sudah dibuat.
