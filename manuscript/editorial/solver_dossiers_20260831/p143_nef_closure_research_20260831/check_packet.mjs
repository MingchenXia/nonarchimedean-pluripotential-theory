import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

// Read-only checker. Reports mechanical facts, never a mathematical verdict.
const root = path.dirname(fileURLToPath(import.meta.url));
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const record = p => { const b = fs.readFileSync(p); return {bytes:b.length, sha256:sha(b)}; };
const errors = [];
const texFiles = ['statement.tex','proof.tex','diagnostics.tex','main.tex'];
const texts = texFiles.map(name=>({name,text:fs.readFileSync(path.join(root,name),'utf8')}));
const labels = texts.flatMap(({name,text})=>[...text.matchAll(/\\label\{([^}]+)\}/g)].map(m=>({name,label:m[1]})));
const refs = texts.flatMap(({name,text})=>[...text.matchAll(/\\(?:c|C|eq)?ref\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(label=>({name,label}))));
const labelSet = new Set(labels.map(x=>x.label));
if (labels.length !== labelSet.size) errors.push('duplicate internal label');
for (const ref of refs) if (!labelSet.has(ref.label)) errors.push('undefined label: '+ref.label);
const bib = fs.readFileSync(path.join(root,'sources.bib'),'utf8');
const bibKeys = [...bib.matchAll(/@\w+\{([^,]+),/g)].map(m=>m[1]);
const cites = texts.flatMap(({text})=>[...text.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(',')));
for (const cite of cites) if (!bibKeys.includes(cite)) errors.push('undefined citation: '+cite);
const inputs = JSON.parse(fs.readFileSync(path.join(root,'INPUTS.json'),'utf8')).entries.map(expected=>{
  const actual=record(expected.path);
  const matches=actual.bytes===expected.bytes && actual.sha256===expected.sha256;
  if (!matches) errors.push('changed parent: '+expected.path);
  return {...expected,matches};
});
let manifest = null;
if (fs.existsSync(path.join(root,'MANIFEST.json'))) {
  const data = JSON.parse(fs.readFileSync(path.join(root,'MANIFEST.json'),'utf8'));
  manifest = data.entries.map(expected=>{
    const actual=record(path.join(root,expected.path));
    const matches=actual.bytes===expected.bytes && actual.sha256===expected.sha256;
    if (!matches) errors.push('changed packet file: '+expected.path);
    return {...expected,matches};
  });
}
let draft=null;
const draftDir=process.argv[2];
if (draftDir) {
  const log=fs.readFileSync(path.join(draftDir,'main.log'),'utf8');
  const warnings=log.split('\n').filter(line=>/undefined|Overfull|Underfull|LaTeX Warning:|^!/.test(line));
  const pdfs=fs.readdirSync(draftDir).filter(name=>name.endsWith('.pdf'));
  if(warnings.length) errors.push('final draft warnings');
  if(pdfs.length) errors.push('unexpected PDF in draft directory');
  draft={directory:draftDir,log:record(path.join(draftDir,'main.log')),warnings,pdfs,
    draftMode:log.includes('pdfdraftmode enabled'),
    noPDFProduced:pdfs.length===0};
  if(!draft.draftMode) errors.push('draftmode marker missing');
}
const result={mechanicalOnly:true,labelCount:labels.length,referenceCount:refs.length,
  citationKeys:[...new Set(cites)],inputs,manifest,draft,errors};
console.log(JSON.stringify(result,null,2));
if(errors.length) process.exitCode=1;
