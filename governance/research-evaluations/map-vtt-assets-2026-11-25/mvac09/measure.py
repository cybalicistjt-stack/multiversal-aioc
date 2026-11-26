from pathlib import Path
from PIL import Image,ImageCms
import json,time,statistics,hashlib,io
src=Path('work/mvac08/package/sprites');out=Path('work/mvac09/package');rows=[]
for p in sorted(src.glob('*.png')):
 im=Image.open(p).convert('RGBA');original=p.read_bytes();variants=[]
 for name,fmt,opts in [('png_opt','PNG',{'optimize':True,'compress_level':9}),('webp_lossless','WEBP',{'lossless':True,'method':6,'exact':True}),('webp_q85','WEBP',{'quality':85,'method':6,'exact':True}),('jpeg_white_q90','JPEG',{'quality':90,'optimize':True})]:
  dest=out/'renditions'/name;dest.mkdir(parents=True,exist_ok=True);render=im
  if fmt=='JPEG':render=Image.new('RGB',im.size,'white');render.paste(im,mask=im.getchannel('A'))
  start=time.perf_counter();buf=io.BytesIO();render.save(buf,fmt,**opts);encoded=buf.getvalue();encode=(time.perf_counter()-start)*1000
  suffix={'PNG':'png','WEBP':'webp','JPEG':'jpg'}[fmt];f=dest/(p.stem+'.'+suffix);f.write_bytes(encoded);decoded=Image.open(io.BytesIO(encoded)).convert('RGBA');a=decoded.getchannel('A').tobytes();b=im.getchannel('A').tobytes()
  ms=[]
  for _ in range(5):
   start=time.perf_counter();Image.open(io.BytesIO(encoded)).load();ms.append((time.perf_counter()-start)*1000)
  # Pixel identity ignores RGB in fully transparent source pixels only when computing visible error; exact RGBA recorded separately.
  visible=[]
  for bg in [(0,0,0,255),(255,255,255,255)]:
   x=Image.alpha_composite(Image.new('RGBA',im.size,bg),im).convert('RGB').tobytes();y=Image.alpha_composite(Image.new('RGBA',im.size,bg),decoded).convert('RGB').tobytes();visible.append({'background':bg[0],'maxError':max(abs(u-v)for u,v in zip(x,y)),'meanAbsoluteError':sum(abs(u-v)for u,v in zip(x,y))/len(x)})
  variants.append({'name':name,'bytes':len(encoded),'sha256':hashlib.sha256(encoded).hexdigest(),'rgbaExact':im.tobytes()==decoded.tobytes(),'alphaExact':a==b,'visibleErrors':visible,'encodeMs':encode,'pillowDecodeMedianMs':statistics.median(ms),'path':str(f)})
 rows.append({'assetId':p.stem,'sourceBytes':len(original),'sourceSHA256':hashlib.sha256(original).hexdigest(),'width':im.width,'height':im.height,'variants':variants})
r={'scope':'Named local Pillow encoder/decoder only; not browser/target-device performance','assets':rows,'totals':{'original':sum(r['sourceBytes']for r in rows),**{name:sum(next(v for v in r['variants']if v['name']==name)['bytes']for r in rows)for name in ['png_opt','webp_lossless','webp_q85','jpeg_white_q90']}}};(out/'MEASUREMENTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r['totals']))
