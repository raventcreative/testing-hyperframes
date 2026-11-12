# VO — Tim 3 Claude cari kerja remote · background TERANG · 43,5 dtk VO (video 44,83 dtk)
Referensi: ref4 (44 dtk) — "tim info loker isinya 3 Claude": Claude 1 keliling situs loker, Claude 2 nyaring (cocok skill, bisa dari
Indonesia, "bukan penipuan"), Claude 3 bikin CV + cover letter per lowongan, hasilnya satu halaman "papan info loker", CTA "komen
REMOTE nanti aku kirim link-nya". Visual referensi: ruangan 3D gelap dengan karakter kotak-kotak.

## Yang diubah dari referensi
- Visual sepenuhnya milik kita: sistem LIGHT AI PRENEUR (grid animasi, kartu putih, maskot + robot), bukan ruangan 3D/karakter
  referensi. Tiga "anggota tim" = kartu Claude (Pencari · Penyaring · Penulis CV) + TEAM RAIL yang dipakai terus di s03–s06.
- Perintahnya punya nama sendiri: `/loker-remote` (bukan "/remote-job-hunter").
- Klaim dibuat lebih aman: "bukan penipuan" (seolah dijamin) → "yang mencurigakan dibuang" + kriteria konkret di layar ("tanpa biaya
  di depan", "tanpa syarat warga negara"). Tidak ada "pasti dapat kerja", tidak ada angka hasil (jumlah lowongan, tingkat balasan).
- Ada langkah manusia: "Aku tinggal **cek**, pilih yang paling cocok, terus klik apply" — tombol Apply membuka halaman lamaran
  aslinya (toast "Buka halaman lamaran aslinya ↗"), Claude tidak melamar otomatis.
- Semua lowongan, perusahaan, skor kecocokan dan isi CV adalah **contoh** dan diberi label CONTOH / DATA CONTOH di layar.
  Situs loker hanya ditulis sebagai nama teks (tanpa logo).
- CTA: "Komen REMOTE, aku kirim lewat DM." (setup-nya: `production/SETUP_TIM_3_CLAUDE.md`).

## Fakta yang dicek (2026-11-12)
- Claude Code mendukung **subagent**: asisten khusus dengan system prompt, akses tool dan context window sendiri; didefinisikan
  sebagai file Markdown di `.claude/agents/`; bisa dijalankan berurutan (hasil satu diteruskan ke berikutnya).
  Sumber: https://code.claude.com/docs/en/sub-agents
- **Satu perintah**: perintah slash kustom dari `.claude/commands/<nama>.md` atau skill `.claude/skills/<nama>/SKILL.md` → `/<nama>`.
  Sumber: https://code.claude.com/docs/en/slash-commands
- Nama situs di layar (teks saja): Remote OK, We Work Remotely, Remotive, Himalayas, Jobicy, Working Nomads (situs loker remote;
  beberapa punya feed/API publik, syarat pemakaian beda-beda), plus LinkedIn, Upwork, Glints (situs kerja umum, adegan "capek").
  Sumber: pencarian web 2026-11-12 (artikel dev.to "four remote job boards have free public APIs" + daftar agregator) — situs resminya
  tidak bisa dibuka dari sandbox (DNS diblok), jadi VO tidak menyebut nama situs atau fitur API apa pun; nama hanya muncul sebagai teks.

## Naskah (dikirim ke ElevenLabs, voice tersimpan; SETIAP baris diawali tag `[playful] [excited]`)
[playful] [excited] Aku bikin tim isi tiga Claude, yang tugasnya nyariin aku kerja remote.
[playful] [excited] Soalnya nyari kerja remote itu capek banget. Buka puluhan situs loker satu-satu, apply berkali-kali, yang bales dikit banget.
[playful] [excited] Sekarang aku cukup ketik satu perintah, dan timnya langsung kerja.
[playful] [excited] Claude pertama keliling ke banyak situs loker, ngumpulin lowongan remote yang ada.
[playful] [excited] Claude kedua nyaring: mana yang cocok sama skill aku, bisa dikerjain dari Indonesia, dan yang mencurigakan dibuang.
[playful] [excited] Yang lolos dilempar ke Claude ketiga. Dia bikinin CV dan cover letter khusus buat tiap lowongan.
[playful] [excited] Terus semuanya masuk ke satu halaman, kayak papan loker pribadi.
[playful] [excited] Aku tinggal cek, pilih yang paling cocok, terus klik apply.
[playful] [excited] Mau cobain? Komen REMOTE, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt`. Audio: `assets/audio/vo.mp3` (+ `assets/audio/vo.json` = waktu per baris + alignment
karakter). Dibuat dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3
--tags "[playful] [excited]"`. Cek ulang dengan faster-whisper `small`: semua kata terucap, tag tidak ikut terbaca.
