#!/usr/bin/env python3
"""Preserve the supplied packet, verify documentary evidence, build the draft.
No supplied path is dereferenced. Nothing here certifies mathematics.
"""
import hashlib,json,pathlib,re,subprocess,sys,platform,shutil,datetime
ROOT=pathlib.Path(__file__).resolve().parent

def digest(b):return hashlib.sha256(b).hexdigest()
def write_json(p,v): (ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def unit_record(p,meta):
 b=(ROOT/p).read_bytes()
 return {'saved_literal':p,'actual_sha256':digest(b),'local_inclusive_one_based_LF':[1,len(b.decode().split('\n'))],
         'original_metadata':meta,'coordinate_warning':'Original LF or rendered coordinates are documentary strings; source files outside this workspace were not read.'}

raw=(ROOT/'input.json').read_bytes();p=json.loads(raw)
if (ROOT/'input.sha256').exists():assert (ROOT/'input.sha256').read_text().strip()==digest(raw)
else:(ROOT/'input.sha256').write_text(digest(raw)+'\n')
(ROOT/'assignment-original.txt').write_text(p['assignment'])
write_json('task-original.json',p['task'])
e=ROOT/'evidence';e.mkdir(exist_ok=True)
blocks=re.findall(r'BEGIN ([^\n]+)\n(.*?)\nEND [^\n]+',p['assignment'],re.S)
block_index=[]
for i,(title,body) in enumerate(blocks):
 path=f'evidence/block-{i:02d}.txt';(ROOT/path).write_text(body+'\n')
 block_index.append({'id':i,'title':title,'chars':len(body),'path':path,'sha256':digest((body+'\n').encode())})
write_json('evidence/block-index.json',block_index)
units=json.loads(blocks[5][1]);d=ROOT/'evidence/units';d.mkdir(exist_ok=True)
records=[];mismatches=[]
for i,x in enumerate(units):
 path=f'evidence/units/primary-{i:02d}.txt';(ROOT/path).write_text(x.get('literal',''))
 meta={k:v for k,v in x.items() if k not in ['literal','raw_html','selected_mathematical_body']}
 r=unit_record(path,meta);records.append(r)
 if x.get('sha256') and x['sha256']!=r['actual_sha256']:
  mismatches.append({'path':path,'supplied':x['sha256'],'saved':r['actual_sha256'],'meaning':'Supplied delimitations/binding not asserted equal to these literal bytes.'})
write_json('evidence/units/index.json',records)
g0dict=json.loads(blocks[1][1]);g=ROOT/'evidence/G0-primary';g.mkdir(exist_ok=True);g0records=[]
for i,(h,b) in enumerate(g0dict.items()):
 path=f'evidence/G0-primary/{i:02d}.txt';(ROOT/path).write_text(b)
 r=unit_record(path,{'supplied_binding':h});g0records.append(r)
 if h!=r['actual_sha256']:mismatches.append({'path':path,'supplied':h,'saved':r['actual_sha256'],'meaning':'Binding identifier preserved separately from actual literal-byte hash.'})
write_json('evidence/G0-primary/index.json',g0records)
more=json.loads(blocks[17][1]);m=ROOT/'evidence/additional';m.mkdir(exist_ok=True);more_records=[]
for i,x in enumerate(more):
 path=f'evidence/additional/{i:02d}.txt';(ROOT/path).write_text(x.get('literal',''))
 more_records.append(unit_record(path,{k:v for k,v in x.items() if k!='literal'}))
write_json('evidence/additional/index.json',more_records)
# Save the complete rendered primary units newly actually fetched; distinguish from PDFs.
newpath='evidence/new-Fujino-Miyamoto-2101.00806v1-response.json'
nresp=json.loads((ROOT/newpath).read_text())
ntext='\n'.join(c.get('text','') for c in nresp.get('content',[]) if c.get('type')=='text')
selected=[]
for line in ntext.splitlines():
 match=re.match(r'L(\d+)@',line)
 if match and (47<=int(match[1])<=52 or 179<=int(match[1])<=303):selected.append(line)
fpath='evidence/Fujino-Miyamoto-1.4-statement-and-proof-rendered.txt'
(ROOT/fpath).write_text('\n'.join(selected)+'\n')
assert any(l.startswith('L47@') for l in selected) and any(l.startswith('L303@') for l in selected)
ledger=[
 {'id':'G0','kind':'exact task mathematical grant, actual ample rational domain only','statement':'All-field actual-ample genuine psh, compactness, EP, intersections, E1, intrinsic target, derivatives, comparison, coercivity, attainment and equation exactly as supplied.',
  'evidence':[unit_record('evidence/block-00.txt',{'block_title':blocks[0][0]})],
  'read_scope':'Exact supplied mathematical body and selected primary units; the grant applies to actual ample bundles only.'},
 {'id':'E0','kind':'published algebraic section definitions and arithmetic, with numerical cone conventions','url':'https://arxiv.org/pdf/1801.08229v4','version':'v4, March 2022','statement':'Canonical trivial metric, literal actual FS sections, direct defining single net and section powers/products; finite-dimensional N1, effective cone and open numerical ample cone.',
  'evidence':[records[0],records[29],g0records[0],g0records[51]],'read_scope':'Complete pertinent supplied definition/arithmetic bodies. No closure conclusion of 4.5/4.6 is used.'},
 {'id':'E1','kind':'published external algebraic ampleness theorem','url':'https://arxiv.org/pdf/2101.00806v1','version':'v1, 4 January 2021; source internal date 2020/11/29 version0.09',
  'statement':'Fujino--Miyamoto Theorem1.4: on a complete normal variety over an algebraically closed field, an actual real Cartier divisor is ample iff all its positive-dimensional integral subvariety top intersections are positive; used for numerical ampleness of actual rational representatives on projective smooth X.',
  'evidence':[unit_record(fpath,{'inclusive_zero_based_renderer_lines':[[47,52],[179,303]],'response':newpath,'actual_pdf_downloaded':False})],
  'read_scope':'Complete pertinent printed theorem statement and normal-variety proof inspected; full work and recursively cited Birkar/flattening/classical criteria not all read or reconstructed.'},
 {'id':'E2','kind':'published ample global generation','url':'https://stacks.math.columbia.edu/tag/01Q3','statement':'Stacks Proposition28.27.13: sufficiently large twists of finite-type quasicoherent sheaves by an ample bundle on qcqs schemes are globally generated.',
  'evidence':[records[20]],'read_scope':'Complete supplied mathematical statement and proof; standard cited background not recursively proved.'},
 {'id':'E3','kind':'published literal normal section division','url':'https://arxiv.org/pdf/1801.08229v4','version':'v4, March 2022','statement':'Lemma2.23 section divisibility on normal X with effective rational Cartier divisor; applied to explicit homogeneous FS sections only.',
  'evidence':[records[1]],'read_scope':'Entire supplied statement/proof; normal affine height-one regularity criterion retained as its standard algebraic input.'},
 {'id':'E4','kind':'published actual continuous metric intersections','url':'https://arxiv.org/pdf/1805.01016v3','version':'v3','statement':'BE7.12--7.14 smooth FS regularization on actual semiample bundles; BE8.3--8.6 original fundamental cycle product and uniform continuity over complete fields including trivial valuations.',
  'evidence':[records[14],records[15]],'read_scope':'Entire pertinent supplied proof units; BE7.8 nontrivial-field criterion is not used. Recursively cited CLD/Stokes/tropical background not all reconstructed.'},
 {'id':'E5','kind':'published local metric frame invariance','url':'https://arxiv.org/pdf/1204.6277v2','version':'v2','statement':'CLD18.1.2 harmonic analytic unit-log frame changes and8.8.5 invariance of continuous local metric products; applied on original boundaryless U.',
  'evidence':[records[17],records[19]],'read_scope':'Entire pertinent supplied units; recursively complete local Bedford--Taylor theory not claimed read.'},
 {'id':'D0','kind':'preserved independently reconstructed diagnostic, not positive premise','statement':'General BJ4.6 varying-family extended-valued flattening is false; no desired equation counterexample follows.',
  'evidence':[unit_record('evidence/block-02.txt',{'public_renderer_coordinates':[[3187,3198],[3222,3241],[3264,3270],[3550,3550],[4559,4565]]}),records[30]],'read_scope':'Supplied independent failure body and fresh full mathematical counterexample in paper Section11.'},
 {'id':'D1','kind':'preserved unused proposals/printed claims','statement':'Unaccepted105; continuations109--114; BJ+general EP; printed nonample homogeneous/Siu statements. No mathematical conclusion from these is granted.',
  'evidence':[{'block':i,'path':block_index[i]['path'],'sha256':block_index[i]['sha256']} for i in [3,4,6,8,10,12,14]],
  'read_scope':'Relevant proposals assessed and reconstructed in paper. No whole-primary or prior independent acceptance assumed.'},
 {'id':'E6','kind':'ample-only intersection proof fragment reconstructed from G0','statement':'Capacity bounds are proved in Section6.2 from actual ample integration by parts, locality, equal mass and positive mixed expansion; alpha<1/(n+1) is used.',
  'evidence':[records[38],g0records[62]],'read_scope':'Entire relevant supplied ample proof fragment read. Printed broader/nonample closure and liberal exponent are not assumed.'}
]
write_json('external-premise-ledger.json',ledger)
write_json('evidence-manifest.json',{'input_sha256':digest(raw),'blocks':block_index,'literal_units':records,'G0_dictionary':g0records,'additional_literal_units':more_records,'binding_mismatches':mismatches,'no_supplied_path_dereferenced':True,'hashes_are_not_proofs':True})
status=json.loads((ROOT/'status.json').read_text());assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
notes=json.loads((ROOT/'notes.json').read_text());seen=set()
assert len(notes['notes'])<=4 and notes['candidate'] is False
for note in notes['notes']:
 assert set(note)=={'id','summary','detailedSummary','text','support'}
 assert note['id'] not in seen and all(s in seen for s in note['support'])
 seen.add(note['id'])
# Direct argv, no shell command construction.
(ROOT/'build').mkdir(exist_ok=True)
commands=[['python3','checks.py'],['pandoc','P16.5-paper.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--output=P16.5-paper.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P16.5-paper.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P16.5-paper.tex']]
log=[]
for i,cmd in enumerate(commands):
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
 stdout=f'build/command-{i:02d}.stdout.txt';stderr=f'build/command-{i:02d}.stderr.txt'
 (ROOT/stdout).write_text(r.stdout);(ROOT/stderr).write_text(r.stderr)
 log.append({'argv':cmd,'returncode':r.returncode,'stdout':stdout,'stderr':stderr})
 write_json('run-log.json',log)
 if r.returncode:print(r.stdout[-6000:]);print(r.stderr[-3000:]);sys.exit(r.returncode)
shutil.copyfile(ROOT/'build/P16.5-paper.pdf',ROOT/'P16.5-paper.pdf')
versions={}
for cmd in [['pandoc','--version'],['pdflatex','--version']]:
 r=subprocess.run(cmd,text=True,capture_output=True);versions[cmd[0]]=r.stdout.splitlines()[:2]
write_json('environment.json',{'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(ROOT),'python':sys.version,'platform':platform.platform(),'executable_versions':versions,'no_tools_installed':True,'heavy_computation':False,'supervised_compute_facility':'not exposed; not needed for these small finite diagnostics','scope':'No authentication, config, cache or other-worker data inspected.'})
files={str(q.relative_to(ROOT)):digest(q.read_bytes()) for q in sorted(ROOT.rglob('*')) if q.is_file() and q.name!='artifact-hashes.json' and '__pycache__' not in str(q)}
write_json('artifact-hashes.json',files)
print(json.dumps({'build':'pass','notes':len(notes['notes']),'candidate':False,'supplied_blocks':len(blocks),'primary_literal_units':len(records)+len(g0records)+len(more_records),'binding_mismatches':len(mismatches),'paper_pdf_bytes':(ROOT/'P16.5-paper.pdf').stat().st_size,'limitation':'Documentary checks and compilation are not mathematical certification.'},indent=2))
