# VO — R30 · Tim marketing AI, 3 modul, kamu bosnya · background NAVY · VO 88,0 dtk (mulai 0,3 dtk) · video 90,47 dtk

Referensi: `aip_remake_batch7/refs/ref4.mp4` (92,35 dtk, bahasa Inggris, kreator lain; diagram "one-person marketing team" putih
dengan banyak logo, 36 agent, 4 kartu modul, kartu CRM/kalender, "morning page", CTA "Comment MARKETING"). Panjang dijaga ≈ referensi
(−2 %): 14 kalimat + jeda 0,7 dtk di 6 pergantian bagian (`tools/vo_pad.py`), suara tidak diperlambat.

## ATM: what we changed (Amati · Tiru · Modifikasi)
**Amati:** hook "one-person company that feels like 24 employees / 36 agents"; marketing sebagai loop, bukan funnel; tidak ada post
yang tayang sebelum di-approve; Modul 1 Research & Content (Claude), Modul 2 Creative & Distribution (Higgsfield, ElevenLabs,
auto-post + balas komentar), Modul 3 Analytics Loop (tool analitik "Jev"/"Jeff"), Claude Code menjalankan semuanya tersambung ke CRM,
kalender, channel; tiap pagi satu halaman; "AI moves the information, you move the brand and the budget"; CTA "Comment MARKETING".
**Tiru (hanya ide + mekanisme):** 3 modul (riset & konten → kreatif & distribusi → loop analitik), aturan setujui-dulu, satu halaman
ringkasan pagi, Claude Code sebagai mesin, prinsip "AI memindahkan informasi, kamu pegang brand & budget", kata kunci MARKETING (brief).
**Modifikasi:**
1. **Hook sendiri:** bukan "24 karyawan / 36 agent", tapi daftar kerjaan marketing yang berputar cepat (spinning pain list) dan
   mendarat di "Semua kamu kerjain sendiri?" → "kamu cukup jadi bosnya". Tanpa angka agent/karyawan.
2. **Struktur + metafora sendiri:** to-do reel slot → chip berhamburan (chaos) → masuk 3 kotak tim AI (control) → kartu "Kamu · bos";
   corong digambar lalu dicoret → berubah jadi putaran 3 stasiun, "Minggu 1 → Minggu 2"; gerbang terkunci + tombol "Setujui" yang
   membuka feed; Modul 1 = radar tren + pertanyaan pembeli + toples "Bank ide" (process fill) + kalender seminggu; Modul 2 = studio
   (Higgsfield gambar/video, ElevenLabs suara dengan gelombang suara ASLI reel ini) → stempel Disetujui → 3 channel → balasan komentar
   + komentar sensitif dilempar ke "Inbox kamu"; Modul 3 = tabel CONTOH (likes vs chat/booking/jual, tanpa angka) → titik cyan
   kembali ke modul 1 → grafik 4 minggu ILUSTRASI → spreadsheet manual dicoret; Claude Code = terminal + 3 konektor + "Ringkasan pagi";
   penutup = kartu AI (memindahkan data) vs kartu Kamu (Brand, Budget, terkunci) → CTA. Tidak ada diagram/logo-wall/kartu referensi.
3. **Sudut praktisi (benar):** "Suara di video ini juga pakai ElevenLabs" — VO reel ini memang ElevenLabs (voice Dakocan, eleven_v4).
   Tidak ada klaim hasil/penghasilan Freddie.
4. **Nilai tambah Indonesia:** contoh kedai kopi (CONTOH, fiktif), balasan komentar gaya bahasa lokal, aturan keamanan yang
   referensi tidak punya: komentar SENSITIF (komplain/refund) tidak dibalas AI, diteruskan ke kamu; ukur chat/booking/penjualan,
   bukan cuma likes; kalender ide seminggu.
5. **CTA + penutup sendiri:** "Komen marketing, aku kirim blueprint-nya lewat DM." (kata kunci dari brief) + kartu file "Blueprint tim
   marketing AI · 3 modul · aturan setujui · ringkasan pagi" (= isi `DM_MARKETING.md`). Tidak menjanjikan "gratis" di VO/cover.
**Cek kata:** referensi bahasa Inggris → tidak ada ≥3 kata berurutan yang sama.

## Klaim referensi yang DIBUANG / DIGENERALKAN
- "24 employees", "36 agents", "5/10 agents" per modul → dibuang (angka tidak bisa/perlu diverifikasi, terdengar hype).
- Tool analitik "Jev" (di layar referensi "Jev · Which posts brought calls and sales"; transkrip "Jeff") → **tidak terverifikasi**:
  pencarian hanya menemukan Jevu.ai (notetaker panggilan sales, bukan analitik postingan). Dibuang; di reel cukup "putaran analitik"
  (tanpa nama tool), tabel berlabel CONTOH.
- Logo-logo lain di diagram referensi (HubSpot, Canva, Notion, dll.) → tidak dipakai.
- "more followers turn into customers", "makes more of what makes you money", "$4,200" di morning page → dibuang (tanpa janji
  hasil/uang). Ringkasan pagi berisi contoh fiktif berlabel CONTOH tanpa nominal.
- "answers every comment" → dikoreksi: komentar dibalas dengan gaya bahasamu, yang sensitif tetap ke kamu.

## Fakta yang dicek (20 Nov 2026)
| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| Claude Code menjalankan semuanya, "tersambung ke data pelanggan, kalender, akun sosmed" (layar: "lewat konektor MCP") | "Claude Code can connect to hundreds of external tools and data sources through the Model Context Protocol (MCP), an open source standard for AI-tool integrations." · "MCP servers give Claude Code access to your tools, databases, and APIs." | https://code.claude.com/docs/en/mcp (WebFetch) |
| "Claude nyari apa yang lagi rame … nulis draf postingan, caption, email" | Kemampuan umum Claude (riset web + menulis); disebut sebagai alur kerja, bukan fitur khusus | — (deskripsi alur, bukan klaim produk) |
| "Higgsfield bikin gambar dan video" | Higgsfield: platform AI multi-model untuk video, gambar, editing (video: Kling, Veo, Sora…; gambar: Soul, Nano Banana, GPT Image…) | https://higgsfield.ai/about , https://higgsfield.ai/llms.txt (via WebSearch; higgsfield.ai DNS-blok di sandbox) |
| "ElevenLabs ngisi suaranya" + "Suara di video ini juga pakai ElevenLabs" | ElevenLabs text-to-speech, termasuk bahasa Indonesia; VO reel ini dibuat lewat API ElevenLabs (tools/el_tts_ts.py, voice Dakocan, model eleven_v4) | https://elevenlabs.io/text-to-speech/indonesian (via WebSearch; elevenlabs.io DNS-blok di sandbox); `production/vo_el.json` |
| Logo 3D (Claude, Claude Code, ElevenLabs, Instagram, TikTok, WhatsApp) | Simple Icons 16.38.0, CC0-1.0 | npm `simple-icons@16.38.0` → `production/asset_credits.json` |
Higgsfield tidak ada di Simple Icons → hanya nama (teks), tanpa logo. Semua isi kedai kopi, komentar, tabel, grafik, ringkasan pagi,
nama "Kantor Sinar", "Bu Rina" = CONTOH/ILUSTRASI buatan kita (label di layar).

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = tag AUTO klien)
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (take 2, 83,92 dtk) →
`python3 -I tools/vo_pad.py .` (+0,7 dtk sebelum baris 3, 5, 7, 9, 11, 13) → `assets/audio/vo.mp3` (88,04 dtk).
1. `[playful] [excited] [confident]` Cari tren, nulis caption, bikin desain, isi suara, posting, balas komen, cek angka. Semua kamu kerjain sendiri?
2. `[playful] [excited]` Coba bayangin semua itu dipegang tim marketing AI, dan kamu cukup jadi bosnya.
3. `[playful] [excited]` Bentuknya bukan corong yang sekali jalan selesai, tapi putaran. Hasil minggu ini jadi bahan buat minggu depan.
4. `[playful] [excited]` Dan aturan nomor satu: nggak ada postingan yang tayang sebelum kamu setujui.
5. `[playful] [excited]` Modul satu, cari tren dan bikin konten. Claude nyari apa yang lagi rame di pasarmu, dan pertanyaan yang paling sering ditanya pembeli.
6. `[playful] [excited]` Dari situ, dia nulis draf postingan, caption, sampai email. Jadi kamu nggak pernah kehabisan ide.
7. `[playful] [excited]` Modul dua, kreatif dan distribusi. Higgsfield bikin gambar dan video, ElevenLabs ngisi suaranya. Suara di video ini juga pakai ElevenLabs.
8. `[playful] [excited]` Begitu kamu setujui, postingan dijadwalkan ke tiap channel, dan komentar dibalas pakai gaya bahasamu. Yang sensitif, tetap dilempar ke kamu.
9. `[playful] [excited]` Modul tiga, putaran analitik. Tiap postingan dicek: mana yang bawa chat, booking, dan penjualan. Bukan cuma likes.
10. `[playful] [excited]` Hasilnya balik lagi ke modul satu. Minggu depan, kamu bikin lebih banyak yang terbukti jalan, tanpa rekap spreadsheet manual.
11. `[playful] [excited]` Yang menjalankan semuanya Claude Code, tersambung ke data pelanggan, kalender, dan akun sosmedmu.
12. `[playful] [excited]` Tiap pagi kamu terima satu halaman: apa yang berhasil, siapa yang sudah booking, dan langkah berikutnya.
13. `[playful] [excited]` Ingat, AI cuma memindahkan informasi. Brand dan budget, tetap kamu yang pegang.
14. `[playful] [excited] [confident]` Komen marketing, aku kirim blueprint-nya lewat DM.

**Listen-check (faster-whisper small + medium, take 2):** take 1 diganti karena KEDUA model mendengar "Riset" sebagai "Reset" (baris 1 & 5)
→ reword "Cari tren" / "cari tren dan bikin konten". Take 2: semua kata benar di minimal satu model, kecuali nama merek yang dieja di layar
("Claude" → "Cloud", "ElevenLabs" → "11 Labs", "Higgsfield" → "Hicksfield"; ejaan di caption & layar benar).

## Recipes dipakai (dari `skills/aipreneur-reels-studio/references/mascot_robot_recipes.md`) + kredit teknik
1. **Spinning pain list** (s01): to-do reel berputar kabur, mendarat per kerjaan, spin cepat → "Semua: kamu sendiri?" — jake11moran-f60e35 (prompt-motion.com).
2. **Accent-dot journey / guide object** (semua scene): titik cyan #01ccf7 = selector reel → mahkota bos → jatuh lewat corong → mengitari
   putaran → tombol Setujui → kalender ide → BANJIR cyan jadi header modul 2 → inbox → kembali stasiun 3→1 → MENGGAMBAR garis grafik →
   kursor terminal → menyusuri kabel konektor → bullet ringkasan pagi → mekar jadi logo AI PRENEUR — ultimaxbt-bbebf5, rossaxbt-94583b.
3. **Button → page** (s02→s03): tombol "Setujui" ditekan lalu membesar jadi banjir cyan yang menyusut jadi header Modul 1 (shared element; technique_bank "buttons expand into pages").
4. **Process fill** (s03): 6 temuan (tren + pertanyaan) dituang ke toples "Bank ide", level naik per bahan, lalu draf keluar — ror-fly-9950f1.
5. **Chaos → control → clarity → brand** (arc keseluruhan): kerjaan berhamburan → 3 tim AI + bos → modul jelas + ringkasan 1 halaman → kartu brand/budget + logo — daniel-haida-8691d4.
6. **Camera push 1.00→1.04** per scene (layer `#P-cam`, hand-over di layer `#P-hud` yang tidak di-zoom) + **small-overshoot springs** (back.out ≤2.4) + **beat/word-locked changes** (setiap perubahan dikunci ke kata VO) + **VO ducking** (music bed di-duck oleh render_aip.sh/remix_aip.sh).
Transisi antar-scene berbeda tiap kali: hand-over org (s01→s02), button→flood (s02→s03), dot-flood (s03→s04), whip pan (s04→s05), dive (s05→s06), swipe-up (s06→s07).
