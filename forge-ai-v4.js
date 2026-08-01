(() => {
'use strict';
const VERSION='4.0';
const THREAD_KEY='aioc-forge-ai-threads-v4';
const active={type:'',threadId:'',concept:'',suggestions:{},original:{},consolidated:null};
const FIELD_CONTEXT={
 name:['Give this game object a distinctive canonical name.','Keep it concise, setting-appropriate, and usable as a stable display name.'],
 summary:['Describe what a player or GM needs to understand immediately.','Use 1–3 sentences covering identity, play role, and defining feature.'],
 classification:['Choose a normalized biological or metaphysical classification.','Prefer a reusable category such as sapient humanoid, synthetic life, elemental organism, spirit, or colonial organism.'],
 bodyPlan:['Describe anatomy using structured traits.','Include symmetry, limbs, locomotion, size band, covering, and unusual organs.'],
 lifespan:['State maturity, typical lifespan, and unusual life-cycle stages.','Use clear ranges where the source supports them.'],
 senses:['List each sense and its useful game distinction.','Example: vision—low light; vibration—short range; scent—tracking.'],
 movement:['List movement modes with relative capability.','Example: ground—standard; climb—slow; flight—fast but limited endurance.'],
 advantages:['Use discrete mechanical or narrative advantages.','Write one advantage per line as trait → benefit → limit.'],
 limitations:['Use discrete limitations that can be adjudicated.','Write one limitation per line as trigger → consequence → mitigation.'],
 environmentAdaptations:['Link environments to adaptations and effects.','Write environment → adaptation → gameplay consequence.'],
 cultures:['Describe cultural variants without treating culture as biological destiny.','Separate major traditions, institutions, values, and internal differences.'],
 languages:['Use normalized communication methods or language IDs.','Include spoken, signed, chemical, telepathic, machine, or other modes.'],
 relations:['Summarize common relationships as tendencies, not absolutes.','Mention factions, historical causes, and variation.'],
 effects:['Write implementable mechanical clauses.','Use trigger/target/check/effect/duration/limit where applicable.'],
 resourceCosts:['Write resource ID, amount, timing, and refund rule.','Example: stamina 2 on activation; refunded if no valid target.'],
 requirements:['Use testable prerequisites.','Separate equipment, state, training, environment, and target requirements.'],
 scaling:['State exactly what changes and at which progression points.','Avoid open-ended “becomes stronger” language.'],
 behavior:['Give actionable GM/AI tactics.','Include priorities, opening behavior, retreat condition, and social response.'],
 objectives:['Use measurable objective statements.','Each objective should have completion evidence and optional failure state.'],
 choices:['Write one choice per line with intent and consequence hook.','Format: label | player intent | immediate branch.'],
 outcomes:['Map inputs to explicit state changes.','Format: condition/choice → result → flags/relationships/rewards.'],
 provenance:['Record source, interpretation, and uncertainty.','Identify source document/section and what was newly authored or inferred.'],
 dependencies:['Reference stable IDs only.','Use the object picker where possible; unresolved IDs remain review warnings.']
};
const VOCAB={
 classification:['Sapient humanoid','Sapient non-humanoid','Animal','Plant-like organism','Fungoid organism','Synthetic life','Construct','Spirit','Undead','Elemental organism','Aberration','Collective organism','Energy life','Other'],
 bodyPlan:['Bilateral humanoid','Bilateral quadruped','Radial','Serpentine','Avian','Aquatic','Arthropod','Amorphous','Modular','Colonial','Energy-form','Variable'],
 lifespan:['Ephemeral (days–months)','Short (1–20 years)','Humanlike (40–120 years)','Long (120–500 years)','Ancient (500+ years)','Ageless','Cyclic reincarnation','Constructed/replaced'],
 senses:['Normal vision','Low-light vision','Darkvision','Thermal vision','Ultraviolet vision','Echolocation','Vibration sense','Scent tracking','Electromagnetic sense','Magic sense','Telepathy','Pressure sense'],
 movement:['Ground','Climb','Swim','Burrow','Glide','Flight','Teleport','Phase','Space movement','Dimensional travel'],
 advantages:['Environmental resistance','Enhanced sense','Natural armor','Rapid recovery','Special movement','Communication advantage','Resource efficiency','Social adaptation','Craft aptitude','Innate ability'],
 limitations:['Environmental vulnerability','Resource dependency','Sensory weakness','Movement restriction','Social complication','Biological requirement','Cooldown/recovery need','Equipment incompatibility','Cultural restriction'],
 environmentAdaptations:['Aquatic','Arctic','Desert','Forest','Mountain','Urban','Underground','Volcanic','Vacuum','High radiation','Magical saturation','Low gravity','High gravity','Toxic atmosphere']
};
function loadThreads(){try{return JSON.parse(localStorage.getItem(THREAD_KEY)||'[]')}catch{return []}}
function saveThreads(v){localStorage.setItem(THREAD_KEY,JSON.stringify(v))}
function uid4(){return 'ai-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2,7)}
function getType(){const small=document.querySelector('#forge2 header small')?.textContent||'';const m=small.match(/(?:Creating|Editing)\s+(.+)/i);return (m?.[1]||document.querySelector('.content h1,.content h2')?.textContent||'Game Object').trim()}
function getFields(){return [...document.querySelectorAll('#forge2form [name]')].map(el=>({name:el.name,label:el.closest('label')?.querySelector('span')?.textContent?.replace(/\s*\*\s*$/,'')||el.name,value:el.value,type:el.tagName==='SELECT'?'select':el.tagName==='TEXTAREA'?'textarea':el.type,options:el.tagName==='SELECT'?[...el.options].map(o=>o.value).filter(Boolean):[]}))}
function allCurrentValues(){const out={};document.querySelectorAll('#forge2form [name]').forEach(el=>out[el.name]=el.value);return out}
function thread(){let ts=loadThreads();let t=ts.find(x=>x.id===active.threadId);if(!t){t={id:uid4(),type:getType(),concept:'',chatUrl:'',messages:[],suggestions:{},original:{},created:new Date().toISOString(),updated:new Date().toISOString()};ts.push(t);saveThreads(ts);active.threadId=t.id}return t}
function updateThread(patch){const ts=loadThreads(),i=ts.findIndex(x=>x.id===active.threadId);if(i<0)return;Object.assign(ts[i],patch,{updated:new Date().toISOString()});saveThreads(ts)}
function guidanceFor(f){const specific=FIELD_CONTEXT[f.name]||[];const control=f.options.length?`Allowed values: ${f.options.join(', ')}.`:'';return [...specific,control].filter(Boolean).join(' ')}
function makeSuggestion(field,concept){const c=concept.trim();if(!c)return '';
 const n=field.name.toLowerCase();
 if(n==='name')return titleCase(c.split(/[,.]/)[0].replace(/\b(a|an|the|that|which|with|who)\b/gi,'').trim()).slice(0,64);
 if(n==='summary')return `A ${c.replace(/[.]$/,'')} designed for use as a normalized Multiversal ${getType().toLowerCase()} game object.`;
 if(VOCAB[field.name])return chooseVocab(VOCAB[field.name],c);
 if(n.includes('tag'))return keywords(c).slice(0,5).join(', ');
 if(n.includes('provenance'))return 'Original AIOC concept; review against canonical source material before publication.';
 if(n.includes('depend')||n.endsWith('ref')||n.endsWith('refs'))return '';
 const hints=FIELD_CONTEXT[field.name]?.[1]||'';
 return hints?`Suggested from concept: ${c}. ${hints}`:`Suggested from concept: ${c}.`;
}
function chooseVocab(arr,c){const s=c.toLowerCase();const hit=arr.find(x=>x.toLowerCase().split(/[ (/-]/).some(w=>w.length>3&&s.includes(w)));return hit||arr[0]}
function keywords(s){return [...new Set(s.toLowerCase().replace(/[^a-z0-9\s-]/g,'').split(/\s+/).filter(x=>x.length>3))]}
function titleCase(s){return s.replace(/\w\S*/g,w=>w[0].toUpperCase()+w.slice(1).toLowerCase())}
function inject(){const form=document.querySelector('#forge2form');if(!form||form.dataset.ai4==='1')return;form.dataset.ai4='1';const t=thread();active.type=getType();active.concept=t.concept||'';active.suggestions=t.suggestions||{};active.original=t.original||{};
 const panel=document.createElement('section');panel.className='ai4-panel';panel.innerHTML=`<div class="ai4-title"><div><b>AI Draft Session</b><small>Dedicated context for this ${escapeHtml(active.type)} draft</small></div><span>AI 4.0</span></div><label>Concept<textarea id="ai4Concept" rows="3" placeholder="Describe the complete idea in plain language…">${escapeHtml(active.concept)}</textarea></label><div class="ai4-actions"><button type="button" onclick="ForgeAI4.propagate()">Propagate suggestions to every field</button><button type="button" onclick="ForgeAI4.openThread()">Open dedicated ChatGPT thread</button><button type="button" onclick="ForgeAI4.threadSettings()">Thread link</button></div><small class="ai4-note">Suggestions remain editable. Your typed value is never overwritten unless you choose Apply.</small>`;form.prepend(panel);
 getFields().forEach(f=>decorateField(f));
 observeReview();
}
function decorateField(f){const el=document.querySelector(`#forge2form [name="${CSS.escape(f.name)}"]`);if(!el)return;const lab=el.closest('label');if(!lab||lab.dataset.ai4)return;lab.dataset.ai4='1';const g=document.createElement('div');g.className='ai4-guidance';g.textContent=guidanceFor(f)||'Use a concise value that can be normalized into the game object.';lab.appendChild(g);
 const sug=active.suggestions[f.name]||'';const box=document.createElement('div');box.className='ai4-suggestion';box.innerHTML=`<div><b>Suggested value</b><span id="ai4s-${escapeAttr(f.name)}">${escapeHtml(sug||'Generate from the concept above.')}</span></div><div><button type="button" onclick="ForgeAI4.field('${escapeJs(f.name)}')">Suggest</button><button type="button" onclick="ForgeAI4.apply('${escapeJs(f.name)}')" ${sug?'':'disabled'}>Apply</button></div>`;lab.appendChild(box);
 if(VOCAB[f.name]){const chips=document.createElement('div');chips.className='ai4-chips';chips.innerHTML=VOCAB[f.name].map(v=>`<button type="button" onclick="ForgeAI4.set('${escapeJs(f.name)}','${escapeJs(v)}')">${escapeHtml(v)}</button>`).join('');lab.appendChild(chips)}
 el.addEventListener('input',()=>{lab.classList.toggle('ai4-changed',!!active.suggestions[f.name]&&el.value!==active.suggestions[f.name]);});
}
function propagate(){const concept=document.querySelector('#ai4Concept')?.value.trim()||'';if(!concept){alert('Enter the overall concept first.');return}const fields=getFields();const suggestions={...active.suggestions},original={...active.original};fields.forEach(f=>{const s=makeSuggestion(f,concept);if(s)suggestions[f.name]=s;if(original[f.name]===undefined)original[f.name]=f.value});active.concept=concept;active.suggestions=suggestions;active.original=original;updateThread({concept,suggestions,original});fields.forEach(f=>refreshSuggestion(f.name));}
function suggestField(name){const concept=document.querySelector('#ai4Concept')?.value.trim()||active.concept;const f=getFields().find(x=>x.name===name);if(!f)return;active.suggestions[name]=makeSuggestion(f,concept);updateThread({concept,suggestions:active.suggestions});refreshSuggestion(name)}
function refreshSuggestion(name){const span=document.getElementById(`ai4s-${name}`),lab=document.querySelector(`#forge2form [name="${CSS.escape(name)}"]`)?.closest('label');if(span)span.textContent=active.suggestions[name]||'No suggestion yet.';const btn=lab?.querySelector('.ai4-suggestion button:last-child');if(btn)btn.disabled=!active.suggestions[name]}
function apply(name){const el=document.querySelector(`#forge2form [name="${CSS.escape(name)}"]`);if(!el||!active.suggestions[name])return;el.value=active.suggestions[name];el.dispatchEvent(new Event('input',{bubbles:true}));}
function set(name,value){active.suggestions[name]=value;updateThread({suggestions:active.suggestions});refreshSuggestion(name);apply(name)}
function prompt(kind='propagate'){
 const t=thread(),fields=getFields();const values=allCurrentValues();const schema=fields.map(f=>({field:f.name,label:f.label,input:f.type,allowed:f.options.length?f.options:(VOCAB[f.name]||[]),guidance:guidanceFor(f)}));
 if(kind==='consolidate')return `You are the dedicated Multiversal Content Forge assistant for one ${active.type} draft.\n\nORIGINAL CONCEPT:\n${t.concept}\n\nORIGINAL AI SUGGESTIONS:\n${JSON.stringify(t.suggestions,null,2)}\n\nAUTHOR-EDITED VALUES:\n${JSON.stringify(values,null,2)}\n\nTASK:\nConsolidate and rework the author-edited values into a coherent final version. Preserve every intentional author change. Improve consistency, terminology, completeness, and game-object readiness. Do not silently restore an original suggestion where the author changed it. Return JSON only, with exactly the field keys in this schema:\n${JSON.stringify(schema,null,2)}`;
 return `You are the dedicated Multiversal Content Forge assistant for one ${active.type} draft. Maintain continuity across later messages in this same conversation.\n\nCONCEPT:\n${t.concept}\n\nCURRENT STEP FIELD SCHEMA:\n${JSON.stringify(schema,null,2)}\n\nEXISTING VALUES:\n${JSON.stringify(values,null,2)}\n\nTASK:\nPropose a value for every field, including fields that could remain blank. Use allowed values where provided. Make prose mechanically convertible: use explicit actors, triggers, targets, effects, durations, limits, IDs, and structured clauses. Return JSON only with exactly the field keys listed above.`;
}
async function copyPrompt(kind){const p=prompt(kind);await navigator.clipboard.writeText(p);const t=thread();t.messages.push({role:'user',kind,content:p,at:new Date().toISOString()});updateThread({messages:t.messages});return p}
async function openThread(){await copyPrompt('propagate');const t=thread();window.open(t.chatUrl||'https://chatgpt.com/','_blank','noopener');toast('Prompt copied. Paste it into the dedicated ChatGPT conversation. Save that conversation link here once, then this button will reopen the same thread.')}
function settings(){const t=thread();const url=prompt('Paste the dedicated ChatGPT conversation URL. Leave blank to open a new chat each time.',t.chatUrl||'');if(url===null)return;updateThread({chatUrl:url.trim()});toast(url.trim()?'Dedicated thread link saved.':'Thread link cleared.')}
function importJson(){const raw=prompt('Paste the JSON returned by ChatGPT.','');if(!raw)return;try{const obj=JSON.parse(raw);Object.entries(obj).forEach(([k,v])=>{const el=document.querySelector(`#forge2form [name="${CSS.escape(k)}"]`);if(el){active.suggestions[k]=Array.isArray(v)?v.join(', '):String(v??'');refreshSuggestion(k)}});updateThread({suggestions:active.suggestions});toast('AI suggestions imported. Review and apply field by field.')}catch{alert('That was not valid JSON. Ask ChatGPT to return JSON only.') }}
function observeReview(){const obs=new MutationObserver(()=>{const screen=document.querySelector('#forge2 .forge2-screen');if(!screen||screen.querySelector('.ai4-review'))return;const text=screen.textContent||'';if(/Review|Validation|Save entry/i.test(text)&&!document.querySelector('#forge2form')){const bar=document.createElement('section');bar.className='ai4-review';bar.innerHTML=`<h3>Final AI consolidation</h3><p>Choose your authored values as-is, or ask the same ChatGPT thread to consolidate the original concept, original suggestions, and all of your changes.</p><div><button type="button" onclick="ForgeAI4.useTyped()">Use what I typed</button><button type="button" onclick="ForgeAI4.consolidate()">Ask GPT to consolidate</button><button type="button" onclick="ForgeAI4.applyConsolidated()" ${active.consolidated?'':'disabled'}>Use consolidated version</button></div><textarea id="ai4FinalJson" rows="7" placeholder="Paste consolidated JSON here, then choose Use consolidated version.">${active.consolidated?escapeHtml(JSON.stringify(active.consolidated,null,2)):''}</textarea>`;screen.querySelector('footer')?.before(bar)}});obs.observe(document.body,{childList:true,subtree:true})}
async function consolidate(){await copyPrompt('consolidate');const t=thread();window.open(t.chatUrl||'https://chatgpt.com/','_blank','noopener');toast('Consolidation prompt copied. Paste it into the dedicated thread, then paste its JSON into the final review box.')}
function applyConsolidated(){const raw=document.querySelector('#ai4FinalJson')?.value;if(!raw)return;try{active.consolidated=JSON.parse(raw);updateThread({consolidated:active.consolidated});localStorage.setItem('aioc-forge-v4-consolidated',JSON.stringify({threadId:active.threadId,data:active.consolidated}));toast('Consolidated version selected. Return to fields to inspect it, or save using the forge review controls.')}catch{alert('The consolidated response is not valid JSON.')}}
function useTyped(){active.consolidated=null;updateThread({consolidated:null});toast('Your entered values remain the final version.')}
function toast(s){const n=document.createElement('div');n.className='ai4-toast';n.textContent=s;document.body.appendChild(n);setTimeout(()=>n.remove(),5000)}
function escapeHtml(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function escapeAttr(s){return escapeHtml(s)}function escapeJs(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'")}
const mo=new MutationObserver(()=>inject());mo.observe(document.body,{childList:true,subtree:true});setTimeout(inject,100);
window.ForgeAI4={propagate,field:suggestField,apply,set,openThread,threadSettings:settings,importJson,consolidate,applyConsolidated,useTyped,copyPrompt};
})();
