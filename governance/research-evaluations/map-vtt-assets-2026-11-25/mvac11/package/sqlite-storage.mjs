import{DatabaseSync}from'node:sqlite';import{serialize,deserialize}from'node:v8';import{emptyState}from'./pack-core.mjs';
export class SQLitePackStorage{
 constructor(path){this.db=new DatabaseSync(path);this.db.exec('PRAGMA journal_mode=WAL; PRAGMA synchronous=FULL; CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY,v BLOB NOT NULL)');}
 async read(){const r=this.db.prepare("SELECT v FROM kv WHERE k='root'").get();return r?deserialize(r.v):null;}
 async stage(record){this.db.prepare("INSERT OR REPLACE INTO kv VALUES ('stage',?)").run(serialize(record));}
 async clearStaging(){this.db.prepare("DELETE FROM kv WHERE k='stage'").run();}
 async commit(next,expected){this.db.exec('BEGIN IMMEDIATE');try{const r=await this.read();if((r?.current.revision||0)!==expected)throw Error('Stale pack activation revision.');this.db.prepare("INSERT OR REPLACE INTO kv VALUES ('root',?)").run(serialize({current:next,previous:r?.current||emptyState()}));this.db.prepare("DELETE FROM kv WHERE k='stage'").run();this.db.exec('COMMIT');}catch(e){this.db.exec('ROLLBACK');throw e;}}
 close(){this.db.close();}
}
