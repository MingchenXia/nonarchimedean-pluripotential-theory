import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const dossiers=path.dirname(here), manuscript='/private/tmp/nappt_p071_20260827/manuscript';
const target=process.argv[2];
if(!target||!/^\/private\/tmp\/nappt_weighted_syntax_20260831\.[A-Za-z0-9]+$/.test(target))throw Error('Provide a newly created task-specific mktemp directory');
if(fs.readdirSync(target).length)throw Error('Scratch directory must be empty');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const overlays=[
 ['ch20_model_forms.tex','p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch20_model_forms.tex','bc479b67a29261f001d0409656e150bc3bf9441dbdf1ff90fb4298fe3c1ad414'],
 ['ch22_compactness.tex','p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch22_compactness.tex','0acc3463796d93d0fd56c5f8f2fbc2d1de75f9c8c46607a5fddc0d91844bcc0a'],
 ['ch23_bfj_envelopes.tex','p081_ch23_curve_consumer_repair_20260831/revised1/patched/ch23_bfj_envelopes.tex','cb9d7c65bdf64b2b52c32483877f13a143b59d07615fc6d5f9ff3ced0d0e2e06'],
 ['ch24_bfj_ma.tex','p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch24_bfj_ma.tex','391930d26a49779b10a96ac7e381fefade0677642669e7a20e93c7902e660eae'],
 ['ch26_energy.tex','p081_weighted_energy_consumers_repair_20260831/patched/ch26_energy.tex','8552d7b5e4c5c58cf48e94db28bf44f3286af4f997adf3f4716cee52d8f26d28'],
 ['ch28_finite_energy_measures.tex','p081_ch28_curve_uniqueness_snc_repair_20260831/patched/ch28_finite_energy_measures.tex','8c27a6812bf18c9a664a74494ecbcc0ccf7fa10c6f0b2e6f949d691cc8e56106'],
 ['ch29_continuity.tex','p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/patched/ch29_continuity.tex','d0fdf6a4412bb7bc93ce8f3b40a0accc49d646d1592e5c9bb7d742edf75eba8f'],
 ['ch31_bfj_examples.tex','p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/patched/ch31_bfj_examples.tex','0fd8e79cd263002c551618dedbcabb43287f4b579fe4f8bcfbb91d90dda13d59']
];
const copied=new Set(), inputs=[], missingLiteralInputs=[];
function copy(rel,scan=true){
 if(copied.has(rel))return;
 const source=path.join(manuscript,rel);
 if(!source.startsWith(manuscript+'/'))throw Error('Invalid source path');
 if(!fs.existsSync(source)){missingLiteralInputs.push(rel);return;}
 const dest=path.join(target,rel);fs.mkdirSync(path.dirname(dest),{recursive:true});
 fs.copyFileSync(source,dest);copied.add(rel);inputs.push(record(source));
 if(scan&&rel.endsWith('.tex'))scanInputs(fs.readFileSync(source,'utf8'));
}
function scanInputs(text){
 for(const m of text.matchAll(/\\(?:input|include|draftinclude)\{([^}]+)\}/g)){
  const rel=m[1];if(rel.includes('#')||rel.includes('\\'))continue;
  copy(path.extname(rel)?rel:rel+'.tex');
 }
}
function tree(rel){
 const full=path.join(manuscript,rel);if(!fs.existsSync(full))return;
 for(const e of fs.readdirSync(full,{withFileTypes:true})){
  const name=path.join(rel,e.name);
  if(e.isDirectory())tree(name);
  else if(/\.(?:tex|bib|cls|sty|bst|ist|png|jpg|jpeg|pdf|eps)$/.test(e.name))copy(name);
 }
}
copy('book.tex');copy('book.bbl',false);
for(const root of ['style','bibliography','figures'])tree(root);
const overlayRecords=[];
for(const [name,rel,hash] of overlays){
 const source=path.join(dossiers,rel),r=record(source);
 if(r.sha256!==hash)throw Error('Frozen overlay mismatch: '+rel);
 const dest=path.join(target,'parts/part3',name);fs.copyFileSync(source,dest);
 scanInputs(fs.readFileSync(source,'utf8'));overlayRecords.push({destination:dest,...r});
}
fs.copyFileSync(path.join(here,'GATE.md'),path.join(target,'REVIEW_STATUS.md'));
const result={date:'2026-08-31',status:'isolated draft-mode syntax review; no mathematical acceptance',scratchDirectory:target,inputs,overlays:overlayRecords,missingLiteralInputs};
fs.writeFileSync(path.join(here,'ASSEMBLY.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({scratchDirectory:target,copiedSourceFiles:copied.size,overlaidChapters:overlays.length,missingLiteralInputs},null,2));
