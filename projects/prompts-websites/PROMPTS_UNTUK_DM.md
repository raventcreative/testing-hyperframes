# 5 website prompts (kirim ini ke yang comment "PROMPTS")

Paste salah satu prompt ini ke Claude (atau AI lain). Hasilnya satu file `index.html` yang bisa langsung dibuka di browser.
Ganti teks di dalam [kurung siku] dengan brand lo.

---

## 01 · Nirmala: immersive art studio

You are an expert creative front-end developer. Build a single self-contained `index.html` (HTML, CSS and vanilla JS, no build step) for **[Nirmala], an immersive digital art studio**.

- Mood: dark charcoal background (#0d0f14), soft lilac and white light, cinematic and calm.
- Hero: full-screen canvas with ~6,000 glowing particles that slowly form the studio's initial letter, drift apart on scroll and re-form. Two words left and right of the shape: "IMAGINE" and "MANIFEST".
- Sections: 3 featured projects in large cards with hover tilt, a short manifesto in big thin type, a contact strip.
- Typography: one geometric sans for headings, one light sans for body. Generous spacing.
- Motion: smooth scroll-linked reveals (IntersectionObserver), no libraries. Respect `prefers-reduced-motion`.
- Fully responsive down to 375 px. Semantic HTML, accessible contrast, alt text.
Return only the complete file.

---

## 02 · Kopiloka: coffee brand

You are an expert creative front-end developer. Build a single self-contained `index.html` for **[Kopiloka], a modern Indonesian coffee brand** with takeaway cups and roasted beans.

- Mood: warm espresso brown (#2a1a12) to cream (#f4ece1), editorial and bold.
- Hero: huge headline "COFFEE FOR YOUR MORNING", a product composition built in CSS (cup + bean bag shapes) with a slow parallax float, two small tags ("SLOW ROAST", "HOUSE LATTE").
- Sections: menu grid of 4 drinks with price in Rupiah, a "freshly roasted" timeline (roast → pack → your cup), store locations, newsletter.
- Motion: sticky section titles, items rise in on scroll, a rotating circular "fresh every day" badge.
- Fully responsive, semantic, accessible. No external images: draw shapes with CSS/SVG.
Return only the complete file.

---

## 03 · Retrograde: creative agency

You are an expert creative front-end developer. Build a single self-contained `index.html` for **[Retrograde Studio], a creative agency that makes brands feel new**.

- Mood: near-black (#0a0a0c) with a warm red glow, film grain, old CRT screens floating in space.
- Hero: headline "WE MAKE THE PAST FEEL NEW", 6 tilted screen cards in a 3D CSS scene that drift slightly with the mouse.
- Sections: "Our cases" carousel (one big screen in focus, others blurred behind), "Meet the team" row of 5 portrait cards (use gradient placeholders), contact.
- Motion: CSS 3D transforms + perspective, smooth carousel with keyboard support, subtle scanline overlay.
- Fully responsive, semantic, accessible, respects reduced motion.
Return only the complete file.

---

## 04 · Teduh: health clinic

You are an expert creative front-end developer. Build a single self-contained `index.html` for **[Klinik Teduh], a modern family health clinic**.

- Mood: calm mint (#e8f3ee) and deep green (#1f5e4b), trustworthy, lots of white space.
- Hero: headline "Medicine that starts with understanding you", a soft animated line-art DNA strand in SVG, two buttons (Book a visit, Our services).
- Sections: "Everything under one roof" service cards (General check-up, Lab, Imaging, Specialists), key numbers (patients served, avg. wait time), doctor cards, a simple appointment request form with validation.
- Motion: gentle fade/slide reveals, number counters on scroll.
- Fully responsive, WCAG-friendly contrast, labelled form fields.
Return only the complete file.

---

## 05 · Neuron Labs: AI company

You are an expert creative front-end developer. Build a single self-contained `index.html` for **[Neuron Labs], an applied AI company**.

- Mood: deep navy (#06102b) with electric blue and a touch of magenta, futuristic but clean.
- Hero: headline "Engineering intelligence that evolves with you", a canvas point-cloud head silhouette that slowly rotates and reacts to the mouse.
- Sections: 3 product cards, "how it works" in 4 steps, logos row (use text placeholders), pricing table with 3 plans, footer.
- Motion: scroll-triggered reveals, glowing borders on hover, smooth anchor scrolling.
- Fully responsive, semantic, accessible, respects reduced motion. Vanilla JS only.
Return only the complete file.
