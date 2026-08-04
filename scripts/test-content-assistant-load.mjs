import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const filter = await readFile('content-structure-assistant-filter.js', 'utf8');
const page = await readFile('content-assistant-v2.html', 'utf8');
const legacy = await readFile('content-assistant.html', 'utf8');

assert.doesNotMatch(filter, /observe\(document\.documentElement/,
  'content assistant filter must not observe the entire document');
assert.match(filter, /observe\(list,\{childList:true\}\)/,
  'content assistant filter must observe only queue child replacement');
assert.match(filter, /if\(note\.innerHTML!==markup\)note\.innerHTML=markup/,
  'assistant note updates must be idempotent');
assert.match(filter, /requestAnimationFrame\(apply\)/,
  'filter work must be coalesced outside the mutation callback');
assert.match(page, /ASSISTED CONTENT COMPLETION 1\.5/,
  'uncached assistant entrypoint must expose build 1.5');
assert.match(page, /content-structure-assistant-filter\.js/,
  'uncached assistant entrypoint must load the guarded structure filter');
assert.match(legacy, /content-assistant-v2\.html/,
  'legacy assistant URL must redirect without loading the old application');
assert.doesNotMatch(legacy, /content-structure-assistant-filter\.js/,
  'legacy redirect must not start assistant scripts');

console.log('Content Completion Assistant load regression passed.');
