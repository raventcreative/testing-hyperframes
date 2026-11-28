// node tools/sfx_events.cjs <port>  -> production/sfx_events.json (the SFX cues the composition registers in window.SFX_EVENTS)
// serve the project first: python3 -m http.server <port> --bind 127.0.0.1
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto("http://127.0.0.1:" + process.argv[2] + "/index.html"); await p.waitForFunction(() => Array.isArray(window.SFX_EVENTS) && window.SFX_EVENTS.length > 0);
  const ev = await p.evaluate(() => window.SFX_EVENTS); fs.writeFileSync(path.resolve(__dirname, "../production/sfx_events.json"), JSON.stringify(ev)); console.log(ev.length, "events"); await b.close(); })();
