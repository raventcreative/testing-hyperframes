---
name: landing-flythrough-3d
description: 14.5-second cinematic 3D fly-through of a landing page (1440×1152, 60 fps) — the captured page lies flat on a studio floor, one continuous camera glide down the page while extracted cards/mockups/photos/chips/testimonials lift 20–40 px, rise to an overhead full-strip view, dive into the hero which becomes a floating title card (brand badge, Geist Medium headline + Instrument Serif italic tail, four floating logo tiles). WebGL2, time-seekable, DOF, soft shadows, 16-subframe motion blur, music hit at 9.97 s. Use for "/landing-flythrough-3d", "video fly-through landing page", "bikin video 3D dari website".
---
# /landing-flythrough-3d

Verbatim client brief (quality bar + exact timings): `references/brief.md`.

## Start protocol
1. Ask for the inputs: landing page URL, brand name, logo mark, closing headline (statement + short italic tail),
   optional 15 s music track. (For AIpreneur pages: their brand fonts/colours may replace Geist/Instrument Serif only if asked.)
2. Be upfront about rendering: this cloud Claude Code container can capture, build and render, but Chromium here runs
   WebGL in software (no GPU) → slower renders and `libx264` CPU encoding instead of GPU. If the user needs GPU speed,
   they run the render on their own machine with Claude Code. (A claude.ai chat without code execution can only give a
   live preview.)
3. Capture the page and show still previews at **0, 1.6, 2.5, 5, 6.5, 9.3 and 11 s**. Get approval before the final render.

## Capture (Playwright + Chromium)
- Viewport 1440 wide, full-page screenshot; **lock the layout first** (wait for fonts/images, disable lazy-load and
  animations, freeze heights: set every section's computed height inline) so section-height changes can't shift the sequence.
- Extract floating elements (cards, product mockups, photos, chips, testimonials, logo tiles) as transparent PNGs
  (element screenshots with `omitBackground`, page background hidden), and save `elements.json`:
  `{id, kind, x, y, w, h, lift}` in page pixels. The base page texture gets those areas left in place (elements float above them).

## Scene (one WebGL2 file, seek(t) pure)
- Page = plane with 24 px rounded corners on a studio floor (radial #f9fbfb centre → #f2f3f6 corners), soft shadows
  (shadow map or baked blurred contact shadow), mipmapped textures (generateMipmap + anisotropy).
- Floating elements = planes 20–40 px above the page, lifting slightly toward the camera as it passes (smoothstep by distance).
- Camera: ONE continuous move. 0–8.2 s glide hero → bottom with ease-in at start and ease-out only at the very end of the
  whole move; 7.75–9.25 rise to overhead (whole page as one strip); 9.25–9.47 hold; 9.47–9.97 dive into the hero;
  9.97–14.5 hero becomes a floating card → title card: brand badge, headline (Geist Medium) + italic tail (Instrument
  Serif), four floating logo tiles kept around the hero through the transition.
- Banned: cuts, crossfades, sudden speed changes, sideways roll, zoom reversals, glow, any text overlay before the title card.
- Depth of field: focus on the element under the camera's look-at (gather blur from a depth texture, CoC by depth).
- Motion blur: 16 subframes per output frame (accumulate in a float buffer or render 16 seeks and average).

## Audio
Music hit synced to 9.97 s (shift the track so its downbeat/drop lands there), subtle whooshes at 8.66 s and 9.80 s,
mix −14 LUFS. Credit any SFX source in production/asset_credits.json.

## QA + render
- Test a 30 fps preview first; check forward motion with optical flow (ffmpeg `minterpolate`/frame-diff or OpenCV
  Farneback: mean flow magnitude per frame must change smoothly, no sign flips = no zoom reversal).
- Final: 1440×1152, 60 fps, H.264 MP4 (`-c:v h264_nvenc` when a GPU exists, else `libx264 -crf 16 -preset slow`), yuv420p, +faststart.
- Look at frames around 7.75, 8.66, 9.25, 9.47, 9.80, 9.97 s one by one for pops.
