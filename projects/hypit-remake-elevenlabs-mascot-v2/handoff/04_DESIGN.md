# HYPIT REMAKE — VISUAL SYSTEM V2 (ELEVENLABS + MASCOT)

> Dokumen identitas visual. Ini **override eksplisit** terhadap palet/typography default REF-H. Motion/refinement REF-H tetap jadi benchmark kualitas.

## Background

- `assets/background_asli.png`: file asli **1080×1350**, putih-ivory dengan soft icy-blue di bagian sudut/tepi. HARUS tetap terlihat di seluruh video.
- Canvas final 1080×1920. Gunakan CSS `background-size: cover` (uniform scale + center crop) **atau** mirror/blur extension di top/bottom; pilih hasil yang paling setia ke supplied image. Jangan distorsi aspek rasio.
- Tambahkan grain mikro lembut (low opacity) dan glow/spatial haze hanya sebagai depth, bukan mengganti latar.

## Color tokens

| Name | Value | Role |
|---|---|---|
| `navy-deep` | `#121532` | Kedalaman gradient, angka, teks di atas background terang |
| `navy-mid` | `#274976` | Partner gradient, accent panel dan solid shape |
| `white` | `#FFFFFF` | Huruf putih hanya di atas shape navy |
| `ice-white` | `#F7FAFF` | Material porcelain dan highlight permukaan |
| `pale-steel` | `#DCE8F6` | Rim, UI light strokes, secondary planes |
| `graphite` | `#26354E` | Secondary text di atas BG putih |

Gunakan `linear-gradient(105deg, #121532 0%, #274976 100%)` pada backing teks putih, acrylic enamel/plates/ticker. Boleh gradient radial lokal demi material depth, bukan mengganti 2 warna utama. Hindari violet neon, merah, magenta, kuning headline.

## Typography

- **Poppins Bold 700/800**: kata kunci / small caption accent / angka yang telah terverifikasi.
- **Poppins Regular 400**: kata penghubung, caption standar, microcallout.
- Caption top: x 70–1010, centre, baseline area y ±215–375; target 42–48px; 1–2 baris maksimal, lebih pendek lebih bagus. Max ±3–6 kata per chunk, mengikut VO.
- In-scene labels 25–34px bila benar-benar diperlukan. Untuk console code boleh monospace kecil.
- No giant headings, no bottom subtitle box.

## Highlight system (PENTING)

Sumber estetika: `assets/kotak_highlight_asli.png` (1080×1350 RGBA dengan horizontal navy bar). File ini adalah **referensi backing**; jika dipakai langsung, jangan menampilkan kanvas transparannya sebagai overlay besar.

Implementasi fleksibel: elemen inline `.word-highlight` memakai `background: linear-gradient(105deg,#121532,#274976); color:#fff; padding:6px 18px 9px; border-radius:12px; box-decoration-break:clone; -webkit-box-decoration-break:clone`. Huruf putih wajib di dalam kotak; padding cukup supaya tidak dempet.

Tween kotak: `scaleX(0.1)→scaleX(1)` atau mask reveal yang sinkron dengan kata VO; huruf masuk kemudian 1–2 frame. Jangan menampilkan seluruh highlight permanen untuk semua kata.

## Composition / safe-area

- Output 9:16 / 1080×1920.
- Small caption: y 220–385; jangan ada benda besar menutupnya.
- Hero/metafora utama: x 50–1030, y 415–1510, centre sekitar 930. Besar 60–75% luas zona visual.
- Area di bawah y 1570 relatif lega untuk UI platform.
- Source image sudah light; navy surfaces harus punya tepi, silhouette, highlight putih/refleksi halus, dan contact shadow. Jangan blok gelap fullscreen.

## Motion identity

1. Hero fisik yang membuktikan makna kata.
2. Anticipation → contact/apex di kata VO → resolve + micro-settle.
3. Tiga depth plane, edge bevel, key light kiri atas, shadow ke bawah kanan.
4. Kamera push-in lambat max 1.06x, parallax selektif; jangan setiap scene pola sama.
5. Pola transisi dominan match-cut/hard-cut atas metafora yang saling menyambung; 2–3 chapter transitions via shutter/push singkat jika perlu.
6. Frame pertama berisi objek, frame terakhir diam dan terbaca; no fade-to-black.

## Mascot cameos

Source `mascot/mascot_three_view_source.png` ialah sheet karakter tiga tampak satu PNG (bukan model ber-rig). Integrasi melalui PNG masked cutouts dan animasi parent GSAP whole-body 2.5D yang relevan dengan tindakan hero pada s02/s04/s08/s11/s14/s16/s19. Maskot maksimal sekitar 25–40% lebar panggung, tidak menutupi visual hero/caption, tidak selalu muncul. Face/hair/polo hitam bertuliskan AI PRENEUR/celana krem/sepatu putih harus identik. Untuk gerak tangan, kepala, atau lip sync independen minta aset GLB/FBX ber-rig/layer terpisah. Lihat detail `09_MASCOT_MOTION_GUIDE.md`.

## Voice lock V3

Word-sync **hanya** berdasarkan `assets/vo_elevenlabs_final.mp3` PROVIDED (durasi media 61.07425 detik), bukan audio source lama. Estimasi timing di kode demo bukan timing produksi. Claude Code harus review actual voice/word alignment sebelum memproduksi scene berwaktu. Preview dan approval Freddie mendahului render final.

## What NOT to do

- Full-screen navy gradient: akan menimpa background asli.
- Komposisi yang cuma teks besar dan satu kotak kecil.
- Copy ulang warna merah/kuning dari original, logo ARRAZY, WA, atau desain asli.
- Kata putih tanpa shape backing; teks kecil tidak terbaca di smartphone.
- Dashboard/screenshot palsu dengan informasi faktual baru; jika perlu buat schematic/abstract UI.
- Manipulasi logo brand yang tidak diberikan; klaim QA PASS tanpa snapshot/render.
