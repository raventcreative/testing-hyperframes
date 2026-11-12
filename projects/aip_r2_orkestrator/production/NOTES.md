# AIP R2 · 4 open source buat ngatur banyak AI agent — production notes (LIGHT)

Project: `projects/aip_r2_orkestrator/` · 1080×1920 · 30 fps · **48.9667 s** (1469 frames) · HyperFrames 0.8.186 · kit copied from
`projects/promptbuilder_2026/` (light bg + animated grid, robot + mascot, captions, SFX synth). Serve: `python3 -m http.server 8822 --bind 127.0.0.1`.
Script + fact check: `production/VO_SCRIPT.md`. VO 47.36 s starts at 0.30 s (`assets/audio/vo.mp3`), SFX bed `assets/audio/sfx.wav`.

## Pipeline (re-run in this order after any VO change)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`
   (writes `assets/audio/vo.json` → move to `production/vo_el_alignment.json`)
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (from the ElevenLabs character alignment, no whisper)
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (snapping disabled for alignment input; "Team AI" → "TeamAI", "agent," → "AGENT,")
4. `python3 -I tools/rounds.py .` → `vendor/rounds.js` (the 4 tools t1–t4) · `python3 -I tools/build_index.py .` → `index.html` (+ `vendor/r2kit.js` in head)
5. `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav`
6. cover: `node thumbnail/render_cover.cjs thumbnail/COVER_ORKESTRATOR_1080x1920.png` (server on :8822)

## Shared kit: `vendor/r2kit.js` (window.R2)
TOOLS (names + repo paths as text), `ic()` lucide mask icons (ISC), the 4-pill **TOOL RAIL** (y 312, x 124 + i·212, 200×56; upcoming =
number + skeleton, active = navy + name wipes in on the spoken name, done = green check) drawn identically in s01 · t1–t4 · s06, and the
white app-card header (x 70–1010, y 392–930) used by t1–t4.

## Scenes (global s)
| id | start–end | VO | visual · transition out |
|---|---|---|---|
| s01 | 0.00–6.33 | AI agent kamu makin banyak, tapi makin berantakan? Ini empat open source gratis buat ngaturnya. | 4 agent windows at frame 0 → 9 on "makin banyak" → red tangle lines, error badges, "Notifikasi numpuk" toast + shake on "berantakan?" → pile swept down/dimmed on "Ini" → rail drops in + "4 open source" on "empat", underline "open source", green GRATIS seal slams on "gratis", the same 9 agents snap into a tidy green grid on "ngaturnya." · everything but the rail lifts away |
| t1 | 6.33–15.07 | Satu, OpenHands Agent Canvas. Satu pusat kontrol buat jalanin Claude Code, Codex, sampai Gemini, di laptop, server, atau cloud. | card rises; agent rows (OpenHands, Claude Code, Codex, Gemini CLI) start on their words (counter 1→4), "+ agent lain yang support ACP", control-centre panel on "pusat kontrol", Laptop/Server/Cloud tiles switch on their words; robot types on its holo keyboard · card flips edge-on (rotY 90) |
| t2 | 15.07–22.57 | Dua, Paperclip. Kamu bikin perusahaan isi AI agent: ada struktur tim, tugas, budget, dan approval dari kamu. | flips in from −90; org chart: Kamu (pemilik) → Agent CEO → 3 agent employees, "Perusahaan AI" chip, org lines draw on "struktur tim", task chips, budget meter, approval request + pointer click "Setujui" → "Disetujui" on "kamu." · pushed off left |
| t3 | 22.57–29.70 | Tiga, Orca. Satu agent jadi koordinator, bagi tugas ke agent lain, masing-masing kerja paralel di worktree sendiri. | slides in from right; coordinator + crown, "Tugas besar: fitur checkout" splits into 3 pieces that land in 3 worker lanes (Claude Code / Codex / Gemini CLI), 3 progress bars run in parallel, worktree tags, "selesai" + "3/3 beres" · sinks + fades |
| t4 | 29.70–37.93 | Empat, TeamAI dari Tencent. Skill, rules, sama MCP semua agent di tim disimpan di satu repo Git, terus sync otomatis. | iris opens; "dari Tencent" chip; repo-tim fills (skills/, rules/, mcp/, + agents, models), 4 teammates' agents (Claude Code, Codex, Cursor, OpenCode), `$ teamai init github.com/tim-kamu/repo` types, Git tag, sync dots travel out → "✓ sync" badges · shrinks away |
| s06 | 37.93–43.93 | Keempatnya open source, gratis. Cuma, model AI-nya tetap pakai akun atau API kamu sendiri. | rail pills drop into a 2×2 grid of tool cards, "Lisensi MIT · open source" badge stamps, "Tool-nya GRATIS dipakai" ribbon; on "Cuma," grid shrinks up and the honest note rises: Model AI → Akun kamu / API key, "Tool gratis, biaya model ikut akun / API kamu" · lifts away |
| s07 | 43.93–48.97 | Mau link plus cara install-nya? Komen AGENT, aku kirim lewat DM. | "Paket link 4 repo" card (4 GitHub paths) + "+ cara install" sticker, comment bar types AGENT + heart + send, paper plane, DM card "4 link repo + cara install" → "terkirim ✓" on "DM."; end beat 47.77: corner logo fades, big dark AI PRENEUR logo |

Robot (co-host, right) flies in on "Ini", waves, types during t1, presents/points/scans/claps through t2–t3, looks at the host in t4,
shakes its head on "Cuma,", cheers the CTA. Mascot (host, left) counts each tool and presents it, glances at the robot on its fly-in and on "AGENT,".

## QA (real runtime, `npx --yes hyperframes@0.8.186 snapshot`)
- Contact sheets (scratchpad `aipr2/`): `finalF1/contact-sheet-{1,2}.jpg` (0–21 s), `finalF2/contact-sheet-{1,2}.jpg` (22–43.8 s),
  `finalF3/contact-sheet.jpg` (44–48.96 s), `finalF4/contact-sheet.jpg` (re-check after the last fixes: t4 iris, end beat).
- `hyperframes lint .` → 0 errors (2 kit warnings about #bg/#fx in index.html). `hyperframes validate .` → 0 errors; warnings = kit's
  "multiple Three.js instances" + WCAG notes, most of them false positives on stacked state layers (white text on navy tiles).
- Captions: all 35 chunks measured one line, widest 765 px (< 940).

## Known issues / notes
- The mascot's eyes show the kit's strong glass highlight while it glances sideways at the robot (same as the approved kit; only 2 glances).
- t1/t2/t3/t4 cards have ~0.6–1 s of header-only before the body fills (the body enters on the first spoken beat).
- After "Cuma," the 2×2 tool grid is shown at 72 % scale (context only; the note card is the focus).
- Official websites (openhands.dev, paperclip.ing, onorca.dev) were not reachable from this session (DNS blocked); facts come from the
  GitHub READMEs + LICENSE files (raw.githubusercontent.com), see VO_SCRIPT.md.
- Full render not run (the lead renders). Nothing committed.
