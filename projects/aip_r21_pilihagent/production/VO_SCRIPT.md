# VO — R21 · 6 agent AI, pilih yang mana? (cloud vs open source vs pengatur) · background NAVY · 44,9 dtk VO (video 46,20 dtk)

Referensi: `aip_remake_batch6/refs/ref1.mp4` (106 dtk, bahasa Inggris, akun lain; abu-abu terang/hitam/ungu, serif besar, maskot tiap
produk, footage orang). Nama di transkrip rusak ("Grockbot", "Mousebot", "MetaMuse"); dari frame videonya terbaca jelas:
**OPENAI · Dots**, **META · Muse**, **SPACEXAI · Grok Bot**, **OPENCLAW FOUNDATION · MIT · OpenClaw**, **NOUS RESEARCH · MIT ·
Hermes-Agent**, **OPEN SOURCE · APACHE 2.0 · MausBot**. Keenam nama terverifikasi di sumber resmi (tabel di bawah) → hitungannya tetap
**enam**, tidak ada yang dibuang.

## ATM: what we changed (Amati · Tiru · Modifikasi)
**Amati (referensi):** hook taksonomi "Six AI agents, three run in someone else's cloud, three are open source, and one of them is
something else entirely" di atas grid 3×2 kartu maskot; struktur: tur satu per satu (Dots → Muse → Grok Bot → OpenClaw → Hermes →
MausBot), masing-masing halaman judul serif + kartu UI/footage; angka bintang GitHub (392k, 252k) dan "85K+ skills"; MausBot sebagai
"chief of staff" yang membagi kerja ke Claude Code / Codex / Grok; penutup daftar "So, which one?" lalu "MausBot is free and open source,
mausbot.com".
**Tiru (hanya ide + mekanisme):** enam agent dibagi dua kelompok (cloud orang vs open source) plus satu yang berbeda (pengatur).
**Modifikasi (wajib, semuanya dikerjakan):**
1. **Hook sendiri, sudut beda:** bukan taksonomi, tapi PERTANYAAN keputusan untuk penonton: "Enam agent AI lagi rame. Sebelum pilih,
   jawab ini dulu: tinggal pakai, atau pegang sendiri?" Visual: ledakan kartu notifikasi → kartu "1 pertanyaan" → JALAN BERCABANG dengan
   dua papan arah (Tinggal pakai · jalan di cloud mereka / Pegang sendiri · open source, di mesinmu) dan bulatan "KAMU" di persimpangan.
2. **Struktur + metafora sendiri:** bukan tur enam produk, tapi panduan memilih: cabang cloud (3 agent dalam SATU beat: awan dengan
   tiga kartu tergantung) → plus-minusnya (laptop ditutup sementara "komputer cloud" tetap kerja; data & login terbang masuk ke awan)
   → cabang open source (kunci diputar, batas putus-putus "MESINMU", laptop + server) → satu beat untuk OpenClaw (chat dari WhatsApp,
   mock HP buatan kita) dan Hermes (laci skill: tugas selesai → "skill baru") → kehati-hatian (sakelar setelan `tools.exec.mode`
   full → ask) → MausBot satu beat (hub dengan jari-jari ke agent yang sudah kamu punya) → aturan memilih (slider PRAKTIS | KENDALI
   yang membalik kartu jawaban) → CTA. Gaya NAVY AI PRENEUR; ikon Lucide generik, nama produk hanya teks — tanpa logo/maskot produk,
   tanpa grid 3×2, tanpa halaman judul serif, tanpa palet merah/ungu/kuning referensi, tanpa footage, tanpa daftar "So, which one?".
   Beda dari R15 (OpenMausBot + Hermes sebagai "kantor + karyawan"): tidak ada metafora kantor/karyawan/ID card/SKILL.md revisi;
   OpenMausBot dan Hermes masing-masing cuma satu beat.
3. **Sudut praktisi:** TIDAK ada klaim "aku pakai ini" — tidak terverifikasi bahwa Freddie memakai salah satu dari enam agent ini, jadi
   tidak dikarang. Suara tetap praktis: pertanyaan yang harus dijawab dulu, plus-minus, setelan yang harus diganti.
4. **Nilai tambah untuk penonton Indonesia (yang tidak ada di referensi):** Muse **belum tersedia di Indonesia**; Dots & Grok Bot
   berbayar, Muse gratis untuk dasar; plus-minus jujur (cloud: praktis & jalan terus walau laptop mati, tapi data + login aplikasimu
   disimpan di server mereka; open source: kendali di tanganmu, tapi rawat & keamanannya juga tanggung jawabmu); **koreksi izin bawaan
   OpenClaw** dengan perintah persisnya `openclaw config set tools.exec.mode ask`; di layar juga: bawaan OpenMausBot "Full access →
   pilih Ask"; contoh UMKM di chat ("rekap pesanan hari ini?", berlabel CONTOH); aturan memilih satu kalimat (praktis → cloud,
   kendali → open source).
5. **CTA + penutup sendiri:** "Komen PILIH, aku kirim lewat DM." + kartu "Tabel pilih 6 agent · + link resmi & setting aman" (referensi:
   "MausBot is free and open source, mausbot.com").
**Cek kata:** referensi berbahasa Inggris, naskah kita bahasa Indonesia — run kata sama terpanjang = 2 ("open source"), dicek otomatis
setelah normalisasi (batas: tidak lebih dari 3).

## Klaim referensi yang DIBUANG / DIKOREKSI
- "392k GitHub stars" (OpenClaw), "252k GitHub stars" (Hermes), "85K+ skills on ClawHub", "biggest community" → tidak dipakai (angka
  berubah-ubah / tidak dicek). Tidak ada angka bintang di layar.
- "three run in someone else's cloud" untuk Dots/Muse/Grok Bot → dipertahankan sebagai FAKTA yang dicek (tiap agent punya komputer/VM
  cloud sendiri), ditambah konsekuensinya yang tidak disebut referensi: data + login aplikasi yang kamu sambungkan ada di server mereka.
- "It can even add Hermes and OpenClaw to the team" (MausBot) → Hermes TERVERIFIKASI (engine "Hermes · ACP integration"), OpenClaw
  TIDAK ada di tabel engine OpenMausBot → di layar hanya Claude Code, Codex, Grok CLI, Hermes.
- "A chief of staff bot hands out the work… approve from your desktop or your phone" → fitur Chief of Staff dan akses HP memang ada di
  README, tapi tidak dipakai (menghindari visual referensi); kita: "pengatur agent yang kamu punya" + hub dengan denyut "bagi tugas".
- "mausbot.com" → tidak dipakai; README resmi menautkan **openmausbot.com** dan repo `github.com/milind-soni/OpenMausBot` (catatan R15:
  ada repo tiruan bernama mirip; link DM harus repo resmi).
- "SPACEXAI" sebagai pembuat Grok Bot → di layar ditulis domain resminya **x.ai** (halaman x.ai sendiri kini memakai nama SpaceXAI;
  nama perusahaan tidak diucapkan di VO).

## Fakta yang dicek (sumber resmi, dicek 13 Nov 2026)
Catatan akses: dari sesi ini openai.com dan x.ai tidak bisa di-fetch langsung (DNS diblokir jaringan sesi); isi halaman resminya dibaca
lewat indeks pencarian yang dibatasi ke domain resmi (help.openai.com, openai.com, about.fb.com, muse.ai, x.ai, docs.x.ai). Tiga repo
open source di-clone langsung dari GitHub (sparse: README, LICENSE, docs) ke scratch dan dibaca.

| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| **Dots dari OpenAI**, agent di ChatGPT yang jalan terus | (parafrase) dot = agent "always-on" di ChatGPT yang bekerja di antara percakapan; "Give your dot a goal, connect the apps it needs, and define what it can do on its own." Rilis 29 Sep 2026 (release notes). | help.openai.com/en/articles/20001530-getting-started-with-your-dot · openai.com/index/introducing-dots/ · help.openai.com ChatGPT release notes |
| Dots: komputer cloud sendiri | (parafrase halaman peluncuran) tiap dot bekerja di komputer cloud-nya sendiri; komputermu terpisah kecuali kamu sambungkan (akses lokal opsional, mati di awal) | openai.com/index/introducing-dots/ · help.openai.com (getting started with your dot) |
| Dots: berbayar | "Dots are rolling out in ChatGPT to Pro users aged 18 and older in markets excluding the European Economic Area, Switzerland, and the UK"; juga Business Premium ("supported ChatGPT regions") | help.openai.com (getting started / managing dots in workspaces) |
| (catatan, tidak di VO) Dots minta izin | "Dots start with built-in rules for when to act independently and when to ask for approval. Custom Rules let you allow specific actions, require approval, or block them."; auto-review; "Certain sensitive tasks, such as changing a password, always stay with you." | help.openai.com |
| **Muse dari Meta**, agen personal | "Introducing Muse: The World's First Personal AI Agent Built for Everyone" (8 Sep 2026); "Muse is a personal AI agent. It doesn't just answer questions, it actually does the work." | about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ |
| Muse: mesin virtual di cloud | "Muse runs on Muse Secure VM, a dedicated, virtual machine (VM) that houses both the agent and a person's data."; "OAuth tokens for third-party services you choose to connect – these are stored in your VM" | about.fb.com (Introducing Muse) · muse.ai/security-and-privacy |
| Muse: gratis untuk dasar | "free for most of what people need, with subscription plans for people who want to do more" | about.fb.com (Introducing Muse) |
| **Muse belum ada di Indonesia** | Peluncuran: "available in the US and Canada"; Okt 2026: "Muse Is Now Available in Singapore"; Muse for Small Business: "available today to people in the US and Canada… working to bring Muse to more markets". Tidak ada pengumuman Indonesia per 13 Nov 2026. | about.fb.com (Introducing Muse; …/2026/10/muse-is-now-available-in-singapore…; …/introducing-muse-small-business/) |
| **Grok Bot**, tim bot (x.ai) | "AI teammates that finish the work"; "Introducing Grok Bot"; create and manage Bots | x.ai/bot · x.ai/news/introducing-grok-bot · docs.x.ai/grok-bot/bots |
| Grok Bot: komputer cloud bersama, jalan saat laptop tertutup | "every Bot on your account uses one persistent cloud computer" (file, sesi browser, login dibagi antar Bot); FAQ (parafrase): menutup app/laptop/HP tidak menghentikan tugas atau rutinitas yang berjalan di latar; komputer cloud-nya berlokasi di AS (parafrase FAQ) | docs.x.ai/grok-bot/how-grok-bot-works · docs.x.ai/grok-bot/faq · docs.x.ai/grok-bot/skills-routines-and-automations |
| Grok Bot: berbayar | termasuk paket X Subscription Premium, Super, Ultra (tidak di Plus/Free); halaman harga: SuperGrok mencakup Grok Bot | docs.x.ai/grok-bot/faq · x.ai/news/x-subscription · x.ai/pricing |
| "kerja terus di cloud mereka, tapi data dan login aplikasimu ikut di sana" | Dots: komputer cloud sendiri + aplikasi tersambung; Muse: VM berisi agent + data, token OAuth di VM; Grok Bot: satu komputer cloud persisten, login dibagi | sumber di atas |
| **OpenClaw**, open source (MIT, OpenClaw Foundation) | LICENSE: "MIT License · Copyright (c) 2026 OpenClaw Foundation"; README: "OpenClaw is an open-source AI assistant that runs on your own computer…" | github.com/openclaw/openclaw (commit d5d77e1, 13 Nov 2026) — README, LICENSE |
| OpenClaw dichat dari WhatsApp | "meets you in the channels you already use: Discord, iMessage, Slack, Teams, Telegram, WhatsApp, and 20+ more" | README |
| Laptop atau server | "One Gateway runs it as a personal claw on a laptop or as a shared multiplayer claw"; installer macOS/Linux/Windows; Docker/VPS docs | README · docs/vps.md |
| **Bawaan OpenClaw jalanin perintah tanpa nanya** | `exec.security`: "Default is `full` for gateway/node hosts" (full = "do not require an allowlist match"); `exec.ask`: "Default is `off`" ("off – no ordinary policy prompts"); README: "Tools run on the host for the main session unless you configure sandboxing." | docs/tools/exec-approvals.md · README (Security) |
| **Ubah ke mode ask** + perintahnya | `tools.exec.mode`: `ask` = allowlist / on-miss, "Run allowlist matches; ask a human on misses"; `full` = "Run host exec without ordinary policy prompts"; contoh resmi `openclaw config set tools.exec.mode auto` (nilai `ask` di kunci yang sama) | docs/tools/permission-modes.md |
| **Hermes**, open source (MIT, Nous Research) | "The self-improving AI agent built by Nous Research"; LICENSE MIT © 2025 Nous Research | github.com/NousResearch/hermes-agent (commit 9d94f82, 13 Nov 2026) — README, LICENSE |
| Hermes nulis skill dari pengalamannya | "it creates skills from experience, improves them during use"; "Autonomous skill creation after complex tasks. Skills self-improve during use." | README |
| Hermes di laptop atau server | installer Linux/macOS/WSL2/Windows; "Run it on a $5 VPS, a GPU cluster…" (angka tidak dipakai) | README |
| (catatan, tidak di VO) penjaga perintah Hermes | `approvals.mode` default `smart`: "Use an auxiliary LLM to assess risk… Uncertain cases escalate to a manual prompt."; `manual` = selalu tanya | website/docs/user-guide/security.md |
| **MausBot**: bukan agent baru, pengatur agent yang kamu punya | "Also known as MausBot; formerly OpenGrokBot"; "Bring your own agents. Bots run on the `claude`, `codex`, and `grok` CLIs installed on your own machine — your existing logins and subscriptions"; tabel engine: "Hermes · Hermes CLI login · ACP integration" | github.com/milind-soni/OpenMausBot (commit d76d024, 13 Nov 2026) — README · apps/docs/content/docs/providers/index.mdx |
| MausBot open source, Apache 2.0 | LICENSE: Apache License 2.0 | LICENSE |
| (layar) bawaan MausBot Full access → pilih Ask | "Every bot and conversation starts at **Full access**… On a hosted company workspace the default stays Ask"; level "Ask for approval" | docs/approval-levels.md |

Contoh di layar (isi chat "rekap pesanan hari ini?" / "12 pesanan, 3 belum bayar", tugas "cek email pelanggan / rekap pesanan / kirim
laporan", "rekap stok mingguan", perintah `rm -r arsip-lama/`) adalah ilustrasi dan diberi label CONTOH. Kartu agent, HP, sakelar
setelan, hub dan slider adalah mock buatan kita (ikon Lucide generik), bukan screenshot atau logo produk. Nama Claude Code / Codex /
Grok CLI / WhatsApp hanya teks.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = tag AUTO klien)
Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (SATU panggilan,
44,88 dtk, tanpa re-take) → `assets/audio/vo.mp3`. Kata kunci dikirim huruf kecil ("pilih") supaya tidak dieja; caption menampilkan
PILIH. Tag yang benar-benar dipakai (dari `production/vo_el.json`):
1. `[playful] [excited] [curious]` Enam agent AI lagi rame. Sebelum pilih, jawab ini dulu: tinggal pakai, atau pegang sendiri?
2. `[playful] [excited]` Tinggal pakai: Dots dari OpenAI, Grok Bot, dan Muse dari Meta, yang belum ada di Indonesia.
3. `[playful] [excited]` Praktis, kerja terus di cloud mereka, tapi data dan login aplikasimu ikut di sana.
4. `[playful] [excited]` Pegang sendiri: OpenClaw dan Hermes, open source di laptop atau servermu.
5. `[playful] [excited]` OpenClaw kamu chat dari WhatsApp, Hermes nulis skill dari pengalamannya.
6. `[playful] [excited]` Kendalinya di tanganmu, keamanannya juga. Bawaan OpenClaw jalanin perintah tanpa nanya, ubah ke mode ask.
7. `[playful] [excited]` Yang keenam beda: MausBot. Bukan agent baru, tapi pengatur agent yang kamu punya.
8. `[playful] [excited]` Jadi, mau praktis, pilih cloud. Mau kendali, pilih open source.
9. `[playful] [excited] [confident]` Komen PILIH, aku kirim lewat DM.   (dikirim: "Komen pilih, aku kirim lewat DM.")

Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, auto tags).
Cek dengar dengan faster-whisper **small** dan **medium** (bahasa id) — tidak ada kata yang salah dengar di KEDUA model, jadi tidak ada
re-take: "Dots" (small ✓ / medium "Dodge"), "OpenClaw" (small "OpenCloud" / medium ✓), "tanpa nanya" (small "tanpanannya" / medium ✓),
"MausBot" → "mousebot" di keduanya (= cara baca namanya), "Grok Bot" → "grogbot/Grokbot", "mode ask" ✓, "pilih" ✓.
