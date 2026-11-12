# VO — R19 · Asisten suara open source di Mac (Atticus) · background NAVY · 43,5 dtk VO (video 44,93 dtk)

Referensi: `aip_remake_batch5/refs/ref9.mp4` (27 dtk, bahasa Inggris, akun lain; hitam/abu-abu terang, emblem "J.A.R.V.I.S",
screenshot macOS ungu). Di transkripnya namanya terdengar "Atticus"; dari frame videonya terbaca jelas halaman GitHub
**SaarthurR / atticus-mac** ("Atticus for Mac") dan perintah `github.com/SaarthurR/atticus-mac` yang ditempel ke Claude Code.
Repo itu dicek langsung (clone + halaman GitHub, 12 Nov 2026): aplikasinya **Atticus**, asisten suara open source untuk Mac.

## ATM: what we changed (Amati · Tiru · Modifikasi)
**Amati (referensi):** hook perbandingan dengan AI fiksi terkenal ("This free tool just replaced Jarvis and it runs right on your
computer") + emblem J.A.R.V.I.S; struktur: nama + penghitung bintang GitHub ("350 → 407 stars in 19 days", "#5 on GitHub trending")
→ salin link → tempel ke Claude Code, "set this up on my machine" → terminal dengan progres (Cloning, Building Atticus.app, Granting
mic + accessibility) → "hold a shortcut" (keycap ⌃ ⌥ Space di bawah laptop) → 4 demo di screenshot macOS ("Put Chrome next to
Spotify", "Find my Q3 report", "What's on my screen?", "Open Sarah's email" → "Reply to this") → CTA "Comment Jarvis and I'll send you
the repo and my full setup guide" (kartu komentar + DM).
**Tiru (hanya ide + mekanisme):** asisten suara open source di Mac yang dipasang lewat Claude Code; mekanisme "tunjukkan apa yang bisa
dia kerjakan lewat beberapa perintah suara, lalu cara pasangnya".
**Modifikasi (wajib, semuanya dikerjakan):**
1. **Hook sendiri, sudut beda:** bukan "menggantikan Jarvis", tapi mekanismenya sendiri yang dibuat penasaran: "Tahan tiga tombol,
   ngomong, lepas. Mac kamu yang beresin sisanya." Visual: tiga keycap besar (control · option · space = shortcut default asli
   Atticus) yang ditekan, voice pill, lalu desktop berantakan yang merapikan dirinya. Headline "3 tombol, 1 kalimat." Tanpa kata/gambar
   "Jarvis" atau Marvel di layar maupun di suara.
2. **Struktur + metafora sendiri:** nama + spesifikasi jujur (repo resmi, MIT, khusus macOS 26+, versi Windows = proyek komunitas
   terpisah) → 3 contoh pemakaian Indonesia (jendela WhatsApp ke kiri, file penawaran ketemu dari isinya, balasan email klien yang
   cuma jadi draf) → cara pasang → biaya (metafora steker + 2 colokan) → izin akses (mata + sakelar izin macOS) → data (garis batas
   "MAC KAMU": yang tinggal vs yang terkirim) → CTA. Referensi memasang dulu baru demo; kita demo dulu, pasang belakangan, plus tiga
   beat kejujuran (biaya, izin, data) yang tidak ada di referensi. Semua visual milik kita (gaya NAVY AI PRENEUR): keycap, jendela
   mock buatan sendiri, voice pill, sinar pemindai file + lencana COCOK, sudut fokus "BACA LAYAR" + tombol Kirim terkunci, pil link →
   kartu "Claude Code" (teks saja, tanpa logo) → rel 4 langkah installer, steker & colokan, sakelar izin, paket yang menyeberangi garis.
   Tanpa screenshot produk, tanpa halaman GitHub, tanpa penghitung bintang, tanpa wallpaper ungu, tanpa palet hitam/abu-abu, tanpa
   huruf serif miring, tanpa logo pihak ketiga (WhatsApp, Claude, Anthropic, Ollama, LM Studio ditulis teks saja).
3. **Sudut praktisi:** TIDAK ada klaim "aku pakai ini" — tidak terverifikasi bahwa Freddie memakai Atticus, jadi tidak dikarang.
   Suara tetap praktis: contoh nyata, syarat, dan apa yang perlu dicek sebelum memasang.
4. **Nilai tambah untuk penonton Indonesia (yang tidak ada di referensi):** contoh lokal (WhatsApp, "file penawaran klien" dengan nama
   file acak, email "Bu Rina · Katering Sehat" — semua berlabel CONTOH); syarat yang jujur (macOS 26 ke atas, langganan Claude Pro/Max
   atau model lokal; pengguna Windows: hanya versi komunitas terpisah); KOREKSI "gratis" (aplikasinya gratis, otaknya tidak);
   kehati-hatian privasi: dia bisa lihat layarmu, izin yang kamu kasih (Mikrofon, Pengenalan ucapan, Aksesibilitas, Rekam layar; +
   opsional Kalender/Otomasi untuk agen), suara diolah di Mac tapi permintaan + tangkapan layar dikirim ke penyedia model (kecuali
   model lokal); "draf tidak dikirim otomatis"; cara resmi pasang (perintah `curl … install.sh | bash` dari README) ditampilkan.
5. **CTA + penutup sendiri:** "Komen ASISTEN, aku kirim lewat DM." + kartu "Atticus · repo resmi · link + cara setting yang aman"
   (referensi: "Comment Jarvis… repo and my full setup guide").
**Cek kata:** referensi berbahasa Inggris, naskah kita bahasa Indonesia — tidak ada lebih dari 3 kata berurutan yang sama (dicek
otomatis setelah normalisasi; yang sama hanya nama diri "Claude Code"). Mekanisme "tahan shortcut, ngomong" adalah cara kerja asli
produk (README: "Hold ⌃ control ⌥ option space, say what you need, let go") — kita pakai sebagai hook dengan sudut dan visual sendiri.

## Klaim referensi yang DIBUANG / DIKOREKSI
- "just replaced Jarvis" — perbandingan dengan tokoh/produk fiksi berhak cipta, tidak bisa diverifikasi → dibuang; tidak ada "Jarvis"
  di layar maupun di suara (caption menampilkan kata yang diucapkan, jadi kata itu juga tidak diucapkan).
- "popular … on GitHub", "350 / 407 stars in 19 days", "#5 on GitHub trending" → tidak dipakai. Angka bintang berubah-ubah (halaman
  GitHub 12 Nov 2026: 736 bintang, 76 fork) dan peringkat trending tidak bisa dicek → tanpa angka.
- "it installs everything for you" → dikoreksi: README tidak menyebut cara "tempel ke Claude Code"; cara resminya satu perintah
  `curl -fsSL https://raw.githubusercontent.com/SaarthurR/atticus-mac/main/install.sh | bash`. Claude Code memang bisa menjalankan
  perintah di Mac-mu (docs Claude Code), jadi "minta dia yang pasangin" benar, dan di layar perintah resminya ikut ditampilkan.
  Syarat tetap berlaku: macOS 26+, Xcode command line tools, klien AI; jendela setup lalu meminta izin macOS satu per satu.
- "This free tool" → dikoreksi: aplikasinya gratis + MIT, tapi "otaknya" pakai langganan Claude Pro/Max (atau Devin / Pi / model
  lokal lewat server lokal). Di VO: "Aplikasinya gratis, otaknya langganan Claude Pro atau Max, atau model lokal."
- "runs right on your computer" → dikoreksi: aplikasinya jalan di Mac dan suara diubah jadi teks di Mac (audio tidak keluar), tetapi
  permintaanmu dan tangkapan layar (kalau dia perlu melihat layar) dikirim ke penyedia model klien AI-mu; tetap di Mac hanya kalau
  pakai model lokal.
- "say reply to this" → dipertegas: dia menulis DRAF balasan; "It never sends." Kita tunjukkan tombol Kirim terkunci + "tidak dikirim
  otomatis".
- Contoh referensi (Chrome + Spotify, "Q3 report", "Sarah's email") → diganti contoh Indonesia milik kita.

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
Repo: **github.com/SaarthurR/atticus-mac** (di-clone ke scratch untuk dibaca; commit terbaru 46edb57, 10 Nov 2026, "Atticus 1.6.0";
file VERSION = 1.6.0; commit oleh Saarth Ranka).
| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| Namanya Atticus, asisten suara untuk Mac | About: "Fast, free voice assistant for your Mac. No API key. Remembers you and learns your shortcuts. Hold ⌃⌥Space and talk." | halaman GitHub repo (12 Nov 2026) |
| Open source, lisensi MIT | LICENSE: "MIT License · Copyright (c) 2026 SaarthurR"; README: "Free and open source", "License: MIT" (+ `LICENSE-Plip` MIT untuk kode yang diadaptasi) | README, LICENSE |
| Gratis (aplikasinya) | "Atticus is free; tips keep it going." | README |
| Tahan 3 tombol (Control + Option + Space), ngomong, lepas | "Hold ⌃ control ⌥ option space, say what you need, let go." (bisa diganti "Press to toggle" di Settings) | README |
| Khusus Mac, macOS 26 ke atas | "Needs macOS 26 and an AI client"; "macOS 26 or later (Atticus uses Apple's new on-device speech)"; `install.sh`: "Atticus needs macOS 26 or later." | README, install.sh |
| Windows: versi komunitas, proyek terpisah | "On Windows? @FindlayHi built Atticus for Windows (github.com/FindlayHi/atticus-windows)" — repo itu ada (git ls-remote), bukan buatan pemilik Atticus | README |
| Buka aplikasi + geser jendela, tanpa AI ("buka WhatsApp, taruh di kiri") | "Instant commands. Opens apps, moves windows, plays music and searches the web with no AI at all."; "*Open Spotify* · *Terminal on the left* → Runs instantly, with no AI at all." | README |
| Cari file dari isinya, bukan cuma nama | "*Find my notes about the Tokyo trip* → Searches your files by what's inside them, opens the match…" | README ("Just ask") |
| Baca layar | "Sees your screen. Ask about anything on screen." | README |
| Balas email: draf jadi, tidak dikirim sendiri; tombol "Sisipkan" | "*Reply to this. Thursday works, send me a time.* → Reads the email on screen and writes the reply. Insert puts it at your cursor. It never sends." | README |
| Pasang: tempel link ke Claude Code, minta dia pasangin | Claude Code "reads your codebase, edits files, runs commands…" → bisa menjalankan installer resmi; installer resmi: `curl -fsSL …/atticus-mac/main/install.sh \| bash` | code.claude.com/docs/en/overview; README "Quick install" |
| Rel 4 langkah installer: cek Mac (macOS 26+) · unduh ke ~/.atticus · build Atticus.app · buka setup (izin satu-satu) | `install.sh`: cek `sw_vers` ≥ 26 + `xcode-select`, `git clone … "$HOME/.atticus"`, `build.sh`, `open ~/Applications/Atticus.app`; README: "The first launch opens a setup window. It checks your AI plan, then asks for each macOS permission." | install.sh, README |
| Otaknya: langganan Claude Pro atau Max, tanpa API key | "An AI client: a paid Claude plan (Pro or Max) and Claude Code, the Devin CLI…, Pi…, or a custom server through Claude Code with no Claude account."; "Your plan, no API key." | README (Install, What it does) |
| Atau model lokal (Ollama, LM Studio) | "Atticus can send Claude Code to a local server that implements the Anthropic Messages API… Ollama 0.14.0+ · LM Studio 0.4.1+ · llama.cpp · vLLM"; "you do not need a Claude account" | README ("Use a local model") |
| Izin: Mikrofon, Pengenalan ucapan, Aksesibilitas, Rekam layar (+ opsional Kalender, Otomasi untuk agen) | Setup window: Microphone "Listens when you start a voice request." · Speech Recognition "Turns your words into text, on this Mac." · Accessibility "Moves windows and clicks buttons for you." · Screen Recording "Looks at your screen when you say 'this'."; wajib = AI provider + Microphone + Speech Recognition + Accessibility; agen: Accessibility, Screen Recording, Automation, Calendar; README: "Accessibility permission enables native clicks, scrolling, menus, keys, dragging and field typing." | `ui/onboarding.html`, README |
| Dia bisa lihat layarmu | Screen Recording permission + "Look at my screen: Automatic / Never" ("The picture goes with that one ask."); `atticus.py --look` = "labeled screenshots of every display" | `ui/settings.html`, `atticus.py` |
| Suaramu diolah di Mac | "Apple's on-device speech turns your voice into text, and audio never leaves your Mac." (Whisper opsional juga lokal: "audio still never leaves it") | README ("Safe by default", "Dictate anywhere") |
| Permintaan + tangkapan layar dikirim ke penyedia model | Permintaan dijalankan lewat klien AI pilihanmu (Claude Code → Claude/Anthropic; Devin; Pi; atau server lokal). `atticus.py` membaca teks jendela depan dan mengambil screenshot (`screencapture`) kalau teksnya kurang, lalu menyerahkannya ke model; file screenshot dihapus setelahnya ("no screenshot left in /tmp"); setting "The picture goes with that one ask." | `atticus.py` (baris ±7960–7975), `ui/settings.html`, README (Model choice) |
| (catatan, tidak di VO) Telemetri anonim | "Atticus sends a random ID … It never sends task text, dictated words, file contents, paths, or screen content. Turn it off in Settings → Account & Access → Count me as a user." | README ("Anonymous usage") |
Contoh di layar (WhatsApp ke kiri, nama file, "Penawaran Harga · CV Contoh Jaya", email Bu Rina, isi draf, "rapikan jendelaku, dong")
adalah ilustrasi dan diberi label CONTOH/mock; jendela, kartu "Claude Code" dan sakelar izin adalah mock buatan kita, bukan screenshot
produk. Label sakelar diterjemahkan dari teks asli jendela setup Atticus.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = tag AUTO klien)
Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan,
43,60 dtk) → `assets/audio/vo.mp3`. Tag yang benar-benar dipakai (dari `production/vo_el.json`):
1. `[playful] [excited]` Tahan tiga tombol, ngomong, lepas. Mac kamu yang beresin sisanya.
2. `[playful] [excited]` Namanya Atticus, asisten suara open source khusus Mac.
3. `[playful] [excited]` Bilang: buka WhatsApp, taruh di kiri. Jendelanya langsung pindah.
4. `[playful] [excited]` Cari file penawaran klien? Dia nyari dari isi filenya, bukan cuma nama.
5. `[playful] [excited]` Buka email, bilang: balas, Kamis aku bisa. Drafnya jadi, tapi nggak dikirim sendiri.
6. `[playful] [excited]` Pasangnya: tempel link repo ke Claude Code, minta dia yang pasangin.
7. `[playful] [excited]` Aplikasinya gratis, otaknya langganan Claude Pro atau Max, atau model lokal.
8. `[playful] [excited]` Tapi ingat, dia bisa lihat layarmu. Kamu kasih izin mikrofon, aksesibilitas, rekam layar.
9. `[playful] [excited]` Suaramu diolah di Mac, tapi permintaan dan tangkapan layar dikirim ke penyedia model.
10. `[playful] [excited] [confident]` Komen ASISTEN, aku kirim lewat DM.

Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, auto tags).
Cek dengar dengan faster-whisper small (bahasa id): semua baris terbaca sesuai naskah; whisper menulis "Claude" → "cloud"
(ejaan whisper yang biasa), "beresin" → "berisin", "Max" → "Macs", "ingat" → "inget", "balas" → "bales" — pelafalan normal dan jelas.
