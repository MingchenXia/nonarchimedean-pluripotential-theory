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
task={'problem':'Independently audit all exact theorems and supporting claims of this '+atom+' continuation: '+claim['exact_result']+' The entire main proof and all caller-imported supporting proofs are supplied directly in the argument. The original classification remains open unless explicitly claimed completed; original closure is not an extra criterion for a partial theorem audit.',
    'completionCriteria':'Independently audit the new arbitrary-complete-nontrivially-valued-field PURE analytic CURVE recognition theorem and every supporting application: good/separated/strict/boundaryless actual curves, finite continuous ordinary D[h]=0 with actual generic Artinian lengths, singular/nilpotent/imperfect/positive-characteristic scope. Full caller-imported previously reviewed exact completed-algebraic transport and algebraically-closed intrinsic curve recognition proofs are supplied directly, including source dependencies. Reuse their exact established statements with origin/binding/application checks; a prior verdict alone does not support extrapolation. Verify C=completion of a valued algebraic closure, actual geometric hypotheses/purity/current transport/ordinary opens, then actual GR-harmonic recognition over C and published GR3.14(6) detection over K, with GR4.1.2 ALL analytic extensions and ALL analytic curve-map classical quantifiers. Any R-PL/GJR consequence requires exact GR3.15 hypotheses and applicable proof chain. Never infer arbitrary transcendental current pullback from the already-recognized harmonic function functoriality. First-stage ordinary-smooth psh approximation is a stronger separate theorem and is NOT a criterion for this recognition-only audit; do not add that unused proof obligation. Audit any optional reverse/current-extension claims independently if made. Precise task-permitted published standard foundations can be used with exact hypotheses/citations/applications; every new or extrapolated indispensable lemma needs an accessible actual proof. No filesystem tools are available; complete new proofs, selected essential primary bodies and full supporting gates are supplied in the argument. Mathematical defects FAIL, uncertain indispensable integration steps INCONCLUSIVE, PASS only exact all-K pure-curve partial scope; original arbitrary-dimensional atom remains open. Every passage.premise is valid zero-based with statement exactly matching its premise. Source integrity, compilation, diagnostics and old verdicts alone do not certify the new chain.'}
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
