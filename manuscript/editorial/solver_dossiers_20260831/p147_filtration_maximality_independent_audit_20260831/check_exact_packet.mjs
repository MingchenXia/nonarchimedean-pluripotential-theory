// Independent read-only exact-byte and assembly check; no builds or writes.
import {readFileSync, existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import path from 'node:path';

const packet = '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p147_filtration_maximality_research_20260831';
const digest = b => createHash('sha256').update(b).digest('hex');
const read = name => readFileSync(path.join(packet, name));
const assert = (ok, message) => {if (!ok) throw new Error(message);};
const principal = {
  'MANIFEST.json': '3ffa1f46f96ce438bf46dd0159cd036f10e79437c1b242a688359b53d652b7fb',
  'statement.tex': 'd6fca037467563e9af28d2ca97917eb1d2f5697c0b36d36f6a6217439bdd444c',
  'proof.tex': '865717efa134e64f113ccf3b57a339b657059bc2b0ee7368ee5b70dd9872a362',
  'diagnostics.tex': '969a55ac2a16374b3131d381d2b2d122f6d720dd4cc2ec7f85b8ed3c32883b8a'
};
for (const [name, hash] of Object.entries(principal)) assert(digest(read(name)) === hash, `Frozen hash differs: ${name}`);
const manifest = JSON.parse(read('MANIFEST.json'));
assert(manifest.files.length === 12, 'Expected 12 frozen manifest entries');
for (const entry of manifest.files) {
  assert(!path.isAbsolute(entry.path) && !entry.path.includes('..'), 'Unexpected manifest path');
  const bytes = read(entry.path);
  assert(bytes.length === entry.bytes && digest(bytes) === entry.sha256, `Manifest differs: ${entry.path}`);
}
const inputs = JSON.parse(read('INPUTS.json')).inputs;
assert(inputs.length === 6, 'Expected six recorded inputs');
for (const entry of inputs) assert(digest(readFileSync(entry.path)) === entry.sha256, `Historical input drift: ${entry.path}`);
const texNames = manifest.files.filter(x => x.path.endsWith('.tex')).map(x => x.path);
for (const name of texNames) assert(!/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/.test(read(name).toString('utf8')), `Control byte: ${name}`);
const text = ['statement.tex', 'proof.tex', 'diagnostics.tex'].map(name => read(name).toString('utf8')).join('\n');
const labels = [...text.matchAll(/\\label\{([^}]+)\}/g)].map(x => x[1]);
assert(labels.length === 19 && labels.length === new Set(labels).size, 'Unexpected or duplicate labels');
const refs = [...text.matchAll(/\\(?:eqref|ref|[cC]ref)\{([^}]+)\}/g)].map(x => x[1]);
assert(refs.length === 12, 'Expected 12 internal references');
for (const ref of refs) for (const label of ref.split(',').map(x => x.trim())) assert(labels.includes(label), `Unresolved label: ${label}`);
const bib = read('sources.bib').toString('utf8');
const keys = new Set([...bib.matchAll(/@\w+\s*\{\s*([^,\s]+)\s*,/g)].map(x => x[1]));
for (const match of text.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)) for (const key of match[1].split(',').map(x => x.trim())) assert(keys.has(key), `Unresolved citation: ${key}`);
const checks = JSON.parse(read('checks.json'));
assert(checks.hasPDF === false && checks.finalDraftLogWarnings.length === 0, 'Unexpected recorded syntax status');
const logPath = path.join(checks.draftDirectory, 'main.log');
const bblPath = path.join(checks.draftDirectory, 'main.bbl');
assert(digest(readFileSync(logPath)) === '8c6ea7f2ef8214d1a27861a4eee60c232b6e231feff5263aea8be0a44ef24a3e', 'Historical draft log drift');
assert(digest(readFileSync(bblPath)) === 'e020ba3eca838e6017161d53f7162dda299d3ab964763af2c8fa6f949a7d547e', 'Historical bibliography drift');
assert(!existsSync(path.join(checks.draftDirectory, 'main.pdf')), 'Unexpected candidate PDF');
const log = readFileSync(logPath, 'utf8');
assert(!/(?:LaTeX|Package .*?) Warning:|^!|Undefined control sequence|(?:Overfull|Underfull) \\[hv]box/m.test(log), 'Unexpected substantive syntax diagnostic');
assert(log.includes('pdfdraftmode enabled'), 'Expected explicit draftmode diagnostic');
let monomialChecks = 0;
for (let d=1; d<=7; d++) for (let m=1; m<=12; m++) {
  const degree = d*m;
  for (let ell=0; ell<=degree+2; ell++) {
    let actual = 0;
    for (let a=0; a<=degree; a++) for (let b=0; b<=degree-a; b++) if (a+b>=ell) actual++;
    const expected = ell>degree ? 0 : (degree+1)*(degree+2)/2-ell*(ell+1)/2;
    assert(actual===expected, `Blowup count mismatch: d=${d}, m=${m}, ell=${ell}`);
    monomialChecks++;
  }
}
assert(monomialChecks===2436, 'Unexpected arithmetic test count');
console.log(JSON.stringify({result:'PASS', manifestEntries:12, principalHashes:4, parentInputs:6, labels:19, references:12, bibliographyKeys:keys.size, forbiddenControlBytes:0, independentMonomialChecks:monomialChecks, draftLog:'read and hash-checked; no independent build and no PDF/visual claim'}, null, 2));
