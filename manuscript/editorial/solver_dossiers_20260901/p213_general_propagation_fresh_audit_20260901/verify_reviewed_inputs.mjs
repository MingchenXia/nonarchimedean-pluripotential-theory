// Read-only reproducibility check. It checks bytes, not mathematical truth.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const auditDir = path.dirname(fileURLToPath(import.meta.url));
const specification = JSON.parse(fs.readFileSync(path.join(auditDir, 'REVIEWED_INPUTS.json'), 'utf8'));
let filesChecked = 0;
let manifestEntriesChecked = 0;

function check(entry, base = auditDir) {
  const filename = path.resolve(base, entry.path);
  const bytes = fs.readFileSync(filename);
  const digest = crypto.createHash('sha256').update(bytes).digest('hex');
  if (digest !== entry.sha256) throw new Error(`SHA-256 mismatch: ${filename}`);
  if (entry.bytes !== undefined && bytes.length !== entry.bytes) {
    throw new Error(`Byte-count mismatch: ${filename}`);
  }
  return filename;
}

for (const entry of specification.files) {
  const filename = check(entry);
  filesChecked += 1;
  if (entry.checkManifestEntries) {
    const manifest = JSON.parse(fs.readFileSync(filename, 'utf8'));
    for (const row of manifest.files) {
      check(row, path.dirname(filename));
      manifestEntriesChecked += 1;
    }
  }
}

console.log(JSON.stringify({
  verdict: 'BYTE_CHECK_PASS_ONLY',
  filesChecked,
  manifestEntriesChecked,
  writeOperations: 0,
  mathematicalVerdict: 'See the separately authored AUDIT.md; hashes do not prove it.'
}, null, 2));
