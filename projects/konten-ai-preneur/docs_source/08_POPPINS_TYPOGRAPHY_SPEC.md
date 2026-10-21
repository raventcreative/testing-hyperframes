# AI PRENEUR — LOCKED POPPINS TYPOGRAPHY SYSTEM

**Versi revisi:** campuran Poppins Regular 400 + Poppins Bold 700, sesuai permintaan user. Semua aspek lain dari paket v1 (11 VO, 48 detik, background, logo, warna, storyboard dan transisi) tetap.

## Typeface lock

- Semua teks animasi/UI buatan dalam film: **Poppins** saja. Pakai font face **Regular 400** dan **Bold 700** yang benar. Tidak menggunakan Medium 500, SemiBold 600, ExtraBold 800, font pengganti, atau fake synthetic bold.
- **AI PRENEUR adalah file logo asli**, bukan teks yang ditulis ulang memakai Poppins. Bentuk/logo asli jangan diubah.
- File font **tidak disertakan** dalam paket. Claude Code harus memeriksa ketersediaan versi resmi dan izin pemakaiannya pada Windows; jika diperlukan dan diizinkan, gunakan sumber berlisensi yang terverifikasi, lalu pastikan asset font benar-benar ter-load saat render. Jangan klaim Poppins dipakai jika fallback yang ter-export.
- Untuk stylesheet jika didukung runtime: deklarasi `@font-face` masing-masing weight 400 dan 700, `font-family: 'Poppins', sans-serif`, `font-synthesis: none`; jangan menebak path `.ttf`/`.woff2` sebelum file ada.

## Contrast dan ritme

- **Regular:** kalimat pembuka, konteks, penjelasan, labels yang tidak aktif. Solid `#0a0d2c`.
- **Bold:** klaim inti, kata kunci, result, pay-off, CTA. Gradient `linear-gradient(120deg,#0a0d2c 15%,#294b77 100%)` pada headline, teks tetap mudah dibaca.
- Gunakan perubahan berat font sebagai **dramaturgi**: Regular membangun konteks, Bold menyelesaikan gagasan. Ada jeda baca; jangan bikin tiap huruf lompat/bounce.
- Jaga crop-mask, tracking, baseline, optical alignment dan line wrap berdasarkan **metric Poppins yang sesungguhnya**. Evaluasi minimal frame masuk, settle, keluar tiap scene di preview portrait.

## Per-scene exact weight pairing

| Scene | Poppins Regular 400 | Poppins Bold 700 |
|---|---|---|
| S01 | “BANYAK ORANG BILANG” | “AI HASILNYA MASIH BIASA AJA.” |
| S02 | “PADAHAL MASALAHNYA” | “SERING BUKAN DI AI-NYA.” |
| S03 | “MASALAHNYA ADA DI” | “ARAHAN YANG DIBERIKAN.” |
| S04 | “TAPI HASILNYA MENGIKUTI” | “AI ITU CEPAT.”, “SEBERAPA JELAS BRIEF-NYA.” |
| S05 | “BUKAN CUMA SURUH” | “‘BIKIN YANG KEREN’” |
| S06 | “TAPI MENJELASKAN” dan label kategori tidak aktif | “STYLE”, “RITME”, “KOMPOSISI”, “TRANSISI”, “HIERARKI” saat aktif (ubah penekanan sesuai narasi) |
| S07 | “PROMPT YANG TEPAT” | “MENGUBAH OUTPUT” |
| S08 | “DARI TEKS BIASA” | “JADI MOTION YANG TERLIHAT MAHAL.” |
| S09 | “INILAH CARA” | “AI PRENEUR MENGARAHKAN AI.” |
| S10 | “LEBIH CEPAT.”, “LEBIH TERARAH.” | “LEBIH PREMIUM.” pada final tableau |
| S11 | “AI BISA MEMBUAT” | “MOTION SELEVEL INI.”, “ASAL PROMPT-NYA TEPAT.” |

**QA font PASS:** inspect font asset load and browser computed font face/weight when possible; check exported MP4 keyframes for actual expected glyph shapes, spacing, weight contrast and gradient; logo retains original pixels; all quoted words remain exactly identical. **FAIL:** Manrope/Plus Jakarta/Segoe/Arial fallback; synthetic bold; any third weight; cropped words; unreadable gradient; missing font in exported frames.
