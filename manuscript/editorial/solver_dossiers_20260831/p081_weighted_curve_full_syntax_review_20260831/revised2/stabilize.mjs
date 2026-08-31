import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const base=JSON.parse(fs.readFileSync(path.join(here,'BUILD.json'),'utf8'));
const scratch=base.scratchDirectory;
if(!/^\/private\/tmp\/nappt_weighted_syntax_20260831\.[A-Za-z0-9]+$/.test(scratch))throw Error('scratch');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
for(const e of base.overlays)if(record(e.destination).sha256!==e.source.sha256)throw Error('overlay changed');
const runs=[];let summary;
for(let pass=9;pass<=11;pass++){
 const name='pass'+pass,output=path.join(scratch,name+'.stdout'),fd=fs.openSync(output,'wx');
 const args=['-no-shell-escape','-draftmode','-interaction=nonstopmode','-halt-on-error','book.tex'];
 const exitCode=await new Promise((resolve,reject)=>{const child=spawn('pdflatex',args,{cwd:scratch,stdio:['ignore',fd,fd]});child.on('error',reject);child.on('close',resolve);});
 fs.closeSync(fd);const logfile=path.join(scratch,name+'.log');fs.copyFileSync(path.join(scratch,'book.log'),logfile);
 const lines=fs.readFileSync(logfile,'utf8').split('\n');
 summary={exitCode,warnings:lines.filter(l=>/Warning|undefined|NA-BOOK-MISSING|^!/.test(l)),overfull:lines.filter(l=>/Overfull/.test(l)),underfullCount:lines.filter(l=>/Underfull/.test(l)).length};
 runs.push({name,args,...summary,stdout:record(output),log:record(logfile)});
 console.log(JSON.stringify({pass,...summary}));
 if(exitCode!==0)break;
 if(!summary.warnings.some(l=>/Label\(s\).*changed|undefined|Rerun/.test(l)))break;
}
const result={date:'2026-08-31',status:'syntax/reference stabilization only; no PDF or mathematical acceptance',baseBuild:record(path.join(here,'BUILD.json')),scratchDirectory:scratch,runs,...summary,pdfProduced:fs.existsSync(path.join(scratch,'book.pdf'))};
fs.writeFileSync(path.join(here,'STABILIZED_BUILD.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});
if(result.pdfProduced||result.exitCode!==0)throw Error('unexpected build failure/PDF');
