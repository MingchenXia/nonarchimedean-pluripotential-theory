import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
// Mechanical isolated-copy assembly only.
const here=path.dirname(fileURLToPath(import.meta.url));
const repo='/private/tmp/nappt_p071_20260827';
const name='ch28_finite_energy_measures.tex';
const parent=path.join(path.dirname(here),'p081_weighted_energy_consumers_repair_20260831');
const input=path.join(parent,'patched',name);
const live=path.join(repo,'manuscript/parts/part3',name);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
if(entry(input).sha256!=='8a234254e7085d1297b2f2d6d18f9445fe33045fd64a53b8f8baa8fca521349a')throw Error('Frozen parent changed');
const src=fs.readFileSync(input,'utf8'),base=fs.readFileSync(live,'utf8');
const anchor='\\label{prop:ch28-curve-uniqueness}';
if(src.split(anchor).length!==2)throw Error('Ambiguous proposition');
const a=src.indexOf('\\begin{proof}',src.indexOf(anchor));
const b=src.indexOf('\\end{proof}',a)+'\\end{proof}'.length;
if(a<0||b<a)throw Error('Proof boundary missing');
const proof=fs.readFileSync(path.join(here,'uniqueness_proof.tex'),'utf8').trimEnd();
const dst=src.slice(0,a)+proof+src.slice(b);
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const old=labels(base),now=labels(dst),missing=old.filter(x=>!now.includes(x));
const duplicate=now.filter((x,i)=>now.indexOf(x)!==i);
if(missing.length||duplicate.length)throw Error(JSON.stringify({missing,duplicate}));
fs.mkdirSync(path.join(here,'patched'),{recursive:true});
const output=path.join(here,'patched',name);fs.writeFileSync(output,dst);
const d=spawnSync('diff',['-u','--label','a/manuscript/parts/part3/'+name,'--label','b/manuscript/parts/part3/'+name,live,output],{encoding:'utf8'});
if(![0,1].includes(d.status))throw Error(d.stderr);
const patch=path.join(here,'chapter.patch');fs.writeFileSync(patch,d.stdout);
const check=spawnSync('git',['apply','--check',patch],{cwd:repo,encoding:'utf8'});
if(check.status!==0)throw Error(check.stderr);
const manifest={date:'2026-08-31',status:'root-authored repair; independent and production reviews pending',
 inputs:[entry(live),entry(input),entry(path.join(parent,'MANIFEST.json'))],
 outputs:['uniqueness_proof.tex','GATE.md','assemble.mjs','chapter.patch','patched/'+name].map(n=>entry(path.join(here,n))),
 checks:{oldLabels:old.length,newLabels:now.length,missing,duplicate,gitApplyCheck:'PASS; not applied'}};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify(manifest,null,2));
