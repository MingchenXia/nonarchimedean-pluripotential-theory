import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

// Read-only exact-byte and structural checks; no mathematical verdict is inferred.
const candidate = '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_annular_torsor_residual_functional_research_20260831';
const pins = {
  'statement.tex': '19baf4828b51e2b36370a2ececd41ad5802f01e3cf41c90f00df9b8bacec773a',
  'proof.tex': 'f851830312841ef4d8825ba4b049a718a16820ef3888263721278bf7a06c99fe',
  'CURVATURE_AND_EXAMPLES.md': 'b88523c7d72f143f2093d3803d6b64886ac7d8ff0d872a4f30678df41a543c0a',
  'MANIFEST.json': 'ec7f22f0fd750a325139c2f7403e213b53e921b5f1f89e5ab45ac6e0f059da30'
};
function snapshot(file) {
  const data = fs.readFileSync(file);
  return { path: file, bytes: data.length, sha256: crypto.createHash('sha256').update(data).digest('hex') };
}
const manifest = JSON.parse(fs.readFileSync(path.join(candidate, 'MANIFEST.json'), 'utf8'));
const entries = manifest.entries.map(expected => {
  const actual = snapshot(expected.path);
  return { ...actual, role: expected.role, matches: actual.bytes === expected.bytes && actual.sha256 === expected.sha256 };
});
const pinned = Object.entries(pins).map(([name, expected]) => {
  const actual = snapshot(path.join(candidate, name));
  return { ...actual, matches: actual.sha256 === expected };
});
const files = ['statement.tex', 'proof.tex'];
const raw = files.map(name => fs.readFileSync(path.join(candidate, name), 'utf8')).join('\n');
const tex = raw.replace(/(?<!\\)%.*$/gm, '');
const labels = [...tex.matchAll(/\\label\{([^}]+)\}/g)].map(m => m[1]);
const references = [...tex.matchAll(/\\(?:eqref|cref|Cref|ref)\{([^}]+)\}/g)].flatMap(m => m[1].split(',').map(s => s.trim()));
const citations = [...tex.matchAll(/\\[A-Za-z]*cite[A-Za-z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}/g)].flatMap(m => m[1].split(',').map(s => s.trim()));
const bib = fs.readFileSync(path.join(candidate, 'sources.bib'), 'utf8');
const bibkeys = [...bib.matchAll(/@\w+\s*\{\s*([^,\s]+)\s*,/g)].map(m => m[1]);
const duplicates = labels.filter((name, i) => labels.indexOf(name) !== i);
const environmentStack = [];
const environmentErrors = [];
for (const match of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)) {
  if (match[1] === 'begin') environmentStack.push(match[2]);
  else {
    const opened = environmentStack.pop();
    if (opened !== match[2]) environmentErrors.push({ expected: opened, actual: match[2], offset: match.index });
  }
}
let braces = 0;
let minimumBraces = 0;
for (const match of tex.matchAll(/(?<!\\)[{}]/g)) {
  braces += match[0] === '{' ? 1 : -1;
  minimumBraces = Math.min(minimumBraces, braces);
}
const structural = {
  labelCount: labels.length, labels, referenceCount: references.length,
  duplicateLabels: [...new Set(duplicates)],
  missingReferences: [...new Set(references.filter(x => !labels.includes(x)))],
  citationKeys: [...new Set(citations)], bibliographyKeys: bibkeys,
  missingCitations: [...new Set(citations.filter(x => !bibkeys.includes(x)))],
  unclosedEnvironments: environmentStack, environmentErrors,
  braceBalance: braces, minimumBraceBalance: minimumBraces,
  prohibitedControlCharacters: [...raw.matchAll(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g)].map(m => m.index)
};
const failures = entries.filter(x => !x.matches).length + pinned.filter(x => !x.matches).length
  + structural.duplicateLabels.length + structural.missingReferences.length
  + structural.missingCitations.length + structural.unclosedEnvironments.length
  + structural.environmentErrors.length + Math.abs(braces) + Math.abs(minimumBraces)
  + structural.prohibitedControlCharacters.length;
console.log(JSON.stringify({
  schema: 'independent-read-only-torsor-check-v1', date: '2026-08-31', candidate,
  pinned, manifestEntryCount: entries.length, manifestEntries: entries,
  structural, failureCount: failures,
  operations: { candidateWrites: false, sourceWrites: false, texCompile: false, pdfInspection: false, git: false, production: false },
  limitation: 'Structural and checksum success is not a mathematical or production verdict.'
}, null, 2));
process.exitCode = failures ? 1 : 0;
