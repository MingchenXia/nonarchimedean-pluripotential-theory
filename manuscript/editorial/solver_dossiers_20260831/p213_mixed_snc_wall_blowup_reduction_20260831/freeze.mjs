// Exact-byte manifest generation only; default invocation is read-only.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const parent = path.dirname(here);
const sha = data => crypto.createHash('sha256').update(data).digest('hex');
const inputs = [
  ['p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md','3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a','conditional L'],
  ['p213_nonreduced_tube_finite_projection_research_20260831/SOURCE_LEDGER.md','cdf06f52596133e91abaa2c2e5870bbfb2db0f56ee71dd10dd2311636ccb9898','L source ledger'],
  ['p213_nonreduced_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md','d9e57c21c276edb40bc7619562b7f0a782cdc7a7eb05a04dd0b0cf0770dc9ea9','conditional V'],
  ['p213_nonreduced_snc_wall_residual_functional_research_20260831/SOURCE_LEDGER.md','5be17264811305baedb22ca98830969bf52f087678348519e820f2473992fb03','V source ledger'],
  ['p213_skeletal_packets_20260831/skeletal_representation/statement.tex','5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','optional R statement'],
  ['p213_skeletal_packets_20260831/skeletal_representation/proof.tex','27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a','optional R proof'],
];
const entries = inputs.map(([relative, expected, role]) => {
  const file = path.join(parent, relative);
  const data = fs.readFileSync(file);
  if (sha(data) !== expected) throw Error('Changed input: ' + relative);
  return {path: file, bytes: data.length, sha256: expected, role};
});
for (const name of ['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs']) {
  const file = path.join(here,name);
  const data = fs.readFileSync(file);
  if (/[\x00-\x08\x0b-\x1f\x7f]/.test(data.toString('utf8'))) throw Error('Forbidden control: '+name);
  entries.push({path:file,bytes:data.length,sha256:sha(data),role:'new authored output'});
}
const note = fs.readFileSync(path.join(here,'RESEARCH_NOTE.md'),'utf8');
const tags = [...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if (new Set(tags).size !== tags.length) throw Error('Repeated equation tag');
const manifest = path.join(here,'MANIFEST.json');
const sumsPath = path.join(here,'SHA256SUMS');
if (fs.existsSync(manifest)) {
  if (process.argv.includes('--freeze')) throw Error('Already frozen; no overwrite');
  const record = JSON.parse(fs.readFileSync(manifest,'utf8'));
  for (const entry of record.entries) {
    const data = fs.readFileSync(entry.path);
    if (data.length !== entry.bytes || sha(data) !== entry.sha256) throw Error('Manifest mismatch: '+entry.path);
  }
  const sums = fs.readFileSync(sumsPath,'utf8').trim().split('\n');
  for (const line of sums) {
    const match = line.match(/^([a-f0-9]{64})  (.+)$/);
    if (!match || sha(fs.readFileSync(match[2])) !== match[1]) throw Error('Checksum mismatch');
  }
  console.log(JSON.stringify({verified:true,entries:record.entries.length,sums:sums.length,uniqueTags:tags.length,manifestSha256:sha(fs.readFileSync(manifest))}));
  process.exit(0);
}
if (!process.argv.includes('--freeze')) {
  console.log(JSON.stringify({preflight:true,entries:entries.length,uniqueTags:tags.length,outputs:entries.slice(-3)},null,2));
  process.exit(0);
}
if (fs.existsSync(sumsPath)) throw Error('Unexpected checksum file');
const record = {
  date:'2026-08-31', author:'/root',
  status:'Frozen conditional research candidate; fresh independent and production verification are separate pending requirements',
  scope:'Mixed selected boundary components on an actual original-DVR regular proper SNC pair; current on whole proper residual-curve tube; h admissible blowups and unchanged compact-source moments; residual coefficient identity conditional on L and V',
  exclusions:['arbitrary ordinary-W support','capture of an arbitrary prescribed cell','all-moment common-ratio propagation','higher bidegrees','full P21.3','production or priority claim'],
  checks:{forbiddenControls:0,uniqueEquationTags:tags.length}, entries,
};
const bytes = JSON.stringify(record,null,2)+'\n';
fs.writeFileSync(manifest,bytes,{flag:'wx'});
const sums = entries.map(e=>e.sha256+'  '+e.path).concat(sha(bytes)+'  '+manifest).join('\n')+'\n';
fs.writeFileSync(sumsPath,sums,{flag:'wx'});
console.log(JSON.stringify({frozen:true,entries:entries.length,sums:entries.length+1,noteSha256:entries[entries.length-3].sha256,manifestSha256:sha(bytes),sumsSha256:sha(sums)},null,2));
