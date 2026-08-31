import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';

// Read-only audit. In particular, do not run the author's writing phase.
const repo='/private/tmp/nappt_p071_20260827';
const packet=path.join(repo,'manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch21_real_model_max_repair_20260831');
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const manifestBytes=fs.readFileSync(path.join(packet,'MANIFEST.json'));
const manifest=JSON.parse(manifestBytes);
const out={manifestSha256:sha(manifestBytes),files:[],chapters:[]};
for(const entry of manifest.files){
  const bytes=fs.readFileSync(path.join(packet,entry.name));
  assert.equal(sha(bytes),entry.sha256,entry.name+' hash');
  assert.equal(bytes.length,entry.bytes,entry.name+' bytes');
  out.files.push({name:entry.name,sha256:sha(bytes),status:'PASS'});
}
const labels=text=>[...text.matchAll(/\\label\{([^}]+)\}/g)].map(x=>x[1]);
const stripComments=text=>text.replace(/(?<!\\)%[^\n]*/g,'');
const envBalance=text=>{
  const counts={};
  for(const m of stripComments(text).matchAll(/\\(begin|end)\{([^}]+)\}/g)){
    counts[m[2]]=(counts[m[2]]??0)+(m[1]==='begin'?1:-1);
  }
  return Object.fromEntries(Object.entries(counts).filter(([,n])=>n!==0));
};
for(const entry of manifest.entries){
  const beforeBytes=fs.readFileSync(entry.source);
  const afterBytes=fs.readFileSync(entry.destination);
  assert.equal(sha(beforeBytes),entry.sourceSha256,'parent '+entry.chapter);
  assert.equal(sha(afterBytes),entry.sha256,'candidate '+entry.chapter);
  assert.equal(afterBytes.length,entry.bytes);
  const before=beforeBytes.toString('utf8'),after=afterBytes.toString('utf8');
  const oldLabels=labels(before),newLabels=labels(after);
  assert.equal(oldLabels.length,entry.oldLabels);
  assert.equal(newLabels.length,entry.newLabels);
  assert.equal(new Set(newLabels).size,newLabels.length,'duplicate labels');
  assert.deepEqual(oldLabels.filter(x=>!newLabels.includes(x)),[],'lost labels');
  assert(!/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/.test(after),'control bytes');
  assert.deepEqual(envBalance(after),envBalance(before),'new environment imbalance');
  const live=path.join(repo,'manuscript/parts/part3',path.basename(entry.destination));
  const diff=spawnSync('git',['diff','--no-index','--',live,entry.destination],{encoding:'utf8'});
  assert([0,1].includes(diff.status),'diff failed');
  assert.equal(diff.stdout,fs.readFileSync(path.join(packet,`ch${entry.chapter}.patch`),'utf8'),'recorded patch differs');
  out.chapters.push({chapter:entry.chapter,sourceSha256:sha(beforeBytes),sha256:sha(afterBytes),oldLabels:oldLabels.length,newLabels:newLabels.length,addedLabels:newLabels.filter(x=>!oldLabels.includes(x)),unbalancedEnvironments:envBalance(after),status:'PASS'});
}

// Replay only the fully inspected, frozen in-memory transformation prefix.
// Exclude imports and the entire output/mkdir/write/spawn phase; supply read-only fs.
let prefix=fs.readFileSync(path.join(packet,'assemble.mjs'),'utf8');
prefix=prefix.slice(0,prefix.indexOf("const output=path.join(packet,'patched');"));
prefix=prefix.replace(/^import[^\n]*\n/gm,'');
prefix=prefix.replace('const packet=path.dirname(fileURLToPath(import.meta.url));','');
assert(!/writeFile|mkdir|spawnSync|process\.|\bimport\b/.test(prefix),'unexpected side effect in prefix');
const replay=new Function('fs','path','crypto','packet',prefix+'\nreturn {ch20,ch21,operations};');
const result=replay(Object.freeze({readFileSync:fs.readFileSync.bind(fs)}),path,crypto,packet);
assert.equal(result.ch20,fs.readFileSync(manifest.entries[0].destination,'utf8'));
assert.equal(result.ch21,fs.readFileSync(manifest.entries[1].destination,'utf8'));
assert.deepEqual(result.operations,manifest.operations,'operation ledger differs');
for(const name of ['rational_approximation.tex','truncation.tex','envelope_directedness_proof.tex']){
  const fragment=fs.readFileSync(path.join(packet,name),'utf8');
  assert.equal(result.ch20.split(fragment).length-1,1,'fragment occurrence '+name);
}
out.assembly={operations:result.operations.length,reproducesBothFrozenFiles:true,fragmentsEmbeddedExactlyOnce:true};
console.log(JSON.stringify(out,null,2));
