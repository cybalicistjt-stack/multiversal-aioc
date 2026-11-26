from pathlib import Path
import re,json
w=Path('work/mvac13');s=Path('deliverables/Multiversal_MVAC12_Storage_and_Map_Continuity.html').read_text();original=s
def scripts():return list(re.finditer(r'<script[^>]*>([\s\S]*?)</script>',s))
def change(i,fn):
 global s
 m=scripts()[i];old=m.group(1);new=fn(old);assert old!=new,i;s=s[:m.start(1)]+new+s[m.end(1):]
old_native=scripts()[2].group(1)
change(2,lambda t:t.replace('serialize:serializeDraft}',"serialize:serializeDraft,decode:value=>decodeMapFile(value,doc=>!documentError(doc)),copy:(doc,id,title)=>newMapDocument(doc.mode,title,doc.draft,'copy',id)}"))
new_native=scripts()[2].group(1)
def relocate(t):
 d=json.loads(t)
 for b in d['manifest']['blobs']:
  l=b['locator'];uri=old_native[l['start']:l['start']+l['length']];assert uri.startswith('data:image/png;base64,');l['start']=new_native.index(uri)
 return json.dumps(d,separators=(',',':'))
change(6,relocate)
change(3,lambda t:t.replace("DATA.fixtures[index].id","(DATA.fixtures[index]?.id||'Recovered')").replace('new ResizeObserver(draw).observe(stage);',(w/'author-hook.js').read_text()+'\nnew ResizeObserver(draw).observe(stage);'))
service=(w/'service.js').read_text();prior=Path('work/mvac11/browser-ui.js').read_text();prior=prior.replace("const refs=()=>window.MVAC11_REFERENCES?.()||[]", "const refs=()=>[...(window.MVAC11_REFERENCES?.()||[]),...durableRecoveryRefs]")
prior=prior.replace("(async()=>{try{await storage.open();ready=true;await manager.restore();",service+"\n(async()=>{try{await storage.open();durableRecoveryRefs=[...new Set((await storage.restored()).flatMap(r=>(r.document.draft.illustratedAssets?.items||[]).map(a=>a.asset)))];ready=true;await manager.restore();")
prior=prior.replace("(async()=>{try{await storage.open();",Path('work/mvac12/storage-ui.js').read_text()+"\n(async()=>{try{await storage.open();")
code='(()=>{'+Path('work/mvac07/package/intake-core.mjs').read_text().replace('export ','')+'\n'+Path('work/mvac07/package/browser-bridge.mjs').read_text().replace('export ','')+'\n'+'\n'.join((w/'package'/n).read_text().replace('export ','')for n in ['pack-core.mjs','pack-validator.mjs','storage-layout.mjs','indexeddb-storage.mjs'])+'\n'+prior+'})();'
code=code.replace("$('packs-demo1-data').textContent","JSON.stringify(JSON.parse($('packs-data').textContent).v1)").replace("$('packs-demo2-data').textContent","JSON.stringify(JSON.parse($('packs-data').textContent).v2)")
(w/'pack-runtime.js').write_text(code);change(17,lambda _:code)
core=(w/'package/recovery-core.mjs').read_text().replace('export ','');exports='window.MVAC13_RECOVERY_CORE={BACKUP_FORMAT,LINK_FORMAT,canonical,digest,inspectJSON,checkMedia,assetRefs,dependencyReport,createSave,inspectSave,restoreTransaction};'
additional=(w/'package/legacy-forge-core.cjs').read_text()+'\n(()=>{'+core+'\n'+exports+'})();\n'+(w/'recovery-ui.js').read_text()
s=s.replace('<button id="storage-open">','<button id="recovery-open">Save & restore</button><button id="storage-open">').replace('<script id="source-data"',(w/'recovery-ui.html').read_text()+'<script id="source-data"').replace('</body>','<script>'+additional+'</script></body>').replace('STUDIO · MVAC-12','STUDIO · MVAC-13').replace('MVAC-12 Map & Scene Studio','MVAC-13 Map & Scene Studio')
Path('deliverables/Multiversal_MVAC13_Portable_Save_and_Restore.html').write_text(s);print({'bytes':len(s.encode()),'growthBytes':len(s.encode())-len(original.encode())})
