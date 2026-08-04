import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const filter = await readFile('content-structure-assistant-filter.js', 'utf8');
const page = await readFile('content-assistant.html', 'utf8');

assert.doesNotMatch(filter, /observe\(document\.documentElement/,
  'content assistant filter must not observe the entire document');
assert.match(filter, /observe\(list,\{childList:true\}\)/,
  'content assistant filter must observe only queue child replacement');
assert.match(filter, /if\(note\.innerHTML!==markup\)note\.innerHTML=markup/,
  'assistant note updates must be idempotent');
assert.match(filter, /requestAnimationFrame\(apply\)/,
  'filter work must be coalesced outside the mutation callback');
assert.match(page, /content-structure-assistant-filter\.js/,
  'completion assistant page must load the guarded structure filter');

console.log('Content Completion Assistant load regression passed.');
