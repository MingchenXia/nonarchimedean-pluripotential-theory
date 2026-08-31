// Read-only preflight by default; --copy exclusively preserves selected files.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const sourceRoot='/private/tmp/nappt_p071_20260827';
const durableRoot='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix='manuscript/editorial/solver_dossiers_20260831';
const own=path.join(prefix,'chapter72_mixed_model_preservation_20260831');
const here=path.dirname(fileURLToPath(import.meta.url));
if (![sourceRoot,durableRoot].some(root=>path.join(root,own)===here)) throw Error('Unexpected script location');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=JSON.parse(fs.readFileSync(path.join(here,'INPUT_PINS.json'),'utf8'));
if (pins.length!==6 || new Set(pins.map(p=>p.directory)).size!==6) throw Error('Expected six distinct selected dossiers');
const checked=[];
for(const pin of pins){
  if(!/^[a-z0-9_]+$/.test(pin.directory)||!/^[a-f0-9]{64}$/.test(pin.sha256))throw Error('Invalid pin');
  const dir=path.join(sourceRoot,prefix,pin.directory);
  const bytes=fs.readFileSync(path.join(dir,'MANIFEST.json'));
  if(sha(bytes)!==pin.sha256)throw Error('Changed manifest: '+pin.directory);
  const record=JSON.parse(bytes);
  for(const e of record.entries){
    const data=fs.readFileSync(path.resolve(dir,e.path));
    if(sha(data)!==e.sha256||(e.bytes!==undefined&&data.length!==e.bytes))throw Error('Changed entry: '+e.path);
  }
  const sums=fs.readFileSync(path.join(dir,'SHA256SUMS'),'utf8').trim().split('\n');
  for(const line of sums){
    const match=line.match(/^([a-f0-9]{64})\s+\*?(.+)$/);
    if(!match||sha(fs.readFileSync(path.resolve(dir,match[2])))!==match[1])throw Error('Changed checksum');
  }
  checked.push({...pin,entries:record.entries.length,sums:sums.length});
}
function walk(relative){
  return fs.readdirSync(path.join(sourceRoot,relative),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>{
    const next=path.join(relative,e.name);
    if(e.isSymbolicLink())throw Error('Unexpected symlink');
    if(e.isDirectory())return walk(next);
    if(!e.isFile())throw Error('Unexpected non-file');
    return e.name==='.DS_Store'?[]:[next];
  });
}
const selected=pins.flatMap(pin=>walk(path.join(prefix,pin.directory)));
selected.push('manuscript/editorial/chapter72_mixed_model_followup_checkpoint_20260831.md',path.join(own,'preserve.mjs'),path.join(own,'INPUT_PINS.json'));
if(new Set(selected).size!==selected.length)throw Error('Duplicate selected path');
const files=selected.map(relative=>{
  if(path.isAbsolute(relative)||relative.split(path.sep).includes('..'))throw Error('Unsafe relative path');
  const data=fs.readFileSync(path.join(sourceRoot,relative)),digest=sha(data),target=path.join(durableRoot,relative),present=fs.existsSync(target);
  if(present&&sha(fs.readFileSync(target))!==digest)throw Error('Refuse different durable bytes: '+relative);
  if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(data.toString('utf8')))throw Error('Credential-like string; inspect privately: '+relative);
  return{relative,bytes:data.length,sha256:digest,alreadyPresent:present};
});
const summary={directories:pins.length,manifestEntries:checked.reduce((n,p)=>n+p.entries,0),checksums:checked.reduce((n,p)=>n+p.sums,0),files:files.length,newFiles:files.filter(f=>!f.alreadyPresent).length,bytes:files.reduce((n,f)=>n+f.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary},null,2));process.exit(0);}
for(const root of[sourceRoot,durableRoot])for(const name of['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(root,own,name)))throw Error('Already preserved');
for(const entry of files){
  const source=path.join(sourceRoot,entry.relative),target=path.join(durableRoot,entry.relative);
  if(sha(fs.readFileSync(source))!==entry.sha256)throw Error('Source drift');
  fs.mkdirSync(path.dirname(target),{recursive:true});
  if(!entry.alreadyPresent)fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
  if(sha(fs.readFileSync(target))!==entry.sha256)throw Error('Copy mismatch');
}
const record={date:'2026-08-31',sourceRoot,durableRoot,checkedManifests:checked,files,
  status:'Exact conditional research candidates and fresh scoped independent audits; production verification absent; no live theorem promotion or atom retirement',
  scope:['All-vertical nonreduced residual functional conditional on L','Original-field model adaptation diagnostic with residue-characteristic-zero resolution restriction','Mixed selected-boundary reduction conditional on L and V, same retained moments on a smaller whole tube'],
  exclusions:['Ordinary-W outer-collar follow-up and point-retaining research not yet complete','No arbitrary-cell capture or all-moment rigidity','No higher-bidegree or full P21.3 claim','No book PDF rebuild','Unrelated untracked files and external primary sources are excluded'],
  pathPolicy:'Historical frozen absolute paths remain unchanged; current durable copies have identical bytes',credentialHeuristic:'No credential-like string detected'};
const bytes=JSON.stringify(record,null,2)+'\n';
const commitPaths=[...selected,path.join(own,'PRESERVATION.json')].sort();
for(const root of[sourceRoot,durableRoot]){
  fs.writeFileSync(path.join(root,own,'PRESERVATION.json'),bytes,{flag:'wx'});
  fs.writeFileSync(path.join(root,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});
}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(bytes)},null,2));
