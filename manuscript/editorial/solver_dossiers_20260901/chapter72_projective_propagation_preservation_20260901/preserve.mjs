// Read-only unless --copy. Identity/preservation checks are not proof verification.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const src='/private/tmp/nappt_p071_20260827';
const dst='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const base='manuscript/editorial/solver_dossiers_20260901';
const own=base+'/chapter72_projective_propagation_preservation_20260901';
const here=path.dirname(fileURLToPath(import.meta.url));
if(![src,dst].some(root=>path.join(root,own)===here))throw Error('Unexpected script location');
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const read=file=>fs.readFileSync(file);
const pins=JSON.parse(read(path.join(here,'INPUT_PINS.json')));
if(new Set(pins.map(p=>p.directory)).size!==pins.length)throw Error('Duplicate dossier');
const checked=pins.map(pin=>{
  if(!/^[a-z0-9_]+$/.test(pin.directory))throw Error('Unsafe directory');
  const dir=path.join(src,base,pin.directory);
  let manifestEntries=0;
  if(pin.manifestSha256){
    const bytes=read(path.join(dir,'MANIFEST.json'));
    if(sha(bytes)!==pin.manifestSha256)throw Error('Manifest drift '+pin.directory);
    const manifest=JSON.parse(bytes),entries=manifest.entries??manifest.files;
    if(!Array.isArray(entries))throw Error('Unknown manifest schema');
    for(const entry of entries){
      const file=entry.file??entry.path;
      if(typeof file!=='string')throw Error('Missing manifest path');
      const bytes=read(path.resolve(dir,file));
      if(bytes.length!==entry.bytes||sha(bytes)!==entry.sha256)throw Error('Input drift '+file);
      manifestEntries++;
    }
  }else if(fs.existsSync(path.join(dir,'MANIFEST.json'))){
    throw Error('Unexpected unpinned manifest');
  }
  const sums=read(path.join(dir,'SHA256SUMS'));
  if(sha(sums)!==pin.checksumSha256)throw Error('Checksum-list drift');
  const lines=sums.toString().trimEnd().split('\n');
  for(const line of lines){
    const m=line.match(/^([a-f0-9]{64})\s+\*?(.+)$/);
    if(!m||sha(read(path.resolve(dir,m[2])))!==m[1])throw Error('Checksum input drift');
  }
  return{...pin,manifestEntries,checksumEntries:lines.length};
});
function walk(rel){
  return fs.readdirSync(path.join(src,rel),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(entry=>{
    const file=path.join(rel,entry.name);
    if(entry.isSymbolicLink())throw Error('Symlink not allowed');
    if(entry.isDirectory())return walk(file);
    if(!entry.isFile())throw Error('Unexpected file type');
    return entry.name==='.DS_Store'?[]:[file];
  });
}
const selected=pins.flatMap(p=>walk(path.join(base,p.directory)));
for(const file of ['INPUT_PINS.json','CHECKPOINT.md','preserve.mjs'])selected.push(own+'/'+file);
if(new Set(selected).size!==selected.length)throw Error('Duplicate selected file');
const files=selected.map(rel=>{
  const bytes=read(path.join(src,rel)),digest=sha(bytes),target=path.join(dst,rel);
  const alreadyPresent=fs.existsSync(target);
  if(alreadyPresent&&sha(read(target))!==digest)throw Error('Refuse differing durable file '+rel);
  if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(bytes.toString()))throw Error('Credential-like bytes: inspect privately');
  return{path:rel,bytes:bytes.length,sha256:digest,alreadyPresent};
});
const summary={dossiers:pins.length,manifestEntries:checked.reduce((s,p)=>s+p.manifestEntries,0),checksumEntries:checked.reduce((s,p)=>s+p.checksumEntries,0),files:files.length,newFiles:files.filter(f=>!f.alreadyPresent).length,bytes:files.reduce((s,f)=>s+f.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary}));process.exit(0);}
for(const root of [src,dst])for(const file of ['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(root,own,file)))throw Error('Already preserved; do not rewrite');
for(const entry of files){
  const source=path.join(src,entry.path),target=path.join(dst,entry.path);
  if(sha(read(source))!==entry.sha256)throw Error('Concurrent source drift');
  fs.mkdirSync(path.dirname(target),{recursive:true});
  if(!entry.alreadyPresent)fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
  if(sha(read(target))!==entry.sha256)throw Error('Copy mismatch');
}
const record={date:'2026-09-01',sourceRoot:src,durableRoot:dst,checkedDossiers:checked,files,status:'Exact research preservation only; no production acceptance, live theorem promotion or atom retirement',historicalPaths:'Preserved without rewriting',exclusions:['External primary PDFs/text','Unrelated dirty/untracked work','Live chapter changes','Generated PDFs']};
const output=JSON.stringify(record,null,2)+'\n';
const commitPaths=[...selected,own+'/PRESERVATION.json'].sort();
for(const root of [src,dst]){
  fs.writeFileSync(path.join(root,own,'PRESERVATION.json'),output,{flag:'wx'});
  fs.writeFileSync(path.join(root,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});
}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(output)}));
