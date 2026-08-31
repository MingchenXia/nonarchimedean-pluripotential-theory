// Mechanical exact-byte freeze/check. Authored math is never rewritten.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const parent = path.dirname(here);
const pins = [
  ['/private/tmp/CLD25.pdf', '5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719', 'primary PDF'],
  ['/private/tmp/CLD25.txt', '021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e', 'primary extracted text'],
  [path.join(parent, 'p213_skeletal_packets_20260831/skeletal_representation/statement.tex'), '5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a', 'conditional R statement'],
  [path.join(parent, 'p213_skeletal_packets_20260831/skeletal_representation/proof.tex'), '27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a', 'conditional R proof; no production acceptance imported'],
  [path.join(parent, 'p213_general_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md'), '1c8011863516d8bdc900b3432b270c923126ee36d6600d915f714dc016553ae7', 'prior reduced-model scope; motivation only'],
];
const entries = pins.map(([file, expected, role]) => {
  const bytes = fs.readFileSync(file);
  if (sha(bytes) !== expected) throw Error('Input pin changed: ' + file);
  return {path: file, bytes: bytes.length, sha256: expected, role};
});
for (const name of ['RESEARCH_NOTE.md', 'SOURCE_LEDGER.md', 'freeze.mjs']) {
  const file = path.join(here, name);
  const bytes = fs.readFileSync(file);
  if (/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(bytes.toString('utf8'))) {
    throw Error('Unexpected control character: ' + file);
  }
  entries.push({path: file, bytes: bytes.length, sha256: sha(bytes), role: 'new authored output'});
}
const manifestPath = path.join(here, 'MANIFEST.json');
const sumsPath = path.join(here, 'SHA256SUMS');
if (fs.existsSync(manifestPath)) {
  if (process.argv.includes('--freeze')) throw Error('Already frozen');
  const record = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  for (const entry of record.entries) {
    const bytes = fs.readFileSync(entry.path);
    if (bytes.length !== entry.bytes || sha(bytes) !== entry.sha256) throw Error('Manifest mismatch');
  }
  let sums = 0;
  for (const line of fs.readFileSync(sumsPath, 'utf8').trim().split('\n')) {
    const match = line.match(/^([a-f0-9]{64})  (.+)$/);
    if (!match || sha(fs.readFileSync(match[2])) !== match[1]) throw Error('Checksum mismatch');
    sums++;
  }
  console.log(JSON.stringify({frozenCheck: true, entries: record.entries.length, sums, manifestSha256: sha(fs.readFileSync(manifestPath))}));
  process.exit(0);
}
if (!process.argv.includes('--freeze')) {
  console.log(JSON.stringify({preflight: true, entries}));
  process.exit(0);
}
if (fs.existsSync(sumsPath)) throw Error('Unexpected existing checksum file');
const record = {
  date: '2026-08-31',
  author: '/root',
  packet: path.basename(here),
  status: 'Frozen bounded research candidate; fresh independent and production verification pending',
  scope: 'Finite-flat multiplicity tube calculation; positive closed-current pushforward; unique generic Gauss source under unramified DVR assumptions; individual source-cell comparison conditional on R',
  exclusions: ['No global nonreduced SNC divisor functional', 'No arbitrary-W locality theorem', 'No arbitrary analytic wall realization', 'No current pullback through finite maps or base extension', 'No full P21.3 or priority claim'],
  entries,
};
const bytes = JSON.stringify(record, null, 2) + '\n';
fs.writeFileSync(manifestPath, bytes, {flag: 'wx'});
const sums = entries.map(entry => entry.sha256 + '  ' + entry.path)
  .concat(sha(bytes) + '  ' + manifestPath).join('\n') + '\n';
fs.writeFileSync(sumsPath, sums, {flag: 'wx'});
console.log(JSON.stringify({frozen: true, entries: entries.length, sums: entries.length + 1, noteSha256: entries.find(entry => entry.path.endsWith('/RESEARCH_NOTE.md') && path.dirname(entry.path) === here).sha256, manifestSha256: sha(bytes), sumsSha256: sha(sums)}));
