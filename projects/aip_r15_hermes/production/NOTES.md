# NOTES — R15 · Duo agent AI open source: kantor + karyawan (OpenMausBot + Hermes Agent) (AI PRENEUR · NAVY)

- **Duration** 49.80 s (1494 frames @30) · VO 48.48 s starting at 0.30 s · CTA keyword **AGENT** · reference `aip_remake_batch5/refs/ref5.mp4` (61 s).
- **Kit**: copied from `projects/aip_r9_youtube` (newest NAVY; without `out/`, its VO/QA/cover PNG). Index built by `tools/build_index.py`
  from `production/timing.json`; shared scene kit `vendor/r15kit.js` (topic header with icon roll + 6 progress segments, lucide icons,
  example bot roster, timeline boilerplate incl. the per-letter typer; scene lengths come from the timing via `K.dur(id)`, so a re-timed VO
  needs no hand edits). Audio as the batch-3/4 kits: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` + `<audio id="sfx"
  src="assets/audio/sfx.wav">` — no music (the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = client's AUTO tags: `[playful] [excited]` on every line + `[curious]` on line 9, `[confident]` on the CTA), one call →
  `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json` (from the character alignment); `tools/timing.py` →
  `production/timing.json` + `vendor/vo_words.js`. timing.py change vs R9: the generic "snap to next onset" only moves a word start that
  falls in real silence (the ElevenLabs alignment is exact; the old rule pushed "key." 0.5 s late); line-first words still snap to the real
  voice onset. The VO was generated twice: take 1 had "…tanpa API key. Atau…" (4 words identical to the reference across a sentence
  break) → line 5 rewritten ("nggak perlu API key") and the whole VO regenerated in one call (same length 48.48 s).
  Pronunciation checked with faster-whisper small.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples; level matches R9: mean −33 dB).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_AGENT_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_AGENT_1080x1920.png`,
  static server `python3 -m http.server 8935` at the project root). NAVY: chip "2 AGENT · GRATIS · OPEN SOURCE", "Tim AI kerja di /
  LAPTOPMU / OpenMausBot + Hermes Agent", the laptop with the three example bots + "jalan di laptopmu · 127.0.0.1", side badges
  kantornya / karyawannya, mascot + typing robot. Everything that matters sits inside the 4:5 grid crop (y 285–1635). No third-party logos.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–5.73 | Tim AI kamu numpang di server siapa? Duo open source ini jalanin agennya di laptopmu. | headline "Tim AI kamu numpang di… / server siapa?" + a "SERVER ORANG LAIN" rack whose 3 slots fill with example bots (Admin Email, Rekap Penjualan, Riset Harga), blinking LEDs; cyan "?" disc pings on "siapa?"; "Duo open source ini": headline lifts, badges OpenMausBot (OPEN SOURCE · APACHE-2.0) + Hermes Agent (OPEN SOURCE · MIT) drop in, chips light on "open source"; "jalanin agennya": rack dissolves, a laptop "LAPTOP KAMU" forms around the same bots; "laptopmu": green "jalan di laptopmu · 127.0.0.1" + screen glow |
| s02 | 5.73–12.40 | OpenMausBot jadi kantornya: aplikasi chat, tiap bot pegang satu tugas, misalnya balas email pelanggan. | Hermes badge slides off, OpenMausBot badge becomes the topic header (OpenMausBot · kantornya · APACHE-2.0); "kantornya": 4 desks (1 bot, 1 meja, contoh) with a laptop each; "aplikasi chat": desks fly into the sidebar of our own chat-app mock (white thread pane, "engine: Hermes"); "tiap bot pegang satu tugas": each row shows its job, "1 bot · 1 tugas" pill; "misalnya balas email pelanggan": "3 email pelanggan baru" + reply bubble types "Draf balasan 3 email siap. Aku tunggu kamu cek dulu, ya." (CONTOH) |
| s03 | 12.40–18.87 | Hermes dari Nous Research jadi karyawannya: dia nulis skill dari pengalaman, jadi tugas berulang makin lancar. | header → Hermes Agent · karyawannya · MIT; an employee ID badge swings down on a lanyard (KARYAWAN, Hermes Agent, Nous Research highlighted, MIT · OPEN SOURCE); green DITERIMA stamp on "karyawannya"; SKILL.md card (~/.hermes/skills/, "balas-email-pelanggan · contoh") types 4 steps; REVISI rev 1 → rev 2 (+ step 5 "Pakai template refund", "+ baru") → rev 3, then "makin lancar" |
| s04 | 18.87–22.13 | Kantor dan karyawannya gratis, otaknya yang bayar. | header → Biayanya · aplikasinya gratis, modelnya bayar; a receipt (NOTA · tim AI kamu): Kantor · OpenMausBot · Apache-2.0 Rp0, Karyawan · Hermes Agent · MIT Rp0, two GRATIS stamps; Otak (model AI) · ChatGPT atau DeepSeek → cyan "bayar" pill + "Total: tergantung modelmu" |
| s05 | 22.13–27.73 | Login pakai langganan ChatGPT, nggak perlu API key. Atau DeepSeek, bayar per pemakaian. | "OTAKNYA · PILIH SATU": terminal (A · LANGGANAN CHATGPT) types `$ hermes model`, the real menu label "ChatGPT or Codex Subscription" is selected, "login: buka link, masukkan kode" + green TANPA API KEY chip; ATAU pill; DeepSeek card ("pakai API key sendiri · DEEPSEEK_API_KEY") with a usage meter that fills in steps on "bayar per pemakaian" (no prices) |
| s06 | 27.73–33.40 | Skill, memori, dan riwayat chat ada di laptopmu, tapi pesanmu tetap dikirim ke penyedia model. | header → Data kamu · yang tinggal & yang terkirim; "DI LAPTOPMU" panel: Skill ~/.hermes/skills/, Memori ~/.hermes/memories/, Riwayat chat ~/.openmausbot/ with locks, green TERSIMPAN LOKAL; message "Rangkum 3 email ini, ya"; "dikirim": a letter flies along a dotted path to the dim "penyedia model · ChatGPT / DeepSeek" cloud, which lights up; amber "isi pesan ikut terkirim" |
| s07 | 33.40–39.23 | Yang sering dilewatin: default-nya akses penuh. Ganti ke Ask, biar aksi berisiko nunggu izinmu. | header → Level izin · langkah yang sering dilewatin; amber SERING DILEWATIN tag; settings card "Level izin bot" (Admin Email · Hermes) with switch "Ask for approval / Full access" — amber on Full access (DEFAULT tag) + "bot jalan tanpa nanya"; "Ganti ke Ask": slides to Ask (cyan); footnote "+ di Hermes sendiri: approvals.mode: manual"; approval card "Hermes minta izin · PERINTAH BERISIKO", `$ curl -fsSL https://…/setup.sh \| sh` (jalankan skrip dari internet), buttons Izinkan sekali / Selalu izinkan / Tolak, MENUNGGU KAMU + pulsing ring |
| s08 | 39.23–44.60 | Minusnya, laptop harus tetap nyala biar jadwalnya jalan, dan keamanannya kamu yang jaga. | header → Minusnya · trade-off; "JADWAL OTOMATIS · CONTOH": laptop tile NYALA → TIDUR → NYALA while a day track runs under 07.00 rekap penjualan (JALAN) / 12.00 cek email masuk (TERLEWAT, dimmed) / 21.00 laporan harian (JALAN); "bisa juga dipasang di server sendiri"; white checklist "Yang kamu jaga" ticks: Download dari repo resmi · Tak ada token kripto resmi · Level izin: Ask · API key jangan dibagi |
| s09 | 44.60–46.63 | Mau link resmi plus urutan setting-nya? | header → Urutan setting · link resmi · 4 langkah; 4 rows: 1 Download OpenMausBot (github.com/milind-soni/OpenMausBot, RESMI), 2 Install Hermes Agent, lalu login (github.com/NousResearch/hermes-agent · hermes model, RESMI), 3 Pilih engine Hermes di tiap bot, 4 Ubah level izin ke Ask (+ approvals.mode: manual); numbers pulse on "urutan"; last 0.3 s rows fold, header lifts away |
| s10 | 46.63–49.80 | Komen AGENT, aku kirim lewat DM. | "OpenMausBot + Hermes · link resmi + urutan setting" card pops; comment bar, AGENT typed per letter (caret), heart; DM panel (AI PRENEUR pill) + paper plane, the card lands as attachment, "terkirim"; end logo (corner logo fades at 48.40) |

Hand-overs: s01 → s02 keep the two badges (the OpenMausBot badge turns into the topic header); s02–s09 share the same header plate (its
icon/name/sub/chip roll between topics, one more progress segment per topic); every workspace exits in its scene's last ~0.2 s, so the
next scene starts from the header alone; s09's rows fold into the "panduan" card that pops in at the start of s10.
Hosts: mascot bottom-left (welcome, question on "siapa?", present/explain/emphasize per beat, compare on "bayar."/"Minusnya,", cta on
"Komen"), robot bottom-right (thinks on "numpang", types the chat/skill/login/switch, scans the roster/meter/schedule, startles on
"dikirim" and "default-nya", cheers on "open" and "Komen").

## Sources (checked 12 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- github.com/milind-soni/OpenMausBot — README (what it is, "Also known as MausBot; formerly OpenGrokBot", local-first 127.0.0.1 +
  `~/.openmausbot`, Allow/Deny cards, free + open source, no token, `npx openmausbot serve`, "must remain running"), LICENSE (Apache-2.0),
  `apps/docs/content/docs/providers/index.mdx` (built-in engine "Hermes · Hermes CLI login · ACP integration"), `docs/approval-levels.md`
  (every bot starts at Full access; Ask for approval), `docs/custom-engines.md`, `server/drivers/acp/hermes.ts`.
- github.com/NousResearch/hermes-agent — README (self-improving, skills from experience, MIT, built by Nous Research), LICENSE (MIT),
  `website/docs/integrations/providers.md` (`hermes model` → "ChatGPT or Codex Subscription", device-code login; DeepSeek via
  `DEEPSEEK_API_KEY`), `website/docs/user-guide/security.md` (dangerous-command approval, smart/manual/off, `curl … | sh` pattern),
  `…/features/skills.md` (`~/.hermes/skills/`), `…/features/memory.md` (`~/.hermes/memories/`), `…/features/acp.md` (memory + skills
  kept over ACP; approval prompts are up to the host).
- Not reachable from this session: openmausbot.com / mausbot.com (network policy) — nothing is taken from them.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R9 kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors, 0 contrast warnings (fixed: the "· 127.0.0.1" suffix and the DEFAULT tag);
  remaining warnings = "multiple Three.js instances" (robot + mascot bundles, as in the kit) + SwiftShader ReadPixels notices.
- Script check (`tools/check_scene.cjs`, preview on :8935, then stopped): every scene/robot/mascot/main timeline registers, no exceptions.
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): one full pass of 58 frames — first frame, every scene's beats, both sides of
  every cut, the end — + targeted fix passes (s09→s10 seam after the header fade, the two contrast fixes, a final 4-frame sanity pass after
  stripping the preview's stamped ids). Contact sheets (JPG): `production/qa/runtime_full_1..4.jpg` (full frames),
  `production/qa/runtime_hero_1..4.jpg` (hero zone + captions, larger), `production/qa/runtime_fix_seam_s09_s10.jpg`,
  `production/qa/runtime_fix_contrast.jpg`. PNG dumps deleted (disk budget).
- Fixed during QA: row-highlight ids collided with the header chip ids in s02 (chip invisible, all rows outlined); the shared typer selected
  word spans as letters when typing into a `<span>` (last word visible before typing, s03/s05); reply typing too slow to read in s02;
  DITERIMA stamp covered the avatar; header vanished on the s09→s10 cut; unsupported glyphs (✓ → ▸) replaced by SVG/entities
  (Poppins latin has none of them).

## Known issues / notes for the lead
- Short "header only" beats at the start of every topic (≈0.1–0.3 s while the header rolls and the workspace rises) — intentional
  breathing room, same as R9; a caption chunk can show an empty chip for 1–2 frames at its very start while its first word rises (house
  caption behaviour).
- s08: the lower half of the hero zone is empty until the checklist lands at ≈42.3 s (the schedule panel carries the beat).
- All on-screen examples are illustrative and labelled "contoh": bot names/jobs, the email thread, SKILL.md steps and rev 1–3, the
  routines 07.00/12.00/21.00, the `curl … | sh` command (a pattern Hermes really flags). The chat app, terminal and settings card are our
  own mocks, not screenshots of either product. "Ask for approval / Full access" and "ChatGPT or Codex Subscription" are the real labels.
- "nggak perlu API key" refers to the ChatGPT-plan login; Hermes docs do not list which ChatGPT tiers qualify, so no tier is named.
  DeepSeek needs an API key (pay per use) — said as "bayar per pemakaian", no prices.
- Links for the DM: `github.com/milind-soni/OpenMausBot` (releases there) and `github.com/NousResearch/hermes-agent`. A look-alike repo
  `OpenMausBot/OpenMausBot` (copied README, 7 commits, its own releases) exists — do not send that one.
- `hyperframes snapshot`/`preview` write `.hyperframes/` into the project folder (harmless); the preview's stamped `data-hf-id`
  attributes were stripped again so the files match the kit.
- VO is 48.48 s; the reel is 49.80 s (≤ 50 s): tail after "DM." ≈ 1.0 s with the end logo (TAIL 1.4 s in timing.py instead of 1.6).
