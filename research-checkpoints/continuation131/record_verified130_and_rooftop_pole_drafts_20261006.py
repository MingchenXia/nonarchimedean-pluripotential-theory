from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads((G/'push-receipt-continuation130.json').read_text())
assert r['commit_sha']=='ee15585af9645fd48b0d1d17407eac57951e06a2'
assert r['parent_sha']=='6c6b3bd7bfca1aa6fdce393ce3fd73b62efd174f'
assert sha(G/'upload-manifest-continuation130.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
notes=[K/'P16.5-general-big-rooftop-energy-and-countable-barriers-draft-20261006-continuation151.md',
       K/'P16.5-general-big-Zariski-and-reference-pole-nullness-draft-20261006-continuation152.md']
b={'recorded_utc':now,'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
   'scope':'Own151 actual flag intersections/sums yield rooftop energy subadditivity and countable finite-cost barriers; own152 deficient positive-product moment bounds plus B/c measure tails yield original Zariski and canonical reference pole nullness. No absolute reference integrability, general nonalgebraic polar-nullness, weighted estimates, comparison or all-target inverse.',
   'independently_accepted':False,'original_closed':False,
   'all_recursive_background_foundations_reproved':False,'frozen_native128_includes_these_notes':False,
   'active_or_prepared_frozen_native_inputs_modified':False,'hot_feedback_sent':False,
   'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
p=K/'P16.5-root-continuation151-152-whole-proofs-and-exact-scope-binding-20261006.json'
assert not p.exists();p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
    a['updated_utc']=now
    a['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=r
    a['github_pending_checkpoint']=None
    a['continuation151_152_general_big_rooftop_and_reference_poles_candidate']=b
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':r['commit_sha'],'files':r['files'],'new_unreviewed_local_notes':[151,152],
                  'original_count':7,'open_originals':35},indent=2))
