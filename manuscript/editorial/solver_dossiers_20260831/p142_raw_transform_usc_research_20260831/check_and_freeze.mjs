import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const manuscript=path.join(root,'manuscript');
const scratch='/var/folders/_r/yk2xmp3x0zvgyvv1yxpn25br0000gn/T/nappt-p142-syntax-20260831-ufxa0d';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>({path:p,bytes:fs.statSync(p).size,sha256:sha(fs.readFileSync(p))});
const write=(name,data)=>fs.writeFileSync(path.join(here,name),data,{flag:'wx'});
const labels=['prop:pseff-ideal-valuative-basic','eq:ts-evaluation','thm:pseff-perturbation-independent-transform'];
const inputAuxes=['parts/part6/ch71_pseudoeffective_mp_dxz.aux','parts/part5/ch58_tropical_spectra.aux'].map(p=>path.join(manuscript,p));
const auxLines=inputAuxes.flatMap(p=>fs.readFileSync(p,'utf8').split('\n'));
const refs=labels.flatMap(label=>[label,label+'@cref'].map(key=>{
 const found=auxLines.filter(s=>s.startsWith('\\newlabel{'+key+'}'));
 if(found.length!==1)throw Error('external label not unique '+key);
 return found[0];
}));
write('external_refs.aux','\\relax\n'+refs.join('\n')+'\n');
write('EXTERNAL_REFERENCES.json',JSON.stringify({sources:inputAuxes.map(record),labels,kind:'exact six-line extraction, not a new proof of the imported assertions'},null,2)+'\n');
fs.copyFileSync(path.join(scratch,'compile.log'),path.join(here,'draft_attempt1.log'),fs.constants.COPYFILE_EXCL);
const runs=[];
const texInput=path.relative(manuscript,path.join(here,'compile.tex'));
for(const [kind,args,cwd] of [
 ['latex',['-draftmode','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+scratch,texInput],manuscript],
 ['bibtex',[path.join(scratch,'compile')],manuscript],
 ['latex',['-draftmode','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+scratch,texInput],manuscript],
 ['latex',['-draftmode','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+scratch,texInput],manuscript]
]){
 const binary=kind==='latex'?'/Library/TeX/texbin/pdflatex':'/Library/TeX/texbin/bibtex';
 const r=spawnSync(binary,args,{cwd,encoding:'utf8',maxBuffer:20*1024*1024});
 const i=runs.length+1;
 write('draft_run'+i+'.out',r.stdout+'\n'+r.stderr);
 const run={kind,binary,args,cwd,exitCode:r.status,output:record(path.join(here,'draft_run'+i+'.out'))};
 runs.push(run);
 if(r.status!==0){write('BUILD_FAILED.json',JSON.stringify({scratch,runs},null,2)+'\n');throw Error(kind+' failed; inspect frozen output');}
}
const log=fs.readFileSync(path.join(scratch,'compile.log'),'utf8');
fs.copyFileSync(path.join(scratch,'compile.log'),path.join(here,'draft_final.log'),fs.constants.COPYFILE_EXCL);
fs.copyFileSync(path.join(scratch,'compile.bbl'),path.join(here,'compile.bbl'),fs.constants.COPYFILE_EXCL);
const warnings=log.split('\n').filter(l=>/Warning|Overfull|Underfull|^!/.test(l));
const texFiles=['statement.tex','proof.tex','example.tex'];
const all=texFiles.map(p=>fs.readFileSync(path.join(here,p),'utf8')).join('\n');
const allLabels=[...all.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(allLabels).size!==allLabels.length)throw Error('duplicate label');
if(/\\(?:ref|autoref)\{/.test(all))throw Error('bare internal ref');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(all))throw Error('control byte');
if(fs.existsSync(path.join(scratch,'compile.pdf')))throw Error('unexpected PDF');
write('BUILD.json',JSON.stringify({date:'2026-08-31',mode:'draft syntax check only; no PDF',scratch,runs,warnings,labels:allLabels,externalReferences:labels,pdfProduced:false,scope:'standalone proof packet, not a full manuscript build or mathematical verification'},null,2)+'\n');
if(warnings.some(s=>/undefined|Rerun|Label\(s\).*changed|Overfull/.test(s)))throw Error('unresolved draft warning: inspect BUILD.json');
const inputs=[
 'parts/part6/ch71_pseudoeffective_mp_dxz.tex',
 'parts/part6/ch72_major_open_problems.tex',
 'parts/part5/ch52_rays_test_curves.tex',
 'parts/part5/ch53_transcendental_metrics.tex',
 'parts/part5/ch58_tropical_spectra.tex',
 'editorial/open_problem_atomic_inventory_20260824.md',
 'bibliography/ComplexGeometry.bib'
].map(p=>record(path.join(manuscript,p)));
write('PARENT_INPUTS.json',JSON.stringify(inputs,null,2)+'\n');
const entries=fs.readdirSync(here,{withFileTypes:true}).filter(e=>e.isFile()&&e.name!=='MANIFEST.json').map(e=>({name:e.name,...record(path.join(here,e.name))}));
write('MANIFEST.json',JSON.stringify({date:'2026-08-31',kind:'frozen isolated candidate; independent and production gates pending',files:entries},null,2)+'\n');
console.log(JSON.stringify({frozen:true,files:entries.length,statement:record(path.join(here,'statement.tex')),proof:record(path.join(here,'proof.tex')),example:record(path.join(here,'example.tex')),manifest:record(path.join(here,'MANIFEST.json')),warnings},null,2));
