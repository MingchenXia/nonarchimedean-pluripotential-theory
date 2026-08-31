// Read-only identity checks. These do not prove any mathematical assertion.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const auditDirectory = path.dirname(fileURLToPath(import.meta.url));
const pins = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'REVIEWED_INPUTS.json'), 'utf8'));

function verify(base, entry) {
  const target = path.resolve(base, entry.file);
  const bytes = fs.readFileSync(target);
  const actual = crypto.createHash('sha256').update(bytes).digest('hex');
  if (actual !== entry.sha256 || (entry.bytes !== undefined && bytes.length !== entry.bytes)) {
    throw new Error(`Identity mismatch: ${target}`);
  }
}

for (const entry of pins.inputs) verify(auditDirectory, entry);
const manifestPath = path.resolve(auditDirectory, pins.manifest);
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
for (const entry of manifest.entries) verify(path.dirname(manifestPath), entry);

process.stdout.write(JSON.stringify({
  pinnedFiles: pins.inputs.length,
  manifestEntries: manifest.entries.length,
  allExact: true,
  writesPerformed: 0,
  meaning: 'Byte identity only; mathematical review is AUDIT.md; no production verification'
}, null, 2) + '\n');
