import fs from "node:fs";
const contract=JSON.parse(fs.readFileSync(process.argv[2]||"governance/content-recovery/CLASSIFICATION_CONTRACT.json","utf8"));
const fixture=JSON.parse(fs.readFileSync(process.argv[3]||"governance/content-recovery/fixtures/MIXED_DOMAIN_FIXTURE.json","utf8"));
function classify(r){
 const t=(r.explicitObjectType||"").toLowerCase();
 const p=r.source.member.toLowerCase();
 const base=p.split("::").at(-1).split("/").at(-1);
 if(["relationship","connection-edge","progression_edge","binding"].some(x=>t.includes(x))) return ["relationship-or-edge","support-record","exact","explicit-edge"];
 if(t.startsWith("mv.object.")) return ["primary-game-asset-candidate","native-cos","exact","explicit-cos-primary"];
 if(base==="manifest.json") return ["manifest-or-governance-record","support-record","exact","manifest-path"];
 if(p.includes("/schemas/")||p.includes(".schema.json")) return ["technical-artifact","technical-excluded","exact","schema-path"];
 if(p.includes("/tests/")||p.includes("test-results")||p.includes("expected-import")) return ["balance-or-test-record","support-record","strong","test-path"];
 if(p.includes("/analysis/")||p.includes("balance-flags")||p.includes("balance-audit")) return ["balance-or-test-record","support-record","strong","balance-path"];
 if(p.includes("master-index")||p.includes("/registry/")||p.includes("inventory.jsonl")) return ["reference-or-index","support-record","strong","index-path"];
 if(p.includes("/reports/")||p.includes("report.json")||p.includes("report.csv")) return ["supporting-structured-record","support-record","strong","report-path"];
 if(p.includes("validation.json")||p.includes("handoff")) return ["manifest-or-governance-record","support-record","partial","validation-handoff"];
 return ["unresolved","structured-raw","unresolved","fallback"];
}
let failures=[];
for(const r of fixture.records){
 const [recordClass,mappingState,confidence,ruleId]=classify(r);
 const actual={recordClass,mappingState,confidence,ruleId};
 if(JSON.stringify(actual)!==JSON.stringify(r.expected)) failures.push({fixtureId:r.fixtureId,expected:r.expected,actual});
 if(!r.payloadSha256||!r.source?.member) failures.push({fixtureId:r.fixtureId,error:"payload anchor missing"});
}
if(fixture.recordCount!==fixture.records.length) failures.push({error:"recordCount mismatch"});
if(contract.format!=="multiversal-deterministic-classification-contract") failures.push({error:"unsupported contract format"});
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log(`Classification fixture passed: ${fixture.records.length} records.`);