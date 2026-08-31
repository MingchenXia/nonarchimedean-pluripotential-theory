// Mechanical isolated-copy assembly; never writes the live chapters.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url));
const repo='/private/tmp/nappt_p071_20260827';
const parent=path.join(path.dirname(here),'p081_ch20_weighted_intersection_repair_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const parentChapter=path.join(parent,'patched/ch20_model_forms.tex');
if(entry(parentChapter).sha256!=='42f0c9dd4e957d7038c8bfb3d7c9742c5e5d023d732a219748c6906f447e1b7d')throw Error('Frozen Ch20 changed');
const changes=JSON.parse(fs.readFileSync(path.join(here,'replacements.json'),'utf8'));
const names=[...new Set(changes.map(x=>x.chapter))];
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const out=path.join(here,'patched');fs.mkdirSync(out,{recursive:true});
const checks=[],bases=[],inputs=[entry(parentChapter),entry(path.join(parent,'MANIFEST.json'))];
let patch='';
for(const name of names){
 const live=path.join(repo,'manuscript/parts/part3',name);
 const base=fs.readFileSync(live,'utf8');bases.push(entry(live));
 let text=fs.readFileSync(name==='ch20_model_forms.tex'?parentChapter:live,'utf8');
 for(const c of changes.filter(x=>x.chapter===name)){
  if(text.split(c.old).length!==2)throw Error('Replacement not unique: '+c.old);
  text=text.replace(c.old,c.new);
 }
 const old=labels(base),now=labels(text),missing=old.filter(x=>!now.includes(x));
 const duplicates=now.filter((x,i)=>now.indexOf(x)!==i);
 if(missing.length||duplicates.length)throw Error(JSON.stringify({name,missing,duplicates}));
 const target=path.join(out,name);fs.writeFileSync(target,text);
 const d=spawnSync('diff',['-u','--label','a/manuscript/parts/part3/'+name,'--label','b/manuscript/parts/part3/'+name,live,target],{encoding:'utf8'});
 if(![0,1].includes(d.status))throw Error(d.stderr);patch+=d.stdout;
 checks.push({chapter:name,oldLabels:old.length,newLabels:now.length,missing,duplicates});
}
const patchPath=path.join(here,'combined.patch');fs.writeFileSync(patchPath,patch);
const apply=spawnSync('git',['apply','--check',patchPath],{cwd:repo,encoding:'utf8'});
if(apply.status!==0)throw Error(apply.stderr);
const manifest={date:'2026-08-31',status:'isolated candidate; independent and production gates remain',bases,inputs,
 outputs:['replacements.json','GATE.md','assemble.mjs','combined.patch',...names.map(n=>'patched/'+n)].map(n=>entry(path.join(here,n))),
 checks:{chapters:checks,gitApplyCheck:'PASS; not applied',liveFilesUnchanged:true}};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify(manifest,null,2));
