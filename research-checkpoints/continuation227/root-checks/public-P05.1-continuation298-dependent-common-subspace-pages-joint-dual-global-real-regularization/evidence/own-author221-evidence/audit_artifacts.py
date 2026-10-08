#!/usr/bin/env python3
"""Bounded reproducibility audit. Not a mathematical theorem verifier."""
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
assert Path.cwd().resolve()==ROOT
BASE=Path('/workspace/research/campaigns/round-221/P05.1-arbitrary-dependent-common-subspace-pages-joint-dual-global-real-regularization-paper')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def records(p):return [json.loads(s) for s in p.read_text().splitlines()]
def merge(intervals):
 out=[]
 for a,b in sorted(intervals):
  if out and a<=out[-1][1]:out[-1][1]=max(b,out[-1][1])
  else:out.append([a,b])
 return out
math=json.loads((BASE/'mathematical-packet-bindings.json').read_text())
primary=json.loads((BASE/'private-primary-packet-bindings.json').read_text())
assert len(math)==26 and len(primary)==4
source_records=[]
for z in math+primary:
 p=Path(z['path']); raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==z['sha256'],p.name
 source_records.append({'label':z['label'],'path':str(p),'bytes':len(raw),'sha256':z['sha256']})
reads=records(ROOT/'read-coverage.jsonl'); coverage=[]
for i,z in enumerate(math):
 length=len(Path(z['path']).read_text()); rows=[r for r in reads if r['packet']=='math' and r['index']==i]
 assert rows and all(r['path']==z['path'] and r['sha256']==z['sha256'] and r['characters']==length and 0<=r['start']<r['stop']<=length and r['stop']-r['start']<=42000 for r in rows)
 whole=merge([(r['start'],r['stop']) for r in rows]);assert whole==[[0,length]],(i,whole,length)
 coverage.append({'index':i,'file':Path(z['path']).name,'characters':length,'merged_ranges':whole,'recorded_successful_chunks':len(rows)})
units=records(ROOT/'primary-unit-coverage.jsonl')
expected={1:[(254,301),(418,638),(691,852),(1000,1034),(1350,1503),(1741,1748),(2253,2360)],3:[(196,250),(379,420),(443,598),(604,704),(1515,1555),(1913,1995)]}
primary_coverage=[]
for index,needed in expected.items():
 z=primary[index];rows=[r for r in units if r['index']==index]
 assert all(r['path']==z['path'] and r['sha256']==z['sha256'] and r['LF_end']-r['LF_start']<240 for r in rows)
 actual=merge([(r['LF_start'],r['LF_end']+1) for r in rows])
 for a,b in needed:assert any(c<=a and d>=b+1 for c,d in actual),(index,a,b)
 primary_coverage.append({'index':index,'label':z['label'],'LF_units_required':needed,'merged_half_open_LF':actual})
notes=json.loads((ROOT/'native-notes.json').read_text());assert notes['candidate'] is False
seen=set()
for n in notes['notes']:
 assert n['id'] not in seen and n['id']==f'n{len(seen)+1}'
 assert all(isinstance(n[k],str) and n[k] for k in ['id','summary','detailedSummary','text'])
 assert set(n['support']).issubset(seen); seen.add(n['id'])
assert len(seen)==7
out=json.loads((ROOT/'exact-output.json').read_text()); stdout=json.loads((ROOT/'exact-check.stdout.log').read_text());assert out==stdout
assert (ROOT/'exact-check.stderr.log').read_text()==''
assert out['diagnostic293']['legal_PCC_cost']=='-3/64'
assert len(out['diagnostic293']['dual_epigraph_vertices'])==8
assert out['joint_model']['feasible_tuples_checked']==26961 and out['joint_model']['joint_minimizers_checked']==33
assert out['raw_orders_checked']==44
assert [m['raw_sum_of_orders'] for m in out['saturated_determinant_checks']]==['3','8','48','20/3','624','0']
initial=json.loads((ROOT/'initial-build/build-report.json').read_text())
assert sha(ROOT/'P05.1-paper.tex')==initial['source_sha256']
assert all(s['returncode']==0 for s in initial['steps']) and initial['steps'][-1]['label']=='tex-pass-3' and initial['steps'][-1]['warnings']==[]
assert initial['steps'][1]['warnings'] and initial['steps'][2]['warnings']
for report in sorted(ROOT.glob('build-rerun-*/build-report.json')):
 z=json.loads(report.read_text());assert z['source_unchanged'] and z['source_sha256']==initial['source_sha256']
 assert all(s['returncode']==0 for s in z['steps']) and z['steps'][-1]['warnings']==[]
cmd=['/usr/bin/pandoc','-f','latex','-t','markdown','P05.1-paper.tex']
r=subprocess.run(cmd,cwd=ROOT,capture_output=True,check=False)
assert r.returncode==0 and r.stderr==b'' and r.stdout==(ROOT/'argument.md').read_bytes()
required=['P05.1-paper.tex','P05.1-paper.pdf','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-source-coverage.md','execution-record.md','commands.json','environment.json','build-report.json','native-notes.json','make_notes.py','read_bound.py','read_units.py','check_exact.py','exact-input.json','exact-output.json','exact-check.stdout.log','exact-check.stderr.log','bound-input-verification.json','read-coverage.jsonl','primary-unit-coverage.jsonl','build_paper.py','audit_artifacts.py','README.md']
assert all((ROOT/p).is_file() for p in required)
report={'status':'PASS: binding/coverage/execution audit only','bound_inputs_verified':len(source_records),'whole_math_body_coverage':coverage,'whole_primary_unit_coverage':primary_coverage,'notes':len(seen),'candidate':False,'exact_arithmetic_observations':{'PCC_cost':'-3/64','dual_vertices':8,'dependent_model_tuples':26961,'trace_values':33,'factor_orders':44},'initial_build_preserved':True,'final_initial_build_warnings':[],'source_to_markdown_bytes_equal':True,'limits':'No mathematical correctness, independent acceptance, literal density, continuum verification or native FINAL/model attestation follows.'}
(ROOT/'coverage-audit.json').write_text(json.dumps(report,indent=2)+'\n')
paths={ROOT/p for p in required+['coverage-audit.json','P05.1-paper.aux','P05.1-paper.log','P05.1-paper.out','P05.1-paper.toc','pandoc.stdout.log','pandoc.stderr.log']}
paths.update(ROOT/f'tex-pass-{p}.{suffix}.log' for p in [1,2,3] for suffix in ['stdout','stderr','engine'])
paths.update(ROOT/p for p in ['build-rerun.stdout.log','build-rerun.stderr.log'] if (ROOT/p).exists())
paths.update((ROOT/'LOCALONLY').glob('*.txt'));paths.update((ROOT/'initial-build').glob('*'))
for directory in ROOT.glob('build-rerun-*'):
 assert directory.is_dir();paths.update(directory.glob('*'))
bindings=[]
for p in sorted(paths):
 assert p.is_file() and p.resolve().is_relative_to(ROOT)
 bindings.append({'file':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p),'publication':'LOCALONLY' if p.is_relative_to(ROOT/'LOCALONLY') else 'own artifact / quote-free metadata'})
(ROOT/'artifact-bindings.json').write_text(json.dumps({'format':'author artifact byte bindings; not acceptance','inputs':source_records,'artifacts':bindings,'excluded_self_reference':['artifact-bindings.json','audit*.stdout.log','audit*.stderr.log','input.json (operator workspace input; not an authored output)'],'candidate':False},indent=2)+'\n')
print(json.dumps({'status':report['status'],'bound_inputs':len(source_records),'whole_math_bodies':len(coverage),'complete_original_read_ranges':sum(len(x) for x in expected.values()),'notes':len(seen),'own_artifacts_bound':len(bindings),'candidate':False},indent=2))
