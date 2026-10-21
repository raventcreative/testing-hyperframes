# ASSET MANIFEST — KONTEN AI PRENEUR

Semua path di bawah ini RELATIF terhadap root hasil ekstraksi `konten ai preneur/`.

| Relative path | Peran | Status | Batasan / fallback |
|---|---|---|---|
| `assets/background/background_user_original.png` | Asset asli latar belakang 980×1225 RGB | provided + verified | Jangan ubah identitas gradasi, warna dasar, atau memperkenalkan efek/neon besar. |
| `assets/background/background_portrait_1080x1920.png` | Background native portrait hasil center-crop + resize kualitas tinggi | derived + verified | Dipakai sebagai layer full-frame. Jika versi crop kurang sesuai framing, kembali ke original dan lakukan proper cover crop, bukan stretch. |
| `assets/logo/ai_preneur_logo_original.png` | Logo/wide wordmark di dalam square transparan 1485×1485 RGBA | provided + verified | Jangan mengubah glif, proporsi, warna atau tulisan. |
| `assets/logo/ai_preneur_wordmark_trimmed.png` | Ekstraksi crop transparan untuk layout wordmark | derived + verified | Hanya menghapus padding transparan, tidak mengubah logo. |
| `assets/voice/VOICE KE 1.mp3` … `VOICE KE 11.mp3` | Original VO scene 1–11 (sequential, no missing indices) | provided + verified | User-provided; jangan regenerasi, retime, pitch shift, truncate atau reorder. |
| `assets/voice/VOICE_MASTER_48s.m4a` | Master voice timeline pada 48.000s, 48kHz mono AAC | derived + verified | Gunakan sekali sebagai track utama. 11 source MP3 untuk verification only; jangan diputar dua kali. |
| `reference/reference_motion_original.mp4` | Referensi kualitas motion dari user, 52.607s 720×1280 | provided + verified | Hanya untuk analisis/inspirasi; JANGAN masukkan ke output final, copy frame, ambil audio, atau upload/publish. |

## Konten tambahan yang TIDAK diperlukan

Tidak perlu foto talent, stock footage, musik, screenshot website, video lain, ikon merek, statistik hasil usaha, atau URL aplikasi. Presentasi diwujudkan dengan typography, abstract UI, dan graphics original dalam HTML/CSS/JS. Jika ingin menyisipkan studi kasus real dan logo merek lain di kemudian hari, minta aset asli dengan izin penggunaan.

## Larangan sumber media

No speculative internet downloads, no fake branded dashboards, no fabricated prices/performance numbers. Any SFX must be licensed/permission-verified locally. If nothing suitable exists, omit SFX and preserve VO only. No paid operations, cloud publication, or external upload.
