# VO — YouTube agent: 11 skill Claude buat channel kamu · background NAVY · 44,1 dtk VO (video 45,70 dtk)

Referensi: `aip_remake_batch4/refs/ref4.mp4` (48 dtk, EN, cream/peach + maskot crab piksel, "Claude just killed YouTube").
Yang diubah dari referensi:
- Hook TIDAK pakai klaim clickbait "Claude just killed YouTube". Kita mulai dari masalah penonton: kreator yang ngurus channel
  sendirian ("Ngurus channel YouTube sendirian?") — 7 kerjaan, 1 orang — lalu janji yang bisa dibuktikan: 11 skill gratis,
  dari naskah sampai riset video viral.
- Nama pack + bukti "gratis" dibikin satu beat sendiri (open source MIT · tanpa daftar · tanpa API key), semuanya dari README.
- Tiap skill ditunjukkan sebagai DEMO kecil dengan contoh Indonesia (hook "Kenapa video kamu sepi, padahal upload tiap minggu?",
  judul "Konten Seminggu, Direkam Sehari", komentar penonton, niche "masak hemat anak kos"), bukan rekaman layar GitHub.
- Detail yang lebih jujur dari referensi: skor hook = heuristik (contoh angka, bukan prediksi), "rumus" di mesin viral = penilaian
  atas KATA di judul (sesuai fine print README), cara pasang menyebut "minta install" (sesuai README: tempel link + "Install this
  skill, then confirm /yt-script works"), dan perintahnya ditulis benar **/yt-script** (referensi menyebut "slash ytscript").
- Visual: gaya NAVY AI PRENEUR (panel kaca navy, aksen cyan, Poppins, robot + maskot), tanpa logo YouTube, tanpa maskot crab.
- CTA beda: "Komen YOUTUBE, aku kirim lewat DM."

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
Sumber utama: README repo **github.com/Jakeschincariol/youtube-agent-skill** (raw README + file skill di `skills/`), LICENSE.
| Klaim di VO / visual | Bunyi di sumber | Sumber |
|---|---|---|
| Nama "YouTube Agent Skill", 11 skill | "# The YouTube agent skill — Eleven Claude skills that run a YouTube channel." Tabel "The eleven": /yt-script, /yt-package, /yt-edit, /yt-comment, /yt-plan, /yt-viral, /yt-retention, /yt-shorts, /yt-seo, /yt-chapters, /yt-audit | README |
| Gratis, open source, tanpa daftar, tanpa API key | "Free, MIT, no signup, no API key, nothing to connect." LICENSE = MIT (© 2026 Jake Schincariol) | README, LICENSE |
| Naskah dari 21 rumus hook + skor hook sebelum rekaman | /yt-script: "Five hooks off 21 formulas, scored, then the spoken script…"; "scores the hook before you waste a take on it"; hooks.json berisi tepat 21 rumus (nama di reel = nama asli: The Statistic … The Direct Address); hookscore.py = panel 5 properti (SPECIFICITY, ADDRESS, STAKES, CURIOSITY, BREVITY), verdict 60% rata-rata + 40% terlemah, STRONG ≥ 72 | README, skills/yt-script/SKILL.md, hooks.json, hookscore.py |
| Judul + thumbnail ditulis sepasang | /yt-package: "Title and thumbnail as one pairing, linted for truncation, duplication and vagueness." Aturan title.py: 60 karakter (desktop), teks thumbnail tidak mengulang judul, maks 3 kata di thumbnail | README, skills/yt-package/SKILL.md |
| Transkrip → daftar potongan edit + timecode | /yt-edit: "A transcript into an edit decision list: dead air, filler cues, retakes, with timecodes." deadair.py menandai DEAD / FILLER / REPEAT; hening dipotong di tengah | README, skills/yt-edit/SKILL.md |
| Komentar dipilah, dibalas gaya bahasa kamu | /yt-comment: "The comment section triaged into four piles, then replies in your voice. Says which one to pin." 4 tumpukan: Questions, Corrections, Praise, Bait (bait tidak dibalas); suara dari ~/.claude/youtube/voice.md | README, skills/yt-comment/SKILL.md |
| Rencana upload seminggu sesuai waktu kamu | /yt-plan: "A week that fits the hours you actually have. One anchor, one cheap one, three Shorts." | README, skills/yt-plan/SKILL.md |
| Mesin viral: video di niche kamu yang ngalahin rata-rata channel-nya sendiri + nyebut rumus judulnya | About repo: "…and a virality engine"; /yt-viral: "What is working in your niche, ranked by multiple over each channel's own median"; "The formula line is a judgement about the TITLE, matched against the 21 formulas — not a claim about why the video worked" | README, skills/yt-viral/SKILL.md |
| Cara pasang: buka Claude Code, tempel link GitHub, minta install, ketik /yt-script | "Paste this into Claude: https://github.com/Jakeschincariol/youtube-agent-skill — Install this skill, then confirm /yt-script works." Alternatif: git clone + `cp -r youtube-agent-skill/skills/yt-* ~/.claude/skills/`, atau plugin (`/plugin marketplace add …`, `/plugin install youtube-agent`) | README |

Catatan klaim: "gratis" = pack-nya (MIT); Claude / Claude Code sendiri tetap butuh akun Claude — VO tidak mengklaim Claude gratis.
"rata-rata channel-nya" = bahasa lisan untuk "median channel" (layar menulis "× median channel"). Semua angka di demo (skor 82/90/70/86/74
→ 76 STRONG, 6,4× / 4,1× / 3,2× / 2,3×, 8 jam vs ± 7 jam, timecode, 12:40) adalah CONTOH ilustrasi yang konsisten satu sama lain dan
diberi label "contoh"; nama channel ("Dapur Kos Hemat", "Rantau Masak", "Bekal Sat Set", "Menu Hemat Harian", "Kanal Kreator Hemat"),
judul video dan handle "@penonton_01…06" dikarang dan generik. Tidak ada logo YouTube; tidak ada angka bintang GitHub (berubah-ubah).
README juga bilang: skill-nya hanya menulis, tidak meng-upload ("Nothing gets published until you do it") — tidak diklaim sebaliknya.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; tiap baris diawali tag `[playful] [excited]`)
1. Ngurus channel YouTube sendirian? Sebelas skill Claude gratis ini bantu dari naskah sampai ide viral.
2. Namanya YouTube Agent Skill: open source, tanpa daftar, tanpa API key.
3. Satu, naskah dari dua puluh satu rumus hook, plus skor hook-nya sebelum rekaman.  (caption: **21**)
4. Dua, judul dan thumbnail ditulis sepasang.
5. Tiga, transkrip jadi daftar potongan edit, lengkap dengan timecode.
6. Empat, komentar dipilah, lalu dibalas pakai gaya bahasa kamu.
7. Lima, rencana upload seminggu sesuai waktu kamu.
8. Paling seru, mesin viral: dia cari video di niche kamu yang ngalahin rata-rata channel-nya sendiri, terus nyebut rumus judulnya.
9. Cara pasang: buka Claude Code, tempel link GitHub-nya, minta install, terus ketik slash Y T script.  (caption: **/yt-script.**)
10. Komen YOUTUBE, aku kirim lewat DM.

Voice: `tools/voice_config.json` (voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75), dibuat dengan
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"`
(satu panggilan, 44,16 dtk) → `assets/audio/vo.mp3`. Cek pelafalan dengan faster-whisper small: semua baris terbaca (whisper menulis
"Claude" sebagai "cloud" dan "slash Y T script" sebagai "slash yeti script" — dibaca "ye-te", wajar untuk penonton Indonesia).
