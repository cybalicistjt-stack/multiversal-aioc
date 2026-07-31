(() => {
  const SEED_VERSION = '2026-07-31.1';
  if (localStorage.getItem('aioc-multiversal-seed') === SEED_VERSION) return;

  const now = new Date().toISOString();
  const current = (() => {
    try { return JSON.parse(localStorage.getItem('aioc-state') || '{}'); }
    catch { return {}; }
  })();

  const seeded = {
    version: '0.2.1',
    project: {
      name: 'Multiversal',
      phase: 'MS-02 — Cross-Platform Engineering Spikes',
      workPackage: 'WP-011 — Tauri iOS/iPadOS Spike',
      progress: 78,
      branch: 'main',
      commit: 'f1f49b504c414a56a5b8b762b175a5f6705c0f05',
      nextDecision: 'Run the prepared one-pass Apple validation package on the borrowed supported Mac; preserve evidence and clean the machine afterward.',
      targetDate: '',
      risk: 'medium'
    },
    agents: [
      {id:1101,name:'Codex Lead',role:'Implementation and repository execution',status:'blocked',task:'Awaiting the borrowed Mac to execute the remaining WP-011 Apple gates',capacity:100,quality:94,credits:0},
      {id:1102,name:'Architecture Reviewer',role:'Architecture and contract authority',status:'ready',task:'Review exact-head WP-011 evidence after Mac execution',capacity:65,quality:96,credits:0},
      {id:1103,name:'QA and Test Specialist',role:'Independent validation',status:'ready',task:'Validate simulator, lifecycle, persistence, accessibility, checksums, and clean-checkout evidence',capacity:70,quality:95,credits:0},
      {id:1104,name:'Governance Coordinator',role:'Work orders, receipts, and closure',status:'ready',task:'Prepare closure transaction only after every Apple gate passes',capacity:75,quality:96,credits:0},
      {id:1105,name:'Rules and Content Agent',role:'Game systems and canonical content',status:'idle',task:'Held while the ordered MS-02 engineering sequence completes',capacity:45,quality:92,credits:0},
      {id:1106,name:'UI System Agent',role:'Multiversal interface and accessibility',status:'idle',task:'Awaiting authorized application-development packages',capacity:50,quality:92,credits:0}
    ],
    approvals: [
      {id:1201,title:'WP-011 Apple evidence acceptance',detail:'Approve closure only after iPhone and iPad simulator, lifecycle, persistence, accessibility, clean-checkout, provenance, checksum, and independent-review gates pass.',status:'pending',created:now},
      {id:1202,title:'WP-012 physical-device interpretation',detail:'After WP-011 closes, resolve whether the P9-11 physical-device spike requirement can be satisfied by existing evidence or requires real hardware.',status:'pending',created:now},
      {id:1203,title:'WP-012 platform record boundary',detail:'At OC-02, accept exactly one evidence-based result: TAURI, CAPACITOR_FALLBACK, or STOP. No fallback implementation is preapproved.',status:'pending',created:now}
    ],
    alerts: [
      {id:1301,title:'WP-011 Apple gates remain open',detail:'Windows-compatible preparation is complete, but Xcode generation, iPhone/iPad launch, lifecycle, storage, accessibility, and clean-checkout proof require the borrowed Mac.',status:'blocked',created:now},
      {id:1302,title:'WP-012 dependency blocked',detail:'WP-012 may not activate until WP-011 is formally closed with complete evidence.',status:'blocked',created:now},
      {id:1303,title:'Moderate Linux-only glib advisory remains open',detail:'GHSA-wrw7-89jp-8q8g / RUSTSEC-2024-0429 affects transitive glib 0.18.5 on the Linux GTK/WebKit path. It is absent from Windows, Android, macOS, and iOS target graphs; remediation is deferred to a later Linux-validated package.',status:'open',created:now},
      {id:1304,title:'WP-014 and MS-03 are not authorized',detail:'Do not begin later implementation or deployment work before the ordered MS-02 sequence and owner checkpoint are complete.',status:'guardrail',created:now}
    ],
    decisions: [
      {id:1401,title:'MS-01 closed',status:'approved',date:'2026-07-27',detail:'Governed repository bootstrap and foundational controls completed.'},
      {id:1402,title:'MS-02 authorized and aligned',status:'approved',date:'2026-07-27',detail:'MS02-AUTH-001 and MS02-ALIGN-001 authorize the ordered WP-009 through WP-013 sequence.'},
      {id:1403,title:'WP-009 closed',status:'approved',date:'2026-07-27',detail:'Desktop Tauri engineering spike closed through PR #51 after all gates and independent review.'},
      {id:1404,title:'WP-010 closed',status:'approved',date:'2026-07-28',detail:'Android Tauri engineering spike closed through PR #54 with merged closure evidence.'},
      {id:1405,title:'WP-011 Windows preparation authorized',status:'approved',date:'2026-07-28',detail:'Complete all configuration, tests, tooling, evidence templates, and Mac runbooks on Windows; leave Apple-only execution gates open.'},
      {id:1406,title:'Tauri CLI aligned to runtime family',status:'approved',date:'2026-07-28',detail:'Updated @tauri-apps/cli from 2.8.4 to 2.11.4 after clean mobile regeneration proved the older generator incompatible with the locked 2.11 runtime.'},
      {id:1407,title:'Borrowed Mac is a disposable validation environment',status:'approved',date:'2026-07-31',detail:'Use the Mac once for unavoidable Apple validation, export all evidence, remove project data and credentials, and return it clean.'},
      {id:1408,title:'WP-012 legacy shell packet superseded',status:'approved',date:'2026-07-30',detail:'WP-012 is a mobile-hard-gate decision package, not a broad UI implementation package.'},
      {id:1409,title:'No paid hosted Mac, signing, or public distribution',status:'guardrail',date:'2026-07-31',detail:'WP-011 is simulator engineering validation only; credentials, production signing, publication, and paid hosting remain outside scope.'}
    ],
    sessions: [
      {id:1501,title:'WP-011 Windows-compatible preparation',status:'complete',created:'2026-07-28',summary:'Prepared governed iOS overlay, pinned toolchain, Mac bootstrap/preflight, simulator matrix, evidence template, clean-checkout procedure, checksums, and correction/retest runbook.'},
      {id:1502,title:'WP-011 package systems audit',status:'complete',created:'2026-07-31',summary:'Audited one-pass borrowed-Mac package, corrected evidence verification, hard-gate handling, cleanup inventory, prerequisite recovery, and repository binding.'},
      {id:1503,title:'WP-011 borrowed-Mac execution',status:'blocked',created:now,summary:'Ready to execute when the supported Mac is available.'}
    ],
    artifacts: [
      {id:1601,title:'WP-011 One-Pass Apple Spike v0.4.0',type:'execution package',status:'ready',path:'Project source: Multiversal_MS-02_WP-011_One-Pass_Apple_Spike_v0.4.0.zip',detail:'Repository-bound autonomous Mac validation package with completed repo adapter.'},
      {id:1602,title:'WP-011 Windows preparation evidence',type:'governance document',status:'merged',path:'docs/governance/WP-011-windows-preparation.md',detail:'Records completed Windows-safe preparation and deliberately deferred Mac-only gates.'},
      {id:1603,title:'WP-011 Mac execution runbook',type:'runbook',status:'ready',path:'docs/governance/WP-011-mac-execution-runbook.md',detail:'Execution sequence for the supported Mac.'},
      {id:1604,title:'WP-011 correction and retest runbook',type:'runbook',status:'ready',path:'docs/governance/WP-011-correction-retest-runbook.md',detail:'Bounded recovery for failed Apple gates.'},
      {id:1605,title:'WP-011 toolchain lock',type:'machine-readable lock',status:'ready',path:'docs/governance/WP-011-toolchain-lock.json',detail:'Node 24.18.0, pnpm 11.17.0, Rust 1.97.1, Tauri CLI 2.11.4.'},
      {id:1606,title:'WP-011 preflight receipt',type:'receipt',status:'blocked-record',path:'receipts/WP-011-preflight-receipt.json',detail:'Records why Apple execution could not occur on Windows.'},
      {id:1607,title:'Android debug APK evidence',type:'build artifact',status:'verified',path:'WP-010 / WP-011 preparation evidence',detail:'SHA-256 06a107a146c244208832ac968820cd4788e19fe6fe67466cafcc936d48ad33b7.'},
      {id:1608,title:'Governed repository bootstrap',type:'source package',status:'complete',path:'Multiversal_MS-01_WP-004_Governed_Repository_Bootstrap_v0.1.0.zip',detail:'Foundational governed repository controls.'},
      {id:1609,title:'Game framework DB-004',type:'development bible package',status:'complete',path:'Multiversal_DB-004_Game_Framework_v0.1.0.zip',detail:'Canonical game-framework documentation package.'}
    ],
    notes: [
      {id:1701,title:'Owner workflow',body:'The owner is not a professional programmer. Instructions must be practical, direct, step-by-step, and minimize manual file handling and repeated prompt transfer.',created:now},
      {id:1702,title:'Mac constraint',body:'The Mid-2015 MacBook Pro is borrowed, available once, and must be cleaned afterward. It is only for unavoidable WP-011 Apple tests, not general development.',created:now},
      {id:1703,title:'Development approach',body:'Multiversal is being built through a governed agentic AI team with Codex executing repository work under sealed work orders, receipts, independent review, and owner checkpoints.',created:now}
    ],
    prompts: [
      {id:1801,title:'Resume governed Multiversal work',category:'Continuation',body:'Read .ai/current-work-order.md, .ai/agent-handoff.md, the active sealed work order, control state, latest receipt, and exact repository HEAD. Resume from the first incomplete governed step. Do not repeat completed work, broaden scope, or bypass a gate.'},
      {id:1802,title:'Execute WP-011 on borrowed Mac',category:'Apple spike',body:'Execute the repository-bound WP-011 One-Pass Apple Spike v0.4.0 from preflight through evidence export and verified cleanup. Continue autonomously through all noncredential actions. Stop only for a genuine protected human gate, unavailable required hardware/software, or destructive ambiguity. Never claim PASS without required evidence.'},
      {id:1803,title:'Independent exact-head review',category:'Review',body:'Review the exact repository HEAD and bound evidence as an independent architecture and QA specialist. Verify every required gate, artifact path, checksum, limitation, and recovery procedure. Reject unsupported PASS claims and identify any scope drift or missing proof.'},
      {id:1804,title:'Create governed task packet',category:'Governance',body:'Create the smallest executable task packet consistent with the current authorized work package. Bind exact authority, baseline commit, allowed paths, prohibited actions, dependencies, gates, deliverables, rollback, evidence, and mandatory stop conditions.'}
    ],
    knowledge: [
      {id:1901,title:'Multiversal project identity',type:'project',tags:'multiversal,platform,ttrpg',links:'Development Bible; GitHub repositories',summary:'A broad tabletop role-playing game platform with governed packs, rules systems, world building, campaign play, character tools, and AI-assisted development.'},
      {id:1902,title:'MS-01',type:'milestone',tags:'governance,bootstrap,closed',links:'WP-004; repository controls',summary:'Governed repository and foundational development-control milestone. Closed.'},
      {id:1903,title:'MS-02',type:'milestone',tags:'engineering,spikes,active',links:'WP-009; WP-010; WP-011; WP-012; WP-013',summary:'Ordered cross-platform engineering validation milestone. WP-009 and WP-010 are closed; WP-011 is active and awaiting Apple execution.'},
      {id:1904,title:'WP-009 Desktop Tauri Spike',type:'work-package',tags:'desktop,tauri,closed',links:'PR #51',summary:'Desktop engineering spike completed and independently approved.'},
      {id:1905,title:'WP-010 Android Tauri Spike',type:'work-package',tags:'android,tauri,closed',links:'PR #54',summary:'Android engineering spike completed with emulator/build evidence and closure receipt.'},
      {id:1906,title:'WP-011 Tauri iOS/iPadOS Spike',type:'work-package',tags:'apple,ios,ipad,tauri,active',links:'PR #58; issue #55; Apple package v0.4.0',summary:'Windows preparation is merged. Remaining Apple-only simulator, lifecycle, persistence, accessibility, clean-checkout, provenance, checksum, and review gates await the borrowed Mac.'},
      {id:1907,title:'WP-012 Evaluate Mobile Hard Gates',type:'work-package',tags:'mobile,decision,blocked',links:'WP-009; WP-010; WP-011; OC-02',summary:'Dependency-blocked decision package that must issue TAURI, CAPACITOR_FALLBACK, or STOP based on complete spike evidence.'},
      {id:1908,title:'WP-013',type:'work-package',tags:'preauthorized,blocked,owner-checkpoint',links:'WP-012',summary:'Sequentially preauthorized but dependency-blocked. The sequence stops at its owner checkpoint.'},
      {id:1909,title:'WP-014 and MS-03',type:'guardrail',tags:'unauthorized,stop',links:'Owner authority',summary:'Not authorized. No work may begin without a later explicit owner decision.'},
      {id:1910,title:'Five context and credit protocols',type:'tooling',tags:'context,credits,continuity,ai',links:'context_protocol.py; task_packet_protocol.py; workflow_protocol.py; control_protocol.py; continuity_protocol.py',summary:'Project tools that minimize repeated context, govern task packets, preserve workflow state, enforce control boundaries, and support session continuity.'},
      {id:1911,title:'Pack architecture',type:'architecture',tags:'packs,canonical,content',links:'Phase 8; DB-004',summary:'Multiversal content is normalized into governed .pack packages with stable IDs, schemas, dependencies, validation, installation/uninstallation tests, and source provenance.'},
      {id:1912,title:'Development Bible',type:'documentation',tags:'canonical,planning,implementation',links:'DB-004 and later DB packages',summary:'Canonical bridge between extensive completed planning and future Codex implementation.'}
    ],
    docs: [
      {id:2001,title:'Current Work Order',status:'current',path:'.ai/current-work-order.md',updated:'2026-07-30'},
      {id:2002,title:'Agent Handoff',status:'current',path:'.ai/agent-handoff.md',updated:'2026-07-30'},
      {id:2003,title:'WP-011 Windows Preparation',status:'current',path:'docs/governance/WP-011-windows-preparation.md',updated:'2026-07-28'},
      {id:2004,title:'WP-011 Mac Execution Runbook',status:'ready',path:'docs/governance/WP-011-mac-execution-runbook.md',updated:'2026-07-28'},
      {id:2005,title:'WP-012 Readiness Audit',status:'dependency-blocked',path:'docs/governance/WP-012-readiness-audit.md',updated:'2026-07-30'},
      {id:2006,title:'glib Dependabot Investigation',status:'open-advisory',path:'docs/governance/MAINT-WP011-BLOCKED-glib-investigation.md',updated:'2026-07-30'}
    ],
    tasks: [
      {id:2101,title:'Obtain the borrowed Mac',detail:'Supported macOS/Xcode route with iPhone and iPad simulator runtimes.',owner:'Owner',status:'ready'},
      {id:2102,title:'Transfer WP-011 package and pinned repository',detail:'Use the v0.4.0 one-pass package bound to Multiversal-app commit f1f49b5.',owner:'Codex Lead',status:'blocked'},
      {id:2103,title:'Run Mac preflight',detail:'Verify OS, Xcode, simulator runtimes, disk, Node, pnpm, Rust, CocoaPods, Tauri CLI, exact commit, and clean checkout.',owner:'Codex Lead',status:'blocked'},
      {id:2104,title:'Generate and build the Tauri iOS project',detail:'Use the pinned CLI; do not fabricate Xcode projects or change architecture.',owner:'Codex Lead',status:'blocked'},
      {id:2105,title:'Validate iPhone and iPad',detail:'Launch, orientation, lifecycle, persistence, clean relaunch, text scaling, focus, target size, VoiceOver, and negative identity canaries.',owner:'QA Agent',status:'blocked'},
      {id:2106,title:'Run clean detached-checkout validation',detail:'Regenerate, build, launch, inventory artifacts, and verify checksums from a clean checkout.',owner:'Codex Lead',status:'blocked'},
      {id:2107,title:'Export evidence externally',detail:'Copy receipts, logs, screenshots, checksums, environment capture, generated scripts, and repository changes off the Mac.',owner:'Governance Coordinator',status:'blocked'},
      {id:2108,title:'Clean borrowed Mac',detail:'Remove repository, temporary tools/assets installed for the session, credentials, keys, caches, and project evidence only after external verification.',owner:'Codex Lead',status:'blocked'},
      {id:2109,title:'Independent exact-head review',detail:'Architecture and QA review of bound evidence and exact final commit.',owner:'Review Agents',status:'blocked'},
      {id:2110,title:'Close WP-011',detail:'Only after all required gates and review pass; otherwise record a precise HARD_GATE result.',owner:'Governance Coordinator',status:'blocked'},
      {id:2111,title:'Activate WP-012 decision package',detail:'Only after formal WP-011 closure and sealed context receipt.',owner:'Governance Coordinator',status:'blocked'}
    ],
    dependencies: [
      {id:2201,title:'WP-009 → WP-010',from:'WP-009',to:'WP-010',status:'satisfied'},
      {id:2202,title:'WP-010 → WP-011',from:'WP-010',to:'WP-011',status:'satisfied'},
      {id:2203,title:'Borrowed supported Mac → WP-011 closure',from:'Mac/Xcode/simulators',to:'WP-011',status:'blocking'},
      {id:2204,title:'WP-011 → WP-012',from:'WP-011',to:'WP-012',status:'blocking'},
      {id:2205,title:'WP-012 → WP-013',from:'WP-012',to:'WP-013',status:'blocking'},
      {id:2206,title:'WP-013 owner checkpoint → later work',from:'WP-013 OC',to:'WP-014 / MS-03',status:'protected-stop'}
    ],
    releases: [
      {id:2301,title:'MS-01 governed bootstrap',version:'MS-01',status:'closed',notes:'Repository controls, governance, schemas, work-order infrastructure, validation, and operating foundations.'},
      {id:2302,title:'WP-009 desktop spike',version:'WP-009',status:'closed',notes:'Desktop Tauri shell and platform evidence.'},
      {id:2303,title:'WP-010 Android spike',version:'WP-010',status:'closed',notes:'Android Tauri generation, build, emulator validation, and closure evidence.'},
      {id:2304,title:'WP-011 preparation baseline',version:'6e1a03d',status:'merged-open',notes:'Complete Windows-safe preparation; Apple validation gates remain open.'}
    ],
    migrations: [
      {id:2401,title:'Tauri CLI 2.8.4 → 2.11.4',status:'complete',impact:'Development generator only; aligned with locked Tauri 2.11 runtime. Android regeneration and tests passed.'},
      {id:2402,title:'WP-012 legacy shell packet → mobile-hard-gate decision',status:'complete',impact:'Prevents unauthorized broad UI implementation and preserves the approved P9-11 sequence.'}
    ],
    timeline: [
      {id:2501,title:'MS-01 governed repository foundation',status:'done',date:'2026-07-27',progress:100,dependsOn:''},
      {id:2502,title:'WP-009 Desktop Tauri Spike',status:'done',date:'2026-07-27',progress:100,dependsOn:'MS-01'},
      {id:2503,title:'WP-010 Android Tauri Spike',status:'done',date:'2026-07-28',progress:100,dependsOn:'WP-009'},
      {id:2504,title:'WP-011 Windows-compatible preparation',status:'done',date:'2026-07-28',progress:100,dependsOn:'WP-010'},
      {id:2505,title:'WP-011 borrowed-Mac Apple execution',status:'blocked',date:'2026-07-31',progress:15,dependsOn:'Borrowed supported Mac'},
      {id:2506,title:'WP-011 independent review and closure',status:'blocked',date:'',progress:0,dependsOn:'Apple execution evidence'},
      {id:2507,title:'WP-012 Evaluate Mobile Hard Gates',status:'blocked',date:'',progress:0,dependsOn:'WP-011 closure'},
      {id:2508,title:'WP-013 owner-checkpoint package',status:'blocked',date:'',progress:0,dependsOn:'WP-012 closure'},
      {id:2509,title:'WP-014 / MS-03',status:'unauthorized',date:'',progress:0,dependsOn:'Explicit owner authorization'}
    ],
    credits: {used:0,budget:100,entries:[]},
    settings: {
      githubRepo:'cybalicistjt-stack/Multiversal-app',
      githubToken:'',
      aiKey:'',
      owner:'John Brandon Turner',
      theme:'dark',
      autosnapshot:true
    }
  };

  const preserveArrays = ['worlds','worldtimeline','abilities','creatures','species','items','vehicles','quests','dialogue','storyflow','relationships','calendar','checkpoints'];
  for (const key of preserveArrays) {
    if (Array.isArray(current[key]) && current[key].length) seeded[key] = current[key];
  }
  if (current.focus) seeded.focus = current.focus;

  localStorage.setItem('aioc-state', JSON.stringify({...current, ...seeded}));
  localStorage.setItem('aioc-multiversal-seed', SEED_VERSION);
})();
