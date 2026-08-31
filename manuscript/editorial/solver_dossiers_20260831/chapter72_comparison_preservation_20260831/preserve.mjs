// Default: read-only preflight. --copy preserves only the explicit frozen work.
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
 ['p147_source_correction_independent_audit_20260831/SOURCE_CORRECTION_AUDIT.md','afa9420dc2ec5d3b029d5a60a4368093ded498ad0a85e0f43132dbbbd072260e'],
 ['p147_live_source_correction_20260831/MANIFEST.json','f3d95e752a4013ea00d657ad799ba6556e772ecfebe87ce692e601c930ad2eea'],
 ['p213_auxiliary_obstructions_independent_audit_20260831/INDEPENDENT_AUXILIARY_AUDIT.md','8793e00d1c4f5635ab127e4584fac5c9761e6f6aecbe45aa3e5af31fb1aad1a2'],
 ['p143_dominated_divisorial_research_20260831/MANIFEST.json','c2da7ad2ecb958415835af56e906b2e89a76587a365686b7a79c38e67be1b5a7'],
 ['p143_dominated_divisorial_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md','6205fdb014e6364aa8d14fa6a3ec6313da9c16b585bccb9617415dd31474b1d2'],
 ['p143_kahler_truncation_research_20260831/MANIFEST.json','f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b'],
 ['p143_kahler_truncation_independent_audit_20260831/CONDITIONAL_AUDIT.md','3bfe0d21e177b422282a64f6a6252729fe53dbffd6ca5a03d3021f134e687522'],
 ['p143_nef_closure_research_20260831/MANIFEST.json','8b03ba68f6a8a1e901d19befd9e832088481d371c936b1349603898317a0bb3b'],
 ['p143_nef_closure_independent_audit_20260831/INDEPENDENT_CONDITIONAL_EXACT_BYTE_AUDIT.md','c1814f2cf8c60b0f91cd2f5a330fe0f2d48971ba454bc56e14b37a4c1e1106dc'],
 ['p14_pseff_all_point_operations_research_20260831/MANIFEST.json','f42fd86160b4a719696d7b0acfec25e741cdfa06c3066a807f9d30a078871add'],
 ['p14_pseff_all_point_operations_independent_audit_20260831/CONDITIONAL_AUDIT.md','cf52f916ba1b501113454dcfd737d7c1759ed5c1ddff61d47662b5641f829341'],
]);
for(const [p,h] of pins)if(sha(fs.readFileSync(path.join(sourceRoot,prefix,p)))!==h)throw Error('Frozen pin changed: '+p);
const directories=[...new Set([...pins.keys()].map(p=>path.dirname(p)))];
function walk(r){return fs.readdirSync(path.join(sourceRoot,r),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name)).flatMap(e=>{
 if(e.isSymbolicLink())throw Error('Unexpected symlink');
 const p=path.join(r,e.name);return e.isDirectory()?walk(p):e.name==='.DS_Store'?[]:[p];
});}
const paths=directories.flatMap(d=>walk(path.join(prefix,d)));
paths.push('manuscript/editorial/chapter72_comparison_followup_checkpoint_20260831.md',path.join(own,'preserve.mjs'));
paths.push('manuscript/parts/part6/ch72_major_open_problems.tex','manuscript/editorial/open_problem_atomic_inventory_20260824.md','manuscript/bibliography/NonArchimedean.bib');
if(new Set(paths).size!==paths.length)throw Error('Duplicate selected path');
const files=paths.map(relative=>{
 if(path.isAbsolute(relative)||relative.split(path.sep).includes('..'))throw Error('Unsafe path');
 const source=path.join(sourceRoot,relative),target=path.join(durableRoot,relative),b=fs.readFileSync(source),h=sha(b),present=fs.existsSync(target);
 if(present&&sha(fs.readFileSync(target))!==h)throw Error('Refuse different durable bytes: '+relative);
 if(/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(b.toString('utf8')))throw Error('Credential-like string; inspect privately: '+relative);
 return {relative,bytes:b.length,sha256:h,alreadyPresent:present};
});
const summary={directories:directories.length,files:files.length,newFiles:files.filter(x=>!x.alreadyPresent).length,bytes:files.reduce((a,x)=>a+x.bytes,0)};
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,...summary},null,2));process.exit(0);}
for(const r of [sourceRoot,durableRoot])for(const n of ['PRESERVATION.json','COMMIT_PATHS.nul'])if(fs.existsSync(path.join(r,own,n)))throw Error('Already preserved');
for(const x of files){
 const source=path.join(sourceRoot,x.relative),target=path.join(durableRoot,x.relative);
 if(sha(fs.readFileSync(source))!==x.sha256)throw Error('Input drift during copy');
 fs.mkdirSync(path.dirname(target),{recursive:true});
 if(!x.alreadyPresent)fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
 if(sha(fs.readFileSync(target))!==x.sha256)throw Error('Copy mismatch');
}
const report={date:'2026-08-31',sourceRoot,durableRoot,directories,files,status:'Independent/conditional research only; production pending; source-only live corrections; no atom retirement',credentialHeuristic:'No credential-like string detected',excluded:'Unfinished P21.3 follow-up and unrelated worktree files'};
const data=JSON.stringify(report,null,2)+'\n';
const commitPaths=[...paths,path.join(own,'PRESERVATION.json')].sort();
for(const r of [sourceRoot,durableRoot]){
 fs.writeFileSync(path.join(r,own,'PRESERVATION.json'),data,{flag:'wx'});
 fs.writeFileSync(path.join(r,own,'COMMIT_PATHS.nul'),commitPaths.join('\0')+'\0',{flag:'wx'});
}
console.log(JSON.stringify({copied:true,...summary,commitPaths:commitPaths.length,preservationSha256:sha(data)},null,2));
