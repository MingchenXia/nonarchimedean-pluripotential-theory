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
    if claim.get('status') == 'incomplete' or not claim.get('proof_file') or not main.is_file():
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
focus={
 'P15.1':'Audit arbitrary pseudoeffective zero-volume class energy with the precise actual reference type: d<n via class-volume upper bound, degree independence, all same-type mixed products of degree>d zero, raw mass, signed IBP and positive T-admissible Dirichlet current, cocycle/concavity/shift/variation, same-class auxiliary representative independence, all perturbation energy/path limits with their actual convergence hypotheses, especially any class-only convergence without smooth representative bounds. Reconstruct every asserted finite-energy extension, truncation/weighted continuity, reference minimality and carrier statement at the exact scope.',
 'P15.2':'Audit arbitrary pseudoeffective zero-volume prescribed-type operator: actual degree versus class numerical dimension, degree-zero convention, all mixed vanishing, positive raw mass and carrier dimension, full-form auxiliary reference dependence, bounded-type mass polynomials and signed smooth-test IBP, rescaling and every claimed potential/auxiliary path convergence rate. Reconstruct every asserted unbounded/full-mass extension or geometric quotient carrier. No importing the rate-free fibration BASE estimate for arbitrary X tests.'}
task={'problem':'Independently reconstruct every theorem and supporting claim of this '+atom+' continuation: '+claim['exact_result']+' Full new argument and exact primary bodies are supplied directly. Original catalogue closure is separate and requires its full stated scope.',
 'completionCriteria':focus[atom]+' Standard published foundations may be precisely stated/cited/applied with checked hypotheses; full new indispensable applications are required. Source quotations contain identified printed defects: use the correct intrinsic 1/2 gradient definition, consistent ddc normalization, and prove that any correction is harmless for the exact application. Root proposals, old comparisons and reviews are not theorem grants. No filesystem tools. Compilation/hashes/finite diagnostics are not mathematical verification. FAIL for concrete defects, INCONCLUSIVE for unsettled indispensable steps, PASS only the exact substantive theorem. Explicitly excluded stronger scope has no theorem obligation in this scoped review. Every passage.premise is a valid ZERO-based index with statement exactly matching that premise.'}
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
