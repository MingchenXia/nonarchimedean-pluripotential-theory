import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const candidate = "/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_mixed_ordinary_local_comparison_20260901";
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const get = p => { const b=fs.readFileSync(p); return {path:p,bytes:b.length,sha256:hash(b)}; };
const expected = {
  'RESEARCH_NOTE.md':'61e29bd02db4abe9f5e242e67d62249957c4049cdf269e6ae1dea13266c0bed2',
  'MANIFEST.json':'a8d380564b09eaf5b3f94590b61410fa0d5d5286a362e73c1f5156e888ef60c0',
  'SHA256SUMS':'407f85b46b98ff6f141e6e45b36c1815ececaa53b83b038090a60b1a4d3716ec'
};
const errors=[];
const pins=Object.entries(expected).map(([f,sha])=>{
  const r=get(path.resolve(candidate,f));
  if(r.sha256!==sha) errors.push('announced pin mismatch: '+f);
  return {...r,expectedSha256:sha,match:r.sha256===sha};
});
const manifest=JSON.parse(fs.readFileSync(path.join(candidate,'MANIFEST.json'),'utf8'));
const entries=manifest.entries.map(e=>{
  const r=get(path.resolve(candidate,e.path));
  const match=r.sha256===e.sha256&&r.bytes===e.bytes;
  if(!match) errors.push('manifest mismatch: '+e.path);
  return {...r,role:e.role,expectedBytes:e.bytes,expectedSha256:e.sha256,match};
});
const sums=fs.readFileSync(path.join(candidate,'SHA256SUMS'),'utf8').trim().split('\n').map(line=>{
  const m=line.match(/^([0-9a-f]{64})  (.+)$/);
  if(!m) throw new Error('Malformed sum: '+line);
  const r=get(path.resolve(candidate,m[2])),match=r.sha256===m[1];
  if(!match) errors.push('checksum mismatch: '+m[2]);
  return {...r,expectedSha256:m[1],match};
});
const note=fs.readFileSync(path.join(candidate,'RESEARCH_NOTE.md'),'utf8');
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
const controls=[...note].filter(c=>c.charCodeAt(0)<32&&!'\n\r\t'.includes(c)).length;
if(controls)errors.push('forbidden controls');
if(tags.length!==18||new Set(tags).size!==18)errors.push('equation tags');
if(entries.length!==15||sums.length!==16)errors.push('entry count');
const records=[...entries.map(({path,bytes,sha256,role})=>({path,bytes,sha256,role})),
 ...pins.filter(r=>!entries.some(e=>e.path===r.path)).map(({path,bytes,sha256})=>({path,bytes,sha256,role:'candidate freeze record'}))];
console.log(JSON.stringify({
  scope:'Read-only exact-byte checks; no mathematical or production certification by this script',
  candidate,announcedPins:pins,candidateManifestEntries:entries,candidateChecksums:sums,
  equationTags:tags,forbiddenControls:controls,inputRecords:records,
  checks:{announcedPins:pins.length,manifestEntries:entries.length,checksums:sums.length,inputRecords:records.length,distinctTags:new Set(tags).size,mismatches:errors.length},
  errors
},null,2));
if(errors.length)process.exitCode=1;

