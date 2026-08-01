const BUILD='4.0.0-four-archive-audit';
const KEY='mv-aioc-v2-audit-status';
const state={manifest:null,inventory:null,status:null,schedule:null,reconciliation:null,importedAt:null};
const $=s=>document.querySelector(s);
const esc=v=>String(v??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const stat=(v,l)=>`<div class="stat"><strong>${Number(v||0).toLocaleString()}</strong><span>${esc(l)}</span></div>`;
function loadLocal(){try{Object.assign(state,JSON.parse(localStorage.getItem(KEY)||'{}'))}catch{}}
function save(){localStorage.setItem(KEY,JSON.stringify(state))}
async function getJson(url){const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw new Error(`${r.status} ${url}`);return r.json()}
async function bootstrap(){
  loadLocal();
  try{state.manifest=await getJson('../audit/archive-corpus-manifest.json')}catch(e){state.manifest={error:e.message,archives:[]}}
  for(const [key,url] of [['inventory','../audit-output/archive-inventory.json'],['status','../audit-output/corpus-status.json'],['schedule','../audit-output/document-batch-schedule.json'],['reconciliation','../audit-output/reconciliation-report.json']]){
    try{state[key]=await getJson(url)}catch{}
  }
  save();render();
}
function archiveRows(){return (state.manifest?.archives||[]).map(a=>`<div class="row"><div><b>${esc(a.path)}</b><small>${esc(a.group)} · ${a.required?'required':'optional'}</small></div><span class="badge">${esc(a.status||'unknown')}</span></div>`).join('')||'<div class="empty">No archive manifest loaded.</div>'}
function coverage(){
  const s=state.status||{},inv=state.inventory||{};
  return `<section class="metrics">${stat(s.archiveCount??inv.presentArchiveCount,'Archives present')}${stat(s.pdfCount??inv.pdfCount,'Unique PDFs')}${stat(s.csvCount??inv.csvCount,'Unique CSVs')}${stat(s.totalPages,'Total PDF pages')}${stat(s.completedPages,'Machine-scanned pages')}${stat(s.findingCount,'PDF findings')}${stat(s.csvFindingCount,'CSV findings')}${stat(s.duplicateSourceGroups??inv.duplicateMemberGroups?.length,'Duplicate source groups')}</section>`
}
function gates(){const s=state.status||{};const gates=[['Authoritative corpus complete',state.manifest?.completionGate?.allRequiredArchivesPresent===true],['Archive extraction complete',!!state.inventory?.readyForCompleteAudit],['All PDF pages machine-scanned',s.automaticAuditComplete===true],['Human review complete',s.humanReviewComplete===true],['Canonical promotion complete',s.canonicalPromotionComplete===true]];return gates.map(([n,p])=>`<div class="row"><div><b>${p?'✓':'○'} ${esc(n)}</b><small>${p?'Gate satisfied':'Still pending'}</small></div><span class="badge">${p?'pass':'pending'}</span></div>`).join('')}
function scheduleView(){const docs=state.schedule?.documents||[];return docs.slice(0,200).map(d=>`<div class="row"><div><b>${esc(d.member)}</b><small>${esc(d.group)} · ${esc(d.type)}${d.pageCount?` · ${d.pageCount} pages · ${(d.batches||[]).length} batches`:''}</small></div><span class="badge">${esc(d.sha256?.slice(0,10)||'')}</span></div>`).join('')||'<div class="empty">Run the audit workflow or import document-batch-schedule.json.</div>'}
function reconciliation(){const r=state.reconciliation||{};const rows=[['Duplicate finding groups',r.duplicateGroupCount??r.duplicateGroups?.length],['Candidate canonical matches',r.candidateMatchCount??r.candidateMatches?.length],['CSV schema groups',r.csvSchemaCount??r.csvSchemas?.length],['Unresolved findings',r.unresolvedCount]];return rows.map(([n,v])=>`<div class="row"><b>${esc(n)}</b><strong>${Number(v||0).toLocaleString()}</strong></div>`).join('')}
function render(){const s=state.status||{};statusView.innerHTML=`<section class="hero"><span class="badge">AUTHORITATIVE FOUR-ARCHIVE CORPUS</span><h2>Part 1 + Part 2 + Part 3 + Creatures</h2><p>The archive set is complete. Machine extraction, human verification, and canonical approval remain distinct gates.</p></section>${coverage()}<section class="grid two"><div class="panel"><h3>Archive authority</h3>${archiveRows()}</div><div class="panel"><h3>Completion gates</h3>${gates()}</div></section><section class="grid two"><div class="panel"><h3>Reconciliation</h3>${reconciliation()}</div><div class="panel"><h3>Coverage receipt</h3><div class="row"><b>Page coverage</b><strong>${Number(s.pageCoveragePercent||0).toFixed(2)}%</strong></div><div class="row"><b>Imported status</b><small>${esc(state.importedAt||'Repository or local state')}</small></div><p class="muted">${esc(s.authorityNote||'Automatic extraction creates review candidates only.')}</p></div></section><section class="panel"><h3>Document and table schedule</h3>${scheduleView()}</section>`;bind()}
function bind(){menuBtn.onclick=()=>document.querySelector('.sidebar').classList.toggle('open')}
async function importFiles(files){for(const file of files){const data=JSON.parse(await file.text());if(data.format==='multiversal-forensic-corpus-status')state.status=data;else if(data.format==='multiversal-forensic-archive-inventory')state.inventory=data;else if(data.format==='multiversal-document-batch-schedule')state.schedule=data;else if(data.format?.includes('reconciliation'))state.reconciliation=data;else if(data.format==='multiversal-forensic-archive-corpus')state.manifest=data;}state.importedAt=new Date().toISOString();save();render()}
statusImport.onchange=e=>importFiles([...e.target.files]).catch(err=>alert(err.message));
exportStatus.onclick=()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({format:'multiversal-audit-status-bundle',build:BUILD,createdAt:new Date().toISOString(),...state},null,2)],{type:'application/json'}));a.download='multiversal-audit-status-bundle.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500)};
bootstrap();
