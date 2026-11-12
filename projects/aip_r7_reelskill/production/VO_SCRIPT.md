# VO — 1 skill Claude bikin reels animasi tanpa kredit video AI · background NAVY · 43,9 dtk VO (video 45,47 dtk)

Referensi: `aip_remake_batch4/refs/ref2.mp4` (50 dtk, EN, "one Claude skill can make unlimited animated reels").
Yang diubah dari referensi:
- Hook kita langsung ke manfaat yang kelihatan: dinding 4 reels animasi yang JALAN di layar + "tanpa kredit video AI sama sekali"
  (bukan "did you know"). Bahasa Indonesia, aku/kamu, suara praktisi.
- Alatnya disebut terang: **HyperFrames** (open source dari HeyGen) — Freddie memang memakainya, dan reels ini sendiri dibuat dengan
  HyperFrames + Claude (benar: komposisi HTML/GSAP di folder ini, caption = kode, SFX disintesis kode `tools/sfx.py`).
- Semua statistik pribadi referensi DIBUANG (60 reels / 1 juta views / 11 ribu followers) — tidak ada angka pertumbuhan sama sekali.
- Contoh gaya (cerita anak sebelum tidur, kartun, kolam koi, film pendek) dibangun sebagai mini-scene HTML/CSS/SVG + GSAP sungguhan
  di dalam reels (`vendor/r7kit.js` → `R7K.MINI`), bukan gambar/klip dari referensi. Tampilan referensi (krem/peach, maskot kepiting
  pixel, layout) tidak dipakai — house style NAVY AI PRENEUR.
- CTA beda: "Komen REELS" + panduan pasang (bukan "150 orang pertama gratis").

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
| Klaim di VO / visual | Sumber | Isi yang dipakai |
|---|---|---|
| Nama & pembuat: **HyperFrames**, open source dari **HeyGen** | github.com/heygen-com/hyperframes (README); npm `hyperframes` (repository `heygen-com/hyperframes`, homepage hyperframes.heygen.com) | repo milik org heygen-com; README: "used in production at HeyGen" |
| Lisensi | `LICENSE` di repo (Apache License 2.0); npm `license: Apache-2.0` | Apache-2.0; README: "no per-render fees or commercial-use thresholds" |
| Apa yang dilakukan ("Claude nulis reels-nya jadi kode", "HTML → MP4") | README: "Write HTML. Render video. Built for agents."; "turning HTML, CSS, media, and seekable animations into deterministic MP4 videos"; animasi GSAP/CSS/Lottie/Three.js…; "seeks each frame in headless Chrome and encodes the result with FFmpeg" | agent (Claude Code dll.) menulis komposisi HTML, HyperFrames merender ke MP4 |
| "Pasang skill-nya pakai satu perintah" | README: `npx skills add heygen-com/hyperframes` (alternatif Claude Code plugin: `claude plugin marketplace add heygen-com/hyperframes` + `claude plugin install hyperframes@hyperframes`); skill pintu masuk `/hyperframes` | satu perintah `npx skills add heygen-com/hyperframes` (README: "HyperFrames ships 9 skills" — VO sengaja TIDAK menyebut jumlah skill) |
| "render di laptop kamu sendiri" | README: CLI `npx hyperframes init / preview / render`, "Render locally or in Docker"; syarat **Node.js 22+** dan **FFmpeg** | render lokal → tidak ada kredit video yang terpakai |
| "tanpa kredit video AI" | konsekuensi dari di atas: tidak ada model video-generation; render = Chrome headless + FFmpeg di mesin sendiri, tanpa biaya per-render | VO TIDAK mengklaim Claude gratis (Claude tetap butuh akun/paket); hanya "nggak ada kredit video yang kepotong" |
| "reels yang lagi kamu tonton ini … semuanya kode" | folder ini: `index.html` + `compositions/*.html` (GSAP), caption dibangun kode dari `production/timing.json`, `assets/audio/sfx.wav` disintesis `tools/sfx.py` (numpy, tanpa sampel) | suara narator = ElevenLabs TTS (tidak diklaim sebagai kode); VO hanya menyebut animasi, teks, efek suara |
| Panduan di CTA | README (Node.js 22+ & FFmpeg; `npx skills add heygen-com/hyperframes`) | kartu panduan memakai teks ini persis |

Catatan: situs hyperframes.heygen.com tidak bisa dibuka dari sandbox (DNS diblokir) — semua fakta di atas dari README GitHub resmi,
file LICENSE, dan metadata npm. Angka bintang GitHub sengaja tidak dipakai. Isi mini-scene (Kiki & Bulan, Bolo, "Besok, aku coba lagi.")
adalah contoh buatan sendiri; panel "Model video AI" generik tanpa merek; potongan kredit di s03 ilustrasi, tanpa harga.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; tiap baris diawali tag `[playful] [excited]`)
1. Reels animasi kayak gini, aku bikin tanpa kredit video AI sama sekali.
2. Kamu kasih Claude satu ide, terus Claude nulis seluruh reels-nya jadi kode.
3. Bukan model video AI, tapi HTML sama animasi. Jadi nggak ada kredit video yang kepotong.
4. Gayanya bebas. Cerita anak sebelum tidur, lengkap sama bulan dan bintangnya. Kartun lucu yang lompat-lompat.
5. Kolam koi yang airnya beneran gerak. Sampai film pendek yang ada ceritanya.
6. Namanya HyperFrames, open source dari HeyGen. Pasang skill-nya pakai satu perintah, render di laptop kamu sendiri.
7. Dan reels yang lagi kamu tonton ini? Dibikin persis begitu. Tiap animasi, tiap teks, sampai efek suaranya, semuanya kode.
8. Mau panduan pasangnya?
9. Komen REELS, aku kirim lewat DM.

Voice: `tools/voice_config.json` (voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75), satu panggilan:
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"`
→ `assets/audio/vo.mp3` (43,9 dtk). Take 1 (tanpa "lengkap sama bulan dan bintangnya" / "Kartun lucu yang lompat-lompat", 40,8 dtk)
disimpan di `production/vo_take1/` — diganti karena showcase butuh waktu tayang lebih panjang. Cek pelafalan dengan faster-whisper
small: semua kata terbaca ("Reels animasi…", "Namanya Hyper Frames, open source dari HeyGen", "Komen Reels aku kirim lewat DM").
