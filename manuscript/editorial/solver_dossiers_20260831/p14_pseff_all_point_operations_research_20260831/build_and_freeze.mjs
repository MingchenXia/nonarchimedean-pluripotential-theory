import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const parent=path.dirname(here);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:sha(b)};};
if(fs.existsSync(path.join(here,'MANIFEST.json')))throw Error('Already frozen');
const inputs=[];
for(const d of ['p142_raw_transform_usc_research_20260831','p143_dominated_divisorial_research_20260831','p143_kahler_truncation_research_20260831']){
 for(const n of ['statement.tex','proof.tex','MANIFEST.json'])inputs.push(record(path.join(parent,d,n)));
}
for(const p of ['/private/tmp/mp24.txt','/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.txt'])inputs.push(record(p));
fs.writeFileSync(path.join(here,'INPUTS.json'),JSON.stringify(inputs,null,2)+'\n',{flag:'wx'});
const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'nappt-p14-pseff-operations-draft-20260831-'));
for(const n of ['main.tex','statement.tex','proof.tex','sources.bib'])fs.copyFileSync(path.join(here,n),path.join(scratch,n),fs.constants.COPYFILE_EXCL);
const commands=[['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']],['bibtex',['main']],['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']],['pdflatex',['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex']]];
const runs=[];
for(let i=0;i<commands.length;i++){
 const [tool,args]=commands[i];
 const r=spawnSync('/Library/TeX/texbin/'+tool,args,{cwd:scratch,encoding:'utf8',maxBuffer:5*1024*1024,timeout:60000});
 fs.writeFileSync(path.join(here,`run${i+1}.out`),(r.stdout??'')+(r.stderr??''),{flag:'wx'});
 runs.push({tool,args,exitCode:r.status});
 if(r.status!==0)throw Error('Draft build failure: '+tool);
}
for(const n of ['main.log','main.bbl','main.blg'])fs.copyFileSync(path.join(scratch,n),path.join(here,n),fs.constants.COPYFILE_EXCL);
const core=['statement.tex','proof.tex'].map(n=>fs.readFileSync(path.join(here,n),'utf8')).join('\n');
const labels=[...core.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...core.matchAll(/\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(labels.length!==new Set(labels).size||refs.some(r=>!labels.includes(r)))throw Error('Reference mismatch');
const log=fs.readFileSync(path.join(here,'main.log'),'utf8');
const warnings=log.split('\n').filter(x=>/^!|Undefined control|(?:LaTeX|Package .*?) Warning:|Overfull \\[hv]box/.test(x));
const underfull=log.split('\n').filter(x=>/Underfull \\[hv]box/.test(x));
if(warnings.length||fs.existsSync(path.join(scratch,'main.pdf')))throw Error('Unexpected diagnostic or PDF');
for(const x of inputs)if(record(x.path).sha256!==x.sha256)throw Error('Input drift');
fs.writeFileSync(path.join(here,'BUILD.json'),JSON.stringify({date:'2026-08-31',scratch,runs,warnings,underfull,pdfProduced:false,labels:labels.length,references:refs.length,scope:'Standalone draft assembly; mathematical reviews pending'},null,2)+'\n',{flag:'wx'});
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);}
const files=walk(here).filter(p=>p!==path.join(here,'MANIFEST.json')).map(p=>({name:path.relative(here,p),...record(p)}));
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify({date:'2026-08-31',status:'Conditional research; independent and production review required',files},null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({frozen:true,files:files.length,inputs:inputs.length,labels:labels.length,references:refs.length,warnings,underfull,pdfProduced:false,statement:record(path.join(here,'statement.tex')),proof:record(path.join(here,'proof.tex')),manifest:record(path.join(here,'MANIFEST.json'))},null,2));
