# VO — 4 open source buat ngatur banyak AI agent · background TERANG · 47,4 dtk VO (reel 48,97 dtk)

Referensi: `aip_remake_batch3/refs/ref2.mp4` (93 dtk, talking head + rekaman layar README GitHub): "Era Hermes Agent sudah selesai… 4 open
source yang bakal gantiin Hermes Agent" → OpenHands, Paperclip, Orca, TeamAI, lalu jualan e-book.

## Yang kita ubah dari referensi
- **Tanpa klaim clickbait** "era Hermes sudah selesai / gantiin Hermes" — Hermes sama sekali tidak disebut. Sudut kita: masalah nyata
  (agent makin banyak → makin berantakan) lalu 4 alat open source dengan peran yang beda-beda.
- Faceless, 1 kalimat per alat, tiap alat dijelaskan dengan **apa yang benar-benar ditulis di README-nya** (bukan "keunggulan, cari sendiri").
- Dibuang (tidak terverifikasi / tidak akurat): "TeamAI biasanya untuk pemula", "Orca bisa ganti-ganti model", e-book "120+ repo".
- **TeamAI dibingkai dengan jujur**: dia bukan runtime orkestrator, tapi tempat simpan skill/rules/MCP/model semua agent tim di 1 repo Git
  yang sync otomatis — tetap relevan untuk "ngatur banyak agent", jadi dipertahankan (proyeknya nyata, open source MIT, deskripsinya cocok).
- Tambahan kejujuran: "Tool-nya gratis, tapi model AI-nya tetap pakai akun / API kamu sendiri."
- 93 dtk → 47 dtk. CTA: **"Komen AGENT, aku kirim lewat DM."**

## Fakta yang dicek (sumber resmi, diakses 2026-11-12)
| Klaim di reel | Sumber | Status |
|---|---|---|
| OpenHands Agent Canvas = "pusat kontrol" self-hosted buat coding agent; jalanin OpenHands, Claude Code, Codex, Gemini (+ Pi, OpenCode, agent ACP lain) di local, remote, cloud backend | README `github.com/OpenHands/OpenHands` ("The self-hosted developer control center for coding agents and automations. Run OpenHands, Claude Code, Codex, Gemini, Pi, OpenCode, or any ACP-compatible agent across local, remote, and cloud backends.") | ✅ |
| OpenHands open source | `LICENSE` repo OpenHands/OpenHands = MIT ("Copyright © 2025 OpenHands contributors") | ✅ |
| Paperclip = orkestrasi tim AI agent: org chart, tugas, budget, approval; "perusahaan" isi agent | README `github.com/paperclipai/paperclip` ("Open-source orchestration for teams of AI agents", "If OpenClaw is an employee, Paperclip is the company", "org charts, budgets, governance", "Tasks, approvals & review gates") | ✅ |
| Paperclip open source / gratis | README badge MIT + "Open source. Self-hosted. No Paperclip account required." (`npx paperclipai@latest onboard --yes`) | ✅ |
| Orca: 1 agent koordinator bagi tugas ke worker agent; banyak coding agent paralel, masing-masing di worktree sendiri | README `github.com/stablyai/orca` ("Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree", "Orchestrate Agents: Hand a big task to one agent. It splits the work, starts worker agents in their own workspaces, and brings their results back to you.") | ✅ |
| Orca open source / gratis | README "Orca is free and open source under the MIT License" + `LICENSE` MIT (Lovecast Inc.) | ✅ |
| TeamAI dari Tencent: skill, rules, MCP (dan agents, model, learnings) tim disimpan di 1 repo Git, sync otomatis | README `github.com/Tencent/teamai-cli` ("TeamAI manages a team's skills, rules, agents, learnings, models, MCP, and other agent resources in a git repo. A teammate initializes once. After that, the latest team agent resources sync automatically.") · perintah `teamai init <repo>` dari README | ✅ |
| TeamAI open source | `LICENSE` Tencent/teamai-cli: "teamai-cli is licensed under MIT" | ✅ |
| Contoh agent di layar (Claude Code, Codex, Gemini CLI, Cursor, OpenCode) | tercantum di README masing-masing (OpenHands: Claude Code/Codex/Gemini/OpenCode; TeamAI tabel: Claude Code, Codex, Cursor, OpenCode; Orca: "any CLI agent") | ✅ |
| "Model AI tetap pakai akun / API kamu" | Orca: "run a fleet of coding agents … with your own subscription" (deskripsi repo); Paperclip `test-drive` butuh API key; OpenHands "Bring your own model" | ✅ |

Catatan: situs resmi (openhands.dev, paperclip.ing, onorca.dev) tidak bisa dibuka dari sesi ini (DNS diblok proxy) — semua fakta diambil
dari README + LICENSE di GitHub (raw.githubusercontent.com) dan pencarian web (liputan TeamAI). Angka bintang GitHub sengaja tidak dipakai
(cepat berubah). Contoh di layar ("fitur checkout", "Agent CEO", nama "Rina/Budi/Sari/Dimas", "repo-tim") adalah ilustrasi UI generik.

## Naskah (dikirim ke ElevenLabs persis seperti ini — tiap baris diawali tag)
```
[playful] [excited] AI agent kamu makin banyak, tapi makin berantakan? Ini empat open source gratis buat ngaturnya.
[playful] [excited] Satu, OpenHands Agent Canvas. Satu pusat kontrol buat jalanin Claude Code, Codex, sampai Gemini, di laptop, server, atau cloud.
[playful] [excited] Dua, Paperclip. Kamu bikin perusahaan isi AI agent: ada struktur tim, tugas, budget, dan approval dari kamu.
[playful] [excited] Tiga, Orca. Satu agent jadi koordinator, bagi tugas ke agent lain, masing-masing kerja paralel di worktree sendiri.
[playful] [excited] Empat, Team AI dari Tencent. Skill, rules, sama MCP semua agent di tim disimpan di satu repo Git, terus sync otomatis.
[playful] [excited] Keempatnya open source, gratis. Cuma, model AI-nya tetap pakai akun atau API kamu sendiri.
[playful] [excited] Mau link plus cara install-nya? Komen agent, aku kirim lewat DM.
```
(Teks tanpa tag: `production/vo_lines.txt`. "Team AI" ditulis terpisah supaya dibaca benar; caption menampilkan "TeamAI". "agent" ditulis
huruf kecil supaya tidak dieja; caption menampilkan "AGENT".)

Voice: `tools/voice_config.json` (Eleven v4, stability 0.41, similarity 0.75) via `/home/user/testing-hyperframes/tools/el_tts_ts.py --tags "[playful] [excited]"`
→ `assets/audio/vo.mp3` + `production/vo_el_alignment.json` → `tools/align_words.py` → `production/vo_words_raw.json` → `tools/timing.py`.
Cek ulang dengan faster-whisper small: semua kalimat terdengar benar, tag tidak ikut terbaca.
