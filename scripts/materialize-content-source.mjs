import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';

const root = process.cwd();
const sourceDir = path.join(root, 'content-source');
const encodedPath = path.join(sourceDir, 'phase-1-8-canonical-objects.json.gz.b64');
const outputPath = path.join(sourceDir, 'phase-1-8-canonical-objects.json');

const encoded = (await fs.readFile(encodedPath, 'utf8')).replace(/\s/g, '');
const json = zlib.gunzipSync(Buffer.from(encoded, 'base64')).toString('utf8');
const payload = JSON.parse(json);
if (payload.format !== 'multiversal-content-source-bundle') throw new Error('Unexpected content-source bundle format.');
if (!Array.isArray(payload.records) || payload.records.length !== 487) throw new Error(`Expected 487 source records; found ${payload.records?.length ?? 0}.`);
await fs.writeFile(outputPath, JSON.stringify(payload, null, 2) + '\n');
console.log(`Materialized ${payload.records.length} canonical content-source records.`);
