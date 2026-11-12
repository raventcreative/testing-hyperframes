# VO — R14 · Claude Code edit reels: 3 prompt aja · background TERANG (LIGHT) · VO 49,5 dtk (reel 50,83 dtk)

Referensi: `aip_remake_batch5/refs/ref4.mp4` + `ref4.txt` (≈50 dtk, bahasa Indonesia, kreator lain, merek hitam/merah + maskot rambut
merah). Pembeda dari reel kita sendiri **R5** (`aip_r5_editvideo`, "Edit video pakai Claude, 4 langkah", NAVY): R5 = tutorial 4 langkah
(download app → 4 tool gratis → style sheet → storyboard/revisi/final) dengan rail 4 langkah, kartu 2×2 yang dibalik, film strip,
panel "Bedah gaya", storyboard dan kartu reel jadi. **R14 = "3 prompt"**: tiap langkah adalah satu prompt yang ditampilkan utuh sebagai
kartu yang bisa disalin (teks prompt asli + tombol Salin), lalu didemokan dengan metafora visual sendiri. Tidak ada rail langkah,
tidak ada storyboard, tidak ada kartu flip, LIGHT bukan NAVY, naskah tanpa kalimat yang sama (cek n-gram: hanya ekor CTA wajib).

## ATM — Amati (apa isi referensinya)
- **Ide berguna:** Claude Code bisa ngedit reels: satu folder kerja + lima alat (Remotion, HyperFrames, FFmpeg, Whisper, yt-dlp) yang
  dipasangkan Claude; kasih 3–5 video favorit → "brand sheet" (terinspirasi, bukan nyontek); taruh rekaman mentah + prompt ketiga →
  bagian kosong terpotong, caption masuk; revisi tinggal bilang.
- **Mekanisme hook:** klaim kemampuan ("Claude Code bisa ngedit reels buat kamu") + biaya rendah ("modalnya cuma 1 folder dan 5 tools").
- **Struktur beat:** folder (mentah/referensi/hasil) → daftar 5 tool dengan penghitung 0/5…5/5 → "nggak perlu install sendiri, tempel
  1 prompt" → selera/brand sheet + stempel "bukan nyontek" → rekaman + prompt 3 → waveform terpotong, caption → revisi → penutup reflektif
  ("bukan soal jago edit, tapi tahu selera") → CTA komen kata kunci + follow.
- **Mekanisme CTA:** komen kata kunci → prompt dikirim lewat DM (+ ajakan follow akun mereka).
- Transkripnya berisi nama yang rusak ("Clot-clot", "FF Impact", "UTB LP") → dicek ulang: Claude Code, FFmpeg, yt-dlp.

## ATM — Tiru (yang kita ambil)
Hanya mekanisme umumnya: alur tiga prompt (siapin alat → bikin selera → edit) dan CTA "komen kata kunci → dikirim lewat DM".

## ATM: what we changed (Modifikasi)
1. **Hook sendiri, sudut beda:** "Simpan dulu: tiga prompt buat ngedit reels pakai Claude Code." — ajakan simpan + prompt-nya sendiri
   sebagai aset yang bisa disalin (referensi: klaim kemampuan + "modal murah"). Frame 0 = judul "[3] prompt" + tumpukan kartu + tombol
   simpan (bookmark) yang ditekan di kata "Simpan".
2. **Struktur & visual sendiri:** tiap prompt muncul sebagai KARTU PROMPT besar berisi teks prompt asli (5 baris, bisa dijeda dan
   disalin) → kursor klik **Salin** → kartu melipat jadi strip "PROMPT n" di atas, lalu demo dengan metafora sendiri:
   - Prompt 1: folder kerja `studio-reels/` sebagai hub, lima alat jadi node di sekelilingnya (konektor tergambar, centang hijau, label
     lisensi tiap alat), catatan "Izin dulu" dan "*Lisensi Remotion" — bukan daftar + penghitung 0/5 seperti referensi, bukan kartu flip R5.
   - Prompt 2: 4 thumbnail reels generik (desain kita) + pemindai, bingkai putus-putus "pola" di tiap thumbnail, konsol `selera.md`
     dengan kenop (Tempo · Caption · Warna · Pembuka, nilai = CONTOH) — bukan brand sheet + stempel "BUKAN NYONTEK", bukan "Bedah gaya" R5.
   - Prompt 3: baris transkrip (Whisper) dengan gunting di jeda + take ulang, baris menutup, batang durasi mentah vs hasil, pratinjau 9:16
     dengan caption + stiker, revisi lewat suara di chat Claude Code ("caption-nya naikin dikit" → caption naik, EDIT v2) — bukan waveform
     + ponsel "HOOK" referensi, bukan storyboard R5.
   - Beat baru: "Prompt satu dan dua cukup sekali, video berikutnya tinggal prompt tiga" (stempel SEKALI AJA, file video baru masuk ke
     kartu 3 "tiap video baru"). CTA: tuts keyboard P-R-O-M-P-T + paket "3 prompt lengkap" terbang ke DM — bukan kotak komentar + Follow.
   - Gaya rumah AI PRENEUR LIGHT (grid animasi, kartu putih, gradasi navy, Poppins), maskot + robot kita sendiri; tidak ada warna
     merah/hitam, maskot, kartu, ikon, atau layout referensi.
3. **Sudut praktisi (benar):** "Ini alur yang aku pakai sendiri." + stempel "Alur kerjaku" (Freddie memang ngedit dengan alur ini;
   reel ini sendiri dibuat dengan HyperFrames). Tidak ada hasil/angka pribadi yang diklaim.
4. **Nilai untuk penonton Indonesia yang tidak ada di referensi:**
   - peringatan hak cipta: "Ambil polanya, bukan isinya, dan **jangan upload ulang video orang**" (yt-dlp buat belajar);
   - **lisensi Remotion** di layar (gratis buat individu & usaha sampai 3 karyawan, selebihnya Company License) — referensi tidak menyebut;
   - **Claude minta izin** sebelum menjalankan perintah (dan prompt 1 menyuruh Claude menjelaskan tiap perintah dulu);
   - langkah yang dilewati referensi: **prompt 1 & 2 cukup sekali, video berikutnya tinggal prompt 3**;
   - cara Claude "menonton" video yang jujur: dipecah jadi frame + transkrip (di teks prompt 2);
   - DM berisi versi lengkap + catatan jujur (Claude Code butuh paket Claude berbayar, Whisper bisa salah dengar nama) →
     `production/TIGA_PROMPT.md`.
5. **CTA & penutup sendiri:** kata kunci **PROMPT** — "Mau teks lengkapnya? Komen PROMPT, aku kirim lewat DM." Tanpa ajakan follow,
   tanpa penutup reflektif referensi. Tidak ada >3 kata berurutan yang sama dengan naskah referensi (dicek otomatis: satu-satunya 3-gram
   yang sama adalah "kirim lewat DM" dari baris CTA wajib; 4-gram: nol).

## Fakta yang dicek (sumber resmi, 12 Nov 2026)
| Klaim di reel / DM | Sumber | Isi yang dicek |
|---|---|---|
| Claude Code: baca/edit file, jalankan perintah; ada di terminal, IDE, aplikasi desktop, web | code.claude.com/docs/en/overview | "agentic coding tool that reads your codebase, edits files, runs commands… Available in your terminal, IDE, desktop app, and browser." Desktop: "A paid subscription is required"; kebanyakan surface butuh langganan Claude / akun Console (→ hanya di DM, reel tidak menyebut gratis) |
| Claude minta izin sebelum jalanin perintah; kerja di folder yang dipilih | code.claude.com/docs/en/desktop | mode default **Manual**: "Claude asks before editing files or running commands"; "Project folder: … choose the folder Claude works in" |
| **Remotion** = bikin video/animasi dengan kode (React); lisensi khusus | github.com/remotion-dev/remotion (README + LICENSE.md) | "Make videos programmatically with React"; Free License untuk individu, "for-profit organization with up to 3 employees", nirlaba, evaluasi; selain itu **Company License** (remotion.dev sendiri tidak bisa dibuka dari sesi ini → LICENSE.md di GitHub) |
| **HyperFrames** = motion graphic dari HTML, open source | github.com/heygen-com/hyperframes | "Write HTML. Render video. Built for agents." HTML/CSS/animasi → MP4, **Apache 2.0**, butuh Node.js 22+ & FFmpeg; plugin/skill Claude Code (`claude plugin marketplace add heygen-com/hyperframes`, `npx skills add heygen-com/hyperframes`) |
| **FFmpeg** = potong/gabung/convert | github.com/FFmpeg/FFmpeg (README) | "a collection of libraries and tools to process multimedia content"; `ffmpeg` = "command line toolbox to manipulate, convert and stream multimedia content"; **LGPL** dengan komponen opsional **GPL** |
| **Whisper** = suara jadi teks (caption), bahasa Indonesia | github.com/openai/whisper (README, whisper/transcribe.py, tokenizer.py) | "general-purpose speech recognition model"; kode & bobot **MIT**; `pip install -U openai-whisper`; CLI `--output_format` txt/vtt/srt/tsv/json, `--word_timestamps`; bahasa "id" (indonesian) ada |
| **yt-dlp** = download video referensi | github.com/yt-dlp/yt-dlp | "A feature-rich command-line audio/video downloader"; **Unlicense** (binary rilis membundel kode GPLv3+); install via binary rilis / pip / package manager |
| "Claude bikin folder, terus pasang lima alat" | docs Claude Code di atas + README tiap alat | instalasi = perintah terminal yang dijalankan Claude di folder lokal dengan izin kamu (npm/npx, pip, package manager) |
Tidak dipakai/tidak diklaim: kata "gratis" untuk Claude atau untuk kelima alat sekaligus (Remotion tidak gratis untuk perusahaan besar);
angka, durasi hasil, atau janji "pasti". Nilai di layar (tempo "cepat", "besar, di tengah", timestamp transkrip, nama file) = CONTOH.

## Naskah (dikirim ke ElevenLabs; tag = AUTO klien, TANPA --tags)
Setiap baris otomatis diawali `[playful] [excited]` + satu tag konteks bila cocok (dari `assets/audio/vo.json`):
```
[playful] [excited] Simpan dulu: tiga prompt buat ngedit reels pakai Claude Code.
[playful] [excited] Ini alur yang aku pakai sendiri.
[playful] [excited] Prompt satu: siapin alat. Claude bikin folder, terus pasang lima alat.
[playful] [excited] YT-DLP ambil video contoh, Whisper ubah suara jadi teks, FFmpeg motong, HyperFrames sama Remotion bikin animasi.
[playful] [excited] Prompt dua: bikin selera. Kasih reels favoritmu, Claude catat polanya: tempo, caption, warna, pembuka.
[playful] [excited] Ambil polanya, bukan isinya, dan jangan upload ulang video orang.
[playful] [excited] Prompt tiga: edit. Masukin video mentahmu, Claude buang jeda, pasang caption, sesuai selera tadi.
[playful] [excited] Kurang pas? Tinggal bilang, kayak ke editor: caption-nya naikin dikit.
[playful] [excited] Prompt satu dan dua cukup sekali. Video berikutnya, tinggal prompt tiga.
[playful] [excited] [curious] Mau teks lengkapnya?
[playful] [excited] [confident] Komen prompt, aku kirim lewat DM.
```
Baris terakhir dikirim dengan "prompt" huruf kecil supaya dibaca sebagai kata (bukan dieja P-R-O-M-P-T); di caption dan layar tampil
**"Komen PROMPT, aku kirim lewat DM."**. 111 kata, VO 49,52 dtk (dalam batas 35–50 dtk).

VO: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (voice Dakocan
plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, tags auto) → `assets/audio/vo.mp3` + `assets/audio/vo.json`.
Cek pelafalan dengan faster-whisper `small` (id): semua kata terbaca (Claude Code, YT-DLP, Whisper, FFmpeg, HyperFrames, Remotion,
caption, DM); tag tidak ikut terbaca. Waktu kata: `tools/align_words.py` (alignment karakter ElevenLabs) → `tools/timing.py`, dengan
koreksi TFIX untuk kata pertama setelah tag ("Prompt" baris 5/7/9, "Mau") dan "alat." di akhir baris 3 (dicek terhadap envelope energi).
