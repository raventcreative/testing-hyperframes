// node render.cjs [stills|video|all]  -> out/stills/*.png + out/*.mp4 (slides 1-2, 6 s @30fps)
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execSync}=require('child_process');
const D=__dirname, mode=process.argv[2]||'all', FPS=30, DUR=8, NAME='CAROUSEL_AIP_7AGENT_SLIDE_';
(async()=>{const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+D+'/index.html');await p.evaluate(()=>document.fonts.ready);await p.evaluate(async(T)=>{reflow();setT(T);await ready()},DUR-0.1);
 const ids=await p.$$eval('.slide',e=>e.map(x=>x.id));
 console.log(await p.$$eval('.slide',ss=>ss.map(s=>s.id+':'+Math.round(s.querySelector('.content').getBoundingClientRect().bottom-s.getBoundingClientRect().top)).join(' ')));
 if(mode!=='video') for(const id of ids){const n=id.slice(1).padStart(2,'0');await (await p.$('#'+id)).screenshot({path:`${D}/out/stills/${NAME}${n}.png`});}
 if(mode!=='stills') for(const id of ids){const n=id.slice(1).padStart(2,'0'),tmp=`${D}/out/_f${n}`;fs.rmSync(tmp,{recursive:true,force:true});fs.mkdirSync(tmp);
  const el=await p.$('#'+id);
  for(let f=0;f<FPS*DUR;f++){await p.evaluate(async t=>{setT(t);await ready()},f/FPS);await el.screenshot({path:`${tmp}/${String(f).padStart(4,'0')}.png`});}
  execSync(`ffmpeg -v error -y -framerate ${FPS} -i ${tmp}/%04d.png -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -movflags +faststart ${D}/out/${NAME}${n}.mp4`);
  fs.rmSync(tmp,{recursive:true,force:true});console.log('video',n);}
 await b.close();})();
