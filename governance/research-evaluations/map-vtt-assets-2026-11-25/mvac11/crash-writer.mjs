import fs from'node:fs';import{serialize,deserialize}from'node:v8';import{SQLitePackStorage}from'./package/sqlite-storage.mjs';
const[path,candidatePath,phase]=process.argv.slice(2),storage=new SQLitePackStorage(path),next=deserialize(fs.readFileSync(candidatePath));
if(phase==='before-write')process.exit(81);
await storage.stage({key:'uncommitted',rows:[]});if(phase==='after-stage')process.exit(82);
const previous=(await storage.read()).current;storage.db.exec('BEGIN IMMEDIATE');storage.db.prepare("INSERT OR REPLACE INTO kv VALUES ('root',?)").run(serialize({current:next,previous}));if(phase==='during-activation')process.exit(83);storage.db.exec('COMMIT');process.exit(84);
