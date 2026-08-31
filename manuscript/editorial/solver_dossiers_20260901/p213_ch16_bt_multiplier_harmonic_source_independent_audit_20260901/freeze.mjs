import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const input=JSON.parse(fs.readFileSync(path.join(dir,'INPUT_HASHES.json')));
const mismatches=[];
for(const e of input.inputs){
 let b;
 if(e.path.startsWith('git:'))b=execFileSync('git',['show',e.path.slice(4)],{cwd:root,maxBuffer:20*1024*1024});
 else b=fs.readFileSync(e.path);
 if(b.length!==e.bytes||sha(b)!==e.sha256)mismatches.push(e.path);
}
if(mismatches.length)throw new Error('Input changed: '+mismatches.join(', '));
const names=fs.readdirSync(dir).filter(n=>n!=='MANIFEST.json'&&n!=='SHA256SUMS'&&n!=='VALIDATION.json').sort();
const controls=[];
for(const name of names){const b=fs.readFileSync(path.join(dir,name));
 const bad=[...b].filter(c=>(c<32&&c!==9&&c!==10)||c===127).length;
 controls.push({file:name,forbiddenControlBytes:bad});if(bad)throw new Error('Control byte in '+name);
}
const validation={date:'2026-09-01',inputEntriesVerified:input.inputs.length,inputMismatches:0,
 forbiddenControls:controls,bookFilesWritten:false,productionCalls:false,gitMutations:false,
 compilePerformed:false,pdfGeneratedOrInspected:false,
 status:'Independent exact-byte correctness review of specified existing-result corrections; not production acceptance.'};
fs.writeFileSync(path.join(dir,'VALIDATION.json'),JSON.stringify(validation,null,2)+'\n',{flag:'wx'});
names.push('VALIDATION.json');names.sort();
const entries=names.map(file=>{const b=fs.readFileSync(path.join(dir,file));return{file,bytes:b.length,sha256:sha(b)};});
fs.writeFileSync(path.join(dir,'MANIFEST.json'),JSON.stringify({date:'2026-09-01',status:validation.status,entries},null,2)+'\n',{flag:'wx'});
const sums=[...entries,{file:'MANIFEST.json',sha256:sha(fs.readFileSync(path.join(dir,'MANIFEST.json')))}];
fs.writeFileSync(path.join(dir,'SHA256SUMS'),sums.map(e=>e.sha256+'  '+e.file).join('\n')+'\n',{flag:'wx'});
for(const e of entries){const b=fs.readFileSync(path.join(dir,e.file));if(b.length!==e.bytes||sha(b)!==e.sha256)throw new Error('Manifest verification failed: '+e.file);}
console.log(JSON.stringify({manifestEntries:entries.length,checksumEntries:sums.length,inputEntries:input.inputs.length,
 manifestSha256:sha(fs.readFileSync(path.join(dir,'MANIFEST.json'))),sumsSha256:sha(fs.readFileSync(path.join(dir,'SHA256SUMS'))),
 reportSha256:sha(fs.readFileSync(path.join(dir,'AUDIT_REPORT.md'))),addendumSha256:sha(fs.readFileSync(path.join(dir,'AFTERPATCH_ADDENDUM.md')))},null,2));
