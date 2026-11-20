// node render_closing.cjs <page.html> <out.png> [out.mp4]  — PNG = static final (Follow button), MP4 = 6 s @30fps
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execSync}=require('child_process');
(async()=>{const [page,png,mp4]=process.argv.slice(2);const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+page);await p.evaluate(()=>document.fonts.ready);
 await p.evaluate(()=>final());await (await p.$('#s')).screenshot({path:png});
 if(mp4){const tmp=mp4+'_frames';fs.rmSync(tmp,{recursive:true,force:true});fs.mkdirSync(tmp);const el=await p.$('#s');
  for(let f=0;f<180;f++){await p.evaluate(t=>setT(t),f/30);await el.screenshot({path:`${tmp}/${String(f).padStart(4,'0')}.png`});}
  execSync(`ffmpeg -v error -y -framerate 30 -i ${tmp}/%04d.png -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -movflags +faststart "${mp4}"`);fs.rmSync(tmp,{recursive:true,force:true});}
 await b.close();console.log('closing ->',png,mp4||'');})();
