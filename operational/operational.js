const nav=[
  ['Command Center','./'],
  ['Capability Workbench','#capability-workbench'],
  ['Repository Intelligence','../diagnostics.html'],
  ['Orchestration','../feature-modules.html'],
  ['Developer Workbench','../development-os.html'],
  ['Content Studio','../studio.html'],
  ['Testing & Simulation','../testing-suite.html'],
  ['Release & Recovery','../refresh.html']
];
document.querySelector('#nav').innerHTML=nav.map(([name,href],index)=>`<a class="${index===0?'active':''}" href="${href}">${name}</a>`).join('');

const stats=[['7','Implementation milestones'],['22','Required CI suites'],['487','Certified content objects'],['1','Active app work item']];
document.querySelector('#stats').innerHTML=stats.map(([value,label])=>`<div class="stat"><strong>${value}</strong><span>${label}</span></div>`).join('');

const workbench=[
  ['Development OS','Unified development workspace and project-control surface.','../development-os.html'],
  ['AIOC Core','Core operating and data-management surface.','../aioc-core.html'],
  ['Content Studio','Content authoring and structured creation tools.','../studio.html'],
  ['Balance Lab','Balance analysis and tuning workspace.','../balance.html'],
  ['Testing Suite','Integrated tests and validation tools.','../testing-suite.html'],
  ['Feature Modules','Feature and subsystem planning workspace.','../feature-modules.html'],
  ['Diagnostics','Operational diagnostics and recovery inspection.','../diagnostics.html'],
  ['Refresh & Recovery','Controlled refresh and recovery surface.','../refresh.html']
];
document.querySelector('#workbench').innerHTML=workbench.map(([name,description,href],index)=>`<a class="module" href="${href}"><span>COS-${String(index+1).padStart(2,'0')}</span><h3>${name}</h3><p>${description}</p></a>`).join('');

const modules=[
  ['Operational Core','State, decisions, handoffs, continuity, and recovery services.','../aioc-core.html'],
  ['Repository Intelligence','Repository health, drift detection, snapshots, and continuity certification.','../diagnostics.html'],
  ['Executive Dashboard','Governed project-health and next-action projection.','../development-os.html'],
  ['Orchestration','Certified queueing, dispatch, approvals, and intervention controls.','../feature-modules.html'],
  ['Developer Workbench','Change planning, review, validation, execution, and handoff.','../development-os.html'],
  ['Content Studio Services','Authoring, provenance, pack assembly, installation, and release.','../studio.html'],
  ['Testing & Simulation','Scenario harnesses, balance analysis, digital twin, and regression mining.','../testing-suite.html'],
  ['Release & Recovery','Readiness, security hardening, deployment, runtime verification, and recovery.','../refresh.html'],
  ['Operational Handoff','Certified operating state and Multiversal application delivery handoff.','../governance/current-state/AIOC_OPERATIONAL_HANDOFF.md']
];
document.querySelector('#modules').innerHTML=modules.map(([name,description,href],index)=>`<a class="module" href="${href}"><span>AIOC-${String(index+1).padStart(2,'0')}</span><h3>${name}</h3><p>${description}</p></a>`).join('');

fetch('../governance/current-state/AIOC_CURRENT_STATE.md',{cache:'no-store'})
  .then(response=>{if(!response.ok)throw new Error(response.status);return response.text();})
  .then(text=>{
    const status=text.match(/\*\*Status:\*\*\s*([^\n]+)/)?.[1]?.trim()||'Operational';
    document.querySelector('#orientation').textContent=`Governed state: ${status} · Repository: cybalicistjt-stack/multiversal-aioc`;
  })
  .catch(()=>{
    document.querySelector('#orientation').textContent='Certified operational state · governed repository projection';
  });