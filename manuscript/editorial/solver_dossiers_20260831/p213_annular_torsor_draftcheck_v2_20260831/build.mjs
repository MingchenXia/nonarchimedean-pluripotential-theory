import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const candidate=path.resolve(here,'../p213_annular_torsor_residual_functional_research_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const expected=new Map([
 ['statement.tex','19baf4828b51e2b36370a2ececd41ad5802f01e3cf41c90f00df9b8bacec773a'],
 ['proof.tex','f851830312841ef4d8825ba4b049a718a16820ef3888263721278bf7a06c99fe'],
 ['CURVATURE_AND_EXAMPLES.md','b88523c7d72f143f2093d3803d6b64886ac7d8ff0d872a4f30678df41a543c0a'],
 ['MANIFEST.json','ec7f22f0fd750a325139c2f7403e213b53e921b5f1f89e5ab45ac6e0f059da30'],
]);
function checkInputs(){
 const inputs=[...expected].map(([name,hash])=>{
  const r=record(path.join(candidate,name));if(r.sha256!==hash)throw Error('Frozen input drift: '+name);return r;
 });
 const manifest=JSON.parse(fs.readFileSync(path.join(candidate,'MANIFEST.json'),'utf8'));
 for(const e of manifest.entries){const r=record(e.path);if(r.sha256!==e.sha256||r.bytes!==e.bytes)throw Error('Parent manifest drift: '+e.path);}
 return{inputs,parentEntryCount:manifest.entries.length};
}
const inputCheck=checkInputs();
if(process.argv.includes('--check')){
 const own=JSON.parse(fs.readFileSync(path.join(here,'MANIFEST.json'),'utf8'));
 for(const e of own.entries){const r=record(path.join(here,e.path));if(r.sha256!==e.sha256||r.bytes!==e.bytes)throw Error('Draftcheck drift: '+e.path);}
 console.log(JSON.stringify({readOnly:true,...inputCheck,localEntryCount:own.entries.length,errors:[]}));process.exit(0);
}
if(fs.existsSync(path.join(here,'MANIFEST.json')))throw Error('Already frozen');
const write=(name,data)=>fs.writeFileSync(path.join(here,name),typeof data==='string'?data:JSON.stringify(data,null,2)+'\n',{flag:'wx'});
write('INPUTS.json',inputCheck);
const tex='/Library/TeX/texbin/pdflatex',bib='/Library/TeX/texbin/bibtex';
const texArgs=['-draftmode','-interaction=nonstopmode','-halt-on-error','main.tex'];
const steps=[[tex,texArgs],[bib,['main']],[tex,texArgs],[tex,texArgs]];
const runs=[];
for(let i=0;i<steps.length;i++){
 const [command,args]=steps[i];
 const r=spawnSync(command,args,{cwd:here,env:{...process.env,BIBINPUTS:candidate+':'+(process.env.BIBINPUTS||'')},encoding:'utf8',maxBuffer:8*1024*1024});
 write('run'+(i+1)+'.out',(r.stdout||'')+(r.stderr||''));
 runs.push({command,args,exitCode:r.status,signal:r.signal,error:r.error?.message||null});
 if(r.status!==0){write('BUILD.json',{runs,success:false});throw Error('Draft build failed at step '+(i+1));}
}
const finalInputs=checkInputs();
const log=fs.readFileSync(path.join(here,'main.log'),'utf8');
const bibliographyLog=fs.readFileSync(path.join(here,'main.blg'),'utf8');
const warnings=log.split('\n').filter(l=>/^!|LaTeX Warning:|undefined|Overfull|Underfull/.test(l));
const bibWarnings=bibliographyLog.split('\n').filter(l=>/Warning--|error message|I couldn.t open/i.test(l));
const pdfs=fs.readdirSync(here).filter(n=>n.endsWith('.pdf'));
const text=['statement.tex','proof.tex'].map(n=>fs.readFileSync(path.join(candidate,n),'utf8')).join('\n');
const labels=[...text.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...text.matchAll(/\\(?:eq|c|C)?ref\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const unresolved=refs.filter(r=>!labels.includes(r));
if(pdfs.length||unresolved.length||new Set(labels).size!==labels.length)throw Error('Unexpected artifact or references');
const build={date:'2026-08-31',mechanicalOnly:true,success:true,runs,finalInputs,labelCount:labels.length,referenceCount:refs.length,unresolved,warnings,bibWarnings,pdfs,
 excluded:'Curvature/example Markdown was hashed and read but not typeset; no independent mathematical or production verdict',
 styleNote:'Frozen italic exponential constants and target/source volume notation are retained; address only in eventual reviewed integration.'};
write('BUILD.json',build);
const entries=fs.readdirSync(here).sort().map(name=>{const r=record(path.join(here,name));return{path:name,bytes:r.bytes,sha256:r.sha256};});
write('MANIFEST.json',{date:'2026-08-31',status:'Frozen draft-only build evidence',entries,selfHashPolicy:'Reported externally; no recursive self-entry'});
console.log(JSON.stringify({success:true,labels:labels.length,references:refs.length,warnings,bibWarnings,pdfs,entries:entries.length,manifestSha256:record(path.join(here,'MANIFEST.json')).sha256},null,2));
