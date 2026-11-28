# AI PRENEUR · remake batch 10 (R38–R39) — build brief (2026-11-28)

Client: "sekarang dua ini ya … pas ngejelasin maskot 3D-nya kamu majuin sampai setengah badan … kalau ngasih contoh maskot 3D
kamu hilangin biar video contohnya aja … foto 02/24 itu kamu hilangin … motion animasi, transisi, skill-nya gunain … jangan pakai
dunia voxel".

## Format = batch-9 2D look (see `projects/aip_remake_batch9/BRIEF.md` + the R37 build `projects/aip_r37_appngebut/` as the
reference implementation), with THESE CHANGES (client rules — also add them to the skill, see below):
1. **Explaining beats → mascot comes FORWARD, half-body.** When the VO explains / talks to camera (hook, "why it matters",
   transitions between ideas, CTA), the client's 3D chibi mascot is BIG in the foreground, framed from the waist up (half
   body: head + torso + hands, cropped at the waist by the frame bottom — this crop is intended), centred or slightly off-centre,
   gesturing/lip-synced, with the spoken headline above. Animate the move: push-in/rise from the small corner pose to the
   half-body pose (spring, no pop).
2. **Example / demo beats → NO mascot.** When a card, UI demo, diagram or example is on screen, the mascot is fully hidden
   (it exits — slide/scale out — before the example lands, and comes back for the next explaining beat). The example gets the
   whole frame: bigger cards than R37, readable text.
3. **No beat counter** ("02 / 24" pill with progress ring) — remove it entirely.
4. Keep everything else: spoken headline word-for-word at the top with one emphasised word (italic + accent), brand plate
   background only (navy / white), html-demo scripted windows, shared-element transitions, closed-form springs, a different
   transition each beat, motion blur on fast moves, rich SFX, pill CTA at the end. NO voxel world, no robot.
Base kits: WHITE → `projects/aip_r36_petaagent/`, NAVY → `projects/aip_r37_appngebut/` (copy, hard-link big assets, never copy
out/ or assets/rec/). Client recordings in `brand/rec/` only where the topic matches (not needed here unless you show Claude
Code); anything from `brand/rec` goes in a gitignored `assets/rec/`.

## Reels
| reel | folder | theme | ref | ref length | target | CTA keyword |
|---|---|---|---|---|---|---|
| R38 | `aip_r38_wifisensing` | **WHITE** | ref1 (open-source Wi-Fi sensing "see through walls, no cameras", RuView) | 43.4 s | 40–48 s | WIFI |
| R39 | `aip_r39_colibri` | **NAVY** | ref2 (Colibri: run big MoE models on your own PC, experts streamed from SSD) | 61.4 s | 58–66 s | COLIBRI |
References: `projects/aip_remake_batch10/refs/refN.mp4` (gitignored), `refN.txt`, `refN_sheet.jpg`.

### Fact rules (strict — the references overclaim)
- **Verify on GitHub before scripting** (README, LICENSE; raw.githubusercontent.com works when the API is blocked): exact repo
  owner/name, licence, what it really does, hardware it needs, platforms. Say ONLY what the README supports. No star counts
  unless read today from the repo page. If the repo cannot be found or does not do what the reference claims, STOP and report
  to the coordinator before building (do not invent a substitute).
- R38: ref1 claims "100k stars, MIT", "see you through walls", "watch every move from your phone". Check each. Wi-Fi
  sensing (CSI) typically needs specific hardware (e.g. ESP32 / particular NICs) — state the real requirement. Frame it
  responsibly: what it is, how it works (body movement changes Wi-Fi signals → model estimates pose/presence), real limits,
  and a privacy/consent note (only on your own space, with consent). No fear-mongering hook that the README does not support
  ("we're cooked" is fine as tone only if the claim under it is true).
- R39: ref2 names models (DeepSeek V4 Flash, GLM, Qwen, Kimi K3) and RAM figures (8/16/32 GB) — keep only the names and
  numbers that the Colibri README states; drop the rest. Explain MoE simply (many small experts, only a few work per word;
  always-on part in RAM, the rest on SSD, hot experts cached) — accurate to the README. Note SSD space + speed trade-off.
- Logos only from Simple Icons (CC0), 3D per the CLAUDE.md logo rule; record in asset_credits.json. Unbranded voxel/flat icons
  for anything without a Simple Icons entry.

## VO / QA / render / deliver — exactly as batch 8/9
ElevenLabs `tools/el_tts_ts.py` (Dakocan, eleven_v4), ONE untouched take (reword + regenerate the whole take when whisper small
AND medium mishear), whisper-medium diff on the FINAL mp4, −14 LUFS two-pass, rich SFX (≈8–10 dB under VO peaks, none on word
onsets, no sidechain on SFX) — add a soft "whoosh-in" when the mascot comes forward and a "pop-out" when it leaves.
`npx --yes hyperframes@0.8.186 check .` 0 errors; snapshot every second and look at every frame: mascot half-body never covers
the headline, never half-visible during demo beats, no cut text, cards inside the frame. Render with the shared-lock script
(batch-8 command; one render at a time; skips under 2200 MB free — disk ~2.8 GB, keep footprint small, delete your own
out/video.mp4 after the final remix). Deliver: `out/AIP_R3x_<TOPIC>.mp4`, covers 1080×1920 + HD (cover-topik: theme plate,
mascot + ONE 3D topic logo from Simple Icons above the head — or an unbranded icon if none exists), `production/DM_<KEYWORD>.md`,
`CAPTION.md`, `VO_SCRIPT.md` (techniques used), `asset_credits.json`, `VO_CHECK.md`. Do NOT commit/push.
