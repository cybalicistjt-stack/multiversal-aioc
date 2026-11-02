import test from "node:test";
import assert from "node:assert/strict";
import {randomBytes} from "node:crypto";
import {makeLabSigner,issueLabLease,verifyLabLease,sealLabCache,openLabCache,mayTransfer} from "./offline-crypto-lab.mjs";
const keyPair=makeLabSigner();
const claims={subject:"Raven1",device:"win-01",purpose:"campaign-runtime",scope:"root-A",campaign:"C-1",manifest:"msha",epoch:2,issuedAt:1000,expiresAt:2000,paidThrough:2500};
const request={subject:"Raven1",device:"win-01",purpose:"campaign-runtime",scope:"root-A",campaign:"C-1",manifest:"msha",knownEpoch:2,now:1500,locked:false,unchangedSession:true};
test("real Ed25519 signatures bind a finite lease to subject device scope and campaign",()=>{
 const lease=issueLabLease(keyPair.privateKey,claims);
 assert.equal(verifyLabLease(keyPair.publicKey,lease,request).ok,true);
 for(const changes of [{subject:"Raven2"},{device:"android-01"},{scope:"root-B"},{campaign:"C-2"},{manifest:"other"},{now:2000},{knownEpoch:3},{locked:true},{unchangedSession:false},{purpose:"character-view"}]){
  assert.equal(verifyLabLease(keyPair.publicKey,lease,{...request,...changes}).ok,false);
 }
 assert.equal(verifyLabLease(keyPair.publicKey,{...lease,signature:"bad"},request).ok,false);
 assert.throws(()=>issueLabLease(keyPair.privateKey,{...claims,expiresAt:2600}),/FINITE/);
});
test("actual AES-GCM authenticated binding forbids wrong account/manifest and wrong key",()=>{
 const key=randomBytes(32),binding={subject:"Raven1",device:"win-01",purpose:"campaign-runtime",manifest:"msha"};
 const packet=sealLabCache(key,"restricted payload",binding);
 assert.equal(openLabCache(key,packet,binding).toString(),"restricted payload");
 assert.throws(()=>openLabCache(key,packet,{...binding,subject:"Raven2"}));
 assert.throws(()=>openLabCache(randomBytes(32),packet,binding));
 assert.throws(()=>openLabCache(key,{...packet,tag:"bad"},binding));
});
test("restricted lineage remains unexportable even for a personal subscriber",()=>{
 assert.equal(mayTransfer({known:true,restricted:true,nestedRestricted:false,owner:"Raven1"},{subject:"Raven1",licensed:true}),false);
 assert.equal(mayTransfer({known:true,restricted:false,nestedRestricted:true,owner:"Raven1"},{subject:"Raven1",licensed:true}),false);
 assert.equal(mayTransfer({known:false},{subject:"Raven1",licensed:true}),false);
 assert.equal(mayTransfer({known:true,restricted:false,nestedRestricted:false,owner:"Raven1"},{subject:"Raven1",licensed:true}),true);
});
