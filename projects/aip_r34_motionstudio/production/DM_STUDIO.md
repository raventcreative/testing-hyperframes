# DM · STUDIO — 4 repo open-source buat bikin video & animasi pakai Claude (+4 bonus)

Halo! Ini daftar yang aku janjiin di reel. Semua repo di bawah aku cek langsung di GitHub (21 Nov 2026) — angka bintang bisa berubah.

## 4 pilihan utama
1. **HyperFrames** — https://github.com/heygen-com/hyperframes
   Claude (atau agent lain) nulis video sebagai HTML + CSS + animasi, lalu HyperFrames merendernya jadi MP4. Reel AIpreneur dibikin pakai ini.
   Lisensi Apache-2.0 · ±87,5 rb bintang.
2. **GSAP skills (resmi dari GreenSock)** — https://github.com/greensock/gsap-skills
   Skill resmi buat agent AI supaya pakai GSAP dengan benar: easing, timeline, stagger, ScrollTrigger, plugin. Gerakan jadi halus, nggak kaku.
   Lisensi MIT.
3. **Blender MCP** — https://github.com/ahujasid/mcp-for-blender (dulu bernama `blender-mcp`)
   Add-on Blender + server MCP: Claude bisa bikin & ngatur scene 3D di Blender dari prompt (objek, material, kamera; bisa jalanin kode Python di Blender).
   Proyek komunitas, bukan buatan Blender Foundation. Lisensi MIT. Tips: simpan file Blender dulu sebelum minta AI jalanin kode.
4. **Video Shotcraft** — https://github.com/Vincentwei1021/video-shotcraft
   Skill untuk Claude Code & Codex: bikin video promo produk sinematik dari screenshot & copy produkmu sendiri (Remotion), tiap shot tetap bisa diedit.
   Kode Apache-2.0; Remotion punya lisensi sendiri (gratis untuk individu & tim kecil, perusahaan bisa butuh lisensi berbayar — cek remotion.dev/license).

## 4 bonus (fondasi yang sering dipakai bareng)
5. **Remotion** — https://github.com/remotion-dev/remotion — bikin video pakai React (cek lisensinya untuk perusahaan).
6. **three.js** — https://github.com/mrdoob/three.js — library 3D di browser (MIT). Dunia voxel 3D di reel ini pakai three.js.
7. **Theatre.js** — https://github.com/theatre-js/theatre — editor motion design untuk web (Apache-2.0).
8. **Manim** — https://github.com/ManimCommunity/manim — animasi matematika/penjelasan pakai Python (MIT).

## Cara mulai paling gampang (Claude Code)
1. Install Claude Code, buka folder kosong.
2. Tempel link HyperFrames + GSAP skills, minta: "Pasang dua repo ini, lalu bikin video 9:16 durasi 15 detik tentang <produk/topikku>, gaya minimal."
3. Cek hasilnya frame per frame, minta revisi per adegan, baru render.
4. Butuh objek 3D? Tambah Blender MCP. Butuh promo produk sinematik dari screenshot? Coba Video Shotcraft.

Catatan jujur: semua repo ini gratis & open-source, tapi Claude Code butuh paket Claude, dan hasil tetap perlu kamu cek sebelum posting.
