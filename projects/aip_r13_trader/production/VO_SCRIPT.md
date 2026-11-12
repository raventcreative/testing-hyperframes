# VO — Claude bantu analisa saham: Day Trader Skill · background NAVY · 47,84 dtk VO (video 49,47 dtk)

Referensi: `aip_remake_batch5/refs/ref3.mp4` (72,7 dtk, ID, brand merah/hitam + maskot rambut merah, "Trader Skill", CTA "Trader",
penutup "Follow AI Shift"). Topik FINANSIAL: tidak ada klaim profit, tidak ada "pasti cuan", tidak ada ticker asli sebagai tips (contoh
generik **SAHAM A**), di layar terus-menerus pill **"Bukan ajakan beli/jual · edukasi"** (frame 0 sampai frame terakhir), akun latihan
(paper) dulu, tiap order butuh persetujuan kamu, alat bukan jaminan. Hasil jujur referensi (uji coba ≈ lempar koin) dipertahankan.

## ATM — Amati, Tiru, Modifikasi

**Amati (referensi):**
- Ide berguna: satu pack skill Claude gratis yang kerjanya kayak tim trader (11 tugas), plus "Time Machine" yang mensimulasikan sisa hari
  sebelum uang keluar; order cuma jalan kalau kamu setuju; awalnya akun latihan.
- Mekanisme hook: klaim manfaat + gratis ("Sekarang Claude bisa bantu kamu trading saham, dan gratis").
- Struktur beat: nama → "kelihatannya 1 skill, padahal 11" → daftar 10 skill satu per satu (grid kartu putih) → "yang ke-11 paling gila"
  Time Machine → hasil uji (Tesla, 29 % / 25 %) → "hampir lempar koin" → persetujuan + akun latihan → cara pasang → "Berani cobain?" → CTA.
- Mekanisme CTA: komen kata kunci → link dikirim lewat DM, lalu ajakan follow.

**Tiru (yang kita ambil, hanya ide umum):** pack 11 skill sebagai "tim", Time Machine sebagai pemeriksa realitas, hasil jujur ≈ lempar
koin, persetujuan + paper trading, pasang dengan menempel link, CTA komen kata kunci.

**Modifikasi — ATM: what we changed**
1. **Hook sendiri, sudut beda:** referensi menjual "Claude bisa bantu trading, gratis". Kita membalik sudutnya ke *rem*: "Mau pakai AI buat
   trading saham? Pilih yang berani bilang: jangan dulu." Visual hook: tombol BELI yang didorong AI lain ("Lagi naik terus, beli sekarang!"
   dicoret) lalu dikunci oleh Claude ("Jangan dulu."). Tidak ada kata yang sama dengan hook referensi.
2. **Struktur + metafora visual sendiri:** bukan daftar 10 kartu satu per satu + "nomor 11", tapi **3 lapis** — LAPIS 1 CARI (scanner, news,
   analyst, pelosi) · LAPIS 2 RENCANA (entry, exit, time machine) · LAPIS 3 REM (budget, risk, broker, alerts) — sebagai tiga rak kaca
   navy; 11 chip skill (nama perintah asli dari README) jatuh ke raknya. Tiap lapis punya demo sendiri: grid grafik + sapuan scanner, kartu
   berita + laporan kuartal, chart rencana dengan zona stop (merah) / target (hijau), kipas 46 jalur simulasi yang diwarnai sesuai apa yang
   kena duluan, waffle 100 sel untuk hasil, dua tiket order PASS vs BLOCK, tiga "gerbang" persetujuan, saklar PAPER/LIVE, catatan jujur,
   chat Claude untuk cara pasang. Tidak ada layout, warna, maskot, kartu atau ikon referensi (gaya NAVY AI PRENEUR, robot + maskot kita).
3. **Sudut praktisi Freddie:** tidak dipakai — tidak ada bukti Freddie memakai pack ini untuk trading, jadi tidak ada "aku pakai ini buat…"
   dan tidak ada hasil/angka pribadi yang dikarang. Suara tetap "aku/kamu" dan sudutnya edukasi.
4. **Nilai untuk penonton Indonesia yang tidak ada di referensi:** (a) catatan jujur bahwa datanya **saham Amerika** (Yahoo Finance, Nasdaq
   Trader, SEC EDGAR — jadi bukan data BEI) → "anggap ini alat belajar, bukan jaminan"; (b) langkah yang dilewati referensi: **batas rugi
   per trade** + contoh order yang **DIBLOKIR** karena melewati batas; (c) persetujuan dijelaskan sebagai **3 kunci** (Risk PASS → kamu ketik
   "ya" → klik "Allow once"); (d) kutipan fine print README "kebanyakan orang yang day trading rugi"; (e) DM di CTA menulis "Mulai di akun
   paper dulu, ya."; (f) tidak ada ajakan "Berani cobain?" (referensi) — diganti peringatan.
5. **CTA + penutup sendiri:** "Komen SAHAM, aku kirim lewat DM." (kata kunci SAHAM, bukan "Trader"; "aku", bukan "kami"; tanpa "follow
   untuk info menarik lainnya").
- Cek kata: tidak ada 4 kata berurutan yang sama dengan transkrip referensi (dicek otomatis, n-gram 4 = 0). Satu-satunya 3 kata yang
  sama adalah "kirim lewat DM" — bagian CTA wajib dari brief.

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
Sumber utama: repo **github.com/Jakeschincariol/day-trader-skill** — dibaca lewat raw.githubusercontent.com (README.md, LICENSE,
trader-broker/SKILL.md, trader-timemachine/SKILL.md, trader-risk/SKILL.md, trader-scanner/SKILL.md, trader-budget/config.example.json).
Nama repo + author juga terlihat di layar referensi ("Jakeschincariol / day-trader-skill"). (Halaman HTML github.com dan API GitHub
diblok proxy sesi ini; isi repo dibaca langsung dari file mentahnya.)

| Klaim di VO / visual | Bunyi di sumber | Sumber |
|---|---|---|
| Nama "Day Trader Skill", 11 skill Claude | "# The Day Trader skill — 11 Claude skills for day trading…"; tabel "The eleven": /trader-scanner, /trader-news, /trader-entry, /trader-exit, /trader-timemachine, /trader-risk, /trader-budget, /trader-broker, /trader-alerts, /trader-analyst, /trader-pelosi. (README juga menyebutnya "the Trader skill v2"; "Trader skill" asli adalah repo lain, `trader-skill`.) | README |
| Gratis, open source (MIT), repo github.com/Jakeschincariol | "Free, MIT, no signup, no API key."; LICENSE = MIT, © 2026 Jake Schincariol | README, LICENSE |
| Lapis cari: ribuan grafik, berita, laporan keuangan (+ Kongres AS) | scanner "Scans thousands of charts for setups"; news "Tracks breaking news on every stock you watch"; analyst "Reads earnings reports and sums up what changed"; pelosi "Reads Congress's stock-trade disclosures"; `scan.py universe  # ~5,900 US stocks, Nasdaq Trader` (layar: "± 5.900 saham AS dipindai") | README, trader-scanner/SKILL.md |
| Lapis rencana: titik masuk, stop loss + target sebelum beli, rasio 1 : 1 | entry "tells you the moment to get in"; exit "Sets your stop and your target before you enter"; contoh: "target one times that risk" (1R) | README |
| Time Machine: 10.000 simulasi sisa sesi, sebelum uang keluar | "replays the rest of the session 10,000 times from the stock's own recent bars… before you risk a dollar"; "a simulation, not a prediction" | README, trader-timemachine/SKILL.md |
| Hasil contoh: target duluan 29,4 %, stop duluan 25,5 %, masih terbuka saat tutup 45,1 % → nyaris lempar koin | contoh README (Tesla, 19 Okt 2026, data asli): "target first 29.4 %, stop first 25.5 %, still open at the close 45.1 %… Its verdict: close to a coin flip." Ticker TIDAK ditampilkan (layar: "1 saham AS"). | README (How to use it, langkah 5) |
| Lapis rem: batas rugi per trade, yang lewat batas diblokir | risk "Checks every trade against your limits and stops anything over them" — "PASS or BLOCK, with the reason"; budget "Sizes every position to your budget and your max loss per trade" | README, trader-risk/SKILL.md |
| Angka tiket (contoh): modal $5.000, batas rugi $50, stop $5,86/lembar → 8 lembar = $46,88 (PASS); 30 lembar = $175,80 (BLOCK) | config.example.json: "budget": 5000, "max_loss_per_trade_usd": 50; README: "5.86 a share at risk… 50 / 5.86 = 8 shares… the loss is $46.88". 30 × 5,86 = 175,80 (hitungan kita, untuk contoh yang diblokir) | README, trader-budget/config.example.json |
| Tidak ada order tanpa persetujuan kamu (3 kunci) | "no trade goes through until you say yes. Nothing in this pack can place an order on its own."; broker: "1. trader-risk passed this exact order… 2. The user typed an explicit yes… 3. The user clicked Allow once" | README, trader-broker/SKILL.md |
| Bawaannya akun latihan (paper) | "Paper trading is the default."; config.example.json `"paper": true` | README, config.example.json |
| Datanya saham Amerika | "plain Python that read free public data: Yahoo Finance charts, Nasdaq Trader's symbol lists, SEC EDGAR and the House Clerk"; universe "~5,900 US stocks" | README |
| Bukan jaminan; kebanyakan day trader rugi | "Not financial advice… Most people who day trade lose money. You can lose money." | README (Fine print) |
| Cara pasang: tempel link GitHub ke Claude + "install skill"; di Claude Code bisa juga lewat /plugin | "Paste this into Claude: https://github.com/Jakeschincariol/day-trader-skill — install skill"; "Or as a plugin, in Claude Code: /plugin marketplace add… /plugin install day-trader-skill@day-trader-skill" | README (Install) |

Yang dibuang/diperbaiki dari referensi: nama "Trader Skill" → nama asli "Day Trader Skill"; ticker Tesla tidak ditampilkan (layar menulis
"1 saham AS", contoh generik "SAHAM A" di semua demo); "29 % / 25 %" → angka persis README 29,4 / 25,5 / 45,1 (jumlah 100); "dia ngulang
sisa hari itu 10 ribu kali" → "10.000 simulasi sisa sesi bursa" (bahasa sendiri, sesuai README); "Anggota Congress" hanya jadi chip
"pelosi · Kongres AS" (tidak dibacakan); "Berani cobain trading pakai skill ini?" dibuang (mendorong trading); "Follow AI Shift" dibuang.
Semua angka di demo (harga 1.000 / 970 / 1.030, $50, $46,88, $175,80, 8 / 30 lembar, ± 5.900, 08:04, naik/turun di laporan) adalah CONTOH
berlabel "contoh"/"ilustrasi" dan konsisten satu sama lain; ticker selalu "SAHAM A" (atau "A/B/C" di tag SETUP). Claude sendiri tetap
butuh akun Claude — VO tidak mengklaim Claude gratis ("gratis" = pack-nya, MIT).

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = AUTO tags klien)
Tag yang dipakai (dari `production/vo_el.json`): semua baris `[playful] [excited]`, baris 6 + `[sighs]` (konteks "tipis"), baris 11 +
`[confident]` (CTA).
1. `[playful] [excited]` Mau pakai AI buat trading saham? Pilih yang berani bilang: jangan dulu.
2. `[playful] [excited]` Namanya Day Trader Skill: sebelas skill Claude gratis, dibagi tiga lapis.  (caption: **11**)
3. `[playful] [excited]` Lapis satu nyari: ribuan grafik, berita, sampai laporan keuangan.
4. `[playful] [excited]` Lapis dua ngerencanain: titik masuk, stop loss, dan target.
5. `[playful] [excited]` Plus Time Machine: sepuluh ribu simulasi sisa sesi bursa, sebelum sepeser pun keluar.  (caption: **10.000**)
6. `[playful] [excited] [sighs]` Di contohnya, peluang target duluan sama stop loss duluan beda tipis: nyaris lempar koin.
7. `[playful] [excited]` Lapis tiga ngerem: batas rugi dijaga, trade yang lewat batas diblokir.
8. `[playful] [excited]` Nggak ada order tanpa persetujuan kamu, dan bawaannya akun latihan.
9. `[playful] [excited]` Datanya saham Amerika, jadi anggap ini alat belajar, bukan jaminan.
10. `[playful] [excited]` Pasangnya: tempel link GitHub-nya ke Claude, terus tulis install skill.
11. `[playful] [excited] [confident]` Komen SAHAM, aku kirim lewat DM.

Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, tags "auto"), dibuat
dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan, 47,92 dtk
alignment / 47,84 dtk audio, 116 kata) → `assets/audio/vo.mp3`. Cek pelafalan dengan faster-whisper small: semua baris terbaca
(whisper menulis "Claude" sebagai "cloud", "tempel link GitHub-nya" sebagai "tempen lingkit hapnya" — salah dengar whisper yang biasa,
juga terjadi di R9; "sepeser" → "sepesar").
