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
    'completionCriteria':'Reconstruct every load-bearing theorem and full dependency chain. Audit genuinely new forward ordinary zero-Hessian ascent under the EXACT completed algebraic-extension hypotheses in the claim, every pure dimension claimed or precise curve-only scope. Density of finite coefficients alone is insufficient: reconstruct rational analytic domain/test descent, actual unit-log equality, compact ordinary supports and overlap gluing. Cover every upstairs compact ordinary test, infinite fibres and every analytic point. Any finite-stage theorem used must be fully reconstructed. Finite separable/pure-inseparable results alone do not give completion ascent. Reverse descent alone is already known. Retain EVERY compact ordinary CLD test, differentiated carrier total variation on fixed compact supports and ALL actual canonical calibration/Artinian lengths, singular/nonreduced structures, purity, ambient hypotheses, ordinary opens and tower/application quantifiers. Invariant scalar Newton polygons and Reynolds moments do not automatically supply alternating ordinary superforms or differentiated convergence. Check any orbit polynomial coefficients including characteristic-p cancellation and zeros, collision strata, fibre orbits/stabilizers and all normalization/field factors. Real averaging is distinct from field division by group order; finite Galois invariance is not a topological cover. Any Newton polynomial/smoothing argument requires actual bounded derivatives and calibrated fold-stratum control, not C0 density or a heuristic finite diagnostic. Any completed infinite-algebraic extension claim requires density, domain descent, unit-log equality, compact/fixed support and full test proof, not a dense coefficient field slogan. Compact cutoffs must use ONLY the explicitly proved compact-F finite-cover construction; do not certify the false broad fixed-index compact-support statement for arbitrary countable-at-infinity closed F. All primary exact statements/proof bodies and applications must be checked; imported note/receipt/hash/local-file reference gives no theorem premise. Reconstruct directly supplied supporting proofs. Ordinary, weakly smooth, current-positive regularization and original classical recognition remain distinct. Mathematical defects FAIL; indispensable unresolved steps INCONCLUSIVE; PASS only the exact partial scope, original closure requires every original criterion. Every passage.premise must be a valid zero-based exact statement match. Typesetting and finite checks are not proof verification.'}
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
