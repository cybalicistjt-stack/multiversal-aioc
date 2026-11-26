from pathlib import Path
import re,json
w=Path('work/mvac12');s=Path('deliverables/Multiversal_MVAC11_Optional_Pack_Activation.html').read_text()
def change(i,fn):
 global s
 ms=list(re.finditer(r'<script[^>]*>([\s\S]*?)</script>',s));m=ms[i];old=m.group(1);new=fn(old);assert new!=old,i;s=s[:m.start(1)]+new+s[m.end(1):]
def native(t):
 # Benchmark and author render follow the native rectangle without a decorative inset.
 t=t.replace('const frame=frameFor(doc),padding=Math.min(34,Math.min(w,h)*.08),base=',"const frame=frameFor(doc),padding=['regional','urban'].includes(doc.mode)?0:Math.min(34,Math.min(w,h)*.08),base=")
 # Keep model-space vertices; clip at presentation, including export.
 t=t.replace('    let relief = false;','    ctx.save();ctx.beginPath();ctx.rect(paper.x,paper.y,frameW,frameH);ctx.clip();\n    let relief = false;')
 t=t.replace('    if (!output && window.MV_VTT06_RENDER) {','    ctx.restore(); // presentation crop; source geometry is never trimmed\n    if (!output && window.MV_VTT06_RENDER) {')
 return t
def shell(t):
 t=t.replace("let lastTransform=null;","let lastTransform=null,renderWidth=800,renderHeight=520;")
 t=t.replace("const d=viewDoc();await", "const d=viewDoc(),extent=N.frame(d);renderWidth=800;renderHeight=520;if(['regional','urban'].includes(d.mode)){renderHeight=Math.round(800*extent.height/extent.width);if(renderHeight>1000){renderWidth=Math.round(1000*extent.width/extent.height);renderHeight=1000;}}await")
 t=t.replace("audience:'player',width:800,height:520","audience:'player',width:renderWidth,height:renderHeight")
 t=t.replace('N.render(d,{width:800,height:520,zoom:1,level:floor})','N.render(d,{width:renderWidth,height:renderHeight,zoom:1,level:floor})')
 t=t.replace('Math.min(w/800,h/520)','Math.min(w/renderWidth,h/renderHeight)').replace('(w-800*s)/2','(w-renderWidth*s)/2').replace('(h-520*s)/2','(h-renderHeight*s)/2')
 t=t.replace('Math.min((800-68)/frame.width,(520-68)/frame.height)',"Math.min((renderWidth-(['regional','urban'].includes(viewDoc().mode)?0:68))/frame.width,(renderHeight-(['regional','urban'].includes(viewDoc().mode)?0:68))/frame.height)")
 t=t.replace('(800-frame.width*base)/2','(renderWidth-frame.width*base)/2').replace('(520-frame.height*base)/2','(renderHeight-frame.height*base)/2')
 t=t.replace('800*v.s,520*v.s','renderWidth*v.s,renderHeight*v.s').replace('(old.w-800*old.s*ratio)/2','(old.w-renderWidth*old.s*ratio)/2').replace('(old.h-520*old.s*ratio)/2','(old.h-renderHeight*old.s*ratio)/2')
 start=t.index('for(const r of layer.items.filter(r=>added.has(r.id)))');end=t.index('delete layer.addedIds;',start)
 t=t[:start]+t[end:] # off-map decorative instances are also retained
 t=t.replace("if(tool==='asset'&&armedAsset)","if(tool==='draw'&&pathDraft){const v=transform(),a=artPoint({x:0,y:0}),b=artPoint({x:1,y:1});pathAdd({x:((e.clientX-r.left-v.left)/v.s-a.x)/(b.x-a.x),y:((e.clientY-r.top-v.top)/v.s-a.y)/(b.y-a.y)});}else if(tool==='asset'&&armedAsset)")
 t=t.replace("if(e.key==='Escape'){armedAsset=null;", "if(e.key==='Enter'&&pathDraft){e.preventDefault();pathFinish();return;}if(e.key==='Escape'){pathCancel();armedAsset=null;")
 t=t.replace("function canLeave(){", "function canLeave(){") # keep existing draft guard
 # Cancel pending path when leaving a map/context, without changing committed source.
 t=t.replace("function setMode(next){", "function setMode(next){pathCancel();")
 t=t.replace("function draw(){", "function draw(){")
 marker="lastTransform=v;$('zoom-label')"
 preview="if(pathDraft){const pts=pathDraft.points.map(screenPoint);ctx.strokeStyle='#f7c974';ctx.fillStyle='#f7c974';ctx.lineWidth=2;ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(p.x,p.y):ctx.moveTo(p.x,p.y));ctx.stroke();for(const p of pts){ctx.beginPath();ctx.arc(p.x,p.y,4,0,Math.PI*2);ctx.fill();}}"
 t=t.replace(marker,preview+marker)
 # Initial render may happen before added declarations, so use var initialization before existing boot.
 addition=(w/'edge-author.js').read_text().replace('let pathDraft=null,pathSequence=0;','var pathDraft=null,pathSequence=0;')
 pos=t.index('new ResizeObserver(draw).observe(stage);');t=t[:pos]+addition+'\n'+t[pos:]
 # scene switch must discard uncommitted geometry
 t=t.replace("function changeScene(", "function changeScene(")
 t=t.replace("$('scene').onchange=()=>changeScene", "$('scene').onchange=()=>{pathCancel();changeScene").replace("Number($('scene').value));", "Number($('scene').value));};")
 return t

def examples(t):
 data=json.loads(t);d=data['fixtures'][1]['document'];count=0
 for f in d['draft']['features']:
  if f['kind']!='street':continue
  ps=f['geometry']['points']
  for i in [0,-1]:
   p=ps[i]
   if p['x']<.5:p['x']=-.5;count+=1
   elif p['x']>11.5:p['x']=12.5;count+=1
   if p['y']<.5:p['y']=-.5;count+=1
 d['revision']+=1;d['draft']['boundaryRemasterVersion']='MVAC12';assert count==9,count
 return json.dumps(data,separators=(',',':'))
change(0,examples)

old_native=list(re.finditer(r'<script[^>]*>([\s\S]*?)</script>',s))[2].group(1)
change(2,native);change(3,shell)
new_native=list(re.finditer(r'<script[^>]*>([\s\S]*?)</script>',s))[2].group(1)
def relocate(t):
 d=json.loads(t)
 for b in d['manifest']['blobs']:
  l=b['locator'];uri=old_native[l['start']:l['start']+l['length']];assert uri.startswith('data:image/png;base64,')
  at=new_native.find(uri);assert at>=0 and new_native.find(uri,at+1)<0;l['start']=at
 return json.dumps(d,separators=(',',':'))
change(6,relocate)
s=s.replace('<button id="undo"','<button id="extend-road">Extend selected road</button><button id="draw-road" title="Click road vertices, including outside the map">Draw road</button><button id="draw-land">Draw landscape</button><button id="draw-finish">Finish drawing</button><button id="draw-cancel">Cancel drawing</button><button id="undo"',1)
s=s.replace('STUDIO · MVAC-11','STUDIO · MVAC-12').replace('MVAC-11 Map & Scene Studio','MVAC-12 Map & Scene Studio')
# Storage changes installed from the maintained source modules.
code='(()=>{'+Path('work/mvac07/package/intake-core.mjs').read_text().replace('export ','')+'\n'+Path('work/mvac07/package/browser-bridge.mjs').read_text().replace('export ','')+'\n'+'\n'.join((w/'package'/n).read_text().replace('export ','') if n in ['pack-core.mjs','storage-layout.mjs','indexeddb-storage.mjs'] else (Path('work/mvac11/package')/n).read_text().replace('export ','') for n in ['pack-core.mjs','pack-validator.mjs','storage-layout.mjs','indexeddb-storage.mjs'])+'\n'+Path('work/mvac11/browser-ui.js').read_text().replace("(async()=>{try{await storage.open();",(w/'storage-ui.js').read_text()+"\n(async()=>{try{await storage.open();")+'})();'
code=code.replace("$('packs-demo1-data').textContent","JSON.stringify(JSON.parse($('packs-data').textContent).v1)").replace("$('packs-demo2-data').textContent","JSON.stringify(JSON.parse($('packs-data').textContent).v2)")
(w/'pack-runtime.js').write_text(code)
change(17,lambda _:code)
change(13,lambda t:t.replace('const im=await loadImage(a.src);if(im.naturalWidth',"const sourceTicket=ticket,im=await loadImage(a.src);if(sourceTicket!==ticket)throw Error('Source preview cancelled.');if(im.naturalWidth").replace('window.MVAC09_RENDITIONS={','window.MVAC09_RENDITIONS={'+(w/'cache-hook.js').read_text()))
s=s.replace('<script id="source-data"',(w/'storage-ui.html').read_text()+'<script id="source-data"').replace('<button id="packs-open">','<button id="storage-open">Storage & caches</button><button id="packs-open">')
Path('deliverables/Multiversal_MVAC12_Storage_and_Map_Continuity.html').write_text(s)
print({'bytes':len(s.encode())})
