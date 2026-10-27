# A — LOCKED CREATIVE BRIEF V2

**Video:** Hypit GitHub / editable video workflow, brand AI PRENEUR. Target kreator, marketer dan pebisnis Indonesia. Inti manfaat: referensi video dipelajari dan struktur produksinya dapat disusun ulang agar bisa diedit, digunakan ulang untuk varian konten. Jangan menjanjikan viralitas atau menyalin footage orang tanpa izin.

**Goal:** storytelling dan visual motion elegan, premium, punya retensi lebih tinggi daripada sumber. Tampilkan cerita lewat satu objek diorama detail setiap frasa dan perubahan fisik saat kata penting diucapkan; copy layar ringkas, bukan text slideshow.

**Hook:** “Sekarang lo bisa bedah format video viral, sampai efek per katanya.” Buktikan secara visual dengan scanner reel yang membongkar potongan film/effect keyframes.

**Story arc:** `Bedah format → Hypit & GitHub stars → coding agent → workflow editable → contoh video jualan beberapa varian → hak aset → pasang skill & biaya pihak ketiga → CTA komentar HYPIT.`

**VO:** `07_VO_ELEVENLABS_READY.txt` = naskah yang dikunci; `assets/vo_elevenlabs_final.mp3` = suara ElevenLabs ASLI dari Freddie, sudah terlampir, terverifikasi file MP3 61.07425 detik, mono 44.1 kHz. Claude Code perlu review isi audio dan word alignment, serta mengikuti jeda dan ujung kata sebenarnya. Jangan mengutip durasi video sumber, jangan gunakan `voice_source_full.m4a` sebagai audio timeline. Bahasa santai `lo`, profesional/natural.

**Spec:** Reels 9:16, 1080x1920, 30fps, H.264/AAC final; source code HyperFrames dengan GSAP seek-safe. Caption kecil atas dari kata-kata VO terverifikasi. SFX kecil optional, **NO BGM**.

**Art/user locks:**

- Background wajib user-supplied `assets/background_asli.png` 1080x1350, proporsional cover/extension menjadi 1080x1920 (tidak stretch).
- Warna shape/highlight/objek: gradient `#121532` → `#274976`. Background tidak boleh diubah menjadi blok gelap full-screen.
- Font **Poppins Regular 400 + Bold 700/800**. Semua kata putih berada di dalam **kotak navy gradient berpadding** yang dirujuk dari `assets/kotak_highlight_asli.png`.
- Satu hero objek dimensional besar per scene, 20–60 mikrodetail penting, tiga plane, key light kiri atas, contact shadow, sedikit push/parallax, puncak gerak pada kata VO; 70–80% hard/match-cuts antarfrasa.
- Maskot PROVIDED `mascot/mascot_three_view_source.png`: preserve chibi style, wajah/rambut/outfit/tulisan polo. File ini png tiga tampak, **belum rig**; cameo animasi whole-body 2.5D hanya pada scene terpilih. Jangan terlihat seperti sticker menari terus atau mendominasi objek utama. Instruksi detail ada di `09_MASCOT_MOTION_GUIDE.md`.
- Tidak ada logo AIpreneur lain yang diberikan. Last frame CTA `Komen HYPIT` dan maskot boleh; tanpa logo rekaan.

**CTA:** “Mau link repo dan panduan instalnya? Komen HYPIT. Nanti gue bagiin.” Link dan panduan ada pada `10_HYPIT_STARTER_GUIDE.md`; tim harus menyiapkan pengiriman manual/automation sendiri, jangan berpura-pura DM sudah terkirim.

**Asset rights:** source MP4 mencakup sponsor pihak ketiga di akhir. Jangan copy footage/iklan, audio, logo, nomor ponsel, atau klaim Arrazy. Gunakan visual asset buatan baru, contoh UI hanya schematic dan bukan screenshot palsu dari produk.

**House-style hierarchy:** User-specific navy/bg/Poppins/mascot > craft/apex/scene model REF-H > motif tambahan. Poppins dan gradient user wajib meskipun beda default REF-H.

**QA & approval:** align benar dari audio baru, lint/check/snapshot, determinisme, preview penuh → tanya Freddie approval → render final → ffprobe/verifikasi. Jangan mengklaim render selesai hanya karena ZIP ada.
