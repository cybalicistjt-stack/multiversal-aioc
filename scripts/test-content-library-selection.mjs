import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('content-library-selection.js', 'utf8');

let clickHandler = null;
let workbenchClicks = 0;
let explorerActive = true;

const explorer = {
  classList: {
    contains(name) {
      return name === 'active' && explorerActive;
    }
  }
};

const workbench = {
  disabled: false,
  click() {
    workbenchClicks += 1;
  }
};

const document = {
  addEventListener(type, handler) {
    if (type === 'click') clickHandler = handler;
  },
  querySelector(selector) {
    if (selector === '[data-mode="explorer"]') return explorer;
    if (selector === '[data-mode="workbench"]') return workbench;
    return null;
  }
};

const window = {};
const context = vm.createContext({ document, window, queueMicrotask, Object });
vm.runInContext(source, context, { filename: 'content-library-selection.js' });

assert.equal(typeof clickHandler, 'function', 'selection controller must register a click handler');
assert.equal(typeof window.ContentLibrarySelectionController?.openSelectedObject, 'function', 'controller API must be exposed');

const cardEvent = {
  target: {
    closest(selector) {
      return selector === '#objectList .object-card[data-id]' ? { dataset: { id: 'mv.object.test' } } : null;
    }
  }
};

clickHandler(cardEvent);
await Promise.resolve();
assert.equal(workbenchClicks, 1, 'clicking a COS object in Object Explorer must open Object Workbench');

clickHandler({ target: { closest: () => null } });
await Promise.resolve();
assert.equal(workbenchClicks, 1, 'unrelated clicks must not change modes');

explorerActive = false;
clickHandler(cardEvent);
await Promise.resolve();
assert.equal(workbenchClicks, 1, 'clicking an object outside Object Explorer must preserve the active mode');

const html = fs.readFileSync('content-library.html', 'utf8');
assert.match(html, /content-library-selection\.js\?build=content-library-2\.5/, 'deployed page must load the selection controller');
assert.ok(html.indexOf('content-library.js?build=content-library-2.5') < html.indexOf('content-library-selection.js?build=content-library-2.5'), 'selection controller must load after the core library script');

console.log('Content Library selection regression passed.');
