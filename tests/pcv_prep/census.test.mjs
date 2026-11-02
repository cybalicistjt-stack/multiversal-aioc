import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
const root=new URL("../../governance/application-planning/product-convergence/prep/",import.meta.url);
const census=JSON.parse(readFileSync(new URL("APP_SOURCE_CENSUS.json",root),"utf8"));
const selected=JSON.parse(readFileSync(new URL("SOURCE_CROSSWALK.json",root),"utf8"));
const prep=JSON.parse(readFileSync(new URL("PCV_PREP_BACKLOG.json",root),"utf8"));
test("PREP01 source census has full scoped tree, immutable blob digests, and no duplicate paths",()=>{
 assert.equal(census.git_tree_truncated,false);
 assert.equal(census.files,census.client_source+census.contract_source);
 assert.ok(census.files>=2000);
 assert.equal(census.records.length,census.files);
 assert.equal(new Set(census.records.map(x=>x.path)).size,census.files);
 assert.ok(census.records.every(x=>/^[a-f0-9]{40}$/.test(x.sha)));
 assert.ok(census.records.every(x=>x.path.startsWith("apps/client-ui/src/")||x.path.startsWith("packages/contracts/src/")));
});
test("PREP01 selected citations are in census and any pinned blob matches",()=>{
 const index=new Map(census.records.map(x=>[x.path,x.sha]));
 for(const item of selected.sources){
  assert.ok(index.has(item.path),item.path);
  if(item.sha)assert.equal(index.get(item.path),item.sha,item.id);
  assert.ok(item.risk&&item.owner);
 }
 assert.equal(selected.audited_app_main,census.source_commit);
});
test("PREP01 raw path evidence is never mislabelled integrated",()=>{
 assert.ok(census.records.every(x=>!Object.hasOwn(x,"status")&&!Object.hasOwn(x,"integrated")));
 assert.ok(prep.modules.length===7);
 assert.ok(prep.modules.every(x=>x.status==="candidate"));
 assert.ok(prep.strict_boundaries.some(x=>x.includes("PCV04")));
});
