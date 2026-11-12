# VO — Jualan website 3D, 1 prompt jadi · background TERANG · 47,0 dtk VO (video 48,37 dtk)
Referensi: ref3 (≈47 dtk bicara, video 49,7 dtk) — "semua website 3D ini dari satu prompt": library "Motion Sites" berisi 100+ situs 3D,
tiap situs = prompt siap pakai; copy → tempel ke AI (Kimi / Claude) → situs jadi → ganti gambar klien → "jadi dalam satu sore", "bisa
dijual $500", bikin beberapa → portofolio; library berbayar → paket prompt gratis; CTA "comment 3D". Visual referensi: latar krem/peach,
maskot kepiting piksel, cuplikan situs-situs dari library.

## Yang diubah dari referensi
- Visual sepenuhnya milik kita: sistem LIGHT AI PRENEUR (grid animasi, kartu putih, maskot + robot). Contoh website 3D di layar adalah
  desain kita sendiri — tiga UMKM fiktif (Kopi Senja · Langkah sneakers · Roti Bunda), produk melayang digambar sebagai SVG dan
  digerakkan GSAP (goyang 3D dangkal, bayangan, partikel mengorbit) — semua berlabel **CONTOH**. Tidak ada screenshot situs orang lain.
- Jendela library hanya **ilustrasi** (label ILUSTRASI): nama "MotionSites" + alamat teks motionsites.ai, isi grid = ubin abstrak buatan
  kita, bukan desain mereka. Isi prompt yang terlihat ("Buat landing page 3D untuk [nama brand]…") juga contoh tulisan kita.
- Tanpa angka yang tidak bisa dicek: "100+ situs 3D" dihapus (situs resminya sendiri menyebut angka lain, ±500 prompt, dan itu klaim
  sepihak); "jadi dalam satu sore" dihapus (tidak ada janji waktu).
- "$500" diganti: **"Harganya? Tergantung klien dan seberapa besar kerjaannya. Kamu yang tentuin."** — kartu penawaran di layar tanpa
  angka (Rp ??? → coretan pena), daftar scope: jumlah halaman, foto & teks klien, animasi 3D, revisi & domain.
- "cara paling gampang yang pernah kulihat" → ditandai sebagai pendapat: "**Menurutku**, ini cara paling gampang…" (chip "Menurutku…").
- "Kimi atau Claude" → "Claude atau AI lain" (chip model "Claude" + "AI lain", tanpa logo pihak lain).
- Ditambah langkah yang jujur: AI membuat **template** dulu ("Nama Brand", slot "Foto produk"), lalu foto + teks + warna diganti punya
  klien; sudut Indonesia = UMKM (kedai kopi, toko sepatu, toko roti, salon, katering, "usaha kamu?").
- Karena library-nya berbayar, CTA menawarkan paket prompt starter gratis dari Freddie: `production/STARTER_PROMPTS_3D.md`.
  CTA: **"Komen 3D, aku kirim lewat DM."**

## Fakta yang dicek (2026-11-12)
- **MotionSites** (motionsites.ai) = library prompt untuk website animasi / "cinematic 3D"; cara pakainya: pilih desain → copy
  prompt-nya → tempel ke AI builder seperti Lovable, Cursor, Bolt, **Claude**, v0, Replit → sesuaikan → luncurkan. Ada Academy (tutorial,
  termasuk "Build a 3D Scroll-Animated Website with AI": gambar → model 3D → Claude + Three.js).
  Sumber: halaman resmi yang terindeks WebSearch (domain motionsites.ai): https://motionsites.ai/templates ("Official Premium AI
  Website Prompts"), https://motionsites.ai/academy ("Learn Cinematic 3D AI Websites"),
  https://motionsites.ai/lesson/build-3d-scroll-animated-website-with-ai, https://motionsites.ai/unlimited ("Go Unlimited").
- **Berbayar**: akses penuh lewat paket "Go Unlimited" (tingkat tahunan / lifetime) atau paket prompt; hanya sedikit prompt gratis.
  Sumber: https://motionsites.ai/unlimited (via WebSearch) + ulasan pihak ketiga https://www.stork.ai/blog/motionsites-review-2026
  (1 Nov 2026: akun gratis dapat 3 prompt, sisanya perlu plan/pack) dan
  https://www.toolcenter.ai/en/articles/motionsites-review-2026 (Okt 2026). Pembuatnya menurut beberapa sumber: Viktor Oddy (tidak
  disebut di reel). Harga antar-sumber berbeda-beda (promo berubah), jadi **harga tidak
  disebut** di VO maupun layar.
- Catatan: motionsites.ai dan situs ulasannya tidak bisa dibuka langsung dari sandbox ini (DNS diblok); fakta di atas dari cuplikan
  halaman resmi di hasil WebSearch + dua ulasan pihak ketiga yang saling cocok. VO hanya memakai yang konsisten di semua sumber:
  nama, isi (desain website animasi & 3D + prompt-nya), cara pakai (copy → tempel ke Claude / AI lain), dan bahwa library-nya berbayar.

## Naskah (dikirim ke ElevenLabs, voice tersimpan; SETIAP baris diawali tag `[playful] [excited]`)
[playful] [excited] Website 3D kayak gini bisa jadi cuma dari satu prompt.
[playful] [excited] Menurutku, ini cara paling gampang buat mulai jualan jasa website.
[playful] [excited] Ada library namanya MotionSites. Isinya desain website animasi dan 3D, dan tiap desain udah ada prompt-nya.
[playful] [excited] Kamu pilih yang kamu suka, copy prompt-nya, terus tempel ke Claude atau AI lain.
[playful] [excited] Dan AI-nya langsung bikinin websitenya.
[playful] [excited] Terus ganti foto sama teksnya pakai punya klien kamu.
[playful] [excited] Kedai kopi, toko sepatu, toko roti, apa pun usahanya, tampilannya langsung naik kelas.
[playful] [excited] Harganya? Tergantung klien dan seberapa besar kerjaannya. Kamu yang tentuin.
[playful] [excited] Cara mulainya: bikin dua tiga contoh dulu, pamerin, dan itu jadi portofolio kamu.
[playful] [excited] Library-nya berbayar, jadi aku bikinin paket prompt starter gratis buat kamu.
[playful] [excited] Komen 3D, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt`. Audio: `assets/audio/vo.mp3` (+ `assets/audio/vo.json` = waktu per baris + alignment
karakter). Dibuat dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3
--tags "[playful] [excited]"` → 47,12 dtk, 11 baris. Cek ulang dengan faster-whisper `small`: semua kata terucap ("3D" terdengar
dan tertranskrip sebagai "3D"), tag tidak ikut terbaca. Dua kata yang alignment-nya meleset dikoreksi di `tools/timing.py` (TFIX:
"naik kelas." dan "Komen" — dicek terhadap envelope energi + whisper).
