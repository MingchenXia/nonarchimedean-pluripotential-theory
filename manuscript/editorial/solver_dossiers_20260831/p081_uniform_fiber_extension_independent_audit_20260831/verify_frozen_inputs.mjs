// Read-only frozen-input checker. Mathematical findings are in INDEPENDENT_AUDIT.md.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
const candidate='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_uniform_fiber_extension_research_20260831';
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p,'utf8');
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:digest(b)};};
const sums=path.join(candidate,'SHA256SUMS');
if(record(sums).sha256!=='97a7c2bacd9aeabd7eafc7ebce32cc4ba253a88c573f4317efd74ba62abda262')throw Error('Frozen inventory changed');
const inputs=[];
for(const line of read(sums).trim().split('\n')){
 const m=/^([0-9a-f]{64})  (.+)$/.exec(line);if(!m)throw Error('Malformed inventory line');
 const p=path.isAbsolute(m[2])?m[2]:path.join(candidate,m[2]);
 const e=record(p);if(e.sha256!==m[1])throw Error('Frozen hash mismatch: '+p);inputs.push(e);
}
const expected={
 'statement.tex':'4a758e5271862cad16c2242c5a2778c49de3cb4bff4797ff2a5d22ef0b00b503',
 'proof.tex':'f1b2014cbc612885421d1df26383f146809a0e621c43c98ea30993bf1f3ad3fa'
};
for(const[f,h]of Object.entries(expected))if(record(path.join(candidate,f)).sha256!==h)throw Error('Principal bytes changed');
const principal=Object.keys(expected).map(f=>read(path.join(candidate,f))).join('\n');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(principal))throw Error('Forbidden TeX control byte');
const labels=[...principal.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...principal.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(new Set(labels).size!==labels.length)throw Error('Duplicate label');
if(refs.some(r=>!labels.includes(r)))throw Error('Unresolved local reference');
const bib=read(path.join(candidate,'references.bib'));
const keys=[...bib.matchAll(/@\w+\{([^,]+),/g)].map(m=>m[1]);
const cites=[...principal.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
if(cites.some(k=>!keys.includes(k)))throw Error('Missing citation key');
const checks={
 date:'2026-08-31',status:'mechanical evidence only; independent mathematical verdict is in INDEPENDENT_AUDIT.md',
 frozen_inventory_entries:inputs.length,hash_mismatches:0,principal_hashes_match:true,
 labels:labels.length,reference_occurrences:refs.length,citation_occurrences:cites.length,
 duplicate_labels:[],unresolved_references:[],missing_bibliography_keys:[],
 forbidden_control_bytes:false,compile_performed:false,pdf_visual_QA_performed:false,production_submitted:false,
 mathematical_scope:'unconditional constant-case FS extension; EP transfer conditional on explicit ambient EP',
 continuity_or_arbitrary_field_claim:false
};
const checkBytes=Buffer.from(JSON.stringify(checks,null,2)+'\n');
const manifest={
 date:'2026-08-31',status:'independent no-substantive-gap review; not production or integration acceptance',
 candidate_inventory:record(sums),reviewed_inputs:inputs,
 outputs:[record(path.join(dir,'INDEPENDENT_AUDIT.md')),record(path.join(dir,'verify_frozen_inputs.mjs')),
 {path:path.join(dir,'CHECKS.json'),bytes:checkBytes.length,sha256:digest(checkBytes)}],
 limitations:['Ambient EP theorem is an explicit conditional input, not fully re-audited here.',
 'Source PDF bytes hashed only; cited interfaces read from matching source text.',
 'No compile, PDF, live edit or production submission.',
 'Manifest excludes its own self-hash.']
};
console.log(JSON.stringify({checks,manifest},null,2));
