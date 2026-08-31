import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const directory = path.dirname(fileURLToPath(import.meta.url));
const prior = path.resolve(directory, '../p213_product_current_separation_research_20260831');
const pins = [
  ['/private/tmp/CLD25.pdf', '5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719'],
  ['/private/tmp/CLD25.txt', '021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e'],
  [path.join(prior, 'RESEARCH_NOTE.md'), 'd4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81'],
  [path.join(prior, 'SOURCE_LEDGER.md'), '568f7a92f88e18821d3698c8fd35499440f3bcffc106dfb3fffc32f19b8de578'],
  [path.join(prior, 'MANIFEST.json'), '2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440']
];
function snapshot(file) {
  const b = fs.readFileSync(file);
  return { path: file, bytes: b.length, sha256: crypto.createHash('sha256').update(b).digest('hex') };
}
const inputs = pins.map(([file, expected]) => {
  const actual = snapshot(file);
  return { ...actual, matches: actual.sha256 === expected };
});
const priorManifest = JSON.parse(fs.readFileSync(path.join(prior, 'MANIFEST.json'), 'utf8'));
const priorEntries = priorManifest.entries.map(e => {
  const actual = snapshot(path.resolve(prior, e.path));
  return { ...actual, matches: actual.sha256 === e.sha256 };
});
const raw = ['statement.tex','proof.tex'].map(n => fs.readFileSync(path.join(directory,n),'utf8')).join('\n');
const tex = raw.replace(/(?<!\\)%.*$/gm,'');
const labels = [...tex.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs = [...tex.matchAll(/\\(?:eqref|cref|Cref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(s=>s.trim()));
const cites = [...tex.matchAll(/\\[A-Za-z]*cite[A-Za-z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(s=>s.trim()));
const bib = fs.readFileSync(path.join(directory,'sources.bib'),'utf8');
const bibkeys = [...bib.matchAll(/@\w+\s*\{\s*([^,\s]+)\s*,/g)].map(m=>m[1]);
const stack=[], environmentErrors=[];
for (const m of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)) {
  if (m[1]==='begin') stack.push(m[2]);
  else { const opened=stack.pop(); if(opened!==m[2]) environmentErrors.push({opened,closed:m[2],offset:m.index}); }
}
let balance=0,minimum=0;
for(const m of tex.matchAll(/(?<!\\)[{}]/g)){balance+=m[0]==='{'?1:-1;minimum=Math.min(minimum,balance);}
const finalLog=fs.readFileSync(path.join(directory,'build/main.log'),'utf8');
const structural={
 labelCount:labels.length,labels,referenceCount:refs.length,
 duplicateLabels:labels.filter((x,i)=>labels.indexOf(x)!==i),
 missingReferences:[...new Set(refs.filter(x=>!labels.includes(x)))],
 citationKeys:[...new Set(cites)],missingCitations:[...new Set(cites.filter(x=>!bibkeys.includes(x)))],
 environmentErrors,unclosedEnvironments:stack,braceBalance:balance,minimumBraceBalance:minimum,
 prohibitedControlCharacters:[...raw.matchAll(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g)].map(m=>m.index)
};
const build={
 mode:'pdflatex -draftmode; no PDF',
 finalWarnings:finalLog.split('\n').filter(s=>/Warning:|Overfull|Underfull|^!|Undefined control sequence/.test(s)),
 expectedDraftNotice:finalLog.includes('pdfdraftmode enabled'),
 pdfExists:fs.existsSync(path.join(directory,'build/main.pdf'))||fs.existsSync(path.join(directory,'main.pdf'))
};
let frozenManifestCheck=null;
const manifestPath=path.join(directory,'MANIFEST.json');
if(fs.existsSync(manifestPath)){
 const manifest=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
 const results=manifest.entries.map(e=>{
   const actual=snapshot(e.path);
   return {path:e.path,matches:actual.bytes===e.bytes&&actual.sha256===e.sha256};
 });
 frozenManifestCheck={entryCount:results.length,mismatches:results.filter(e=>!e.matches)};
}
const defects=inputs.filter(x=>!x.matches).length+priorEntries.filter(x=>!x.matches).length
 +structural.duplicateLabels.length+structural.missingReferences.length+structural.missingCitations.length
 +environmentErrors.length+stack.length+Math.abs(balance)+Math.abs(minimum)
 +structural.prohibitedControlCharacters.length+build.finalWarnings.length+Number(build.pdfExists)
 +(frozenManifestCheck?.mismatches.length??0);
console.log(JSON.stringify({
 schema:'bounded-mixed-branch-validation-v1',date:'2026-08-31',directory,
 status:'author checks only; independent and production review pending',
 inputs,priorManifestEntryCount:priorEntries.length,priorEntries,structural,build,frozenManifestCheck,defectCount:defects,
 scope:'Two coefficients on the explicit q=w-t branch, over F throughout; no all-current separation.',
 operations:{liveEdits:false,frozenParentEdits:false,currentBaseChange:false,slicing:false,git:false,production:false,pdf:false},
},null,2));
process.exitCode=defects?1:0;

