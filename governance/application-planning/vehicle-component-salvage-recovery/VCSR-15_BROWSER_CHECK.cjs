'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const {chromium}=require('playwright');
const htmlPath=path.join(__dirname,'artifacts','Multiversal_VCSR_Cycle_15.html');
const htmlBytes=fs.readFileSync(htmlPath);
const html=htmlBytes.toString('utf8');
const digest=require('node:crypto').createHash('sha256').update(htmlBytes).digest('hex');
console.log('VCSR15 exact HTML SHA256:',digest,'bytes:',htmlBytes.length);
assert(html.startsWith('<!doctype html>'),'Cumulative offline document must be complete');
const scripts=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
assert(scripts.length>=14,'Earlier 13 scripts plus Cycle15 must be retained');
scripts.forEach((s,i)=>new vm.Script(s,{filename:'vcsr15-inline-'+i+'.js'}));
new vm.Script(scripts.join('\n'),{filename:'vcsr15-shared-global-scope.js'});
console.log('Cumulative inline scripts compiled:',scripts.length,'individually and in shared scope');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
 for(const viewport of [{width:1280,height:850},{width:390,height:844}]){
  const context=await browser.newContext({viewport,acceptDownloads:true});
  const page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message||String(e)));
  await page.setContent(html,{waitUntil:'load',timeout:120000});
  assert.equal(await page.evaluate(()=>state.schemaVersion),15,'Cycle15 not bootstrapped: '+JSON.stringify(errors));
  assert.equal(await page.evaluate(()=>v15Validate(state)),true,'Invalid cumulative Cycle15');
  await page.locator('[data-view="projects"]').click();
  await page.locator('#v15RunTests').click();
  const suite=await page.locator('#v15TestResults').innerText();
  console.log('Cycle15 embedded case summary:',suite.slice(0,3500));
  assert.match(suite,/Cycle 15 39\/39 local checks passed/,'Cycle15 embedded checks failed');
  const oldSource=await page.evaluate(()=>JSON.stringify(state.v12.assets));
  async function act(command,values={}){
   if(values.operationId)await page.locator('#v15Operation').fill(values.operationId);
   else await page.locator('#v15Operation').fill('v15:manual:'+command);
   if(values.evidenceRef!==undefined)await page.locator('#v15EvidenceRef').fill(values.evidenceRef);
   if(values.timeRef!==undefined)await page.locator('#v15TimeRef').fill(values.timeRef);
   if(values.resultRef!==undefined)await page.locator('#v15ResultRef').fill(values.resultRef);
   if(values.gmConfirm!==undefined)await page.locator('#v15GMConfirm').fill(values.gmConfirm);
   await page.locator('[data-v15-action="'+command+'"]').click();
   const feedback=await page.locator('#feedback').innerText();
   assert(!/required|rejected|invalid|missing|stale|conflict/i.test(feedback),'Action '+command+' failed: '+feedback);
  }
  await act('approve',{evidenceRef:'GM:approved:fixture:01'});
  await act('start');
  await act('pause');
  await act('resume',{evidenceRef:'GM:resume:fixture:02'});
  await act('time',{timeRef:'APW:campaign-time-owner:fixture-001'});
  await act('request-result');
  await act('record-owner',{resultRef:'MIB-12:external:result-fixture-001',gmConfirm:'GM:acknowledged:result-001'});
  await act('close');
  const project=await page.evaluate(()=>state.v15.projects.find(p=>p.id==='v15:fixture:rover-repair'));
  assert.equal(project.status,'closed-local');
  assert.equal(project.manualTimeEvidence.length,1);
  assert.equal(await page.evaluate(()=>JSON.stringify(state.v12.assets)),oldSource,'Local Project mutated owning physical Assets');
  await page.locator('#role').selectOption('player');
  const handoff=await page.evaluate(()=>handoff());
  assert.equal(handoff.schemaVersion,15);
  assert(!handoff.projectsBridge.projects.some(p=>p.id==='v15:fixture:gm-hidden'),'Private project leaked');
  assert(!handoff.projectsBridge.externalOwnerRequests.some(p=>p.id==='v15:fixture:mineral'),'Private mine leaked');
  assert(!handoff.projectsBridge.externalOwnerRequests.some(p=>p.id==='v15:fixture:biological'),'Private biological reference leaked');
  assert.equal(handoff.projectsBridge.localReceipts.length,0,'Private local operation receipts leaked');
  assert(handoff.projectsBridge.projects.every(p=>!p.authoritative&&!('gmApprovalRef'in p)||p.gmApprovalRef===undefined),'Private approval reference exposed');
  const playerDownload=page.waitForEvent('download');
  await page.locator('#v15Download').click();
  const playerFile=await playerDownload,playerBytes=fs.readFileSync(await playerFile.path());
  const playerDoc=JSON.parse(playerBytes.toString('utf8'));
  assert(!playerDoc.projectsBridge.projects.some(p=>p.id==='v15:fixture:gm-hidden'),'Private project leaked in real downloaded handoff');
  assert(!playerDoc.projectsBridge.externalOwnerRequests.some(p=>p.id==='v15:fixture:mineral'),'Private mineral request leaked in downloaded JSON');
  assert.equal(playerDoc.projectsBridge.localReceipts.length,0,'Private receipts appeared in downloaded Player JSON');
  await page.locator('#role').selectOption('gm');
  const dl=page.waitForEvent('download');
  await page.locator('#v15Checkpoint').click();
  const file=await dl,buf=fs.readFileSync(await file.path()),doc=JSON.parse(buf.toString('utf8'));
  assert.equal(doc.schemaVersion,15);
  assert.equal(doc.v15.projects.find(p=>p.id==='v15:fixture:rover-repair').status,'closed-local');
  const fresh=await context.newPage(),freshErrors=[];fresh.on('pageerror',e=>freshErrors.push(String(e)));
  await fresh.setContent(html,{waitUntil:'load',timeout:120000});
  await fresh.setInputFiles('#fileInput',{name:'Cycle15-GM-Checkpoint.json',mimeType:'application/json',buffer:buf});
  await fresh.locator('#applyImport').click();
  assert.equal(await fresh.evaluate(()=>state.schemaVersion),15,'Fresh browser did not reopen v15');
  assert.equal(await fresh.evaluate(()=>v15Validate(state)),true);
  assert.equal(await fresh.evaluate(()=>state.v15.projects.find(p=>p.id==='v15:fixture:rover-repair').status),'closed-local','Fresh import lost project');
  const selectors=['vehicles','mecha','ships','runtime','repairs','logistics','spatial','projects'];
  for(const selector of selectors)await fresh.locator('[data-view="'+selector+'"]').click();
  for(const pg of [page,fresh]){
   const overflow=await pg.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
   assert(overflow<=1,'Horizontal overflow at '+viewport.width+': '+overflow);
  }
  assert.deepEqual(errors,[],'Uncaught JS exceptions in active session');
  assert.deepEqual(freshErrors,[],'Uncaught JS exceptions after fresh import');
  console.log(JSON.stringify({viewport,cycle15:'39/39',regressions:'Cycle01-14 suites invoked',manualActions:['approve','start','pause','resume','time-owner-evidence','request-result','record-owner','close'],playerFiltering:true,playerHandoffBytes:playerBytes.length,htmlSha256:digest,checkpointBytes:buf.length,freshImport:true,olderViews:selectors,pageErrors:0,horizontalOverflow:0}));
  await context.close();
 }
 }finally{await browser.close();}
})().catch(err=>{console.error(err.stack||err);process.exitCode=1;});
