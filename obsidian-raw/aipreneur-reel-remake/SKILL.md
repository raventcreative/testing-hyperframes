---
name: aipreneur-reel-remake
description: Remake reel referensi (IG/TikTok) jadi Reels premium AI PRENEUR pakai HyperFrames — VO ditulis ulang (bukan nyontek), maskot 3D host + robot AI PRENEUR, motion/transisi beda tiap scene, aset asli/open-source, render chunk, SFX sintetis, cover. Pakai saat Ravent/Freddie kirim video referensi + background dan minta "remake", "bikin versi kita", "jangan sampai keliatan nyolong", atau lanjut "video berikutnya".
---

# AIPRENEUR Reel Remake (HyperFrames)

Workflow lengkap dari 4 project yang udah jadi: **ONELINEMOTION** (roket lewat 10 dunia animasi), **KONTEN7HARI** (konten 7 hari 20 menit, Manus + Claude), **REPO9** (9 aplikasi berbayar vs kembaran gratis di GitHub), **ANIM10** (10 gaya animasi Claude, robot di-render ulang di tiap genre).
Repo: `raventcreative/testing-hyperframes` → `projects/<nama>_2026/`. Render: `npx --yes hyperframes@0.8.186`.

---

## 1. Aturan klien (wajib, jangan dilanggar)

**Remake ≠ copy**
- VO **ditulis ulang pakai kata sendiri** ("biar gak keliatan nyolong konten"). Kirim naskah dulu → klien rekam di ElevenLabs → kirim MP3.
- Struktur dibedain: urutan diacak (contoh ANIM10: no.1 → no.5), karakter sendiri (robot AI PRENEUR ikut genre), layout beda dari referensi.
- Keyword CTA beda dari referensi (referensi "ANIMATION" → kita "PROMPT"; "REPO" → "OPEN").
- Durasi ringkas kalau diminta ("1 menit lebih, intinya sama").

**"Jangan sampai AI banget"**
- Aset hanya yang asli/open-source: Simple Icons (CC0), lobehub icons (MIT, mis. Claude/Manus), lucide-static (ISC), avatar org GitHub resmi. Catat sumber di `assets/logos/SOURCES.txt`.
- Data harus diverifikasi (mis. bintang/lisensi repo via `gh api -X GET search/repositories -f q='repo:owner/name'`). Gak ada angka karangan.
- **Gak pakai foto orang.** Repo milik perorangan → pakai ikon, bukan avatar.
- Visual 3D/genre dibikin dari robot 3D klien (bukan generate AI).

**Brand & tipografi**
- Font **Poppins Bold 700 + Regular 400** saja.
- Background **navy** (`bg_user.png` 1080×1350, gradient navy-biru) → teks **putih + cyan #01CCF7** di atas chip navy `rgba(8,14,46,.85)`.
- Background **terang** (putih/biru + grid) → teks **gradient navy `#0a0d2c → #294b77`**; grid background harus gerak pelan ("biar gak diem").
- Logo AI PRENEUR pojok kiri atas (putih di navy, gelap di terang), y ≈ 262.

**Safe zone IG (1080×1920)**
- Atas 250 px & bawah 420 px ketutup UI → konten penting di y 250–1500.
- Ikon kanan: x > 960, y 1050–1700. Cover: crop grid 4:5 = y 285–1635.

**Kualitas & komunikasi**
- Motion + transisi **tiap scene beda**, jangan boring. Frame pertama harus langsung "kena" (jangan fade dari kosong).
- Kasih update persen kalau ditanya "udah berapa persen" (jujur: bagian mana selesai, ETA).
- Deliverable: **preview MP4 + cover/thumbnail elegan** (SendUserFile), ringkasan singkat bahasa Indonesia.
- Commit + push ke `main` (fetch + merge `origin/main` dulu — ada sesi lain yang ikut push).

**Feedback klien yang pernah muncul (cek sebelum kirim)**
- Teks kepanjangan keluar dari kotak/kartu → ukur & kecilkan.
- Teks numpuk saat efek mengetik → placeholder harus hilang sebelum ngetik mulai.
- Robot ngetik tapi keyboard di belakang & robot hadap depan = aneh → keyboard di depan + robot hadap depan (logika ruang harus masuk akal).

---

## 2. Workflow step by step

### 0. Bedah referensi
```bash
ffprobe -v error -show_entries stream=width,height,duration -of compact ref.mp4
ffmpeg -i ref.mp4 -vf "fps=3,scale=180:320" f/%03d.png && ffmpeg -i f/%03d.png -vf tile=10x5 -frames:v 1 sheet.png
python3 tools/fw_transcribe.py ref.wav ref_words.json large-v3 en   # faster-whisper, word timestamps
```
Catat: struktur, jumlah item, layout, CTA, apa yang bikin retensi.

### 1. Naskah VO (kirim ke klien)
- Gaya faceless reel: **kamu/aku, kalimat pendek**, tanpa opening "Hai gue Freddie" (kecuali talking head).
- Kasih **3 opsi hook** (skill `/freddie-kashawan-content` → `/reels-script`), rekomendasikan 1. Pola yang terbukti: janji visual + loop retensi ("…Tahan sampai nomor 10").
- Tiap item: nama + 1 alasan/manfaat (nilai tambah yang gak ada di referensi).
- Catatan pelafalan ElevenLabs (mis. "PS2" → tulis "PS dua" kalau salah baca). Jeda baris kosong antar item.
- Simpan `production/VO_SCRIPT.md`.

### 2. Timing dari MP3 klien
- `tools/fw_transcribe.py assets/audio/vo.mp3 production/vo_words_raw.json large-v3 id`
- `tools/timing.py`: `MERGE` (gabung kata yang kepotong, mis. "kotak"+"-kotak"), `FIX`/`FIXI` (koreksi ejaan: "cloud"→"Claude", angka→"Satu,"), snapping onset energi, `SC` = daftar scene (id, kata pertama, potongan caption, kata cyan, kata marker). VO offset 0.3 s, tail 1.3 s.
- Output: `production/timing.json` + `vendor/vo_words.js` (VO_WORDS, VO_PHONES untuk lip sync, VO_ENV, VO_SCENES).
- `tools/rounds.py` → `vendor/rounds.js`: **satu sumber timing** (tNum, tName, sweep, tDesc) dipakai stage, strip, overlay, SFX, maskot.
- **Caption harus 1 baris** (ukur lebar ≤ 930 px di browser; pecah chunk kalau lebih).

### 3. Arsitektur host (`tools/build_index.py` → `index.html`)
Urutan cat = urutan DOM:
`bg` → layer persisten (stage/tracker/robot) → slot scene (`s01`, `r1…r10`, `s12`) → judul → strip/tracker → maskot → logo+grain → caption → audio (VO + `sfx.wav`).
- **Layer persisten** = fungsi murni dari waktu global: dengar event `hf-seek`, `t = e.detail.time + (window.__T0 || 0)` (wajib untuk render per chunk). Contoh: tracker REPO9, strip + stage + title ANIM10, maskot, robot.
- **Scene** = `<template>` + `<style>` + satu root `data-composition-id` + `<script>` IIFE dengan timeline GSAP paused.
- Caption: tiap kata di chip sendiri, naik saat diucapkan; kata cyan = keyword, marker = chip putih.

### 4. Karakter
- **Maskot (host)**: `vendor/mascot3d.js` (`Mascot3D.Mascot`, `M3.direct(VW, D, {intents})`, lip sync dari VO_PHONES). Rim light cyan di navy / biru dingin di bg terang. Intent: welcome, emphasize, present, reveal, question, pointFwd, cta, point.
- **Robot AI PRENEUR (co-host)**: `vendor/robot3d.js` (`Robot3D.Robot`, `setView`/`setState`, wajah layar: blink/gaze/happy/talk bars). Gestur: wave, point, present, cheer, clap, nod, no, scan, type, think, shock, hop, jump, power.
- **StyleBot** (ANIM10): robot + set kantor di-render dalam 10 genre (lego, glow, comic, chalk, pixel, line, explainer, ps2, flat, cgi) + transisi `renderSweep` (garis scan cyan "re-render"). Source `src/stylebot.js` + `src/sb/styles/*.js`, bundle `tools/build_stylebot.sh`. Warm semua shader di `create()`.

### 5. Lookdev dulu, baru paralel
1. Bangun 1 scene template / lookdev sendiri sampai bagus (snapshot, cek).
2. Tulis `production/SCENE_BRIEF.md`: layout + zona aman per layer, gaya, konvensi kode, tabel timing terverifikasi, cek wajib.
3. Bagi ke agent paralel (≤ 5): mis. hook+CTA, ronde 1–3, 4–7, 8–10, polish style. Agent **jangan commit**; kamu yang review & commit.
4. QA semua: snapshot tiap beat, perbaiki sendiri yang kecil.

### 6. SFX (`tools/sfx.py`, numpy, tanpa sampel)
Whoosh (SVF bandpass), boom, pop, tick, chime, rip, scribble, flap, rise, buzz, typing, scan digital, + stinger genre (klik balok, shimmer neon, POW komik, gores kapur, arpeggio 8-bit, pena, marimba, pad synth 2000-an, pop UI, braaam sinematik). Taruh di tiap beat (angka, transisi, reveal, CTA).

### 7. Render (`tools/render_chunks.py`)
- Chunk di awal scene (≈ 10–12 s per chunk), tiap chunk = salinan project dengan index ditulis ulang (slot digeser, caption digeser, ambient dipotong linear, `window.__T0`), `-w 3`, part yang udah ada di-skip (resumable).
- `CHUNKS=1,2` = render sebagian dulu (mis. bagian yang gak nunggu revisi).
- Gabung x264 crf 15 + VO (offset) + SFX → `loudnorm I=-14`.
- Jalankan dengan `run_in_background` (jangan `nohup &`, jangan `sleep`).

### 8. QA final
```bash
ffprobe … -count_packets   # frame = total_sec × 30
ffmpeg -i out.mp4 -af ebur128 -f null -   # ≈ -14/-15 LUFS
```
Ambil frame di sambungan chunk + tiap ronde + hook + CTA → contact sheet → lihat.

### 9. Cover (`thumbnail/cover.html` + `render_cover.cjs`)
Playwright + static server (`python3 -m http.server`). Render 3D live (robot/StyleBot/maskot) di halaman. Isi: logo, headline besar (angka cyan), sub-chip, visual inti (tile/ikon), maskot melambai, pertanyaan pancing komen ("Mana yang paling keren?"). Semua penting di crop 4:5.

---

## 3. Playbook retensi (yang bikin view tembus)
- **Frame 0 langsung isi** (karakter + layar), hook visual = bukti janji (mis. robot ganti 10 gaya dalam 2 detik).
- **Alat progres** yang bikin nunggu: tracker 9 tile yang dicoret→flip (REPO9), strip 10 chip terkunci yang kebuka per ronde + chip 10 teaser (ANIM10).
- **Loop teaser**: "Tahan sampai nomor 10" + yang paling wow ditaruh terakhir.
- Ganti pola visual tiap ±2 detik; tiap ronde punya transisi signature sendiri.
- SFX di setiap beat.
- CTA divisualkan: keyword ngetik sendiri di kolom komen → hati → pesawat kertas → kartu DM "terkirim".

**Bank transisi yang udah dipakai** (jangan ulang persis di video berikutnya): coin flip, sound-wave morph, magnifier scan, page peel, mic ripple, kanban drag, sobekan kalender + sync, channel funnel, REC + clapper (REPO9) · scan "re-render" genre, panel komik, tulisan kapur, koin pixel, satu garis, callout explainer, character select, brand kit, letterbox + slate (ANIM10) · roket lewat 10 dunia (ONELINEMOTION) · stepper split-flap "LANGKAH n" (KONTEN7HARI).

---

## 4. Gotcha teknis HyperFrames 0.8.186
- Runtime **menghapus id root template** → pakai `document.getElementById` dengan id ber-prefix (`r3-…`); root scene `id="root"` (scoping CSS).
- Preview server **menyuntik `data-hf-id`** ke file di disk → regex harus toleran (`<div[^>]*\bid="x"[^>]*…`).
- Regex slot chunk harus cocok dengan semua id scene: `[swr]\d+` (bug lama: `[sw]\d\d` gak cocok r1–r9 → ronde kosong di render). Tambah assert jumlah slot per chunk.
- GSAP: timeline paused, patch `_sc` (scale → scaleX/Y), `ft` = fromTo `immediateRender:false`, `I(el,v)` = gsap.set + tl.set(…,0), akhiri `tl.set({}, {}, D-0.01)`, patch render urutan seek, `window.__timelines[id]`.
- **Jangan pakai onUpdate** (gak reliable saat seek): counter/ngetik pakai `tl.set` per nilai. Gerak stop-motion = waktu dikuantisasi (12 fps).
- fromTo dengan from-value sebagian → properti lain mulai dari state t=0 (elemen loncat). **Selalu isi from-value lengkap.**
- Satu tween `attr`/`clip-path` per properti; jangan `svgOrigin` di SVG yang di-transform CSS.
- Deterministik: no `Math.random` (PRNG seed), no `Date`, no CSS animation/transition, no rAF.
- Snapshot ≤ 10 `--at` per run, `--describe false --timeout 60000`. Snapshot gagal **diam-diam** kalau script scene error → `node tools/check_scene.cjs <ids>` (butuh preview server).
- Lint warning `nested_structure_needs_subcomposition` untuk `#bg/#fx` di index aman diabaikan.
- WebGL di render = SwiftShader (CPU): ukur ms per frame tiap style; lego/cgi termahal (~1 s). 4 CPU, jangan render + banyak agent snapshot bersamaan kalau mau cepat.
- `rm` kena safety check → pakai path literal. Jangan ulang aksi yang ditolak.

---

## 5. Checklist kirim
- [ ] Frame & durasi pas, loudness ≈ -14 LUFS, sambungan chunk mulus.
- [ ] Gak ada teks keluar kotak / numpuk / ketutup maskot; caption 1 baris.
- [ ] Semua logo/data asli + sumber tercatat; gak ada foto orang.
- [ ] Frame pertama kuat; CTA keyword jelas.
- [ ] Cover jadi (crop 4:5 aman).
- [ ] Commit + push (merge `origin/main` dulu).
- [ ] Ingatkan klien siapkan isi yang dijanjikan CTA (link/prompt).
