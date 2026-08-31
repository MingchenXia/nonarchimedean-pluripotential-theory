import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const directory=path.dirname(fileURLToPath(import.meta.url));
const frozen='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831';
const candidate=path.join(frozen,'skeletal_representation');
function snapshot(file){const b=fs.readFileSync(file);return{path:file,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
const notePath=path.join(frozen,'FROZEN_PAUSED.md');
const frozenNote=fs.readFileSync(notePath,'utf8');
const frozenPins=[...frozenNote.matchAll(/^([a-f0-9]{64})  (\S+)$/gm)].map(m=>{
 const actual=snapshot(path.join(frozen,m[2]));
 return {...actual,expected:m[1],matches:actual.sha256===m[1],mathematicalAuditScope:m[2].startsWith('skeletal_representation/')};
});
const primaryPins=[
 ['/private/tmp/CLD25.pdf','5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719'],
 ['/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e']
].map(([p,expected])=>{const actual=snapshot(p);return{...actual,expected,matches:actual.sha256===expected};});
const additionalInputs=[notePath,path.join(candidate,'sources.bib'),path.join(candidate,'compile_check.tex')].map(snapshot);
const raw=['statement.tex','proof.tex'].map(n=>fs.readFileSync(path.join(candidate,n),'utf8')).join('\n');
const tex=raw.replace(/(?<!\\)%.*$/gm,'');
const labels=[...tex.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...tex.matchAll(/\\(?:eqref|cref|Cref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(s=>s.trim()));
const cites=[...tex.matchAll(/\\[A-Za-z]*cite[A-Za-z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(s=>s.trim()));
const bib=fs.readFileSync(path.join(candidate,'sources.bib'),'utf8');
const keys=[...bib.matchAll(/@\w+\s*\{\s*([^,\s]+)\s*,/g)].map(m=>m[1]);
const stack=[],environmentErrors=[];
for(const m of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)){
 if(m[1]==='begin')stack.push(m[2]);else{const opened=stack.pop();if(opened!==m[2])environmentErrors.push({opened,closed:m[2],offset:m.index});}
}
let balance=0,minimum=0;
for(const m of tex.matchAll(/(?<!\\)[{}]/g)){balance+=m[0]==='{'?1:-1;minimum=Math.min(minimum,balance);}
const structural={
 labelCount:labels.length,labels,referenceCount:refs.length,
 duplicateLabels:labels.filter((s,i)=>labels.indexOf(s)!==i),
 missingReferences:[...new Set(refs.filter(s=>!labels.includes(s)))],
 citationKeys:[...new Set(cites)],missingCitations:[...new Set(cites.filter(s=>!keys.includes(s)))],
 braceBalance:balance,minimumBraceBalance:minimum,environmentErrors,unclosedEnvironments:stack,
 prohibitedControlCharacters:[...raw.matchAll(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g)].map(m=>m.index)
};
let auditManifestCheck=null;
if(fs.existsSync(path.join(directory,'MANIFEST.json'))){
 const manifest=JSON.parse(fs.readFileSync(path.join(directory,'MANIFEST.json'),'utf8'));
 const mismatches=manifest.entries.map(e=>({expected:e,actual:snapshot(e.path)}))
 .filter(e=>e.expected.bytes!==e.actual.bytes||e.expected.sha256!==e.actual.sha256);
 auditManifestCheck={entryCount:manifest.entries.length,mismatches};
}
const defectCount=frozenPins.filter(e=>!e.matches).length+primaryPins.filter(e=>!e.matches).length
 +structural.duplicateLabels.length+structural.missingReferences.length+structural.missingCitations.length
 +Math.abs(balance)+Math.abs(minimum)+environmentErrors.length+stack.length
 +structural.prohibitedControlCharacters.length+(auditManifestCheck?.mismatches.length??0);
console.log(JSON.stringify({
 schema:'fresh-source-skeletal-audit-check-v1',date:'2026-08-31',directory,candidate,
 principalFrozenRecord:notePath,
 note:'No completed author manifest is present in the source packet; FROZEN_PAUSED.md contains five exact hash records. The three cross/remaining-gap files are identity checks only.',
 frozenPins,primaryPins,additionalInputs,structural,auditManifestCheck,defectCount,
 operations:{candidateEdits:false,priorAuditEdits:false,liveEdits:false,texCompile:false,pdfCreation:false,git:false,production:false},
 limitation:'Hashes and structural checks do not constitute the mathematical verdict.'
},null,2));
process.exitCode=defectCount?1:0;

