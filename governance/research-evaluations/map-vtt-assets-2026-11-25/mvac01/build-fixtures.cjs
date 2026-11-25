const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('node:assert/strict');
const {ctx,native:n,renderModules}=require('../uvtt28-harness.cjs');const H=ctx.window.MMHT_ART_EXPORT;
const root=path.resolve('work/mvac01'),dir=path.join(root,'package');for(const x of ['native','roles','renders','cases'])fs.mkdirSync(path.join(dir,x),{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),canon=x=>JSON.stringify(x),write=(p,o)=>{const bytes=Buffer.from(JSON.stringify(o,null,2)+'\n');fs.writeFileSync(path.join(dir,p),bytes);return{path:p,bytes:bytes.length,sha256:sha(bytes)}};
const baseline=fs.readFileSync('deliverables/Multiversal_Consolidated_Playtest_UHT28_MME06_UVTT_Optional_Assets.html'),html=fs.readFileSync('work/map-28.html','utf8'),catalogRaw=html.match(/<script[^>]*id="mmht-curated-catalog"[^>]*>([\s\S]*?)<\/script>/)[1],catalog=JSON.parse(catalogRaw);
const choices=[['F01','regional',1,'Regional geography'],['F02','urban',1,'Settlement / districts'],['F03','interior',1,'Multi-floor architecture'],['F04','tactical',1,'Tactical encounter'],['F05','cave-map',1,'Cave / tunnel'],['F06','deck-ship',2,'Ship / docking decks'],['F07','topology-map',1,'Non-Euclidean topology']];
let checks=[];function check(name,fn){fn();checks.push({name,status:'passed',boundary:'controlled native component'});}
let fixtures=[],renders=[],roleRows=[];
const projectionPayload=doc=>{let d=structuredClone(doc);delete d.artExportCacheKey;return d;};
async function draw(doc,fixture,zoom,level,role,kind='artwork'){
 const original=canon(doc);let r,p;
 if(kind==='artwork'||kind==='repeat-artwork')r=n.render(doc,{width:800,height:520,zoom,level});
 else{p=H.prepare(doc,{audience:role,width:800,height:520,level,grid:'none',reviewed:role==='player',reviewedArt:false});await ctx.window.MMHT_MME02E2.preloadForBenchmark(p.doc);r=H.render(p);}
 const png=r.canvas.toBuffer('image/png'),pixels=Buffer.from(r.canvas.getContext('2d').getImageData(0,0,800,520).data),name=`renders/${fixture}-${kind}-${role}-${level.replaceAll(':','_')}-z${zoom}.png`;fs.writeFileSync(path.join(dir,name),png);
 const record={fixture,kind,role,level,zoom,width:800,height:520,path:name,pngBytes:png.length,pngSHA256:sha(png),rgbaSHA256:sha(pixels),drawDurationMs:Math.round(r.durationMs*1000)/1000,scope:kind==='artwork'?'GM-private artwork benchmark; fog off, gameplay/specialty overlays omitted':'Local prepared static export; unreviewed dressing removed; no authenticated role session'};
 check(`${fixture} ${role} ${level} zoom ${zoom} source unchanged`,()=>assert.equal(canon(doc),original));
 if(p)ctx.window.MMHT_MME02E2.releaseForExport(p.doc);r.canvas.width=r.canvas.height=1;return record;
}
(async()=>{
 for(const[id,type,index,purpose]of choices){
  const ex=catalog.examples.find(x=>x.type===type&&x.index===index);assert(ex);const d=structuredClone(catalog.sources[ex.source]),before=canon(d);
  check(id+' native validator',()=>assert.equal(n.documentError(d),null));const serial=n.serializeDraft(d),packet=JSON.parse(serial),decoded=n.decodeMapFile(packet,x=>!n.documentError(x));
  check(id+' native save/load stable draft and identity',()=>{assert(decoded);assert.equal(canon(decoded.draft),canon(d.draft));assert.equal(decoded.id,d.id);assert.equal(decoded.revision,d.revision)});
  const nativeFile=write(`native/${id}.native-map.json`,packet),levels=(d.draft.levels||[]).map(x=>x.levelId);if(!levels.length)levels.push(d.viewport?.level||'level:0');
  const secrets=(d.draft.features||[]).filter(x=>x.layerId==='layer:gm'||x.gmOnly||x.visibility==='gm').map(x=>({id:x.featureId,label:x.mapLabel||'',level:x.levelId||null,kind:x.kind}));
  const record={fixtureId:id,purpose,type,index,catalogId:ex.id,catalogSource:ex.source,nativeId:d.id,revision:d.revision,title:d.title,mode:d.mode,levels,featureCount:(d.draft.features||[]).length,secrets,nativeFile,baselineLevel:d.viewport?.level||levels[0],notes:type==='topology-map'?'Topology source retained. Artwork snapshots do not prove portal reachability or impossible-space gameplay.':type==='deck-ship'?'Both deck source records retained. Native artwork is not a complete Deck Builder overlay screenshot.':''};
  for(const z of [.5,1,2,4])renders.push(await draw(d,id,z,record.baselineLevel,'gm'));
  // Every floor gets explicit GM/player static projection expectations, separately from live authorization.
  for(const level of levels){
   const policies={gm:{audience:'gm',width:800,height:520,level,grid:'none'},player:{audience:'player',width:800,height:520,level,grid:'none',reviewed:true,reviewedArt:false}};
   for(const role of ['gm','player']){
    const p=H.prepare(d,policies[role]),payload=projectionPayload(p.doc),text=canon(payload),ids=new Set((payload.draft.features||[]).map(x=>x.featureId));
    if(role==='player')check(`${id} ${level} private feature IDs and labels absent`,()=>{for(const secret of secrets){assert(!ids.has(secret.id));if(secret.label)assert(!text.includes(secret.label))}});
    check(`${id} ${level} ${role} projected native validator`,()=>assert.equal(n.documentError(p.doc),null));
    const file=write(`roles/${id}-${level.replaceAll(':','_')}-${role}.projection.json`,{fixture:id,role,level,scope:'Static export projection; not an authentication or session packet',normalization:'Removed volatile artExportCacheKey only for snapshot identity; original prepared object used for rendering',options:policies[role],document:payload});
    roleRows.push({fixture:id,level,role,file,sourcePrivateFeatures:secrets.length,projectedFeatures:ids.size,expectedPrivateDisclosure:role==='player'?false:'GM export may include visible GM content; inspect per-floor scope'});
   }
  }
  renders.push(await draw(d,id,1,record.baselineLevel,'player','static-export'));
  check(id+' whole freeze operation source unchanged',()=>assert.equal(canon(d),before));fixtures.push(record);console.log('Frozen',id,d.title);
 }
 // Independent synthetic canary distinguishes privacy assertions from absent/private-on-another-floor content.
 const ex=catalog.examples.find(x=>x.type==='interior'&&x.index===1),canary=structuredClone(catalog.sources[ex.source]);const template=canary.draft.features.find(x=>x.kind==='room');assert(template);
 const secret=structuredClone(template);secret.featureId='mvac01:gm-only-canary';secret.layerId='layer:gm';secret.levelId=canary.viewport.level;secret.mapLabel='MVAC01_GM_ONLY_CANARY_72C9';canary.draft.features.push(secret);
 const canaryNative=write('cases/privacy-canary.native-map.json',JSON.parse(n.serializeDraft(canary)));
 const gm=H.prepare(canary,{audience:'gm',level:secret.levelId,width:800,height:520,grid:'none'}),pl=H.prepare(canary,{audience:'player',level:secret.levelId,width:800,height:520,grid:'none',reviewed:true,reviewedArt:false});
 check('Same-floor canary kept for GM export',()=>assert(canon(gm.doc).includes(secret.mapLabel)));check('Same-floor canary absent from player export',()=>assert(!canon(pl.doc).includes(secret.mapLabel)&&!canon(pl.doc).includes(secret.featureId)));
 write('cases/privacy-canary.expectation.json',{derivedFrom:'F03',nativeFile:canaryNative,sourceIdRetainedForTest:true,canary:secret,observedLocal:{gmContains:true,playerContains:false},liveClients:'NOT_RUN'});
 // Repeat at same settings to establish deterministic pixel identity on this renderer/environment.
 const first=fixtures[0],original=JSON.parse(fs.readFileSync(path.join(dir,first.nativeFile.path))).document,repeat=await draw(original,first.fixtureId,1,first.baselineLevel,'gm','repeat-artwork');
 check('F01 repeated same-environment render pixels identical',()=>assert.equal(repeat.rgbaSHA256,renders.find(x=>x.fixture==='F01'&&x.zoom===1&&x.kind==='artwork').rgbaSHA256));renders.push(repeat);
 const pack=JSON.parse(fs.readFileSync('work/optional-assets28/manifest.json')),sheet=pack.sheets[0];
 const cases=[['D01','missing_pack',{packId:pack.packId,assetId:sheet.assetId,installed:false},'missing_dependency'],['D02','version_mismatch',{packId:pack.packId,requestedVersion:1,installedVersion:2,compatibleMigration:false},'incompatible_version'],['D03','corrupt_bytes',{expectedSHA256:sheet.sha256,observedSHA256:'0'.repeat(64)},'integrity_failure'],['D04','unknown_distribution_rights',{rightsEvidence:null,requestedUse:'raw_pack_distribution'},'rights_unresolved'],['D05','unsupported_representation',{mime:'image/avif',decoderAvailable:false,fallback:null},'unsupported_format'],['D06','interrupted_install',{manifestVerified:true,blobsComplete:false,activationCommitted:false},'not_ready_last_good_retained']].map(([id,type,input,expected])=>({id,type,input,expected,observed:'NOT_RUN',implementation:'Production dependency/install/rights resolver is not present in UHT28; this is a frozen acceptance input and oracle, not a passing model test'}));
 const dependencies=write('cases/dependency-failures.json',cases);
 const environment={node:process.version,platform:process.platform,arch:process.arch,renderer:'@napi-rs/canvas '+require('@napi-rs/canvas/package.json').version,modules:renderModules,harnessSHA256:sha(fs.readFileSync('work/uvtt28-harness.cjs')),coreSHA256:sha(fs.readFileSync('work/core-28.js')),mapSHA256:sha(fs.readFileSync('work/map-28.html'))};
 const receipt={format:'multiversal:mvac01-fixture-baseline:v1',date:'2026-11-25',status:'bounded_fixture_freeze_passed',baseline:{filename:'Multiversal_Consolidated_Playtest_UHT28_MME06_UVTT_Optional_Assets.html',bytes:baseline.length,sha256:sha(baseline),catalogScriptSHA256:sha(Buffer.from(catalogRaw))},environment,fixtures,renderSettings:{width:800,height:520,dpr:1,zooms:[.5,1,2,4],grid:'off',fog:'off',rolePolicy:'Artwork GM benchmark plus per-floor static export projections; unreviewed player dressing excluded',renderDuration:'One draw observation per row; preload excluded; not a browser/device/p95 benchmark'},renders,roles:roleRows,dependencies,checks,openAcceptance:['Real browser artwork-first workflow','Keyboard, pointer and inspector interactions','Authenticated GM and two player sessions','Network payload privacy, ownership and reconnect','Physical Windows/Android and owner MacBook Air performance','Installed optional packs, persistence, quota/eviction and recovery','Receiving-VTT import','Owner/creator visual acceptance'],userData:'All maps are existing illustrative tester samples; canary and failure cases are synthetic. Package contains GM test data and is not a player export.'};
 write('MANIFEST.json',receipt);fs.writeFileSync(path.join(root,'run-results.json'),JSON.stringify({checks:checks.length,fixtures:fixtures.length,levels:roleRows.length/2,projectionSnapshots:roleRows.length,renders:renders.length,allChecksPassed:true,scope:receipt.status,baseline:receipt.baseline},null,2));console.log(JSON.stringify({checks:checks.length,fixtures:fixtures.length,projections:roleRows.length,renders:renders.length}));
})().catch(e=>{console.error(e.stack);process.exitCode=1});
