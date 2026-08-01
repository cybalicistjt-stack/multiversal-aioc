(() => {
  'use strict';

  const FIELD_GUIDANCE = {
    name: ['Use the canonical display name. Keep it distinct enough to generate a stable ID.', []],
    summary: ['Describe what a player or GM needs to understand in one or two sentences.', []],
    classification: ['Choose the closest biological or metaphysical classification, then refine only when needed.', ['Biological species','Constructed species','Energy lifeform','Spirit species','Undead lineage','Synthetic intelligence','Hybrid lineage','Swarm intelligence','Extradimensional species']],
    bodyPlan: ['Record body arrangement first, then size range and unusual anatomy.', ['Humanoid biped','Quadruped','Hexapod','Serpentine','Avian','Aquatic','Amorphous','Swarm','Modular construct','Variable form']],
    lifespan: ['Use a normalized life-cycle category, then add exceptions.', ['Ephemeral: days or weeks','Short-lived: under 30 years','Humanlike: 30–120 years','Long-lived: 120–500 years','Ancient: 500+ years','Ageless','Cyclical rebirth','Manufactured lifecycle']],
    senses: ['List each sense as “sense — range/quality — limits.”', ['Normal vision','Low-light vision','Darkvision','Thermal sense','Echolocation','Vibration sense','Scent tracking','Electromagnetic sense','Aura sense','Planar sense']],
    movement: ['List each mode as “mode — speed class — special rule.”', ['Walk','Climb','Swim','Burrow','Fly','Glide','Teleport','Phase','Zero-gravity movement','Vehicle-dependent']],
    environmentAdaptations: ['Prefer linked adaptation or ability IDs. Use prose only for details not represented elsewhere.', ['Cold adapted','Heat adapted','Aquatic','High pressure','Low gravity','Vacuum tolerant','Toxic atmosphere','Radiation resistant','Urban adapted','Planar instability adapted']],
    advantages: ['Add one mechanical advantage per line using “trigger → effect → limit.”', ['Environmental resistance','Enhanced sense','Movement advantage','Resource efficiency','Social advantage','Crafting affinity','Recovery advantage','Defensive adaptation']],
    limitations: ['Add one meaningful limitation per line using “condition → penalty/consequence → mitigation.”', ['Environmental vulnerability','Resource dependency','Movement restriction','Sensory weakness','Social complication','Maintenance need','Recovery limitation']],
    cultures: ['Create separate culture entries when they materially change play. Use “name — values — practices — game impact.”', ['Nomadic','Urban','Clan-based','Hive society','Scholarly','Militarized','Mercantile','Spiritual','Post-scarcity','Diasporic']],
    relations: ['Describe default tendencies, not absolute behavior. Reference factions/species where possible.', ['Allied','Cooperative','Neutral','Competitive','Distrusted','Feared','Hostile','Dependent','Protector relationship']],
    resourceCosts: ['Use one cost per line: “resource ID — amount/formula — timing.”', ['No cost','1 action resource','1 stamina','1 focus','1 charge','Variable cost','Health cost','Relationship cost']],
    requirements: ['Use testable prerequisites: trait, state, equipment, position, target quality, or cooldown.', ['No prerequisite','Requires line of sight','Requires equipped item','Requires target condition','Requires environment tag','Requires minimum relationship','Requires prepared state']],
    effects: ['Use one effect per line: “target → operation → magnitude/duration → tags.”', ['Deal damage','Restore resource','Apply condition','Remove condition','Move target','Create zone','Modify relationship','Reveal information','Transform object','Summon entity']],
    scaling: ['State what scales, the progression trigger, and any cap.', ['Flat','By rank','By margin of success','By resource spent','By target count','By duration','By relationship tier','By environmental intensity']],
    resources: ['Use one track per line: “resource name — maximum/formula — refresh rule — failure at zero.”', ['Health','Stamina','Focus','Morale','Heat','Charge','Fuel','Integrity','Corruption','Relationship leverage']],
    defenses: ['Use one defense per line and reference rules/conditions instead of embedding duplicate mechanics.', ['Armor','Evasion','Will','Fortitude','Barrier','Resistance','Immunity','Damage reduction']],
    weaknesses: ['Use “trigger/type → consequence → how discovered or mitigated.”', ['Damage vulnerability','Condition vulnerability','Environmental weakness','Resource disruption','Behavioral exploit','Social leverage']],
    traits: ['Prefer existing ability/trait IDs. New prose traits should be atomic and convertible later.', ['Passive trait','Triggered trait','Environmental trait','Social trait','Movement trait','Senses trait']],
    actions: ['Use “action name — action type — target — check — result.”', ['Basic attack','Defensive action','Movement action','Control action','Support action','Social action','Escape action']],
    behavior: ['Describe priorities and decision rules, not fiction alone.', ['Protect allies','Focus weakest target','Control space','Avoid hazards','Retreat below threshold','Negotiate first','Guard objective','Hunt marked target']],
    objectives: ['Use one objective per line with success evidence and optional failure state.', ['Reach location','Protect entity','Recover object','Learn truth','Change relationship','Defeat threat','Survive duration','Prevent event']],
    branches: ['Use “condition → next scene/node → state changes.”', ['Success branch','Failure branch','Partial-success branch','Optional branch','Hidden branch','Timed branch']],
    choices: ['Use one choice per line: “label → check/cost → consequence → next node.”', ['Agree','Refuse','Ask for information','Threaten','Persuade','Offer resource','Reveal evidence','Leave']],
    outcomes: ['Use one outcome per line and identify state changes or generated objects.', ['Success','Partial success','Failure','Complication','Relationship change','World-state change','New quest','Reward']],
    dependencies: ['Select existing object IDs whenever possible. Unresolved IDs will remain warnings.', []],
    provenance: ['Record source title, section/page when available, conversion date, and any interpretation.', []]
  };

  const CONTROLLED = {
    classification:['Biological species','Constructed species','Energy lifeform','Spirit species','Undead lineage','Synthetic intelligence','Hybrid lineage','Swarm intelligence','Extradimensional species'],
    bodyPlan:['Humanoid biped','Quadruped','Hexapod','Serpentine','Avian','Aquatic','Amorphous','Swarm','Modular construct','Variable form'],
    lifespan:['Ephemeral: days or weeks','Short-lived: under 30 years','Humanlike: 30–120 years','Long-lived: 120–500 years','Ancient: 500+ years','Ageless','Cyclical rebirth','Manufactured lifecycle'],
    cooldown:['None','Once per round','Once per scene','Once per encounter','Once per rest','Charges','Requires recharge roll','Narrative trigger'],
    range:['Self','Touch','Adjacent','Short','Medium','Long','Line of sight','Scene-wide','World-scale'],
    duration:['Instant','Until end of turn','1 round','Sustained','Scene','Encounter','Until removed','Permanent'],
    size:['Tiny','Small','Medium','Large','Huge','Colossal','Variable'],
    availability:['Common','Controlled','Restricted','Rare market','Faction-only','Unique','Unavailable'],
    recommendedTier:['Novice','Experienced','Veteran','Elite','Legendary','Mixed tier']
  };

  const REFERENCE_KEYS = /(^|Refs?$|IDs?$|dependencies|participants|speakerRef|worldRef|speciesRef|startNode|nextNodes|followups|sceneRefs|traitRefs|abilityRefs|inventoryRefs|itemRefs)/i;
  let enhancedForm = null;

  function currentObjectType(){
    const text=document.querySelector('#forge2 header small')?.textContent||'';
    return text.replace(/^(Creating|Editing)\s+/i,'').trim()||'Game Object';
  }

  function addDatalist(input,key,values){
    const id=`forge3-${key}-${Math.random().toString(36).slice(2,7)}`;
    const dl=document.createElement('datalist'); dl.id=id;
    values.forEach(v=>{const o=document.createElement('option');o.value=v;dl.appendChild(o);});
    input.setAttribute('list',id); input.after(dl);
  }

  function existingReferences(){
    try{return (window.state?.gameObjects||[]).map(o=>`${o.id} — ${o.name}`);}catch{return [];}
  }

  function appendChipValue(control,value){
    const isList=/Refs?$|IDs?$|dependencies|participants|tags|domains|languages|environments|materials|slots|tone|flags/i.test(control.name||'');
    if(isList){
      const existing=String(control.value||'').split(',').map(x=>x.trim()).filter(Boolean);
      if(!existing.includes(value))existing.push(value);
      control.value=existing.join(', ');
    } else if(control.tagName==='TEXTAREA') {
      const prefix=control.value.trim()?`${control.value.trim()}\n`:'';
      control.value=prefix+value;
    } else control.value=value;
    control.dispatchEvent(new Event('input',{bubbles:true}));
  }

  function enhanceLabel(label){
    if(label.dataset.forge3==='1')return;
    const control=label.querySelector('input,textarea,select'); if(!control)return;
    label.dataset.forge3='1';
    const key=control.name||'';
    const info=FIELD_GUIDANCE[key]||['Use a concise, rules-aware value. Prefer existing IDs and normalized terms over embedded mechanics.',[]];
    const help=document.createElement('div');help.className='forge3-help';help.textContent=info[0];label.appendChild(help);

    if(control.tagName==='INPUT'&&CONTROLLED[key]) addDatalist(control,key,CONTROLLED[key]);
    if(control.tagName==='INPUT'&&REFERENCE_KEYS.test(key)){
      const refs=existingReferences(); if(refs.length)addDatalist(control,key,refs);
      const refHint=document.createElement('button');refHint.type='button';refHint.className='forge3-ref-button';refHint.textContent='Browse existing objects';
      refHint.onclick=()=>openReferencePicker(control);label.appendChild(refHint);
    }

    const chips=[...(CONTROLLED[key]||[]),...(info[1]||[])].slice(0,10);
    if(chips.length){const wrap=document.createElement('div');wrap.className='forge3-chips';chips.forEach(v=>{const b=document.createElement('button');b.type='button';b.textContent=v;b.onclick=()=>appendChipValue(control,v);wrap.appendChild(b);});label.appendChild(wrap);}

    if(control.tagName==='TEXTAREA'){
      const tools=document.createElement('div');tools.className='forge3-field-tools';
      const template=document.createElement('button');template.type='button';template.textContent='＋ Add structured line';template.onclick=()=>appendChipValue(control,structuredTemplate(key));
      const ai=document.createElement('button');ai.type='button';ai.textContent='✦ Ask AI for this field';ai.onclick=()=>openAiAssistant(key,control);
      tools.append(template,ai);label.appendChild(tools);
    }
  }

  function structuredTemplate(key){
    const map={effects:'Target → operation → magnitude/duration → tags',advantages:'Trigger → advantage → limit',limitations:'Condition → consequence → mitigation',resources:'Resource ID → maximum/formula → refresh → zero-state',defenses:'Defense type/ID → value/formula → exceptions',weaknesses:'Trigger/type → consequence → mitigation',traits:'Trait name/ID → trigger → effect → limit',actions:'Action name → action type → target → check → result',objectives:'Objective → success evidence → failure consequence',branches:'Condition → next node/scene → state changes',choices:'Choice label → cost/check → outcome → next node',outcomes:'Outcome → state changes → rewards/consequences',cultures:'Culture name → values → practices → game impact'};
    return map[key]||'Trigger/subject → rule or fact → limit/exception';
  }

  function addAiPanel(form){
    if(form.querySelector('.forge3-ai-panel'))return;
    const panel=document.createElement('section');panel.className='forge3-ai-panel';
    panel.innerHTML=`<div><b>✦ AI Draft Assistant</b><small>Describe the idea in ordinary language. The assistant creates a governed prompt for this ${escapeHtml(currentObjectType())} and the fields on this step.</small></div><textarea id="forge3Concept" rows="3" placeholder="Example: A silicon-based desert species that stores heat and communicates through color changes."></textarea><div><button type="button" id="forge3Starter">Use local starter</button><button type="button" id="forge3Prompt">Create AI prompt</button></div>`;
    form.prepend(panel);
    panel.querySelector('#forge3Starter').onclick=()=>localStarter(panel.querySelector('#forge3Concept').value,form);
    panel.querySelector('#forge3Prompt').onclick=()=>openAiAssistant('whole step',null,panel.querySelector('#forge3Concept').value);
  }

  function localStarter(concept,form){
    const words=String(concept||'').trim(); if(!words)return notify('Describe the concept first.');
    const summary=form.querySelector('[name="summary"]');if(summary&&!summary.value)summary.value=words;
    const name=form.querySelector('[name="name"]');if(name&&!name.value){name.value=words.split(/[,.]/)[0].split(/\s+/).slice(0,5).join(' ').replace(/^(a|an|the)\s+/i,'');}
    const tags=form.querySelector('[name="tags"],[name="domains"],[name="environments"]');if(tags&&!tags.value){tags.value=words.toLowerCase().match(/[a-z]{5,}/g)?.slice(0,6).join(', ')||'';}
    notify('Starter values added. Review them before continuing.');
  }

  function buildAiPrompt(field,concept=''){
    const form=document.querySelector('#forge2form');
    const fields=[...form.querySelectorAll('input[name],textarea[name],select[name]')].map(c=>({name:c.name,value:c.value,required:c.required,type:c.tagName.toLowerCase()}));
    const target=field==='whole step'?fields:fields.filter(f=>f.name===field);
    return `You are assisting with the Multiversal Content Forge.\n\nObject type: ${currentObjectType()}\nAuthor concept: ${concept||document.querySelector('#forge3Concept')?.value||'(none provided)'}\nCurrent structured fields: ${JSON.stringify(fields,null,2)}\n\nTask: Draft ${field==='whole step'?'values for the current step':`the field "${field}"`} using concise, rules-aware content. Prefer controlled vocabulary, stable game-object IDs, and atomic mechanical statements. Do not invent unresolved IDs without marking them as proposed. Return ONLY JSON with keys matching these target fields: ${target.map(f=>f.name).join(', ')}. Arrays must be arrays, not comma-separated prose. Do not add commentary.`;
  }

  async function openAiAssistant(field,control,concept=''){
    const prompt=buildAiPrompt(field,concept);
    const modal=document.createElement('div');modal.className='forge3-modal';
    modal.innerHTML=`<section><header><div><small>AI process bridge</small><h3>${field==='whole step'?'Draft this step':`Draft ${escapeHtml(field)}`}</h3></div><button type="button">✕</button></header><p>This prompt can be pasted into ChatGPT or Codex now. A direct API connector can be added later without changing the game-object schema.</p><textarea rows="14">${escapeHtml(prompt)}</textarea><footer><button type="button" data-copy>Copy prompt</button>${control?'<button type="button" data-apply>Apply pasted result</button>':''}</footer>${control?'<label>Paste the AI JSON result<textarea data-result rows="6" placeholder="Paste JSON here"></textarea></label>':''}</section>`;
    document.body.appendChild(modal);modal.querySelector('header button').onclick=()=>modal.remove();
    modal.querySelector('[data-copy]').onclick=async()=>{await navigator.clipboard.writeText(prompt);notify('AI prompt copied.');};
    if(control)modal.querySelector('[data-apply]').onclick=()=>{try{const data=JSON.parse(modal.querySelector('[data-result]').value);const v=data[field];control.value=Array.isArray(v)?v.join(', '):String(v??'');control.dispatchEvent(new Event('input',{bubbles:true}));modal.remove();notify('AI result applied. Review before saving.');}catch{notify('The pasted result is not valid JSON for this field.');}};
  }

  function openReferencePicker(control){
    const objects=window.state?.gameObjects||[];
    const modal=document.createElement('div');modal.className='forge3-modal';
    modal.innerHTML=`<section><header><div><small>Stable references</small><h3>Choose game objects</h3></div><button type="button">✕</button></header><input data-search placeholder="Search by name, type, or ID"><div class="forge3-object-list">${objects.length?objects.map(o=>`<button type="button" data-id="${escapeHtml(o.id)}" data-searchable="${escapeHtml(`${o.name} ${o.type} ${o.id}`.toLowerCase())}"><b>${escapeHtml(o.name)}</b><small>${escapeHtml(o.type)} · ${escapeHtml(o.id)}</small></button>`).join(''):'<p>No game objects exist yet. Create the referenced object first or enter a proposed ID.</p>'}</div></section>`;
    document.body.appendChild(modal);modal.querySelector('header button').onclick=()=>modal.remove();
    modal.querySelector('[data-search]').oninput=e=>modal.querySelectorAll('[data-id]').forEach(b=>b.hidden=!b.dataset.searchable.includes(e.target.value.toLowerCase()));
    modal.querySelectorAll('[data-id]').forEach(b=>b.onclick=()=>{appendChipValue(control,b.dataset.id);modal.remove();});
  }

  function notify(text){let n=document.createElement('div');n.className='forge3-toast';n.textContent=text;document.body.appendChild(n);setTimeout(()=>n.remove(),2400);}
  function escapeHtml(s=''){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}

  function enhance(){
    const form=document.querySelector('#forge2form');if(!form||form===enhancedForm)return;
    enhancedForm=form;addAiPanel(form);form.querySelectorAll('label').forEach(enhanceLabel);
    document.querySelector('.forge2-screen header small')?.insertAdjacentHTML('beforeend',' · GUIDED 3.0');
  }

  new MutationObserver(enhance).observe(document.documentElement,{childList:true,subtree:true});
  window.addEventListener('load',enhance);
})();
