import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

// Read-only exact-byte and syntax-provenance checks, not a mathematical verdict.
const root = '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p14_pseff_all_point_operations_research_20260831';
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const record = p => { const b=fs.readFileSync(p); return {path:p,bytes:b.length,sha256:sha(b)}; };
const errors=[];
const manifestPath=path.join(root,'MANIFEST.json');
const manifest=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
const manifestEntries=manifest.files.map(expected=>{
  const actual=record(expected.path);
  const matches=actual.bytes===expected.bytes&&actual.sha256===expected.sha256;
  if(!matches)errors.push('manifest mismatch: '+expected.path);
  return {...actual,matches};
});
const inputs=JSON.parse(fs.readFileSync(path.join(root,'INPUTS.json'),'utf8')).map(expected=>{
  const actual=record(expected.path);
  const matches=actual.bytes===expected.bytes&&actual.sha256===expected.sha256;
  if(!matches)errors.push('input mismatch: '+expected.path);
  return {...actual,matches};
});
const expectedCore={
  'statement.tex':'1ec3db259a1c00302085459a42c2708cec4f3676aa03177a9011552dc474a642',
  'proof.tex':'52900352bdde0ec57c4ef4c7488d783f29c57b8c4db0beb3df7e3abb884a44fe',
  'MANIFEST.json':'f42fd86160b4a719696d7b0acfec25e741cdfa06c3066a807f9d30a078871add'
};
const core=Object.entries(expectedCore).map(([name,expected])=>{
  const actual=record(path.join(root,name));
  const matches=actual.sha256===expected;
  if(!matches)errors.push('announced freeze mismatch: '+name);
  return {...actual,matches};
});
const texts=['statement.tex','proof.tex','main.tex'].map(name=>fs.readFileSync(path.join(root,name),'utf8'));
const labels=texts.flatMap(t=>[...t.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]));
const refs=texts.flatMap(t=>[...t.matchAll(/\\(?:c|C|eq)?ref\{([^}]+)\}/g)].flatMap(m=>m[1].split(',')));
if(new Set(labels).size!==labels.length)errors.push('duplicate labels');
for(const r of refs)if(!labels.includes(r))errors.push('undefined label: '+r);
const log=fs.readFileSync(path.join(root,'main.log'),'utf8');
const logFlags=log.split('\n').filter(x=>/undefined|Overfull|Underfull|LaTeX Warning:|^!/.test(x));
if(logFlags.some(x=>!/Underfull/.test(x)))errors.push('unexpected final log warning');
const unchangedCoreFromAttempt=['statement.tex','proof.tex'].map(name=>({name,
  equal:fs.readFileSync(path.join(root,name)).equals(fs.readFileSync(path.join(root,'draft_attempt1',name)))}));
if(unchangedCoreFromAttempt.some(x=>!x.equal))errors.push('principal math changed since draft attempt');
const oldMain=fs.readFileSync(path.join(root,'draft_attempt1','main.tex'),'utf8');
const newMain=texts[2];
const geometryOnly=newMain.replace('\\usepackage[margin=1in]{geometry}\n','')===oldMain;
if(!geometryOnly)errors.push('layout change is not geometry-only');
const filesBelow=p=>fs.readdirSync(p,{withFileTypes:true}).flatMap(e=>e.isDirectory()?filesBelow(path.join(p,e.name)):[path.join(p,e.name)]);
const pdfFiles=filesBelow(root).filter(p=>p.endsWith('.pdf'));
if(pdfFiles.length)errors.push('unexpected PDF');
console.log(JSON.stringify({mechanicalOnly:true,core,manifestEntries,inputs,
  labelCount:labels.length,referenceCount:refs.length,logFlags,draftmodeMarker:log.includes('pdfdraftmode enabled'),
  pdfFiles,unchangedCoreFromAttempt,geometryOnly,errors},null,2));
if(errors.length)process.exitCode=1;
