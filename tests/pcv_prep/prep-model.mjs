// PCV-PREP-02..07 isolated model code. No production A3/A5/A6/A7/A9/MIB13 import.
// All identities/rolls/events are synthetic: tests do not prove installed gameplay.
import {createHash} from "node:crypto";
export const digest=x=>createHash("sha256").update(JSON.stringify(x)).digest("hex");
const clone=x=>JSON.parse(JSON.stringify(x));
const positive=n=>Number.isSafeInteger(n)&&n>0;

export class SessionLab {
 constructor({campaign="prep-river-archive",gm="Raven1",player="Raven2"}={}) {
  this.s={campaign,gm,player,revision:0,sequence:0,phase:"exploration",members:{[gm]:"gm",[player]:"player"},
    hp:{[gm]:12,[player]:9,"guardian":8},stamina:{[gm]:4,[player]:4},
    pending:{},decisions:{},events:[],commandFingerprints:{}};
 }
 assertAuthorized(actor){if(!this.s.members[actor])throw Error("NOT_MEMBER");}
 append(kind,payload,visibility="all"){
  const e={sequence:++this.s.sequence,kind,visibility,payload:clone(payload)};
  this.s.events.push(e);this.s.revision++;return clone(e);
 }
 proposal(command){
  const {commandId,actor,kind,target,cost=0,expectedRevision}=command;
  this.assertAuthorized(actor);
  if(typeof commandId!=="string"||!commandId||!["strike","heal","inspect"].includes(kind)||
     !Number.isSafeInteger(cost)||cost<0)throw Error("INVALID_PROPOSAL");
  const fingerprint=digest({actor,kind,target,cost});
  if(this.s.commandFingerprints[commandId]){
   if(this.s.commandFingerprints[commandId]!==fingerprint)throw Error("COMMAND_CONFLICT");
   return clone(this.s.pending[commandId]??this.s.decisions[commandId]);
  }
  if(expectedRevision!==this.s.revision)throw Error("STALE_REVISION");
  if(this.s.stamina[actor]<cost)throw Error("NO_RESOURCE");
  this.s.commandFingerprints[commandId]=fingerprint;
  this.s.pending[commandId]={commandId,actor,kind,target,cost,sourceRevision:this.s.revision};
  this.append("proposal",{commandId,actor,kind},"gm");
  return clone(this.s.pending[commandId]);
 }
 adjudicate({commandId,gm,decision,roll=10}){
  if(gm!==this.s.gm||this.s.members[gm]!=="gm")throw Error("GM_ONLY");
  if(this.s.decisions[commandId]){
   if(this.s.decisions[commandId].decision!==decision)throw Error("DECISION_CONFLICT");
   return clone(this.s.decisions[commandId]);
  }
  const p=this.s.pending[commandId];if(!p)throw Error("UNKNOWN_PROPOSAL");
  if(!["approve","reject"].includes(decision)||!Number.isSafeInteger(roll)||roll<1||roll>20)throw Error("INVALID_DECISION");
  if(decision==="approve"){
   if(this.s.stamina[p.actor]<p.cost)throw Error("NO_RESOURCE");
   if(p.kind==="strike"&&!Object.hasOwn(this.s.hp,p.target))throw Error("BAD_TARGET");
   if(p.kind==="heal"&&!Object.hasOwn(this.s.hp,p.target))throw Error("BAD_TARGET");
   this.s.stamina[p.actor]-=p.cost;
   if(p.kind==="strike"&&roll>=10)this.s.hp[p.target]=Math.max(0,this.s.hp[p.target]-2);
   if(p.kind==="heal")this.s.hp[p.target]+=2;
  }
  const receipt={commandId,decision,actor:p.actor,kind:p.kind,target:p.target,
    rulesProfile:"synthetic-d20-prep",roll,gm};
  this.s.decisions[commandId]=receipt;delete this.s.pending[commandId];
  this.append("decision",receipt,p.kind==="inspect"?"gm":"all");return clone(receipt);
 }
 project(viewer){
  this.assertAuthorized(viewer);
  return {campaign:this.s.campaign,sequence:this.s.sequence,revision:this.s.revision,phase:this.s.phase,
    hp:clone(this.s.hp),events:this.s.events.map(e=>e.visibility==="all"||viewer===this.s.gm?clone(e):{sequence:e.sequence,kind:"withheld",visibility:"hidden"})};
 }
 checkpoint(){const state=clone(this.s);return {state,sha256:digest(state),grade:"SYNTHETIC_NOT_PCVA5"};}
 static restore(receipt){
  if(!receipt||receipt.grade!=="SYNTHETIC_NOT_PCVA5"||digest(receipt.state)!==receipt.sha256)throw Error("CHECKPOINT_TAMPER");
  const x=Object.create(SessionLab.prototype);x.s=clone(receipt.state);return x;
 }
 transition(step){
  const s=this.s;
  if(s.phase!==step.from||!["exploration","investigation","social","combat","downtime"].includes(step.kind))throw Error("BAD_TRANSITION");
  s.phase=step.to;return this.append("adventure-step",{id:step.id,kind:step.kind,event:step.event});
 }
}

const stakeForbidden=new Set(["real-money","subscription-token","premium-currency","gift-card","cash-redeemable","purchased-credit"]);
export class FictionalEconomyLab {
 constructor({gm="Raven1",player="Raven2"}={}) {
  this.wallet={campaign:{[gm]:100,[player]:100},free:{[gm]:100,[player]:100}};
  this.wagers=new Map();this.receipts=new Map();this.house=0;
 }
 balance(mode,actor){if(!["campaign","free"].includes(mode))throw Error("BAD_MODE");return this.wallet[mode][actor];}
 resetFree(actor){if(!Object.hasOwn(this.wallet.free,actor))throw Error("UNKNOWN_ACTOR");this.wallet.free[actor]=100;return this.balance("free",actor);}
 place({id,actor,mode,stake,market}){
  if(this.wagers.has(id)){
   const prior=this.wagers.get(id);
   if(digest(prior.input)!==digest({id,actor,mode,stake,market}))throw Error("REPLAY_CHANGED");
   return clone(prior);
  }
  if(!["campaign","free"].includes(mode)||!Object.hasOwn(this.wallet[mode],actor))throw Error("UNKNOWN_OWNER");
  if(!stake||stakeForbidden.has(stake.kind)||stake.realWorldValue===true||stake.redeemable===true||
      stake.purchased===true||!["fictional-credits","fictional-item-value"].includes(stake.kind))throw Error("REAL_WORLD_STAKE_DENIED");
  if(!positive(stake.amount)||typeof market!=="string"||!market)throw Error("INVALID_STAKE");
  if(this.wallet[mode][actor]<stake.amount)throw Error("INSUFFICIENT_ASSETS");
  this.wallet[mode][actor]-=stake.amount;
  const record={input:clone({id,actor,mode,stake,market}),status:"reserved"};
  this.wagers.set(id,record);return clone(record);
 }
 settle({id,result,ownerReceipt,regulator="off"}){
  if(this.receipts.has(id)){const p=this.receipts.get(id);
   if(p.result!==result||p.ownerReceiptId!==ownerReceipt?.id)throw Error("SETTLEMENT_CONFLICT");
   return clone(p);
  }
  const wager=this.wagers.get(id);if(!wager)throw Error("UNKNOWN_WAGER");
  if(!ownerReceipt||ownerReceipt.verifiedFixture!==true||!ownerReceipt.id||ownerReceipt.market!==wager.input.market)throw Error("NO_OWNER_RESULT_RECEIPT");
  if(!["win","lose","void"].includes(result)||!["off","light","custom","full"].includes(regulator))throw Error("BAD_OUTCOME");
  const {actor,mode,stake}=wager.input;
  const gross=result==="win"?2*stake.amount:result==="void"?stake.amount:0;
  // Test-only overlay; actual MRC tax settings are GM-authored and not determined here.
  const levy=regulator==="full"&&result==="win"?Math.floor(gross/10):0;
  this.wallet[mode][actor]+=gross-levy;this.house+=levy;
  const receipt={id,result,mode,ownerReceiptId:ownerReceipt.id,gross,levy,net:gross-levy};
  this.receipts.set(id,receipt);wager.status="settled";return clone(receipt);
 }
}

export function dependencyClosure(graph,root){
 const seen=new Set(),active=new Set();
 function dfs(id){
  if(active.has(id))throw Error("DEPENDENCY_CYCLE");
  if(seen.has(id))return;
  const n=graph[id];if(!n)throw Error("MISSING_DEPENDENCY");
  if(n.trusted!==true||n.licensed!==true)throw Error("UNTRUSTED_OR_UNLICENSED");
  active.add(id);for(const d of n.required||[])dfs(d);
  active.delete(id);seen.add(id);
 }
 dfs(root);return [...seen].sort();
}
export function canTransferDefinition(source,target){
 if(!source||!target||source.owner!==target.subject||!target.rightsVerified)return false;
 if(source.restricted===true||source.nestedRestricted===true||source.provenanceKnown!==true)return false;
 return true;
}
export function featureCensus(sample){
 const seen=new Set();
 return sample.map(x=>{
  if(seen.has(x.id))throw Error("DUPLICATE_FEATURE");seen.add(x.id);
  if(!x.path||!x.owner)return {...x,disposition:"unresolved"};
  if(x.productRouteEvidence===true&&x.ownerProof===true)return {...x,disposition:"candidate-integrated-needs-runtime"};
  return {...x,disposition:"source-observed-not-integrated"};
 });
}
export function auditParity(surfaces){
 const defects=[];
 for(const s of surfaces){
  const ph=[...new Set(s.phoneActions||[])].sort(),desk=[...new Set(s.desktopActions||[])].sort();
  if(JSON.stringify(ph)!==JSON.stringify(desk))defects.push(s.id+":ACTION_MISMATCH");
  if(s.focusVisible!==true||s.keyboardFallback!==true||s.screenReaderLabel!==true||s.touchTargetPx<44)
   defects.push(s.id+":ACCESSIBILITY");
  if(s.precisionDragOnly===true)defects.push(s.id+":DRAG_ONLY");
 }
 return {ok:defects.length===0,defects};
}
export function validateInstallerPreflight(candidate){
 if(!candidate||!["win","android"].includes(candidate.platform)||!candidate.sourceHead||
    !candidate.buildId||!candidate.sha256||!(/^[a-f0-9]{64}$/i.test(candidate.sha256)))
  return {ok:false,reason:"MISSING_PACKAGE_PROVENANCE"};
 return {ok:false,reason:"NOT_INSTALLED_VERIFICATION",preflightOnly:true};
}
export function syntheticGoldenRun(golden){
 if(golden.kind!=="SYNTHETIC_NONCANONICAL_ACCEPTANCE_FIXTURE")throw Error("CANONICALITY_NOT_PROVEN");
 const session=new SessionLab({campaign:golden.campaign,gm:golden.gm,player:golden.player});
 for(const step of golden.steps)session.transition(step);
 const before=session.checkpoint(),restored=SessionLab.restore(before);
 if(restored.s.sequence!==golden.steps.length||restored.s.phase!=="completed")throw Error("BROKEN_GOLDEN_REPLAY");
 return {status:"SIMULATED_ONLY",events:restored.s.events.length,checkpoint:before.sha256,phase:restored.s.phase};
}
