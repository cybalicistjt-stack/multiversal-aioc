from pathlib import Path
import re,json,hashlib
old=Path('deliverables/Multiversal_MVAC11_Optional_Pack_Activation.html').read_text();path=Path('deliverables/Multiversal_MVAC12_Storage_and_Map_Continuity.html');new=path.read_text();scripts=lambda s:[m.group(1) for m in re.finditer(r'<script[^>]*>([\s\S]*?)</script>',s)];a,b=scripts(old),scripts(new)
assert len(a)==len(b)==18
changed=[i for i in range(18)if a[i]!=b[i]];assert changed==[0,2,3,6,13,17],changed
uris=lambda s:sorted(re.findall(r'data:image/(?:png|webp);base64,[A-Za-z0-9+/]+={0,2}',s));assert uris(old)==uris(new)
assert not re.search(r'<script[^>]+\bsrc\s*=',new);assert not re.search(r'<link[^>]+rel=["\']stylesheet',new)
m=json.loads(b[6])['manifest']
for blob in m['blobs']:
 l=blob['locator'];u=b[2][l['start']:l['start']+l['length']];import base64
 raw=base64.b64decode(u.split(',')[1]);assert hashlib.sha256(raw).hexdigest()==blob['sha256'];assert len(raw)==blob['byteLength']
assert len(m['blobs'])==48
report={'html':path.name,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'growthBytes':len(new.encode())-len(old.encode()),'inlineScriptBodies':18,'inheritedBodiesExact':12,'intentionalChanges':{'0':'Harbor City built-in example: 9 outward street endpoints across 6 streets; revision +1','2':'Regional/settlement benchmark inset removed; shared native presentation crop; source geometry preserved','3':'Aspect-preserving preview, off-map path drawing, extension and asset placement; native history/save integration','6':'48 embedded source locator offsets refreshed; every image digest/length unchanged','13':'Explicit rendition canvas release and async cancellation fence','17':'Split optional-pack originals/cache adapter; maintenance UI; no built-in externalization'},'allEmbeddedImageDataURIsByteIdentical':True,'manifestBlobPinsReverified':48,'builtInArtworkRetained':59,'requiredExternalScriptOrStylesheet':False,'browserPersistenceAcceptance':'NOT_RUN','nativeRendererGPUCacheLifetime':'NOT_RUN; separate rendition canvases released only'}
Path('work/mvac12/package/ARTIFACT_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
