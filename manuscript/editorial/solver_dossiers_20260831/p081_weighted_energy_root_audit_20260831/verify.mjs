import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const inputDir=path.join(path.dirname(here),'p081_weighted_energy_consumers_repair_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const rec=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const manifestPath=path.join(inputDir,'MANIFEST.json');
const manifest=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
const entries=[...manifest.outputs,...manifest.base_chapters,...manifest.mathematical_and_reference_inputs];
const mismatches=[];
for(const e of entries){const a=rec(e.path);if(a.bytes!==e.bytes||a.sha256!==e.sha256)mismatches.push({expected:e,actual:a});}
if(mismatches.length)throw Error(JSON.stringify(mismatches));
const result={date:'2026-08-31',status:'bounded root technical review, not production acceptance',
 checkedEntries:entries.length,mismatches,inputs:[rec(manifestPath),...entries],
 auditFiles:['ROOT_AUDIT.md','verify.mjs'].map(n=>rec(path.join(here,n)))};
// Only newly generated audit metadata, never candidate or live source.
if(process.argv.includes('--record'))fs.writeFileSync(path.join(here,'CHECKS.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({checkedEntries:entries.length,mismatches,audit:rec(path.join(here,'ROOT_AUDIT.md'))},null,2));
