const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{
  const data=JSON.parse(fs.readFileSync(process.argv[2]));
  const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
  const p=await b.newPage({viewport:{width:1600,height:700}});
  await p.goto('file://'+__dirname+'/page.html');
  for(const n of ['inspire','haken']){
    const d=data[n];
    const view={w:1600,h:760,dpr:2,halfw:0.235,eye:[0.58,-0.9,0.45],target:[0.085,0,0.0]};
    const url=await p.evaluate(([d,v])=>window.render(d,v),[d,view]);
    fs.writeFileSync(__dirname+`/${n}.png`, Buffer.from(url.split(',')[1],'base64'));
    await p.evaluate(()=>{document.body.innerHTML='';});
    await p.addScriptTag({path:__dirname+'/three.min.js'}).catch(()=>{});
  }
  await b.close();
})();
