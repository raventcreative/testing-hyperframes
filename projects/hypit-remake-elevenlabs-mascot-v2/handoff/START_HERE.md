# HYPIT — Remake Reels + ElevenLabs VO + Maskot (V3 READY WITH VO)

Paket ini berisi **kode starter, MP3 ElevenLabs final yang Freddie sudah kirim, naskah VO, tiga tampak maskot AI PRENEUR asli, arahan motion, storyboard, serta SATU prompt siap tempel ke Claude Code**. Ini **bukan MP4 final**; animasi dan render akan dibuat oleh Claude Code.

## Yang Freddie lakukan di Windows

1. Extract ZIP ke folder baru (jangan edit langsung dari ZIP).
2. **MP3 ElevenLabs sudah termasuk**, yaitu `assets/vo_elevenlabs_final.mp3`. Tidak perlu ekspor atau upload ke Claude Code secara terpisah.
3. Buka Claude Code dalam folder hasil extract, lalu tempel **SELURUH** isi `01_CLAUDE_CODE_EXECUTION_PROMPT.txt` sebagai satu pesan.
4. Claude Code memvalidasi VO berdurasi sekitar **61,074 detik**, mencocokkan kata-kata audionya dengan naskah dan menyusun word timing nyata, lalu membangun animasi HyperFrames dan gerak maskot.
5. Claude Code menyiapkan **preview penuh** dan QA terlebih dulu. Tonton dan beri approval; **render final baru setelah approval**.

**Tidak perlu memprogram dari nol.** Claude Code menggunakan kode contoh, semua aset referensi, locked storyboard dan satu instruksi eksekusi sebagai panduan. Perintah selalu disesuaikan dengan HyperFrames yang sudah terpasang.

## Aset maskot: batas yang perlu diketahui

`mascot/mascot_three_view_source.png` adalah **PNG satu lembar**, tampak depan/samping/belakang. Bisa dipotong sebagai sprite dan diberi animasi posisi, whole-body lean/tilt, variasi sudut, shadow dan 2.5D di HyperFrames. **Belum punya rig 3D** untuk gerak lengan/kepala/jari/mulut independen. Kalau Freddie nanti punya **GLB/FBX rigged** atau PNG berlayer, kirim ke Claude Code untuk kualitas motion karakter yang lebih hidup. Jangan sampai Claude mengarang deformasi karakter dari satu gambar.

## Isi ZIP

| File/folder | Fungsi |
|---|---|
| `01_CLAUDE_CODE_EXECUTION_PROMPT.txt` | **SATU prompt master V2** siap copy-paste ke Claude Code |
| `assets/vo_elevenlabs_final.mp3` | **VO ElevenLabs yang sudah diberikan Freddie**, ~61,074 detik, audio utama final |
| `07_VO_ELEVENLABS_READY.txt` | Naskah resmi untuk pengecekan pengucapan/alignment |
| `08_VO_RECORDING_GUIDE.md` | Informasi audio terlampir dan panduan re-record opsional |
| `09_MASCOT_MOTION_GUIDE.md` | Animasi maskot dari PNG dan opsi upgrade ke rig |
| `10_HYPIT_STARTER_GUIDE.md` | Link repo + langkah mulai yang bisa diberikan ke komentar `HYPIT` |
| `02_LOCKED_CREATIVE_BRIEF.md` | Brief utama, spec, user style locks |
| `03_STORYBOARD_PROVISIONAL.md` | **19 adegan VO baru**, waktu harus disinkronkan ke MP3 yang sudah terlampir |
| `04_DESIGN.md` | Poppins, background asli, navy gradient, highlight shape |
| `05_ASSET_MANIFEST.md`, `06_QA_ACCEPTANCE.md` | Status aset dan checklist review |
| `assets/`, `mascot/`, `reference/` | Gambar user, maskot, video referensi / source-only audio |
| `code_starter/` | HTML/CSS/GSAP HyperFrames demo, **bukan video jadi** |
| `production/` | Dokumen yang dibuat Claude Code dari audio final saat bekerja |

## Batas editorial

- Hanya memakai **VO baru**. `assets/voice_source_full.m4a` hanya referensi dari video lama; **dilarang mencampurkannya dengan suara ElevenLabs**.
- Footage asli dan iklan pihak ketiga dalam reference bukan aset final. Gunakan metafora/objek buatan sendiri dan pertahankan hak penggunaan aset.
- Tidak ada logo AI PRENEUR terpisah dalam paket; **jangan buat logo palsu**. Tulisan AI PRENEUR pada polo maskot memang ada di foto sumber.
- CTA suara menjanjikan link repo dan panduan; keduanya benar-benar terdapat di `10_HYPIT_STARTER_GUIDE.md`, tetapi **pengiriman DM belum diotomatisasi**.
- Jumlah stars repo dinamis. Naskah hanya mengatakan “puluhan ribu stars”; tidak memaksakan angka atau usia repo lama.

Status: **Paket dan VO ElevenLabs sudah tersedia.** Pemeriksaan verbatim audio, word alignment, video build, preview, QA runtime dan render final dilakukan selanjutnya di Claude Code.
