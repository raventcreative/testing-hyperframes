# R34 · 4 repo open-source: Claude jadi studio animasi — VO script (NAVY, CTA STUDIO)

Reference: `projects/aip_remake_batch8/refs/ref4.mp4` (38.4 s, EN, "20 free GitHub repos … motion studio, you only need four").
Target 35–42 s → final **42.0 s** (VO 41.0 s, one untouched ElevenLabs take, offset 0.3 s).

## VO lines (`production/vo_lines.txt`, voice Dakocan, eleven_v4, auto tags)
1. Video yang lagi kamu tonton ini dibikin pakai kode, bukan aplikasi edit.
2. Empat repo open-source ini bikin Claude jadi studio animasi.
3. Satu, HyperFrames, lebih dari delapan puluh tujuh ribu bintang.
4. Claude nulis HTML, HyperFrames merendernya jadi video.
5. Reel ini juga dibikin pakai HyperFrames.
6. Dua, GSAP skills, resmi dari GreenSock.
7. Agent kamu paham easing dan timeline, gerakannya jadi halus.
8. Tiga, Blender MCP.
9. Minta scene 3D, Claude yang nyusun di Blender.
10. Empat, Video Shotcraft.
11. Skill Claude Code dan Codex: promo produk sinematik dari screenshot kamu, tiap shot bisa diedit.
12. Komen STUDIO, daftar repo-nya aku kirim lewat DM.

## ATM — what we changed
- **Own hook**: the reference opens on "20 free repos"; ours opens on the honest proof — *this very video is made with code, not an
  editing app* (true: AIpreneur reels are built with HyperFrames, HTML + GSAP → MP4), and comes back to it on HyperFrames ("Reel ini juga…").
- **No "20"**: we only verified and list real repos, so the VO says *empat* and the DM lists 4 picks + 4 bonus = 8 verified repos.
  The reference's "I'll send you all 20" is not repeated.
- Own wording per repo (Indonesian, "kamu"), own facts from the READMEs (licence, star count of today, the Shotcraft README's
  "from your own screenshots"), own metaphors (crates, cursor cube, lanes, default cube, dolly camera). ≤3 consecutive words of the
  reference (different language). No earning promises.
- Visual world is ours: navy voxel islands, the client's 3D mascot host + the AIpreneur robot co-host. Nothing from the reference's
  orange UI, mascot or layout.

## Fact check (GitHub, 21 Nov 2026)
| repo | verified | facts used |
|---|---|---|
| heygen-com/hyperframes | ✓ README + search API | 87,516 stars ("87,5 rb" / "lebih dari delapan puluh tujuh ribu"), Apache-2.0, "Write HTML. Render video. Built for agents." |
| greensock/gsap-skills | ✓ | "Official AI skills for GSAP" (greensock org), MIT, 18.8k stars; gsap-core covers easing, gsap-timeline covers timelines |
| ahujasid/mcp-for-blender (formerly **blender-mcp**; github.com/ahujasid/blender-mcp lands on it) | ✓ | MIT, 35.2k stars; Blender add-on (socket server) + MCP server, the AI sends commands incl. Python that Blender runs; third-party, not by the Blender Foundation |
| Vincentwei1021/video-shotcraft | ✓ | Apache-2.0 (Remotion has its own licence), 21.8k stars; skill for Claude Code & Codex, cinematic editable product promos with Remotion, built from your own screenshots & copy, every shot is a React component you can change |
Bonus repos in the DM (verified the same day): remotion-dev/remotion, mrdoob/three.js, theatre-js/theatre, ManimCommunity/manim.
Nothing unverifiable was kept. "20 repos" claim dropped.

## Techniques applied (techniques only, client format wins)
1. **throughline-explainer — one through-line object**: a cyan #01ccf7 cube. It is the text cursor on the code monitor (hook), jumps out
   of the screen and knocks the clips off the "editing app" timeline, lands on crate 2, hops into crate 1 (portal), waits on the
   HyperFrames monitor as the render key and hops to the phone, rides the "DENGAN SKILL" lane on power3.out, falls off its end into the
   Blender island where it lands as the selected *default cube* (orange outline) and grows into the table, becomes the tally light of
   the dolly camera and the marker on the edited shot card. Never teleports between scenes.
2. **html-demo — scripted windows View(t) on 3D screens**: code editor typing (index.html) with a blinking cursor, README card with a
   ticking star counter, render progress → working state → ✓, phone playing a still of this reel, prompt card typing, GSAP easing board
   whose curve and dot share one function with the 3D cube, Shotcraft shot strip with a scripted cursor (arrives early, presses, rests).
3. **product-launch-film — shared elements / closed-form motion**: crate face → portal → next island; cube → table top (scale
   transform); shot card flies into the lens → CTA; all motion is pure easing/spring functions of t (small overshoot "back" only on pops).
4. **business-explainer-30s / prompt-motion "process fill"**: Blender beat — prompt → Claude builds the scene part by part (legs, lamp,
   plant, camera) until complete.
5. **Transitions all different**: cursor knock + zoom-out reveal · portal dive into crate 1 (+ white flash) · whip tilt to the sky (+ blur)
   · fall flight following the cube down to the next island (+ blur) · dive into the voxel camera's viewfinder → REC brackets · shot card
   flies into the lens (+ flash) → CTA.
Co-host: AIpreneur robot (R25 GLB + runtime) flies in beside the mascot at the zoom-out, presents/scans/types on a holo keyboard
(HTML, Blender prompt), points, cheers the CTA. Mascot glances disabled.

## VO QA
- Listen-check whisper small + medium on the take: only spelling differences ("Claude"→"Cloud/clot", "pakai"→"pake",
  "87.000", "4." for "Empat", hyphenation). Same known Claude spelling as R11–R30. No word misheard by both models → take kept.
- Final check on the final MP4 with whisper medium: see production/VO_CHECK.md.
