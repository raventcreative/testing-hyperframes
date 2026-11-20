---
name: feed-carousel
description: AIpreneur static IG feed post / carousel (4:5, 1080×1350 PNG) in the client's locked format — navy or white brand background, AIpreneur logo top-left (white on navy, dark on white), Poppins Bold headline + Inter Regular body, strict safe zone and generous negative space. Use for "/feed-carousel", "bikin carousel", "bikin feed", "slide IG", "post feed AIpreneur".
---

# Feed / Carousel AIpreneur — format terkunci (client, 2026-11-20)

## Format
| Item | Aturan |
|---|---|
| Ukuran | 4:5, **1080 × 1350 px**, PNG |
| Background navy | `brand/feed/bg-navy.png` |
| Background putih | `brand/feed/bg-white.png` (grid tipis pojok kanan atas) |
| Logo | pojok kiri atas. Navy → `brand/feed/logo-white.png`; putih → `brand/feed/logo-dark.png` |
| Headline | **Poppins Bold** (`brand/fonts/poppins-latin-700-normal.woff2`) |
| Teks biasa | **Inter Regular** (`brand/fonts/inter-latin-400-normal.woff2`) |
| Warna — putih | headline gradient `#0a0d2c → #294b77`; body `#0a0d2c`; aksen `#294b77` |
| Warna — navy | teks putih; aksen/highlight `#00c9ff` |
| Warna lain | **tidak boleh** (no merah, kuning, dll.) |

## Safe zone & spacing (jangan mepet)
- Margin kiri/kanan **96 px** (aman juga dari crop grid profil IG 3:4 = ±34 px tiap sisi).
- Logo: x 96, y 88, tinggi **34 px** (lebar ±375 px).
- Jarak logo → teks pertama **≥ 120 px** (konten mulai y ≥ 242).
- Margin bawah **≥ 96 px**; footer (nomor slide / "Geser →") di y 1254 ke bawah, Inter 24 px, opacity .7.
- Headline 64–88 px, line-height 1.12, maks 3 baris, maks lebar 860 px.
- Body 30–36 px, line-height 1.5, maks ±4 baris per slide; jarak headline → body 40 px.
- Negative space **≥ 35%** kanvas. Satu ide per slide. Kalau teks kepanjangan → pecah ke slide baru, jangan kecilkan font di bawah batas.

## Cara pakai
1. `cp -r skills/feed-carousel/templates projects/feed_<slug>` lalu isi `slides.js`:
   ```js
   window.BRAND='../../brand';           // path ke brand/ dari folder project
   window.SLIDES=[{theme:'navy'|'white', title:'Headline <span class="acc">aksen</span>', body:'...', h:76, b:34, align:'flex-start'|'center'}];
   ```
   Tema default: cover navy, isi selang-seling navy/putih kecuali client minta lain.
2. `node projects/feed_<slug>/render.cjs projects/feed_<slug>` → `out/slide_XX.png`.
3. QA wajib (lihat tiap PNG): logo tidak kepotong, jarak logo–teks ≥ 120 px, tidak ada teks di luar margin 96 px, tidak ada widow 1 kata di headline (pakai `<br>`), warna hanya dari tabel.
4. Kirim PNG + caption (sudut pandang pelengkap, bukan ringkasan slide; hashtag `#aipreneur #skoolcommunity #aimarketing`), commit + push ke `main`.

Contoh hasil: `examples/sample_navy.png`, `examples/sample_white.png`.

## Slide penutup (WAJIB, client rule 2026-11-20)
Slide terakhir tiap carousel = slide penutup ini, **persis** seperti `examples/closing_reference.png`. **Jangan diterjemahkan, jangan diubah kalimatnya** (tetap bahasa Inggris walau slide lain bahasa Indonesia):
- Headline: "Your business / deserves a / **better agent.**" (underline "better agent.")
- Sub: "Less manual work. More business growth." · pills: Custom Software · AI Agents · Automation
- Kartu akun: avatar A (navy) · **@aipreneur.automation** · "Follow for AI agents and automation" · tombol **Follow**
- Baris CTA: ikon panah bawah + "Get your custom agentic software. Tap the link in our bio."
- Background putih, logo kiri atas, counter `NN / NN`, dots footer (tanpa tombol next).
Render: `python3 skills/feed-carousel/templates/closing/closing.py --n <N> --total <N> --out <png> [--mp4 <mp4>]`
(`--mp4` = versi animasi 6 s untuk carousel video: elemen naik satu-satu, kursor klik Follow → Following).
Jangan pasang otomatis ke carousel lama kecuali client minta.
