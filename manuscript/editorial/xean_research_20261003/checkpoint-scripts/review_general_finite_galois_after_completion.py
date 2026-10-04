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
    if claim['status']=='incomplete':
        print('No new completed theorem; preserve concrete gaps without review.',flush=True);raise SystemExit(0)
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
task={'problem':'Independently audit every exact theorem and supporting claim in this P06.2 finite-Galois continuation: '+claim['exact_result']+' Full authoritative proof and caller supporting evidence are supplied directly. Original higher-dimensional classical recognition remains open and is not an extra criterion for this partial gate.',
    'completionCriteria':'Reconstruct all claimed finite-Galois ordinary scalar zero-current ascent for EVERY complete nontrivially valued K, every finite Galois E/K including wild extensions, every good separated strict boundaryless pure n-dimensional X with n>=1, actual nilpotents, and every finite continuous h. Audit all compact complementary ordinary (n-1,n-1) tests. No exact invariant-form descent, current pullback, measure-valued Hessian or scalar-test-only substitute is granted. Verify actual decomposition groups/finite residue tensor factors, separable analytic constant-field Newton lifts with true Banach/nilpotent controls, neighborhood ordinary interiors/purity, same-carrier calibration factor and full tensor coset splitting; reconstruct induction without hidden separable closedness. Norm units and full moment-coordinate matching need actual invariant-algebra descent. Test localization requires genuine common downstairs compact cutoffs and all singleton fibre geometry. Reconstruct differentiated error-measure uniform TV on one fixed calibrated carrier for every normal rank, tensor bidegree, boundary-face intersection and ambient dimension, along with L1 convergence, compact Stokes, smooth C0 density and continuous-multiplier conclusion. Retain actual saturated calibration and Artinian lengths, no field-degree factor for scalar extension. Every essential source theorem needs exact authentic hypotheses/body and verified application. Imported descriptions, prior PASS/receipt/hash are no theorem grants. Use only valid compact cutoff source and upper dimension bounds; no CLD12.2.4 equality or broad CLD15.2.9. Optional finite separable/mixed finite/completed algebraic extensions, if claimed, require their separate complete complementary-form and geometry chains. Do not impose unclaimed optional extensions. Original P06.2 remains open without original full criteria. Mathematical defects FAIL; indispensable unresolved obligations INCONCLUSIVE; PASS only exactly established claimed partial scope. Every passage.premise must be valid zero-based index with exact statement match. Compilation/finite diagnostics are not proof certification.'}
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
