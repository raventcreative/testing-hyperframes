---
tags: [aipreneur, reel, remake, hyperframes, claude]
date: 2026-11-10
project: projects/bankanim_2026
---
# Reel: Bank animasi bikinan Claude (remake)

- **Referensi**: "Lo que se puede hacer con Claude es una locura" (51 s, talking head + rekaman layar, CTA "comenta GUIA").
- **Versi kita**: faceless (maskot host + robot AI PRENEUR), 29,2 s, background terang + grid bergerak, teks gradient navy, CTA **Komen EDIT**.
- **Hook (A)**: "Video ini nggak diedit di After Effects. Semuanya dibikin pake Claude." — klaim benar (video ini memang dibikin pakai kode lewat Claude).
- **Klaim yang dibuang**: "+30 brand" dari referensi (gak bisa diverifikasi). Teks contoh postingan dibuat netral ("Data kamu, gaya kamu.").
- **Aset**: 12 micro-animasi dikode sendiri (`vendor/microanim.js`), ikon lucide (ISC), logo Claude dari lobehub (MIT). Tanpa aset AI, tanpa foto orang.

## Alur scene + transisi (baru, jangan diulang persis)
1. s01 — timeline editor generik, klip berjatuhan → jendela kode ngetik → stempel chip Claude.
2. s02 — kode "compile" (scan + glow) → kilatan → 12 kartu meledak ke GRID.
3. s03 — grid rebah jadi meja 3D, kartu yang disebut naik 1,9× ke tengah tepat di katanya.
4. s04 — gelombang mulus + panel "Kurva easing" (linear → ease-in-out) yang muterin kartu grafik 360°.
5. s05 — grid jadi dock → kursor klik Copy ("Tersalin ✓") → terminal "Claude Code" (prompt diketik seirama keyboard hologram robot) → kartu baru lahir & mendarat.
6. s06 — inspector live (Teks "98%" → "Rp 25 jt", data 5 kolom, warna) → kartu masuk ke frame postingan.
7. s07 — dialog "Install aplikasi 2,4 GB" & graph editor penuh keyframe distempel "GAK PERLU".
8. s08 — 12 kartu masuk folder "Paket lengkap" → kolom komen "EDIT" → pesawat kertas → DM "terkirim" → logo besar.

## Pelajaran teknis
- **Kontrak GRID**: tiap scene mulai & selesai di posisi grid yang sama; kartu digambar dari waktu global → potongan scene mulus tanpa loncat.
- ID kartu `sXX-c<n>` dari `MicroAnim.grid` bisa bentrok dengan id lain → hindari pola itu di elemen lain.
- `z-index` pada kartu yang di-lift sempat bikin kartu hilang → pakai urutan DOM.
- Render chunk yang udah final bisa jalan duluan sambil nunggu scene lain (CHUNKS=0,2).

Output: `projects/bankanim_2026/out/BANKANIM_Remake_PREVIEW.mp4` (lokal, di-ignore git) · cover `thumbnail/COVER_BANKANIM_1080x1920.png`.

## v2 (revisi klien: "jelasin semua, kasih contoh tiap animasi")
- VO baru dari klien (58,3 s) → reel 59,6 s. 12 **ronde**: tiap animasi diangkat dari strip, dikasih nama, nomor "animasi k dari 12", lalu **CONTOH PEMAKAIAN** (UI generik) yang jalan pas katanya, terus terbang balik ke chip-nya (✓).
- **Strip persisten** (`compositions/strip.html`): 12 chip di bawah logo, counter "k / 12"; setelah ronde 12 strip mekar balik jadi GRID → s05.
- **Round kit** (`r1.html`) disalin persis ke r2–r12 → konsisten. `vendor/rounds.js` = sumber waktu tiap ronde.
- Bug yang ketemu: angka "10.000" via GSAP textContent jadi "10" (fix U+2060); s08 cari kata "kirim" ketemu yang di r10 → posisi negatif → GSAP menggeser seluruh timeline (30 s!). **Cari kata selalu mulai dari awal scene.**
- Kartu besar & chip tampil bareng 1 frame di akhir ronde → durasi terbang balik 0,36 → 0,34 s.
Output: `out/BANKANIM_v2.mp4`.
