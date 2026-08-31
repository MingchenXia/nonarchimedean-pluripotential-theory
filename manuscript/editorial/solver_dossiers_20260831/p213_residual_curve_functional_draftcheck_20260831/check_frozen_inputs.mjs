import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

// Read-only syntax/hash checker; no mathematical or production verdict.
const root=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const errors=[];
const inputs=JSON.parse(fs.readFileSync(path.join(root,'INPUTS.json'),'utf8')).map(e=>{
 const actual=record(e.path);const matches=actual.bytes===e.bytes&&actual.sha256===e.sha256;
 if(!matches)errors.push('changed frozen input: '+e.path);return{...actual,matches};
});
const parentManifest=JSON.parse(fs.readFileSync(inputs.find(e=>e.path.endsWith('/MANIFEST.json')).path,'utf8'));
const parentEntries=parentManifest.entries.map(e=>{
 const actual=record(e.path);const matches=actual.bytes===e.bytes&&actual.sha256===e.sha256;
 if(!matches)errors.push('changed parent-manifest entry: '+e.path);return{...actual,matches};
});
const source=inputs.filter(e=>e.path.endsWith('.tex')).map(e=>({path:e.path,text:fs.readFileSync(e.path,'utf8')}));
const labels=source.flatMap(s=>[...s.text.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]));
const refs=source.flatMap(s=>[...s.text.matchAll(/\\(?:c|C|eq)?ref\{([^}]+)\}/g)].flatMap(m=>m[1].split(',')));
if(new Set(labels).size!==labels.length)errors.push('duplicate source label');
for(const r of refs)if(!labels.includes(r))errors.push('undefined source reference: '+r);
const bibText=fs.readFileSync(inputs.find(e=>e.path.endsWith('.bib')).path,'utf8');
const bibKeys=[...bibText.matchAll(/@\w+\{([^,]+),/g)].map(m=>m[1]);
const citationKeys=[...new Set(source.flatMap(s=>[...s.text.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','))))];
for(const key of citationKeys)if(!bibKeys.includes(key))errors.push('undefined citation: '+key);
const styleNotes=source.flatMap(s=>s.text.split('\n').flatMap((line,index)=>/e\^\{/.test(line)?[{path:s.path,line:index+1,text:line.trim(),note:'eventual integration: use roman exponential constant; frozen source untouched'}]:[]));
const log=fs.readFileSync(path.join(root,'main.log'),'utf8');
const finalWarnings=log.split('\n').filter(line=>/undefined|Overfull|Underfull|LaTeX Warning:|^!/.test(line));
if(finalWarnings.length)errors.push('final TeX warnings');
const bibLog=fs.readFileSync(path.join(root,'main.blg'),'utf8');
const bibWarnings=bibLog.split('\n').filter(line=>/Warning--|error message|I couldn.t open/i.test(line));
if(bibWarnings.length)errors.push('BibTeX warnings');
const pdfs=fs.readdirSync(root).filter(name=>name.endsWith('.pdf'));
if(pdfs.length)errors.push('unexpected PDF');
let manifest=null;
if(fs.existsSync(path.join(root,'MANIFEST.json'))){
 manifest=JSON.parse(fs.readFileSync(path.join(root,'MANIFEST.json'),'utf8')).entries.map(e=>{
  const actual=record(path.join(root,e.path));const matches=actual.bytes===e.bytes&&actual.sha256===e.sha256;
  if(!matches)errors.push('changed draftcheck entry: '+e.path);return{...actual,matches};
 });
}
console.log(JSON.stringify({mechanicalOnly:true,inputs,parentEntries,labelCount:labels.length,referenceCount:refs.length,
 citationKeys,bibliographyKeys:bibKeys,unusedBibliographyKeys:bibKeys.filter(key=>!citationKeys.includes(key)),
 finalWarnings,bibWarnings,pdfs,draftmodeMarker:log.includes('pdfdraftmode enabled'),styleNotes,manifest,errors},null,2));
if(errors.length)process.exitCode=1;
