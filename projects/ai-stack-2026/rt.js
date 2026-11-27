const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'carousel.html')); await p.evaluate(() => document.fonts.ready);
  await p.addStyleTag({ content: 'html,body{background:transparent!important}.slide{background:none!important}' });
  await (await p.$('.slide')).screenshot({ path: path.join(__dirname, 'out', 'slide-01-transparent.png'), omitBackground: true });
  await b.close();
})();
