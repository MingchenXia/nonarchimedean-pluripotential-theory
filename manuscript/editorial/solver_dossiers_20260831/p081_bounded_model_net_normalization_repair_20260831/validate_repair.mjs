import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

// Read-only checker. It emits JSON to stdout and never writes or applies a patch.
const dir=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const read=p=>fs.readFileSync(p,'utf8');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const part=path.join(root,'manuscript/parts/part3');
const dossiers=path.dirname(dir);
const graph=path.join(dossiers,'p081_weighted_energy_consumers_repair_20260831/ch26_graph_replacement.tex');
const edits=JSON.parse(read(path.join(dir,'assembly_edits.json')));
const fixedInputs=[
 [edits[0].parent,'8552d7b5e4c5c58cf48e94db28bf44f3286af4f997adf3f4716cee52d8f26d28'],
 [path.join(part,'ch26_energy.tex'),'242f10b4c8be9e90bc457f897999f00d24d011a6c1b564436fe9c3a82f8d3d3d'],
 [path.join(part,'ch30_functoriality.tex'),'61957fd06cf4cd24833cd5d7d698b9aa8640d9d094ca7d8237a235be395bf951'],
 [graph,'32162fefceffa938272c9e7230206496538c5a52290083d6573f3d1faf31ff31']
];
for(const [p,h] of fixedInputs)if(entry(p).sha256!==h)throw Error('Input bytes changed: '+p);
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const reports=[];
for(const e of edits){
 const before=read(e.parent),after=read(path.join(dir,'patched',e.chapter));
 if(before.split(e.old).length!==2)throw Error('Nonunique source fragment: '+e.name);
 if(e.replacement!==read(path.join(dir,e.fragment))+'\n')throw Error('Fragment/assembly mismatch: '+e.name);
 if(before.replace(e.old,e.replacement)!==after)throw Error('Full copy/assembly mismatch: '+e.name);
 const oldLabels=labels(before),newLabels=labels(after);
 if(oldLabels.some(l=>!newLabels.includes(l)))throw Error('Lost label: '+e.chapter);
 if(new Set(newLabels).size!==newLabels.length)throw Error('Duplicate label: '+e.chapter);
 const kind=e.chapter.startsWith('ch26')?'proposition':'theorem';
 const prefix=s=>s.slice(0,s.indexOf('\\end{'+kind+'}')+('\\end{'+kind+'}').length);
 if(prefix(e.old)!==prefix(e.replacement))throw Error('Theorem statement changed: '+e.chapter);
 reports.push({chapter:e.chapter,parent:entry(e.parent),fragment:entry(path.join(dir,e.fragment)),
  full:entry(path.join(dir,'patched',e.chapter)),oldLabels:oldLabels.length,newLabels:newLabels.length,
  addedLabels:newLabels.filter(l=>!oldLabels.includes(l)),statementUnchanged:true,
  unchangedOutsideReplacement:true});
}
const full26=read(path.join(dir,'patched/ch26_energy.tex'));
if(!full26.includes(read(graph)))throw Error('Frozen weighted graph fragment not preserved');
const full30=read(path.join(dir,'patched/ch30_functoriality.tex'));
if(!full30.includes('monotonicity of a net only after passing to the net of finite minima'))
 throw Error('Excluded descent passage changed');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?
 walk(path.join(d,e.name)):e.name.endsWith('.tex')?[path.join(d,e.name)]:[]);
const owners=new Map();
for(const p of [...walk(path.join(root,'manuscript/parts')),
 ...walk(path.join(root,'manuscript/appendices')),
 path.join(dir,'patched/ch26_energy.tex'),path.join(dir,'patched/ch30_functoriality.tex')])
 for(const l of labels(read(p)))owners.set(l,p);
const core=edits.map(e=>e.replacement).join('\n');
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const external=[...new Set(refs.filter(l=>!labels(core).includes(l)))].sort();
if(external.some(l=>!owners.has(l)))throw Error('Unknown external reference');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(core))throw Error('Control character in replacement');
const diff=(a,b,label)=>{
 try{return execFileSync('diff',['-u','--label','a/'+label,'--label','b/'+label,a,b],{encoding:'utf8'});}
 catch(e){if(e.status!==1)throw e;return e.stdout;}
};
const incremental=edits.map(e=>diff(e.parent,path.join(dir,'patched',e.chapter),'manuscript/parts/part3/'+e.chapter)).join('');
const combined=edits.map(e=>diff(path.join(part,e.chapter),path.join(dir,'patched',e.chapter),'manuscript/parts/part3/'+e.chapter)).join('');
for(const [name,expected] of [['incremental_overlay.patch',incremental],['combined_live.patch',combined]])
 if(fs.existsSync(path.join(dir,name))&&read(path.join(dir,name))!==expected)throw Error('Saved patch differs: '+name);
let patchCheck='not yet saved';
if(fs.existsSync(path.join(dir,'combined_live.patch'))){
 execFileSync('git',['apply','--check',path.join(dir,'combined_live.patch')],{cwd:root});
 patchCheck='git apply --check passed; no patch applied';
}
const sources=[...new Set([...fixedInputs.map(e=>e[0]),
 ...external.map(l=>owners.get(l)).filter(p=>!p.startsWith(dir+'/')),
 path.join(part,'ch20_model_forms.tex'),path.join(part,'ch21_bfj_psh.tex'),
 path.join(part,'ch22_compactness.tex'),path.join(part,'ch24_bfj_ma.tex')])].map(entry);
if(fs.existsSync(path.join(dir,'SOURCE_HASHES.json')))
 for(const e of JSON.parse(read(path.join(dir,'SOURCE_HASHES.json'))))
  if(entry(e.path).sha256!==e.sha256)throw Error('Frozen source changed: '+e.path);
const stubs='% Mechanical reference placeholders for draft syntax only.\n'+
 '\\begingroup\\refstepcounter{theorem}\n'+external.map(l=>'\\label{'+l+'}').join('\n')+'\n\\endgroup\n';
const report={status:'mechanical author checks only; independent and production review pending',
 chapters:reports,weightedGraphPreserved:entry(graph),excludedDescentUnchanged:true,
 externalReferences:external.length,referenceMap:external.map(label=>({label,path:owners.get(label)})),
 sources,combinedPatchCheck:patchCheck,incrementalPatchBase:'frozen Ch26 weighted overlay plus live Ch30',
 noLiveWrites:true,noProductionCalls:true};
process.stdout.write(JSON.stringify({report,incremental,combined,stubs},null,2));
