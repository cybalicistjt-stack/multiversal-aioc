from pathlib import Path
import json,hashlib,io,time,platform,math
from PIL import Image,features,__version__
import numpy as np
r=Path('/workspace/scratch/b605cb1003d1');w=Path(__file__).parent
prior=json.loads((r/'work/assets28/audit.json').read_text())
rows=[]
for i,old in enumerate(prior['sheets'],1):
 p=r/f'work/assets28/sheet-{i:02}.jpg';data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==old['sha256']
 with Image.open(io.BytesIO(data))as image:
  image.load();a=np.array(image.convert('RGB'),dtype=np.float32);f=io.BytesIO();t=time.perf_counter();image.save(f,'WEBP',quality=75,method=4);encode=time.perf_counter()-t;b=f.getvalue();t=time.perf_counter()
  with Image.open(io.BytesIO(b))as decoded:decoded.load();d=np.array(decoded.convert('RGB'),dtype=np.float32)
  decode=time.perf_counter()-t;mse=float(np.mean((a-d)**2));psnr=10*math.log10(255**2/mse)if mse else None
  rows.append(dict(sheet=i,sourceSHA256=old['sha256'],sourceBytes=len(data),width=image.width,height=image.height,sourceAlpha='A'in image.getbands(),rgba8Estimate=image.width*image.height*4,webp75Bytes=len(b),encodeSeconds=round(encode,6),decodeAndArraySeconds=round(decode,6),PSNRvsDecodedJPEG=round(psnr,3)if psnr else None))
baseline=r/'deliverables/Multiversal_Consolidated_Playtest_UHT28_MME06_UVTT_Optional_Assets.html'
result={'scope':'Existing owner sheets verified; WebP q75/method4 encodes in memory only. No original or app edited. Pixel error compares to decoded lossy JPEG, not original artwork; no visual quality acceptance or client benchmark.','environment':{'python':platform.python_version(),'Pillow':__version__,'webp':features.version('webp'),'machine':platform.machine(),'platform':platform.platform()},'baseline':{'filename':baseline.name,'bytes':baseline.stat().st_size,'sha256':hashlib.sha256(baseline.read_bytes()).hexdigest()},'sheets':rows,'totals':{'count':len(rows),'sourceBytes':sum(x['sourceBytes']for x in rows),'rgba8Estimate':sum(x['rgba8Estimate']for x in rows),'largestSingleRGBA8':max(x['rgba8Estimate']for x in rows),'webp75Bytes':sum(x['webp75Bytes']for x in rows),'priorWebp85Bytes':sum(x['webp85Bytes']for x in prior['sheets']),'webp75SmallerCount':sum(x['webp75Bytes']<x['sourceBytes']for x in rows),'base64CharactersForSeparateOriginals':sum(4*((x['sourceBytes']+2)//3)for x in rows)}}
(w/'asset_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='sheets'},indent=2))
