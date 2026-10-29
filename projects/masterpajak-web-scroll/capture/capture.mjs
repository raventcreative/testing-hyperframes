// Capture masterpajak.ai: full-page screenshot (2x DPR) + layout map of sections, headings,
// buttons and feature-like blocks (bounding boxes in page px) for the scroll/feature choreography.
import { createRequire } from 'node:module';
import fs from 'node:fs';
const { chromium } = createRequire(import.meta.url)('playwright');
const URL = process.argv[2] || 'https://masterpajak.ai/';
const OUT = new globalThis.URL('../out/capture/', import.meta.url).pathname;
fs.mkdirSync(OUT, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
await page.goto(URL, { waitUntil: 'networkidle', timeout: 60000 });
// trigger lazy content / scroll-reveal animations
for (let y = 0; y < 30000; y += 600) { await page.evaluate((v) => window.scrollTo(0, v), y); await page.waitForTimeout(120); }
await page.evaluate(() => window.scrollTo(0, 0));
await page.waitForTimeout(800);
const layout = await page.evaluate(() => {
  const box = (el) => { const r = el.getBoundingClientRect(); return { x: r.x, y: r.y + scrollY, w: r.width, h: r.height }; };
  const txt = (el) => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 160);
  const pick = (sel) => [...document.querySelectorAll(sel)].filter((e) => e.offsetParent && e.getBoundingClientRect().width > 0).map((e) => ({ tag: e.tagName, text: txt(e), ...box(e) }));
  return {
    title: document.title, pageHeight: document.documentElement.scrollHeight, width: innerWidth,
    sections: pick('section, header, footer, main > div'),
    headings: pick('h1, h2, h3, h4'),
    buttons: pick('a, button').filter((b) => b.text && b.text.length < 40),
    images: pick('img, svg[class], video'),
  };
});
fs.writeFileSync(OUT + 'layout.json', JSON.stringify(layout, null, 2));
await page.screenshot({ path: OUT + 'fullpage.png', fullPage: true });
fs.writeFileSync(OUT + 'page.html', await page.content());
console.log('captured', layout.title, 'height', layout.pageHeight, 'sections', layout.sections.length, 'headings', layout.headings.length);
await browser.close();
