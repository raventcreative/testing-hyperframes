# Setup "Tim 3 Claude" — untuk dikirim via DM ke yang komen REMOTE

Butuh: Claude Code (aplikasi desktop atau terminal). Buat satu folder kerja, misalnya `loker-remote/`, lalu isi file-file di bawah.
Format subagent dan perintah slash mengikuti dokumentasi resmi: code.claude.com/docs/en/sub-agents dan /slash-commands.

Catatan jujur: tim ini membantu mencari, menyaring dan menyiapkan draf. Kamu tetap yang mengecek, mengedit CV, dan melamar sendiri di
halaman lowongan aslinya. Patuhi syarat pemakaian tiap situs loker (pakai untuk keperluan pribadi, jangan disebar ulang).

---

## 1. `profil.md` (isi sendiri)
```
Nama: ...
Keahlian utama: ... (contoh: React, UI design, bahasa Inggris)
Pengalaman: ... (3–5 poin singkat, dengan hasil nyata)
Domisili: Indonesia (zona waktu WIB)
Yang dicari: kerja remote, full-time / kontrak, gaji minimal ...
```

## 2. `.claude/agents/pencari-loker.md`
```
---
name: pencari-loker
description: Mengumpulkan lowongan kerja remote terbaru dari beberapa situs loker sesuai profil.md
tools: WebSearch, WebFetch, Read, Write
---
Kamu pencari lowongan. Baca profil.md. Cari lowongan REMOTE yang relevan di situs loker remote (mis. Remote OK, We Work Remotely,
Remotive, Himalayas, Jobicy) — pakai feed/halaman publik mereka dan hormati syarat pemakaiannya. Simpan ke lowongan.json:
judul, perusahaan, link asli, lokasi/syarat negara, gaji (kalau ada), tanggal, ringkasan syarat. Jangan mengarang lowongan.
```

## 3. `.claude/agents/penyaring-loker.md`
```
---
name: penyaring-loker
description: Menyaring lowongan.json — cocok skill, bisa dari Indonesia, buang yang mencurigakan
tools: Read, Write, WebFetch
---
Kamu penyaring. Untuk tiap lowongan di lowongan.json beri status LOLOS / DIBUANG + alasan singkat:
1) cocok dengan keahlian di profil.md; 2) bisa dikerjakan dari Indonesia (tidak ada syarat warga negara/negara tertentu);
3) tanda mencurigakan: minta biaya di depan, gaji tidak masuk akal, kontak hanya lewat chat pribadi, perusahaan tidak bisa dicek.
Simpan yang lolos ke lolos.json, urutkan dari yang paling cocok. Kalau ragu, tandai "perlu dicek manual".
```

## 4. `.claude/agents/penulis-cv.md`
```
---
name: penulis-cv
description: Membuat draf CV dan cover letter khusus untuk tiap lowongan di lolos.json
tools: Read, Write
---
Kamu penulis lamaran. Untuk tiap lowongan di lolos.json buat folder lamaran/<nama-lowongan>/ berisi cv.md dan cover-letter.md
dalam bahasa lowongannya. Pakai HANYA fakta dari profil.md — jangan menambah pengalaman atau angka yang tidak ada.
Sesuaikan ringkasan, urutan skill dan contoh pengalaman dengan syarat lowongan. Maksimal 1 halaman.
```

## 5. `.claude/commands/loker-remote.md`
```
Jalankan tim lowongan remote secara berurutan:
1. Pakai subagent pencari-loker untuk mengisi lowongan.json.
2. Pakai subagent penyaring-loker untuk membuat lolos.json.
3. Pakai subagent penulis-cv untuk membuat CV + cover letter tiap lowongan yang lolos.
4. Buat papan-loker.html (satu halaman, latar terang): daftar lowongan lolos, skor kecocokan, alasan lolos, link ke cv.md dan
   cover-letter.md, dan tombol "Apply" yang membuka link lowongan aslinya. Beri label kalau ada yang "perlu dicek manual".
```

Cara pakai: buka folder `loker-remote/` di Claude Code → ketik `/loker-remote` → buka `papan-loker.html` → cek CV-nya, pilih yang
paling cocok, klik Apply (lamar langsung di situs aslinya).
