(()=>{'use strict';
const HANDOFF_KEY='multiversal-design-studio-handoff';
const STATE_KEY='aioc-state';
const projectBase=location.pathname.includes('/multiversal-aioc/')?'/multiversal-aioc/':'/';
const recordId=r=>r?.refId||r?.stableId||r?.catalogId||r?.databaseId;

function readState(){try{return window.AIOCData?AIOCData.load():JSON.parse(localStorage.getItem(STATE_KEY)||'{}')}catch{return{}}}
function writeState(state,reason){if(window.AIOCData)AIOCData.save(state,{reason});else localStorage.setItem(STATE_KEY,JSON.stringify(state))}
function activeId(){return document.querySelector('.object-card.active')?.dataset.id||null}
async function selectedRecord(){const id=activeId();if(!id)return null;const records=await window.MultiversalContentDB.getAll();return records.find(r=>recordId(r)===id)||null}
function toDraft(source){
  const sourceId=recordId(source);
  const body=source.gameObject||{};
  return {
    id:sourceId,
    stableId:sourceId,
    name:source.name||sourceId,
    objectKind:source.contentType||'Unclassified',
    objectType:source.contentType||'Unclassified',
    developmentStage:'Draft',
    description:body.description||source.manualEntry||source.notes||'',
    spec:structuredClone(body.spec||body||{}),
    dependencies:[...(source.dependencies||[])],
    tags:[...(source.tags||[])],
    provenance:{
      source:source.source||'Canonical Content Library',
      sourceRecordId:sourceId,
      sourceLocator:source.sourceLocator||'',
      importedFrom:'content-library',
      importedAt:new Date().toISOString(),
      immutableSource:true
    },
    extensions:{'app.multiversal.designStudio':{status:'working-copy',sourceRecordId:sourceId,lastEditedAt:new Date().toISOString()}}
  };
}
async function sendToStudio(){
  const source=await selectedRecord();
  if(!source){alert('Select a Content Library record first.');return;}
  const draft=toDraft(source);
  const state=readState();
  state.gameObjects=Array.isArray(state.gameObjects)?state.gameObjects:[];
  const existing=state.gameObjects.findIndex(o=>(o.id||o.stableId)===draft.id);
  if(existing>=0){
    const current=state.gameObjects[existing];
    state.gameObjects[existing]={...draft,...current,provenance:{...draft.provenance,...current.provenance},extensions:{...draft.extensions,...current.extensions}};
  }else state.gameObjects.push(draft);
  writeState(state,'content-library-to-design-studio');
  localStorage.setItem(HANDOFF_KEY,JSON.stringify({sourceRecord:source,draftId:draft.id,createdAt:new Date().toISOString()}));
  location.assign(`${projectBase}studio.html?draft=${encodeURIComponent(draft.id)}&from=content-library`);
}
function install(){
  const header=document.querySelector('.lib-header');
  if(!header||document.querySelector('#openInStudio'))return;
  const button=document.createElement('button');
  button.id='openInStudio';
  button.textContent='Continue selected in Design Studio';
  button.title='Create or reopen a governed working copy of the selected canonical record';
  button.addEventListener('click',sendToStudio);
  header.append(button);
}
new MutationObserver(install).observe(document.documentElement,{childList:true,subtree:true});
install();
})();