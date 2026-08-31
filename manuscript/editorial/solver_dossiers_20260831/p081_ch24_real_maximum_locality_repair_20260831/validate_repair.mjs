import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
// Read-only checks. All generated text is emitted, never written here.
const dir=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const dossiers=path.dirname(dir);
const parent=path.join(dossiers,'p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch24_bfj_ma.tex');
const live=path.join(root,'manuscript/parts/part3/ch24_bfj_ma.tex');
const up=path.join(dossiers,'p081_ch20_ch21_real_model_max_repair_20260831');
const full=path.join(dir,'patched/ch24_bfj_ma.tex');
const read=p=>fs.readFileSync(p,'utf8');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const fixed=[
 [parent,'391930d26a49779b10a96ac7e381fefade0677642669e7a20e93c7902e660eae'],
 [live,'6fba68089c9ed14700f6944e8409b7b477d91478ec3eee5fcabe6c6b5b152916'],
 [path.join(up,'rational_approximation.tex'),'f857bbc52b34d75e9dcd3047fa0b55c79a052d7377732ce61f8d7038984b1572'],
 [path.join(up,'patched/ch20_model_forms.tex'),'7b287229f071aceeaa8396a8ea00bd6f6d70a566f67bdd452fc72bd2281fb586'],
 [path.join(up,'patched/ch21_bfj_psh.tex'),'957e2a2d16ff85c036aa42c1647aa055f56767fb9973a02b34d4853899d39310']
];
for(const [p,h] of fixed)if(entry(p).sha256!==h)throw Error('Frozen input changed: '+p);
const edits=JSON.parse(read(path.join(dir,'assembly_edits.json')));
let assembled=read(parent);
for(const e of edits){
 if(assembled.split(e.old).length!==2)throw Error('Nonunique edit: '+e.name);
 if(e.fragment){
  if(e.replacement!==read(path.join(dir,e.fragment))+'\n')throw Error('Fragment mismatch');
  const kind=e.fragment==='open_locality_replacement.tex'?'corollary':'proposition';
  const prefix=s=>s.slice(0,s.indexOf('\\end{'+kind+'}')+('\\end{'+kind+'}').length);
  if(prefix(e.old)!==prefix(e.replacement))throw Error('Original statement changed');
 }
 assembled=assembled.replace(e.old,e.replacement);
}
if(assembled!==read(full))throw Error('Full copy differs from exact assembly');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const before=labels(read(parent)),after=labels(read(full));
if(before.some(l=>!after.includes(l))||new Set(after).size!==after.length)throw Error('Label loss or duplication');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):
 e.name.endsWith('.tex')?[path.join(d,e.name)]:[]);
const owners=new Map();
for(const p of [...walk(path.join(root,'manuscript/parts')),...walk(path.join(root,'manuscript/appendices')),
 path.join(up,'patched/ch20_model_forms.tex'),path.join(up,'patched/ch21_bfj_psh.tex'),full])
 for(const l of labels(read(p)))owners.set(l,p);
const core=edits.map(e=>e.replacement).join('\n');
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const external=[...new Set(refs.filter(l=>!labels(core).includes(l)))].sort();
if(external.some(l=>!owners.has(l)))throw Error('Unknown reference');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(core))throw Error('Control character');
const diff=base=>{try{return execFileSync('diff',['-u','--label','a/manuscript/parts/part3/ch24_bfj_ma.tex',
 '--label','b/manuscript/parts/part3/ch24_bfj_ma.tex',base,full],{encoding:'utf8'});}
 catch(e){if(e.status!==1)throw e;return e.stdout;}};
const incremental=diff(parent),combined=diff(live);
for(const [name,value] of [['incremental_overlay.patch',incremental],['combined_live.patch',combined]])
 if(fs.existsSync(path.join(dir,name))&&read(path.join(dir,name))!==value)throw Error('Patch changed: '+name);
let check='not yet saved';
if(fs.existsSync(path.join(dir,'combined_live.patch'))){
 execFileSync('git',['apply','--check',path.join(dir,'combined_live.patch')],{cwd:root});
 check='git apply --check passed; no patch applied';
}
const sourcePaths=[...new Set([...fixed.map(e=>e[0]),...external.map(l=>owners.get(l)).filter(p=>p!==full)])];
const sources=sourcePaths.map(entry);
if(fs.existsSync(path.join(dir,'SOURCE_HASHES.json')))
 for(const e of JSON.parse(read(path.join(dir,'SOURCE_HASHES.json'))))
  if(entry(e.path).sha256!==e.sha256)throw Error('Recorded source changed');
const stubs='% Draft placeholders only; not source assertions.\n\\begingroup\\refstepcounter{theorem}\n'+
 external.map(l=>'\\label{'+l+'}').join('\n')+'\n\\endgroup\n';
const report={status:'isolated author mechanical checks; independent and production review pending',
 parent:entry(parent),live:entry(live),full:entry(full),fragments:edits.filter(e=>e.fragment).map(e=>entry(path.join(dir,e.fragment))),
 edits:edits.map(e=>e.name),oldLabels:before.length,newLabels:after.length,
 originalStatementsUnchanged:true,allLabelsPreserved:true,unchangedOutsideExactEdits:true,
 earlierWeightedChangesPreserved:true,externalReferences:external.length,
 referenceMap:external.map(label=>({label,path:owners.get(label)})),sources,
 patchCheck:check,noLiveWrites:true,noProductionCalls:true};
process.stdout.write(JSON.stringify({report,incremental,combined,stubs},null,2));
