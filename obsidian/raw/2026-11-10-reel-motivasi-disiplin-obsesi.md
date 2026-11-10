---
tags: [aipreneur, reel, remake, hyperframes, elevenlabs, batch, mindset]
date: 2026-11-10
project: projects/tigamental_2026
---
# Reel: Motivasi, disiplin, obsesi (target posting 100 hari) · TERANG

- **Referensi**: "Same wall. Three different mindsets." (20 s, tanpa VO, 3 stickman mukul tembok, counter 14 / 100 / 1.000, gelap).
- **Versi kita**: 26,3 s, background terang + grid, teks gradient navy, VO ElevenLabs v4. Pesannya sama, **metaforanya ganti** ke dunia audiens: **streak posting konten 100 hari** (board 100 kotak ala heatmap). CTA engagement: **"Kamu yang mana? Tulis di komen."**
- **Tiga orang = tiga badge** (bukan figur/foto): MOTIVASI amber (flame), DISIPLIN biru (calendar-check), OBSESI ungu (infinity).

## Alur
1. s01 — poster "100 HARI" dari kotak-kotak + bendera, 3 badge abu-abu masuk lajur, bendera pecah jadi 3, board kosong ngalir.
2. s02 MOTIVASI — banjir warna amber, kotak keisi cepat bergelombang, hari ke-14 api padam + asap, stempel "BERHENTI · DI HARI KE-14".
3. s03 DISIPLIN — metronom 1 kotak per ketukan ("pelan tapi pasti"), time-lapse pas 100 di "ke-100,", ✓ "TARGET TERCAPAI" + konfeti.
4. s04 OBSESI — dolly masuk ke lajur 3, fast-forward ke 100, bendera dicabut & dilempar, zoom out: board 100 jadi 1 dari 10 tile papan 1.000, counter 100 → 101.
5. s05 — gunung vektor: biru di puncak "100 ✓", gunung ungu jauh lebih tinggi naik di belakang, kamera pan ke "1.000".
6. s06 — panel pecah jadi 3 kartu polling (14 · 100 · 1.000), komen "Aku tim Disiplin" diketik, hati, logo besar.

## Pelajaran teknis
- 100 kotak per board **tanpa** 100 tween: satu `clip-path` polygon berbentuk L per board, di-set per nilai (≤ ~95 elemen animasi per scene).
- Satu agen bikin semua scene dari satu generator (`gen.cjs`) → sistem lajur identik di semua cut (0 pixel beda).
- Reel tanpa VO di referensi → kita tambah VO + CTA komen (engagement), tetap pendek (26 s).
Output: `out/TIGAMENTAL_1080x1920.mp4` · cover `thumbnail/COVER_TIGAMENTAL_1080x1920.png`.
