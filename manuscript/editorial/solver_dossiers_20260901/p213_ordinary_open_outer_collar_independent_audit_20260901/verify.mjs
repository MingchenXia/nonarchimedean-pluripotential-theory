import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831';
const candidate=path.join(root,'p213_ordinary_open_outer_collar_research_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins={
  'RESEARCH_NOTE.md':'f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b',
  'SOURCE_LEDGER.md':'6cceb8f6f03141e6115262fbe2b164227b1b51afa939b627c18047680241c776',
  'MANIFEST.json':'eea85c5daa7630ffc8d0d2774b2f50fbfd8a4419ddb1b2df95257b8455075bab',
  'SHA256SUMS':'992215911f8392cea64aa2d275e5c8665bdc0e94652501caeecc3d34f13fc78e',
};
function check(dir){
  const m=JSON.parse(fs.readFileSync(path.join(dir,'MANIFEST.json'),'utf8'));
  for(const e of m.entries){
    const b=fs.readFileSync(path.resolve(dir,e.path));
    if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);
  }
  const lines=fs.readFileSync(path.join(dir,'SHA256SUMS'),'utf8').trim().split('\n');
  for(const line of lines){
    const m=line.match(/^([a-f0-9]{64})  (.+)$/);
    if(!m||sha(fs.readFileSync(path.resolve(dir,m[2])))!==m[1])throw Error('Checksum mismatch: '+line);
  }
  return {path:dir,manifestEntries:m.entries.length,checksums:lines.length,mismatches:0};
}
const pinned=Object.entries(pins).map(([name,pin])=>{
  const file=path.join(candidate,name),b=fs.readFileSync(file);
  if(sha(b)!==pin)throw Error('Announced pin mismatch: '+name);
  return {path:file,bytes:b.length,sha256:pin};
});
for(const name of ['RESEARCH_NOTE.md','SOURCE_LEDGER.md','VALIDATION.json','MANIFEST.json','SHA256SUMS']){
  const b=fs.readFileSync(path.join(candidate,name));
  if([...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))throw Error('Control: '+name);
}
const note=fs.readFileSync(path.join(candidate,'RESEARCH_NOTE.md'),'utf8');
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Duplicate equation tags');
const report={date:'2026-09-01',reviewer:'/root/p081_weighted_repair_fresh',readOnly:true,
  pinned,candidate:check(candidate),
  predecessors:[
    check(path.join(root,'p213_nonreduced_tube_finite_projection_research_20260831')),
    check(path.join(root,'p213_nonreduced_snc_wall_residual_functional_research_20260831'))
  ],newCandidateFilesCheckedForControls:5,forbiddenControls:0,
  uniqueEquationTags:tags.length,equationTags:tags,mismatches:0};
if(!process.argv.includes('--inputs-only')&&fs.existsSync(path.join(here,'SHA256SUMS')))
  report.audit=check(here);
console.log(JSON.stringify(report,null,2));
