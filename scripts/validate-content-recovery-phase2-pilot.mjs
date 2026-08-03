import fs from "node:fs";

const pilot=JSON.parse(fs.readFileSync("governance/content-recovery/pilots/PHASE2_PILOT_INPUT.json","utf8"));
const report=JSON.parse(fs.readFileSync("governance/content-recovery/pilots/PHASE2_DRY_RUN_REPORT.json","utf8"));

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

const failures=[];
if(pilot.recordCount!==pilot.records.length) failures.push("pilot recordCount mismatch");
if(pilot.records.length<20) failures.push("pilot is too small");
for(const r of pilot.records){
 const [recordClass,mappingState,confidence,ruleId]=classify(r);
 const actual={recordClass,mappingState,confidence,ruleId};
 if(JSON.stringify(actual)!==JSON.stringify(r.expected)) failures.push({id:r.id,expected:r.expected,actual});
 if(!r.recoveryId||!r.payloadSha256||!r.source?.archive||!r.source?.member) failures.push({id:r.id,error:"missing recovery anchor"});
}
const total=Object.values(report.classificationCounts).reduce((a,b)=>a+b,0);
if(total!==report.ledgerRecordCount) failures.push(`dry-run counts sum to ${total}, expected ${report.ledgerRecordCount}`);
if(report.resolvedCount+report.unresolvedCount!==report.ledgerRecordCount) failures.push("resolved/unresolved totals mismatch");
if(report.unresolvedPercent<80) failures.push("pilot no longer represents the documented unresolved gap");
if(!String(report.decision).includes("Do not treat")) failures.push("safety decision missing");
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log(`Phase 2 pilot passed: ${pilot.records.length} anchored unresolved examples; ${report.unresolvedPercent}% full-ledger fallback rate documented.`);