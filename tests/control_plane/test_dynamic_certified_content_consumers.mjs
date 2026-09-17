import assert from 'node:assert/strict';
import fs from 'node:fs';

const server = fs.readFileSync('bridge/mcp-server/src/server-v3.mjs', 'utf8');
const operational = fs.readFileSync('operational/operational.js', 'utf8');

assert.doesNotMatch(server, /recordCount\s*===\s*487|expected:\s*487/, 'MCP deployment verification must not hard-code the historical 487 count');
assert.match(server, /content-db\/manifest\.json/, 'MCP deployment verification must compare the live index with the certified manifest');
assert.doesNotMatch(operational, /\['487','Certified content objects'\]/, 'operational dashboard must not hard-code the historical certified count');
assert.match(operational, /content-db\/manifest\.json/, 'operational dashboard must load the live certified manifest count');

console.log('Dynamic certified-content consumer contract: PASS');
