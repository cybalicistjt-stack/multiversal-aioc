(()=>{'use strict';
const INDEPENDENT=new Set(['standalone','reusable-generic']);
let decisions={};
let scheduled=false;

function readDecisions(){
  try{
    const state=window.AIOCData?AIOCData.load():JSON.parse(localStorage.getItem('aioc-state')||'{}');
    return state.contentStructure?.decisions||{};
  }catch{return{}}
}

function ensureNote(){
  let note=document.querySelector('#structureFilterNote');
  if(note)return note;
  const list=document.querySelector('#queueList');
  if(!list?.parentElement)return null;
  note=document.createElement('div');
  note.id='structureFilterNote';
  note.className='assistant-note';
  list.parentElement.insertBefore(note,list);
  return note;
}

function apply(){
  scheduled=false;
  const list=document.querySelector('#queueList');
  if(!list)return;
  let hidden=0;
  list.querySelectorAll('[data-id]').forEach(el=>{
    const decision=decisions[el.dataset.id];
    const exclude=Boolean(decision&&!INDEPENDENT.has(decision.kind));
    if(el.hidden!==exclude)el.hidden=exclude;
    if(exclude)hidden++;
  });
  const note=ensureNote();
  if(!note)return;
  const markup=`<b>Structure decisions active</b><p>${hidden} records classified as components, variants, duplicates, or obsolete are hidden from this completion queue. Review them in <a href="./content-structure.html">Content Structure</a>.</p>`;
  if(note.innerHTML!==markup)note.innerHTML=markup;
}

function scheduleApply(){
  if(scheduled)return;
  scheduled=true;
  requestAnimationFrame(apply);
}

function refreshDecisions(){
  decisions=readDecisions();
  scheduleApply();
}

window.addEventListener('DOMContentLoaded',()=>{
  decisions=readDecisions();
  const list=document.querySelector('#queueList');
  if(list)new MutationObserver(scheduleApply).observe(list,{childList:true});
  scheduleApply();
});
window.addEventListener('storage',refreshDecisions);
window.addEventListener('aioc-data-saved',refreshDecisions);
})();