import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
// Read-only: generated text is returned on stdout, never written here.
const dir=path.dirname(fileURLToPath(import.meta.url));
const root='/private/tmp/nappt_p071_20260827';
const read=p=>fs.readFileSync(p,'utf8');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const entry=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const live=path.join(root,'manuscript/parts/part3/ch25_capacity.tex');
const full=path.join(dir,'patched/ch25_capacity.tex');
const fragment=path.join(dir,'ch25_curve_replacement.tex');
const edits=JSON.parse(read(path.join(dir,'assembly_edits.json')));
let assembled=read(live);
for(const e of edits) {
 if(assembled.split(e.old).length!==2)throw Error('Nonunique edit '+e.name);
 assembled=assembled.replace(e.old,e.replacement);
}
if(assembled.trimEnd()+'\n'!==read(full))throw Error('Full copy differs from exact edit assembly');
if(edits[0].replacement!==read(fragment))throw Error('Fragment differs from assembled first edit');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const original=labels(read(live)),proposed=labels(read(full));
const lost=original.filter(l=>!proposed.includes(l));
if(lost.length||new Set(proposed).size!==proposed.length)throw Error('Label loss/duplication');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?
 walk(path.join(d,e.name)):e.name.endsWith('.tex')?[path.join(d,e.name)]:[]);
const dossier=path.dirname(dir);
const graph26=path.join(dossier,'p081_weighted_energy_consumers_repair_20260831/ch26_graph_replacement.tex');
const graph31=path.join(dossier,'p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/ch31_curve_replacement.tex');
const expectedPeerHashes=[
 [graph26,'32162fefceffa938272c9e7230206496538c5a52290083d6573f3d1faf31ff31'],
 [graph31,'eafd97355fda0739ec1135b36b247c43a6816ac754e4d154d9acf9168bae4b5d']
];
for(const [p,h] of expectedPeerHashes)if(entry(p).sha256!==h)throw Error('Frozen dependency changed: '+p);
const owners=new Map();
for(const p of [...walk(path.join(root,'manuscript/parts')),
 ...walk(path.join(root,'manuscript/appendices')),graph26,graph31,full])
 for(const l of labels(read(p)))owners.set(l,p);
const core=edits.map(e=>e.replacement).join('\n');
const refs=[...core.matchAll(/\\(?:[cC]ref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
const external=[...new Set(refs.filter(l=>!labels(core).includes(l)))].sort();
const unresolved=external.filter(l=>!owners.has(l));
if(unresolved.length)throw Error('Unknown references: '+unresolved.join(','));
if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(core))throw Error('Control character');
let patch;
try{patch=execFileSync('diff',['-u','--label','a/manuscript/parts/part3/ch25_capacity.tex',
 '--label','b/manuscript/parts/part3/ch25_capacity.tex',live,full],{encoding:'utf8'});}
catch(e){if(e.status!==1)throw e;patch=e.stdout;}
let patchCheck='not yet saved';
if(fs.existsSync(path.join(dir,'chapter.patch'))){
 if(read(path.join(dir,'chapter.patch'))!==patch)throw Error('Saved patch differs');
 execFileSync('git',['apply','--check',path.join(dir,'chapter.patch')],{cwd:root});
 patchCheck='git apply --check passed; no patch applied';
}
const sourcePaths=[live,...new Set(external.map(l=>owners.get(l)).filter(p=>p!==full)),
 path.join(root,'manuscript/parts/part3/ch21_bfj_psh.tex'),
 path.join(root,'manuscript/parts/part3/ch22_compactness.tex'),
 path.join(root,'manuscript/parts/part3/ch23_bfj_envelopes.tex'),
 path.join(root,'manuscript/parts/part3/ch24_bfj_ma.tex')];
const sources=[...new Set(sourcePaths)].map(entry);
if(fs.existsSync(path.join(dir,'SOURCE_HASHES.json'))){
 for(const e of JSON.parse(read(path.join(dir,'SOURCE_HASHES.json'))))
  if(entry(e.path).sha256!==e.sha256)throw Error('Frozen source changed: '+e.path);
}
const draftCore=read(fragment)+'\n'+edits.slice(1).map(e=>e.replacement).join('\n\n');
const stubs='% Mechanical placeholders only: not source statements or mathematical verification.\n'+
 '\\begingroup\\refstepcounter{theorem}\n'+external.map(l=>'\\label{'+l+'}').join('\n')+
 '\n\\endgroup\n';
const report={status:'mechanical checks only; not independent or production validation',
 live:entry(live),fragment:entry(fragment),full:entry(full),oldLabels:original.length,
 newLabels:proposed.length,addedLabels:proposed.filter(l=>!original.includes(l)),
 lostLabels:lost,externalReferences:external.length,
 referenceMap:external.map(label=>({label,path:owners.get(label)})),
 sources,patchCheck,assemblyEdits:edits.map(e=>e.name)};
process.stdout.write(JSON.stringify({report,patch,stubs,draftCore}));
