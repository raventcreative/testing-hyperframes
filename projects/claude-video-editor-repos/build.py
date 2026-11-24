# Turn Claude into a video editor: 15 GitHub repos (AIpreneur navy remake, 1 slide 1080x1350).
# Every repo verified on GitHub 2026-11-24 (stars rounded, see production/repos.md). Icons: Lucide (ISC).
from pathlib import Path
D = Path(__file__).parent
def ic(b): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
I = {
 "dl": ic('<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/>'),
 "mic": ic('<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10a7 7 0 0 1-14 0"/><path d="M12 17v4"/>'),
 "cc": ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 10.5a2 2 0 1 0 0 3M17 10.5a2 2 0 1 0 0 3"/>'),
 "cut": ic('<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/>'),
 "bot": ic('<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01"/>'),
 "phone": ic('<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>'),
 "reel": ic('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M8 3l2 6M14 3l2 6"/><path d="m10 13 4 2.5-4 2.5z"/>'),
 "film": ic('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 3v18M17 3v18M3 8h4M3 16h4M17 8h4M17 16h4"/>'),
 "code": ic('<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>'),
 "box": ic('<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>'),
 "spark": ic('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>'),
 "curve": ic('<path d="M3 20C8 20 8 4 13 4s5 16 8 16"/>'),
 "studio": ic('<path d="M4 11h16v9H4z"/><path d="m4 11 2-6 14 2-1 4"/>'),
 "list": ic('<path d="M9 6h11M9 12h11M9 18h11"/><path d="m4 6 1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>'),
}
R = [
 ("yt-dlp", "yt-dlp/yt-dlp", "210k", "dl", "Download source videos"),
 ("Whisper", "openai/whisper", "113k", "mic", "Speech to text transcripts"),
 ("WhisperX", "m-bain/whisperX", "25.6k", "cc", "Word-level timestamps for captions"),
 ("FFmpeg Skill", "kajisho5/ffmpeg-skill", "10.3k", "cut", "42 FFmpeg editing tools for agents"),
 ("Video Use", "browser-use/video-use", "31.5k", "bot", "Edit videos with coding agents"),
 ("Claude Shorts", "AgriciDaniel/claude-shorts", "490", "phone", "Long video into short clips"),
 ("Herk Edit Kit", "nateherkai/herk-edit-kit", "3.1k", "reel", "Reels & Shorts, transcript-driven cuts"),
 ("PySceneDetect", "Breakthrough/PySceneDetect", "5.6k", "film", "Find every scene cut automatically"),
 ("Remotion Skills", "remotion-dev/skills", "7.9k", "code", "Official skills for video in React"),
 ("Three.js Skills", "CloudAI-X/threejs-skills", "4.4k", "box", "3D scenes and objects for videos"),
 ("Motion Skills", "iart-ai/motion-skills", "2.1k", "spark", "56 motion graphics skills"),
 ("Motion Graphics", "Barty-Bart/motion-graphics", "1.5k", "curve", "Motion design for Claude Code"),
 ("HyperFrames", "heygen-com/hyperframes", "89k", "studio", "HTML to video, edit with Claude"),
 ("OpenMontage", "OpenMontageInc/OpenMontage", "82.8k", "studio", "Full agentic video production"),
 ("Awesome Skills", "zhuyansen/awesome-claude-video-skills", "2.6k", "list", "Curated list of video skills"),
]
cards = "".join(f'''<div class="c"><div class="t"><em>{i+1:02d}</em><b>{n}</b><span class="ic">{I[k]}</span></div>
  <code>{r.replace('/', '/<wbr>')}</code><p>{d}</p><div class="st">★ {s}</div></div>''' for i, (n, r, s, k, d) in enumerate(R))
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude Video Editor Repos</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <h1>Turn <img class="cl" src="assets/claude3d.png" alt="Claude"> Claude into a<br><span>/video editor</span></h1>
  <p class="sub">15 open-source GitHub repos. Stars checked Nov 2026.</p>
  <div class="grid">{cards}</div>
  <div class="cta">Comment <b>VIDEO EDITOR</b> and I’ll send you all 15 links.</div>
</section></body></html>''')
print("ok", len(R))
