// Read-only identity checks, not a mathematical certificate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const auditDirectory = path.dirname(fileURLToPath(import.meta.url));
const pins = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'REVIEWED_INPUTS.json'), 'utf8'));
function check(entry) {
  const target = path.resolve(auditDirectory, entry.file);
  const bytes = fs.readFileSync(target);
  const digest = crypto.createHash('sha256').update(bytes).digest('hex');
  if (digest !== entry.sha256 || (entry.bytes !== undefined && bytes.length !== entry.bytes)) {
    throw new Error(`Identity mismatch: ${target}`);
  }
}
for (const entry of pins.inputs) check(entry);
let ownChecksums = 0;
const checksumPath = path.join(auditDirectory, 'SHA256SUMS');
if (fs.existsSync(checksumPath)) {
  for (const line of fs.readFileSync(checksumPath, 'utf8').trim().split('\n')) {
    const match = line.match(/^([a-f0-9]{64})\s+(.+)$/);
    if (!match) throw new Error('Malformed checksum line');
    check({sha256: match[1], file: match[2]});
    ownChecksums++;
  }
}
process.stdout.write(JSON.stringify({
  localInputPins: pins.inputs.length,
  ownChecksums,
  onlineSourceLocators: pins.onlineSources.length,
  onlineSourcesBytePinned: false,
  allCheckedIdentitiesExact: true,
  writesPerformed: 0,
  meaning: 'Provenance only. Mathematical reasoning and its precise scope are in AUDIT.md.'
}, null, 2) + '\n');
