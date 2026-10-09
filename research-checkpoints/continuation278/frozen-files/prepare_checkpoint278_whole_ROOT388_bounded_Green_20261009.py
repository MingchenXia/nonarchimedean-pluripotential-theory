from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation278-publication-records'; M=G/'upload-manifest-continuation278.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation277.json')
assert prior['commit_sha']=='a9d7d960ddc0dafaebd5b85e12cc8b9794a2b16b'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=K/'P16.7-continuation388-bounded-Green-and-full-class-radial-dual-working-paper-20261009.tex'
B=K/'P16.7-continuation388-ROOT-whole-proof-source-scope-and-binding-20261009.json'
assert sha(P)=='7e5eb11cc158c75d94b5498f860d5545c251883a3fbdec0593538de50f21029f'
assert sha(B)=='48eb689a58598c623049b94891b9e2d22e17d8eff785598758b83879e1b03ab0'
b=load(B); assert not b['accepted_paper'] and not b['original_closed'] and not b['new_correctness_grant']
for key in ['new_full_read_primary_units','premise_and_source_scope_bindings']:
    for e in b[key]:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==277
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
campaigns={273:R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1',274:R/'campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual'}
states={}
for n,c in campaigns.items():
    states[n]=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert states[n]['error'] is None and states[n]['status'] in ['running','completed']
active=[n for n,s in states.items() if s['calls']['unsettled']]
assert sum(s['calls']['unsettled'] for s in states.values())<=2
F.mkdir()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for p in [P,B,R/'bind_ROOT388_bounded_Green_and_full_radial_dual_20261009.py',R/'record_verified_checkpoint277_20261009.py',G/'push-receipt-continuation277.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:freeze(p)
for n,s in states.items():write(F/('native%d-public-status.json'%n),s)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Entire new ROOT388 proof UNREVIEWED; no original closure or acceptance',counts=b['counts'],paper_sha256=sha(P),binding_sha256=sha(B),new_proof_scope=b['new_proof_scope'],exact_hypotheses=b['exact_hypotheses'],remaining_original=b['remaining_original'],active_rounds=active,maximum_concurrent_campaigns=2,no_active_native_math_read_or_hot_feedback=True,supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,compilation=b['compilation'],protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint278: bounded Green and full-class radial dual\n\nThe entire new ROOT working paper388 supplies a local Hilbert-gradient completion proof of continuous-dpsh Green symmetry, with a uniform psh closure estimate that respects every smallest-sheaf stage. Within the explicit ordinary bounded foundations it derives full Ctheta first variation, concavity, tangent inequality, common-mass Lipschitz continuity, monotonicity and comparison. Under the separately unreviewed actual branch calibration, it proves the FULL bounded-class dual of the specified radial measures is1/6+(2/3)integralh^3, finite exactly under the cubic-tail condition. The upper bound applies to every bounded Ctheta test using the tangent inequality at genuine bounded radial solutions.\n\nThis complete new proof remains UNREVIEWED, and its geometric/calibration dependencies and remaining all-direction original requirements are explicit. It is not fed to either active native campaign.16/42 original problems solved,26 OPEN,97 accepted scoped papers unchanged. All full primary bodies, literal units, pixels and book contexts stay LOCALONLY. No supplied/native program execution or editor change. Compilation request remains unverified. NONFORCE publication independently verifies the Git tree, remote bindings and branch.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p)
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,maximum_concurrent_campaigns=2,items=[dict(round=n,status=s['status'],unsettled_calls=s['calls']['unsettled']) for n,s in states.items()]),github_pending_checkpoint=dict(continuation=278,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),latest_unreviewed_ROOT_bounded_Green_paper=dict(continuation=388,paper=str(P),paper_sha256=sha(P),binding=str(B),binding_sha256=sha(B),accepted=False,original_closed=False),next_work='Verify278 entireROOT388. Native273 and274 remain independent, at mostTWO. Capture only completed/errornull/unsettled0 FINAL and physically read entire proof before any classification. Then independently review388 fullbounded Green/tangent and fullradialdual together with actualnative273 theorem chain. Generalall-directionE1/arbitrarysupport andoriginalP12.3 stillOPEN;16solved26OPEN97accepted unchanged; protected editor unchanged.')
    write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation278/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint full bounded Green proof and full-class radial dual working paper',scope='EntireROOT388 UNREVIEWED, exact ordinarybounded and geometriccalibration assumptions; no original closure, acceptance, fullprimary/book publication, activefeedback or editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,paper_sha256=sha(P),solved=16,open=26,papers=97),indent=2))
