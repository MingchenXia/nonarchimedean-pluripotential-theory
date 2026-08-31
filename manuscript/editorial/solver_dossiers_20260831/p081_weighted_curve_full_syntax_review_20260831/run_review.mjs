import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const assembly=JSON.parse(fs.readFileSync(path.join(here,'ASSEMBLY.json'),'utf8'));
const scratch=assembly.scratchDirectory;
if(!/^\/private\/tmp\/nappt_weighted_syntax_20260831\.[A-Za-z0-9]+$/.test(scratch))throw Error('Unexpected scratch path');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const runs=[];
async function run(name,command,args){
 const output=path.join(scratch,name+'.stdout');
 const fd=fs.openSync(output,'wx');
 const code=await new Promise((resolve,reject)=>{
  const proc=spawn(command,args,{cwd:scratch,stdio:['ignore',fd,fd]});
  proc.on('error',reject);proc.on('close',resolve);
 });
 fs.closeSync(fd);runs.push({name,command,args,exitCode:code,output:record(output)});
 console.log(JSON.stringify({stage:name,exitCode:code}));
 if(code!==0)throw Error('Build step failed: '+name);
 if(command==='pdflatex')fs.copyFileSync(path.join(scratch,'book.log'),path.join(scratch,name+'.log'));
}
for(let pass=2;pass<=4;pass++){
 await run('pass'+pass,'pdflatex',['-no-shell-escape','-draftmode','-interaction=nonstopmode','-halt-on-error','book.tex']);
 if(pass<4)await run('index'+pass,'makeindex',['-s','style/svind.ist','-o','book.ind','book.idx']);
}
const log=fs.readFileSync(path.join(scratch,'book.log'),'utf8');
const diagnostics=log.split('\n').filter(l=>/Warning|Overfull|Underfull|undefined|NA-BOOK-MISSING|^!/.test(l));
const pdfExists=fs.existsSync(path.join(scratch,'book.pdf'));
if(pdfExists)throw Error('Unexpected PDF in draft-only review');
const result={date:'2026-08-31',status:'full-manuscript draft-mode syntax/reference test, not mathematical acceptance',
 assembly:record(path.join(here,'ASSEMBLY.json')),scratchDirectory:scratch,runs,
 finalLog:record(path.join(scratch,'book.log')),diagnostics,pdfProduced:false,
 liveBookChanged:false,productionVerification:false};
fs.writeFileSync(path.join(here,'BUILD.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({complete:true,diagnostics,pdfProduced:false},null,2));
