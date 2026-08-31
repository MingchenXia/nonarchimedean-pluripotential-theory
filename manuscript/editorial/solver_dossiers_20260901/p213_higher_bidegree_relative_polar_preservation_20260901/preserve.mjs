import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const from='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901';
const into=path.dirname(own);
const names=['p213_higher_bidegree_relative_polar_route_research_20260901'];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const recordPath=path.join(own,'PRESERVATION.json');
function walk(base){
 const out=[];
 function visit(rel){
  for(const e of fs.readdirSync(path.join(base,rel),{withFileTypes:true})){
   const p=path.join(rel,e.name);
   if(e.isSymbolicLink())throw Error('Symlink '+p);
   if(e.isDirectory())visit(p);else if(e.isFile())out.push(p);else throw Error('Special file '+p);
  }
 }
 visit('');return out.sort();
}
if(process.argv.includes('--verify')){
 const r=JSON.parse(fs.readFileSync(recordPath));
 for(const p of r.files){
  const b=fs.readFileSync(path.join(root,p.repositoryPath));
  if(b.length!==p.bytes||hash(b)!==p.sha256)throw Error('Archive changed '+p.repositoryPath);
 }
 for(const n of names){
  const expected=r.files.filter(p=>p.dossier===n).map(p=>p.relativePath).sort();
  if(JSON.stringify(expected)!==JSON.stringify(walk(path.join(into,n))))throw Error('Membership changed '+n);
 }
 console.log(JSON.stringify({preservation:'PASS',files:r.files.length,mathematicalVerdict:false,cleanProductionGate:false}));
 process.exit(0);
}
if(fs.existsSync(recordPath))throw Error('Already preserved');
for(const n of names)if(fs.existsSync(path.join(into,n)))throw Error('Refuse existing target '+n);
const sourceChecks=names.map(n=>({dossier:n,result:execFileSync(process.execPath,[path.join(from,n,'check_packet.mjs')],{encoding:'utf8'})}));
const planned=names.flatMap(n=>walk(path.join(from,n)).map(rel=>{
 const source=path.join(from,n,rel),b=fs.readFileSync(source);
 return{dossier:n,relativePath:rel,source,repositoryPath:path.relative(root,path.join(into,n,rel)),bytes:b.length,sha256:hash(b)};
}));
for(const p of planned){
 const dest=path.join(root,p.repositoryPath);
 fs.mkdirSync(path.dirname(dest),{recursive:true});
 fs.copyFileSync(p.source,dest,fs.constants.COPYFILE_EXCL);
 if(hash(fs.readFileSync(dest))!==p.sha256||hash(fs.readFileSync(p.source))!==p.sha256)throw Error('Copy drift');
}
const r={date:'2026-09-01',status:'Unpromoted mathematical drafts; exact byte preservation only',files:planned,sourceChecks,externalPointers:'Original exact dependency pointers are retained, not rewritten. Some original baseline/source checkers require their original absolute dependencies; this archive does not claim complete relocation of those dependencies.',newProductionCalls:false,liveBookEdits:false};
fs.writeFileSync(recordPath,JSON.stringify(r,null,2)+'\n',{flag:'wx'});
const all=[...planned.map(p=>p.repositoryPath),...['preserve.mjs','README.md','PRESERVATION.json','COMMIT_PATHS.nul'].map(p=>path.relative(root,path.join(own,p)))].sort();
if(new Set(all).size!==all.length)throw Error('Duplicate commit path');
fs.writeFileSync(path.join(own,'COMMIT_PATHS.nul'),all.join('\0')+'\0',{flag:'wx'});
console.log(JSON.stringify({preserved:true,dossiers:names.length,files:planned.length,commitPaths:all.length}));
