// node render.cjs <dir-with-feed.html+slides.js> -> <dir>/out/slide_XX.png (1080x1350)
const {chromium}=require('playwright'),path=require('path'),fs=require('fs');
(async()=>{const dir=path.resolve(process.argv[2]||'.');
 const n=(()=>{const w={};new Function('window',fs.readFileSync(path.join(dir,'slides.js'),'utf8'))(w);return w.SLIDES.length})();
 fs.mkdirSync(path.join(dir,'out'),{recursive:true});
 const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1350}});
 for(let i=0;i<n;i++){await p.goto('file://'+path.join(dir,'feed.html')+'?s='+i);await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:path.join(dir,'out',`slide_${String(i+1).padStart(2,'0')}.png`)});}
 await b.close();console.log('rendered',n);})();
