# VO — R36 · Peta AI agent untuk jalanin bisnis · tema WHITE · VO 54,2 dtk (video 55,5 dtk, VO mulai 0,3 dtk)
Referensi: batch 9 · `projects/aip_remake_batch9/refs/ref1.mp4` (51,2 dtk, bahasa Inggris, kreator lain: satu poster/peta besar
"137 AI agents" yang di-zoom bagian per bagian). Format visual = "ref2 look" (teknik saja dari ref2): reel 2D bersih di plate brand,
satu ide per beat, headline = kalimat yang diucapkan (satu kata miring + aksen), satu kartu/diagram di tengah, host kecil kiri bawah,
penghitung beat "07 / 24" kanan bawah, tombol pil CTA di akhir. TANPA dunia voxel (permintaan klien).

## Naskah final (production/vo_lines.txt — satu take ElevenLabs utuh, Dakocan, eleven_v4, auto tags)
1. Ini peta semua AI agent buat jalanin satu bisnis.
2. Tiga puluh agent, dan petanya gratis buat kamu.
3. Mulainya dari yang udah kamu pakai: WhatsApp, Instagram, marketplace, Google Sheets, kalender, email.
4. Claude di tengah, membaca semuanya.
5. Dari situ, tumbuh tujuh departemen.
6. Penjualan: cari calon pembeli, kirim chat pertama, atur janji temu.
7. Closing: kirim penawaran, lalu follow-up sampai ada jawaban.
8. Marketing: tulis konten, balas tiap komentar.
9. CS: jawab pelanggan, tandai yang mulai menghilang.
10. Operasional: urus pesanan dan jadwal tim.
11. Admin dan keuangan: kirim tagihan, ingetin yang belum bayar.
12. Analis: kenali calon klien sebelum kamu ketemu.
13. Tiap agent cuma pegang satu tugas, alurnya ditulis jelas.
14. Nggak ada yang dikirim ke pelanggan sebelum kamu setuju.
15. Tiap pagi, kamu dapat satu halaman: apa yang beres, apa yang nunggu kamu.
16. Komen peta, aku kirim peta lengkapnya lewat DM.

## ATM: what we changed
**Amati** — strukturnya berguna: input yang sudah dipakai → Claude di tengah membaca → departemen tumbuh → tiap departemen
mengerjakan apa → tiap agent satu tugas + alur tertulis → tidak ada yang sampai ke klien sebelum disetujui → satu halaman tiap pagi.
**Tiru** — urutan ide itu (inti materinya) + metafora "peta".
**Modifikasi**:
1. **Angka jujur** — referensi mengklaim "137 agent"; kita bangun petanya sendiri (`DM_PETA.md`: 7 departemen → 30 agent bernama,
   satu kalimat tugas masing-masing) dan VO menyebut **30** — angka yang benar-benar dikirim lewat DM.
2. **Input untuk pebisnis Indonesia** — WhatsApp, Instagram, marketplace, Google Sheets, kalender, email (referensi: inbox/CRM/
   calendar/books). Departemen kita: Penjualan, Closing, Marketing, CS, Operasional, Admin & Keuangan, Analis.
3. **Contoh sendiri** (semua berlabel CONTOH): usaha katering harian untuk kantor — prospek kantor konsultan/klinik gigi/coworking,
   chat pertama, janji temu Kamis 10.00, penawaran PDF, follow-up H+1/H+3, konten menu, komentar, kanban pesanan, tagihan INV-0117,
   pengingat INV-0109, brief klien. Vertical baru (bukan yang dilarang/baru dipakai).
4. **Through-line** — pengingat yang ditulis agent "Pengingat Bayar" (beat 16) adalah agent yang dipilih di beat "satu tugas",
   alur kerjanya yang ditulis, dan pesan yang tertahan di gerbang persetujuan lalu lolos setelah "Setujui" diklik.
5. **Rekaman asli klien** — beat "Claude di tengah" memakai rekaman claude.ai milik klien (brand/rec/claude_code_chrome_2026-10-30.mp4,
   16,6 dtk, crop 680×220 di (745,430): "What's on today, FREDDIE KASHAWAN?" + kotak prompt; sidebar berisi judul chat pribadi
   TIDAK ikut). Jendela itu menyusut menjadi simpul tengah peta (shared element). File turunan di assets/rec/ (gitignored).
6. **Tanpa "jam tujuh"** di VO (layar ringkasan pagi menulis "Senin · 07.00" sebagai contoh).
- **Dibuang**: nama/brand pembuat referensi (SkillTree), logo HubSpot/Slack/QuickBooks, angka "137", "$184k", "212 tickets", poster
  mereka. Referensi berbahasa Inggris; tidak ada >3 kata berurutan yang sama.

## Fakta / klaim
- Tidak ada klaim hasil/penghasilan. Peta = cetak biru; DM menulis bahwa kemampuan integrasi tergantung connector/akses akun.
- Logo hanya dari Simple Icons 16.38.0 (CC0) → 3D extrude (lihat asset_credits.json). Marketplace = ikon toko generik (Lucide), bukan brand.

## Listen-check (faster-whisper small + medium, sebelum build)
- Take 1: "aku kasih" → "apukasi/apokasi" dan "Riset" → "Reset" di KEDUA model → diganti "dan petanya gratis buat kamu" dan
  "Analis: kenali calon klien sebelum kamu ketemu"; take 2 = final (seluruh take digenerate ulang, tidak ada potongan).
- Take 2 medium: hanya format/nama — "Tiga puluh"→"30", "tujuh"→"7", "follow-up"→"follow up", "Claude"→"Cloud" (nama Inggris
  dibaca benar; sama seperti R20/R34). Small salah dengar "chat/jawab/tandai/jadwal/Analis" tapi medium benar → tidak diubah
  (aturan: ubah hanya yang salah di kedua model).
- Cek final di MP4: lihat `production/VO_CHECK.md`.

## Teknik yang dipakai (teknik saja; client format menang bila bentrok)
1. **html-demo** — setiap kartu digambar sebagai fungsi murni dari waktu (View(t)): kotak cari mengetik, baris prospek masuk, chat
   mengetik ~95 karakter/dtk, slot kalender terkunci, kursor glide 0,6 dtk → tekan 0,17 dtk pada "Setujui" (target diukur dari DOM),
   hasil muncul dengan state kerja → hasil → settle.
2. **product-launch-film** — shared-element: jendela claude.ai → simpul tengah; tile input → terserap ke simpul; pil "Penjualan"
   → kartu departemen (morph rect); kartu Analis → kembali jadi pilnya di peta; titik agent → kartu tugas → dokumen alur kerja;
   halaman pagi → dokumen peta di CTA. Pegas closed-form (overshoot kecil), satu gerak kamera per scene (push 0,96→1,03).
3. **beat-promo-film / technique bank** — setiap beat berubah pada kata VO (24 beat, rata-rata 2,3 dtk), tidak ada hold > ~1 dtk;
   3-subframe motion blur (ghost t±1/90 dtk) pada tile/pesan yang terbang; blur kecepatan pada whip kartu.
4. **Through-line / guide object** — PETA itu sendiri (hook → 7 departemen → mini-map di tiap kartu departemen dengan titik aktif →
   kembali ke peta saat "satu tugas" → dokumen "Peta AI agent" di CTA).
5. **Transisi bervariasi** — morph, whip kiri, flip, zoom-through, whip kanan, drop/rise, flip, morph balik;
   tidak ada gerak yang sama dua kali berurutan.
6. Host = maskot 3D klien (utuh, kiri bawah), satu intent per beat, tangan bergantian kiri/kanan, CTA pada "Komen"; lip sync dari VO.
