import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827/manuscript/editorial';
const candidate=path.join(root,'solver_dossiers_20260901/p213_maximal_rank_source_cell_capture_research_20260901');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins={
  'RESEARCH_NOTE.md':'4cc25ff627af56aca05c8733e3e5bff65aea21015abe35e49726f9966bb1b384',
  'SOURCE_LEDGER.md':'cb4df5336a983b058d55b25c1dd4ec68e82d3ef155785e2bb59f3ed8281413b4',
  'MANIFEST.json':'52b8f6a75dda7caca6d3449a4e5e969f3abd3f4a6800cb9cf6bc091230713265',
  'SHA256SUMS':'3f6f3de6b1dd631260d47c3dcfd28d2fef05f055458fba3e186baf067d15efb8'
};
function check(dir){
  const m=JSON.parse(fs.readFileSync(path.join(dir,'MANIFEST.json')));
  for(const e of m.entries){const b=fs.readFileSync(path.resolve(dir,e.path));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);}
  const lines=fs.readFileSync(path.join(dir,'SHA256SUMS'),'utf8').trim().split('\n');
  for(const line of lines){const m=line.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(fs.readFileSync(path.resolve(dir,m[2])))!==m[1])throw Error('Checksum mismatch: '+line);}
  return {path:dir,manifestEntries:m.entries.length,checksums:lines.length,mismatches:0};
}
const pinned=Object.entries(pins).map(([name,s])=>{const p=path.join(candidate,name),b=fs.readFileSync(p);if(sha(b)!==s)throw Error('Announced pin mismatch: '+name);return {path:p,bytes:b.length,sha256:s};});
for(const name of ['RESEARCH_NOTE.md','SOURCE_LEDGER.md','VALIDATION.json','MANIFEST.json','SHA256SUMS']){
  const b=fs.readFileSync(path.join(candidate,name));if([...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))throw Error('Control: '+name);
}
const tags=[...fs.readFileSync(path.join(candidate,'RESEARCH_NOTE.md'),'utf8').matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Duplicate tag');
const report={date:'2026-09-01',reviewer:'/root/p081_weighted_repair_fresh',readOnly:true,pinned,candidate:check(candidate),
  predecessors:[check(path.join(root,'solver_dossiers_20260831/p213_common_moment_generic_isolation_research_20260831')),
    check(path.join(root,'solver_dossiers_20260831/p213_original_field_model_adaptation_diagnostic_20260831'))],
  candidateFilesCheckedForControls:5,forbiddenControls:0,equationTags:tags,mismatches:0};
if(!process.argv.includes('--inputs-only')&&fs.existsSync(path.join(here,'SHA256SUMS')))report.audit=check(here);
console.log(JSON.stringify(report,null,2));
