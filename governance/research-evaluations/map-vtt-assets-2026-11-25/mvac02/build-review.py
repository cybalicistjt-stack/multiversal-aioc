from pathlib import Path
import json,re,html,shutil,zipfile,hashlib
w=Path('work/mvac02');p=w/'package';d=Path('deliverables');report=(w/'report.md').read_text()
def inline(s):
 s=html.escape(s);s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s);s=re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)',r'<a href="\2">\1</a>',s);return s
def md(s):
 out=[];paragraph=[];table=False;ul=False
 def flush():
  if paragraph:out.append('<p>'+inline(' '.join(paragraph))+'</p>');paragraph.clear()
 for line in s.splitlines()+['']:
  if line.startswith('|'):
   flush()
   if not table:out.append('<div class="scroll"><table>');table=True;head=True
   if re.match(r'^\|[\s:|\-]+$',line):continue
   tag='th' if head else 'td';out.append('<tr>'+''.join('<'+tag+'>'+inline(c.strip())+'</'+tag+'>' for c in line.strip('|').split('|'))+'</tr>');head=False;continue
  if table:out.append('</table></div>');table=False
  if line.startswith('- '):
   flush()
   if not ul:out.append('<ul>');ul=True
   out.append('<li>'+inline(line[2:])+'</li>');continue
  if ul:out.append('</ul>');ul=False
  if line.startswith('#'):
   flush();n=len(line)-len(line.lstrip('#'));out.append(f'<h{n}>'+inline(line[n:].strip())+f'</h{n}>')
  elif not line.strip():flush()
  else:paragraph.append(line)
 return '\n'.join(out)
data={'objects':json.loads((p/'OBJECT_TRACES.json').read_text()),'cases':json.loads((p/'CASES.json').read_text()),'verification':json.loads((p/'VERIFICATION.json').read_text())}
script='''const data=JSON.parse(document.getElementById('data').textContent);const el=id=>document.getElementById(id);const stages=['create','save','prepare','play','export','recovery'];
function option(parent,value,label){const o=document.createElement('option');o.value=value;o.textContent=label;parent.append(o);}
for(const o of data.objects)option(el('object'),o.id,o.label);for(const s of stages)option(el('stage'),s,s[0].toUpperCase()+s.slice(1));for(const c of data.cases)option(el('case'),c.id,c.id);
el('object').value='door';el('stage').value='create';el('case').value='ready-door';
function render(){const o=data.objects.find(x=>x.id===el('object').value);const c=data.cases.find(x=>x.id===el('case').value);el('trace').textContent=o.stages[el('stage').value];el('owner').textContent=o.owner;el('source').textContent=JSON.stringify(o,null,2);const selected=data.objects.find(x=>x.id===c.objectId);const r=evaluate(selected,c.overrides);el('outcome').textContent=r.status;el('case-details').textContent=JSON.stringify({object:selected.label,input:c.overrides,expected:c.expected,observed:r.status,scope:'Design oracle only; no runtime authorization or owner mutation'},null,2);}
el('object').onchange=()=>{el('case').value=data.cases.find(c=>c.objectId===el('object').value).id;render();};el('stage').onchange=render;el('case').onchange=()=>{el('object').value=data.cases.find(c=>c.id===el('case').value).objectId;render();};render();'''
adapter=(p/'reference-adapter.mjs').read_text().replace('export function','function')
(w/'review-script.js').write_text(adapter+'\n'+script)
style='''body{margin:0;background:#101820;color:#e7edf0;font:16px/1.65 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:32px 24px 80px}h1,h2,h3{line-height:1.2;color:#f6f5ea}h1{font-size:clamp(30px,5vw,48px)}h2{margin-top:50px;font-size:25px;border-top:1px solid #43535f;padding-top:24px}a{color:#8bd8e0}code{color:#f0d49b;overflow-wrap:anywhere}p{max-width:95ch}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:14px;vertical-align:top;text-align:left;border:1px solid #43535f}th{background:#203441}select{background:#172a36;color:white;padding:12px;border:1px solid #7e9cae;border-radius:6px;max-width:100%;font:inherit}label{display:flex;flex-direction:column;gap:8px}section{background:#172630;border:1px solid #496171;padding:24px;border-radius:12px;margin:28px 0}.controls{display:grid;grid-template-columns:1fr 1fr;gap:16px}.wide{grid-column:1/-1}pre{white-space:pre-wrap;word-break:break-word;background:#0e1820;padding:16px;border-radius:6px;font-size:13px}.tag{display:inline-block;padding:5px 12px;border:1px solid #648c8b;border-radius:20px;color:#aee2d0}output{display:block;font-size:24px;color:#f0d49b}details{margin-top:20px}summary{cursor:pointer}li{margin:8px 0}@media(max-width:650px){main{padding:20px 14px}.controls{grid-template-columns:1fr}td,th{min-width:150px}section{padding:16px}}'''
body=md(report)
inspector='''<section aria-labelledby="inspector"><span class="tag">Interactive design review</span><h2 id="inspector">Follow an object through the system</h2><p>These are contract examples. Changing a selection runs a local design oracle; it does not change a map or authorize a live action.</p><div class="controls"><label>Object<select id="object"></select></label><label>Stage<select id="stage"></select></label><label class="wide">Case<select id="case"></select></label></div><h3>Existing owner</h3><p id="owner"></p><h3>Stage contract</h3><p id="trace" aria-live="polite"></p><h3>Case result</h3><output id="outcome" aria-live="polite"></output><pre id="case-details"></pre><details><summary>Exact sidecar example and native source</summary><pre id="source"></pre></details></section>'''
# Put the inspector before the full technical report, after its opening title.
pos=body.find('</h1>')+5;body=body[:pos]+inspector+body[pos:]
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Multiversal MVAC-02 — Integration contract review</title><style>'+style+'</style><main>'+body+'</main><script type="application/json" id="data">'+json.dumps(data).replace('<','\\u003c')+'</script><script>'+adapter+'\n'+script+'</script></html>'
(d/'Multiversal_MVAC02_Integration_Contract_Review.html').write_text(page);shutil.copyfile(w/'report.md',p/'MVAC02_CONTRACTS.md');shutil.copyfile(w/'report.md',d/'Multiversal_MVAC02_Integration_Contracts.md')
print('HTML bytes',len(page.encode()))
