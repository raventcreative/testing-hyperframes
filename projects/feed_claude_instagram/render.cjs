const {chromium}=require('playwright'),path=require('path'),fs=require('fs');
(async()=>{const d=__dirname;fs.mkdirSync(d+'/out',{recursive:true});
 const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+d+'/feed.html');await p.evaluate(()=>document.fonts.ready);
 const ids=await p.$$eval('.slide',e=>e.map(x=>x.id));
 const over=await p.$$eval('.slide',ss=>ss.map(s=>{const r=s.getBoundingClientRect(),c=s.querySelector('.content').getBoundingClientRect();return s.id+' content bottom='+Math.round(c.bottom-r.top)}));
 console.log(over.join('\n'));
 for(const id of ids){await (await p.$('#'+id)).screenshot({path:`${d}/out/slide_${id.slice(1).padStart(2,'0')}.png`});}
 await b.close();})();
