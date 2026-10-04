"""Freeze exact proofs with complete imported dependencies accessible to reviews."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time

source=Path(sys.argv[1]);directory=Path(sys.argv[2]);atom=sys.argv[3]
directory.mkdir(exist_ok=False)
print('Waiting for committed '+atom+' proof; complete dependencies will be embedded.',flush=True)
while True:
    try:c=json.loads((source/'run.json').read_text())['campaign']
    except (OSError,json.JSONDecodeError):time.sleep(5);continue
    if c['status']!='completed':raise RuntimeError('Research did not complete: '+c['status'])
    workspace=Path(c['result']['workspace'])
    claim=json.loads((workspace/'status.json').read_text())
    if isinstance(claim,list):
        assert len(claim)==1;claim=claim[0]
    assert claim['id']==atom
    main=workspace/(atom+'-argument.md')
    if not claim.get('proof_file') or not main.is_file():
        print('No complete new theorem proof; unresolved notes preserved.',flush=True);raise SystemExit(0)
    declared=workspace/claim['proof_file']
    tex=declared if declared.suffix=='.tex' else workspace/(atom+'-partial.tex')
    assert tex.is_file();break
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inp=json.loads((source/'input.json').read_text())
support=[n for n in inp.get('notes',[]) if n.get('imported')]
sections=[main.read_text(), '\n\n# Complete supporting proofs supplied for independent reconstruction\n\nThese are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.\n']
for n in support:
    assert isinstance(n['text'],str)
    sections.append('\n## Full imported dependency '+n['id']+'\n\n'+n['text'])
extra_evidence=Path(sys.argv[4]) if len(sys.argv)>4 else None
if extra_evidence is not None:
    sections.append('\n# Primary source evidence supplied directly\n\n'+extra_evidence.read_text())
(directory/'argument.md').write_text('\n'.join(sections))
task={'problem':'Independently audit all exact theorems and supporting claims of this '+atom+' continuation: '+claim['exact_result']+' The entire main proof and all caller-imported supporting proofs are supplied directly in the argument. The original classification remains open unless explicitly claimed completed; original closure is not an extra criterion for a partial theorem audit.',
    'completionCriteria':'Independently reconstruct every exact theorem and complete dependency chain of this two-graph product continuation. Preserve both finite balanced rational graphs, each local rank-one positive relation cone, cycles, actual saturated lattices, product weights, all affine dimensions, EVERY positive-growth real-PA PC reference and bounded real-PA obstacle on finite rational spatial domains including nonseparable functions. One graph times an affine space or a separable obstacle does not establish a two-graph product theorem. Audit actual raw rational-endpoint PCCs with real coefficients at every real centre and every permitted rational structure, remote endpoint constraints and product junctions. Bilinear interpolation is not automatically jointly convex; independent partial infima or scalar incidence LPs do not automatically encode the whole product. Prove global raw envelope equality, two-sided exact growth, finite rational spatial domains despite real affine coefficients, actual PAPC against all nonnegative real local cycles of every positive dimension on every ordinary open, regularization and operator domain. Retain saturated primitive indices, product weights, d! normalization, refinement/locality/balancing/commutativity and every intermediate lower-face contribution. Full contact includes all product junction fibres, rectangle interiors, edge fibres and all ends. An obstruction needs an actual PAPC/regularizable envelope and the COMPLETE negative integral; failed constructions, isolated atoms or regularity-failure alternatives are insufficient. Independently reconstruct any predecessor used; receipts/hashes/verdicts give no theorem premises. Obtain exact authentic primary statements/full available proof bodies and verify each application. In a quoted text packet verify identifiers and proof boundaries instead of trusting range numbers. Mathematical defects FAIL, indispensable unresolved obligations INCONCLUSIVE, PASS only exact stated partial scope. Original arbitrary balanced-pair classification stays open absent all original criteria. Compilation and finite diagnostics do not validate mathematics. Every passage.premise must be valid zero-based index with exact statement match.'}

task['completionCriteria'] += ' This new target concerns EACH prescribed rational-coefficient reference gamma, not merely existence of a bad reference. Retain all actual REALedgeweights, original finitegraphs/cycles/ends/components and rank-one positive relations. Verify coercivity on every affine/recession cell, unchanged reference outside a compact set, nonnegative compactly supported rational-PA obstacle, finite actual rational walls, all PCCs, exact global raw envelope under sole upper growth, genuine PAPC/reg in the fixed gamma class, and complete actual saturated recursive integral with all other gap terms and refinement vertices. Positive half must cover every bounded real-PA obstacle. If all-real-reference strengthening is claimed, explicitly reconstruct irrational-wall/operator-domain gates; it is not a default consequence of rational reference proof. No optional unclaimed extension is an extra acceptance criterion.'
(directory/'task.json').write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
settings=json.loads(Path('/workspace/research/campaigns/round-03/P05.2-cylinder-theorem-review/settings.json').read_text())
settings['usagePrefix']='catalogue-20261003/evidence/'+atom+'/'+hashlib.sha256(str(directory).encode()).hexdigest()[:12]
assert len(settings['usagePrefix'])<=91
(directory/'settings.json').write_text(json.dumps(settings,indent=2)+'\n')
freeze={'source_workspace':str(workspace),'source_status':claim,
    'argument_sha256':sha(directory/'argument.md'),'main_argument':str(main),
    'main_argument_sha256':sha(main),'source_tex_sha256':sha(tex),
    'declared_proof_file':str(declared),'declared_proof_sha256':sha(declared),
    'source_status_sha256':sha(workspace/'status.json'),
    'extra_primary_evidence':({'path':str(extra_evidence),'sha256':sha(extra_evidence)} if extra_evidence else None),
    'embedded_dependencies':[{ 'id':n['id'],'text_sha256':hashlib.sha256(n['text'].encode()).hexdigest()} for n in support]}
(directory/'freeze.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n')
binding={'original_freeze_sha256':sha(directory/'freeze.json'),
    'review_argument':str(directory/'argument.md'),'review_argument_sha256':freeze['argument_sha256'],
    'main_argument':str(main),'main_argument_sha256':sha(main),
    'source_tex':str(tex),'source_tex_sha256':sha(tex),
    'declared_proof_file':str(declared),'declared_proof_sha256':sha(declared),
    'source_status_sha256':freeze['source_status_sha256']}
(directory/'source-artifact-binding.json').write_text(json.dumps(binding,indent=2)+'\n')
print('Proof and full dependencies frozen; starting '+atom+' independent review.',flush=True)
command=['bash','scripts/cloud.sh','xean','--records','review',str(directory/'task.json'),
    str(directory/'argument.md'),str(directory/'review.sqlite'),str(directory/'settings.json')]
with (directory/'run.json').open('w') as out,(directory/'run.stderr').open('w') as err:
    result=subprocess.run(command,cwd='/workspace/xean',stdout=out,stderr=err)
print(atom+' embedded-dependency review exit '+str(result.returncode),flush=True)
raise SystemExit(result.returncode)
