import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sourceRoot='/private/tmp/nappt_p071_20260827';
const durableRoot='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix='manuscript/editorial/solver_dossiers_20260831';
const ownRelative=path.join(prefix,path.basename(here));
const names=[
 'p081_ch20_weighted_intersection_repair_20260831',
 'p081_ch20_weighted_intersection_independent_audit_20260831',
 'p081_ch20_ch22_ch24_unit_weight_followup_20260831',
 'p081_ch20_ch22_ch24_unit_weight_followup_independent_audit_20260831',
 'p081_ch23_curve_consumer_repair_20260831',
 'p081_ch23_curve_consumer_independent_audit_20260831',
 'p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831',
 'p081_ch29_ch31_assembled_independent_audit_20260831',
 'p081_ch29_ch31_pedagogy_review_20260831',
 'p081_weighted_energy_consumers_repair_20260831',
 'p081_weighted_energy_root_audit_20260831',
 'p081_ch28_curve_uniqueness_snc_repair_20260831',
 'p081_ch28_curve_uniqueness_snc_independent_audit_20260831',
 'p081_uniform_fiber_extension_research_20260831',
 'p081_uniform_fiber_extension_independent_audit_20260831',
 'p081_curve_base_fiber_extension_research_20260831',
 'p081_curve_base_fiber_extension_independent_audit_20260831',
 'p081_ch25_weighted_capacity_repair_20260831',
 'p081_ch25_weighted_capacity_independent_audit_20260831',
 'p081_ch25_fixed_reference_example_independent_check_20260831',
 'p081_real_model_max_independent_audit_20260831',
 'p081_ch20_ch21_real_model_max_repair_20260831',
 'p081_ch20_ch21_real_model_max_repair_audit_20260831',
 'p081_ch20_ch21_real_model_max_fresh_independent_audit_20260831',
 'p081_bounded_model_net_normalization_repair_20260831',
 'p081_bounded_model_net_normalization_root_audit_20260831',
 'p081_ch24_real_maximum_locality_repair_20260831',
 'p081_ch24_real_maximum_locality_root_audit_20260831',
 'p081_bounded_net_and_ch24_downstream_independent_audit_20260831',
 'p081_curve_repair_research_checkpoint_20260831',
 'p081_weighted_curve_full_syntax_review_20260831'
];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function walk(relative){return fs.readdirSync(path.join(sourceRoot,relative),{withFileTypes:true}).flatMap(e=>{
 if(e.isSymbolicLink())throw Error('unexpected symlink');
 const p=path.join(relative,e.name);return e.isDirectory()?walk(p):e.name==='.DS_Store'?[]:[p];
});}
const files=names.flatMap(n=>walk(path.join(prefix,n))).map(relative=>({source:path.join(sourceRoot,relative),relative}));
for(const relative of [
 'manuscript/frontmatter/preface.tex',
 'manuscript/editorial/envelope_transfer_and_curve_repairs_checkpoint_20260831.md',
 'manuscript/editorial/foundational_model_and_capacity_repair_checkpoint_20260831.md',
 path.join(ownRelative,'preserve.mjs'),path.join(ownRelative,'GITHUB_REMOTE_CHECK.json')
])files.push({source:path.join(sourceRoot,relative),relative});
const buildRoot=path.join(sourceRoot,prefix,'p081_weighted_curve_full_syntax_review_20260831');
const buildRecords=[
 ['BUILD.json','pass4.log'],['revised1/BUILD.json','pass6.log'],
 ['revised2/STABILIZED_BUILD.json','pass9.log']
];
for(const [recordPath,name] of buildRecords){
 const b=JSON.parse(fs.readFileSync(path.join(buildRoot,recordPath),'utf8'));
 const expected=b.finalLog?.sha256??b.runs.at(-1).log.sha256;
 const source=path.join(b.scratchDirectory,name);
 if(sha(fs.readFileSync(source))!==expected)throw Error('stable build log mismatch '+name);
 files.push({source,relative:path.join(ownRelative,'build_logs',name)});
}
const last=JSON.parse(fs.readFileSync(path.join(buildRoot,'revised3/BUILD.json'),'utf8'));
const lastLog=last.runs.at(-1).log;
if(last.exitCode!==0||last.pdfProduced||last.warnings.some(s=>/undefined|Rerun|Label\(s\).*changed/.test(s)))throw Error('latest syntax review not stable');
if(sha(fs.readFileSync(lastLog.path))!==lastLog.sha256)throw Error('latest build log changed');
files.push({source:lastLog.path,relative:path.join(ownRelative,'build_logs',path.basename(lastLog.path))});
for(const [source,expected] of [
 ['/private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf','8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270'],
 ['/private/tmp/BFJ_singular_1201.0187_audit_20260831.txt','df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f']
]){
 if(sha(fs.readFileSync(source))!==expected)throw Error('primary source changed');
 files.push({source,relative:path.join(ownRelative,'primary_sources',path.basename(source))});
}
if(new Set(files.map(e=>e.relative)).size!==files.length)throw Error('duplicate destination');
const entries=files.map(e=>{
 const bytes=fs.readFileSync(e.source),target=path.join(durableRoot,e.relative),hash=sha(bytes);
 if(fs.existsSync(target)&&sha(fs.readFileSync(target))!==hash)throw Error('refuse differing durable file '+e.relative);
 if(!e.relative.endsWith('.pdf')&&/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(bytes.toString('utf8')))throw Error('credential-like string; inspect privately before committing '+e.relative);
 return{...e,bytes:bytes.length,sha256:hash,alreadyPresent:fs.existsSync(target)};
});
if(!process.argv.includes('--copy')){console.log(JSON.stringify({preflight:true,directories:names.length,files:entries.length,newFiles:entries.filter(e=>!e.alreadyPresent).length,bytes:entries.reduce((s,e)=>s+e.bytes,0)},null,2));process.exit(0);}
for(const e of entries){
 if(sha(fs.readFileSync(e.source))!==e.sha256)throw Error('source changed during copy');
 const dest=path.join(durableRoot,e.relative);fs.mkdirSync(path.dirname(dest),{recursive:true});
 if(!e.alreadyPresent)fs.copyFileSync(e.source,dest,fs.constants.COPYFILE_EXCL);
 if(sha(fs.readFileSync(dest))!==e.sha256)throw Error('copy mismatch');
}
const output={date:'2026-08-31',kind:'explicit frozen-source preservation; no mathematical integration',sourceRoot,durableRoot,directories:names,files:entries,latestBuild:JSON.parse(fs.readFileSync(path.join(buildRoot,'revised3/BUILD.json'),'utf8')),excluded:'unfinished general-SNC research and unrelated untracked files',credentialHeuristic:'no credential-like strings detected in selected text files'};
const data=JSON.stringify(output,null,2)+'\n',manifest=path.join(here,'PRESERVATION.json');fs.writeFileSync(manifest,data,{flag:'wx'});
const durableManifest=path.join(durableRoot,ownRelative,'PRESERVATION.json');fs.writeFileSync(durableManifest,data,{flag:'wx'});
const commitPaths=[...entries.map(e=>e.relative),path.join(ownRelative,'PRESERVATION.json')].sort();
const paths=Buffer.from(commitPaths.join('\0')+'\0');fs.writeFileSync(path.join(here,'COMMIT_PATHS.nul'),paths,{flag:'wx'});fs.writeFileSync(path.join(durableRoot,ownRelative,'COMMIT_PATHS.nul'),paths,{flag:'wx'});
console.log(JSON.stringify({copied:true,directories:names.length,files:entries.length,newFiles:entries.filter(e=>!e.alreadyPresent).length,bytes:entries.reduce((s,e)=>s+e.bytes,0),preservationSha256:sha(data),commitPathCount:commitPaths.length},null,2));
