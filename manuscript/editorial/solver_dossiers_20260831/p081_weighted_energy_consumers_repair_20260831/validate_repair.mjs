import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

// Read-only validator: emits JSON; all saved artifacts are created separately
// through apply_patch. In particular, it never writes a manuscript file.
const dir=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const dossiers=path.dirname(dir);
const read=p=>fs.readFileSync(p,'utf8');
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:digest(b)};};
const baseFiles=['ch26_energy.tex','ch28_finite_energy_measures.tex'];
const expected=[
 '242f10b4c8be9e90bc457f897999f00d24d011a6c1b564436fe9c3a82f8d3d3d',
 '1bb59ce13a77fb7c6a2153f77e20eae7a340d84e727f2a76bb314c10c14b56a5'
];
const live=baseFiles.map(f=>path.join(root,'manuscript/parts/part3',f));
const full=baseFiles.map(f=>path.join(dir,'patched',f));
for(let i=0;i<live.length;i++)if(entry(live[i]).sha256!==expected[i])
 throw Error('Recorded live input changed: '+live[i]);
const fragments=['ch26_graph_replacement.tex','ch28_stability_replacement.tex',
 'ch28_dual_energy_replacement.tex'];
const core=fragments.map(f=>read(path.join(dir,f))).join('\n');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const oldLabels=live.flatMap(p=>labels(read(p)));
const newLabels=full.flatMap(p=>labels(read(p)));
if(new Set(newLabels).size!==newLabels.length)throw Error('Duplicate proposed label');
const missing=oldLabels.filter(l=>!newLabels.includes(l));
if(missing.length)throw Error('Old labels missing: '+missing.join(','));
for(let i=0;i<fragments.length;i++){
 const target=full[i===0?0:1];
 if(!read(target).includes(read(path.join(dir,fragments[i])).trim()))
  throw Error('Exact fragment absent from full copy: '+fragments[i]);
}
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(core)||/\tfrac/.test(core))
 throw Error('Control character or escaped-tab typo in core');

const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>
 e.isDirectory()?walk(path.join(d,e.name)):
 e.name.endsWith('.tex')?[path.join(d,e.name)]:[]);
const manuscriptFiles=[...walk(path.join(root,'manuscript/parts')),
 ...walk(path.join(root,'manuscript/appendices'))];
const revised31=path.join(dossiers,
 'p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/ch31_curve_replacement.tex');
if(entry(revised31).sha256!==
 'eafd97355fda0739ec1135b36b247c43a6816ac754e4d154d9acf9168bae4b5d')
 throw Error('Frozen elementary graph source changed');
const labelOwners=new Map();
for(const p of [...manuscriptFiles,revised31,...full])
 for(const l of labels(read(p)))labelOwners.set(l,p);
const coreLabels=labels(core);
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)]
 .flatMap(m=>m[1].split(','));
const external=[...new Set(refs.filter(l=>!coreLabels.includes(l)))].sort();
const unresolved=external.filter(l=>!labelOwners.has(l));
if(unresolved.length)throw Error('Missing external label: '+unresolved.join(','));
const stubs='% Mechanical reference placeholders only; not input statements.\n'+
 '\\begingroup\\refstepcounter{theorem}\n'+
 external.map(l=>'\\label{'+l+'}').join('\n')+'\n\\endgroup\n';
const diff=(a,b,name)=>{
 try{return execFileSync('diff',['-u','--label','a/manuscript/parts/part3/'+name,
  '--label','b/manuscript/parts/part3/'+name,a,b],{encoding:'utf8'});}
 catch(e){if(e.status===1)return e.stdout;throw e;}
};
const patch=baseFiles.map((f,i)=>diff(live[i],full[i],f)).join('');
const inputOwners=[...new Set(external.map(l=>labelOwners.get(l)))];
const referenceMap=external.map(label=>({label,path:labelOwners.get(label)}));
if(process.argv.includes('--prepare')){
 console.log(JSON.stringify({external_reference_stubs:stubs,patch,referenceMap,
  old_labels:oldLabels.length,new_labels:newLabels.length},null,2));
 process.exit(0);
}
if(read(path.join(dir,'external_reference_stubs.tex'))!==stubs)
 throw Error('Reference placeholder bytes changed');
if(read(path.join(dir,'combined.patch'))!==patch)throw Error('Patch bytes mismatch');
execFileSync('git',['apply','--check',path.join(dir,'combined.patch')],{cwd:root});
const log=read(path.join(dir,'build/compile_check.log'));
if(!log.includes('pdfdraftmode enabled'))throw Error('Expected draftmode compile');
const diagnostics=log.split('\n').filter(l=>/Warning|Overfull|Underfull|undefined/.test(l));
if(diagnostics.length)throw Error('Compile diagnostics: '+diagnostics.join('\n'));
const validation={date:'2026-08-31',status:'isolated author repair, independent review pending',
 old_labels:oldLabels.length,new_labels:newLabels.length,missing_labels:missing,
 exact_fragments_in_full_copies:true,external_core_reference_occurrences:refs.length,
 unresolved_external_labels:unresolved,live_input_hashes_unchanged:true,
 patch_matches_full_copies:true,git_apply_check:'passed; check only, not applied',
 syntax_compile:'draftmode only; external references are mechanical placeholders',
 compile_diagnostics:diagnostics,full_book_compile:false,production_submitted:false,
 independent_mathematical_verdict:'pending root review; author is not independent reviewer',
 referenceMap};
const reportInputs=[
 path.join(dossiers,'p081_ch29_ch31_assembled_independent_audit_20260831/INDEPENDENT_ASSEMBLY_AUDIT.md'),
 path.join(dossiers,'p081_ch29_ch31_assembled_independent_audit_20260831/MANIFEST.json'),
 path.join(dossiers,'p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/MANIFEST.json')
];
const outputs=[...fragments,'patched/ch26_energy.tex','patched/ch28_finite_energy_measures.tex',
 'GATE.md','SOURCE_AND_CHANGE_LEDGER.md','compile_check.tex','external_reference_stubs.tex',
 'combined.patch','validate_repair.mjs','build/compile_check.log'].map(f=>entry(path.join(dir,f)));
const validationBytes=Buffer.from(JSON.stringify(validation,null,2)+'\n');
outputs.push({path:path.join(dir,'VALIDATION.json'),bytes:validationBytes.length,
 sha256:digest(validationBytes)});
const manifest={date:'2026-08-31',status:validation.status,
 outputs,base_chapters:live.map(entry),
 mathematical_and_reference_inputs:[...new Set([...inputOwners,revised31,...reportInputs])].map(entry),
 note:'No self-hash; existing input interfaces, not entire input chapters, are used. All scripts are read-only.'};
console.log(JSON.stringify({validation,manifest},null,2));
