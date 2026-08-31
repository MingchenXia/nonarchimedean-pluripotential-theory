// Default is read-only. --copy preserves only the explicitly pinned dossiers.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const sourceRoot='/private/tmp/nappt_p071_20260827';
const durableRoot='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix='manuscript/editorial/solver_dossiers_20260831';
const here=path.dirname(fileURLToPath(import.meta.url));
const own=path.relative(sourceRoot,here);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=new Map([
 ['p213_residual_curve_functional_interface_research_20260831/MANIFEST.json','175b64dfd4e08ad59dcb561928ab50172194e04af264c4641b49c8dcc0359278'],
 ['p213_residual_curve_functional_interface_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md','177d0ca3454b6f73caedf81fe4eaa34f674a712460ace16409b36115892f2359'],
 ['p213_residual_curve_functional_interface_independent_audit_20260831/SOURCE_LEDGER.md','66f9c9e662eb186cb2934a17b56b5a2d7090511a86db0cea9f10c8b44432bb84'],
 ['p213_residual_curve_functional_interface_independent_audit_20260831/SHA256SUMS','b0897da0a383909fd6639f7a5680693bb1f52f5017b64732f46ac9252d90adf8'],
 ['p213_residual_curve_functional_draftcheck_20260831/MANIFEST.json','d4f5a7653dc06fdad87ba7d342cb5ce268ff6b469ca77f6abf90be15c6e8db76'],
]);
for(const [relative,expected] of pins){
 if(sha(fs.readFileSync(path.join(sourceRoot,prefix,relative)))!==expected)
  throw Error('Changed frozen pin: '+relative);
}
const directories=[...new Set([...pins.keys()].map(p=>path.dirname(p)))];
function walk(relative){
 return fs.readdirSync(path.join(sourceRoot,relative),{withFileTypes:true})
  .sort((a,b)=>a.name.localeCompare(b.name)).flatMap(entry=>{
   if(entry.isSymbolicLink())throw Error('Unexpected symlink');
   const next=path.join(relative,entry.name);
   return entry.isDirectory()?walk(next):entry.name==='.DS_Store'?[]:[next];
  });
}
const paths=directories.flatMap(d=>walk(path.join(prefix,d)));
paths.push('manuscript/editorial/chapter72_cld_product_checkpoint_20260831.md',path.join(own,'preserve.mjs'));
if(new Set(paths).size!==paths.length)throw Error('Duplicate selected path');
const files=paths.map(relative=>{
 if(path.isAbsolute(relative)||relative.split(path.sep).includes('..'))throw Error('Unsafe path');
 const source=path.join(sourceRoot,relative),target=path.join(durableRoot,relative);
 const bytes=fs.readFileSync(source),hash=sha(bytes),present=fs.existsSync(target);
 if(present&&sha(fs.readFileSync(target))!==hash)throw Error('Refuse different durable bytes: '+relative);
 if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(bytes.toString('utf8')))
  throw Error('Credential-like string; inspect privately: '+relative);
 return {relative,bytes:bytes.length,sha256:hash,alreadyPresent:present};
});
const summary={directories:directories.length,files:files.length,newFiles:files.filter(x=>!x.alreadyPresent).length,bytes:files.reduce((s,x)=>s+x.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary},null,2));process.exit(0);}
for(const root of [sourceRoot,durableRoot])for(const name of ['PRESERVATION.json','COMMIT_PATHS.nul'])
 if(fs.existsSync(path.join(root,own,name)))throw Error('Already preserved');
for(const entry of files){
 const source=path.join(sourceRoot,entry.relative),target=path.join(durableRoot,entry.relative);
 if(sha(fs.readFileSync(source))!==entry.sha256)throw Error('Input drift during copy');
 fs.mkdirSync(path.dirname(target),{recursive:true});
 if(!entry.alreadyPresent)fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
 if(sha(fs.readFileSync(target))!==entry.sha256)throw Error('Copy mismatch');
}
const report={date:'2026-08-31',sourceRoot,durableRoot,directories,files,
 status:'Bounded independently reviewed product research; production pending; no live theorem edit or atom retirement',
 credentialHeuristic:'No credential-like string detected',
 excluded:'Unfinished torsor and current-separation follow-ups; unrelated worktree files; external source PDFs'};
const data=JSON.stringify(report,null,2)+'\n';
const commitPaths=[...paths,path.join(own,'PRESERVATION.json')].sort();
for(const root of [sourceRoot,durableRoot]){
 fs.writeFileSync(path.join(root,own,'PRESERVATION.json'),data,{flag:'wx'});
 fs.writeFileSync(path.join(root,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});
}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(data)},null,2));
