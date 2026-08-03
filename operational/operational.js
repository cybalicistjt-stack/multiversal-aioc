const projectBase = location.pathname.includes('/multiversal-aioc/') ? '/multiversal-aioc/' : '/';
const route = path => `${projectBase}${path.replace(/^\//,'')}`;

const nav=[
  ['Command Center',route('operational/')],
  ['Capability Workbench','#capability-workbench'],
  ['Content Library',route('content-library.html')],
  ['Repository Intelligence',route('diagnostics.html')],
  ['Orchestration',route('feature-modules.html')],
  ['Developer Workbench',route('development-os.html')],
  ['Content Studio',route('studio.html')],
  ['Testing & Simulation',route('testing-suite.html')],
  ['Release & Recovery',route('refresh.html')]
];
const navElement=document.querySelector('#nav');
navElement.innerHTML=nav.map(([name,href],index)=>`<a class="${index===0?'active':''}" href="${href}" data-target="${href}">${name}</a>`).join('');
navElement.addEventListener('click',event=>{
  const link=event.target.closest('a[data-target]');
  if(!link)return;
  const target=link.dataset.target;
  if(target.startsWith('#'))return;
  event.preventDefault();
  window.location.assign(target);
});

const stats=[['7','Implementation milestones'],['22','Required CI suites'],['487','Certified content objects'],['1','Active app work item']];
document.querySelector('#stats').innerHTML=stats.map(([value,label])=>`<div class="stat"><strong>${value}</strong><span>${label}</span></div>`).join('');

const workbench=[
  ['Content Library','Canonical game objects, relationships, assets, intelligence, and release pipeline.',route('content-library.html')],
  ['Development OS','Unified development workspace and project-control surface.',route('development-os.html')],
  ['AIOC Core','Core operating and data-management surface.',route('aioc-core.html')],
  ['Content Studio','Content authoring and structured creation tools.',route('studio.html')],
  ['Balance Lab','Balance analysis and tuning workspace.',route('balance.html')],
  ['Testing Suite','Integrated tests and validation tools.',route('testing-suite.html')],
  ['Feature Modules','Feature and subsystem planning workspace.',route('feature-modules.html')],
  ['Diagnostics','Operational diagnostics and recovery inspection.',route('diagnostics.html')],
  ['Refresh & Recovery','Controlled refresh and recovery surface.',route('refresh.html')]
];
document.querySelector('#workbench').innerHTML=workbench.map(([name,description,href],index)=>`<a class="module" href="${href}"><span>COS-${String(index+1).padStart(2,'0')}</span><h3>${name}</h3><p>${description}</p></a>`).join('');

const modules=[
  ['Operational Core','State, decisions, handoffs, continuity, and recovery services.',route('aioc-core.html')],
  ['Repository Intelligence','Repository health, drift detection, snapshots, and continuity certification.',route('diagnostics.html')],
  ['Executive Dashboard','Governed project-health and next-action projection.',route('development-os.html')],
  ['Orchestration','Certified queueing, dispatch, approvals, and intervention controls.',route('feature-modules.html')],
  ['Developer Workbench','Change planning, review, validation, execution, and handoff.',route('development-os.html')],
  ['Content Library','Canonical object exploration, relationships, assets, and pipeline management.',route('content-library.html')],
  ['Content Studio Services','Authoring, provenance, pack assembly, installation, and release.',route('studio.html')],
  ['Testing & Simulation','Scenario harnesses, balance analysis, digital twin, and regression mining.',route('testing-suite.html')],
  ['Release & Recovery','Readiness, security hardening, deployment, runtime verification, and recovery.',route('refresh.html')],
  ['Operational Handoff','Certified operating state and Multiversal application delivery handoff.',route('governance/current-state/AIOC_OPERATIONAL_HANDOFF.md')]
];
document.querySelector('#modules').innerHTML=modules.map(([name,description,href],index)=>`<a class="module" href="${href}"><span>AIOC-${String(index+1).padStart(2,'0')}</span><h3>${name}</h3><p>${description}</p></a>`).join('');

fetch(route('governance/current-state/AIOC_CURRENT_STATE.md'),{cache:'no-store'})
  .then(response=>{if(!response.ok)throw new Error(response.status);return response.text();})
  .then(text=>{
    const status=text.match(/\*\*Status:\*\*\s*([^\n]+)/)?.[1]?.trim()||'Operational';
    document.querySelector('#orientation').textContent=`Governed state: ${status} · Repository: cybalicistjt-stack/multiversal-aioc`;
  })
  .catch(()=>{
    document.querySelector('#orientation').textContent='Certified operational state · governed repository projection';
  });