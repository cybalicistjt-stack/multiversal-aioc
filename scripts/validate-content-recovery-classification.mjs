import fs from "node:fs";
const contract=JSON.parse(fs.readFileSync(process.argv[2]||"governance/content-recovery/CLASSIFICATION_CONTRACT.json","utf8"));
const fixturePaths=["governance/content-recovery/fixtures/MIXED_DOMAIN_FIXTURE.json","governance/content-recovery/fixtures/RULE_EXPANSION_FIXTURE.json"];
const coverage=JSON.parse(fs.readFileSync("governance/content-recovery/pilots/PHASE2_RULE_EXPANSION_COVERAGE.json","utf8"));
function classify(r){
 const t=(r.explicitObjectType||"").toLowerCase().trim();
 const p=r.source.member.toLowerCase();
 const locator=(r.source.locator||"").toLowerCase();
 const rid=(r.recoveryId||"").toLowerCase();
 const base=p.split("::").at(-1).split("/").at(-1);
 if(["relationship","connection-edge","progression_edge","binding"].some(x=>t.includes(x))) return ["relationship-or-edge","support-record","exact","explicit-edge"];
 if(base==="manifest.json") return ["manifest-or-governance-record","support-record","exact","manifest-path"];
 if(p.includes("/schemas/")||p.includes(".schema.json")) return ["technical-artifact","technical-excluded","exact","schema-path"];
 if(p.includes("/tests/")||p.includes("test-results")||p.includes("expected-import")) return ["balance-or-test-record","support-record","strong","test-path"];
 if(p.includes("/analysis/")||p.includes("balance-flags")||p.includes("balance-audit")) return ["balance-or-test-record","support-record","strong","balance-path"];
 if(["record_ownership_map","record-ownership-map","ownership_map","reference_map","reference-resolution","reference_resolution","source_unit_register","source-unit-register","embedded_mechanics_baseline","embedded mechanics"].some(x=>p.includes(x))) return ["reference-or-index","support-record","strong","mapping-or-register-path"];
 if(["master-index","/registry/","inventory.jsonl","object_index.csv","object-index.csv"].some(x=>p.includes(x))) return ["reference-or-index","support-record","strong","index-path"];
 if(p.includes("/reports/")||p.includes("report.json")||p.includes("report.csv")) return ["supporting-structured-record","support-record","strong","report-path"];
 if(p.includes("validation.json")||p.includes("handoff")) return ["manifest-or-governance-record","support-record","partial","validation-handoff"];
 if(t.startsWith("mv.object.")) return ["primary-game-asset-candidate","native-cos","exact","explicit-cos-primary"];
 if(t&&["definition","profile","node","object","template","archetype","trait","effect","action","condition","resource","species","creature","item","vehicle","spell"].some(x=>t.endsWith(x))) return ["primary-game-asset-candidate","cos-mapped","strong","explicit-domain-type"];
 if(["effects.jsonl","capability-node.jsonl","actions.jsonl","traits.jsonl","conditions.jsonl","creatures.jsonl","items.jsonl","species.jsonl","vehicles.jsonl"].some(x=>p.includes(x))) return ["primary-game-asset-candidate","partially-mapped","strong","canonical-member-path"];
 if(["canonical effects!","creature traits!","creature actions!","items!","species!","vehicles!","spells!"].some(x=>locator.includes(x))) return ["primary-game-asset-candidate","partially-mapped","strong","workbook-sheet"];
 if(rid.startsWith("mv.")&&!rid.startsWith("mv.relationship")&&!rid.startsWith("mv.edge")) return ["primary-game-asset-candidate","partially-mapped","partial","stable-id-namespace"];
 return ["unresolved","structured-raw","unresolved","fallback"];
}
let failures=[];let checked=0;
for(const path of fixturePaths){
 const fixture=JSON.parse(fs.readFileSync(path,"utf8"));
 if(fixture.recordCount!==fixture.records.length) failures.push({path,error:"recordCount mismatch"});
 for(const r of fixture.records){
  const [recordClass,mappingState,confidence,ruleId]=classify(r);const actual={recordClass,mappingState,confidence,ruleId};
  if(JSON.stringify(actual)!==JSON.stringify(r.expected)) failures.push({fixtureId:r.fixtureId,expected:r.expected,actual});
  if(!r.payloadSha256||!r.source?.member) failures.push({fixtureId:r.fixtureId,error:"payload anchor missing"});
  checked++;
 }
}
const classTotal=Object.values(coverage.classes).reduce((a,b)=>a+b,0);
const ruleTotal=Object.values(coverage.rules).reduce((a,b)=>a+b,0);
if(classTotal!==coverage.ledgerRecords||ruleTotal!==coverage.ledgerRecords) failures.push({error:"coverage totals do not reconcile"});
if(coverage.resolved+coverage.unresolved!==coverage.ledgerRecords) failures.push({error:"resolved totals do not reconcile"});
if(coverage.boundary.includes("production ledger is published")===false) failures.push({error:"coverage safety boundary missing"});
if(contract.format!=="multiversal-deterministic-classification-contract"||contract.version!=="1.1.0") failures.push({error:"unsupported contract"});
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log(`Classification fixtures passed: ${checked} records. Coverage reconciles: ${coverage.resolved}/${coverage.ledgerRecords} resolved.`);