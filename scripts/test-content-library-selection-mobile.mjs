import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('content-library-selection.js', 'utf8');

function makeClassList(initial = []) {
  const values = new Set(initial);
  return {
    contains: value => values.has(value),
    add: value => values.add(value),
    remove: value => values.delete(value),
  };
}

let coreClicks = 0;
let workbenchClicks = 0;
const card = {
  dataset: { id: 'mv.object.action-definition.access-data-pad' },
  classList: makeClassList(),
  click() { coreClicks += 1; },
  closest(selector) { return selector.includes('.object-card') ? this : null; },
};
const explorer = { classList: makeClassList(['active']) };
const workbench = { disabled: false, click() { workbenchClicks += 1; explorer.classList.remove('active'); } };
const listeners = new Map();
const document = {
  addEventListener(type, handler) { listeners.set(type, handler); },
  querySelector(selector) {
    if (selector === '[data-mode="explorer"]') return explorer;
    if (selector === '[data-mode="workbench"]') return workbench;
    return null;
  },
  querySelectorAll() { return []; },
};
const context = vm.createContext({ document, window: {}, queueMicrotask, setTimeout, clearTimeout });
vm.runInContext(source, context);

assert.ok(listeners.has('pointerup'));
listeners.get('pointerup')({ target: card, pointerType: 'touch', preventDefault() {} });
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(coreClicks, 1);
assert.equal(workbenchClicks, 1);
assert.equal(card.classList.contains('active'), true);

console.log('Mobile Content Library selection acceptance passed.');
