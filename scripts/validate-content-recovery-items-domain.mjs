import fs from "node:fs";
const contract=JSON.parse(fs.readFileSync("governance/content-recovery/domain-reviews/ITEMS_DOMAIN_CLASSIFICATION_CONTRACT.json","utf8"));
const fixture=JSON.parse(fs.readFileSync("governance/content-recovery/fixtures/ITEMS_DOMAIN_REVIEW_FIXTURE.json","utf8"));
const coverage=JSON.parse(fs.readFileSync("governance/content-recovery/pilots/PHASE2_ITEMS_DOMAIN_REVIEW_COVERAGE.json","utf8"));
const bySheet=new Map(contract.rules.map(r=>[r.sheet,r]));
const failures=[];
if(contract.format!=="multiversal-content-recovery-domain-classification-contract"||contract.domain!=="items-equipment-materials") failures.push("unsupported contract");
if(fixture.recordCount!==fixture.records.length) failures.push("fixture recordCount mismatch");
for(const record of fixture.records){
 const sheet=record.source.locator.split("!")[0];
 const rule=bySheet.get(sheet);
 if(!rule) failures.push(`${record.fixtureId}: missing rule`);
 else {
  const actual={ruleId:rule.id,recordClass:rule.recordClass,mappingState:rule.mappingState,confidence:rule.confidence};
  if(JSON.stringify(actual)!==JSON.stringify(record.expected)) failures.push(`${record.fixtureId}: ${JSON.stringify({expected:record.expected,actual})}`);
 }
 if(!record.payloadSha256||!record.source.archive||!record.source.member) failures.push(`${record.fixtureId}: missing provenance anchor`);
}
const ruleRows=contract.rules.reduce((n,r)=>n+r.rows,0);
const dispositionRows=Object.values(coverage.dispositions).reduce((a,b)=>a+b,0);
const coverageRuleRows=Object.values(coverage.rules).reduce((a,b)=>a+b,0);
if(ruleRows!==contract.sourceGroupRows||ruleRows!==coverage.reviewedRows) failures.push("reviewed row totals do not reconcile");
if(dispositionRows!==coverage.reviewedRows||coverageRuleRows!==coverage.reviewedRows) failures.push("coverage breakdown does not reconcile");
if(coverage.previousResolved+coverage.reviewedRows!==coverage.resolvedAfterReview) failures.push("resolved total does not reconcile");
if(coverage.resolvedAfterReview+coverage.remainingUnresolved!==coverage.ledgerRecords) failures.push("ledger total does not reconcile");
if(!coverage.boundary.includes("No production classified ledger is published")) failures.push("safety boundary missing");
if(failures.length){console.error(failures.join("\n"));process.exit(1)}
console.log(`Items domain fixture passed: ${fixture.recordCount} records; ${coverage.reviewedRows} rows reviewed; ${coverage.remainingUnresolved} remain unresolved.`);