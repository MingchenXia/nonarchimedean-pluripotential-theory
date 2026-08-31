// Read-only by default. --copy preserves only these explicitly pinned dossiers.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const sourceRoot = '/private/tmp/nappt_p071_20260827';
const durableRoot = '/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix = 'manuscript/editorial/solver_dossiers_20260831';
const here = path.dirname(fileURLToPath(import.meta.url));
const own = path.join(prefix, 'chapter72_cld_geometry_preservation_20260831');
if (![sourceRoot, durableRoot].some(root => path.join(root, own) === here)) {
  throw Error('Unexpected script location');
}
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const manifests = new Map([
  ['p213_annular_torsor_residual_functional_research_20260831', 'ec7f22f0fd750a325139c2f7403e213b53e921b5f1f89e5ab45ac6e0f059da30'],
  ['p213_annular_torsor_residual_functional_independent_audit_20260831', '697830cc3fe77808345532b9da4a2cc228a86134ecff55d8fb4d3f97be609ddc'],
  ['p213_annular_torsor_draftcheck_20260831', '803b975d3eb0cf2624aeb342a4f9a74b7c03dd7dbe13ef30b187be7ae9b1beb5'],
  ['p213_annular_torsor_draftcheck_v2_20260831', '6a3671d8a1cd3d70b97728558a48ed039eb840badfa01a04bb5287fdc65b1568'],
  ['p213_product_current_separation_research_20260831', '2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440'],
  ['p213_product_common_moment_supplement_20260831', 'daf71d19d289cceacb0ce18f974f7acdaeec7484c8618cc291b40c2da9eb5491'],
  ['p213_product_current_separation_independent_audit_20260831', '5253dcb538c575903769823cccd14fa3f0a63786faf601074f926431a76e8f9e'],
  ['p213_mixed_branch_transport_research_20260831', '7f702a642668d1e33b4c78b5b21814fb930fd86e9acbf1e9bc2cb988d29ee890'],
  ['p213_mixed_branch_transport_independent_audit_20260831', '74e8a45c59b7e718daf6bc70c8868c4df08d896c48963b88fc0b2b993e49c2f7'],
]);
const checkedManifests = [];
for (const [name, expected] of manifests) {
  const dir = path.join(sourceRoot, prefix, name);
  const bytes = fs.readFileSync(path.join(dir, 'MANIFEST.json'));
  if (sha(bytes) !== expected) throw Error('Changed manifest pin: ' + name);
  const record = JSON.parse(bytes);
  for (const entry of record.entries) {
    const data = fs.readFileSync(path.resolve(dir, entry.path));
    if (sha(data) !== entry.sha256 || (entry.bytes !== undefined && data.length !== entry.bytes)) {
      throw Error('Changed manifest entry: ' + entry.path);
    }
  }
  checkedManifests.push({directory: name, sha256: expected, entries: record.entries.length});
}

function walk(relative) {
  return fs.readdirSync(path.join(sourceRoot, relative), {withFileTypes: true})
    .sort((a, b) => a.name.localeCompare(b.name)).flatMap(entry => {
      if (entry.isSymbolicLink()) throw Error('Unexpected symlink');
      const next = path.join(relative, entry.name);
      if (entry.isDirectory()) return walk(next);
      if (!entry.isFile()) throw Error('Unexpected non-file: ' + next);
      return entry.name === '.DS_Store' ? [] : [next];
    });
}
const directories = [...manifests.keys()];
const paths = directories.flatMap(name => walk(path.join(prefix, name)));
paths.push('manuscript/editorial/chapter72_cld_geometry_followup_checkpoint_20260831.md', path.join(own, 'preserve.mjs'));
if (new Set(paths).size !== paths.length) throw Error('Duplicate selected path');
const files = paths.map(relative => {
  if (path.isAbsolute(relative) || relative.split(path.sep).includes('..')) throw Error('Unsafe path');
  const source = path.join(sourceRoot, relative);
  const target = path.join(durableRoot, relative);
  const bytes = fs.readFileSync(source);
  const hash = sha(bytes);
  const present = fs.existsSync(target);
  if (present && sha(fs.readFileSync(target)) !== hash) throw Error('Refuse different durable bytes: ' + relative);
  if (/(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(bytes.toString('utf8'))) {
    throw Error('Credential-like string; inspect privately: ' + relative);
  }
  return {relative, bytes: bytes.length, sha256: hash, alreadyPresent: present};
});
const summary = {
  directories: directories.length,
  manifestEntries: checkedManifests.reduce((sum, item) => sum + item.entries, 0),
  files: files.length,
  newFiles: files.filter(item => !item.alreadyPresent).length,
  bytes: files.reduce((sum, item) => sum + item.bytes, 0),
};
if (!process.argv.includes('--copy')) {
  console.log(JSON.stringify({preflight: true, ...summary}, null, 2));
  process.exit(0);
}

for (const root of [sourceRoot, durableRoot]) {
  for (const name of ['PRESERVATION.json', 'COMMIT_PATHS.nul']) {
    if (fs.existsSync(path.join(root, own, name))) throw Error('Already preserved');
  }
}
for (const entry of files) {
  const source = path.join(sourceRoot, entry.relative);
  const target = path.join(durableRoot, entry.relative);
  if (sha(fs.readFileSync(source)) !== entry.sha256) throw Error('Input drift during copy');
  fs.mkdirSync(path.dirname(target), {recursive: true});
  if (!entry.alreadyPresent) fs.copyFileSync(source, target, fs.constants.COPYFILE_EXCL);
  if (sha(fs.readFileSync(target)) !== entry.sha256) throw Error('Copy mismatch');
}
const record = {
  date: '2026-08-31', sourceRoot, durableRoot, directories, checkedManifests, files,
  status: 'Bounded independently reviewed geometry research; production pending; no live theorem edit or atom retirement',
  qualifications: [
    'Annular torsor result has the precise complete-DVR/perfect-residue/good-reduction scope in its statement.',
    'Tame-branch theorem assumes the independently audited product premise; no proof for residue-characteristic-divisible N.',
    'The original accessibility prose retains its omitted-bridge finding; the separate actual-H supplement has stronger explicit assumptions.',
    'Mixed-branch equality is standalone over arbitrary complete nontrivially valued F and finite L/F; its predecessor application is conditional.',
    'Independent audits disclose predecessor authorship and are not production or priority certificates.',
    'Failed and successful draft-only build evidence is retained; no new PDF or whole-current rigidity conclusion.',
  ],
  credentialHeuristic: 'No credential-like string detected',
  excluded: 'Unrelated worktree files, external primary-source PDFs/text, prior already-preserved dossiers',
  pathPolicy: 'Frozen historical manifests retain original absolute paths; their bytes have not been silently rebased.',
};
const data = JSON.stringify(record, null, 2) + '\n';
const commitPaths = [...paths, path.join(own, 'PRESERVATION.json')].sort();
for (const root of [sourceRoot, durableRoot]) {
  fs.writeFileSync(path.join(root, own, 'PRESERVATION.json'), data, {flag: 'wx'});
  fs.writeFileSync(path.join(root, own, 'COMMIT_PATHS.nul'), commitPaths.join('\0') + '\0', {flag: 'wx'});
}
console.log(JSON.stringify({copied: true, ...summary, commitPaths: commitPaths.length, preservationSha256: sha(data)}, null, 2));
