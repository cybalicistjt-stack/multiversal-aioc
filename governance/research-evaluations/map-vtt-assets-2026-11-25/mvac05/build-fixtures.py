from pathlib import Path
import json,hashlib,copy
p=Path('work/mvac05/package');actions=['private-use','modify','session-delivery','flattened-map-export','raw-redistribution'];caps=['private-use','transform','campaign-use','export','redistribution','commercial-use'];digest=hashlib.sha256(b'MVAC05 synthetic bytes').hexdigest()
def resource(id,label,action_states,cap_states,**opts):
 r={'resourceId':id,'label':label,'resourceRevision':'1','mediaKind':'prop','visibility':'owner-policy','provenance':{'creator':'Synthetic Studio','source':'synthetic:source:'+id,'evidenceId':'synthetic:provenance:'+id,'purchaseReceipt':None,'importAccepted':True},'license':{'id':'synthetic-license:'+id,'revision':'1','state':'recorded','evidenceId':'synthetic:license:'+id,'sourceReference':'synthetic:terms:'+id,'textSHA256':hashlib.sha256(('synthetic terms '+id).encode()).hexdigest()},'capabilityEvidence':[{'evidenceId':'synthetic:cap:'+id+':'+c,'source':'synthetic-fixture','capability':c,'state':cap_states.get(c,'unknown')}for c in caps],'actionEvidence':[{'evidenceId':'synthetic:action:'+id+':'+a,'source':'synthetic-fixture','action':a,'state':action_states.get(a,'unknown'),'resourceRevision':'1','licenseRevision':'1','subjectId':'synthetic:owner','audiences':['self']if a in ['private-use','modify']else ['campaign']if a=='session-delivery'else ['public'],'campaignId':'synthetic:campaign'if a=='session-delivery'else None,'commercial':'any'if opts.get('commercial')else'noncommercial','validUntil':None}for a in actions],'attribution':{'state':'not-required','requiredFields':[],'values':{}},'bytes':{'state':'byte-present','sha256':digest,'byteLength':22},'parents':[],'actualLicenseClearance':False}
 return r
all_allow=dict.fromkeys(actions,'allowed');cap_allow=dict.fromkeys(caps,'allowed')
resources=[resource('private-art','Private-use artwork',{'private-use':'allowed','modify':'allowed'},dict.fromkeys(['private-use','transform'],'allowed')),resource('map-output','Finished-map output allowed; raw assets denied',{'private-use':'allowed','modify':'allowed','flattened-map-export':'allowed','raw-redistribution':'denied','session-delivery':'denied'},{'private-use':'allowed','transform':'allowed','export':'allowed','redistribution':'denied','campaign-use':'denied'}),resource('campaign-art','Campaign-scoped delivery',{'private-use':'allowed','session-delivery':'allowed'},{'private-use':'allowed','campaign-use':'allowed'}),resource('credited-art','Reusable artwork with attribution',all_allow,cap_allow,commercial=True),resource('unknown-sheet','Imported sheet; license unknown',{},{}),resource('provider-reference','Provider reference; original bytes absent',{'private-use':'allowed','session-delivery':'allowed'},{'private-use':'allowed','campaign-use':'allowed'}),resource('gm-handout','GM-only handout',all_allow,cap_allow,commercial=True),resource('derived-art','Derivative with a private-only parent',all_allow,cap_allow,commercial=True),resource('revoked-art','Revoked grant',all_allow,dict.fromkeys(caps,'revoked'),commercial=True)]
resources[3]['attribution']={'state':'required','requiredFields':['creator','title','source','license','changes'],'values':{'creator':'Synthetic Studio','title':'Test lantern','source':'synthetic:source:credited-art','license':'Synthetic attribution terms v1','changes':'Reduced to a map symbol'}}
resources[4]['license']['state']='unknown';resources[4]['provenance']['creator']=None;resources[4]['provenance']['purchaseReceipt']='synthetic:purchase:does-not-grant-rights'
resources[5]['bytes']={'state':'reference-only','sha256':None,'byteLength':None};resources[6]['visibility']='gm-only';resources[7]['parents']=[{'resourceId':'private-art','resourceRevision':'1','licenseRevision':'1'}]
# Independent expected outcomes per action; all use the default noncommercial policy/attribution context.
expected={
 'private-art':['permitted-by-sample-evidence','permitted-by-sample-evidence','unresolved','unresolved','unresolved'],
 'map-output':['permitted-by-sample-evidence','permitted-by-sample-evidence','blocked','permitted-by-sample-evidence','blocked'],
 'campaign-art':['permitted-by-sample-evidence','unresolved','permitted-by-sample-evidence','unresolved','unresolved'],
 'credited-art':['permitted-by-sample-evidence']*5,'unknown-sheet':['unresolved']*5,
 'provider-reference':['permitted-by-sample-evidence','unresolved','unresolved','unresolved','unresolved'],
 'gm-handout':['permitted-by-sample-evidence']*5,
 'derived-art':['permitted-by-sample-evidence','permitted-by-sample-evidence','unresolved','unresolved','unresolved'],
 'revoked-art':['blocked']*5}
cases=[{'id':r['resourceId']+':'+a,'resourceId':r['resourceId'],'action':a,'expected':expected[r['resourceId']][i],'requestOverrides':{}}for r in resources for i,a in enumerate(actions)]
cases += [
 {'id':'purchase-and-hash-do-not-grant-export','resourceId':'unknown-sheet','action':'raw-redistribution','expected':'unresolved','requestOverrides':{}},
 {'id':'missing-credit-output','resourceId':'credited-art','action':'flattened-map-export','expected':'blocked','requestOverrides':{'includeAttribution':False}},
 {'id':'private-policy-player-handout','resourceId':'gm-handout','action':'raw-redistribution','expected':'blocked','requestOverrides':{'audience':'player'}},
 {'id':'missing-audience-policy','resourceId':'credited-art','action':'raw-redistribution','expected':'blocked','requestOverrides':{'policyReceipts':{}}},
 {'id':'wrong-campaign','resourceId':'campaign-art','action':'session-delivery','expected':'blocked','requestOverrides':{'campaignId':'synthetic:other-campaign'}},
 {'id':'commercial-map-needs-separate-grant','resourceId':'map-output','action':'flattened-map-export','expected':'unresolved','requestOverrides':{'commercial':True}},
 {'id':'commercial-credited-export','resourceId':'credited-art','action':'flattened-map-export','expected':'permitted-by-sample-evidence','requestOverrides':{'commercial':True}},
 {'id':'unsupported-action','resourceId':'map-output','action':'arbitrary-action','expected':'blocked','requestOverrides':{}},
 {'id':'stale-license','resourceId':'credited-art','action':'raw-redistribution','expected':'unresolved','requestOverrides':{'expectedLicenseRevisions':{'credited-art':'0'}}}
]
for name,v in [('RESOURCES.json',resources),('CASES.json',cases)]: (p/name).write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps({'resources':len(resources),'cases':len(cases)}))
