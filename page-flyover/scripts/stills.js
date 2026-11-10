const { chromium } = require('playwright'); const fs=require('fs'); const {execFileSync}=require('child_process');
const [,, outDir, times, sub] = process.argv;
(async()=>{
 const b=await chromium.launch({args:['--ignore-gpu-blocklist','--enable-unsafe-swiftshader']});
 const p=await b.newPage({viewport:{width:1440,height:1152},deviceScaleFactor:1}); p.setDefaultTimeout(0);
 p.on('pageerror',e=>console.log('[err]',e.message));
 await p.goto('http://127.0.0.1:8765/film.html'); console.log(JSON.stringify(await p.evaluate(()=>window.ready)));
 for(const t of times.split(',').map(Number)){
  const t0=Date.now(); const info=await p.evaluate(([t,s])=>window.seek(t,s),[t,+sub]); const t1=Date.now();
  const raw=Buffer.from(await p.evaluate(()=>window.grab()),'base64'); const f=`${outDir}/still_${t.toFixed(2)}`;
  fs.writeFileSync(f+'.rgba',raw); execFileSync('ffmpeg',['-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s','1440x1152','-i',f+'.rgba','-vf','vflip','-frames:v','1',f+'.png']); fs.unlinkSync(f+'.rgba');
  console.log(t, JSON.stringify(info), `seek ${t1-t0}ms total ${Date.now()-t0}ms`);
 }
 await b.close();})();
