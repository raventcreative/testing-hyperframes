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
SCENES_TABLE

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
QA_RESULTS

## Known issues / notes for the lead
KNOWN_ISSUES
