(()=>{'use strict';
const DB_NAME='multiversal-content-library-collections';
const DB_VERSION=1;
const STORE='collections';
const ACTIVE_KEY='multiversal-content-library-active-collection';
const CANONICAL='canonical-487';
const STAGING='recovered-staging';
const original=window.MultiversalContentDB;
let memory=new Map();
function openDb(){return new Promise((resolve,reject)=>{const request=indexedDB.open(DB_NAME,DB_VERSION);request.onupgradeneeded=()=>{if(!request.result.objectStoreNames.contains(STORE))request.result.createObjectStore(STORE,{keyPath:'id'});};request.onsuccess=()=>resolve(request.result);request.onerror=()=>reject(request.error);});}
async function getCollection(id){if(memory.has(id))return memory.get(id);const db=await openDb();return new Promise((resolve,reject)=>{const request=db.transaction(STORE,'readonly').objectStore(STORE).get(id);request.onsuccess=()=>{if(request.result)memory.set(id,request.result);resolve(request.result||null);};request.onerror=()=>reject(request.error);});}
async function putCollection(collection){const db=await openDb();await new Promise((resolve,reject)=>{const request=db.transaction(STORE,'readwrite').objectStore(STORE).put(collection);request.onsuccess=()=>resolve();request.onerror=()=>reject(request.error);});memory.set(collection.id,collection);return collection;}
async function removeCollection(id){const db=await openDb();await new Promise((resolve,reject)=>{const request=db.transaction(STORE,'readwrite').objectStore(STORE).delete(id);request.onsuccess=()=>resolve();request.onerror=()=>reject(request.error);});memory.delete(id);}
function activeId(){return localStorage.getItem(ACTIVE_KEY)||CANONICAL;}
function selectCollection(id){localStorage.setItem(ACTIVE_KEY,id);original.clear?.();location.reload();}
async function load(options={}){
  const id=activeId();
  if(id===CANONICAL)return original.load(options);
  const collection=await getCollection(id);
  if(!collection)throw new Error('The selected staging collection is not installed in this browser. Import the recovery ledger again or switch to the certified 487-object collection.');
  options.onProgress?.(`Loaded ${collection.records.length.toLocaleString()} recovered staging records.`);
  return {manifest:collection.manifest||{},index:{format:'multiversal-content-database',recordCount:collection.records.length,records:collection.records,summary:collection.summary||{},sourceFiles:collection.sourceFiles||[]},records:collection.records,count:collection.records.length,summary:collection.summary||{},databaseVersion:collection.databaseVersion||'recovery-staging-v1',generatedAt:collection.generatedAt,fallback:false,collectionId:id,collectionName:collection.name,staging:true};
}
async function listCollections(){const canonical={id:CANONICAL,name:'Certified canonical collection',recordCount:487,kind:'canonical'};const staged=await getCollection(STAGING);return staged?[canonical,{id:STAGING,name:staged.name||'Recovered staging collection',recordCount:staged.records.length,kind:'staging',generatedAt:staged.generatedAt}]:[canonical];}
async function importRecoveryLedger(file,onProgress){
  if(!file)throw new Error('Choose recovery_ledger.csv first.');
  if(!/\.csv$/i.test(file.name))throw new Error('The staging importer currently accepts recovery_ledger.csv.');
  const records=await new Promise((resolve,reject)=>{const worker=new Worker('./recovery-import-worker.js');worker.onmessage=event=>{const message=event.data||{};if(message.type==='progress')onProgress?.(`Scanned ${message.processed.toLocaleString()} rows; retained ${message.accepted.toLocaleString()} unique named and typed records…`);if(message.type==='complete'){worker.terminate();resolve(message.records||[]);}if(message.type==='error'){worker.terminate();reject(new Error(message.message));}};worker.onerror=error=>{worker.terminate();reject(error);};worker.postMessage({file});});
  if(!records.length)throw new Error('No named, explicitly typed recovery records were found.');
  const byType={};for(const record of records)byType[record.contentType]=(byType[record.contentType]||0)+1;
  const collection={id:STAGING,name:'Recovered source staging collection',kind:'staging',databaseVersion:'recovery-staging-v1',generatedAt:new Date().toISOString(),records,recordCount:records.length,summary:{byType},manifest:{format:'multiversal-content-database-manifest',source:'Neutral recovery ledger browser import',recordCount:records.length,status:'STAGING_NOT_CANONICAL',preservedCanonicalCollection:CANONICAL}};
  await putCollection(collection);localStorage.setItem(ACTIVE_KEY,STAGING);return collection;
}
window.MultiversalContentDB={...original,load,getAll:async options=>(await load(options)).records,count:async()=> (await load()).count,status:async()=>{try{const db=await load();return{installed:true,count:db.count,meta:{databaseVersion:db.databaseVersion,generatedAt:db.generatedAt,collectionId:activeId(),staging:!!db.staging}};}catch(error){return{installed:false,count:0,error:String(error.message||error),meta:null};}},clear:async()=>{memory.clear();return original.clear?.();},exportDatabase:()=>load(),listCollections,selectCollection,activeCollection:activeId,importRecoveryLedger,removeStaging:async()=>{await removeCollection(STAGING);if(activeId()===STAGING)localStorage.setItem(ACTIVE_KEY,CANONICAL);}};
async function installControls(){
  const header=document.querySelector('.lib-header');if(!header)return;
  const wrap=document.createElement('div');wrap.className='collection-controls';wrap.innerHTML='<label>Collection <select id="contentCollection"></select></label><input id="recoveryLedgerFile" type="file" accept=".csv,text/csv" hidden><button id="importRecoveryLedger" type="button">Import recovery ledger</button><button id="removeRecoveryStaging" type="button" hidden>Remove staging</button>';
  header.insertBefore(wrap,document.querySelector('#refreshLibrary'));
  const select=wrap.querySelector('#contentCollection');const collections=await listCollections();select.innerHTML=collections.map(c=>`<option value="${c.id}" ${c.id===activeId()?'selected':''}>${c.name} (${Number(c.recordCount).toLocaleString()})</option>`).join('');select.onchange=()=>selectCollection(select.value);
  const input=wrap.querySelector('#recoveryLedgerFile'),button=wrap.querySelector('#importRecoveryLedger'),remove=wrap.querySelector('#removeRecoveryStaging');remove.hidden=!collections.some(c=>c.id===STAGING);
  button.onclick=()=>input.click();input.onchange=async()=>{try{button.disabled=true;const status=document.querySelector('#libraryStatus');status.textContent='Preparing recovery-ledger staging import…';const collection=await importRecoveryLedger(input.files?.[0],message=>status.textContent=message);status.textContent=`Imported ${collection.records.length.toLocaleString()} staging records. Reloading…`;location.reload();}catch(error){document.querySelector('#libraryStatus').textContent=`Staging import failed: ${error.message}`;button.disabled=false;}};
  remove.onclick=async()=>{if(!confirm('Remove the browser-local recovered staging collection? The certified 487-object collection will remain untouched.'))return;await window.MultiversalContentDB.removeStaging();location.reload();};
}
window.addEventListener('DOMContentLoaded',installControls,{once:true});
})();
