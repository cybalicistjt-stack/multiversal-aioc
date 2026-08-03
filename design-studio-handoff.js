(()=>{'use strict';
const HANDOFF_KEY='multiversal-design-studio-handoff';
const STATE_KEY='aioc-state';
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function readState(){try{return window.AIOCData?AIOCData.load():JSON.parse(localStorage.getItem(STATE_KEY)||'{}')}catch{return{}}}
function writeState(state,reason){if(window.AIOCData)AIOCData.save(state,{reason});else localStorage.setItem(STATE_KEY,JSON.stringify(state))}
function requestedId(){return new URLSearchParams(location.search).get('draft')||JSON.parse(localStorage.getItem(HANDOFF_KEY)||'null')?.draftId||null}
function findDraft(state,id){return (state.gameObjects||[]).find(o=>(o.id||o.stableId)===id)}
function saveDraft(event){
  event.preventDefault();
  const state=readState();
  state.gameObjects=Array.isArray(state.gameObjects)?state.gameObjects:[];
  const id=document.querySelector('#draftId').value.trim();
  const index=state.gameObjects.findIndex(o=>(o.id||o.stableId)===id);
  const current=index>=0?state.gameObjects[index]:{};
  let spec={};
  try{spec=JSON.parse(document.querySelector('#draftSpec').value||'{}')}catch{alert('Mechanics/spec must be valid JSON.');return;}
  const updated={...current,id,stableId:id,name:document.querySelector('#draftName').value.trim(),objectKind:document.querySelector('#draftType').value.trim(),objectType:document.querySelector('#draftType').value.trim(),description:document.querySelector('#draftDescription').value.trim(),developmentStage:document.querySelector('#draftStage').value,spec,extensions:{...(current.extensions||{}),'app.multiversal.designStudio':{...(current.extensions?.['app.multiversal.designStudio']||{}),status:'working-copy',lastEditedAt:new Date().toISOString()}}};
  if(index>=0)state.gameObjects[index]=updated;else state.gameObjects.push(updated);
  writeState(state,'save-design-studio-draft');
  document.querySelector('#draftSaveStatus').textContent=`Saved ${new Date().toLocaleTimeString()} · canonical source remains unchanged.`;
  if(typeof renderMetrics==='function')renderMetrics();
}
function render(){
  const id=requestedId();
  if(!id)return;
  const state=readState();
  const draft=findDraft(state,id);
  if(!draft)return;
  const sourceId=draft.provenance?.sourceRecordId||id;
  const section=document.createElement('section');
  section.className='card';
  section.style.marginTop='16px';
  section.innerHTML=`<span class="status">CONTENT LIBRARY WORKING COPY</span><h2>Continue developing: ${esc(draft.name||id)}</h2><p>This editable draft was created from canonical record <b>${esc(sourceId)}</b>. Changes stay in the Design Studio working state until a later governed promotion replaces or extends canonical content.</p><form id="draftEditor"><label class="small">Stable ID<input id="draftId" value="${esc(id)}" readonly style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff"></label><label class="small">Name<input id="draftName" value="${esc(draft.name||'')}" required style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff"></label><label class="small">Object type<input id="draftType" value="${esc(draft.objectType||draft.objectKind||'Unclassified')}" style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff"></label><label class="small">Development stage<select id="draftStage" style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff">${['Concept','Draft','Review','Balance','Testing','Approved','Released'].map(x=>`<option ${x===(draft.developmentStage||'Draft')?'selected':''}>${x}</option>`).join('')}</select></label><label class="small">Description<textarea id="draftDescription" rows="5" style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff">${esc(draft.description||'')}</textarea></label><label class="small">Mechanics / spec JSON<textarea id="draftSpec" rows="14" style="width:100%;padding:10px;margin:5px 0 10px;border-radius:8px;border:1px solid #5e526f;background:#11131a;color:#fff;font-family:monospace">${esc(JSON.stringify(draft.spec||{},null,2))}</textarea></label><button class="primary" type="submit">Save working game object</button><p id="draftSaveStatus" class="small">Source provenance retained. Canonical source is read-only.</p></form>`;
  const hero=document.querySelector('.hero');
  hero.insertAdjacentElement('afterend',section);
  document.querySelector('#draftEditor').addEventListener('submit',saveDraft);
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',render);else render();
})();