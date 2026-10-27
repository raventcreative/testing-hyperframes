# 20 Efek Video Editing — Panduan & Prompt untuk Claude Code

Materi untuk audiens yang komentar **EDIT**. Kamu bisa memakai daftar ini untuk menyusun video pendek dengan efek kreatif berbasis kode. Ini bukan jaminan hasil instan; kualitas tetap bergantung pada footage, asset, arahan visual, rig karakter, dan review.

## 20 efek dan fungsi visualnya

| No. | Nama efek | Seperti apa hasilnya | Cocok untuk |
|---:|---|---|---|
| 01 | Orbit | Ikon/objek bergerak mengelilingi subjek dengan kedalaman | Memperkenalkan banyak fitur tanpa full-screen list |
| 02 | Chat Takeover | Tampilan chat membesar dan mengambil alih fokus scene | Memvisualkan prompt, conversation, instruksi |
| 03 | Frame Escape | Subjek atau properti seakan keluar dari bingkai video | Momen surprise, hook, transformasi |
| 04 | Snap Zoom | Kamera berpindah cepat ke detail tertentu lalu settle | Menegaskan reaksi atau detail penting |
| 05 | Checklist Pop | Beberapa checklist muncul satu-satu dengan ritme | Menunjukkan progress dan fitur selesai |
| 06 | Headline Storm | Barisan teks masuk secara editorial dari beberapa sisi | Hook, kata kunci, urgent reveal |
| 07 | Zoom Portal | Kamera masuk ke bentuk portal dan keluar di dunia lain | Pindah topik/scene yang terhubung |
| 08 | Growth Curve | Garis/grafik tergambar dan bergerak mengikuti narasi | Kemajuan yang didukung data sebenarnya; jangan reka angka |
| 09 | Studio Reveal | Panggung/ruang dan lighting muncul secara sinematik | Membentuk suasana premium |
| 10 | B-roll Overlay | Layer video kecil ditumpuk pada footage/timeline | Menjelaskan proses editing atau cuplikan pendukung |
| 11 | Paper Cutout | Subjek menjadi potongan kertas bertekstur dengan bayangan | Pergantian style kreatif |
| 12 | Dolly Zoom | Kamera bergerak sembari lensa berubah agar ruang terasa bergeser | Menimbulkan fokus dramatis pada subjek |
| 13 | Magazine Cover | Subjek menjadi elemen desain cover editorial | Produk, tokoh, cerita utama |
| 14 | Liquid Glass | Panel transparan/distorsi lembut melewati objek | Transisi material mewah dan highlight UI |
| 15 | Zoom Through Cut | Kamera menembus objek/layar menuju scene berikutnya | Perpindahan antarkonsep |
| 16 | Green Screen | Latar subjek diganti dengan scene lain secara rapi | Dunia virtual, before-after latar |
| 17 | Frame Break | Objek atau layar pecah menjadi fragmen | Pattern interrupt yang terukur |
| 18 | Digital Zoom | Tampilan kamera/HUD memperbesar area tertentu | Tutorial, bukti detail, ekspresi |
| 19 | Phone Mockup | Footage ditampilkan pada perangkat HP bergaya premium | Menunjukkan output dalam konteks penggunaan |
| 20 | Checklist | Rangkuman semua efek dengan centang progres | Proof + penutup yang memuaskan |

## Urutan storyboard yang gampang dipahami

1. **0–5 detik — Hook.** Tunjukkan hasil editing terlebih dulu, lalu balik ke footage aslinya.
2. **5–15 detik — Frame hidup.** Orbit, Chat Takeover, Frame Escape, Snap Zoom, Checklist Pop.
3. **15–25 detik — Informasi bergerak.** Headline Storm, Zoom Portal, Growth Curve, Studio Reveal, B-roll Overlay.
4. **25–35 detik — Material berubah.** Paper Cutout, Dolly Zoom, Magazine Cover, Liquid Glass, Zoom Through Cut.
5. **35–45 detik — Dunia berubah.** Green Screen, Frame Break, Digital Zoom, Phone Mockup, Checklist.
6. **45–60+ detik — Proses & payoff.** Jelaskan dari footage + instruksi → scene kode → animasi → preview. Tunjukkan hasil dan CTA.

Ini hanyalah estimasi. Pengucapan voice-over menentukan timing akhir.

## Trik motion supaya tidak terasa template

Pilih 2–4 transisi yang menyambung gerakan dan pakai ulang secara konsisten:

- Bingkai jendela video → layar chat → portal.
- Tepi kertas → rel kamera → frame majalah.
- Pantulan kaca → lensa → pindah latar.
- Sudut HUD → bezel ponsel → checklist.

Cara berpikirnya sederhana: benda dari scene sebelumnya **menjadi alasan** benda baru muncul di scene selanjutnya. Kalau tidak ada hubungan, gunakan cut yang bersih.

## Prompt dasar siap salin ke Claude Code

```text
You are my creative director and motion-design engineer.

My assets:
- Footage or character: [REAL PATH]
- Brand colors: [HEX]
- Font: [FONT]
- Logo: [REAL PATH]
- Voice-over: [REAL PATH]
- Reference video(s): [REAL PATHS]

Create an ORIGINAL vertical 1080x1920, 30fps social video that demonstrates 20 editing effects in four storytelling chapters. Use the references only for motion principles, camera movement, object interactions, and transition techniques. Do not copy source footage, creator assets, logos, text or original audio.

Use these 20 effects as labeled demonstrations:
Orbit, Chat Takeover, Frame Escape, Snap Zoom, Checklist Pop, Headline Storm, Zoom Portal, Growth Curve, Studio Reveal, B-roll Overlay, Paper Cutout, Dolly Zoom, Magazine Cover, Liquid Glass, Zoom Through Cut, Green Screen, Frame Break, Digital Zoom, Phone Mockup, Checklist.

Create a scene-by-scene storyboard before coding. Give every scene a clear hero object, physical motion, camera angle, lighting, key moment synced to VO, and a meaningful transition. Prioritize shape-match and object handoff transitions rather than random swipes.

Inspect the available video/3D assets before implementation. If the character lacks bones or facial morph targets, do not invent lip-sync capability; explain the limitation and use appropriate camera/prop animation instead.

Use deterministic GSAP/HyperFrames timelines when supported. Build a short quality prototype, inspect frames and cuts, then complete an assembled preview. After approval, render the final MP4 and verify technical quality. Preserve the original assets.
```

## Checklist sebelum posting

- [ ] Seluruh 20 efek ditampilkan dan memiliki urutan yang masuk akal.
- [ ] Tidak mengklaim semua proses selesai satu klik jika memang tidak demikian.
- [ ] Tidak mengambil frame, wajah, watermark, atau audio milik kreator lain tanpa izin.
- [ ] Voice-over sinkron dengan gerakan utama.
- [ ] Font, logo, warna, dan safe area konsisten.
- [ ] Hasil ekspor dicek dari MP4 sebenarnya, tidak hanya di preview kode.

**Catatan:** Jika ingin versi yang benar-benar meniru gerak satu video referensi, lampirkan video itu di project lalu minta Claude Code membuat *motion atlas* timestamped terlebih dahulu. Jangan menyalin mentah aset sumber.
