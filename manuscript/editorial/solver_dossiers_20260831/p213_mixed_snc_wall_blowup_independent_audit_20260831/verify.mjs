import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const candidate=path.join(path.dirname(here),'p213_mixed_snc_wall_blowup_reduction_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins={
  'RESEARCH_NOTE.md':'9463a10f2918a01a214c458052a50c5604293a6e4192f7c5aa1c91234c7e1120',
  'SOURCE_LEDGER.md':'dbde85d634fd9d9d248f5118202564a134fc4ce5df22b32451aa191bac0f956a',
  'freeze.mjs':'dc246f9ebd766a760bd6eaa233f21e6a468e752e48825b0b5ed3ba191ec70c39',
  'MANIFEST.json':'34049f77811973f0e9d074bc7d8d88ae9f5aa4e586b3590d75b388f856f607fb',
  'SHA256SUMS':'3c9e1f7536e2f57345c665297876c08f05d746292dfa0852eb74e2cb4fc8b036',
};
function checkManifest(file){
  const manifest=JSON.parse(fs.readFileSync(file,'utf8'));
  for(const e of manifest.entries){
    const b=fs.readFileSync(e.path);
    if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);
  }
  return manifest.entries.length;
}
function checkSums(file){
  const lines=fs.readFileSync(file,'utf8').trim().split('\n');
  for(const line of lines){
    const m=line.match(/^([a-f0-9]{64})  (.+)$/);
    if(!m||sha(fs.readFileSync(m[2]))!==m[1])throw Error('Checksum mismatch: '+line);
  }
  return lines.length;
}
const pinned=Object.entries(pins).map(([name,expected])=>{
  const file=path.join(candidate,name),b=fs.readFileSync(file),actual=sha(b);
  if(actual!==expected)throw Error('Pin mismatch: '+name);
  return {path:file,bytes:b.length,sha256:actual};
});
const outputs=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'];
for(const name of outputs){
  const b=fs.readFileSync(path.join(candidate,name));
  if([...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))throw Error('Control character: '+name);
}
const note=fs.readFileSync(path.join(candidate,'RESEARCH_NOTE.md'),'utf8');
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Repeated equation tags');
const report={date:'2026-08-31',reviewer:'/root/p081_weighted_repair_fresh',readOnly:true,
  candidateManifestEntries:checkManifest(path.join(candidate,'MANIFEST.json')),
  candidateChecksums:checkSums(path.join(candidate,'SHA256SUMS')),
  pinned,forbiddenControls:0,equationTags:tags,uniqueEquationTags:tags.length,mismatches:0};
if(!process.argv.includes('--inputs-only')&&fs.existsSync(path.join(here,'MANIFEST.json'))){
  report.auditManifestEntries=checkManifest(path.join(here,'MANIFEST.json'));
  if(fs.existsSync(path.join(here,'SHA256SUMS')))report.auditChecksums=checkSums(path.join(here,'SHA256SUMS'));
}
console.log(JSON.stringify(report,null,2));
