import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const sha = bytes => crypto.createHash("sha256").update(bytes).digest("hex");
const failures = [];
function read(rel) { return fs.readFileSync(path.resolve(root, rel)); }
function record(rel) {
  const bytes = read(rel);
  return { path: rel, bytes: bytes.length, sha256: sha(bytes) };
}
function checkRecord(entry, base = root) {
  const full = path.resolve(base, entry.path);
  const bytes = fs.readFileSync(full);
  const actual = sha(bytes);
  const ok = actual === entry.sha256 && (entry.bytes === undefined || bytes.length === entry.bytes);
  if (!ok) failures.push({ type: "file", path: full, expected: entry, actual: { bytes: bytes.length, sha256: actual } });
  return { path: full, bytes: bytes.length, sha256: actual, ok };
}
function checkManifest(rel) {
  const full = path.resolve(root, rel), base = path.dirname(full);
  const data = JSON.parse(fs.readFileSync(full, "utf8"));
  const entries = data.files || data.entries;
  if (!Array.isArray(entries)) throw new Error("Unrecognized manifest " + full);
  const results = entries.map(entry => checkRecord(entry, base));
  return { path: full, sha256: sha(fs.readFileSync(full)), count: entries.length, failures: results.filter(x => !x.ok).length };
}
function checkSums(rel) {
  const full = path.resolve(root, rel), base = path.dirname(full);
  const rows = fs.readFileSync(full, "utf8").trim().split(/\r?\n/).filter(Boolean);
  let count = 0, mismatches = 0;
  for (const line of rows) {
    const m = /^([0-9a-f]{64}) [ *](.+)$/.exec(line);
    if (!m) throw new Error("Malformed checksum line: " + line);
    const actual = sha(fs.readFileSync(path.resolve(base, m[2])));
    count++;
    if (actual !== m[1]) { mismatches++; failures.push({ type: "checksum", source: full, path: m[2], expected: m[1], actual }); }
  }
  return { path: full, sha256: sha(fs.readFileSync(full)), count, failures: mismatches };
}
const pins = JSON.parse(read("INPUT_PINS.json"));
const inputResults = pins.files.map(entry => checkRecord(entry));
const packetResults = [];
for (const role of ["L", "O", "Q", "A"]) {
  const m = pins.files.find(x => x.role === role + "_manifest");
  const s = pins.files.find(x => x.role === role + "_sums");
  packetResults.push({ role, manifest: checkManifest(m.path), sums: checkSums(s.path) });
}
const ownNames = ["RESEARCH_NOTE.md", "SOURCE_LEDGER.md", "INPUT_PINS.json", "check_packet.mjs", "VALIDATION.md"];
const presentOwn = ownNames.filter(name => fs.existsSync(path.resolve(root, name)));
const controlChecks = presentOwn.map(name => {
  const text = read(name).toString("utf8");
  const matches = [...text.matchAll(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g)].map(x => x.index);
  if (matches.length) failures.push({ type: "control-character", path: name, offsets: matches });
  return { path: name, unwanted_control_characters: matches.length };
});
const note = read("RESEARCH_NOTE.md").toString("utf8");
const scopeChecks = {
  old_count_descent: note.includes("k(q) = k(p)−1"),
  arbitrary_field_regular_not_smooth: note.includes("regularity need not mean smoothness over k"),
  positive_vertex_denominator: note.includes("lambda_v/h(x)"),
  rooted_order: note.includes("every parent precedes its children"),
  explicit_A_interface: ["(A1)", "(A2)", "(A3)"].every(x => note.includes(x)),
  no_regular_from_BFJ_315: note.includes("normal vertically Q-factorial model, not automatically a regular model"),
  current_n_at_least_two: note.includes("interface calculation in relative dimension n>=2"),
  actual_tube_attribution: note.includes("actual-model/formal-tube identification in O Section 2"),
  full_inverse_image: note.includes("EXACTLY the full inverse image"),
  same_source: note.includes("SAME full compact source form"),
  degree_factor: note.includes("kappa_p = b_p/(N_0 d_p)"),
  omission_factor: note.includes("b_p^(j)=(N_j/N_0)b_p^(0)"),
  anchor_excluded: note.includes("Transport from F to that model chart remains a separate required anchor."),
};
for (const [name, ok] of Object.entries(scopeChecks)) if (!ok) failures.push({ type: "scope-marker", name });
let ownManifest = null, ownSums = null;
if (fs.existsSync(path.resolve(root, "MANIFEST.json"))) ownManifest = checkManifest("MANIFEST.json");
if (fs.existsSync(path.resolve(root, "SHA256SUMS"))) ownSums = checkSums("SHA256SUMS");
const result = {
  schema: 1,
  command_kind: "Read-only exact-byte and literal-scope checks, not mathematical verification",
  root,
  inputs: { count: inputResults.length, failures: inputResults.filter(x => !x.ok).length },
  packets: packetResults,
  own_files: presentOwn.map(record),
  control_checks: controlChecks,
  scope_checks: scopeChecks,
  own_manifest: ownManifest,
  own_sums: ownSums,
  failures,
};
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
if (failures.length) process.exitCode = 1;
