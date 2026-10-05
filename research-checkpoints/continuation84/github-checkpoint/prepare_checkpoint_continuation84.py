"""Freeze the unreviewed compact-IBP bridge, literal primary units and actual native states."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R/'github-checkpoint'
D = G/'continuation84-publication-records'
S = R/'root-checks/continuation84-compact-IBP-source-reads'
F = R/'root-checks/P16.1-compact-PL-extension-IBP-and-smooth-membership-20261005-continuation84.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')
assert not D.exists() and not S.exists()
assert sha(F) == '9874b4492760442f72ba1444e5c7f3c16e42ae15899f76acf80e4a7304bb9a65'
assert b'\r' not in F.read_bytes() and len(F.read_bytes().decode().split('\n')) == 117
receipt = json.loads((G/'push-receipt-continuation83.json').read_text())
assert receipt['commit_sha'] == 'd5e58c097227925f290eab6c6262f460422551dd'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation83.json') == receipt['manifest_sha256']
now = datetime.now(timezone.utc).isoformat()
S.mkdir()
units = []
groups = [
    ('P16-arxiv-1801.08229-20261004.txt', '1801.08229v4',
     '659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0',
     [(886,931,'Divisorial linear growth and canonical section bound.'),
      (938,1005,'Rational PL lattice and density; real span is not max closed.'),
      (1311,1337,'Flag-ideal global generation and same-class FS differences.'),
      (1780,1849,'Signed raw model pairing and integration by parts.'),
      (2173,2297,'Genuine definition and decreasing/varying-class closure proof.'),
      (2494,2535,'Divisorial order and its proof.'),
      (2550,2599,'Birational error proof; printed LF2594 must retain the preceding ample error class. Correction is unreviewed.'),
      (2859,2873,'Onto pullback retains target-side approaching EP.'),
      (2905,2975,'Continuous envelopes and nets.'),
      (2976,3064,'Smooth characteristic-zero EP proof; no singular EP.'),
      (4529,4602,'Borel strong locality and comparison.'),
      (5751,5785,'Pertinent Dirac finite-energy criterion proof; no full higher upper-bound proof read claim.'),
      (6138,6265,'Smooth equation and continuous Green proof; regularization requires existing genuine membership.'),
      (6300,6359,'Orthogonality proof and its explicit EP antecedent.')]),
    ('Ducros-published-1250007-20261005-continuation72.txt', 'published-1250007',
     'c3275ab4def257991b4cd4cf86d9929c717aeb3b66fab623d8162b9af6326dfa',
     [(2077,2150,'Only compact unit-log image theorem3.2 with strict/rational data.')]),
    ('new-primary-2609.27610v1-20261004.txt', '2609.27610v1',
     'c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d',
     [(630,752,'Contact and finite local PL definitions are audited, not accepted support.'),
      (1200,1587,'Printed local BT, IBP, mass, domination and growth chain is audited; same-constant support, exact finite PL extension, winning-side MA and nets require reconstruction.')])
]
for name, version, digest, ranges in groups:
    source = R/'shared-sources'/name
    assert sha(source) == digest
    lines = source.read_bytes().decode().split('\n')
    for first, last, limit in ranges:
        literal = S/f'{source.stem}-LF{first}-{last}.txt'
        literal.write_text('\n'.join(lines[first-1:last]))
        assert literal.read_bytes().decode() == '\n'.join(lines[first-1:last])
        units.append({'source':str(source),'source_sha256':digest,'version':version,
            'inclusive_one_based_LF':[first,last],'literal_file':str(literal),
            'literal_sha256':sha(literal),'whole_literal_body_root_read':True,
            'application_and_limit':limit})
assert len(units) == 17
write(S/'source-read-record.json', {'recorded_utc':now,'proposal':str(F),
    'proposal_sha256':sha(F),'whole_saved_proposal_root_read':True,
    'proposal_read_ranges':[[1,85],[85,117]],'units':units,
    'whole_primary_files_root_read':False,'new_source_applications_independently_reviewed':False,
    'accepted_dependency':False,'original_closed':False,
    'binding_antecedent':'Actual round75 metric representation and bounded shared-collar positive products and weighted convergence remain unreviewed.',
    'remaining':'Stipulated geometry for all inputs, controlled principal-open removal with exact values, singular Runge, arbitrary-field EP, normalization compatibility and actual singular equation.'})
D.mkdir()
items = []
for atom, no, stem, session in [
    ('P16.1',77,'P16.1-public-source-compact-IBP-and-smooth-weak-global-equation',66863),
    ('P13.2',79,'P13.2-public-source-actual-finite-energy-realization',10689)]:
    campaign = R/'campaigns'/f'round-{no}'/stem
    manifest = json.loads((campaign/'input-manifest.json').read_text())
    for name, key in [('input.json','input_sha256'),('settings.json','settings_sha256')]:
        assert sha(campaign/name) == manifest[key]
    proc = subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(campaign/'campaign.sqlite')],
        cwd='/workspace/xean', capture_output=True, text=True, check=True)
    path = D/f'{atom}-round{no}-native-status.json'
    path.write_text(proc.stdout)
    state = json.loads(proc.stdout)
    items.append({'atom':atom,'round':no,'role':'author','directory':str(campaign),
        'tool_session_id':session,'observed_status':state['status'],'error':state['error'],
        'status':str(path),'status_sha256':sha(path),'input_sha256':manifest['input_sha256'],
        'settings_sha256':manifest['settings_sha256'],'original_closed':False})
assert items[0]['observed_status'] == 'completed'
assert items[1]['observed_status'] == 'blocked'
assert items[1]['error'] == 'Unknown, dead, or forward support: supplied:P13.1/n1'
write(D/'current-small-batch-observation.json', {'recorded_utc':now,'all_items':items,
    'active_items':[],'hot_feedback_sent':False,'route':'Xean native Codex',
    'model':'gpt-6.1-sol','reasoning':'xhigh',
    'round77':'Native result preserved; candidate=false. Whole new paper/notes not yet root-read at this observation.',
    'round79':'Authored files preserved in its own workspace; native result=null after unknown support rejection. Not an accepted or completed native result; no auth/runtime change.',
    'next':'Read both full papers/notes, reproduce provenance and repair accepted-grant note registration in a fresh continuation.'})
write(D/'native-compile-followup.json', {'recorded_utc':now,
    'source':'/workspace/research/deliverables/scoped-P13.2-round73/P13.2-paper.tex',
    'invocation_cell':266,'state':'Unavailable','actual_tool_result':
    'This app tool is no longer available through dynamic tools. Use the codex_app MCP server. If that server is unavailable on this host, task delegation is unavailable.',
    'native_success_asserted':False,'compiler_diagnostics_received':False,
    'unchanged_author_local_two_pass_compile':'SUCCESS','pages':11,
    'current_editor_preserved':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex'})
a = json.loads((R/'active-work.json').read_text())
c = json.loads((R/'checklist-current.json').read_text())
solved = ['P13.1','P15.1','P15.2','P16.6']
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == solved
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 41
batch = json.loads((D/'current-small-batch-observation.json').read_text())
a['updated_utc'] = c['updated_utc'] = now
a['current_small_batch'] = c['current_small_batch'] = batch
c['active_atoms'] = []
a['continuation84_unreviewed_root_proposal'] = {'path':str(F),'sha256':sha(F),
    'source_read_record':str(S/'source-read-record.json'),'accepted_dependency':False}
a['native_publication_compile_addendum_continuation84'] = str(D/'native-compile-followup.json')
a['github_checkpoint'] = c['latest_verified_github_checkpoint'] = receipt
a['github_pending_checkpoint'] = c['github_pending_checkpoint'] = 'Checkpoint84: unreviewed compact IBP and smooth membership bridge; native77 completed partial and79 support-validation rejection; native compiler unavailable.'
write(R/'active-work.json',a)
write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    shutil.copyfile(R/name,D/name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in p.relative_to(R).parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation84/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in [S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file(): add(p)
for p in [F,G/'prepare_checkpoint_continuation84.py',G/'push-receipt-continuation83.json']:
    add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files}) == len(files)
manifest = G/'upload-manifest-continuation84.json'
assert not manifest.exists()
write(manifest, {'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':41,
    'commit_message':'Retain compact integration-by-parts bridge and actual continuation outcomes',
    'scope':'Unreviewed root84 conditional finite algebraic PL extension, raw IBP/mass and smooth first-membership bridge with17 actual-read literal units. Actual native77 partial complete and79 support-validation rejection recorded; builtin publication compiler unavailable. Four originals solved,38 open; no new accepted theorem, private records, SQL, authentication, Git database or book edits.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items]},indent=2))
