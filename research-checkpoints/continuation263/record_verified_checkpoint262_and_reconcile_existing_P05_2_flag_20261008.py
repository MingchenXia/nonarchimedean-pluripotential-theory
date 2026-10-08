from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation262.json';M=G/'upload-manifest-continuation262.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
z=json.loads(P.read_text());m=json.loads(M.read_text())
assert z['commit_sha']=='c21d636c36c7a1e09639bbf264dad6f37ee4f06d' and z['tree_sha']=='cedd1072fa31bf34d6326561edd02f152fb07df1'
assert z['parent_sha']=='7003bb48ca0a9b0794a6c329d03602695fd0cbe3'
assert z['manifest_sha256']==sha(M)=='0b84eb36e773243b220d101e68b844c4443f303bec70a888d05942979a3a2298'
assert z['files']==m['file_count']+1==258
assert z['repository']=='MingchenXia/nonarchimedean-pluripotential-theory' and z['branch']=='codex/xean-research-20261003'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for e in m['files']:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();repairs=[]
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text())
 assert x['github_pending_checkpoint']['continuation']==262 and len(x['fully_solved_original_atoms'])==16
 assert x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=262,
  commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=z['verified_utc'],
  ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,
  independent_native_git_tree_verified=True,force_update=False))
 if 'targets' in x:
  t=next(t for t in x['targets'] if t['id']=='P05.2');r=x['P05_2_original_full_solution']
  assert r['original_closed'] and r['fully_solved_original_atom'] and r['cumulative_accepted_paper_number']==90 and 'P05.2' in x['fully_solved_original_atoms']
  for key in ['source','review_binding','mandatory_annotation']:
   e=r[key];assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
  assert not t['fully_solved']
  t.update(closure='solved',fully_solved=True,research_status='whole_original_orthogonality332_already_accepted_flag_reconciled',remaining_gaps=[],
   current_focus='Existing whole original receipt O332/paper90 reconciled with previously stale target flag; no new acceptance or count increase')
  if not any(q.get('cumulative_accepted_paper_number')==90 for q in t['reviewed_papers']):t['reviewed_papers'].append(r)
  repairs.append(dict(file=str(p),atom='P05.2',existing_acceptance_paper=90,formal_count_changed=False))
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
record=R/'root-checks/existing-P05.2-original332-flag-reconciliation-after-checkpoint262-20261008.json'
assert not record.exists();record.write_text(json.dumps(dict(recorded_utc=now,repairs=repairs,
 scope='Metadata consistency only: formal solved list already included P05.2, existing complete mathematical acceptance O332/paper90 and all source/review bindings retained; no new theorem, acceptance, paper or original count.'),indent=2)+'\n')
print(json.dumps(dict(continuation=262,verified_commit=z['commit_sha'],verified_tree=z['tree_sha'],files=z['files'],
 formal_solved=16,formal_OPEN=26,accepted_papers=97,pending_checkpoint=None,existing_P05_2_flag_reconciled=True),indent=2))
