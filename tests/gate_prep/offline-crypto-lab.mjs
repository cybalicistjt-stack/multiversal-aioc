// GATE-PREP-03 Node crypto LAB: not OS-bound keys or native/installed DRM.
import {randomBytes,createCipheriv,createDecipheriv,sign,verify,generateKeyPairSync} from "node:crypto";
export function makeLabSigner() {return generateKeyPairSync("ed25519");}
const encode=(obj)=>Buffer.from(JSON.stringify(obj)).toString("base64url");
export function issueLabLease(privateKey,claims) {
 if(!claims||typeof claims.subject!=="string"||!claims.device||!claims.purpose ||
    !Number.isSafeInteger(claims.issuedAt)||!Number.isSafeInteger(claims.expiresAt)||
    !Number.isSafeInteger(claims.paidThrough)||claims.expiresAt<=claims.issuedAt||
    claims.expiresAt>claims.paidThrough)throw Error("INVALID_FINITE_LEASE");
 const payload=encode({...claims,issuer:"multiversal-lab",audience:"offline-content-lab"});
 return {payload,signature:sign(null,Buffer.from(payload),privateKey).toString("base64url")};
}
export function verifyLabLease(publicKey,envelope,request){
 try{
  if(!verify(null,Buffer.from(envelope.payload),publicKey,Buffer.from(envelope.signature,"base64url"))) return {ok:false,reason:"BAD_SIGNATURE"};
  const c=JSON.parse(Buffer.from(envelope.payload,"base64url").toString("utf8"));
  if(c.issuer!=="multiversal-lab"||c.audience!=="offline-content-lab")return {ok:false,reason:"BAD_AUDIENCE"};
  if(request.locked||!request.unchangedSession)return {ok:false,reason:"ACCOUNT_LOCKED"};
  if(c.subject!==request.subject||c.device!==request.device)return {ok:false,reason:"WRONG_BINDING"};
  if(c.purpose!==request.purpose||c.scope!==request.scope)return {ok:false,reason:"WRONG_SCOPE"};
  if(c.campaign!==request.campaign||c.manifest!==request.manifest)return {ok:false,reason:"WRONG_MANIFEST"};
  if(request.knownEpoch>c.epoch)return {ok:false,reason:"KNOWN_REVOKED"};
  if(!Number.isSafeInteger(request.now)||request.now<c.issuedAt||request.now>=c.expiresAt||request.now>=c.paidThrough) return {ok:false,reason:"EXPIRED"};
  return {ok:true,claims:c};
 }catch{return {ok:false,reason:"MALFORMED"};}
}
export function sealLabCache(key,plain,binding){
 if(!Buffer.isBuffer(key)||key.length!==32)throw Error("LAB_KEY_MUST_BE_32_BYTES");
 const nonce=randomBytes(12),cipher=createCipheriv("aes-256-gcm",key,nonce);
 cipher.setAAD(Buffer.from(JSON.stringify(binding)));
 const body=Buffer.concat([cipher.update(Buffer.from(plain)),cipher.final()]);
 return {nonce:nonce.toString("base64url"),body:body.toString("base64url"),tag:cipher.getAuthTag().toString("base64url")};
}
export function openLabCache(key,packet,binding){
 const decipher=createDecipheriv("aes-256-gcm",key,Buffer.from(packet.nonce,"base64url"));
 decipher.setAAD(Buffer.from(JSON.stringify(binding)));
 decipher.setAuthTag(Buffer.from(packet.tag,"base64url"));
 return Buffer.concat([decipher.update(Buffer.from(packet.body,"base64url")),decipher.final()]);
}
// No API in this module can make authorization transferable between subjects.
export function mayTransfer(lineage,destination){
 if(!lineage||lineage.known!==true||lineage.restricted===true||lineage.nestedRestricted===true)return false;
 return lineage.owner===destination.subject&&destination.licensed===true;
}
