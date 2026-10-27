# AIpreneur — SIX WORLDS / ONE MASCOT

**Paket arahan produksi untuk Claude Code. Bukan hasil render MP4.**

## Isi paket

1. `01_CREATIVE_BRIEF_AND_STYLE.md` — visual identity dan keputusan creative director.
2. `02_SOURCE_VIDEO_BREAKDOWN.md` — audit video asli dengan perkiraan timecode.
3. `03_FINAL_VOICEOVER.md` — naskah bahasa Indonesia siap direkam.
4. `04_SCENE_BY_SCENE_STORYBOARD.md` — adegan baru, objek, transisi, kamera, dan respons 3D.
5. `05_PASTE_IN_CLAUDE_CODE.md` — prompt eksekusi utama, lengkap dan mandiri.
6. `06_EFFECT_RECIPES.md` — resep teknis enam efek dan batasan realisme.
7. `07_QUALITY_CHECKLIST.md` — persyaratan preview, sinkron VO, dan render.
8. `08_COMMENT_CLAUDE_RESOURCE.md` — materi yang benar-benar bisa dikirim ke penonton yang komentar CLAUDE.
9. `assets/` — MP4 referensi utama, tiga referensi gerak pendamping, background asli, logo asli, lembar cuplikan.

## Cara kerja

1. Ekstrak ZIP ini ke satu folder baru di project Claude Code. **Jangan menimpa project atau asset maskot lama.**
2. Pastikan Claude Code bisa membaca file di paket dan menemukan model maskot 3D yang **sudah ada** di project. Jangan mengarang path asset.
3. Buka `05_PASTE_IN_CLAUDE_CODE.md`, salin isinya ke Claude Code, dan minta Claude membaca semua file paket.
4. Rekam `03_FINAL_VOICEOVER.md`; taruh audio final sebagai `assets/voiceover_final.mp3` atau `.wav` di folder produksi.
5. Claude harus membuat animatic/preview dan memeriksanya, kemudian menunggu persetujuan sebelum render delivery final.

## Asset & kejujuran produksi

- Source video: 22,94 detik, 720×1280, sekitar 29,97 fps; **hanya acuan ide visual, nama efek dan tempo**, bukan footage untuk disisipkan ke remake.
- Tiga reference library tambahan: `ref_A_editorial_kinetic.mp4` untuk layering, `ref_B_cinematic_dimensional.mp4` untuk material dan camera depth, `ref_C_clean_character_3d.mp4` untuk staging karakter. **Ambil prinsip gerak saja, tidak palet, desain, footage atau identitas sumber.**
- Background user: 1080×1350. Buat versi 1080×1920 secara proporsional dengan memperpanjang gradient/tepi, **jangan stretch**.
- Logo user: PNG transparan, tulisan gelap dengan margin transparan sangat besar. Trim **hanya alpha transparan** ketika menempatkannya di kiri atas, jangan recolor bentuk aslinya.
- File model GLB/GLTF/FBX maskot **tidak disertakan**. Asset itu menurut user sudah tersedia di Claude Code.
- Audio VO final **belum disertakan**. Durasi storyboard adalah provisional; sinkron tepat dilakukan setelah file VO tersedia.

## Creative rule yang mengalahkan rule lama

Paket ini secara eksplisit memakai background pale-blue/white milik user, text gradient `#0A0D2C → #294B77`, teks putih pada badge gradien navy, dan **Poppins**. Aturan lama dari referensi style yang memakai navy background / font lain tidak boleh mengganti arahan terbaru ini. Ambil standar dimensi, animasi, dan QA-nya saja.

## Bukan klaim 22 template

Video referensi **mendemonstrasikan enam** gaya. CTA aslinya menyebut 22 efek, tetapi paket ini **hanya berjanji enam prompt yang memang tersedia**. Hindari membuat janji link repo atau jumlah efek yang belum tersedia.
