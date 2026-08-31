import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
// Read-only exact-byte and static-interface checker; no mathematical verdict.
const dir=path.dirname(fileURLToPath(import.meta.url));
const packet=path.resolve(dir,'../p081_curve_base_fiber_extension_research_20260831');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const expected={ 'statement.tex':'6122b495f877fc78c861a99a3a29ce06d015ac3c9d27de982f7526fd245aace4',
 'proof.tex':'96434222904dd0d66b60b67a2cf32230789f0cff139aac0d784be5bf382ca77e',
 'SHA256SUMS':'a70a097b770c5077a9c42fa8215b3dd2f2921ff4b7858a900ea4e90e0eb4d7e0'};
const principal=Object.entries(expected).map(([f,h])=>{
 const e=entry(path.join(packet,f));if(e.sha256!==h)throw Error('Principal mismatch '+f);return e;});
const manifest=fs.readFileSync(path.join(packet,'SHA256SUMS'),'utf8');
const entries=manifest.trim().split('\n').map(l=>{
 const m=l.match(/^([0-9a-f]{64})  (.+)$/);if(!m)throw Error('Malformed manifest line');
 const p=path.resolve(packet,m[2]),e=entry(p);if(e.sha256!==m[1])throw Error('Mismatch '+p);return e;});
const core=['statement.tex','proof.tex'].map(f=>fs.readFileSync(path.join(packet,f),'utf8')).join('\n');
const labels=[...core.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const cites=[...core.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const bib=fs.readFileSync(path.join(packet,'references.bib'),'utf8');
const keys=[...bib.matchAll(/@\w+\{([^,]+),/g)].map(m=>m[1]);
const missingRefs=refs.filter(r=>!labels.includes(r)),missingCites=cites.filter(r=>!keys.includes(r));
if(new Set(labels).size!==labels.length||missingRefs.length||missingCites.length)throw Error('Static interface mismatch');
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(core))throw Error('Unexpected control byte');
process.stdout.write(JSON.stringify({status:'read-only mechanical checks; mathematical verdict is separate',
 packet,principal,entries,checkedManifestEntries:entries.length,mismatches:0,labels:labels.length,
 referenceUses:refs.length,citationUses:cites.length,missingRefs,missingCites,
 compiled:false,pdfProduced:false,productionCalled:false},null,2)+'\n');
