# R35 · "7 harta karun GitHub" — build brief (2026-11-24)

Client: "remake ya, dengan yang biru navy". Theme **NAVY**. Folder `projects/aip_r35_github7/`.
Reference: `refs/ref.mp4` (86.2 s, gitignored), transcript `refs/ref.txt`, contact sheet `refs/ref_sheet.jpg`.
Target length **80–90 s** (keep the reference's length — client rule).

## Follow exactly the batch-8 system
Read `projects/aip_remake_batch8/BRIEF.md` in full (format, skills to apply, VO hard rules, QA, render command,
brand-plate addendum) + the skill files it lists. Same format: voxel 3D world + the client's 3D mascot host + the AIpreneur
robot co-host. **Base kit = `projects/aip_r34_motionstudio/`** (navy, brand plate, mascot + robot, Claude-Code-recording
pipeline, SFX, remix) — copy it (hard-link big static assets to save disk; never copy `out/`), then rebuild scenes.
Background = ONLY the navy brand plate `projects/aip_r25_prompt3d/assets/brand/bg_1080x1920.png`. Rich audible SFX
(client asked "kasih sound effect biar gak suara VO aja"). VO = one untouched ElevenLabs take (Dakocan), whisper-medium
diff on the final MP4, −14 LUFS.

## Content (ATM: own hook/order/metaphors, ≤3 consecutive words of the reference, Indonesian, "kamu")
7 free open-source tools — **verify each on GitHub before writing** (repo owner/name, licence, what it does, platforms,
anything you state). Say only what the README says; drop/replace anything you cannot verify with a real verifiable repo.
Candidates from the reference:
1. Jan — `janhq/jan` (ChatGPT-like chat, runs local/offline)
2. Upscayl — `upscayl/upscayl` (AI image upscaler; Windows/Mac/Linux)
3. Buzz — `chidiwilliams/buzz` (offline transcription with Whisper)
4. Ultimate Vocal Remover — `Anjok07/ultimatevocalremovergui` (vocal/instrument separation)
5. Meetily — `Zackriya-Solutions/meetily` (AI meeting notes, local)
6. Chatterbox — `resemble-ai/chatterbox` (TTS; check language support — the reference says Indonesian is not officially
   supported: state only what the README says)
7. ComfyUI — `comfyanonymous/ComfyUI` or `Comfy-Org/ComfyUI` (check which is canonical; node-based image/video gen;
   heavy models need a strong GPU)
- Freddie angle (practitioner, business owner): which ones a business owner/creator actually uses (content, meeting,
  voice-over, product photos) — no invented results or numbers.
- Drop the reference's product plug ("cooling pad / link di keranjang") — not ours. A hardware caveat (GPU/RAM) is fine.
- One idea per tool, a visual metaphor per tool built in the voxel world (not the reference's flat cards); tool logos only
  if they exist in Simple Icons (CC0) — otherwise a voxel icon of our own. Do not use GitHub's octocat unless from
  Simple Icons (it is there: `github`).
- CTA keyword: **GITHUB** ("Komen GITHUB, aku kirim semua link-nya lewat DM").
- No stored client recording matches this topic (brand/rec has IG, website, Claude Code) — no screen recording needed;
  draw any UI as scripted windows (html-demo technique), labelled honestly (no fake screenshots of the real apps).

## Deliver (do NOT git commit/push — the coordinator does)
`out/AIP_R35_GITHUB_7_TOOLS.mp4`, covers `thumbnail/COVER_R35_GITHUB7_1080x1920.png` + HD (cover-topik navy, mascot +
ONE topic logo in 3D above the head: GitHub from Simple Icons), `production/DM_GITHUB.md` (the 7 verified repo links +
one line each + hardware notes), `production/CAPTION.md`, `production/VO_SCRIPT.md` (skills/techniques used, sources),
`production/asset_credits.json`. Report: final MP4 path, duration, loudness, whisper-medium diff result, what was
verified/dropped. Disk is tight (~2.7 GB free): delete your own `out/video.mp4` after the remix is final.
