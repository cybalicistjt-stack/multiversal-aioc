from pathlib import Path
import io,json,zipfile,struct,zlib,base64
from PIL import Image,ImageDraw
p=Path('work/mvac07/package/fixtures');p.mkdir(parents=True,exist_ok=True)
im=Image.new('RGBA',(24,20),(0,0,0,0));d=ImageDraw.Draw(im);d.rectangle((3,3,20,16),fill=(74,180,132,255));im.save(p/'small.png');im.convert('RGB').save(p/'small.jpg',quality=90);im.convert('RGB').save(p/'progressive.jpg',quality=90,progressive=True);im.save(p/'small.webp',lossless=True);im.save(p/'lossy.webp',lossless=False,quality=80)
(p/'basic.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="24" viewBox="0 0 32 24"><g fill="#55b988"><rect x="2" y="2" width="20" height="18" rx="2"/><circle cx="25" cy="12" r="5" fill="#e9d79c"/></g></svg>')
(p/'LICENSE.txt').write_text('Synthetic intake fixture. This file is evidence text, not an automatic rights grant.\n');(p/'metadata.json').write_text('{"creator":"Synthetic test","license":"unknown","__proto__":{"notApplied":true}}\n')
def png_chunk(t,data):return struct.pack('>I',len(data))+t+data+struct.pack('>I',zlib.crc32(t+data)&0xffffffff)
b=(p/'small.png').read_bytes();ihdr=bytearray(b[16:29]);ihdr[:8]=struct.pack('>II',100000,100000);(p/'pixel-bomb.png').write_bytes(b[:8]+png_chunk(b'IHDR',ihdr)+b[33:]);(p/'bad-crc.png').write_bytes(b[:-5]+bytes([b[-5]^1])+b[-4:]);(p/'apng.png').write_bytes(b[:33]+png_chunk(b'acTL',struct.pack('>II',2,0))+b[33:]);(p/'truncated.png').write_bytes(b[:50]);(p/'polyglot.png').write_bytes(b+b'<script>bad</script>')
im2=Image.new('RGBA',(24,20),(255,0,0,255));im.save(p/'animated.webp',save_all=True,append_images=[im2],duration=80,loop=0)
(p/'static.gif').write_bytes(base64.b64decode('R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=='))
svg_cases={'script.svg':'<svg width="32" height="24"><script>alert(1)</script></svg>','external.svg':'<svg width="32" height="24"><image href="https://example.invalid/a.png"/></svg>','entity.svg':'<!DOCTYPE svg [<!ENTITY x SYSTEM "file:///private">]><svg width="32" height="24">&x;</svg>','event.svg':'<svg width="32" height="24" onload="bad()"></svg>','paint-url.svg':'<svg width="32" height="24"><rect width="10" height="10" fill="url(https://example.invalid/)"/></svg>','path.svg':'<svg width="32" height="24"><path d="M0 0L10 10"/></svg>','huge.svg':'<svg width="999999" height="999999"></svg>','group-opacity.svg':'<svg width="32" height="24"><g opacity="0.5"><circle r="1"/></g></svg>'}
for n,s in svg_cases.items():(p/n).write_text(s)
def pack(name,entries,compression=zipfile.ZIP_DEFLATED):
 with zipfile.ZipFile(p/name,'w',compression)as z:
  for path,content,attrs in entries:
   i=zipfile.ZipInfo(path);i.compress_type=compression
   if attrs is not None:i.create_system=3;i.external_attr=attrs
   z.writestr(i,content)
pack('valid.zip',[('art/one.png',b,None),('art/two.png',b,None),('LICENSE.txt',(p/'LICENSE.txt').read_bytes(),None),('metadata.json',(p/'metadata.json').read_bytes(),None)])
pack('stored.zip',[('one.png',b,None)],zipfile.ZIP_STORED)
pack('traversal.zip',[('../escape.png',b,None)])
pack('duplicate.zip',[('ART/one.png',b,None),('art/ONE.PNG',b,None)])
pack('symlink.zip',[('linked.png',b,0o120777<<16)])
pack('nested.zip',[('nested.zip',(p/'valid.zip').read_bytes(),None)])
pack('unsupported-active.zip',[('one.png',b,None),('active.html',b'<script>bad()</script>',None)])
pack('ratio-bomb.zip',[('repeat.txt',b'A'*200000,None)])
pack('bad-media.zip',[('one.png',b,None),('broken.png',b'not PNG',None)])
# Central/local mismatch and expansion forgery exercise real byte parsers.
v=bytearray((p/'valid.zip').read_bytes());central=v.index(b'PK\x01\x02');local=0;v[central+46]^=1;(p/'name-mismatch.zip').write_bytes(v)
v=bytearray((p/'stored.zip').read_bytes());central=v.index(b'PK\x01\x02');v[central+16]^=1;v[14]^=1;(p/'bad-archive-crc.zip').write_bytes(v)
v=bytearray((p/'ratio-bomb.zip').read_bytes());central=v.index(b'PK\x01\x02');v[22:26]=struct.pack('<I',1024);v[central+24:central+28]=struct.pack('<I',1024);(p/'forged-expansion.zip').write_bytes(v)
# Descriptor ZIP from a non-seekable target.
class Sink(io.BytesIO):
 def seekable(self):return False
 def seek(self,*args):raise io.UnsupportedOperation()
s=Sink()
with zipfile.ZipFile(s,'w',zipfile.ZIP_DEFLATED)as z:z.writestr('descriptor.png',b)
(p/'descriptor.zip').write_bytes(s.getvalue())
(p/'bad.webp').write_bytes((p/'small.webp').read_bytes()[:-4]);(p/'bad.jpg').write_bytes((p/'small.jpg').read_bytes()[:-5])
print(json.dumps({'fixtures':len(list(p.iterdir())),'samplePNGBytes':len(b)}))
