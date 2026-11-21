# QA before sending (do all of it)

1. `npx --yes hyperframes@0.8.186 check .` → 0 errors (mark canvases `data-layout-ignore data-layout-allow-occlusion`;
   keep only one root-level HTML with data-composition-id — templates live in tools/).
2. Snapshot EVERY second: `npx --yes hyperframes@0.8.186 snapshot . -o <dir> --at 0.5,1.5,…,N.5 --no-end --timeout 60000 --describe false`,
   build 6×2 contact sheets, look at every frame. Check: text cut by frame/texture edge, text behind objects, captions over
   the mascot face, empty caption boxes, camera inside/behind geometry, washed-out lighting, tiny unreadable labels,
   off-brand UI colours, mascot cropped, logos overlapping UI.
3. Zoom (crop at 2×) on any small text you are unsure about.
4. Render (delayed nohup launch), then: ffprobe duration; whisper the final audio once; sample 12–19 frames and look.
5. Covers: render, look, check headline/name widths and that nothing touches the frame edge.
6. Commit + push (`out/` is gitignored; MP4s are sent, not committed).
7. VO edits (lesson R30): never cut/pad the VO at line boundaries taken from the ElevenLabs alignment — they can sit
   inside speech (lines run together) and chop the next word ("Modul" → "odul"). Cut only at measured silence
   (20 ms RMS < −60 dB, search ±0.3 s), with 5–10 ms fades. Don't put a hard sidechain compressor on the SFX (it pumps);
   lower the SFX level instead. Final check: whisper MEDIUM on the final MP4, diff against vo_lines.txt word by word.
8. Loudness: render_aip.sh normalises in one pass and can land at −18 LUFS; measure (ebur128) and, if off by > 1 LU,
   remix with a two-pass loudnorm (see projects/aip_r30_timmarketingai/tools/remix_audio.sh).
9. SFX must be clearly audible (client 2026-11-21: "kasih sound effect biar gak suara VO aja"): whoosh on every transition,
   pops/clicks on UI and caption-in, typing/blips/ticks where things happen, soft risers on reveals; about −8 to −10 dB under VO
   peaks, no sidechain pumping, no hit on a word onset. Never ship a reel that sounds like VO + music only.
