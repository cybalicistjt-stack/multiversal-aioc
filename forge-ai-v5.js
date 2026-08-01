(() => {
'use strict';
const BUILD='5.0';
function q(s,r=document){return r.querySelector(s)}
function qa(s,r=document){return [...r.querySelectorAll(s)]}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function toast(msg){const n=document.createElement('div');n.className='ai5-toast';n.textContent=msg;document.body.appendChild(n);setTimeout(()=>n.remove(),4200)}
function closeAssistant(){q('.ai5-panel')?.remove();document.body.classList.remove('ai5-active')}
function closeBuilder(){if(confirm('Close this builder? Save a draft first if you want to keep unfinished work.')){window.ForgeV2?.close?.(false)}}
function backToForm(){const form=q('#forge2form');if(form){form.scrollIntoView({behavior:'smooth',block:'start'});toast('Back at the form. Your current entries are unchanged.')}else{toast('Open or return to a builder step first.')}}
function concept(){return q('#ai5Concept')?.value.trim()||''}
function currentFields(){return qa('#forge2form [name]').map(el=>({name:el.name,label:q('span',el.closest('label'))?.textContent?.replace(/\s*\*\s*$/,'')||el.name,value:el.value,allowed:el.tagName==='SELECT'?qa('option',el).map(o=>o.value).filter(Boolean):[]}))}
function buildPrompt(){const fields=currentFields();return `You are assisting with a Multiversal Content Forge game object.\n\nCONCEPT:\n${concept()}\n\nFIELDS:\n${JSON.stringify(fields,null,2)}\n\nTASK:\nSuggest a value for every field. Preserve controlled values exactly where allowed choices are listed. Make mechanical text explicit and importable. Return JSON only using the exact field names.`}
async function continueChatGPT(){if(!concept()){alert('Describe the idea first.');return}try{await navigator.clipboard.writeText(buildPrompt())}catch{}window.open('https://chatgpt.com/','_blank','noopener');toast('ChatGPT opened. The prepared request is copied. ChatGPT requires you to send it; external sites cannot submit through your subscription automatically.')}
function automaticInfo(){alert('Automatic AI inside AIOC requires an OpenAI API key and separate API billing. A ChatGPT subscription cannot be used as an external app API. This option is intentionally not enabled until you choose API setup.')}
function insert(){const form=q('#forge2form');if(!form||q('.ai5-panel')||form.dataset.ai5==='1')return;form.dataset.ai5='1';q('.ai4-panel')?.remove();qa('.ai4-suggestion,.ai4-guidance,.ai4-chips').forEach(n=>n.remove());const p=document.createElement('section');p.className='ai5-panel';p.innerHTML=`<div class="ai5-head"><div><b>AI help for this object</b><small>Optional. You can leave at any time without losing the form.</small></div><span>AI ${BUILD}</span></div><label><span>Describe the whole idea</span><textarea id="ai5Concept" rows="4" placeholder="Example: A peaceful crystal species adapted to volcanic tunnels, with vibration senses and communal memory."></textarea></label><div class="ai5-primary"><button type="button" class="primary" onclick="ForgeAI5.chatgpt()">Continue in my ChatGPT account</button><button type="button" onclick="ForgeAI5.auto()">Run automatically in AIOC</button></div><p class="ai5-explain"><b>ChatGPT account:</b> opens ChatGPT and prepares the request, but you must press Send there. <b>Automatic:</b> requires separate API setup and billing.</p><div class="ai5-exits"><button type="button" onclick="ForgeAI5.hide()">Hide AI help</button><button type="button" onclick="ForgeAI5.back()">Back to form</button><button type="button" class="danger-outline" onclick="ForgeAI5.closeBuilder()">Close builder</button></div>`;form.prepend(p);document.body.classList.add('ai5-active');
}
const mo=new MutationObserver(insert);mo.observe(document.body,{childList:true,subtree:true});setTimeout(insert,100);
window.ForgeAI5={chatgpt:continueChatGPT,auto:automaticInfo,hide:closeAssistant,back:backToForm,closeBuilder};
})();
