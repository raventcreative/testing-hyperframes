# The voxel 3D + mascot reel (client-approved format, Nov 2026)

Reference builds: `projects/aip_voxel_uji` (18 s test, white) and `projects/aip_r26_hookmatrix` (57.8 s, navy).

## Layers (index.html, 1080×1920, 30 fps)
1. `#stage` canvas `#vx` — Three.js voxel worlds (`vendor/vx.js` scenes + `vendor/vxlib.js` builders). Deterministic:
   `render(t)` is a pure function of time, driven by HyperFrames' `hf-seek` event; async build exposed via
   `window.__hf.buildReady.vx`. importmap → `vendor/three/three.module.min.js` (r170) + addons (SVGLoader,
   RoomEnvironment, BufferGeometryUtils).
2. `#host` canvas `#ms` — the client's mascot (`assets/mascot3d/mascot_biz_rigged.glb` + `vendor/mascot3d.js` R-series
   runtime + `vendor/mascot_host.js`): lip sync from VO_PHONES/VO_ENV (tools/vo_data.py), acting from `intents`
   (welcome/present/explain/emphasize/reveal/point/compare/cta/idle keyed to words). Glances disabled (eyes go blank).
   Layer UNDER the UI (`data-layout-ignore data-layout-allow-occlusion`). Never crop the mascot.
3. `#ui` — logo, title tabs, counter chips, captions, flashes (GSAP timeline `window.__timelines.main`, counters set on hf-seek).
4. `<audio>` vo (data-start 0.3) + sfx.wav (tools/sfx.py from the repo's `vo_safe` samples). Music bed added after render
   by render_aip.sh/remix_aip.sh (ducked, −14 LUFS).

## Structure
- 0 → ~6 s: **world first**, full screen, no mascot, captions at the bottom.
- Then a **zoom-out reveal** (the world is a floating diorama island) and the **mascot rises from the bottom**
  (view dy ease-out over 0.6 s). From here the action band sits above the mascot: `LIFT` view offset
  (`cam.setViewOffset`, ramps 0 → 230 px) + captions move to y≈1000.
- Worlds = floating islands in a sky (navy: star sprites, cyan rims; white: pale sky + voxel clouds). Move between
  worlds with camera flights (island hop), match cuts (dive into an object, white flash, pull out of the same object).
- Our own voxel characters/props only (job seeker with glasses, 7 role-coloured robots, HR, slot machine, dominoes,
  turntable…). Never the reference's characters, palette or UI.

## Transition catalogue (use a DIFFERENT one per beat)
portal zoom-through · zoom-out reveal · island hop flight · elevator doors (layers slide apart) · vertical whip tilt ·
jackpot flash + cube burst · iris · 180° orbit · turntable spin-blur · button shockwave ring · dive-into-object match cut ·
dolly zoom (vertigo) · cube grid wipe (used once; prefer 3D transitions).
Motion life: squash-and-stretch landings + dust, confetti, crumbling voxel numbers, glow sprites on emissive parts,
counters that tick, keyword highlights lighting up, cards printing/flying (keep them away from text).

## Camera keys
`keys(t, [[time,[px,py,pz,tx,ty,tz,fov],ease]...])`, eases lin/io/out/in/sine/back/expo. Shots `{w, a, b, cam, ws?, abs?}`
(`ws` = worlds visible together, `abs` = absolute coords for flights). Keep the camera inside islands' bounds and away
from tall objects (a camera behind a building shows a giant white roof). Use smooth eases for close-ups; snap (expo)
only for whips/portals.

## Timing
Words from the ElevenLabs alignment (tools/words.py, VO offset +0.3 s). Elements must be on screen when the VO names
them; transitions finish before the next line starts. Robots/counters land on the counted word.
