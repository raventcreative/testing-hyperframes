# 100 ChatGPT photo-editing prompts (AIpreneur navy remake, 1 slide 1080x1350).
# Note: these are style prompts, not built-in ChatGPT commands (stated on the slide).
from pathlib import Path
D = Path(__file__).parent
G = [
 ("Portrait & retouch", ["Cinematic portrait", "DSLR look", "Professional retouch", "Natural skin", "Skin retouch", "Portrait enhance",
   "Facial enhance", "Sharp details", "Soft portrait", "Luxury portrait", "Editorial portrait", "Magazine cover", "Fashion editorial",
   "Street portrait", "Dramatic portrait", "Golden hour", "Sunset portrait", "Night portrait", "Neon portrait", "Rainy cinematic",
   "Winter portrait", "Summer portrait", "Autumn portrait", "Spring portrait", "Portrait polish"]),
 ("Mood & film look", ["Black and white", "Film look", "Vintage film", "90s film", "Retro portrait", "Analog look", "Warm film stock",
   "Cinematic color", "Teal and orange", "Matte finish", "High contrast", "Low-key portrait", "High-key portrait", "Soft glow",
   "Dreamy glow", "Ethereal portrait", "Moody tones", "Pastel tones", "Faded film", "Grainy film", "Bleach bypass", "Warm tones",
   "Cool tones", "Desaturated look", "Monochrome blue"]),
 ("Light & cleanup", ["Dramatic lighting", "Soft lighting", "Rim lighting", "Golden light", "Studio lighting", "Background blur",
   "Portrait bokeh", "Depth of field", "Lens blur", "Background replace", "Background cleanup", "Object removal", "Photo cleanup",
   "Old photo restore", "HD restore", "4K upscale", "Resolution boost", "Color restore", "Fix exposure", "Natural colors",
   "Color grading", "White balance fix", "Shadow recovery", "Highlight recovery", "Noise reduction"]),
 ("Business & social", ["Product photo", "Luxury product", "Product studio", "Flat lay", "Food photo", "Real estate photo",
   "Instagram portrait", "Instagram story", "Reel cover", "Profile picture", "Pro headshot", "Corporate portrait", "LinkedIn headshot",
   "Wedding portrait", "Prewedding film", "Festive portrait", "Batik portrait", "Kebaya portrait", "Ramadan portrait",
   "Travel portrait", "City portrait", "Beach portrait", "Mountain portrait", "Creative portrait", "Viral photoshoot"]),
]
assert all(len(x) == 25 for _, x in G)
n = 0; cols = ""
for name, items in G:
    li = ""
    for t in items:
        n += 1; li += f"<li><em>{n:02d}</em>{t}</li>"
    cols += f'<div class="g"><h3>{name}</h3><ol>{li}</ol></div>'
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>100 ChatGPT Photo Prompts</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <div class="hd"><div class="badge"><img src="assets/openai.png" alt="ChatGPT"></div>
    <div><h1>100 ChatGPT prompts<br>for <span>photo editing.</span></h1>
    <p class="how">Upload a photo, then type: <b>“Edit this photo: <span>cinematic portrait</span>”</b></p></div></div>
  <div class="cols">{cols}</div>
  <p class="ft">These are style prompts, not built-in commands. Swap in any prompt from the list.</p>
</section></body></html>''')
print("ok", n)
