export function manifestScenario(id,manifest,pin){const base=structuredClone(manifest),p=structuredClone(pin);let packs=[base];
 if(id==='new-default'||id==='new-version-only'){const v2=structuredClone(base);v2.packVersion='1.1.0';const r=structuredClone(v2.representations[0]);r.representationId=r.representationId.replace(':1',':2');r.anchor.xRatio=.45;r.recipe.version='2';v2.representations.push(r);v2.assets[0].representationIds.push(r.representationId);v2.assets[0].defaultRepresentationId=r.representationId;packs=id==='new-default'?[base,v2]:[v2];}
 if(id==='mandatory-feature')base.requiredFeatures.push('unsupported-future-geometry-v99');
 if(id==='missing-dependency')base.dependencies.push({packId:'synthetic:terrain-dependency',packVersion:'1.0.0'});
 if(id==='altered-pin-metadata')base.representations[0].anchor.xRatio=.45;
 if(id==='missing-representation')p.representationId='missing:representation';
 if(id==='same-bytes-distinct-records'){const a=structuredClone(base.assets[0]),r=structuredClone(base.representations[0]);a.assetId='synthetic:alias:distinct-logical-resource';a.label='Synthetic alias — same bytes, separate rights reference';a.rightsReference={owner:'ARI',resourceId:'synthetic:independent-resource',licenseEvidenceId:'synthetic:separate-evidence',state:'reference-recorded'};r.assetId=a.assetId;r.representationId='synthetic:alias:representation';a.representationIds=[r.representationId];a.defaultRepresentationId=r.representationId;base.assets.push(a);base.representations.push(r);}
 return {packs,pin:p};}
export const SCENARIOS=[
 {id:'baseline',label:'Embedded pack 1.0.0',expected:'resolved'},
 {id:'new-default',label:'1.1.0 available — keep the 1.0.0 placement',expected:'resolved'},
 {id:'new-version-only',label:'Only 1.1.0 present — no silent upgrade',expected:'missing-pinned-pack'},
 {id:'same-bytes-distinct-records',label:'Two logical assets share one blob',expected:'resolved'},
 {id:'mandatory-feature',label:'Unknown mandatory feature',expected:'dependency-or-schema-failure'},
 {id:'missing-dependency',label:'Required dependency unavailable',expected:'dependency-or-schema-failure'},
 {id:'altered-pin-metadata',label:'Pinned anchor changed under same identity',expected:'incompatible-pinned-content'},
 {id:'missing-representation',label:'Pinned representation unavailable',expected:'missing-pinned-representation'}
];
