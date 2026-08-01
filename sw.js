const CACHE = 'multiversal-aioc-forge-v13';
const ASSETS = [
  './',
  './index.html',
  './styles.css',
  './forge-v2.css',
  './forge-interview-v6.css',
  './forge-starters-v7.css',
  './forge-creatures-v8.css',
  './forge-ability-v9.css',
  './multiversal-seed.js',
  './app.js',
  './forge-v2.js',
  './forge-interview-v6.js',
  './forge-starters-v7.js',
  './forge-creatures-v8.js',
  './forge-ability-v9.js',
  './forge-ability-v9-fix.js',
  './manifest.webmanifest',
  './icon-192.svg',
  './icon-512.svg',
  './refresh.html'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)));
  self.skipWaiting();
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key.startsWith('multiversal-aioc') && key !== CACHE).map(key => caches.delete(key)))));
  self.clients.claim();
});
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (event.request.mode === 'navigate') {
    event.respondWith(fetch(event.request, {cache:'no-store'}).then(response => {
      const copy=response.clone(); caches.open(CACHE).then(cache=>cache.put('./index.html',copy)); return response;
    }).catch(()=>caches.match('./index.html')));
    return;
  }
  event.respondWith(fetch(event.request,{cache:'no-store'}).then(response=>{
    if(response&&response.ok){const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));}
    return response;
  }).catch(()=>caches.match(event.request)));
});