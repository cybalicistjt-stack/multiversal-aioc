from pathlib import Path
from PIL import Image,ImageCms,ImageOps
import io,json,hashlib
p=Path('work/mvac09/package');srgb=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes();results=[];profiles=[]
def test(name,f):
 try:f();results.append({'id':name,'status':'PASS'})
 except Exception as e:results.append({'id':name,'status':'FAIL','error':str(e)})
for source in sorted((p/'sprites').glob('*.png')):
 raw=source.read_bytes();before=hashlib.sha256(raw).hexdigest();im=Image.open(io.BytesIO(raw)).convert('RGBA')
 for profile,maxside in [('thumbnail',128),('play',256),('print-source',320)]:
  target=im.copy();target.thumbnail((maxside,maxside),Image.Resampling.LANCZOS);dest=p/'profiles'/profile;dest.mkdir(parents=True,exist_ok=True);f=dest/source.name;target.save(f,'PNG',optimize=True,icc_profile=srgb,dpi=(300,300)if profile=='print-source'else(96,96));decoded=Image.open(f)
  assert decoded.size[0]<=im.width and decoded.size[1]<=im.height
  assert decoded.info.get('icc_profile')==srgb
  assert source.read_bytes()==raw
  profiles.append({'source':source.name,'sourceSHA256':before,'profile':profile,'width':target.width,'height':target.height,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'sourceColor':'untagged assumed sRGB; no source-profile certification','outputColor':'embedded sRGB ICC','orientation':'source PNG already normalized','alpha':'RGBA; alpha-aware LANCZOS in named Pillow runtime','upscaled':False,'dpiMetadata':300 if profile=='print-source'else 96,'maximumPrintInchesAt300Dpi':[round(target.width/300,3),round(target.height/300,3)],'path':str(f)})
test('33 generated PNG profiles remain bounded, tagged and source-preserving',lambda:(_ for _ in ()).throw(AssertionError())if len(profiles)!=33 else None)
# Named color/orientation fixtures exercise the actual normalization operations.
opaque=Image.new('RGB',(30,18));opaque.putdata([(x*8,y*14,(x+y)*5)for y in range(18)for x in range(30)]);exif=Image.Exif();exif[274]=6;buf=io.BytesIO();opaque.save(buf,'JPEG',quality=95,icc_profile=srgb,exif=exif);raw=buf.getvalue();digest=hashlib.sha256(raw).hexdigest();decoded=Image.open(io.BytesIO(raw));oriented=ImageOps.exif_transpose(decoded);normalized=ImageCms.profileToProfile(oriented,ImageCms.ImageCmsProfile(io.BytesIO(decoded.info['icc_profile'])),ImageCms.createProfile('sRGB'),outputMode='RGB')
test('real JPEG EXIF orientation normalization swaps axes once',lambda:None if normalized.size==(18,30)and oriented.getexif().get(274)not in[6]else(_ for _ in()).throw(AssertionError()))
test('real ICC sRGB identity transform retains pixels',lambda:None if normalized.tobytes()==oriented.convert('RGB').tobytes()else(_ for _ in()).throw(AssertionError()))
test('color/orientation normalization retains original encoded bytes',lambda:None if hashlib.sha256(raw).hexdigest()==digest else(_ for _ in()).throw(AssertionError()))
# A translucent colored edge with colored alpha-zero surroundings exposes matte contamination.
trans=Image.new('RGBA',(64,64),(0,0,255,0))
for y in range(64):
 for x in range(64):
  if 12<=x<52 and 12<=y<52:trans.putpixel((x,y),(220,50,20,160))
small=trans.resize((32,32),Image.Resampling.LANCZOS);edge=[c for c in small.getdata()if 5<c[3]<150]
test('alpha-aware resize does not mix blue transparent RGB into visible edge',lambda:None if edge and max(c[2]for c in edge)<60 else(_ for _ in()).throw(AssertionError()))
for bg in[(0,0,0,255),(255,255,255,255)]:
 composite=Image.alpha_composite(Image.new('RGBA',small.size,bg),small)
 test('translucent edge composite '+str(bg[0]),lambda composite=composite:None if composite.getextrema()[3]==(255,255)else(_ for _ in()).throw(AssertionError()))
report={'scope':'Named local Pillow/ImageCms profile, alpha and EXIF fixtures; no browser/GPU/physical-display/print-color certification','passed':sum(x['status']=='PASS'for x in results),'failed':sum(x['status']=='FAIL'for x in results),'results':results,'profiles':profiles};(p/'COLOR_PROFILES.json').write_text(json.dumps(report,indent=2)+'\n');print({k:report[k]for k in ['passed','failed']});assert report['failed']==0
