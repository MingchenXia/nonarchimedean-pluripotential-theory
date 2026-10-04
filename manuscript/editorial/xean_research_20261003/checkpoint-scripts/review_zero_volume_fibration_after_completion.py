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
 'P15.2':'Audit the exact relative BASE zero-volume Monge–Ampere operator: supplied surjective holomorphic map of smooth compact Kahler manifolds, singular fibres allowed, 1<=nu<n, betaKahler, theta=pi*beta, bounded beta-psh target and arbitrary bounded theta+epsilonomega-psh perturbative potentials converging uniformly without an epsilon-relative rate. Check exact closed degreezero pushforward c_omega, bounded BT pullback/projection and integrationby-parts, all actual fibres/critical values, mixed cohomological bounds of order epsilon^(n-nu), weak limiting operator and raw mass intB beta^nu, representative AND auxiliary Kahler-class independence with the explicit transverse calibration. Audit every claimed movingpath extension, descent, or unbounded extension at exact hypotheses.',
 'P15.1':'Audit the exact UNNORMALIZED relative BASE zero-volume energy: supplied surjective holomorphic map of smooth compact Kahler manifolds, singular fibres allowed, 1<=nu<n, betaKahler, bounded target and arbitrary non-descending bounded perturbative potentials uniformly approaching its pullback without epsilon-relative rate. Check bounded BT foundations, cohomological rawmass/reference scale, closed degreezero fibre pushforward, polynomial coefficients/Vandermonde identity, energy monotonicity/constantshift stability after rescaling, limiting BASE energy, cocycle/variation/concavity at claimed precise regularity, independence of auxiliary Kahler class after explicit c_omega calibration, and any movingpath/descent/unbounded claims.'}
task={'problem':'Independently reconstruct every exact theorem and supporting claim of this '+atom+' continuation: '+claim['exact_result']+' Full new argument and primary bodies are supplied directly. This is a special-scope audit; the original general atom remains open unless genuinely proved in full.',
 'completionCriteria':focus[atom]+' Standard published foundations may be precisely stated, cited and applied with checked hypotheses; every new indispensable application needs its full proof here. The operator proposal is unverified mathematical input, not a theorem grant. Old comparison papers and reviews alone certify no new result. No filesystem tools are available. Compilation, source hashes and finite diagnostics are not mathematical evidence. FAIL for concrete mathematical defects, INCONCLUSIVE for unsettled indispensable steps, PASS only the exact substantive special-scope result. No proof obligation for an explicitly excluded stronger general scope. Every passage.premise is a valid ZERO-based index with statement exactly matching that premise.'}
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
