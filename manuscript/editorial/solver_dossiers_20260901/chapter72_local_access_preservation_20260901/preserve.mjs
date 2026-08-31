// Read-only preflight unless --copy is explicitly supplied. All writes exclusive.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import{fileURLToPath}from'node:url';
const sourceRoot='/private/tmp/nappt_p071_20260827';
const durableRoot='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const editorial='manuscript/editorial';
const own=editorial+'/solver_dossiers_20260901/chapter72_local_access_preservation_20260901';
const here=path.dirname(fileURLToPath(import.meta.url));
if(![sourceRoot,durableRoot].some(root=>path.join(root,own)===here))throw Error('Unexpected location');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=JSON.parse(fs.readFileSync(path.join(here,'INPUT_PINS.json'),'utf8'));
if(new Set(pins.map(p=>p.directory)).size!==pins.length)throw Error('Repeated dossier');
const checked=pins.map(pin=>{
 if(!/^solver_dossiers_202(?:60831|60901)\/[a-z0-9_]+$/.test(pin.directory))throw Error('Unexpected directory '+pin.directory);
 const dir=path.join(sourceRoot,editorial,pin.directory),bytes=fs.readFileSync(path.join(dir,'MANIFEST.json'));
 if(sha(bytes)!==pin.sha256)throw Error('Manifest drift '+pin.directory);
 const m=JSON.parse(bytes);
 for(const e of m.entries){const b=fs.readFileSync(path.resolve(dir,e.path));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Input drift '+e.path);}
 const lines=fs.readFileSync(path.join(dir,'SHA256SUMS'),'utf8').trim().split('\n');
 for(const line of lines){const r=line.match(/^([a-f0-9]{64})\s+\*?(.+)$/);if(!r||sha(fs.readFileSync(path.resolve(dir,r[2])))!==r[1])throw Error('Checksum drift '+line);}
 return {...pin,manifestEntries:m.entries.length,checksums:lines.length};
});
function walk(relative){return fs.readdirSync(path.join(sourceRoot,relative),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>{
 const next=path.join(relative,e.name);if(e.isSymbolicLink())throw Error('Symlink '+next);if(e.isDirectory())return walk(next);if(!e.isFile())throw Error('Non-file '+next);return e.name==='.DS_Store'?[]:[next];
});}
const selected=pins.flatMap(pin=>walk(path.join(editorial,pin.directory)));
selected.push(editorial+'/chapter72_local_access_checkpoint_20260901.md',own+'/preserve.mjs',own+'/INPUT_PINS.json');
if(new Set(selected).size!==selected.length)throw Error('Repeated file');
const files=selected.map(relative=>{
 if(path.isAbsolute(relative)||relative.split(path.sep).includes('..'))throw Error('Unsafe path');
 const b=fs.readFileSync(path.join(sourceRoot,relative)),h=sha(b),target=path.join(durableRoot,relative),present=fs.existsSync(target);
 if(present&&sha(fs.readFileSync(target))!==h)throw Error('Refuse differing durable file '+relative);
 if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(b.toString('utf8')))throw Error('Credential-like bytes; inspect privately '+relative);
 return {relative,bytes:b.length,sha256:h,alreadyPresent:present};
});
const summary={dossiers:pins.length,manifestEntries:checked.reduce((n,p)=>n+p.manifestEntries,0),checksums:checked.reduce((n,p)=>n+p.checksums,0),files:files.length,newFiles:files.filter(f=>!f.alreadyPresent).length,bytes:files.reduce((n,f)=>n+f.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary},null,2));process.exit(0);}
for(const root of[sourceRoot,durableRoot])for(const name of['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(root,own,name)))throw Error('Already preserved');
for(const f of files){const source=path.join(sourceRoot,f.relative),target=path.join(durableRoot,f.relative);if(sha(fs.readFileSync(source))!==f.sha256)throw Error('Source changed during copy');fs.mkdirSync(path.dirname(target),{recursive:true});if(!f.alreadyPresent)fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);if(sha(fs.readFileSync(target))!==f.sha256)throw Error('Copy mismatch');}
const record={date:'2026-09-01',sourceRoot,durableRoot,checkedManifests:checked,files,status:'Conditional research proofs and exact scoped reviews only; status of each candidate is recorded in the checkpoint; no production acceptance or atom retirement',scope:['Ordinary-open collars, point-retaining mixed reduction and proper target-open source comparison','Mixed-model local coefficient synthesis','Residue-characteristic-zero algebraic source-cell capture and nearby all-vertical residual walls','Source-cell-to-residual-curve access assembly'],exclusions:['No common constant through arbitrary unrelated source incidences','No all-current or higher-bidegree rigidity, full P21.3 or general envelope theorem','No live chapter promotion or book PDF rebuild','External primary PDFs/text and source-QA images outside the selected dossiers are not copied','Unrelated worktree files excluded'],pathPolicy:'Historical frozen absolute paths remain unchanged; the selected durable copies are byte-identical',credentialHeuristic:'No credential-like bytes detected'};
const bytes=JSON.stringify(record,null,2)+'\n',commitPaths=[...selected,own+'/PRESERVATION.json'].sort();
for(const root of[sourceRoot,durableRoot]){fs.writeFileSync(path.join(root,own,'PRESERVATION.json'),bytes,{flag:'wx'});fs.writeFileSync(path.join(root,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha:sha(bytes)},null,2));
