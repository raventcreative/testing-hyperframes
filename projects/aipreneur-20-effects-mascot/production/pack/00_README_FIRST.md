# AI PRENEUR — 20 EFFECTS / 3D MASCOT REMAKE

Paket creative direction dan prompt produksi untuk Claude Code + HyperFrames. **Ini bukan video MP4 jadi.** Video dibuat di project Claude Code yang sudah mempunyai karakter/maskot 3D.

## Isi paket

1. `01_VOICE_OVER.md` — naskah Bahasa Indonesia siap direkam.
2. `02_REFERENCE_BREAKDOWN.md` — bedah video sumber per efek, 20 efek, dan batas ketepatan waktunya.
3. `03_PREMIUM_STORYBOARD.md` — 26 adegan original, aksi maskot, motion, dan sambungan transisi.
4. `04_CLAUDE_CODE_EXECUTION_PROMPT.md` — **file utama untuk di-copy-paste ke Claude Code**.
5. `05_EDIT_GIVEAWAY_GUIDE.md` — ringkasan 20 efek dan prompt dasar yang memang bisa dibagikan saat audiens komentar `EDIT`.
6. `assets/reference_20_effects.mp4` — video asli, untuk dianalisis Claude Code **sebagai referensi saja**, bukan untuk dipasang dalam hasil final.
7. `assets/background_navy.png` — background navy gradasi yang diberikan pengguna.
8. `assets/aipreneur_logo_original.png` — logo asli ber-alpha transparan, tetapi memiliki margin transparan yang besar.
9. `assets/reference_contact_sheet.png` — overview frame video sumber.

## Cara pakai

1. Ekstrak ZIP ke **folder project Claude Code yang sudah berisi maskot 3D**. Jangan menimpa pekerjaan lama tanpa mengecek konflik nama file. Paket ini hanya menambah satu folder baru.
2. Buka project Claude Code, lalu paste seluruh isi `04_CLAUDE_CODE_EXECUTION_PROMPT.md` ke Claude Code. Beri tahu Claude Code lokasi folder paket jika perlu.
3. Pastikan Claude Code dapat menemukan maskot asli (`.glb`, `.gltf`, `.vrm`, `.fbx`, atau asset/rangka lain), tekstur, dan rig-nya. Jika model lebih dari satu, **pilih secara eksplisit** yang benar.
4. Rekam voice-over dari `01_VOICE_OVER.md` memakai suara yang diinginkan. Simpan audio di project Claude Code, misalnya `assets/vo/freddie_vo.wav`; berikan path yang nyata. **Sebelum audio tersedia, timing storyboard masih estimasi.**
5. Jalankan fase inspeksi aset → storyboard → prototype → visual review → assembled preview. Setelah kamu setuju preview, lakukan render final.

## Prioritas kreatif (wajib)

**Instruksi khusus remake ini mengalahkan style V3 lama apabila bertentangan.**

- Background: navy asli yang dilampirkan, bukan ivory.
- Font: Poppins Regular dan Poppins Bold saja.
- Warna teks: putih `#FFFFFF`; kata-kata penting `#00D0FE`.
- Subjek: **maskot 3D dari project Claude Code**, bukan orang pada video sumber.
- Logo: AI PRENEUR di **kiri atas**, putih, dengan sheen/glint biru lembut sesekali; jangan berpendar terus-menerus.
- Tetap ambil dari V3: kualitas 3D, kedalaman tiga layer, light direction, contact shadow, gerakan bermakna, QA, dan timing deterministik.
- Output: Reels/TikTok 1080 × 1920, 30 fps, H.264 MP4 + AAC.
- Audio: voice-over; tanpa BGM. SFX halus boleh digunakan bila sumbernya jelas/berizin.

## Catatan file logo

PNG logo **sudah transparan** (pemeriksaan pixel corner: alpha 0). Preview yang terlihat hitam bukan berarti raster hitam opaque. Huruf putih berada di tengah kanvas transparan 1485 × 1485. Di Claude Code cukup buat **salinan kerja yang di-trim berdasarkan alpha** untuk membuang margin kosong, tanpa mengubah huruf atau anti-alias. Jangan melakukan penghapusan background baru atau merancang ulang logo.

## Catatan background

Background yang dikirim lebih pendek daripada kanvas 9:16. Skalakan secara proporsional, lalu **mirror-extend** bagian atas/bawah atau crop secara terkontrol tanpa meregangkan gambar. Jangan distorsi gradasi aslinya.

## Batasan penting

- Analisis video asli didasarkan pada frame dan teks visual. Ini **bukan transkrip kata-per-kata audio asli**.
- Nama 20 efek berasal dari daftar yang tampak di referensi. Naskah dalam paket ini adalah **adaptasi original**.
- Lip-sync dan gerak sendi hanya boleh dijanjikan jika model 3D benar-benar memiliki rig/morph target yang diperlukan. Bila tidak, gunakan kamera, pose, dan interaksi properti yang benar-benar bisa dihasilkan, serta laporkan keterbatasannya.
- Menampilkan mockup UI untuk menjelaskan alur bukan bukti bahwa aplikasi tersebut sudah dikembangkan; jangan memperlakukannya sebagai rekaman produk nyata.
- Resource komentar `EDIT` bisa berupa isi paket ini; sebelum kampanye diunggah, pastikan proses DM/otomatisasi pengirimannya disiapkan sendiri.
