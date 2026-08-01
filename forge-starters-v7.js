(() => {
'use strict';
const ITEM_GROUPS=[
 {id:'weapons',name:'Weapons',icon:'⚔',help:'Tools whose primary rules purpose is attacking, threatening, restraining, or delivering an effect.',types:[
  ['melee-light','Light melee','Knives, daggers, batons, claws, small improvised weapons'],
  ['melee-one-hand','One-handed melee','Swords, axes, maces, clubs, powered hand weapons'],
  ['melee-two-hand','Two-handed melee','Great weapons, polearms, heavy striking weapons'],
  ['reach-polearm','Reach and polearms','Spears, staves, lances, whips, chain weapons'],
  ['unarmed-natural','Unarmed and natural','Gauntlets, martial enhancers, claws, bites, implanted weapons'],
  ['thrown','Thrown weapons','Javelins, knives, grenades, chakrams, returning weapons'],
  ['projectile-smallarm','Projectile small arms','Pistols, revolvers, compact launchers'],
  ['projectile-longarm','Projectile long arms','Rifles, carbines, shotguns, bows, crossbows'],
  ['projectile-heavy','Heavy projectile','Machine guns, cannons, siege and anti-materiel weapons'],
  ['energy-smallarm','Energy small arms','Beam, pulse, plasma, sonic, electrical, or magical sidearms'],
  ['energy-longarm','Energy long arms','Rifles and long-range directed-energy weapons'],
  ['energy-heavy','Heavy energy','Vehicle, emplacement, siege, or anti-armor energy weapons'],
  ['guided-launcher','Guided and launcher','Rockets, missiles, torpedoes, smart launchers'],
  ['area-deployable','Area and deployable','Mines, traps, grenades, bombs, persistent hazards'],
  ['exotic-transforming','Exotic and transforming','Morphing, dimensional, living, psychic, or rule-breaking weapons']
 ]},
 {id:'armor',name:'Armor and protection',icon:'⬡',help:'Worn, carried, projected, or installed protection.',types:[
  ['armor-light','Light armor','Flexible protection, concealed armor, reinforced clothing'],
  ['armor-medium','Medium armor','Balanced protection and mobility'],
  ['armor-heavy','Heavy armor','Maximum personal protection with mobility or skill costs'],
  ['armor-powered','Powered armor','Motorized, cybernetic, magical, or energy-assisted suits'],
  ['armor-environmental','Environmental suit','Vacuum, pressure, radiation, toxin, heat, cold, underwater'],
  ['shield-hand','Carried shield','Physical, magical, or technological hand shields'],
  ['shield-field','Field protection','Personal barriers, deflectors, wards, reactive screens'],
  ['protective-accessory','Protective accessory','Helmets, masks, bracers, charms, dampeners']
 ]},
 {id:'consumables',name:'Consumables',icon:'◒',help:'Items normally expended, depleted, or used in charges.',types:[
  ['potion-healing','Healing and recovery','Potions, injectors, medicine, repair gel, restorative food'],
  ['potion-enhancement','Enhancement','Temporary attribute, sense, movement, or resistance boosts'],
  ['potion-transformation','Transformation','Shape, scale, material, species, or state changes'],
  ['potion-antidote','Antidote and cleansing','Remove toxins, conditions, curses, radiation, corruption'],
  ['food-drink','Food and drink','Rations, cuisine, stimulants, culturally significant consumables'],
  ['ammo-charge','Ammunition and charges','Rounds, arrows, cells, fuel cartridges, spell charges'],
  ['single-use-device','Single-use device','Emergency tools, beacons, deployables, instant fabrication'],
  ['chemical-substance','Chemical or substance','Poisons, solvents, adhesives, industrial compounds']
 ]},
 {id:'technology',name:'Technology and devices',icon:'⌁',help:'Functional devices, systems, electronics, machines, and advanced tools.',types:[
  ['computer-communicator','Computing and communication','Computers, communicators, translators, networks, data storage'],
  ['sensor-scanner','Sensors and scanners','Detection, analysis, targeting, medical, forensic, dimensional'],
  ['medical-biotech','Medical and biotechnology','Diagnostics, surgery, regeneration, gene tools, life support'],
  ['robot-drone','Robots and drones','Companions, workers, scouts, combat drones, autonomous devices'],
  ['cybernetic-implant','Cybernetics and implants','Replacement parts, enhancements, neural devices, internal tools'],
  ['power-energy','Power and energy','Generators, batteries, reactors, converters, power cells'],
  ['fabrication-repair','Fabrication and repair','Toolkits, printers, forges, assemblers, repair systems'],
  ['stealth-security','Stealth and security','Locks, alarms, camouflage, countermeasures, intrusion tools'],
  ['transport-accessory','Transport equipment','Navigation, cargo, towing, survival, docking, vehicle modules'],
  ['dimensional-temporal','Dimensional and temporal','Portals, anchors, phase devices, time manipulation'],
  ['magitech','Magitech and hybrid','Technology whose operation includes magical or supernatural rules']
 ]},
 {id:'tools',name:'Tools and equipment',icon:'⌘',help:'Reusable gear used to perform tasks, travel, survive, create, or investigate.',types:[
  ['general-tool','General tool','Hand tools, kits, instruments, utility devices'],
  ['craft-profession','Craft and profession','Trade kits, laboratories, studios, ritual implements'],
  ['survival-exploration','Survival and exploration','Shelter, climbing, navigation, environmental gear'],
  ['investigation-forensic','Investigation and forensic','Evidence, analysis, surveillance, research tools'],
  ['social-performance','Social and performance','Disguises, instruments, presentation and influence tools'],
  ['container-storage','Containers and storage','Bags, vaults, dimensional storage, secure containers'],
  ['clothing-accessory','Clothing and accessories','Uniforms, jewelry, badges, culturally meaningful wearables']
 ]},
 {id:'special',name:'Special and narrative items',icon:'✦',help:'Objects defined by ownership, story, rarity, supernatural role, or economic function.',types:[
  ['artifact-relic','Artifact or relic','Unique, legendary, historical, divine, cursed, or reality-altering objects'],
  ['quest-key','Quest or key item','Evidence, keys, objectives, components, plot-critical objects'],
  ['currency-trade','Currency and trade good','Money, credit, barter, commodities, collectible value'],
  ['book-data','Book, record, or data','Manuals, maps, grimoires, recordings, software, memories'],
  ['companion-living','Living item or companion object','Symbiotes, intelligent objects, bonded organisms'],
  ['vehicle-part','Vehicle part or module','Engines, weapons, defenses, sensors, cabins, cargo systems'],
  ['building-installation','Installation or structure component','Doors, traps, generators, furniture, base systems']
 ]}
];
const VEHICLE_GROUPS=[
 {id:'ground',name:'Ground vehicles',icon:'▰',help:'Vehicles whose normal movement is across a surface.',types:[
  ['car-civilian','Civilian car','Personal cars, taxis, utility cars, luxury vehicles'],
  ['car-performance','Performance car','Racing, pursuit, sports, high-speed road vehicles'],
  ['truck-utility','Truck and utility','Cargo trucks, pickups, construction and service vehicles'],
  ['armored-ground','Armored ground vehicle','APCs, tanks, armored cars, siege vehicles'],
  ['motorcycle-cycle','Motorcycle and cycle','Motorcycles, bicycles, hoverbikes, small personal cycles'],
  ['tracked-crawler','Tracked and crawler','Tanks, tractors, exploration crawlers, mining vehicles'],
  ['hover-ground','Hover and antigravity','Skimmers, hovercraft used primarily over land'],
  ['train-rail','Rail and train','Locomotives, transit trains, armored trains, maglev'],
  ['animal-drawn','Animal-drawn','Carts, wagons, chariots, sleds']
 ]},
 {id:'water',name:'Water vehicles',icon:'≋',help:'Surface, underwater, and amphibious vessels.',types:[
  ['boat-small','Small boat','Canoes, skiffs, launches, personal watercraft'],
  ['ship-civilian','Civilian ship','Cargo, passenger, fishing, exploration, luxury vessels'],
  ['ship-warship','Warship','Patrol boats, destroyers, battleships, carriers'],
  ['submersible','Submersible','Submarines, bathyspheres, underwater habitats'],
  ['amphibious','Amphibious vehicle','Vehicles designed for both land and water'],
  ['living-aquatic','Living aquatic vessel','Biological, grown, summoned, or bonded watercraft']
 ]},
 {id:'air',name:'Air vehicles',icon:'△',help:'Atmospheric flight and lighter-than-air vehicles.',types:[
  ['aircraft-fixed','Fixed-wing aircraft','Planes, jets, gliders, bombers, transports'],
  ['aircraft-rotor','Rotorcraft','Helicopters, tilt-rotors, autogyros'],
  ['airship-lighter','Airship','Balloons, zeppelins, floating fortresses'],
  ['vtol-hover','VTOL and hover aircraft','Dropships, grav craft, ducted-fan vehicles'],
  ['personal-flight','Personal flight vehicle','Jetpacks, flight boards, small flyers'],
  ['living-aerial','Living aerial vessel','Flying creatures used as vehicles, grown ships, summoned craft']
 ]},
 {id:'space',name:'Spacecraft',icon:'◇',help:'Vehicles designed for orbital, interplanetary, interstellar, or deep-space operation.',types:[
  ['space-fighter','Fighter and interceptor','Small combat craft, pursuit, escort, strike fighters'],
  ['space-shuttle','Shuttle and lander','Surface-to-orbit, boarding, landing, short-range transfer'],
  ['space-freighter','Freighter and transport','Cargo, passengers, colony ships, logistics vessels'],
  ['space-explorer','Explorer and science vessel','Survey, research, diplomacy, long-range expedition'],
  ['space-corvette','Corvette and patrol','Small independent warship, customs, escort, patrol'],
  ['space-frigate','Frigate and destroyer','Fleet escort, anti-fighter, screening, multirole combat'],
  ['space-cruiser','Cruiser and battleship','Heavy independent or line combat vessels'],
  ['space-carrier','Carrier and tender','Deploys fighters, drones, mecha, or support craft'],
  ['space-station','Station and mobile base','Orbital stations, generation ships, mobile fortresses'],
  ['space-living','Living or grown spacecraft','Organic, symbiotic, summoned, or bioship designs'],
  ['space-dimensional','Dimensional spacecraft','World-hopping, planar, phase, or reality-transition craft']
 ]},
 {id:'mecha',name:'Mecha and walkers',icon:'♜',help:'Piloted, crewed, bonded, or autonomous walking machines and giant bodies.',types:[
  ['mecha-powered-suit','Powered suit','Human-scale or slightly larger wearable machines'],
  ['mecha-light','Light mecha','Fast scout, skirmisher, urban, reconnaissance frames'],
  ['mecha-medium','Medium mecha','General-purpose combat and utility frames'],
  ['mecha-heavy','Heavy mecha','Siege, artillery, assault, fortress-breaking frames'],
  ['mecha-colossal','Colossal mecha','Kaiju-scale, city-scale, super-robot, strategic frames'],
  ['walker-utility','Utility walker','Construction, cargo, mining, exploration, agriculture'],
  ['walker-war','Military walker','Bipedal or multipedal armored combat vehicles'],
  ['transforming-mecha','Transforming mecha','Changes between vehicle, humanoid, animal, or other modes'],
  ['combined-mecha','Combined or modular mecha','Multiple units join into a larger system'],
  ['living-mecha','Living or bonded mecha','Biological frames, spirits, symbiotes, summoned bodies']
 ]},
 {id:'personal',name:'Personal and special transport',icon:'➤',help:'Small-scale mobility devices, mounts, and unusual travel systems.',types:[
  ['mount-natural','Natural mount','Rideable animals and creatures'],
  ['mount-fantastic','Fantastic mount','Magical, undead, constructed, or alien mounts'],
  ['personal-board','Board and personal platform','Skateboards, hoverboards, surf devices, small platforms'],
  ['mobility-chair','Mobility and accessibility','Chairs, exoskeleton mobility, adaptive transport'],
  ['teleport-platform','Teleport and portal transport','Gate devices, teleport pods, transition platforms'],
  ['dimensional-vessel','Dimensional vessel','Craft whose main role is travel between worlds or realities'],
  ['time-vehicle','Temporal vehicle','Craft whose primary travel axis includes time'],
  ['living-vehicle','Living vehicle','Bonded organisms, grown transports, intelligent mounts']
 ]}
];
let originalStart=null,selected=null;
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function js(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'")}
function init(){if(!window.ForgeV2||window.ForgeV2.__starterV7)return;originalStart=window.ForgeV2.start.bind(window.ForgeV2);window.ForgeV2.start=function(type){if(type==='items'||type==='vehicles')return open(type);return originalStart(type)};window.ForgeV2.__starterV7=true}
function open(type){selected=null;renderGroups(type)}
function data(type){return type==='items'?ITEM_GROUPS:VEHICLE_GROUPS}
function renderGroups(type){const title=type==='items'?'What kind of item are you creating?':'What kind of vehicle are you creating?';document.body.insertAdjacentHTML('beforeend',`<div id="starter7" class="starter7-overlay"><section class="starter7-screen"><header><div><small>Multiversal guided starting point</small><h2>${title}</h2></div><button onclick="ForgeStarters7.close()">✕</button></header><main><p class="starter7-lead">Choose the closest starting family. This does not lock the design; it changes the interview questions and records a structured classification.</p><div class="starter7-groups">${data(type).map(g=>`<button onclick="ForgeStarters7.group('${type}','${g.id}')"><i>${g.icon}</i><span><b>${esc(g.name)}</b><small>${esc(g.help)}</small></span><em>›</em></button>`).join('')}</div><button class="starter7-blank" onclick="ForgeStarters7.blank('${type}')">Start without choosing a category</button></main></section></div>`)}
function group(type,id){const g=data(type).find(x=>x.id===id);document.querySelector('#starter7').innerHTML=`<section class="starter7-screen"><header><button onclick="ForgeStarters7.open('${type}')">←</button><div><small>${esc(g.name)}</small><h2>Choose a starting subtype</h2></div><button onclick="ForgeStarters7.close()">✕</button></header><main><p class="starter7-lead">Choose the closest subtype. You can combine, rename, or change it during the interview.</p><div class="starter7-types">${g.types.map(t=>`<button onclick="ForgeStarters7.choose('${type}','${g.id}','${t[0]}')"><b>${esc(t[1])}</b><small>${esc(t[2])}</small></button>`).join('')}</div></main></section>`}
function choose(type,gid,tid){const g=data(type).find(x=>x.id===gid),t=g.types.find(x=>x[0]===tid);selected={type,groupId:gid,groupName:g.name,subtypeId:tid,subtypeName:t[1],guidance:t[2]};close();originalStart(type);setTimeout(()=>prefill(selected),80)}
function prefill(s){const box=document.querySelector('#forge6Concept');if(!box)return;box.value=`Create a Multiversal ${s.type==='items'?'item':'vehicle'} in the ${s.groupName} family, subtype ${s.subtypeName}. Starting guidance: ${s.guidance}. `;box.focus();const key='aioc-forge-starter-v7-current';localStorage.setItem(key,JSON.stringify({...s,created:new Date().toISOString()}));const note=document.createElement('section');note.className='starter7-selected';note.innerHTML=`<b>Starting from: ${esc(s.groupName)} → ${esc(s.subtypeName)}</b><span>${esc(s.guidance)}</span><button onclick="ForgeStarters7.change('${s.type}')">Change starting type</button>`;box.parentElement.insertBefore(note,box)}
function blank(type){close();originalStart(type)}
function change(type){document.querySelector('#forge6')?.remove();document.body.classList.remove('forge6-open');open(type)}
function close(){document.querySelector('#starter7')?.remove()}
const mo=new MutationObserver(init);mo.observe(document.documentElement,{childList:true,subtree:true});setTimeout(init,100);
window.ForgeStarters7={open,group,choose,blank,change,close};
})();