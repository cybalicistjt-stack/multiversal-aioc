(()=>{'use strict';
const SCRIPT_BASE=new URL('.',document.currentScript?.src||window.location.href);
const INDEX_URL=new URL('content-db/index.json',SCRIPT_BASE).href;
const MANIFEST_URL=new URL('content-db/manifest.json',SCRIPT_BASE).href;
const SOURCE_REGISTRY_URL=new URL('content-db/source-registry.json',SCRIPT_BASE).href;
const RECORD_SCHEMA_URL=new URL('content-db/content-record.schema.json',SCRIPT_BASE).href;
const SOURCE_VERSION='canonical-content-db-v1';
const LOAD_TIMEOUT_MS=20000;
let cache=null;

async function fetchJson(url){
  const controller=new AbortController();
  const timer=setTimeout(()=>controller.abort(),LOAD_TIMEOUT_MS);
  try{
    const requestUrl=new URL(url);
    requestUrl.searchParams.set('v',Date.now());
    const response=await fetch(requestUrl.href,{cache:'no-store',signal:controller.signal});
    if(!response.ok)throw new Error(`${requestUrl.pathname} returned ${response.status}`);
    return await response.json();
  }catch(error){
    if(error?.name==='AbortError')throw new Error(`${url} did not respond within ${LOAD_TIMEOUT_MS/1000} seconds.`);
    throw error;
  }finally{clearTimeout(timer)}
}

function normalize(record,index){
  return {
    catalogId:record.databaseId||record.catalogId||`content-${index+1}`,
    inventoryId:record.provenance?.inventoryId||record.inventoryId||record.databaseId||'',
    refId:record.stableId||record.refId||'',
    name:record.name||record.stableId||`Unnamed content record ${index+1}`,
    contentType:record.objectType||record.contentType||'Unclassified',
    stage:record.developmentStage||record.stage||'Source identified',
    source:record.source||record.provenance?.authority||'Multiversal canonical content database',
    sourceLocator:record.sourceLocator||'',
    tags:Array.isArray(record.tags)?record.tags:[],
    notes:record.notes||'',
    coverageStatus:record.coverageStatus||'',
    promotionDecision:record.promotionDecision||'',
    reviewStatus:record.reviewStatus||'',
    expectedOnly:false,
    databaseSource:'repository',
    databaseVersion:record.databaseVersion||SOURCE_VERSION,
    packIds:Array.isArray(record.packIds)?record.packIds:[],
    dependencies:Array.isArray(record.dependencies)?record.dependencies:[],
    provenance:record.provenance||{},
    manualEntry:record.manualEntry||null,
    gameObject:record.gameObject||null,
    validation:record.validation||null,
    balance:record.balance||null,
    testing:record.testing||null
  };
}

async function load({force=false,onProgress}={}){
  if(cache&&!force)return cache;
  onProgress?.('Loading generated canonical content database…');
  const [manifest,index,sourceRegistry,recordSchema]=await Promise.all([
    fetchJson(MANIFEST_URL),
    fetchJson(INDEX_URL),
    fetchJson(SOURCE_REGISTRY_URL),
    fetchJson(RECORD_SCHEMA_URL)
  ]);
  if(index.format!=='multiversal-content-database')throw new Error('Unsupported content database format.');
  if(!Array.isArray(index.records))throw new Error('Content database records are missing.');
  if(index.recordCount!==index.records.length)throw new Error('Content database record count does not match its manifest.');
  if(index.records.length<1000)throw new Error(`Content database is incomplete: ${index.records.length} records found.`);
  const records=index.records.map(normalize);
  cache={
    manifest,index,sourceRegistry,recordSchema,records,
    count:records.length,
    summary:index.summary||{},
    databaseVersion:index.databaseVersion||manifest.databaseVersion||'unknown',
    generatedAt:index.generatedAt||manifest.generatedAt||null,
    fallback:false
  };
  onProgress?.(`Loaded ${cache.count.toLocaleString()} canonical content records.`);
  return cache;
}

async function getAll(options){return(await load(options)).records}
async function count(){return(await load()).count}
async function status(){try{const db=await load();return{installed:true,count:db.count,meta:{databaseVersion:db.databaseVersion,generatedAt:db.generatedAt,summary:db.summary,fallback:false}}}catch(error){return{installed:false,count:0,error:String(error.message||error),meta:null}}}
function clear(){cache=null;return Promise.resolve()}
async function exportDatabase(){return load()}
window.MultiversalContentDB={load,getAll,count,status,clear,exportDatabase,SOURCE_VERSION,INDEX_URL,MANIFEST_URL,SOURCE_REGISTRY_URL,RECORD_SCHEMA_URL,LOAD_TIMEOUT_MS};
})();
