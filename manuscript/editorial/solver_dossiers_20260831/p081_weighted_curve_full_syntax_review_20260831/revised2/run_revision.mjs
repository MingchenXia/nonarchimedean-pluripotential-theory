import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(here);
const dossiers=path.dirname(parent),repo='/private/tmp/nappt_p071_20260827';
const first=JSON.parse(fs.readFileSync(path.join(parent,'ASSEMBLY.json'),'utf8'));
const priorBuild=JSON.parse(fs.readFileSync(path.join(parent,'revised1/BUILD.json'),'utf8'));
const scratch=first.scratchDirectory;
if(scratch!==priorBuild.scratchDirectory||!/^\/private\/tmp\/nappt_weighted_syntax_20260831\.[A-Za-z0-9]+$/.test(scratch))throw Error('unexpected scratch');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const expected=new Map(first.overlays.map(e=>[e.destination,e.sha256]));
for(const e of priorBuild.overlays)expected.set(e.destination,e.source.sha256);
for(const [p,h] of expected)if(record(p).sha256!==h)throw Error('previous overlay changed '+p);
const changes=[
 ['parts/part3/ch20_model_forms.tex','p081_ch20_ch21_real_model_max_repair_20260831/revised1/patched/ch20_model_forms.tex','3f2814e440f738708c084ee186a06e0930c0d48db89e80db1f21e7300e373ca2'],
 ['parts/part3/ch21_bfj_psh.tex','p081_ch20_ch21_real_model_max_repair_20260831/revised1/patched/ch21_bfj_psh.tex','ae6f71cd7db4c21108fb975e159ccaacf76d7f7251978224f7ac70886168769f'],
 ['parts/part3/ch24_bfj_ma.tex','p081_ch24_real_maximum_locality_repair_20260831/patched/ch24_bfj_ma.tex','b831435e0e66562d10d368f359792c017c53160b0acf4e895b4d23f0d7c6238d'],
 ['parts/part3/ch25_capacity.tex','p081_ch25_weighted_capacity_repair_20260831/revised1/patched/ch25_capacity.tex','4f66e1358ede7c8d9afff6b8b3c0fbaf53a27247d9741ce02f890fe24a0959a7'],
 ['parts/part3/ch26_energy.tex','p081_bounded_model_net_normalization_repair_20260831/patched/ch26_energy.tex','e37465c226a13e766ed2eecce014913fca3e5cdc2002e1766c151c83c73c6a74'],
 ['parts/part3/ch30_functoriality.tex','p081_bounded_model_net_normalization_repair_20260831/patched/ch30_functoriality.tex','02fa119b5732e3270989e3fddc0aa431add6eb04b27c40c208de9b3411ed2e28']
];
const overlays=[];
for(const [relative,p,h] of changes){const source=record(path.join(dossiers,p));if(source.sha256!==h)throw Error('frozen source changed '+p);const dest=path.join(scratch,relative),prior=record(dest);fs.copyFileSync(source.path,dest);overlays.push({relative,source,prior,destination:dest});}
{
 const source=record(path.join(repo,'manuscript/frontmatter/preface.tex'));
 if(source.sha256!=='cf272800e9522242b103e693cfc522741859c690a282269f26e48fcd5ad3ec48')throw Error('warning changed');
 const dest=path.join(scratch,'frontmatter/preface.tex'),prior=record(dest);
 fs.copyFileSync(source.path,dest);overlays.push({relative:'frontmatter/preface.tex',source,prior,destination:dest});
}
const runs=[];
async function run(name,command,args){
 const output=path.join(scratch,name+'.stdout'),fd=fs.openSync(output,'wx');
 const code=await new Promise((resolve,reject)=>{const child=spawn(command,args,{cwd:scratch,stdio:['ignore',fd,fd]});child.on('error',reject);child.on('close',resolve);});
 fs.closeSync(fd);runs.push({name,command,args,exitCode:code,output:record(output)});
 console.log(JSON.stringify({stage:name,exitCode:code}));
 if(command==='pdflatex')fs.copyFileSync(path.join(scratch,'book.log'),path.join(scratch,name+'.log'));
 if(code!==0)throw Error('failed '+name);
}
for(let pass=7;pass<=8;pass++){
 await run('pass'+pass,'pdflatex',['-no-shell-escape','-draftmode','-interaction=nonstopmode','-halt-on-error','book.tex']);
 if(pass===7)await run('index7','makeindex',['-s','style/svind.ist','-o','book.ind','book.idx']);
}
const log=fs.readFileSync(path.join(scratch,'book.log'),'utf8'),lines=log.split('\n');
const warnings=lines.filter(l=>/Warning|undefined|NA-BOOK-MISSING|^!/.test(l)),overfull=lines.filter(l=>/Overfull/.test(l));
if(fs.existsSync(path.join(scratch,'book.pdf')))throw Error('unexpected PDF');
const result={date:'2026-08-31',status:'eleven-chapter isolated syntax review; not mathematical acceptance or PDF layout review',scratchDirectory:scratch,previousBuild:record(path.join(parent,'revised1/BUILD.json')),previousStableLog:record(path.join(scratch,'pass6.log')),overlays,runs,finalLog:record(path.join(scratch,'pass8.log')),warnings,overfull,underfullCount:lines.filter(l=>/Underfull/.test(l)).length,pdfProduced:false};
fs.writeFileSync(path.join(here,'BUILD.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:true,warnings,overfull,underfullCount:result.underfullCount,pdfProduced:false},null,2));
