// node render.js <outDir> <fps> <subframes> ; resumable: skips frames already on disk
const { chromium } = require('playwright'); const fs=require('fs'); const {spawn}=require('child_process');
const [,, out, fpsS, subS] = process.argv; const fps=+fpsS, sub=+subS, N=Math.round(14.5*fps);
fs.mkdirSync(out,{recursive:true});
let start=0; while(start<N && fs.existsSync(`${out}/f_${String(start).padStart(4,'0')}.png`)) start++;
(async()=>{
 const args=['--ignore-gpu-blocklist','--enable-unsafe-swiftshader'].concat(process.env.GPU?['--use-angle=d3d11','--enable-gpu']:[]);
 const b=await chromium.launch({args}); const p=await b.newPage({viewport:{width:1440,height:1152}}); p.setDefaultTimeout(0);
 await p.goto('http://127.0.0.1:8765/film.html'); await p.evaluate(()=>window.ready);
 const ff=spawn('ffmpeg',['-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s','1440x1152','-framerate',String(fps),'-i','-','-vf','vflip','-start_number',String(start),`${out}/f_%04d.png`],{stdio:['pipe','inherit','inherit']});
 const T0=Date.now();
 for(let i=start;i<N;i++){
  await p.evaluate(([t,s])=>window.seek(t,s),[i/fps,sub]);
  const buf=Buffer.from(await p.evaluate(()=>window.grab()),'base64');
  if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
  if(i%20===0){const el=(Date.now()-T0)/1000, per=el/(i-start+1); console.log(`frame ${i}/${N}  ${per.toFixed(1)}s/frame  eta ${((N-i)*per/60).toFixed(1)}min`);}
 }
 ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('DONE');
})();
