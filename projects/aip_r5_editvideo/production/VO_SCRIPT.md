# VO — Edit video pakai Claude, step by step (R5) · background NAVY · 53,8 dtk VO (55,2 dtk reel)
Referensi: `aip_remake_batch3/refs/ref5.mp4` (81 dtk, EN, "All the top creators are editing with Claude…"; oranye, serif italic,
screenshot GitHub, kartu "Style breakdown" + "Storyboard"). Remake: idenya sama (4 langkah: folder → tool → style sheet → storyboard/
revisi/final), tapi naskah, sudut pandang dan visual kita sendiri:
- Hook praktisi, bukan klaim "semua kreator top": **"Reel ini aku edit bareng Claude."** (benar: reel ini sendiri adalah komposisi
  HyperFrames yang disusun bareng Claude). Freddie memang ngedit pakai HyperFrames → "ini yang aku pakai".
- Langkah 3 diberi detail yang jujur soal cara kerjanya: Claude tidak "nonton" video; dia memecah reel jadi frame (lewat FFmpeg,
  ditulis di layar "via FFmpeg") lalu membedah gayanya.
- yt-dlp dibingkai untuk mempelajari referensi (di kartu: "unduh reel buat dipelajari"), bukan re-upload.
- Tidak ada klaim "works like a charm every time", tidak ada angka palsu, Claude sendiri TIDAK disebut gratis (yang gratis = 4 tool
  open source). Nilai di UI (2:14, 1080×1920, isi style sheet) = contoh tampilan.
- Lebih ringkas dari referensi (81 → 55 dtk). CTA beda: **"Komen EDIT"**.

## Fakta yang dicek (sumber resmi, 12 Nov 2026)
| Klaim di reel | Sumber | Isi yang dicek |
|---|---|---|
| Claude desktop app (macOS · Windows) | claude.com/download · support.claude.com/en/articles/10065433-install-claude-desktop | download resmi untuk macOS & Windows (Linux beta); login akun Claude. Paket/harga tidak disebut di reel. |
| Buka folder di Claude, Claude bisa jalankan perintah (install tool) | code.claude.com/docs/en/desktop | tab Code: environment Local + pilih project folder, Claude kerja langsung di folder itu; perintah terminal jalan sesuai mode izin (default: minta izin dulu) |
| HyperFrames = motion graphic dari HTML, gratis/open source | github.com/heygen-com/hyperframes | "Write HTML. Render video. Built for agents." HTML/CSS/GSAP → MP4, lisensi Apache-2.0, butuh Node.js 22+ & FFmpeg; skill untuk Claude Code (`claude plugin marketplace add heygen-com/hyperframes` / `npx skills add heygen-com/hyperframes`) |
| FFmpeg = potong & convert video, open source | github.com/FFmpeg/FFmpeg (README) | "a collection of libraries and tools to process multimedia content", LGPL dengan komponen opsional GPL (ffmpeg.org tidak bisa diakses dari sesi ini) |
| Whisper = suara jadi caption, open source | github.com/openai/whisper (+ whisper/transcribe.py, whisper/tokenizer.py) | "general-purpose speech recognition model", kode & bobot MIT; CLI `--output_format` txt/vtt/srt/tsv/json, `--word_timestamps`; bahasa Indonesia ("id") ada |
| yt-dlp = unduh video referensi, open source | github.com/yt-dlp/yt-dlp | "A feature-rich command-line audio/video downloader", Unlicense (binary rilis membundel kode GPLv3+) |
| "Tempel link GitHub-nya, Claude yang pasang" | code.claude.com/docs/en/desktop + README tiap repo | instalasi = perintah terminal yang dijalankan Claude di folder lokal (dengan izin kamu); link yang ditampilkan = repo resmi di atas |

## Naskah (dikirim ke ElevenLabs, tiap baris diawali tag `[playful] [excited]`)
Reel ini aku edit bareng Claude. Ini setup-nya, step by step.
Satu: download Claude desktop. Bikin folder AI Video Editor, isinya tiga: raw footage, referensi, export. Terus buka folder itu di Claude.
Dua: pasang empat tool gratis. HyperFrames buat motion graphic, ini yang aku pakai. FFmpeg buat motong video, Whisper buat caption, YT-DLP buat ambil video referensi. Tempel link GitHub-nya, Claude yang pasang.
Tiga, ini kuncinya: kasih tiga sampai lima reel yang kamu suka. Claude pecah jadi frame, lalu bedah gayanya: font, warna, caption, transisi, sampai sound. Hasilnya satu style sheet.
Empat: masukin raw footage, kirim prompt. Claude bikin storyboard dulu, baru videonya. Kurang pas? Bilang aja, font-nya gedein. Kalau udah oke, render jadi video final.
Mau prompt lengkapnya? Komen EDIT, aku kirim lewat DM.

VO: `python3 tools/el_tts_ts.py production/vo_lines.txt production/vo_take1/vo.mp3 --tags "[playful] [excited]"` (voice
plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75) → `assets/audio/vo.mp3` (53,92 dtk). Cek pelafalan dengan
faster-whisper small: semua istilah terbaca (HyperFrames, FFmpeg, Whisper, YT-DLP, GitHub, storyboard, style sheet).
Kata & waktu: `tools/align_words.py` (dari alignment karakter ElevenLabs) → `production/vo_words_raw.json` → `tools/timing.py`.
