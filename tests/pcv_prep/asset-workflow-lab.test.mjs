import test from "node:test";
import assert from "node:assert/strict";
import {AssetLab} from "./asset-workflow-lab.mjs";
const create=()=>{
 const x=new AssetLab();x.addAsset({id:"wood",owner:"Raven2",campaign:"C",quantity:10});
 x.addAsset({id:"ore",owner:"Raven2",campaign:"C",quantity:4,restricted:true,weight:2});
 return x;
};
test("PREP04 real-model owner checks, source version and one-time transfer",()=>{
 const x=create();
 assert.throws(()=>x.transfer({commandId:"t1",assetId:"wood",actor:"Raven2",to:"Raven1",campaign:"C",qty:10,expectedVersion:1}),/AUTHORIZED/);
 assert.throws(()=>x.transfer({commandId:"t1",assetId:"ore",actor:"Raven2",to:"Raven1",campaign:"C",qty:4,expectedVersion:1,fixtureOwnerProof:true}),/RESTRICTED/);
 const t=x.transfer({commandId:"t1",assetId:"wood",actor:"Raven2",to:"Raven1",campaign:"C",qty:10,expectedVersion:1,fixtureOwnerProof:true});
 assert.equal(t.to,"Raven1");assert.equal(x.transfer({commandId:"t1",assetId:"wood"}).to,"Raven1");
 assert.equal(x.assets.get("wood").version,2);
});
test("PREP04 crafting is atomic on invalid ingredients and inherits restricted lineage",()=>{
 const x=create();
 assert.throws(()=>x.craft({orderId:"c0",actor:"Raven2",campaign:"C",materials:[{id:"wood",qty:11}],outputId:"failed",outputQty:1,fixtureOwnerProof:true}),/INPUT_NOT_OWNED/);
 assert.equal(x.assets.get("wood").quantity,10);assert.equal(x.assets.has("failed"),false);
 const receipt=x.craft({orderId:"c1",actor:"Raven2",campaign:"C",materials:[{id:"wood",qty:2},{id:"ore",qty:1}],outputId:"tool",outputQty:1,fixtureOwnerProof:true});
 assert.equal(receipt.restricted,true);assert.equal(x.assets.get("tool").restricted,true);
 assert.equal(x.craft({orderId:"c1"}).outputId,"tool");assert.equal(x.assets.get("ore").quantity,3);
});
test("PREP04 vehicle cargo capacity and campaign ownership fail closed",()=>{
 const x=create();x.addVehicle({id:"wagon",owner:"Raven2",campaign:"C",capacity:5});
 assert.throws(()=>x.loadCargo({vehicleId:"wagon",assetId:"ore",actor:"Raven2",qty:3,campaign:"C",fixtureOwnerProof:true}),/CARGO_DENIED/);
 assert.equal(x.assets.get("ore").quantity,4);
 const r=x.loadCargo({vehicleId:"wagon",assetId:"ore",actor:"Raven2",qty:2,campaign:"C",fixtureOwnerProof:true});
 assert.equal(r.used,4);assert.equal(x.assets.get("ore").quantity,2);
 assert.throws(()=>x.loadCargo({vehicleId:"wagon",assetId:"wood",actor:"Raven2",qty:2,campaign:"C",fixtureOwnerProof:true}),/CARGO_DENIED/);
});
test("PREP04 base slot and wrong-Campaign protections",()=>{
 const x=create();x.addBase({id:"forge",owner:"Raven2",campaign:"C",slots:1});
 assert.throws(()=>x.assignBase({baseId:"forge",assetId:"wood",actor:"Raven2",campaign:"other",fixtureOwnerProof:true}),/BASE_DENIED/);
 assert.equal(x.assignBase({baseId:"forge",assetId:"wood",actor:"Raven2",campaign:"C",fixtureOwnerProof:true}).assetId,"wood");
 assert.throws(()=>x.assignBase({baseId:"forge",assetId:"ore",actor:"Raven2",campaign:"C",fixtureOwnerProof:true}),/BASE_DENIED/);
});
