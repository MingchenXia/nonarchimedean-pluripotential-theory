from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation180.json'
F = G / 'continuation180-publication-records'
S = K / 'small-batch170-public-status-20261006-continuation180'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
assert not M.exists() and not F.exists() and not S.exists()
prior = json.loads((G / 'push-receipt-continuation179.json').read_text())
assert prior['commit_sha'] == '8d73fbbcb128b0a575975f23782c1d2356c4ce00'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir(); S.mkdir()
items = []
for n, atom in ((167,'P16.5'), (169,'P19.2'), (170,'P19.2')):
    c = next((R / f'campaigns/round-{n}').iterdir())
    status = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'; p.write_text(json.dumps(status, indent=2) + '\n')
    items.append({'round': n, 'atom': atom, 'directory': str(c), 'observed_status': status['status'], 'observed_utc': status['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'unsettled_calls': status['calls']['unsettled'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': n == 167})
active = [x for x in items if x['unsettled_calls'] > 0]
assert len(active) <= 2
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': '170 whole11-page minimal P19.2 counterexample review. Completed167 P16.5 original PASS,169 P19.2 scope INCONCLUSIVE,168 partialcandidatefalse. Next original target being selected; no hot feedback.'}
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 64
    j.update(updated_utc=now,current_small_batch=batch);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    shutil.copyfile(R / name,F / name)
(F / 'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'originals_solved':9,'originals_open':33,'cumulative_independently_accepted_research_papers':64,'new_original_closure':'P16.5','P19_2_original_closed':False,'active_batch':[x['round'] for x in active],'no_hot_feedback':True,'existing_editor_unchanged':True},indent=2)+'\n')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.patch','.py')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation180/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S,R / 'deliverables/original-P16.5',K / 'public-P19.2-round168-partial-relative-levels-reader',K / 'public-P19.2-continuation212-model-energy-and-raw-profile-reader'):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.patch'):
            add(p)
C=next((R / 'campaigns/round-170').iterdir())
for name in ('argument.md','task.json','settings.json','freeze.json','mathematical-data-bindings.json','original-task.json','launch-record.json'):
    add(C/name)
for n,atom in ((167,'P16.5'),(169,'P19.2')):
    for suffix in ('actual-canonical-independent-review','native-model-final-review','whole-original-review-binding'):
        add(K / f'{atom}-round{n}-{suffix}-20261006.json')
for name in ('P19.2-round168-actual-canonical-author-result-20261006.json','P19.2-round168-native-model-final-author-result-20261006.json','P19.2-round168-completed-partial-original-and-input-binding-20261006.json','P16.5-round167-original-closure-and-publication-record-20261006.json','P19.2-transcendental-model-energy-and-raw-profile-obstruction-candidate-20261006-continuation212.tex'):
    add(K/name)
for name in ('bind_completed_reviews167_169_20261006.py','bind_completed_partial_author168_20261006.py','prepare_original_P16_5_publication_after167_20261006.py','accept_original_P16_5_after_review167_20261006.py','prepare_raw_mass_obstruction212_review170_20261006.py','launch_frozen_raw_mass_original_review170_20261006.py','record_verified179_20261006.py'):
    add(R/name)
add(G/'push-receipt-continuation179.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
front=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':front['fully_solved_original_atoms'],'remaining_open_atoms':33,'historical_reviewed_scoped_papers':64,'commit_message':'Solve original P16.5 and review minimal transcendental raw-profile obstruction','scope':'Whole18-page P16.5 full actual-big and numerical-zero theorem independently PASS167, original closure9/42,64 cumulative accepted papers. Complete canonical/native reports and exact source/evidence/input bindings.169 P19.2 mathematical finer-dS obstruction checked but original scope INCONCLUSIVE;168 completepartial10-page candidatefalse. New whole11-page212 minimal usual-datum/NA-energy/raw-mass obstruction and launched native170 fresh whole-original audit,onlyR. All source/PDF/compile/reading scopes preserved. No P19.2 closure,no private active outputs,no hot feedback,existing P16.4 editor unchanged.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'manifest_sha256':sha(M),'listed_files':len(files),'active_batch':[x['round'] for x in active],'originals_solved':9,'cumulative_accepted_papers':64},indent=2))
