#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,shutil,zipfile
from pathlib import Path
FINAL_CK_SHA='c26ecb279ed5759a4c251ad54c80ebaa38e055194f6698681922b33e64269a3e'
EXPECTED_STATUS='PASS_R2C_PROTECTED_MACHINE_GATE'
THRESH={'intelligibility':4.0,'pronunciation_accuracy':4.2,'special_phone_accuracy':4.2,'stress_rhythm':4.0,'accent_target':4.0,'style_fidelity':3.8}

def sha(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()

def load_tsv(p:Path): return list(csv.DictReader(p.open(encoding='utf-8'),delimiter='\t'))
def write_tsv(p:Path,rows,fields):
 with p.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--run-dir',required=True); ap.add_argument('--acceptance-tsv',required=True); ap.add_argument('--output-dir',required=True); a=ap.parse_args()
 run=Path(a.run_dir); accp=Path(a.acceptance_tsv); out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
 result=json.loads((run/'R2C_PROTECTED_RESULT.json').read_text(encoding='utf-8'))
 ck=run/'R2C_PROTECTED_weights_batch0799.pt'
 if result.get('status')!=EXPECTED_STATUS or not result.get('r2_complete'): raise SystemExit('R2C result is not a complete machine PASS')
 if not ck.exists() or sha(ck)!=FINAL_CK_SHA: raise SystemExit('final checkpoint hash mismatch')
 if any(x.get('pass')!=125 for x in result.get('final_five_seed_gate',[])) or len(result.get('final_five_seed_gate',[]))!=5: raise SystemExit('final five-seed gate not 625/625')
 if result.get('protected_hashes_initial')!=result.get('protected_hashes_final'): raise SystemExit('protected module hash mismatch')
 acc=load_tsv(accp)
 if len(acc)!=125 or len({r['acceptance_row_id'] for r in acc})!=125 or len({r['audio_filename'] for r in acc})!=125: raise SystemExit('acceptance table must contain 125 unique governed rows/files')
 wavsrc=run/'wav'/'R2C_final'
 if not wavsrc.is_dir(): raise SystemExit(f'persisted final WAV directory missing: {wavsrc}')
 aud=out/'audio'; aud.mkdir(exist_ok=True)
 manifest=[]
 for r in acc:
  src=wavsrc/r['audio_filename']; dst=aud/r['audio_filename']
  if not src.exists(): raise SystemExit(f'missing final machine-gate WAV: {src.name}')
  shutil.copy2(src,dst)
  manifest.append({'acceptance_row_id':r['acceptance_row_id'],'audio_filename':r['audio_filename'],'bytes':dst.stat().st_size,'sha256':sha(dst)})
 if len(list(aud.glob('*.wav')))!=125: raise SystemExit('human audio package does not contain exactly 125 WAVs')
 shutil.copy2(accp,out/'TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv')
 fields=['acceptance_row_id','source_utterance_id','tier','dwc_text','english_gloss','ipa','base_style','stance_overlay','audio_filename','intelligibility_1_5','pronunciation_accuracy_1_5','special_phone_accuracy_1_5','stress_rhythm_1_5','accent_target_1_5','style_fidelity_1_5','meaning_preserved_YN','notes']
 score=[]
 for r in acc: score.append({k:r.get(k,'') for k in fields[:9]}|{k:'' for k in fields[9:]})
 write_tsv(out/'DWC_R2C_HUMAN_ACCEPTANCE_SCORECARD.tsv',score,fields)
 write_tsv(out/'DWC_R2C_HUMAN_AUDIO_MANIFEST.tsv',manifest,['acceptance_row_id','audio_filename','bytes','sha256'])
 scorer='''#!/usr/bin/env python3\nimport csv,json,sys\nfrom pathlib import Path\nP=Path(sys.argv[1]); rows=list(csv.DictReader(P.open(encoding="utf-8"),delimiter="\\t"))\nif len(rows)!=125: raise SystemExit(f"expected 125 rows, got {len(rows)}")\nreq={"intelligibility_1_5":4.0,"pronunciation_accuracy_1_5":4.2,"stress_rhythm_1_5":4.0,"accent_target_1_5":4.0}\ndef val(r,k):\n try: x=float(r[k])\n except: raise SystemExit(f"missing/bad {k} at {r.get('acceptance_row_id')}")\n if not 1<=x<=5: raise SystemExit(f"out-of-range {k} at {r.get('acceptance_row_id')}")\n return x\nmeans={k:sum(val(r,k) for r in rows)/125 for k in req}\nsp=[r for r in rows if 'special_phone' in r.get('tier','').lower()]\nmeans['special_phone_accuracy_1_5']=sum(val(r,'special_phone_accuracy_1_5') for r in sp)/len(sp) if sp else None\nst=[r for r in rows if (r.get('base_style','').strip().lower() not in ('','none','neutral','default') or r.get('stance_overlay','').strip().lower() not in ('','none','neutral','default'))]\nmeans['style_fidelity_1_5']=sum(val(r,'style_fidelity_1_5') for r in st)/len(st) if st else None\nmeaning=sum(r.get('meaning_preserved_YN','').strip().upper() in ('Y','YES','TRUE','1') for r in rows)\nthresholds={'intelligibility_1_5':4.0,'pronunciation_accuracy_1_5':4.2,'special_phone_accuracy_1_5':4.2,'stress_rhythm_1_5':4.0,'accent_target_1_5':4.0,'style_fidelity_1_5':3.8}\nchecks={k:(means[k] is None or means[k]>=v) for k,v in thresholds.items()}\nchecks['meaning_preservation_100pct']=(meaning==125)\nreport={'status':'PASS_HUMAN_CNS_PERCEPTUAL_GATE' if all(checks.values()) else 'FAIL_HUMAN_CNS_PERCEPTUAL_GATE','rows':125,'means':means,'meaning_preserved':meaning,'thresholds':thresholds,'checks':checks}\nout=P.with_name('DWC_R2C_HUMAN_ACCEPTANCE_RESULT.json'); out.write_text(json.dumps(report,indent=2),encoding='utf-8'); print(json.dumps(report,indent=2)); print('RESULT='+str(out))\n'''
 (out/'score_human_acceptance.py').write_text(scorer,encoding='utf-8')
 data=[{k:r.get(k,'') for k in ['acceptance_row_id','source_utterance_id','tier','dwc_text','english_gloss','ipa','base_style','stance_overlay','audio_filename']} for r in acc]
 page='''<!doctype html><meta charset="utf-8"><title>DWC R2C Human CNS Review</title><style>body{font:15px system-ui;margin:24px;max-width:1500px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #bbb;padding:5px;vertical-align:top}th{position:sticky;top:0;background:#fff}input[type=number]{width:52px}textarea{width:180px;height:42px}.meta{white-space:nowrap}button{padding:10px 16px;margin:8px}</style><h1>DWC R2C Human CNS Perceptual Review</h1><p>Listen to the exact 125 WAVs that passed the final machine gate. Score 1–5. Special-phone score is required only for special_phone rows. Style score is required only where a style/stance target is shown. Meaning must be Y or N for every row.</p><p>Thresholds: intelligibility ≥4.0; pronunciation ≥4.2; special-phone ≥4.2; stress/rhythm ≥4.0; accent target ≥4.0; style ≥3.8; meaning preservation 100%.</p><button onclick="exportTSV()">Export completed TSV</button><table><thead><tr><th>ID</th><th>DWC / gloss / IPA</th><th>Audio</th><th>Intell.</th><th>Pron.</th><th>Special</th><th>Stress</th><th>Accent</th><th>Style</th><th>Meaning Y/N</th><th>Notes</th></tr></thead><tbody id="tb"></tbody></table><script>const rows=DATA; const tb=document.getElementById('tb'); function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))} function inp(cls){return `<input class="${cls}" type="number" min="1" max="5" step="0.1">`} rows.forEach(r=>{let tr=document.createElement('tr');tr.innerHTML=`<td class=meta>${esc(r.acceptance_row_id)}<br>${esc(r.tier)}</td><td><b>${esc(r.dwc_text)}</b><br>${esc(r.english_gloss)}<br>${esc(r.ipa)}<br><small>${esc(r.base_style)} ${esc(r.stance_overlay)}</small></td><td><audio controls preload=none src="audio/${encodeURIComponent(r.audio_filename)}"></audio></td><td>${inp('intell')}</td><td>${inp('pron')}</td><td>${inp('special')}</td><td>${inp('stress')}</td><td>${inp('accent')}</td><td>${inp('style')}</td><td><input class="meaning" size=3 maxlength=3></td><td><textarea class="notes"></textarea></td>`;tb.appendChild(tr)}); function exportTSV(){const hdr=['acceptance_row_id','source_utterance_id','tier','dwc_text','english_gloss','ipa','base_style','stance_overlay','audio_filename','intelligibility_1_5','pronunciation_accuracy_1_5','special_phone_accuracy_1_5','stress_rhythm_1_5','accent_target_1_5','style_fidelity_1_5','meaning_preserved_YN','notes'];let out=[hdr.join('\t')];[...tb.rows].forEach((tr,i)=>{const r=rows[i],q=[r.acceptance_row_id,r.source_utterance_id,r.tier,r.dwc_text,r.english_gloss,r.ipa,r.base_style,r.stance_overlay,r.audio_filename,tr.querySelector('.intell').value,tr.querySelector('.pron').value,tr.querySelector('.special').value,tr.querySelector('.stress').value,tr.querySelector('.accent').value,tr.querySelector('.style').value,tr.querySelector('.meaning').value,tr.querySelector('.notes').value.replace(/[\t\r\n]+/g,' ')];out.push(q.map(x=>String(x??'')).join('\t'))});const b=new Blob([out.join('\n')+'\n'],{type:'text/tab-separated-values'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='DWC_R2C_HUMAN_ACCEPTANCE_SCORECARD_COMPLETED.tsv';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)}</script>'''.replace('DATA',json.dumps(data,ensure_ascii=False))
 (out/'review.html').write_text(page,encoding='utf-8')
 evidence={'schema_version':'0.1.0','status':'HUMAN_REVIEW_PACKAGE_READY','machine_checkpoint':{'file':ck.name,'bytes':ck.stat().st_size,'sha256':FINAL_CK_SHA},'machine_gate':'625/625 final; PASS_R2C_PROTECTED_MACHINE_GATE','audio_source':'exact persisted seed-1 WAVs from final passing R2C machine gate; no rerender','audio_rows':125,'thresholds':THRESH,'human_gate':'NOT_YET_RUN'}
 (out/'HUMAN_REVIEW_EVIDENCE.json').write_text(json.dumps(evidence,indent=2),encoding='utf-8')
 readme='''# DWC R2C Human CNS Review\n\n1. Open `review.html` in a browser.\n2. Listen to all 125 items and enter ratings.\n3. Click **Export completed TSV**.\n4. Run `python score_human_acceptance.py DWC_R2C_HUMAN_ACCEPTANCE_SCORECARD_COMPLETED.tsv` (optional; ChatGPT can score the uploaded TSV too).\n5. Upload the completed TSV and generated result JSON to the Multiversal project chat.\n\nDo not treat machine PASS as human pronunciation acceptance. A human failure is evidence for model/data repair, not permission to mutate canonical DWC/PSS/CNS rules without independent linguistic evidence.\n'''
 (out/'README.md').write_text(readme,encoding='utf-8')
 sums=[]
 for p in sorted(out.rglob('*')):
  if p.is_file() and p.name!='SHA256SUMS.txt': sums.append(f'{sha(p)}  {p.relative_to(out)}')
 (out/'SHA256SUMS.txt').write_text('\n'.join(sums)+'\n',encoding='utf-8')
 z=out.with_suffix('.zip')
 with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as zz:
  for p in sorted(out.rglob('*')):
   if p.is_file(): zz.write(p,p.relative_to(out))
 print('PASS human review package: 125 exact final-gate WAVs')
 print('PACKAGE_DIR='+str(out)); print('PACKAGE_ZIP='+str(z))
if __name__=='__main__': main()
