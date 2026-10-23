# F — QA / DELIVERY ACCEPTANCE

## Gate sebelum build

- [ ] Verifikasi file gambar dan video dengan file metadata/ffprobe.
- [ ] Periksa CLI HyperFrames yang **terpasang** (semua flag `--help` lokal).
- [x] MP3 ElevenLabs Freddie disertakan di `assets/vo_elevenlabs_final.mp3`; file diprobe 61.07425s, mono 44.1kHz. Claude Code wajib mengecek ulang di mesin Windows untuk sinkronisasi.
- [ ] Buat transkrip lokal Bahasa Indonesia + word timing dari **VO ElevenLabs baru**; koreksi `Hypit`, `Claude Code`, `HYPIT`, dan CTA terhadap file TXT terkunci.
- [ ] **Audio source full .m4a** tidak ada di hasil V2, tidak ada footage/sponsor source dalam hasil final.
- [ ] 19-scene V2 map dipotong ulang berdasarkan jeda narasi nyata, bukan timecode 46 detik lama. Caption menggunakan **verbatim VO baru**.

## Visual identity gate

- [ ] `assets/background_asli.png` terlihat sepanjang video; tidak stretch/distort.
- [ ] `#121532` ke `#274976` dipakai sebagai gradient visual utama untuk panel/objek/highlight, **bukan** background fullscreen.
- [ ] Poppins Regular + Bold terlihat konsisten.
- [ ] Semua kata putih berada dalam kotak navy gradient yang punya padding.
- [ ] Tidak ada headline besar berulang; visual mendominasi, caption 1–2 baris kecil di atas.
- [ ] Hero object setiap scene besar, detail 20–60 elemen di scene penting, material/light/grounding masuk akal.
- [ ] Setidaknya 3 depth cues terlihat untuk scene dimensional.
- [ ] Frame 0 tidak kosong, frame terakhir tenang dan tidak hitam.
- [ ] Tidak ada image/visual third-party sponsor yang ikut tanpa izin.
- [ ] Maskot sumber 3-view dipakai dengan cutout bersih dan face/hair/outfit/teks polo terjaga; tidak ada label FRONT/SIDE/BACK atau background putih sheet.
- [ ] Maskot muncul secara selektif, tidak menutupi hero/caption/CTA, animasi whole-body sprite/2.5D; **tidak mengarang sendi, animasi mulut, atau 3D rig** dari PNG tunggal.

## Motion/audio gate

- [ ] Scene cut mengikuti frase VO dan pitch/intensitas, 1 kausal action per frase.
- [ ] Key action/apex sinkron ke kata kunci ±50ms berdasarkan timestamp alignment.
- [ ] Frame screenshot pada entrance, apex, mid-tween, end setiap scene; perbaiki flat/small/empty hero.
- [ ] VO ElevenLabs baru diletakkan **tepat satu kali**, tidak dipercepat/dipitch; audible sampai “Nanti gue bagiin.”
- [ ] No BGM. SFX jika ada legal, halus, mix di bawah VO.
- [ ] Tidak ada output palsu, preview perlu ditonton seutuhnya.

## Programmatic gate

- [ ] `npx hyperframes lint`: 0 errors.
- [ ] `npx hyperframes check`/`validate`/`inspect` tergantung CLI lokal: 0 critical errors; tandai overlap yang memang disengaja.
- [ ] Determinisme: screenshot timestamp yang sama setelah seek dua urutan berbeda, beda 0 pixel.
- [ ] Snapshot contact sheet per scene vs `reference/ref_H_overview.jpg` hanya untuk kualitas craft/depth (bukan warna/font).
- [ ] `ffprobe` preview jika preview berupa video; dimensi/audio/frame rate benar.
- [ ] **STOP untuk approval preview user**, jangan auto-render final.
- [ ] Setelah approval, render `--quality` sesuai help lokal.
- [ ] Verifikasi MP4 final: 1080×1920, 30fps, H.264 + AAC, durasi/frame count, audio tail, tidak ada black frame, screenshot scene midpoint dan final still.
- [ ] Laporkan yang benar-benar terverifikasi saja: PASS, PASS WITH WARNINGS, atau BLOCKED.
- [ ] Pastikan `10_HYPIT_STARTER_GUIDE.md` link/panduan tersedia sebagai resource CTA, tetapi jangan mengklaim DM automation berjalan.
