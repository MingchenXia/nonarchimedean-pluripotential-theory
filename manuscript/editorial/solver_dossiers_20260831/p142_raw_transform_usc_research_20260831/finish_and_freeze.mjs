import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const manuscript='/private/tmp/nappt_p071_20260827/manuscript';
const scratch='/var/folders/_r/yk2xmp3x0zvgyvv1yxpn25br0000gn/T/nappt-p142-syntax-20260831-ufxa0d';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>({path:p,bytes:fs.statSync(p).size,sha256:sha(fs.readFileSync(p))});
const write=(n,s)=>fs.writeFileSync(path.join(here,n),s,{flag:'wx'});
const binary='/Library/TeX/texbin/pdflatex';
const args=['-draftmode','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+scratch,path.relative(manuscript,path.join(here,'compile.tex'))];
const r=spawnSync(binary,args,{cwd:manuscript,encoding:'utf8',maxBuffer:20*1024*1024});
write('draft_final.out',r.stdout+'\n'+r.stderr);
if(r.status!==0)throw Error('final draft compilation failed');
const log=fs.readFileSync(path.join(scratch,'compile.log'),'utf8');
write('draft_final.log',log);
for(const file of ['compile.bbl','compile.blg'])fs.copyFileSync(path.join(scratch,file),path.join(here,file),fs.constants.COPYFILE_EXCL);
const warnings=log.split('\n').filter(s=>/Warning|Overfull|Underfull|^!/.test(s));
if(warnings.some(s=>/undefined|Rerun|Label\(s\).*changed|Overfull|^!/.test(s)))throw Error('remaining draft warning');
if(fs.existsSync(path.join(scratch,'compile.pdf')))throw Error('unexpected PDF');
const all=['statement.tex','proof.tex','example.tex'].map(n=>fs.readFileSync(path.join(here,n),'utf8')).join('\n');
const labels=[...all.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
if(labels.length!==new Set(labels).size)throw Error('duplicate labels');
if(/\\(?:ref|autoref)\{/.test(all))throw Error('bare internal reference');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(all))throw Error('control byte');
write('BUILD.json',JSON.stringify({date:'2026-08-31',binary,args,cwd:manuscript,exitCode:r.status,scratch,pdfProduced:false,warnings,labels,log:record(path.join(here,'draft_final.log')),bibliographyLog:record(path.join(here,'compile.blg')),scope:'standalone draft-mode syntax/reference check only, with three imported book labels; not a mathematical or visual audit',earlierFailure:'preserved BUILD_FAILED.json and draft_run2.out; normal relative-basename BibTeX in scratch succeeded with BIBINPUTS='+manuscript+':'},null,2)+'\n');
const inputs=[
 'parts/part6/ch71_pseudoeffective_mp_dxz.tex','parts/part6/ch72_major_open_problems.tex',
 'parts/part5/ch52_rays_test_curves.tex','parts/part5/ch53_transcendental_metrics.tex',
 'parts/part5/ch58_tropical_spectra.tex','editorial/open_problem_atomic_inventory_20260824.md',
 'bibliography/ComplexGeometry.bib'
].map(p=>record(path.join(manuscript,p)));
write('PARENT_INPUTS.json',JSON.stringify(inputs,null,2)+'\n');
const entries=fs.readdirSync(here,{withFileTypes:true}).filter(e=>e.isFile()&&e.name!=='MANIFEST.json').map(e=>({name:e.name,...record(path.join(here,e.name))}));
write('MANIFEST.json',JSON.stringify({date:'2026-08-31',kind:'isolated candidate; independent and production gates pending',files:entries},null,2)+'\n');
console.log(JSON.stringify({frozen:true,files:entries.length,statement:record(path.join(here,'statement.tex')),proof:record(path.join(here,'proof.tex')),example:record(path.join(here,'example.tex')),manifest:record(path.join(here,'MANIFEST.json')),warnings},null,2));
