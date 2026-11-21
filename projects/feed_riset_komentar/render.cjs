// node render.cjs -> out/slide_XX.png for SLIDES (closing slide rendered separately with closing.py)
const {chromium}=require('playwright'),path=require('path'),fs=require('fs');
(async()=>{const dir=__dirname;const w={};new Function('window',fs.readFileSync(path.join(dir,'slides.js'),'utf8'))(w);const n=w.SLIDES.length;
 fs.mkdirSync(path.join(dir,'out'),{recursive:true});
 const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1350}});
 for(let i=0;i<n;i++){await p.goto('file://'+path.join(dir,'feed.html')+'?s='+i);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  const bad=await p.evaluate(()=>{const o=[];document.querySelectorAll('.content *').forEach(e=>{if(e.closest('.ph'))return;const r=e.getBoundingClientRect();if(r.width&&(r.left<95.5||r.right>984.5||r.bottom>1200.5||r.top<241.5))o.push(e.className+' '+[r.left,r.top,r.right,r.bottom].map(Math.round))});
   const m=document.querySelector('.media');if(m){const r=m.getBoundingClientRect();o.push('media h='+Math.round(r.height))}return o});
  console.log(i+1,bad.join(' | '));
  await p.screenshot({path:path.join(dir,'out',`slide_${String(i+1).padStart(2,'0')}.png`)});}
 await b.close();})();
