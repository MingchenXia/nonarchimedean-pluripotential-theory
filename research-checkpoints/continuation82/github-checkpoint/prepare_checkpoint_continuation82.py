"""Freeze an inconclusive actual audit, canonical norm draft, and unchanged-scope continuation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research'); G = R/'github-checkpoint'; D = G/'continuation82-publication-records'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
receipt = json.loads((G/'push-receipt-continuation81.json').read_text())
assert receipt['commit_sha'] == '9068a5c6fc6ce37c6fd332e2e7f13f6399942436'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation81.json') == receipt['manifest_sha256']
V = R/'root-checks/public-P13.2-round-74-actual-partial-mathematical-review-reader'
N = V/'canonical-native-review.json'
j = json.loads(N.read_text())
assert sha(N) == 'bfa964b16717216c2fdcf9e877fdb27cab67d64787e26fbc95a3e2d438f317fc'
assert j['verdict'] == 'INCONCLUSIVE' and len(j['premises']) == 200 and len(j['passages']) == 209
read = json.loads((V/'root-read-and-binding-observation-continuation82.json').read_text())
assert read['entire_actual_report_root_read'] and read['all_200_actual_premises_root_read'] and read['all_209_retained_passage_quotes_root_read']
assert not read['new_partial_accepted'] and not read['original_closed']
P = R/'root-checks/P16.1-canonical-nonflat-norm-weights-and-direct-radial-trace-20261005-continuation82.md'
S = R/'root-checks/continuation82-canonical-norm-and-radial-trace-source-reads'
s = json.loads((S/'source-read-record.json').read_text())
assert sha(P) == s['proposal_sha256'] == '099e025e5d9f64a45083bd9c0857179fcc004b1b6646e0755bc3949e413eedf4'
assert s['whole_saved_proposal_root_read'] and not s['accepted_dependency'] and len(s['units']) == 1
for u in s['units']:
    assert sha(u['source']) == u['source_sha256'] and sha(u['literal_file']) == u['literal_sha256']
    first,last = u['inclusive_one_based_LF']
    assert Path(u['literal_file']).read_bytes().decode() == '\n'.join(Path(u['source']).read_bytes().decode().split('\n')[first-1:last])
now = datetime.now(timezone.utc).isoformat(); D.mkdir(); items = []
for atom,no,role,stem,session in [
    ('P16.1',75,'author','P16.1-public-source-actual-metric-collars-and-whole-base-trace-equation',89454),
    ('P13.2',76,'review','P13.2-public-source-same-partial-theorem-and-valid-evidence-mathematical-review',94979)]:
    c = R/'campaigns'/f'round-{no}'/stem
    if role == 'review':
        m = json.loads((c/'freeze.json').read_text())
        assert sha(c/'argument.md') == m['argument_sha256'] and sha(c/'task.json') == m['task_sha256']
        assert sha(c/'settings.json') == m['settings_sha256']
        bindings = {k:m[k] for k in ['argument_sha256','task_sha256','settings_sha256']}
        names = ['task.json','argument.md','settings.json','freeze.json']; database = c/'review.sqlite'
        original = R/'campaigns/round-74/P13.2-public-source-fixed-ray-polynomial-and-uniform-target-mathematical-review'
        assert (c/'task.json').read_bytes() == (original/'task.json').read_bytes()
        assert (original/'argument.md').read_text() in (c/'argument.md').read_text()
        target = D/'round-76-launch'; target.mkdir()
        for name in names: shutil.copyfile(c/name,target/name)
    else:
        m = json.loads((c/'input-manifest.json').read_text())
        assert sha(c/'input.json') == m['input_sha256'] and sha(c/'settings.json') == m['settings_sha256']
        bindings = {k:m[k] for k in ['input_sha256','settings_sha256']}; database = c/'campaign.sqlite'
    proc = subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(database)],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    q = D/f'{atom}-round{no}-native-status.json'; q.write_text(proc.stdout)
    status = json.loads(proc.stdout)['status']
    items.append({'atom':atom,'round':no,'role':role,'directory':str(c),'tool_session_id':session,
        'observed_status':status,'status':str(q),'status_sha256':sha(q),**bindings,
        'saved_new_prefix_settings_and_exact_task_root_read':True,'source_and_context_bindings_reproduced':True,
        'new_mathematics_accepted':False,'original_closed':False,'launched':True})
assert len([i for i in items if i['observed_status']=='running']) <= 2
solved = ['P13.1','P15.1','P15.2','P16.6']
batch = {'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
    'all_items':items,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'hot_feedback_sent':False,'fully_solved_original_atoms':solved,
    'previous_review74_verdict':'INCONCLUSIVE','review76_mathematical_task_unchanged':True}
write(D/'current-small-batch-observation.json',batch)
audit = {'recorded_utc':now,'reader':str(V),'actual_result_sha256':sha(N),'actual_verdict':'INCONCLUSIVE',
    'whole_actual_report_premises_and_retained_passages_root_read':True,
    'premises':200,'retained_passages':209,'new_partial_accepted':False,'original_closed':False,
    'binding_observation_sha256':sha(V/'root-read-and-binding-observation-continuation82.json'),
    'limits':'All retained bindings cover the stated premises, but native validation rejected a reported negative-index grant passage. Short quotes do not by themselves certify source hypotheses. The full mathematical task is independently reaudited unchanged in round76.'}
write(D/'actual-inconclusive-partial-review.json',audit)
proposal = {'recorded_utc':now,'path':str(P),'sha256':sha(P),'whole_saved_root_body_read':True,
    'source_read_record':str(S/'source-read-record.json'),'source_read_record_sha256':sha(S/'source-read-record.json'),
    'accepted_dependency':False,'original_closed':False,'hot_feedback_sent':False,
    'new_mathematics':s['unconditional_draft_scope'],'conditional_antecedents':s['conditional_antecedents'],
    'remaining_requirements':'Smooth actual membership/removal, metric/curve compatibility, singular Runge/genuine membership, envelope and finite-energy equation.'}
write(D/'new-unreviewed-canonical-norm-and-radial-trace.json',proposal)
write(D/'native-compile-followup.json',{'recorded_utc':now,'P13_1_retry_cell':134,
    'P13_1_retry_state':'Finished with unavailable native handler; no compiler diagnostics.',
    'exact_native_result':'No handler registered for tool: codex_app.compile_latex_document',
    'local_P13_1_two_pass_compile':'SUCCESS','native_success_asserted':False,
    'source_and_current_editor_preserved':True,'fresh_compile_invocation_added':False})
a = json.loads((R/'active-work.json').read_text()); c = json.loads((R/'checklist-current.json').read_text())
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == solved
assert sorted(t['atom'] for t in a['full_solutions']) == solved
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 40
a['updated_utc'] = now; a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint82: actual INCONCLUSIVE review74, unreviewed canonical nonflat norm and radial trace draft, exact-scope independent review76; original author75 remains active.'
a['current_small_batch'] = batch; a['P13.2_round74_actual_partial_review'] = audit
a['continuation82_unreviewed_root_proposal'] = proposal
a['native_publication_compile_addendum_continuation82'] = str(D/'native-compile-followup.json')
c['updated_utc'] = now; c['latest_verified_github_checkpoint'] = receipt; c['current_small_batch'] = batch
c['active_atoms'] = sorted({i['atom'] for i in batch['active_items']})
for atom in ['P16.1','P13.2']:
    t = next(t for t in c['targets'] if t['id'] == atom)
    t['continuation82_active_native_item'] = next(i for i in items if i['atom'] == atom)
next(t for t in c['targets'] if t['id']=='P13.2')['continuation82_actual_partial_review'] = audit
write(R/'active-work.json',a); write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
files = []
def add(path,remote=None):
    p = Path(path); assert p.is_file() and not p.is_symlink()
    assert not any(part in {'.git','.codex','.aws','.env','auth.json','campaign.sqlite','review.sqlite','run.json'} for part in p.relative_to(R).parts)
    assert p.suffix not in {'.sqlite','.jsonl'}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation82/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [V,S,D]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for p in [P,R/'prepare_P13_2_same_scope_evidence_review_and_root82_20261005.py',
    G/'prepare_checkpoint_continuation82.py',G/'push-receipt-continuation81.json']: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files}) == len(files)
p = G/'upload-manifest-continuation82.json'; assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40,
    'current_native_batch':items,'commit_message':'Reconstruct canonical nonflat norm weights and preserve inconclusive audit',
    'scope':'Complete actual INCONCLUSIVE partial review74 and root-read all200 premises/209 retained quotes; exact-scope independent review76, unreviewed canonical positive integer norm weights and whole-base Gauss/radial trace route. Original author75 remains active. Native compiler unavailable handler recorded honestly. Four originals closed,38 open; no new acceptance. No book edits, private transcripts, SQL, authentication or Git database.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['role'],i['observed_status']) for i in items],
    'actual_review74_verdict':'INCONCLUSIVE','fully_solved_originals':4},indent=2))
