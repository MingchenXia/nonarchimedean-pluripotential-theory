import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {execFileSync} from "node:child_process";
import {fileURLToPath} from "node:url";
export const dir=path.dirname(fileURLToPath(import.meta.url));
export const config=JSON.parse(fs.readFileSync(path.join(dir,"ORIGIN_MAP.json"),"utf8"));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const inside=(a,b)=>a===b||a.startsWith(b+path.sep);
const stat=p=>{try{return fs.lstatSync(p)}catch(e){if(e.code==="ENOENT")return null;throw e}};
function regular(p){
 const s=stat(p);
 if(!s||!s.isFile()||s.isSymbolicLink())throw Error("Not an ordinary file: "+p);
 return s;
}
function noSymlink(p,base){
 if(!inside(p,base))throw Error("Path escapes root: "+p);
 for(let q=p;inside(q,base);q=path.dirname(q)){
  const s=stat(q);if(s?.isSymbolicLink())throw Error("Symlink refused: "+q);
  if(q===base)break;
 }
}
function walk(base){
 const out=[];
 function visit(p){
  const s=fs.lstatSync(p);if(s.isSymbolicLink())throw Error("Symlink refused: "+p);
  if(s.isDirectory())for(const n of fs.readdirSync(p).sort())visit(path.join(p,n));
  else if(s.isFile()){
   const relative=path.relative(base,p);
   if(/[\x00-\x1f\x7f]/.test(relative))throw Error("Control byte in filename");
   out.push(relative);
  }else throw Error("Special file refused: "+p);
 }
 visit(base);return out;
}
function dataInfo(p){regular(p);const b=fs.readFileSync(p);return{bytes:b.length,sha256:hash(b)};}
function matches(b,e){return hash(b)===e.sha256&&(e.bytes===undefined||b.length===e.bytes);}
function mirror(original){
 if(inside(original,config.sourceWorktree))return path.join(config.repository,path.relative(config.sourceWorktree,original));
 return null;
}
function selectedOrigin(original){
 return config.names.some(n=>inside(original,path.join(config.sourceBase,n)));
}
function resolvePin(original,e,archived){
 const mapped=mirror(original);
 const checked=[];
 let chosen=null;
 const order=archived?[mapped,original]:[original,mapped];
 for(const p of [...new Set(order.filter(Boolean))]){
  if(!stat(p))continue;
  regular(p);const b=fs.readFileSync(p);
  checked.push({path:p,bytes:b.length,sha256:hash(b),matches:matches(b,e)});
  if(matches(b,e)&&!chosen)chosen={path:p,bytes:b.length,sha256:hash(b),method:p===original?"original-absolute-path":"verified-durable-mirror"};
 }
 const binding=config.historicalBindings.find(x=>x.path===original&&x.sha256===e.sha256);
 if(!chosen&&binding){
  let b=execFileSync("git",["show",binding.commit+":"+binding.repositoryPath],{cwd:config.repository,maxBuffer:2**24});
  for(const step of binding.replacements??[]){
   const before=resolvePin(step.beforeFile,{sha256:step.beforeSha256},archived).chosen.path;
   const after=resolvePin(step.afterFile,{sha256:step.afterSha256},archived).chosen.path;
   let a=fs.readFileSync(before,"utf8"),z=fs.readFileSync(after,"utf8");
   if(step.stripAfterHeaderBefore){const i=z.indexOf(step.stripAfterHeaderBefore);if(i<0)throw Error("Historical header marker missing");z=z.slice(i);}
   if(step.trimTerminalWhitespace){a=a.trimEnd();z=z.trimEnd();}
   const s=b.toString("utf8");if(s.split(a).length!==2)throw Error("Historical substitution not unique");b=Buffer.from(s.replace(a,z));
  }
  if(matches(b,e))chosen={path:original,bytes:b.length,sha256:hash(b),method:binding.replacements?"historical-exact-reconstruction":"historical-git-blob",commit:binding.commit,repositoryPath:binding.repositoryPath,...(binding.replacements?{replacements:binding.replacements}:{})};
 }
 if(!chosen)throw Error("Pin mismatch or unavailable: "+original+" expected "+e.sha256);
 if(archived&&selectedOrigin(original)&&chosen.path!==mapped)throw Error("Selected archived file is missing or corrupt: "+mapped);
 return{originalAbsolutePath:original,durableCandidate:mapped,chosen,checked};
}
function pinOccurrences(json,file){
 const out=[];
 function visit(v,pointer){
  if(!v||typeof v!=="object")return;
  if(typeof v.sha256==="string"&&/^[a-f0-9]{64}$/.test(v.sha256)&&(typeof v.path==="string"||typeof v.file==="string"))
   out.push({rawPath:v.path??v.file,sha256:v.sha256,...(v.bytes===undefined?{}:{bytes:v.bytes}),pointer});
  if(typeof v.source==="string"&&/^[a-f0-9]{64}$/.test(v.sourceSha256??""))
   out.push({rawPath:v.source,sha256:v.sourceSha256,pointer:pointer+"/sourceSha256"});
  for(const [k,x]of Object.entries(v))visit(x,pointer+"/"+k);
 }
 visit(json,"");return out.map(e=>({...e,container:file}));
}
function auditDossiers(archived){
 const occurrences=[],counts={manifestEntries:0,checksumEntries:0,jsonPins:0,manifests:0,sumFiles:0,historicalPins:0};
 for(const name of config.names){
  const originalBase=path.join(config.sourceBase,name),readBase=path.join(archived?config.targetBase:config.sourceBase,name);
  for(const relative of walk(readBase)){
   const p=path.join(readBase,relative);
   if(relative.endsWith(".json")){
    const json=JSON.parse(fs.readFileSync(p,"utf8"));
    if(path.basename(relative)==="MANIFEST.json"){
     const entries=json.files??json.entries;
     if(!Array.isArray(entries))throw Error("Unknown manifest format: "+p);
     counts.manifests++;counts.manifestEntries+=entries.length;
    }
    for(const e of pinOccurrences(json,relative)){
     const containerOriginal=path.join(originalBase,relative);
     const absolute=path.resolve(path.dirname(containerOriginal),e.rawPath);
     const r=resolvePin(absolute,e,archived);
     if(r.chosen.method.startsWith("historical-"))counts.historicalPins++;
     occurrences.push({dossier:name,originalSourceBase:originalBase,kind:"JSON identity pin",...e,...r,externalToDossier:!inside(absolute,originalBase)});
     counts.jsonPins++;
    }
   }
   if(path.basename(relative)==="SHA256SUMS"){
    counts.sumFiles++;
    for(const [i,line]of fs.readFileSync(p,"utf8").trimEnd().split("\n").entries()){
     const m=/^([a-f0-9]{64})[ \t]+[*]?(.+)$/.exec(line);
     if(!m)throw Error("Malformed checksum line: "+p+":"+(i+1));
     const e={rawPath:m[2],sha256:m[1]},absolute=path.resolve(path.dirname(path.join(originalBase,relative)),e.rawPath);
     const r=resolvePin(absolute,e,archived);
     occurrences.push({dossier:name,originalSourceBase:originalBase,kind:"SHA256SUMS",container:relative,line:i+1,...e,...r,externalToDossier:!inside(absolute,originalBase)});
     counts.checksumEntries++;
    }
   }
  }
 }
 return{counts,occurrences};
}
export function plan(){
 const files=[];
 for(const name of config.names){
  const src=path.join(config.sourceBase,name),dst=path.join(config.targetBase,name);
  noSymlink(src,config.sourceBase);noSymlink(dst,config.targetBase);
  const names=walk(src),targetNames=stat(dst)?walk(dst):[];
  for(const extra of targetNames)if(!names.includes(extra))throw Error("Unrequested existing target file: "+path.join(dst,extra));
  for(const relative of names){
   const source=path.join(src,relative),target=path.join(dst,relative),info=dataInfo(source);
   noSymlink(target,config.targetBase);
   if(stat(target)){
    const existing=dataInfo(target);
    if(existing.sha256!==info.sha256||existing.bytes!==info.bytes)throw Error("Different target refuses overwrite: "+target);
   }
   files.push({dossier:name,relativePath:relative,source,target,repositoryPath:path.relative(config.repository,target),...info,action:stat(target)?"existing-identical":"copy-new"});
  }
 }
 for(const p of config.requiredPins){
  const f=files.find(x=>x.dossier===p.name&&x.relativePath===p.file);
  if(!f||f.sha256!==p.sha256)throw Error("Announced frozen pin mismatch: "+p.name+"/"+p.file);
 }
 const checks=auditDossiers(false);
 return{files,checks};
}
const generated=["COPIED_FILES.json","EXTERNAL_REFERENCES.json","PRESERVATION_RECORD.json","COMMIT_PATHS.nul","MANIFEST.json","SHA256SUMS"];
const staticOwn=["README.md","ORIGIN_MAP.json","preserve.mjs","preservation_lib.mjs","verify_relocated.mjs"];
function writeNew(name,bytes){fs.writeFileSync(path.join(dir,name),bytes,{flag:"wx"});}
export function copy(){
 for(const n of generated)if(stat(path.join(dir,n)))throw Error("Record already exists; use read-only verify: "+n);
 const p=plan();
 for(const f of p.files){
  noSymlink(f.target,config.targetBase);
  fs.mkdirSync(path.dirname(f.target),{recursive:true});
  if(f.action==="copy-new")fs.copyFileSync(f.source,f.target,fs.constants.COPYFILE_EXCL);
  const a=dataInfo(f.source),b=dataInfo(f.target);
  if(a.sha256!==f.sha256||b.sha256!==f.sha256||b.bytes!==f.bytes)throw Error("Copy/end-source mismatch: "+f.target);
 }
 const after=auditDossiers(true);
 const json=v=>Buffer.from(JSON.stringify(v,null,2)+"\n");
 const listed=staticOwn.concat(generated).map(n=>path.relative(config.repository,path.join(dir,n)));
 const commitPaths=[...p.files.map(f=>f.repositoryPath),...listed].sort();
 if(new Set(commitPaths).size!==commitPaths.length)throw Error("Duplicate commit path");
 writeNew("COPIED_FILES.json",json({date:config.date,meaning:"Every dossier-owned file, copied byte-for-byte; external dependencies not copied.",files:p.files}));
 writeNew("EXTERNAL_REFERENCES.json",json({date:config.date,meaning:"Each external pin resolves against its ORIGINAL source container. Existing matching durable mirrors may be used. Historical live-context pins are separately identified; no frozen manifest was rewritten.",references:after.occurrences.filter(e=>e.externalToDossier)}));
 const record={date:config.date,status:"PASS: mechanical preservation only",dossiers:config.names.length,ownedFiles:p.files.length,
 copiedNew:p.files.filter(f=>f.action==="copy-new").length,alreadyIdentical:p.files.filter(f=>f.action==="existing-identical").length,
 ownedBytes:p.files.reduce((a,f)=>a+f.bytes,0),ownedPngFiles:p.files.filter(f=>f.relativePath.endsWith(".png")).length,
 originChecks:p.checks.counts,archiveChecks:after.counts,externalPinOccurrences:after.occurrences.filter(e=>e.externalToDossier).length,
 externalOriginalPaths:[...new Set(after.occurrences.filter(e=>e.externalToDossier).map(e=>e.originalAbsolutePath))].sort(),
 commitPaths:commitPaths.length,sourceBase:config.sourceBase,targetBase:config.targetBase,
 noExternalSourceFilesCopied:true,noFrozenManifestsRewritten:true,noLiveBookEdits:true,noGitStageOrCommit:true,noProductionCalls:true,
 limitation:"Direct frozen MF/SUM and JSON/source pins checked, not a recursive audit or copy of every unselected dependency tree. Original embedded checkers are not asserted relocatable."};
 writeNew("PRESERVATION_RECORD.json",json(record));
 writeNew("COMMIT_PATHS.nul",Buffer.from(commitPaths.join("\0")+"\0","utf8"));
 const localForManifest=staticOwn.concat(generated.filter(n=>!["MANIFEST.json","SHA256SUMS"].includes(n)));
 const all=localForManifest.map(n=>({path:n,...dataInfo(path.join(dir,n))}))
  .concat(p.files.map(f=>({path:path.relative(dir,f.target),bytes:f.bytes,sha256:f.sha256})));
 writeNew("MANIFEST.json",json({schema:1,date:config.date,status:"Frozen mechanical preservation; no mathematical or production status changed.",files:all}));
 const sums=all.concat({path:"MANIFEST.json",...dataInfo(path.join(dir,"MANIFEST.json"))}).map(f=>f.sha256+"  "+f.path).join("\n")+"\n";
 writeNew("SHA256SUMS",Buffer.from(sums));
 return verify();
}
export function verify(){
 const ledger=JSON.parse(fs.readFileSync(path.join(dir,"COPIED_FILES.json"),"utf8"));
 for(const f of ledger.files){
  noSymlink(f.target,config.targetBase);const b=fs.readFileSync(f.target);
  if(!matches(b,f))throw Error("Archived byte mismatch: "+f.target);
 }
 for(const name of config.names){
  const expected=ledger.files.filter(f=>f.dossier===name).map(f=>f.relativePath).sort();
  const actual=walk(path.join(config.targetBase,name)).sort();
  if(JSON.stringify(expected)!==JSON.stringify(actual))throw Error("Archived directory membership mismatch: "+name);
 }
 const checks=auditDossiers(true);
 const mf=JSON.parse(fs.readFileSync(path.join(dir,"MANIFEST.json"),"utf8"));
 for(const e of mf.files){const b=fs.readFileSync(path.resolve(dir,e.path));if(!matches(b,e))throw Error("Preservation manifest mismatch: "+e.path);}
 const lines=fs.readFileSync(path.join(dir,"SHA256SUMS"),"utf8").trimEnd().split("\n");
 for(const line of lines){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);if(!m||hash(fs.readFileSync(path.resolve(dir,m[2])))!==m[1])throw Error("Preservation sums mismatch");}
 const paths=fs.readFileSync(path.join(dir,"COMMIT_PATHS.nul"));
 if(paths.at(-1)!==0)throw Error("Missing final NUL");
 const names=paths.toString("utf8").slice(0,-1).split("\0");
 const expected=[...ledger.files.map(f=>f.repositoryPath),...staticOwn.concat(generated).map(n=>path.relative(config.repository,path.join(dir,n)))].sort();
 if(JSON.stringify(names)!==JSON.stringify(expected)||new Set(names).size!==names.length)throw Error("NUL commit table mismatch");
 for(const p of names)if(path.isAbsolute(p)||p.split(path.sep).includes("..")||!stat(path.join(config.repository,p)))throw Error("Unsafe/missing commit path");
 return{status:"PASS",archivedDossiers:config.names.length,archivedOwnedFiles:ledger.files.length,
 archiveChecks:checks.counts,preservationManifestEntries:mf.files.length,preservationChecksumEntries:lines.length,
 nulCommitPaths:names.length,externalFilesNotCopied:true,frozenManifestsUnchanged:true,writesDuringVerify:0,
 note:"Relocation-aware direct-identity check, not a production or mathematical verdict."};
}
