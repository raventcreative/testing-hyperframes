# VO — Agent AI di server klien: checklist AMAN · background TERANG · 45,0 dtk VO (video 46,57 dtk)
Referensi: batch 6 · ref2 (178 dtk, reel bahasa Indonesia, kreator lain; latar krem + aksen merah + karakter piksel): "Kamu kasih AI agent
akses ke server kamu… tapi diam-diam dia juga membaca file password, mengubah pengaturan lain, dan menjalankan perintah yang tidak pernah kamu
minta. Terus kamu tahu dari mana?" → sapaan + nama kreator + ucapan terima kasih ke pendukung → "3 lapis pengaman": (1) catat semua aktivitas
— akun khusus agent, auditd, git + git diff, log Hermes, log milik admin; (2) batasi akses — least privilege; (3) sandbox + persetujuan
manusia — Hermes approvals mode manual & jangan YOLO, OpenCode permission ask/deny → "pembatas harus teknis, bukan instruksi" → tanya pendapat
di komentar + traktir kopi + follow. Visual referensi: kartu putih di latar krem, gedung isometrik biru, kubus kaca sandbox, terminal gelap
dengan tabel WAKTU/AKUN/PERINTAH, diff merah/hijau di terminal gelap, kartu toggle merah, kartu config YAML/JSON gelap, kartu kopi.

## ATM: what we changed
**Amati** — ide yang berguna: kalau agent AI dikasih akses ke server, pasang pengaman teknis (akun terpisah, pencatat perintah, snapshot +
diff, log yang tak bisa dihapus agent, pengaturan izin di Hermes/OpenCode). Mekanisme hook: skenario menakutkan ("diam-diam…") + pertanyaan
"kamu tahu dari mana?". Struktur: hook → janji pengaturan di akhir → perkenalan → 3 lapis bernomor → penutup filosofis → ajakan komentar/donasi.
**Tiru** — hanya ide + mekanismenya: daftar pengaman bertahap, tiap langkah dengan perintah/setting nyata, tutup dengan prinsip "pembatas
teknis > instruksi" dan CTA kata kunci.
**Modifikasi** (wajib):
1. **Hook sendiri, sudut beda** — referensi menakut-nakuti soal agent yang nakal ("diam-diam baca file password"); kita mulai dari
   **pertanggungjawaban ke klien**: *Klien nanya: "Kemarin AI-nya ngapain aja di server saya?" Kamu punya buktinya?* — sudut freelancer / dev
   UMKM Indonesia yang ngerjain website klien pakai agent. Visual: chat klien + kartu "Bukti kerja agent" yang KOSONG.
2. **Struktur, urutan, dan metafora visual sendiri** — bukan "3 lapis" tapi **checklist tiga babak per waktu: SEBELUM · SELAMA · SESUDAH agent
   kerja** (7 hal), dengan **rel fase** di atas layar yang mencentang tiap item. Urutan kita: akun sendiri → commit git (titik awal) → Hermes
   manual → OpenCode ask → auditd → log milik root → git status + diff → "larangan di prompt bukan pagar". Metafora per babak (semua gaya LIGHT
   AI PRENEUR: latar putih–biru + grid animasi, kartu putih, teks gradasi navy, Poppins): **kartu akses bertali (ID badge)** vs **kunci utama
   admin** + **grup sudo yang menolak agent**; **foto snapshot (polaroid) + bendera "titik awal"** di garis waktu; **tuas pilihan / rem tangan**
   smart · manual · off untuk Hermes + kartu izin asli (once/session/always/deny); **palang tol per alat** (bash/edit/webfetch: naik = allow,
   turun = ask, rm * = deny) untuk OpenCode; **printer struk kasir** yang mencetak tiap perintah (auditd); **brankas milik root** + penghapus
   akun agent yang mental + "Permission denied"; **kartu bandingkan SEBELUM | SESUDAH** dengan gagang pembanding (git diff) + daftar file
   git status; **catatan tempel vs pagar** (aksi agent tembus catatan, mental di pagar sistem). **Tidak ada** gedung isometrik, kubus sandbox,
   karakter piksel, terminal gelap bertabel, kartu toggle merah, kartu kopi, palet krem/merah, atau tata letak referensi.
3. **Sudut praktisi yang benar** — tidak ada klaim "aku pakai ini di server klien" (tidak bisa dipastikan). Suara "aku" hanya di CTA. Yang
   dibawa: kebiasaan praktisi yang bisa langsung dipakai (perintah & config asli, cara cek sesudahnya), tanpa angka atau hasil pribadi.
4. **Nilai untuk penonton Indonesia** — konteks freelancer/UMKM yang pegang website klien (contoh "toko online", folder /var/www/toko, "Promo
   Lebaran → Promo Akhir Tahun"), bukti untuk klien, dan langkah yang referensi lewatkan: **perintah nyata** di layar (`sudo adduser agent`,
   `git add -A && git commit`, `hermes config set approvals.mode manual`, config `permission` OpenCode, aturan auditd, `rm` yang ditolak,
   `git restore`), **git status** untuk file baru (git diff saja tidak menunjukkan file baru), **config OpenCode ditaruh di
   /etc/opencode/opencode.json milik root** biar agent tak bisa melonggarkannya sendiri, dan di DM: Hermes lewat backend SSH dengan user `agent`,
   `approvals.deny`, `--auto` OpenCode yang harus dihindari, aturan auditd 32/64-bit, cek `never,task`, `ausearch -k agent -i`.
5. **CTA dan penutup sendiri** — "Ingat, larangan di prompt itu bukan pagar. Pagarnya harus di sistem." + "Komen AMAN, aku kirim lewat DM."
   (tanpa ajakan debat "berani nggak", tanpa donasi/kopi, tanpa follow). Isi DM: `production/DM_AMAN.md`.
- **Dibuang:** nama kreator, sapaan, daftar terima kasih, traktir kopi, ajakan follow; "least privilege" sebagai lapis terpisah (dilebur ke
  item akun + akses folder); sandbox sebagai lapis tersendiri (disebut singkat di DM: backend container Hermes melewati approval karena
  container-nya yang jadi batas); "mode YOLO" sebagai satu-satunya bahaya (kita tunjukkan `--yolo`, `/yolo`, dan `mode: off`).
- **Aturan 3 kata:** dicek baris per baris terhadap transkrip referensi. Dicek otomatis (n-gram): satu-satunya kesamaan 3 token
  adalah "Di OpenCode," (kata depan + nama produk; transkrip menulisnya "di open code"); sisanya maksimal 2 kata ("akun agent", "di server",
  "yang dia", "Di Hermes,"). "mode manual" tidak dipakai — kita bilang "approvals ke manual". Kalimat referensi "Di open code, bawaannya…" sengaja dihindari → "Di OpenCode, setelan awalnya serba boleh";
  "baris mana yang diganti" → "file dan baris yang dia ubah"; "dia bisa menghapus jejaknya" → "agent nggak bisa hapus jejaknya".

## Fakta yang dicek (2026-11-13, sumber resmi)
- **Akun terpisah, bukan admin** — Ubuntu Server docs, *User management* (ubuntu.com/server/docs/how-to/security/user-management/):
  `sudo adduser username` membuat akun lokal; "To give any other account full root access through sudo, add them to the sudo group" → akun
  agent **tidak** dimasukkan ke grup sudo. Alternatif non-Debian: `useradd -m -s /bin/bash` (shadow-maint, man useradd(8)). Akses hanya ke
  folder web klien lewat ACL: `setfacl -R -m u:agent:rwX` (+ `-d` untuk default ACL) — man setfacl(1), manpages.ubuntu.com (noble).
- **auditd** — paket Ubuntu `auditd` (packages.ubuntu.com/noble/auditd, 1:3.1.2). Man page resmi (github.com/linux-audit/audit-userspace,
  docs/): auditctl(8) `-a always,exit … -S execve … -F uid=<akun>` ("uid: User ID. May be numeric or the user account name"), `-k key`
  ("can be searched on with ausearch"), saran menulis dua aturan `arch=b64` dan `arch=b32`; bagian "DISABLED BY DEFAULT" (aturan `-a
  never,task` di beberapa sistem → cek `auditctl -l`); `-e 2` mengunci konfigurasi sampai reboot. augenrules(8): file `*.rules` di
  /etc/audit/rules.d/, dimuat dengan `augenrules --load`. ausearch(8): `-k`, `-i` (interpret uid → nama akun), `--start today`.
- **Log milik root** — auditd.conf(5): `log_file` bawaan /var/log/audit/audit.log; `log_group` bawaan root; direktori log harus milik root
  dan tidak bisa ditulis grup/lainnya. Akun tanpa sudo tidak bisa menghapus/mengubahnya → di layar `rm …: Permission denied` (ilustrasi pesan
  standar `rm`). Hermes juga menulis log sendiri di `~/.hermes/logs/` (Hermes docs, *Security → Best Practices*: "Monitor logs — check
  ~/.hermes/logs/") — kalau Hermes jalan pakai akun agent, log itu ada di wilayah agent → pegangan tetap log auditd (dicatat di DM).
- **git snapshot + diff** — dokumentasi resmi git (github.com/git/git, Documentation/*.adoc): git-commit(1), git-status(1) ("paths that have
  differences … and paths in the working tree that are not tracked by Git" → file baru), git-diff(1) (perubahan baris relatif ke index/commit),
  git-restore(1) (mengembalikan path di working tree), git-clean(1) `-n/--dry-run` (di DM).
- **Hermes Agent (Nous Research, MIT)** — github.com/NousResearch/hermes-agent, `website/docs/user-guide/security.md` (sumber halaman docs
  hermes-agent.nousresearch.com/docs/user-guide/security; situs docs diblokir proxy sandbox, file sumbernya dibaca langsung dari GitHub):
  `approvals.mode` di `~/.hermes/config.yaml` = **smart** (bawaan: LLM pembantu menilai risiko) | **manual** ("Always prompt the user for
  approval on dangerous commands") | **off** ("equivalent to running with --yolo"); YOLO lewat `hermes --yolo`, `/yolo`, `HERMES_YOLO_MODE=1`
  ("bypasses all dangerous command approval prompts"); prompt CLI: once | session | always | deny (deny = bawaan); `approvals.deny` (glob,
  diblok sebelum yolo); backend docker/modal dll. melewati cek approval (container = batas); catatan "Deny rules are a shell-command policy,
  not … an OS capability sandbox … For containment, use OS permissions". `configuration.md`: `hermes config set KEY VAL` (setting bertitik →
  config.yaml); backend SSH: `terminal.backend: ssh` + `TERMINAL_SSH_HOST`, `TERMINAL_SSH_USER` di ~/.hermes/.env.
- **OpenCode (MIT)** — github.com/anomalyco/opencode (repo docs `services/site/src/docs/`, commit 5b131f5, 13 Nov 2026; opencode.ai diblokir
  proxy sandbox). V1 `permissions.mdx`: key `"permission"` di `opencode.json`, nilai `allow | ask | deny`, aturan pola dengan "last matching
  rule winning", **"Most permissions default to allow"**; `--auto` menyetujui otomatis semua yang tidak di-deny. V2 (`@opencode/cli` 2.3.0,
  npm 13 Nov 2026; `opencode-ai` 1.19.5 masih ada) `permissions.mdx`: array `permissions` (`shell`, `edit`, …), base policy *allow semua kecuali
  baca .env*; `migrate-v1.mdx`: "V2 normalizes supported V1 and native V2 fields" → format V1 di layar tetap dibaca V2. `config.mdx` (V1):
  managed settings Linux **/etc/opencode/** — "require admin/root access to write, so users cannot modify them", prioritas tertinggi.
- **"Larangan di prompt bukan pagar"** — didukung dua dokumen resmi di atas: Hermes (deny rules bukan sandbox; pakai izin OS) dan OpenCode V2
  ("`shell` runs with the host user's filesystem, process, and network authority"). Hermes juga memindai file konteks karena *prompt injection*
  (perintah titipan di file) memang risiko nyata.
- Contoh di layar (nama toko, file, jam, isi struk, "Promo Lebaran") berlabel **CONTOH**/ilustrasi; tidak ada angka statistik atau klaim hasil.

## Naskah (dikirim ke ElevenLabs, voice tersimpan, **tanpa --tags** → auto tag klien)
Tag yang benar-benar dipakai (dari `assets/audio/vo.json`):
[playful] [excited] [curious] Klien nanya: "Kemarin AI-nya ngapain aja di server saya?" Kamu punya buktinya?
[playful] [excited] Ini checklist tiga babak: sebelum, selama, dan sesudah agent kerja.
[playful] [excited] Sebelum: agent dapat akun sendiri, bukan admin, nggak masuk grup sudo.
[playful] [excited] Commit dulu folder webnya ke git, biar ada titik awal.
[playful] [excited] Di Hermes, set approvals ke manual, jangan pernah nyalain yolo.
[playful] [excited] Di OpenCode, setelan awalnya serba boleh, jadi ubah permission-nya ke ask.
[playful] [excited] Selama: audit-d merekam semua perintah akun agent, plus jamnya.
[playful] [excited] Log-nya milik root, jadi agent nggak bisa hapus jejaknya.
[playful] [excited] Sesudah: git status dan git diff nunjukin file dan baris yang dia ubah.
[playful] [excited] Ingat, larangan di prompt itu bukan pagar. Pagarnya harus di sistem.
[playful] [excited] [confident] Komen aman, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt` (112 kata, 707 karakter). Kata kunci CTA dikirim huruf kecil ("Komen aman") supaya tidak dieja
A-M-A-N; caption menampilkan **AMAN,**. "auditd" ditulis "audit-d" untuk TTS; caption menampilkan **auditd**. Dibuat dengan
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` → **take 1 (satu-satunya), 45,04 dtk,
11 baris**. Cek dengar faster-whisper (bahasa id) `small` + `medium` di seluruh take: semua kata Indonesia terdengar benar di minimal satu
model (small: "Client" untuk "Klien", "stelaan" untuk "setelan", "Loknya" — medium benar ketiganya). Istilah teknis: "git diff" ditulis "Git
Div" oleh kedua model bahasa Indonesia, tapi whisper `medium`/`small` mode bahasa Inggris pada potongan yang sama menulis "GitDiff"/"Get Diff"
→ pengucapan benar, ejaan saja; "audit-d" → "Audit D"/"Audit Day" (= pengucapan lazim "audit-dee"). Tidak ada kata yang salah dengar di kedua
model → **tidak ada re-take** (hemat kredit). Tag tidak ikut terbaca.
Klien nanya: "Kemarin AI-nya ngapain aja di server saya?" Kamu punya buktinya?
Ini checklist tiga babak: sebelum, selama, dan sesudah agent kerja.
Sebelum: agent dapat akun sendiri, bukan admin, nggak masuk grup sudo.
Commit dulu folder webnya ke git, biar ada titik awal.
Di Hermes, set approvals ke manual, jangan pernah nyalain yolo.
Di OpenCode, setelan awalnya serba boleh, jadi ubah permission-nya ke ask.
Selama: audit-d merekam semua perintah akun agent, plus jamnya.
Log-nya milik root, jadi agent nggak bisa hapus jejaknya.
Sesudah: git status dan git diff nunjukin file dan baris yang dia ubah.
Ingat, larangan di prompt itu bukan pagar. Pagarnya harus di sistem.
Komen aman, aku kirim lewat DM.
