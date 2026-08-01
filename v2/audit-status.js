const BUILD='4.1.0-persistent-audit-results';
const KEY='mv-aioc-v2-audit-status';
const state={manifest:null,publication:null,inventory:null,status:null,schedule:null,reconciliation:null,importedAt:null};
const $=s=>document.querySelector(s);
const esc=v=>String(v??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const stat=(v,l)=>`<div class="stat"><strong>${Number(v||0).toLocaleString()}</strong><span>${esc(l)}</span></div>`;
function loadLocal(){try{Object.assign(state,JSON.parse(localStorage.getItem(KEY)||'{}'))}catch{}}
function save(){localStorage.setItem(KEY,JSON.stringify(state))}
async function getJson(url){const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw new Error(`${r.status} ${url}`);return r.json()}
async function firstJson(urls){for(const url of urls){try{return await getJson(url)}catch{}}return null}
async function bootstrap(){
  loadLocal();
  state.manifest=await firstJson(['../audit/archive-corpus-manifest.json'])||state.manifest||{archives:[]};
  state.publication=await firstJson(['./audit-data/publication-manifest.json'])||state.publication;
  const sources={
    inventory:['./audit-data/archive-inventory.json','../audit-output/archive-inventory.json'],
    status:['./audit-data/corpus-status.json','../audit-output/corpus-status.json'],
    schedule:['./audit-data/document-batch-schedule.json','../audit-output/document-batch-schedule.json'],
    reconciliation:['./audit-data/reconciliation-report.json','../audit-output/reconciliation-report.json']
  };
  for(const [key,urls] of Object.entries(sources))state[key]=await firstJson(urls)||state[key];
  save();render();
}
function archiveRows(){return (state.manifest?.archives||[]).map(a=>`<div class="row"><div><b>${esc(a.path)}</b><small>${esc(a.group)} · ${a.required?'required':'optional'}</small></div><span class="badge">${esc(a.status||'unknown')}</span></div>`).join('')||'<div class="empty">No archive manifest loaded.</div>'}
function coverage(){
  const s=state.status||{},inv=state.inventory||{},p=state.publication?.summary||{};
  return `<section class="metrics">${stat(s.archiveCount??p.archiveCount??inv.presentArchiveCount,'Archives present')}${stat(s.pdfCount??p.pdfCount??inv.pdfCount,'Unique PDFs')}${stat(s.csvCount??p.csvCount??inv.csvCount,'Unique CSVs')}${stat(s.totalPages??p.totalPages,'Total PDF pages')}${stat(s.completedPages??p.completedPages,'Machine-scanned pages')}${stat(s.findingCount??p.findingCount,'PDF findings')}${stat(s.csvFindingCount,'CSV findings')}${stat(s.duplicateSourceGroups??inv.duplicateMemberGroups?.length,'Duplicate source groups')}</section>`
}
function gates(){const s=state.status||{},p=state.publication?.summary||{};const gates=[['Authoritative corpus complete',state.manifest?.completionGate?.allRequiredArchivesPresent===true],['Archive extraction complete',!!state.inventory?.readyForCompleteAudit],['All PDF pages machine-scanned',s.machineScanComplete===true||s.automaticAuditComplete===true||p.machineScanComplete===true],['Human review complete',s.humanReviewComplete===true||p.humanReviewComplete===true],['Canonical promotion complete',s.canonicalPromotionComplete===true||p.canonicalPromotionComplete===true]];return gates.map(([n,pass])=>`<div class="row"><div><b>${pass?'✓':'○'} ${esc(n)}</b><small>${pass?'Gate satisfied':'Still pending'}</small></div><span class="badge">${pass?'pass':'pending'}</span></div>`).join('')}
function scheduleView(){const docs=state.schedule?.documents||[];return docs.slice(0,200).map(d=>`<div class="row"><div><b>${esc(d.member)}</b><small>${esc(d.group)} · ${esc(d.type)}${d.pageCount?` · ${d.pageCount} pages · ${(d.batches||[]).length} batches`:''}</small></div><span class="badge">${esc(d.sha256?.slice(0,10)||'')}</span></div>`).join('')||'<div class="empty">The workflow has not yet published a document schedule.</div>'}
function reconciliation(){const r=state.reconciliation||{};const rows=[['Duplicate finding groups',r.duplicateGroupCount??r.duplicateGroups?.length],['Candidate canonical matches',r.candidateMatchCount??r.candidateMatches?.length],['CSV schema groups',r.csvSchemaCount??r.csvSchemas?.length],['Unresolved findings',r.unresolvedCount??state.publication?.summary?.unresolvedCount]];return rows.map(([n,v])=>`<div class="row"><b>${esc(n)}</b><strong>${Number(v||0).toLocaleString()}</strong></div>`).join('')}
function render(){const s=state.status||{},published=state.publication?.publishedAt;statusView.innerHTML=`<section class="hero"><span class="badge">AUTHORITATIVE FOUR-ARCHIVE CORPUS</span><h2>Part 1 + Part 2 + Part 3 + Creatures</h2><p>The archive set is complete. Machine extraction, human verification, and canonical approval remain distinct gates.</p></section>${coverage()}<section class="grid two"><div class="panel"><h3>Archive authority</h3>${archiveRows()}</div><div class="panel"><h3>Completion gates</h3>${gates()}</div></section><section class="grid two"><div class="panel"><h3>Reconciliation</h3>${reconciliation()}</div><div class="panel"><h3>Coverage receipt</h3><div class="row"><b>Page coverage</b><strong>${Number(s.pageCoveragePercent||0).toFixed(2)}%</strong></div><div class="row"><b>Published result</b><small>${esc(published||state.importedAt||'Awaiting first successful workflow publication')}</small></div><div class="row"><b>Source commit</b><small>${esc(state.publication?.sourceCommit||'Not published yet')}</small></div><p class="muted">${esc(s.authorityNote||'Automatic extraction creates review candidates only.')}</p></div></section><section class="panel"><h3>Document and table schedule</h3>${scheduleView()}</section>`;bind()}
function bind(){menuBtn.onclick=()=>document.querySelector('.sidebar').classList.toggle('open')}
async function importFiles(files){for(const file of files){const data=JSON.parse(await file.text());if(data.format==='multiversal-forensic-corpus-status')state.status=data;else if(data.format==='multiversal-forensic-archive-inventory')state.inventory=data;else if(data.format==='multiversal-document-batch-schedule')state.schedule=data;else if(data.format?.includes('reconciliation'))state.reconciliation=data;else if(data.format==='multiversal-forensic-archive-corpus')state.manifest=data;else if(data.format==='multiversal-static-audit-publication')state.publication=data;}state.importedAt=new Date().toISOString();save();render()}
statusImport.onchange=e=>importFiles([...e.target.files]).catch(err=>alert(err.message));
exportStatus.onclick=()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({format:'multiversal-audit-status-bundle',build:BUILD,createdAt:new Date().toISOString(),...state},null,2)],{type:'application/json'}));a.download='multiversal-audit-status-bundle.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500)};
bootstrap();
