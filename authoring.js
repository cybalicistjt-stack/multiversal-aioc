(() => {
  'use strict';

  const AUTHOR_TYPES = {
    worlds:{label:'World',icon:'◉',prefix:'world',steps:[
      ['Identity',[['name','World name','text',true],['summary','One-sentence premise','textarea',true],['genre','Genres / tones','tags'],['source','Source or inspiration','text']]],
      ['Reality',[['technology','Technology level','select',['primitive','ancient','medieval','industrial','modern','advanced','post-scarcity','mixed']],['magic','Magic / supernatural level','select',['none','rare','low','common','high','reality-defining','mixed']],['cosmology','Cosmology and planar rules','textarea'],['environmentTags','Environmental tags','tags']]],
      ['Society',[['populations','Major populations and species','tags'],['governments','Governments and powers','textarea'],['currencies','Currencies and exchange','tags'],['travel','Travel and communication','textarea']]],
      ['Play',[['themes','Play themes','tags'],['threats','Major threats','textarea'],['adventureHooks','Adventure hooks','textarea'],['dependencies','Required object IDs','refs']]],
      ['Publishing',[['tags','Search tags','tags'],['notes','Author notes','textarea'],['provenance','Provenance / source notes','textarea']]]
    ]},
    abilities:{label:'Ability',icon:'✧',prefix:'ability',steps:[
      ['Identity',[['name','Ability name','text',true],['summary','What it does in play','textarea',true],['category','Ability category','select',['attack','defense','movement','social','investigation','utility','crafting','environmental','passive','reaction','ritual','other']],['domains','Domains','tags']]],
      ['Activation',[['actionType','Action type','select',['free','minor','standard','major','reaction','interrupt','passive','extended']],['resourceCosts','Resource costs','textarea'],['requirements','Requirements','textarea'],['cooldown','Cooldown / usage limit','text']]],
      ['Targeting',[['target','Target type','select',['self','single','multiple','area','object','environment','relationship','scene']],['range','Range','text'],['area','Area / shape','text'],['duration','Duration','text']]],
      ['Resolution',[['check','Check or roll','textarea'],['effects','Effects','textarea',true],['conditions','Conditions applied or removed','refs'],['scaling','Scaling and advancement','textarea']]],
      ['Governance',[['balance','Balance notes','textarea'],['aiUsage','AI and NPC usage notes','textarea'],['dependencies','Referenced object IDs','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    creatures:{label:'Creature / NPC',icon:'♞',prefix:'creature',steps:[
      ['Identity',[['name','Name','text',true],['summary','Concept and appearance','textarea',true],['creatureType','Creature type','select',['beast','humanoid','construct','spirit','undead','aberration','plant','swarm','vehicle-creature','other']],['speciesRef','Species ID','refs'],['worldRef','World ID','refs']]],
      ['Encounter Role',[['threat','Threat rating','number'],['role','Encounter role','select',['minion','support','skirmisher','controller','defender','striker','elite','boss','noncombatant']],['size','Size','select',['tiny','small','medium','large','huge','colossal','variable']],['disposition','Default disposition','select',['friendly','neutral','wary','hostile','predatory','programmed','variable']]]],
      ['Capabilities',[['movement','Movement modes and speeds','textarea'],['senses','Senses','textarea'],['defenses','Defenses and resistances','textarea'],['weaknesses','Weaknesses and vulnerabilities','textarea'],['resources','Resources and tracks','textarea']]],
      ['Rules',[['abilityRefs','Ability IDs','refs'],['traits','Special traits','textarea'],['actions','Unique actions','textarea'],['conditions','Immunities / condition notes','textarea']]],
      ['Use in Play',[['behavior','Tactics and behavior','textarea'],['social','Social profile and motivations','textarea'],['inventoryRefs','Item IDs / inventory','refs'],['loot','Loot and rewards','textarea'],['environmentTags','Environments','tags']]],
      ['Governance',[['dependencies','Other dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea'],['notes','Author notes','textarea']]]
    ]},
    species:{label:'Species',icon:'♧',prefix:'species',steps:[
      ['Identity',[['name','Species name','text',true],['summary','Defining concept','textarea',true],['classification','Classification','text'],['worldRefs','World IDs','refs']]],
      ['Body and Life',[['bodyPlan','Body plan and size range','textarea'],['lifespan','Lifespan and life cycle','textarea'],['senses','Senses','textarea'],['movement','Movement and adaptations','textarea']]],
      ['Game Traits',[['traitRefs','Ability / trait IDs','refs'],['advantages','Advantages','textarea'],['limitations','Limitations','textarea'],['environmentAdaptations','Environmental adaptations','textarea']]],
      ['Culture',[['cultures','Cultures and variation','textarea'],['languages','Languages / communication','tags'],['relations','Relations with others','textarea']]],
      ['Governance',[['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    items:{label:'Item',icon:'◇',prefix:'item',steps:[
      ['Identity',[['name','Item name','text',true],['summary','Description and purpose','textarea',true],['itemType','Item type','select',['weapon','armor','tool','consumable','artifact','container','currency','quest','implant','vehicle-part','mundane','other']],['rarity','Rarity','select',['common','uncommon','rare','exceptional','legendary','unique']]]],
      ['Physical',[['size','Size','text'],['weight','Weight / bulk','text'],['materials','Materials','tags'],['slots','Equipment slots','tags']]],
      ['Rules',[['abilityRefs','Granted ability IDs','refs'],['effects','Rules and effects','textarea'],['requirements','Requirements','textarea'],['charges','Charges / durability','text']]],
      ['Economy',[['value','Value','text'],['availability','Availability','text'],['crafting','Crafting / repair','textarea']]],
      ['Governance',[['worldRefs','World IDs','refs'],['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    vehicles:{label:'Vehicle',icon:'▷',prefix:'vehicle',steps:[
      ['Identity',[['name','Vehicle name','text',true],['summary','Description and role','textarea',true],['vehicleType','Vehicle type','select',['ground','water','air','space','dimensional','mount','walker','living','other']],['worldRefs','World IDs','refs']]],
      ['Frame',[['scale','Scale / size','text'],['crew','Crew requirements','text'],['capacity','Passenger and cargo capacity','textarea'],['movement','Movement modes and speeds','textarea']]],
      ['Systems',[['resources','Fuel, power, heat, or other tracks','textarea'],['defenses','Armor, defenses, structure','textarea'],['abilityRefs','System / ability IDs','refs'],['hardpoints','Hardpoints and modules','textarea']]],
      ['Operation',[['requirements','Piloting requirements','textarea'],['sharedOwnership','Ownership and access rules','textarea'],['maintenance','Maintenance and repair','textarea']]],
      ['Governance',[['itemRefs','Installed item IDs','refs'],['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    quests:{label:'Quest / Adventure',icon:'⚑',prefix:'quest',steps:[
      ['Identity',[['name','Quest name','text',true],['summary','Premise','textarea',true],['questType','Quest type','select',['investigation','combat','social','exploration','survival','heist','mystery','escort','faction','sandbox','other']],['worldRef','World ID','refs']]],
      ['Setup',[['startingHook','Starting hook','textarea'],['recommendedTier','Recommended tier / experience','text'],['participants','Starting NPC / faction IDs','refs'],['requirements','Prerequisites','textarea']]],
      ['Structure',[['objectives','Objectives','textarea',true],['sceneRefs','Scene / location IDs','refs'],['branches','Branches and choices','textarea'],['failureStates','Failure states','textarea']]],
      ['Resolution',[['rewards','Rewards','textarea'],['outcomes','Possible outcomes','textarea'],['followups','Follow-up quest IDs','refs'],['stateChanges','World / relationship state changes','textarea']]],
      ['Governance',[['dependencies','Creature, item, rule, and location IDs','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    dialogue:{label:'Dialogue',icon:'❞',prefix:'dialogue',steps:[
      ['Identity',[['name','Dialogue node / conversation name','text',true],['summary','Purpose in the scene','textarea',true],['speakerRef','Speaker ID','refs'],['context','Scene and context','textarea']]],
      ['Entry Conditions',[['requiredFlags','Required flags','tags'],['relationshipRequirements','Relationship requirements','textarea'],['skillRequirements','Skill / knowledge requirements','textarea']]],
      ['Content',[['line','Spoken text or prompt','textarea',true],['tone','Tone / emotion tags','tags'],['choices','Player choices','textarea'],['checks','Checks and difficulties','textarea']]],
      ['Consequences',[['outcomes','Choice outcomes','textarea'],['flagsSet','Flags set or cleared','tags'],['relationshipChanges','Relationship changes','textarea'],['nextNodes','Next dialogue IDs','refs']]],
      ['Governance',[['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    storyflow:{label:'Story Flow',icon:'⑂',prefix:'storyflow',steps:[
      ['Identity',[['name','Flow name','text',true],['summary','Narrative purpose','textarea',true],['worldRef','World ID','refs']]],
      ['Nodes',[['startNode','Starting node ID','refs'],['nodes','Nodes and descriptions','textarea',true],['transitions','Transitions and conditions','textarea',true]]],
      ['State',[['flags','Flags and variables','textarea'],['endStates','Ending states','textarea'],['repeatability','Repeat / reset behavior','textarea']]],
      ['Governance',[['dependencies','Linked quest, dialogue, scene IDs','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    relationships:{label:'Relationship',icon:'⌬',prefix:'relationship',steps:[
      ['Participants',[['name','Relationship name','text',true],['participantA','First entity ID','refs'],['participantB','Second entity ID','refs'],['relationshipType','Type','select',['family','friendship','romance','rivalry','faction','debt','loyalty','fear','respect','professional','other']]]],
      ['State',[['summary','Current relationship','textarea',true],['strength','Strength (-100 to 100)','number'],['trust','Trust (-100 to 100)','number'],['tension','Tension (0 to 100)','number'],['visibility','Who knows about it','textarea']]],
      ['Dynamics',[['triggers','Change triggers','textarea'],['benefits','Benefits and permissions','textarea'],['complications','Complications','textarea'],['history','History','textarea']]],
      ['Governance',[['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]},
    worldtimeline:{label:'World Timeline Event',icon:'⌛',prefix:'timeline',steps:[
      ['Event',[['name','Event name','text',true],['summary','What happened','textarea',true],['worldRef','World ID','refs'],['dateLabel','In-world date / era','text']]],
      ['Impact',[['participants','Entity IDs involved','refs'],['locations','Location IDs','refs'],['causes','Causes','textarea'],['consequences','Consequences','textarea']]],
      ['Continuity',[['precedingEvents','Previous event IDs','refs'],['followingEvents','Following event IDs','refs'],['certainty','Canon status','select',['canonical','reported','legendary','secret','alternate','draft']]]],
      ['Governance',[['dependencies','Dependencies','refs'],['tags','Tags','tags'],['provenance','Source provenance','textarea']]]
    ]}
  };

  const AUTHOR_KEYS = Object.keys(AUTHOR_TYPES);
  let forgeDraft = null;
  let forgeStep = 0;
  let forgeType = null;
  let forgeEditingId = null;
  let forgeTab = 'entry';

  function migrateForge(){
    state.gameObjects ||= [];
    state.packLists ||= [];
    state.authorEntries ||= [];
    state.forgeDrafts ||= [];
    state.forgeVersion = '1.0.0';
    AUTHOR_KEYS.forEach(k => state[k] ||= []);
    if(!state.packLists.length){state.packLists.push({id:uid(),name:'Multiversal Draft Objects',description:'Default staging list for authored game objects.',version:'0.1.0',status:'draft',objectIds:[],created:now(),updated:now()});}
    if(!FEATURE_GROUPS.some(g=>g[1].some(x=>x[0]==='packlists'))){
      const group=FEATURE_GROUPS.find(g=>g[0]==='Multiversal Authoring');
      group[1].push(['packlists','Pack Lists']);
      ALL_FEATURES.push(['packlists','Pack Lists']);
    }
    save(true);
  }

  migrateForge();
  const baseFeatureBody = featureBody;
  featureBody = function(id){
    if(id==='packlists') return packListsView();
    if(AUTHOR_TYPES[id]) return forgeLibrary(id);
    return baseFeatureBody(id);
  };

  const baseIcon = icon;
  icon = function(id){return id==='packlists'?'▣':(AUTHOR_TYPES[id]?.icon||baseIcon(id));};

  function forgeLibrary(type){
    const def=AUTHOR_TYPES[type], entries=state.authorEntries.filter(x=>x.objectType===type);
    const drafts=state.forgeDrafts.filter(x=>x.objectType===type);
    return `${pageHead('Multiversal Content Forge',`${def.label} Builder`,`Create a readable design entry and a normalized game object together. Save drafts at any step, validate, and send finished objects to a Pack List.`,
      `<button class="secondary" onclick="forgeOpenDrafts('${type}')">Drafts (${drafts.length})</button><button class="primary" onclick="forgeStart('${type}')">＋ Create ${def.label}</button>`)}
      <section class="forge-summary panel pad"><div>${metric('Entries',entries.length,'Readable author records')}</div><div>${metric('Game objects',state.gameObjects.filter(x=>x.type===type).length,'Structured import candidates')}</div><div>${metric('Ready',state.gameObjects.filter(x=>x.type===type&&x.validation?.status==='ready').length,'Pass validation')}</div></section>
      <section class="panel pad"><div class="row"><h3>${def.label} Library</h3><input class="forge-search" placeholder="Search ${def.label.toLowerCase()}s" oninput="forgeFilter(this,'${type}')"></div><div id="forgeLibraryRows">${forgeRows(type,entries)}</div></section>`;
  }

  function forgeRows(type,entries){
    if(!entries.length)return `<div class="empty"><b>No ${AUTHOR_TYPES[type].label.toLowerCase()} entries yet.</b><br>Create one with the guided builder. Every save creates both an entry and a game object.</div>`;
    return entries.sort((a,b)=>String(b.updated).localeCompare(String(a.updated))).map(e=>{
      const obj=state.gameObjects.find(o=>o.id===e.gameObjectId), status=obj?.validation?.status||'draft';
      return `<article class="forge-row" data-search="${esc((e.name+' '+e.summary+' '+(e.tags||[]).join(' ')).toLowerCase())}"><div class="forge-mark">${AUTHOR_TYPES[type].icon}</div><div class="forge-row-main"><b>${esc(e.name)}</b><small>${esc(e.summary||'No summary')}</small><div class="forge-chips">${badge(status)}<span>${esc(obj?.id||'No object ID')}</span><span>v${esc(obj?.version||'0.1.0')}</span></div></div><div class="forge-actions"><button onclick="forgeInspect('${e.id}','entry')">View</button><button onclick="forgeEdit('${e.id}')">Edit</button><button onclick="forgeAddToPack('${obj?.id||''}')">Add to pack</button></div></article>`;
    }).join('');
  }

  window.forgeFilter=function(input,type){document.querySelectorAll('#forgeLibraryRows .forge-row').forEach(r=>r.hidden=!r.dataset.search.includes(input.value.toLowerCase()));};

  window.forgeStart=function(type){
    forgeType=type;forgeStep=0;forgeEditingId=null;forgeDraft={objectType:type,fields:{},created:now(),updated:now()};forgeShowWizard();
  };
  window.forgeEdit=function(entryId){
    const entry=state.authorEntries.find(x=>String(x.id)===String(entryId));if(!entry)return;
    const obj=state.gameObjects.find(x=>x.id===entry.gameObjectId);
    forgeType=entry.objectType;forgeStep=0;forgeEditingId=entry.id;forgeDraft={objectType:forgeType,fields:clone(obj?.data||{}),created:entry.created,updated:now(),objectId:obj?.id,version:obj?.version||'0.1.0'};forgeShowWizard();
  };
  window.forgeOpenDrafts=function(type){
    const drafts=state.forgeDrafts.filter(x=>x.objectType===type);
    document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Saved work</small><h2>${AUTHOR_TYPES[type].label} Drafts</h2></div><button onclick="forgeClose()">✕</button></div><div class="forge-draft-list">${drafts.length?drafts.map(d=>`<div class="line"><div><b>${esc(d.fields.name||'Untitled draft')}</b><small>Step ${(d.step||0)+1} · ${new Date(d.updated).toLocaleString()}</small></div><div><button onclick="forgeResumeDraft('${d.id}')">Resume</button><button onclick="forgeDeleteDraft('${d.id}')">Delete</button></div></div>`).join(''):'<div class="empty">No saved drafts.</div>'}</div>`));
  };
  window.forgeResumeDraft=function(id){const d=state.forgeDrafts.find(x=>String(x.id)===String(id));if(!d)return;forgeType=d.objectType;forgeStep=d.step||0;forgeEditingId=d.editingId||null;forgeDraft=clone(d);forgeClose();forgeShowWizard();};
  window.forgeDeleteDraft=function(id){state.forgeDrafts=state.forgeDrafts.filter(x=>String(x.id)!==String(id));save();forgeClose();forgeOpenDrafts(forgeType);};

  function forgeShowWizard(){
    forgeClose();const def=AUTHOR_TYPES[forgeType],step=def.steps[forgeStep];
    document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>${forgeEditingId?'Editing':'Creating'} ${def.label}</small><h2>${esc(step[0])}</h2></div><button onclick="forgeClose(true)">✕</button></div>
      <div class="forge-stepper">${def.steps.map((s,i)=>`<button class="${i===forgeStep?'active':i<forgeStep?'done':''}" onclick="forgeJump(${i})"><i>${i<forgeStep?'✓':i+1}</i><span>${esc(s[0])}</span></button>`).join('')}</div>
      <form id="forgeForm" class="forge-form" onsubmit="event.preventDefault();forgeNext()">${step[1].map(fieldHtml).join('')}</form>
      <div class="forge-footer"><button class="secondary" onclick="forgeSaveDraft()">Save draft</button><div><button ${forgeStep===0?'disabled':''} onclick="forgeBack()">Back</button><button class="primary" onclick="forgeNext()">${forgeStep===def.steps.length-1?'Review object':'Next'}</button></div></div>`));
  }

  function fieldHtml(f){const [key,label,type,opt]=f,v=forgeDraft.fields[key]??'',required=opt===true, options=Array.isArray(opt)?opt:[];let control='';
    if(type==='textarea')control=`<textarea name="${key}" ${required?'required':''} rows="4" placeholder="${esc(fieldHint(key))}">${esc(v)}</textarea>`;
    else if(type==='select')control=`<select name="${key}"><option value="">Choose…</option>${options.map(o=>`<option ${v===o?'selected':''}>${esc(o)}</option>`).join('')}</select>`;
    else control=`<input name="${key}" type="${type==='number'?'number':'text'}" value="${esc(Array.isArray(v)?v.join(', '):v)}" ${required?'required':''} placeholder="${type==='tags'||type==='refs'?'Separate multiple values with commas':esc(fieldHint(key))}">`;
    return `<label class="forge-field"><span>${esc(label)}${required?' <b>*</b>':''}</span>${control}${type==='refs'?'<small>Use stable object IDs. Missing references are flagged during validation.</small>':type==='tags'?'<small>Comma-separated; tags are normalized automatically.</small>':''}</label>`;
  }
  function fieldHint(k){return ({summary:'Describe it as a player or GM would encounter it.',effects:'State the mechanical result clearly and completely.',provenance:'Record source documents, inspirations, and conversion notes.',dependencies:'Example: ability.fire-breath, condition.burning'}[k]||'');}

  function captureStep(){const form=document.querySelector('#forgeForm');if(!form)return true;if(!form.reportValidity())return false;new FormData(form).forEach((v,k)=>{const meta=AUTHOR_TYPES[forgeType].steps.flatMap(s=>s[1]).find(f=>f[0]===k);forgeDraft.fields[k]=(meta&&['tags','refs'].includes(meta[2]))?String(v).split(',').map(x=>x.trim()).filter(Boolean):String(v).trim();});forgeDraft.updated=now();return true;}
  window.forgeNext=function(){if(!captureStep())return;const last=AUTHOR_TYPES[forgeType].steps.length-1;if(forgeStep<last){forgeStep++;forgeShowWizard();}else forgeReview();};
  window.forgeBack=function(){if(captureStep()&&forgeStep>0){forgeStep--;forgeShowWizard();}};
  window.forgeJump=function(i){if(captureStep()){forgeStep=i;forgeShowWizard();}};
  window.forgeSaveDraft=function(){if(!captureStep())return;let d=state.forgeDrafts.find(x=>String(x.id)===String(forgeDraft.id));if(!d){forgeDraft.id=uid();state.forgeDrafts.push(clone({...forgeDraft,step:forgeStep,editingId:forgeEditingId}));}else Object.assign(d,clone({...forgeDraft,step:forgeStep,editingId:forgeEditingId}));save();toastForge('Draft saved on this device.');};

  function forgeReview(){
    const preview=buildObject(forgeDraft.fields,forgeType,forgeDraft.objectId,forgeDraft.version),validation=validateObject(preview);
    preview.validation=validation;forgeDraft.preview=preview;
    forgeClose();document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Review before saving</small><h2>${esc(preview.name)}</h2></div><button onclick="forgeClose(true)">✕</button></div>
      <div class="forge-review-tabs"><button class="active" onclick="forgeReviewTab(this,'entry')">Entry</button><button onclick="forgeReviewTab(this,'object')">Game object</button><button onclick="forgeReviewTab(this,'validation')">Validation (${validation.errors.length+validation.warnings.length})</button></div>
      <div id="forgeReviewBody">${reviewEntryHtml(preview)}</div>
      <div class="forge-footer"><button onclick="forgeStep=${AUTHOR_TYPES[forgeType].steps.length-1;forgeShowWizard()">Back to fields</button><div><label class="pack-select">Pack List ${packSelect('forgePackTarget')}</label><button class="primary" onclick="forgeCommit()">Save entry + object</button></div></div>`));
  }
  window.forgeReviewTab=function(btn,tab){btn.parentElement.querySelectorAll('button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const o=forgeDraft.preview;document.querySelector('#forgeReviewBody').innerHTML=tab==='object'?`<pre class="object-json">${esc(JSON.stringify(o,null,2))}</pre>`:tab==='validation'?validationHtml(o.validation):reviewEntryHtml(o);};
  function reviewEntryHtml(o){return `<div class="forge-entry-preview"><div class="forge-entry-hero"><span>${AUTHOR_TYPES[o.type].icon}</span><div><small>${esc(AUTHOR_TYPES[o.type].label)}</small><h3>${esc(o.name)}</h3><p>${esc(o.summary||'')}</p></div></div>${Object.entries(o.data).filter(([k,v])=>!['name','summary'].includes(k)&&v!==''&&(!Array.isArray(v)||v.length)).map(([k,v])=>`<div class="forge-preview-field"><b>${esc(humanize(k))}</b><p>${esc(Array.isArray(v)?v.join(', '):v)}</p></div>`).join('')}</div>`;}
  function validationHtml(v){return `<div class="validation-report"><h3>${badge(v.status)} Validation report</h3>${v.errors.map(x=>`<div class="validation-item error">✕ ${esc(x)}</div>`).join('')}${v.warnings.map(x=>`<div class="validation-item warning">⚠ ${esc(x)}</div>`).join('')}${!v.errors.length&&!v.warnings.length?'<div class="validation-item success">✓ Object is ready for a Pack List.</div>':''}</div>`;}

  window.forgeCommit=function(){
    const obj=forgeDraft.preview||buildObject(forgeDraft.fields,forgeType);obj.validation=validateObject(obj);const existing=state.gameObjects.find(x=>x.id===obj.id);if(existing)Object.assign(existing,obj);else state.gameObjects.push(obj);
    let entry=state.authorEntries.find(x=>String(x.id)===String(forgeEditingId));const entryData={id:entry?.id||uid(),objectType:forgeType,name:obj.name,summary:obj.summary,tags:obj.tags||[],gameObjectId:obj.id,created:entry?.created||now(),updated:now(),status:obj.validation.status,notes:obj.data.notes||'',provenance:obj.provenance};if(entry)Object.assign(entry,entryData);else state.authorEntries.push(entryData);
    const legacy=state[forgeType].find(x=>String(x.id)===String(entryData.id));if(legacy)Object.assign(legacy,entryData);else state[forgeType].push(clone(entryData));
    state.forgeDrafts=state.forgeDrafts.filter(x=>String(x.id)!==String(forgeDraft.id));
    const target=document.querySelector('#forgePackTarget')?.value;if(target)addObjectToPack(obj.id,target);
    save();forgeClose();render();toastForge(`${AUTHOR_TYPES[forgeType].label} saved as an entry and game object.`);
  };

  function buildObject(data,type,id,version='0.1.0'){
    const name=String(data.name||'Untitled').trim(), stable=id||`${AUTHOR_TYPES[type].prefix}.${slug(name)}.${shortId()}`;
    const deps=[...(data.dependencies||[]),...Object.entries(data).filter(([k,v])=>/Ref|Refs$|abilityRefs|traitRefs|inventoryRefs|itemRefs|participants|nextNodes|followups|sceneRefs/.test(k)&&Array.isArray(v)).flatMap(([,v])=>v)].filter(Boolean);
    return {$schema:'mv.game-object/1.0.0',id:stable,type,schemaVersion:'1.0.0',version,name,summary:data.summary||'',tags:unique(data.tags||[]),dependencies:unique(deps),provenance:{source:data.provenance||'',createdIn:'Multiversal AIOC Content Forge',createdAt:now(),updatedAt:now()},data:clone(data)};
  }
  function validateObject(o){const errors=[],warnings=[];if(!o.name||o.name==='Untitled')errors.push('A name is required.');if(!o.summary)errors.push('A playable summary is required.');if(!/^[a-z][a-z0-9._-]+$/.test(o.id))errors.push('Stable ID contains invalid characters.');const dup=state.gameObjects.find(x=>x.id===o.id&&x!==o);if(dup)errors.push(`Duplicate stable ID: ${o.id}`);const known=new Set(state.gameObjects.map(x=>x.id));(o.dependencies||[]).forEach(d=>{if(!known.has(d))warnings.push(`Unresolved dependency: ${d}`);});const required=AUTHOR_TYPES[o.type].steps.flatMap(s=>s[1]).filter(f=>f[3]===true).map(f=>f[0]);required.forEach(k=>{if(!o.data[k]||(Array.isArray(o.data[k])&&!o.data[k].length))errors.push(`Required field is missing: ${humanize(k)}`);});return {status:errors.length?'invalid':warnings.length?'review':'ready',errors,warnings,checkedAt:now()};}

  window.forgeInspect=function(entryId,tab='entry'){
    const e=state.authorEntries.find(x=>String(x.id)===String(entryId)),o=state.gameObjects.find(x=>x.id===e?.gameObjectId);if(!e||!o)return;forgeTab=tab;
    document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>${esc(AUTHOR_TYPES[e.objectType].label)}</small><h2>${esc(e.name)}</h2></div><button onclick="forgeClose()">✕</button></div><div class="forge-review-tabs"><button class="${tab==='entry'?'active':''}" onclick="forgeInspectTab(this,'entry','${e.id}')">Entry</button><button class="${tab==='object'?'active':''}" onclick="forgeInspectTab(this,'object','${e.id}')">Object</button><button onclick="forgeInspectTab(this,'validation','${e.id}')">Validation</button></div><div id="forgeInspectBody">${tab==='object'?`<pre class="object-json">${esc(JSON.stringify(o,null,2))}</pre>`:reviewEntryHtml(o)}</div><div class="forge-footer"><button class="danger-outline" onclick="forgeDeleteEntry('${e.id}')">Delete</button><div><button onclick="forgeDownloadObject('${o.id}')">Export JSON</button><button onclick="forgeClose();forgeEdit('${e.id}')">Edit</button><button class="primary" onclick="forgeAddToPack('${o.id}')">Add to Pack List</button></div></div>`));
  };
  window.forgeInspectTab=function(btn,tab,id){btn.parentElement.querySelectorAll('button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const e=state.authorEntries.find(x=>String(x.id)===String(id)),o=state.gameObjects.find(x=>x.id===e.gameObjectId);document.querySelector('#forgeInspectBody').innerHTML=tab==='object'?`<pre class="object-json">${esc(JSON.stringify(o,null,2))}</pre>`:tab==='validation'?validationHtml(o.validation||validateObject(o)):reviewEntryHtml(o);};
  window.forgeDeleteEntry=function(id){if(!confirm('Delete this authoring entry and its game object?'))return;const e=state.authorEntries.find(x=>String(x.id)===String(id));state.authorEntries=state.authorEntries.filter(x=>String(x.id)!==String(id));state[e.objectType]=state[e.objectType].filter(x=>String(x.id)!==String(id));state.gameObjects=state.gameObjects.filter(x=>x.id!==e.gameObjectId);state.packLists.forEach(p=>p.objectIds=p.objectIds.filter(x=>x!==e.gameObjectId));save();forgeClose();render();};
  window.forgeDownloadObject=function(id){const o=state.gameObjects.find(x=>x.id===id);downloadForge(JSON.stringify(o,null,2),`${o.id}.json`,'application/json');};

  function packListsView(){
    return `${pageHead('Content staging','Pack Lists','Group validated game objects, resolve dependencies and duplicate IDs, then compile a Multiversal-app-importable .pack file.',`<button class="primary" onclick="packCreate()">＋ New Pack List</button>`)}
      <div class="pack-grid">${state.packLists.map(p=>packCard(p)).join('')}</div>`;
  }
  function packCard(p){const objs=p.objectIds.map(id=>state.gameObjects.find(o=>o.id===id)).filter(Boolean),report=validatePack(p);return `<section class="panel pack-card"><div class="pack-card-head"><div><small>${esc(p.status||'draft')} · v${esc(p.version||'0.1.0')}</small><h3>${esc(p.name)}</h3><p>${esc(p.description||'')}</p></div>${badge(report.status)}</div><div class="metrics compact">${metric('Objects',objs.length,'staged')}${metric('Types',new Set(objs.map(o=>o.type)).size,'represented')}${metric('Issues',report.errors.length+report.warnings.length,'to review')}</div><div class="pack-types">${[...new Set(objs.map(o=>o.type))].map(t=>`<span>${AUTHOR_TYPES[t]?.icon||'•'} ${esc(AUTHOR_TYPES[t]?.label||t)} ${objs.filter(o=>o.type===t).length}</span>`).join('')||'<span>Empty Pack List</span>'}</div><div class="pack-card-actions"><button onclick="packOpen('${p.id}')">Open</button><button onclick="packValidateDialog('${p.id}')">Validate</button><button class="primary" onclick="packCompile('${p.id}')" ${report.errors.length?'disabled':''}>Compile .pack</button></div></section>`;}

  window.packCreate=function(){
    document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>New staging collection</small><h2>Create Pack List</h2></div><button onclick="forgeClose()">✕</button></div><form id="packCreateForm" class="forge-form"><label class="forge-field"><span>Name *</span><input name="name" required placeholder="Example: Vertigon Core Creatures"></label><label class="forge-field"><span>Description</span><textarea name="description"></textarea></label><label class="forge-field"><span>Version</span><input name="version" value="0.1.0"></label></form><div class="forge-footer"><span></span><button class="primary" onclick="packCreateCommit()">Create Pack List</button></div>`));
  };
  window.packCreateCommit=function(){const f=document.querySelector('#packCreateForm');if(!f.reportValidity())return;const d=Object.fromEntries(new FormData(f));state.packLists.push({id:uid(),name:d.name,description:d.description,version:d.version||'0.1.0',status:'draft',objectIds:[],created:now(),updated:now()});save();forgeClose();render();};
  window.packOpen=function(id){const p=state.packLists.find(x=>String(x.id)===String(id));if(!p)return;const objs=p.objectIds.map(i=>state.gameObjects.find(o=>o.id===i)).filter(Boolean);document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Pack List</small><h2>${esc(p.name)}</h2></div><button onclick="forgeClose()">✕</button></div><div class="pack-editor-meta"><label>Name<input id="packName" value="${esc(p.name)}"></label><label>Version<input id="packVersion" value="${esc(p.version)}"></label><label>Description<textarea id="packDescription">${esc(p.description||'')}</textarea></label></div><div class="row"><h3>Staged game objects (${objs.length})</h3><button onclick="packBrowseObjects('${p.id}')">＋ Add objects</button></div><div class="pack-object-list">${objs.length?objs.map(o=>`<div class="line"><div><b>${AUTHOR_TYPES[o.type]?.icon||'•'} ${esc(o.name)}</b><small>${esc(o.id)} · ${esc(AUTHOR_TYPES[o.type]?.label||o.type)}</small></div><div>${badge(o.validation?.status||'draft')}<button onclick="packRemoveObject('${p.id}','${o.id}')">Remove</button></div></div>`).join(''):'<div class="empty">No objects staged yet.</div>'}</div><div class="forge-footer"><button class="danger-outline" onclick="packDelete('${p.id}')">Delete Pack List</button><div><button onclick="packValidateDialog('${p.id}')">Validate</button><button onclick="packSaveMeta('${p.id}')">Save</button><button class="primary" onclick="packCompile('${p.id}')">Compile .pack</button></div></div>`));};
  window.packSaveMeta=function(id){const p=state.packLists.find(x=>String(x.id)===String(id));p.name=document.querySelector('#packName').value.trim()||p.name;p.version=document.querySelector('#packVersion').value.trim()||p.version;p.description=document.querySelector('#packDescription').value.trim();p.updated=now();save();forgeClose();render();};
  window.packDelete=function(id){if(!confirm('Delete this Pack List? Game objects remain in the library.'))return;state.packLists=state.packLists.filter(x=>String(x.id)!==String(id));save();forgeClose();render();};
  window.packBrowseObjects=function(packId){forgeClose();const p=state.packLists.find(x=>String(x.id)===String(packId)),available=state.gameObjects.filter(o=>!p.objectIds.includes(o.id));document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Add existing objects</small><h2>${esc(p.name)}</h2></div><button onclick="forgeClose()">✕</button></div><input class="forge-search wide" placeholder="Filter objects" oninput="document.querySelectorAll('.object-picker-row').forEach(r=>r.hidden=!r.dataset.s.includes(this.value.toLowerCase()))"><div class="object-picker">${available.length?available.map(o=>`<label class="object-picker-row" data-s="${esc((o.name+' '+o.id+' '+o.type).toLowerCase())}"><input type="checkbox" value="${esc(o.id)}"><span><b>${AUTHOR_TYPES[o.type]?.icon||'•'} ${esc(o.name)}</b><small>${esc(o.id)} · ${esc(AUTHOR_TYPES[o.type]?.label||o.type)}</small></span>${badge(o.validation?.status||'draft')}</label>`).join(''):'<div class="empty">Every object is already staged.</div>'}</div><div class="forge-footer"><span></span><button class="primary" onclick="packAddSelected('${p.id}')">Add selected</button></div>`));};
  window.packAddSelected=function(id){const p=state.packLists.find(x=>String(x.id)===String(id));document.querySelectorAll('.object-picker input:checked').forEach(i=>{if(!p.objectIds.includes(i.value))p.objectIds.push(i.value);});p.updated=now();save();forgeClose();packOpen(id);};
  window.packRemoveObject=function(pid,oid){const p=state.packLists.find(x=>String(x.id)===String(pid));p.objectIds=p.objectIds.filter(x=>x!==oid);save();forgeClose();packOpen(pid);};
  window.forgeAddToPack=function(objectId){if(!objectId)return;document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Stage game object</small><h2>Add to Pack List</h2></div><button onclick="forgeClose()">✕</button></div><div class="forge-form"><label class="forge-field"><span>Pack List</span>${packSelect('addPackTarget')}</label></div><div class="forge-footer"><button onclick="forgeClose();packCreate()">Create new list</button><button class="primary" onclick="forgeAddToPackCommit('${objectId}')">Add object</button></div>`));};
  window.forgeAddToPackCommit=function(oid){const pid=document.querySelector('#addPackTarget').value;addObjectToPack(oid,pid);save();forgeClose();toastForge('Object added to Pack List.');};
  function addObjectToPack(oid,pid){const p=state.packLists.find(x=>String(x.id)===String(pid));if(p&&!p.objectIds.includes(oid)){p.objectIds.push(oid);p.updated=now();}}

  function validatePack(p){const errors=[],warnings=[],objs=p.objectIds.map(id=>state.gameObjects.find(o=>o.id===id));objs.forEach((o,i)=>{if(!o)errors.push(`Missing object record: ${p.objectIds[i]}`);else{const v=validateObject(o);o.validation=v;if(v.errors.length)errors.push(`${o.id}: ${v.errors.join('; ')}`);v.warnings.forEach(w=>warnings.push(`${o.id}: ${w}`));}});const ids=objs.filter(Boolean).map(o=>o.id);ids.filter((id,i)=>ids.indexOf(id)!==i).forEach(id=>errors.push(`Duplicate object in Pack List: ${id}`));const included=new Set(ids);objs.filter(Boolean).forEach(o=>(o.dependencies||[]).forEach(d=>{if(!included.has(d)&&!state.gameObjects.some(x=>x.id===d))warnings.push(`${o.id} references unavailable dependency ${d}`);}));if(!objs.length)warnings.push('Pack List is empty.');return {status:errors.length?'invalid':warnings.length?'review':'ready',errors:unique(errors),warnings:unique(warnings),checkedAt:now()};}
  window.packValidateDialog=function(id){forgeClose();const p=state.packLists.find(x=>String(x.id)===String(id)),r=validatePack(p);save();document.body.insertAdjacentHTML('beforeend',forgeOverlay(`<div class="forge-modal-head"><div><small>Pack validation</small><h2>${esc(p.name)}</h2></div><button onclick="forgeClose()">✕</button></div>${validationHtml(r)}<div class="forge-footer"><span></span><button class="primary" onclick="forgeClose()">Done</button></div>`));};
  window.packCompile=function(id){const p=state.packLists.find(x=>String(x.id)===String(id)),r=validatePack(p);if(r.errors.length){packValidateDialog(id);return;}const objects=p.objectIds.map(x=>state.gameObjects.find(o=>o.id===x)).filter(Boolean);const compiled={$schema:'mv.pack/1.0.0',manifest:{id:`pack.${slug(p.name)}`,name:p.name,version:p.version||'0.1.0',description:p.description||'',status:r.warnings.length?'review':'ready',createdAt:p.created,compiledAt:now(),objectCount:objects.length,objectTypes:Object.fromEntries([...new Set(objects.map(o=>o.type))].map(t=>[t,objects.filter(o=>o.type===t).length])),dependencies:unique(objects.flatMap(o=>o.dependencies||[]).filter(d=>!objects.some(o=>o.id===d))),validation:r},objects};downloadForge(JSON.stringify(compiled,null,2),`${slug(p.name)}-${p.version||'0.1.0'}.pack`,'application/json');p.status=r.warnings.length?'review':'compiled';p.updated=now();save();toastForge('.pack file compiled and downloaded.');};

  function packSelect(id){return `<select id="${id}">${state.packLists.map(p=>`<option value="${p.id}">${esc(p.name)}</option>`).join('')}</select>`;}
  function forgeOverlay(inner){return `<div id="forgeOverlay" class="forge-overlay"><div class="forge-modal">${inner}</div></div>`;}
  window.forgeClose=function(saveDraft=false){if(saveDraft&&forgeDraft&&document.querySelector('#forgeForm')){captureStep();const existing=state.forgeDrafts.find(x=>String(x.id)===String(forgeDraft.id));if(existing)Object.assign(existing,clone({...forgeDraft,step:forgeStep,editingId:forgeEditingId}));else{forgeDraft.id=forgeDraft.id||uid();state.forgeDrafts.push(clone({...forgeDraft,step:forgeStep,editingId:forgeEditingId}));}save();}document.querySelector('#forgeOverlay')?.remove();};
  function toastForge(msg){let t=document.createElement('div');t.className='forge-toast';t.textContent=msg;document.body.appendChild(t);setTimeout(()=>t.remove(),2600);}
  function humanize(s){return s.replace(/([A-Z])/g,' $1').replace(/^./,c=>c.toUpperCase());}
  function slug(s){return String(s).toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,48)||'untitled';}
  function shortId(){return Math.random().toString(36).slice(2,8);}
  function unique(a){return [...new Set((a||[]).filter(Boolean))];}
  function downloadForge(text,name,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}

  render();
})();
