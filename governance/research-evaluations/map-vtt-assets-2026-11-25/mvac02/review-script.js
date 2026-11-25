// MVAC-02 design oracle only. No storage, auth, pack resolution or owner mutation.
function evaluate(o, overrides={}) {
 const c={actualRevision:o.nativeRevision,objectFound:true,packAvailable:true,actualPackVersion:o.packVersion,representationFound:true,unsupportedFeature:false,ownerResolved:true,requiresDistance:false,actualCoordinateSpace:o.coordinateSpace,finiteCoordinates:true,capabilityState:'allowed',action:'preview',byteState:'byte-present',redistribution:'allowed',audience:'gm',policyReceipt:true,expectedOwnerVersion:1,actualOwnerVersion:1,ownerReceipt:null,...overrides};
 const end=status=>({status,ownerMutationPerformed:false,runtimeAuthorizationProved:false});
 if(c.actualRevision!==o.nativeRevision)return end('stale-document');
 if(!c.objectFound)return end('missing-native-object');
 if(c.unsupportedFeature)return end('incompatible-schema');
 if(!c.packAvailable)return end('missing-pack');
 if(c.actualPackVersion!==o.packVersion)return end('incompatible-pack-version');
 if(!c.representationFound)return end('missing-representation');
 if(c.actualCoordinateSpace!==o.coordinateSpace)return end('incompatible-coordinate-space');
 if(!c.finiteCoordinates)return end('invalid-coordinate');
 if(c.requiresDistance&&!o.physicalCalibration)return end('uncalibrated');
 if(!c.ownerResolved)return end('unresolved-owner');
 if(o.visibility==='gm-only'&&c.audience==='player')return end('excluded-private');
 if(!c.policyReceipt)return end('blocked-policy');
 if(c.capabilityState!=='allowed')return end('blocked-rights');
 if(c.action==='export-original'&&c.redistribution!=='allowed')return end('blocked-redistribution');
 if(c.action==='export-original'&&c.byteState!=='byte-present')return end('missing-bytes');
 if(c.expectedOwnerVersion!==c.actualOwnerVersion)return end('stale-owner');
 if(c.ownerReceipt==='ambiguous')return end('query-operation-status');
 if(c.ownerReceipt==='accepted')return end('reuse-owner-receipt');
 return end('ready');
}
function mapRights(state){if(state==='allowed')return 'granted';if(state==='denied'||state==='revoked')return 'denied';return 'unknown';}
function mapCapability(cap){return cap==='redistribute'?'redistribution':cap;}

const data=JSON.parse(document.getElementById('data').textContent);const el=id=>document.getElementById(id);const stages=['create','save','prepare','play','export','recovery'];
function option(parent,value,label){const o=document.createElement('option');o.value=value;o.textContent=label;parent.append(o);}
for(const o of data.objects)option(el('object'),o.id,o.label);for(const s of stages)option(el('stage'),s,s[0].toUpperCase()+s.slice(1));for(const c of data.cases)option(el('case'),c.id,c.id);
el('object').value='door';el('stage').value='create';el('case').value='ready-door';
function render(){const o=data.objects.find(x=>x.id===el('object').value);const c=data.cases.find(x=>x.id===el('case').value);el('trace').textContent=o.stages[el('stage').value];el('owner').textContent=o.owner;el('source').textContent=JSON.stringify(o,null,2);const selected=data.objects.find(x=>x.id===c.objectId);const r=evaluate(selected,c.overrides);el('outcome').textContent=r.status;el('case-details').textContent=JSON.stringify({object:selected.label,input:c.overrides,expected:c.expected,observed:r.status,scope:'Design oracle only; no runtime authorization or owner mutation'},null,2);}
el('object').onchange=()=>{el('case').value=data.cases.find(c=>c.objectId===el('object').value).id;render();};el('stage').onchange=render;el('case').onchange=()=>{el('object').value=data.cases.find(c=>c.id===el('case').value).objectId;render();};render();