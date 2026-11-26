/* Art-only Map Forge v1 adapter. No native geometry or gameplay inference. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.MVForgeImportCore=api;})(typeof window==='object'?window:globalThis,()=>{'use strict';
const FORMAT='multiversal:mapmaker:forge-art:v1';
const fail=m=>{throw Error(m);};
const finite=(n,min,max)=>typeof n==='number'&&Number.isFinite(n)&&n>=min&&n<=max;
const integer=(n,min,max)=>finite(n,min,max)&&Number.isInteger(n);
function fingerprint(s){let h=2166136261;for(let i=0;i<s.length;i++)h=Math.imul(h^s.charCodeAt(i),16777619);return(h>>>0).toString(16).padStart(8,'0');}
function png(src,w,h){
 if(typeof src!=='string'||src.length>600000||!/^data:image\/png;base64,[A-Za-z0-9+/]+={0,2}$/.test(src))fail('Only embedded PNG tiles up to 600 KB are supported.');
 let bytes;try{bytes=atob(src.slice(22));}catch{fail('A PNG tile has invalid base64.');}
 if(bytes.length<33||[137,80,78,71,13,10,26,10].some((v,i)=>bytes.charCodeAt(i)!==v)||bytes.slice(12,16)!=='IHDR')fail('A tile does not have a PNG header.');
 const u32=i=>(bytes.charCodeAt(i)*16777216+bytes.charCodeAt(i+1)*65536+bytes.charCodeAt(i+2)*256+bytes.charCodeAt(i+3));
 if(u32(16)!==w||u32(20)!==h)fail('PNG dimensions do not match the saved tile.');
}
function inspect(project,filename='legacy.mapforge.json'){
 if(!project||project.format!=='multiversal-map-forge'||project.version!==1||!project.map||!Array.isArray(project.tiles))fail('Choose a Multiversal Map Forge version 1 project.');
 const m=project.map;
 if(!integer(m.width,4,200)||!integer(m.height,4,200)||!integer(m.cellSize,16,256)||!finite(project.baseTileSize,1,4096))fail('Invalid legacy map or base-tile dimensions.');
 if(!Array.isArray(m.layers)||m.layers.length<1||m.layers.length>16)fail('Legacy layer count must be 1–16.');
 if(project.tiles.length<1||project.tiles.length>64)fail('Import supports 1–64 tiles. Split larger projects into smaller art packs.');
 const sourceFingerprint=fingerprint(JSON.stringify(project)),tiles=[],byId=new Map();let pixelCount=0,encoded=0;
 for(const [i,t]of project.tiles.entries()){
  if(!t||typeof t.id!=='string'||!t.id||t.id.length>200||byId.has(t.id)||typeof t.name!=='string'||t.name.length>200||!integer(t.width,1,320)||!integer(t.height,1,320))fail('Tile IDs must be unique, with image dimensions up to 320 × 320. Use the atlas extractor for larger tiles.');
  png(t.image,t.width,t.height);pixelCount+=t.width*t.height;encoded+=t.image.length;
  if(pixelCount>4000000||encoded>8000000)fail('This artwork exceeds the decoded-pixel or embedded-image budget.');
  const tile={id:'forge_legacy_'+fingerprint(t.image)+'_'+fingerprint(t.id)+'_'+i,label:t.name.slice(0,120)||'Legacy tile '+(i+1),width:t.width,height:t.height,pack:'forge_import',category:'imported',sizeHint:.44,src:t.image,legacyTileId:t.id};
  tiles.push(tile);byId.set(t.id,tile);
 }
 const layers=[],ids=new Set();let total=0;
 for(const layer of m.layers){
  if(!layer||typeof layer.id!=='string'||!layer.id||layer.id.length>120||ids.has(layer.id)||typeof layer.name!=='string'||layer.name.length>120||typeof layer.visible!=='boolean'||!Array.isArray(layer.placements))fail('Invalid or duplicate legacy layer.');
  ids.add(layer.id);const cells=new Set(),placements=[];
  for(const entry of layer.placements){
   if(!Array.isArray(entry)||entry.length!==2||typeof entry[0]!=='string'||!/^\d{1,3},\d{1,3}$/.test(entry[0])||cells.has(entry[0]))fail('Invalid or duplicate placement cell.');
   const [x,y]=entry[0].split(',').map(Number),p=entry[1];
   if(x>=m.width||y>=m.height||!p||!byId.has(p.tileId)||!finite(p.scale,.1,8)||!integer(p.order,0,Number.MAX_SAFE_INTEGER))fail('A placement is outside the map or references an invalid tile, scale or order.');
   cells.add(entry[0]);placements.push({cellX:x,cellY:y,asset:byId.get(p.tileId).id,scale:p.scale,order:p.order});
   if(++total>20000)fail('This legacy project exceeds 20,000 placements.');
  }
  placements.sort((a,b)=>a.order-b.order);layers.push({id:layer.id,name:layer.name,visible:layer.visible,placements});
 }
 return{sourceFingerprint,filename:String(filename).split(/[\\/]/).pop().slice(0,160),width:m.width,height:m.height,cellSize:m.cellSize,baseTileSize:project.baseTileSize,tiles,layers,total,visible:layers.filter(l=>l.visible).reduce((n,l)=>n+l.placements.length,0),warnings:['Art only: legacy grid cells do not become native rooms, doors, terrain or walls.','Legacy background color and grid are preview context only. Hidden layers stay hidden in the decorative overlay.','Source fingerprint detects accidental changes; it does not authenticate licenses or file origin.']};
}
function transformItems(review,t,instance){
 if(!t||!finite(t.unitsPerCell,.01,20)||!finite(t.originX,-10000,10000)||!finite(t.originY,-10000,10000)||typeof t.level!=='string'||!t.level||t.level.length>110)fail('Choose a valid native origin, level and map units per legacy cell.');
 const byId=new Map(review.tiles.map(a=>[a.id,a]));const items=[];
 for(const [li,l]of review.layers.entries())for(const [i,p]of l.placements.entries()){
  const tile=byId.get(p.asset),width=tile.width/review.baseTileSize*p.scale*t.unitsPerCell;
  if(!finite(width,.05,200))fail('A scaled sprite exceeds the native 0.05–200 map-unit artwork width. Adjust map units per cell.');
  items.push({id:'forge:'+instance+':'+li+':'+i,asset:p.asset,x:t.originX+(p.cellX+.5)*t.unitsPerCell,y:t.originY+(p.cellY+.5)*t.unitsPerCell,width,rotation:0,level:t.level,room:'',legacyLayer:instance+':'+li});
 }
 return items;
}
function compose(target,review,t,mode='art',existingArt=null,externalSprites=[]){
 if(!target?.draft||!['interior','urban','tactical','regional'].includes(target.mode)||!['art','assets'].includes(mode))fail('Open a native target map first.');
 if(target.mode==='regional'&&mode==='art')fail('Regional maps support assets-only import; choose a settlement/interior/tactical map for placed art.');
 if(target.mode==='interior'&&!target.draft.levels?.some(l=>l.levelId===t.level))fail('The selected native floor no longer exists.');
 if(target.mode!=='interior'&&t.level!=='level:0')fail('This map uses level:0 for decorative art.');
 const prior=target.draft.legacyForgeImport;
 if(prior&&prior.format!==FORMAT)fail('Existing legacy-art metadata is unsupported.');
 const sourceCount=prior?.sources?.length||0;if(sourceCount>=8)fail('This map already contains eight legacy art imports.');
 const instance=review.sourceFingerprint+'_'+sourceCount;
 const added=mode==='art'?transformItems(review,t,instance):[];
 const base=existingArt||target.draft.illustratedAssets;
 const items=[...(base?.items||[]).map(x=>({...x})),...added];if(items.length>350)fail('Native maps allow 350 art objects. Use assets-only import or a smaller legacy map.');
 const used=new Set(items.map(x=>x.asset));
 const sprites=new Map();for(const s of [...(prior?.sprites||[]),...externalSprites.filter(s=>used.has(s.id)),...review.tiles]){
  if(sprites.has(s.id)&&sprites.get(s.id).src!==s.src)fail('An asset ID collision was detected. No map was changed.');sprites.set(s.id,{...s});
 }
 if(sprites.size>64)fail('The portable native bundle supports at most 64 imported sprites.');
 const doc=structuredClone(target);
 doc.title=(target.title.slice(0,72)+(mode==='art'?' · Legacy art copy':' · Legacy asset copy')).slice(0,100);
 doc.draft.illustratedAssets={format:'multiversal:art-dressing:v1',mapId:doc.id,revision:doc.revision+1,items};
 doc.draft.legacyForgeImport={format:FORMAT,version:1,sprites:[...sprites.values()],layers:[...(prior?.layers||[]),...review.layers.map((l,i)=>({id:instance+':'+i,name:l.name,visible:mode==='art'?l.visible:false}))],sources:[...(prior?.sources||[]),{filename:review.filename,fingerprint:review.sourceFingerprint,fingerprintAlgorithm:'FNV-1a-32; accidental-change detection only',mapCells:{width:review.width,height:review.height},cellSize:review.cellSize,baseTileSize:review.baseTileSize,mode,placementCount:added.length,transform:{...t}}]};
 if(JSON.stringify(doc).length>9000000)fail('This native map/art bundle exceeds the 9 MB safety budget.');
 return doc;
}
function validate(doc){
 const b=doc?.draft?.legacyForgeImport;if(b===undefined)return null;
 try{
  if(!b||b.format!==FORMAT||b.version!==1||!Array.isArray(b.sprites)||b.sprites.length>64||!Array.isArray(b.layers)||b.layers.length>128||!Array.isArray(b.sources)||!b.sources.length||b.sources.length>8)fail('Invalid portable legacy-art bundle.');
  const ids=new Set(),layers=new Set();let size=0;
  for(const s of b.sprites){if(!s||typeof s.id!=='string'||!/^forge_[a-zA-Z0-9_]{3,80}$/.test(s.id)||ids.has(s.id)||typeof s.label!=='string'||s.label.length>120||!integer(s.width,1,320)||!integer(s.height,1,320))fail('Invalid bundled sprite.');png(s.src,s.width,s.height);ids.add(s.id);size+=s.src.length;}
  if(size>8000000)fail('Embedded artwork exceeds its image budget.');
  for(const l of b.layers){if(!l||typeof l.id!=='string'||!l.id||l.id.length>160||layers.has(l.id)||typeof l.name!=='string'||l.name.length>120||typeof l.visible!=='boolean')fail('Invalid bundled layer.');layers.add(l.id);}
  const a=doc.draft.illustratedAssets;
  if(!a||a.format!=='multiversal:art-dressing:v1'||a.mapId!==doc.id||!Array.isArray(a.items)||a.items.length>350)fail('Legacy artwork is not bound to this native map.');
  const names=new Set();for(const i of a.items){if(!i||typeof i.id!=='string'||!i.id||i.id.length>110||names.has(i.id)||typeof i.asset!=='string'||!finite(i.x,-10000000,10000000)||!finite(i.y,-10000000,10000000)||!finite(i.width,.05,200)||!finite(i.rotation,-3600,3600)||typeof i.level!=='string'||i.level.length>110)fail('Invalid native art placement.');names.add(i.id);if(i.legacyLayer!==undefined&&(!layers.has(i.legacyLayer)||!ids.has(i.asset)))fail('Legacy artwork references a missing layer or sprite.');}
  for(const s of b.sources){if(!s||typeof s.filename!=='string'||s.filename.length>160||!['art','assets'].includes(s.mode)||typeof s.fingerprint!=='string'||!/^[a-f0-9]{8}$/.test(s.fingerprint)||!integer(s.placementCount,0,350))fail('Invalid import provenance.');}
  if(JSON.stringify(doc).length>9000000)fail('Native art bundle is too large.');
  return null;
 }catch(e){return e.message;}
}
return Object.freeze({format:FORMAT,inspect,compose,transformItems,validate,fingerprint});
});
