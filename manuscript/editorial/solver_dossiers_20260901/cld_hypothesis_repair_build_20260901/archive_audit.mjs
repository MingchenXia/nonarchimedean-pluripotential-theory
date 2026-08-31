// Preserve a frozen independent audit without changing any of its bytes.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const rel='manuscript/editorial/solver_dossiers_20260901/';
const name='p213_ch16_bt_multiplier_harmonic_source_independent_audit_20260901';
const source=path.join('/private/tmp/nappt_p071_20260827',rel,name);
const destination=path.join(root,rel,name);
const own=path.join(root,rel,'cld_hypothesis_repair_build_20260901');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const manifestBytes=read(path.join(source,'MANIFEST.json'));
const sumsBytes=read(path.join(source,'SHA256SUMS'));
if(sha(manifestBytes)!=='a2002ffa0e10e32c73c48dde29735f5e314d2760918378fdb75234969ef5b24d')throw Error('Manifest identity changed');
if(sha(sumsBytes)!=='0d05ca457b6df5a1f89ea913835dad08108e0f360a194834297d15697b5dd511')throw Error('Checksum identity changed');
const manifest=JSON.parse(manifestBytes);
for(const e of manifest.entries){
  if(path.basename(e.file)!==e.file)throw Error('Nonlocal archive entry');
  const b=read(path.join(source,e.file));
  if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch '+e.file);
}
const sums=sumsBytes.toString().trim().split('\n');
for(const line of sums){
  const match=line.match(/^([a-f0-9]{64})\s+\*?([^\s]+)$/);
  if(!match||path.basename(match[2])!==match[2])throw Error('Invalid checksum entry');
  if(sha(read(path.join(source,match[2])))!==match[1])throw Error('Checksum mismatch '+match[2]);
}
const inputs=JSON.parse(read(path.join(source,'INPUT_HASHES.json')));
for(const e of inputs.inputs){
  const b=e.path.startsWith('git:')
    ?execFileSync('git',['show',e.path.slice(4)],{cwd:root})
    :read(e.path);
  if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Audit input drift '+e.path);
}
const reviewedDiff=execFileSync('git',['diff',inputs.baseCommit,'--',
  'manuscript/parts/part2/ch16_bedford_taylor.tex',
  'manuscript/parts/part2/ch19_cld_examples.tex'],{cwd:root});
if(!reviewedDiff.equals(read(path.join(source,'REVIEWED.diff'))))throw Error('Live diff differs from reviewed diff');
const snapshot=JSON.parse(read(path.join(own,'SOURCE_SNAPSHOT.json')));
for(const e of snapshot.entries){
  const b=read(path.join(snapshot.sourceRoot,e.path));
  if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Built source drift '+e.path);
}
const buildQa=JSON.parse(read(path.join(own,'BUILD_QA.json')));
if(sha(read(buildQa.pdf.path))!==buildQa.pdf.sha256)throw Error('Published PDF drift');
if(sha(read(buildQa.previousPdf.path))!==buildQa.previousPdf.sha256)throw Error('Preserved PDF drift');
const files=[...manifest.entries.map(e=>e.file),'MANIFEST.json','SHA256SUMS'];
if(new Set(files).size!==files.length)throw Error('Duplicate archive entry');
const record={date:'2026-09-01',source,destination,
  manifestSha256:sha(manifestBytes),checksumFileSha256:sha(sumsBytes),
  manifestEntries:manifest.entries.length,checksumEntries:sums.length,
  inputIdentitiesChecked:inputs.inputs.length,liveReviewedDiffMatches:true,
  builtInputIdentitiesChecked:snapshot.entries.length,publishedAndBackupPdfHashesMatch:true,
  files:files.map(file=>{const b=read(path.join(source,file));return {file,bytes:b.length,sha256:sha(b)};}),
  scope:'Exact preservation of independent review of existing-result corrections; no production verdict or new research promotion.'};
if(process.argv.includes('--copy')){
  if(fs.existsSync(destination)||fs.existsSync(path.join(own,'ARCHIVE_QA.json')))throw Error('Archive already exists');
  fs.mkdirSync(destination);
  for(const file of files){
    fs.copyFileSync(path.join(source,file),path.join(destination,file),fs.constants.COPYFILE_EXCL);
    if(!read(path.join(source,file)).equals(read(path.join(destination,file))))throw Error('Copy mismatch '+file);
  }
  fs.writeFileSync(path.join(own,'ARCHIVE_QA.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
}
console.log(JSON.stringify({copied:process.argv.includes('--copy'),...record},null,2));
