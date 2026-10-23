# D — ASSET MANIFEST

| Relative path | Status | Observed details | Handling |
|---|---|---|---|
| `assets/background_asli.png` | PROVIDED / verified file | 1080×1350 RGB | Background wajib. Adapt 9:16 tanpa stretch. |
| `assets/kotak_highlight_asli.png` | PROVIDED / verified file | 1080×1350 RGBA, horizontal navy rounded-rectangle bar | Referensi visual. Implementasi CSS adaptif diperbolehkan. |
| `reference/video_original_64s.mp4` | PROVIDED / probed | 720×1280, H.264 30fps + AAC; total ±64.319s | Sumber urutan cerita/VO, jangan dipakai sebagai cutaway di final. |
| `assets/voice_source_full.m4a` | PROVIDED / SOURCE ONLY | Original AAC audio extracted with stream copy; ±64s | **Do not use in V2 timeline.** Only inspect old reference if useful. |
| `07_VO_ELEVENLABS_READY.txt` | PROVIDED / copy verified | Locked Indonesian VO wording | Paste in ElevenLabs; don't insert timing/directions. |
| `assets/vo_elevenlabs_final.mp3` | **PROVIDED / ffprobe verified** | Freddie's ElevenLabs MP3, duration 61.07425s, mono 44,100 Hz, MP3 ~994 KB | **Only VO** to mount in final timeline. Review against VO TXT, align words and phrase apex; no source VO. |
| `mascot/mascot_three_view_source.png` | PROVIDED / inspected | 1536×1024 opaque source image, front/side/back view, labelled bottom; chibi AI PRENEUR polo | Extract clean non-destructive cutouts, mask white sheet/labels; whole-sprite motion only until rig/layers supplied. |
| `reference/quality_motion_ref_H.mp4` | PROVIDED / video quality reference | Approved AI PRENEUR REF-H | Contoh craftsmanship/tempo/depth, **bukan** palet/type untuk remake ini. Jangan reuse visual/footage. |
| `reference/ref_H_overview.jpg` | PROVIDED / storyboard stills | REF-H overview contact sheet | Periksa detail density & scene silhouette; bukan aset di final. |
| AIpreneur genuine logo transparent | MISSING / OPTIONAL | Tidak ada logo asli di attachment | Jangan gambar ulang. Final still berbasis CTA saja; jika kemudian diberikan, ukuran width only. |
| Official Hypit code/logo/screens | NOT PROVIDED | Screenshot dalam source video saja | Jangan ekstrak sebagai final B-roll tanpa memastikan hak. Bangun diagram/metafora orisinal. |
| `10_HYPIT_STARTER_GUIDE.md` | PROVIDED / authored from official repo/docs | Actual link and quickstart resource supporting CTA | Team may share it manually. No DM automation exists here. |
| `production/transcript_machine.json` | NOT YET CREATED | — | Claude Code menjalankan ASR setelah receiving new ElevenLabs voice. |
| `production/transcript_review.md` | NOT YET CREATED | — | Claude Code reviews narration and audio alignment. |
| `production/word_timing.json` | NOT YET CREATED | — | Claude Code after aligning ElevenLabs audio. |

Tidak ada logo atau brand CTA tambahan yang diotorisasi. Tidak ada lisensi BGM/SFX yang diberikan.
