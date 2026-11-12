# VO — Repo GitHub buat belajar bikin teknologi dari nol (build-your-own-x) · background NAVY · 40,40 dtk VO (video 42,00 dtk)

Referensi: `aip_remake_batch5/refs/ref7.mp4` (32,9 dtk, bahasa Inggris, latar hitam/krem, kartu putih bergaya macOS, logo asli
Git/Docker, kartu "Resume", chat "Technical interview", akun komentar si kreator; CTA "Comment BUILD"). Versi kita: bahasa Indonesia,
"aku/kamu", gaya NAVY AI PRENEUR (robot + maskot), sudut buat mahasiswa / junior dev Indonesia.

## ATM — Amati, Tiru, Modifikasi

**Amati (referensi):**
- Ide berguna: repo "build your own X" = kumpulan panduan step-by-step buat bikin ulang Git, Docker, database, dll. dari nol; proyek
  kayak gitu bikin CV beda dari to-do app dan bikin kamu bisa jelasin cara kerjanya pas interview.
- Mekanisme hook: klaim peringkat ("repo GitHub dengan bintang terbanyak sepanjang masa, bukan React, Linux atau Python") + angka
  ("over half a million developers"), divisualkan dengan grafik bintang vs React/Linux/Python dan kartu "552.5k".
- Struktur beat: peringkat → "kita pakai Git/Docker/database tiap hari tanpa tahu cara kerjanya" → "repo ini daftar panduan step-by-step"
  → to-do app di CV vs "I built my own Git" → interviewer suka gali ini → "once you've built it, you can explain it" → CTA.
- Mekanisme CTA: komen kata kunci → dikirim lewat DM.

**Tiru (yang kita ambil, hanya ide umum):** repo-nya, isi panduan step-by-step (Git, Docker, database, …), kontras "to-do app vs proyek
yang dirakit dari nol", manfaat buat interview (bisa jelasin cara kerja), CTA komen kata kunci → DM.

**Modifikasi — ATM: what we changed**
1. **Hook sendiri, sudut beda:** referensi membuka dengan klaim peringkat. Kita membuka dari rasa sakit penonton:
   "Portofolio kamu isinya to-do app lagi? Coba rakit Git versi kamu sendiri, dari nol." Visual hook: papan PORTOFOLIO KAMU yang isinya
   to-do app semua (todo-app, todo-app-2, todo-app-final, todo-app-beneran) → stiker "4× to-do app" → papan pergi, muncul KIT RAKIT
   (rangka model kit) yang bagian-bagiannya (blob, commit, tree) digunting dari rangkanya lalu dirakit jadi rantai commit → tree → blob +
   terminal "$ mygit commit". Peringkat repo baru muncul di beat 2, sebagai fakta yang sudah dicek (bukan hook), dengan tanggal.
2. **Struktur + metafora visual sendiri:** RAKIT (kit model) → README + papan peringkat bintang (3 baris dari pencarian GitHub, bukan
   grafik bintang vs React/Linux/Python) → penghitung "360 tutorial · 30 kategori" + 5 node STEP BY STEP + 4 kartu blueprint (jumlah
   tutorial + bahasa per kategori, dihitung dari README) → tumpukan "CV PELAMAR LAIN" (6 dari 6 isinya todo-app) vs kartu "CV KAMU"
   (contoh) dengan proyek mygit → panel cutaway "CARA PAKAI" (git commit) yang tutupnya terbuka jadi "CARA KERJA" (commit → tree → blob +
   hash) → halaman tutorial EN + panel Claude "mode tutor" → permintaan "kode jadi" dicoret + terminal Claude Code `/output-style learning`
   + editor dengan `# TODO(human)` → CTA komen RAKIT + DM. Tidak ada layout, warna, ikon/logo (Git/Docker), kartu "Resume", chat
   "Technical interview", atau toast "You got the job!" dari referensi; semua kartu kita sendiri, ikon Lucide (ISC), gaya NAVY.
3. **Sudut praktisi Freddie:** tidak dipakai — tidak ada bukti Freddie membangun proyek dari repo ini, jadi tidak ada "aku pakai ini buat…"
   dan tidak ada hasil pribadi. Suara tetap "aku/kamu".
4. **Nilai buat penonton Indonesia yang tidak ada di referensi:** (a) catatan bahwa tutorialnya bahasa Inggris → **jadiin Claude tutor**
   yang menjelaskan tiap langkah dalam bahasa Indonesia; (b) cara jujur pakai AI saat belajar: **jangan minta kode jadi** (copy-paste),
   minta petunjuk; (c) langkah konkret yang sudah dicek: gaya **Learning** di Claude Code (`/output-style learning`) — Claude
   meninggalkan beberapa baris (`TODO(human)`) buat kamu tulis sendiri; (d) contoh pertanyaan interview kita sendiri ("Apa yang terjadi
   di balik git commit?") dengan jawaban yang benar secara teknis (objek commit/tree/blob, nama = hash isi) — bukan pertanyaan referensi;
   (e) tidak ada janji "dapat kerja" (referensi menampilkan "You got the job!"); kita cuma bilang CV jadi beda dan kamu bisa menjelaskan.
5. **CTA + penutup sendiri:** "Komen RAKIT, aku kirim lewat DM." (kata kunci RAKIT, bukan BUILD; DM berisi link repo + prompt tutor).
- Cek kata (otomatis, n-gram vs transkrip referensi): satu-satunya 4 kata berurutan yang sama adalah nama repo "Build Your Own X";
  3 kata yang sama hanya istilah/nama: "to-do app", "step by step" (frasa README sendiri), "build your own". Selain itu nol.

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
Catatan akses: API GitHub dan HTML github.com lewat curl diblok proxy sesi ini; halaman repo + pencarian GitHub dibaca lewat WebFetch,
isi README lewat raw.githubusercontent.com. git-scm.com dan codecrafters.io tidak bisa diakses dari sesi ini (di luar allowlist).

| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| Repo **codecrafters-io/build-your-own-x** ("Build Your Own X"), gratis | Halaman repo: deskripsi "Master programming by recreating your favorite technologies from scratch." README: "This repository is a compilation of well-written, step-by-step guides for re-creating our favorite technologies from scratch." | github.com/codecrafters-io/build-your-own-x (WebFetch); README.md (raw.githubusercontent.com) |
| Lisensi **CC0** ("CC0 · bebas dipakai" di layar) | README "Origins & License": badge CC0 1.0; "CodeCrafters, Inc. has waived all copyright and related or neighboring rights to this work." Dimulai oleh Daniel Stefanovic, sekarang dikelola CodeCrafters, Inc. | README.md; halaman repo |
| **562 rb bintang**; "repo dengan bintang terbanyak di GitHub saat ini" (+ "dicek 12 Nov 2026" di layar) | Halaman repo: "562.0k" stars (forks 52.6k). Pencarian GitHub `stars:>300000` diurutkan bintang terbanyak: #1 codecrafters-io/build-your-own-x 562k, #2 sindresorhus/awesome 536k, #3 public-apis/public-apis 498k (lalu freeCodeCamp 459k, …); pencarian `stars:>540000` → 1 hasil saja (build-your-own-x). | github.com/search?q=stars:>300000&s=stars&o=desc dan ?q=stars:>540000 (WebFetch, 12 Nov 2026) |
| Papan peringkat: awesome 536 rb, public-apis 498 rb | sama, hasil pencarian GitHub di atas (dibulatkan ke ribuan, "rb") | idem |
| "ratusan tutorial step by step" · layar "360 tutorial · 30 kategori" | README: 360 entri tutorial (baris "* [**Bahasa**: …"), daftar isi 30 kategori (29 + Uncategorized; ada juga judul "Distributed Systems" berisi 1 tutorial). Dihitung dari README.md 12 Nov 2026. | README.md |
| Git, Docker, database, sistem operasi + jumlah & bahasa di kartu | Git 7 (Python 3, JavaScript 2, Ruby 1, Haskell 1) · Docker 6 (Python 2, Go 2, C 1, Shell 1) · Database 14 (Go 3, Rust 2, Python 2, C, C++, C#, …) · Operating System 19 (C 12, Rust 2, C++ 2, Assembly 2, 1 "any") | README.md (dihitung) |
| Kategori lain di ticker (3D Renderer … Web Server) | daftar isi README | README.md |
| Halaman tutorial di layar: "Build your own Git · Bab 3 · Objects" + kalimat Inggris | **CONTOH** buatan kita (diberi label "CONTOH"), bukan kutipan dari tutorial tertentu; isi kalimatnya sesuai glossary Git (objek dinamai hash isinya). | — |
| CARA KERJA: commit → tree → blob, nama objek = hash isinya, isi berubah → nama berubah | git glossary: object "uniquely identified by the SHA-1 of its contents. Consequently, an object cannot be changed"; commit object berisi parents, committer, author, date + tree; tree = daftar nama file + ref ke blob/tree; blob = isi file. Dicek juga langsung dengan `git cat-file -p HEAD` (tree/parent/author) dan `git cat-file -p HEAD^{tree}` (blob) di repo ini. Hash pendek di layar (a1f3c9e, 7b2e04d, e41c16a) = ilustrasi. | github.com/git/git `Documentation/glossary-content.adoc` (raw.githubusercontent.com); git 2.43 lokal |
| Kode di editor: `header = f"blob {len(data)}\0".encode()` + `return sha1(header + data).hexdigest()` | Cara Git menghitung id blob (header "blob <ukuran>\0" + isi, SHA-1) — konsisten dengan glossary (SHA-1 of its contents); file "objects.py" = contoh kita. | glossary-content.adoc; pengetahuan umum Git |
| **Gaya Learning di Claude Code**, `/output-style learning`, Claude ninggalin beberapa baris buat kamu tulis (`TODO(human)`) | "Learning — Claude explains its choices and leaves small pieces of code for you to write yourself"; "it leaves a few lines for you. Claude marks the spot with a TODO(human) comment"; "● Learn by Doing"; "run /output-style <style> to switch… The /output-style command ignores case." | code.claude.com/docs/en/output-styles (WebFetch, 12 Nov 2026) |
| Layar terminal "✓ Output style: Learning" dan kartu "Learn by Doing · tugas kamu: isi TODO(human)" | mock generik buatan kita (bukan screenshot); teks "Learn by Doing" + TODO(human) dari dokumen di atas | idem |

Yang dibuang/diperbaiki dari referensi: "most starred repository of all time" → kita cuma bilang "bintang terbanyak di GitHub **saat
ini**" (terverifikasi lewat pencarian GitHub, tanggal di layar) dan tidak dijadikan hook; "isn't React, Linux or even Python" dibuang
(perbandingan tidak relevan; Linux/Python bukan pesaing di peringkat bintang); "552.5k" → angka hari ini 562 rb; "over half a million
developers have starred it" → tidak dibacakan (bintang ≠ developer); "You got the job!" dibuang (janji kerja); pertanyaan interview
referensi diganti pertanyaan kita sendiri; CTA "BUILD" → "RAKIT"; tidak ada nama/akun kreator referensi.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = AUTO tags klien)
Tag yang dipakai (dari `production/vo_el.json`): semua baris `[playful] [excited]`, baris 8 + `[confident]` (CTA). Tidak ada tag
konteks lain yang terpicu.
1. `[playful] [excited]` Portofolio kamu isinya to-do app lagi? Coba rakit Git versi kamu sendiri, dari nol.
2. `[playful] [excited]` Panduannya gratis di Build Your Own X, repo dengan bintang terbanyak di GitHub saat ini.
3. `[playful] [excited]` Isinya ratusan tutorial step by step: bikin Git, Docker, database, sampai sistem operasi.
4. `[playful] [excited]` To-do app udah pasaran. Git rakitan sendiri? Itu baru bikin CV kamu beda.
5. `[playful] [excited]` Pas interview, kamu bisa jelasin cara kerjanya dari dalam, bukan cuma cara pakainya.
6. `[playful] [excited]` Tutorialnya bahasa Inggris? Jadiin Claude tutor: minta dia jelasin tiap langkah pakai bahasa Indonesia.
7. `[playful] [excited]` Jangan minta kode jadi. Pakai gaya Learning di Claude Code: beberapa baris, kamu yang tulis sendiri.
8. `[playful] [excited] [confident]` Komen RAKIT, aku kirim lewat DM.

104 kata, VO 40,40 dtk (rentang 35–50 dtk). Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4,
stability .41, similarity .75, tags "auto"), dibuat dengan
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan) →
`assets/audio/vo.mp3`.

Take 1 memakai baris 7 "… sebagian kodenya kamu yang tulis."; faster-whisper small mendengar "kodenya" sebagai "kodonya" dua kali
(juga pada potongan klip), jadi baris 7 ditulis ulang tanpa kata itu ("beberapa baris, kamu yang tulis sendiri." — juga lebih dekat ke
dokumen: "leaves a few lines for you") dan seluruh VO dibuat ulang (take 2 = final).
Cek pelafalan take 2 (faster-whisper small, id): semua baris terbaca. Salah dengar whisper yang biasa: "to-do" → "Tuduh", "GitHub" →
"Git Hap", "Claude" → "kual"/"Cloud", "Jadiin" → "Jadikan", "pakainya" → "pakenya". "Build Your Own X" terdengar "build your own X"
(dicek juga pada klip terpisah, id: "di build your own ex").
