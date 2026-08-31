import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const manifestPath = process.argv[2];
if (!manifestPath) throw new Error("Supply an exact manifest path");
const digest = p => crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const entries = manifest.entries.map(e => {
  const p = path.isAbsolute(e.path) ? e.path : path.resolve(path.dirname(manifestPath), e.path);
  const bytes = fs.statSync(p).size;
  const sha256 = digest(p);
  return {path:p,bytes,sha256,ok:bytes===e.bytes && sha256===e.sha256};
});
const sumsPath = path.join(path.dirname(manifestPath), "SHA256SUMS");
const sums = fs.existsSync(sumsPath) ? fs.readFileSync(sumsPath,"utf8").trim().split(/\r?\n/).map(line => {
  const match = line.match(/^([0-9a-f]{64})\s+\*?(.+)$/);
  if (!match) throw new Error("Malformed checksum line");
  const p=path.isAbsolute(match[2]) ? match[2] : path.resolve(path.dirname(manifestPath),match[2]);
  const sha256=digest(p);
  return {path:p,sha256,ok:sha256===match[1]};
}) : [];
const controls=entries.filter(e=>/\.(?:md|json|mjs|tex|bib)$/.test(e.path)).map(e=>({path:e.path,forbidden_controls:[...fs.readFileSync(e.path)].filter(b=>(b<32&&b!==9&&b!==10)||b===127).length}));
const result={manifest:manifestPath,manifest_sha256:digest(manifestPath),entry_count:entries.length,mismatches:entries.filter(e=>!e.ok),entries,checksum_count:sums.length,checksum_mismatches:sums.filter(e=>!e.ok),checksum_results:sums,controls};
console.log(JSON.stringify(result,null,2));
if(result.mismatches.length||result.checksum_mismatches.length)process.exitCode=1;
