import fs from "node:fs";
const extension=JSON.parse(fs.readFileSync("governance/content-recovery/CLASSIFICATION_CONTRACT_1_3_EXTENSION.json","utf8"));
const fixture=JSON.parse(fs.readFileSync("governance/content-recovery/fixtures/RULE_EXPANSION_3_FIXTURE.json","utf8"));
const coverage=JSON.parse(fs.readFileSync("governance/content-recovery/pilots/PHASE2_RULE_EXPANSION_3_COVERAGE.json","utf8"));
function classify(r){
 const p=r.source.member.toLowerCase();
 const base=p.split("::").at(-1).split("/").at(-1);
 const locator=(r.source.locator||"").toLowerCase();
 if(["dependency-map","dependency_map","dependencies-map","dependencies_map"].some(x=>base.includes(x))) return ["relationship-or-edge","support-record","strong","dependency-map-member"];
 if(["runtime schemas!","release matrix!","pack assembly!","dependency closure!","install order!","uninstall order!","validation matrix!","governance!","runtime!","schemas!"].some(x=>locator.startsWith(x))) return ["reference-or-index","support-record","strong","governance-runtime-sheet"];
 if(["inventory","register","catalog","scores","score","cost-map","cost_map","matrix","coverage"].some(x=>base.includes(x))) return ["reference-or-index","support-record","strong","inventory-register-catalog-member"];
 return ["unresolved","structured-raw","unresolved","fallback"];
}
const failures=[];
if(extension.version!=="1.3.0"||extension.baseVersion!=="1.2.0") failures.push({error:"unsupported extension version"});
if(fixture.recordCount!==fixture.records.length) failures.push({error:"fixture count mismatch"});
for(const r of fixture.records){const [recordClass,mappingState,confidence,ruleId]=classify(r);const actual={recordClass,mappingState,confidence,ruleId};if(JSON.stringify(actual)!==JSON.stringify(r.expected)) failures.push({fixtureId:r.fixtureId,expected:r.expected,actual});if(!r.payloadSha256||!r.source?.member) failures.push({fixtureId:r.fixtureId,error:"payload anchor missing"});}
if(coverage.previousResolved+coverage.newlyResolved!==coverage.resolved) failures.push({error:"coverage increment mismatch"});
if(coverage.resolved+coverage.unresolved!==coverage.ledgerRecords) failures.push({error:"coverage total mismatch"});
if(Object.values(coverage.newRules).reduce((a,b)=>a+b,0)!==coverage.newlyResolved) failures.push({error:"new rule total mismatch"});
if(!coverage.boundary.includes("No production classified ledger")) failures.push({error:"safety boundary missing"});
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exit(1)}
console.log(`Rule expansion 1.3 passed: ${fixture.recordCount} anchored records; ${coverage.resolved}/${coverage.ledgerRecords} resolved.`);
