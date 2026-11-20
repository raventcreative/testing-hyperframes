# DM — kata kunci IDE (R27 · Tes ide produk ke warga AI dulu)

Halo! Ini panduan setup **MiroFish** yang kamu minta + prompt Claude Code-nya. 🙌

---

## 1. Apa itu MiroFish (singkat & jujur)
- Repo: https://github.com/666ghj/MiroFish — open source, lisensi **AGPL-3.0**.
- Kamu unggah "bahan awal" (dokumen idemu) + tulis pertanyaanmu pakai bahasa biasa. MiroFish membangun dunia simulasi berisi
  agen AI dengan kepribadian & ingatan masing-masing, menjalankannya di **dua medsos tiruan**, lalu memberi **laporan** — dan kamu
  bisa **ngobrol dengan agen mana pun** di dalamnya.
- Ini **simulasi, bukan ramalan.** Pakai untuk menemukan keberatan & pertanyaan yang mungkin muncul, lalu buktikan ke pembeli asli.

## 2. Yang perlu kamu siapkan
- Laptop/PC dengan **Node.js 18+**, **Python 3.11 atau 3.12**, dan **uv** (Claude Code bisa bantu cek & pasang).
- **LLM API key** — API apa saja yang formatnya kompatibel OpenAI SDK (README mencontohkan Qwen-plus). Ini **berbayar sesuai pemakaian.**
- **Zep API key** (https://app.getzep.com/) — untuk memori agen; menurut README kuota gratis bulanannya cukup untuk pemakaian sederhana.
- Claude Code (https://code.claude.com/docs/en/overview).

## 3. Prompt untuk Claude Code (copy-paste)
Buka terminal di folder kosong, jalankan `claude`, lalu tempel:

```
Tolong setup MiroFish dari https://github.com/666ghj/MiroFish di laptop ini.
1. Baca README-nya dulu, cek Node.js 18+, Python 3.11/3.12, dan uv. Kalau ada yang belum terpasang, jelaskan dulu caranya sebelum memasang.
2. Clone repo-nya, lalu jalankan `npm run setup:all`.
3. Salin `.env.example` jadi `.env`, tapi JANGAN isi API key — biar aku isi sendiri (LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_NAME, ZEP_API_KEY).
4. Setelah aku bilang "key sudah diisi", jalankan `npm run dev` dan kasih tahu alamatnya (frontend localhost:3000).
5. Minta izin aku dulu setiap kali mau menjalankan perintah yang memasang sesuatu atau menghapus file.
```

Alternatif tanpa Node/Python: README juga menyediakan Docker (`cp .env.example .env` lalu `docker compose up -d`).

## 4. Cara menguji ide produkmu (contoh: kopi susu literan)
Buat satu dokumen (PDF/teks) sebagai bahan awal, isinya:
- **Produk:** apa, ukuran, harga (mis. 1 liter Rp55.000), cara beli & kirim.
- **Target pembeli:** siapa, kota, kebiasaan belanja (mis. karyawan Jabodetabek yang beli online).
- **Alternatif yang mereka punya:** (mis. kopi gelasan Rp18–25 ribu, sachet).
- **Kalimat promosi** yang mau kamu pakai di iklan.

Lalu tulis pertanyaan simulasinya, misalnya:
> "Bagaimana reaksi warganet Indonesia kalau produk ini dipromosikan di media sosial? Keberatan apa yang paling sering muncul,
> dan perubahan apa (harga, ukuran, pesan iklan) yang paling mengurangi keberatan itu?"

Tips hemat dari README: **coba simulasi di bawah 40 ronde dulu** (pemakaiannya besar). Setelah laporan keluar, wawancarai 2–3 agen:
"Kenapa ragu beli?", "Harga berapa yang terasa wajar?", "Apa yang bikin kamu mau coba?"

## 5. Setelah simulasi
- Ambil 1–2 keberatan terbesar, ubah tawaranmu (mis. tambah ukuran 500 ml untuk coba, jelaskan daya tahan di kulkas).
- **Tes kecil ke pembeli asli** sebelum stok besar atau iklan besar: pre-order terbatas, tanya 10–20 calon pembeli, atau iklan kecil.
- Ingat: hasil simulasi bergantung pada bahan awal & model AI yang kamu pakai — bukan jaminan penjualan.

## 6. Catatan aman
- Jangan unggah data rahasia/data pelanggan: isinya dikirim ke penyedia model AI yang kamu pilih.
- Simpan API key di file `.env` saja, jangan dibagikan atau di-upload ke GitHub.
- Lisensi AGPL-3.0: kalau kamu mengubah MiroFish lalu menjalankannya sebagai layanan untuk orang lain, ada kewajiban membuka kode
  perubahannya — baca file LICENSE.

Selamat mencoba! Kalau mentok di salah satu langkah, balas DM ini dengan pesan error-nya. 🚀
— AI PRENEUR
