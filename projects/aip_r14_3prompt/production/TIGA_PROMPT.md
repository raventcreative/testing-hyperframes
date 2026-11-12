# 3 Prompt buat ngedit reels pakai Claude Code (versi lengkap · isi DM untuk komen PROMPT)

Ini tiga prompt yang aku pakai. Urutannya penting: **Prompt 1 dan 2 cukup sekali**, setelah itu **tiap video baru tinggal Prompt 3**.
Tinggal salin, tempel ke Claude Code, lalu sesuaikan bagian dalam [kurung siku].

## Sebelum mulai (baca dulu, 1 menit)
- **Claude Code** bisa dipakai lewat aplikasi desktop Claude (tab **Code**), terminal, atau extension VS Code. Untuk Claude Code kamu
  perlu **paket Claude berbayar** (atau akun Anthropic Console). Pilih satu folder kerja, dan biarkan Claude kerja di folder itu saja.
- Secara default Claude **minta izin dulu** sebelum ngedit file atau jalanin perintah. Baca tiap perintah sebelum kamu klik izinkan.
- Alat yang dipasang: **FFmpeg**, **Whisper** (OpenAI), **yt-dlp**, **HyperFrames** (HeyGen), **Remotion**. Empat yang pertama open
  source. **Remotion pakai lisensi khusus**: gratis buat individu, perusahaan sampai 3 karyawan, dan organisasi nirlaba; perusahaan yang
  lebih besar wajib beli Company License. HyperFrames butuh Node.js 22+ dan FFmpeg; Whisper butuh Python.
- **yt-dlp itu buat belajar**, bukan buat ambil konten orang. Simpan reels contoh di folder inspirasi, pelajari polanya, dan jangan
  pernah upload ulang video orang atau pakai potongannya di video kamu.

---

## PROMPT 1 · Siapin alat (sekali saja)

```
Kamu asisten editor video aku. Di folder ini, bikin struktur:

studio-reels/
  rekaman/    -> video mentah aku
  inspirasi/  -> reels contoh yang aku suka (cuma buat dipelajari)
  final/      -> hasil render

Terus siapin 5 alat ini dan cek semuanya jalan:
1. FFmpeg: potong, gabung, convert video dan audio.
2. Whisper (openai-whisper): suara jadi teks, timestamp per kata, bahasa Indonesia.
3. yt-dlp: download reels contoh ke folder inspirasi.
4. HyperFrames: motion graphic dari HTML (butuh Node.js 22+ dan FFmpeg).
5. Remotion: motion graphic dari React. Ingetin aku soal lisensinya
   (gratis buat individu & perusahaan sampai 3 karyawan, lebih dari itu perlu Company License).

Aturan:
- Sebelum jalanin perintah apa pun, jelasin dulu perintahnya ngapain dan kenapa perlu.
- Kalau perlu install sesuatu di level sistem (Homebrew, winget, apt, Node.js, Python), tanya aku dulu.
- Setelah selesai, tes tiap alat (misalnya cek versinya) dan kasih ringkasan:
  apa yang terpasang, versi berapa, dan apa yang gagal + cara benerinnya.
- Tulis studio-reels/CATATAN.md: cara pakai tiap alat dalam 1-2 kalimat.
```

## PROMPT 2 · Bikin selera (sekali, update kalau selera kamu berubah)

```
Di folder studio-reels/inspirasi ada [3-5] reels yang aku suka.
Pelajari GAYANYA, bukan isinya:

1. Tiap video: ambil frame (misalnya 1 frame per detik pakai FFmpeg) dan bikin transkrip pakai Whisper.
2. Catat polanya:
   - tempo potongan (seberapa sering visual ganti),
   - gaya caption (ukuran, posisi, warna, berapa kata per baris, kata yang di-highlight),
   - warna dan font,
   - 3 detik pembuka (cara mereka narik perhatian),
   - transisi, sound effect / musik, panjang video, cara nutup (CTA).
3. Tulis studio-reels/selera.md: panduan gaya yang ringkas dan bisa dipakai ulang,
   plus 3 aturan wajib dan 3 hal yang harus dihindari.

Penting: ambil polanya aja. Jangan salin teks, gambar, musik, atau ide spesifik dari video mereka,
dan jangan pakai potongan klip mereka di video aku.
```

## PROMPT 3 · Edit (tiap video baru)

```
Edit video [nama-file.mp4] di folder studio-reels/rekaman pakai aturan di selera.md:

1. Transkrip pakai Whisper (bahasa Indonesia, timestamp per kata).
2. Potong jeda kosong dan kalimat yang aku ulang (ambil take terakhir yang paling bersih).
   Jangan motong di tengah kata.
3. Caption per kata dari transkrip, gayanya ikut selera.md. Cek ejaan nama dan istilah.
4. Tambah animasi / motion graphic (HyperFrames atau Remotion) cuma di poin penting,
   jangan nutupin muka atau caption.
5. Render 1080x1920 ke folder studio-reels/final.
6. Kasih aku daftar: bagian yang dipotong (pakai timestamp), apa yang ditambah,
   dan apa yang perlu aku cek sebelum upload.

Kalau ada yang ragu, tanya dulu sebelum render.
```

### Revisi: ngomong aja kayak ke editor
Setelah lihat hasilnya, tinggal bilang apa yang kurang. Contoh:
- `caption-nya naikin dikit, jangan nutupin dagu`
- `potongan di detik 10-15 kecepetan, kasih napas dikit`
- `warna highlight caption ganti ke yang ada di selera.md`
- `tambah judul besar di 2 detik pertama`

## Catatan jujur
- Hasil pertama jarang langsung sempurna. Anggap Claude editor baru: kasih revisi yang spesifik, nanti makin pas.
- Whisper kadang salah dengar nama atau istilah. Selalu cek caption sebelum upload.
- Render butuh waktu dan tenaga komputer; video panjang lebih lama.
- Musik dan footage yang kamu pakai harus punya kamu atau yang memang boleh dipakai.

Sumber (dicek 12 Nov 2026): code.claude.com/docs/en/overview · code.claude.com/docs/en/desktop · github.com/heygen-com/hyperframes ·
github.com/remotion-dev/remotion (LICENSE.md) · github.com/FFmpeg/FFmpeg · github.com/openai/whisper · github.com/yt-dlp/yt-dlp
