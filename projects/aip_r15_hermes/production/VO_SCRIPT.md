# VO — R15 · Duo agent AI open source: kantor + karyawan (OpenMausBot + Hermes Agent) · background NAVY · 48,5 dtk VO (video 49,80 dtk)

Referensi: `aip_remake_batch5/refs/ref5.mp4` (61 dtk, ID, merah/hitam + maskot bola merah, akun lain). Nama di transkrip referensi
rusak ("Mousebot", "Grogbot", "DeepSync Flash"); dari frame videonya (judul "MausBot · rumah untuk tim AI-mu", screenshot app dengan
sidebar bot, avatar Hermes) dan dari GitHub, aplikasinya adalah **OpenMausBot** (alias **MausBot**, dulu OpenGrokBot) dan mesinnya
**Hermes Agent** dari **Nous Research**.

## ATM: what we changed (Amati · Tiru · Modifikasi)
**Amati (referensi):** hook kompetisi "Kombinasi gila, 2 agent AI ini bisa kalahkan Dots, Muse, dan Grok Bot" + "dua-duanya gratis";
struktur: kartu maskot pesaing → rumah (MausBot) → mesin (Hermes, kartu skill Lv1→Lv3) → "Kelebihan lainnya?" → 01 Biaya (login
ChatGPT, grafik skor Grok vs DeepSeek "10× lebih murah") → 02 Semuanya milikmu (laptop + gembok, pesaing "melatih model", dialog izin
`rm -rf`) → layar gelap "Tapi minusnya?" (laptop nyala 24 jam, CVE, mode YOLO) → penutup filosofis "bukan mana yang paling pintar, tapi
siapa yang kamu izinkan memegang datamu?" → "Follow aiShift.id".
**Tiru (hanya ide + mekanisme):** pasangan "aplikasi tim bot + mesin agent", beat plus-minus yang jujur.
**Modifikasi (wajib, semuanya dikerjakan):**
1. **Hook sendiri, sudut beda:** bukan "mengalahkan produk X", tapi soal LOKASI data: "Tim AI kamu numpang di server siapa? Duo open
   source ini jalanin agennya di laptopmu." Visual: rak "server orang lain" → laptop "LAPTOP KAMU · 127.0.0.1".
2. **Struktur + metafora sendiri:** kantor (OpenMausBot) → karyawan (Hermes) → nota biaya → otak (model) → data: yang tinggal vs yang
   terkirim → level izin → minus → urutan setting → CTA. Metafora kita "kantor + karyawan + otak" (referensi: "rumah + mesin"). Visual
   per beat milik kita: meja kerja → app chat (mock buatan sendiri), ID card karyawan + stempel DITERIMA + SKILL.md dengan revisi, nota
   dengan stempel GRATIS, terminal `hermes model`, meter pemakaian DeepSeek, panel "DI LAPTOPMU" vs awan "penyedia model", sakelar
   "Ask for approval | Full access", jadwal yang TERLEWAT saat laptop tidur, checklist keamanan, 4 langkah setup. Tanpa warna merah/hitam,
   tanpa maskot/kartu/ikon referensi, tanpa logo pihak ketiga (OpenAI/DeepSeek/Nous ditulis teks saja). Gaya NAVY AI PRENEUR.
3. **Sudut praktisi:** TIDAK ada klaim "aku pakai ini" — tidak terverifikasi bahwa Freddie memakai pasangan ini, jadi tidak dikarang.
   Suara tetap praktis: urutan setting, langkah yang sering dilewatin, apa yang harus kamu jaga.
4. **Nilai tambah untuk penonton Indonesia (yang tidak ada di referensi):** contoh tim UMKM (Admin Email balas email pelanggan, Rekap
   Penjualan, Riset Harga, Konten IG — diberi label contoh); biaya yang jujur (aplikasi Rp0, model tetap bayar); KOREKSI privasi
   (skill/memori/riwayat memang di laptop, tapi isi pesan tetap dikirim ke penyedia model — referensi menyiratkan data tidak keluar);
   langkah yang dilewatin referensi (OpenMausBot default-nya **Full access** → ganti ke **Ask for approval**; plus `approvals.mode: manual`
   di Hermes); peringatan unduh hanya dari repo resmi + "tidak ada token kripto resmi" (README OpenMausBot); opsi pasang di server sendiri;
   urutan setting 4 langkah.
5. **CTA + penutup sendiri:** "Mau link resmi plus urutan setting-nya?" → "Komen AGENT, aku kirim lewat DM." (referensi: pertanyaan
   filosofis + "Follow aiShift.id").
**Cek kata:** tidak ada lebih dari 3 kata berurutan yang sama dengan transkrip referensi (dicek otomatis setelah normalisasi; run terpanjang
= 3: "API key atau"). Versi awal baris 5 ("…tanpa API key. Atau…" = 4 kata sama) sudah diganti "nggak perlu API key" dan VO dibuat ulang.

## Klaim referensi yang DIBUANG / DIKOREKSI
- "bisa kalahkan Dots, Muse, dan Grok Bot" — tidak ada perbandingan yang bisa diverifikasi → dibuang (README OpenMausBot hanya menyebut
  dirinya alternatif open source, bukan "mengalahkan").
- Grafik "Skor Kecerdasan · Biaya: Grok 4.7 = 46 / $2,73 vs DeepSeek Flash = 45 / $0,26 · ±10× lebih murah" — tidak diverifikasi → dibuang;
  tidak ada angka harga/skor sama sekali. Nama model "DeepSeek Flash" tidak dipakai; cukup "DeepSeek" (provider resmi di docs Hermes).
- "Dua-duanya gratis" → dikoreksi: aplikasinya gratis (Apache-2.0 / MIT), **modelnya tetap bayar** (langganan ChatGPT, atau API DeepSeek
  bayar per pemakaian).
- "datamu tetap di komputermu, bukan di server mereka, yang bahkan bisa jadi bahan latihan modelnya" → dikoreksi: file skill, memori,
  riwayat chat tersimpan lokal, **tetapi isi pesan tetap dikirim ke penyedia model**; klaim soal "dipakai melatih model" (tentang produk
  lain) dibuang.
- "Tiap perintah pun minta izinmu dulu" → tidak benar secara default: OpenMausBot memulai tiap bot di **Full access**, dan Hermes (mode
  `smart`) hanya bertanya untuk perintah berbahaya yang meragukan. Kita bilang: ganti ke **Ask**, biar aksi berisiko nunggu izinmu.
- "kamu mungkin sudah punya salah satunya", "CVE-2026-…", "mode YOLO", "bot jalan 24 jam" → tidak dipakai (diganti: jadwal hanya jalan
  selama laptop/app nyala, atau pasang di server sendiri).

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| OpenMausBot = aplikasi chat berisi tim bot ("kantor") | "The open-source Grok Bot alternative: your own team of AI bots, in a chat app." "Also known as **MausBot**; formerly **OpenGrokBot**." | github.com/milind-soni/OpenMausBot — README |
| Open source, Apache-2.0, gratis | LICENSE = Apache License 2.0 (© 2026 Milind Soni and OpenMausBot contributors; folder `enterprise/` lisensi terpisah). "OpenMausBot is free and open source." | README, LICENSE |
| Agennya jalan di laptopmu (127.0.0.1), riwayat chat di `~/.openmausbot/` | "Bots run on the `claude`, `codex`, and `grok` CLIs installed on your own machine"; "One small harness server on `127.0.0.1` owns every agent process. Transcripts, keys, and events live in `~/.openmausbot`, not a cloud." | README ("Why") |
| Hermes bisa jadi mesin bot di OpenMausBot | Tabel "Built-in engines": "Hermes · Hermes CLI login · ACP integration"; driver `server/drivers/acp/hermes.ts` ("Hermes Agent (Nous Research's `hermes acp`)"); "Every bot can use a different engine and model." | OpenMausBot `apps/docs/content/docs/providers/index.mdx`, `server/drivers/acp/hermes.ts` |
| Default Full access → ganti ke Ask | "Every bot and conversation starts at **Full access** … each engine runs in its own most permissive mode." Level: "Ask for approval" / "Full access"; untuk Hermes: Ask = default Hermes sendiri, Full access = OpenMausBot menyetujui permintaan izin ACP secara otomatis. | OpenMausBot `docs/approval-levels.md` |
| Kartu izin "Allow/Deny" | "Shell commands, file edits, and questions surface as inline cards — Allow / Deny … A permission broker turns every risky action into a decision you make" | README (Features) |
| Hermes Agent dari Nous Research, MIT, open source | "Hermes Agent ☤ … The self-improving AI agent built by Nous Research"; LICENSE MIT (© 2025 Nous Research) | github.com/NousResearch/hermes-agent — README, LICENSE |
| Hermes nulis skill dari pengalaman, makin lancar di tugas berulang | "creates skills from experience, improves them during use"; "Autonomous skill creation after complex tasks. Skills self-improve during use." | README |
| Skill di `~/.hermes/skills/`, memori di `~/.hermes/memories/` | "All skills live in `~/.hermes/skills/`"; "Both are stored in `~/.hermes/memories/`" | hermes-agent `website/docs/user-guide/features/skills.md`, `…/memory.md` |
| Lewat ACP, Hermes tetap pakai memori + skill-nya | "Hermes … keep its existing identity, provider setup, memory, skills, and tools while another application owns the conversation transport"; ACP config memakai `~/.hermes/skills/` | `website/docs/user-guide/features/acp.md` |
| Login pakai langganan ChatGPT, nggak perlu API key (`hermes model`, buka link + kode) | "OpenAI Codex · `hermes model` → **ChatGPT or Codex Subscription** (ChatGPT OAuth, uses Codex models)"; "authenticates via device code by default (open a URL, enter a code)". Tier paket yang berlaku: "not currently documented" → di VO hanya "langganan ChatGPT". | `website/docs/integrations/providers.md` |
| Atau DeepSeek, bayar per pemakaian | "DeepSeek · `DEEPSEEK_API_KEY` in `~/.hermes/.env` (provider: `deepseek`)" — API key = tagihan per pemakaian; TANPA angka harga | `website/docs/integrations/providers.md` |
| Perintah berisiko dicek; `curl … \| sh` termasuk; `approvals.mode: manual` | "Before executing any command, Hermes checks it against a curated list of dangerous patterns"; modes `smart` (default) / `manual` ("Always prompt the user for approval on dangerous commands") / `off`; pola "`curl ... \| sh` — Pipe remote content to shell"; opsi ACP: allow once / allow always / deny | `website/docs/user-guide/security.md`, `…/features/acp.md` |
| Minus: jadwal hanya jalan selama mesin nyala; bisa di server sendiri | "OpenMausBot must remain running to accept a delivery"; "For a server on a VPS or an always-on computer, run `npx openmausbot serve`"; Hermes: "Run it on a $5 VPS…" (angka tidak dipakai) | OpenMausBot README (Triggers, Run on a server); Hermes README |
| "Tak ada token kripto resmi" · repo resmi | "OpenMausBot has no token. Any coin using the OpenMausBot, Maus, or SupaMaus name is not created, endorsed, or affiliated with this project" | OpenMausBot README |
Catatan: situs openmausbot.com / mausbot.com tidak bisa diakses dari sesi ini (jaringan); semua fakta OpenMausBot diambil dari repo GitHub
resminya (README, LICENSE, docs). Jumlah bintang GitHub tidak dipakai (berubah-ubah). Ada repo lain bernama mirip (mis. `OpenMausBot/OpenMausBot`:
README disalin, hanya 7 commit, tombol "latest release" ke rilisnya sendiri, lisensi di sidebar tidak konsisten) — itu BUKAN repo tempat kodenya
dikembangkan; link yang dikirim lewat DM harus `github.com/milind-soni/OpenMausBot` (rilis resmi: `github.com/milind-soni/OpenMausBot/releases`)
dan `github.com/NousResearch/hermes-agent`. Ini alasan peringatan "download dari repo resmi" di reel.
Semua contoh di layar (nama bot, tugas, email, jam jadwal, langkah SKILL.md, rev 1–3, perintah `curl` sebagai contoh perintah berisiko)
adalah ilustrasi dan diberi label "contoh".

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = tag AUTO klien)
Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan,
48,48 dtk) → `assets/audio/vo.mp3`. Tag yang benar-benar dipakai (dari `production/vo_el.json`):
1. `[playful] [excited]` Tim AI kamu numpang di server siapa? Duo open source ini jalanin agennya di laptopmu.
2. `[playful] [excited]` OpenMausBot jadi kantornya: aplikasi chat, tiap bot pegang satu tugas, misalnya balas email pelanggan.
3. `[playful] [excited]` Hermes dari Nous Research jadi karyawannya: dia nulis skill dari pengalaman, jadi tugas berulang makin lancar.
4. `[playful] [excited]` Kantor dan karyawannya gratis, otaknya yang bayar.
5. `[playful] [excited]` Login pakai langganan ChatGPT, nggak perlu API key. Atau DeepSeek, bayar per pemakaian.
6. `[playful] [excited]` Skill, memori, dan riwayat chat ada di laptopmu, tapi pesanmu tetap dikirim ke penyedia model.
7. `[playful] [excited]` Yang sering dilewatin: default-nya akses penuh. Ganti ke Ask, biar aksi berisiko nunggu izinmu.
8. `[playful] [excited]` Minusnya, laptop harus tetap nyala biar jadwalnya jalan, dan keamanannya kamu yang jaga.
9. `[playful] [excited] [curious]` Mau link resmi plus urutan setting-nya?
10. `[playful] [excited] [confident]` Komen AGENT, aku kirim lewat DM.

Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, auto tags).
Cek pelafalan dengan faster-whisper small (bahasa id): semua baris terbaca; whisper menulis "OpenMausBot" → "Open mousebot", "Nous" →
"Nose" (dibaca "nus", wajar), "Minusnya" → "Minisnya" (cepat, tetap jelas di telinga), "DeepSeek" → "deep seek".
