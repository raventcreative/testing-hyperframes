---
name: masterpajak-video
description: MasterPajak AI short videos (series mp10_01…mp10_31) — Indonesian tax/bookkeeping explainers for online sellers/UMKM with the MasterPajak design system (news-web pages, highlighter, robot presenter, hologram panels), ElevenLabs VO + SFX + bed, cover per video, zip delivery. Use for "/masterpajak-video", "bikin video master pajak", "MP <n>".
---
# /masterpajak-video
- Read `references/BRIEF_AGENTS*.md` (series rules + concepts) and the repo's `projects/mp10_series/VO_SCRIPTS.md`.
  Reference projects: `projects/mp10_01_berita` … `projects/mp10_31_kas` (each has `out/*_VO.mp4`, `thumbnail/COVER_MP*.png`).
- Compliance (strict): no DJP / bank / marketplace logos; label numbers "Ilustrasi data" and flows "Simulasi alur";
  never state tax rates, deadlines or guarantees; educational tone, not legal advice.
- VO via ElevenLabs (voice Dakocan, eleven_v4, auto tags); reword words whisper small+medium both mishear.
- Render: `aipreneur-reels-studio/scripts/render/render_vo2.sh <dir> <name>` (muxes VO + ducked SFX + bed via remux_vo.sh, −14 LUFS).
  SFX −2 dB if the client says they're loud.
- Deliver MP4 1080×1920 + cover, and a zip for batches (e.g. MasterPajakAI_16-30_VIDEO_LENGKAP.zip). Drive upload only when asked.
