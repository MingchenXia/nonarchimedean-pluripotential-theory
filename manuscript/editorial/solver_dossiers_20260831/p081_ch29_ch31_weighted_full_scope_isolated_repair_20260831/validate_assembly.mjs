import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const dossiers=path.join(root,'manuscript/editorial/solver_dossiers_20260831');
const weighted=path.join(dossiers,'p081_weighted_curve_green_reference_audit_20260831');
const envelope=path.join(dossiers,'p081_part3_curve_envelope_scope_repair_candidate_20260831');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const entry=p=>({path:p,bytes:fs.statSync(p).size,sha256:hash(p)});
const read=p=>fs.readFileSync(p,'utf8');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const expectedInputs=[
 [path.join(weighted,'statement.tex'),'010711e1a42f4d3ad16ab9b7eb6233a585a1e410ddc420b8b6d70cf0c7c4fc71'],
 [path.join(weighted,'proof.tex'),'b62af8ed2a33650e2385bc82203a71a124a5a04b85ae4297b34c29d484cdad94'],
 [path.join(weighted,'revised1/statement.tex'),'010711e1a42f4d3ad16ab9b7eb6233a585a1e410ddc420b8b6d70cf0c7c4fc71'],
 [path.join(weighted,'revised1/proof.tex'),'30af723c7f07a201ffe4e7a57227867a612cd4cf425fff800babb1db3f18ee3d'],
 [path.join(envelope,'revised1/statement.tex'),'944fc4672a83bf038b068af1a70da1563b4950752ee1eb5ae89ee2f4b2db0b30'],
 [path.join(envelope,'revised1/proof.tex'),'bd98ca99d636a1f40872412e2ababc7f44a5ccb5416b31bcbd83b957515031d6']
];
for(const[p,h]of expectedInputs)if(hash(p)!==h)throw Error('Frozen input changed: '+p);
const base='4ec9fb514e9d33d0f8e1b6d918d6264a104cb676';
const baseChapters=['ch29_continuity.tex','ch31_bfj_examples.tex'].map(f=>path.join(root,'manuscript/parts/part3',f));
for(const p of baseChapters){
 const rel=path.relative(root,p);
 const baseBytes=execFileSync('git',['show',base+':'+rel],{cwd:root});
 if(!baseBytes.equals(fs.readFileSync(p)))throw Error('Live chapter differs from base: '+p);
}
const patched=['patched/ch29_continuity.tex','patched/ch31_bfj_examples.tex'].map(p=>path.join(dir,p));
const allOld=baseChapters.flatMap(p=>labels(read(p)));
const allNew=patched.flatMap(p=>labels(read(p)));
const missing=allOld.filter(l=>!allNew.includes(l));
if(missing.length)throw Error('Old labels missing: '+missing);
if(new Set(allNew).size!==allNew.length)throw Error('Duplicate label in assembled chapters');
for(const[f,full]of [['ch29_curve_replacement.tex',patched[0]],['ch31_curve_replacement.tex',patched[1]]]){
 if(!read(full).includes(read(path.join(dir,f)).trim()))throw Error('Full chapter does not contain exact fragment: '+f);
}
const core=['ch29_curve_replacement.tex','ch31_curve_replacement.tex','inputs.tex'].map(p=>read(path.join(dir,p))).join('\n');
const coreLabels=labels(core);
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(new Set(coreLabels).size!==coreLabels.length)throw Error('Duplicate core label');
if(refs.some(r=>!coreLabels.includes(r)))throw Error('Missing local reference: '+refs.filter(r=>!coreLabels.includes(r)));
const bib=read(path.join(dir,'sources.bib'));
const keys=[...bib.matchAll(/@\w+\s*\{([^,]+),/g)].map(m=>m[1]);
const citations=[...core.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(citations.some(k=>!keys.includes(k)))throw Error('Missing bibliography key');
if(/\\int_G/.test(read(path.join(dir,'ch31_curve_replacement.tex'))))throw Error('Unmapped graph name');
if(/rational piecewise affine function, hence/.test(core))throw Error('Invalid rational mass promotion retained');
if(!core.includes('edge-simple path'))throw Error('Missing path-energy correction');
const log=read(path.join(dir,'build/compile_check.log'));
const diagnostics=log.split('\n').filter(l=>/Warning|Overfull|Underfull|undefined/.test(l));
if(diagnostics.length)throw Error('Compile diagnostics: '+diagnostics.join('\n'));
if(fs.existsSync(path.join(dir,'build/compile_check.pdf')))throw Error('Assembly check expected draft mode only');
execFileSync('git',['apply','--check',path.join(dir,'combined.patch')],{cwd:root});
const validation={
 date:'2026-08-31',status:'isolated proposal, not production approved',base_commit:base,
 frozen_input_hashes_verified:true,live_chapters_unchanged:true,
 original_chapter_labels:allOld.length,proposed_chapter_labels:allNew.length,
 old_labels_missing:missing,core_labels:coreLabels.length,core_reference_occurrences:refs.length,
 core_citation_occurrences:citations.length,latex_mode:'draftmode; no new assembly PDF',
 latex_diagnostics:diagnostics,git_apply_check:'passed; check only, not applied',
 weighted_independent:'exact revised1 accepted in auditor task messages conditional on accepted P063/P081; no independent report file',
 assembled_independent:'pending; weighted audit does not endorse assembled files',
 production:'not submitted; permission gate unresolved',full_manuscript_compile:'not performed; future release gate',
 open_problem_retirement_claim:false
};
const outputs=['ch29_curve_replacement.tex','ch31_curve_replacement.tex','patched/ch29_continuity.tex','patched/ch31_bfj_examples.tex','combined.patch','GATE.md','ASSEMBLY_AUDIT.md','inputs.tex','sources.bib','compile_check.tex','validate_assembly.mjs','build/compile_check.log'].map(p=>entry(path.join(dir,p)));
const supporting=[path.join(weighted,'revised1/MANIFEST.json'),path.join(weighted,'revised1/SOURCE_MATRIX.md'),path.join(envelope,'SOURCE_MATRIX.md'),path.join(envelope,'DEPENDENCY_AND_CORRECTION_LEDGER.md'),path.join(envelope,'revised1/REVISION_NOTE.md')].map(entry);
console.log(JSON.stringify({validation,manifest:{date:'2026-08-31',status:validation.status,base_commit:base,outputs,base_chapters:baseChapters.map(entry),frozen_math_inputs:expectedInputs.map(([p])=>entry(p)),supporting_ledgers:supporting}},null,2));
