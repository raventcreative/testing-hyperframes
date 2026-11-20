---
name: aipreneur-reels-studio
description: Produce AIpreneur (Freddie Kashawan) IG Reels remakes and covers exactly like the testing-hyperframes sessions — 3D voxel world + the client's 3D mascot host, Indonesian ElevenLabs VO (voice Dakocan), navy/white brand themes, per-word captions, open-source 3D logos, minimal thumbnails, testimonial covers, ATM (Amati-Tiru-Modifikasi) remake rules, and a strict no-cut-text QA. Use for any "remake video ini", "bikin reels", "thumbnail", "testimoni" request from this client.
---

# AIpreneur Reels Studio

Client: Freddie Kashawan (AIpreneur). Replies in **Bahasa Indonesia**, short, practical. Deliver finished files only
(no drafts for approval unless asked). Repo with every past project and kit: `github.com/raventcreative/testing-hyperframes`
(branch `main`). Commit + push after every meaningful step (the session has a stop hook that demands it).

Read these references before working:
- `references/brand.md` — themes, colours, fonts, logo, captions (**follow exactly**)
- `references/voxel_reel.md` — the 3D voxel + mascot reel format, engine, transitions, timing
- `references/thumbnails.md` — navy/white minimal covers + testimonial covers
- `references/client_rules.md` — every rule/feedback the client gave (the "why" behind the format)
- `references/qa.md` — the checks to run before sending anything

## End-to-end workflow (remake of a reference video)
1. **Analyse the reference**: ffprobe; 24-frame contact sheet; transcribe with faster-whisper (`small`, numpy input,
   language auto). Note structure, beats, claims.
2. **Fact-check** every claim with WebSearch. Drop what you can't verify; attribute frameworks ("dipopulerkan X").
3. **Script (ATM)** in Indonesian, "kamu" voice, own hook + own order + own metaphors, never >3 consecutive words of
   the reference, add the AIpreneur angle (AI that helps), no earning promises. ~40–56 s. Last line
   `Komen <KEYWORD>, aku kirim <hal> lewat DM.` Write `production/VO_SCRIPT.md` with an "ATM: what we changed" + sources.
4. **VO**: `python3 scripts/vo/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (one line per sentence, no
   --tags → auto tags). Listen-check with faster-whisper small AND medium; reword only words BOTH mishear
   (known bad: "pembukaan", "penyedia", "calon mitra"; "rahasia" triggers [whispers]).
5. **Build** from `templates/voxel_reel/` (copy into `projects/<name>/`): words.py → vo_data.py → write scenes in
   vendor/vx.js → tools/build.py → `npx --yes hyperframes@0.8.186 check .` (0 errors).
6. **QA** per `references/qa.md`: snapshot EVERY second, look at every frame, fix, re-snapshot.
7. **Render**: `nohup setsid bash -c "sleep 15; scripts/render/render_aip.sh $PWD <NAME>.mp4" &` (delayed launch, or
   the render is cancelled when the tool call exits). ~0.75 frame/s with 3D. Verify duration, whisper the final audio,
   sample 12 frames and look.
8. **Deliverables**: video, cover 1080×1920 + HD 2160×3840, `production/DM_<KEYWORD>.md` (what the commenter gets —
   must match any "GRATIS"/number promise on the cover), `production/CAPTION.md` (complementary angle, CTA, hashtags
   `#aipreneur #skoolcommunity #aimarketing`). Send with SendUserFile, short Indonesian summary, commit + push.

## Hard rules (summary — details in references)
- Theme alternates navy ↔ white per delivered video. Only brand colours in UI text (see brand.md).
- World first (full screen, no mascot) → zoom-out reveal → mascot rises from the bottom and hosts the rest.
- Every transition different in a video; never the same motion twice in a row.
- Logos: Simple Icons (CC0) → extruded 3D (SVGLoader + ExtrudeGeometry), credits in production/asset_credits.json.
- No text ever cut by the frame, by a texture edge or hidden behind objects/captions. Captions never over the mascot face.
- Covers: minimal, negative space, ONE topic logo in 3D above the mascot's head.
- Never paste API keys in chat; ElevenLabs key is injected by the environment proxy (`xi-api-key: proxy-injected`).
  In a new environment the user must add the ElevenLabs key as an environment network secret for api.elevenlabs.io.
