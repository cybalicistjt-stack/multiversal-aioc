// PCV-PREP07 scripted synthetic two-person acceptance. No real transport, login or install.
import {SessionLab,FictionalEconomyLab,digest} from "./prep-model.mjs";
export function twoHumanFixtureRun(golden,{gm=golden.gm,player=golden.player}={}){
 if(golden.kind!=="SYNTHETIC_NONCANONICAL_ACCEPTANCE_FIXTURE"||gm===player||!Array.isArray(golden.steps))
  throw Error("NOT_TWO_DISTINCT_FIXTURE_ACTORS");
 let s=new SessionLab({campaign:golden.campaign,gm,player,initialPhase:"start"});
 const accessDenied=[];
 try{s.proposal({commandId:"spoof",actor:"uninvited",kind:"strike",target:"guardian",cost:1,expectedRevision:s.s.revision});}
 catch(e){accessDenied.push(e.message);}
 let resumeCount=0,checkpointDigest=null;
 for(const step of golden.steps){
  if(step.kind==="combat"){
   const cmd={commandId:"golden-hit",actor:player,kind:"strike",target:"guardian",cost:1,expectedRevision:s.s.revision};
   s.proposal(cmd);
   try{s.adjudicate({commandId:"golden-hit",gm:player,decision:"approve",roll:15});}
   catch(e){accessDenied.push(e.message);}
   s.adjudicate({commandId:"golden-hit",gm,decision:"approve",roll:15});
   const before=s.checkpoint();checkpointDigest=before.sha256;
   s=SessionLab.restore(before);resumeCount++;
   // Duplicate after resume cannot apply damage again.
   s.adjudicate({commandId:"golden-hit",gm,decision:"approve",roll:15});
  }
  s.transition(step);
 }
 const publicProjection=s.project(player),privateProjection=s.project(gm);
 if(publicProjection.events.some(e=>e.visibility==="gm"&&e.kind!=="withheld"))throw Error("PRIVATE_LEAK");
 const e=new FictionalEconomyLab({gm,player});
 e.place({id:"campaign-race",actor:player,mode:"campaign",stake:{kind:"fictional-credits",amount:5},market:"fictional-race"});
 e.settle({id:"campaign-race",result:"win",ownerReceipt:{id:"synthetic-result",market:"fictional-race",verifiedFixture:true},regulator:"off"});
 const campaignBalance=e.balance("campaign",player);
 e.place({id:"free-table",actor:player,mode:"free",stake:{kind:"fictional-credits",amount:7},market:"fictional-table"});
 e.resetFree(player);
 return {grade:"SYNTHETIC_ONLY_NOT_INSTALLED",actors:[gm,player],sessionId:golden.session,
  state:s.s.phase,health:s.s.hp.guardian,sequence:s.s.sequence,checkpointDigest,
  finalDigest:digest(s.s),resumeCount,denials:accessDenied,
  gmEventCount:privateProjection.events.length,playerEventCount:publicProjection.events.length,
  campaignBalance,freeBalance:e.balance("free",player),
  actionReceipts:Object.keys(s.s.decisions).length,stepEvents:s.s.events.filter(x=>x.kind==="adventure-step").length};
}
