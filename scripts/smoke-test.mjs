import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
const root=path.resolve(process.cwd());
const pages=['index.html','aioc-core.html','studio.html','balance.html','testing-suite.html','feature-modules.html','development-os.html','diagnostics.html','refresh.html'];
const scripts=['aioc-data.js','aioc-consolidation.js','unified-desktop.js','app.js','forge-v2.js','forge-interview-v6.js','forge-starters-v7.js','forge-creatures-v8.js','forge-ability-v9.js','forge-ability-v9-fix.js','forge-expert-v10.js','design-studio-v11.1.js','sw.js'];
const failures=[];const pass=[];
for(const file of [...pages,...scripts]){const p=path.join(root,file);if(!fs.existsSync(p))failures.push(`Missing ${file}`);else pass.push(`exists ${file}`)}
for(const file of scripts){const p=path.join(root,file);if(!fs.existsSync(p))continue;try{new vm.Script(fs.readFileSync(p,'utf8'),{filename:file});pass.push(`syntax ${file}`)}catch(error){failures.push(`Syntax ${file}: ${error.message}`)}}
for(const file of pages){const p=path.join(root,file);if(!fs.existsSync(p))continue;const html=fs.readFileSync(p,'utf8');for(const match of html.matchAll(/(?:src|href)=["']\.\/([^"'?]+)|(?:src|href)=["']([^"'?:#]+\.(?:js|css|html|webmanifest|svg))/g)){const asset=match[1]||match[2];if(!asset||asset.startsWith('http'))continue;if(!fs.existsSync(path.join(root,asset)))failures.push(`${file} references missing ${asset}`)}pass.push(`assets ${file}`)}
const data=fs.readFileSync(path.join(root,'aioc-data.js'),'utf8');for(const token of ['databaseVersion','backup','restore','attention','validate','state-changed']){if(!data.includes(token))failures.push(`aioc-data.js missing contract ${token}`)}
const unified=fs.readFileSync(path.join(root,'unified-desktop.js'),'utf8');for(const token of ['diagnostics','loadFrame','showLoadError','attentionTotal']){if(!unified.includes(token))failures.push(`unified-desktop.js missing contract ${token}`)}
console.log(`PASS ${pass.length}`);pass.forEach(x=>console.log(`  ✓ ${x}`));if(failures.length){console.error(`FAIL ${failures.length}`);failures.forEach(x=>console.error(`  ✗ ${x}`));process.exit(1)}console.log('AIOC smoke tests passed.');