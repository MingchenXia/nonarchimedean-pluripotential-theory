"""Preserve completed geometric drafts and root checks locally; no upload."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'

active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
active['updated_utc'] = stamp
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. R37 and R38 native authors completed concrete geometric partial papers; both complete proofs, actual canonical notes and TeX read and locally reproduced. R38 independent review export is blocked pending specific approval; R37 independent review is prepared locally and unsent. Earlier GitHub43, P15.2 original-scope audit and R36 abstract review approvals remain pending. No blocked payload resubmitted.'
batch = active['current_public_source_envelope_batch']
for c in batch['campaigns']:
    n = c['round']
    reader = R / 'root-checks' / f'public-envelope-round-{n}-final-reader'
    c['state'] = 'Completed native author; complete proof, actual canonical notes and TeX read; fresh local reproduction passed; no independent acceptance or original closure.'
    c['root_read_record'] = str(reader / 'complete-root-read.json')
    c['root_read_record_sha256'] = sha(reader / 'complete-root-read.json')
    c['reproduction_result'] = str(reader / 'reproduction-result.json')
    c['reproduction_result_sha256'] = sha(reader / 'reproduction-result.json')
    c['review_state'] = 'Prepared locally, not submitted' if n == 37 else 'Automatic review rejected export before launch; specific approval pending'
active['prepared_local_followup_packet_48'] = str(G / 'local-packet-continuation48.json')
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')
checklist_path = R / 'checklist-current.json'
checklist = json.loads(checklist_path.read_text())
assert checklist['fully_solved_original_atoms'] == [] and len(checklist['targets']) == 42
checklist['updated_utc'] = stamp
for target in checklist['targets']:
    if target['id'] == 'P03.1':
        target['current_focus'] = 'R37 completed a concrete full-family positivity theorem for perfected-normalization curve bases with smooth geometrically connected projective factors and analytic projective bundles, arbitrary usc obstacles, with normal and cusp examples. Split, irreducible seminormal codimension-two pinching and nonsplit-node surface failures are proved explicitly. Full proof, actual canonical notes and TeX read; fresh 13-page paper reproduction passed. Independent review prepared locally and unsent. Sharp original classification remains open.'
    if target['id'] in {'P03.1','P03.3'}:
        assert target['closure'] == 'open' and target['fully_solved'] is False
checklist_path.write_text(json.dumps(checklist, ensure_ascii=False, indent=2) + '\n')

out = G / 'local-packet-continuation48.json'
snapshot = G / 'continuation48-local-records'
assert not out.exists() and not snapshot.exists()
snapshot.mkdir()
files = [Path(__file__), R / 'prepare_public_geometric_envelope_review_20261004.py',
         R / 'root-checks/reproduce_public_envelope_round37_20261004.py',
         R / 'root-checks/record_public_envelope_round37_final_read_20261004.py']
scopes = {}
for n, atom, stem in [(37,'P03.1','P03.1-public-source-geometric-positivity'),
                       (38,'P03.3','P03.3-public-source-geometric-continuity')]:
    reader = R / 'root-checks' / f'public-envelope-round-{n}-final-reader'
    files.extend(p for p in reader.iterdir() if p.is_file() and p.suffix in {'.md','.tex','.json','.py','.txt','.log'})
    files.extend(p for p in (reader / 'source-extracts').iterdir() if p.is_file() and p.suffix in {'.txt','.md','.json'})
    reproduction = reader / 'reproduction'
    files.extend(reproduction / name for name in [f'{atom}-paper.pdf','execution.json','artifact-checks.json'])
    if n == 38:
        files = [p for p in files if p not in {reproduction / 'execution.json', reproduction / 'artifact-checks.json'}]
        files.extend(p for p in (reproduction / 'checks').iterdir() if p.is_file() and p.suffix in {'.log','.json'})
    else:
        files.extend(reproduction / f'build-pass-{i}.txt' for i in [1,2])
    author = R / 'campaigns' / f'round-{n}' / stem
    review = author.with_name(stem + '-review')
    files.extend(review / name for name in ['task.json','argument.md','settings.json','freeze.json'])
    if n == 38:
        files.append(review / 'submission-auto-review-rejection.json')
    scopes[str(n)] = json.loads((reader / 'status.json').read_text())
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    src = R / name
    dst = snapshot / name
    shutil.copy2(src,dst)
    assert sha(src) == sha(dst)
    files.append(dst)
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file(), str(p)
    entries.append({'local':str(p),'path':'research-checkpoints/continuation48/'+str(p.relative_to(R)),
                    'sha256':sha(p),'bytes':p.stat().st_size})
data = {
    'prepared_utc':stamp,
    'state':'LOCAL ONLY; no GitHub mutation, model call, blocked review resubmission or author feedback.',
    'files':entries,'file_count':len(entries),'original_atoms':42,'fully_solved_original_atoms':[],
    'selected_atoms':['P03.1','P03.3'],'completed_draft_scope':scopes,
    'drafts_independently_accepted':False,
    'previous_local_packet':str(G/'local-packet-continuation47.json'),
    'last_verified_remote_commit':'604fea852c6a27d4cdc83d97f17393ea67087301',
    'pending_GitHub43_manifest_sha256':sha(pending),
    'blocked_exports_not_resubmitted':True,
    'whole_uploaded_PDF_or_extract_included':False,
    'private_raw_conversations_sql_auth_runtime_included':False,
    'public_primary_PDF_cache_files_included':False,
    'native_editor_limitation':'Native opening/compilation requests for both papers were unresponsive and terminated without diagnostics. Sources preserved; fresh local TeX reproduction succeeded. Editor opening and native compilation remain unconfirmed.'
}
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(out),'sha256':sha(out),'files':len(entries),'external_upload':False,
                  'original_atoms_closed':0},indent=2))
