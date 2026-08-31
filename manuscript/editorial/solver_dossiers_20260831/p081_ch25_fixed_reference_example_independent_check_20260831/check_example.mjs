import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const root='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831';
const dir=path.join(root,'p081_ch25_weighted_capacity_repair_20260831/revised1');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const expected=[
 ['fixed_reference_example.tex','e5b8c7817ca8eb0ffd56f686f9efc36ae47c44edd2c95ebaa84071b005add9fa'],
 ['patched/ch25_capacity.tex','4f66e1358ede7c8d9afff6b8b3c0fbaf53a27247d9741ce02f890fe24a0959a7'],
 ['MANIFEST.json','c1aa7dad837b6a06e0470c1442a7b9966dff398816f9b6cc378f09e0bff32287']
];
for(const [p,h] of expected)if(hash(path.join(dir,p))!==h)throw Error('Source changed: '+p);
const manifest=JSON.parse(fs.readFileSync(path.join(dir,'MANIFEST.json'),'utf8'));
for(const e of manifest.files){const p=path.join(dir,e.name);
 if(fs.statSync(p).size!==e.bytes||hash(p)!==e.sha256)throw Error('Source manifest mismatch');}
if(hash(manifest.source)!==manifest.sourceSha256)throw Error('Earlier frozen author source changed');
const full=fs.readFileSync(path.join(dir,'patched/ch25_capacity.tex'),'utf8');
if(!full.includes(fs.readFileSync(path.join(dir,'fixed_reference_example.tex'),'utf8')))
 throw Error('Example not embedded exactly');
// Integer check after multiplying the displayed rational divisor by N.
for(let n=1;n<=100;n++)for(let j=0;j<=n;j++){
 const self=(j===0||j===n)?-1:-2;
 const value=self*(-j)+(j>0?-(j-1):0)+(j<n?-(j+1):0);
 const target=j===0?-1:j===n?1:0;
 if(value!==target)throw Error('Intersection arithmetic mismatch');
}
process.stdout.write(JSON.stringify({status:'bounded independent example check; not production approval',
 sources:expected.map(([p,sha256])=>({path:path.join(dir,p),sha256})),
 sourceManifestEntries:manifest.files.length,sourceManifestMismatches:0,exampleEmbeddedExactly:true,
 earlierSourceUnchanged:true,integerArithmeticChecks:'N=1,...,100; proof for all N in the report',
 sourceWrites:false,productionCalls:false},null,2));
