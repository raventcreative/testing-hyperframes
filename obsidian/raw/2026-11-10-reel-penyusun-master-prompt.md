---
tags: [aipreneur, reel, remake, hyperframes, elevenlabs, batch, claude]
date: 2026-11-10
project: projects/promptbuilder_2026
---
# Reel: Stop beli prompt — bikin alat penyusun prompt sendiri · TERANG

- **Referensi**: "Masih beli prompt?" (bikin prompt builder pakai Gemini).
- **Versi kita**: faceless (maskot + robot), 45,2 s, background terang + grid bergerak, teks gradient navy, CTA **Komen MASTER** (DM: `production/PROMPT_PEMBUAT_ALAT.md`, prompt yang bikin aplikasi kecil di chat Claude).
- **Ganti dari referensi**: Gemini → Claude (artifact di chat), langkah dibikin generik, tanpa nama model. Harga di s01/s10 = contoh generik (Rp 499.000, Rp 1,2 jt, Rp 2,5 jt), bukan produk asli.
- **Anatomi prompt kita**: 6 blok puzzle berwarna (PERAN, KONTEKS, TUGAS, FORMAT, CONTOH, BATASAN) + rail 5 langkah.

## Alur scene + transisi
1. s01 — toko prompt (2 pack + tiket kelas, keranjang Rp 4.199.000) → stempel STOP → harga dicoret → produk meledak jadi 6 blok masuk mesin "Penyusun Prompt" → segel "Rp 0 · GRATIS" → mesin flip.
2. s02 — dokumen prompt kosong flip masuk, tiap blok jatuh ke slotnya tepat di namanya.
3. s03 — dokumen morph jadi planner seminggu, blok ditulis ulang tiap hari (counter 30×), tumpukan runtuh di "capek."
4. s04 — chip Claude mendarat, blok berpusar jadi alat, tombol nembak 5 titik jadi rail langkah.
5. r1–r5 — jendela chat Claude: buka → tempel prompt (Ctrl+V, 217 kata) → Claude bikin aplikasinya (skeleton → UI) → ketik "rencana konten seminggu buat kedai kopi" per huruf (sinkron robot) → master prompt 6 bagian → "Tersalin ✓".
6. s10 — blok terbang ke kartu alat, tiket kelas disobek, pack prompt di-X & diremas, stiker "Rp 0 · gratis".
7. s11 — kartu alat flip jadi "Prompt pembuat alat", komen MASTER per huruf, hati, pesawat ke DM "terkirim", logo besar.

## Pelajaran teknis
- **RAIL SPEC** pixel-exact di brief (posisi titik, warna tiap state) → 2 agen beda bisa bikin s04 & r1 yang nyambung 0 pixel beda.
- Agen r1–r5 bikin semua scene dari satu kit + generator (`gen.py`) → konsisten; ubah kit, generate ulang.
- Pointer akhir r5 dipindah → s10 (agen lain) harus diupdate: **tiap perubahan end state wajib dikabarin ke pemilik scene berikutnya**.
Output: `out/PROMPTBUILDER_1080x1920.mp4` · cover `thumbnail/COVER_PROMPTBUILDER_1080x1920.png`.
