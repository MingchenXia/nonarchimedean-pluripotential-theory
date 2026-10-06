from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
D = G / 'continuation155-publication-records'
S = K / 'current-small-batch145147-20261006-continuation155'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
M = G / 'upload-manifest-continuation155.json'
assert not M.exists()
front = json.loads((D / 'active-work.json').read_text())
assert front['historical_reviewed_scoped_papers'] == 55 and len(front['fully_solved_original_atoms']) == 8
assert front['remaining_open_original_atoms'] == 34
assert [x['round'] for x in front['current_small_batch']['items']] == [145,147]
obs = json.loads((D / 'scope-observation.json').read_text())
previous = G / 'push-receipt-continuation154.json'
receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == '1ac80d9f543434cdddd34b857637344cfd831f0e'
assert receipt['manifest_sha256'] == sha(G / 'upload-manifest-continuation154.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
papers = [R / 'deliverables/scoped-P16.5-exceptional-big-family',
          R / 'deliverables/scoped-P19.2-closed-toric-profile',
          K / 'public-P19.2-continuation190-finite-entropy-endpoint-reader']
reader140 = K / 'public-P19.2-round140-partial-endpoint-reader'
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix == '.pdf': assert p.parent in papers + [reader140]
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation155/'+str(p.relative_to(R)),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in [D,S]:
    for p in sorted(folder.iterdir()): add(p)
for folder in papers:
    b = json.loads((folder / 'publication-binding.json').read_text())
    assert sha(b['tex']) == b['tex_sha256'] and sha(b['pdf']) == b['pdf_sha256']
    assert b['overfull'] == b['warnings'] == b['undefined'] == 0 and not b['original_closed']
    for p in [Path(b['tex']),Path(b['pdf']),folder / 'publication-binding.json']: add(p)
for n in ['P19.2-argument.md','P19.2-paper.tex','P19.2-paper.pdf','source-application-ledger.json','publication-binding.json']:
    add(reader140 / n)
for p in [K / 'P16.5-round143-exceptional-acceptance-and-original-scope-record-20261006.json',
          K / 'P19.2-round146-toric-acceptance-and-original-scope-record-20261006.json',
          K / 'P16.5-round143-actual-scoped-independent-review-20261006.json',
          K / 'P19.2-round146-actual-scoped-independent-review-20261006.json',previous,
          R / 'record_verified154_20261006.py',R / 'accept_and_publish_exceptional143_20261006.py',
          R / 'accept_and_publish_toric146_20261006.py',R / 'publish_completed_partial140_reader_20261006.py',
          R / 'prepare_toric_closed_profile_independent_review146_20261006.py',R / 'launch_frozen_toric_closed_profile_review146_20261006.py',
          R / 'prepare_finite_entropy_endpoint_review147_20261006.py',R / 'launch_frozen_finite_entropy_endpoint_review147_20261006.py',
          R / 'build_finite_entropy_endpoint_candidate190_20261006.py',
          R / 'prepare_checkpoint155_exceptional_and_toric_acceptances_20261006.py',Path(__file__)]: add(p)
for n in [146,147]:
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
        assert sha(C / name) == f[key]
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','task.json','argument.md','settings.json']:
        add(C / name)
    p = C / 'launch-public-native-status.json'
    if p.exists(): add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D / name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({x['path'] for x in files}) == len(files)
manifest = {'generated_utc':datetime.now(timezone.utc).isoformat(),'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':front['fully_solved_original_atoms'],'remaining_open_atoms':34,
    'historical_reviewed_scoped_papers':55,
    'commit_message':'Publish independently accepted exceptional-big equation and closed toric-profile approximation',
    'scope':'Whole exceptional-big-family equation PASS143,9-page final; whole finite-height one-branch toric profile including zero-mass terminal PASS146,6-page final. Accepted supporting papers53 to55,originals8/42 unchanged. New4-page finite-initial-entropy absolute endpoint diagnostic190 in independent147; unchanged original arbitrary-big author145 continues. Completed partial140 full953-line proof and source ledger root-read,15-page preserved paper. No active private outputs, hot feedback, or runtime/account changes.',
    'assembly_recovery':'The first preparation saved a complete immutable front/status snapshot, then encountered an absent optional146 launch-status file. This finisher preserves that snapshot and publishes the actual completed146 public observation; no missing launch observation is fabricated.'}
M.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'frozen_observation_utc':obs['recorded_utc']},indent=2))
