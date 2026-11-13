# NOTES — R21 · 6 agent AI, pilih yang mana? (AI PRENEUR · NAVY)

- **Duration** 46.20 s (1386 frames @30) · VO 44.83 s starting at 0.30 s (spoken 35–48 s ✓) · CTA keyword **PILIH** · reference
  `aip_remake_batch6/refs/ref1.mp4` (106 s, English). Agents (all six verified, none dropped): Dots (OpenAI), Muse (Meta), Grok Bot (x.ai),
  OpenClaw (OpenClaw Foundation, MIT), Hermes Agent (Nous Research, MIT), MausBot / OpenMausBot (Apache 2.0). Claim-by-claim sources +
  "ATM: what we changed" in `production/VO_SCRIPT.md`.
- **Kit**: copied from `projects/aip_r19_jarvis` (NAVY; without `out/`, `.hyperframes/`, its VO/QA/cover PNG/scenes/bed). Index built by
  `tools/build_index.py` from `production/timing.json`; shared scene kit `vendor/r21kit.js` (+ `vendor/r21icons.js`, Lucide 1.70 ISC,
  generated from lucide-static): topic header with icon roll + 7 progress segments, agent card (generic icon + name + maker, text only),
  timeline boilerplate. **Initial states are pinned in a nested timeline that is the first child at 0** (`I()` → `P0.set`, in every scene
  and in the main/caption timeline via `pin()`), and every timeline ends its build with `tl.render(0, true, true)`. Scene lengths come
  from the timing via `K.dur(id)`. Audio as the batch kits: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` +
  `<audio id="sfx" src="assets/audio/sfx.wav">` — no music (the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = client's AUTO tags: `[playful] [excited]` on every line + `[curious]` on line 1 and `[confident]` on the CTA), ONE call,
  44.88 s, no re-take (≈ 690 characters) → `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json`;
  `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js` (scene starts fixed by line index because "OpenClaw" opens two
  lines; the keyword is sent lower case "pilih" and shown as PILIH via `FIXI`; PRON map updated for lip sync). Listen-check with
  faster-whisper small + medium (id): no word misheard by both.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples; mean −34.1 dB / peak −12.9 dB,
  R19 −35.3 / −12.9).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_PILIH_1080x1920.png` (`python3 -m http.server 8951 --bind 127.0.0.1` at the project
  root, then `PORT=8951 node thumbnail/render_cover.cjs thumbnail/COVER_PILIH_1080x1920.png`; server stopped). NAVY: chip "6 AGENT AI ·
  CLOUD · OPEN SOURCE", "6 agent AI lagi rame, / PILIH MANA? / cloud atau open source? jawab 1 ini", the reel's road fork with the two
  signposts + "kamu" disc + "?", mascot presenting + robot thinking. Key content inside the 4:5 crop (y 285–1635). No third-party logos.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–6.83 | Enam agent AI lagi rame. Sebelum pilih, jawab ini dulu: tinggal pakai, atau pegang sendiri? | big cyan "6" + "agent AI" + "lagi rame" chip; six white agent cards (Dots, Grok Bot, Muse, OpenClaw, Hermes, MausBot — generic icons, text names) pop in like notifications, "+1" pings, wobble on "rame"; "Sebelum": cards sucked to the centre, white card "Sebelum pilih: 1 pertanyaan" slams in; "tinggal pakai": label "1 PERTANYAAN", a road FORK draws itself with two signposts (Tinggal pakai · jalan di cloud mereka / Pegang sendiri · open source, di mesinmu); the "KAMU" disc drives up, leans left (left branch + sign light) then right ("pegang sendiri"), "?" bubble |
| s02 | 6.83–13.20 | Tinggal pakai: Dots dari OpenAI, Grok Bot, dan Muse dari Meta, yang belum ada di Indonesia. | header builds (Tinggal pakai · CLOUD, 1/7); navy cloud silhouette "CLOUD MEREKA · komputer & server milik penyedia"; on each name a tag card drops on a string and sways (Dots · OpenAI · di ChatGPT · komputer cloud sendiri · BERBAYAR; Grok Bot · x.ai · tim bot · komputer cloud bersama · BERBAYAR; Muse · Meta · agen personal · mesin virtual di cloud · GRATIS (DASAR)); "belum": amber "ID" pin with a ban line; "Indonesia": amber stamp BELUM DI INDONESIA on Muse, card dims |
| s03 | 13.20–18.30 | Praktis, kerja terus di cloud mereka, tapi data dan login aplikasimu ikut di sana. | header → Plus-minusnya · JUJUR; cloud stays; green "praktis · tanpa install"; "kerja terus": the laptop lid closes ("laptopmu mati", moon) while the KOMPUTER CLOUD card (CONTOH) ticks its tasks; "tapi data dan login": dashed tray "PUNYAMU" with three chips (data bisnismu, login email, login aplikasi); "ikut di sana": they fly up into the cloud, lock badge, amber card "Disimpan di server mereka · data bisnis + login aplikasi yang kamu sambungkan · PRAKTIS, TAPI BUKAN DI TANGANMU" |
| s04 | 18.30–23.03 | Pegang sendiri: OpenClaw dan Hermes, open source di laptop atau servermu. | header → Pegang sendiri · OPEN SOURCE; big key turns and shrinks into the dashed boundary "MESINMU · kamu yang pegang"; OpenClaw (OpenClaw Foundation) and Hermes (Nous Research) cards slide in on their names; "open source": "MIT · kode terbuka" badges; Laptop / Server (VPS / server sendiri) tiles light on their words, dashed links |
| s05 | 23.03–27.00 | OpenClaw kamu chat dari WhatsApp, Hermes nulis skill dari pengalamannya. | header → OpenClaw & Hermes · MIT; left: our own phone mock "OpenClaw · kamu chat lewat WhatsApp" (CONTOH): "rekap pesanan hari ini?" → typing dots → "12 pesanan, 3 belum bayar", composer bar; right: Hermes panel, task card "rekap stok mingguan ✓" flips into "SKILL BARU · rekap-stok" and drops into the SKILL-NYA drawer (4 → 5), "ditulis dari tugas yang barusan" |
| s06 | 27.00–33.73 | Kendalinya di tanganmu, keamanannya juga. Bawaan OpenClaw jalanin perintah tanpa nanya, ubah ke mode ask. | header → Izin bawaan · PENTING (amber); tiles KENDALI "di tanganmu" (cyan) and KEAMANAN "juga di tanganmu" (amber) light on their words, footnote "open source: kamu yang atur, kamu yang jaga"; settings card "OpenClaw · setelan bawaan": `tools.exec.mode` switch [full · jalan tanpa nanya \| ask · minta izin dulu], knob on full (amber, BAWAAN); "jalanin perintah": `$ rm -r arsip-lama/` (CONTOH) → "✓ dijalankan · tanpa konfirmasi", card shakes, amber "langsung jalan, tanpa ditanya"; "ubah ke mode ask": `$ openclaw config set tools.exec.mode ask` types, knob slides to ask (cyan) |
| s07 | 33.73–38.90 | Yang keenam beda: MausBot. Bukan agent baru, tapi pengatur agent yang kamu punya. | header → MausBot · APACHE 2.0; "#6" badge → white hub (network icon) + rotating dashed ring, "MausBot · open source · Apache 2.0"; "Bukan agent baru": dashed "+ agent baru" card gets a red X; "pengatur agent": four chips dock (Claude Code, Codex, Grok CLI "sudah kamu login", Hermes "lewat ACP"), spokes draw, pulses run hub → agents on "kamu punya"; footnote "bawaan: Full access → pilih Ask" |
| s08 | 38.90–42.93 | Jadi, mau praktis, pilih cloud. Mau kendali, pilih open source. | header → Cara milih · PILIH (7/7); slider [PRAKTIS \| KENDALI] (knob undecided in the middle); "praktis": knob left, answer card "Pilih cloud · tinggal pakai" (Dots, Grok Bot, Muse*; green "tanpa install, langsung jalan"; amber "data & login di server mereka"; "* Muse belum tersedia di Indonesia · Dots & Grok Bot berbayar"); "kendali": knob right, card flips (flat) to "Pilih open source · pegang sendiri" (OpenClaw, Hermes, MausBot; green "aplikasi gratis, kendali penuh"; amber "rawat & atur izin sendiri"; "MausBot = pengatur agent-mu · modelnya pilih sendiri · ganti izin bawaan ke ask"); header + card leave |
| s09 | 42.93–46.20 | Komen PILIH, aku kirim lewat DM. | house CTA: card "Tabel pilih 6 agent · + link resmi & setting aman"; comment bar, PILIH typed per letter + caret, heart; DM panel (AI PRENEUR) "Ini tabelnya + link resmi & setting aman, ya", paper plane, card lands as attachment, "terkirim"; end logo (corner logo fades at 44.80) |

Hosts: mascot bottom-left (welcome, question on "Sebelum", present/explain/emphasize per beat, compare on "tapi" and "Jadi", reveal on
"Praktis"/"MausBot", cta on "Komen", point on "DM."); robot bottom-right (think on "Sebelum"/"data"/"keamanannya", scans the cards, "no"
on "Indonesia"/"Bukan", types the cloud task / the chat / the config command, shock on "sana"/"tanpa", cheers on "Pegang"/"punya"/"Komen").
**Mascot glance-at-robot disabled from the start** (`const glance = (t) => 0;`).

## Sources (checked 13 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- Dots: help.openai.com/en/articles/20001530-getting-started-with-your-dot, openai.com/index/introducing-dots/, ChatGPT release notes
  (read via domain-restricted search: openai.com does not resolve from this session).
- Muse: about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/, about.fb.com/news/2026/10/muse-is-now-available-in-singapore-…,
  about.fb.com/news/2026/09/introducing-muse-small-business/, muse.ai/security-and-privacy.
- Grok Bot: x.ai/bot, x.ai/news/introducing-grok-bot, docs.x.ai/grok-bot/{how-grok-bot-works, faq, bots, security,
  skills-routines-and-automations}, x.ai/news/x-subscription (read via domain-restricted search: x.ai does not resolve from this session).
- OpenClaw: github.com/openclaw/openclaw (sparse clone, commit d5d77e1, 13 Nov 2026) — README, LICENSE, docs/tools/exec-approvals.md,
  docs/tools/permission-modes.md.
- Hermes Agent: github.com/NousResearch/hermes-agent (commit 9d94f82) — README, LICENSE, website/docs/user-guide/security.md.
- OpenMausBot / MausBot: github.com/milind-soni/OpenMausBot (commit d76d024) — README, LICENSE, docs/approval-levels.md,
  apps/docs/content/docs/providers/index.mdx.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R15/R19 kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the kit)
  + SwiftShader ReadPixels notices. The first run flagged 2 contrast warnings on the s05 phone at t=23.1 s (phone fading in; placeholder
  "ketik pesan…" too pale) → fixed (phone slides in fully opaque, darker sub-label, lighter placeholder); re-run: 0 errors, 0 contrast warnings.
- Script check (`tools/check_scene.cjs`, HyperFrames preview on :8951, then stopped): s01–s09, robot, mascot, main all register, no
  exceptions; the preview's stamped `data-hf-id` attributes were stripped again afterwards.
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): one full pass of 71 frames (first frame, every scene's beats, both sides of
  every cut, the end) + targeted fix passes (27 + 9 + 2 + 2 frames). Contact sheets (JPG): `production/qa/runtime_full_1..3.jpg` (full
  frames, full pass — predates the fixes below), `production/qa/runtime_hosts_1..2.jpg` (mascot + robot, eye check),
  `production/qa/runtime_fix1_hero_1.jpg` (hero zone after fix 1), `production/qa/runtime_fix2_hero_1.jpg` (after fix 2),
  `production/qa/runtime_fix3_hero_1.jpg` (s05 opening + s06 end after the last fixes). PNG dumps deleted (disk budget).
- Mascot eyes: pupils in every frame of the full pass (half-closed lids at 3.5 / 43.4 / 44.4 s = blinks); glance disabled from the start.
- Fixed during QA: s02 cloud was offset +67 px vs s03 (GSAP svgOrigin on an SVG group in the real runtime) → cloud wrapped in an HTML
  layer, tweened with a CSS transform-origin; cloud label crossed the lobe notches → bigger cloud body; s01 "KAMU" label sat on the road
  stem → moved beside the disc on a chip; s01 cards enlarged; s03 rebuilt fuller (bigger laptop + cloud computer, PUNYAMU tray, big amber
  "Disimpan di server mereka" card instead of a small chip); s05 bigger bubbles + composer bar, skill card stays on screen and a copy
  flies into the drawer; s06 bigger text, card resized so the last command line is never clipped; s07 bigger agent chips; s08
  "MausBot" chip was clipped by a PENGATUR tag → tag removed (role moved to the note line).

## Known issues / notes for the lead
- Frame 0 shows the "6 agent AI" headline only: the agent cards pop in from 0.04 s, the mascot pops up from below over 0.5 s and the
  robot flies in over 0.75 s (kit behaviour, same as R15/R19). The cover is separate.
- Short "header only" beats at the start of each topic (≈0.1–0.3 s while the header rolls and the workspace rises) and a ≈0.16 s
  header-only beat before s07 (the s06 card fades just before the cut) — intentional, same as R19; a caption chunk can show an empty chip
  for 1–2 frames while its first word rises (house caption behaviour).
- All on-screen examples are illustrative and labelled CONTOH / mocks (chat, task list, `rm -r arsip-lama/`, skill "rekap-stok").
  Agent cards, phone, settings card, hub and slider are our own mocks with generic Lucide icons; brand names are text only.
- DM content (not in the VO, for the team): official links — github.com/openclaw/openclaw, github.com/NousResearch/hermes-agent,
  github.com/milind-soni/OpenMausBot (beware the look-alike repos, see R15), help.openai.com dots article, about.fb.com Muse post,
  x.ai/bot; safe settings — OpenClaw `openclaw config set tools.exec.mode ask` (or `auto`), Hermes `approvals.mode: manual`,
  OpenMausBot level "Ask for approval"; Dots/Grok Bot are paid, Muse not in Indonesia yet (13 Nov 2026).
- `hyperframes snapshot`/`preview` wrote `.hyperframes/` into the project folder (harmless, as in R15/R19); the preview's stamped
  `data-hf-id` attributes were stripped again.
