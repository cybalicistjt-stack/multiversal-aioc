'use strict';
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {chromium}=require('playwright');
const file=path.join(__dirname,'artifacts','Multiversal_VCSR_Cycle_18.html');
const data=fs.readFileSync(file),html=data.toString('utf8'),sha256=crypto.createHash('sha256').update(data).digest('hex');
assert(html.startsWith('<!doctype html>')&&html.includes('</body></html>'),'Full cumulative offline HTML required');
const scripts=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(z=>z[1]);
assert.equal(scripts.length,17,'Cycle18 must contain all 17 cumulative inline scripts');
scripts.forEach((s,i)=>new vm.Script(s,{filename:'vcsr18-inline-'+i+'.js'}));
new vm.Script(scripts.join('\n'),{filename:'vcsr18-combined-global.js'});
console.log('Exact Cycle18 UTF8 bytes:',data.length,'SHA256:',sha256,'scripts individual+combined compiled:',scripts.length);
(async()=>{
const browser=await chromium.launch({headless:true});
try{
 for(const viewport of [{width:1280,height:850},{width:390,height:844}]){
  const context=await browser.newContext({viewport,acceptDownloads:true});
  const page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.setContent(html,{waitUntil:'load',timeout:120000});
  assert.equal(await page.evaluate(()=>state.schemaVersion),18,'Cycle18 bootstrap did not upgrade');
  assert.equal(await page.evaluate(()=>v18Validate(state)),true,'Cycle18 source conformance failed');
  await page.locator('[data-view="golden-proof"]').click();
  await page.locator('#v18Run').click();
  const res=await page.locator('#v18Results').innerText();
  console.log('Embedded Cycle18 checks:',res.slice(0,280));
  assert.match(res,/Cycle18 49\/49 new source-bound golden checks/,'New embedded checks not all green');
  assert.deepEqual(errors,[],'Page errors before UI acceptance');
  const sourceBefore=await page.evaluate(()=>JSON.stringify({sites:state.sites,v8:state.v8,v9:state.v9,v10:state.v10,v12:state.v12,v13:state.v13,v14:state.v14,v15:state.v15,v16:state.v16,v17:state.v17}));
  assert.equal(await page.locator('[data-v18-case]').count(),3,'GM should see all three fixtures');
  const stages=page.locator('.v18-stage');
  assert.equal(await stages.count(),8,'Ordered eight stages must exist');
  assert.equal(await page.locator('.v18-crosswalk tbody tr').count(),8,'Evidence crosswalk is not complete');
  const targets=await page.locator('.v18-stage,.v18-journey').evaluateAll(els=>els.map(e=>({label:e.textContent.trim(),height:e.getBoundingClientRect().height,width:e.getBoundingClientRect().width})));
  assert(targets.every(z=>z.height>=44&&z.width>=44),'Golden controls smaller than locally targeted 44px: '+JSON.stringify(targets.filter(z=>z.height<44||z.width<44)));
  assert.equal(await page.locator('[data-v18-stage][aria-current="step"]').count(),1,'Current accessible stage missing');
  assert(await page.locator('#v18Evidence').isVisible(),'GM stage evidence field should be labeled and visible');
  const unlabeled=await page.locator('.v18-fields input').evaluateAll(els=>els.filter(e=>!e.labels?.length).map(e=>e.id));
  assert.deepEqual(unlabeled,[],'Unlabeled new form fields');
  await page.locator('#role').selectOption('player');
  assert.equal(await page.locator('[data-v18-case]').count(),2,'GM-private ship visible in Player case count');
  assert.equal(await page.locator('#v18Advance').count(),0,'Player should not be able to emit GM fixture evidence');
  const playerD=page.waitForEvent('download');await page.locator('#v18ExportPlayer').click();
  const playerDownload=await playerD,playerBytes=fs.readFileSync(await playerDownload.path()),player=JSON.parse(playerBytes.toString('utf8'));
  assert.equal(player.schemaVersion,18);assert.equal(player.goldenProofBridge.caseCount,2);
  assert(!player.goldenProofBridge.cases.some(c=>c.id==='v18:golden:unknown-ship'),'GM hidden golden source leaked');
  assert.equal(player.goldenProofBridge.localReceipts.length,0,'GM operation identities leaked in Player JSON');
  assert(player.goldenProofBridge.cases.every(c=>!('stageEvidence'in c)&&!('sourceLocationRef'in c)&&!('repairTargetId'in c)),'GM evidence leaked in Player JSON');
  assert(player.spatialBridge&&player.projectsBridge&&player.characterGmBridge&&player.economyRiskBridge,'Prior typed handoffs dropped');
  const extraOutputs=['assetMutated','characterMutated','platformMutated','worldGeometryMutated','salvageOutputsMinted','lootAcquired','repairCompleted','mountInstalled','actionUsed','storageTransferred','remoteCheckpointVerified'];
  assert(extraOutputs.every(k=>player.goldenProofBridge[k]===false),'Player handoff claimed actual gameplay writes');
  await page.locator('#role').selectOption('gm');
  // Keyboard-only selection of a different case. Native button must respond to Enter.
  const roverButton=page.locator('[data-v18-case="v18:golden:rover"]');
  await roverButton.focus();await page.keyboard.press('Enter');
  assert.equal(await page.evaluate(()=>v18Selected),'v18:golden:rover','Keyboard Enter did not switch local case');
  assert.equal(await page.locator('.v18-stage').count(),8);
  // Exercise keyboard-accessible guide and return, with visible focus.
  await page.locator('#v18Help').focus();await page.keyboard.press('Enter');
  assert(await page.locator('.v18-help details').count()>=6,'Keyboard guide unavailable');
  await page.locator('#v18Sources').focus();await page.keyboard.press('Enter');
  assert.equal(await page.locator('.v18-crosswalk tbody tr').count(),8,'Keyboard source crosswalk unavailable');
  const focusStyles=await page.locator('#v18Sources').evaluate(el=>({outline:getComputedStyle(el).outlineStyle,width:getComputedStyle(el).outlineWidth}));
  assert(focusStyles.outline!=='none'&&focusStyles.width!=='0px','Focus has no visible style');
  // Run Rover end-to-end using true controls, not test-only function calls.
  for(let i=0;i<8;i++){
    const current=await page.evaluate(()=>v18Get(state,'v18:golden:rover').steps.length);
    assert.equal(current,i,'Unexpected Rover route step');
    await page.locator('#v18Advance').click();
    const after=await page.evaluate(()=>v18Get(state,'v18:golden:rover').steps.length);
    assert.equal(after,i+1,'Rover step '+(i+1)+' did not advance: '+await page.locator('#toast').allInnerTexts().catch(()=>[]));
  }
  assert.equal(await page.evaluate(()=>v18Get(state,'v18:golden:rover').status),'local-route-complete');
  assert.equal(await page.evaluate(()=>JSON.stringify({sites:state.sites,v8:state.v8,v9:state.v9,v10:state.v10,v12:state.v12,v13:state.v13,v14:state.v14,v15:state.v15,v16:state.v16,v17:state.v17})),sourceBefore,'Rover flow touched existing owners');
  // Independent Blackglass golden route is subject to distinct authorized 2-piece vs owned 3-piece provenance warning.
  await page.locator('[data-v18-case="v18:golden:blackglass"]').click();
  assert((await page.locator('.v18-note').allInnerTexts()).some(t=>t.includes('DISTINCT fixtures')),'Blackglass lineage caveat missing');
  for(let i=0;i<8;i++)await page.locator('#v18Advance').click();
  assert.equal(await page.evaluate(()=>v18Get(state,'v18:golden:blackglass').status),'local-route-complete');
  // The third fixture is expected to halt on unknown ship extraction.
  await page.locator('[data-v18-case="v18:golden:unknown-ship"]').click();
  assert((await page.locator('.v18-note').allInnerTexts()).some(t=>t.includes('no source-authored recoverable module quantity')),'Ship negative gate warning absent');
  for(let i=0;i<3;i++)await page.locator('#v18Advance').click();
  assert.equal(await page.evaluate(()=>v18Get(state,'v18:golden:unknown-ship').steps.length),3);
  await page.locator('#v18Advance').click();
  assert.equal(await page.evaluate(()=>v18Get(state,'v18:golden:unknown-ship').steps.length),3,'Unknown ship incorrectly stripped');
  assert.equal(await page.evaluate(()=>v18Validate(state)),true,'Cumulative state invalid after expected ship failure');
  assert.equal(await page.evaluate(()=>JSON.stringify({sites:state.sites,v8:state.v8,v9:state.v9,v10:state.v10,v12:state.v12,v13:state.v13,v14:state.v14,v15:state.v15,v16:state.v16,v17:state.v17})),sourceBefore,'One of three routes mutated source-owner state');
  const gmD=page.waitForEvent('download');await page.locator('#v18ExportGM').click();
  const gmDownload=await gmD,gmBytes=fs.readFileSync(await gmDownload.path()),checkpoint=JSON.parse(gmBytes.toString('utf8'));
  assert.equal(checkpoint.schemaVersion,18);
  assert.equal(checkpoint.v18.cases.find(c=>c.id==='v18:golden:rover').steps.length,8);
  assert.equal(checkpoint.v18.cases.find(c=>c.id==='v18:golden:blackglass').steps.length,8);
  assert.equal(checkpoint.v18.cases.find(c=>c.id==='v18:golden:unknown-ship').steps.length,3);
  assert(checkpoint.v18.cases.every(c=>c.sourceOwnerVerified===false&&!c.assetMutation&&!c.remoteCheckpointVerified));
  const fresh=await context.newPage(),freshErrors=[];fresh.on('pageerror',e=>freshErrors.push(String(e)));
  await fresh.setContent(html,{waitUntil:'load',timeout:120000});
  await fresh.setInputFiles('#fileInput',{name:'VCSR18-full-cycle-checkpoint.json',mimeType:'application/json',buffer:gmBytes});
  await fresh.locator('#applyImport').click();
  assert.equal(await fresh.evaluate(()=>state.schemaVersion),18,'Fresh full import failed');
  assert.equal(await fresh.evaluate(()=>v18Validate(state)),true,'Fresh import did not validate');
  assert.deepEqual(await fresh.evaluate(()=>state.v18.cases.map(c=>c.steps.length)),[8,8,3]);
  const pages=['vehicles','mecha','ships','runtime','repairs','logistics','spatial','projects','character-bridge','economy-risk','golden-proof'];
  for(const view of pages)await fresh.locator('[data-view="'+view+'"]').click();
  assert.equal(await fresh.locator('.v18-stage').count(),8);
  for(const p of [page,fresh]){const overflow=await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);assert(overflow<=1,'Unexpected horizontal overflow '+overflow+' @ '+viewport.width);}
  assert.deepEqual(errors,[],'JavaScript errors in source page');
  assert.deepEqual(freshErrors,[],'JavaScript errors in imported page');
  console.log(JSON.stringify({viewport,newCycleChecks:'49/49',inherited:'Cycle01–17 suites invoked, not independently recounted',goldenFixtures:{blackglass:8,rover:8,shipBlockedAfter:3},keyboardEnter:true,focusVisible:true,minimumGoldenTargetsPx:44,playerHandoffBytes:playerBytes.length,gmCheckpointBytes:gmBytes.length,checkpointFreshImport:true,priorScreens:pages.length,priorBridges:4,actualSourceMutations:0,pageErrors:0,horizontalOverflow:0,sha256}));
  await context.close();
 }
}finally{await browser.close();}
})().catch(e=>{console.error(e.stack||e);process.exitCode=1;});
