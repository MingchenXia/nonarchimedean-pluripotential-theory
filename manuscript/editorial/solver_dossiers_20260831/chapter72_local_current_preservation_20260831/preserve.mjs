// Read-only by default. --copy preserves only the explicitly pinned dossiers.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const sourceRoot = '/private/tmp/nappt_p071_20260827';
const durableRoot = '/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix = 'manuscript/editorial/solver_dossiers_20260831';
const own = path.join(prefix, 'chapter72_local_current_preservation_20260831');
const here = path.dirname(fileURLToPath(import.meta.url));
if (![sourceRoot, durableRoot].some(root => path.join(root, own) === here)) {
  throw Error('Unexpected script location');
}
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const manifests = new Map([
  ['p213_source_skeletal_representation_independent_audit_20260831', '739f32df56ec5a39430548ba8c5747eed704911d0c4a871bd95a88a528b07599'],
  ['p213_common_moment_generic_isolation_research_20260831', '3a80d5a0b68668adeb158bb56bb3689f8f5e63fe18dce0bae4065c4b7e1dd5e0'],
  ['p213_common_moment_generic_isolation_independent_audit_20260831', 'dcffc0fd6bb09f668417735ae5bfa9f1d0f60bd166c2b008d99a113fa458d75f'],
  ['p213_general_snc_wall_residual_functional_research_20260831', '2ee5bb8478d7f4cd04b1632af51028c90023cc18323e9db5c8f67deea25d36b8'],
  ['p213_general_snc_wall_residual_functional_independent_audit_20260831', 'a0d8d73aa5c19f6580efa035fd9115f3b8feb9176c6a14ff2915b55b45cae867'],
  ['p213_zero_extension_derivative_degree_diagnostic_20260831', '0d18ac6d059e0a61672e962be5c4b59f372e0ba148bd4d0096d1024d911dff7c'],
  ['p213_zero_extension_derivative_degree_independent_audit_20260831', '1c98af3e5491f8b32558ea149d0da0b239518e0ae05def4026b0e37bb8bdbe53'],
  ['p213_nonreduced_tube_finite_projection_research_20260831', 'd82be02c8b536651f8e9366c407448139c88cf7044158edc419834c515b58fec'],
  ['p213_nonreduced_tube_finite_projection_independent_audit_20260831', '48bbb80f30fc942f0e945925383814f6e02af7a90148ea56025270b4be1468b0'],
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
paths.push('manuscript/editorial/chapter72_local_current_followup_checkpoint_20260831.md', path.join(own, 'preserve.mjs'));
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
  status: 'Bounded local-current comparison research and exact independent reviews; production pending; no live theorem edit or atom retirement',
  qualifications: [
    'The representation audit accepts its displayed description identity, not an unproved local-affine-separation adjective.',
    'Common-moment comparison assumes R and concerns noncontracted cells; rank-drop access remains separate.',
    'The reviewed wall theorem assumes a reduced strictly semistable DVR model and T on the whole chosen residual-curve tube.',
    'The extension diagnostic qualifies derivative degrees; continuous products use proper pushforward, not divisor-borderline removability.',
    'The multiplicity-tube candidate has a separate local scope; individual source coefficients require the unramified DVR hypothesis and R.',
    'No global nonreduced or mixed-horizontal wall theorem, arbitrary-W locality, higher-bidegree result, full P21.3 or priority is inferred.',
    'The accompanying checkpoint states the current review status; no production Rethlas acceptance is claimed.',
  ],
  credentialHeuristic: 'No credential-like string detected',
  excluded: 'Unrelated worktree files, external primary PDFs/text and temporary page renders, earlier already-preserved dossiers, unfinished follow-up research',
  pathPolicy: 'Frozen historical manifests retain original absolute paths and bytes; no silent rebasing.',
};
const data = JSON.stringify(record, null, 2) + '\n';
const commitPaths = [...paths, path.join(own, 'PRESERVATION.json')].sort();
for (const root of [sourceRoot, durableRoot]) {
  fs.writeFileSync(path.join(root, own, 'PRESERVATION.json'), data, {flag: 'wx'});
  fs.writeFileSync(path.join(root, own, 'COMMIT_PATHS.nul'), commitPaths.join('\0') + '\0', {flag: 'wx'});
}
console.log(JSON.stringify({copied: true, ...summary, commitPaths: commitPaths.length, preservationSha256: sha(data)}, null, 2));
