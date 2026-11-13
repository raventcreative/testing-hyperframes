# VO — R23 · Biar agent AI nggak asal ubah file: rencana dulu (OpenCode + Hermes) · background NAVY · 42,2 dtk VO (video 43,57 dtk)

Referensi: `aip_remake_batch6/refs/ref3.mp4` (125 dtk, bahasa Indonesia, kreator lain; latar krem + aksen merah, karakter pixel,
robot isometrik + kubus warna). Nama di transkrip: "Hermes" dan "Open Code"; di frame terbaca wordmark **HERMES-AGENT** dan
**opencode** → alatnya **Hermes Agent** (Nous Research) dan **OpenCode** (open source AI coding agent). Keduanya dicek di repo resminya.

## ATM: what we changed (Amati · Tiru · Modifikasi)
**Amati (referensi):** hook "ada dua AI agent gratis yang sudah lama ada, tapi masih jarang dikenal" + janji "di akhir video ini kamu
kenal keduanya dan tahu satu kebiasaan penting"; lalu salam + daftar ucapan terima kasih (TIDAK dipakai); struktur: kenalan pelan-pelan →
"AI agent itu seperti badan, kepintarannya dari model" (robot isometrik + kubus model) → kemampuan (kerja di folder: baca/tulis/jalankan,
coding, skill, bagi tugas ke beberapa agent, terminal/desktop) → baru di detik ±75 satu kebiasaan "minta rencana dulu, baru kerjakan"
(OpenCode mode plan, Hermes `/plan`; kamu baca, cek, izinkan; "file kamu aman") → "dua-duanya gratis dan open source, model ada yang
gratis ada yang bayar" → polling video berikutnya ("Hermes atau Open Code dulu?") + traktir kopi + follow.
**Tiru (hanya ide + mekanisme):** dua agent open source gratis yang sama-sama punya fitur rencana, plus satu kebiasaan: minta rencana,
baca, setujui, baru jalan.
**Modifikasi (wajib, semuanya dikerjakan):**
1. **Hook sendiri, sudut beda:** bukan "agent yang jarang dikenal", tapi MASALAH yang diselesaikan kebiasaan itu, dengan contoh UMKM:
   "Pernah suruh agent AI benerin satu tombol WhatsApp, malah lima file ikut berubah?" Visual: kartu web `tokokue.id` (CONTOH) dengan
   tombol hijau "Pesan via WhatsApp" + panel gelap "FILE YANG BERUBAH" (1 diminta + 5 ikut, tag amber), judul "Cuma minta 1 tombol…" →
   "…kok 5 file berubah?".
2. **Struktur + metafora sendiri:** KEBIASAANNYA jadi pahlawan dan dibuka di 12 detik pertama (referensi baru masuk di detik 75):
   masalah → metafora **tukang: gambar denah dulu, baru bongkar tembok** (cetak biru menggambar dirinya, pintu baru ditandai, lalu hanya
   bata di dalam tanda yang dibongkar) → aturan "Rencana dulu, baru kerja." dengan **palang (boom gate)**: agent menunggu, lembar
   RENCANA masuk slot, lampu hijau, palang naik, agent masuk ke FOLDER PROYEK → baru "di mana"-nya: OpenCode + Hermes (kartu baris,
   lencana cetak biru "MODE RENCANA": `Plan` / `/plan`) → kerja di folder + model bebas (folder `toko-kue/`, pemilih model buatan sendiri)
   → cara di OpenCode (sakelar Build | Plan + tombol Shift+Tab, kolom BACA/EDIT, pensil ditolak gembok) → cara di Hermes (bar perintah
   `/plan …`, dokumen rencana terbuka sebagai file `.hermes/plans/…md`, cap "BELUM DIKERJAKAN · 0 file diubah") → **cek 3 hal** dengan
   lensa (dan temuan: `style.css` ikut terdaftar) → **coret denah itu murah, bongkar tembok itu mahal** (pena merah mencoret `style.css`
   vs tembok bata-kode yang runtuh) → cap "DISETUJUI", OpenCode Plan → Build / Hermes "jalankan rencananya", progres 3/3 → CTA.
   Metafora "badan vs otak" referensi TIDAK dipakai (juga sudah dipakai R20); "kantor/karyawan" R15 juga tidak. Semua visual milik kita,
   gaya NAVY AI PRENEUR: tanpa krem/merah, tanpa karakter pixel, tanpa robot isometrik/kubus, tanpa stepper "rencana dulu → baru
   kerjakan", tanpa terminal gelap bertab "opencode | mode", tanpa checklist "kamu baca / kamu cek / sudah cocok" + tombol merah
   "Izinkan bekerja", tanpa kartu gembok "FILE AMAN", tanpa wordmark/logo alat (nama ditulis teks Poppins saja), tanpa kartu ucapan
   terima kasih/kopi/follow.
3. **Sudut praktisi:** TIDAK ada klaim "aku pakai OpenCode/Hermes" — tidak terverifikasi bahwa Freddie memakai keduanya, jadi tidak
   dikarang. Suaranya tetap praktisi: apa yang diklik, apa yang dicek, kapan baru boleh jalan.
4. **Nilai tambah untuk penonton Indonesia (yang tidak ada di referensi):** contoh UMKM (toko kue, tombol "Pesan via WhatsApp",
   folder `toko-kue/`, semua berlabel CONTOH); **checklist 3 hal** sebelum menyetujui (file yang disentuh, yang dihapus, cara ngetes)
   lengkap dengan contoh temuan (file yang tidak diminta ikut masuk rencana); alasan ekonominya (revisi rencana 1 baris vs bongkar kode);
   langkah persis di tiap alat (OpenCode: agent **Plan**, Shift+Tab di OpenCode 2.x — versi lama Tab; Hermes: perintah bawaan **`/plan`**,
   hasilnya file Markdown di `.hermes/plans/`); lalu cara "menyetujui" di tiap alat (balik ke **Build** / minta Hermes menjalankan
   rencananya); kejujuran soal biaya (aplikasinya gratis, **biaya ikut model yang kamu pilih**; model lokal lewat Ollama/LM Studio).
5. **CTA + penutup sendiri:** "Komen PLAN, aku kirim lewat DM." + kartu "Template “rencana dulu” + cara pakai di OpenCode & Hermes"
   (referensi: polling "Hermes atau Open Code dulu?", traktir kopi, follow).
**Cek kata:** tidak ada lebih dari 3 kata berurutan yang sama dengan transkrip referensi maupun teks layar referensi yang terbaca
(dicek otomatis setelah normalisasi, `scratchpad/r23/overlap.py`): run terpanjang = **2 kata** ("dulu, baru"). Versi awal baris 8
("file yang diubah" = 3 kata sama dengan teks layar referensi "belum ada file yang diubah") sudah diganti "file yang disentuh" SEBELUM VO
dibuat. Dengan R15/R19/R20 yang sama hanya kalimat CTA rumah ("aku kirim lewat DM").

## Klaim referensi yang DIBUANG / DIKOREKSI
- "sudah lama ada, tapi masih jarang dikenal" — tidak bisa diverifikasi → dibuang.
- "AI agent itu seperti badan, kepintarannya datang dari model" — metafora tidak dipakai (R20 sudah memakai "badan vs otak"); cukup
  "modelnya bebas kamu pilih".
- "Mau pakai Claude, GPT, Gemini, atau model gratis" — layar hanya menampilkan pilihan yang ada di docs KEDUA alat: Claude (Anthropic),
  GPT (OpenAI · ChatGPT), Model lokal (Ollama · LM Studio) + "biaya ikut model yang kamu pilih". Gemini tidak ditampilkan (tidak dicek di
  docs Hermes).
- "Dengan cara ini, AI menyusun rencananya dulu, tanpa mengubah apa pun … jadi file kamu aman" → dikoreksi/diperjelas: agent Plan di
  OpenCode memang tidak mengedit file proyek biasa, tapi **boleh menulis file rencananya sendiri** dan perintah shell tetap mengikuti
  setelan izin (catatan kecil di layar); `/plan` di Hermes adalah instruksi "planning only, no execution" + rencana disimpan ke file —
  bukan gembok teknis (dicatat di NOTES/DM). Tidak ada klaim "pasti aman".
- "Dua-duanya gratis dan open source" → benar untuk aplikasinya (lisensi MIT keduanya), tapi model bisa berbayar → di layar "biaya ikut
  model yang kamu pilih".
- "bisa coding, membangun aplikasi atau website, sampai memperbaiki error" — tidak dipakai sebagai klaim terpisah.
- Salam, nama kreator, daftar terima kasih, traktir kopi, "follow …", polling video berikutnya — tidak dipakai.

## Fakta yang dicek (sumber resmi, dicek 13 Nov 2026)
OpenCode: repo **github.com/anomalyco/opencode** (`github.com/sst/opencode` mengarah ke README yang sama), dibaca dari clone (commit
5b131f5, 13 Nov 2026) + registry npm. opencode.ai diblokir proxy sesi ini → docs dibaca dari sumbernya di repo
(`services/site/src/docs/content/*.mdx` = docs versi 2, `services/site/src/docs/v1/content/*.mdx` = docs versi 1).
Hermes Agent: repo **github.com/NousResearch/hermes-agent**, dibaca dari clone (commit 9d94f82, 13 Nov 2026); hermes-agent.nousresearch.com
diblokir proxy → docs dibaca dari `website/docs/**` di repo (sumber situs docs-nya).
| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| OpenCode = agent AI open source | "The open source AI coding agent."; Intro: "OpenCode is an open source coding agent. It's available as a terminal-based interface, desktop app, or web app." | README; docs v2 `index.mdx` |
| OpenCode lisensi MIT, gratis | LICENSE: "MIT License · Copyright (c) 2025 opencode"; npm `@opencode/cli` 2.3.0 (13 Nov 2026) license MIT | LICENSE; registry.npmjs.org/@opencode/cli |
| Hermes Agent dari Nous Research, MIT | "The self-improving AI agent built by Nous Research"; LICENSE "MIT License · Copyright (c) 2025 Nous Research" | hermes-agent README, LICENSE |
| Mode rencana OpenCode = agent **Plan** (bawaan) | Built-ins: "**Plan** (`plan`) · primary · Explores and plans without editing normal project files. It may write OpenCode plan files when asked, and shell commands remain permission-controlled." README: "plan - Read-only agent … Denies file edits by default · Asks permission before running bash commands" | docs v2 `agents.mdx`; README |
| "aktifkan agent Plan" · tombol Shift+Tab (versi lama: Tab) | v2 TUI: "Press **Ctrl+X**, then **A** to choose an agent, or run `/agents`. Press **Shift+Tab** to cycle agents."; keybinds `agent.cycle` = `shift+tab`. v1: "You can use the **Tab** key to switch between primary agents" | docs v2 `cli/tui.mdx`, `cli/keybinds.mdx`; docs v1 `agents.mdx` |
| Plan: boleh baca, nggak boleh ngedit (kecuali file rencananya sendiri) | v1: "Denies file edits, writes, and patches except Markdown plan files in `.opencode/plans/` …"; v2: "without editing normal project files. It may write OpenCode plan files" | docs v1/v2 `agents.mdx` |
| Setuju → balik ke **Build** | "**Build** (`build`) · primary · Default coding agent." | docs v2 `agents.mdx` |
| Mode rencana Hermes = perintah bawaan **`/plan`** | "`/plan [task]` · Write a markdown implementation plan to `.hermes/plans/` in the active workspace — planning only, no execution. … (Formerly the bundled `plan` skill; now built-in …)" | hermes-agent `website/docs/reference/slash-commands.md` |
| "rencananya ditulis ke file, belum dikerjakan" · `.hermes/plans/…md` | Prompt `/plan`: "you are in PLAN MODE — planning only. Do not implement code. Do not edit project files except the plan markdown file itself … saved inside the active workspace under `.hermes/plans/YYYY-MM-DD_HHMMSS-<slug>.md` … offer to execute it … but do not start executing in this turn." | hermes-agent `agent/plan_prompt.py`; `website/docs/user-guide/features/skills.md` |
| Isi rencana: file, langkah, cara tes (dasar checklist 3 hal) | "Step-by-step tasks … names exact file paths … Tests / validation … Risks, tradeoffs, and open questions." | hermes-agent `agent/plan_prompt.py` |
| Kerja di folder proyekmu | OpenCode: "Run the CLI in a project to open the full-screen terminal interface … Pass a directory to work in a different project: `opencode ~/code/my-project`". Hermes: "cwd … (CLI always uses launch dir)"; Desktop: "Selecting a working directory in Desktop" | docs v2 `cli/index.mdx`; hermes `user-guide/configuration.md` |
| Model bebas pilih | OpenCode: "OpenCode includes a provider and model catalog from models.dev … Run `/connect`, choose a provider … Then run `/models`"; Hermes: "Use any model you want — Nous Portal, OpenRouter, OpenAI, your own endpoint, and many others. Switch with `hermes model`" | docs v2 `providers.mdx`, `models.mdx`; hermes README |
| Claude · GPT (ChatGPT) · Model lokal (Ollama · LM Studio) | OpenCode: provider `anthropic` (contoh `anthropic/claude-sonnet-5-5`), "Use a ChatGPT Plus or Pro plan instead of an OpenAI API key", "## Ollama", "LM Studio and vLLM also have built-in local discovery". Hermes: "Anthropic · `hermes model`", "OpenAI Codex · ChatGPT or Codex Subscription", "self-hosted endpoints like Ollama and vLLM"; Local Models: "Run models entirely on your own machine — no account, no API key" | docs v2 `providers.mdx`; hermes `integrations/providers.md`, `user-guide/local-models.md` |
| Biaya ikut model yang dipilih | OpenCode: "Usage counts against your plan" (ChatGPT), OpenCode Go "$10/month subscription" (opsional); Hermes: Nous Portal "one subscription", API key per provider | docs v2 `providers.mdx`, `index.mdx`; hermes README |
| Skill (keduanya) | OpenCode: "Put a `SKILL.md` file in `.opencode/skills/<skill-id>`"; Hermes: "Skills are on-demand knowledge documents … All skills live in `~/.hermes/skills/`" | docs v2 `skills.mdx`; hermes `features/skills.md` |
| Sub-agent (keduanya) | OpenCode: "`subagent` · Runs only in a child session through the `subagent` tool"; built-in **General**, **Explore**. Hermes: "The `delegate_task` tool spawns child AIAgent instances with isolated context" | docs v2 `agents.mdx`; hermes `features/delegation.md` |
| Terminal & aplikasi desktop (keduanya) | OpenCode: TUI + "Desktop App (BETA)" (macOS, Windows, Linux). Hermes: CLI/TUI + "Hermes Desktop … macOS (Apple Silicon), Windows, and Linux" | OpenCode README, docs v2 `index.mdx`; hermes `user-guide/desktop.md` |
| (catatan, tidak di VO) Hermes punya plugin komunitas "plan-mode" yang benar-benar memblokir tool edit sampai disetujui | "Plan mode for Hermes Agent: it explores read-only and writes a plan, and its edit tools stay blocked until you approve" · tier: community | hermes `plugin-catalog/plan-mode.yaml` |
Contoh di layar (tokokue.id, "Kue Lapis Legit", tombol "Pesan via WhatsApp", nama file `tombol-wa.js` / `index.html` / `style.css` /
`header.html` / `menu.js` / `harga.json`, "1 + 5" file, folder `toko-kue/`, isi rencana, "4 m" di denah) adalah ilustrasi dan diberi label
CONTOH; sakelar Build | Plan, kolom BACA/EDIT, bar perintah, dokumen rencana, cap dan progres adalah mock buatan kita (bukan screenshot).
Jumlah bintang GitHub tidak dipakai.

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; TANPA --tags = tag AUTO klien)
Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan,
satu take, 42,19 dtk, ±880 karakter termasuk tag) → `assets/audio/vo.mp3`. Tag yang benar-benar dipakai (dari `production/vo_el.json`):
1. `[playful] [excited] [curious]` Pernah suruh agent AI benerin satu tombol WhatsApp, malah lima file ikut berubah?
2. `[playful] [excited]` Tukang aja gambar denah dulu, baru bongkar tembok.
3. `[playful] [excited]` Agent AI juga gitu: minta rencananya dulu, baru boleh kerja.
4. `[playful] [excited]` Dua agent open source gratis ini punya mode rencana: Open Code dan Hermes.
5. `[playful] [excited]` Dua-duanya kerja di folder proyekmu, modelnya bebas kamu pilih.
6. `[playful] [excited]` Di Open Code, aktifkan agent Plan: boleh baca, nggak boleh ngedit.
7. `[playful] [excited]` Di Hermes, pakai slash plan: rencananya ditulis ke file, belum dikerjakan.
8. `[playful] [excited]` Cek tiga hal: file yang disentuh, yang dihapus, dan cara ngetesnya.
9. `[playful] [excited]` Coret denah itu murah, bongkar tembok itu mahal.
10. `[playful] [excited]` Sudah pas? Baru suruh dia kerjain.
11. `[playful] [excited] [confident]` Komen plan, aku kirim lewat DM.

Ejaan untuk suara vs caption: "Open Code" (dua kata, supaya dibaca jelas) → caption **OpenCode**; "slash plan" → caption **/plan**;
"plan" di CTA dikirim huruf kecil (supaya tidak dieja P-L-A-N) → caption **PLAN** (`MERGE`/`FIXI` di `tools/timing.py`).
Voice: `tools/voice_config.json` (Dakocan, voice plgKUYgnlZ1DCNh54DwJ, eleven_v4, stability .41, similarity .75, auto tags).
**Cek dengar:** faster-whisper `small` (id) pada seluruh take: semua baris terbaca, kecuali "Tukang" → "Trukang", "denah" → "dengah"
(baris 2) dan "DNA" (baris 9), "bongkar tembok" → "bongkartembop", "mode" → "model" (baris 4). Baris 2, 4 dan 9 dicek ulang dengan
faster-whisper `medium` (id): **"Tukang aja gambar denah dulu, baru bongkar tembok" · "Dua agen open source gratis ini punya mode
rencana, Open Code dan Hermes." · "Coret Denah itu murah, bongkar tembok itu mahal."** — tidak ada kata yang salah di KEDUA model → tidak
ada take ulang (aturan batch 6). Whisper small juga menulis "Comment plan" untuk "Komen plan" dan "ngetestnya" untuk "ngetesnya"
(pelafalan wajar).
