// Mechanical reproducibility only. No syntax/hash test proves the mathematics.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const older='../../solver_dossiers_20260831/';
const records=[];
function pin(file,expected,role){
  const bytes=read(path.resolve(own,file)),digest=sha(bytes);
  if(expected&&digest!==expected)throw Error('Input identity mismatch '+file);
  records.push({file,bytes:bytes.length,sha256:digest,role});
}
function proof(directory,expected){
  pin(directory+'/RESEARCH_NOTE.md',expected,'Complete mathematical research input, not a production verdict');
  pin(directory+'/SOURCE_LEDGER.md',null,'Source-interface record');
  pin(directory+'/MANIFEST.json',null,'Frozen input identities');
  const m=JSON.parse(read(path.resolve(own,directory,'MANIFEST.json')));
  const entries=m.entries??m.files;
  if(!Array.isArray(entries))throw Error('Unknown manifest schema');
  for(const e of entries){
    const b=read(path.resolve(own,directory,e.file??e.path));
    if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Input manifest drift');
  }
}
pin(older+'p213_skeletal_packets_20260831/skeletal_representation/statement.tex','5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','R explicit formula only; stronger separation terminology not imported');
pin(older+'p213_skeletal_packets_20260831/skeletal_representation/proof.tex','27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a','Complete original R proof; qualified reconstruction in this note');
pin(older+'p213_source_skeletal_representation_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md','3f646a1aa73096965cc71e12bcb9ce38f30e2d44d179adda5cb8492721bdcdba','Earlier independent scoped R review, not production');
pin(older+'p213_source_skeletal_representation_independent_audit_20260831/SOURCE_LEDGER.md',null,'R primary-source checks');
pin(older+'p213_source_skeletal_representation_independent_audit_20260831/MANIFEST.json','739f32df56ec5a39430548ba8c5747eed704911d0c4a871bd95a88a528b07599','Existing audit identities');
proof(older+'p213_nonreduced_tube_finite_projection_research_20260831','3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a');
proof(older+'p213_ordinary_open_outer_collar_research_20260831','f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b');
proof('../p213_proper_target_open_comparison_20260901','35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec');
proof('../p213_saturated_open_model_propagation_research_20260901','a77fe9f80d2da71d1c9c81163955808736b38508f49da76f0cf8ad8d81fdbefc');
proof('../p213_stratum_incidence_controlled_chambers_research_20260901','30d3d66a465dd51e488fa7f4b440aa2d083fc1640bd331fa61a1472acab5df34');
proof('../p213_projective_same_source_anchor_research_20260901','f6626819973ecf135a2065786a0bee3fa1847592fc061f5892da7e31a591117c');
for(const file of [
  older+'p213_nonreduced_tube_finite_projection_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md',
  '../p213_ordinary_open_outer_collar_independent_audit_20260901/INDEPENDENT_EXACT_BYTE_AUDIT.md',
  '../p213_proper_target_open_comparison_independent_audit_20260901/INDEPENDENT_EXACT_BYTE_AUDIT.md'
])pin(file,null,'Existing independently scoped review, not a theorem premise');
pin('../p213_general_propagation_fresh_audit_20260901/AUDIT.md','6326b3006803c64f4d1aa65c0efabf18f22d0cc9b1ddc369e52e6b56ef70a1b6','A/B independent final review');
pin('../p213_projective_same_source_anchor_fresh_audit_20260901/AUDIT.md','d76d7dd0dbcdc4f2a3416e72faba6d575671e008d3ad75bfd33531329fa0673c','C conditional independent final review; not a review of new extensions');
pin('../p213_displayed_representation_import_audit_20260901/AUDIT.md','b817edc9603cbd3226e87f041e3a6ca0a7c4fc91f5fa0806bf184d1dce581382','Separate exact R-import and clause-dependency review; explicitly not a review of this assembly');
pin('../p213_displayed_representation_import_audit_20260901/DEPENDENCY_GRAPH.json','8a005e4e2fc3d555db649c19809cd81b70143e7a9e1931ecca29cf78776011b0','Independently checked import graph; graph syntax alone is not proof');
pin('/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','Primary CLD source text');
pin('/private/tmp/BFJ_singular_1201.0187_audit_20260831.txt','df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f','Primary BFJ source text');
const authored=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'];
for(const file of authored){
  const b=read(path.join(own,file));
  if(!b.length||b[b.length-1]!==10)throw Error('Missing final newline');
  if([...b].some(v=>(v<32&&v!==9&&v!==10)||v===127))throw Error('Unexpected control byte');
}
const generated=['INPUT_PINS.json','VALIDATION.json','MANIFEST.json','SHA256SUMS'];
if(process.argv.includes('--freeze')){
  for(const file of generated)if(fs.existsSync(path.join(own,file)))throw Error('Refuse refreeze');
  fs.writeFileSync(path.join(own,'INPUT_PINS.json'),JSON.stringify({date:'2026-09-01',files:records},null,2)+'\n',{flag:'wx'});
  fs.writeFileSync(path.join(own,'VALIDATION.json'),JSON.stringify({date:'2026-09-01',inputPins:records.length,controlByteErrors:0,mathematicalVerdict:'Not supplied by this script',independentStatus:'Exact new assembly and extensions pending separate review',productionStatus:'Not verified',liveChanges:false,atomRetirements:0},null,2)+'\n',{flag:'wx'});
  const entries=[...authored,'INPUT_PINS.json','VALIDATION.json'].map(file=>{const b=read(path.join(own,file));return{file,bytes:b.length,sha256:sha(b)};}).concat(records);
  const mf=JSON.stringify({date:'2026-09-01',status:'Frozen qualified scalar assembly and local analytic extension candidate; independent exact-final and production gates unmet',entries},null,2)+'\n';
  fs.writeFileSync(path.join(own,'MANIFEST.json'),mf,{flag:'wx'});
  fs.writeFileSync(path.join(own,'SHA256SUMS'),entries.map(e=>e.sha256+'  '+e.file).concat(sha(mf)+'  MANIFEST.json').join('\n')+'\n',{flag:'wx'});
}
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(own,'MANIFEST.json'))){
  const entries=JSON.parse(read(path.join(own,'MANIFEST.json'))).entries;
  for(const e of entries){const b=read(path.resolve(own,e.file));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Self manifest mismatch');manifestEntries++;}
  for(const line of read(path.join(own,'SHA256SUMS')).toString().trimEnd().split('\n')){const m=line.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(read(path.resolve(own,m[2])))!==m[1])throw Error('Self checksum mismatch');checksumEntries++;}
}
console.log(JSON.stringify({inputPins:records.length,manifestEntries,checksumEntries,allExact:true,noteSha256:sha(read(path.join(own,'RESEARCH_NOTE.md'))),ledgerSha256:sha(read(path.join(own,'SOURCE_LEDGER.md'))),manifestSha256:manifestEntries?sha(read(path.join(own,'MANIFEST.json'))):null,checksumSha256:checksumEntries?sha(read(path.join(own,'SHA256SUMS'))):null,meaning:'Identity only, not mathematical or production acceptance'},null,2));
