(()=>{'use strict';
const INDEX_URL='./content-db/index.json';
const MANIFEST_URL='./content-db/manifest.json';
const SOURCE_VERSION='repository-content-db-v1';
let cache=null;

async function fetchJson(url){
  const response=await fetch(`${url}?v=${Date.now()}`,{cache:'no-store'});
  if(!response.ok)throw new Error(`Repository content database is not available yet (${response.status} ${response.statusText}).`);
  try{return await response.json()}catch{throw new Error(`Repository content database file is not valid JSON: ${url}`)}
}

function normalize(record,index){
  return {
    catalogId:record.databaseId||record.catalogId||`content-${index+1}`,
    inventoryId:record.provenance?.inventoryId||record.inventoryId||record.databaseId||'',
    refId:record.stableId||record.refId||'',
    name:record.name||record.stableId||`Unnamed content record ${index+1}`,
    contentType:record.objectType||record.contentType||'Unclassified',
    stage:record.developmentStage||record.stage||'Source identified',
    source:record.source||record.provenance?.authority||'Multiversal repository content database',
    sourceLocator:record.sourceLocator||'',
    tags:Array.isArray(record.tags)?record.tags:[],
    notes:record.notes||'',
    coverageStatus:record.coverageStatus||'',
    promotionDecision:record.promotionDecision||'',
    reviewStatus:record.reviewStatus||'',
    expectedOnly:false,
    databaseSource:'repository',
    databaseVersion:SOURCE_VERSION,
    packIds:Array.isArray(record.packIds)?record.packIds:[],
    dependencies:Array.isArray(record.dependencies)?record.dependencies:[],
    provenance:record.provenance||{}
  };
}

async function load({force=false,onProgress}={}){
  if(cache&&!force)return cache;
  onProgress?.('Loading repository content database…');
  const [manifest,index]=await Promise.all([fetchJson(MANIFEST_URL),fetchJson(INDEX_URL)]);
  if(index.format!=='multiversal-content-database')throw new Error('The repository index has an unsupported format.');
  if(!Array.isArray(index.records)||index.records.length<1000)throw new Error(`Repository database validation failed: ${index.records?.length||0} records found.`);
  if(Number(index.recordCount)!==index.records.length)throw new Error('Repository database record count does not match its index.');
  cache={
    manifest,
    index,
    records:index.records.map(normalize),
    count:index.records.length,
    summary:index.summary||{},
    databaseVersion:index.databaseVersion||manifest.databaseVersion||'unknown',
    generatedAt:index.generatedAt||manifest.generatedAt||null
  };
  onProgress?.(`Loaded ${cache.count.toLocaleString()} repository records.`);
  return cache;
}

async function getAll(options){return (await load(options)).records}
async function count(){return (await load()).count}
async function status(){
  try{const db=await load();return{installed:true,count:db.count,meta:{databaseVersion:db.databaseVersion,generatedAt:db.generatedAt,summary:db.summary}}}
  catch(error){return{installed:false,count:0,error:String(error.message||error),meta:null}}
}
function clear(){cache=null;return Promise.resolve()}
async function exportDatabase(){return load()}

window.MultiversalContentDB={load,getAll,count,status,clear,exportDatabase,SOURCE_VERSION,INDEX_URL,MANIFEST_URL};
})();