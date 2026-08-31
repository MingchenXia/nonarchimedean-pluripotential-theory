// Preserve exact frozen research files in the durable project without overwriting.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sourceRoot='/private/tmp/nappt_p071_20260827';
const durableRoot='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix='manuscript/editorial/solver_dossiers_20260831';
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
 'p081_uniform_fiber_extension_research_20260831',
 'p081_uniform_fiber_extension_independent_audit_20260831'
];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const walk=rel=>fs.readdirSync(path.join(sourceRoot,rel),{withFileTypes:true}).flatMap(e=>{
 const file=path.join(rel,e.name);if(e.isSymbolicLink())throw Error('Unexpected symlink: '+file);
 return e.isDirectory()?walk(file):e.name==='.DS_Store'?[]:[file];
});
const files=names.flatMap(n=>walk(path.join(prefix,n)));
const entries=files.map(relative=>{
 const bytes=fs.readFileSync(path.join(sourceRoot,relative));
 const target=path.join(durableRoot,relative),hash=sha(bytes);
 if(fs.existsSync(target)&&sha(fs.readFileSync(target))!==hash)throw Error('Refuse to overwrite differing durable file: '+relative);
 return{relative,bytes:bytes.length,sha256:hash,alreadyPresent:fs.existsSync(target)};
});
if(process.argv.includes('--copy'))for(const e of entries){
 const from=path.join(sourceRoot,e.relative),to=path.join(durableRoot,e.relative);
 if(sha(fs.readFileSync(from))!==e.sha256)throw Error('Source changed during preservation: '+e.relative);
 if(!e.alreadyPresent){fs.mkdirSync(path.dirname(to),{recursive:true});fs.copyFileSync(from,to,fs.constants.COPYFILE_EXCL);}
 if(sha(fs.readFileSync(to))!==e.sha256)throw Error('Copy verification failed: '+e.relative);
}
const result={date:'2026-08-31',kind:'frozen research preservation, not live integration',sourceRoot,durableRoot,executed:process.argv.includes('--copy'),directories:names,files:entries};
if(result.executed)fs.writeFileSync(path.join(here,'PRESERVATION.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({executed:result.executed,directories:names.length,files:entries.length,newFiles:entries.filter(e=>!e.alreadyPresent).length,bytes:entries.reduce((s,e)=>s+e.bytes,0)},null,2));
