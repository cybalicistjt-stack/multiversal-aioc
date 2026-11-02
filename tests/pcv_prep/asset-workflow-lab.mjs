// PCV-PREP04 synthetic owner-domain transaction fixture; NOT MIB13/A8 runtime.
const copy=x=>JSON.parse(JSON.stringify(x));
const validQty=n=>Number.isSafeInteger(n)&&n>0;
export class AssetLab {
 constructor(){this.assets=new Map();this.orders=new Map();this.orderFingerprints=new Map();this.vehicles=new Map();this.bases=new Map();this.commands=new Map();}
 addAsset({id,owner,campaign,quantity,weight=1,restricted=false,originKnown=true}){
  if(!id||!owner||!campaign||!validQty(quantity)||!validQty(weight)||this.assets.has(id))throw Error("BAD_ASSET");
  this.assets.set(id,{id,owner,campaign,quantity,weight,restricted,originKnown,version:1});
 }
 addVehicle({id,owner,campaign,capacity}){
  if(!id||!owner||!campaign||!validQty(capacity)||this.vehicles.has(id))throw Error("BAD_VEHICLE");
  this.vehicles.set(id,{id,owner,campaign,capacity,used:0,cargo:{}});
 }
 addBase({id,owner,campaign,slots}){
  if(!id||!owner||!campaign||!validQty(slots)||this.bases.has(id))throw Error("BAD_BASE");
  this.bases.set(id,{id,owner,campaign,slots,assigned:[]});
 }
 transfer({commandId,assetId,actor,to,campaign,qty,expectedVersion,fixtureOwnerProof=false,explicitGmTransfer=false}){
  const fingerprint=JSON.stringify({assetId,actor,to,campaign,qty,expectedVersion,fixtureOwnerProof,explicitGmTransfer});
  if(this.commands.has(commandId)){
   const seen=this.commands.get(commandId);if(seen.fingerprint!==fingerprint)throw Error("TRANSFER_ID_CONFLICT");
   return copy(seen.receipt);
  }
  const a=this.assets.get(assetId);
  if(!a||a.owner!==actor||!fixtureOwnerProof||a.campaign!==campaign||!validQty(qty)||qty>a.quantity||a.version!==expectedVersion)throw Error("TRANSFER_NOT_AUTHORIZED");
  if(a.restricted===true||a.originKnown!==true){
   if(to!==actor||!explicitGmTransfer)throw Error("RESTRICTED_TRANSFER");
  }
  if(typeof to!=="string"||!to)throw Error("BAD_DESTINATION");
  const receipt={commandId,assetId,actor,to,qty,version:a.version+1,fixtureOnly:true};
  if(to!==actor){
   if(qty!==a.quantity)throw Error("SPLIT_REQUIRES_OWNER_DOMAIN");
   a.owner=to;
  }
  a.version++;this.commands.set(commandId,{fingerprint,receipt});return copy(receipt);
 }
 craft({orderId,actor,campaign,materials,outputId,outputQty,fixtureOwnerProof=false}){
  const fingerprint=JSON.stringify({actor,campaign,materials,outputId,outputQty,fixtureOwnerProof});
  if(this.orders.has(orderId)){
   if(this.orderFingerprints.get(orderId)!==fingerprint)throw Error("CRAFT_ID_CONFLICT");
   return copy(this.orders.get(orderId));
  }
  if(!fixtureOwnerProof||!Array.isArray(materials)||!materials.length||!validQty(outputQty)||!outputId||this.assets.has(outputId))throw Error("CRAFT_NOT_AUTHORIZED");
  const required=new Map();
  for(const m of materials){if(!validQty(m.qty))throw Error("INVALID_MATERIAL");required.set(m.id,(required.get(m.id)||0)+m.qty);}
  const checked=[...required].map(([id,qty])=>({asset:this.assets.get(id),qty}));
  if(checked.some(({asset,qty})=>!asset||asset.owner!==actor||asset.campaign!==campaign||asset.quantity<qty||asset.originKnown!==true))throw Error("CRAFT_INPUT_NOT_OWNED");
  for(const {asset,qty} of checked){asset.quantity-=qty;asset.version++;}
  const inheritsRestricted=checked.some(x=>x.asset.restricted);
  const produced={id:outputId,owner:actor,campaign,quantity:outputQty,weight:1,restricted:inheritsRestricted,originKnown:true,version:1};
  this.assets.set(outputId,produced);
  const receipt={orderId,actor,campaign,outputId,restricted:inheritsRestricted,inputs:materials,fixtureOnly:true};
  this.orders.set(orderId,receipt);this.orderFingerprints.set(orderId,fingerprint);return copy(receipt);
 }
 loadCargo({vehicleId,assetId,actor,qty,campaign,fixtureOwnerProof=false}){
  const v=this.vehicles.get(vehicleId),a=this.assets.get(assetId);
  if(!v||!a||!fixtureOwnerProof||v.owner!==actor||a.owner!==actor||v.campaign!==campaign||a.campaign!==campaign||!validQty(qty)||a.quantity<qty||v.used+a.weight*qty>v.capacity)throw Error("CARGO_DENIED");
  a.quantity-=qty;a.version++;v.used+=a.weight*qty;v.cargo[assetId]=(v.cargo[assetId]||0)+qty;
  return {vehicleId,assetId,qty,used:v.used,capacity:v.capacity,fixtureOnly:true};
 }
 assignBase({baseId,assetId,actor,campaign,fixtureOwnerProof=false}){
  const b=this.bases.get(baseId),a=this.assets.get(assetId);
  if(!fixtureOwnerProof||!b||!a||b.owner!==actor||a.owner!==actor||b.campaign!==campaign||a.campaign!==campaign||b.assigned.length>=b.slots||b.assigned.includes(assetId))throw Error("BASE_DENIED");
  b.assigned.push(assetId);return {baseId,assetId,fixtureOnly:true};
 }
}
