(() => {
'use strict';
const KEY='aioc-forge-ai-threads-v4';
function threads(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch{return []}}
function save(v){localStorage.setItem(KEY,JSON.stringify(v))}
function latest(){const ts=threads();return ts.sort((a,b)=>String(b.updated||'').localeCompare(String(a.updated||'')))[0]}
window.addEventListener('load',()=>{
 if(!window.ForgeAI4)return;
 window.ForgeAI4.threadSettings=function(){const ts=threads(),t=latest();if(!t)return alert('Start an AI draft session first.');const url=window.prompt('Paste the dedicated ChatGPT conversation URL. Leave blank to open a new chat each time.',t.chatUrl||'');if(url===null)return;const x=ts.find(v=>v.id===t.id);x.chatUrl=url.trim();x.updated=new Date().toISOString();save(ts);alert(url.trim()?'Dedicated ChatGPT thread saved.':'Thread link cleared.');};
 window.ForgeAI4.importJson=function(){const raw=window.prompt('Paste the JSON returned by ChatGPT.','');if(!raw)return;try{const obj=JSON.parse(raw);Object.entries(obj).forEach(([k,v])=>{const el=document.querySelector(`#forge2form [name="${CSS.escape(k)}"]`);if(el){el.value=Array.isArray(v)?v.join(', '):String(v??'');el.dispatchEvent(new Event('input',{bubbles:true}));}});alert('AI values applied to the visible fields. Review and change anything before continuing.');}catch{alert('That was not valid JSON. Ask ChatGPT to return JSON only.');}};
});
})();
