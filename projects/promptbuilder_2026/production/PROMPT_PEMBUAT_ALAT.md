# Prompt pembuat alat — "Penyusun Master Prompt" (untuk dikirim via DM ke yang komen MASTER)

Cara pakai: buka Claude → tempel prompt di bawah → Claude bikin aplikasi kecil (artifact) di chat → ketik ide singkat → salin master prompt-nya.

---

Buatkan saya aplikasi web kecil bernama "Penyusun Master Prompt" sebagai artifact interaktif (satu file, tanpa login, tanpa API, berjalan langsung di chat).

Fungsi:
1. Ada satu kolom besar "Ide singkat kamu" (contoh placeholder: "rencana konten seminggu buat kedai kopi").
2. Ada pilihan opsional: Platform (Instagram, TikTok, YouTube, Umum), Gaya bahasa (santai, profesional, persuasif), Panjang hasil (singkat, sedang, detail).
3. Tombol "Susun master prompt".
4. Saat tombol ditekan, aplikasi menyusun MASTER PROMPT lengkap dalam bahasa Indonesia dengan 6 bagian berlabel jelas:
   - PERAN: siapa AI harus berperan (pilih peran ahli yang paling cocok dengan ide).
   - KONTEKS: latar belakang, target audiens, dan tujuan yang bisa disimpulkan dari ide.
   - TUGAS: apa yang harus dikerjakan, dipecah jadi langkah yang jelas.
   - FORMAT: bentuk hasil (tabel, poin, naskah, dll.) dan panjangnya.
   - CONTOH: satu contoh singkat hasil yang diharapkan.
   - BATASAN: hal yang harus dihindari (klaim berlebihan, jargon, info yang tidak bisa dicek) dan pertanyaan yang harus AI tanyakan dulu kalau informasinya kurang.
5. Tampilkan hasilnya di kotak yang rapi, dengan tombol "Salin" dan tombol "Susun ulang".
6. Susun bagian-bagian itu dengan logika di dalam aplikasi (template + aturan sederhana berdasarkan kata kunci ide, platform, gaya, panjang), jadi tetap jalan tanpa koneksi ke AI mana pun.

Tampilan: bersih dan modern, latar terang, satu kolom, tombol besar, nyaman dipakai di HP.
