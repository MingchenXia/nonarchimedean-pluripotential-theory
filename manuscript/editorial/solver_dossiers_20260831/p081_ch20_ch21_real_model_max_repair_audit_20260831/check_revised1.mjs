import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';

const repo='/private/tmp/nappt_p071_20260827';
const parent=path.join(repo,'manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch21_real_model_max_repair_20260831');
const here=path.join(parent,'revised1');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const manifestBytes=fs.readFileSync(path.join(here,'MANIFEST.json'));
const manifest=JSON.parse(manifestBytes);
const result={manifestSha256:sha(manifestBytes),chapters:[],files:[]};
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
for(const f of manifest.files){
  const b=fs.readFileSync(path.join(here,f.name));
  assert.equal(sha(b),f.sha256);assert.equal(b.length,f.bytes);
  result.files.push({name:f.name,sha256:sha(b),status:'PASS'});
}
for(const e of manifest.entries){
  const before=fs.readFileSync(e.source,'utf8'),after=fs.readFileSync(e.destination,'utf8');
  assert.equal(sha(before),e.sourceSha256);assert.equal(sha(after),e.sha256);
  assert.equal(Buffer.byteLength(after),e.bytes);
  assert.deepEqual(labels(after),labels(before),'ordered labels changed');
  assert.equal(new Set(labels(after)).size,labels(after).length);
  assert(!/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/.test(after));
  const relative='manuscript/parts/part3/'+e.name;
  const patch=fs.readFileSync(e.patch.path,'utf8');
  assert.equal(sha(patch),e.patch.sha256);
  const diff=spawnSync('diff',['-u','--label','a/'+relative,'--label','b/'+relative,path.join(repo,relative),e.destination],{encoding:'utf8'});
  assert([0,1].includes(diff.status));assert.equal(diff.stdout,patch);
  const check=spawnSync('git',['apply','--check',e.patch.path],{cwd:repo,encoding:'utf8'});
  assert.equal(check.status,0,check.stderr);
  result.chapters.push({name:e.name,sha256:sha(after),labels:labels(after).length,patchSha256:sha(patch),portablePatchCheck:'PASS; not applied'});
}

// As above, replay only the inspected in-memory transformations, never writes.
let prefix=fs.readFileSync(path.join(here,'assemble.mjs'),'utf8');
prefix=prefix.slice(0,prefix.indexOf("fs.mkdirSync(path.join(here,'patched')"));
prefix=prefix.replace(/^import[^\n]*\n/gm,'');
prefix=prefix.replace('const here=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(here);','');
assert(!/writeFile|mkdir|spawnSync|process\.|\bimport\b/.test(prefix));
const replay=new Function('fs','path','crypto','here','parent',prefix+'\nreturn {chapters,changes};');
const r=replay(Object.freeze({readFileSync:fs.readFileSync.bind(fs)}),path,crypto,here,parent);
assert.deepEqual(r.changes,manifest.changes);
for(let i=0;i<r.chapters.length;i++)assert.equal(r.chapters[i].after,fs.readFileSync(manifest.entries[i].destination,'utf8'));
for(const name of ['rational_approximation.tex','truncation.tex','envelope_directedness_proof.tex']){
  const fragment=fs.readFileSync(path.join(parent,name),'utf8');
  assert.equal(r.chapters[0].after.split(fragment).length-1,1,'core fragment changed '+name);
}
result.assembly={changes:r.changes.length,exactReplay:true,coreProofFragmentsUnchanged:true};
console.log(JSON.stringify(result,null,2));
