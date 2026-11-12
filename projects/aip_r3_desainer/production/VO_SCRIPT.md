# VO — 5 tool gratis bikin Claude jadi desainer · background NAVY · 46,2 dtk VO (video 47,53 dtk)

Referensi: `aip_remake_batch3/refs/ref3.mp4` (39 dtk, EN, "turn Claude into an insane AI designer with five free tools").
Yang diubah dari referensi: hook kita mulai dari masalah penonton ("website bikinan AI kelihatan generik?") lalu tiap tool ditunjukkan
EFEKNYA di satu website contoh yang sama (halaman generik → halaman rapi → dipoles & dicoba variasinya → dites di 3 ukuran layar),
lalu file DESIGN.md dan model 3D dari foto. Bahasa Indonesia, aku/kamu, tanpa "insane", tanpa klaim berlebihan. Nama tool kelima
ditulis benar: **img2threejs** (referensi menyebut "Image23js"). CTA beda: "Komen DESAIN".

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
| # | Tool | Repo / sumber | Yang dipakai di VO & visual | Lisensi |
|---|------|---------------|-----------------------------|---------|
| 1 | **Taste Skill** | github.com/Leonxlnx/taste-skill (README; situs tasteskill.dev) | Agent Skill yang bikin coding agent membangun website profesional, bukan landing page generik; aturan: satu sistem desain, copy lugas, satu section per layar, tepi kiri-kanan sama, dicek checker di browser | MIT |
| 2 | **Impeccable** | github.com/pbakaus/impeccable (README; impeccable.style) | "design vocabulary" untuk coding agent: perintah `polish`, `bolder`, `critique`, `audit`, `quieter`, `live`; mode live = pilih elemen di browser, coba varian, yang dipilih ditulis balik ke source | Apache-2.0 |
| 3 | **Playwright CLI** | github.com/microsoft/playwright-cli (README) | CLI Playwright untuk coding agent (Claude Code disebut): `playwright-cli open`, sesi terpisah `-s=nama`, `open --device="iPhone 15"`, `click`, `screenshot` | Apache-2.0 |
| 4 | **Awesome DESIGN.md** | github.com/VoltAgent/awesome-design-md (README) | Kumpulan DESIGN.md yang diekstrak dari website nyata (badge: 84 file; daftar: claude, vercel, linear.app, stripe, notion, figma, spotify, apple, dll.); isi tiap file: palet warna, tipografi, komponen (tombol), layout/spacing | MIT |
| 5 | **img2threejs** | github.com/img2threejs/img2threejs (dulu hoainho/img2threejs, redirect) · demo img2threejs.io | Dari SATU gambar referensi, agent membangun ulang objeknya jadi model Three.js prosedural "code-only" (tanpa file mesh/tekstur), bisa di-orbit di browser, siap dianimasikan; pipeline bertahap blockout → … → material | Apache-2.0 |

Catatan klaim: "gratis" = kelimanya open source (MIT / Apache-2.0); Claude-nya sendiri tetap butuh akun/paket Claude — VO tidak
mengklaim Claude gratis. Angka bintang GitHub sengaja tidak dipakai (berubah-ubah). Nama situs di daftar DESIGN.md hanya teks,
tanpa logo; nilai warna/font di kartu DESIGN.md adalah contoh UI generik, bukan milik merek mana pun. "Kedai Sangrai" dan "NovaAI"
adalah halaman contoh fiktif.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; tiap baris diawali tag `[playful] [excited]`)
1. Website bikinan AI kamu kelihatan generik? Lima tool gratis ini bikin Claude jadi desainer.
2. Pertama, Taste Skill. Claude dikasih aturan desain yang jelas, jadi hasilnya nggak kayak template AI lagi.
3. Kedua, Impeccable. Ketik perintah kayak polish atau bolder, terus coba variasinya langsung di browser.
4. Ketiga, Playwright CLI. Claude buka browser sendiri, ngetes websitenya, terus screenshot buat ngecek hasilnya.
5. Keempat, Awesome DESIGN.md. Kumpulan file desain dari website beneran: warna, font, tombol, sampai layout.
6. Kelima, image to three JS. Kasih satu foto motor, Claude bangun ulang jadi model 3D interaktif, cuma pakai kode.
   (dibaca "image to three JS"; caption menulis **img2threejs**)
7. Semuanya gratis dan open source. Mau link-nya?
8. Komen DESAIN, aku kirim lewat DM.

Voice: `tools/voice_config.json` (voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75), dibuat dengan
`python3 tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"` (satu panggilan) →
`assets/audio/vo.mp3`. Cek pelafalan dengan faster-whisper large-v3: semua kata terbaca benar ("Keempat, awesome design.md",
"Komen desain, aku kirim lewat DM").
