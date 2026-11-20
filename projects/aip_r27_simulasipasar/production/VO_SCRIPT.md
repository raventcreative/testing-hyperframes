# VO — R27 · Tes ide produk ke warga AI dulu (MiroFish) · background PUTIH (WHITE) · VO 38,9 dtk (video 40,40 dtk)
Referensi: batch 7 · `projects/aip_remake_batch7/refs/ref1.mp4` (39 dtk, bahasa Inggris, kreator lain, talking head + layar gelap/hijau
neon): "test your startup idea on thousands of fake customers before you build a single thing" → nama MiroFish, open source, "over 80,000
stars" → upload ide / pitch deck / MVP → dunia digital berisi orang AI (kepribadian, latar, memori, opini) → dilepas ke media sosial,
posting & debat → "focus group that runs by itself" → laporan + tanya kenapa beli/tidak → chat satu-satu → "Claude Code sets the whole
thing up" → CTA "Comment STARTUP … free setup guide". Panjang referensi 39 dtk → kita 40,4 dtk (+3,6 %, aturan ±10 %).

## ATM: what we changed
**Amati** — ide yang berguna: sebuah mesin simulasi open source yang membangun "dunia" berisi agen AI berkepribadian, melepas mereka ke
media sosial tiruan, lalu memberi laporan + bisa diajak ngobrol — dipakai untuk menguji ide sebelum keluar uang. Mekanisme: hook "uji ke
pelanggan palsu dulu", nama + bukti sosial (bintang GitHub), alur langkah demi langkah, CTA kata kunci → panduan setup.
**Tiru** — ide + urutan logis (unggah → dunia AI → interaksi → laporan/chat → setup), CTA kata kunci ke DM berisi panduan setup.
**Modifikasi** (wajib):
1. **Hook sendiri, sudut beda** — referensi: "startup idea, before you build a single thing". Kita: **"Sebelum stok barang atau bayar
   iklan, lempar dulu idemu ke warga AI."** Sudutnya UMKM Indonesia yang uangnya keluar duluan untuk **stok & iklan** (bukan startup/MVP).
   Visual hook: daftar pengeluaran modal yang **berputar cepat** (Cetak kemasan, Sewa booth, Stok barang, Endorse, Sewa ruko, Bayar iklan,
   Desain logo) lalu berhenti di "Stok barang" dan "Bayar iklan" → masuk kartu "UANG KELUAR" → kartu berubah jadi "Ide produk-mu" dan
   bohlamnya **dilempar** ke barisan "warga AI".
2. **Struktur & metafora visual sendiri** — metafora kita: **kota digital berisi warga AI** (skyline yang tumbuh gedung demi gedung, warga
   bermunculan), kartu persona yang "dipilih" lalu membesar jadi profil, **dua medsos tiruan** (feed + forum) yang kacau, bentrok
   "Kemahalan!" VS "Worth it!", lalu **laporan + chat** (chaos → control → clarity → brand). Tidak ada: talking head, layar gelap/hijau
   neon, wajah komik hitam-putih, highlight kuning, UI MiroFish asli, logo MiroFish (semua UI = desain kita, gaya WHITE AI PRENEUR).
3. **Sudut praktisi yang jujur** — tidak ada klaim "aku pakai ini" atau hasil pribadi. Yang kita bawa: kebiasaan praktisi — uji ide dulu
   sebelum belanja, dan **"Ingat, ini simulasi, bukan ramalan"** + teks layar "jadi bahan uji sebelum keluar modal · lalu tes lagi ke
   pembeli beneran" (referensi tidak memberi peringatan ini).
4. **Nilai untuk penonton Indonesia** — contoh produk lokal berlabel **ILUSTRASI**: *Kopi Susu Literan, 1 liter, Rp55.000, dijual
   online*; persona fiktif Rina (karyawan, Bekasi), Bayu (driver ojol, Medan), Sari (guru, Solo); reaksi yang realistis ("Rp55 ribu?
   Kemahalan, mending beli yang gelasan", "Awetnya berapa hari di kulkas?"). Tambahan yang dilewati referensi: **butuh API key** (model AI
   + Zep) = ada biaya → di DM ada cara hemat (ronde sedikit dulu, sesuai README).
5. **CTA & penutup sendiri** — "Komen ide, aku kirim lewat DM." (kata kunci **IDE**; diucapkan "ide" huruf kecil, caption **IDE,**). DM:
   panduan setup + prompt Claude Code (`production/DM_IDE.md`). Tanpa "free", tanpa "STARTUP".
- **Dibuang dari referensi:** "thousands of fake customers", "before you build a single thing", "over 80,000 stars" (kita: "puluhan ribu
  bintang", angka di layar 86 ribu+ dari GitHub hari ini), "pitch deck / rough MVP", "focus group that runs by itself", "why they'd buy or
  why they wouldn't", "free setup guide".
- **Beda dari R6 `aip_r6_founder`** ("Tes ide bisnis ke 100 pembeli AI", skill Founder, panel 100 avatar, katering Rp25.000, CFO, stempel
  TAHAN DULU, CTA FOUNDER): alat lain (MiroFish = simulasi sosial, bukan skill pack), produk lain (kopi literan), visual lain (daftar modal
  berputar, kota digital, kartu persona, dua medsos tiruan, laporan + chat), tanpa angka % beli, hook stok/iklan, CTA IDE.
- **Aturan 3 kata:** naskah bahasa Indonesia, referensi bahasa Inggris — tidak ada 4 kata berurutan yang sama; satu-satunya kesamaan
  adalah nama produk (MiroFish, GitHub, Claude Code).

## Resep yang dipakai (mascot_robot_recipes.md + technique_bank.md; kredit di sana)
1. **Spinning pain list** (jake11moran-f60e35) — hook: daftar pengeluaran modal berputar terlalu cepat untuk dibaca, melambat dan
   berhenti di "Stok barang" lalu "Bayar iklan"; maskot menunjuk.
2. **Robot-screen portal** (match cut) — s03 terbuka sebagai lingkaran dari visor robot (cincin biru + lingkaran yang melewati keempat
   sudut layar ≈0,4 dtk), adegan unggah dokumen ada "di dalam" robot.
3. **Chaos → control → clarity → brand** (daniel-haida-8691d4) — s05 feed + forum kacau (scroll makin cepat, debat VS, shake) → s07
   laporan rapi + chat satu warga → s09 "simulasi, bukan ramalan" → s10 kartu CTA + logo AI PRENEUR.
4. **Kinetic type, strikethrough jadi underline** (techhalla-90b8ec) — s09: coretan biru di "ramalan" meluncur turun jadi garis bawah
   "jadi bahan uji sebelum keluar modal" (coretan kedua tetap di "ramalan").
5. **Camera push 1.0 → 1.04** per adegan (slow push, tidak pernah diam) + **small-overshoot springs** (back.out 1.3–2) untuk semua kartu,
   chip, avatar; **beat-locked changes**: tiap kata kunci VO memicu perubahan (≥1 per detik), device baru tiap 3,6–5,7 dtk (10 adegan).
6. **Button → page (shared element)** (rossaxbt-94583b / technique bank) — s04: kartu mini Rina dipilih lalu membesar jadi kartu profil.

## Fakta yang dicek (2026-11-20, sumber resmi)
- **MiroFish** — repo https://github.com/666ghj/MiroFish (README dibaca dari raw.githubusercontent.com, kode di-clone dangkal untuk dicek).
  Deskripsi repo: "A Simple and Universal Swarm Intelligence Engine, Predicting Anything." **Lisensi AGPL-3.0** (file LICENSE). **86,0 rb
  bintang, 13,0 rb fork** (halaman repo GitHub, 2026-11-20) → VO "puluhan ribu bintang", layar "86 ribu+ · dicek 20 Nov 2026".
- README (Overview): "By extracting seed information from the real world … it automatically constructs a high-fidelity parallel digital
  world. Within this space, **thousands of intelligent agents with independent personalities, long-term memory, and behavioral logic**
  freely interact and undergo social evolution." · "You only need to: **Upload seed materials** … and describe your prediction
  requirements in natural language" · "MiroFish will return: **A detailed prediction report** and a deeply interactive high-fidelity
  digital world" → VO "unggah dokumen idemu … kota digital berisi ribuan warga AI … kepribadian, ingatan, dan cara bersikap".
- README (Workflow): "3. Simulation: **Dual-platform parallel simulation** …; 4. Report Generation: ReportAgent …; 5. Deep Interaction:
  **Chat with any agent in the simulated world**" → "posting, debat, saling balas di media sosial tiruan" (kode: platform `twitter` +
  `reddit` di `backend/app/services/simulation_*.py`, mesin OASIS dari CAMEL-AI, https://github.com/camel-ai/oasis) → layar "2 MEDSOS
  TIRUAN · jalan bareng" (tanpa logo X/Reddit); "Hasilnya laporan … ngobrol langsung sama satu warganya" (`interview_agents` di
  `backend/app/services/zep_tools.py`). Profil agen punya `bio`, `mbti`, `profession` (`oasis_profile_generator.py`).
- Pasang (README Quick Start): Node.js 18+, Python ≥3.11 ≤3.12, uv; `cp .env.example .env`; **wajib `LLM_API_KEY` (API format OpenAI
  SDK, contoh Qwen-plus) + `ZEP_API_KEY` (Zep Cloud, kuota gratis bulanan cukup untuk pemakaian sederhana)**; `npm run setup:all`;
  `npm run dev` (frontend :3000, backend :5001); opsi Docker. Catatan README: "**High consumption, try simulations with fewer than 40
  rounds first**" → VO "kamu tinggal isi API key", layar file .env dengan dua key itu; DM: hemat ronde.
- "Claude Code yang setup": klaim kita (bukan klaim MiroFish) — Claude Code bisa menjalankan perintah terminal, clone repo, dan memasang
  dependensi dengan izinmu (https://code.claude.com/docs/en/overview); kuncinya tetap kamu isi sendiri.
- Didukung/inkubasi Shanda Group (README) — tidak dipakai di VO.
- Semua contoh di layar adalah ilustrasi: produk "Kopi Susu Literan Rp55.000", persona Rina/Bayu/Sari/Dimas/…, komentar, jumlah like,
  "RONDE n", batang laporan (tanpa angka), nama file `ide_kopi_literan.pdf` — berlabel ILUSTRASI/CONTOH. Tidak ada % beli, tidak ada janji.

## Naskah (dikirim ke ElevenLabs, voice Dakocan, eleven_v4, **tanpa --tags** → auto tag klien)
Tag yang benar-benar dipakai (dari `assets/audio/vo.json`): `[playful] [excited]` di semua baris + `[confident]` di CTA.
[playful] [excited] Sebelum stok barang atau bayar iklan, lempar dulu idemu ke warga AI.
[playful] [excited] Namanya MiroFish, open source, puluhan ribu bintang di GitHub.
[playful] [excited] Kamu unggah dokumen idemu, dia bangun kota digital berisi ribuan warga AI.
[playful] [excited] Tiap warga punya kepribadian, ingatan, dan cara bersikap sendiri.
[playful] [excited] Lalu mereka posting, debat, dan saling balas di media sosial tiruan.
[playful] [excited] Contoh: kopi susu literan, lima puluh lima ribu. Ada yang bilang kemahalan, ada yang tanya awetnya.
[playful] [excited] Hasilnya laporan, plus kamu bisa ngobrol langsung sama satu warganya.
[playful] [excited] Pasangnya minta Claude Code, kamu tinggal isi API key.
[playful] [excited] Ingat, ini simulasi, bukan ramalan.
[playful] [excited] [confident] Komen ide, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt` (99 kata, 10 baris). `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py
production/vo_lines.txt assets/audio/vo.mp3` → **take 1 (satu-satunya), 38,88 dtk file**. Caption: "lima puluh lima ribu" → **Rp55 ribu.**,
"Claude Code," dan "API key." satu kotak (MERGE di `tools/timing.py`), "ide," → **IDE,**.
Cek dengar faster-whisper `small` + `medium` (bahasa id, seluruh take): semua baris lengkap & berurutan, semua kata Indonesia benar di
kedua model ("stok/stock barang", "lempar dulu idemu", "puluhan ribu bintang", "unggah dokumen", "kota digital", "kepribadian"
(small: "keperibadian"), "saling balas", "kopi susu literan 55 ribu", "kemahalan", "awetnya", "ngobrol langsung", "isi API key",
"simulasi, bukan ramalan", "Komen ide, aku kirim lewat DM"). Nama merek: "Mirofish" (benar), "GitHub" (benar), Claude Code ditulis
"plot code" (small) / "cloud code" (medium) = penulisan fonetik nama merek, ucapan benar → tidak perlu take ulang. Tidak ada kata yang
dihindari ("pembukaan", "penyedia", "calon mitra", "rahasia").
