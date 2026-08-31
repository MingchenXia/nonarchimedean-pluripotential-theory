import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const dir=path.dirname(fileURLToPath(import.meta.url));
const original=path.dirname(dir);
const root='/private/tmp/nappt_p071_20260827';
const dossiers=path.join(root,'manuscript/editorial/solver_dossiers_20260831');
const weighted=path.join(dossiers,'p081_weighted_curve_green_reference_audit_20260831');
const envelope=path.join(dossiers,'p081_part3_curve_envelope_scope_repair_candidate_20260831');
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const hash=p=>digest(fs.readFileSync(p));
const entry=p=>({path:p,bytes:fs.statSync(p).size,sha256:hash(p)});
const read=p=>fs.readFileSync(p,'utf8');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const freeze=(p,h)=>{if(hash(p)!==h)throw Error('Frozen input changed: '+p);};
const sourceHashes=[
 [path.join(weighted,'statement.tex'),'010711e1a42f4d3ad16ab9b7eb6233a585a1e410ddc420b8b6d70cf0c7c4fc71'],
 [path.join(weighted,'proof.tex'),'b62af8ed2a33650e2385bc82203a71a124a5a04b85ae4297b34c29d484cdad94'],
 [path.join(weighted,'revised1/statement.tex'),'010711e1a42f4d3ad16ab9b7eb6233a585a1e410ddc420b8b6d70cf0c7c4fc71'],
 [path.join(weighted,'revised1/proof.tex'),'30af723c7f07a201ffe4e7a57227867a612cd4cf425fff800babb1db3f18ee3d'],
 [path.join(envelope,'revised1/statement.tex'),'944fc4672a83bf038b068af1a70da1563b4950752ee1eb5ae89ee2f4b2db0b30'],
 [path.join(envelope,'revised1/proof.tex'),'bd98ca99d636a1f40872412e2ababc7f44a5ccb5416b31bcbd83b957515031d6']
];
for(const[p,h]of sourceHashes)freeze(p,h);
freeze(path.join(original,'MANIFEST.json'),'0e0f870b5f1aa6208b72ae9512915923a05c8b74b8b506b44d2861069b44afb3');
freeze(path.join(original,'VALIDATION.json'),'68c923b7a5647547b65bde717bbdb854e26b90e1db4fc2d76804357409547b8e');
const oldManifest=JSON.parse(read(path.join(original,'MANIFEST.json')));
const originalEntries=Object.values(oldManifest).filter(Array.isArray).flat().filter(e=>e&&typeof e==='object'&&e.path&&e.sha256);
for(const e of originalEntries){
 freeze(e.path,e.sha256);
 if(fs.statSync(e.path).size!==e.bytes)throw Error('Frozen size changed: '+e.path);
}
const base='4ec9fb514e9d33d0f8e1b6d918d6264a104cb676';
const chapters=['ch29_continuity.tex','ch31_bfj_examples.tex'];
const live=chapters.map(f=>path.join(root,'manuscript/parts/part3',f));
for(const p of live){
 const bytes=execFileSync('git',['show',base+':'+path.relative(root,p)],{cwd:root});
 if(!bytes.equals(fs.readFileSync(p)))throw Error('Live chapter differs from recorded base: '+p);
}
const otherChapter=path.join(root,'manuscript/parts/part3/ch23_bfj_envelopes.tex');
freeze(otherChapter,'f311c1dc6f375f98d09e5a076997ebe8c7e5ce836f3efbb686b48afabd87a228');
const full=chapters.map(f=>path.join(dir,'patched',f));
const oldLabels=live.flatMap(p=>labels(read(p)));
const firstLabels=chapters.flatMap(f=>labels(read(path.join(original,'patched',f))));
const newLabels=full.flatMap(p=>labels(read(p)));
if(new Set(newLabels).size!==newLabels.length)throw Error('Duplicate proposed chapter label');
const missingOld=oldLabels.filter(l=>!newLabels.includes(l));
const missingFirst=firstLabels.filter(l=>!newLabels.includes(l));
if(missingOld.length||missingFirst.length)throw Error('Earlier label lost: '+[...missingOld,...missingFirst]);
const fragments=['ch29_curve_replacement.tex','ch31_curve_replacement.tex'];
for(let i=0;i<2;i++){
 const oldFragment=read(path.join(original,fragments[i]));
 const newFragment=read(path.join(dir,fragments[i]));
 if(!read(full[i]).includes(newFragment.trim()))throw Error('Exact fragment absent in full copy');
 const expectedFull=read(path.join(original,'patched',chapters[i])).replace(oldFragment,newFragment);
 if(expectedFull!==read(full[i]))throw Error('Change outside revised fragment relative to frozen full copy: '+chapters[i]);
}
const core=[...fragments,'inputs.tex'].map(f=>read(path.join(dir,f))).join('\n');
const coreLabels=labels(core);
if(new Set(coreLabels).size!==coreLabels.length)throw Error('Duplicate core label');
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const missingRefs=refs.filter(r=>!coreLabels.includes(r));
if(missingRefs.length)throw Error('Missing local reference: '+missingRefs);
const keys=[...read(path.join(dir,'sources.bib')).matchAll(/@\w+\s*\{([^,]+),/g)].map(m=>m[1]);
const citations=[...core.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(citations.some(k=>!keys.includes(k)))throw Error('Missing bibliography key');
if(/\\int_G/.test(read(path.join(dir,'ch31_curve_replacement.tex'))))throw Error('Unmapped Ch31 graph name');
if(/rational piecewise affine function, hence/.test(core))throw Error('Old invalid rational-mass inference retained');
for(const required of ['edge-simple path','eq:ch31-real-local-curvature','ex:ch31-nonsplit-weight-normalization','ex:ch31-rational-mass-irrational-slope','not to reflect it']){
 if(!core.includes(required))throw Error('Required repair missing: '+required);
}
const log=read(path.join(dir,'build/compile_check.log'));
const diagnostics=log.split('\n').filter(l=>/Warning|Overfull|Underfull|undefined/.test(l));
if(diagnostics.length)throw Error('Compile diagnostics: '+diagnostics.join('\n'));
if(!log.includes('pdfdraftmode enabled'))throw Error('Compile was not in draft mode');
const buildFiles=fs.readdirSync(path.join(dir,'build')).sort();
if(buildFiles.some(f=>f.endsWith('.pdf')))throw Error('New PDF unexpected; visual-QA not performed');
execFileSync('git',['apply','--check',path.join(dir,'combined.patch')],{cwd:root});
const expectedDiff=(before,after,left,right)=>{
 try { return execFileSync('diff',['-u','--label',left,'--label',right,before,after],{encoding:'utf8'}); }
 catch(e){if(e.status===1)return e.stdout;throw e;}
};
const checkCombined=chapters.map((f,i)=>expectedDiff(live[i],full[i],'a/manuscript/parts/part3/'+f,'b/manuscript/parts/part3/'+f)).join('');
const checkFragments=fragments.map(f=>expectedDiff(path.join(original,f),path.join(dir,f),'a/'+f,'b/'+f)).join('');
if(read(path.join(dir,'combined.patch'))!==checkCombined)throw Error('Combined patch byte mismatch');
if(read(path.join(dir,'fragments_from_frozen.patch'))!==checkFragments)throw Error('Fragment patch byte mismatch');

const validation={
 date:'2026-08-31',status:'frozen isolated revised2 author candidate; independent and production review pending',
 base_commit:base,original_manifest_entries_checked:originalEntries.length,
 original_assembly_unchanged:true,underlying_weighted_and_F_core_hashes_unchanged:true,
 live_Ch29_Ch31_unchanged:true,live_Ch23_unchanged:true,
 original_chapter_labels:oldLabels.length,first_assembly_labels:firstLabels.length,proposed_chapter_labels:newLabels.length,
 old_labels_missing:missingOld,first_assembly_labels_missing:missingFirst,
 core_labels:coreLabels.length,core_reference_occurrences:refs.length,core_citation_occurrences:citations.length,
 exact_fragment_to_fullcopy_match:true,no_other_changes_to_first_assembly_fullcopies:true,
 exact_combined_and_fragment_diffs:true,
 latex_mode:'draftmode, no new PDF',latex_diagnostics:diagnostics,
 git_apply_check:'passed; check only, not applied',
 weighted_independent:'prior revised1 packet audit only, conditional on accepted P063/P081; not an assembly endorsement',
 revised2_independent:'pending exact-byte mathematical review, including both new examples',
 production:'not submitted; permission gate unresolved; sol/xhigh required for all new mathematics',
 cross_chapter_consumers:'separate Ch23 repair and reported Ch26/Ch28 weighted-energy mismatch remain integration gates',
 full_manuscript_compile:'not performed; future release gate',open_problem_retirement_claim:false
};
const authored=['ch29_curve_replacement.tex','ch31_curve_replacement.tex','patched/ch29_continuity.tex','patched/ch31_bfj_examples.tex','combined.patch','fragments_from_frozen.patch','GATE.md','REVISION_LEDGER.md','inputs.tex','sources.bib','compile_check.tex','validate_revised2.mjs'];
const outputs=[...authored,...buildFiles.map(f=>'build/'+f)].map(f=>entry(path.join(dir,f)));
const validationBytes=Buffer.from(JSON.stringify(validation,null,2)+'\n');
outputs.push({path:path.join(dir,'VALIDATION.json'),bytes:validationBytes.length,sha256:digest(validationBytes)});
const supporting=[
 path.join(original,'MANIFEST.json'),path.join(original,'VALIDATION.json'),
 path.join(weighted,'revised1/MANIFEST.json'),path.join(weighted,'revised1/SOURCE_MATRIX.md'),
 path.join(envelope,'SOURCE_MATRIX.md'),path.join(envelope,'DEPENDENCY_AND_CORRECTION_LEDGER.md'),
 path.join(envelope,'revised1/REVISION_NOTE.md'),
 path.join(dossiers,'p081_ch29_ch31_pedagogy_review_20260831/PEDAGOGY_FINDINGS.md')
].map(entry);
const manifest={
 date:'2026-08-31',status:validation.status,base_commit:base,
 outputs,base_chapters:live.map(entry),untouched_Ch23:entry(otherChapter),
 frozen_math_inputs:sourceHashes.map(([p])=>entry(p)),supporting_ledgers:supporting,
 note:'Manifest excludes its own self-hash; validator is read-only and emits this JSON without writing files.'
};
console.log(JSON.stringify({validation,manifest},null,2));
