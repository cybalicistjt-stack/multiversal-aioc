(() => {
'use strict';
const BUILD='8.0';
const LAYERS=[
 {id:'definition',name:'Creature Definition',icon:'◆',help:'Reusable canonical creature identity. The normal choice for a new creature.'},
 {id:'archetype',name:'NPC / Creature Archetype',icon:'♟',help:'Reusable role package built on a creature or species foundation.'},
 {id:'variant',name:'Variant',icon:'◇',help:'A governed alteration of an identified base Definition.'},
 {id:'template',name:'Template',icon:'▧',help:'A reusable layer applied to compatible creatures, such as undead, elite, corrupted, or juvenile.'},
 {id:'form',name:'Form or Transformation',icon:'◈',help:'A governed alternate form or state change that preserves identity.'},
 {id:'instance',name:'Campaign NPC / Individual',icon:'●',help:'Mutable campaign-specific identity. This is staged as an instance draft, not canonical replacement content.'}
];
const FAMILIES=[
 {id:'biological',name:'Biological life',icon:'✦',help:'Naturally occurring, evolved, bred, engineered, or altered organisms.',types:[
  ['animal','Animal','Non-sapient fauna whose ecology, senses, movement, and behavior drive play.'],
  ['beast','Beast','Exceptional or dangerous fauna with pronounced encounter traits.'],
  ['sapient-person','Sapient creature / person','An individual grounded in a Species Definition, culture, social role, and personal state.'],
  ['monster','Monster','A creature primarily framed by unusual danger, transformation, or incompatibility with normal ecology.'],
  ['giant','Giant-scale organism','Biological life whose scale changes movement, targeting, habitats, and encounter composition.'],
  ['vermin','Vermin / nuisance life','Small, invasive, parasitic, or hazardous organisms.'],
  ['plant','Plant organism','Mobile or immobile plant life, including carnivorous and sapient forms.'],
  ['fungal','Fungal organism','Spores, colonies, mycelial minds, fruiting bodies, and infectious ecologies.'],
  ['aquatic','Aquatic organism','Life primarily governed by water, pressure, currents, and amphibious tolerances.'],
  ['aerial','Aerial organism','Life whose core ecology and tactics depend on flight or atmospheric movement.'],
  ['bioengineered','Bioengineered organism','Designed, uplifted, cloned, hybridized, or weaponized biological life.'],
  ['symbiote','Symbiote / parasite','Life defined by a host relationship, bonding, infection, grants, or transformation.']
 ]},
 {id:'constructed',name:'Constructed and synthetic',icon:'⬡',help:'Created bodies, machines, programs, animated objects, and manufactured organisms.',types:[
  ['construct','Construct','Artificial body animated by magic, technology, spirit, rule, or maker intent.'],
  ['robot','Robot','Mechanical or synthetic embodied machine with programmed or learned behavior.'],
  ['android','Android / synthetic person','Person-like constructed being with social identity and individual agency.'],
  ['drone','Drone','Task-focused autonomous, remote, networked, or swarm-capable machine.'],
  ['ai-entity','AI entity','Software, distributed intelligence, virtual person, or network consciousness.'],
  ['animated-object','Animated object','An item, structure, vehicle, or environment given creature-like agency.'],
  ['golem','Golem / bound construct','Created body whose operation depends on commands, seals, cores, or bound forces.'],
  ['nanite-colony','Nanite colony','Distributed machines acting as a collective body or swarm.'],
  ['synthetic-organism','Synthetic organism','Manufactured life combining biological and technological rules.']
 ]},
 {id:'spiritual',name:'Spiritual and post-mortal',icon:'☽',help:'Spirits, souls, undead, divine servants, and beings whose body is not their sole identity.',types:[
  ['spirit','Spirit','A nonmaterial or partially material being tied to concepts, places, beings, or forces.'],
  ['ghost','Ghost','A post-mortal identity anchored by death, memory, obligation, place, or unresolved state.'],
  ['undead-corporeal','Corporeal undead','A dead or post-mortal being operating through a physical body.'],
  ['undead-incorporeal','Incorporeal undead','A post-mortal being without a stable physical body.'],
  ['revenant','Revenant','A returned individual driven by a mission, oath, vengeance, or binding condition.'],
  ['demon','Demonic being','A supernatural being associated with destructive, corruptive, infernal, or setting-specific forces.'],
  ['celestial','Celestial / angelic being','A supernatural servant, emissary, guardian, or manifestation of higher powers.'],
  ['divine-avatar','Divine avatar','A projected, limited, or embodied expression of a deity or cosmic power.'],
  ['ancestor','Ancestor spirit','A continuing dead identity connected to lineage, community, duty, or tradition.'],
  ['dream-being','Dream being','A being sustained by dreams, memory, symbolism, or collective imagination.']
 ]},
 {id:'elemental',name:'Elemental and environmental',icon:'◉',help:'Creatures whose identity is inseparable from an element, environment, or physical phenomenon.',types:[
  ['classical-elemental','Classical elemental','Fire, water, earth, air, or setting-equivalent elemental life.'],
  ['energy-being','Energy being','Electric, plasma, radiation, light, sound, psychic, or other energy-form life.'],
  ['weather-being','Weather entity','Storm, wind, cloud, lightning, seasonal, or atmospheric intelligence.'],
  ['terrain-being','Terrain entity','Mountain, cavern, forest, river, desert, glacier, or city-scale embodied environment.'],
  ['hazard-life','Hazard organism','Life adapted to or formed from toxins, radiation, vacuum, pressure, corruption, or magical saturation.'],
  ['environmental-adaptation','Adapted creature','A base creature strongly modified by a governed Environment Adaptation layer.']
 ]},
 {id:'exotic',name:'Extradimensional and anomalous',icon:'⌬',help:'Life whose existence depends on other realities, time states, impossible biology, or nonstandard rules.',types:[
  ['aberration','Aberration','A creature with anatomy, cognition, or rules outside expected biological and supernatural models.'],
  ['alien-life','Alien lifeform','Life evolved in radically different planetary, chemical, or cosmological conditions.'],
  ['void-creature','Void creature','Life adapted to vacuum, null space, deep space, or metaphysical absence.'],
  ['dimensional-life','Dimensional lifeform','A being native to another plane, reality, layer, or transition space.'],
  ['temporal-entity','Temporal entity','A being with nonlinear time, duplicated states, loops, or chronology-based rules.'],
  ['cosmic-entity','Cosmic entity','A being operating at astronomical, metaphysical, or civilization-scale significance.'],
  ['reality-parasite','Reality parasite','A being sustained by consuming, rewriting, nesting in, or attaching to reality structures.'],
  ['impossible-organism','Impossible organism','A deliberately anomalous being whose exceptions must be explicitly governed.']
 ]},
 {id:'collective',name:'Collectives and swarms',icon:'⁙',help:'Many bodies, nodes, minds, or units represented through a governed collective identity.',types:[
  ['animal-swarm','Animal swarm','Many small biological creatures acting as one encounter entity.'],
  ['insect-swarm','Insect / arthropod swarm','Colonial, hive, nest, or massed arthropod life.'],
  ['spore-colony','Spore / fungal colony','Distributed fungal, microbial, or infectious collective.'],
  ['nanite-swarm','Nanite swarm','Distributed synthetic units operating as a fluid collective.'],
  ['spirit-swarm','Spirit swarm','Many spirits, memories, echoes, or fragments acting together.'],
  ['hive-mind','Hive mind','Multiple bodies linked by a shared or coordinating consciousness.'],
  ['distributed-person','Distributed person','One identity instantiated across multiple bodies, devices, or locations.'],
  ['mixed-swarm','Mixed swarm','A governed collective containing more than one creature or unit kind.']
 ]},
 {id:'play-role',name:'Play-role foundations',icon:'⚑',help:'Start from how the creature is used, then choose or create its underlying taxonomy.',types:[
  ['companion','Companion','A persistent allied creature with ownership, permission, advancement, and relationship considerations.'],
  ['familiar','Familiar','A bonded helper connected to an ability, ritual, character, or supernatural relationship.'],
  ['summon','Summoned creature','A creature brought into play through an ability, condition, contract, or state change.'],
  ['mount','Mount','A creature used for movement, carrying, access, or shared operation.'],
  ['minion','Minion','A low-complexity encounter role; this is a rules profile, not a biological taxonomy.'],
  ['elite','Elite creature','A strengthened encounter presentation retaining its base identity.'],
  ['boss','Boss creature','A major encounter presentation with phases, reactions, objectives, and scene impact.'],
  ['social-npc','Social NPC','A reusable social-role archetype grounded in species or creature foundations.'],
  ['faction-agent','Faction agent','An archetype defined by faction role, knowledge, loadout, and permissions.'],
  ['hazard-creature','Creature hazard','A creature whose main play function overlaps traps, environments, or persistent hazards.']
 ]}
];
const PROFILES=[
 ['minion','Minion','Low handling cost; simple actions and limited state.'],['support','Support','Enables allies, restores resources, grants positioning or information.'],['skirmisher','Skirmisher','Mobility, target selection, and hit-and-run behavior.'],['controller','Controller','Zones, forced movement, conditions, denial, or scene shaping.'],['defender','Defender','Protection, interception, durability, and threat management.'],['striker','Striker','Focused harm, pursuit, exploitation, and finishing pressure.'],['specialist','Specialist','Investigation, social, environmental, technical, or unusual scenario role.'],['elite','Elite','A more complex or resilient encounter layer over a base identity.'],['boss','Boss','Major encounter role with phases, reactions, objectives, or environmental effects.'],['noncombatant','Noncombatant','Primarily social, narrative, logistical, or environmental presence.']
];
let previousStart=null,selection=null,baseline=0;
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function js(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'")}
function init(){if(!window.ForgeV2||window.ForgeV2.__creaturesV8)return;previousStart=window.ForgeV2.start.bind(window.ForgeV2);window.ForgeV2.start=function(type){if(type==='creatures')return openLayer();return previousStart(type)};window.ForgeV2.__creaturesV8=true;enhanceLibrary();}
function overlay(inner){document.querySelector('#creature8')?.remove();document.body.insertAdjacentHTML('beforeend',`<div id="creature8" class="creature8-overlay"><section class="creature8-screen">${inner}</section></div>`)}
function close(){document.querySelector('#creature8')?.remove()}
function header(back,title,kicker='Creature Forge'){return `<header>${back?`<button onclick="${back}">←</button>`:'<span></span>'}<div><small>${esc(kicker)}</small><h2>${esc(title)}</h2></div><button onclick="CreatureForge8.close()">✕</button></header>`}
function openLayer(){selection={};overlay(`${header('', 'What are you creating?')}<main><p class="creature8-lead">Choose the record layer first. This prevents a species, reusable creature, template, variant, and campaign individual from being accidentally treated as the same kind of object.</p><div class="creature8-cards">${LAYERS.map(x=>`<button onclick="CreatureForge8.layer('${x.id}')"><i>${x.icon}</i><span><b>${esc(x.name)}</b><small>${esc(x.help)}</small></span><em>›</em></button>`).join('')}</div></main>`)}
function layer(id){selection.layer=LAYERS.find(x=>x.id===id);openFamilies()}
function openFamilies(){overlay(`${header('CreatureForge8.openLayer()', 'Choose a creature family', selection.layer.name)}<main><div class="creature8-rule"><b>Multiversal rule distinction</b><span>Taxonomy describes what the creature is. Encounter role describes how it is presented. A template or variant changes a base Definition without erasing that identity.</span></div><div class="creature8-cards">${FAMILIES.map(g=>`<button onclick="CreatureForge8.family('${g.id}')"><i>${g.icon}</i><span><b>${esc(g.name)}</b><small>${esc(g.help)}</small></span><em>›</em></button>`).join('')}</div></main>`)}
function family(id){selection.family=FAMILIES.find(x=>x.id===id);openTypes()}
function openTypes(){const g=selection.family;overlay(`${header('CreatureForge8.openFamilies()', 'Choose the closest creature type', g.name)}<main><p class="creature8-lead">This is a starting taxonomy, not a cage. Hybrid and setting-specific creatures can retain multiple tags, but one primary type keeps validation and search reliable.</p><div class="creature8-types">${g.types.map(t=>`<button onclick="CreatureForge8.type('${t[0]}')"><b>${esc(t[1])}</b><small>${esc(t[2])}</small></button>`).join('')}</div></main>`)}
function type(id){const t=selection.family.types.find(x=>x[0]===id);selection.type={id,name:t[1],help:t[2]};openFoundation()}
function openFoundation(){const needsBase=['variant','template','form','archetype','instance'].includes(selection.layer.id);overlay(`${header('CreatureForge8.openTypes()', 'Connect the foundation', selection.type.name)}<main><div class="creature8-summary"><b>${esc(selection.layer.name)} · ${esc(selection.family.name)} · ${esc(selection.type.name)}</b><span>${esc(selection.type.help)}</span></div><label class="creature8-field"><span>${needsBase?'Base Definition ID':'Species or foundation ID (optional)'}</span><input id="c8base" placeholder="Example: creature.ember-wolf or species.human"><small>${needsBase?'Required for a governed '+selection.layer.name.toLowerCase()+'.':'Use an existing canonical Species or Creature Definition when applicable.'}</small></label><label class="creature8-field"><span>Secondary taxonomy tags</span><input id="c8tags" placeholder="Example: aquatic, spirit-touched, engineered"><small>Use these for hybrid identity without replacing the primary type.</small></label><div class="creature8-actions"><button onclick="CreatureForge8.openTypes()">Back</button><button class="primary" onclick="CreatureForge8.profile()">Continue</button></div></main>`)}
function profile(){selection.baseId=document.querySelector('#c8base')?.value.trim()||'';selection.secondary=(document.querySelector('#c8tags')?.value||'').split(',').map(x=>x.trim()).filter(Boolean);if(['variant','template','form','archetype'].includes(selection.layer.id)&&!selection.baseId){alert('Choose or enter the base Definition ID so this layer preserves its identity.');return}overlay(`${header('CreatureForge8.openFoundation()', 'Choose the encounter presentation', 'Rules profile')}<main><p class="creature8-lead">This choice affects handling and validation, not biological taxonomy. It can be changed or omitted later.</p><div class="creature8-types">${PROFILES.map(p=>`<button onclick="CreatureForge8.finish('${p[0]}')"><b>${esc(p[1])}</b><small>${esc(p[2])}</small></button>`).join('')}<button onclick="CreatureForge8.finish('unspecified')"><b>Decide during interview</b><small>Keep the encounter role open while defining identity and ecology.</small></button></div></main>`)}
function finish(pid){selection.profile=PROFILES.find(x=>x[0]===pid)||['unspecified','Unspecified',''];selection.createdAt=new Date().toISOString();baseline=(window.state?.gameObjects||[]).length;localStorage.setItem('aioc-creature-forge-v8-current',JSON.stringify(selection));close();previousStart('creatures');setTimeout(prefill,80);watchSave()}
function prefill(){const box=document.querySelector('#forge6Concept');if(!box)return;const s=selection;const base=s.baseId?` It is based on ${s.baseId}.`:'';box.value=`Create a Multiversal ${s.layer.name} classified primarily as ${s.family.name} → ${s.type.name}.${base} Encounter presentation: ${s.profile[1]}. Preserve the distinction between taxonomy, species foundation, archetype/template/variant layer, and individual state. Define ecology or origin, scale, biology or embodiment, movement, senses, defenses, resources, canonical actions/traits/reactions, behavior guidance, habitats, forms or transformations, dependencies, and provenance. `;const card=document.createElement('section');card.className='creature8-selected';card.innerHTML=`<b>${esc(s.layer.name)} → ${esc(s.type.name)}</b><span>Profile: ${esc(s.profile[1])}${s.baseId?' · Base: '+esc(s.baseId):''}</span><button onclick="CreatureForge8.restart()">Change starting path</button>`;box.parentElement.insertBefore(card,box);box.focus()}
function watchSave(){let tries=0;const timer=setInterval(()=>{tries++;const objs=window.state?.gameObjects||[];if(objs.length>baseline){const o=[...objs].reverse().find(x=>x.type==='creatures'&&!x.multiversalClassification);if(o){applyMetadata(o);clearInterval(timer)}}if(tries>900)clearInterval(timer)},1000)}
function applyMetadata(o){const s=selection||JSON.parse(localStorage.getItem('aioc-creature-forge-v8-current')||'null');if(!s)return;o.recordLayer=s.layer.id;o.multiversalClassification={primaryFamily:s.family.id,primaryType:s.type.id,secondaryTags:s.secondary||[],speciesOrBaseDefinitionId:s.baseId||null,encounterProfile:s.profile[0],taxonomyAuthority:'author-selected',forgeVersion:BUILD};o.rulesConnections=o.rulesConnections||{actions:[],effects:[],conditions:[],resources:[],items:[],abilities:[],environments:[]};o.governance={...(o.governance||{}),preserveBaseIdentity:['variant','template','form','archetype','instance'].includes(s.layer.id),statBlockIsProjection:true,behaviorGuidanceAdvisory:true,requiresProvenanceReview:true};o.validation=o.validation||{status:'review',errors:[],warnings:[]};const w=o.validation.warnings||(o.validation.warnings=[]);if(!o.rulesConnections.actions.length)w.push('No canonical Action references have been connected yet.');if(!o.rulesConnections.resources.length)w.push('Review whether the creature requires canonical Resource references.');if(['variant','template','form','archetype'].includes(s.layer.id)&&!s.baseId)w.push('This record layer requires an identified base Definition.');if(typeof window.save==='function')window.save();}
function enhanceLibrary(){const mo=new MutationObserver(()=>{document.querySelectorAll('.forge2-version').forEach(x=>{if(!x.dataset.c8){x.dataset.c8='1';x.textContent='FORGE 8.0 · SYSTEM-GROUNDED'}})});mo.observe(document.body,{childList:true,subtree:true})}
function restart(){document.querySelector('#forge6')?.remove();document.body.classList.remove('forge6-open');openLayer()}
setTimeout(init,0);setTimeout(init,250);setTimeout(init,1000);
window.CreatureForge8={openLayer,openFamilies,openTypes,openFoundation,layer,family,type,profile,finish,close,restart};
})();