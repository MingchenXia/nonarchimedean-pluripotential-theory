from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
stamp = datetime.now(timezone.utc).isoformat()
previous = G / 'local-packet-continuation54.json'
older = G / 'local-packet-continuation53.json'
assert sha(previous) == '34e2413b5ad5cc8f50385434f07d683c96fda04e8c3d95d830552af952af2a50'
assert sha(older) == 'd9749d19eee4e1d62591e0a1220eac97c01abbf55065a62aba6c976468bd7369'
for prior in (previous, older):
    for entry in json.loads(prior.read_text())['files']:
        assert sha(entry['local']) == entry['sha256'] and Path(entry['local']).stat().st_size == entry['bytes']
packet = G / 'local-packet-continuation55.json'
saved = G / 'continuation55-local-records'
completion = R / 'public-P16-characteristic-support-batch-completion-20261004.json'
assert not packet.exists() and not saved.exists() and not completion.exists()
saved.mkdir()
files = [Path(__file__), R/'prepare_P16_positive_residue_final_review_20261004.py',
         R/'prepare_P16_arbitrary_support_final_reviews_20261004.py']
records = []
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
assert active['full_solutions'] == []
for original in active['current_public_P16_characteristic_support_batch']['campaigns']:
    record = dict(original)
    directory = Path(record['directory'])
    number, atom = record['round'], record['atom']
    assert sha(directory/'input.json') == record['input_sha256']
    assert sha(directory/'settings.json') == record['settings_sha256']
    command = ['/workspace/xean/.xean/cloud/bun/bin/bun', '--no-install', '--no-env-file',
               '/workspace/xean/packages/cli/src/index.ts', 'status', str(directory/'campaign.sqlite')]
    p = subprocess.run(command, cwd='/workspace/xean', capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    status = json.loads(p.stdout)
    assert status['status'] == 'completed' and status['error'] is None
    status_path = saved / (atom + '-native-status.json')
    status_path.write_text(json.dumps(status, indent=2) + '\n')
    suffix = 'v2' if number == 47 else 'v3'
    reader = R / f'root-checks/public-P16-round-{number}-final-reader-{suffix}'
    repro = R / f'root-checks/public-P16-round-{number}-root-reproduction-{suffix}'
    review = directory.with_name(directory.name + '-review')
    root_read = json.loads((reader/'complete-root-read.json').read_text())
    assert root_read['entire_final_argument_root_read'] and root_read['entire_standalone_tex_root_read']
    notes = json.loads((reader/'actual-canonical-notes.json').read_text())
    actual = json.loads((directory/'run.json').read_text())['campaign']['result']
    assert actual['candidate'] is False and actual['notes'] == notes
    record.update(observed_status='completed', status_file=str(status_path), status_sha256=sha(status_path),
        state='Native author completed; entire proof and actual canonical notes root read; clean reproduction and native compiler successful; independent review locally prepared only.',
        completed_observed_utc=stamp, canonical_note_count=len(notes), candidate=False,
        actual_canonical=str(reader/'actual-canonical-notes.json'), canonical_sha256=sha(reader/'actual-canonical-notes.json'),
        root_read=str(reader/'complete-root-read.json'), root_read_sha256=sha(reader/'complete-root-read.json'),
        author_reader=str(reader), root_reproduction=str(repro),
        root_reproduction_sha256=sha(repro/'root-reproduction-result.json'),
        review_directory=str(review), review_freeze_sha256=sha(review/'freeze.json'),
        review_submitted=False, independently_accepted=False, original_atom_closed=False)
    if number == 48:
        scope = directory.with_name(directory.name+'-original-scope-audit')
        record.update(original_scope_audit_directory=str(scope), scope_freeze_sha256=sha(scope/'freeze.json'),
                      scope_audit_submitted=False, original_support_axis_interpretation_independently_pending=True)
    records.append(record)
    files.extend([status_path, directory/'input.json', directory/'settings.json', directory/'input-manifest.json'])
completion.write_text(json.dumps({'recorded_utc':stamp,'campaigns':records,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'hot_feedback_sent':False,'fully_solved_original_atoms':[],
    'independent_review_provider_submissions_attempted':False,
    'latest_GitHub43_retry_rejected_before_process_creation':True},ensure_ascii=False,indent=2)+'\n')
files.append(completion)

public_manifest = R / 'shared-sources/P16-completion-envelopes-public-cache-20261004.json'
assert sha(public_manifest) == '7f3b3baf4ff4319ac5f6b2ae6bd736a5124d2d6cab4ac4308dabd6c17720d806'
public = json.loads(public_manifest.read_text())
for source in public['sources']:
    for key, digest_key in [('abstract_html','abstract_sha256'),('pdf','pdf_sha256'),('literal_extract','extract_sha256')]:
        assert sha(source[key]) == source[digest_key]
        files.append(Path(source[key]))
source_read = saved / 'additional-public-source-root-read.json'
source_read.write_text(json.dumps({'recorded_utc':stamp,'cache_manifest_sha256':sha(public_manifest),
    'selected_primary_read':[
        {'version':'2012.07972v1','LF_ranges':[[1,235],[1200,1338],[2090,2435]],
         'finding':'Reboulet states general E1 completeness is expected in 6.1.1, with known trivial-valued case. Its metric/geodesic construction alone does not prove the missing arbitrary-field MA realization. Printed sign inconsistencies are not imported as black-box proofs.'},
        {'version':'1712.00980v3','LF_ranges':[[1,270],[1090,1190]],
         'finding':'Gubler, Jell, Kunnemann, Martin; equal-characteristic-p discrete geometric-origin setting, resolution and embedded-resolution assumptions in dimension n+d. Surface/d=1 envelope endpoint uses resolution in dimension 3. Equation 9.3 still retains SNC-support. Neither mixed-characteristic nor all-field arbitrary-support theorem follows directly.'}],
    'whole_papers_read':False,'independent_mathematical_verdict':None,
    'active_author_inputs_modified':False,'hot_feedback_sent':False},ensure_ascii=False,indent=2)+'\n')
files.extend([public_manifest, source_read, R/'shared-sources/cache_P16_completion_envelopes_public_20261004.py'])

retry = G/'push-rejection-continuation43-authorization-retry-20261004.json'
assert sha(retry) == '359109014a00a77837beacc96cc223ba9e71d0be1a19736405fad85e17fcfe14'
files.append(retry)
active['updated_utc'] = stamp
active['current_public_P16_characteristic_support_batch'].update(campaigns=records, completion_record=str(completion), completion_record_sha256=sha(completion))
active['prepared_local_followup_packet_55'] = str(packet)
active['github_pending_checkpoint'].update(latest_authorization_retry_rejection=str(retry),
    latest_authorization_retry_rejection_sha256=sha(retry),
    state='Automatic review again rejected exact checkpoint43 after user authorization reply; no process started. Specific generated-payload/destination confirmation is pending asynchronously. No bypass or new export attempted.')
active['native_editor_state'] = 'User P16.4 round46 editor preserved. Round47 and round48 saved sources compiled successfully with the native compiler without opening another tab. Fresh exported PDFs inspected on first and last pages only.'
active['goal_state'] = 'All 42 originals remain open; 37 independently reviewed scoped papers across 13 IDs. P16.3/P16.6 author batch completed and root read. Correctness packets and separate P16.6 original-scope audit are local only. GitHub and generated-material provider exports require the pending specific approval after automatic rejection.'
active['next_work'] = 'On specific authorization, upload exact frozen checkpoint43 and advance at most two independent audits at a time, prioritizing P16.6 correctness and P15.2 original scope. Preserve immutable files, then audit P16.6 original-support-axis scope. No original closure without complete correctness and scope evidence.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
check_path = R/'checklist-current.json'
check = json.loads(check_path.read_text())
assert len(check['targets'])==42 and all(t['closure']=='open' and t['fully_solved'] is False for t in check['targets'])
assert sum(len(t['reviewed_papers']) for t in check['targets'])==37
assert sum(bool(t['reviewed_papers']) for t in check['targets'])==13
check['updated_utc'] = stamp
check['current_batch_completion_record'] = str(completion)
for t in check['targets']:
    if t['id'] in ['P16.3','P16.6']:
        record = next(c for c in records if c['atom']==t['id'])
        t['research_status'] = 'partial_unreviewed'
        t['current_focus'] = ('Round47 positive-characteristic trivial-field theorem and nontrivial positive-residue gaps completely root read; independent correctness packet local only.' if t['id']=='P16.3' else 'Round48 all-dimension all-support genuine E1 theorem at trivial-char0 and discrete-residue-char0 endpoints completely root read; correctness and literal original-support-axis scope packets local only. No full closure counted.')
        t['current_unreviewed_campaign'] = record
for record in records:
    pending = {'atom':record['atom'],'campaign_directory':record['directory'],
               'status':record['state'],'queued_review_directory':record['review_directory']}
    prior = next((p for p in check['unpublished_drafts'] if p['campaign_directory']==record['directory']), None)
    if prior is None: check['unpublished_drafts'].append(pending)
    else: prior.update(pending)
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as handle:
    writer=csv.writer(handle,delimiter='\t')
    writer.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in check['targets']: writer.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    destination=saved/name
    shutil.copyfile(R/name,destination)
    assert sha(destination)==sha(R/name)
    files.append(destination)

allowed = {'.py','.json','.md','.txt','.tex','.pdf','.png','.html','.log','.aux','.out','.stdout','.stderr'}
trees = [R/'root-checks/public-P16-round-47-final-reader',
         R/'root-checks/public-P16-round-47-final-reader-v2',
         R/'root-checks/public-P16-round-47-root-reproduction-v2',
         R/'root-checks/public-P16-round-48-final-reader-v3',
         R/'root-checks/public-P16-round-48-root-reproduction-v3']
for record in records:
    trees.append(Path(record['review_directory']))
    if record['round']==48: trees.append(Path(record['original_scope_audit_directory']))
for tree in trees:
    for path in sorted(tree.rglob('*')):
        if not path.is_file(): continue
        if '__pycache__' in path.parts: continue
        assert path.suffix in allowed, str(path)
        assert not path.is_symlink()
        files.append(path)
files.extend(R/'root-checks'/name for name in [
    'snapshot_P16_characteristic_support_final_20261004.py',
    'snapshot_P16_characteristic_support_final_v2_20261004.py',
    'snapshot_P16_characteristic_support_final_v3_20261004.py',
    'reproduce_P16_positive_residue_final_20261004.py',
    'reproduce_P16_arbitrary_support_final_20261004.py',
    'P16.6-energy-bounded-variational-bridge-20261004.txt'])
files = sorted(set(files))
entries = [{'local':str(path),'path':'research-checkpoints/continuation55/'+str(path.relative_to(R)),
            'bytes':path.stat().st_size,'sha256':sha(path)} for path in files]
packet.write_text(json.dumps({'prepared_utc':stamp,'state':'LOCAL ONLY; no GitHub upload of this packet attempted.',
    'files':entries,'file_count':len(entries),'active_atoms':['P16.3','P16.6'],
    'fully_solved_original_atoms':[],'reviewed_scoped_papers':37,'original_ids_with_reviewed_scoped_papers':13,
    'previous_local_packet':str(previous),'previous_local_packet_sha256':sha(previous),
    'previous_54_all_15_bindings_verified':True,'previous_53_all_401_bindings_verified':True,
    'last_verified_remote_commit':'604fea852c6a27d4cdc83d97f17393ea67087301',
    'checkpoint43_authorization_retry_rejected_before_process_creation':True,
    'prepared_reviews_not_submitted':True,'private_transcripts_SQL_auth_runtime_original_uploaded_PDF_included':False,
    'source_location_addendum_is_separate_from_immutable_author_files':True},indent=2)+'\n')
print(json.dumps({'packet':str(packet),'file_count':len(entries),'packet_sha256':sha(packet),
                  'fully_solved_original_atoms':0,'reviewed_scoped_papers':37,'GitHub_uploaded':False,
                  'native_author_statuses':[c['observed_status'] for c in records]},indent=2))
