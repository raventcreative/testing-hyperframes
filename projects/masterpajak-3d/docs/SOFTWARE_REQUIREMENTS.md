# Software Requirements

| Komponen | Versi yang dipakai | Fungsi |
|---|---|---|
| Node.js | 22.x | Menjalankan driver render |
| three (npm) | 0.180.0 | Engine 3D (WebGL2): geometri, material PBR, bayangan, area light |
| Playwright + Chromium | Chromium 1243 (headless) | Menjalankan scene dan membaca piksel tiap frame secara deterministik |
| FFmpeg | 6.1 (libx264, libvpx-vp9) | Compositing di atas #00FF00, encode H.264 / VP9-alpha / ProRes |
| Python 3 + Pillow | 3.13 / Pillow 11+ | Contact sheet, grafik kecepatan, verifikasi |
| Font | Rubik (OFL), JetBrains Mono (OFL) | Ada di `assets/fonts`, dimuat lewat FontFace (tidak bergantung pada font sistem) |

Tidak perlu GPU. Render memakai WebGL lewat SwiftShader (CPU).

## Pipeline
```
src/docs/*.js        Canvas2D → artwork dokumen resolusi tinggi (2,4–2,8 px per unit layout)
src/lib/PaperSheet   mesh kertas: tebal nyata, tepi bevel, sudut bulat, zigzag, lipatan inextensible
src/shots/v*.js      koreografi (objek / kamera / efek terpisah), fungsi murni dari waktu
src/lib/stage.js     render linear HDR + alpha → N sub-frame (motion blur) → SSAA 2× → tone map PBR Neutral → sRGB
render/render.mjs    Chromium headless → RGBA mentah → FFmpeg (overlay di #00FF00, H.264 BT.709, -an) + VP9 alpha
```

## Kenapa bukan Blender
Blender (`bpy`) sebenarnya tersedia, tapi mesin render hanya punya 4 core CPU tanpa GPU. Cycles butuh perkiraan 5+ jam untuk ~1.500 frame, jadi siklus QC berulang tidak realistis. Pipeline Three.js di atas tetap memakai geometri 3D asli, material PBR, area light, bayangan, motion blur fisik, dan supersampling, dengan iterasi yang jauh lebih cepat.
