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
