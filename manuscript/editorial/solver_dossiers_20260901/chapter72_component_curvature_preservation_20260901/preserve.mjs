// Read-only unless --copy; exact scoped archival copies, never proof certification.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {fileURLToPath} from 'node:url';
const src='/private/tmp/nappt_p071_20260827';
const dst='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const base='manuscript/editorial/solver_dossiers_20260901';
const own=base+'/chapter72_component_curvature_preservation_20260901';
const here=path.dirname(fileURLToPath(import.meta.url));
if(![src,dst].some(root=>path.join(root,own)===here))throw Error('Unexpected script location');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const pins=JSON.parse(read(path.join(here,'INPUT_PINS.json')));
if(new Set(pins.map(p=>p.directory)).size!==pins.length)throw Error('Duplicate dossier');
const checked=pins.map(p=>{
 if(!/^[a-z0-9_]+$/.test(p.directory))throw Error('Unsafe directory');
 const dir=path.join(src,base,p.directory);let manifestEntries=0;
 if(p.manifestSha256){
  const b=read(path.join(dir,'MANIFEST.json'));if(sha(b)!==p.manifestSha256)throw Error('Manifest drift');
  const m=JSON.parse(b),entries=m.entries??m.files;if(!Array.isArray(entries))throw Error('Manifest schema');
  for(const e of entries){const f=e.file??e.path,b=read(path.resolve(dir,f));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Input drift '+f);manifestEntries++;}
 }else if(fs.existsSync(path.join(dir,'MANIFEST.json')))throw Error('Unexpected manifest');
 const sums=read(path.join(dir,'SHA256SUMS'));if(sha(sums)!==p.checksumSha256)throw Error('Checksum-list drift');
 const lines=sums.toString().trimEnd().split('\n');
 for(const l of lines){const x=l.match(/^([a-f0-9]{64})\s+\*?(.+)$/);if(!x||sha(read(path.resolve(dir,x[2])))!==x[1])throw Error('Checksum drift');}
 return{...p,manifestEntries,checksumEntries:lines.length};
});
function walk(rel){return fs.readdirSync(path.join(src,rel),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>{
 const f=path.join(rel,e.name);if(e.isSymbolicLink())throw Error('Symlink');if(e.isDirectory())return walk(f);if(!e.isFile())throw Error('Unexpected entry');return e.name==='.DS_Store'?[]:[f];
});}
const selected=pins.flatMap(p=>walk(path.join(base,p.directory)));
for(const f of ['INPUT_PINS.json','CHECKPOINT.md','preserve.mjs'])selected.push(own+'/'+f);
if(new Set(selected).size!==selected.length)throw Error('Duplicate selected path');
const files=selected.map(rel=>{
 const b=read(path.join(src,rel)),h=sha(b),t=path.join(dst,rel),alreadyPresent=fs.existsSync(t);
 if(alreadyPresent&&sha(read(t))!==h)throw Error('Refuse differing durable file');
 if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(b.toString()))throw Error('Credential-like bytes: inspect privately');
 return{path:rel,bytes:b.length,sha256:h,alreadyPresent};
});
const summary={dossiers:pins.length,manifestEntries:checked.reduce((n,p)=>n+p.manifestEntries,0),checksumEntries:checked.reduce((n,p)=>n+p.checksumEntries,0),files:files.length,newFiles:files.filter(f=>!f.alreadyPresent).length,bytes:files.reduce((n,f)=>n+f.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary}));process.exit(0);}
for(const r of [src,dst])for(const f of ['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(r,own,f)))throw Error('Already preserved');
for(const f of files){const s=path.join(src,f.path),t=path.join(dst,f.path);if(sha(read(s))!==f.sha256)throw Error('Concurrent source drift');fs.mkdirSync(path.dirname(t),{recursive:true});if(!f.alreadyPresent)fs.copyFileSync(s,t,fs.constants.COPYFILE_EXCL);if(sha(read(t))!==f.sha256)throw Error('Copy mismatch');}
const record={date:'2026-09-01',sourceRoot:src,durableRoot:dst,checkedDossiers:checked,files,status:'Normal and component classification independently accepted; approachable/common-curvature candidate audit pending at authorship; no production acceptance or live promotion',historicalPaths:'Retained without rewriting',exclusions:['External primary PDF/text','Unrelated tracked/untracked work','Live theorem promotion','Generated PDFs']};
const bytes=JSON.stringify(record,null,2)+'\n',commitPaths=[...selected,own+'/PRESERVATION.json'].sort();
for(const r of [src,dst]){fs.writeFileSync(path.join(r,own,'PRESERVATION.json'),bytes,{flag:'wx'});fs.writeFileSync(path.join(r,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(bytes)}));
