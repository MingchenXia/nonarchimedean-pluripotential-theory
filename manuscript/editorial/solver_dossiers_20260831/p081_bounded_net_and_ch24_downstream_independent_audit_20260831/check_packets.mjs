import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';

// Independent, read-only exact-byte and assembly checks. Never apply patches.
const repo='/private/tmp/nappt_p071_20260827';
const dossiers=path.join(repo,'manuscript/editorial/solver_dossiers_20260831');
const read=p=>fs.readFileSync(p,'utf8');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const inputs=[
 ['p081_bounded_model_net_normalization_repair_20260831','dd2a97d28da10305eab36272cad26a210d2a10b13dd50bb504efe8d9b45184b8'],
 ['p081_ch24_real_maximum_locality_repair_20260831','408c1c750c116696e2d43a3466038e84e14ab48e37cb6f5995fec5e501eb6185']
];
const reports=[];
for(const [name,expectedManifest] of inputs){
  const dir=path.join(dossiers,name);
  const manifestBytes=fs.readFileSync(path.join(dir,'MANIFEST.json'));
  assert.equal(sha(manifestBytes),expectedManifest);
  const manifest=JSON.parse(manifestBytes);
  for(const e of manifest.entries){
    const b=fs.readFileSync(path.join(dir,e.path));
    assert.equal(b.length,e.bytes,e.path+' length');
    assert.equal(sha(b),e.sha256,e.path+' hash');
  }
  const sources=JSON.parse(read(path.join(dir,'SOURCE_HASHES.json')));
  for(const e of sources){const b=fs.readFileSync(e.path);assert.equal(sha(b),e.sha256,e.path);assert.equal(b.length,e.bytes);}
  const edits=JSON.parse(read(path.join(dir,'assembly_edits.json')));
  const bounded=name.includes('bounded_model_net');
  const groups=bounded?edits.map(e=>({parent:e.parent,chapter:e.chapter,edits:[e]})):[{
    parent:path.join(dossiers,'p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch24_bfj_ma.tex'),
    chapter:'ch24_bfj_ma.tex',edits
  }];
  const chapters=[];
  let incremental='',combined='';
  for(const g of groups){
    const before=read(g.parent);let assembled=before;
    for(const e of g.edits){
      assert.equal(assembled.split(e.old).length,2,'nonunique replacement');
      if(e.fragment){
        assert.equal(e.replacement,read(path.join(dir,e.fragment))+'\n');
        const end=e.old.match(/\\end\{(proposition|theorem|corollary)\}/);
        assert(end,'missing original statement end');
        const cut=e.old.indexOf(end[0])+end[0].length;
        assert.equal(e.replacement.slice(0,cut),e.old.slice(0,cut),'statement changed');
      }
      assembled=assembled.replace(e.old,e.replacement);
    }
    const full=path.join(dir,'patched',g.chapter),after=read(full);
    assert.equal(assembled,after,'full copy differs from exact assembly');
    assert.deepEqual(labels(after),labels(before),'ordered labels changed');
    assert.equal(new Set(labels(after)).size,labels(after).length,'duplicate label');
    assert(!/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/.test(after),'control byte');
    const relative='manuscript/parts/part3/'+g.chapter;
    const diff=base=>{const r=spawnSync('diff',['-u','--label','a/'+relative,'--label','b/'+relative,base,full],{encoding:'utf8'});assert([0,1].includes(r.status));return r.stdout;};
    incremental+=diff(g.parent);combined+=diff(path.join(repo,relative));
    chapters.push({name:g.chapter,sha256:sha(after),parentSha256:sha(before),labels:labels(after).length,exactAssembly:true,statementsUnchanged:true});
  }
  assert.equal(incremental,read(path.join(dir,'incremental_overlay.patch')));
  assert.equal(combined,read(path.join(dir,'combined_live.patch')));
  const check=spawnSync('git',['apply','--check',path.join(dir,'combined_live.patch')],{cwd:repo,encoding:'utf8'});
  assert.equal(check.status,0,check.stderr);
  if(bounded){
    const graph=read(path.join(dossiers,'p081_weighted_energy_consumers_repair_20260831/ch26_graph_replacement.tex'));
    assert(read(path.join(dir,'patched/ch26_energy.tex')).includes(graph));
    assert(read(path.join(dir,'patched/ch30_functoriality.tex')).includes('monotonicity of a net only after passing to the net of finite minima'));
  }
  reports.push({packet:name,manifestSha256:sha(manifestBytes),manifestEntries:manifest.entries.length,sourceEntries:sources.length,exactReplacementSpans:edits.length,chapters,patchCheck:'PASS; not applied'});
}
console.log(JSON.stringify(reports,null,2));
