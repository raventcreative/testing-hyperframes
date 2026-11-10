---
tags: [aipreneur, reel, remake, hyperframes, elevenlabs, batch]
date: 2026-11-10
project: projects/lamarankerja_2026
---
# Reel: Lamaran jalan pas kamu tidur (InstaJob remake) · NAVY

- **Referensi**: "Cari kerja sambil tidur" (talking head + rekaman layar).
- **Versi kita**: faceless (maskot host tidur, robot AI PRENEUR kerja shift malam), 32,9 s, background navy, teks putih + cyan, CTA **Komen KERJA**.
- **VO**: ElevenLabs Eleven v4 otomatis (voice klien, stability 41 %, similarity 75 %, tag [playful] / [excited]) dari `production/VO_SCRIPT.md` → `tools/vo_from_script.py`.
- **Hook**: "Kamu lagi tidur, tapi CV-mu lagi keliling ke banyak kantor."
- **Fakta**: fitur dari situs resmi InstaJob (cari lowongan, kirim lamaran otomatis, email + LinkedIn/Glints/Jobstreet/Indeed, atur posisi/lokasi/mode/batas per hari, bisa dimatikan). **Klaim volume lamaran dari marketing mereka dibuang** (gak bisa dicek). Nama platform cuma TEKS, tanpa logo.
- **Aset**: ikon lucide (ISC), semua UI digambar sendiri. Tanpa aset AI, tanpa foto orang.

## Alur scene + transisi
1. s01 — malam: jam flip 02:00→02:01, Zzz dari host yang tidur, CV pop, pesawat kertas terbang ke skyline, jendela kantor nyala. Jam minggir pas CV muncul.
2. s02 — skyline melipat jadi garis horizon → jadi tepi jendela app "InstaJob" → feed lowongan discan (sinkron scan robot), 3 cocok dicentang di "pas," → terkirim otomatis (pesawat + toast) → kamera nyelam ke CV.
3. s03 — hub routing: CV di tengah, email + 4 channel nyala satu-satu di katanya, jalur titik mengalir → semua imploded balik ke CV.
4. s04 — CV flip → panel Preferensi: posisi & lokasi diketik, mode kerja → Remote, slider 5 → 30/hari, "Tersimpan ✓".
5. s05 — garis cahaya buka panel "Auto apply" → switch OFF di "matiin", aliran berhenti, chip "Dijeda" → mati ala CRT.
6. s06 — jam balik, time-lapse ke 07:00 (layer langit jadi fajar, matahari naik), undangan wawancara, chip "Kamu" turun ke host, CV dirapiin (3 centang + kilau).
7. s07 — kartu "Tutorial lengkap", kolom komen "KERJA" diketik besar, hati, pesawat ke DM "terkirim ✓", logo besar di bawah matahari.

## Pelajaran teknis
- **Layer langit persisten** (`compositions/sky.html`, hf-seek): bintang, bulan sabit (mask radial-gradient), fajar di s06 → kontinuitas cerita malam → pagi tanpa tiap scene gambar ulang.
- Kejadian di hook: kartu CV nutupin jam → **cek frame hook full-res**, tiap elemen hero harus punya ruang sendiri.
- Logo pojok + logo end card = dobel → fade logo pojok sebelum end card.
- Maskot "bangun" kecepetan 0,15 s → wake dimulai `kata − 0,18 s`.
- Preview server background mati setelah 30 menit (batas default) → jalankan dengan timeout panjang; proses preview biasanya tetap hidup.

Output: `projects/lamarankerja_2026/out/LAMARANKERJA_1080x1920.mp4` (lokal, di-ignore git) · cover `thumbnail/COVER_LAMARANKERJA_1080x1920.png`.
