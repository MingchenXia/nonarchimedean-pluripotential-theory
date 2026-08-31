import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";
const root=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const failures=[];
const inputs=[
["/private/tmp/CLD25.txt","021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e"],
["/private/tmp/CLD25.pdf","5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719"],
["../p213_component_scalar_classification_research_20260901/RESEARCH_NOTE.md","73f5d4323d81abc8b711aa4dd0d37def0f1ebd789ae19ae9e167c3b2502d4b84"],
["../p213_component_scalar_classification_research_20260901/SOURCE_LEDGER.md","ee8c6bf9cc37ebf3d909ee78d45175398b4fdf75fbcebd70c1989e2f32b4d8c9"],
["../p213_component_scalar_classification_research_20260901/MANIFEST.json","a264c37c448550648df933e0ca27802cf68db52894e63e92e0dee2c895d18136"],
["../p213_component_scalar_classification_research_20260901/SHA256SUMS","ad283bddc96fb66395771a1a165c42120f83086a079c31108dd793c7fe7c9ab8"],
];
function rec(rel,expected) {
 const b=fs.readFileSync(path.resolve(root,rel)),actual=hash(b);
 if(expected&&actual!==expected)failures.push({path:rel,expected,actual});
 return {path:rel,bytes:b.length,sha256:actual};
}
function mf(rel) {
 const full=path.resolve(root,rel),base=path.dirname(full),o=JSON.parse(fs.readFileSync(full));
 const es=o.entries||o.files;
 for(const e of es) {
  const b=fs.readFileSync(path.resolve(base,e.file||e.path)),actual=hash(b);
  if(actual!==e.sha256||b.length!==e.bytes)failures.push({manifest:rel,path:e.file||e.path,actual});
 }
 return {path:rel,count:es.length};
}
function sums(rel) {
 const full=path.resolve(root,rel),base=path.dirname(full),rows=fs.readFileSync(full,"utf8").trim().split(/\r?\n/);
 for(const row of rows) {
  const m=/^([0-9a-f]{64}) [ *](.+)$/.exec(row);
  if(!m)throw Error("Invalid checksum row");
  const actual=hash(fs.readFileSync(path.resolve(base,m[2])));
  if(actual!==m[1])failures.push({checksums:rel,path:m[2],actual});
 }
 return {path:rel,count:rows.length};
}
const inputFiles=inputs.map(x=>rec(...x));
const oldManifest=mf(inputs[4][0]),oldSums=sums(inputs[5][0]);
const ownFiles=["SOURCE_AUDIT.md","check_audit.mjs"].map(x=>rec(x));
const text=fs.readFileSync(path.join(root,"SOURCE_AUDIT.md"),"utf8");
const controls=[...text.matchAll(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g)].length;
if(controls)failures.push({controls});
let ownManifest=null,ownSums=null;
if(fs.existsSync(path.join(root,"MANIFEST.json")))ownManifest=mf("MANIFEST.json");
if(fs.existsSync(path.join(root,"SHA256SUMS")))ownSums=sums("SHA256SUMS");
process.stdout.write(JSON.stringify({status:"Read-only byte integrity; not theorem verification",inputFiles,oldManifest,oldSums,ownFiles,controls,ownManifest,ownSums,failures},null,2)+"\n");
if(failures.length)process.exitCode=1;
