const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto('file://'+process.argv[2]); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
 await p.screenshot({path:process.argv[3]});
 await p.evaluate(()=>document.body.classList.add('nologo')); await p.screenshot({path:process.argv[4]}); await b.close();})();
