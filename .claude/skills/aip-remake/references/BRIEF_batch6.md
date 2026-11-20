# AI PRENEUR · remake batch 6 (R21–R25) — build brief

Same house style, pipeline, QA lessons and house rules as batches 3–5 — read `projects/aip_remake_batch3/BRIEF.md`,
`projects/aip_remake_batch4/BRIEF.md` and `projects/aip_remake_batch5/BRIEF.md` (ATM rules + "Lesson from R12/R13 QA") in full first.
References: `projects/aip_remake_batch6/refs/refN.mp4` + `refN.txt` (faster-whisper transcripts — names garbled, read them off the frames).
ref2/ref3 are Indonesian reels by another creator (Hisham); ref1/ref5 are English; ref4 Indonesian.

## ATM — Amati, Tiru, Modifikasi (client insists: a real remake, never a copy-paste)
As in batch 5: own hook (different words AND angle), own structure/order and own visual metaphor per beat, Freddie's practitioner angle
only where true (never invented results), Indonesian-audience value the reference lacks, own CTA keyword + closing line, never more than 3
consecutive words of their script, verify every fact on official sources and drop what you can't verify. Do NOT copy the other creator's
name, greetings, thank-you lists or donation mentions. Write "ATM: what we changed" + sources in `production/VO_SCRIPT.md`.

## IMPORTANT — overlap with reels we already published (read their production/VO_SCRIPT.md and make yours clearly different)
- R15 `aip_r15_hermes` (OpenMausBot + Hermes as "office + employee"), R20 `aip_r20_freellm` ("app = body, model = brain" metaphor),
  R11 `aip_r11_harness`, R8 `aip_r8_web3d` (MotionSites 3D websites → sell to clients, CTA 3D), `plugin4_2026` (Superpowers, Karpathy
  Skills, token-compression skill, Codex plugin). Never repeat their hooks, metaphors, layouts or CTAs.

## Order / colours (alternation continues — R20 was LIGHT)
**R21 NAVY · R22 LIGHT · R23 NAVY · R24 LIGHT · R25 NAVY.** Kits (mascot glances already disabled): NAVY → copy `projects/aip_r19_jarvis/`
(or `aip_r15_hermes/`); LIGHT → copy `projects/aip_r20_freellm/` (or `aip_r12_cuanrepo/`). Never copy `out/`. Cover follows the colour.
VO: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py <lines.txt> <out.mp3>` with NO --tags (client's AUTO tags).
**ElevenLabs credit is limited (≈14k characters for the whole batch): aim for ONE take; re-take only if a word is misheard by BOTH
faster-whisper small and medium — then reword that word (avoid words that previously failed: "pembukaan", "penyedia", "calon mitra").**
Spoken length 35–48 s (≈2.5 words/s). Last line "Komen <KEYWORD>, aku kirim lewat DM." (send the keyword in lower case if it would be
spelled out; caption shows it upper case). CPU is shared with 4 other builders and a render queue: one full real-runtime snapshot pass +
targeted fix passes, JPG contact sheets only, delete PNG dumps.

## The five reels
- **R21 · 6 agent AI, pilih yang mana?** (NAVY · `aip_r21_pilihagent` · port 8951 · ref1, 106 s → ≤ 48 s): the reference compares six
  agents (it says "Dots", "Muse", "Grok bot", OpenClaw, Hermes, MausBot — verify each real name/maker/what it does; DROP any you can't
  verify, e.g. say "4 agent" if only 4 check out). Our angle: a decision guide for Indonesian business owners — "jalan di cloud orang"
  (easy, data at the provider) vs "open source di laptopmu" (control, but you maintain it), and one orchestrator. R15 already explained
  OpenMausBot + Hermes in depth: keep them to one beat each here, no "kantor/karyawan" metaphor. Honest cautions (default permissions,
  e.g. if verified that one runs commands without asking). CTA **PILIH**.
- **R22 · Agent AI di server: 3 lapis pengaman** (LIGHT · `aip_r22_amanagent` · 8952 · ref2, 178 s → ≤ 48 s): what if an agent with
  server access quietly reads password files / changes other settings / runs commands you never asked? Layers from the reference: separate
  non-admin account for the agent; command logging (Linux auditd); git snapshot before + git diff after; logs owned by admin so the agent
  can't erase them; then permission settings (Hermes approvals / OpenCode permission config). Verify every command/setting name on official
  docs (auditd, git, Hermes docs, OpenCode docs). Our own angle + order, practical checklist feel for Indonesian freelancers/UMKM devs who
  let agents touch a client's website. CTA **AMAN**.
- **R23 · Biar agent nggak asal ubah file: rencana dulu** (NAVY · `aip_r23_plandulu` · 8953 · ref3, 125 s → ≤ 45 s): Hermes and
  OpenCode (free, open source, pick any model, work in a folder, skills, sub-agents, terminal or desktop) + the one habit: ask for a plan
  first (OpenCode plan mode / Hermes `/plan` — verify the exact names) → read → approve → then it works. R20 used "body vs brain" and R15
  covered Hermes: lead with the HABIT (plan first) as the hero, the two tools as the "where", fresh visuals (e.g. blueprint before
  construction). CTA **PLAN**.
- **R24 · 4 plugin biar Claude Code nggak kerja sambil merem** (LIGHT · `aip_r24_4plugin` · 8954 · ref4, 51 s → ≤ 48 s): Chrome DevTools
  MCP (Google), Context7, Supabase, Vercel — verify each (official MCP/plugin names, makers, what it really does, install). Our own hook
  (not "kerja sambil merem"), own order/metaphor (e.g. giving Claude eyes, a library card, keys to the database, a launch button), an
  Indonesian use case (UMKM web app end-to-end). Different from `plugin4_2026`. Caution: database/deploy access = careful with production.
  CTA **ALAT**.
- **R25 · Website 3D dari 1 prompt — bedah promptnya** (NAVY · `aip_r25_prompt3d` · 8955 · ref5, 50 s): SAME topic as our R8 (MotionSites
  library → sell 3D sites, CTA 3D). Do NOT redo R8. New angle: dissect what makes a single prompt produce a 3D site (the parts of the
  prompt: subject/mascot, scene & lighting, motion/scroll, sections, tech stack) and how to write your own for free, then pricing honestly
  for the Indonesian market (no "$500" claim, no earning promises). Read `aip_r8_web3d/production/VO_SCRIPT.md` and
  `STARTER_PROMPTS_3D.md` and make sure nothing repeats. Write the DM content `production/DM_SITUS.md` (a free prompt template). CTA **SITUS**.
