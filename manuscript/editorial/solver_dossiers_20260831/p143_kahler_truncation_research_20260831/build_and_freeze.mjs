import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:sha(b)};};
if(fs.existsSync(path.join(here,'MANIFEST.json')))throw Error('Already frozen');
const predecessorPaths=[
 'manuscript/parts/part5/ch53_transcendental_metrics.tex',
 'manuscript/parts/part5/ch60_mp_psh.tex',
 'manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex',
 'manuscript/editorial/open_problem_atomic_inventory_20260824.md',
 'manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831/statement.tex',
 'manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831/proof.tex',
 'manuscript/editorial/solver_dossiers_20260831/p143_dominated_divisorial_research_20260831/statement.tex',
 'manuscript/editorial/solver_dossiers_20260831/p143_dominated_divisorial_research_20260831/proof.tex',
];
const inputs=predecessorPaths.map(p=>record(path.join(root,p)));
fs.writeFileSync(path.join(here,'INPUTS.json'),JSON.stringify(inputs,null,2)+'\n',{flag:'wx'});
const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'nappt-p143-kahler-draft-20260831-'));
for(const name of ['main.tex','statement.tex','proof.tex','sources.bib'])fs.copyFileSync(path.join(here,name),path.join(scratch,name),fs.constants.COPYFILE_EXCL);
const commands=[['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']],['bibtex',['main']],['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']],['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']]];
const runs=[];
for(let i=0;i<commands.length;i++){
 const [tool,args]=commands[i];
 const result=spawnSync('/Library/TeX/texbin/'+tool,args,{cwd:scratch,encoding:'utf8',maxBuffer:10*1024*1024,timeout:60000});
 const out=`run${i+1}.out`;
 fs.writeFileSync(path.join(here,out),(result.stdout??'')+(result.stderr??''),{flag:'wx'});
 runs.push({tool,args,exitCode:result.status,output:record(path.join(here,out))});
 if(result.status!==0){fs.writeFileSync(path.join(here,'BUILD_FAILED.json'),JSON.stringify({scratch,runs,error:String(result.error??'')},null,2)+'\n',{flag:'wx'});throw Error('Draft build failed at '+tool);}
}
for(const name of ['main.log','main.bbl','main.blg'])fs.copyFileSync(path.join(scratch,name),path.join(here,name),fs.constants.COPYFILE_EXCL);
const contents=['statement.tex','proof.tex'].map(n=>fs.readFileSync(path.join(here,n),'utf8')).join('\n');
const labels=[...contents.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const references=[...contents.matchAll(/\\(?:[cC]ref|eqref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(new Set(labels).size!==labels.length||references.some(r=>!labels.includes(r)))throw Error('Label mismatch');
if(/[\x00-\x08\x0B\x0C\x0E-\x1F]/.test(contents))throw Error('Control byte');
const log=fs.readFileSync(path.join(here,'main.log'),'utf8');
const warnings=log.split('\n').filter(l=>/^!|Undefined control|(?:LaTeX|Package .*?) Warning:|Overfull \\[hv]box/.test(l));
if(warnings.length)throw Error('Final draft diagnostics: '+warnings.join('\n'));
for(const input of inputs)if(sha(fs.readFileSync(input.path))!==input.sha256)throw Error('Historical input drift');
const build={date:'2026-08-31',scratch,runs,exitCode:0,pdfProduced:fs.existsSync(path.join(scratch,'main.pdf')),labels:labels.length,references:references.length,warnings,log:record(path.join(here,'main.log')),scope:'Standalone draft assembly, not mathematical acceptance or visual QA'};
if(build.pdfProduced)throw Error('Unexpected PDF');
fs.writeFileSync(path.join(here,'BUILD.json'),JSON.stringify(build,null,2)+'\n',{flag:'wx'});
const files=fs.readdirSync(here).filter(n=>n!=='MANIFEST.json').sort().map(name=>({name,...record(path.join(here,name))}));
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify({date:'2026-08-31',kind:'conditional research candidate; independent and production reviews pending',files},null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({frozen:true,files:files.length,statement:record(path.join(here,'statement.tex')),proof:record(path.join(here,'proof.tex')),manifest:record(path.join(here,'MANIFEST.json')),draft:build},null,2));
