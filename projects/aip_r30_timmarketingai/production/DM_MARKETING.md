# DM · MARKETING — Blueprint tim marketing AI (3 modul + aturan setujui + ringkasan pagi)
Halo! Ini blueprint dari reel "tim marketing AI, kamu bosnya". Isinya cara menyusun alurnya + prompt siap copy-paste.
Bisa dijalankan di Claude Code (otomatis, tersambung ke alatmu) atau manual di Claude / ChatGPT (copy-paste per modul).
Catatan jujur: hasil AI itu DRAF. Kamu tetap cek fakta, harga, dan janji di setiap postingan. Blueprint ini tidak menjanjikan
angka penjualan — tujuannya memindahkan kerjaan berulang ke AI supaya kamu fokus ke brand dan budget.

---

## 0. Peta besar (1 putaran = 1 minggu)
```
MODUL 1  Riset & konten     → tren + pertanyaan pembeli → draf postingan, caption, email
   ↓  (KAMU SETUJUI dulu — aturan nomor 1)
MODUL 2  Kreatif & distribusi → gambar/video + suara → jadwal posting → balas komentar (yang sensitif ke kamu)
   ↓
MODUL 3  Putaran analitik    → postingan mana yang bawa chat, booking, penjualan → balik jadi bahan MODUL 1
   ↻
TIAP PAGI: 1 halaman ringkasan (yang berhasil · yang sudah booking · langkah berikutnya)
```

## 1. Brand brief (isi sekali, simpan sebagai `brand.md` — semua modul membacanya)
```
BRAND BRIEF
- Bisnis: [nama + 1 kalimat, mis. kedai kopi susu di Bandung]
- Pembeli utama: [siapa, umur, kebiasaan, di mana mereka nongkrong online]
- Produk/menu andalan + harga: [daftar singkat]
- Gaya bahasa: [santai/akrab, pakai "kak"? emoji boleh/tidak? kata yang DILARANG]
- Bukti yang benar-benar ada: [testimoni asli, rating, sertifikat] — AI dilarang mengarang bukti
- Penawaran minggu ini: [promo + batas waktu, atau "tidak ada"]
- Channel: [Instagram / TikTok / WhatsApp Business / email]
- Topik SENSITIF (wajib diteruskan ke pemilik): komplain, refund/uang kembali, pesanan salah, alergi/kesehatan, ancaman, media
```

## 2. MODUL 1 — Riset & konten (prompt)
```
Kamu tim riset & konten untuk bisnis di brand.md.
1) Cari 5 tren/topik yang sedang ramai dan RELEVAN untuk pembeli kami minggu ini (sebut sumber/linknya; kalau tidak bisa
   mengecek web, tulis "perlu dicek" dan jangan mengarang).
2) Dari daftar pertanyaan pembeli ini: [tempel 10–30 DM/komentar terakhir], kelompokkan jadi 5 pertanyaan yang paling sering.
3) Tulis untuk 7 hari: 7 draf postingan (hook ≤ 10 kata + isi + CTA), 7 caption, dan 1 email/broadcast WhatsApp.
   Setiap draf harus menjawab satu tren ATAU satu pertanyaan pembeli. Gaya bahasa sesuai brand.md.
Output tabel: Hari | Topik | Sumber (tren/pertanyaan) | Hook | Caption | Format (foto/carousel/reels).
Tandai [CEK] di setiap klaim yang butuh verifikasi.
```

## 3. Aturan nomor 1 — gerbang SETUJUI
- Tidak ada postingan/email/balasan publik yang tayang sebelum kamu tulis "SETUJUI" di draf itu.
- Di Claude Code: simpan draf di folder `draf/`; hanya file yang kamu pindah ke `disetujui/` yang boleh dijadwalkan.
- Checklist 30 detik sebelum setuju: fakta & harga benar? janji yang bisa dibuktikan? sesuai gaya brand? ada nama/foto orang lain (izin)?

## 4. MODUL 2 — Kreatif & distribusi (prompt + alat)
```
Untuk setiap draf di folder disetujui/:
1) Tulis brief visual: 1 gambar (rasio 4:5) dan 1 video pendek (9:16, 5–8 detik) — subjek, suasana, warna brand, teks di layar ≤ 6 kata.
2) Tulis naskah suara 15–20 detik untuk reels (bahasa santai, sebut CTA di akhir).
3) Buat jadwal posting minggu ini per channel (jam ramai pembeli kami: [isi]).
4) Siapkan 10 contoh balasan komentar dengan gaya bahasa brand.md untuk pertanyaan yang paling sering.
ATURAN: komentar/DM yang menyentuh topik SENSITIF di brand.md TIDAK dibalas AI — tandai "TERUSKAN KE PEMILIK" + ringkas masalahnya.
```
- Gambar & video: Higgsfield (platform AI gambar & video). Suara: ElevenLabs (text-to-speech, mendukung bahasa Indonesia).
  Cek syarat lisensi/komersial di paket masing-masing sebelum dipakai untuk iklan.
- Jadwal & balas otomatis: pakai fitur penjadwal resmi tiap platform atau alat penjadwal yang kamu pakai; hubungkan ke Claude Code
  hanya lewat konektor/API resmi. Mulai dengan mode "AI menyiapkan, kamu yang klik kirim" selama 2 minggu pertama.

## 5. MODUL 3 — Putaran analitik (prompt)
```
Ini data postingan minggu ini: [tempel/ekspor: judul, format, jangkauan, likes, komentar, DM/chat masuk, booking, penjualan per postingan].
1) Ranking postingan berdasarkan chat + booking + penjualan (BUKAN likes). Likes hanya jadi info tambahan.
2) Untuk 2 teratas: kenapa kira-kira berhasil (topik, hook, format, jam)? Untuk 2 terbawah: apa yang beda?
3) Tulis 3 keputusan untuk minggu depan: perbanyak apa, kurangi apa, tes apa (1 tes saja).
4) Simpan ringkasan ini sebagai `belajar_minggu_ini.md` — MODUL 1 wajib membacanya sebelum menulis draf minggu depan.
```
Tips: tanya pembeli "tahu kami dari postingan mana?" dan catat di kolom sumber — itu cara paling sederhana menghubungkan postingan ke penjualan.

## 6. Claude Code sebagai mesinnya (opsional, untuk yang mau otomatis)
- Satu folder proyek: `brand.md`, `draf/`, `disetujui/`, `data/`, `belajar_minggu_ini.md`, `ringkasan_pagi/`.
- Sambungkan alat lewat konektor MCP (Claude Code mendukung Model Context Protocol untuk tools, database, dan API — lihat
  dokumentasi resmi: code.claude.com/docs/en/mcp): data pelanggan (CRM/spreadsheet), kalender/booking, akun sosmed/penjadwal.
- Prompt pembuka:
```
Baca brand.md. Jalankan MODUL 1 untuk minggu ini dan simpan draf di draf/. Jangan menjadwalkan atau mengirim apa pun.
Setelah aku memindahkan file ke disetujui/, jalankan MODUL 2. Setiap Senin pagi jalankan MODUL 3 dari data/ dan perbarui belajar_minggu_ini.md.
Untuk semua aksi yang mengirim/memposting/mengubah data: minta persetujuanku dulu.
```

## 7. Ringkasan pagi — 1 halaman (prompt)
```
Buat ringkasan pagi maksimal 1 halaman dari data kemarin:
1. Yang berhasil (1–3 postingan/ide, dengan alasan: chat/booking/penjualan)
2. Yang sudah booking/pesan hari ini (nama/jam dari kalender — tanpa data sensitif)
3. Langkah berikutnya (maks 3: draf yang menunggu SETUJUI, komentar sensitif yang perlu kamu jawab, satu tes kecil)
Tanpa jargon, tanpa angka yang tidak ada di data.
```

## 8. Prinsipnya
AI memindahkan informasi: dari tren ke draf, dari draf ke jadwal, dari data ke keputusan. **Brand dan budget tetap kamu yang pegang** —
kamu yang setujui isi, nada, promo, dan berapa uang iklan yang keluar.

Ada yang mau ditanyakan soal setup-nya? Balas DM ini aja. — AI PRENEUR
