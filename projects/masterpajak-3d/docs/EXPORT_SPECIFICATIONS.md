# Spesifikasi Export

## Video final (wajib, 3 file)
| Parameter | Nilai |
|---|---|
| Container / codec | MP4 / H.264 High profile, `+faststart` |
| Resolusi | **1080 × 1080 (1:1)** |
| Frame rate | **60 fps** konstan |
| Pixel format / warna | yuv420p, BT.709 (primaries, transfer, matrix), limited range |
| Kualitas | CRF 11, preset slow |
| Background | **#00FF00** murni, composite dari render ber-alpha asli |
| Audio | **Tidak ada audio stream** (di-encode dengan `-an`, diverifikasi ffprobe) |
| Durasi | 7,0 dtk / 7,0 dtk / 11,0 dtk |

## Bonus transparan
| Parameter | Nilai |
|---|---|
| File | `*_ALPHA.webm` |
| Codec | VP9, yuva420p (alpha asli), CRF 20 |
| Catatan | Isi dan timing sama persis dengan MP4. Bisa dipakai tanpa chroma key |

## Kualitas render
- Supersampling 2× (render internal 2160×2160, box filter ke 1080).
- Motion blur fisik: 2–8 sub-frame per frame dalam shutter 180°. Jumlahnya dihitung dari perpindahan piksel nyata (±1 sub-frame per 1,25 px).
- Pipeline linear HDR, tone mapping Khronos PBR Neutral (menjaga warna brand), output sRGB.
- Alpha di-un-premultiply sebelum composite, jadi tepi bersih dan blur tidak bercampur hijau di dalam objek.
- Tidak ada lantai, bayangan ke background, gradien, atau pantulan hijau. Environment lighting netral, jadi material tidak terkontaminasi hijau.
- Tidak ada elemen berwarna hijau di objek.

Hasil pengecekan aktual ada di `VERIFICATION_REPORT.md`.
