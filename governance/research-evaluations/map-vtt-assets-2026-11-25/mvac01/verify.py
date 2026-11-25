from pathlib import Path
import json,hashlib,csv,io,re
from PIL import Image
r=Path('/workspace/scratch/b605cb1003d1');w=r/'work/mvac01';p=w/'package';m=json.loads((p/'MANIFEST.json').read_text());checks=[]
def sha(x):return hashlib.sha256(x).hexdigest()
def test(name,value):
 assert value,name
 checks.append(name)
def filecheck(row):
 b=(p/row['path']).read_bytes();test(row['path']+' bytes and SHA256',len(b)==row['bytes']and sha(b)==row['sha256'])
for f in m['fixtures']:
 filecheck(f['nativeFile']);d=json.loads((p/f['nativeFile']['path']).read_text());test(f['fixtureId']+' native envelope/identity',d['format']=='multiversal-cartography-tester-v2'and d['document']['id']==f['nativeId']and d['document']['revision']==f['revision'])
for row in m['roles']:
 filecheck(row['file']);d=json.loads((p/row['file']['path']).read_text());f=next(x for x in m['fixtures']if x['fixtureId']==row['fixture'])
 if row['role']=='player':
  payload=json.dumps(d['document']);test(row['file']['path']+' private IDs/labels absent',all(x['id']not in payload and(not x['label']or x['label']not in payload)for x in f['secrets']))
for row in m['renders']:
 b=(p/row['path']).read_bytes();test(row['path']+' PNG identity',sha(b)==row['pngSHA256']and len(b)==row['pngBytes'])
 with Image.open(io.BytesIO(b))as im:test(row['path']+' decoded size/pixel fingerprint',im.size==(800,520)and sha(im.convert('RGBA').tobytes())==row['rgbaSHA256'])
with(p/'ACCEPTANCE_MATRIX.csv').open()as s:tasks=list(csv.DictReader(s))
expected={f'T{i:02}'for i in range(1,13)}|{f'J{i:02}'for i in range(1,17)}|{f'A-T{i:02}'for i in range(1,13)}
test('All 40 retained/new tasks covered exactly',len(tasks)==40 and {x['id']for x in tasks}==expected)
test('No full acceptance invented',all(x['full_acceptance']=='NOT_RUN'for x in tasks))
valid={x['fixtureId']for x in m['fixtures']};test('Task fixture references valid',all(set(x['fixtures'].split('; '))<=valid for x in tasks))
filecheck(m['dependencies']);cases=json.loads((p/m['dependencies']['path']).read_text());test('Six future failure oracles remain NOT_RUN',len(cases)==6 and all(x['observed']=='NOT_RUN'for x in cases))
base=r/'deliverables'/m['baseline']['filename'];test('UHT28 original unchanged',sha(base.read_bytes())==m['baseline']['sha256'])
page=(r/'deliverables/Multiversal_MVAC01_Fixture_Baseline_Review.html').read_text();data=json.loads(re.search(r'<script id="fixture-data" type="application/json">(.*?)</script>',page,re.S)[1]);test('Review has all seven frozen fixtures',len(data)==7 and{x['fixtureId']for x in data}==valid)
for f in data:
 test(f['fixtureId']+' four native zooms and player preview',set(f['images'])=={'0.5','1','2','4'}and f['player'].startswith('data:image/png;base64,'))
count=102
receipt={'date':'2026-11-25','nativeComponentChecks':count,'nativeComponentPassed':all(x['status']=='passed'for x in m['checks'])and len(m['checks'])==count,'fixtureIntegrityChecks':len(checks),'fixtureIntegrityPassed':True,'fixtures':7,'levels':14,'renders':36,'staticProjectionSnapshots':28,'acceptanceTasks':40,'deviceRows':5,'fullWorkflowAcceptance':'NOT_RUN','productChanged':False,'baseline':m['baseline'],'knownIncident':{'class':'validation harness defect','firstAttempt':'repeat-artwork mistakenly called static export rather than artwork renderer; differing pixel hashes','causalRepair':'repeat-artwork routed to same native.render path','changedBuilderRerun':'102 focused checks passed; same-environment repeated artwork pixel hash matched'},'scope':'Fixture/planning acceptance only. No browser, authenticated transport, installed app, target-device, pack-resolver or creator acceptance.'}
(w/'VERIFICATION.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt,indent=2))
