# 50 businesses that need AI automation (AIpreneur navy remake, 1080x1350). Render: node render.js | Check: node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
def ic(b): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
# Icons: Lucide-style strokes (ISC)
G = [
 ("Health & beauty", ic('<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>'),
  ["Dental clinics", "Aesthetic clinics", "Vet clinics", "Physiotherapy", "Optical stores",
   "Pharmacies", "Hair salons", "Barbershops", "Nail & lash studios"]),
 ("Food & beverage", ic('<path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z"/><path d="M6 2v2M10 2v2M14 2v2"/>'),
  ["Restaurants", "Coffee shops", "Bakeries", "Catering", "Cloud kitchens",
   "Frozen food brands", "Boba & juice bars", "Food franchises"]),
 ("Home & property", ic('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
  ["Property agents", "Kos & rental owners", "Interior designers", "Contractors",
   "Cleaning services", "Laundry services", "Pest control", "Furniture stores"]),
 ("Auto & travel", ic('<path d="M19 17h2v-4l-2.5-5H5.5L3 13v4h2"/><circle cx="7.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/><path d="M9.5 17.5h5M3 13h18"/>'),
  ["Car rentals", "Motorbike workshops", "Car detailing", "Used car dealers",
   "Driving schools", "Travel agents", "Umrah & hajj travel", "Villas & homestays"]),
 ("Fitness & education", ic('<path d="M22 10 12 5 2 10l10 5z"/><path d="M6 12v5c3 2.5 9 2.5 12 0v-5"/>'),
  ["Gyms", "Yoga & pilates studios", "Personal trainers", "Martial arts schools",
   "Tutoring centers", "Language courses", "Online course creators", "Daycares"]),
 ("Services & retail", ic('<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>'),
  ["Law firms", "Tax consultants", "Insurance agents", "Wedding organizers", "Photographers",
   "Event venues", "Printing shops", "Online shops", "Fashion boutiques"]),
]
assert sum(len(x) for *_, x in G) == 50
n = 0
def grp(name, icon, items):
    global n
    li = ""
    for t in items:
        n += 1; li += f'<li><em>{n:02d}</em>{t}</li>'
    return f'<div class="g"><h3><span class="ico">{icon}</span>{name}</h3><ul>{li}</ul></div>'
b = [grp(*g) for g in G]
cols = "".join(f'<div>{b[i]}{b[i+1]}</div>' for i in (0, 2, 4))
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>50 Businesses Need AI</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <div class="label">Save this list</div>
  <h1>50 businesses that need<br><span>AI automation</span> right now.</h1>
  <div class="cols">{cols}</div>
  <p class="foot">Pick one niche. Automate the repetitive work. Sell the hours you save.</p>
</section></body></html>''')
print("ok")
