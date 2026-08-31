// Read-only verification. Does not run either author freeze/build script.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import path from 'node:path';

const packet = '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831';
const digest = data => createHash('sha256').update(data).digest('hex');
const read = name => readFileSync(path.join(packet, name));
const assert = (test, msg) => { if (!test) throw new Error(msg); };
const expected = {
  'statement.tex': '488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949',
  'proof.tex': 'bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21',
  'example.tex': '7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f',
  'MANIFEST.json': 'c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87'
};
for (const [name, hash] of Object.entries(expected)) assert(digest(read(name)) === hash, `Frozen hash mismatch: ${name}`);
const manifest = JSON.parse(read('MANIFEST.json'));
assert(manifest.files.length === 20, 'Expected 20 frozen entries');
for (const entry of manifest.files) {
  assert(entry.path === path.join(packet, entry.name), `Unexpected entry path: ${entry.name}`);
  const bytes = readFileSync(entry.path);
  assert(bytes.length === entry.bytes && digest(bytes) === entry.sha256, `Manifest mismatch: ${entry.name}`);
}
const parents = JSON.parse(read('PARENT_INPUTS.json'));
for (const entry of parents) {
  const bytes = readFileSync(entry.path);
  assert(bytes.length === entry.bytes && digest(bytes) === entry.sha256, `Historical parent input has changed: ${entry.path}`);
}
const external = JSON.parse(read('EXTERNAL_REFERENCES.json'));
for (const entry of external.sources) {
  const bytes = readFileSync(entry.path);
  assert(bytes.length === entry.bytes && digest(bytes) === entry.sha256, `Historical external aux has changed: ${entry.path}`);
}
const text = ['statement.tex', 'proof.tex', 'example.tex'].map(name => read(name).toString('utf8')).join('\n');
for (const entry of manifest.files.filter(x => x.name.endsWith('.tex'))) {
  const contents = read(entry.name).toString('utf8');
  assert(!/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/.test(contents), `Control byte: ${entry.name}`);
}
const labels = [...text.matchAll(/\\label\{([^}]+)\}/g)].map(m => m[1]);
assert(labels.length === new Set(labels).size, 'Duplicate candidate label');
assert(labels.length === 14, 'Expected 14 internal labels');
const resolved = new Set([...labels, ...external.labels]);
for (const match of text.matchAll(/\\(?:[cC]ref|[eE]qref|ref)\{([^}]+)\}/g)) {
  for (const label of match[1].split(',').map(x => x.trim())) assert(resolved.has(label), `Unresolved label: ${label}`);
}
const aux = read('external_refs.aux').toString('utf8');
for (const label of external.labels) {
  assert(aux.includes(`\\newlabel{${label}}`) && aux.includes(`\\newlabel{${label}@cref}`), `Missing exact external record: ${label}`);
}
const sourceLines = new Set(external.sources.flatMap(entry => readFileSync(entry.path, 'utf8').split(/\r?\n/)));
for (const line of aux.split(/\r?\n/).filter(x => x.startsWith('\\newlabel'))) assert(sourceLines.has(line), 'External label extraction differs from source aux');
const bbl = read('compile.bbl').toString('utf8');
const bibliographyKeys = new Set([...bbl.matchAll(/\\bibitem\{([^}]+)\}/g)].map(x => x[1]));
for (const match of text.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)) {
  for (const key of match[1].split(',').map(x => x.trim())) assert(bibliographyKeys.has(key), `Unresolved citation: ${key}`);
}
const build = JSON.parse(read('BUILD.json'));
assert(build.exitCode === 0 && build.pdfProduced === false && build.warnings.length === 0, 'Unexpected recorded draft build outcome');
assert(digest(readFileSync(build.log.path)) === build.log.sha256, 'Build log hash mismatch');
const log = readFileSync(build.log.path, 'utf8');
assert(!/(?:LaTeX|Package .*?) Warning:|^!|Undefined control sequence|Overfull \\[hv]box/m.test(log), 'Unexpected final draft diagnostic');
console.log(JSON.stringify({result:'PASS', frozenEntries:manifest.files.length, parentInputs:parents.length, sourceAuxFiles:external.sources.length, internalLabels:labels.length, importedLabels:external.labels.length, bibliographyKeys:[...bibliographyKeys], controlBytes:0, build:'recorded draft-only, no PDF; no independent build or visual claim'}, null, 2));
