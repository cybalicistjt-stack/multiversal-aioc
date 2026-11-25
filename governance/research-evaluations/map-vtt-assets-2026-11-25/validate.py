from pathlib import Path
import json,re,hashlib,csv
from html.parser import HTMLParser
r=Path('/workspace/scratch/b605cb1003d1');w=Path(__file__).parent
plan=json.loads((w/'MVAC_BACKLOG.json').read_text());steps=plan['steps'];ids={x['id']for x in steps};assert len(ids)==24
src=json.loads((w/'sources.json').read_text());sids={x['id']for x in src};assert len(sids)==85
seen=set();stack=set()
def walk(k):
 assert k in ids
 if k in stack:raise AssertionError('dependency cycle')
 if k in seen:return
 stack.add(k)
 for dep in next(x for x in steps if x['id']==k)['dependencies']:walk(dep)
 stack.remove(k);seen.add(k)
for x in steps:
 walk(x['id']);assert x['status']=='planned_not_selected'and x['implementation_complete']is False
 assert set(x['source_refs'])<=sids
 assert x['deliverable']and x['acceptance']and x['existing_owner']
refs={q for x in steps for q in x['prior_recommendations']}
assert {f'C{i:02}'for i in range(1,13)}|{f'R{i:02}'for i in range(1,13)}<=refs
html=(r/'deliverables/Multiversal_Map_Maker_VTT_and_Assets_Integrated_Study_v3.html').read_text()
anchors=re.findall(r'\bid="([^"]+)"',html);links=re.findall(r'href="#([^"]+)"',html)
assert len(anchors)==len(set(anchors));assert set(links)<=set(anchors);assert all(i.lower()in anchors for i in sids)
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.sections=0;self.h2=0;self.sourceLinks=0
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if t=='section':self.sections+=1
  if t=='h2':self.h2+=1
  if t=='a'and d.get('href','').startswith('https:'):self.sourceLinks+=1
p=Parse();p.feed(html);assert p.sections==p.h2;assert p.sourceLinks==85
native=json.loads((w/'asset_audit.json').read_text());b=r/'deliverables'/native['baseline']['filename'];assert hashlib.sha256(b.read_bytes()).hexdigest()==native['baseline']['sha256']
assert len(native['sheets'])==22 and not any(x['sourceAlpha']for x in native['sheets'])
receipt={'date':'2026-11-25','studySources':85,'newPublicSources':25,'newPinnedProjectSources':3,'gapSteps':24,'acyclicDependencyGraph':True,'allR01_R12_and_C01_C12Mapped':True,'allStepsPlannedNotSelected':True,'sourceAnchors':85,'internalAnchorLinks':len(links),'sections':p.sections,'retainedMapTasks':12,'retainedJointTasks':16,'newAssetTasks':12,'baselineUnchanged':True,'newCodecTrialScope':'22 original hash-verified sheets; q75/method4 WebP in-memory; no artistic/device approval','validationScope':'Document structure, plan dependencies/references/status, baseline hash and reused filter test; no real app, device, recipient or multiplayer acceptance.','artifacts':[]}
for ext in ['html','md']:
 a=r/f'deliverables/Multiversal_Map_Maker_VTT_and_Assets_Integrated_Study_v3.{ext}';receipt['artifacts'].append(dict(filename=a.name,bytes=a.stat().st_size,sha256=hashlib.sha256(a.read_bytes()).hexdigest()))
(w/'validation.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt,indent=2))
