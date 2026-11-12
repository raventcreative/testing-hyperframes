# VO — R16 · Bikin "perusahaan AI" sendiri pakai Paperclip · background TERANG (LIGHT) · VO 46,9 dtk (reel 48,2 dtk)

Referensi: `projects/aip_remake_batch5/refs/ref6.mp4` + `ref6.txt` (reel berbahasa Inggris, 36,6 dtk, gelap, maskot kepiting voxel oranye):
"You can create a free army of AI employees … Paperclip AI that's trusted by 112,000 developers … they elect a CEO, create a development
team, a marketing team … communicate with each other 24-7 … watch what each employee is doing … how many tokens each of them uses …
Follow and comment ARMY". Versi kita: bahasa Indonesia, deep dive (R2 `aip_r2_orkestrator` sudah menyebut Paperclip 1 kalimat dalam daftar
4 alat; R16 menjelaskan cara kerjanya dengan visual yang beda total dari R2 dan dari referensi).

## ATM: what we changed
**Amati (referensi):** ide = alat open source yang menjalankan "karyawan AI" di komputer sendiri; hook = "pasukan karyawan AI gratis";
beat = bukti sosial (112.000 developer + kurva bintang) → kamu tulis apa yang mau dibangun → mereka pilih CEO + tim dev/marketing/desain/
support → komunikasi 24/7, kamu jadi "stakeholder" → lihat kerja + token tiap karyawan; CTA = follow + komen "army".
**Tiru (yang dipakai):** hanya ide intinya (tujuan → CEO → tim → kamu memantau kerja dan token tiap agent) dan mekanisme umum "demo alur".
**Modifikasi (wajib):**
1. **Hook sendiri, sudut beda:** "AI agent sekarang bisa dikasih jabatan, atasan, sampai gaji token, kayak karyawan beneran." — sudut
   *struktur kerja* (jabatan / atasan / gaji = istilah Paperclip sendiri: "a boss, a title, and a job description", "token salary
   budgets per agent"), bukan "pasukan gratis". Visual: kartu karyawan AI yang terisi dan dijepit paperclip — tidak ada di referensi.
2. **Struktur & visual sendiri:** kartu karyawan → nama + open source + terminal di komputer kamu → form "Perusahaan baru" dengan tujuan →
   org chart yang membangun dirinya sendiri (garis turun, CEO, dokumen strategi, cap DISETUJUI dari "Kamu", tiket tugas dibagi ke kursi
   kosong) → pengajuan rekrut dengan saklar izin → **monitor heartbeat** (garis detak per agent, bangun/kerja/lapor/tidur) → **meter
   token & budget per agent** (80% peringatan, 100% dijeda) → kartu "Catatan jujur" → CTA. Semua dalam LIGHT house style, robot + maskot
   AI PRENEUR. Tidak ada maskot kepiting, kurva bintang, laptop, stempel FREE, avatar "stakeholder", atau layout mereka. Beda juga dari R2
   (R2 = 1 kartu putih kecil dengan bagan statis + 1 tombol Setujui).
3. **Sudut praktisi tanpa klaim palsu:** tidak ada "aku pakai ini" / hasil pribadi (Freddie belum tercatat memakai Paperclip). Yang ada:
   saran praktis "Mulai kecil dulu" (sesuai saran resmi "Set conservative budgets initially").
4. **Nilai tambah untuk Indonesia yang tidak ada di referensi:** contoh tujuan UMKM ("toko keripik tembus 100 pesanan online seminggu",
   perusahaan contoh "Keripik Renyah", tim web/konten/riset dengan tugas lokal) + **koreksi jujur**: agent TIDAK nyala 24 jam (heartbeat:
   bangun kalau ada tugas/jadwal), **biaya model AI tetap ada** (API atau langganan kamu), **budget per agent dengan auto-pause**, dan
   **kamu tetap pengawas** (strategi & rekrut butuh persetujuan kamu).
5. **CTA sendiri:** "Komen TIM, aku kirim lewat DM." — isi DM disiapkan di `production/DM_TIM.md` (link repo, cara pasang, contoh
   struktur tim UMKM, catatan biaya). Tidak ada "follow untuk update".

**Dibuang (tidak terverifikasi / tidak akurat):** "trusted by 112,000 developers" (itu jumlah *bintang* GitHub, bukan developer; tidak
dipakai di VO — layar hanya menunjukkan "★ 113 rb+ bintang · cek 12 Nov 2026" dari halaman repo), "communicate 24-7 / run all
operations" (dokumentasi resmi: agent *tidak* jalan terus, bangun lewat heartbeat), "they elect a CEO" (CEO adalah agent pertama yang
kamu pasang; strateginya butuh persetujuan kamu), "army". Tidak ada kalimat yang memakai >3 kata berurutan dari naskah referensi (beda
bahasa juga).

## Fakta yang dicek (sumber resmi, diakses 12 Nov 2026)
| Klaim di reel | Sumber | Status |
|---|---|---|
| Paperclip = open source, lisensi MIT | `github.com/paperclipai/paperclip` LICENSE ("MIT License · Copyright (c) 2025 Paperclip AI"), README badge + "MIT © 2026 Paperclip Labs, Inc" | ✅ |
| Gratis, self-hosted, jalan di komputer sendiri, tanpa akun Paperclip | README Quickstart: "Open source. Self-hosted. No Paperclip account required."; "Locally, a single Node.js process manages an embedded Postgres and local file storage" | ✅ |
| `npx paperclipai onboard --yes`, Node.js 24.11+, UI di `localhost:3100` | README Quickstart (`npx paperclipai@latest onboard --yes`, "With Node.js 24.11 or newer"), docs/start/quickstart.md ("starts the API server and UI at http://localhost:3100") | ✅ (layar menulis `npx paperclipai onboard --yes`, persis seperti docs/start/quickstart.md) |
| ★ 113 rb+ bintang (layar saja, bukan VO) | Halaman repo GitHub hari ini: "113.3k stars" | ✅ (angka hanya bisa naik → "113 rb+") |
| Agent punya jabatan, atasan, "gaji" token | README "Your agents have a boss, a title, and a job description."; docs/start/what-is-paperclip.md "token salary budgets per agent" | ✅ |
| Kamu tulis 1 tujuan perusahaan, semua tugas nyambung ke tujuan itu | docs/guides/board-operator/creating-a-company.md (Step 2: Set a Goal); core-concepts: "Task hierarchy — all work traces back to the company goal" | ✅ (tujuan keripik = contoh kita) |
| Agent CEO menyusun strategi → kamu setujui → tugas dipecah & dibagi ke agent | docs/start/core-concepts.md (Delegation: "Create a strategy and submit it for your approval · Break approved goals into tasks · Assign tasks to agents"); approvals.md ("The CEO's initial strategic plan requires board approval") | ✅ |
| CEO mengajukan rekrut agent baru, kamu yang menyetujui | core-concepts.md ("agents can request to hire subordinates, but the board must approve"); approvals.md (`hire_agent` approval: name, role, capabilities, adapter, budget) | ✅ |
| Agent pakai Claude Code / Codex / Gemini CLI / OpenCode (label kecil di bawah tiap agent) | README "Works with" (Claude Code, Codex, Gemini CLI, OpenCode, …); "Choose models and harnesses per agent" | ✅ (pembagian per agent = contoh) |
| Agent tidak nyala terus: bangun lewat heartbeat (tugas baru, jadwal, mention, manual, approval), kerja, lapor, tidur | docs/start/core-concepts.md ("Agents don't run continuously. They wake up in heartbeats … Schedule … Assignment … Comment …"); how-agents-work.md ("wake up, do work, and go back to sleep"); README FAQ "Do agents run continuously?" | ✅ |
| Token tiap agent kelihatan | costs-and-budgets.md ("Paperclip tracks every token spent by every agent" — input/output tokens, cost per agent per month); README "Token and cost tracking by company, agent, project…" | ✅ |
| Budget habis → agent otomatis dijeda (80% peringatan, 100% berhenti) | costs-and-budgets.md (80% soft alert, 100% hard stop "agent is auto-paused, no more heartbeats"); managing-agents.md | ✅ (README menambahkan: pencatatan bisa sedikit terlambat → di NOTES) |
| Model AI tetap pakai API atau langganan kamu → ada biaya | README (`ANTHROPIC_API_KEY=… npx paperclipai test-drive`, "Local Claude and Codex subscription sign-in"); managing-agents.md ("A saved subscription is the default when available; otherwise a saved API key"); costs-and-budgets.md (cost per provider/model) | ✅ |
| Kamu tetap pengawas: cek hasil, setujui strategi & rekrut, jeda kapan saja | approvals.md ("Board Override Powers: Pause or resume any agent at any time …"); README Governance | ✅ |
| "Mulai kecil" | costs-and-budgets.md Best Practices: "Set conservative budgets initially and increase as you see results" | ✅ (saran) |

Catatan sumber: README dan dokumen `docs/` diambil langsung dari `raw.githubusercontent.com/paperclipai/paperclip/master/…` (salinan di
scratchpad sesi); `docs.paperclip.ing` dan `paperclip.ing` tidak bisa dibuka dari sesi ini (DNS diblok), isinya sama dengan folder `docs/`
di repo. Angka bintang dari halaman repo `github.com/paperclipai/paperclip` (WebFetch, 12 Nov 2026). Semua angka di layar selain bintang
(token, %, budget, "100 pesanan") adalah ilustrasi dan diberi label CONTOH / ILUSTRASI / angka ilustrasi.

## Naskah — dikirim ke ElevenLabs persis seperti ini (TANPA `--tags`: tag otomatis klien)
Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` → `assets/audio/vo.mp3`
(46,96 dtk) + `assets/audio/vo.json`. Tag yang benar-benar dipakai (dari `vo.json`):
```
[playful] [excited] [surprised] AI agent sekarang bisa dikasih jabatan, atasan, sampai gaji token, kayak karyawan beneran.
[playful] [excited] Namanya Paperclip: open source, gratis, dan jalan di komputer kamu sendiri.
[playful] [excited] Kamu tulis satu tujuan, misalnya: toko keripik tembus seratus pesanan online seminggu.
[playful] [excited] Agent CEO-nya nyusun strategi, kamu setujui, baru tugasnya dibagi ke tim web, konten, dan riset.
[playful] [excited] Butuh anggota baru? CEO-nya ngajuin rekrut, kamu yang approve.
[playful] [excited] Agent-nya nggak nyala terus: bangun kalau ada tugas atau jadwal, kerja, lapor, terus tidur lagi.
[playful] [excited] Token tiap agent kelihatan, dan kalau budget-nya habis, dia otomatis dijeda.
[playful] [excited] Catatannya: agent-nya tetap pakai API atau langganan AI kamu, jadi ada biayanya. Mulai kecil dulu, dan kamu tetap yang ngawasin.
[playful] [excited] [confident] Komen tim, aku kirim lewat DM.
```
(Teks tanpa tag: `production/vo_lines.txt`. "tim" ditulis huruf kecil supaya tidak dieja T-I-M; caption menampilkan **TIM**. "seratus"
dibaca, caption menampilkan **100**. Tag ke-3 [surprised]/[confident] dipilih otomatis oleh `el_tts_ts.py` dari kata "beneran"/"Komen".)

Cek dengar ulang (faster-whisper `small`, bahasa id, seluruh VO; `medium` untuk baris 1 dan 4): semua 9 baris terbaca sesuai naskah —
"Paperclip", "open source", "CEO", "approve", "API", "DM" jelas; tag tidak ikut terbaca. `small` sempat menulis "Hei, AI" di awal dan
"reset" untuk "riset": `medium` membaca "AI agent sekarang…" dan "…dan riset." — tidak ada kata tambahan.
