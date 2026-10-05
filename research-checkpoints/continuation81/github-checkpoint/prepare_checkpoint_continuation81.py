"""Freeze complete partial readers, geometric evidence, and the next small batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research'); G = R/'github-checkpoint'; D = G/'continuation81-publication-records'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
receipt = json.loads((G/'push-receipt-continuation80.json').read_text())
assert receipt['commit_sha'] == 'c74cadb4e7fa4d4d0a082c727b0c67738dc555fb'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation80.json') == receipt['manifest_sha256']
readers = []; directories = []
for atom,no,filecount,primarycount,literalcount,proofsha in [
    ('P16.1',72,142,23,51,'1ec6cc36bb3d915d0a3f2fab7f93df363b06cef737ba8931f59c4fd509c773e6'),
    ('P13.2',73,115,42,27,'1945efebae76fcc4b540d36d1058c5fb40a04668b32aea28c8ecd03ba36367ee')]:
    p = R/'root-checks'/f'public-{atom}-round-{no}-final-reader'
    s = json.loads((p/'root-preservation-and-read-state-continuation81.json').read_text())
    assert s['whole_argument_root_read'] and s['entire_actual_four_canonical_notes_root_read']
    assert not s['candidate'] and not s['original_closed']
    assert s['all_source_application_limits_and_excerpt_index_root_read']
    assert len(s['primary_file_bindings']) == primarycount and len(s['literal_excerpt_bindings']) == literalcount
    assert sha(p/(atom+'-argument.md')) == proofsha == s['argument_sha256']
    assert len(s['preserved_author_files']) == filecount
    for f in s['preserved_author_files']:
        assert sha(p/f['file']) == f['sha256'] and (p/f['file']).stat().st_size == f['bytes']
    assert sha(p/'canonical-native-result.json') == s['actual_result_sha256']
    readers.append({'atom':atom,'round':no,'reader':str(p),'argument_sha256':proofsha,
        'root_record_sha256':sha(p/'root-preservation-and-read-state-continuation81.json'),
        'whole_argument_root_read':True,'actual_four_notes_root_read':True,
        'author_files':filecount,'primary_bindings':primarycount,'literal_units':literalcount,
        'candidate':False,'original_closed':False,'new_mathematics_independently_reviewed':False})
    directories.append(p)
P = R/'root-checks/P16.1-geometric-fiber-curve-descent-and-normalization-onto-20261005-continuation81.md'
S = R/'root-checks/continuation81-geometric-descent-source-reads'
s = json.loads((S/'source-read-record.json').read_text())
assert sha(P) == s['proposal_sha256'] == '0c0f323068f29b778eb83ad24a0dd976eb1f2215e368bc80a01264105a85c112'
assert s['whole_saved_proposal_root_read'] and not s['accepted_dependency']
assert len(s['units']) == 2 and len(s['live_primary_web_reads']) == 9
for u in s['units']:
    assert sha(u['source']) == u['source_sha256'] and sha(u['literal_file']) == u['literal_sha256']
    first,last = u['inclusive_one_based_LF']
    assert Path(u['literal_file']).read_bytes().decode() == '\n'.join(Path(u['source']).read_bytes().decode().split('\n')[first-1:last])
now = datetime.now(timezone.utc).isoformat(); D.mkdir(); items = []
for atom,no,role,stem,session in [
    ('P13.2',74,'review','P13.2-public-source-fixed-ray-polynomial-and-uniform-target-mathematical-review',17175),
    ('P16.1',75,'author','P16.1-public-source-actual-metric-collars-and-whole-base-trace-equation',89454)]:
    c = R/'campaigns'/f'round-{no}'/stem
    if role == 'review':
        m = json.loads((c/'freeze.json').read_text())
        assert sha(c/'argument.md') == m['argument_sha256'] and sha(c/'task.json') == m['task_sha256']
        assert sha(c/'settings.json') == m['settings_sha256']
        bindings = {k:m[k] for k in ['argument_sha256','task_sha256','settings_sha256']}
        names = ['task.json','argument.md','settings.json','freeze.json']; database = c/'review.sqlite'
    else:
        m = json.loads((c/'input-manifest.json').read_text())
        assert sha(c/'input.json') == m['input_sha256'] and sha(c/'settings.json') == m['settings_sha256']
        bindings = {k:m[k] for k in ['input_sha256','settings_sha256']}
        names = ['input.json','settings.json','input-manifest.json']; database = c/'campaign.sqlite'
    proc = subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(database)],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    q = D/f'{atom}-round{no}-native-status.json'; q.write_text(proc.stdout)
    status = json.loads(proc.stdout)['status']
    items.append({'atom':atom,'round':no,'role':role,'directory':str(c),'tool_session_id':session,
        'observed_status':status,'status':str(q),'status_sha256':sha(q),**bindings,
        'saved_new_prefix_settings_and_exact_task_root_read':True,'source_and_context_bindings_reproduced':True,
        'new_mathematics_accepted':False,'original_closed':False,'launched':True})
    target = D/f'round-{no}-launch'
    target.mkdir()
    for name in names: shutil.copyfile(c/name,target/name)
assert len([i for i in items if i['observed_status']=='running']) <= 2
solved = ['P13.1','P15.1','P15.2','P16.6']
batch = {'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
    'all_items':items,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'hot_feedback_sent':False,'fully_solved_original_atoms':solved,
    'review74_scope':'Independent mathematical review of round73 partial fixed-ray polynomial and signed target-integration theorem; no original closure requested.',
    'author75_scope':'Exact original P16.1; concentrates on unproved real metric representation, common collars, smooth weak regularization and whole-base traces.'}
write(D/'current-small-batch-observation.json',batch)
write(D/'completed-partial-readers.json',{'recorded_utc':now,'items':readers,
    'limits':'Whole proof and actual canonical notes read. Mathematical claims remain unaccepted; neither is a complete original solution.'})
proposal = {'recorded_utc':now,'path':str(P),'sha256':sha(P),'whole_saved_root_body_read':True,
    'source_read_record':str(S/'source-read-record.json'),'source_read_record_sha256':sha(S/'source-read-record.json'),
    'literal_units':2,'live_primary_web_applications':9,'full_webpage_hash_asserted':False,
    'accepted_dependency':False,'original_closed':False,'conditional_antecedents':s['conditional_antecedents'],
    'new_mathematics':'Geometrically connected resolution fibers, ordinary Bertini curve morphisms after blowup, finite normalization descent and explicit normalization-as-blowup; onto PSH conditional on target-side approaching EP.',
    'remaining_requirements':'Actual metric compatibility, singular countable Runge/genuine membership, finite-data positive operator/orthogonality, unbounded projection identities and variational attainment.'}
write(D/'new-unreviewed-geometric-and-normalization-descent.json',proposal)
write(D/'native-compile-followup.json',{'recorded_utc':now,'P13_1_retry_cell':134,
    'P13_1_retry_state':'Pending; latest bounded wait yielded no diagnostics.',
    'local_P13_1_two_pass_compile':'SUCCESS','native_success_asserted':False,
    'source_and_editor_preserved':True,'fresh_compile_invocation_added':False})
a = json.loads((R/'active-work.json').read_text()); c = json.loads((R/'checklist-current.json').read_text())
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == solved
assert sorted(t['atom'] for t in a['full_solutions']) == solved
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 40
a['updated_utc'] = now; a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint81: fully read partial authors72/73, geometric addendum, independent partial review74 and exact original author75. Four originals closed,38 open.'
a['current_small_batch'] = batch; a['completed_actual_round72_73_partials'] = readers
a['continuation81_unreviewed_root_proposal'] = proposal
a['native_publication_compile_addendum_continuation81'] = str(D/'native-compile-followup.json')
c['updated_utc'] = now; c['latest_verified_github_checkpoint'] = receipt; c['current_small_batch'] = batch
c['active_atoms'] = sorted({i['atom'] for i in batch['active_items']})
for atom in ['P16.1','P13.2']:
    t = next(t for t in c['targets'] if t['id'] == atom)
    t['continuation81_completed_author_read'] = next(i for i in readers if i['atom'] == atom)
    t['continuation81_active_native_item'] = next(i for i in items if i['atom'] == atom)
write(R/'active-work.json',a); write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
files = []
def add(path,remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    assert not any(part in {'.git','.codex','.aws','.env','auth.json','campaign.sqlite','review.sqlite','run.json'} for part in p.relative_to(R).parts)
    assert p.suffix not in {'.sqlite','.jsonl'}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation81/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in directories+[S,D]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for p in [P,R/'prepare_round72_reader_and_continuation81_source_reads_20261005.py',
    R/'prepare_round73_reader_and_partial_mathematical_review_20261005.py',
    R/'prepare_public_P16_1_analytic_gate_reconstruction_20261005.py',
    G/'prepare_checkpoint_continuation81.py',G/'push-receipt-continuation80.json']: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files}) == len(files)
p = G/'upload-manifest-continuation81.json'; assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40,
    'current_native_batch':items,'commit_message':'Preserve complete partial proofs and reconstruct geometric descent',
    'scope':'Whole root-read actual round72/73 proofs and canonical notes, source bindings and author papers, nine paraphrased primary geometric applications and two exact BJ units; independent mathematical partial review74 and exact original author75 launch. All new claims remain unreviewed. Four originals closed,38 open. No book edits, private transcripts, SQL, authentication or Git database.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['role'],i['observed_status']) for i in items],
    'fully_solved_originals':4,'historical_reviewed_scoped_papers':40},indent=2))
