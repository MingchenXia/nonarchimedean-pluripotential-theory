import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(here);
const dossiers=path.dirname(parent),repo='/private/tmp/nappt_p071_20260827';
const previous=JSON.parse(fs.readFileSync(path.join(parent,'ASSEMBLY.json'),'utf8'));
const scratch=previous.scratchDirectory;
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const rec=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
if(!/^\/private\/tmp\/nappt_weighted_syntax_20260831\.[A-Za-z0-9]+$/.test(scratch))throw Error('Unexpected scratch directory');
for(const e of previous.overlays)if(rec(e.destination).sha256!==e.sha256)throw Error('Previous scratch overlay changed: '+e.destination);
const changes=[
 ['parts/part3/ch25_capacity.tex',path.join(dossiers,'p081_ch25_weighted_capacity_repair_20260831/patched/ch25_capacity.tex'),'bc939ba01e4763debb7d73b4d6681592ea70229a7c42814c8c59384b3b4cb1ce'],
 ['parts/part3/ch28_finite_energy_measures.tex',path.join(dossiers,'p081_ch28_curve_uniqueness_snc_repair_20260831/revised1/patched/ch28_finite_energy_measures.tex'),'d302fc06208ded647cbb4ef3c63c425e54c5382f2ad25cb8ba9bb68a5f8d9315'],
 ['frontmatter/preface.tex',path.join(repo,'manuscript/frontmatter/preface.tex'),null]
];
const overlay=[];
for(const [relative,source,hash] of changes){
 const entry=rec(source);if(hash&&entry.sha256!==hash)throw Error('Frozen new overlay changed');
 const destination=path.join(scratch,relative),prior=rec(destination);
 fs.copyFileSync(source,destination);overlay.push({relative,source:entry,prior,destination});
}
const runs=[];
async function run(name,command,args){
 const output=path.join(scratch,name+'.stdout'),fd=fs.openSync(output,'wx');
 const code=await new Promise((resolve,reject)=>{const p=spawn(command,args,{cwd:scratch,stdio:['ignore',fd,fd]});p.on('error',reject);p.on('close',resolve);});
 fs.closeSync(fd);runs.push({name,command,args,exitCode:code,output:rec(output)});
 console.log(JSON.stringify({stage:name,exitCode:code}));if(code!==0)throw Error('Failed '+name);
 if(command==='pdflatex')fs.copyFileSync(path.join(scratch,'book.log'),path.join(scratch,name+'.log'));
}
for(let pass=5;pass<=6;pass++){
 await run('pass'+pass,'pdflatex',['-no-shell-escape','-draftmode','-interaction=nonstopmode','-halt-on-error','book.tex']);
 if(pass===5)await run('index5','makeindex',['-s','style/svind.ist','-o','book.ind','book.idx']);
}
const log=fs.readFileSync(path.join(scratch,'book.log'),'utf8');
const lines=log.split('\n');
const warnings=lines.filter(l=>/Warning|undefined|NA-BOOK-MISSING|^!/.test(l));
const overfull=lines.filter(l=>/Overfull/.test(l)),underfull=lines.filter(l=>/Underfull/.test(l));
if(fs.existsSync(path.join(scratch,'book.pdf')))throw Error('Unexpected PDF');
const result={date:'2026-08-31',status:'nine-chapter isolated syntax review plus live editorial warning; not mathematical acceptance',
 previousAssembly:rec(path.join(parent,'ASSEMBLY.json')),previousBuild:rec(path.join(parent,'BUILD.json')),scratchDirectory:scratch,
 overlays:overlay,runs,finalLog:rec(path.join(scratch,'book.log')),warnings,overfull,underfullCount:underfull.length,pdfProduced:false};
fs.writeFileSync(path.join(here,'BUILD.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({complete:true,warnings,overfull,underfullCount:underfull.length,pdfProduced:false},null,2));
