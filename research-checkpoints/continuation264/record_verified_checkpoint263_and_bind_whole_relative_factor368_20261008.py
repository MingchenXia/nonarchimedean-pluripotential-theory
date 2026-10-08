from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
P=G/'push-receipt-continuation263.json';M=G/'upload-manifest-continuation263.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bound(p):
 p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
z=json.loads(P.read_text());m=json.loads(M.read_text())
assert z['commit_sha']=='d29dda3225f257f7a728dcc56e6cf945313d4da7'
assert z['tree_sha']=='8fee7e454871ff5b0bc69b9083e91bfe260ab6c8'
assert z['parent_sha']=='c21d636c36c7a1e09639bbf264dad6f37ee4f06d'
assert z['manifest_sha256']==sha(M)=='8b98510fd900a9592abb1091072f7293d34a18b4e925f6c2fe292dd53ae8773d'
assert z['files']==m['file_count']+1==50
assert z['repository']=='MingchenXia/nonarchimedean-pluripotential-theory' and z['branch']=='codex/xean-research-20261003'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for e in m['files']:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
W=K/'P21.3-continuation368-relative-closed-smooth-form-factor-whole-working-proof-20261008.txt'
B=K/'P21.3-continuation368-ROOT-whole-proof-source-scope-and-binding-20261008.json'
assert W.exists() and not B.exists()
now=datetime.now(timezone.utc).isoformat()
binding=dict(recorded_utc=now,atom='P21.3',whole_working_proof=bound(W),
 status='ENTIRE ROOT working proof; independent reconstruction pending; no correctness grant',
 ROOT_entire_final_working_proof_physically_read=True,
 whole_own_argument='Any smooth (r,r) gamma and initial positive doubly closed BT_F T: gamma wedge T is BT_F IFF product positive and doubly closed. Scalar signed-Radon measure uniqueness proves nonsmooth h/smooth gamma compatibility, inheriting smooth wedge annihilators. Full odd/even graded distribution calculation gives D(gamma wedge hT)=gamma wedge D(hT). Every ordinary open/admissible pair checked. Fixed-common-chart smooth-form coefficient NET convergence to SMOOTH gamma handled on fixed T measures.',
 exact_scope='All complete fields incl trivial; ordinary good separated boundaryless pure spaces; any explicitly prescribed restriction-compatible continuous potential class. Initial BT_F hypothesis remains explicit; product positivity/double closedness independently required. Smooth form may itself fail positivity/closedness. No generated-CPsh/classical-psh identification.',
 whole_immediate_sources_read=['CLD6.2.4--8 cutoff/density/compact partitions with entire immediate proofs','CLD7.2.9--12 complete positivity/measure/multiplier construction','CLD7.7.1--7 entire differential/calculus/Leibniz proof','CLD8.6.1--7 definition/locality/examples/stability/literal flawed multiplier'],
 private_primary_sources=[bound(K/'public-P16.1-round-68-final-reader/sources/CLD-pdf.pdf'),bound(K/'public-P16.1-round-68-final-reader/sources/CLD-literal_extract.txt')],
 recursive_appendix_background_disclosed=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,
 no_arbitrary_current_recognition_or_density=True,no_changing_chart_regularization_theorem=True,no_nonsmooth_form_wedge=True,
 original_closed=False,new_accepted_paper=False,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 future_independent_reconstruction_only=True,ACTIVE_native262_math_not_read_or_fed_back=True,
 primary_bodies_pixels_LOCALONLY=True,protected_editor_open_unchanged=True)
B.write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text())
 assert x['github_pending_checkpoint']['continuation']==263 and len(x['fully_solved_original_atoms'])==16
 assert x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=263,
  commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=z['verified_utc'],
  ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,
  independent_native_git_tree_verified=True,force_update=False),
  ROOT368_unreviewed_relative_closed_smooth_form_factor=dict(whole_proof=bound(W),whole_proof_source_scope_binding=bound(B),original_closed=False,new_accepted_paper=False,held_for_future_independent_reconstruction=True,no_ACTIVE_feedback=True))
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=263,verified_commit=z['commit_sha'],verified_tree=z['tree_sha'],files=z['files'],
 formal_solved=16,formal_OPEN=26,accepted_papers=97,pending_checkpoint=None,new_unreviewed368=bound(W)),indent=2))
