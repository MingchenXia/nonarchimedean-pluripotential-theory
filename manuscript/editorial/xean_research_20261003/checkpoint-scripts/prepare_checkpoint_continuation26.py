"""Freeze both accepted paper packages and their complete review receipts."""
from pathlib import Path
import datetime,hashlib,json,shutil

root=Path('/workspace/research')
checkpoint=root/'github-checkpoint'
active=json.loads((root/'active-work.json').read_text())
parent='61ade56b16fe05716edc475034b7c338ae4faba2'
assert active['github_checkpoint']['commit_sha']==parent
assert active['selected_atoms']==['P06.2','P05.2'] and not active['full_solutions']
checklist=json.loads((root/'checklist-current.json').read_text())
assert checklist['catalogue_atoms']==42 and not checklist['fully_solved_original_atoms']
assert all(not t['fully_solved'] for t in checklist['targets'])
snapshot=checkpoint/'continuation26-uploaded-live-records'
snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/'
files=[]
def add(path,target,mutable=False):
    path=Path(path)
    assert path.is_file(),path
    if mutable:
        copied=snapshot/(str(len(files))+'-'+path.name)
        shutil.copyfile(path,copied)
        path=copied
    assert prefix+target not in {f['path'] for f in files}
    files.append({'local':str(path),'path':prefix+target,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})

for number in (20,21):
    manifest=root/f'deliverables/round-{number}-bundle-manifest.json'
    bundle=json.loads(manifest.read_text())
    assert not bundle['fully_solved_original_atoms']
    for name,expected in bundle['entries'].items():
        path=root/f'deliverables/round-{number}'/name
        assert hashlib.sha256(path.read_bytes()).hexdigest()==expected
        add(path,f'round-{number}/{name}')
    add(manifest,manifest.name)
    add(bundle['bundle'],f'reviewed-papers-round-{number}.zip')
    for suffix in ('source-preparation','native-compile','visual-check'):
        path=root/f'deliverables/round-{number}-{suffix}.json'
        add(path,'records/'+path.name)
for name in ('round-20-preparation-failure.json','round-21-native-compile-attempt-1.json'):
    add(root/'deliverables'/name,'records/'+name)
for relative,label in [('round-20/P05.2-fixed-real-reference-review','fixed-real-reference-graph-products'),
                       ('round-19/P06.2-general-finite-galois-review','general-finite-galois')]:
    directory=root/'campaigns'/relative
    result=json.loads((directory/'run.json').read_text())['campaign']['result']
    att=json.loads((directory/'review-read-attestation.json').read_text())
    assert result['verdict']=='PASS' and att['publish_exact_scope']
    for name in ('run.json','task.json','settings.json','freeze.json','source-artifact-binding.json',
                 'review-read-attestation.json','root-draft-read-record.json','publication-edits.json'):
        add(directory/name,'accepted-reviews/'+label+'/'+name)
for name in ('prepare_round20_real_reference_source_v2.py','prepare_round21_finite_galois_source.py',
             'publish_reviewed_transport_and_graph.py'):
    add(root/name,'checkpoint-scripts/'+name)
add(checkpoint/'push-receipt-continuation25.json','records/push-receipt-continuation25.json')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):
    add(root/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
push=checkpoint/'push_checkpoint_continuation26.py'
assert not push.exists()
text=(checkpoint/'push_checkpoint_continuation25.py').read_text().replace('continuation25','continuation26')
text=text.replace('Checkpoint proof reads and completed algebraic continuation',
                  'Publish reviewed real-reference graph products and finite Galois current transport')
push.write_text(text)
add(push,'checkpoint-scripts/'+push.name)
summary=snapshot/'CHECKPOINT.txt'
summary.write_text('Checkpoint26: Two separate reviewed partial theorem papers published: P05 each prescribed real-reference graph-product characterization,19pages,PASS0/0; P06 finite-Galois ordinary zero-Hessian current transport in every pure dimension against all complementary forms,12pages,PASS27/40. Full authoritative proofs/canonical notes/complete review reports/allpremises/allpassages read and exact artifact/source bindings checked. Native LaTeX SUCCESS and final identical-source exports without warnings. Harmless publication/typesetting/source-display edits recorded; immutable proofs and failed preparer/font history retained. Completed-algebraic all-dimensional complementary-form research is still active with its originally frozen fallible evidence; later PASS verdict not injected. All42original atoms remain open; onlyP05/P06selected and goal active.\n')
add(summary,'CHECKPOINT.txt')
manifest={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003',
    'expected_previous_checkpoint':parent,'files':files,
    'scope':'Two exact reviewed partial papers and complete provenance. All42original problems remain open; native continuation active.'}
path=checkpoint/'upload-manifest-continuation26.json'
assert not path.exists()
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
