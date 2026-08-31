import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const base = path.dirname(fileURLToPath(import.meta.url));
const resolve = p => path.isAbsolute(p) ? p : path.join(base, p);
const digest = b => crypto.createHash('sha256').update(b).digest('hex');
const manifest = JSON.parse(fs.readFileSync(path.join(base, 'MANIFEST.json'), 'utf8'));
const errors = [];
for (const entry of manifest.files) {
  const bytes = fs.readFileSync(resolve(entry.path));
  if (bytes.length !== entry.bytes || digest(bytes) !== entry.sha256) {
    errors.push(`Manifest mismatch: ${entry.path}`);
  }
}
const lines = fs.readFileSync(path.join(base, 'SHA256SUMS'), 'utf8').trim().split('\n');
for (const line of lines) {
  const match = /^([0-9a-f]{64})  (.+)$/.exec(line);
  if (!match) { errors.push(`Malformed checksum line: ${line}`); continue; }
  if (digest(fs.readFileSync(resolve(match[2]))) !== match[1]) {
    errors.push(`Checksum mismatch: ${match[2]}`);
  }
}
for (const name of manifest.authoredFiles) {
  const bytes = fs.readFileSync(resolve(name));
  const controls = [...bytes].filter(b => (b < 32 && b !== 9 && b !== 10) || b === 127);
  if (controls.length) errors.push(`Disallowed controls: ${name}: ${controls.length}`);
}
console.log(JSON.stringify({
  status: errors.length ? 'mismatch' : 'matched',
  manifestEntries: manifest.files.length,
  checksumEntries: lines.length,
  authoredControlChecks: manifest.authoredFiles.length,
  errors,
  mathematicalVerdict: 'Not asserted by this byte-validation script',
}, null, 2));
if (errors.length) process.exitCode = 1;
