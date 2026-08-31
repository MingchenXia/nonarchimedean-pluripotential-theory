// Explicit, non-overwriting preservation of frozen Chapter 72 research.
// Default is read-only preflight. --copy creates byte-identical durable copies.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const sourceRoot = '/private/tmp/nappt_p071_20260827';
const durableRoot = '/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const prefix = 'manuscript/editorial/solver_dossiers_20260831';
const here = path.dirname(fileURLToPath(import.meta.url));
const ownRelative = path.relative(sourceRoot, here);
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const required = new Map([
  ['p142_raw_transform_usc_research_20260831/MANIFEST.json', 'c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87'],
  ['p142_raw_transform_usc_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md', '29464ed02a022362b2564b2392e8fc457ec9deffe14f6771250ef56792f4f084'],
  ['p147_filtration_maximality_research_20260831/MANIFEST.json', '3ffa1f46f96ce438bf46dd0159cd036f10e79437c1b242a688359b53d652b7fb'],
  ['p147_filtration_maximality_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md', '85b6399d9f62b44cdcc7f507419b445eb589cf3f0bc5ad532277842910b8f75a'],
  ['p147_filtration_maximality_literature_status_20260831/LITERATURE_STATUS_ADDENDUM.md', '161adbd9e3fe31c4df5cc3b29ac357b9054d895865703491adebbd14ce807f62'],
  ['p213_calibrated_chart_rigidity_research_20260831/MANIFEST.json', 'a27d1042cf1426de4c28146994a84dac816fa6ec88992cbfd4bfc9c28cc5ec4b'],
]);
const directories = [...new Set([...required.keys()].map(p => path.dirname(p)))];
for (const [name, expected] of required) {
  if (sha(fs.readFileSync(path.join(sourceRoot, prefix, name))) !== expected) {
    throw Error('Required frozen file changed: ' + name);
  }
}
function walk(relative) {
  return fs.readdirSync(path.join(sourceRoot, relative), {withFileTypes: true})
    .sort((a,b) => a.name.localeCompare(b.name))
    .flatMap(entry => {
      if (entry.isSymbolicLink()) throw Error('Unexpected symlink: ' + entry.name);
      const next = path.join(relative, entry.name);
      return entry.isDirectory() ? walk(next) : entry.name === '.DS_Store' ? [] : [next];
    });
}
const paths = directories.flatMap(d => walk(path.join(prefix, d)));
paths.push('manuscript/editorial/chapter72_research_checkpoint_20260831.md');
paths.push(path.join(ownRelative, 'preserve.mjs'));
if (new Set(paths).size !== paths.length) throw Error('Duplicate target');
const files = paths.map(relative => {
  if (path.isAbsolute(relative) || relative.split(path.sep).includes('..')) throw Error('Unsafe relative path');
  const source = path.join(sourceRoot, relative), target = path.join(durableRoot, relative);
  const bytes = fs.readFileSync(source), hash = sha(bytes);
  const present = fs.existsSync(target);
  if (present && sha(fs.readFileSync(target)) !== hash) throw Error('Refuse differing durable file: ' + relative);
  if (!relative.endsWith('.png') && !relative.endsWith('.pdf') &&
      /(?:sk-[A-Za-z0-9_-]{28,}|ghp_[A-Za-z0-9]{25,}|Bearer\s+[A-Za-z0-9._-]{25,})/.test(bytes.toString('utf8'))) {
    throw Error('Credential-like string: inspect privately before preservation: ' + relative);
  }
  return {relative, bytes: bytes.length, sha256: hash, alreadyPresent: present};
});
const summary = {directories: directories.length, files: files.length,
  newFiles: files.filter(f => !f.alreadyPresent).length,
  bytes: files.reduce((n,f) => n + f.bytes, 0)};
if (!process.argv.includes('--copy')) {
  console.log(JSON.stringify({preflight: true, ...summary}, null, 2));
  process.exit(0);
}
for (const root of [sourceRoot, durableRoot]) {
  for (const name of ['PRESERVATION.json', 'COMMIT_PATHS.nul']) {
    if (fs.existsSync(path.join(root, ownRelative, name))) throw Error('Preservation already frozen');
  }
}
for (const entry of files) {
  const source = path.join(sourceRoot, entry.relative), target = path.join(durableRoot, entry.relative);
  if (sha(fs.readFileSync(source)) !== entry.sha256) throw Error('Source changed during copy');
  fs.mkdirSync(path.dirname(target), {recursive: true});
  if (!entry.alreadyPresent) fs.copyFileSync(source, target, fs.constants.COPYFILE_EXCL);
  if (sha(fs.readFileSync(target)) !== entry.sha256) throw Error('Copy mismatch');
}
const report = {
  date: '2026-08-31', sourceRoot, durableRoot, directories, files,
  status: 'Research and independent reviews only; production pending; no atom retirement',
  excluded: 'Live mathematical changes and unfinished follow-up research/audits',
  credentialHeuristic: 'No credential-like string detected in selected text',
};
const data = JSON.stringify(report, null, 2) + '\n';
const commitPaths = [...paths, path.join(ownRelative, 'PRESERVATION.json')].sort();
for (const root of [sourceRoot, durableRoot]) {
  fs.writeFileSync(path.join(root, ownRelative, 'PRESERVATION.json'), data, {flag: 'wx'});
  fs.writeFileSync(path.join(root, ownRelative, 'COMMIT_PATHS.nul'), commitPaths.join('\0') + '\0', {flag: 'wx'});
}
console.log(JSON.stringify({copied: true, ...summary, preservationSha256: sha(data),
  commitPathCount: commitPaths.length}, null, 2));
