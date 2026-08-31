// Read-only unless --copy; exclusive byte-identical preservation of six dossiers.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {fileURLToPath} from 'node:url';
const src='/private/tmp/nappt_p071_20260827';
const dst='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const base='manuscript/editorial/solver_dossiers_20260901';
const own=base+'/chapter72_propagation_preservation_20260901';
const here=path.dirname(fileURLToPath(import.meta.url));
if(![src,dst].some(r=>path.join(r,own)===here))throw Error('Unexpected location');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=JSON.parse(fs.readFileSync(path.join(here,'INPUT_PINS.json'),'utf8'));
if(new Set(pins.map(p=>p.directory)).size!==pins.length)throw Error('Duplicate directory');
const checked=pins.map(p=>{
 if(!/^[a-z0-9_]+$/.test(p.directory))throw Error('Unsafe directory');
 const dir=path.join(src,base,p.directory),b=fs.readFileSync(path.join(dir,'MANIFEST.json'));
 if(sha(b)!==p.sha256)throw Error('Manifest drift '+p.directory);
 const m=JSON.parse(b),entries=m.entries??m.files;
 if(!Array.isArray(entries))throw Error('Unknown manifest schema');
 for(const e of entries){const v=fs.readFileSync(path.resolve(dir,e.path));if(v.length!==e.bytes||sha(v)!==e.sha256)throw Error('Input drift '+e.path);}
 const lines=fs.readFileSync(path.join(dir,'SHA256SUMS'),'utf8').trim().split('\n');
 for(const l of lines){const x=l.match(/^([a-f0-9]{64})\s+\*?(.+)$/);if(!x||sha(fs.readFileSync(path.resolve(dir,x[2])))!==x[1])throw Error('Checksum drift');}
 return{...p,manifestEntries:entries.length,checksumEntries:lines.length};
});
function walk(rel){return fs.readdirSync(path.join(src,rel),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>{
 const p=path.join(rel,e.name);if(e.isSymbolicLink())throw Error('Symlink');if(e.isDirectory())return walk(p);if(!e.isFile())throw Error('Unexpected entry');return e.name==='.DS_Store'?[]:[p];
});}
const selected=pins.flatMap(p=>walk(path.join(base,p.directory)));
for(const f of ['INPUT_PINS.json','CHECKPOINT.md','preserve.mjs'])selected.push(own+'/'+f);
if(new Set(selected).size!==selected.length)throw Error('Duplicate file');
const files=selected.map(rel=>{
 const b=fs.readFileSync(path.join(src,rel)),h=sha(b),target=path.join(dst,rel),present=fs.existsSync(target);
 if(present&&sha(fs.readFileSync(target))!==h)throw Error('Refuse differing durable file '+rel);
 if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(b.toString()))throw Error('Credential-like bytes; inspect privately');
 return{path:rel,bytes:b.length,sha256:h,alreadyPresent:present};
});
const summary={dossiers:pins.length,manifestEntries:checked.reduce((n,x)=>n+x.manifestEntries,0),checksumEntries:checked.reduce((n,x)=>n+x.checksumEntries,0),files:files.length,newFiles:files.filter(x=>!x.alreadyPresent).length,bytes:files.reduce((n,x)=>n+x.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary}));process.exit(0);}
for(const r of [src,dst])for(const f of ['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(r,own,f)))throw Error('Already preserved');
for(const f of files){const s=path.join(src,f.path),t=path.join(dst,f.path);if(sha(fs.readFileSync(s))!==f.sha256)throw Error('Concurrent source drift');fs.mkdirSync(path.dirname(t),{recursive:true});if(!f.alreadyPresent)fs.copyFileSync(s,t,fs.constants.COPYFILE_EXCL);if(sha(fs.readFileSync(t))!==f.sha256)throw Error('Copy mismatch');}
const record={date:'2026-09-01',sourceRoot:src,durableRoot:dst,checkedManifests:checked,files,status:'Bounded diagnostic, source diagnosis and independently reviewed conditional transport, not production acceptance or atom retirement',historicalPaths:'Preserved without rewriting',exclusions:['External source PDFs/text','Unrelated worktree changes','Unfinished investigations','Live mathematical promotion','Generated PDFs']};
const bytes=JSON.stringify(record,null,2)+'\n',commitPaths=[...selected,own+'/PRESERVATION.json'].sort();
for(const r of [src,dst]){fs.writeFileSync(path.join(r,own,'PRESERVATION.json'),bytes,{flag:'wx'});fs.writeFileSync(path.join(r,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(bytes)}));
