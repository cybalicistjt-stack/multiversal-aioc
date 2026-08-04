/* Multiversal recovery-ledger CSV importer. Runs off the UI thread. */
'use strict';
function parseCsvLine(line){
  const out=[];let value='',quoted=false;
  for(let i=0;i<line.length;i++){
    const c=line[i];
    if(c==='"'){
      if(quoted&&line[i+1]==='"'){value+='"';i++;}
      else quoted=!quoted;
    }else if(c===','&&!quoted){out.push(value);value='';}
    else value+=c;
  }
  out.push(value);return out;
}
self.onmessage=async event=>{
  const file=event.data?.file;
  if(!file){self.postMessage({type:'error',message:'No recovery ledger file supplied.'});return;}
  try{
    const reader=file.stream().getReader();
    const decoder=new TextDecoder();
    let carry='',headers=null,processed=0,accepted=0;
    const unique=new Map();
    while(true){
      const {value,done}=await reader.read();
      carry+=decoder.decode(value||new Uint8Array(),{stream:!done});
      const lines=carry.split(/\r?\n/);carry=done?'':lines.pop()||'';
      for(const line of lines){
        if(!line)continue;
        if(!headers){headers=parseCsvLine(line);continue;}
        const values=parseCsvLine(line);processed++;
        const row={};headers.forEach((h,i)=>row[h]=values[i]||'');
        if(!row.name||!row.object_type)continue;
        const key=row.semantic_key||`${row.object_type}|${row.name}`.toLowerCase();
        if(unique.has(key))continue;
        unique.set(key,{
          catalogId:row.recovery_id||`recovered-${processed}`,
          refId:row.recovery_id||'',
          name:row.name,
          contentType:row.object_type,
          stage:'Review',
          source:`${row.archive||'Recovered source'}${row.member?` · ${row.member}`:''}`,
          sourceLocator:row.record_locator||'',
          tags:['recovered','staging','not-canonical'],
          coverageStatus:'recovered-staging',
          reviewStatus:'requires-owner-review',
          promotionDecision:'not-promoted',
          databaseSource:'recovery-ledger',
          databaseVersion:'recovery-staging-v1',
          provenance:{archive:row.archive||'',member:row.member||'',nestedFrom:row.nested_from||'',payloadSha256:row.payload_sha256||'',sourceFileSha256:row.source_file_sha256||'',semanticKey:key,identityVariantCount:Number(row.identity_variant_count||0)},
          gameObject:null
        });
        accepted++;
        if(processed%25000===0)self.postMessage({type:'progress',processed,accepted});
      }
      if(done)break;
    }
    if(carry){
      const values=parseCsvLine(carry);processed++;
      const row={};headers?.forEach((h,i)=>row[h]=values[i]||'');
      if(row.name&&row.object_type){
        const key=row.semantic_key||`${row.object_type}|${row.name}`.toLowerCase();
        if(!unique.has(key))unique.set(key,{catalogId:row.recovery_id||`recovered-${processed}`,refId:row.recovery_id||'',name:row.name,contentType:row.object_type,stage:'Review',source:`${row.archive||'Recovered source'}${row.member?` · ${row.member}`:''}`,sourceLocator:row.record_locator||'',tags:['recovered','staging','not-canonical'],coverageStatus:'recovered-staging',reviewStatus:'requires-owner-review',promotionDecision:'not-promoted',databaseSource:'recovery-ledger',databaseVersion:'recovery-staging-v1',provenance:{archive:row.archive||'',member:row.member||'',nestedFrom:row.nested_from||'',payloadSha256:row.payload_sha256||'',sourceFileSha256:row.source_file_sha256||'',semanticKey:key,identityVariantCount:Number(row.identity_variant_count||0)},gameObject:null});
      }
    }
    self.postMessage({type:'complete',processed,records:[...unique.values()]});
  }catch(error){self.postMessage({type:'error',message:String(error?.message||error)});}
};
