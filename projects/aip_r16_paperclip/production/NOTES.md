# NOTES — R16 · Bikin "perusahaan AI" sendiri pakai Paperclip (AI PRENEUR · LIGHT) · `projects/aip_r16_paperclip/`

1080×1920 · 30 fps · **48.2 s** (1446 frames) · VO 46.88 s starting at 0.30 s · HyperFrames 0.8.186 · CTA keyword **TIM**.
Kit: copied from `projects/aip_r8_web3d` (newest LIGHT; without `out/`, audio, cover PNG, `.hyperframes/`). Serve:
`python3 -m http.server 8936 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed. `.gitignore`: `out/`, `.hyperframes/`.

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO `--tags` = client's auto tags: `[playful] [excited]` on every line, + `[surprised]` on line 1 ("beneran") and `[confident]` on the
   CTA) → `assets/audio/vo.mp3` (46.96 s) + `assets/audio/vo.json` (line times + character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (9 scenes = 9 VO lines, 42 caption chunks, styles).
   Caption display fixes: "seratus" → **100**, "tim," → **TIM,** (the voice reads the words; `FIXI` in timing.py). No alignment fixes needed
   (ElevenLabs alignment agrees with faster-whisper small/medium within ~0.15 s).
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −29.9 LUFS vs VO −18.0 LUFS). No music (lead adds it).
6. Cover: `COVER_URL=http://127.0.0.1:8936/thumbnail/cover.html node thumbnail/render_cover.cjs thumbnail/COVER_TIM_1080x1920.png`.

## Shared visual system — `vendor/r16kit.js` (window.R16) + `vendor/r16icons.js` (lucide, ISC)
- `R16.av(id, role, size)`: agent avatar = circle in the role colour + white bot glyph + white role badge. Roles: CEO (gold, briefcase,
  "Claude Code"), Tim Web (blue, globe, "Codex"), Tim Konten (orange, pen, "Claude Code"), Tim Riset (green, search, "Gemini CLI"),
  Agent Desain (violet, palette, "OpenCode") — adapter labels are adapters listed in Paperclip's README; the per-agent split is an example.
- `R16.idCards(p)`: the "KARTU KARYAWAN AI" card (Agent Konten, JABATAN / ATASAN / GAJI) + two cards behind (s01, s02).
- `R16.org(p, o)`: goal banner (TUJUAN · Keripik Renyah · CONTOH · "Tembus 100 pesanan online / minggu"), Kamu chip, CEO + teams,
  connector bars, task tickets; 3-team or 4-team layout (s03 end → s04 → s05 → s06 start, identical geometry).
- `R16.mon/monHead/monTraces/monPills`: the monitor panel with one row per agent (s06 heartbeat traces → s07 budget bars).
- `R16.scene(ID)`: timeline boilerplate — seek-safe scale shorthand; **every initial state pinned at 0 in a nested timeline `P0` that is
  the first child of the scene timeline at 0** (`I()` = immediate `gsap.set` + `P0.set`); `ft` = fromTo without immediate render;
  `L()` word lookup that throws if a word is missing; `done()` = end marker + backward-seek patch + **`tl.render(0, true, true)`** +
  registration. index.html uses the same rule for captions, logo, grid and grain (`pin()` → `P0`, `tl.render(0, true, true)` at the end).

## Scenes (global s) — hero zone y 290–935, captions y≈966–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–6.70 | AI agent sekarang bisa dikasih jabatan, atasan, sampai gaji token, kayak karyawan beneran. | frame 0: ID card "KARTU KARYAWAN AI · ILUSTRASI", Agent Konten (avatar, AI agent · Claude Code), empty skeleton fields; "AI agent": two more cards fan out behind (Web, Riset), sparkles; "jabatan" → chip Penulis konten; "atasan" → boss chip with the CEO avatar; "gaji token" → coin + "Jatah token / bulan" + meter; "kayak karyawan" → a paperclip drops and clamps the card; "beneran" → green stamp KARYAWAN AI + shake |
| s02 | 6.70–11.57 | Namanya Paperclip: open source, gratis, dan jalan di komputer kamu sendiri. | cards drop away, the clip flies up and becomes the title glyph; "Paperclip" letters rise; pills github.com/paperclipai/paperclip · ★ 113 rb+ bintang · cek 12 Nov 2026; chips "Open source · MIT", "Gratis"; terminal "komputer kamu" (butuh Node.js 24.11+): `$ npx paperclipai onboard --yes` types, "✓ Paperclip jalan di localhost:3100", chip "di komputer kamu sendiri"; terminal content clears for the hand-over |
| s03 | 11.57–16.83 | Kamu tulis satu tujuan, misalnya: toko keripik tembus seratus pesanan online seminggu. | the empty terminal card grows into a browser window "localhost:3100 · Paperclip di komputer kamu" (CONTOH) with our form "Perusahaan baru": Nama perusahaan Keripik Renyah (pulses on "toko keripik"), cursor clicks TUJUAN UTAMA (focus ring), the goal types "Tembus 100 pesanan online / minggu", Simpan tujuan → Tersimpan; the window fades and the goal field rises to the top = the org chart's goal banner |
| s04 | 16.83–22.97 | Agent CEO-nya nyusun strategi, kamu setujui, baru tugasnya dibagi ke tim web, konten, dan riset. | connector drops, CEO node pops; strategy doc "Strategi CEO · menunggu persetujuan" writes 1 Toko online · 2 Konten tiap hari · 3 Cek harga pesaing; "kamu" → Kamu chip (pemilik · pengawas); "setujui" → a stamp flies from it, DISETUJUI lands, status "disetujui kamu"; "baru tugasnya dibagi" → bus draws, dashed empty seats, the doc folds into 3 task tickets that fly to the seats; "web / konten / riset" → each team pops into its seat over its ticket |
| s05 | 22.97–26.73 | Butuh anggota baru? CEO-nya ngajuin rekrut, kamu yang approve. | tickets tuck into their teams, teams slide left, bus stretches, a dashed "Kursi kosong" appears; request card from the CEO "Pengajuan rekrut · dari CEO · butuh izin kamu": Agent Desain, desain feed & promo, lapor ke CEO · budget kecil (contoh), switch "Izinkan rekrut?"; "kamu yang approve" → the cursor from the Kamu chip flips the switch green, the card flies into the seat, Agent Desain pops in |
| s06 | 26.73–32.33 | Agent-nya nggak nyala terus: bangun kalau ada tugas atau jadwal, kerja, lapor, terus tidur lagi. | the chart folds into the "Heartbeat agent" monitor (the five avatars fly into rows); "nggak nyala terus" → all dim, status "tidur", z's float; a playhead sweeps the rows like a heart monitor; triggers "Tugas baru" / "Jadwal 09.00" light on "bangun"; a task flies onto Tim Web (spike, bangun → kerja), a clock onto Tim Konten (spike); "kerja" → working plateaus; "lapor" → two reports fly to the CEO, it wakes; "tidur lagi" → everyone back to tidur; Riset and Desain never wake |
| s07 | 32.33–36.73 | Token tiap agent kelihatan, dan kalau budget-nya habis, dia otomatis dijeda. | header flips to "Token & budget · jatah bulanan per agent · angka ilustrasi", legend 80% peringatan · 100% dijeda; traces fade into budget bars + % + token counters that roll up; "budget-nya" → Tim Web 64% → 80% (amber, "80% · awas"); "habis" → 100% red + shake; "otomatis dijeda" → red DIJEDA pill, pause badge on the avatar, row tinted, note "otomatis dijeda di 100% budget"; panel drops away at the end |
| s08 | 36.73–45.23 | Catatannya: agent-nya tetap pakai API atau langganan AI kamu, jadi ada biayanya. Mulai kecil dulu, dan kamu tetap yang ngawasin. | pill "Catatan jujur"; cost card: Paperclip · Rp 0 · gratis · open source MIT + Model AI agent-nya (otak tiap agent, dari akun kamu): chips API key / Langganan AI on their words, "ada biaya · sesuai pemakaian token" + coin drop; card "Mulai kecil dulu": slider slides down, chips 2–3 agent · budget kecil; card "Kamu pengawasnya": ticks cek hasil kerjanya · setujui strategi & rekrut · jeda kapan aja; all drops away at the end |
| s09 | 45.23–48.20 | Komen TIM, aku kirim lewat DM. | package card "Paket TIM · link Paperclip + cara pasang · contoh struktur tim UMKM" + comment sheet; TIM types big, heart, send → paper plane into the package; DM card, bubble "Paket TIM · link + contoh tim / repo Paperclip, cara pasang, struktur tim UMKM", "terkirim" ✓✓; end logo + glint (corner logo fades at 47.0) |

Hosts: robot (co-host, right) flies in on "agent", points at the card fields, cheers "beneran", TYPES the install command and the goal on
its holo keyboard, thinks on "strategi", scans the task split, cheers the approved hire, shakes its head at "nggak nyala terus", types on
"kerja", scans the token meters, shock on "habis", head shake on "dijeda", thinks on "Catatannya", points at "ngawasin", cheers the CTA,
waves at the end. Mascot (host, left): intents on every beat (present / point / explain / question on "Butuh anggota baru?" / cta).
**Mascot glance-at-robot DISABLED** (lead's kit bug report: in the real render the glance turned the eyes into blank white discs):
`const glance = (t) => 0;` in `compositions/mascot.html` (old function kept as `glance_unused`).

## Sources (checked 12 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- github.com/paperclipai/paperclip: README (open-source orchestration for teams of AI agents; goal → hire the team → approve and run;
  heartbeats; cost control/budgets; governance; Quickstart `npx paperclipai@latest onboard --yes`, Node.js 24.11+, embedded Postgres,
  "No Paperclip account required"; FAQ "Do agents run continuously?"), LICENSE (MIT), repo page (113.3k stars on 12 Nov 2026).
- Repo docs (`docs/` = docs.paperclip.ing, which is DNS-blocked here): start/what-is-paperclip.md ("token salary budgets per agent"),
  start/core-concepts.md (goal, CEO strategy approval, delegation, hire approval, heartbeats), start/quickstart.md (`npx paperclipai
  onboard --yes`, localhost:3100), guides/board-operator/{creating-a-company, costs-and-budgets (80% soft alert, 100% auto-pause),
  approvals, org-structure, managing-agents (subscription or API key)}, guides/agent-developer/how-agents-work.md.
- NOT used: "trusted by 112,000 developers" (stars ≠ developers), "24/7 / run all operations" (docs: agents don't run continuously),
  "they elect a CEO".

## DM text for the TIM keyword
`production/DM_TIM.md` (repo link, install, example UMKM team, cost + safety notes incl. telemetry opt-out).

## QA (real runtime, hyperframes 0.8.186)
- `lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R8 kit).
- `validate .` (final run, after every fix) → **0 errors, 0 contrast warnings**; remaining warnings = kit notices ("multiple instances of
  Three.js" from the robot + mascot bundles, SwiftShader "GPU stall due to ReadPixels"). Earlier contrast notes were fixed: light-grey
  small labels → #5d6f8f, solid fallback colours under gradient headers, placeholder #627495, and the two cards behind the ID card no
  longer carry header text (it sat hidden under the front card and was measured against white).
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): ONE full pass of 81 frames (first frame, every scene's beats, both sides of
  every cut, the end) + two targeted fix passes (7.0/7.3 s card drop, 36.45–37.2 s s07→s08 cut, 41.6/44.6 s s08 text; 0 s + 3.0 s after
  the back-card change). JPG contact sheets in
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r16/`:
  `rt1_full_1.jpg`, `rt1_full_2.jpg` (full frames), `rt1_hero_1.jpg` … `rt1_hero_3.jpg` (hero + captions, larger), `rt2_fix.jpg`,
  `rt3_s01.jpg`; the runtime's own `rt1/contact-sheet-*.jpg`. All PNG dumps deleted.
- Mascot eyes checked on every captured frame: pupils everywhere, no white-disc eyes (glance disabled).
- Dev layout check (own harness, GSAP seek of every scene every 0.2 s, 241 frames): no text outside its pill/card, no text outside
  x 72–1008, nothing in the caption zone (hero content ends ≤ 914 px), nothing in the logo corner, every caption chunk on ONE line
  inside x 60–1020; every word lookup (`L()` / `wt()`) verified against `vendor/vo_words.js`.
- Initial states: every scene + index.html pins them in a nested timeline that is the first child at 0, then `tl.render(0, true, true)`.
  Hand-overs at identical geometry: s01→s02 (ID cards + clip), s02→s03 (empty terminal card → browser window), s03→s04 (goal banner),
  s04→s05→s06 (org chart), s06→s07 (monitor rows); s07, s08 exit in their last 0.2–0.27 s and the next scene's content arrives at once.

## Known issues / notes for the lead
- Frame 0 shows the ID card + the mascot rising into place; the robot flies in at ≈0.7 s (kit behaviour, same as R8/R11). The cover PNG
  is the intended thumbnail.
- Captions: during the 0.34 s word rise a navy keyword pill can show as a thin bar under the line for a frame or two (same caption system
  as the kit; e.g. 17.2 s "Agent" before "CEO-nya" rises).
- At the s07→s08 cut (≈36.73–36.8 s) the hero zone is nearly empty for ~3 frames (panel gone, "Catatan jujur" pill popping in).
- All company data is illustrative and labelled: Keripik Renyah, the goal, tasks, "Agent Desain", budget/token numbers ("angka
  ilustrasi"), the localhost window ("CONTOH"), the ID card ("ILUSTRASI"). Adapter labels per agent are examples of supported adapters.
- "★ 113 rb+ bintang · cek 12 Nov 2026" is the GitHub repo page count on 12 Nov 2026 (113.3k); not spoken. The reference's "112,000
  developers" is NOT used.
- `.hyperframes/` (written by snapshot/validate) is git-ignored in this folder, together with `out/`.
